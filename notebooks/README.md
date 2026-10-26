# Notebooks

Each member works only in their own notebooks, which keeps the team free of git conflicts. Every notebook starts with:

```python
import sys; sys.path.append("..")
from src.config import *
```

and uses the shared functions of `src/config.py` (`clean`, `map_labels`, `validate`, `behaviour_hash`,
`collapse_behaviours`, `cleaning_report`, …), so every dataset is processed the same way.

## The notebooks

| Notebook | Owner | Phase | Content |
|---|---|---|---|
| `01_unsw.ipynb` | Ahmed Hamouda | 2 | UNSW-NB15: data understanding (checks 0–8) |
| `02_cic18.ipynb` | Ahmed Hamouda | 2 | CSE-CIC-IDS2018: data understanding |
| `03_ton.ipynb` | Cyrine Chabbar (completed by Ahmed Hamouda) | 2 | ToN-IoT: data understanding |
| `04_bot.ipynb` | Cyrine Chabbar (completed by Ahmed Hamouda) | 2 | BoT-IoT: data understanding |
| `01_unsw_cleaning.ipynb` | Ahmed Hamouda | 3 | UNSW cleaning → `data/processed/UNSW_clean.parquet` |
| `02_cic18_cleaning.ipynb` | Ahmed Hamouda | 3 | CIC18 cleaning → `CIC18_clean.parquet` |
| `03_ton_cleaning.ipynb` | Ahmed Hamouda | 3 | ToN cleaning → `ToN_clean.parquet` |
| `04_bot_cleaning.ipynb` | Ahmed Hamouda | 3 | BoT cleaning → `BoT_clean.parquet` |
| `05_ciciot2023.ipynb` | Yassine Mtibaa | 2, 3 | CICIoT2023: data understanding and cleaning → `IoT23_clean.parquet` |
| `06_merge_netflow.ipynb` | Ahmed Hamouda | 3 | stack the 4 NetFlow files, after-merge decisions → `netflow_merged.parquet` |
| `07_eda_netflow.ipynb` | Ahmed Hamouda | 4 | EDA of the merged NetFlow data: statistics, plots, correlation, Mann–Whitney U, Kolmogorov–Smirnov |
| `07_eda_iot23.ipynb` | Yassine Mtibaa | 4 | EDA of CICIoT2023: statistics, correlation, normality, chi-square, comparison with NetFlow |
| `08_features_netflow.ipynb` | Ahmed Hamouda | 5 | feature engineering of the merged NetFlow data → `netflow_features.parquet` (59 features) |
| `08_features_iot23.ipynb` | Yassine Mtibaa | 5 | feature engineering of CICIoT2023 |

## Run order (to rebuild the data)

The data files are not in the repository (too large). With the raw CSV files in `data/raw/` (see the main README):

1. **NetFlow:** `01_unsw_cleaning` → `02_cic18_cleaning` → `03_ton_cleaning` → `04_bot_cleaning` (any order) →
   `06_merge_netflow` → `07_eda_netflow` → `08_features_netflow`.
2. **CICIoT2023:** `05_ciciot2023` → `07_eda_iot23` → `08_features_iot23`.

The phase 2 notebooks (`01_unsw` … `04_bot`) only read the raw files; they are not needed to rebuild the data.
The large files (17–27 million rows) need about 16 GB of RAM; the notebooks load only the columns they use.

## Rules followed in every notebook

- **Phase 2 is diagnosis only;** the data are changed in phase 3, after the team approved each decision
  (`docs/decision_log.md`, `report/data_problems/phase2_data_problems.pdf`).
- **NetFlow:** one row per different behaviour with a `count` column (identical flows merged), no sampling cap.
  **CICIoT2023:** at most 200,000 rows per label (`sample_per_label`).
- **No modelling in the project:** phase 5 has no train/test split; the steps that learn from the data must be refitted
  on a training part before any model.
- Every result is followed by a short **"Interpretation."** cell.

## Before you commit

- Restart the kernel and run all cells, so the notebook runs cleanly from top to bottom.
- Clear very large outputs to keep the repository small.
- Never commit files from `data/` (they are ignored automatically).
