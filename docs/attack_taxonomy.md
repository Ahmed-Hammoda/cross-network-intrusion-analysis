# Attack taxonomy

Every attack label in the project, grouped into 9 families. Each flow in our cleaned data gets two
columns: `attack_family` (9 values + Benign) and `attack_label` (54 values + Benign). The mapping
is implemented in `src/config.py` (`TAXONOMY`) and must not be changed without a team decision.

**Why two levels?** Family level gives every rare attack enough data for statistical tests;
label level keeps the detail for future modelling.

**Dataset keys:** `UNSW` NF-UNSW-NB15-v3 · `CIC18` NF-CSE-CIC-IDS2018-v3 · `ToN` NF-ToN-IoT-v3 ·
`BoT` NF-BoT-IoT-v3 · `IoT23` CICIoT2023

## Overview

| # | Family | Labels | Sources | What these attacks have in common |
|---|---|---|---|---|
| 1 | Denial of service | 18 | all 5 | Make a service unavailable by exhausting its resources |
| 2 | Reconnaissance | 8 | UNSW, ToN, BoT, IoT23 | Gather information about hosts and services before an attack |
| 3 | Credential attacks | 3 | CIC18, ToN, IoT23 | Obtain usernames and passwords |
| 4 | Web and injection | 9 | CIC18, ToN, IoT23 | Abuse web applications or send malicious input |
| 5 | Malware and botnets | 7 | UNSW, CIC18, ToN, IoT23 | Malicious software installed on, or controlling, a victim |
| 6 | Exploitation and intrusion | 3 | UNSW, CIC18 | Use a vulnerability to gain control of a host |
| 7 | Interception and spoofing | 3 | ToN, IoT23 | Place the attacker between victims or impersonate a host |
| 8 | Fuzzing and crypto | 2 | UNSW | Malformed input and attacks on encryption |
| 9 | Data theft | 1 | BoT | Steal sensitive data from a victim |
| | **Total** | **54** | | |

Families with labels in several datasets (Denial of service, Reconnaissance, Credential attacks,
Web and injection, Malware and botnets) are the ones used to compare networks (SQ3).

---

## 1. Denial of service (18 labels)

**Goal:** overload a target (server, network link, device) so legitimate users cannot reach it.
**DoS** uses one source; **DDoS** uses many sources at once, which makes it larger and harder to block.
**Traffic signature:** very high packet or connection rates, many short or half-open flows, unusual flag patterns.

| Label | Source | Description |
|---|---|---|
| DoS | UNSW, CIC18, ToN, BoT | Single-source attempt to exhaust a system's resources. In CIC18 this covers HTTP floods (Hulk, GoldenEye) and slow attacks (Slowloris, SlowHTTPTest) |
| DDoS | CIC18, ToN, BoT | The same goal from many distributed sources. In CIC18 it covers LOIC (HTTP and UDP) and HOIC tools |
| DDoS ACK fragmentation | IoT23 | Flood of fragmented TCP ACK packets that the victim must reassemble |
| DDoS UDP flood | IoT23 | Large volume of UDP packets to random ports, forcing the victim to reply or drop |
| DDoS SlowLoris | IoT23 | Opens many HTTP connections and keeps them open with partial requests, exhausting the server's connection slots |
| DDoS ICMP flood | IoT23 | Floods the victim with ICMP echo (ping) requests |
| DDoS RST-FIN flood | IoT23 | Floods packets with RST and FIN flags set, forcing connection-table lookups |
| DDoS PSH-ACK flood | IoT23 | Floods packets with PSH and ACK flags, mimicking data transfer |
| DDoS HTTP flood | IoT23 | Many seemingly legitimate HTTP requests that exhaust the web server |
| DDoS UDP fragmentation | IoT23 | Large fragmented UDP packets that consume reassembly resources |
| DDoS ICMP fragmentation | IoT23 | Fragmented ICMP packets that consume reassembly resources |
| DDoS TCP flood | IoT23 | High-volume TCP packets to overload the victim's stack |
| DDoS SYN flood | IoT23 | Many TCP SYN packets without completing the handshake, filling the half-open connection table |
| DDoS Synonymous-IP flood | IoT23 | SYN flood where the spoofed source address equals the destination address |
| DoS TCP flood | IoT23 | Single-source TCP flood |
| DoS HTTP flood | IoT23 | Single-source HTTP request flood |
| DoS SYN flood | IoT23 | Single-source SYN flood |
| DoS UDP flood | IoT23 | Single-source UDP flood |

## 2. Reconnaissance (8 labels)

**Goal:** map the network before attacking — which hosts are alive, which ports are open, which
software and versions run. Usually the first stage of a larger attack.
**Traffic signature:** one source contacting many destinations or ports, very short flows, few bytes, many failed connections.

| Label | Source | Description |
|---|---|---|
| Reconnaissance | UNSW, BoT | Gathering information about a network host (also called probing) |
| Scanning | ToN | A group of techniques that discover hosts and services on a network |
| Analysis | UNSW | Varied intrusions against web applications through ports, emails and scripts (includes port scans and spam) |
| Ping sweep | IoT23 | ICMP echo requests across an address range to find live hosts |
| OS scan | IoT23 | Probes whose responses reveal the target's operating system |
| Vulnerability scan | IoT23 | Automated checks of hosts against known vulnerabilities |
| Port scan | IoT23 | Probing many ports on a host to find open services |
| Host discovery | IoT23 | Finding which devices are present and active on the network |

