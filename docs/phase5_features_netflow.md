# Phase 5 — Feature engineering: merged NetFlow v3 data

**Owner:** Ahmed Hamouda · Notebook: [`notebooks/08_features_netflow.ipynb`](../notebooks/08_features_netflow.ipynb) ·
Report: [`report/features/phase5_features_report.pdf`](../report/features/phase5_features_report.pdf) ·
Figures: `figures/NetFlow_fe_*.png` · Tables: `tables/NetFlow_fe_*.csv`

> **Requirement:** explain feature selection, extraction/creation, encoding, and scaling/transformation when appropriate;
> justify the final feature set.

**No train/test split:** the project stops before modelling. The learned steps (scaling, the list of frequent application
protocols, the selection) are fitted on all the data; before any model they must be refitted on the training part only.

## Steps and results

| Step | What was done | Result |
|---|---|---|
| 0 Starting columns | Left out: timestamps, source port, DNS query ID, TTL, FTP code, raw label, network name (phase 2) | 31 numeric + 8 code columns |
| 1 Creation | `in_bytes_per_pkt`, `out_bytes_per_pkt`, `out_in_ratio`, `bytes_per_sec`, `pkts_per_sec`, `no_answer`, `one_packet`, `syn_only`, `hit_timeout` | each family stands out in at least one (e.g. Reconnaissance: 92 % one-packet SYN-only) |
| 2 Encoding | port → 3 ranges; protocol → TCP / UDP / other; TCP flags → one column per bit (client and server); L7 → protocols with ≥ 1 % + other | 32 yes/no columns; `L7_SUB`, `ICMP_TYPE`, `DNS_QUERY_TYPE` dropped with a reason |
| 3 Transformation / scaling | log(1 + x) on 36 numeric columns; (x − median) / IQR, or / std when IQR = 0 (5 columns) | columns with \|skewness\| ≤ 1: 0 → 17 of 36; comparable scales |
| 4 Selection | exact copies (0), fingerprints (TCP window, 2), near-constant ≥ 99.5 % (3), correlated pairs: H₀ \|ρ\| ≤ 0.90 rejected by a bootstrap test, keep higher mutual information (14), exact dependence (`port_dynamic`, 1), VIF > 10 (8) | 72 → **44 features** |
| 5 Final set | 17 original, 5 created, 22 encoded; dictionary and export | `data/processed/netflow_features.parquet` (351 MB, on the PC only), `tables/NetFlow_fe_dictionary.csv` |
| 6 PCA | 2-D view of the families (sample) | PC1 + PC2 = 43.2 % of the variance; Reconnaissance and Fuzzing form clusters, most families overlap |
| 7 Not used | hour-of-day (leaks the lab schedule), polynomial terms, binning of volumes, target encoding, train/test split | justified in the notebook, §7 |
| 8 Checks before modelling | missing values, constant columns, leakage columns, encoding, \|ρ\| < 0.90, full rank, VIF ≤ 10 | **7 of 7 pass** (largest VIF 9.84); 6 points to handle in modelling (`tables/NetFlow_fe_premodelling_checks.csv`) |

## Main conclusions

1. The created features earn their place: 5 of the 9 survive the selection, and the 2 most informative features are
   created ratios (`in_bytes_per_pkt`, `out_in_ratio`). They make the raw byte counts redundant (VIF > 2,000 after the log).
2. The log transformation and robust scaling are necessary: the data are extremely skewed, and the outliers are the
   attacks. Columns with IQR = 0 are divided by their standard deviation; otherwise they dominate the PCA.
3. The final set keeps only traffic behaviour: no column identifies the network, the machine or the moment (important
   for SQ3).
4. The final set is free of redundancy: no pair above |ρ| = 0.90, no exact linear dependence, every VIF ≤ 10. The EDA
   (§4.1) showed that the 12-column heatmap missed all 11 redundant pairs, so the selection tests all 72 candidates.

**Before modelling:** split first (by network for SQ3), refit the scaling and the selection on the training part, keep
the 27 % of behaviours that share a feature vector on one side of the split, use class weights and macro-F1.

## Shared with the CICIoT2023 part (Yassine Mtibaa)

- Same section order: creation → encoding → scaling / transformation → selection → final feature set → PCA.
- Same redundancy rule, in `src/redundancy.py`: |ρ| > 0.90 tested with a bootstrap (the threshold of the EDA), exact
  dependences, VIF ≤ 10, and the same checklist before modelling.
- Same note on refitting the learned steps on the training part before modelling.
