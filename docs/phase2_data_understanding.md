# Phase 2 — Data understanding (data exploration and quality assessment)

> Each member fills in one section per dataset they own. General dataset descriptions are in
> [`datasets.md`](datasets.md); attack descriptions are in [`attack_taxonomy.md`](attack_taxonomy.md).
>
> **Phase 2 is diagnosis only:** find and measure the problems, and propose a solution for each.
> Nothing is changed in the data until phase 3.

The five checks below follow the structure of the course lab (Part 1, questions 1.1–1.5), adapted
from customer data to network-traffic data.

---

## 2.1 Initial data inspection

- Load the dataset and describe its structure (`df.shape`, `df.info()`, `df.head()`).
- Number of rows and columns — **compare with the official numbers** in `datasets.md`.
- Data type of each column, grouped by role:

  | Group | Example columns | Expected type | Unit |
  |---|---|---|---|
  | Identifiers | source / destination IP | text | — |
  | Ports and protocol | source / destination port, protocol, L7 protocol | integer codes (categorical) | — |
  | Volume | in/out bytes, in/out packets | integer | bytes, packets |
  | Time | flow duration, start/end timestamps, inter-arrival times | integer / float | milliseconds |
  | TCP flags | client / server TCP flags | integer bitmask (categorical) | — |
  | Labels | `Label` (0/1), `Attack` (class name) | integer / text | — |

- Obvious quality issues visible at first glance (odd types, columns full of zeros, strange labels).

**Deliverable:** a table of dimensions (official vs loaded) and a table of columns with type and unit.

## 2.2 Missing values analysis

- Count missing values per column, and the **percentage** missing per column.
- In network data, also count **infinite values** (±inf). They come from rate features divided by a
  zero duration and behave like missing values.
- Visualise the pattern: a bar chart of missing % per column (and a missing-value heatmap on a sample
  if there are many).
- For each column with missing or infinite values, propose a strategy and justify it:
  - very few rows affected → drop those rows;
  - many rows in one column → impute (median, or 0 when "nothing happened" is the true meaning) or drop the column;
  - missing only in one attack class → investigate first, it may be a property of that attack.

**Deliverable:** missing/inf table + plot + one planned strategy per affected column.

## 2.3 Data type issues

- Columns that should be **numeric** but are stored as text (`object` dtype) — e.g. numbers read
  with stray characters.
- Columns that should be **datetime**: the flow start/end timestamps are stored as integers in
  milliseconds — they must be converted before any time-based analysis.
- Columns that should be **categorical** but are stored as numbers: protocol numbers, L7 protocol
  codes, ports and TCP-flag bitmasks are codes, not quantities — averaging them is meaningless.
- Categorical values that are **inconsistent**: label spellings (e.g. `Infilteration` vs
  `Infiltration`), extra spaces, different capitalisation, CICIoT2023 label formats.
- Propose a solution for each issue.

**Deliverable:** table — column → current type → correct type → planned fix.

## 2.4 Outlier detection

- Detect outliers in numeric columns with statistical methods: **IQR rule** (below Q1 − 1.5·IQR or
  above Q3 + 1.5·IQR) and **z-score** (|z| > 3). Network features are very skewed, so also look at
  them on a log scale.
- Box plots of the key numeric variables, **split by attack family** (log scale).
- Decide which outliers are **legitimate** and which are **errors**:
  - legitimate — huge byte counts in DDoS, thousands of tiny flows in a scan: the outlier *is* the
    attack, and removing it would delete the signal we want to study;
  - errors — impossible values: negative bytes, packets or durations, end time before start time,
    ports outside 0–65535.
- Propose how to handle each type (keep and later transform legitimate ones; remove or correct errors).

**Deliverable:** outlier counts per column (IQR and z-score), box plots, legitimate-vs-error table
with the planned treatment.

## 2.5 Data consistency check

- **Duplicate records:** count exact duplicate rows, overall and per attack class.
- **Unique identifiers:** flows have no ID column (unlike `customer_id` in the lab), so check whether
  any record identifies a flow uniquely — e.g. source/destination IP + ports + start timestamp — and
  report how many collisions exist.
- **Formatting consistency:** column names (spaces, capitalisation), label spellings, and — for
  CICIoT2023 — the same label written in different ways across files.
