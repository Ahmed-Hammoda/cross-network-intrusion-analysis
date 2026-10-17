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
| 1 | Business understanding | Sat | Report 4 | 🔄 In progress |
| 2 | Data understanding | Sat | Code 5 + Report 4 | ⬜ To do |
| 3 | Data preprocessing | Sun | Code 12 + Report 5 | ⬜ To do |
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
| Clone the repo and `pip install -r requirements.txt` | Cyrine Chabbar | ⬜ To do |
| Clone the repo and `pip install -r requirements.txt` | Yassine Mtibaa | ⬜ To do |
| Download own datasets into `data/raw/` | All | ⬜ To do |

---

## Phase 1 — Business understanding (Sat)

Written in [`phase1_business_understanding.md`](phase1_business_understanding.md).

| # | Task | Owner | Status |
|---|---|---|---|
| 1.1 | Project context | Ahmed Hamouda | 🔄 In progress |
| 1.2 | Define the problem | Ahmed Hamouda | 🔄 In progress |
| 1.3 | Research questions | Ahmed Hamouda | 🔄 In progress |
| 1.4 | Success criteria | Ahmed Hamouda | 🔄 In progress |
| 1.5 | Review and approve phase 1 | Cyrine Chabbar, Yassine Mtibaa | ⬜ To do |

## Phase 2 — Data understanding (Sat)

Written in [`phase2_data_understanding.md`](phase2_data_understanding.md), one section per dataset.

| # | Task | UNSW | CIC18 | ToN | BoT | IoT23 |
|---|---|---|---|---|---|---|
| 2.1 | Describe rows and columns (check against official counts) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.2 | Data types and units | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.3 | What are the problems (NaN, inf, duplicates, constant columns, label spellings, imbalance) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.4 | Solution for each problem (without code) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| | **Owner** | Ahmed | Ahmed | Cyrine | Cyrine | Yassine |

| # | Shared task | Owner | Status |
|---|---|---|---|
| 2.5 | NetFlow v3 feature dictionary (53 features: name, meaning, unit, type) | Ahmed Hamouda | ⬜ To do |
| 2.6 | Dataset comparison table and class-distribution plots | Cyrine Chabbar | ⬜ To do |
| 2.7 | CICIoT2023 feature dictionary (45 features) | Yassine Mtibaa | ⬜ To do |

## Phase 3 — Data preprocessing (Sun)

| # | Task | UNSW | CIC18 | ToN | BoT | IoT23 |
|---|---|---|---|---|---|---|
| 3.1 | Handle all problems with code (ID columns, inf, NaN, duplicates, label mapping, sampling) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.2 | Handle outliers (investigate per class, justify the decision) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.3 | Before/after quality report + save cleaned Parquet | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| | **Owner** | Ahmed | Ahmed | Cyrine | Cyrine | Yassine |

| # | Shared task | Owner | Status |
|---|---|---|---|
| 3.4 | Merge the 4 NetFlow files and run the post-merge checks | Ahmed Hamouda | ⬜ To do |
| 3.5 | Explain merging / integration decisions | Ahmed Hamouda | ⬜ To do |
| 3.6 | Explain why CICIoT2023 is kept separate | Yassine Mtibaa | ⬜ To do |
| 3.7 | Log every decision in [`decision_log.md`](decision_log.md) | All | ⬜ To do |

## Phase 4 — Exploratory data analysis (Mon)

| # | Task | Owner | Status |
|---|---|---|---|
| 4.1 | Meaningful descriptive statistics and plots (per family and per source) | Cyrine Chabbar | ⬜ To do |
| 4.2 | Correlation analysis / heatmap | Ahmed Hamouda | ⬜ To do |
| 4.3 | Relationships between variables | Cyrine Chabbar | ⬜ To do |
| 4.4 | Justified hypothesis tests with interpretation: | | |
| | · Normality check (justifies non-parametric tests) | Yassine Mtibaa | ⬜ To do |
| | · Mann–Whitney U: benign vs attack, with effect size (RQ1) | Ahmed Hamouda | ⬜ To do |
| | · Kruskal–Wallis + Dunn post-hoc: across families (RQ2) | Cyrine Chabbar | ⬜ To do |
| | · Chi-square: protocol × family (RQ2) | Yassine Mtibaa | ⬜ To do |
| | · Kolmogorov–Smirnov: same attack across networks (RQ3) | Ahmed Hamouda | ⬜ To do |
| 4.5 | CICIoT2023 EDA, compared to NetFlow at family level | Yassine Mtibaa | ⬜ To do |

## Phase 5 — Feature engineering (Tue)

| # | Task | Owner | Status |
|---|---|---|---|
| 5.1 | Feature selection (train/test split first, remove constant and highly correlated features, rank features) | Ahmed Hamouda | ⬜ To do |
| 5.2 | Extraction / creating / encoding (ratio features, bytes per packet, protocol encoding) | Cyrine Chabbar | ⬜ To do |
| 5.3 | Scaling / transformation (log transform, scaler fitted on train only) | Yassine Mtibaa | ⬜ To do |
| 5.4 | Justify the final feature set | All | ⬜ To do |

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
| 7.2 | Conclusions and next steps: answer RQ1–RQ4, limitations, future modelling plan | All | ⬜ To do |
| 7.3 | Figures and tables with captions | All | ⬜ To do |
| 7.4 | References (datasets and papers) | Ahmed Hamouda | ⬜ To do |
| 7.5 | Final check: the code runs cleanly from a fresh clone | Cyrine Chabbar | ⬜ To do |
