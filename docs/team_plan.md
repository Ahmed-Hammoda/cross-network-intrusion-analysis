# Team plan

## Task split

| Member | Datasets | Also responsible for |
|---|---|---|
| Member 1 | NF-UNSW-NB15-v3, NF-CSE-CIC-IDS2018-v3 | Phase 1 (business understanding), NetFlow feature dictionary, final merge |
| Member 2 | NF-ToN-IoT-v3, NF-BoT-IoT-v3 | Dataset comparison table, class-balance plots for NetFlow data |
| Member 3 | CICIoT2023 | CICIoT2023 feature dictionary, "why not merged" section |

## Schedule

| Day | Work |
|---|---|
| Sat | Phase 1 + Phase 2: business understanding, data understanding (rows, columns, types, units, problems, planned solutions) |
| Sun | Phase 3: preprocessing with code, outliers, merge / integration decisions |
| Mon | Phase 4: EDA, descriptive statistics, correlations, hypothesis tests |
| Tue | Phase 5: feature engineering |
| Wed | Presentation + report |

## Notebook per member (avoids git merge conflicts)

| Notebook | Owner |
|---|---|
| `notebooks/01_unsw.ipynb` | Member 1 |
| `notebooks/02_cic18.ipynb` | Member 1 |
| `notebooks/03_ton.ipynb` | Member 2 |
| `notebooks/04_bot.ipynb` | Member 2 |
| `notebooks/05_ciciot2023.ipynb` | Member 3 |
| `notebooks/06_merge_netflow.ipynb` | Member 1 |

## Research questions

1. Which flow features best separate benign traffic from attacks, and does that change by attack family?
2. Are attack families statistically distinguishable from each other using flow statistics?
3. Do the same attack types (DoS, scanning, brute force) look statistically the same on different networks?
4. How severe is class imbalance, and which rare attacks will need special handling later?
