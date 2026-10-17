# Phase 2 — Data understanding

> Template — each member fills in the section for their own datasets.
> General dataset descriptions are in `datasets.md`; attack descriptions in `attack_taxonomy.md`.

## 2.1 Data sources

See `datasets.md` (provenance, collection method, citation, download link for each dataset).

## 2.2 Per-dataset description

Copy this block for each dataset.

### `<KEY>` — `<dataset name>` (owner: <member name>)

**Dimensions**

| | Official | Loaded | Match? |
|---|---|---|---|
| Rows | | | |
| Columns | | | |

**Data types and units**

| Group | Columns | Type | Unit |
|---|---|---|---|
| Identifiers | | | |
| Ports / protocol | | | |
| Volume (bytes, packets) | | | |
| Time (duration, timestamps, IAT) | | | |
| TCP flags | | | |
| Labels | | | |

**Key variables** — the 5–8 columns most relevant to our research questions, and why.

**Class distribution** — table of flows per `Attack` label (and figure in `figures/`).

**Initial quality problems and planned solutions (no code)**

| # | Problem found | Columns / rows affected | Planned solution | Rule in `config.py`? |
|---|---|---|---|---|
| 1 | | | | |

## 2.3 Cross-dataset comparison (Cyrine Chabbar)

Table comparing the five datasets: rows, features, attack share, number of labels, network type.

## 2.4 Feature dictionaries

- NetFlow v3 — 53 features (Ahmed Hamouda): `netflow_feature_dictionary.md`
- CICIoT2023 — 45 features (Yassine Mtibaa): `ciciot_feature_dictionary.md`
