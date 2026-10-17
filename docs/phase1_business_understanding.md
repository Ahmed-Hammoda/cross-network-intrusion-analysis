# Phase 1 — Business understanding

> Draft — Member 1. Status: 🔄 In progress. Team review before Sunday.

## 1.1 Project context

Organisations defend their networks with Network Intrusion Detection Systems (NIDS), which
inspect traffic and raise alerts when it looks malicious. Modern NIDS increasingly rely on
machine learning trained on labelled traffic datasets. But networks differ: an office network,
an industrial IoT network and a network of smart-home devices carry very different traffic,
and attackers target each differently.

Most published work trains and evaluates on a single dataset recorded in a single lab. Whether
what is learned on one network still holds on another is much less studied, and the main
obstacle has been that public datasets use different feature sets, so they cannot be combined.
The 2025 NetFlow v3 release removes that obstacle for four benchmark datasets by re-extracting
them into one shared set of 53 features.

## 1.2 Problem definition

We do not yet know, in a statistically grounded way, how attack traffic differs from normal
traffic across different network environments, which flow characteristics separate the
different attack families, and whether those characteristics stay the same from one network to
another.

This project builds one unified, cleaned, analysis-ready dataset from four NetFlow v3 datasets
(enterprise, lab, IoT/industrial and IoT botnet networks), analyses CICIoT2023 (real IoT devices)
alongside it, and maps all 54 attack labels to one shared taxonomy of 9 attack families. Using
exploratory analysis and hypothesis testing, it identifies the traffic characteristics that
distinguish attacks and tests whether they are consistent across networks. Model training is out
of scope for this phase.

## 1.3 Research questions

| # | Question | How we answer it |
|---|---|---|
| RQ1 | Which flow features best separate benign traffic from attacks, and does this differ by attack family? | Descriptive statistics, Mann–Whitney U with effect sizes, feature ranking |
| RQ2 | Are the attack families statistically distinguishable from each other using flow statistics? | Kruskal–Wallis with Dunn post-hoc tests, chi-square on protocol |
| RQ3 | Do the same attack types (DoS, scanning, brute force) look statistically the same on different networks? | Kolmogorov–Smirnov tests on shared features, per source |
| RQ4 | How severe is class imbalance, and which rare attacks will need special handling in future modelling? | Class distributions per source and family |

## 1.4 Success criteria

| # | Criterion | Measure |
|---|---|---|
| S1 | Clean data | 0 NaN, 0 infinite values, 0 exact duplicates in every cleaned file and in the merged dataset |
| S2 | Complete taxonomy | 100% of original labels mapped to exactly one family; no unmapped labels |
| S3 | No lost attacks | Every attack label present after sampling; every label below the cap kept in full |
| S4 | Valid integration | The 4 NetFlow sources have identical columns and data types before merging |
| S5 | Statistical evidence | At least 3 hypothesis tests, each justified, with effect sizes and interpretation |
| S6 | Justified features | A final feature set with a documented reason for every removed or created feature |
| S7 | Reproducibility | All notebooks run from a fresh clone using only the README instructions |
