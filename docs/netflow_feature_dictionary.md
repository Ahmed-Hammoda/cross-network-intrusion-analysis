# NetFlow v3 feature dictionary (53 features)

**Owner:** Ahmed Hamouda · Source: the official feature list of the University of Queensland
(`NetFlow_v3_Features.csv`), checked against the data. The same 53 features exist in all four NetFlow v3 datasets
(UNSW, CIC18, ToN, BoT), followed by two label columns.

**Corrections to the official list** (problem K16 in the data problems report): `DURATION_OUT` is described as
"client to server" but measures the server-to-client stream; the four `DST_TO_SRC_IAT_*` columns are all described as
"minimum" but are the minimum, maximum, average and standard deviation; `ICMP_TYPE` is type × 256 + code. The meanings
below are the corrected ones.

**Direction:** "in" / "src → dst" = from the client (who started the flow) to the server; "out" / "dst → src" = the
answer from the server.

**Last column — what happened in the project:** ✅ = one of the 59 final features (phase 5; numeric columns are
log(1 + x)-transformed and robust-scaled) · 🔁 = encoded into new 0/1 columns · ❌ = not a feature, with the decision
code of `report/data_problems/phase2_data_problems.pdf` or the phase 5 reason.

## Identifiers

| Feature | Meaning | Unit | Type | In the project |
|---|---|---|---|---|
| `IPV4_SRC_ADDR` | IPv4 address of the client | — | text | ❌ dropped in cleaning: identifies the machine, reveals the label (M3) |
| `IPV4_DST_ADDR` | IPv4 address of the server | — | text | ❌ dropped in cleaning (M3) |
| `L4_SRC_PORT` | source port of the client | — | code | ❌ random temporary port (M5) |
| `DNS_QUERY_ID` | DNS transaction identifier | — | code | ❌ random number (M5) |
| `FLOW_START_MILLISECONDS` | start time of the flow | ms since 1970 | integer → datetime | ❌ reveals the lab's attack schedule (M2); used only for time plots |
| `FLOW_END_MILLISECONDS` | end time of the flow | ms since 1970 | integer → datetime | ❌ same as the start time (M2) |

## Protocol and application

| Feature | Meaning | Unit | Type | In the project |
|---|---|---|---|---|
| `L4_DST_PORT` | destination port (the service contacted) | — | code | 🔁 3 port ranges: `port_well_known`, `port_registered`, `port_dynamic` |
| `PROTOCOL` | IP protocol number (6 TCP, 17 UDP, 1 ICMP, 58 ICMPv6) | — | code | 🔁 `proto_udp`, `proto_other` (`proto_tcp` removed: ρ = −0.98 with `proto_udp`) |
| `L7_PROTO` | application protocol detected by nDPI, as `main.sub` | — | code (float) | 🔁 split into `L7_MAIN` / `L7_SUB` (U3, B3, C3, T3); `L7_MAIN` → `l7_*` columns (protocols ≥ 1 %); `L7_SUB` dropped (set for 0.07 % of flows) |
| `ICMP_TYPE` | ICMP type × 256 + ICMP code | — | code | ❌ set to 0 outside ICMP (M6); only 0.98 % of flows, already marked by `proto_other` |
| `ICMP_IPV4_TYPE` | ICMP type | — | code | ❌ copy of `ICMP_TYPE` ÷ 256 (M8) |
| `DNS_QUERY_TYPE` | DNS query type (1 = A, 28 = AAAA, …) | — | code | ❌ detail of DNS queries, already marked by the DNS columns |
| `DNS_TTL_ANSWER` | time-to-live of the first A record of the DNS answer | seconds | integer | ✅ (invalid values > 2³¹ − 1 set to 0, M9) |
| `FTP_COMMAND_RET_CODE` | return code of an FTP command | — | code | ❌ identifies the lab's FTP servers (M10) |

## Volume

| Feature | Meaning | Unit | Type | In the project |
|---|---|---|---|---|
| `IN_BYTES` | bytes sent by the client | bytes | integer | ✅ |
| `OUT_BYTES` | bytes sent back by the server | bytes | integer | ✅ |
| `IN_PKTS` | packets sent by the client | packets | integer | ✅ |
| `OUT_PKTS` | packets sent back by the server | packets | integer | ✅ |
| `RETRANSMITTED_IN_BYTES` | TCP bytes retransmitted by the client | bytes | integer | ✅ |
| `RETRANSMITTED_IN_PKTS` | TCP packets retransmitted by the client | packets | integer | ❌ ρ = 0.98 with `RETRANSMITTED_IN_BYTES` (phase 5) |
| `RETRANSMITTED_OUT_BYTES` | TCP bytes retransmitted by the server | bytes | integer | ✅ |
| `RETRANSMITTED_OUT_PKTS` | TCP packets retransmitted by the server | packets | integer | ❌ ρ = 1.00 with `RETRANSMITTED_OUT_BYTES` (phase 5) |

## Packet sizes

