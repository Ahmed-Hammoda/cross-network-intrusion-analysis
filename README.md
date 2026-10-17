# Multi-Source Network Intrusion Analysis (CRISP-DM)

Data Science midterm project — MEDTECH, Computer System Engineering.

We merge four NetFlow v3 intrusion-detection datasets that share the same 53 features
into one unified dataset, analyse CICIoT2023 alongside it, and map every attack to one
shared taxonomy of 9 attack families (54 attack labels). The project covers CRISP-DM
phases 1–6, from business understanding to feature engineering (no model training).

## Datasets

| Key | Dataset | Network | Flows | Owner |
|---|---|---|---|---|
| `UNSW` | NF-UNSW-NB15-v3 | Mixed lab | 2,365,424 | Member 1 |
| `CIC18` | NF-CSE-CIC-IDS2018-v3 | Enterprise / office | 20,115,529 | Member 1 |
| `ToN` | NF-ToN-IoT-v3 | IoT / industrial | 27,520,260 | Member 2 |
| `BoT` | NF-BoT-IoT-v3 | IoT botnet | 16,993,808 | Member 2 |
| `IoT23` | CICIoT2023 | Real IoT devices | ~47 million | Member 3 |

The four NetFlow v3 datasets are merged into one. CICIoT2023 has different features, so it is
analysed separately and linked through the shared taxonomy.

**The data is not stored in this repository** (too large). Download it from the official sources
and place the files in `data/raw/` with the names listed in `src/config.py`:

- NetFlow v3 (University of Queensland): https://staff.itee.uq.edu.au/marius/NIDS_datasets/ — use the **v3** links
- CICIoT2023 (Canadian Institute for Cybersecurity): https://www.unb.ca/cic/datasets/iotdataset-2023.html — CSV folder

## Repository structure

```
data/raw/          downloaded files (git-ignored)
data/processed/    cleaned + sampled Parquet files, one per dataset (git-ignored)
notebooks/         one notebook per dataset + merge + EDA + feature engineering
src/config.py      shared contract: paths, taxonomy, cleaning/sampling rules, shared functions
tables/            quality reports and summary tables (CSV)
figures/           plots for the report and slides
docs/              decision log and team task split
```

## Setup

```bash
pip install -r requirements.txt
jupyter notebook
```

In each notebook:

```python
import sys; sys.path.append("..")
from src.config import *
```

## Team rules

1. Everyone uses the functions in `src/config.py` (`clean`, `map_labels`, `sample_per_label`,
   `quality_report`, `save_clean`) — nobody re-implements them.
2. Any change to the taxonomy or cleaning rules is agreed first and logged in `docs/decision_log.md`.
3. No scaling, log transforms or encoding per dataset — that is feature engineering, done once on merged data.
4. Each member works in their own notebook to avoid merge conflicts.

## References

- Luay, M. et al. (2025). *Temporal Analysis of NetFlow Datasets for Network Intrusion Detection Systems*. arXiv:2503.04404.
- Neto, E.C.P. et al. (2023). *CICIoT2023: A Real-Time Dataset and Benchmark for Large-Scale Attacks in IoT Environment*. Sensors 23(13), 5941.
