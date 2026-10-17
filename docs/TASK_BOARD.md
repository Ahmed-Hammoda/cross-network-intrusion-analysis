# Task board

Status: ✅ Done · 🔄 In progress · ⬜ To do

Update the status in your own rows when you finish a task, and commit with a message like
`board: phase 2 UNSW done`. Rubric points are shown so we always know where the marks are.

## Progress overview

| Phase | Day | Rubric weight | Status |
|---|---|---|---|
| 0. Project setup | Sat | — | ✅ Done |
| 1. Business understanding | Sat | Report 4 pts | 🔄 In progress |
| 2. Data understanding | Sat | Code 5 + Report 4 pts | ⬜ To do |
| 3. Data preprocessing | Sun | Code 12 + Report 5 pts | ⬜ To do |
| 4. Exploratory data analysis | Mon | Code 13 + Report 6 pts | ⬜ To do |
| 5. Feature engineering | Tue | Code 7 + Report 3 pts | ⬜ To do |
| 6. Conclusions and next steps | Tue | Report 3 pts | ⬜ To do |
| 7. Presentation | Wed | 35 pts | ⬜ To do |
| 8. Report | Wed | 25 pts (total) | ⬜ To do |

---

## Phase 0 — Project setup

| # | Task | Owner | Status |
|---|---|---|---|
| 0.1 | Choose topic and datasets (4 NetFlow v3 + CICIoT2023) | All | ✅ Done |
| 0.2 | Define shared attack taxonomy (9 families, 54 labels) | All | ✅ Done |
| 0.3 | Split work by dataset, no dependencies | All | ✅ Done |
| 0.4 | Shared contract `src/config.py` (cleaning, mapping, sampling, quality report) | Member 1 | ✅ Done |
| 0.5 | GitHub repository, structure, README | Member 1 | ✅ Done |
| 0.6 | Each member clones the repo and runs `pip install -r requirements.txt` | All | ⬜ To do |
| 0.7 | Each member downloads their datasets into `data/raw/` | All | ⬜ To do |

## Phase 1 — Business understanding (Sat) → `docs/phase1_business_understanding.md`

| # | Task | Owner | Status |
|---|---|---|---|
| 1.1 | Project context | Member 1 | 🔄 In progress |
| 1.2 | Problem definition | Member 1 | 🔄 In progress |
| 1.3 | Research questions | Member 1 | 🔄 In progress |
| 1.4 | Measurable success criteria | Member 1 | 🔄 In progress |
| 1.5 | Team review of phase 1 | All | ⬜ To do |

## Phase 2 — Data understanding (Sat) → `docs/phase2_data_understanding.md`

Rubric: identify sources; describe rows, columns, data types, units, key variables and initial quality issues.

| # | Task | UNSW | CIC18 | ToN | BoT | IoT23 |
|---|---|---|---|---|---|---|
| 2.1 | Load and confirm row/column counts against official numbers | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.2 | Describe columns: data types, units, key variables | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.3 | Class distribution (flows per attack label) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.4 | Find quality problems (NaN, inf, duplicates, constant columns, odd types, label spellings) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.5 | Write the planned solution for each problem (no code yet) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

Owners: UNSW and CIC18 → Member 1 · ToN and BoT → Member 2 · IoT23 → Member 3

| # | Shared task | Owner | Status |
|---|---|---|---|
| 2.6 | NetFlow v3 feature dictionary (53 features: name, meaning, unit, type) | Member 1 | ⬜ To do |
| 2.7 | CICIoT2023 feature dictionary (45 features) | Member 3 | ⬜ To do |
| 2.8 | Dataset comparison table (sources, sizes, networks, attack share) | Member 2 | ⬜ To do |

## Phase 3 — Data preprocessing (Sun)

Rubric: handle missing values, duplicates, inconsistent types/categories, outliers; explain merging; prevent leakage; before/after checks.

