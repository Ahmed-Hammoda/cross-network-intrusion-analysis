# Team plan

Tasks, days and status are tracked in the [task board](TASK_BOARD.md).

## Ownership

| Member | Datasets | Notebooks | Also responsible for |
|---|---|---|---|
| Member 1 | NF-UNSW-NB15-v3, NF-CSE-CIC-IDS2018-v3 | `01_unsw`, `02_cic18`, `06_merge_netflow` | Phase 1, NetFlow feature dictionary, final merge |
| Member 2 | NF-ToN-IoT-v3, NF-BoT-IoT-v3 | `03_ton`, `04_bot` | Dataset comparison table, class-balance plots |
| Member 3 | CICIoT2023 | `05_ciciot2023` | CICIoT2023 feature dictionary, "why not merged" section |

`07_eda` and `08_feature_engineering` are shared: each member works in the sections assigned to
them on the task board.

## Why there are no dependencies between members

| Possible dependency | How it is removed |
|---|---|
| "I need your code to start" | Everyone calls the same shared functions in `src/config.py` |
| "Which family does label X go in?" | The taxonomy is fixed in `src/config.py` |
| "Your output doesn't fit my merge" | Same columns, file names and data types for every output |
| "Our report tables don't match" | `quality_report()` writes the same table format for everyone |

The only joining step is the merge in `06_merge_netflow`, which only reads files that already
follow the same format.
