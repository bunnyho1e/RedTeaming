import copy
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('fetch_sources', ROOT / 'fetch_sources.py')
fetcher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fetcher)


class SourceValidationTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))

    def test_active_catalog_and_every_profile_exclude_held_sources(self):
        rows = fetcher.validate_catalog(self.data)
        active = {r['id'].lower() for r in rows}
        excluded = {r.lower() for r in self.data['source_review']['excluded_from_catalog']}
        self.assertTrue(active.isdisjoint(excluded))
        for ids in self.data['profiles'].values():
            self.assertLessEqual({i.lower() for i in ids}, active)
        coverage = json.loads((ROOT / 'redos-coverage.json').read_text())
        covered_ids = {sid for r in coverage['rows'] if r['status'] == 'included' for sid in r['source_ids']}
        self.assertEqual(covered_ids, set(self.data['profiles']['redos']))
        for r in coverage['rows']:
            if r['status'] != 'included':
                self.assertFalse(r['source_ids'])

    def test_every_new_git_host_has_a_valid_canonical_url(self):
        validated = fetcher.validate_catalog(self.data)
        self.assertTrue({'github', 'gitlab', 'salsa', 'isc', 'sourceware', 'debian-source'} <= {r['host'] for r in validated})

    def test_duplicate_identity_is_case_insensitive(self):
        duplicate = copy.deepcopy(self.data['repositories'][0])
        duplicate['id'] = duplicate['id'].upper()
        self.data['repositories'].append(duplicate)
        with self.assertRaises(ValueError):
            fetcher.validate_catalog(self.data)

    def test_excluded_identity_cannot_be_reintroduced_with_changed_case(self):
        row = self.data['repositories'][0]
        self.data['source_review']['excluded_from_catalog'].append(row['id'].upper())
        with self.assertRaises(ValueError):
            fetcher.validate_catalog(self.data)

    def test_pin_path_and_url_tampering_are_rejected(self):
        variants = [('commit', '--upload-pack=bad'), ('clone_url', 'file:///tmp/source'),
                    ('path', '../outside'), ('slug', 'owner/../outside'), ('category', '../outside')]
        for key, value in variants:
            data = copy.deepcopy(self.data)
            data['repositories'][0][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                fetcher.validate_catalog(data)

    def test_unknown_profile_source_is_rejected_even_for_all_downloads(self):
        self.data['profiles']['redos'].append('github:unreviewed/source')
        with self.assertRaises(ValueError):
            fetcher.validate_catalog(self.data)

    def test_package_rejects_traversal_redirect_url_and_invalid_digest(self):
        original = next(r for r in self.data['repositories'] if r.get('kind') == 'source-package')
        for key, value in [('filename', '../escape.tar.gz'), ('filename', 'socat_1:ads.tar.gz'),
                           ('url', 'https://example.com/source.tar.gz'), ('sha256', '0'*40),
                           ('size', 129*1024*1024)]:
            data = copy.deepcopy(self.data)
            package = next(r for r in data['repositories'] if r['id'] == original['id'])
            package['files'][0][key] = value
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                fetcher.validate_catalog(data)


class SourceFetchSafetyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.root_patch = patch.object(fetcher, 'ROOT', self.root)
        self.root_patch.start()
        self.payload = b'opaque source archive contents: never interpreted or extracted'
        filename = 'socat_1.orig.tar.gz'
        self.row = {'id':'debian-source:socat','host':'debian-source','slug':'socat',
                    'kind':'source-package','path':'tools/network/debian-source/socat','version':'1',
                    'files':[{'filename':filename,'url':'https://deb.debian.org/debian/pool/main/s/socat/'+filename,
                              'size':len(self.payload),'sha256':hashlib.sha256(self.payload).hexdigest()}]}

    def tearDown(self):
        self.root_patch.stop()
        self.temp.cleanup()

    def response(self, body=None, url=None):
        stream = io.BytesIO(self.payload if body is None else body)
        stream.geturl = lambda: url or self.row['files'][0]['url']
        return stream

    def test_package_is_verified_and_kept_opaque_without_git_or_execution(self):
        with patch.object(fetcher.urllib.request, 'urlopen', return_value=self.response()) as download, \
             patch.object(fetcher, 'git') as git:
            self.assertEqual(fetcher.fetch(self.row), self.row['id'])
            git.assert_not_called()
            destination = self.root / self.row['path'] / self.row['files'][0]['filename']
            self.assertEqual(destination.read_bytes(), self.payload)
            self.assertEqual(list(destination.parent.iterdir()), [destination])
            self.assertEqual(fetcher.fetch(self.row), self.row['id'])
            self.assertEqual(download.call_count, 1)

    def test_bad_package_digest_is_not_committed_to_destination(self):
        body = b'x' * len(self.payload)
        with patch.object(fetcher.urllib.request, 'urlopen', return_value=self.response(body)):
            with self.assertRaisesRegex(ValueError, 'checksum'):
                fetcher.fetch(self.row)
        self.assertEqual(list((self.root / self.row['path']).iterdir()), [])

    def test_oversized_package_download_is_aborted_and_temp_removed(self):
        with patch.object(fetcher.urllib.request, 'urlopen', return_value=self.response(self.payload + b'x')):
            with self.assertRaisesRegex(ValueError, 'exceeds'):
                fetcher.fetch(self.row)
        self.assertEqual(list((self.root / self.row['path']).iterdir()), [])

    def test_plain_http_redirect_is_rejected(self):
        with patch.object(fetcher.urllib.request, 'urlopen', return_value=self.response(url='http://example.com/file')):
            with self.assertRaisesRegex(ValueError, 'HTTPS'):
                fetcher.fetch(self.row)

    def test_destination_directory_symlink_is_rejected_before_download(self):
        outside = self.root / 'outside'
        outside.mkdir()
        (self.root / 'tools').symlink_to(outside, target_is_directory=True)
        with patch.object(fetcher.urllib.request, 'urlopen') as download:
            with self.assertRaisesRegex(ValueError, 'Symlink'):
                fetcher.fetch(self.row)
            download.assert_not_called()
        self.assertEqual(list(outside.iterdir()), [])

    def test_archive_file_symlink_is_rejected_before_download(self):
        target = self.root / self.row['path']
        target.mkdir(parents=True)
        outside = self.root / 'outside'
        outside.write_bytes(b'unchanged')
        (target / self.row['files'][0]['filename']).symlink_to(outside)
        with patch.object(fetcher.urllib.request, 'urlopen') as download:
            with self.assertRaisesRegex(ValueError, 'symlink'):
                fetcher.fetch(self.row)
            download.assert_not_called()
        self.assertEqual(outside.read_bytes(), b'unchanged')

    def test_existing_mismatched_archive_is_preserved(self):
        target = self.root / self.row['path']
        target.mkdir(parents=True)
        destination = target / self.row['files'][0]['filename']
        destination.write_bytes(b'local data')
        with patch.object(fetcher.urllib.request, 'urlopen') as download:
            with self.assertRaisesRegex(ValueError, 'Existing'):
                fetcher.fetch(self.row)
            download.assert_not_called()
        self.assertEqual(destination.read_bytes(), b'local data')

    def test_dangerous_existing_git_configuration_is_rejected(self):
        target = self.root / 'repo'
        target.mkdir()
        fetcher.git('init', cwd=target, capture=True)
        fetcher.git('config', '--local', 'filter.payload.smudge', 'unreviewed-command', cwd=target)
        with self.assertRaisesRegex(ValueError, 'filter.payload.smudge'):
            fetcher.check_local_git_config(target)

    def test_inherited_git_environment_cannot_redirect_checkout(self):
        with patch.dict(os.environ, {'GIT_DIR':'/outside','GIT_WORK_TREE':'/outside',
                                     'GIT_CONFIG_COUNT':'1','GIT_CONFIG_KEY_0':'core.worktree',
                                     'GIT_CONFIG_VALUE_0':'/outside'}):
            with patch.object(fetcher.subprocess, 'run') as run:
                fetcher.git('status', cwd=self.root)
                env = run.call_args.kwargs['env']
        self.assertNotIn('GIT_DIR', env)
        self.assertNotIn('GIT_WORK_TREE', env)
        self.assertNotIn('GIT_CONFIG_COUNT', env)
        self.assertEqual(env['GIT_CONFIG_GLOBAL'], os.devnull)


if __name__ == '__main__':
    unittest.main()