| # | Task | UNSW | CIC18 | ToN | BoT | IoT23 |
|---|---|---|---|---|---|---|
| 3.1 | Drop identifier columns (IP addresses) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.2 | Handle inf and NaN | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.3 | Remove exact duplicates | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.4 | Map labels to taxonomy (`map_labels`) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.5 | Outlier investigation per class (investigate, don't blindly remove) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.6 | Stratified sampling per label (`sample_per_label`) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.7 | Before/after quality report + save Parquet | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

| # | Shared task | Owner | Status |
|---|---|---|---|
| 3.8 | Merge the 4 NetFlow files (`06_merge_netflow.ipynb`) | Member 1 | ⬜ To do |
| 3.9 | Post-merge checks (same columns/types, no NaN/inf/duplicates, label → one family) | Member 1 | ⬜ To do |
| 3.10 | Write merge/integration decisions + why CICIoT2023 is not merged | Member 1 + 3 | ⬜ To do |
| 3.11 | Update `docs/decision_log.md` with every decision | All | ⬜ To do |

## Phase 4 — Exploratory data analysis (Mon) → `07_eda.ipynb`

| # | Task | Owner | Status |
|---|---|---|---|
| 4.1 | Descriptive statistics per family and per source | Member 1 | ⬜ To do |
| 4.2 | Distribution plots (log scale) and box plots by family | Member 2 | ⬜ To do |
| 4.3 | Correlation analysis and heatmap | Member 1 | ⬜ To do |
| 4.4 | Relationships between variables (e.g. bytes vs packets by family) | Member 2 | ⬜ To do |
| 4.5 | Normality check → justify non-parametric tests | Member 3 | ⬜ To do |
| 4.6 | Hypothesis test 1: Mann–Whitney U (benign vs attack) + effect size | Member 1 | ⬜ To do |
| 4.7 | Hypothesis test 2: Kruskal–Wallis + Dunn post-hoc (across families) | Member 2 | ⬜ To do |
| 4.8 | Hypothesis test 3: Chi-square (protocol × family) | Member 3 | ⬜ To do |
| 4.9 | Hypothesis test 4: Kolmogorov–Smirnov (same attack across networks, RQ3) | Member 1 | ⬜ To do |
| 4.10 | CICIoT2023 EDA in parallel, compared at family level | Member 3 | ⬜ To do |

## Phase 5 — Feature engineering (Tue) → `08_feature_engineering.ipynb`

| # | Task | Owner | Status |
|---|---|---|---|
| 5.1 | Train/test split **before** any fitting (leakage prevention) | Member 1 | ⬜ To do |
| 5.2 | Remove highly correlated / constant features | Member 1 | ⬜ To do |
| 5.3 | Feature ranking (mutual information / ANOVA F) | Member 2 | ⬜ To do |
| 5.4 | Create features (ratios, bytes per packet, flag shares) | Member 2 | ⬜ To do |
| 5.5 | Encode categorical (protocol) | Member 3 | ⬜ To do |
| 5.6 | Log transform skewed features + RobustScaler fitted on train only | Member 3 | ⬜ To do |
| 5.7 | Justify the final feature set | All | ⬜ To do |

## Phase 6 — Conclusions and next steps (Tue)

| # | Task | Owner | Status |
|---|---|---|---|
| 6.1 | Answer RQ1–RQ4 with evidence | All | ⬜ To do |
| 6.2 | Limitations (lab traffic, label noise, imbalance, dataset age) | Member 3 | ⬜ To do |
| 6.3 | Future modeling plan (no implementation) | Member 2 | ⬜ To do |

## Phase 7 — Presentation (Wed) → `presentation/`

| # | Task | Owner | Status |
|---|---|---|---|
| 7.1 | Slides: problem, RQs, datasets, taxonomy | Member 1 | ⬜ To do |
| 7.2 | Slides: preprocessing and merge | Member 2 | ⬜ To do |
| 7.3 | Slides: EDA findings, tests, features, conclusions | Member 3 | ⬜ To do |
| 7.4 | Rehearsal + timing + Q&A practice (everyone explains everyone's code) | All | ⬜ To do |

## Phase 8 — Report (Wed) → `report/`

| # | Task | Owner | Status |
|---|---|---|---|
| 8.1 | LaTeX report on Overleaf with the six phases | All | ⬜ To do |
| 8.2 | Figures and tables with captions | All | ⬜ To do |
| 8.3 | References (datasets + papers) | Member 1 | ⬜ To do |
| 8.4 | Final check: code runs cleanly from a fresh clone | Member 2 | ⬜ To do |
