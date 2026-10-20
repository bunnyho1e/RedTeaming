# RedTeaming

**Know the surface. Challenge the controls. Prove the impact.**

A curated source collection for red teaming, penetration testing, security research, AI-assisted testing and assessment automation.

**193 active public projects · 187 GitHub · 6 GitLab · 13 categories**

- [Browse every active project, stars, license and pinned source](CATALOG.md)
- [Source review and limits](SOURCE_REVIEW.md)
- [Seven excluded projects and the reasons](EXCLUDED.md)
- [Machine-readable catalog and profiles](catalog.json)
- [Recorded source review evidence](source-review.json)
- [Original authors and third-party licenses](THIRD_PARTY.md)

## Source selection

Seven flagged sources were removed from the active catalog, all profiles and the prepared workspace: HexStrike and Capstone with advisory matches for their previous pins, Trivy under a conservative policy following a historical supply-chain incident, and four archived projects. Every remaining source has stars and a reachable recorded commit. This selection is not a malware-free certification. AI agents still require permission/data-flow review; deliberately vulnerable labs require isolation.

## Download sources into one workspace

```bash
git clone https://github.com/bunnyho1e/RedTeaming.git
cd RedTeaming
python3 fetch_sources.py --all --jobs 4
```

The helper downloads only the **193 active sources** at their recorded commits into `tools/<category>/<host>/<project>/`. It does not install or execute upstream tools or fetch nested submodules. Git and Python 3.9+ are sufficient. A normal Git clone alone does not download the upstream source trees.

```bash
python3 fetch_sources.py --profile starter
python3 fetch_sources.py --profile web
python3 fetch_sources.py --profile ad
python3 fetch_sources.py --profile mobile
python3 fetch_sources.py --profile cloud
python3 fetch_sources.py --profile ai
python3 fetch_sources.py --all --dry-run
```

## Source versions and verification

`catalog.json` is the active allowlist. Re-running the helper checks out its exact recorded pins. Changes to those pins require a new source review. The earlier 200-source bundle is no longer part of this active download path.

The prepared submodule workspace passes its 11 tests, and the direct helper's dry run selects exactly the same 193 source IDs. The review does not cover every transitive dependency, reference link or release binary. Original upstream license terms apply to each project.
