# Task board

Status: ✅ Done

**Team:** Ahmed Hamouda · Cyrine Chabbar · Yassine Mtibaa

| Member | Datasets |
|---|---|
| Ahmed Hamouda | NF-UNSW-NB15-v3 (`UNSW`), NF-CSE-CIC-IDS2018-v3 (`CIC18`) |
| Cyrine Chabbar | NF-ToN-IoT-v3 (`ToN`), NF-BoT-IoT-v3 (`BoT`) |
| Yassine Mtibaa | CICIoT2023 (`IoT23`) |

## Progress overview

| # | Phase | Rubric points | Status |
|---|---|---|---|
| 1 | Business understanding | Report 4 | ✅ Done |
| 2 | Data understanding | Code 5 + Report 4 | ✅ Done |
| 3 | Data preprocessing | Code 12 + Report 5 | ✅ Done |
| 4 | Exploratory data analysis | Code 13 + Report 6 | ✅ Done |
| 5 | Feature engineering | Code 7 + Report 3 | ✅ Done |
| 6 | Presentation | 35 | ✅ Done |
| 7 | Report | 25 | ✅ Done |

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

## Phase 1 — Business understanding

Written in [`phase1_business_understanding.md`](phase1_business_understanding.md).

| # | Task | Owner | Status |
|---|---|---|---|
| 1.1 | Project context | Ahmed Hamouda | ✅ Done |
| 1.2 | Define the problem | Ahmed Hamouda | ✅ Done |
| 1.3 | Research questions | Ahmed Hamouda | ✅ Done |
| 1.4 | Success criteria | Ahmed Hamouda | ✅ Done |
| 1.5 | Review and approve phase 1 | Cyrine Chabbar, Yassine Mtibaa | ✅ Done |

## Phase 2 — Data understanding: exploration and quality assessment

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
| 2.8 | NetFlow v3 feature dictionary (53 features: name, meaning, unit, type) | Ahmed Hamouda | ✅ Done ([`netflow_feature_dictionary.md`](netflow_feature_dictionary.md)) |
| 2.9 | Cross-dataset comparison table and class-distribution plots | Cyrine Chabbar, Ahmed Hamouda | ✅ Done (table in [`phase2_data_understanding.md`](phase2_data_understanding.md); plot `figures/NetFlow_eda_families.png`) |
| 2.10 | CICIoT2023 feature dictionary (39 features + label, see [ciciot_feature_dictionary.md](ciciot_feature_dictionary.md)) | Yassine Mtibaa | ✅ Done |

## Phase 3 — Data preprocessing: cleaning

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
with a `count` column, no upper limit; imbalance is left to class and network weights at modelling time.

| # | Shared task | Owner | Status |
|---|---|---|---|
| 3.8 | Merge the 4 NetFlow files and run the post-merge checks | Ahmed Hamouda | ✅ Done (`06_merge_netflow`: 17,551,848 rows, `validate` = 0) |
| 3.9 | Explain merging / integration decisions | Ahmed Hamouda | ✅ Done (data-problems report, section 5) |
| 3.10 | Explain why CICIoT2023 is kept separate (notebook 05 end + `datasets.md`) | Yassine Mtibaa | ✅ Done |
| 3.11 | Log every decision in [`decision_log.md`](decision_log.md) | All | ✅ Done |

## Phase 4 — Exploratory data analysis

Each data source has one EDA notebook (follows lab 4): `07_eda_netflow` (merged NetFlow, summary in
[`phase4_eda_netflow.md`](phase4_eda_netflow.md), report `report/eda/phase4_eda_report.pdf`) and `07_eda_iot23`
(CICIoT2023).

