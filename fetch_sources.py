#!/usr/bin/env python3
"""Fetch active pinned sources without running installers, tools or submodules."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import urllib.request

ROOT = Path(__file__).resolve().parent
HOST_BASES = {
    'github': 'https://github.com/',
    'gitlab': 'https://gitlab.com/',
    'salsa': 'https://salsa.debian.org/',
    'isc': 'https://gitlab.isc.org/',
    'sourceware': 'https://sourceware.org/git/',
}
MAX_ARCHIVE_BYTES = 128 * 1024 * 1024
GIT_OPTIONS = [
    '-c', 'core.hooksPath=/dev/null', '-c', 'core.fsmonitor=false',
    '-c', 'protocol.allow=never', '-c', 'protocol.https.allow=always',
    '-c', 'http.sslVerify=true', '-c', 'submodule.recurse=false',
]


def git(*args, cwd, capture=False):
    env = {**{k: v for k, v in os.environ.items() if not k.startswith('GIT_')}, 'GIT_TERMINAL_PROMPT': '0',
           'GIT_CONFIG_GLOBAL': os.devnull, 'GIT_CONFIG_NOSYSTEM': '1',
           'GIT_LFS_SKIP_SMUDGE': '1'}
    return subprocess.run(['git', *GIT_OPTIONS, *args], cwd=cwd,
                          check=True, env=env, text=True, capture_output=capture)


def validate_catalog(data):
    categories = {c['id'] for c in data['categories']}
    if any(not re.fullmatch(r'[a-z][a-z0-9-]*', c) for c in categories):
        raise ValueError('Invalid category')
    excluded = {x.lower() for x in data.get('source_review', {}).get('excluded_from_catalog', [])}
    seen = set()
    rows = data['repositories']
    for r in rows:
        key = r['id'].lower()
        if key in seen or key in excluded:
            raise ValueError('Duplicate or excluded catalog member: ' + r['id'])
        seen.add(key)
        parts = r['slug'].split('/')
        if (r['category'] not in categories or any(
                not re.fullmatch(r'[A-Za-z0-9_.-]+', p) or p in {'.', '..'} for p in parts)):
            raise ValueError('Invalid source identity')
        if r['id'] != r['host'] + ':' + r['slug']:
            raise ValueError('Invalid source ID')
        expected = 'tools/' + r['category'] + '/' + r['host'] + '/' + r['slug'].replace('/', '--')
        if r['path'] != expected:
            raise ValueError('Invalid source path')
        if r.get('kind', 'git') == 'source-package':
            if r['host'] != 'debian-source' or len(parts) != 1 or not r.get('version'):
                raise ValueError('Invalid source package')
            files = r.get('files', [])
            filenames = set()
            if not files:
                raise ValueError('Empty source package')
            for f in files:
                name = f['filename']
                if (name in filenames or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9.+_~-]*', name)
                        or not name.startswith(r['slug'] + '_')
                        or not name.endswith(('.dsc', '.tar.gz', '.tar.bz2', '.tar.xz', '.tar.zst'))):
                    raise ValueError('Invalid source package filename')
                filenames.add(name)
                url = 'https://deb.debian.org/debian/pool/main/' + r['slug'][0] + '/' + r['slug'] + '/' + name
                if (f['url'] != url or not re.fullmatch(r'[0-9a-f]{64}', f['sha256'])
                        or not isinstance(f['size'], int) or isinstance(f['size'], bool)
                        or not 0 < f['size'] <= MAX_ARCHIVE_BYTES):
                    raise ValueError('Invalid source package URL, digest or size')
        elif r.get('kind', 'git') == 'git':
            base = HOST_BASES.get(r['host'])
            if (not base or (len(parts) < 2 and r['host'] != 'sourceware')
                    or r['clone_url'] != base + r['slug'] + '.git'
                    or not re.fullmatch(r'[0-9a-f]{40}', r['commit'])):
                raise ValueError('Noncanonical source URL or invalid pin')
        else:
            raise ValueError('Unsupported source kind')
    active_ids = {r['id'] for r in rows}
    if any(not set(ids) <= active_ids for ids in data['profiles'].values()):
        raise ValueError('Profile contains unavailable sources')
    return rows


def safe_target(row):
    target = ROOT / row['path']
    for part in (target, *target.parents):
        if part == ROOT:
            break
        if part.is_symlink():
            raise ValueError('Symlink in source destination: ' + row['path'])
    if ROOT.resolve() not in target.resolve().parents:
        raise ValueError('Source destination escapes workspace')
    return target


def fetch_package(row, target):
    target.mkdir(parents=True, exist_ok=True)
    for f in row['files']:
        destination = target / f['filename']
        if destination.is_symlink():
            raise ValueError('Refusing archive destination symlink')
        if destination.exists():
            if (destination.stat().st_size != f['size']
                    or hashlib.sha256(destination.read_bytes()).hexdigest() != f['sha256']):
                raise ValueError('Existing source package checksum mismatch: ' + str(destination))
            continue
        temp_name = None
        try:
            request = urllib.request.Request(f['url'], headers={'User-Agent': 'RedTeaming-source-fetch/2'})
            with urllib.request.urlopen(request, timeout=60) as response:
                if not response.geturl().startswith('https://'):
                    raise ValueError('Source download redirected away from HTTPS')
                with tempfile.NamedTemporaryFile(dir=target, delete=False) as output:
                    temp_name = output.name
                    digest = hashlib.sha256()
                    size = 0
                    while True:
                        chunk = response.read(65536)
                        if not chunk:
                            break
                        size += len(chunk)
                        if size > f['size']:
                            raise ValueError('Source package exceeds recorded size')
                        output.write(chunk)
                        digest.update(chunk)
            if size != f['size'] or digest.hexdigest() != f['sha256']:
                raise ValueError('Source package checksum mismatch: ' + f['filename'])
            os.replace(temp_name, destination)
            temp_name = None
        finally:
            if temp_name is not None:
                Path(temp_name).unlink(missing_ok=True)
    # Keep source packages opaque: never extract or execute their contents.


def check_local_git_config(target):
    result = git('config', '--local', '--null', '--list', cwd=target, capture=True)
    safe = {'core.repositoryformatversion', 'core.filemode', 'core.bare',
            'core.logallrefupdates', 'core.ignorecase', 'core.precomposeunicode',
            'remote.origin.url', 'remote.origin.fetch'}
    for entry in result.stdout.split('\0'):
        if not entry:
            continue
        name = entry.split('\n', 1)[0].lower()
        if name not in safe and not re.fullmatch(r'branch\..+\.(remote|merge)', name):
            raise ValueError('Unreviewed local Git setting: ' + name)


def fetch(row):
    target = safe_target(row)
    if row.get('kind', 'git') == 'source-package':
        fetch_package(row, target)
        return row['id']
    target.parent.mkdir(parents=True, exist_ok=True)
    dotgit = target / '.git'
    if dotgit.is_symlink() or (dotgit.exists() and not dotgit.is_dir()):
        raise ValueError('Refusing external Git directory: ' + row['path'])
    if not dotgit.exists():
        if target.exists() and any(target.iterdir()):
            raise ValueError('Refusing to initialize nonempty directory: ' + row['path'])
        target.mkdir(exist_ok=True)
        git('init', cwd=target)
        git('remote', 'add', 'origin', row['clone_url'], cwd=target)
    check_local_git_config(target)
    origin = git('config', '--local', '--get', 'remote.origin.url', cwd=target, capture=True).stdout.strip()
    if origin != row['clone_url']:
        raise ValueError('Unexpected existing origin: ' + row['path'])
    git('fetch', '--depth', '1', 'origin', row['commit'], cwd=target)
    git('checkout', '--detach', row['commit'], cwd=target)
    actual = git('rev-parse', 'HEAD', cwd=target, capture=True).stdout.strip()
    if actual != row['commit']:
        raise ValueError('Fetched source pin mismatch')
    return row['id']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--all', action='store_true')
    selection.add_argument('--profile')
    selection.add_argument('--category')
    selection.add_argument('--repo')
    parser.add_argument('--jobs', type=int, choices=range(1, 17), default=4)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    data = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
    rows = validate_catalog(data)
    if args.profile:
        if args.profile not in data['profiles']:
            parser.error('Unknown profile')
        wanted = set(data['profiles'][args.profile])
        rows = [r for r in rows if r['id'] in wanted]
    elif args.category:
        rows = [r for r in rows if r['category'] == args.category]
    elif args.repo:
        rows = [r for r in rows if r['id'] == args.repo]
    if not rows:
        parser.error('No active source matches this selection')
    if args.dry_run:
        for r in rows:
            print(r['id'] + '\t' + r.get('commit', r.get('version', '')))
    else:
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            for source_id in pool.map(fetch, rows):
                print('Fetched ' + source_id, flush=True)
    print(str(len(rows)) + ' active sources selected.')


if __name__ == '__main__':
    main()