| Feature | Meaning | Unit | Type | In the project |
|---|---|---|---|---|
| `LONGEST_FLOW_PKT` | largest packet of the flow | bytes | integer | ✅ |
| `SHORTEST_FLOW_PKT` | smallest packet of the flow | bytes | integer | ✅ |
| `MIN_IP_PKT_LEN` | smallest IP packet length | bytes | integer | ❌ 0 on one-way flows, otherwise equal to `SHORTEST_FLOW_PKT` (M7) |
| `MAX_IP_PKT_LEN` | largest IP packet length | bytes | integer | ❌ always equal to `LONGEST_FLOW_PKT` (M7) |
| `NUM_PKTS_UP_TO_128_BYTES` | packets of at most 128 bytes | packets | integer | ✅ |
| `NUM_PKTS_128_TO_256_BYTES` | packets of 129–256 bytes | packets | integer | ✅ |
| `NUM_PKTS_256_TO_512_BYTES` | packets of 257–512 bytes | packets | integer | ✅ |
| `NUM_PKTS_512_TO_1024_BYTES` | packets of 513–1024 bytes | packets | integer | ✅ |
| `NUM_PKTS_1024_TO_1514_BYTES` | packets of 1025–1514 bytes | packets | integer | ✅ |

## Time and rate

| Feature | Meaning | Unit | Type | In the project |
|---|---|---|---|---|
| `FLOW_DURATION_MILLISECONDS` | duration of the flow (cut at about 120 s by the exporter) | ms | integer | ✅ |
| `DURATION_IN` | duration of the client-to-server stream | ms | integer | ✅ |
| `DURATION_OUT` | duration of the server-to-client stream | ms | integer | ✅ |
| `SRC_TO_DST_SECOND_BYTES` | client-to-server bytes per second | bytes/s | float or integer | ❌ dropped before cleaning: NaN / inf on 0-ms flows, type differs between datasets (U2, B2, C3, T3) |
| `DST_TO_SRC_SECOND_BYTES` | server-to-client bytes per second | bytes/s | float or integer | ❌ same as above |
| `SRC_TO_DST_AVG_THROUGHPUT` | average client-to-server throughput | bits/s | integer | ✅ |
| `DST_TO_SRC_AVG_THROUGHPUT` | average server-to-client throughput | bits/s | integer | ✅ |
| `SRC_TO_DST_IAT_MIN` | smallest gap between two client packets | ms | integer | ✅ |
| `SRC_TO_DST_IAT_MAX` | largest gap between two client packets | ms | integer | ✅ |
| `SRC_TO_DST_IAT_AVG` | average gap between client packets | ms | integer | ❌ ρ = 0.96 with `SRC_TO_DST_IAT_MAX` (phase 5) |
| `SRC_TO_DST_IAT_STDDEV` | standard deviation of the gaps between client packets | ms | integer | ✅ |
| `DST_TO_SRC_IAT_MIN` | smallest gap between two server packets | ms | integer | ✅ |
| `DST_TO_SRC_IAT_MAX` | largest gap between two server packets | ms | integer | ✅ |
| `DST_TO_SRC_IAT_AVG` | average gap between server packets | ms | integer | ❌ ρ = 0.97 with `DST_TO_SRC_IAT_MAX` (phase 5) |
| `DST_TO_SRC_IAT_STDDEV` | standard deviation of the gaps between server packets | ms | integer | ✅ |

## TCP behaviour

| Feature | Meaning | Unit | Type | In the project |
|---|---|---|---|---|
| `TCP_FLAGS` | all TCP flags seen in the flow (bitmask) | — | code | ❌ = `CLIENT_TCP_FLAGS` OR `SERVER_TCP_FLAGS` (M8) |
| `CLIENT_TCP_FLAGS` | TCP flags sent by the client (bitmask: FIN 1, SYN 2, RST 4, PSH 8, ACK 16, URG 32, ECE 64, CWR 128) | — | code | 🔁 one 0/1 column per flag (`client_syn`, …); `client_urg` (near-constant) and `client_ece` (= `client_cwr`) removed |
| `SERVER_TCP_FLAGS` | TCP flags sent by the server (same bitmask) | — | code | 🔁 one 0/1 column per flag (`server_rst`, …); `server_urg` and `server_cwr` removed (near-constant) |
| `TCP_WIN_MAX_IN` | largest TCP window announced by the client | bytes | integer | ❌ set by each lab machine's operating system: a testbed fingerprint (M10, phase 5) |
| `TCP_WIN_MAX_OUT` | largest TCP window announced by the server | bytes | integer | ❌ same fingerprint (M10, phase 5) |
| `MIN_TTL` | smallest IP time-to-live in the flow | hops | integer | ❌ identifies the lab's machines (M4) |
| `MAX_TTL` | largest IP time-to-live in the flow | hops | integer | ❌ same (M4) |

## Labels (not features)

| Column | Meaning | In the project |
|---|---|---|
| `Label` | 0 = Benign, 1 = attack | dropped after `map_labels()`: identical to `is_attack` (K15) |
| `Attack` | attack name, as spelled in each dataset | kept as the raw name; mapped to `attack_label` and `attack_family` (shared taxonomy) |

## Summary

| Status | Count |
|---|---|
| ✅ kept as a final feature | 25 |
| 🔁 encoded into 0/1 columns | 5 (`L4_DST_PORT`, `PROTOCOL`, `L7_PROTO`, `CLIENT_TCP_FLAGS`, `SERVER_TCP_FLAGS`) |
| ❌ not a feature | 23 |
| **Total** | **53** |

The final model input also contains 8 created features (ratios, rates, behaviour flags) and the encoded columns:
59 features in total, listed in `tables/NetFlow_fe_dictionary.csv` and `report/features/phase5_features_report.pdf`.
