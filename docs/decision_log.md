# Decision log

Every cleaning or taxonomy decision that `src/config.py` does not already cover is written here
**before** it is applied, and agreed by the team. This file becomes the "Preprocessing methodology"
section of the report.

| Date | Member | Dataset | Decision | Reason | Agreed by |
|---|---|---|---|---|---|
| 2026-10-17 | All | All | Shared contract in `src/config.py`: drop ID columns, inf → NaN → drop, drop exact duplicates, cap 200k flows per label (random_state=42) | Same cleaning for every source, so differences between networks reflect the traffic, not preprocessing | All |
| 2026-10-17 | All | NetFlow v3 | Merge the 4 NetFlow v3 datasets; keep CICIoT2023 separate | NetFlow v3 files share 53 identical features; CICIoT2023 features are measured differently | All |
|  |  |  |  |  |  |
