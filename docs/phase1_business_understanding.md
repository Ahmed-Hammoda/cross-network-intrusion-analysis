# Phase 1 — Business understanding

> Owner: Ahmed Hamouda · Status: ✅ Done · To be reviewed by Cyrine Chabbar and Yassine Mtibaa

## 1.1 Project context

Every organisation's network is constantly targeted by attacks: floods that take services down,
scans that look for weaknesses, password guessing and malware. To defend themselves, organisations
use **Network Intrusion Detection Systems (NIDS)**, which monitor network traffic and raise an alert
when something looks malicious.

Modern NIDS increasingly rely on data: they learn what attacks look like from large collections of
labelled network traffic. But networks are not all the same. An office network, an industrial IoT
network and a home full of smart devices carry very different traffic, and attackers target each of
them differently.

Most studies use one dataset recorded on one network, so it is rarely checked whether what holds for
one network also holds for another. The main reason is that public datasets describe traffic with
different features and cannot be combined. In 2025, researchers re-extracted four major benchmark
datasets into one shared set of 53 features, which makes this comparison possible for the first time
at this scale. Our project builds on that opportunity.

## 1.2 Problem definition

We do not clearly know which traffic characteristics separate attacks from normal traffic, how the
different types of attacks differ from each other, or whether these characteristics stay the same
across different kinds of networks.

To study this, we:

- **combine** four datasets from four different networks (office, lab, IoT/industrial, IoT botnet)
  into one unified dataset, and analyse a fifth dataset (real IoT devices) alongside it;
- **organise** all 54 attack types into 9 attack families;
- **analyse** the data with statistics and visualisations to find what makes attacks different and
  whether this holds across networks.

This phase does not build a detection model: it prepares and understands the data such a model
would need.

## 1.3 Research questions

| | Question |
|---|---|
| **RQ1** | Which traffic characteristics best distinguish normal traffic from attack traffic, and how do they vary across attack families? |
| **RQ2** | To what extent do the different attack families differ from each other in their traffic behaviour? |
| **RQ3** | How consistent is the traffic behaviour of the same attack type across different network environments? |
| **RQ4** | How are the attack types distributed, and which ones are too rare to be detected reliably without special handling? |

## 1.4 Success criteria

The project is successful if:

1. **Every research question is answered with evidence** — each answer is supported by statistical
   results and visualisations, not by assumptions.
2. **The key indicators of attacks are identified** — we can name the main characteristics that
   reveal each attack family.
3. **The cross-network comparison is clear** — we can state which attack behaviours hold across
   networks and which depend on the network.
4. **The next step is ready** — we deliver a justified feature set and a clear plan for building a
   detection model in the future.
5. **The work is understandable and reproducible** — every team member can explain every decision,
   and anyone can repeat the work from the repository.
