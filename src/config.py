"""
Shared contract for the whole team.

Every member imports this file. Nobody changes it alone: any change is
agreed by the team first and written in docs/decision_log.md.

Usage in a notebook:
    import sys; sys.path.append("..")
    from src.config import *
"""

from pathlib import Path

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# 1. Paths (relative to the repository root, no hard-coded personal paths)
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
FIG_DIR = ROOT / "figures"
TABLE_DIR = ROOT / "tables"

for _d in (RAW_DIR, PROCESSED_DIR, FIG_DIR, TABLE_DIR):
    _d.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 2. Datasets and owners
# ---------------------------------------------------------------------------
DATASETS = {
    "UNSW":   {"file": "NF-UNSW-NB15-v3.csv",       "group": "netflow", "owner": "Member 1", "network": "Mixed lab"},
    "CIC18":  {"file": "NF-CSE-CIC-IDS2018-v3.csv", "group": "netflow", "owner": "Member 1", "network": "Enterprise / office"},
    "ToN":    {"file": "NF-ToN-IoT-v3.csv",         "group": "netflow", "owner": "Member 2", "network": "IoT / industrial"},
    "BoT":    {"file": "NF-BoT-IoT-v3.csv",         "group": "netflow", "owner": "Member 2", "network": "IoT botnet"},
    "IoT23":  {"file": "CICIoT2023/",               "group": "ciciot",  "owner": "Member 3", "network": "Real IoT devices"},
}

# ---------------------------------------------------------------------------
# 3. Shared attack taxonomy: original label -> (attack_label, attack_family)
#    Keys are matched case-insensitively after removing spaces, '-' and '_'.
# ---------------------------------------------------------------------------
BENIGN = "Benign"

FAMILIES = [
    "Denial of service",
    "Reconnaissance",
    "Credential attacks",
    "Web and injection",
    "Malware and botnets",
    "Exploitation and intrusion",
    "Interception and spoofing",
    "Fuzzing and crypto",
    "Data theft",
]

