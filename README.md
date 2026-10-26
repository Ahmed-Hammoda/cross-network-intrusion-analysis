# Cross-Network Intrusion Analysis (CRISP-DM)

Data Science project — MEDTECH, Computer System Engineering.

We merge four NetFlow v3 intrusion-detection datasets that share the same 53 features into one
unified dataset, analyse CICIoT2023 alongside it, and map every attack to one shared taxonomy of
**9 attack families and 54 attack labels** across **5 network environments**.

**Main research question:** how can traffic collected from different network environments be used
to detect cyberattacks and identify their type reliably, including on networks the detection model
has never seen? Sub-questions in [Phase 1](docs/phase1_business_understanding.md).

## Team

| Member | Responsible for |
|---|---|
| Ahmed Hamouda | phase 1; NF-UNSW-NB15-v3, NF-CSE-CIC-IDS2018-v3; cleaning of the 4 NetFlow datasets, merge, EDA and feature engineering of the merged NetFlow data |
| Cyrine Chabbar | NF-ToN-IoT-v3, NF-BoT-IoT-v3 (data understanding), dataset comparison |
| Yassine Mtibaa | CICIoT2023 |

## Phases

| # | Phase | Day |
|---|---|---|
| 1 | Business understanding — context, problem, research questions, success criteria | Sat |
| 2 | Data understanding — rows and columns, data types and units, problems, solutions (without code) | Sat |
| 3 | Data preprocessing — handle every problem with code, outliers, merging / integration decisions | Sun |
| 4 | Exploratory data analysis — descriptive statistics and plots, correlations, relationships, hypothesis tests | Mon |
| 5 | Feature engineering — selection, extraction / creation / encoding, scaling / transformation, final feature set | Tue |
| 6 | Presentation | Wed |
| 7 | Report | Wed |

Progress on every task is tracked in the [task board](docs/TASK_BOARD.md).

## Project documents

| Document | Content |
|---|---|
| [Task board](docs/TASK_BOARD.md) | Every phase and task, owner, day and status (to do / in progress / done) |
| [Datasets](docs/datasets.md) | Description, provenance, size and known issues of each dataset |
| [Attack taxonomy](docs/attack_taxonomy.md) | All 54 attacks described and grouped into 9 families |
| [Phase 1 — Business understanding](docs/phase1_business_understanding.md) | Context, problem, research questions, success criteria |
| [Phase 2 — Data understanding](docs/phase2_data_understanding.md) | Checks 2.1–2.5 for every dataset, cross-dataset comparison |
| [NetFlow data problems (PDF)](report/data_problems/phase2_data_problems.pdf) | Every NetFlow problem with evidence and the approved decision, before and after the merge |
| [NetFlow feature dictionary](docs/netflow_feature_dictionary.md) | The 53 NetFlow v3 features: meaning, unit, type, what happened to each |
| [CICIoT2023 feature dictionary](docs/ciciot_feature_dictionary.md) | The 39 CICIoT2023 features |
| [Phase 4 — EDA, NetFlow](docs/phase4_eda_netflow.md) · [report (PDF)](report/eda/phase4_eda_report.pdf) | Statistics, plots, correlation, hypothesis tests of the merged NetFlow data |
| [Phase 5 — Feature engineering, NetFlow](docs/phase5_features_netflow.md) · [report (PDF)](report/features/phase5_features_report.pdf) · [explained (PDF)](report/features/phase5_explained.pdf) | Creation, encoding, scaling, selection, final 59 features |
| [Decision log](docs/decision_log.md) | Every cleaning, integration, EDA and feature decision |
| [Team plan](docs/team_plan.md) | Who owns which datasets and notebooks |
| [Notebook guide](notebooks/README.md) | Every notebook, its owner and the run order |

## Datasets

| Key | Dataset | Network | Flows | Owner |
|---|---|---|---|---|
| `UNSW` | NF-UNSW-NB15-v3 | Mixed lab | 2,365,424 | Ahmed Hamouda |
| `CIC18` | NF-CSE-CIC-IDS2018-v3 | Enterprise / office | 20,115,529 | Ahmed Hamouda |
| `ToN` | NF-ToN-IoT-v3 | IoT / industrial | 27,520,260 | Cyrine Chabbar |
| `BoT` | NF-BoT-IoT-v3 | IoT botnet | 16,933,808 | Cyrine Chabbar |
| `IoT23` | CICIoT2023 | Real IoT devices | 45,019,243 packet windows | Yassine Mtibaa |

The four NetFlow v3 datasets are merged into one. CICIoT2023 has different features, so it is
analysed separately and linked through the shared taxonomy. Details in [datasets.md](docs/datasets.md).

**The data is not stored in this repository** (GitHub rejects files over 100 MB). Download it from
the official sources and put the files in `data/raw/` with the names listed in `src/config.py`:

- NetFlow v3 (University of Queensland): https://staff.itee.uq.edu.au/marius/NIDS_datasets/ — use the **v3** links
- CICIoT2023 (Canadian Institute for Cybersecurity): https://www.unb.ca/cic/datasets/iotdataset-2023.html — the `MERGED_CSV` folder only, into `data/raw/CICIoT2023/`

Then rebuild the processed files by running the notebooks in the order given in [notebooks/README.md](notebooks/README.md).

## Repository structure

```
├── src/config.py            Shared contract: paths, taxonomy, cleaning / mapping / sampling / quality functions
├── data/raw/                Downloaded datasets (git-ignored)
├── data/processed/          Cleaned, merged and feature Parquet files (git-ignored, rebuilt by the notebooks)
├── notebooks/               Our code — see notebooks/README.md for what each member delivers
├── tables/                  Quality reports and summary tables (CSV)
├── figures/                 Plots for the report and slides
├── docs/                    Task board, dataset and attack descriptions, phase write-ups, decision log
├── report/                  Phase reports (data problems, EDA, feature engineering) and the final report
└── presentation/            Slides
```

## Setup

```bash
git clone <repo-url>
cd <repo-name>
pip install -r requirements.txt
jupyter notebook
```

Each notebook starts with:

```python
import sys; sys.path.append("..")
from src.config import *
```

## Team rules

1. Everyone uses the shared functions in `src/config.py` (`clean`, `map_labels`, `validate`, …) — nobody
   re-implements them, so differences between networks reflect the traffic, not our preprocessing.
   NetFlow keeps one row per different behaviour (`collapse_behaviours`, no cap); CICIoT2023 keeps at most
   200,000 rows per label (`sample_per_label`).
2. Any change to the taxonomy or cleaning rules is agreed by the team first and logged in
   `docs/decision_log.md`.
3. No scaling, log transforms or encoding per dataset — that is feature engineering (phase 5), done once on
   the merged data. The project stops before modelling, so there is no train/test split; before any model,
   the learned steps must be refitted on the training part only.
4. Each member works only in their own notebooks to avoid merge conflicts.
5. Update your rows in the [task board](docs/TASK_BOARD.md) when you finish a task.

## Git workflow

```bash
git pull                      # always start by getting the team's latest work
# ... work in your own notebook ...
git add notebooks/01_unsw.ipynb tables/ figures/ docs/
git commit -m "UNSW: phase 2 data understanding"
git push
```

Clear notebook outputs that contain large printed tables before committing, to keep the repository small.

## References

- Luay, M. et al. (2025). *Temporal Analysis of NetFlow Datasets for Network Intrusion Detection Systems*. arXiv:2503.04404.
- Neto, E.C.P. et al. (2023). *CICIoT2023: A Real-Time Dataset and Benchmark for Large-Scale Attacks in IoT Environment*. Sensors 23(13), 5941.
