# RedTeaming

**Know the surface. Challenge the controls. Prove the impact.**

A curated source collection for red teaming, penetration testing and security research.

**252 active source projects · 250 pinned Git sources · 2 SHA-256 pinned Debian source packages · 15 categories**

RedOS update: **59 added sources**, covering **145/147 identified menu entries** and **58/74 additional inventory entries**. The RedOS profile contains 111 distinct source projects; multiple commands can come from one project.

- [Browse active projects and exact versions](CATALOG.md)
- [RedOS tool-by-tool coverage and remaining gaps](REDOS_COVERAGE.md)
- [RedOS source screening and findings](REDOS_REVIEW.md)
- [Dated collection-wide review and limits](SOURCE_REVIEW.md)
- [Excluded sources and reasons](EXCLUDED.md)
- [Machine-readable catalog and profiles](catalog.json)
- [Third-party authors and licenses](THIRD_PARTY.md)

## Download sources

```bash
git clone https://github.com/bunnyho1e/RedTeaming.git
cd RedTeaming
python3 fetch_sources.py --profile redos --jobs 4
```

A normal Git clone downloads this catalog and helper. The helper then fetches the selected sources into `tools/<category>/<host>/<project>/`: Git projects at exact recorded commits, and socat/traceroute as complete Debian source-package files verified against recorded SHA-256 digests. Source packages remain unextracted.

No upstream installer, tool, nested submodule, container, GDB extension or PowerShell module is started. Git and Python 3.9+ are sufficient for this fetch step; each tool has its own build/runtime dependencies.

```bash
python3 fetch_sources.py --all --dry-run
python3 fetch_sources.py --all --jobs 4
python3 fetch_sources.py --profile web
python3 fetch_sources.py --profile ad
python3 fetch_sources.py --profile mobile
python3 fetch_sources.py --profile passwords
python3 fetch_sources.py --profile wireless
python3 fetch_sources.py --profile system
```

Other existing profiles remain available: `starter`, `cloud`, `ai`. Use `--category <id>` or `--repo <source-id>` for a narrower selection.

## Review status

The original 193 source pins retain their 2026-10-20 review. The 59 additions were screened on 2026-10-21 using provider identity/pin checks, bounded static source inspection and known-advisory queries. OSV returned no record for the 61 candidate queries in this batch; this is not a malware-free certification or a dependency audit. Four large toolchains received selected-file review only.

All 9 exclusions apply to every download/profile. PowerSploit is archived; Nishang is held because its PowerShell 2 module-import branch can admit and start the Keylogger script. The 15 custom RTG component identities and the ambiguous `exploit-suggester` entry remain unverified and are not downloadable members. See the coverage and review documents for exact evidence and limits.

The helper checks source URLs, paths, pins, exclusions and package checksums. It refuses destination symlinks and unreviewed existing local Git settings. Upstream release binaries and transitive dependencies require their own review. Deliberately vulnerable labs and AI agents retain their existing review classifications.

## Data and validation

`catalog.json` is the active allowlist. `redos-coverage.json` maps the 221 identified inventory entries. `redos-source-review.json` records the new observations; `source-review.json` retains both review dates. New source identities are not claims that versions match the VM byte for byte.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/render_catalog.py
python3 fetch_sources.py --all --dry-run
```
