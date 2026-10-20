# Excluded sources — 2026-10-20

Seven sources were removed following the user's conservative selection policy. The active catalog now contains **193 projects: 187 GitHub and 6 GitLab**. These exclusions apply to every profile, category download and `fetch --all`.

| Source | Reason for removal | Evidence |
| --- | --- | --- |
| `0x4m4/hexstrike-ai` | Four CVE records match the previously pinned commit; command execution, authentication and file-path concerns. | [CVE-2026-90619](https://osv.dev/vulnerability/CVE-2026-90619), [90620](https://osv.dev/vulnerability/CVE-2026-90620), [90690](https://osv.dev/vulnerability/CVE-2026-90690), [90691](https://osv.dev/vulnerability/CVE-2026-90691) |
| `capstone-engine/capstone` | The previous pin is returned for an OSS-Fuzz uninitialized-value finding in M68K disassembly. | [OSV-2026-246](https://osv.dev/vulnerability/OSV-2026-246) |
| `aquasecurity/trivy` | Removed conservatively because of a confirmed historical supply-chain compromise. The October source pin was not established to be malicious. | [Maintainer advisory](https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23) |
| `aliasrobotics/cai` | GitHub reports the project as archived. | [Upstream](https://github.com/aliasrobotics/cai) |
| `protectai/llm-guard` | GitHub reports the project as archived. | [Upstream](https://github.com/protectai/llm-guard) |
| `google/adb-sync` | GitHub reports the project as archived. | [Upstream](https://github.com/google/adb-sync) |
| `BuffaloWill/Serpico` | GitHub reports the project as archived. | [Upstream](https://github.com/BuffaloWill/Serpico) |

An archived or vulnerable project is not thereby proven malicious. The remaining 193 projects passed the recorded host, pin and popularity checks, with no OSV record returned for those commit queries at the review time. That does not certify them as malware-free, review every dependency, or validate every release artifact. References inside upstream documentation and transitive dependencies are outside this top-level selection.

The exclusion evidence remains in `source-review.json` under `excluded_repositories`; only its `repositories` array describes the active selection. Excluded names in this document are an audit record, not downloadable catalog members.
