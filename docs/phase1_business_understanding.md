# Phase 1 — Business understanding

> Owner: Ahmed Hamouda · Status: ✅ Done · To be reviewed by Cyrine Chabbar and Yassine Mtibaa
>
> This phase describes the **whole project**: the midterm (data preparation and analysis, CRISP-DM
> phases 1–5) and the final part (building and evaluating a detection model).

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

Today, most detection models are built and tested on a single network, so their real-world
reliability on other networks is unknown. Deploying such a model can give organisations a false
sense of security.

## 1.3 Problem definition (data science problem)

We translate the business problem into a data science project in two parts:

| Part | When | CRISP-DM phases | What we do |
|---|---|---|---|
| **Midterm** | This week | 1–5: business understanding → feature engineering | Combine traffic from several networks into one consistent dataset, organise all attacks into one taxonomy, analyse which traffic characteristics reveal each attack family and whether they hold across networks, and prepare the features for modelling |
| **Final** | Next week | Modelling and evaluation | Train classification models that detect attacks and identify their family, and test them on a network they were not trained on |

The modelling task is a **supervised classification problem** at two levels:

- **binary** — is this traffic normal or an attack?
- **multi-class** — which of the 9 attack families does it belong to?

## 1.4 Research questions

### Main research question

> **How can traffic collected from different network environments be used to detect cyberattacks
> and identify their type reliably, including on networks the detection model has never seen?**

### Sub-questions

| | Sub-question | Answered in |
|---|---|---|
| **SQ1** | Which traffic characteristics best distinguish normal traffic from attack traffic, and how do they vary across attack families? | Midterm — EDA, hypothesis tests |
| **SQ2** | To what extent do the different attack families differ from each other in their traffic behaviour? | Midterm — EDA, hypothesis tests |
| **SQ3** | How consistent is the traffic behaviour of the same attack type across different network environments? | Midterm — cross-network tests |
| **SQ4** | How are the attack types distributed, and which ones are too rare to be detected reliably without special handling? | Midterm — class distribution analysis |
| **SQ5** | How accurately can a model detect attacks and identify their family when trained on traffic from several networks? | Final — modelling and evaluation |
| **SQ6** | How much does detection performance change when the model is applied to a network it was not trained on, and which attack families are affected most? | Final — cross-network evaluation |

SQ1–SQ4 build the understanding that SQ5 and SQ6 rely on: the midterm shows *what* separates
attacks and *whether* it transfers between networks; the final part measures *how well* a model can
use it.

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