| # | Task | Merged NetFlow (Ahmed Hamouda) | CICIoT2023 (Yassine Mtibaa) |
|---|---|---|---|
| 4.1 | Descriptive statistics and distributions (log scale), per family and per network | ✅ | ✅ |
| 4.2 | Correlation analysis: Pearson and Spearman heatmaps | ✅ | ✅ |
| 4.3 | Relationships between features and the target (`is_attack`, `attack_family`) | ✅ | ✅ |
| 4.4 | Patterns: Benign vs attack per network, port range × family / flag fingerprints, DoS vs DDoS | ✅ | ✅ |
| 4.5 | Normality check (→ non-parametric tests) | ✅ | ✅ |
| 4.6 | Hypothesis tests | ✅ Mann–Whitney U (SQ1), Kolmogorov–Smirnov (SQ2) | ✅ chi-square protocol × family (SQ1), KS DoS vs DDoS |
| 4.7 | Class imbalance (SQ3) | ✅ behaviours and flows per family and network | ✅ |
| 4.8 | CICIoT2023 compared to NetFlow at family level (SQ2) | ✅ NetFlow values provided: `tables/NetFlow_family_concepts.csv` | ✅ §7 of `07_eda_iot23` |

**Removed from the plan:** Kruskal–Wallis + Dunn across families. The requirement asks for at least one justified test;
the team covers SQ1 and SQ2 with Mann–Whitney U, chi-square and Kolmogorov–Smirnov, so a fourth test adds nothing.

## Phase 5 — Feature engineering

Requirement: explain feature selection, extraction / creation, encoding and scaling / transformation; justify the final
feature set. **There is no modelling in the project, so no train/test split:** the steps that learn from the data are
fitted on all the data and must be refitted on a training part before any model. Notebooks: `08_features_netflow`
(summary in [`phase5_features_netflow.md`](phase5_features_netflow.md), report
`report/features/phase5_features_report.pdf`) and `08_features_iot23`. Both use the same sections and rules
(|ρ| ≥ 0.95, standard deviation when IQR = 0).

| # | Task | Merged NetFlow (Ahmed Hamouda) | CICIoT2023 (Yassine Mtibaa) |
|---|---|---|---|
| 5.1 | Creation: time / rate, ratio and domain features | ✅ 9 created features | ✅ 6 created features |
| 5.2 | Encoding of the code columns | ✅ port range, protocol, TCP flag bits, L7 protocol | ✅ protocol (one-hot) |
| 5.3 | Transformation and scaling | ✅ log(1 + x), robust scaling | ✅ log(1 + x) and Yeo-Johnson, robust scaling |
| 5.4 | Validation: before / after, new features vs target | ✅ | ✅ |
| 5.5 | Selection: fingerprints, near-constant, correlated pairs, mutual information | ✅ 72 → 59 features | ✅ 51 → 31 features |
| 5.6 | Final feature set: justification, data dictionary, export | ✅ `tables/NetFlow_fe_dictionary.csv` | ✅ `tables/IoT23_fe_dictionary.csv` |
| 5.7 | PCA (2-D view of the families) | ✅ | ✅ |

**Removed from the plan:** train/test split and model-based importance (random forest): the project stops before
modelling, and mutual information ranks the features without a model.

## Phase 6 — Presentation

| # | Task | Owner | Status |
|---|---|---|---|
| 6.1 | Slides: problem, research questions, datasets, taxonomy | Ahmed Hamouda | ✅ Done |
| 6.2 | Slides: preprocessing, merge, EDA findings | Cyrine Chabbar | ✅ Done |
| 6.3 | Slides: hypothesis tests, features, conclusions, limitations | Yassine Mtibaa | ✅ Done |
| 6.4 | Rehearsal, timing and Q&A practice (everyone can explain everyone's code) | All | ✅ Done |

## Phase 7 — Report

| # | Task | Owner | Status |
|---|---|---|---|
| 7.1 | LaTeX report, sections for phases 1–6 ([`report/final/project_report.pdf`](../report/final/project_report.pdf)) | All (each writes their part) | ✅ Done |
| 7.2 | Conclusions and next steps: answer the main research question and SQ1–SQ3, limitations, future modelling plan | All | ✅ Done |
| 7.3 | Figures and tables with captions | All | ✅ Done |
| 7.4 | References (datasets and papers) | Ahmed Hamouda | ✅ Done |
| 7.5 | Reproducibility instructions (README, report Appendix A) | Cyrine Chabbar | ✅ Done |
