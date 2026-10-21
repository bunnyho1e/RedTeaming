# RedOS coverage — 2026-10-21

**Menu: 145 included / 2 unverified. Additional inventory: 58 included / 2 held / 14 unverified.**

These 221 entries map to **111 distinct included source projects**. Duplicate Hydra/Medusa menu entries and multi-command suites are retained as inventory rows, not counted as separate repositories. The original Impacket source already covers the 70 recorded Impacket entrypoints.

[RedOS website](https://www.redteamgarage.com/rtg/rtg-redos) · [Review findings](REDOS_REVIEW.md) · [Coverage JSON](redos-coverage.json)

## Scope

147 menu entries plus 74 additional normalized tools/collections/commands. About 4.28 GiB of VDI data was not recovered after the official download hit its quota; this is not a complete VM SBOM.

Matches tool/source identities; new pins do not claim byte-for-byte equality with VM-installed versions.

Docker maps to the official Docker CLI source, without a claim to include the daemon/Desktop. `nc/netcat` maps to Debian OpenBSD netcat; the VM alternative was not conclusively established. GDB/GEF/PEDA are separate sources; none is loaded automatically.

## Main menu

| Tool | Command | Status | Source(s) / reason |
| --- | --- | --- | --- |
| amass | `amass` | INCLUDED | [owasp-amass/amass](https://github.com/owasp-amass/amass) |
| asnmap | `asnmap` | INCLUDED | [projectdiscovery/asnmap](https://github.com/projectdiscovery/asnmap) |
| assetfinder | `assetfinder` | INCLUDED | [tomnomnom/assetfinder](https://github.com/tomnomnom/assetfinder) |
| crt.sh upit preko curl-a | `curl` | INCLUDED | [curl/curl](https://github.com/curl/curl) |
| dnsenum | `dnsenum` | INCLUDED | [SparrowOchon/dnsenum2](https://github.com/SparrowOchon/dnsenum2) |
| dnsx | `dnsx` | INCLUDED | [projectdiscovery/dnsx](https://github.com/projectdiscovery/dnsx) |
| exiftool | `exiftool` | INCLUDED | [exiftool/exiftool](https://github.com/exiftool/exiftool) |
| gau | `gau` | INCLUDED | [lc/gau](https://github.com/lc/gau) |
| gowitness | `gowitness` | INCLUDED | [sensepost/gowitness](https://github.com/sensepost/gowitness) |
| httpx | `httpx` | INCLUDED | [projectdiscovery/httpx](https://github.com/projectdiscovery/httpx) |
| katana | `katana` | INCLUDED | [projectdiscovery/katana](https://github.com/projectdiscovery/katana) |
| knockpy | `knockpy` | INCLUDED | [guelfoweb/knockpy](https://github.com/guelfoweb/knockpy) |
| masscan | `masscan` | INCLUDED | [robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) |
| nmap | `nmap` | INCLUDED | [nmap/nmap](https://github.com/nmap/nmap) |
| puredns | `puredns` | INCLUDED | [d3mondev/puredns](https://github.com/d3mondev/puredns) |
| sherlock | `sherlock` | INCLUDED | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) |
| subfinder | `subfinder` | INCLUDED | [projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder) |
| theHarvester | `theHarvester` | INCLUDED | [laramies/theHarvester](https://github.com/laramies/theHarvester) |
| tshark | `tshark` | INCLUDED | [wireshark/wireshark](https://gitlab.com/wireshark/wireshark) |
| waybackurls | `waybackurls` | INCLUDED | [tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls) |
| feroxbuster | `feroxbuster` | INCLUDED | [epi052/feroxbuster](https://github.com/epi052/feroxbuster) |
| ffuf | `ffuf` | INCLUDED | [ffuf/ffuf](https://github.com/ffuf/ffuf) |
| gobuster | `gobuster` | INCLUDED | [OJ/gobuster](https://github.com/OJ/gobuster) |
| nikto | `nikto` | INCLUDED | [sullo/nikto](https://github.com/sullo/nikto) |
| nuclei | `nuclei` | INCLUDED | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) |
| wapiti | `wapiti` | INCLUDED | [wapiti-scanner/wapiti](https://github.com/wapiti-scanner/wapiti) |
| wfuzz | `wfuzz` | INCLUDED | [xmendez/wfuzz](https://github.com/xmendez/wfuzz) |
| WPScan | `wpscan` | INCLUDED | [wpscanteam/wpscan](https://github.com/wpscanteam/wpscan) |
| arjun | `arjun` | INCLUDED | [s0md3v/Arjun](https://github.com/s0md3v/Arjun) |
| crlfuzz | `crlfuzz` | INCLUDED | [dwisiswant0/crlfuzz](https://github.com/dwisiswant0/crlfuzz) |
| dalfox | `dalfox` | INCLUDED | [hahwul/dalfox](https://github.com/hahwul/dalfox) |
| dirsearch | `dirsearch` | INCLUDED | [maurosoria/dirsearch](https://github.com/maurosoria/dirsearch) |
| mitmproxy | `mitmproxy` | INCLUDED | [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy) |
| sqlmap | `sqlmap` | INCLUDED | [sqlmapproject/sqlmap](https://github.com/sqlmapproject/sqlmap) |
| hydra | `hydra` | INCLUDED | [vanhauser-thc/thc-hydra](https://github.com/vanhauser-thc/thc-hydra) |
| medusa | `medusa` | INCLUDED | [jmk-foofus/medusa](https://github.com/jmk-foofus/medusa) |
| Metasploit Framework | `msfconsole` | INCLUDED | [rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework) |
| searchsploit | `searchsploit` | INCLUDED | [exploit-database/exploitdb](https://gitlab.com/exploit-database/exploitdb) |
| addcomputer.py | `addcomputer.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| adidnsdump | `adidnsdump` | INCLUDED | [dirkjanm/adidnsdump](https://github.com/dirkjanm/adidnsdump) |
| atexec.py | `atexec.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| attrib.py | `attrib.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| badsuccessor.py | `badsuccessor.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| bloodhound-python | `bloodhound-python` | INCLUDED | [dirkjanm/BloodHound.py](https://github.com/dirkjanm/BloodHound.py) |
| certipy-ad | `certipy` | INCLUDED | [ly4k/Certipy](https://github.com/ly4k/Certipy) |
| changepasswd.py | `changepasswd.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| CheckLDAPStatus.py | `CheckLDAPStatus.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| checkMSSQLStatus.py | `checkMSSQLStatus.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| dacledit.py | `dacledit.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| dcomexec.py | `dcomexec.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| describeTicket.py | `describeTicket.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| dpapi.py | `dpapi.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| dpapidump.py | `dpapidump.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| DumpNTLMInfo.py | `DumpNTLMInfo.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| esentutl.py | `esentutl.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| evil-winrm (Python) | `evil-winrm-py` | INCLUDED | [adityatelange/evil-winrm-py](https://github.com/adityatelange/evil-winrm-py) |
| exchanger.py | `exchanger.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| filetime.py | `filetime.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| findDelegation.py | `findDelegation.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| Get-GPPPassword.py | `Get-GPPPassword.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| GetADComputers.py | `GetADComputers.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| GetADUsers.py | `GetADUsers.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| getArch.py | `getArch.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| GetLAPSPassword.py | `GetLAPSPassword.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| GetNPUsers.py | `GetNPUsers.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| getPac.py | `getPac.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| getST.py | `getST.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| getTGT.py | `getTGT.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| GetUserSPNs.py | `GetUserSPNs.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| goldenPac.py | `goldenPac.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| impacket-secretsdump | `impacket-secretsdump` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| karmaSMB.py | `karmaSMB.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| kerbrute | `kerbrute` | INCLUDED | [ropnop/kerbrute](https://github.com/ropnop/kerbrute) |
| keylistattack.py | `keylistattack.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| kintercept.py | `kintercept.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| ldapdomaindump | `ldapdomaindump` | INCLUDED | [dirkjanm/ldapdomaindump](https://github.com/dirkjanm/ldapdomaindump) |
| lookupsid.py | `lookupsid.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| machine_role.py | `machine_role.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| mimikatz.py | `mimikatz.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| mqtt_check.py | `mqtt_check.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| mssqlclient.py | `mssqlclient.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| mssqlinstance.py | `mssqlinstance.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| net.py | `net.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| netview.py | `netview.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| ntfs-read.py | `ntfs-read.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| ntlmrelayx.py | `ntlmrelayx.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| owneredit.py | `owneredit.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| ping.py | `ping.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| ping6.py | `ping6.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| psexec.py | `psexec.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| raiseChild.py | `raiseChild.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| rbcd.py | `rbcd.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| rdp_check.py | `rdp_check.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| reg.py | `reg.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| registry-read.py | `registry-read.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| regsecrets.py | `regsecrets.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| Responder | `responder` | INCLUDED | [lgandx/Responder](https://github.com/lgandx/Responder) |
| rpcdump.py | `rpcdump.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| rpcmap.py | `rpcmap.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| sambaPipe.py | `sambaPipe.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| samedit.py | `samedit.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| samrdump.py | `samrdump.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| services.py | `services.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| smbclient.py | `smbclient.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| smbexec.py | `smbexec.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| smbserver.py | `smbserver.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| sniff.py | `sniff.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| sniffer.py | `sniffer.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| split.py | `split.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| ticketConverter.py | `ticketConverter.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| ticketer.py | `ticketer.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| tstool.py | `tstool.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| wmiexec.py | `wmiexec.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| wmipersist.py | `wmipersist.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| wmiquery.py | `wmiquery.py` | INCLUDED | [fortra/impacket](https://github.com/fortra/impacket) |
| LinEnum | `linenum` | INCLUDED | [rebootuser/LinEnum](https://github.com/rebootuser/LinEnum) |
| linpeas | `linpeas` | INCLUDED | [peass-ng/PEASS-ng](https://github.com/peass-ng/PEASS-ng) |
| pwntools | `python3` | INCLUDED | [Gallopsled/pwntools](https://github.com/Gallopsled/pwntools) |
| cewl | `cewl` | INCLUDED | [digininja/CeWL](https://github.com/digininja/CeWL) |
| crunch | `crunch` | INCLUDED | [debian/crunch](https://salsa.debian.org/debian/crunch) |
| hashcat | `hashcat` | INCLUDED | [hashcat/hashcat](https://github.com/hashcat/hashcat) |
| hydra (auth brute) | `hydra` | INCLUDED | [vanhauser-thc/thc-hydra](https://github.com/vanhauser-thc/thc-hydra) |
| medusa (auth brute) | `medusa` | INCLUDED | [jmk-foofus/medusa](https://github.com/jmk-foofus/medusa) |
| aircrack-ng | `aircrack-ng` | INCLUDED | [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) |
| aireplay-ng | `aireplay-ng` | INCLUDED | [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) |
| airodump-ng | `airodump-ng` | INCLUDED | [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) |
| bettercap | `bettercap` | INCLUDED | [bettercap/bettercap](https://github.com/bettercap/bettercap) |
| bully | `bully` | INCLUDED | [aanarchyy/bully](https://github.com/aanarchyy/bully) |
| hcxdumptool | `hcxdumptool` | INCLUDED | [ZerBea/hcxdumptool](https://github.com/ZerBea/hcxdumptool) |
| reaver | `reaver` | INCLUDED | [t6x/reaver-wps-fork-t6x](https://github.com/t6x/reaver-wps-fork-t6x) |
| binwalk | `binwalk` | INCLUDED | [ReFirmLabs/binwalk](https://github.com/ReFirmLabs/binwalk) |
| gdb + GEF/PEDA | `gdb` | INCLUDED | [binutils-gdb](https://sourceware.org/git/?p=binutils-gdb.git), [hugsy/gef](https://github.com/hugsy/gef), [longld/peda](https://github.com/longld/peda) |
| Ghidra | `ghidra` | INCLUDED | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) |
| ltrace | `ltrace` | INCLUDED | [cespedes/ltrace](https://gitlab.com/cespedes/ltrace) |
| radare2 | `r2` | INCLUDED | [radareorg/radare2](https://github.com/radareorg/radare2) |
| strace | `strace` | INCLUDED | [strace/strace](https://github.com/strace/strace) |
| aws-cli | `aws` | INCLUDED | [aws/aws-cli](https://github.com/aws/aws-cli) |
| pacu | `pacu` | INCLUDED | [RhinoSecurityLabs/pacu](https://github.com/RhinoSecurityLabs/pacu) |
| ScoutSuite | `scout` | INCLUDED | [nccgroup/ScoutSuite](https://github.com/nccgroup/ScoutSuite) |
| garak | `garak` | INCLUDED | [NVIDIA/garak](https://github.com/NVIDIA/garak) |
| rtg-ai | `rtg-ai` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| rtg-tools | `rtg-tools` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| apktool | `apktool` | INCLUDED | [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) |
| dex2jar | `d2j-dex2jar` | INCLUDED | [pxb1988/dex2jar](https://github.com/pxb1988/dex2jar) |
| frida-tools | `frida` | INCLUDED | [frida/frida-tools](https://github.com/frida/frida-tools) |
| jadx | `jadx` | INCLUDED | [skylot/jadx](https://github.com/skylot/jadx) |
| objection | `objection` | INCLUDED | [sensepost/objection](https://github.com/sensepost/objection) |

## Additional inventory

| Tool | Command | Status | Source(s) / reason |
| --- | --- | --- | --- |
| Cirecon | `cirecon` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| RTG Specter | `rtg_specter` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| RTG Ghost C2 CE | `rtg-ghost-c2` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| rtg-llmprobe | `rtg-llmprobe` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| rtg-llmfuzz | `rtg-llmfuzz` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| rtg-jailbreaker | `rtg-jailbreaker` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| rtg-llmscout | `rtg-llmscout` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| rtg-recon | `rtg-recon` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| rtg-report | `rtg-report` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| rtg-mutate | `rtg-mutate` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| RTG Toolkit | `rtg-toolkit` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| RTG Tool Manager | `rtg-toolkit-manager` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| RTG Toolkit Importer | `rtg-toolkit-import` | UNVERIFIED | No canonical public source, reviewable version and redistribution terms verified for this RTG component. VM binaries were not copied. |
| SecLists | `seclists` | INCLUDED | [danielmiessler/SecLists](https://github.com/danielmiessler/SecLists) |
| PayloadsAllTheThings | `payloadsallthethings` | INCLUDED | [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) |
| PowerSploit | `powersploit` | HELD | Archived; conservative existing policy retained. |
| Nishang | `nishang` | HELD | PowerShell 2 module-import exclusion condition admits Keylogger; see REDOS_REVIEW.md. |
| GTFOBins | `gtfobins` | INCLUDED | [GTFOBins/GTFOBins.github.io](https://github.com/GTFOBins/GTFOBins.github.io) |
| LOLBAS | `lolbas` | INCLUDED | [LOLBAS-Project/LOLBAS](https://github.com/LOLBAS-Project/LOLBAS) |
| exploitdb | `exploitdb` | INCLUDED | [exploit-database/exploitdb](https://gitlab.com/exploit-database/exploitdb) |
| exploit-suggester | `exploit-suggester` | UNVERIFIED | Only /opt/rtg/tools/exploit-suggester was established; no exact upstream identity/version was recovered. No similarly named project was substituted. |
| naabu | `naabu` | INCLUDED | [projectdiscovery/naabu](https://github.com/projectdiscovery/naabu) |
| dnsrecon | `dnsrecon` | INCLUDED | [darkoperator/dnsrecon](https://github.com/darkoperator/dnsrecon) |
| fierce | `fierce` | INCLUDED | [mschwager/fierce](https://github.com/mschwager/fierce) |
| whatweb | `whatweb` | INCLUDED | [urbanadventurer/WhatWeb](https://github.com/urbanadventurer/WhatWeb) |
| nbtscan | `nbtscan` | INCLUDED | [resurrecting-open-source-projects/nbtscan](https://github.com/resurrecting-open-source-projects/nbtscan) |
| onesixtyone | `onesixtyone` | INCLUDED | [trailofbits/onesixtyone](https://github.com/trailofbits/onesixtyone) |
| tcpdump | `tcpdump` | INCLUDED | [the-tcpdump-group/tcpdump](https://github.com/the-tcpdump-group/tcpdump) |
| anew | `anew` | INCLUDED | [tomnomnom/anew](https://github.com/tomnomnom/anew) |
| cdncheck | `cdncheck` | INCLUDED | [projectdiscovery/cdncheck](https://github.com/projectdiscovery/cdncheck) |
| mapcidr | `mapcidr` | INCLUDED | [projectdiscovery/mapcidr](https://github.com/projectdiscovery/mapcidr) |
| qsreplace | `qsreplace` | INCLUDED | [tomnomnom/qsreplace](https://github.com/tomnomnom/qsreplace) |
| shuffledns | `shuffledns` | INCLUDED | [projectdiscovery/shuffledns](https://github.com/projectdiscovery/shuffledns) |
| tlsx | `tlsx` | INCLUDED | [projectdiscovery/tlsx](https://github.com/projectdiscovery/tlsx) |
| John the Ripper | `john` | INCLUDED | [openwall/john](https://github.com/openwall/john) |
| msfvenom | `msfvenom` | INCLUDED | [rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework) |
| Evil-WinRM (Ruby) | `evil-winrm` | INCLUDED | [Hackplayers/evil-winrm](https://github.com/Hackplayers/evil-winrm) |
| PowerShell | `pwsh` | INCLUDED | [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) |
| WinPEAS | `winpeas` | INCLUDED | [peass-ng/PEASS-ng](https://github.com/peass-ng/PEASS-ng) |
| wifite | `wifite` | INCLUDED | [derv82/wifite2](https://github.com/derv82/wifite2) |
| pixiewps | `pixiewps` | INCLUDED | [wiire-a/pixiewps](https://github.com/wiire-a/pixiewps) |
| airmon-ng | `airmon-ng` | INCLUDED | [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) |
| airbase-ng | `airbase-ng` | INCLUDED | [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) |
| airdecap-ng | `airdecap-ng` | INCLUDED | [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) |
| airdecloak-ng | `airdecloak-ng` | INCLUDED | [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) |
| airolib-ng | `airolib-ng` | INCLUDED | [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) |
| airserv-ng | `airserv-ng` | INCLUDED | [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) |
| airtun-ng | `airtun-ng` | INCLUDED | [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) |
| Proxychains / Proxychains4 | `proxychains4` | INCLUDED | [rofl0r/proxychains-ng](https://github.com/rofl0r/proxychains-ng) |
| Socat | `socat` | INCLUDED | [socat](https://tracker.debian.org/pkg/socat) |
| Ncat | `ncat` | INCLUDED | [nmap/nmap](https://github.com/nmap/nmap) |
| nc / netcat | `netcat` | INCLUDED | [debian/netcat-openbsd](https://salsa.debian.org/debian/netcat-openbsd) |
| Tor | `tor` | INCLUDED | [torproject/tor](https://gitlab.com/torproject/tor) |
| torsocks | `torsocks` | INCLUDED | [pkg-privacy-team/torsocks](https://salsa.debian.org/pkg-privacy-team/torsocks) |
| MobSF | `mobsf` | INCLUDED | [MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) |
| JADX GUI | `jadx-gui` | INCLUDED | [skylot/jadx](https://github.com/skylot/jadx) |
| dex2jar pomoćni alati | `dex2jar-helpers` | INCLUDED | [pxb1988/dex2jar](https://github.com/pxb1988/dex2jar) |
| rabin2 | `rabin2` | INCLUDED | [radareorg/radare2](https://github.com/radareorg/radare2) |
| rax2 | `rax2` | INCLUDED | [radareorg/radare2](https://github.com/radareorg/radare2) |
| rafind2 | `rafind2` | INCLUDED | [radareorg/radare2](https://github.com/radareorg/radare2) |
| GCC | `gcc` | INCLUDED | [gcc-mirror/gcc](https://github.com/gcc-mirror/gcc) |
| Go | `go` | INCLUDED | [golang/go](https://github.com/golang/go) |
| objdump | `objdump` | INCLUDED | [binutils-gdb](https://sourceware.org/git/?p=binutils-gdb.git) |
| readelf | `readelf` | INCLUDED | [binutils-gdb](https://sourceware.org/git/?p=binutils-gdb.git) |
| strings | `strings` | INCLUDED | [binutils-gdb](https://sourceware.org/git/?p=binutils-gdb.git) |
| Docker | `docker` | INCLUDED | [docker/cli](https://github.com/docker/cli) |
| OpenSSL | `openssl` | INCLUDED | [openssl/openssl](https://github.com/openssl/openssl) |
| curl | `curl` | INCLUDED | [curl/curl](https://github.com/curl/curl) |
| wget | `wget` | INCLUDED | [debian/wget](https://salsa.debian.org/debian/wget) |
| dig | `dig` | INCLUDED | [isc-projects/bind9](https://gitlab.isc.org/isc-projects/bind9) |
| host | `host` | INCLUDED | [isc-projects/bind9](https://gitlab.isc.org/isc-projects/bind9) |
| whois | `whois` | INCLUDED | [rfc1036/whois](https://github.com/rfc1036/whois) |
| traceroute | `traceroute` | INCLUDED | [traceroute](https://tracker.debian.org/pkg/traceroute) |
| tcptraceroute | `tcptraceroute` | INCLUDED | [mct/tcptraceroute](https://github.com/mct/tcptraceroute) |