TAXONOMY = {
    # --- benign ---
    "Benign": (BENIGN, BENIGN),

    # --- NetFlow v3 labels (UNSW, CIC18, ToN, BoT) ---
    "DoS": ("DoS", "Denial of service"),
    "DDoS": ("DDoS", "Denial of service"),
    "Reconnaissance": ("Reconnaissance", "Reconnaissance"),
    "Scanning": ("Scanning", "Reconnaissance"),
    "Analysis": ("Analysis", "Reconnaissance"),
    "BruteForce": ("BruteForce", "Credential attacks"),
    "Password": ("Password", "Credential attacks"),
    "Web Attacks": ("Web Attacks", "Web and injection"),
    "Injection": ("Injection", "Web and injection"),
    "XSS": ("XSS", "Web and injection"),
    "Bot": ("Bot", "Malware and botnets"),
    "Backdoor": ("Backdoor", "Malware and botnets"),
    "Ransomware": ("Ransomware", "Malware and botnets"),
    "Worms": ("Worms", "Malware and botnets"),
    "Exploits": ("Exploits", "Exploitation and intrusion"),
    "Shellcode": ("Shellcode", "Exploitation and intrusion"),
    "Infiltration": ("Infiltration", "Exploitation and intrusion"),
    "Infilteration": ("Infiltration", "Exploitation and intrusion"),  # spelling seen in some UQ files
    "MITM": ("MITM", "Interception and spoofing"),
    "Fuzzers": ("Fuzzers", "Fuzzing and crypto"),
    "Generic": ("Generic", "Fuzzing and crypto"),
    "Theft": ("Theft", "Data theft"),

    # --- CICIoT2023 labels (verify exact spellings on load; add any missing ones here) ---
    "BenignTraffic": (BENIGN, BENIGN),
    "DDoS-ACK_Fragmentation": ("DDoS ACK fragmentation", "Denial of service"),
    "DDoS-UDP_Flood": ("DDoS UDP flood", "Denial of service"),
    "DDoS-SlowLoris": ("DDoS SlowLoris", "Denial of service"),
    "DDoS-ICMP_Flood": ("DDoS ICMP flood", "Denial of service"),
    "DDoS-RSTFINFlood": ("DDoS RST-FIN flood", "Denial of service"),
    "DDoS-PSHACK_Flood": ("DDoS PSH-ACK flood", "Denial of service"),
    "DDoS-HTTP_Flood": ("DDoS HTTP flood", "Denial of service"),
    "DDoS-UDP_Fragmentation": ("DDoS UDP fragmentation", "Denial of service"),
    "DDoS-ICMP_Fragmentation": ("DDoS ICMP fragmentation", "Denial of service"),
    "DDoS-TCP_Flood": ("DDoS TCP flood", "Denial of service"),
    "DDoS-SYN_Flood": ("DDoS SYN flood", "Denial of service"),
    "DDoS-SynonymousIP_Flood": ("DDoS Synonymous-IP flood", "Denial of service"),
    "DoS-TCP_Flood": ("DoS TCP flood", "Denial of service"),
    "DoS-HTTP_Flood": ("DoS HTTP flood", "Denial of service"),
    "DoS-SYN_Flood": ("DoS SYN flood", "Denial of service"),
    "DoS-UDP_Flood": ("DoS UDP flood", "Denial of service"),
    "Recon-PingSweep": ("Ping sweep", "Reconnaissance"),
    "Recon-OSScan": ("OS scan", "Reconnaissance"),
    "VulnerabilityScan": ("Vulnerability scan", "Reconnaissance"),
    "Recon-PortScan": ("Port scan", "Reconnaissance"),
    "Recon-HostDiscovery": ("Host discovery", "Reconnaissance"),
    "DictionaryBruteForce": ("Dictionary brute force", "Credential attacks"),
    "SqlInjection": ("SQL injection", "Web and injection"),
    "CommandInjection": ("Command injection", "Web and injection"),
    "Uploading_Attack": ("Uploading attack", "Web and injection"),
    "BrowserHijacking": ("Browser hijacking", "Web and injection"),
    "Backdoor_Malware": ("Backdoor malware", "Web and injection"),
    "Mirai-greip_flood": ("Mirai GRE-IP flood", "Malware and botnets"),
    "Mirai-greeth_flood": ("Mirai GRE-Eth flood", "Malware and botnets"),
    "Mirai-udpplain": ("Mirai UDP-Plain", "Malware and botnets"),
    "MITM-ArpSpoofing": ("ARP spoofing", "Interception and spoofing"),
    "DNS_Spoofing": ("DNS spoofing", "Interception and spoofing"),
}


def _norm(label: str) -> str:
    return "".join(ch for ch in str(label).strip().lower() if ch not in " -_")


_TAXONOMY_NORM = {_norm(k): v for k, v in TAXONOMY.items()}

# CICIoT2023 also has a plain "XSS" label; the normalised key above already covers it.

# ---------------------------------------------------------------------------
# 4. Cleaning and sampling rules (identical for every dataset)
# ---------------------------------------------------------------------------
RANDOM_STATE = 42
SAMPLE_CAP_PER_LABEL = 200_000   # keep every flow of a label below this, sample this many above it

# Identifier columns dropped from the cleaned files (they identify machines, not behaviour).
# Names are matched case-insensitively; missing ones are ignored.
ID_COLUMNS = ["IPV4_SRC_ADDR", "IPV4_DST_ADDR", "Src IP", "Dst IP", "Flow ID"]

# Label columns in the raw files
NETFLOW_LABEL_COL = "Attack"     # multi-class label in NetFlow v3 ("Label" is the 0/1 column)
CICIOT_LABEL_COL = "label"

# ---------------------------------------------------------------------------
# 5. Shared functions — everyone calls these, nobody re-implements them
# ---------------------------------------------------------------------------

