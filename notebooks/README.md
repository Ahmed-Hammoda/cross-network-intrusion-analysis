# Notebooks

Each member adds their own notebooks here. **Only edit your own notebooks** — that is what keeps
us free of git conflicts.

Every notebook starts with:

```python
import sys; sys.path.append("..")
from src.config import *
```

and uses only the shared functions from `src/config.py` for cleaning, label mapping, sampling and
quality reports, so all five datasets are processed in exactly the same way.

## Expected notebooks

| Notebook | Owner | Phases |
|---|---|---|
| `01_unsw.ipynb` | Ahmed Hamouda | 2, 3 |
| `02_cic18.ipynb` | Ahmed Hamouda | 2, 3 |
| `03_ton.ipynb` | Cyrine Chabbar | 2, 3 |
| `04_bot.ipynb` | Cyrine Chabbar | 2, 3 |
| `05_ciciot2023.ipynb` | Yassine Mtibaa | 2, 3 |
| `06_merge_netflow.ipynb` | Ahmed Hamouda | 3 |
| `07_eda.ipynb` | All (own sections) | 4 |
| `08_feature_engineering.ipynb` | All (own sections) | 5 |

---

## What each dataset notebook must contain (01 to 05)

Same structure for every dataset, so the results line up in the report.

**Phase 2 — Data understanding**
1. Load the file and compare rows and columns with the official numbers in `docs/datasets.md`.
2. Columns, data types and units (`df.info()`, grouped: identifiers, ports/protocol, bytes/packets, time, TCP flags, labels).
3. Class distribution: flows per attack label (table + plot saved in `figures/`).
4. Quality problems: NaN, infinite values, duplicates, constant columns, unexpected label spellings.
5. A markdown table: each problem found → planned solution (no code yet).

**Phase 3 — Preprocessing**
6. `clean(df, SOURCE)` — drops ID columns, handles inf/NaN, removes duplicates.
7. `map_labels(df, label_col, SOURCE)` — adds `attack_label`, `attack_family`, `is_attack`, `source_dataset`.
8. Outlier investigation per class, with a written justification of the decision (in intrusion data,
   extreme values are often the attack itself, so do not remove them blindly).
9. `sample_per_label(df)` — cap 200k flows per label, every rarer label kept in full.
10. `quality_report(...)` and `save_clean(df, SOURCE)` — writes `tables/{SOURCE}_quality.csv`,
    `tables/{SOURCE}_labels.csv` and `data/processed/{SOURCE}_clean.parquet`.

Any decision not covered by `config.py` goes into `docs/decision_log.md` **before** you apply it.

## Expected from each member

### Ahmed Hamouda — `01_unsw`, `02_cic18`, `06_merge_netflow`
- UNSW-NB15 and CIC-2018 through phases 2 and 3 as above.
- CIC-2018 has ~20 million rows: read it in chunks if memory is tight.
- `06_merge_netflow`: load the 4 NetFlow Parquet files, confirm identical columns and data types,
  concatenate, then check: no NaN / inf / duplicates, every label maps to exactly one family,
  sampling caps respected. Compare one shared class (e.g. DoS) across sources. Save
  `data/processed/netflow_merged.parquet`.
- In `07_eda`: correlation heatmap, Mann–Whitney U test, Kolmogorov–Smirnov test.
- In `08_feature_engineering`: train/test split and feature selection.

### Cyrine Chabbar — `03_ton`, `04_bot`
- ToN-IoT and BoT-IoT through phases 2 and 3 as above.
- ToN-IoT is the largest file (~27.5 million rows): read it in chunks if needed.
- BoT-IoT is 99.7% attacks: document that it is not used to describe benign traffic.
- Dataset comparison table and class-distribution plots for the 4 NetFlow sources, built from the
  `tables/*_quality.csv` and `tables/*_labels.csv` files.
- In `07_eda`: descriptive statistics, plots, relationships between variables, Kruskal–Wallis + Dunn test.
- In `08_feature_engineering`: new features and encoding.

### Yassine Mtibaa — `05_ciciot2023`
- CICIoT2023 through phases 2 and 3 as above.
- The data is split across many CSV files: load them one by one.
- First check the exact label spellings; add any label missing from `TAXONOMY` in `config.py`
  (after telling the team) — `map_labels` stops with an error until every label is mapped.
- Write why CICIoT2023 is not merged with the NetFlow data (different features, measured differently).
- In `07_eda`: normality check, chi-square test, CICIoT2023 comparison at family level.
- In `08_feature_engineering`: transformations and scaling (fitted on the training set only).

## Before you commit

- Restart the kernel and run all cells, so the notebook runs cleanly from top to bottom.
- Clear very large outputs to keep the repository small.
- Never commit files from `data/` (they are ignored automatically).
