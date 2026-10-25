# Task board

Status: ✅ Done · 🔄 In progress · ⬜ To do

Update the status in your own rows when you finish a task, and commit with a message like
`board: phase 2 UNSW done`.

**Team:** Ahmed Hamouda · Cyrine Chabbar · Yassine Mtibaa

| Member | Datasets |
|---|---|
| Ahmed Hamouda | NF-UNSW-NB15-v3 (`UNSW`), NF-CSE-CIC-IDS2018-v3 (`CIC18`) |
| Cyrine Chabbar | NF-ToN-IoT-v3 (`ToN`), NF-BoT-IoT-v3 (`BoT`) |
| Yassine Mtibaa | CICIoT2023 (`IoT23`) |

## Progress overview

| # | Phase | Day | Rubric points | Status |
|---|---|---|---|---|
| 1 | Business understanding | Sat | Report 4 | ✅ Done |
| 2 | Data understanding | Sat | Code 5 + Report 4 | ✅ Done |
| 3 | Data preprocessing | Sun | Code 12 + Report 5 | ✅ Done |
| 4 | Exploratory data analysis | Mon | Code 13 + Report 6 | ⬜ To do |
| 5 | Feature engineering | Tue | Code 7 + Report 3 | ⬜ To do |
| 6 | Presentation | Wed | 35 | ⬜ To do |
| 7 | Report | Wed | 25 | ⬜ To do |

## Setup (before phase 1)

| Task | Owner | Status |
|---|---|---|
| Choose topic and datasets (4 NetFlow v3 + CICIoT2023) | All | ✅ Done |
| Shared attack taxonomy (9 families, 54 labels) | All | ✅ Done |
| Work split by dataset, no dependencies | All | ✅ Done |
| Shared contract `src/config.py` | Ahmed Hamouda | ✅ Done |
| GitHub repository and documentation | Ahmed Hamouda | ✅ Done |
| Clone the repo and `pip install -r requirements.txt` | Cyrine Chabbar | ✅ Done |
| Clone the repo and `pip install -r requirements.txt` | Yassine Mtibaa | ✅ Done |

---

## Phase 1 — Business understanding (Sat)

Written in [`phase1_business_understanding.md`](phase1_business_understanding.md).

| # | Task | Owner | Status |
|---|---|---|---|
| 1.1 | Project context | Ahmed Hamouda | ✅ Done |
| 1.2 | Define the problem | Ahmed Hamouda | ✅ Done |
| 1.3 | Research questions | Ahmed Hamouda | ✅ Done |
| 1.4 | Success criteria | Ahmed Hamouda | ✅ Done |
| 1.5 | Review and approve phase 1 | Cyrine Chabbar, Yassine Mtibaa | ✅ Done |

## Phase 2 — Data understanding: exploration and quality assessment (Sat)

Diagnosis only — find, measure and propose; nothing is changed until phase 3.
Details of every check: [`phase2_data_understanding.md`](phase2_data_understanding.md) (follows lab Part 1).
Every NetFlow problem and its approved decision: [`report/data_problems/phase2_data_problems.pdf`](../report/data_problems/phase2_data_problems.pdf).

| # | Task | UNSW | CIC18 | ToN | BoT | IoT23 |
|---|---|---|---|---|---|---|
| 2.1 | Initial inspection: structure, rows/columns vs official, data types and units, first issues | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.2 | Missing and infinite values: count, % per column, plot, strategy per column | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.3 | Data type issues: text→numeric, timestamps→datetime, codes→categorical, label spellings | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.4 | Outlier detection: IQR + z-score, box plots by family, legitimate vs error, planned treatment | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.5 | Consistency: duplicates, identifier uniqueness, formatting, logical checks (`validate`) | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.6 | Class distribution (flows per attack label) | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2.7 | Summary table: every problem → planned solution (no code) | ✅ | ✅ | ✅ | ✅ | ✅ |
| | **Owner** | Ahmed | Ahmed | Cyrine | Cyrine | Yassine |

| # | Shared task | Owner | Status |
|---|---|---|---|
| 2.8 | NetFlow v3 feature dictionary (53 features: name, meaning, unit, type) | Ahmed Hamouda | ⬜ To do |
| 2.9 | Cross-dataset comparison table and class-distribution plots | Cyrine Chabbar | 🔄 Table done ([`phase2_data_understanding.md`](phase2_data_understanding.md)); plots to do |
| 2.10 | CICIoT2023 feature dictionary (39 features + label, see [ciciot_feature_dictionary.md](ciciot_feature_dictionary.md)) | Yassine Mtibaa | ✅ Done |

## Phase 3 — Data preprocessing: cleaning (Sun)

Apply the solutions planned in phase 2, with before/after evidence for every step (follows lab Part 2).

| # | Task | UNSW | CIC18 | ToN | BoT | IoT23 |
|---|---|---|---|---|---|---|
| 3.1 | Handle missing / infinite values (strategy per column, justified, before/after) | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3.2 | Data type conversion (timestamps→datetime, codes→category), verified | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3.3 | Standardise categorical values: column names, label spellings → shared taxonomy (`map_labels`) | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3.4 | Outlier treatment: remove errors, keep legitimate ones; document removed vs kept | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3.5 | Remove duplicates; drop identifier columns | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3.6 | Data validation (`validate` returns 0 violations) + data quality report | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3.7 | Stratified sampling per label + save cleaned Parquet | ✅ | ✅ | ✅ | ✅ | ✅ |
| | **Owner** | Ahmed | Ahmed | Cyrine | Cyrine | Yassine |