## 3. Credential attacks (3 labels)

**Goal:** obtain valid usernames and passwords to log in as a legitimate user.
**Traffic signature:** many repeated connections to the same login service (SSH, FTP, web login), similar sizes, mostly failed.

| Label | Source | Description |
|---|---|---|
| BruteForce | CIC18 | Trying many username/password combinations from a predefined list (FTP and SSH in CIC18) |
| Password | ToN | Attacks that retrieve passwords by brute force or by sniffing traffic |
| Dictionary brute force | IoT23 | Trying passwords from a dictionary of common or leaked passwords |

## 4. Web and injection (9 labels)

**Goal:** abuse a web application — run commands on the server, read its database, or attack its users.
**Traffic signature:** traffic to web ports with unusual request sizes and patterns; often low volume, which makes these attacks hard to see in flow statistics.

| Label | Source | Description |
|---|---|---|
| Web Attacks | CIC18 | A group including SQL injection, command injection and unrestricted file upload |
| Injection | ToN | Sending untrusted input that changes how a program runs (mainly SQL and code injection) |
| XSS | ToN | Cross-site scripting: injecting malicious scripts into a web app so they run in other users' browsers |
| SQL injection | IoT23 | Malicious SQL in input fields to read or modify the database |
| Command injection | IoT23 | Input that makes the server run operating-system commands |
| XSS | IoT23 | Cross-site scripting (same technique as in ToN) |
| Uploading attack | IoT23 | Uploading a malicious file (e.g. a web shell) through an upload feature |
| Browser hijacking | IoT23 | Changing a victim's browser settings or redirecting it to attacker pages |
| Backdoor malware | IoT23 | Installing a backdoor through a web vulnerability (kept in this family because CICIoT2023 classifies it as web-based) |

## 5. Malware and botnets (7 labels)

**Goal:** run malicious software on the victim — to control it remotely, encrypt its files, or spread further.
**Traffic signature:** periodic command-and-control connections, unusual destinations, self-propagating scan patterns.

| Label | Source | Description |
|---|---|---|
| Bot | CIC18 | Infected machines remotely controlled by an attacker to perform malicious activities |
| Backdoor | UNSW, ToN | A hidden way to bypass normal authentication and access a system remotely |
| Ransomware | ToN | Encrypts the victim's files and demands payment for the decryption key |
| Worms | UNSW | Malware that copies itself and spreads to other computers on its own |
| Mirai GRE-IP flood | IoT23 | Mirai-infected IoT devices flooding GRE-encapsulated IP packets |
| Mirai GRE-Eth flood | IoT23 | Mirai-infected IoT devices flooding GRE-encapsulated Ethernet frames |
| Mirai UDP-Plain | IoT23 | Mirai-infected IoT devices flooding plain UDP packets at high rate |

## 6. Exploitation and intrusion (3 labels)

**Goal:** use a software vulnerability to execute code on, or gain access inside, a target.

| Label | Source | Description |
|---|---|---|
| Exploits | UNSW | Commands that take control of a host through a known vulnerability |
| Shellcode | UNSW | Small payload code injected into a vulnerable program to give the attacker control |
| Infiltration | CIC18 | Insider attack: a malicious file sent by email exploits an application, then a backdoor scans the internal network |

## 7. Interception and spoofing (3 labels)

**Goal:** sit between communicating devices to read or alter their traffic, often by impersonating another host.

| Label | Source | Description |
|---|---|---|
| MITM | ToN | Man-in-the-middle: the attacker places itself between a victim and the host it talks to |
| ARP spoofing | IoT23 | Fake ARP replies link the attacker's MAC address to another host's IP, redirecting local traffic through the attacker (a MITM technique) |
| DNS spoofing | IoT23 | Forged DNS answers send the victim to an attacker-controlled address |

## 8. Fuzzing and crypto (2 labels)

| Label | Source | Description |
|---|---|---|
| Fuzzers | UNSW | Sending large amounts of random or malformed data to crash a program or reveal vulnerabilities |
| Generic | UNSW | Attacks against block ciphers that try to produce collisions, regardless of the cipher's configuration |

## 9. Data theft (1 label)

| Label | Source | Description |
|---|---|---|
| Theft | BoT | Attacks that steal sensitive information, such as data exfiltration and keylogging |

---

## Rare classes to watch

These labels have very few flows. They are always kept in full (never sampled down) and are
analysed mainly at family level:

| Label | Source | Flows |
|---|---|---|
| Worms | UNSW | 158 |
| Backdoor | UNSW | 1,226 |
| Theft | BoT | 1,651 |
| Analysis | UNSW | 2,381 |
| Web Attacks | CIC18 | 2,538 |
| Ransomware | ToN | 3,971 |
| Shellcode | UNSW | 4,659 |
| DoS | UNSW | 5,980 |
| MITM | ToN | 6,013 |

## Source

Descriptions are written by the team, based on the dataset documentation:
- NetFlow v3 class descriptions — https://staff.itee.uq.edu.au/marius/NIDS_datasets/
- CICIoT2023 attack categories — Neto et al. (2023), Sensors 23(13), 5941
