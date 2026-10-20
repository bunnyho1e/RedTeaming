# Active source review — 2026-10-20

**193 active sources, each with stars and a reachable recorded commit. Seven reviewed sources have been removed from the catalog, all profiles and all downloads.**

[Workspace](README.md) · [Exclusions and reasons](EXCLUDED.md) · [Recorded evidence](source-review.json)

The original review covered 200 sources: live GitHub/GitLab metadata, exact commit existence, archive flags, OSV queries for recorded commits, cached OpenSSF Scorecard results and selected static entrypoints. The remaining 193 have no advisory returned by those commit-only OSV queries. An empty response is not proof of zero vulnerabilities or absence of malware; dependency and release-binary audits were not performed. All observations apply to the recorded versions and dates.

The remaining collection includes AI agents requiring permission/data-flow review and intentionally vulnerable training labs requiring isolation. Those categories are explicitly labeled. Stars measure popularity. Scorecard measures development practices and can refer to a different commit; see the JSON for its assessment date, commit and missing data. A `SOURCE_CHECKED_ONLY` status does not grant execution approval.

No upstream tool, installer, exploit or container was installed or executed during this review. This is a provenance and known-advisory screen, not a full source audit or malware certification.

## Playbooks & knowledge

| Source | Stars | Status | Scorecard / date | Reviewed pin |
| --- | ---: | --- | --- | --- |
| [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | 251,641 | SOURCE_CHECKED_ONLY | 3.6/10 · 2026-10-12 | [7d37069a361d](https://github.com/trimstray/the-book-of-secret-knowledge/tree/7d37069a361d3fd9f214480755f7969744e866fa) |
| [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | 81,886 | SOURCE_CHECKED_ONLY | 3.9/10 · 2026-10-12 | [3ac27901c711](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/3ac27901c711bdf3f5b65a7b1d1820a1f65bd09a) |
| [The-Art-of-Hacking/h4cker](https://github.com/The-Art-of-Hacking/h4cker) | 29,848 | SOURCE_CHECKED_ONLY | 4.7/10 · 2026-10-12 | [cbf27e671dae](https://github.com/The-Art-of-Hacking/h4cker/tree/cbf27e671daea238e9f05a81fb8354357437c08a) |
| [enaqx/awesome-pentest](https://github.com/enaqx/awesome-pentest) | 27,486 | SOURCE_CHECKED_ONLY | 4/10 · 2026-10-19 | [d70480bad202](https://github.com/enaqx/awesome-pentest/tree/d70480bad2020b90299363ccb0ebf65fb75653d7) |
| [peass-ng/PEASS-ng](https://github.com/peass-ng/PEASS-ng) | 20,699 | SOURCE_CHECKED_ONLY | Unavailable | [2d186bd98a4a](https://github.com/peass-ng/PEASS-ng/tree/2d186bd98a4a0f5a8c5e9d203cb550c710a88a02) |
| [GTFOBins/GTFOBins.github.io](https://github.com/GTFOBins/GTFOBins.github.io) | 13,764 | SOURCE_CHECKED_ONLY | 3.4/10 · 2026-10-19 | [acd524623f9c](https://github.com/GTFOBins/GTFOBins.github.io/tree/acd524623f9c406acedd2754ebd9c2431f3675ad) |
| [OWASP/mastg](https://github.com/OWASP/mastg) | 13,268 | SOURCE_CHECKED_ONLY | Unavailable | [02ffd85fb743](https://github.com/OWASP/mastg/tree/02ffd85fb74383ec2a30b42866d38f89d72c0ead) |
| [redcanaryco/atomic-red-team](https://github.com/redcanaryco/atomic-red-team) | 12,705 | SOURCE_CHECKED_ONLY | 3.7/10 · 2026-10-12 | [388942adbd96](https://github.com/redcanaryco/atomic-red-team/tree/388942adbd9641f4dfdcf079d7efe9a75ec0ac43) |
| [HackTricks-wiki/hacktricks](https://github.com/HackTricks-wiki/hacktricks) | 12,592 | SOURCE_CHECKED_ONLY | Unavailable | [98ca040281bf](https://github.com/HackTricks-wiki/hacktricks/tree/98ca040281bfaa87a4555ab2eeb75db983fa94bb) |
| [infosecn1nja/Red-Teaming-Toolkit](https://github.com/infosecn1nja/Red-Teaming-Toolkit) | 10,789 | SOURCE_CHECKED_ONLY | Unavailable | [053fe2ee2e76](https://github.com/infosecn1nja/Red-Teaming-Toolkit/tree/053fe2ee2e764cdcddd6f08820a4194db5cbd0a8) |
| [OWASP/wstg](https://github.com/OWASP/wstg) | 10,067 | SOURCE_CHECKED_ONLY | 4.9/10 · 2026-10-19 | [0dfbd5a585a5](https://github.com/OWASP/wstg/tree/0dfbd5a585a503e27761b8f6c8bd8caf0903c8e8) |
| [LOLBAS-Project/LOLBAS](https://github.com/LOLBAS-Project/LOLBAS) | 8,891 | SOURCE_CHECKED_ONLY | Unavailable | [2056cb766250](https://github.com/LOLBAS-Project/LOLBAS/tree/2056cb7662509dc998fc6ce79636aec4e6c0397f) |
| [s0md3v/AwesomeXSS](https://github.com/s0md3v/AwesomeXSS) | 5,152 | SOURCE_CHECKED_ONLY | Unavailable | [9982704e7c62](https://github.com/s0md3v/AwesomeXSS/tree/9982704e7c6217a74463d187c5a6258b9343eaa9) |
| [0x4D31/awesome-threat-detection](https://github.com/0x4D31/awesome-threat-detection) | 4,760 | SOURCE_CHECKED_ONLY | Unavailable | [f1e6a1528c26](https://github.com/0x4D31/awesome-threat-detection/tree/f1e6a1528c2690d02fa87a97c860235eabc34639) |
| [OWASP/ASVS](https://github.com/OWASP/ASVS) | 3,700 | SOURCE_CHECKED_ONLY | 5/10 · 2026-10-19 | [2b47a9dd1676](https://github.com/OWASP/ASVS/tree/2b47a9dd16760ee484a6672d197f1f7e25d9c632) |
| [OWASP/masvs](https://github.com/OWASP/masvs) | 2,460 | SOURCE_CHECKED_ONLY | Unavailable | [bbe226fd17e6](https://github.com/OWASP/masvs/tree/bbe226fd17e6dab51927f392936deef31c816423) |
| [bugcrowd/HUNT](https://github.com/bugcrowd/HUNT) | 2,339 | SOURCE_CHECKED_ONLY | Unavailable | [5ba4dccff3bd](https://github.com/bugcrowd/HUNT/tree/5ba4dccff3bd98c7ca0a7024e5cff8aaf0afbd5d) |
| [trailofbits/awesome-ml-security](https://github.com/trailofbits/awesome-ml-security) | 171 | SOURCE_CHECKED_ONLY | Unavailable | [d7fe4fa91719](https://github.com/trailofbits/awesome-ml-security/tree/d7fe4fa917192dba20051741d357c939c709a1e3) |
| [OWASP/www-project-api-security](https://github.com/OWASP/www-project-api-security) | 48 | SOURCE_CHECKED_ONLY | Unavailable | [c144e52e4e4f](https://github.com/OWASP/www-project-api-security/tree/c144e52e4e4f8c47c7e0343ff0411c3c615ebec0) |
| [exploit-database/exploitdb-papers](https://gitlab.com/exploit-database/exploitdb-papers) | 28 | SOURCE_CHECKED_ONLY | Unavailable | [d79ce5ad128f](https://gitlab.com/exploit-database/exploitdb-papers/-/tree/d79ce5ad128f48f222ce4e659d0924eb0d06a1db) |

## Recon & attack surface

| Source | Stars | Status | Scorecard / date | Reviewed pin |
| --- | ---: | --- | --- | --- |
| [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 94,520 | SOURCE_CHECKED_ONLY | 5.6/10 · 2026-10-12 | [e40a45ec2a07](https://github.com/sherlock-project/sherlock/tree/e40a45ec2a074b90703b3b4b842c8a3adbd6ada3) |
| [smicallef/spiderfoot](https://github.com/smicallef/spiderfoot) | 23,634 | SOURCE_CHECKED_ONLY | 3.8/10 · 2026-10-12 | [0f815a203afe](https://github.com/smicallef/spiderfoot/tree/0f815a203afebf05c98b605dba5cf0475a0ee5fd) |
| [laramies/theHarvester](https://github.com/laramies/theHarvester) | 18,003 | SOURCE_CHECKED_ONLY | 7.5/10 · 2026-10-19 | [8c72cbf331c2](https://github.com/laramies/theHarvester/tree/8c72cbf331c28629706cd9b6be91da62424ddcd9) |
| [projectdiscovery/katana](https://github.com/projectdiscovery/katana) | 17,694 | SOURCE_CHECKED_ONLY | 6.1/10 · 2026-10-12 | [9662cd7b60ba](https://github.com/projectdiscovery/katana/tree/9662cd7b60ba1bc3a88232433ddefc4f48a65bfe) |
| [owasp-amass/amass](https://github.com/owasp-amass/amass) | 15,381 | SOURCE_CHECKED_ONLY | 3/10 · 2026-10-12 | [79299dce87b0](https://github.com/owasp-amass/amass/tree/79299dce87b0085db0f2f4ef3e9c52cccb49f514) |
| [projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder) | 14,623 | SOURCE_CHECKED_ONLY | 6.1/10 · 2026-10-12 | [b9239ac6abae](https://github.com/projectdiscovery/subfinder/tree/b9239ac6abaeb389f36e4d0e1484394b697d7b91) |
| [s0md3v/Photon](https://github.com/s0md3v/Photon) | 13,294 | SOURCE_CHECKED_ONLY | 2.4/10 · 2026-10-12 | [c8d2566841d6](https://github.com/s0md3v/Photon/tree/c8d2566841d69a268b244609921143d84b72b0c6) |
| [blacklanternsecurity/bbot](https://github.com/blacklanternsecurity/bbot) | 10,722 | SOURCE_CHECKED_ONLY | Unavailable | [a6fb827bb144](https://github.com/blacklanternsecurity/bbot/tree/a6fb827bb144cdb85b52e142a4d6e14ed5f94b69) |
| [projectdiscovery/httpx](https://github.com/projectdiscovery/httpx) | 10,495 | SOURCE_CHECKED_ONLY | 6.2/10 · 2026-10-12 | [f3ac85045712](https://github.com/projectdiscovery/httpx/tree/f3ac850457129af3910cf641fe4e2bc2ee178172) |
| [six2dez/reconftw](https://github.com/six2dez/reconftw) | 8,214 | SOURCE_CHECKED_ONLY | 5.5/10 · 2026-10-12 | [b9807ab78788](https://github.com/six2dez/reconftw/tree/b9807ab787880700e08f435df5c84023d16b0b6c) |
| [projectdiscovery/naabu](https://github.com/projectdiscovery/naabu) | 6,313 | SOURCE_CHECKED_ONLY | 5.8/10 · 2026-10-12 | [38726814aff1](https://github.com/projectdiscovery/naabu/tree/38726814aff178e20c2c0c0da5df6e86735416bb) |
| [lc/gau](https://github.com/lc/gau) | 5,127 | SOURCE_CHECKED_ONLY | 4.4/10 · 2026-10-12 | [4eabace30987](https://github.com/lc/gau/tree/4eabace309877abb231def9eeb27b96c07ed3635) |
| [tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls) | 4,580 | SOURCE_CHECKED_ONLY | Unavailable | [8d27cf3e3031](https://github.com/tomnomnom/waybackurls/tree/8d27cf3e3031de01179e8ba9127e968eb01008e9) |
| [Findomain/Findomain](https://github.com/Findomain/Findomain) | 3,796 | SOURCE_CHECKED_ONLY | 4.8/10 · 2026-10-19 | [cc5f40c03fcc](https://github.com/Findomain/Findomain/tree/cc5f40c03fcc20d8b31e263dc5d4c0b22edfaad7) |
| [tomnomnom/assetfinder](https://github.com/tomnomnom/assetfinder) | 3,691 | SOURCE_CHECKED_ONLY | Unavailable | [4e95d8701aae](https://github.com/tomnomnom/assetfinder/tree/4e95d8701aae8cff1c27af2626eb22ba110ad583) |
| [tomnomnom/httprobe](https://github.com/tomnomnom/httprobe) | 3,124 | SOURCE_CHECKED_ONLY | Unavailable | [0745f649beb0](https://github.com/tomnomnom/httprobe/tree/0745f649beb01c3cf712e0c52f9760d8a92cfdc2) |
| [projectdiscovery/uncover](https://github.com/projectdiscovery/uncover) | 3,088 | SOURCE_CHECKED_ONLY | 5.5/10 · 2026-10-12 | [827504844132](https://github.com/projectdiscovery/uncover/tree/8275048441329a9ce0622bead7b37826d34e5d7d) |
| [projectdiscovery/dnsx](https://github.com/projectdiscovery/dnsx) | 2,909 | SOURCE_CHECKED_ONLY | 5.7/10 · 2026-10-12 | [a1536fedba21](https://github.com/projectdiscovery/dnsx/tree/a1536fedba21caf278eaf65063844616c31b4ecc) |
| [projectdiscovery/notify](https://github.com/projectdiscovery/notify) | 1,622 | SOURCE_CHECKED_ONLY | 5.4/10 · 2026-10-12 | [2d6ef20689e8](https://github.com/projectdiscovery/notify/tree/2d6ef20689e805c957c195471d9d2e926ba6a758) |
| [projectdiscovery/pdtm](https://github.com/projectdiscovery/pdtm) | 1,170 | SOURCE_CHECKED_ONLY | Unavailable | [de1221928066](https://github.com/projectdiscovery/pdtm/tree/de12219280663c676851e0f2c79fe10016ee6537) |
| [projectdiscovery/tlsx](https://github.com/projectdiscovery/tlsx) | 1,151 | SOURCE_CHECKED_ONLY | 5.8/10 · 2026-10-12 | [7f24430c54c4](https://github.com/projectdiscovery/tlsx/tree/7f24430c54c473e6b32caf29753562da6ffb4181) |
| [projectdiscovery/asnmap](https://github.com/projectdiscovery/asnmap) | 1,139 | SOURCE_CHECKED_ONLY | 4.5/10 · 2026-10-12 | [cedef8b116fb](https://github.com/projectdiscovery/asnmap/tree/cedef8b116fb2ea228108bfa2eee6ed74ae31ad9) |
| [projectdiscovery/alterx](https://github.com/projectdiscovery/alterx) | 1,017 | SOURCE_CHECKED_ONLY | 5.5/10 · 2026-10-12 | [3322e4f82614](https://github.com/projectdiscovery/alterx/tree/3322e4f82614302860c544ee5c014a02081bd2ea) |

## Web & API testing

| Source | Stars | Status | Scorecard / date | Reviewed pin |
| --- | ---: | --- | --- | --- |
| [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy) | 45,764 | SOURCE_CHECKED_ONLY | 6.4/10 · 2026-10-12 | [696d4e28c54c](https://github.com/mitmproxy/mitmproxy/tree/696d4e28c54cd2f66640c6307ab978fec1ba2f16) |
| [sqlmapproject/sqlmap](https://github.com/sqlmapproject/sqlmap) | 38,748 | SOURCE_CHECKED_ONLY | 4.8/10 · 2026-10-12 | [d57415479ae0](https://github.com/sqlmapproject/sqlmap/tree/d57415479ae016db0e4c76abd3a75ad12cb4e34a) |
| [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) | 32,152 | SOURCE_CHECKED_ONLY | 6.9/10 · 2026-10-12 | [f3b817b818a6](https://github.com/projectdiscovery/nuclei/tree/f3b817b818a61e87296a27441351e85d739140b8) |
| [ffuf/ffuf](https://github.com/ffuf/ffuf) | 16,909 | SOURCE_CHECKED_ONLY | 5.7/10 · 2026-10-12 | [8d65e0373e5f](https://github.com/ffuf/ffuf/tree/8d65e0373e5f223530174e5694285af849770078) |
| [zaproxy/zaproxy](https://github.com/zaproxy/zaproxy) | 15,975 | SOURCE_CHECKED_ONLY | 6.8/10 · 2026-10-12 | [e06ba5ee209e](https://github.com/zaproxy/zaproxy/tree/e06ba5ee209e27a9a81ff16e17696d6b59757d3a) |
| [s0md3v/XSStrike](https://github.com/s0md3v/XSStrike) | 15,220 | SOURCE_CHECKED_ONLY | Unavailable | [ab27955d3674](https://github.com/s0md3v/XSStrike/tree/ab27955d367432f944d8f29897e09c15356e76f7) |
| [OJ/gobuster](https://github.com/OJ/gobuster) | 14,229 | SOURCE_CHECKED_ONLY | 3.7/10 · 2026-10-19 | [c77583fbb882](https://github.com/OJ/gobuster/tree/c77583fbb8824058d74d38240896eff610683c8e) |
| [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates) | 13,136 | SOURCE_CHECKED_ONLY | 4.2/10 · 2026-10-12 | [ee9e6969a9be](https://github.com/projectdiscovery/nuclei-templates/tree/ee9e6969a9befe639e9083bacc33b824400d0bb9) |
| [sullo/nikto](https://github.com/sullo/nikto) | 10,785 | SOURCE_CHECKED_ONLY | 3.8/10 · 2026-10-12 | [312645d87347](https://github.com/sullo/nikto/tree/312645d873478a77986627ab1fc8cffe595e85d4) |
| [testssl/testssl.sh](https://github.com/testssl/testssl.sh) | 9,241 | SOURCE_CHECKED_ONLY | Unavailable | [9bd7e16df96a](https://github.com/testssl/testssl.sh/tree/9bd7e16df96a8e4e36c89f6c55443eceb9e36c71) |
| [epi052/feroxbuster](https://github.com/epi052/feroxbuster) | 8,127 | SOURCE_CHECKED_ONLY | 3.7/10 · 2026-10-19 | [b07a7662d588](https://github.com/epi052/feroxbuster/tree/b07a7662d588bd8e4371e9be4704a02d976c89bb) |
| [KathanP19/HowToHunt](https://github.com/KathanP19/HowToHunt) | 7,370 | SOURCE_CHECKED_ONLY | 2.1/10 · 2026-10-19 | [4c8c23fce6c7](https://github.com/KathanP19/HowToHunt/tree/4c8c23fce6c754e9495101d3894cc7228ee7c709) |
| [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool) | 6,796 | SOURCE_CHECKED_ONLY | Unavailable | [3bc7407cf222](https://github.com/ticarpi/jwt_tool/tree/3bc7407cf2222d6a821dcc19c776e5a1b1cb9a9b) |
| [hahwul/dalfox](https://github.com/hahwul/dalfox) | 5,328 | SOURCE_CHECKED_ONLY | 3.2/10 · 2026-10-12 | [947732dbeda0](https://github.com/hahwul/dalfox/tree/947732dbeda028d7127b6768d19c6d5b0d6b3160) |
| [projectdiscovery/interactsh](https://github.com/projectdiscovery/interactsh) | 4,596 | SOURCE_CHECKED_ONLY | 6.4/10 · 2026-10-12 | [a5b78b2f1d99](https://github.com/projectdiscovery/interactsh/tree/a5b78b2f1d990cd18c85cc422f0e651cf204c464) |
| [nabla-c0d3/sslyze](https://github.com/nabla-c0d3/sslyze) | 3,793 | SOURCE_CHECKED_ONLY | 3.1/10 · 2026-10-12 | [3bd5094dec1d](https://github.com/nabla-c0d3/sslyze/tree/3bd5094dec1dfbaac1a03957c35ba5e487f5b890) |
| [schemathesis/schemathesis](https://github.com/schemathesis/schemathesis) | 3,681 | SOURCE_CHECKED_ONLY | 6.2/10 · 2026-10-12 | [406c7dbb105c](https://github.com/schemathesis/schemathesis/tree/406c7dbb105c8c0693096ca9a9bdd5a731b4003f) |
| [assetnote/kiterunner](https://github.com/assetnote/kiterunner) | 3,282 | SOURCE_CHECKED_ONLY | Unavailable | [7d5824cda9a2](https://github.com/assetnote/kiterunner/tree/7d5824cda9a2eef86d8d18b05b713d7e260f34d2) |
| [PortSwigger/turbo-intruder](https://github.com/PortSwigger/turbo-intruder) | 1,815 | SOURCE_CHECKED_ONLY | 2.8/10 · 2026-10-19 | [7b9d1f9db1a2](https://github.com/PortSwigger/turbo-intruder/tree/7b9d1f9db1a268aed8d62a3415e9fd52c1cecf47) |
| [doyensec/inql](https://github.com/doyensec/inql) | 1,813 | SOURCE_CHECKED_ONLY | 1.6/10 · 2026-10-12 | [00a0bd79418e](https://github.com/doyensec/inql/tree/00a0bd79418ebbee09d93550b83ba3f406a872e8) |
| [nikitastupin/clairvoyance](https://github.com/nikitastupin/clairvoyance) | 1,544 | SOURCE_CHECKED_ONLY | Unavailable | [3492afd418c5](https://github.com/nikitastupin/clairvoyance/tree/3492afd418c5761876b557f781cd387088c1af5b) |
| [PortSwigger/param-miner](https://github.com/PortSwigger/param-miner) | 1,466 | SOURCE_CHECKED_ONLY | 2.1/10 · 2026-10-19 | [e43e3b16be11](https://github.com/PortSwigger/param-miner/tree/e43e3b16be11117ed67cfde60e80acf2e95a4adc) |
| [PortSwigger/http-request-smuggler](https://github.com/PortSwigger/http-request-smuggler) | 1,249 | SOURCE_CHECKED_ONLY | Unavailable | [3ecb1afa6a1d](https://github.com/PortSwigger/http-request-smuggler/tree/3ecb1afa6a1d21ef1ec4e6eb1337818b53a2b4c0) |
| [zaproxy/zap-extensions](https://github.com/zaproxy/zap-extensions) | 955 | SOURCE_CHECKED_ONLY | 5.2/10 · 2026-10-12 | [845d3da8eac4](https://github.com/zaproxy/zap-extensions/tree/845d3da8eac45b05c17920ed10eacb32d5d994b9) |
| [PortSwigger/BChecks](https://github.com/PortSwigger/BChecks) | 794 | SOURCE_CHECKED_ONLY | Unavailable | [d4e08e3ed331](https://github.com/PortSwigger/BChecks/tree/d4e08e3ed331a34bfbb5241432bfac248629a8bb) |
| [Hackmanit/TInjA](https://github.com/Hackmanit/TInjA) | 428 | SOURCE_CHECKED_ONLY | Unavailable | [507d903e1bb2](https://github.com/Hackmanit/TInjA/tree/507d903e1bb27073418daea4b1aec146b8775f48) |
| [PortSwigger/autorize](https://github.com/PortSwigger/autorize) | 305 | SOURCE_CHECKED_ONLY | Unavailable | [6e4a7a7f44c4](https://github.com/PortSwigger/autorize/tree/6e4a7a7f44c4930b9b10d0be58ad491ba2769e4d) |

## Identity & Active Directory

| Source | Stars | Status | Scorecard / date | Reviewed pin |
| --- | ---: | --- | --- | --- |
| [fortra/impacket](https://github.com/fortra/impacket) | 16,182 | SOURCE_CHECKED_ONLY | Unavailable | [4f0348e83809](https://github.com/fortra/impacket/tree/4f0348e83809139473fd6461241bbf80d441df4b) |
| [Pennyw0rth/NetExec](https://github.com/Pennyw0rth/NetExec) | 5,939 | SOURCE_CHECKED_ONLY | Unavailable | [ae683dba107a](https://github.com/Pennyw0rth/NetExec/tree/ae683dba107a0365f79141bf4758412dbf3dc950) |
| [GhostPack/Rubeus](https://github.com/GhostPack/Rubeus) | 5,197 | SOURCE_CHECKED_ONLY | Unavailable | [74215f68ea70](https://github.com/GhostPack/Rubeus/tree/74215f68ea70bd6a66c008da91bf5fe21d20b154) |
| [GhostPack/Seatbelt](https://github.com/GhostPack/Seatbelt) | 4,741 | SOURCE_CHECKED_ONLY | 3.4/10 · 2026-10-19 | [392171df8447](https://github.com/GhostPack/Seatbelt/tree/392171df84472591d4eae7ebd5b1cdc96ba91377) |
| [ly4k/Certipy](https://github.com/ly4k/Certipy) | 3,698 | SOURCE_CHECKED_ONLY | Unavailable | [3ae34426c58d](https://github.com/ly4k/Certipy/tree/3ae34426c58d266a1979ff9607514c3d7fe1aa21) |
| [SpecterOps/BloodHound](https://github.com/SpecterOps/BloodHound) | 3,498 | SOURCE_CHECKED_ONLY | Unavailable | [41421cc5e283](https://github.com/SpecterOps/BloodHound/tree/41421cc5e28370e1feab7e454a032ba808c7cce1) |
| [ropnop/kerbrute](https://github.com/ropnop/kerbrute) | 3,475 | SOURCE_CHECKED_ONLY | 1.9/10 · 2026-10-12 | [9cfb81e4fab8](https://github.com/ropnop/kerbrute/tree/9cfb81e4fab8037acb44c678773ca3f93bc2b39c) |
| [dirkjanm/BloodHound.py](https://github.com/dirkjanm/BloodHound.py) | 2,449 | SOURCE_CHECKED_ONLY | Unavailable | [fd3f322e066d](https://github.com/dirkjanm/BloodHound.py/tree/fd3f322e066d66314bfb31d4ae6f497df5872177) |
| [lkarlslund/Adalanche](https://github.com/lkarlslund/Adalanche) | 2,215 | SOURCE_CHECKED_ONLY | Unavailable | [d75b012549d7](https://github.com/lkarlslund/Adalanche/tree/d75b012549d7bfe89324f6fd6382868dd44a90eb) |
| [ShawnDEvans/smbmap](https://github.com/ShawnDEvans/smbmap) | 2,088 | SOURCE_CHECKED_ONLY | 2.5/10 · 2026-10-19 | [31b8a8f27a32](https://github.com/ShawnDEvans/smbmap/tree/31b8a8f27a32f53ed1d63294dffd30519b79d169) |
| [GhostPack/Certify](https://github.com/GhostPack/Certify) | 2,043 | SOURCE_CHECKED_ONLY | Unavailable | [ce9a4d27d2f1](https://github.com/GhostPack/Certify/tree/ce9a4d27d2f18d391c141ebdc8cb82fa5f6b88e3) |
| [dirkjanm/krbrelayx](https://github.com/dirkjanm/krbrelayx) | 1,679 | SOURCE_CHECKED_ONLY | Unavailable | [10b45a33bc43](https://github.com/dirkjanm/krbrelayx/tree/10b45a33bc4361ec4a5546eea62db2e4244d3255) |
| [dirkjanm/ldapdomaindump](https://github.com/dirkjanm/ldapdomaindump) | 1,437 | SOURCE_CHECKED_ONLY | 2.5/10 · 2026-10-19 | [d559463eb298](https://github.com/dirkjanm/ldapdomaindump/tree/d559463eb29857f2660bf3867bfb9f8610d1ddb1) |
| [SpecterOps/SharpHound](https://github.com/SpecterOps/SharpHound) | 1,365 | SOURCE_CHECKED_ONLY | Unavailable | [85924979a9d2](https://github.com/SpecterOps/SharpHound/tree/85924979a9d23ab0e83a3fcfabee3b9962bb14be) |
| [c3c/ADExplorerSnapshot](https://github.com/c3c/ADExplorerSnapshot) | 1,106 | SOURCE_CHECKED_ONLY | Unavailable | [2f845904afec](https://github.com/c3c/ADExplorerSnapshot/tree/2f845904afecd83ca49a475e2c121c4501f94453) |
| [aniqfakhrul/powerview.py](https://github.com/aniqfakhrul/powerview.py) | 1,013 | SOURCE_CHECKED_ONLY | Unavailable | [ea133da24ac9](https://github.com/aniqfakhrul/powerview.py/tree/ea133da24ac9f51879f89a559c3fe575e3d1c801) |
| [dirkjanm/PKINITtools](https://github.com/dirkjanm/PKINITtools) | 933 | SOURCE_CHECKED_ONLY | Unavailable | [0f0cfa542b03](https://github.com/dirkjanm/PKINITtools/tree/0f0cfa542b0348609ad494713e84744234b2d3b0) |

## Cloud, containers & code security

| Source | Stars | Status | Scorecard / date | Reviewed pin |
| --- | ---: | --- | --- | --- |
| [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | 30,146 | SOURCE_CHECKED_ONLY | Unavailable | [b58d3f102cf3](https://github.com/gitleaks/gitleaks/tree/b58d3f102cf3a2c84cb7f923d05c25c9b1aed84b) |
| [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) | 28,598 | SOURCE_CHECKED_ONLY | 7.9/10 · 2026-10-12 | [e63326d6545d](https://github.com/trufflesecurity/trufflehog/tree/e63326d6545de8f425d93ce24078c6e68d83f70e) |
| [semgrep/semgrep](https://github.com/semgrep/semgrep) | 17,139 | SOURCE_CHECKED_ONLY | Unavailable | [51602ad27f09](https://github.com/semgrep/semgrep/tree/51602ad27f09ef9342a5620601de5ef8f572fbc6) |
| [prowler-cloud/prowler](https://github.com/prowler-cloud/prowler) | 15,071 | SOURCE_CHECKED_ONLY | Unavailable | [4d922da2a6a2](https://github.com/prowler-cloud/prowler/tree/4d922da2a6a29fdf49287176bae11401aaf02b75) |
| [anchore/grype](https://github.com/anchore/grype) | 13,053 | SOURCE_CHECKED_ONLY | 8.2/10 · 2026-05-18 · stale | [afe2742527d9](https://github.com/anchore/grype/tree/afe2742527d98d822da06c9f32eed86fe3d193e0) |
| [kubescape/kubescape](https://github.com/kubescape/kubescape) | 11,815 | SOURCE_CHECKED_ONLY | 7.4/10 · 2026-10-20 | [db78f2539b02](https://github.com/kubescape/kubescape/tree/db78f2539b02eca751f7aaa155443f28a31f6de5) |
| [anchore/syft](https://github.com/anchore/syft) | 9,703 | SOURCE_CHECKED_ONLY | 8.6/10 · 2026-10-12 | [f15c3343e29d](https://github.com/anchore/syft/tree/f15c3343e29dfb20cf6d82c820e7090b49808c96) |
| [bridgecrewio/checkov](https://github.com/bridgecrewio/checkov) | 9,084 | SOURCE_CHECKED_ONLY | 7/10 · 2022-11-28 · stale | [7a6782e3d81e](https://github.com/bridgecrewio/checkov/tree/7a6782e3d81e19f1bdd9213129f3138767691f5f) |
| [aquasecurity/kube-bench](https://github.com/aquasecurity/kube-bench) | 8,227 | SOURCE_CHECKED_ONLY | 5.2/10 · 2026-03-16 · stale | [e278a5915a98](https://github.com/aquasecurity/kube-bench/tree/e278a5915a982f2756026de6e2f9ca77077ef9f9) |
| [nccgroup/ScoutSuite](https://github.com/nccgroup/ScoutSuite) | 7,856 | SOURCE_CHECKED_ONLY | 4/10 · 2026-10-12 | [7909f2fc6186](https://github.com/nccgroup/ScoutSuite/tree/7909f2fc6186063e5c9e7ddef8c4d7d1072c8f3d) |
| [ossf/scorecard](https://github.com/ossf/scorecard) | 5,769 | SOURCE_CHECKED_ONLY | 8.3/10 · 2026-10-19 | [6d4113e03c00](https://github.com/ossf/scorecard/tree/6d4113e03c0014d63613b65b26a0c5a14c98ce3f) |
| [RhinoSecurityLabs/pacu](https://github.com/RhinoSecurityLabs/pacu) | 5,364 | SOURCE_CHECKED_ONLY | 4/10 · 2026-10-19 | [e597f23ecfb8](https://github.com/RhinoSecurityLabs/pacu/tree/e597f23ecfb88b82f706c5f0cac9d4577c2af262) |
| [aquasecurity/kube-hunter](https://github.com/aquasecurity/kube-hunter) | 5,086 | SOURCE_CHECKED_ONLY | 3.7/10 · 2026-03-16 · stale | [bc47f08e88ea](https://github.com/aquasecurity/kube-hunter/tree/bc47f08e88ea2a5fb059bf3b8a8edb1aefb4c6cc) |
| [rhysd/actionlint](https://github.com/rhysd/actionlint) | 4,338 | SOURCE_CHECKED_ONLY | 3.6/10 · 2026-10-12 | [011a6d15e749](https://github.com/rhysd/actionlint/tree/011a6d15e749bb3f2d771eed9c7aa0e7e3e10ee7) |
| [BishopFox/cloudfox](https://github.com/BishopFox/cloudfox) | 2,601 | SOURCE_CHECKED_ONLY | Unavailable | [d44899f21302](https://github.com/BishopFox/cloudfox/tree/d44899f21302269fc5e7743c662edafe15c7575c) |

## Mobile & instrumentation

| Source | Stars | Status | Scorecard / date | Reviewed pin |
| --- | ---: | --- | --- | --- |
| [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 152,585 | SOURCE_CHECKED_ONLY | 4.1/10 · 2026-10-19 | [a60891aea193](https://github.com/Genymobile/scrcpy/tree/a60891aea193d92e7e5c3942700eca63f9d19a5f) |
| [skylot/jadx](https://github.com/skylot/jadx) | 51,117 | SOURCE_CHECKED_ONLY | 4.7/10 · 2026-10-12 | [c4c45fde27b4](https://github.com/skylot/jadx/tree/c4c45fde27b4f3386dc2ff016ff187229a60a716) |
| [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) | 26,254 | SOURCE_CHECKED_ONLY | 5.1/10 · 2026-10-19 | [fd9d5d4dc7e4](https://github.com/iBotPeaches/Apktool/tree/fd9d5d4dc7e45fa7f984698ded7a03c554d0a7b3) |
| [frida/frida](https://github.com/frida/frida) | 22,383 | SOURCE_CHECKED_ONLY | 3.8/10 · 2026-10-19 | [adf8be5f5b7f](https://github.com/frida/frida/tree/adf8be5f5b7f3840521783b628a191b62d7e6f66) |
| [MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | 21,996 | SOURCE_CHECKED_ONLY | 6.8/10 · 2026-10-19 | [08872c8454e5](https://github.com/MobSF/Mobile-Security-Framework-MobSF/tree/08872c8454e59f8a6347c35b46852c9929f5eb5e) |
| [google/oss-fuzz](https://github.com/google/oss-fuzz) | 12,755 | SOURCE_CHECKED_ONLY | 6.8/10 · 2026-10-12 | [6e2d4a84b25b](https://github.com/google/oss-fuzz/tree/6e2d4a84b25ba47ea6042a06af2c284be1a64124) |
| [ashishb/android-security-awesome](https://github.com/ashishb/android-security-awesome) | 9,768 | SOURCE_CHECKED_ONLY | 6.4/10 · 2026-10-12 | [b21a710ccf4b](https://github.com/ashishb/android-security-awesome/tree/b21a710ccf4b6dbd470933105f5d53e9ca5663e0) |
| [sensepost/objection](https://github.com/sensepost/objection) | 9,452 | SOURCE_CHECKED_ONLY | 4.4/10 · 2026-10-12 | [35c4e2c9e68a](https://github.com/sensepost/objection/tree/35c4e2c9e68a0354b21db4833252e0c4acd5bd28) |
| [r0ysue/r0capture](https://github.com/r0ysue/r0capture) | 7,792 | SOURCE_CHECKED_ONLY | Unavailable | [3e4e9f9765c4](https://github.com/r0ysue/r0capture/tree/3e4e9f9765c4e1d06c17e3a24bf64189de498eb0) |
| [ReversecLabs/drozer](https://github.com/ReversecLabs/drozer) | 4,640 | SOURCE_CHECKED_ONLY | Unavailable | [d992f6378d42](https://github.com/ReversecLabs/drozer/tree/d992f6378d42680ea96ee03eff4117f150e1049c) |
| [httptoolkit/httptoolkit](https://github.com/httptoolkit/httptoolkit) | 3,656 | SOURCE_CHECKED_ONLY | Unavailable | [bb579a8ceadf](https://github.com/httptoolkit/httptoolkit/tree/bb579a8ceadfe86b98160843c0447a5b9eec554f) |
| [patrickfav/uber-apk-signer](https://github.com/patrickfav/uber-apk-signer) | 2,784 | SOURCE_CHECKED_ONLY | Unavailable | [76cbf02556b4](https://github.com/patrickfav/uber-apk-signer/tree/76cbf02556b4454f4c2bd6c908b4355003c4e37d) |
| [Ch0pin/medusa](https://github.com/Ch0pin/medusa) | 2,358 | SOURCE_CHECKED_ONLY | Unavailable | [a7bd929f297f](https://github.com/Ch0pin/medusa/tree/a7bd929f297f0725a5e4d2e3952874a757d4e2fc) |
| [googleprojectzero/fuzzilli](https://github.com/googleprojectzero/fuzzilli) | 2,358 | SOURCE_CHECKED_ONLY | 4.7/10 · 2026-10-12 | [be2811d00282](https://github.com/googleprojectzero/fuzzilli/tree/be2811d00282320381fc8007d64873745772011d) |
| [MobSF/mobsfscan](https://github.com/MobSF/mobsfscan) | 793 | SOURCE_CHECKED_ONLY | 6.5/10 · 2026-10-19 | [4645ea70bc09](https://github.com/MobSF/mobsfscan/tree/4645ea70bc093268502fe9f6df93e41bb482254a) |
| [frida/frida-tools](https://github.com/frida/frida-tools) | 533 | SOURCE_CHECKED_ONLY | Unavailable | [330ed423f71b](https://github.com/frida/frida-tools/tree/330ed423f71b7797e4be1821795463728430b43e) |
| [kalilinux/nethunter/apps/kali-nethunter-app](https://gitlab.com/kalilinux/nethunter/apps/kali-nethunter-app) | 150 | SOURCE_CHECKED_ONLY | Unavailable | [b57348d6fbe8](https://gitlab.com/kalilinux/nethunter/apps/kali-nethunter-app/-/tree/b57348d6fbe8cc13170bfe10bcac6a82c1e42e14) |
| [kalilinux/nethunter/build-scripts/kali-nethunter-installer](https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-installer) | 39 | SOURCE_CHECKED_ONLY | Unavailable | [e63b0476a7fd](https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-installer/-/tree/e63b0476a7fd5767729208c68a78ad79afaaf556) |

## Network & traffic

| Source | Stars | Status | Scorecard / date | Reviewed pin |
| --- | ---: | --- | --- | --- |
| [fatedier/frp](https://github.com/fatedier/frp) | 110,009 | SOURCE_CHECKED_ONLY | 5.3/10 · 2026-10-12 | [b0bf32571a3d](https://github.com/fatedier/frp/tree/b0bf32571a3d4d4f9bb77223ce0d0e5d32ea1216) |
| [curl/curl](https://github.com/curl/curl) | 43,180 | SOURCE_CHECKED_ONLY | 9/10 · 2026-10-19 | [eb2b201a2da3](https://github.com/curl/curl/tree/eb2b201a2da3bfc6fefd7ff2d8e476e3cb9e5bcb) |
| [robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) | 26,085 | SOURCE_CHECKED_ONLY | 5.5/10 · 2026-10-12 | [8e6b3b0c07a8](https://github.com/robertdavidgraham/masscan/tree/8e6b3b0c07a81e8ea61d557c06134a21a6881614) |
| [bettercap/bettercap](https://github.com/bettercap/bettercap) | 20,166 | SOURCE_CHECKED_ONLY | 4.9/10 · 2026-10-12 | [8eca2820f3c4](https://github.com/bettercap/bettercap/tree/8eca2820f3c41d2004434ed5a291d87462caeeb7) |
| [jpillora/chisel](https://github.com/jpillora/chisel) | 16,670 | SOURCE_CHECKED_ONLY | 5.9/10 · 2026-10-12 | [5ee6c74d60d9](https://github.com/jpillora/chisel/tree/5ee6c74d60d96a75afb18bc866eb19327170aeed) |
| [evilsocket/opensnitch](https://github.com/evilsocket/opensnitch) | 14,183 | SOURCE_CHECKED_ONLY | 4.2/10 · 2026-10-12 | [a1353848ba1b](https://github.com/evilsocket/opensnitch/tree/a1353848ba1b660320e90cefea782c3fba272c00) |
| [nmap/nmap](https://github.com/nmap/nmap) | 13,829 | SOURCE_CHECKED_ONLY | 4.2/10 · 2026-10-12 | [01f4ed2968f6](https://github.com/nmap/nmap/tree/01f4ed2968f6ee09e487e67609e9ef037ffe4092) |
| [sshuttle/sshuttle](https://github.com/sshuttle/sshuttle) | 13,616 | SOURCE_CHECKED_ONLY | 6.9/10 · 2026-10-12 | [6954af07f4ba](https://github.com/sshuttle/sshuttle/tree/6954af07f4ba8683f6797534f453ba863d354049) |
| [secdev/scapy](https://github.com/secdev/scapy) | 12,631 | SOURCE_CHECKED_ONLY | 8.2/10 · 2026-10-12 | [9aa380f694e0](https://github.com/secdev/scapy/tree/9aa380f694e0f32788fa701857cef17970b7b8c1) |
| [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) | 7,787 | SOURCE_CHECKED_ONLY | 6/10 · 2026-10-12 | [7e2256f38f35](https://github.com/aircrack-ng/aircrack-ng/tree/7e2256f38f3590af4c19a6ae14ed79bab02242e6) |
| [nicocha30/ligolo-ng](https://github.com/nicocha30/ligolo-ng) | 5,109 | SOURCE_CHECKED_ONLY | Unavailable | [e543732f4be6](https://github.com/nicocha30/ligolo-ng/tree/e543732f4be6dc899096ae322ae620bf010bfbfc) |
| [jtesta/ssh-audit](https://github.com/jtesta/ssh-audit) | 4,327 | SOURCE_CHECKED_ONLY | 3.8/10 · 2026-10-19 | [1df77bfbb664](https://github.com/jtesta/ssh-audit/tree/1df77bfbb664ec435cd662b938c1080012df3354) |
| [the-tcpdump-group/tcpdump](https://github.com/the-tcpdump-group/tcpdump) | 3,246 | SOURCE_CHECKED_ONLY | 4.2/10 · 2026-10-12 | [35f39fa1b238](https://github.com/the-tcpdump-group/tcpdump/tree/35f39fa1b238e51ebc1a139102e5fc00f2a82ffd) |
| [wireshark/wireshark](https://gitlab.com/wireshark/wireshark) | 1,653 | SOURCE_CHECKED_ONLY | Unavailable | [f2c97e2b22bd](https://gitlab.com/wireshark/wireshark/-/tree/f2c97e2b22bdcaa9982b8dd61b4401530f29c8fb) |

## Red team & adversary emulation

| Source | Stars | Status | Scorecard / date | Reviewed pin |
| --- | ---: | --- | --- | --- |
| [rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework) | 39,189 | SOURCE_CHECKED_ONLY | 4.8/10 · 2026-10-12 | [1e321cedaf4c](https://github.com/rapid7/metasploit-framework/tree/1e321cedaf4c2a3f92de6a21b2f7d4b8eff31ca4) |
| [BishopFox/sliver](https://github.com/BishopFox/sliver) | 12,146 | SOURCE_CHECKED_ONLY | 5.9/10 · 2026-10-19 | [5383bd67b526](https://github.com/BishopFox/sliver/tree/5383bd67b526b4a8425d9bd699a53eb3a18b1255) |
| [apache/caldera](https://github.com/apache/caldera) | 7,453 | SOURCE_CHECKED_ONLY | Unavailable | [cb8d6a8160e0](https://github.com/apache/caldera/tree/cb8d6a8160e0f4990af323a7c071d5e8482b42c7) |
| [lanmaster53/recon-ng](https://github.com/lanmaster53/recon-ng) | 6,004 | SOURCE_CHECKED_ONLY | 2.2/10 · 2026-10-12 | [32b08fe7b699](https://github.com/lanmaster53/recon-ng/tree/32b08fe7b6993ca1f2d8f76ba8f5d23c7f34a11d) |
| [trustedsec/ptf](https://github.com/trustedsec/ptf) | 5,580 | SOURCE_CHECKED_ONLY | 3.2/10 · 2026-10-12 | [74f58d6b6557](https://github.com/trustedsec/ptf/tree/74f58d6b6557de115d0286a5d5c1849ba6048258) |
| [BC-SECURITY/Empire](https://github.com/BC-SECURITY/Empire) | 5,336 | SOURCE_CHECKED_ONLY | Unavailable | [33e2b4bbd0f3](https://github.com/BC-SECURITY/Empire/tree/33e2b4bbd0f31308a63d889fd96d8c8fe9c2c12f) |
| [its-a-feature/Mythic](https://github.com/its-a-feature/Mythic) | 4,845 | SOURCE_CHECKED_ONLY | Unavailable | [96b24b48a7f2](https://github.com/its-a-feature/Mythic/tree/96b24b48a7f26594f1126eabef8ad00301ba28a0) |
| [cobbr/Covenant](https://github.com/cobbr/Covenant) | 4,746 | SOURCE_CHECKED_ONLY | 0.5/10 · 2026-10-12 | [5decc3ccfab0](https://github.com/cobbr/Covenant/tree/5decc3ccfab04e6e881ed00c9de649740dac8ad1) |

## Reverse engineering & vulnerability research

| Source | Stars | Status | Scorecard / date | Reviewed pin |
| --- | ---: | --- | --- | --- |
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | 91,728 | SOURCE_CHECKED_ONLY | 3.7/10 · 2026-10-19 | [c91ec18e6780](https://github.com/NationalSecurityAgency/ghidra/tree/c91ec18e6780a8a531a806a0660a9c28978a99a0) |
| [x64dbg/x64dbg](https://github.com/x64dbg/x64dbg) | 49,962 | SOURCE_CHECKED_ONLY | 3.8/10 · 2026-10-12 | [c44297200731](https://github.com/x64dbg/x64dbg/tree/c44297200731995c51dbc75ab3098e2f0094b282) |
| [radareorg/radare2](https://github.com/radareorg/radare2) | 25,103 | SOURCE_CHECKED_ONLY | 5.5/10 · 2026-10-12 | [8b507e97e51f](https://github.com/radareorg/radare2/tree/8b507e97e51f4017e54def231cc6925e9afec333) |
| [rizinorg/cutter](https://github.com/rizinorg/cutter) | 20,062 | SOURCE_CHECKED_ONLY | 5.5/10 · 2026-10-12 | [d7f11b220884](https://github.com/rizinorg/cutter/tree/d7f11b220884a6cc8549da955b744bd318645103) |
| [Gallopsled/pwntools](https://github.com/Gallopsled/pwntools) | 13,787 | SOURCE_CHECKED_ONLY | 4.8/10 · 2026-10-19 | [99a4fe5596bc](https://github.com/Gallopsled/pwntools/tree/99a4fe5596bcba851537fdbe821ceb5fb80c4de1) |
| [pwndbg/pwndbg](https://github.com/pwndbg/pwndbg) | 11,083 | SOURCE_CHECKED_ONLY | 4.8/10 · 2026-10-12 | [d887a5c04b10](https://github.com/pwndbg/pwndbg/tree/d887a5c04b10eb36637600185775064d3c2904e1) |
| [VirusTotal/yara](https://github.com/VirusTotal/yara) | 9,959 | SOURCE_CHECKED_ONLY | 5/10 · 2026-10-12 | [5cd1e8b64082](https://github.com/VirusTotal/yara/tree/5cd1e8b64082c0e0ddce2ad1e1748df41700ab9e) |
| [unicorn-engine/unicorn](https://github.com/unicorn-engine/unicorn) | 9,472 | SOURCE_CHECKED_ONLY | 3.9/10 · 2026-10-12 | [7c5db94191de](https://github.com/unicorn-engine/unicorn/tree/7c5db94191defc1e04a4f66f4eb1220903cba837) |
| [angr/angr](https://github.com/angr/angr) | 9,222 | SOURCE_CHECKED_ONLY | 5.5/10 · 2026-10-12 | [16245f07bc53](https://github.com/angr/angr/tree/16245f07bc53b52bd75cbfd738bb4cadba7b6174) |
| [hugsy/gef](https://github.com/hugsy/gef) | 8,404 | SOURCE_CHECKED_ONLY | 4.3/10 · 2026-10-12 | [49c07dc60624](https://github.com/hugsy/gef/tree/49c07dc60624f264d40b5c6ea39b2bf3a4e9958f) |
| [AFLplusplus/AFLplusplus](https://github.com/AFLplusplus/AFLplusplus) | 6,816 | SOURCE_CHECKED_ONLY | 5.5/10 · 2026-10-12 | [d0070729206a](https://github.com/AFLplusplus/AFLplusplus/tree/d0070729206a80a9af297b2341edd63f68fdac35) |
| [mandiant/capa](https://github.com/mandiant/capa) | 6,257 | SOURCE_CHECKED_ONLY | 7.1/10 · 2026-10-16 | [7a235c46965e](https://github.com/mandiant/capa/tree/7a235c46965ea0965c65be3b9ee1e21dca686f3d) |
| [lief-project/LIEF](https://github.com/lief-project/LIEF) | 5,598 | SOURCE_CHECKED_ONLY | 3.8/10 · 2026-10-12 | [80cf4a582cd7](https://github.com/lief-project/LIEF/tree/80cf4a582cd7afc486cc3791e30775517c71b579) |
| [Yara-Rules/rules](https://github.com/Yara-Rules/rules) | 4,925 | SOURCE_CHECKED_ONLY | 3.1/10 · 2026-10-12 | [0f93570194a8](https://github.com/Yara-Rules/rules/tree/0f93570194a80d2f2032869055808b0ddcdfb360) |
| [googleprojectzero/winafl](https://github.com/googleprojectzero/winafl) | 2,614 | SOURCE_CHECKED_ONLY | 3.4/10 · 2026-10-12 | [fd85f38548b1](https://github.com/googleprojectzero/winafl/tree/fd85f38548b14352f4b70ad414f364ea6dc1a769) |
| [exploit-database/exploitdb](https://gitlab.com/exploit-database/exploitdb) | 263 | SOURCE_CHECKED_ONLY | Unavailable | [12879ca774a9](https://gitlab.com/exploit-database/exploitdb/-/tree/12879ca774a9d7543907d24a7bc1cebb47959afe) |

## Wordlists & test data

| Source | Stars | Status | Scorecard / date | Reviewed pin |
| --- | ---: | --- | --- | --- |
| [danielmiessler/SecLists](https://github.com/danielmiessler/SecLists) | 74,227 | SOURCE_CHECKED_ONLY | 4.2/10 · 2026-10-12 | [75064ac792b5](https://github.com/danielmiessler/SecLists/tree/75064ac792b5b554d17386abae3f0e38db7f923c) |
| [fuzzdb-project/fuzzdb](https://github.com/fuzzdb-project/fuzzdb) | 9,004 | SOURCE_CHECKED_ONLY | 1.8/10 · 2026-10-12 | [5656ab25dc6b](https://github.com/fuzzdb-project/fuzzdb/tree/5656ab25dc6bb43bae32236fab775658a90d7380) |
| [1N3/IntruderPayloads](https://github.com/1N3/IntruderPayloads) | 3,988 | SOURCE_CHECKED_ONLY | Unavailable | [9b84328441e0](https://github.com/1N3/IntruderPayloads/tree/9b84328441e0b1d5b63764941bfd72a2460dba5d) |
| [assetnote/wordlists](https://github.com/assetnote/wordlists) | 1,743 | SOURCE_CHECKED_ONLY | Unavailable | [6dea231f4cbd](https://github.com/assetnote/wordlists/tree/6dea231f4cbd356a637851b1c13b83de4da00adb) |

## AI security & automation

| Source | Stars | Status | Scorecard / date | Reviewed pin |
| --- | ---: | --- | --- | --- |
| [usestrix/strix](https://github.com/usestrix/strix) | 70,166 | REVIEW_AGENT | Unavailable | [a0f8ea2cd379](https://github.com/usestrix/strix/tree/a0f8ea2cd379c4bf56e665d3db2ba8a4f7c0683c) |
| [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | 49,125 | REVIEW_AGENT | Unavailable | [4bd88c12a909](https://github.com/KeygraphHQ/shannon/tree/4bd88c12a9096d0b78ceb2828729d12dca70fa60) |
| [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) | 44,376 | REVIEW_AGENT | Unavailable | [05119078c104](https://github.com/danielmiessler/Fabric/tree/05119078c104142d8bde2d8984e7af388d55d404) |
| [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | 31,386 | REVIEW_AGENT | Unavailable | [843dfeb4bfc8](https://github.com/vxcontrol/pentagi/tree/843dfeb4bfc809c09d1bc5022e567c602d8fc9dd) |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 26,166 | REVIEW_AGENT | Unavailable | [b49d55dfdec2](https://github.com/promptfoo/promptfoo/tree/b49d55dfdec226bb299afee253122879570cc536) |
| [GreyDGL/PentestGPT](https://github.com/GreyDGL/PentestGPT) | 16,037 | REVIEW_AGENT | Unavailable | [e8b1bb77d1ac](https://github.com/GreyDGL/PentestGPT/tree/e8b1bb77d1ac00329675cec3b060aba971ec1ac8) |
| [NVIDIA/garak](https://github.com/NVIDIA/garak) | 9,623 | REVIEW_AGENT | Unavailable | [cc1215c5c301](https://github.com/NVIDIA/garak/tree/cc1215c5c301a69f115b0b2b7ef8e4172ae2e7fc) |
| [trailofbits/skills](https://github.com/trailofbits/skills) | 7,652 | REVIEW_AGENT | Unavailable | [5c99c03fb8a9](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0) |
| [Giskard-AI/giskard-oss](https://github.com/Giskard-AI/giskard-oss) | 5,911 | REVIEW_AGENT | Unavailable | [042ed8716264](https://github.com/Giskard-AI/giskard-oss/tree/042ed87162641dcb1512b02fe57054667a28cf9d) |
| [microsoft/PyRIT](https://github.com/microsoft/PyRIT) | 4,659 | REVIEW_AGENT | Unavailable | [85d4f0c398bf](https://github.com/microsoft/PyRIT/tree/85d4f0c398bfd1bf3f09e1a56ddf3ee65caf054b) |
| [meta-llama/PurpleLlama](https://github.com/meta-llama/PurpleLlama) | 4,440 | REVIEW_AGENT | 5.9/10 · 2026-10-12 | [d934ea285d12](https://github.com/meta-llama/PurpleLlama/tree/d934ea285d124d81c10f7e15a06a1e1f74eff2c3) |
| [trailofbits/buttercup](https://github.com/trailofbits/buttercup) | 1,726 | REVIEW_AGENT | Unavailable | [298c01fbff3b](https://github.com/trailofbits/buttercup/tree/298c01fbff3bf0bf166c87856acd7e42f94f7157) |
| [six2dez/burp-ai-agent](https://github.com/six2dez/burp-ai-agent) | 1,547 | REVIEW_AGENT | Unavailable | [1718308d8d86](https://github.com/six2dez/burp-ai-agent/tree/1718308d8d864b94c8347ec537e301a9cbb5d5ac) |
| [PortSwigger/mcp-server](https://github.com/PortSwigger/mcp-server) | 1,245 | REVIEW_AGENT | Unavailable | [642e6fa31c63](https://github.com/PortSwigger/mcp-server/tree/642e6fa31c63db3886a353fcd7ed62037e0ceed5) |
| [ethz-spylab/agentdojo](https://github.com/ethz-spylab/agentdojo) | 939 | REVIEW_AGENT | Unavailable | [089ed468cf3e](https://github.com/ethz-spylab/agentdojo/tree/089ed468cf3ed0322acc66b0211f26d9d90dbf60) |
| [dreadnode/rigging](https://github.com/dreadnode/rigging) | 421 | REVIEW_AGENT | Unavailable | [3461e81e799a](https://github.com/dreadnode/rigging/tree/3461e81e799aff9040fe0d0671196b78667a7589) |
| [GitHubSecurityLab/seclab-taskflow-agent](https://github.com/GitHubSecurityLab/seclab-taskflow-agent) | 279 | REVIEW_AGENT | Unavailable | [ab02b1fe8ac3](https://github.com/GitHubSecurityLab/seclab-taskflow-agent/tree/ab02b1fe8ac3d94352332b2c739c579f0d5ae810) |

## Reporting & workflow

| Source | Stars | Status | Scorecard / date | Reviewed pin |
| --- | ---: | --- | --- | --- |
| [infobyte/faraday](https://github.com/infobyte/faraday) | 6,807 | SOURCE_CHECKED_ONLY | 3.6/10 · 2026-10-12 | [ad91a06cc0f9](https://github.com/infobyte/faraday/tree/ad91a06cc0f9adfec2eda83622c62b8637df99a4) |
| [giuspen/cherrytree](https://github.com/giuspen/cherrytree) | 3,974 | SOURCE_CHECKED_ONLY | 4.2/10 · 2026-10-19 | [44aee2c96c17](https://github.com/giuspen/cherrytree/tree/44aee2c96c1725e896138e6c786522e303dab55d) |
| [Syslifters/sysreptor](https://github.com/Syslifters/sysreptor) | 2,604 | SOURCE_CHECKED_ONLY | Unavailable | [7b742e0848ce](https://github.com/Syslifters/sysreptor/tree/7b742e0848ce3f434ad22e2d5f35f0b38ee28aab) |
| [reportportal/reportportal](https://github.com/reportportal/reportportal) | 2,040 | SOURCE_CHECKED_ONLY | 6.2/10 · 2026-10-12 | [e0bb071de9c0](https://github.com/reportportal/reportportal/tree/e0bb071de9c07dfc4c3ddaf55de621853feccf2b) |
| [GhostManager/Ghostwriter](https://github.com/GhostManager/Ghostwriter) | 1,945 | SOURCE_CHECKED_ONLY | 4.7/10 · 2026-10-19 | [f38174bb6ee4](https://github.com/GhostManager/Ghostwriter/tree/f38174bb6ee4ead86b8039abb1f7742ae8b97242) |
| [dradis/dradis-ce](https://github.com/dradis/dradis-ce) | 843 | SOURCE_CHECKED_ONLY | 6.7/10 · 2026-10-19 | [0c85e061127f](https://github.com/dradis/dradis-ce/tree/0c85e061127f6da8c1d0bd62facbfa4768d782f1) |

## Practice labs

| Source | Stars | Status | Scorecard / date | Reviewed pin |
| --- | ---: | --- | --- | --- |
| [vulhub/vulhub](https://github.com/vulhub/vulhub) | 21,370 | ISOLATED_LAB | 3.6/10 · 2026-10-12 | [9b90d4276f84](https://github.com/vulhub/vulhub/tree/9b90d4276f84feed6333286afeb7e1250379a1da) |
| [juice-shop/juice-shop](https://github.com/juice-shop/juice-shop) | 14,180 | ISOLATED_LAB | Unavailable | [399fba761943](https://github.com/juice-shop/juice-shop/tree/399fba76194305a312693eee44f4df64bdf0c3ce) |
| [digininja/DVWA](https://github.com/digininja/DVWA) | 13,870 | ISOLATED_LAB | 5.8/10 · 2026-10-12 | [a1978a2fed19](https://github.com/digininja/DVWA/tree/a1978a2fed195acd093010af6395f86a281537ca) |
| [WebGoat/WebGoat](https://github.com/WebGoat/WebGoat) | 9,422 | ISOLATED_LAB | 4.1/10 · 2026-10-12 | [e7b131360d74](https://github.com/WebGoat/WebGoat/tree/e7b131360d74336c0c94ab5c8a21259503f59be8) |
| [Orange-Cyberdefense/GOAD](https://github.com/Orange-Cyberdefense/GOAD) | 8,511 | ISOLATED_LAB | Unavailable | [992307adf944](https://github.com/Orange-Cyberdefense/GOAD/tree/992307adf944b934a3b76a2f56a637104c54b805) |
| [RhinoSecurityLabs/cloudgoat](https://github.com/RhinoSecurityLabs/cloudgoat) | 3,761 | ISOLATED_LAB | Unavailable | [63c65bd26edc](https://github.com/RhinoSecurityLabs/cloudgoat/tree/63c65bd26edc6919499adfa20b176c450e35c33c) |
| [OWASP/crAPI](https://github.com/OWASP/crAPI) | 1,609 | ISOLATED_LAB | Unavailable | [b5fc307f3e5f](https://github.com/OWASP/crAPI/tree/b5fc307f3e5f875809b095b771108ef342a33724) |
| [kalilinux/build-scripts/kali-live](https://gitlab.com/kalilinux/build-scripts/kali-live) | 80 | SOURCE_CHECKED_ONLY | Unavailable | [adb2e3894166](https://gitlab.com/kalilinux/build-scripts/kali-live/-/tree/adb2e38941662f105b57134e0155ec468da294ad) |
