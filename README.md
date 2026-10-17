# Cross-Network Intrusion Analysis (CRISP-DM)

Data Science midterm project — MEDTECH, Computer System Engineering.

We merge four NetFlow v3 intrusion-detection datasets that share the same 53 features into one
unified dataset, analyse CICIoT2023 alongside it, and map every attack to one shared taxonomy of
**9 attack families and 54 attack labels** across **5 network environments**. The project covers
CRISP-DM from business understanding to feature engineering (no model training in this phase).

**Main question:** which traffic characteristics distinguish attacks from normal traffic — and do
they stay the same from one network to another?

## Project documents

| Document | Content |
|---|---|
| [Task board](docs/TASK_BOARD.md) | Every phase and task, owner, day and status (to do / in progress / done) |
| [Datasets](docs/datasets.md) | Description, provenance, size and known issues of each dataset |
| [Attack taxonomy](docs/attack_taxonomy.md) | All 54 attacks described and grouped into 9 families |
| [Phase 1 — Business understanding](docs/phase1_business_understanding.md) | Context, problem, research questions, success criteria |
| [Phase 2 — Data understanding](docs/phase2_data_understanding.md) | Per-dataset description template |
| [Decision log](docs/decision_log.md) | Every cleaning and integration decision |
| [Team plan](docs/team_plan.md) | Who owns which datasets and notebooks |

## Datasets

| Key | Dataset | Network | Flows | Owner |
|---|---|---|---|---|
| `UNSW` | NF-UNSW-NB15-v3 | Mixed lab | 2,365,424 | Member 1 |
| `CIC18` | NF-CSE-CIC-IDS2018-v3 | Enterprise / office | 20,115,529 | Member 1 |
| `ToN` | NF-ToN-IoT-v3 | IoT / industrial | 27,520,260 | Member 2 |
| `BoT` | NF-BoT-IoT-v3 | IoT botnet | 16,993,808 | Member 2 |
| `IoT23` | CICIoT2023 | Real IoT devices | ~47 million | Member 3 |

The four NetFlow v3 datasets are merged into one. CICIoT2023 has different features, so it is
analysed separately and linked through the shared taxonomy. Details in [datasets.md](docs/datasets.md).

**The data is not stored in this repository** (GitHub rejects files over 100 MB). Download it from
the official sources and put the files in `data/raw/` with the names listed in `src/config.py`:

- NetFlow v3 (University of Queensland): https://staff.itee.uq.edu.au/marius/NIDS_datasets/ — use the **v3** links
- CICIoT2023 (Canadian Institute for Cybersecurity): https://www.unb.ca/cic/datasets/iotdataset-2023.html — CSV folder into `data/raw/CICIoT2023/`

## Repository structure

```
├── src/config.py            Shared contract: paths, taxonomy, cleaning / mapping / sampling / quality functions
├── data/raw/                Downloaded datasets (git-ignored)
├── data/processed/          Cleaned, sampled Parquet files (git-ignored)
├── notebooks/
│   ├── 01_unsw.ipynb                 Member 1
│   ├── 02_cic18.ipynb                Member 1
│   ├── 03_ton.ipynb                  Member 2
│   ├── 04_bot.ipynb                  Member 2
│   ├── 05_ciciot2023.ipynb           Member 3
│   ├── 06_merge_netflow.ipynb        Merge of the 4 NetFlow files
│   ├── 07_eda.ipynb                  Phase 4
│   └── 08_feature_engineering.ipynb  Phase 5
├── tables/                  Quality reports and summary tables (CSV)
├── figures/                 Plots for the report and slides
├── docs/                    Task board, dataset and attack descriptions, phase write-ups, decision log
├── report/                  Final LaTeX report (Overleaf export)
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

1. Everyone uses the shared functions in `src/config.py` (`clean`, `map_labels`, `sample_per_label`,
   `quality_report`, `save_clean`) — nobody re-implements them, so differences between networks
   reflect the traffic, not our preprocessing.
2. Any change to the taxonomy or cleaning rules is agreed by the team first and logged in
   `docs/decision_log.md`.
3. No scaling, log transforms or encoding per dataset — that is feature engineering, done once on
   the merged data, after the train/test split.
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
