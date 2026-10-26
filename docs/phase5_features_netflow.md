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
| 4 Selection | exact copies (0), fingerprints (TCP window, 2), near-constant ≥ 99.5 % (3), \|ρ\| ≥ 0.95 keep higher mutual information (8) | 72 → **59 features** |
| 5 Final set | 25 original, 8 created, 26 encoded; dictionary and export | `data/processed/netflow_features.parquet` (634 MB, on the PC only), `tables/NetFlow_fe_dictionary.csv` |
| 6 PCA | 2-D view of the families (sample) | PC1 + PC2 = 42.8 % of the variance; Reconnaissance and Fuzzing form clusters, most families overlap |
| 7 Not used | hour-of-day (leaks the lab schedule), polynomial terms, binning of volumes, target encoding, train/test split | justified in the notebook, §7 |

## Main conclusions

1. The created features earn their place: 8 of the 9 survive the selection, and 3 are among the 5 most informative
   features (`in_bytes_per_pkt`, `out_in_ratio`, `out_bytes_per_pkt`).
2. The log transformation and robust scaling are necessary: the data are extremely skewed, and the outliers are the
   attacks. Columns with IQR = 0 are divided by their standard deviation; otherwise they dominate the PCA.
3. The final set keeps only traffic behaviour: no column identifies the network, the machine or the moment (important
   for SQ3).

## Shared with the CICIoT2023 part (Yassine Mtibaa)

- Same section order: creation → encoding → scaling / transformation → selection → final feature set → PCA.
- Same correlation threshold (|ρ| ≥ 0.95).
- Same note on refitting the learned steps on the training part before modelling.
