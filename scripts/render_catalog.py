#!/usr/bin/env python3
"""Render catalog and review tables from their recorded JSON observations."""
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


def write(name, lines):
    (ROOT / name).write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')


def cell(value):
    return str(value if value is not None else 'Not reported').replace('|', '\\|').replace('\n', ' ')


def pin_url(row):
    if row.get('kind') == 'source-package':
        return row['descriptor_url']
    if row['host'] == 'sourceware':
        return row['url'] + ';a=tree;h=' + row['commit']
    return row['url'] + ('/tree/' if row['host'] == 'github' else '/-/tree/') + row['commit']


def source_link(row):
    return '[' + row['slug'] + '](' + row['url'] + ')'


def pin_link(row):
    return '[' + row.get('commit', row.get('version', ''))[:12] + '](' + pin_url(row) + ')'


def main():
    data = read('catalog.json')
    batch = read('redos-source-review.json')
    coverage = read('redos-coverage.json')
    review = read('source-review.json')
    rows = data['repositories']
    by_id = {r['id']: r for r in rows}
    hosts = Counter(r['host'] for r in rows)
    total = len(rows)
    excluded = len(data['source_review']['excluded_from_catalog'])
    new_count = batch['summary']['active_additions']
    git_count = sum(r.get('kind', 'git') == 'git' for r in rows)
    totals = f"**{total} active source projects · {git_count} pinned Git sources · {total-git_count} SHA-256 pinned Debian source packages · {len(data['categories'])} categories**"
    profile_count = len(data['profiles']['redos'])
    lines = ['# RedTeaming', '', '**Know the surface. Challenge the controls. Prove the impact.**', '',
      'A curated source collection for red teaming, penetration testing and security research.', '', totals, '',
      f"RedOS update: **{new_count} added sources**, covering **145/147 identified menu entries** and **58/74 additional inventory entries**. The RedOS profile contains {profile_count} distinct source projects; multiple commands can come from one project.", '',
      '- [Browse active projects and exact versions](CATALOG.md)',
      '- [RedOS tool-by-tool coverage and remaining gaps](REDOS_COVERAGE.md)',
      '- [RedOS source screening and findings](REDOS_REVIEW.md)',
      '- [Dated collection-wide review and limits](SOURCE_REVIEW.md)',
      '- [Excluded sources and reasons](EXCLUDED.md)',
      '- [Machine-readable catalog and profiles](catalog.json)',
      '- [Third-party authors and licenses](THIRD_PARTY.md)', '',
      '## Download sources', '', '```bash',
      'git clone https://github.com/bunnyho1e/RedTeaming.git', 'cd RedTeaming',
      'python3 fetch_sources.py --profile redos --jobs 4', '```', '',
      f"A normal Git clone downloads this catalog and helper. The helper then fetches the selected sources into `tools/<category>/<host>/<project>/`: Git projects at exact recorded commits, and socat/traceroute as complete Debian source-package files verified against recorded SHA-256 digests. Source packages remain unextracted.", '',
      'No upstream installer, tool, nested submodule, container, GDB extension or PowerShell module is started. Git and Python 3.9+ are sufficient for this fetch step; each tool has its own build/runtime dependencies.', '',
      '```bash', 'python3 fetch_sources.py --all --dry-run',
      'python3 fetch_sources.py --all --jobs 4',
      'python3 fetch_sources.py --profile web', 'python3 fetch_sources.py --profile ad',
      'python3 fetch_sources.py --profile mobile', 'python3 fetch_sources.py --profile passwords',
      'python3 fetch_sources.py --profile wireless', 'python3 fetch_sources.py --profile system',
      '```', '',
      'Other existing profiles remain available: `starter`, `cloud`, `ai`. Use `--category <id>` or `--repo <source-id>` for a narrower selection.', '',
      '## Review status', '',
      f"The original 193 source pins retain their 2026-10-20 review. The {new_count} additions were screened on 2026-10-21 using provider identity/pin checks, bounded static source inspection and known-advisory queries. OSV returned no record for the 61 candidate queries in this batch; this is not a malware-free certification or a dependency audit. Four large toolchains received selected-file review only.", '',
      f"All {excluded} exclusions apply to every download/profile. PowerSploit is archived; Nishang is held because its PowerShell 2 module-import branch can admit and start the Keylogger script. The 15 custom RTG component identities and the ambiguous `exploit-suggester` entry remain unverified and are not downloadable members. See the coverage and review documents for exact evidence and limits.", '',
      'The helper checks source URLs, paths, pins, exclusions and package checksums. It refuses destination symlinks and unreviewed existing local Git settings. Upstream release binaries and transitive dependencies require their own review. Deliberately vulnerable labs and AI agents retain their existing review classifications.', '',
      '## Data and validation', '',
      '`catalog.json` is the active allowlist. `redos-coverage.json` maps the 221 identified inventory entries. `redos-source-review.json` records the new observations; `source-review.json` retains both review dates. New source identities are not claims that versions match the VM byte for byte.', '',
      '```bash', 'python3 -m unittest discover -s tests -v',
      'python3 scripts/render_catalog.py', 'python3 fetch_sources.py --all --dry-run', '```']
    write('README.md', lines)
    lines = ['# RedTeaming source catalog', '', totals, '',
      'Metadata dates: original 193 projects on 2026-10-20; RedOS additions on 2026-10-21. Stars describe popularity and are not a security assessment. Providers without a star/archive observation are labeled accordingly.', '',
      '[Workspace](README.md) · [RedOS coverage](REDOS_COVERAGE.md) · [Review](SOURCE_REVIEW.md) · [Exclusions](EXCLUDED.md)', '']
    for category in data['categories']:
        lines += ['## ' + category['title'], '', '| Project | Host | Stars | Purpose | State | License | Fixed source |', '| --- | --- | ---: | --- | --- | --- | --- |']
        for r in sorted((r for r in rows if r['category'] == category['id']), key=lambda r: (-(r.get('stars') or 0), r['id'].lower())):
            state = 'Not archived' if r.get('archived') is False else 'Archived' if r.get('archived') is True else 'Not reported'
            license = r.get('license_spdx')
            if not license or license == 'NOASSERTION':
                license = r.get('license_name') or 'Consult upstream license files'
            lines.append('| ' + ' | '.join([source_link(r), r['host'], cell(r.get('stars')), cell(r['purpose']), state, cell(license), pin_link(r)]) + ' |')
        lines.append('')
    write('CATALOG.md', lines)
    lines = ['# Third-party attribution and license inventory', '',
      'Every linked source belongs to its upstream authors and contributors. This repository catalogs source identities and downloads them on request; it does not vendor third-party source trees. Original license and copyright files remain with each fetched project. No license for this collection overrides third-party terms.', '',
      'Host-provided license metadata can be incomplete or describe only part of a project. WPScan uses its Public Source License; PEDA uses CC-BY-NC-SA-3.0. Follow each recorded source and its license files for applicable terms. Debian packages include upstream source plus Debian packaging/patches.', '',
      '| Project | Host | Recorded license | Fixed source |', '| --- | --- | --- | --- |']
    for r in sorted(rows, key=lambda r: r['id'].lower()):
        license = r.get('license_spdx')
        if not license or license == 'NOASSERTION':
            license = r.get('license_name') or 'Consult upstream license files'
        lines.append('| ' + ' | '.join([source_link(r), r['host'], cell(license), pin_link(r)]) + ' |')
    write('THIRD_PARTY.md', lines)
    lines = ['# Source review — dated observations', '',
      f"**{total} active source projects; {excluded} excluded source identities.**", '',
      '[RedOS batch review](REDOS_REVIEW.md) · [Full evidence](source-review.json) · [Exclusions](EXCLUDED.md)', '',
      'The original 193 observations are retained from 2026-10-20, including their OSV/Scorecard dates and statuses. They were not silently re-audited or re-pinned during the RedOS update. The 59 new observations are dated 2026-10-21 and use the scoped methods recorded in [redos-source-review.json](redos-source-review.json).', '',
      'No upstream tool, installer, exploit, module or container was installed or executed. Git source retrieval and text inspection do not establish that code is malware-free. OSV can lack records for a vulnerable project or an unindexed commit; an empty result is not a clean bill of health. Cached Scorecard data in the older evidence can describe another commit and is not a malware detector.', '',
      'The original `REVIEW_AGENT` and `ISOLATED_LAB` classifications remain. `SOURCE_CHECKED_ONLY` and `SOURCE_SCREENED_ONLY` permit source inclusion in this catalog, not execution approval. Dependencies, release binaries, full-code audits and VM-wide scans are outside this screen.', '']
    reviews = {r['id']: r for r in review['repositories']}
    for category in data['categories']:
        lines += ['## ' + category['title'], '', '| Source | Observation date | Status | Advisory query | Fixed source |', '| --- | --- | --- | --- | --- |']
        for r in sorted((r for r in rows if r['category'] == category['id']), key=lambda r:r['id'].lower()):
            obs = reviews[r['id']]
            osv = obs.get('osv', {})
            query = 'Package/version: no record returned' if osv.get('query') == 'package_and_version' else 'Commit: no record returned' if not osv.get('advisory_ids') else ', '.join(osv['advisory_ids'])
            lines.append('| ' + ' | '.join([source_link(r), obs.get('checked_at','')[:10], obs['status'], cell(query), pin_link(r)]) + ' |')
        lines.append('')
    write('SOURCE_REVIEW.md', lines)
    lines = ['# RedOS source review — 2026-10-21', '',
      '**61 source candidates screened; 59 added; 2 held.** The original 193 source pins are unchanged.', '',
      '[Coverage](REDOS_COVERAGE.md) · [Machine-readable evidence](redos-source-review.json) · [Exclusions](EXCLUDED.md)', '',
      '## Methods and limits', '',
      'The review checked provider/source identities, exact Git commit responses, archive status when reported, selected build/entrypoint/license files, and bounded static text patterns. Common patterns covered remote installer pipelines, encoded execution, credential-store access, persistence, webhook endpoints and miners. Matches were interpreted in the context of each tool. Password auditing, proxy interception and assessment payloads are intentional capabilities; their presence alone does not prove a concealed implant.', '',
      'OSV returned no vulnerability record for 59 commit queries and two Debian package/version queries. Those 61 queries include the two held candidates. No-record results do not establish absence of vulnerabilities or malicious behavior. Source fingerprints and captured file lists are evidence of what was examined, not a claim that every line was manually audited.', '',
      'GCC, Go, PowerShell and GNU Binutils/GDB received selected-file review rather than a complete source-pattern scan. Other snapshot screens had a 64 MiB compressed / 256 MiB expanded limit and a 2 MiB per-text-file limit, and selected common source/config file suffixes. Transitive dependencies and release binaries were not installed or audited. GitLab providers omitted archive-state fields in some metadata responses; those states are recorded as unknown.', '',
      'For strace, upstream .gitattributes deliberately removes code from autogenerated archives. Actual pinned Git objects were fetched and inspected instead. Socat and traceroute are complete Debian source packages: descriptor, upstream archive and Debian patch archive. Their recorded SHA-256 digests and sizes matched; descriptor signatures were not cryptographically verified. The fetcher stores those files without extracting them.', '',
      'No upstream tool, installer, module, container or target-facing operation was executed. This is a scoped source screen, not a malware-free certification.', '',
      '## Held candidates', '',
      '- **PowerSploit:** GitHub reports archived. Retained outside the active catalog under the existing conservative policy.',
      '- **Nishang:** `nishang.psm1` line 20 uses OR between three unequal-name checks in the PowerShell 2 branch. That condition admits `Gather/Keylogger.ps1`, whose top-level job-start calls can begin logging during module import. The other branch excludes that script. This specific import side effect is why the candidate is held; it is not labeled a proven concealed implant.', '',
      'Both candidates and their exact pins remain in the evidence files and [exclusion record](EXCLUDED.md), outside every active profile.', '',
      '## Unverified inventory identities', '',
      'The 15 RTG-specific component identities have no canonical public source/version and redistribution terms verified in the inspected author repositories. The RedOS website links a VM download; the inspected RTG-Community tree contains documentation and OffensiveTools contains older scripts/binaries, not verified source trees for these components. These findings do not prove that no source exists elsewhere. No opaque VM binaries or similarly named unrelated projects were substituted.', '',
      'The additional `exploit-suggester` entry was established only by its VM directory name. Its exact upstream and version remain unknown. The partial VM download also leaves the overall inventory incomplete; see coverage limits.', '',
      '## Added sources and review notes', '',
      '| Source | Fixed version | Scoped observation |', '| --- | --- | --- |']
    for obs in sorted(batch['repositories'], key=lambda r:r['id'].lower()):
        r = by_id[obs['id']]
        lines.append('| ' + ' | '.join([source_link(r), pin_link(r), cell(obs['review_notes'])]) + ' |')
    write('REDOS_REVIEW.md', lines)
    lines = ['# RedOS coverage — 2026-10-21', '',
      '**Menu: 145 included / 2 unverified. Additional inventory: 58 included / 2 held / 14 unverified.**', '',
      f"These 221 entries map to **{profile_count} distinct included source projects**. Duplicate Hydra/Medusa menu entries and multi-command suites are retained as inventory rows, not counted as separate repositories. The original Impacket source already covers the 70 recorded Impacket entrypoints.", '',
      '[RedOS website](https://www.redteamgarage.com/rtg/rtg-redos) · [Review findings](REDOS_REVIEW.md) · [Coverage JSON](redos-coverage.json)', '',
      '## Scope', '', coverage['inventory_limit'], '', coverage['version_limit'], '',
      'Docker maps to the official Docker CLI source, without a claim to include the daemon/Desktop. `nc/netcat` maps to Debian OpenBSD netcat; the VM alternative was not conclusively established. GDB/GEF/PEDA are separate sources; none is loaded automatically.', '']
    for group, title in [('menu','Main menu'),('additional','Additional inventory')]:
        lines += ['## ' + title, '', '| Tool | Command | Status | Source(s) / reason |', '| --- | --- | --- | --- |']
        for r in coverage['rows']:
            if r['group'] != group:
                continue
            source = ', '.join(source_link(by_id[sid]) for sid in r['source_ids']) if r['source_ids'] else cell(r['note'])
            lines.append('| ' + ' | '.join([cell(r['name']), '`'+cell(r['command'])+'`', r['status'].upper(), source]) + ' |')
        lines.append('')
    write('REDOS_COVERAGE.md', lines)
    print(f'Rendered {total} source projects; {new_count} additions; {excluded} exclusions; hosts: {dict(hosts)}')


if __name__ == '__main__':
    main()
