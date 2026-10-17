# Phase 1 — Business understanding

## 1.1 Project context

Every organisation connected to the internet is a target. Its network is constantly probed by
scans looking for weaknesses, flooded by denial-of-service attacks that take services offline,
attacked with password guessing, and infected by malware that turns its devices into bots. A single
missed attack can mean stolen data, stopped services and lost money and trust.

To defend themselves, organisations use **Network Intrusion Detection Systems (NIDS)**: systems
that monitor network traffic and raise an alert when it looks malicious. Security teams depend on
these alerts every day, and they face two costly failures:

- **missed attacks** — the system stays silent while an attack is happening;
- **false alarms** — the system alerts on normal traffic, wasting analysts' time until real alerts
  get ignored.

Modern NIDS increasingly use machine learning, learning what attacks look like from labelled traffic.
But organisations run very different networks: offices, industrial IoT systems, smart devices. A
detector trained on one kind of network often performs much worse on another, and an organisation
usually cannot collect and label its own attack data before deploying a detector.

## 1.2 Business problem

> Organisations need an intrusion detection approach that recognises cyberattacks accurately, tells
> the security team **what kind** of attack is happening, and stays reliable when it is used on a
> **different type of network** from the one it was trained on.

Most detection models are built and tested on a single network, so their real-world reliability on
other networks is unknown. Deploying such a model can give organisations a false sense of security.

## 1.3 Problem definition

We translate the business problem into a data science problem:

1. **Integrate** traffic recorded on five different networks — an office network, a lab network, an
   industrial IoT network, an IoT botnet network and a network of real IoT devices — into consistent,
   analysis-ready data.
2. **Organise** all 54 attack types found in these sources into one shared taxonomy of 9 attack
   families.
3. **Analyse** which traffic characteristics reveal each attack family, and whether they hold from
   one network to another.
4. **Build and evaluate** a supervised classification model at two levels:
   - **binary** — is this traffic normal or an attack?
   - **multi-class** — which attack family does it belong to?

   and measure its performance on a network it was not trained on.

## 1.4 Research questions

### Main research question

> **How can traffic collected from different network environments be used to detect cyberattacks
> and identify their type reliably, including on networks the detection model has never seen?**

### Sub-questions

| | Sub-question |
|---|---|
| **SQ1** | Which traffic characteristics best distinguish normal traffic from attack traffic, and how do they differ across attack families? |
| **SQ2** | How consistent is the traffic behaviour of the same attack type across different network environments? |
| **SQ3** | How accurately can a model detect attacks and identify their family, and how much does its performance change on a network it was not trained on? |

SQ1 identifies *what* reveals an attack, SQ2 tests *whether* it transfers between networks, and SQ3
measures *how well* a model can use it — together they answer the main question.

## 1.5 Success criteria

The project is successful if:

1. **The main question is answered with evidence** — every sub-question has a clear answer supported
   by statistical results, visualisations or model evaluation, not by assumptions.
2. **The key indicators of each attack family are identified** — we can explain what gives each type
   of attack away.
3. **The detection model is useful to a security team** — it detects most attacks while raising few
   false alarms, and it names the attack family.
4. **Its reliability on new networks is measured honestly** — we know how well it works on an unseen
   network and where it fails.
5. **The work is understandable and reproducible** — every team member can explain every decision,
   and anyone can repeat the work from the repository.
