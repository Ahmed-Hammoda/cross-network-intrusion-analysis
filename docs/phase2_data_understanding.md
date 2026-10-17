# Phase 2 — Data understanding

> Template — each member fills in the section for their own datasets.
> General dataset descriptions are in `datasets.md`; attack descriptions in `attack_taxonomy.md`.

## 2.1 Data sources

See `datasets.md` (provenance, collection method, citation, download link for each dataset).

## 2.2 Per-dataset description

Copy this block for each dataset.

### `<KEY>` — `<dataset name>` (owner: <member name>)

**Dimensions**

| | Official | Loaded | Match? |
|---|---|---|---|
| Rows | | | |
| Columns | | | |

**Data types and units**

| Group | Columns | Type | Unit |
|---|---|---|---|
| Identifiers | | | |
| Ports / protocol | | | |
| Volume (bytes, packets) | | | |
| Time (duration, timestamps, IAT) | | | |
| TCP flags | | | |
| Labels | | | |

**Key variables** — the 5–8 columns most relevant to our research questions, and why.

**Class distribution** — table of flows per `Attack` label (and figure in `figures/`).

**Initial quality problems and planned solutions (no code)**

| # | Problem found | Columns / rows affected | Planned solution | Rule in `config.py`? |
|---|---|---|---|---|
| 1 | | | | |

### `IoT23` — CICIoT2023 (owner: Yassine Mtibaa)

Code: `notebooks/05_ciciot2023.ipynb` · Tables: `tables/IoT23_phase2_*.csv` · Feature dictionary: `ciciot_feature_dictionary.md`.
Every count below is computed on **all rows** (the 63 files are read in parallel; nothing is sampled except plots).

**Dimensions**

| | Official | Loaded | Match? |
|---|---|---|---|
| Rows | 46,686,579 (UNB, 2023 release; "~47 million" in `datasets.md`) | 45,019,243 | No — newer `MERGED_CSV` release |
| Columns | 46 features + label (UNB); 45 in `datasets.md` | 39 features + `Label` | No — 8 columns removed, 1 renamed, 1 added |
| Files | 169 CSV (2023 release) | 63 (`Merged01–63.csv`, 9.3 GB) | — |

The release we downloaded renames `Duration` to `Time_To_Live`, adds `IGMP`, and drops `flow_duration`,
`Srate`, `Drate`, `urg_count`, `Magnitue`, `Radius`, `Covariance` and `Weight`. All 63 files share one
column layout.

**Granularity.** One row is **one window of up to 100 packets** (`Number`, median 100), not one flow.
Features are averages, shares (0–1), counts or size statistics over the window. There is no identifier,
port or timestamp column.

**Data types and units**

| Group | Columns | Type | Unit |
|---|---|---|---|
| Identifiers | none | — | — |
| Ports / protocol | `Protocol Type`, `Header_Length`, `Time_To_Live` | int (categorical code), float, float | IANA code; bytes; hops |
| Protocol shares | `HTTP`, `HTTPS`, `DNS`, `Telnet`, `SMTP`, `SSH`, `IRC`, `TCP`, `UDP`, `DHCP`, `ARP`, `ICMP`, `IGMP`, `IPv`, `LLC` | float | share of packets in the window (0–1) |
| Volume (bytes, packets) | `Tot sum`, `Min`, `Max`, `AVG`, `Std`, `Tot size`, `Variance`, `Number` | int / float | bytes (`Variance`: bytes²); `Number`: packets |
| Time | `Rate`, `IAT` | float | packets/s; seconds |
| TCP flags | `fin/syn/rst/psh/ack/ece/cwr_flag_number`; `ack/syn/fin/rst_count` | float; int | share 0–1; packets 0–100 |
| Labels | `Label` | text | 34 labels |

**Key variables** — `Rate` (floods are defined by extreme rates), `Protocol Type` and the `TCP`/`UDP`/`ICMP`
shares (protocol × family, chi-square), the TCP flag shares (distinguish SYN, ACK, RST-FIN and PSH-ACK floods),
`AVG`/`Std`/`Min`/`Max` (packet-size profile), `IAT` (slow vs fast attacks), `Header_Length` (transport header
present or not), and `Number` (capture artefact to watch).

**Class distribution** (`tables/IoT23_phase2_labels.csv`, `figures/IoT23_class_distribution.png`)