- **Logical inconsistencies:** negative values in counts and durations, end time before start time,
  packets > 0 but bytes = 0 (or the reverse), TCP flags set on non-TCP flows, timestamps outside the
  dataset's capture period, a `Label` (0/1) that disagrees with `Attack` (Benign vs attack).

`validate(df)` in `src/config.py` runs the automatic logical checks and returns a table.

**Deliverable:** duplicate counts, identifier check, formatting findings, logical-check table.

---

## Template — copy one block per dataset

### `<KEY>` — `<dataset name>` (owner: `<member name>`)

**2.1 Initial inspection**

| | Official | Loaded | Match? |
|---|---|---|---|
| Rows | | | |
| Columns | | | |

Columns, types and units: *(table)* · First observations: *(text)*

**2.2 Missing values** — *(table + plot)*

**2.3 Data type issues** — *(table)*

**2.4 Outliers** — *(table + box plots)*

**2.5 Consistency** — *(duplicates, identifier check, formatting, logical checks)*

**Summary: problems found and planned solutions (no code)**

| # | Problem | Columns / rows affected | Planned solution | Phase 3 step |
|---|---|---|---|---|
| 1 | | | | |

---

## Completed dataset sections

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

**Outlier detection (2.4)** (`tables/IoT23_phase2_outliers.csv`, `figures/IoT23_boxplots_by_family.png`)

IQR rule and z-score on a uniform random sample of ~750k rows (quantiles need every value); minima, maxima and
physical-limit checks on all rows. The 22 share columns are bounded in [0, 1] and not tested.

| Column | Mild IQR outliers | \|z\| > 3 | Why so many / so few |
|---|---|---|---|
| `Time_To_Live` | 27.0 % | 1.9 % | IQR = 0 (most windows have TTL 64): every other value counts as an outlier |
| `Tot sum` | 25.1 % | 2.2 % | most windows are 100 × 60-byte packets; benign and web traffic carry far more bytes |
| `Max`, `AVG`, `Std` | 21–22 % | 1.5–3.1 % | floods use minimum-size packets; benign windows have large, varied packets |
| `IAT` | 13.7 % | 0.001 % | extremely skewed (skewness 866): a few very long gaps inflate the standard deviation |

The IQR rule over-flags columns dominated by one value, and the z-score under-flags because extreme values
inflate the standard deviation. Box plots by family show that a value that is extreme for the whole dataset is often
**typical for one family** (high `Rate` and short `IAT` for floods, large packets for benign and web traffic,
`Header_Length` = 0 for ICMP/GRE floods), so outliers are not removed globally.

| Value | Verdict | Rows (all data) | Planned treatment |
|---|---|---|---|
| `Rate` = inf | error (window of 0 s) | 991 | drop (3.1) |
| `IAT` < 0 | error (impossible) | 2 | drop (3.4) |
| `Rate` very high (max 1.57 × 10⁷ pkt/s) | legitimate: floods | — | keep; log transform in phase 5 |
| `Max` > 1,514 bytes | legitimate: captured before segmentation offload | 687,281 | keep, documented |
| `Header_Length` = 0 | legitimate: ICMP / GRE have no TCP/UDP header | 7,177,555 | keep |
| `Time_To_Live` = 0 | legitimate: non-IP (ARP) windows | 455 | keep |
| `IAT` > 1 hour (max 78,612 s) | doubtful but possible (idle device) | 14 | keep, flagged |

**Initial quality problems and planned solutions (no code)**