def map_labels(df: pd.DataFrame, label_col: str, source: str) -> pd.DataFrame:
    """Add source_dataset, attack_label, attack_family and is_attack columns.

    Raises an error listing any label that is not in TAXONOMY, so a new label
    is never silently put in the wrong family.
    """
    raw = df[label_col].astype(str)
    mapped = raw.map(lambda x: _TAXONOMY_NORM.get(_norm(x)))
    unknown = sorted(raw[mapped.isna()].unique())
    if unknown:
        raise ValueError(f"[{source}] labels not in TAXONOMY, add them to config.py first: {unknown}")

    df = df.copy()
    df["source_dataset"] = source
    df["attack_label"] = mapped.str[0]
    df["attack_family"] = mapped.str[1]
    df["is_attack"] = (df["attack_family"] != BENIGN).astype("int8")
    return df


def downcast(df: pd.DataFrame) -> pd.DataFrame:
    """float64 -> float32 and int64 -> smallest int type, to halve memory."""
    for col in df.select_dtypes(include="float64").columns:
        df[col] = df[col].astype("float32")
    for col in df.select_dtypes(include="int64").columns:
        df[col] = pd.to_numeric(df[col], downcast="integer")
    return df


def clean(df: pd.DataFrame, source: str) -> tuple[pd.DataFrame, dict]:
    """Apply the shared cleaning rules and return (clean_df, stats).

    Order: drop ID columns -> inf to NaN -> drop NaN rows -> drop exact duplicates.
    No scaling or transformation here: that is feature engineering, done once on merged data.
    """
    stats = {"source_dataset": source, "rows_raw": len(df), "cols_raw": df.shape[1]}

    drop = [c for c in df.columns if c.lower() in {x.lower() for x in ID_COLUMNS}]
    df = df.drop(columns=drop)
    stats["id_columns_dropped"] = ", ".join(drop) if drop else "none"

    num = df.select_dtypes(include=[np.number]).columns
    n_inf = int(np.isinf(df[num].to_numpy(dtype="float64", na_value=np.nan)).sum())
    df[num] = df[num].replace([np.inf, -np.inf], np.nan)
    stats["inf_values"] = n_inf

    stats["nan_values"] = int(df.isna().sum().sum())
    stats["rows_with_nan"] = int(df.isna().any(axis=1).sum())
    df = df.dropna()

    stats["duplicate_rows"] = int(df.duplicated().sum())
    df = df.drop_duplicates()

    stats["rows_clean"] = len(df)
    stats["cols_clean"] = df.shape[1]
    return downcast(df), stats


def sample_per_label(df: pd.DataFrame, cap: int = SAMPLE_CAP_PER_LABEL) -> pd.DataFrame:
    """Keep every flow of labels with <= cap flows; sample `cap` flows from larger labels."""
    parts = [
        g if len(g) <= cap else g.sample(n=cap, random_state=RANDOM_STATE)
        for _, g in df.groupby("attack_label", observed=True)
    ]
    return pd.concat(parts, ignore_index=True)


def quality_report(stats: dict, before: pd.DataFrame, after: pd.DataFrame, source: str) -> pd.DataFrame:
    """Save tables/{source}_quality.csv (summary) and tables/{source}_labels.csv (per label)."""
    pd.DataFrame([stats]).to_csv(TABLE_DIR / f"{source}_quality.csv", index=False)

    labels = pd.DataFrame({
        "flows_after_cleaning": before["attack_label"].value_counts(),
        "flows_after_sampling": after["attack_label"].value_counts(),
    }).fillna(0).astype(int)
    labels["attack_family"] = labels.index.map(
        lambda l: before.loc[before["attack_label"] == l, "attack_family"].iloc[0]
    )
    labels.insert(0, "source_dataset", source)
    labels.index.name = "attack_label"
    labels.to_csv(TABLE_DIR / f"{source}_labels.csv")
    return labels


def save_clean(df: pd.DataFrame, source: str) -> Path:
    path = PROCESSED_DIR / f"{source}_clean.parquet"
    df.to_parquet(path, index=False)
    return path
