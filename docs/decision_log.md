# Decision log

Every cleaning or taxonomy decision that `src/config.py` does not already cover is written here
**before** it is applied, and agreed by the team. This file becomes the "Preprocessing methodology"
section of the report.

| Date | Member | Dataset | Decision | Reason | Agreed by |
|---|---|---|---|---|---|
| 2026-10-17 | All | All | Shared contract in `src/config.py`: drop ID columns, inf → NaN → drop, drop exact duplicates, cap 200k flows per label (random_state=42) | Same cleaning for every source, so differences between networks reflect the traffic, not preprocessing | All |
| 2026-10-17 | All | NetFlow v3 | Merge the 4 NetFlow v3 datasets; keep CICIoT2023 separate | NetFlow v3 files share 53 identical features; CICIoT2023 features are measured differently | All |
| 2026-10-17 | Yassine Mtibaa | IoT23 | Use the `MERGED_CSV` release (63 files, 45,019,243 rows, 39 features + `Label`) and read only that folder, never `CSV/` as well | The CIC download contains the same data twice; the release differs from the 2023 documentation, so all counts come from the loaded files | Pending team |
| 2026-10-17 | Yassine Mtibaa | IoT23 | Call `map_labels(df, "Label", "IoT23")` (the files use `Label`, not `label` as in `CICIOT_LABEL_COL`); no TAXONOMY change needed, all 34 UPPERCASE labels already map | Avoids a KeyError without changing the shared contract | Pending team |
| 2026-10-17 | Yassine Mtibaa | IoT23 | Apply `clean()` file by file, then `drop_duplicates()` again after concatenating the 63 files | 9.3 GB does not fit in one DataFrame; duplicates also occur across files (≈ 51 % of rows are exact duplicates) | Pending team |
| 2026-10-17 | Yassine Mtibaa | IoT23 | Set the 2 negative `IAT` values to NaN before `clean()` (rows then dropped) | A negative time between packets is impossible | Pending team |
| 2026-10-17 | Yassine Mtibaa | IoT23 | **Open question:** 610,472 feature vectors (≈ 13.3 M rows) carry more than one label, almost all DoS vs DDoS of the same flood type. Proposal: keep them for EDA (they are a finding for RQ2) and report them; drop them only before any future model training | `clean()` does not catch them because the label differs; removing them silently would hide that DoS and DDoS are indistinguishable at window level | Pending team |
| 2026-10-17 | Yassine Mtibaa | IoT23 | Keep structural values: `Header_Length` = 0 (ICMP/GRE), packets > 1,514 bytes (segmentation offload), TTL = 0 (non-IP windows) | Valid measurements explained by the protocol or the capture, not entry errors | Pending team |
| 2026-10-17 | Yassine Mtibaa | IoT23 | Redundant columns (`LLC`, `Tot size`, `Variance`, `Tot sum`, 4 × `*_count`), near-constant columns and `Number` are kept in phase 3 and decided in feature selection (phase 5) | Team rule 3: column selection and encoding are feature engineering | Pending team |
|  |  |  |  |  |  |