| Family | Labels | Rows | % of rows |
|---|---|---|---|
| Denial of service | 16 | 40,282,751 | 89.48 |
| Malware and botnets (Mirai) | 3 | 2,521,731 | 5.60 |
| Benign | 1 | 1,051,373 | 2.34 |
| Reconnaissance | 5 | 661,121 | 1.47 |
| Interception and spoofing | 2 | 465,937 | 1.03 |
| Web and injection | 6 | 23,799 | 0.05 |
| Credential attacks | 1 | 12,522 | 0.03 |

Largest label `DDoS ICMP flood` (6,893,259) vs smallest `Uploading attack` (1,196): **5,764×**.
All 34 labels map to `TAXONOMY` without changes (`map_labels` normalises the UPPERCASE spellings).

**Initial quality problems and planned solutions (no code)**

| # | Problem found | Columns / rows affected | Planned solution | Rule in `config.py`? |
|---|---|---|---|---|
| 1 | Release differs from documentation | whole dataset | Use loaded numbers; `datasets.md` updated | — |
| 2 | Label column is `Label`, not `label` | `Label` | Pass `"Label"` to `map_labels` | No → decision log |
| 3 | 7 truncated lines (12–36 empty cells), 9 rows without label | Merged42/44/46/48/50/51/52 | Dropped by `clean()` (NaN rows) | Yes (`clean`) |
| 4 | 8 integer columns read as float in those files | `*_count`, `Tot sum`, `Min`, `Max`, `Number` | Resolved once the truncated lines are dropped; `downcast()` | Yes (`clean`) |
| 5 | `Std`/`Variance` NaN for single-packet windows (structural) | 670 rows, all `Number` = 1 | Dropped by `clean()`; documented | Yes (`clean`) |
| 6 | Infinite `Rate` (window of 0 s) | 991 rows, many classes | inf → NaN → dropped | Yes (`clean`) |
| 7 | Negative `IAT` (impossible) | 2 rows | Set to NaN → dropped | No → decision log |
| 8 | Exact duplicate rows | 22,976,869 rows (51.0 %), ≈ 70 % of DDoS ICMP flood | `clean()` per file, then again after concatenation | Yes (`clean`) |
| 9 | Same features with different labels | 610,472 vectors, 13,286,035 rows (29.5 %): DoS vs DDoS of the same flood type | Keep for EDA and report (RQ2); drop before any model training | No → decision log (open) |
| 10 | UPPERCASE label spellings | 33 of 34 labels | Normalised by `map_labels` | Yes (`map_labels`) |
| 11 | Extreme imbalance (benign 2.3 %, 5,764× ratio) | `Label` | `sample_per_label` (200k cap) | Yes (`sample_per_label`) |
| 12 | Redundant columns: `LLC` = `IPv`, `Tot size` = `AVG`, `Variance` = `Std`², `Tot sum` = `AVG` × `Number`, `*_count` = share × `Number` | 8 columns (0 violations on complete rows) | Remove in feature selection | No → phase 5 |
| 13 | Near-constant columns (> 99 % zeros) | `Telnet`, `SMTP`, `IRC`, `IGMP`, `DHCP`, `SSH`, `ece_flag_number`, `cwr_flag_number` | Remove in feature selection | No → phase 5 |
| 14 | Categorical code stored as number | `Protocol Type` (values 0, 1, 2, 6, 17, 47) | Encode in feature engineering | No → phase 5 |
| 15 | Structural values that look like errors | `Header_Length` = 0 (7.18 M rows, ICMP/GRE), `Max` > 1,514 B (687,281 rows, 33 % of benign), TTL = 0 (455 rows) | Keep: explained by protocol / capture | — |
| 16 | `Number` < 100 in 100 % of non-flood rows vs ≈ 0.1 % of flood rows | `Number` | Capture artefact; decide in feature selection | No → phase 5 |
| 17 | Extreme outliers | `Rate` (max 1.57 × 10⁷), `IAT` (max 78,612 s), sizes | Investigate per class in phase 3; keep legitimate attack values | No → phase 3 |
| 18 | No identifiers or timestamps; shuffled files | whole dataset | Limitation: no time- or device-based split | — |

## 2.3 Cross-dataset comparison (Cyrine Chabbar)

Table comparing the five datasets: rows, features, attack share, number of labels, network type.

## 2.4 Feature dictionaries

- NetFlow v3 — 53 features (Ahmed Hamouda): `netflow_feature_dictionary.md`
- CICIoT2023 — 45 features (Yassine Mtibaa): `ciciot_feature_dictionary.md`
