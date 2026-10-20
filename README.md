# RedTeaming

**Know the surface. Challenge the controls. Prove the impact.**

A curated source collection for red teaming, penetration testing, security research, AI-assisted testing and assessment automation.

**200 public projects · 194 GitHub · 6 GitLab · 13 categories**

- [Browse every project, popularity snapshot, license and pinned source](CATALOG.md)
- [Download the complete prepared Git collection](RedTeaming.bundle)
- [Machine-readable catalog and profiles](catalog.json)
- [Original authors and third-party licenses](THIRD_PARTY.md)

## Download every source into one workspace

The Git bundle contains the collection's full Git history, scripts, documentation and 200 pinned submodule entries. The upstream projects' source files are downloaded by the fetch command below. This GitHub tree currently publishes the catalog and source bundle; clone the bundle to use the prepared submodule workspace.

```bash
git clone https://github.com/bunnyho1e/RedTeaming.git RedTeaming-download
git clone RedTeaming-download/RedTeaming.bundle RedTeaming-sources
cd RedTeaming-sources
python3 scripts/workspace.py fetch --all --jobs 6
```

Git and Python 3.9+ are enough for the helper. Each upstream tool has its own installation and operating-system requirements. Fetching source does not install or run those tools.

## Select an area

```bash
python3 scripts/workspace.py fetch --profile starter
python3 scripts/workspace.py fetch --profile web
python3 scripts/workspace.py fetch --profile ad
python3 scripts/workspace.py fetch --profile mobile
python3 scripts/workspace.py fetch --profile cloud
python3 scripts/workspace.py fetch --profile ai
python3 scripts/workspace.py fetch --category recon
```

The 13 categories cover playbooks, reconnaissance, web/API testing, Active Directory and identity, cloud security, mobile instrumentation, network traffic, adversary emulation, reverse engineering, wordlists, AI security, reporting and practice labs.

Included projects range from Nuclei, Burp extensions, BloodHound, Impacket, NetExec, Frida and MobSF to Metasploit, Sliver, PentestGPT, PentAGI, Strix, Shannon, ExploitDB, Wireshark and Kali NetHunter.

## Verify and update

```bash
python3 scripts/workspace.py verify
python3 -m unittest discover -s tests -v
python3 scripts/workspace.py update --profile web --jobs 4
git diff --cached --stat
```

The prepared collection passes 11 tests. Each source is pinned to a verified commit; original authors, upstream history and license terms are preserved. `update` advances selected pins and stages the changes for review; it does not push. Popularity and license metadata retain their recorded verification dates.

## Provenance

Popularity snapshot: **2026-10-20**. Stars are popularity signals, not a guarantee of quality or security. Archived projects are labeled in the catalog. Each upstream project's own license governs its source; the bundle's MIT license covers this collection's original scripts and documentation.

Bundle SHA-256:

```text
54161d1ad565b0fd36ddff9db85a09c82ea59269b285d551da0ee4c0d6e76b6a
```
