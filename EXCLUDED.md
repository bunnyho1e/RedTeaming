# Excluded sources — 2026-10-21

**Nine source identities are outside the 252-member active catalog.** Seven exclusions are retained from the 2026-10-20 review; two candidates were held during the RedOS update. Every profile, category and `--all` selection uses the same exclusions.

| Source | Reason | Evidence |
| --- | --- | --- |
| `0x4m4/hexstrike-ai` | Four CVE records matched the previously pinned commit. | [CVE-2026-90619](https://osv.dev/vulnerability/CVE-2026-90619), [90620](https://osv.dev/vulnerability/CVE-2026-90620), [90690](https://osv.dev/vulnerability/CVE-2026-90690), [90691](https://osv.dev/vulnerability/CVE-2026-90691) |
| `capstone-engine/capstone` | The previous pin matched an OSS-Fuzz uninitialized-value finding in M68K disassembly. | [OSV-2026-246](https://osv.dev/vulnerability/OSV-2026-246) |
| `aquasecurity/trivy` | Conservatively removed after a confirmed historical supply-chain compromise; the October source pin was not established malicious. | [Maintainer advisory](https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23) |
| `aliasrobotics/cai` | Archived at the original review. | [Upstream](https://github.com/aliasrobotics/cai) |
| `protectai/llm-guard` | Archived at the original review. | [Upstream](https://github.com/protectai/llm-guard) |
| `google/adb-sync` | Archived at the original review. | [Upstream](https://github.com/google/adb-sync) |
| `BuffaloWill/Serpico` | Archived at the original review. | [Upstream](https://github.com/BuffaloWill/Serpico) |
| `PowerShellMafia/PowerSploit` | Archived at the RedOS review; existing conservative policy retained. | [Pinned source](https://github.com/PowerShellMafia/PowerSploit/tree/d943001a7defb5e0d1657085a77a0e78609be58f) |
| `samratashok/nishang` | PowerShell 2 module-import exclusion checks use OR and admit Keylogger; importing that script can start a logging job. Held for this side effect, not labeled a proven concealed implant. | [Import condition, line 20](https://github.com/samratashok/nishang/blob/d87229d2112456470ad30a50edbf312463f2b09a/nishang.psm1#L20), [job starts, lines 382–387](https://github.com/samratashok/nishang/blob/d87229d2112456470ad30a50edbf312463f2b09a/Gather/Keylogger.ps1#L382-L387) |

Archived or vulnerable does not mean proven malicious. Empty advisory results do not establish that a source is malware-free. The exact reviewed pins, dates and decisions are retained under `excluded_repositories` in [source-review.json](source-review.json); the two new observations also appear in [redos-source-review.json](redos-source-review.json).

Fifteen RTG component identities and the ambiguous `exploit-suggester` inventory entry remain **unverified**, rather than labeled malicious or assigned to a guessed project. They have no active download entries. See [REDOS_COVERAGE.md](REDOS_COVERAGE.md) for every remaining gap.