NetFlow notebooks: `01_unsw_cleaning`, `02_cic18_cleaning`, `03_ton_cleaning`, `04_bot_cleaning`. For NetFlow, 3.7 follows
the approved plan (section 6 of the data-problems report) instead of the 200k cap: one row per different behaviour
with a `count` column, no upper limit; imbalance is handled with class and network weights after the split.

| # | Shared task | Owner | Status |
|---|---|---|---|
| 3.8 | Merge the 4 NetFlow files and run the post-merge checks | Ahmed Hamouda | ✅ Done (`06_merge_netflow`: 17,551,848 rows, `validate` = 0) |
| 3.9 | Explain merging / integration decisions | Ahmed Hamouda | ✅ Done (data-problems report, section 5) |
| 3.10 | Explain why CICIoT2023 is kept separate (notebook 05 end + `datasets.md`) | Yassine Mtibaa | ✅ Done |
| 3.11 | Log every decision in [`decision_log.md`](decision_log.md) | All | ✅ Done |

## Phase 4 — Exploratory data analysis (Mon)

| # | Task | Owner | Status |
|---|---|---|---|
| 4.1 | Distributions of key variables (log scale) and descriptive statistics per family and per source | Cyrine Chabbar | ⬜ To do |
| 4.2 | Correlation analysis / heatmap of numeric features | Ahmed Hamouda | ⬜ To do |
| 4.3 | Relationships between features and the target (`is_attack`, `attack_family`) | Cyrine Chabbar | ⬜ To do |
| 4.4 | Interesting patterns and trends (per family, per network) | Yassine Mtibaa | ✅ Done (IoT23: flag fingerprints, DoS vs DDoS, separability — `07_eda_iot23`) |
| 4.5 | Justified hypothesis tests with interpretation: | | |
| | · Normality check (justifies non-parametric tests) | Yassine Mtibaa | ✅ Done (rejected everywhere → non-parametric) |
| | · Mann–Whitney U: benign vs attack, with effect size (SQ1) | Ahmed Hamouda | ⬜ To do |
| | · Kruskal–Wallis + Dunn post-hoc: across families (SQ1) | Cyrine Chabbar | ⬜ To do |
| | · Chi-square: protocol × family (SQ1) | Yassine Mtibaa | ✅ Done (IoT23: V = 0.43) |
| | · Kolmogorov–Smirnov: same attack across networks (SQ2) | Ahmed Hamouda | ⬜ To do |
| 4.6 | Class imbalance analysis (SQ3) | Cyrine Chabbar | ⬜ To do |
| 4.7 | CICIoT2023 EDA, compared to NetFlow at family level | Yassine Mtibaa | 🔄 IoT23 EDA done; NetFlow comparison runs once the cleaned NetFlow files exist |

## Phase 5 — Feature engineering (Tue)

Follows lab Parts 3–5. **First step: train/test split** — every encoder, scaler and selector is
fitted on the training set only (no data leakage).

| # | Task | Owner | Status |
|---|---|---|---|
| 5.1 | Train/test split (stratified by `attack_label`) | Ahmed Hamouda | ⬜ To do |
| 5.2 | Time features: duration from timestamps, packets/s, bytes/s (no hour-of-day — it would leak the lab's attack schedule) | Yassine Mtibaa | ⬜ To do |
| 5.3 | Categorical features: one-hot protocol, frequency/target encoding for L7 protocol and ports, rare categories grouped | Cyrine Chabbar | ⬜ To do |
| 5.4 | Numeric features: ratios (in/out bytes, bytes per packet), binning, polynomial terms where justified | Cyrine Chabbar | ⬜ To do |
| 5.5 | Domain-specific features: traffic asymmetry, TCP-flag shares, burstiness from inter-arrival times | Ahmed Hamouda | ⬜ To do |
| 5.6 | Scaling / transformation: log transform skewed features, RobustScaler fitted on train | Yassine Mtibaa | ⬜ To do |
| 5.7 | Feature validation: before/after plots, new features vs target | Yassine Mtibaa | ⬜ To do |
| 5.8 | Feature selection: remove low-variance and highly correlated features, importance ranking, justify | Ahmed Hamouda | ⬜ To do |
| 5.9 | Export final dataset + data dictionary of all features + usage instructions | Cyrine Chabbar | ⬜ To do |
| 5.10 | Bonus: PCA (2D view of class separability) | Ahmed Hamouda | ⬜ To do |

## Phase 6 — Presentation (Wed)

| # | Task | Owner | Status |
|---|---|---|---|
| 6.1 | Slides: problem, research questions, datasets, taxonomy | Ahmed Hamouda | ⬜ To do |
| 6.2 | Slides: preprocessing, merge, EDA findings | Cyrine Chabbar | ⬜ To do |
| 6.3 | Slides: hypothesis tests, features, conclusions, limitations | Yassine Mtibaa | ⬜ To do |
| 6.4 | Rehearsal, timing and Q&A practice (everyone can explain everyone's code) | All | ⬜ To do |

## Phase 7 — Report (Wed)

| # | Task | Owner | Status |
|---|---|---|---|
| 7.1 | LaTeX report on Overleaf, sections for phases 1–5 | All (each writes their part) | ⬜ To do |
| 7.2 | Conclusions and next steps: answer the main research question and SQ1–SQ3, limitations, future modelling plan | All | ⬜ To do |
| 7.3 | Figures and tables with captions | All | ⬜ To do |
| 7.4 | References (datasets and papers) | Ahmed Hamouda | ⬜ To do |
| 7.5 | Final check: the code runs cleanly from a fresh clone | Cyrine Chabbar | ⬜ To do |
