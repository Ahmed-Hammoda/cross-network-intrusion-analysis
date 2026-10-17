# Dataset catalogue

Five datasets from five network environments. The four NetFlow v3 datasets share the same
53 features and are merged into one unified dataset. CICIoT2023 uses a different feature set,
so it is analysed separately and linked to the others through the shared attack taxonomy
(see `attack_taxonomy.md`).

## Summary

| Key | Dataset | Network environment | Flows | Attack share | Attack classes | Features | Owner |
|---|---|---|---|---|---|---|---|
| `UNSW` | NF-UNSW-NB15-v3 | Mixed lab network | 2,365,424 | 5.4% | 9 | 53 | Ahmed Hamouda |
| `CIC18` | NF-CSE-CIC-IDS2018-v3 | Enterprise / office network | 20,115,529 | 12.93% | 6 | 53 | Ahmed Hamouda |
| `ToN` | NF-ToN-IoT-v3 | IoT / industrial network | 27,520,260 | 38.98% | 9 | 53 | Cyrine Chabbar |
| `BoT` | NF-BoT-IoT-v3 | IoT botnet network | 16,993,808 | 99.7% | 4 | 53 | Cyrine Chabbar |
| `IoT23` | CICIoT2023 | Real IoT devices (105) | ~47 million | — | 33 | 45 | Yassine Mtibaa |
| | **Total** | | **~114 million** | | **54 labels** | | |

---

## What NetFlow v3 means

The University of Queensland team took the original raw traffic captures (PCAP files) of four
well-known benchmark datasets and re-extracted every flow with the same tool (nProbe) into
the same NetFlow format. Version 3 (2025) has 53 features, including new temporal features
(flow start/end timestamps and inter-packet arrival-time statistics in both directions).

**Why this matters for us:** a feature such as flow duration means exactly the same thing in all
four files, so stacking them into one dataset is valid. The original versions of these datasets
used different feature tools and could not be merged directly.

- Source: https://staff.itee.uq.edu.au/marius/NIDS_datasets/ (use the **v3** links)
- Citation: Luay, M., Layeghy, S., Hosseininoorbin, S., Sarhan, M., Moustafa, N., Portmann, M. (2025).
  *Temporal Analysis of NetFlow Datasets for Network Intrusion Detection Systems*. arXiv:2503.04404.
- Label columns: `Label` (0 = benign, 1 = attack) and `Attack` (class name)

---

## 1. NF-UNSW-NB15-v3 — mixed lab network

| | |
|---|---|
| Original dataset | UNSW-NB15, Australian Centre for Cyber Security (UNSW Canberra), 2015 |
| How it was made | Synthetic normal and attack traffic generated with the IXIA PerfectStorm tool in a cyber range lab |
| Flows | 2,365,424 (127,639 attacks, 2,237,731 benign) |
| Attack classes | Fuzzers, Analysis, Backdoor, DoS, Exploits, Generic, Reconnaissance, Shellcode, Worms |
| Why we use it | The widest variety of attack types; the only source of Exploits, Shellcode, Worms, Fuzzers, Generic |
| Known issues | Strong imbalance (94.6% benign); Worms has only 158 flows; "Generic" and "Analysis" are broad umbrella categories |

## 2. NF-CSE-CIC-IDS2018-v3 — enterprise / office network

| | |
|---|---|
| Original dataset | CSE-CIC-IDS2018, Communications Security Establishment + Canadian Institute for Cybersecurity, 2018 |
| How it was made | A full organisation network simulated on AWS, with many victim machines and separate attacker machines, over 10 days |
| Flows | 20,115,529 (2,600,903 attacks, 17,514,626 benign) |
| Attack classes | BruteForce, Bot, DoS, DDoS, Infiltration, Web Attacks |
| Why we use it | The most realistic office network in our set; the only source of Bot and Infiltration |
| Known issues | Large file; Web Attacks has only 2,538 flows; label noise in the original CIC datasets is documented in the literature |

## 3. NF-ToN-IoT-v3 — IoT / industrial network

| | |
|---|---|
| Original dataset | ToN-IoT, UNSW Canberra Cyber Range and IoT Labs |
| How it was made | A testbed combining IoT and industrial IoT devices, cloud and edge layers, with scripted attacks |
| Flows | 27,520,260 (10,728,046 attacks, 16,792,214 benign) — the largest file |
| Attack classes | Backdoor, DoS, DDoS, Injection, MITM, Password, Ransomware, Scanning, XSS |
| Why we use it | The only source of Ransomware, MITM, Injection, XSS and Password attacks |
| Known issues | Very large; Ransomware (3,971) and MITM (6,013) are rare |

## 4. NF-BoT-IoT-v3 — IoT botnet network

| | |
|---|---|
| Original dataset | BoT-IoT, UNSW Canberra Cyber Range Lab |
| How it was made | Simulated IoT devices attacked by botnet traffic |
| Flows | 16,993,808 (16,881,819 attacks, 51,989 benign) |
| Attack classes | DDoS, DoS, Reconnaissance, Theft |
| Why we use it | Large-scale IoT botnet floods; the only source of Theft (data theft, keylogging) |
| Known issues | Almost entirely attacks (only 0.3% benign) — not used to describe normal traffic; Theft has only 1,651 flows |

## 5. CICIoT2023 — real IoT devices

| | |
|---|---|
| Source | Canadian Institute for Cybersecurity, University of New Brunswick, 2023 |
| How it was made | 33 attacks run in an IoT topology of 105 real devices, where the attackers are themselves compromised IoT devices |
| Size | Almost 47 million records, split across many CSV files |
| Attack classes | 33 specific attacks in 7 categories: DDoS, DoS, Recon, Web-based, Brute Force, Spoofing, Mirai |
| Why we use it | Newest dataset; real devices; the only source of Spoofing and Mirai; labels at the specific-technique level |
| Why it is not merged | Different extraction tool and 45 different features, measured differently from NetFlow — merging would mix incompatible measurements |
| Download | https://www.unb.ca/cic/datasets/iotdataset-2023.html (CSV folder, not the PCAPs) |
| Citation | Neto, E.C.P. et al. (2023). *CICIoT2023: A Real-Time Dataset and Benchmark for Large-Scale Attacks in IoT Environment*. Sensors 23(13), 5941. |

---

## Memory and disk plan

The full data is ~114 million rows, more than a 32 GB laptop can hold at once. So:
load one file at a time → clean → map labels → sample (cap 200k flows per label, keep every
flow of rarer labels) → save Parquet → free memory. Rare attacks are never lost.