| # | Problem found | Columns / rows affected | Planned solution | Rule in `config.py`? |
|---|---|---|---|---|
| 1 | Release differs from documentation | whole dataset | Use loaded numbers; `datasets.md` updated | — |
| 2 | Label column is `Label`, not `label` | `Label` | Pass `"Label"` to `map_labels` | No → decision log |
| 3 | 7 truncated lines (12–36 empty cells), 9 rows without label | Merged42/44/46/48/50/51/52 | Dropped by `clean()` (NaN rows) | Yes (`clean`) |
| 4 | 8 integer columns read as float in those files | `*_count`, `Tot sum`, `Min`, `Max`, `Number` | Resolved once the truncated lines are dropped; `downcast()` | Yes (`clean`) |
| 5 | `Std`/`Variance` NaN for single-packet windows (structural) | 670 rows, all `Number` = 1 — the same rows also have `Rate` = inf | Dropped by `clean()` with the zero-duration windows; no imputation | Yes (`clean`) |
| 6 | Infinite `Rate` (window of 0 s) | 991 rows: 670 single-packet + 321 windows of 2–8 packets sharing one timestamp | inf → NaN → dropped | Yes (`clean`) |
| 7 | Negative `IAT` (impossible) | 2 rows | Set to NaN → dropped | No → decision log |
| 8 | Exact duplicate rows | 22,976,869 rows (51.0 %), ≈ 70 % of DDoS ICMP flood | `clean()` per file, then again after concatenation | Yes (`clean`) |
| 9 | Same features with different labels | 610,472 vectors, 13,286,035 rows (29.5 %): DoS vs DDoS of the same flood type | Keep for EDA and report (SQ1); drop before any model training | No → decision log (open) |
| 10 | UPPERCASE label spellings | 33 of 34 labels | Normalised by `map_labels` | Yes (`map_labels`) |
| 11 | Extreme imbalance (benign 2.3 %, 5,764× ratio) | `Label` | `sample_per_label` (200k cap) | Yes (`sample_per_label`) |
| 12 | Redundant columns: `LLC` = `IPv`, `Tot size` = `AVG`, `Variance` = `Std`², `Tot sum` = `AVG` × `Number`, `*_count` = share × `Number` | 8 columns (0 violations on complete rows) | Remove in feature selection | No → phase 5 |
| 13 | Near-constant columns (> 99 % zeros) | `Telnet`, `SMTP`, `IRC`, `IGMP`, `DHCP`, `SSH`, `ece_flag_number`, `cwr_flag_number` | Remove in feature selection | No → phase 5 |
| 14 | Categorical code stored as number | `Protocol Type` (values 0, 1, 2, 6, 17, 47) | Encode in feature engineering | No → phase 5 |
| 15 | Structural values that look like errors | `Header_Length` = 0 (7.18 M rows, ICMP/GRE), `Max` > 1,514 B (687,281 rows, 33 % of benign), TTL = 0 (455 rows) | Keep: explained by protocol / capture | — |
| 16 | `Number` < 100 in 100 % of non-flood rows vs ≈ 0.1 % of flood rows | `Number` | Capture artefact; decide in feature selection | No → phase 5 |
| 17 | Extreme outliers | `Rate` (max 1.57 × 10⁷), `IAT` (max 78,612 s), sizes | Investigate per class in phase 3; keep legitimate attack values | No → phase 3 |
| 18 | No identifiers or timestamps; shuffled files | whole dataset | Limitation: no time- or device-based split | — |

---

### NetFlow v3 — `UNSW`, `CIC18` (owner: Ahmed Hamouda), `ToN`, `BoT` (owner: Cyrine Chabbar)

Code: `notebooks/01_unsw.ipynb`, `02_cic18.ipynb`, `03_ton.ipynb`, `04_bot.ipynb` (Steps 0–8 on **all rows**).
`03_ton` and `04_bot` are Cyrine Chabbar's notebooks, completed with the checks from Ahmed Hamouda's analysis.
Every problem, with its evidence, real examples from the data and the approved decision, is in
[`report/data_problems/phase2_data_problems.pdf`](../report/data_problems/phase2_data_problems.pdf):
problems that must be solved **before the merge** (one section per dataset) and problems solved **once on the
merged table**, each split into "change the data" and "keep it as it is". The decisions are logged in
[`decision_log.md`](decision_log.md).

**Dimensions** — all four files have 55 columns: 53 features + `Label` (0/1) + `Attack` (class name).

| | Official rows | Loaded rows | Match? |
|---|---|---|---|
| `UNSW` | 2,365,424 | 2,365,424 | Yes |
| `CIC18` | 20,115,529 | 20,115,529 | Yes |
| `ToN` | 27,520,260 | 27,520,260 | Yes |
| `BoT` | 16,993,808 (official page) | 16,933,808 | No — typo on the official page; Theft is 1,615 flows, not 1,651 |

**Class distribution** (flows in the raw file; `tables/<KEY>_labels.csv`)

