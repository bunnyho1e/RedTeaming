# Source review — dated observations

**252 active source projects; 9 excluded source identities.**

[RedOS batch review](REDOS_REVIEW.md) · [Full evidence](source-review.json) · [Exclusions](EXCLUDED.md)

The original 193 observations are retained from 2026-10-20, including their OSV/Scorecard dates and statuses. They were not silently re-audited or re-pinned during the RedOS update. The 59 new observations are dated 2026-10-21 and use the scoped methods recorded in [redos-source-review.json](redos-source-review.json).

No upstream tool, installer, exploit, module or container was installed or executed. Git source retrieval and text inspection do not establish that code is malware-free. OSV can lack records for a vulnerable project or an unindexed commit; an empty result is not a clean bill of health. Cached Scorecard data in the older evidence can describe another commit and is not a malware detector.

The original `REVIEW_AGENT` and `ISOLATED_LAB` classifications remain. `SOURCE_CHECKED_ONLY` and `SOURCE_SCREENED_ONLY` permit source inclusion in this catalog, not execution approval. Dependencies, release binaries, full-code audits and VM-wide scans are outside this screen.

## Playbooks & knowledge

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [0x4D31/awesome-threat-detection](https://github.com/0x4D31/awesome-threat-detection) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [f1e6a1528c26](https://github.com/0x4D31/awesome-threat-detection/tree/f1e6a1528c2690d02fa87a97c860235eabc34639) |
| [bugcrowd/HUNT](https://github.com/bugcrowd/HUNT) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [5ba4dccff3bd](https://github.com/bugcrowd/HUNT/tree/5ba4dccff3bd98c7ca0a7024e5cff8aaf0afbd5d) |
| [enaqx/awesome-pentest](https://github.com/enaqx/awesome-pentest) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [d70480bad202](https://github.com/enaqx/awesome-pentest/tree/d70480bad2020b90299363ccb0ebf65fb75653d7) |
| [GTFOBins/GTFOBins.github.io](https://github.com/GTFOBins/GTFOBins.github.io) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [acd524623f9c](https://github.com/GTFOBins/GTFOBins.github.io/tree/acd524623f9c406acedd2754ebd9c2431f3675ad) |
| [HackTricks-wiki/hacktricks](https://github.com/HackTricks-wiki/hacktricks) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [98ca040281bf](https://github.com/HackTricks-wiki/hacktricks/tree/98ca040281bfaa87a4555ab2eeb75db983fa94bb) |
| [infosecn1nja/Red-Teaming-Toolkit](https://github.com/infosecn1nja/Red-Teaming-Toolkit) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [053fe2ee2e76](https://github.com/infosecn1nja/Red-Teaming-Toolkit/tree/053fe2ee2e764cdcddd6f08820a4194db5cbd0a8) |
| [LOLBAS-Project/LOLBAS](https://github.com/LOLBAS-Project/LOLBAS) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [2056cb766250](https://github.com/LOLBAS-Project/LOLBAS/tree/2056cb7662509dc998fc6ce79636aec4e6c0397f) |
| [OWASP/ASVS](https://github.com/OWASP/ASVS) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [2b47a9dd1676](https://github.com/OWASP/ASVS/tree/2b47a9dd16760ee484a6672d197f1f7e25d9c632) |
| [OWASP/mastg](https://github.com/OWASP/mastg) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [02ffd85fb743](https://github.com/OWASP/mastg/tree/02ffd85fb74383ec2a30b42866d38f89d72c0ead) |
| [OWASP/masvs](https://github.com/OWASP/masvs) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [bbe226fd17e6](https://github.com/OWASP/masvs/tree/bbe226fd17e6dab51927f392936deef31c816423) |
| [OWASP/wstg](https://github.com/OWASP/wstg) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [0dfbd5a585a5](https://github.com/OWASP/wstg/tree/0dfbd5a585a503e27761b8f6c8bd8caf0903c8e8) |
| [OWASP/www-project-api-security](https://github.com/OWASP/www-project-api-security) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [c144e52e4e4f](https://github.com/OWASP/www-project-api-security/tree/c144e52e4e4f8c47c7e0343ff0411c3c615ebec0) |
| [peass-ng/PEASS-ng](https://github.com/peass-ng/PEASS-ng) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [2d186bd98a4a](https://github.com/peass-ng/PEASS-ng/tree/2d186bd98a4a0f5a8c5e9d203cb550c710a88a02) |
| [redcanaryco/atomic-red-team](https://github.com/redcanaryco/atomic-red-team) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [388942adbd96](https://github.com/redcanaryco/atomic-red-team/tree/388942adbd9641f4dfdcf079d7efe9a75ec0ac43) |
| [s0md3v/AwesomeXSS](https://github.com/s0md3v/AwesomeXSS) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [9982704e7c62](https://github.com/s0md3v/AwesomeXSS/tree/9982704e7c6217a74463d187c5a6258b9343eaa9) |
| [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [3ac27901c711](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/3ac27901c711bdf3f5b65a7b1d1820a1f65bd09a) |
| [The-Art-of-Hacking/h4cker](https://github.com/The-Art-of-Hacking/h4cker) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [cbf27e671dae](https://github.com/The-Art-of-Hacking/h4cker/tree/cbf27e671daea238e9f05a81fb8354357437c08a) |
| [trailofbits/awesome-ml-security](https://github.com/trailofbits/awesome-ml-security) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [d7fe4fa91719](https://github.com/trailofbits/awesome-ml-security/tree/d7fe4fa917192dba20051741d357c939c709a1e3) |
| [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [7d37069a361d](https://github.com/trimstray/the-book-of-secret-knowledge/tree/7d37069a361d3fd9f214480755f7969744e866fa) |
| [exploit-database/exploitdb-papers](https://gitlab.com/exploit-database/exploitdb-papers) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [d79ce5ad128f](https://gitlab.com/exploit-database/exploitdb-papers/-/tree/d79ce5ad128f48f222ce4e659d0924eb0d06a1db) |

## Recon & attack surface

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [blacklanternsecurity/bbot](https://github.com/blacklanternsecurity/bbot) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [a6fb827bb144](https://github.com/blacklanternsecurity/bbot/tree/a6fb827bb144cdb85b52e142a4d6e14ed5f94b69) |
| [d3mondev/puredns](https://github.com/d3mondev/puredns) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [46bd4c963ec2](https://github.com/d3mondev/puredns/tree/46bd4c963ec2b28c5241c03c161bdc41bb93fdc0) |
| [darkoperator/dnsrecon](https://github.com/darkoperator/dnsrecon) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [13c47504dedd](https://github.com/darkoperator/dnsrecon/tree/13c47504dedd4203610f407ef9619fc085a2df97) |
| [exiftool/exiftool](https://github.com/exiftool/exiftool) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [2200871d9cef](https://github.com/exiftool/exiftool/tree/2200871d9cef988051d2a99d67df3bda6cbb30a8) |
| [Findomain/Findomain](https://github.com/Findomain/Findomain) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [cc5f40c03fcc](https://github.com/Findomain/Findomain/tree/cc5f40c03fcc20d8b31e263dc5d4c0b22edfaad7) |
| [guelfoweb/knockpy](https://github.com/guelfoweb/knockpy) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [da43fdd2399f](https://github.com/guelfoweb/knockpy/tree/da43fdd2399f9ca5a39229cb8ba3e51249f53e30) |
| [laramies/theHarvester](https://github.com/laramies/theHarvester) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [8c72cbf331c2](https://github.com/laramies/theHarvester/tree/8c72cbf331c28629706cd9b6be91da62424ddcd9) |
| [lc/gau](https://github.com/lc/gau) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [4eabace30987](https://github.com/lc/gau/tree/4eabace309877abb231def9eeb27b96c07ed3635) |
| [mschwager/fierce](https://github.com/mschwager/fierce) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [965840d51610](https://github.com/mschwager/fierce/tree/965840d516102bc71157d256b708b96d45a1368d) |
| [owasp-amass/amass](https://github.com/owasp-amass/amass) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [79299dce87b0](https://github.com/owasp-amass/amass/tree/79299dce87b0085db0f2f4ef3e9c52cccb49f514) |
| [projectdiscovery/alterx](https://github.com/projectdiscovery/alterx) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [3322e4f82614](https://github.com/projectdiscovery/alterx/tree/3322e4f82614302860c544ee5c014a02081bd2ea) |
| [projectdiscovery/asnmap](https://github.com/projectdiscovery/asnmap) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [cedef8b116fb](https://github.com/projectdiscovery/asnmap/tree/cedef8b116fb2ea228108bfa2eee6ed74ae31ad9) |
| [projectdiscovery/cdncheck](https://github.com/projectdiscovery/cdncheck) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [2c31ce5d9dc9](https://github.com/projectdiscovery/cdncheck/tree/2c31ce5d9dc95c369f99e95d58d56f59796d8dd0) |
| [projectdiscovery/dnsx](https://github.com/projectdiscovery/dnsx) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [a1536fedba21](https://github.com/projectdiscovery/dnsx/tree/a1536fedba21caf278eaf65063844616c31b4ecc) |
| [projectdiscovery/httpx](https://github.com/projectdiscovery/httpx) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [f3ac85045712](https://github.com/projectdiscovery/httpx/tree/f3ac850457129af3910cf641fe4e2bc2ee178172) |
| [projectdiscovery/katana](https://github.com/projectdiscovery/katana) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [9662cd7b60ba](https://github.com/projectdiscovery/katana/tree/9662cd7b60ba1bc3a88232433ddefc4f48a65bfe) |
| [projectdiscovery/mapcidr](https://github.com/projectdiscovery/mapcidr) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [43eaae983813](https://github.com/projectdiscovery/mapcidr/tree/43eaae9838133f23a8a26d59460daf11e40a05aa) |
| [projectdiscovery/naabu](https://github.com/projectdiscovery/naabu) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [38726814aff1](https://github.com/projectdiscovery/naabu/tree/38726814aff178e20c2c0c0da5df6e86735416bb) |
| [projectdiscovery/notify](https://github.com/projectdiscovery/notify) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [2d6ef20689e8](https://github.com/projectdiscovery/notify/tree/2d6ef20689e805c957c195471d9d2e926ba6a758) |
| [projectdiscovery/pdtm](https://github.com/projectdiscovery/pdtm) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [de1221928066](https://github.com/projectdiscovery/pdtm/tree/de12219280663c676851e0f2c79fe10016ee6537) |
| [projectdiscovery/shuffledns](https://github.com/projectdiscovery/shuffledns) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [bc31821c9b3a](https://github.com/projectdiscovery/shuffledns/tree/bc31821c9b3a06a13fc50e65481fec68e1b01ad2) |
| [projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [b9239ac6abae](https://github.com/projectdiscovery/subfinder/tree/b9239ac6abaeb389f36e4d0e1484394b697d7b91) |
| [projectdiscovery/tlsx](https://github.com/projectdiscovery/tlsx) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [7f24430c54c4](https://github.com/projectdiscovery/tlsx/tree/7f24430c54c473e6b32caf29753562da6ffb4181) |
| [projectdiscovery/uncover](https://github.com/projectdiscovery/uncover) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [827504844132](https://github.com/projectdiscovery/uncover/tree/8275048441329a9ce0622bead7b37826d34e5d7d) |
| [resurrecting-open-source-projects/nbtscan](https://github.com/resurrecting-open-source-projects/nbtscan) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [e09e22a2a322](https://github.com/resurrecting-open-source-projects/nbtscan/tree/e09e22a2a322ba74bb0b3cd596933fe2e31f4b2b) |
| [s0md3v/Photon](https://github.com/s0md3v/Photon) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [c8d2566841d6](https://github.com/s0md3v/Photon/tree/c8d2566841d69a268b244609921143d84b72b0c6) |
| [sensepost/gowitness](https://github.com/sensepost/gowitness) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [601c84367aaf](https://github.com/sensepost/gowitness/tree/601c84367aaf26eae7d1b5181b70633cb662cf66) |
| [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [e40a45ec2a07](https://github.com/sherlock-project/sherlock/tree/e40a45ec2a074b90703b3b4b842c8a3adbd6ada3) |
| [six2dez/reconftw](https://github.com/six2dez/reconftw) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [b9807ab78788](https://github.com/six2dez/reconftw/tree/b9807ab787880700e08f435df5c84023d16b0b6c) |
| [smicallef/spiderfoot](https://github.com/smicallef/spiderfoot) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [0f815a203afe](https://github.com/smicallef/spiderfoot/tree/0f815a203afebf05c98b605dba5cf0475a0ee5fd) |
| [SparrowOchon/dnsenum2](https://github.com/SparrowOchon/dnsenum2) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [17d3d0413763](https://github.com/SparrowOchon/dnsenum2/tree/17d3d04137636515150f54a8234d573d8205f0ec) |
| [tomnomnom/anew](https://github.com/tomnomnom/anew) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [d67d68db0d56](https://github.com/tomnomnom/anew/tree/d67d68db0d56469fdea7505c5a9209c0a465effa) |
| [tomnomnom/assetfinder](https://github.com/tomnomnom/assetfinder) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [4e95d8701aae](https://github.com/tomnomnom/assetfinder/tree/4e95d8701aae8cff1c27af2626eb22ba110ad583) |
| [tomnomnom/httprobe](https://github.com/tomnomnom/httprobe) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [0745f649beb0](https://github.com/tomnomnom/httprobe/tree/0745f649beb01c3cf712e0c52f9760d8a92cfdc2) |
| [tomnomnom/qsreplace](https://github.com/tomnomnom/qsreplace) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [320475befaf6](https://github.com/tomnomnom/qsreplace/tree/320475befaf66d986400aa8c3ed9b43e0b6b5a02) |
| [tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [8d27cf3e3031](https://github.com/tomnomnom/waybackurls/tree/8d27cf3e3031de01179e8ba9127e968eb01008e9) |
| [trailofbits/onesixtyone](https://github.com/trailofbits/onesixtyone) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [3bedd7cab7fe](https://github.com/trailofbits/onesixtyone/tree/3bedd7cab7fe1bcfc2def208f87fbf10a013efc7) |
| [urbanadventurer/WhatWeb](https://github.com/urbanadventurer/WhatWeb) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [d279d93042d0](https://github.com/urbanadventurer/WhatWeb/tree/d279d93042d034f3fd29d5a893d44ccc0595d3f8) |

## Web & API testing

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [assetnote/kiterunner](https://github.com/assetnote/kiterunner) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [7d5824cda9a2](https://github.com/assetnote/kiterunner/tree/7d5824cda9a2eef86d8d18b05b713d7e260f34d2) |
| [doyensec/inql](https://github.com/doyensec/inql) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [00a0bd79418e](https://github.com/doyensec/inql/tree/00a0bd79418ebbee09d93550b83ba3f406a872e8) |
| [dwisiswant0/crlfuzz](https://github.com/dwisiswant0/crlfuzz) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [7a442bb03f3c](https://github.com/dwisiswant0/crlfuzz/tree/7a442bb03f3c337f34b1ed7664bae50bde3eb455) |
| [epi052/feroxbuster](https://github.com/epi052/feroxbuster) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [b07a7662d588](https://github.com/epi052/feroxbuster/tree/b07a7662d588bd8e4371e9be4704a02d976c89bb) |
| [ffuf/ffuf](https://github.com/ffuf/ffuf) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [8d65e0373e5f](https://github.com/ffuf/ffuf/tree/8d65e0373e5f223530174e5694285af849770078) |
| [Hackmanit/TInjA](https://github.com/Hackmanit/TInjA) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [507d903e1bb2](https://github.com/Hackmanit/TInjA/tree/507d903e1bb27073418daea4b1aec146b8775f48) |
| [hahwul/dalfox](https://github.com/hahwul/dalfox) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [947732dbeda0](https://github.com/hahwul/dalfox/tree/947732dbeda028d7127b6768d19c6d5b0d6b3160) |
| [KathanP19/HowToHunt](https://github.com/KathanP19/HowToHunt) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [4c8c23fce6c7](https://github.com/KathanP19/HowToHunt/tree/4c8c23fce6c754e9495101d3894cc7228ee7c709) |
| [maurosoria/dirsearch](https://github.com/maurosoria/dirsearch) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [b45e01bb8914](https://github.com/maurosoria/dirsearch/tree/b45e01bb891457d6846e6af0a3755e032f937d78) |
| [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [696d4e28c54c](https://github.com/mitmproxy/mitmproxy/tree/696d4e28c54cd2f66640c6307ab978fec1ba2f16) |
| [nabla-c0d3/sslyze](https://github.com/nabla-c0d3/sslyze) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [3bd5094dec1d](https://github.com/nabla-c0d3/sslyze/tree/3bd5094dec1dfbaac1a03957c35ba5e487f5b890) |
| [nikitastupin/clairvoyance](https://github.com/nikitastupin/clairvoyance) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [3492afd418c5](https://github.com/nikitastupin/clairvoyance/tree/3492afd418c5761876b557f781cd387088c1af5b) |
| [OJ/gobuster](https://github.com/OJ/gobuster) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [c77583fbb882](https://github.com/OJ/gobuster/tree/c77583fbb8824058d74d38240896eff610683c8e) |
| [PortSwigger/autorize](https://github.com/PortSwigger/autorize) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [6e4a7a7f44c4](https://github.com/PortSwigger/autorize/tree/6e4a7a7f44c4930b9b10d0be58ad491ba2769e4d) |
| [PortSwigger/BChecks](https://github.com/PortSwigger/BChecks) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [d4e08e3ed331](https://github.com/PortSwigger/BChecks/tree/d4e08e3ed331a34bfbb5241432bfac248629a8bb) |
| [PortSwigger/http-request-smuggler](https://github.com/PortSwigger/http-request-smuggler) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [3ecb1afa6a1d](https://github.com/PortSwigger/http-request-smuggler/tree/3ecb1afa6a1d21ef1ec4e6eb1337818b53a2b4c0) |
| [PortSwigger/param-miner](https://github.com/PortSwigger/param-miner) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [e43e3b16be11](https://github.com/PortSwigger/param-miner/tree/e43e3b16be11117ed67cfde60e80acf2e95a4adc) |
| [PortSwigger/turbo-intruder](https://github.com/PortSwigger/turbo-intruder) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [7b9d1f9db1a2](https://github.com/PortSwigger/turbo-intruder/tree/7b9d1f9db1a268aed8d62a3415e9fd52c1cecf47) |
| [projectdiscovery/interactsh](https://github.com/projectdiscovery/interactsh) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [a5b78b2f1d99](https://github.com/projectdiscovery/interactsh/tree/a5b78b2f1d990cd18c85cc422f0e651cf204c464) |
| [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [f3b817b818a6](https://github.com/projectdiscovery/nuclei/tree/f3b817b818a61e87296a27441351e85d739140b8) |
| [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [ee9e6969a9be](https://github.com/projectdiscovery/nuclei-templates/tree/ee9e6969a9befe639e9083bacc33b824400d0bb9) |
| [s0md3v/Arjun](https://github.com/s0md3v/Arjun) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [d1fb995cb1e0](https://github.com/s0md3v/Arjun/tree/d1fb995cb1e064d4e171d83f19f6af79b0a3c5ce) |
| [s0md3v/XSStrike](https://github.com/s0md3v/XSStrike) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [ab27955d3674](https://github.com/s0md3v/XSStrike/tree/ab27955d367432f944d8f29897e09c15356e76f7) |
| [schemathesis/schemathesis](https://github.com/schemathesis/schemathesis) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [406c7dbb105c](https://github.com/schemathesis/schemathesis/tree/406c7dbb105c8c0693096ca9a9bdd5a731b4003f) |
| [sqlmapproject/sqlmap](https://github.com/sqlmapproject/sqlmap) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [d57415479ae0](https://github.com/sqlmapproject/sqlmap/tree/d57415479ae016db0e4c76abd3a75ad12cb4e34a) |
| [sullo/nikto](https://github.com/sullo/nikto) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [312645d87347](https://github.com/sullo/nikto/tree/312645d873478a77986627ab1fc8cffe595e85d4) |
| [testssl/testssl.sh](https://github.com/testssl/testssl.sh) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [9bd7e16df96a](https://github.com/testssl/testssl.sh/tree/9bd7e16df96a8e4e36c89f6c55443eceb9e36c71) |
| [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [3bc7407cf222](https://github.com/ticarpi/jwt_tool/tree/3bc7407cf2222d6a821dcc19c776e5a1b1cb9a9b) |
| [wapiti-scanner/wapiti](https://github.com/wapiti-scanner/wapiti) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [1e816981319a](https://github.com/wapiti-scanner/wapiti/tree/1e816981319a974f250caab219c0eb19c028e990) |
| [wpscanteam/wpscan](https://github.com/wpscanteam/wpscan) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [5d672f66ee51](https://github.com/wpscanteam/wpscan/tree/5d672f66ee512301b654a2d79c9ddf6f8509eeb4) |
| [xmendez/wfuzz](https://github.com/xmendez/wfuzz) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [2263cd0932fe](https://github.com/xmendez/wfuzz/tree/2263cd0932fef333118cd197656f709141bab615) |
| [zaproxy/zap-extensions](https://github.com/zaproxy/zap-extensions) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [845d3da8eac4](https://github.com/zaproxy/zap-extensions/tree/845d3da8eac45b05c17920ed10eacb32d5d994b9) |
| [zaproxy/zaproxy](https://github.com/zaproxy/zaproxy) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [e06ba5ee209e](https://github.com/zaproxy/zaproxy/tree/e06ba5ee209e27a9a81ff16e17696d6b59757d3a) |

## Identity & Active Directory

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [adityatelange/evil-winrm-py](https://github.com/adityatelange/evil-winrm-py) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [bb5710eb268d](https://github.com/adityatelange/evil-winrm-py/tree/bb5710eb268d6aa136117529f71a92ca821c0fda) |
| [aniqfakhrul/powerview.py](https://github.com/aniqfakhrul/powerview.py) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [ea133da24ac9](https://github.com/aniqfakhrul/powerview.py/tree/ea133da24ac9f51879f89a559c3fe575e3d1c801) |
| [c3c/ADExplorerSnapshot](https://github.com/c3c/ADExplorerSnapshot) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [2f845904afec](https://github.com/c3c/ADExplorerSnapshot/tree/2f845904afecd83ca49a475e2c121c4501f94453) |
| [dirkjanm/adidnsdump](https://github.com/dirkjanm/adidnsdump) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [95adaf8ed278](https://github.com/dirkjanm/adidnsdump/tree/95adaf8ed278088217f08f88a15d12bb411dd2e8) |
| [dirkjanm/BloodHound.py](https://github.com/dirkjanm/BloodHound.py) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [fd3f322e066d](https://github.com/dirkjanm/BloodHound.py/tree/fd3f322e066d66314bfb31d4ae6f497df5872177) |
| [dirkjanm/krbrelayx](https://github.com/dirkjanm/krbrelayx) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [10b45a33bc43](https://github.com/dirkjanm/krbrelayx/tree/10b45a33bc4361ec4a5546eea62db2e4244d3255) |
| [dirkjanm/ldapdomaindump](https://github.com/dirkjanm/ldapdomaindump) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [d559463eb298](https://github.com/dirkjanm/ldapdomaindump/tree/d559463eb29857f2660bf3867bfb9f8610d1ddb1) |
| [dirkjanm/PKINITtools](https://github.com/dirkjanm/PKINITtools) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [0f0cfa542b03](https://github.com/dirkjanm/PKINITtools/tree/0f0cfa542b0348609ad494713e84744234b2d3b0) |
| [fortra/impacket](https://github.com/fortra/impacket) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [4f0348e83809](https://github.com/fortra/impacket/tree/4f0348e83809139473fd6461241bbf80d441df4b) |
| [GhostPack/Certify](https://github.com/GhostPack/Certify) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [ce9a4d27d2f1](https://github.com/GhostPack/Certify/tree/ce9a4d27d2f18d391c141ebdc8cb82fa5f6b88e3) |
| [GhostPack/Rubeus](https://github.com/GhostPack/Rubeus) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [74215f68ea70](https://github.com/GhostPack/Rubeus/tree/74215f68ea70bd6a66c008da91bf5fe21d20b154) |
| [GhostPack/Seatbelt](https://github.com/GhostPack/Seatbelt) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [392171df8447](https://github.com/GhostPack/Seatbelt/tree/392171df84472591d4eae7ebd5b1cdc96ba91377) |
| [Hackplayers/evil-winrm](https://github.com/Hackplayers/evil-winrm) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [64d8e0f962d2](https://github.com/Hackplayers/evil-winrm/tree/64d8e0f962d239643c4efadacce9f716bd5cb775) |
| [lgandx/Responder](https://github.com/lgandx/Responder) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [424fbe53d6a6](https://github.com/lgandx/Responder/tree/424fbe53d6a61824e3c7685fe5f69668721b821e) |
| [lkarlslund/Adalanche](https://github.com/lkarlslund/Adalanche) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [d75b012549d7](https://github.com/lkarlslund/Adalanche/tree/d75b012549d7bfe89324f6fd6382868dd44a90eb) |
| [ly4k/Certipy](https://github.com/ly4k/Certipy) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [3ae34426c58d](https://github.com/ly4k/Certipy/tree/3ae34426c58d266a1979ff9607514c3d7fe1aa21) |
| [Pennyw0rth/NetExec](https://github.com/Pennyw0rth/NetExec) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [ae683dba107a](https://github.com/Pennyw0rth/NetExec/tree/ae683dba107a0365f79141bf4758412dbf3dc950) |
| [ropnop/kerbrute](https://github.com/ropnop/kerbrute) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [9cfb81e4fab8](https://github.com/ropnop/kerbrute/tree/9cfb81e4fab8037acb44c678773ca3f93bc2b39c) |
| [ShawnDEvans/smbmap](https://github.com/ShawnDEvans/smbmap) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [31b8a8f27a32](https://github.com/ShawnDEvans/smbmap/tree/31b8a8f27a32f53ed1d63294dffd30519b79d169) |
| [SpecterOps/BloodHound](https://github.com/SpecterOps/BloodHound) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [41421cc5e283](https://github.com/SpecterOps/BloodHound/tree/41421cc5e28370e1feab7e454a032ba808c7cce1) |
| [SpecterOps/SharpHound](https://github.com/SpecterOps/SharpHound) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [85924979a9d2](https://github.com/SpecterOps/SharpHound/tree/85924979a9d23ab0e83a3fcfabee3b9962bb14be) |

## Cloud, containers & code security

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [anchore/grype](https://github.com/anchore/grype) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [afe2742527d9](https://github.com/anchore/grype/tree/afe2742527d98d822da06c9f32eed86fe3d193e0) |
| [anchore/syft](https://github.com/anchore/syft) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [f15c3343e29d](https://github.com/anchore/syft/tree/f15c3343e29dfb20cf6d82c820e7090b49808c96) |
| [aquasecurity/kube-bench](https://github.com/aquasecurity/kube-bench) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [e278a5915a98](https://github.com/aquasecurity/kube-bench/tree/e278a5915a982f2756026de6e2f9ca77077ef9f9) |
| [aquasecurity/kube-hunter](https://github.com/aquasecurity/kube-hunter) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [bc47f08e88ea](https://github.com/aquasecurity/kube-hunter/tree/bc47f08e88ea2a5fb059bf3b8a8edb1aefb4c6cc) |
| [aws/aws-cli](https://github.com/aws/aws-cli) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [685e02ddb5ea](https://github.com/aws/aws-cli/tree/685e02ddb5eab6bb506650d1b2fd69771afadfc1) |
| [BishopFox/cloudfox](https://github.com/BishopFox/cloudfox) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [d44899f21302](https://github.com/BishopFox/cloudfox/tree/d44899f21302269fc5e7743c662edafe15c7575c) |
| [bridgecrewio/checkov](https://github.com/bridgecrewio/checkov) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [7a6782e3d81e](https://github.com/bridgecrewio/checkov/tree/7a6782e3d81e19f1bdd9213129f3138767691f5f) |
| [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [b58d3f102cf3](https://github.com/gitleaks/gitleaks/tree/b58d3f102cf3a2c84cb7f923d05c25c9b1aed84b) |
| [kubescape/kubescape](https://github.com/kubescape/kubescape) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [db78f2539b02](https://github.com/kubescape/kubescape/tree/db78f2539b02eca751f7aaa155443f28a31f6de5) |
| [nccgroup/ScoutSuite](https://github.com/nccgroup/ScoutSuite) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [7909f2fc6186](https://github.com/nccgroup/ScoutSuite/tree/7909f2fc6186063e5c9e7ddef8c4d7d1072c8f3d) |
| [ossf/scorecard](https://github.com/ossf/scorecard) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [6d4113e03c00](https://github.com/ossf/scorecard/tree/6d4113e03c0014d63613b65b26a0c5a14c98ce3f) |
| [prowler-cloud/prowler](https://github.com/prowler-cloud/prowler) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [4d922da2a6a2](https://github.com/prowler-cloud/prowler/tree/4d922da2a6a29fdf49287176bae11401aaf02b75) |
| [RhinoSecurityLabs/pacu](https://github.com/RhinoSecurityLabs/pacu) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [e597f23ecfb8](https://github.com/RhinoSecurityLabs/pacu/tree/e597f23ecfb88b82f706c5f0cac9d4577c2af262) |
| [rhysd/actionlint](https://github.com/rhysd/actionlint) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [011a6d15e749](https://github.com/rhysd/actionlint/tree/011a6d15e749bb3f2d771eed9c7aa0e7e3e10ee7) |
| [semgrep/semgrep](https://github.com/semgrep/semgrep) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [51602ad27f09](https://github.com/semgrep/semgrep/tree/51602ad27f09ef9342a5620601de5ef8f572fbc6) |
| [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [e63326d6545d](https://github.com/trufflesecurity/trufflehog/tree/e63326d6545de8f425d93ce24078c6e68d83f70e) |

## Mobile & instrumentation

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [ashishb/android-security-awesome](https://github.com/ashishb/android-security-awesome) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [b21a710ccf4b](https://github.com/ashishb/android-security-awesome/tree/b21a710ccf4b6dbd470933105f5d53e9ca5663e0) |
| [Ch0pin/medusa](https://github.com/Ch0pin/medusa) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [a7bd929f297f](https://github.com/Ch0pin/medusa/tree/a7bd929f297f0725a5e4d2e3952874a757d4e2fc) |
| [frida/frida](https://github.com/frida/frida) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [adf8be5f5b7f](https://github.com/frida/frida/tree/adf8be5f5b7f3840521783b628a191b62d7e6f66) |
| [frida/frida-tools](https://github.com/frida/frida-tools) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [330ed423f71b](https://github.com/frida/frida-tools/tree/330ed423f71b7797e4be1821795463728430b43e) |
| [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [a60891aea193](https://github.com/Genymobile/scrcpy/tree/a60891aea193d92e7e5c3942700eca63f9d19a5f) |
| [google/oss-fuzz](https://github.com/google/oss-fuzz) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [6e2d4a84b25b](https://github.com/google/oss-fuzz/tree/6e2d4a84b25ba47ea6042a06af2c284be1a64124) |
| [googleprojectzero/fuzzilli](https://github.com/googleprojectzero/fuzzilli) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [be2811d00282](https://github.com/googleprojectzero/fuzzilli/tree/be2811d00282320381fc8007d64873745772011d) |
| [httptoolkit/httptoolkit](https://github.com/httptoolkit/httptoolkit) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [bb579a8ceadf](https://github.com/httptoolkit/httptoolkit/tree/bb579a8ceadfe86b98160843c0447a5b9eec554f) |
| [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [fd9d5d4dc7e4](https://github.com/iBotPeaches/Apktool/tree/fd9d5d4dc7e45fa7f984698ded7a03c554d0a7b3) |
| [MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [08872c8454e5](https://github.com/MobSF/Mobile-Security-Framework-MobSF/tree/08872c8454e59f8a6347c35b46852c9929f5eb5e) |
| [MobSF/mobsfscan](https://github.com/MobSF/mobsfscan) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [4645ea70bc09](https://github.com/MobSF/mobsfscan/tree/4645ea70bc093268502fe9f6df93e41bb482254a) |
| [patrickfav/uber-apk-signer](https://github.com/patrickfav/uber-apk-signer) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [76cbf02556b4](https://github.com/patrickfav/uber-apk-signer/tree/76cbf02556b4454f4c2bd6c908b4355003c4e37d) |
| [pxb1988/dex2jar](https://github.com/pxb1988/dex2jar) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [b5bda4fb4935](https://github.com/pxb1988/dex2jar/tree/b5bda4fb4935ae8b3869b422454ae3b3896c7bc1) |
| [r0ysue/r0capture](https://github.com/r0ysue/r0capture) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [3e4e9f9765c4](https://github.com/r0ysue/r0capture/tree/3e4e9f9765c4e1d06c17e3a24bf64189de498eb0) |
| [ReversecLabs/drozer](https://github.com/ReversecLabs/drozer) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [d992f6378d42](https://github.com/ReversecLabs/drozer/tree/d992f6378d42680ea96ee03eff4117f150e1049c) |
| [sensepost/objection](https://github.com/sensepost/objection) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [35c4e2c9e68a](https://github.com/sensepost/objection/tree/35c4e2c9e68a0354b21db4833252e0c4acd5bd28) |
| [skylot/jadx](https://github.com/skylot/jadx) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [c4c45fde27b4](https://github.com/skylot/jadx/tree/c4c45fde27b4f3386dc2ff016ff187229a60a716) |
| [kalilinux/nethunter/apps/kali-nethunter-app](https://gitlab.com/kalilinux/nethunter/apps/kali-nethunter-app) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [b57348d6fbe8](https://gitlab.com/kalilinux/nethunter/apps/kali-nethunter-app/-/tree/b57348d6fbe8cc13170bfe10bcac6a82c1e42e14) |
| [kalilinux/nethunter/build-scripts/kali-nethunter-installer](https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-installer) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [e63b0476a7fd](https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-installer/-/tree/e63b0476a7fd5767729208c68a78ad79afaaf556) |

## Network & traffic

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [socat](https://tracker.debian.org/pkg/socat) | 2026-10-21 | SOURCE_SCREENED_ONLY | Package/version: no record returned | [1.8.1.3-2](https://deb.debian.org/debian/pool/main/s/socat/socat_1.8.1.3-2.dsc) |
| [traceroute](https://tracker.debian.org/pkg/traceroute) | 2026-10-21 | SOURCE_SCREENED_ONLY | Package/version: no record returned | [2.1.6-1](https://deb.debian.org/debian/pool/main/t/traceroute/traceroute_2.1.6-1.dsc) |
| [aanarchyy/bully](https://github.com/aanarchyy/bully) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [3ab3bc830738](https://github.com/aanarchyy/bully/tree/3ab3bc830738f447dce112e8551e3ac8193bf521) |
| [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [7e2256f38f35](https://github.com/aircrack-ng/aircrack-ng/tree/7e2256f38f3590af4c19a6ae14ed79bab02242e6) |
| [bettercap/bettercap](https://github.com/bettercap/bettercap) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [8eca2820f3c4](https://github.com/bettercap/bettercap/tree/8eca2820f3c41d2004434ed5a291d87462caeeb7) |
| [curl/curl](https://github.com/curl/curl) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [eb2b201a2da3](https://github.com/curl/curl/tree/eb2b201a2da3bfc6fefd7ff2d8e476e3cb9e5bcb) |
| [derv82/wifite2](https://github.com/derv82/wifite2) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [43c4d2c520e4](https://github.com/derv82/wifite2/tree/43c4d2c520e45cfb828a430741b915ca4f5d7128) |
| [evilsocket/opensnitch](https://github.com/evilsocket/opensnitch) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [a1353848ba1b](https://github.com/evilsocket/opensnitch/tree/a1353848ba1b660320e90cefea782c3fba272c00) |
| [fatedier/frp](https://github.com/fatedier/frp) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [b0bf32571a3d](https://github.com/fatedier/frp/tree/b0bf32571a3d4d4f9bb77223ce0d0e5d32ea1216) |
| [jpillora/chisel](https://github.com/jpillora/chisel) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [5ee6c74d60d9](https://github.com/jpillora/chisel/tree/5ee6c74d60d96a75afb18bc866eb19327170aeed) |
| [jtesta/ssh-audit](https://github.com/jtesta/ssh-audit) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [1df77bfbb664](https://github.com/jtesta/ssh-audit/tree/1df77bfbb664ec435cd662b938c1080012df3354) |
| [mct/tcptraceroute](https://github.com/mct/tcptraceroute) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [3772409867b3](https://github.com/mct/tcptraceroute/tree/3772409867b3c5591c50d69f0abacf780c3a555f) |
| [nicocha30/ligolo-ng](https://github.com/nicocha30/ligolo-ng) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [e543732f4be6](https://github.com/nicocha30/ligolo-ng/tree/e543732f4be6dc899096ae322ae620bf010bfbfc) |
| [nmap/nmap](https://github.com/nmap/nmap) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [01f4ed2968f6](https://github.com/nmap/nmap/tree/01f4ed2968f6ee09e487e67609e9ef037ffe4092) |
| [robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [8e6b3b0c07a8](https://github.com/robertdavidgraham/masscan/tree/8e6b3b0c07a81e8ea61d557c06134a21a6881614) |
| [rofl0r/proxychains-ng](https://github.com/rofl0r/proxychains-ng) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [aa87f65c4f8a](https://github.com/rofl0r/proxychains-ng/tree/aa87f65c4f8aacfa73f76ba23bfea4e82250be3b) |
| [secdev/scapy](https://github.com/secdev/scapy) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [9aa380f694e0](https://github.com/secdev/scapy/tree/9aa380f694e0f32788fa701857cef17970b7b8c1) |
| [sshuttle/sshuttle](https://github.com/sshuttle/sshuttle) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [6954af07f4ba](https://github.com/sshuttle/sshuttle/tree/6954af07f4ba8683f6797534f453ba863d354049) |
| [t6x/reaver-wps-fork-t6x](https://github.com/t6x/reaver-wps-fork-t6x) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [f9b5e150f913](https://github.com/t6x/reaver-wps-fork-t6x/tree/f9b5e150f913a23d34c8098d598b90aaa08261cc) |
| [the-tcpdump-group/tcpdump](https://github.com/the-tcpdump-group/tcpdump) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [35f39fa1b238](https://github.com/the-tcpdump-group/tcpdump/tree/35f39fa1b238e51ebc1a139102e5fc00f2a82ffd) |
| [wiire-a/pixiewps](https://github.com/wiire-a/pixiewps) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [20eaf62b3fd2](https://github.com/wiire-a/pixiewps/tree/20eaf62b3fd2afc67b039d1521460b3b7d165842) |
| [ZerBea/hcxdumptool](https://github.com/ZerBea/hcxdumptool) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [6dc11f43753c](https://github.com/ZerBea/hcxdumptool/tree/6dc11f43753c584fc795eaa34b6af21a359fa61c) |
| [torproject/tor](https://gitlab.com/torproject/tor) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [8dbbbe6e86a6](https://gitlab.com/torproject/tor/-/tree/8dbbbe6e86a6ca0d058ec3c6a4e937859857d7bb) |
| [wireshark/wireshark](https://gitlab.com/wireshark/wireshark) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [f2c97e2b22bd](https://gitlab.com/wireshark/wireshark/-/tree/f2c97e2b22bdcaa9982b8dd61b4401530f29c8fb) |
| [debian/netcat-openbsd](https://salsa.debian.org/debian/netcat-openbsd) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [47c18df2086e](https://salsa.debian.org/debian/netcat-openbsd/-/tree/47c18df2086ecf7911357ec9bff6daddf6de6c09) |
| [pkg-privacy-team/torsocks](https://salsa.debian.org/pkg-privacy-team/torsocks) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [7538c6964862](https://salsa.debian.org/pkg-privacy-team/torsocks/-/tree/7538c69648624ef9c01fa2441ffea6c16434ae6a) |

## Red team & adversary emulation

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [apache/caldera](https://github.com/apache/caldera) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [cb8d6a8160e0](https://github.com/apache/caldera/tree/cb8d6a8160e0f4990af323a7c071d5e8482b42c7) |
| [BC-SECURITY/Empire](https://github.com/BC-SECURITY/Empire) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [33e2b4bbd0f3](https://github.com/BC-SECURITY/Empire/tree/33e2b4bbd0f31308a63d889fd96d8c8fe9c2c12f) |
| [BishopFox/sliver](https://github.com/BishopFox/sliver) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [5383bd67b526](https://github.com/BishopFox/sliver/tree/5383bd67b526b4a8425d9bd699a53eb3a18b1255) |
| [cobbr/Covenant](https://github.com/cobbr/Covenant) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [5decc3ccfab0](https://github.com/cobbr/Covenant/tree/5decc3ccfab04e6e881ed00c9de649740dac8ad1) |
| [its-a-feature/Mythic](https://github.com/its-a-feature/Mythic) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [96b24b48a7f2](https://github.com/its-a-feature/Mythic/tree/96b24b48a7f26594f1126eabef8ad00301ba28a0) |
| [lanmaster53/recon-ng](https://github.com/lanmaster53/recon-ng) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [32b08fe7b699](https://github.com/lanmaster53/recon-ng/tree/32b08fe7b6993ca1f2d8f76ba8f5d23c7f34a11d) |
| [rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [1e321cedaf4c](https://github.com/rapid7/metasploit-framework/tree/1e321cedaf4c2a3f92de6a21b2f7d4b8eff31ca4) |
| [trustedsec/ptf](https://github.com/trustedsec/ptf) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [74f58d6b6557](https://github.com/trustedsec/ptf/tree/74f58d6b6557de115d0286a5d5c1849ba6048258) |

## Reverse engineering & vulnerability research

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [AFLplusplus/AFLplusplus](https://github.com/AFLplusplus/AFLplusplus) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [d0070729206a](https://github.com/AFLplusplus/AFLplusplus/tree/d0070729206a80a9af297b2341edd63f68fdac35) |
| [angr/angr](https://github.com/angr/angr) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [16245f07bc53](https://github.com/angr/angr/tree/16245f07bc53b52bd75cbfd738bb4cadba7b6174) |
| [Gallopsled/pwntools](https://github.com/Gallopsled/pwntools) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [99a4fe5596bc](https://github.com/Gallopsled/pwntools/tree/99a4fe5596bcba851537fdbe821ceb5fb80c4de1) |
| [googleprojectzero/winafl](https://github.com/googleprojectzero/winafl) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [fd85f38548b1](https://github.com/googleprojectzero/winafl/tree/fd85f38548b14352f4b70ad414f364ea6dc1a769) |
| [hugsy/gef](https://github.com/hugsy/gef) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [49c07dc60624](https://github.com/hugsy/gef/tree/49c07dc60624f264d40b5c6ea39b2bf3a4e9958f) |
| [lief-project/LIEF](https://github.com/lief-project/LIEF) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [80cf4a582cd7](https://github.com/lief-project/LIEF/tree/80cf4a582cd7afc486cc3791e30775517c71b579) |
| [longld/peda](https://github.com/longld/peda) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [84d38bda5059](https://github.com/longld/peda/tree/84d38bda505941ba823db7f6c1bcca1e485a2d43) |
| [mandiant/capa](https://github.com/mandiant/capa) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [7a235c46965e](https://github.com/mandiant/capa/tree/7a235c46965ea0965c65be3b9ee1e21dca686f3d) |
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [c91ec18e6780](https://github.com/NationalSecurityAgency/ghidra/tree/c91ec18e6780a8a531a806a0660a9c28978a99a0) |
| [pwndbg/pwndbg](https://github.com/pwndbg/pwndbg) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [d887a5c04b10](https://github.com/pwndbg/pwndbg/tree/d887a5c04b10eb36637600185775064d3c2904e1) |
| [radareorg/radare2](https://github.com/radareorg/radare2) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [8b507e97e51f](https://github.com/radareorg/radare2/tree/8b507e97e51f4017e54def231cc6925e9afec333) |
| [rebootuser/LinEnum](https://github.com/rebootuser/LinEnum) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [c47f9b226d3c](https://github.com/rebootuser/LinEnum/tree/c47f9b226d3ce2848629f25fe142c1b2986bc427) |
| [ReFirmLabs/binwalk](https://github.com/ReFirmLabs/binwalk) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [26713972e3f9](https://github.com/ReFirmLabs/binwalk/tree/26713972e3f9f52dc37d4a421c4554b0bd9e82ef) |
| [rizinorg/cutter](https://github.com/rizinorg/cutter) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [d7f11b220884](https://github.com/rizinorg/cutter/tree/d7f11b220884a6cc8549da955b744bd318645103) |
| [strace/strace](https://github.com/strace/strace) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [0bddc7627d00](https://github.com/strace/strace/tree/0bddc7627d002c20351d734ab32b468c5739cb5e) |
| [unicorn-engine/unicorn](https://github.com/unicorn-engine/unicorn) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [7c5db94191de](https://github.com/unicorn-engine/unicorn/tree/7c5db94191defc1e04a4f66f4eb1220903cba837) |
| [VirusTotal/yara](https://github.com/VirusTotal/yara) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [5cd1e8b64082](https://github.com/VirusTotal/yara/tree/5cd1e8b64082c0e0ddce2ad1e1748df41700ab9e) |
| [x64dbg/x64dbg](https://github.com/x64dbg/x64dbg) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [c44297200731](https://github.com/x64dbg/x64dbg/tree/c44297200731995c51dbc75ab3098e2f0094b282) |
| [Yara-Rules/rules](https://github.com/Yara-Rules/rules) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [0f93570194a8](https://github.com/Yara-Rules/rules/tree/0f93570194a80d2f2032869055808b0ddcdfb360) |
| [cespedes/ltrace](https://gitlab.com/cespedes/ltrace) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [3f9b64ac0d5d](https://gitlab.com/cespedes/ltrace/-/tree/3f9b64ac0d5da4c5a2d9d76e1a61b4966d51a785) |
| [exploit-database/exploitdb](https://gitlab.com/exploit-database/exploitdb) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [12879ca774a9](https://gitlab.com/exploit-database/exploitdb/-/tree/12879ca774a9d7543907d24a7bc1cebb47959afe) |
| [binutils-gdb](https://sourceware.org/git/?p=binutils-gdb.git) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [6fd421ad78bc](https://sourceware.org/git/?p=binutils-gdb.git;a=tree;h=6fd421ad78bcb259f371394498e2c1346380e5b7) |

## Wordlists & test data

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [1N3/IntruderPayloads](https://github.com/1N3/IntruderPayloads) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [9b84328441e0](https://github.com/1N3/IntruderPayloads/tree/9b84328441e0b1d5b63764941bfd72a2460dba5d) |
| [assetnote/wordlists](https://github.com/assetnote/wordlists) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [6dea231f4cbd](https://github.com/assetnote/wordlists/tree/6dea231f4cbd356a637851b1c13b83de4da00adb) |
| [danielmiessler/SecLists](https://github.com/danielmiessler/SecLists) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [75064ac792b5](https://github.com/danielmiessler/SecLists/tree/75064ac792b5b554d17386abae3f0e38db7f923c) |
| [digininja/CeWL](https://github.com/digininja/CeWL) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [ca01aeae1c77](https://github.com/digininja/CeWL/tree/ca01aeae1c77bb086ef757611dea6377b8d1168b) |
| [fuzzdb-project/fuzzdb](https://github.com/fuzzdb-project/fuzzdb) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [5656ab25dc6b](https://github.com/fuzzdb-project/fuzzdb/tree/5656ab25dc6bb43bae32236fab775658a90d7380) |
| [debian/crunch](https://salsa.debian.org/debian/crunch) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [dfa548807003](https://salsa.debian.org/debian/crunch/-/tree/dfa548807003f7a6be471d07f3bb8a0ad608aa22) |

## AI security & automation

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [05119078c104](https://github.com/danielmiessler/Fabric/tree/05119078c104142d8bde2d8984e7af388d55d404) |
| [dreadnode/rigging](https://github.com/dreadnode/rigging) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [3461e81e799a](https://github.com/dreadnode/rigging/tree/3461e81e799aff9040fe0d0671196b78667a7589) |
| [ethz-spylab/agentdojo](https://github.com/ethz-spylab/agentdojo) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [089ed468cf3e](https://github.com/ethz-spylab/agentdojo/tree/089ed468cf3ed0322acc66b0211f26d9d90dbf60) |
| [Giskard-AI/giskard-oss](https://github.com/Giskard-AI/giskard-oss) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [042ed8716264](https://github.com/Giskard-AI/giskard-oss/tree/042ed87162641dcb1512b02fe57054667a28cf9d) |
| [GitHubSecurityLab/seclab-taskflow-agent](https://github.com/GitHubSecurityLab/seclab-taskflow-agent) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [ab02b1fe8ac3](https://github.com/GitHubSecurityLab/seclab-taskflow-agent/tree/ab02b1fe8ac3d94352332b2c739c579f0d5ae810) |
| [GreyDGL/PentestGPT](https://github.com/GreyDGL/PentestGPT) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [e8b1bb77d1ac](https://github.com/GreyDGL/PentestGPT/tree/e8b1bb77d1ac00329675cec3b060aba971ec1ac8) |
| [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [4bd88c12a909](https://github.com/KeygraphHQ/shannon/tree/4bd88c12a9096d0b78ceb2828729d12dca70fa60) |
| [meta-llama/PurpleLlama](https://github.com/meta-llama/PurpleLlama) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [d934ea285d12](https://github.com/meta-llama/PurpleLlama/tree/d934ea285d124d81c10f7e15a06a1e1f74eff2c3) |
| [microsoft/PyRIT](https://github.com/microsoft/PyRIT) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [85d4f0c398bf](https://github.com/microsoft/PyRIT/tree/85d4f0c398bfd1bf3f09e1a56ddf3ee65caf054b) |
| [NVIDIA/garak](https://github.com/NVIDIA/garak) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [cc1215c5c301](https://github.com/NVIDIA/garak/tree/cc1215c5c301a69f115b0b2b7ef8e4172ae2e7fc) |
| [PortSwigger/mcp-server](https://github.com/PortSwigger/mcp-server) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [642e6fa31c63](https://github.com/PortSwigger/mcp-server/tree/642e6fa31c63db3886a353fcd7ed62037e0ceed5) |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [b49d55dfdec2](https://github.com/promptfoo/promptfoo/tree/b49d55dfdec226bb299afee253122879570cc536) |
| [six2dez/burp-ai-agent](https://github.com/six2dez/burp-ai-agent) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [1718308d8d86](https://github.com/six2dez/burp-ai-agent/tree/1718308d8d864b94c8347ec537e301a9cbb5d5ac) |
| [trailofbits/buttercup](https://github.com/trailofbits/buttercup) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [298c01fbff3b](https://github.com/trailofbits/buttercup/tree/298c01fbff3bf0bf166c87856acd7e42f94f7157) |
| [trailofbits/skills](https://github.com/trailofbits/skills) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [5c99c03fb8a9](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0) |
| [usestrix/strix](https://github.com/usestrix/strix) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [a0f8ea2cd379](https://github.com/usestrix/strix/tree/a0f8ea2cd379c4bf56e665d3db2ba8a4f7c0683c) |
| [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | 2026-10-20 | REVIEW_AGENT | Commit: no record returned | [843dfeb4bfc8](https://github.com/vxcontrol/pentagi/tree/843dfeb4bfc809c09d1bc5022e567c602d8fc9dd) |

## Reporting & workflow

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [dradis/dradis-ce](https://github.com/dradis/dradis-ce) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [0c85e061127f](https://github.com/dradis/dradis-ce/tree/0c85e061127f6da8c1d0bd62facbfa4768d782f1) |
| [GhostManager/Ghostwriter](https://github.com/GhostManager/Ghostwriter) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [f38174bb6ee4](https://github.com/GhostManager/Ghostwriter/tree/f38174bb6ee4ead86b8039abb1f7742ae8b97242) |
| [giuspen/cherrytree](https://github.com/giuspen/cherrytree) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [44aee2c96c17](https://github.com/giuspen/cherrytree/tree/44aee2c96c1725e896138e6c786522e303dab55d) |
| [infobyte/faraday](https://github.com/infobyte/faraday) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [ad91a06cc0f9](https://github.com/infobyte/faraday/tree/ad91a06cc0f9adfec2eda83622c62b8637df99a4) |
| [reportportal/reportportal](https://github.com/reportportal/reportportal) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [e0bb071de9c0](https://github.com/reportportal/reportportal/tree/e0bb071de9c07dfc4c3ddaf55de621853feccf2b) |
| [Syslifters/sysreptor](https://github.com/Syslifters/sysreptor) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [7b742e0848ce](https://github.com/Syslifters/sysreptor/tree/7b742e0848ce3f434ad22e2d5f35f0b38ee28aab) |

## Practice labs

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [digininja/DVWA](https://github.com/digininja/DVWA) | 2026-10-20 | ISOLATED_LAB | Commit: no record returned | [a1978a2fed19](https://github.com/digininja/DVWA/tree/a1978a2fed195acd093010af6395f86a281537ca) |
| [juice-shop/juice-shop](https://github.com/juice-shop/juice-shop) | 2026-10-20 | ISOLATED_LAB | Commit: no record returned | [399fba761943](https://github.com/juice-shop/juice-shop/tree/399fba76194305a312693eee44f4df64bdf0c3ce) |
| [Orange-Cyberdefense/GOAD](https://github.com/Orange-Cyberdefense/GOAD) | 2026-10-20 | ISOLATED_LAB | Commit: no record returned | [992307adf944](https://github.com/Orange-Cyberdefense/GOAD/tree/992307adf944b934a3b76a2f56a637104c54b805) |
| [OWASP/crAPI](https://github.com/OWASP/crAPI) | 2026-10-20 | ISOLATED_LAB | Commit: no record returned | [b5fc307f3e5f](https://github.com/OWASP/crAPI/tree/b5fc307f3e5f875809b095b771108ef342a33724) |
| [RhinoSecurityLabs/cloudgoat](https://github.com/RhinoSecurityLabs/cloudgoat) | 2026-10-20 | ISOLATED_LAB | Commit: no record returned | [63c65bd26edc](https://github.com/RhinoSecurityLabs/cloudgoat/tree/63c65bd26edc6919499adfa20b176c450e35c33c) |
| [vulhub/vulhub](https://github.com/vulhub/vulhub) | 2026-10-20 | ISOLATED_LAB | Commit: no record returned | [9b90d4276f84](https://github.com/vulhub/vulhub/tree/9b90d4276f84feed6333286afeb7e1250379a1da) |
| [WebGoat/WebGoat](https://github.com/WebGoat/WebGoat) | 2026-10-20 | ISOLATED_LAB | Commit: no record returned | [e7b131360d74](https://github.com/WebGoat/WebGoat/tree/e7b131360d74336c0c94ab5c8a21259503f59be8) |
| [kalilinux/build-scripts/kali-live](https://gitlab.com/kalilinux/build-scripts/kali-live) | 2026-10-20 | SOURCE_CHECKED_ONLY | Commit: no record returned | [adb2e3894166](https://gitlab.com/kalilinux/build-scripts/kali-live/-/tree/adb2e38941662f105b57134e0155ec468da294ad) |

## Password & authentication assessment

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [hashcat/hashcat](https://github.com/hashcat/hashcat) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [1171851feba3](https://github.com/hashcat/hashcat/tree/1171851feba38e1daf946a46f7289bce8fe1e1b1) |
| [jmk-foofus/medusa](https://github.com/jmk-foofus/medusa) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [fef1e1f0ee91](https://github.com/jmk-foofus/medusa/tree/fef1e1f0ee91f6108a5a48d3b3c11dc4df40b122) |
| [openwall/john](https://github.com/openwall/john) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [5184bc0b8c10](https://github.com/openwall/john/tree/5184bc0b8c105f8c5978b112e723d65b2de3e63e) |
| [vanhauser-thc/thc-hydra](https://github.com/vanhauser-thc/thc-hydra) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [17b526133202](https://github.com/vanhauser-thc/thc-hydra/tree/17b52613320257a620ce3b5611b2e8196eb6e7fc) |

## Supporting system & development tools

| Source | Observation date | Status | Advisory query | Fixed source |
| --- | --- | --- | --- | --- |
| [docker/cli](https://github.com/docker/cli) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [6d274590f2f6](https://github.com/docker/cli/tree/6d274590f2f63276a54da8adf475a455d21c1fdd) |
| [gcc-mirror/gcc](https://github.com/gcc-mirror/gcc) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [ae723691c3ec](https://github.com/gcc-mirror/gcc/tree/ae723691c3ec65d1047c42f85d3b26599efa06b5) |
| [golang/go](https://github.com/golang/go) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [c0be4674865b](https://github.com/golang/go/tree/c0be4674865b06f0be851e27cef93136708be506) |
| [openssl/openssl](https://github.com/openssl/openssl) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [152ac8b6cadd](https://github.com/openssl/openssl/tree/152ac8b6cadd2cb611154f90228466cf2b4c143d) |
| [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [7894f69557f0](https://github.com/PowerShell/PowerShell/tree/7894f69557f039db23b1709f8712e89f5f511280) |
| [rfc1036/whois](https://github.com/rfc1036/whois) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [54d60d8ebaf0](https://github.com/rfc1036/whois/tree/54d60d8ebaf0034dc485a56bbb08f9f1356d7545) |
| [isc-projects/bind9](https://gitlab.isc.org/isc-projects/bind9) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [e076d40829a5](https://gitlab.isc.org/isc-projects/bind9/-/tree/e076d40829a5cf423cd3003b67aff5834b611765) |
| [debian/wget](https://salsa.debian.org/debian/wget) | 2026-10-21 | SOURCE_SCREENED_ONLY | Commit: no record returned | [6a394e49b3ce](https://salsa.debian.org/debian/wget/-/tree/6a394e49b3ce8abfbeb487eaa9c80d3982a8436b) |
