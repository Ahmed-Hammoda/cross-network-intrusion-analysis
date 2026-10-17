# CICIoT2023 feature dictionary (`IoT23`)

> Owner: Yassine Mtibaa · Task 2.7 · Source: the `MERGED_CSV` release (63 files, 45,019,243 rows).
> Ranges are computed on all rows by `notebooks/05_ciciot2023.ipynb` (`tables/IoT23_phase2_columns.csv`).

## What one row is

A CICIoT2023 row is **one window of up to 100 consecutive packets**, not one flow. `Number` gives the
number of packets in the window (median 100). Every feature is a summary over that window: an average,
a **share** between 0 and 1, a count, or a size statistic. This is why "flags" can equal 0.99 and why
TTL can be fractional. There is no identifier, port or timestamp column.

The release we use has **39 features + `Label`**. Compared with the original 2023 release documented
on the UNB website (46 features), `Duration` was renamed `Time_To_Live`, `IGMP` was added, and
`flow_duration`, `Srate`, `Drate`, `urg_count`, `Magnitue`, `Radius`, `Covariance` and `Weight` were removed.

## Features

| # | Column | Group | Meaning | Unit | Stored as | Range (all rows) | Notes |
|---|---|---|---|---|---|---|---|
| 1 | `Header_Length` | Ports / protocol | Average header length of the packets in the window | bytes | float | 0 – 60 | 0 = no TCP/UDP header (ICMP, GRE): structural value |
| 2 | `Protocol Type` | Ports / protocol | IANA protocol number of the window | code | int | {0, 1, 2, 6, 17, 47} | Categorical: 1 ICMP, 2 IGMP, 6 TCP, 17 UDP, 47 GRE, 0 other |
| 3 | `Time_To_Live` | Ports / protocol | Average IP time-to-live | hops | float | 0 – 255 | 0 only in non-IP (ARP) windows |
| 4 | `Rate` | Time | Packets per second in the window | packets/s | float | 0 – 1.57 × 10⁷ (+ inf) | 991 infinite values |
| 5 | `fin_flag_number` | TCP flags | Share of packets with FIN set | share 0–1 | float | 0 – 1 | Name suggests 0/1; it is a proportion |
| 6 | `syn_flag_number` | TCP flags | Share of packets with SYN set | share 0–1 | float | 0 – 1 | |
| 7 | `rst_flag_number` | TCP flags | Share of packets with RST set | share 0–1 | float | 0 – 1 | |
| 8 | `psh_flag_number` | TCP flags | Share of packets with PSH set | share 0–1 | float | 0 – 1 | |
| 9 | `ack_flag_number` | TCP flags | Share of packets with ACK set | share 0–1 | float | 0 – 1 | |
| 10 | `ece_flag_number` | TCP flags | Share of packets with ECE set | share 0–1 | float | 0 – 1 | Near-constant (≈ always 0) |
| 11 | `cwr_flag_number` | TCP flags | Share of packets with CWR set | share 0–1 | float | 0 – 1 | Near-constant (≈ always 0) |
| 12 | `ack_count` | TCP flags | Packets with ACK set | packets | int | 0 – 100 | = `ack_flag_number` × `Number` (redundant) |
| 13 | `syn_count` | TCP flags | Packets with SYN set | packets | int | 0 – 100 | = `syn_flag_number` × `Number` (redundant) |
| 14 | `fin_count` | TCP flags | Packets with FIN set | packets | int | 0 – 100 | = `fin_flag_number` × `Number` (redundant) |
| 15 | `rst_count` | TCP flags | Packets with RST set | packets | int | 0 – 100 | = `rst_flag_number` × `Number` (redundant) |
| 16 | `HTTP` | Protocol shares | Share of packets that are HTTP | share 0–1 | float | 0 – 1 | |
| 17 | `HTTPS` | Protocol shares | Share of packets that are HTTPS | share 0–1 | float | 0 – 1 | |
| 18 | `DNS` | Protocol shares | Share of packets that are DNS | share 0–1 | float | 0 – 1 | |
| 19 | `Telnet` | Protocol shares | Share of packets that are Telnet | share 0–1 | float | 0 – 0.6 | Near-constant |
| 20 | `SMTP` | Protocol shares | Share of packets that are SMTP | share 0–1 | float | 0 – 0.9 | Near-constant |
| 21 | `SSH` | Protocol shares | Share of packets that are SSH | share 0–1 | float | 0 – 1 | Near-constant |
| 22 | `IRC` | Protocol shares | Share of packets that are IRC | share 0–1 | float | 0 – 0.9 | Near-constant |
| 23 | `TCP` | Protocol shares | Share of packets that are TCP | share 0–1 | float | 0 – 1 | Agrees with `Protocol Type` = 6 |
| 24 | `UDP` | Protocol shares | Share of packets that are UDP | share 0–1 | float | 0 – 1 | Agrees with `Protocol Type` = 17 |
| 25 | `DHCP` | Protocol shares | Share of packets that are DHCP | share 0–1 | float | 0 – 1 | Near-constant |
| 26 | `ARP` | Protocol shares | Share of packets that are ARP | share 0–1 | float | 0 – 1 | |
| 27 | `ICMP` | Protocol shares | Share of packets that are ICMP | share 0–1 | float | 0 – 1 | Agrees with `Protocol Type` = 1 |
| 28 | `IGMP` | Protocol shares | Share of packets that are IGMP | share 0–1 | float | 0 – 1 | Near-constant |
| 29 | `IPv` | Protocol shares | Share of packets that are IP | share 0–1 | float | 0 – 1 | |
| 30 | `LLC` | Protocol shares | Share of packets with an LLC header | share 0–1 | float | 0 – 1 | Identical to `IPv` (redundant) |
| 31 | `Tot sum` | Volume | Total bytes in the window | bytes | int | 60 – 316,492 | = `AVG` × `Number` (redundant) |
| 32 | `Min` | Volume | Smallest packet in the window | bytes | int | 42 – 13,583 | Values > 1,514: captured before segmentation offload |
| 33 | `Max` | Volume | Largest packet in the window | bytes | int | 46 – 52,194 | > 1,514 in 687,281 rows (33 % of benign) |
| 34 | `AVG` | Volume | Mean packet size | bytes | float | 46 – 13,583 | |
| 35 | `Std` | Volume | Standard deviation of packet size | bytes | float | 0 – 11,655 | NaN when `Number` = 1 (670 rows) |
| 36 | `Tot size` | Volume | Mean packet size | bytes | float | 46 – 13,583 | Identical to `AVG` (redundant) |
| 37 | `IAT` | Time | Mean time between packets | seconds | float | −0.018 – 78,612 | 2 negative values (impossible) |
| 38 | `Number` | Volume | Packets in the window | packets | int | 1 – 100 | < 100 in every non-flood row: capture artefact |
| 39 | `Variance` | Volume | Variance of packet size | bytes² | float | 0 – 1.36 × 10⁸ | = `Std`² (redundant) |
| 40 | `Label` | Labels | Traffic class | text | str | 34 labels | UPPERCASE in this release; mapped by `map_labels` |

## Summary of column issues

- **Redundant (8):** `LLC`, `Tot size`, `Variance`, `Tot sum`, `ack_count`, `syn_count`, `fin_count`, `rst_count`. Each is an exact copy or formula of another column on every complete row.
- **Near-constant (8):** `Telnet`, `SMTP`, `IRC`, `IGMP`, `DHCP`, `SSH`, `ece_flag_number`, `cwr_flag_number`.
- **Categorical stored as number (1):** `Protocol Type`.
- **Misleading names (7):** the `*_flag_number` columns are shares, not flags.
- **Capture artefact (1):** `Number`.

Removal and encoding happen in feature engineering (phase 5), after the train/test split.