| Dataset | Benign | Attack | Largest attack labels | Smallest attack labels |
|---|---|---|---|---|
| `UNSW` | 2,237,731 (94.6 %) | 127,693 | Exploits 42,748, Fuzzers 33,816 | Worms 158, Analysis 1,226 |
| `CIC18` | 17,514,626 (87.1 %) | 2,600,903 | DDoS HOIC 1,032,311, FTP brute force 386,720 | SQL injection 440, XSS 480 |
| `ToN` | 16,792,214 (61.0 %) | 10,728,046 | DDoS 4,141,256, XSS 2,834,435 | Ransomware 3,971, MITM 6,013 |
| `BoT` | 51,989 (0.3 %) | 16,881,819 | DoS 8,034,190, DDoS 7,150,882 | Theft 1,615 |

**Main problems found** (codes as in the report)

| Code | Problem | Decision |
|---|---|---|
| U2, B2 | `..._SECOND_BYTES` NaN / inf on zero-duration flows (65 % of BoT Benign) | Drop both columns before `clean()` |
| U3, B3, C3, T3 | `L7_PROTO` stores two codes in one decimal number (float in UNSW / BoT, integer elsewhere) | Split into `L7_MAIN` + `L7_SUB` |
| U4, C4, T4 | Exact duplicate rows (whole captures recorded twice in CIC18) | Remove |
| C1, T1 | Label spellings missing from the taxonomy | Map with `map_labels`; 11 CIC18 entries added to `config.py` |
| C5 | Same flow with two different labels (880 rows, all web attacks) | Remove all copies |
| C6 | DoS SlowHTTPTest flows are refused FTP connections | Remove |
| C7 | Attack labels on flows identical to Benign traffic of the same machines | Remove; no XSS flow remains in CIC18 |
| T5 | XSS / injection labels on DNS traffic (port 53) | Remove |
| U1, C2, T2, B1 | Strong imbalance (BoT inverted: 0.3 % Benign) | One row per behaviour + weights; no cap (report, section 6) |
| U5, C8, T8, B4 | Very rare classes (Worms 158, Theft 1,615) | Keep every flow; report at family level too |
| T6, B6, B7, U8, T7 | Attack flows that look like Benign or like another attack (DoS = DDoS) | Keep; documented limit of single-flow features |
| M1–M12 | Problems of the merged table: codes stored as numbers, timestamps, IPs and TTL that reveal the label or the dataset, ICMP fields on TCP flows, copy columns, invalid DNS TTL, same behaviour with a different family in another dataset | Solved once on the merged table (see the report) |
| K1–K18 | Zeros meaning "not applicable", exporter quirks, outliers, correlations | Keep; decided in EDA or feature selection |

---

## Cross-dataset comparison (Cyrine Chabbar)

One table comparing all five datasets: rows, columns, attack share, number of attack labels,
network type, and the number of problems found in each.

| Dataset | Network type | Rows | Columns | Attack share | Attack labels | Problems found |
|---|---|---|---|---|---|---|
| `UNSW` | Mixed lab | 2,365,424 flows | 55 | 5.4 % | 9 | 8 (U1–U8) |
| `CIC18` | Enterprise / office | 20,115,529 flows | 55 | 12.9 % | 14 | 10 (C1–C10) |
| `ToN` | IoT / industrial | 27,520,260 flows | 55 | 39.0 % | 9 | 9 (T1–T9) |
| `BoT` | IoT botnet | 16,933,808 flows | 55 | 99.7 % | 4 | 7 (B1–B7) |
| `IoT23` | Real IoT devices | 45,019,243 windows | 40 | 97.66 % | 33 | 18 (see its section) |

The four NetFlow datasets also share 12 problems of the merged table (M1–M12) and 18 "keep as it is" findings
(K1–K18). After cleaning (phase 3): UNSW 1,405,100 rows, CIC18 8,945,792, ToN 5,637,642, BoT 1,563,315 — one row
per different behaviour; merged 17,551,848 rows standing for 63,012,224 flows.

## Feature dictionaries

- NetFlow v3 — 53 features (Ahmed Hamouda): `netflow_feature_dictionary.md`
- CICIoT2023 — 39 features + `Label` in the release we use (Yassine Mtibaa): `ciciot_feature_dictionary.md`
