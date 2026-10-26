# Phase 4 — Exploratory data analysis: merged NetFlow v3 data

**Owner:** Ahmed Hamouda · Notebook: [`notebooks/07_eda_netflow.ipynb`](../notebooks/07_eda_netflow.ipynb) ·
Figures: `figures/NetFlow_eda_*.png` · Tables: `tables/NetFlow_eda_*.csv`

Analysis of `data/processed/netflow_merged.parquet`, following the course lab (Lab 4). CICIoT2023 is analysed separately
in `07_eda_iot23` (Yassine Mtibaa).

## How the requirement is covered

| Phase 4 requirement | Notebook section |
|---|---|
| Descriptive statistics | §1 rows per family and network; §2 mean, median, std, IQR, skewness of 4 key variables, median per family |
| Plots | §1 bar chart of families; §3 histograms (log scale) and box plots by family |
| Correlation analysis / heatmaps | §4 Pearson and Spearman heatmaps of 12 traffic features |
| Relationships between variables | §5 Benign vs attack in each network; destination port range × family |
| Justified hypothesis tests with interpretation | §6 normality check, then Mann–Whitney U (SQ1) and Kolmogorov–Smirnov (SQ2) |

## Method

- **One row = one behaviour** (17,551,848 rows for 63,012,224 flows): identical flows are not independent observations.
- **Counts and summary statistics on all rows.** Box plots, correlation and the KS test use **one sample**: up to 10,000
  behaviours per network × family (`random_state = 42`), so every family and network is fairly represented.
  The Mann–Whitney test runs on all rows.
- **Non-parametric tests:** the normality check rejects normality for every variable, raw and log-transformed.
- **Effect sizes decide** (rank-biserial r, KS statistic D), because every p-value is ≈ 0 with this much data;
  p-values are Bonferroni-corrected.

## Hypothesis tests

| Test | Question | Result |
|---|---|---|
| Mann–Whitney U (SQ1) | In each network, does attack traffic differ from Benign traffic? (bytes in/out, packets, duration) | H₀ rejected in all 16 tests. Large effects in UNSW (attacks **smaller**, r up to −0.73) and ToN-IoT (attacks **larger**, r up to +0.69); small in CIC-2018 and BoT-IoT |
| Kolmogorov–Smirnov (SQ2) | Does Denial of service have the same distribution in every network? (bytes, duration) | H₀ rejected in all 12 pairs; 9 clearly different (D > 0.3). Duration D = 0.99 between ToN-IoT and BoT-IoT |

## Main findings

1. All traffic variables are strongly right-skewed and not normal → medians, log scales, Spearman, non-parametric tests.
2. Each attack family has its own typical flow, and the destination port range is strongly linked to the family.
3. **SQ1:** attacks differ from normal traffic, but the direction depends on the network (smaller in UNSW, larger in
   ToN-IoT) — no single variable works everywhere.
4. **SQ2:** the same attack family (Denial of service) produces clearly different traffic in different networks.
5. **Next:** log transform, ports as categories, one variable per correlated group (phase 5). A drop in performance on
   an unseen network is expected (SQ3).
