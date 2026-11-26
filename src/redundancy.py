"""
Redundancy checks shared by the feature-engineering notebooks (08_features_netflow, 08_features_iot23)
and the correlation sections of the EDA notebooks (07_eda_netflow, 07_eda_iot23).

Rule (decision log, "Redundancy rule"):
  1. Correlated pairs: a pair is redundant when a one-sided bootstrap test rejects
     H0: |rho| <= RHO_LIMIT (Spearman, alpha = 0.05). The feature with the lower mutual information is removed.
  2. Exact linear dependences (a column equal to a combination of others, e.g. one-hot columns that sum to 1):
     the column with the lowest mutual information in the dependence is removed.
  3. Multicollinearity: while the largest variance inflation factor (VIF) is above VIF_LIMIT,
     the feature with the largest VIF is removed.

Usage in a notebook:
    import sys; sys.path.append("..")
    from src.redundancy import *
"""

import numpy as np
import pandas as pd
from scipy import stats

RHO_LIMIT = 0.90      # same threshold as the EDA notebooks
VIF_LIMIT = 10.0      # usual rule of thumb: VIF > 10 = serious multicollinearity
ALPHA = 0.05
N_BOOT = 500


def strong_pairs(X: pd.DataFrame, min_abs: float) -> pd.DataFrame:
    """Every pair of columns with |Spearman rho| >= min_abs, strongest first."""
    rho = X.corr(method="spearman")
    up = rho.where(np.triu(np.ones(rho.shape, dtype=bool), k=1)).stack()
    up = up[up.abs() >= min_abs]
    out = up.rename("rho").reset_index()
    out.columns = ["feature A", "feature B", "rho"]
    return out.reindex(out["rho"].abs().sort_values(ascending=False).index).reset_index(drop=True)


def rho_test(x, y, limit: float = RHO_LIMIT, n_boot: int = N_BOOT, seed: int = 42) -> dict:
    """Spearman rho with two tests.

    * H0: rho = 0 (no monotonic relation) -> scipy's p-value.
    * H0: |rho| <= limit (not redundant) vs H1: |rho| > limit (redundant) -> one-sided bootstrap test:
      the rows are resampled n_boot times, p = share of resamples where |rho| <= limit.
    The bootstrap makes no normality assumption (the features are not normal, phase 4).
    """
    x = np.asarray(x, dtype="float64"); y = np.asarray(y, dtype="float64")
    r = stats.spearmanr(x, y)
    rng = np.random.default_rng(seed)
    n = len(x)
    boot = np.empty(n_boot)
    for b in range(n_boot):
        i = rng.integers(0, n, n)
        boot[b] = stats.spearmanr(x[i], y[i]).statistic
    a = np.abs(boot)
    lo, hi = np.percentile(boot, [2.5, 97.5])
    p_red = (1 + (a <= limit).sum()) / (n_boot + 1)
    return {"rho": r.statistic, "p (H0: rho = 0)": r.pvalue, "95% CI low": lo, "95% CI high": hi,
            f"p (H0: |rho| <= {limit})": p_red, "redundant": p_red < ALPHA}


def test_pairs(X: pd.DataFrame, pairs: pd.DataFrame, limit: float = RHO_LIMIT, n_boot: int = N_BOOT) -> pd.DataFrame:
    """rho_test for every pair of a strong_pairs() table."""
    rows = [{"feature A": a, "feature B": b, **rho_test(X[a], X[b], limit, n_boot)}
            for a, b in zip(pairs["feature A"], pairs["feature B"])]
    return pd.DataFrame(rows, columns=["feature A", "feature B", "rho", "p (H0: rho = 0)", "95% CI low", "95% CI high",
                                       f"p (H0: |rho| <= {limit})", "redundant"])


def drop_redundant_pairs(tested: pd.DataFrame, mi: pd.Series, limit: float = RHO_LIMIT) -> dict:
    """Rule 1: walk the redundant pairs from the strongest; drop the feature with the lower mutual information."""
    drop = {}
    red = tested[tested["redundant"].astype(bool)]
    for _, p in red.reindex(red["rho"].abs().sort_values(ascending=False).index).iterrows():
        a, b = p["feature A"], p["feature B"]
        if a in drop or b in drop:
            continue
        lose, keep = (a, b) if mi[a] < mi[b] else (b, a)
        drop[lose] = (f"rho = {p['rho']:.3f} with {keep} (95% CI {p['95% CI low']:.3f} to {p['95% CI high']:.3f}, "
                      f"H0: |rho| <= {limit} rejected); lower MI ({mi[lose]:.3f} vs {mi[keep]:.3f})")
    return drop


def _standardise(X: pd.DataFrame) -> np.ndarray:
    A = X.to_numpy(dtype="float64")
    sd = A.std(axis=0)
    sd[sd == 0] = 1.0
    return (A - A.mean(axis=0)) / sd


def exact_dependences(X: pd.DataFrame, mi: pd.Series, tol: float = 1e-6) -> dict:
    """Rule 2: find columns that are an exact linear combination of others (with the intercept).

    The columns are centred, so a constant sum (e.g. one-hot columns that always add up to 1) also shows up.
    The smallest singular vector of the centred matrix names the columns of one dependence; the one with the lowest
    mutual information is removed, and the search is repeated until the matrix has full rank.
    """
    cols = list(X.columns)
    drop = {}
    while len(cols) > 1:
        Z = _standardise(X[cols])
        _, s, vt = np.linalg.svd(Z, full_matrices=False)
        if s[-1] > tol * s[0] * np.sqrt(len(Z)):
            break
        v = vt[-1]
        involved = [cols[i] for i in np.flatnonzero(np.abs(v) > 0.05)]
        lose = min(involved, key=lambda c: mi[c])
        drop[lose] = f"exact linear dependence with {', '.join(c for c in involved if c != lose)}; lowest MI in it ({mi[lose]:.3f})"
        cols.remove(lose)
    return drop


def vif(X: pd.DataFrame) -> pd.Series:
    """Variance inflation factor of every column: VIF_j = 1 / (1 - R_j^2), R_j^2 from regressing column j on the others.

    Computed as the diagonal of the inverse correlation matrix (same result as one regression per column).
    VIF = 1: independent of the others; > 10: serious multicollinearity; inf: exact linear dependence.
    """
    R = np.corrcoef(_standardise(X), rowvar=False)
    try:
        v = np.diag(np.linalg.inv(R))
    except np.linalg.LinAlgError:
        v = np.full(len(X.columns), np.inf)
    v = np.where(v < 0, np.inf, v)          # numerical sign of a singular matrix
    return pd.Series(v, index=X.columns).sort_values(ascending=False)


def vif_prune(X: pd.DataFrame, limit: float = VIF_LIMIT) -> tuple[dict, pd.DataFrame]:
    """Rule 3: while the largest VIF is above the limit, remove that feature and recompute.

    Returns the removed features (with their VIF at removal) and a table of VIF before and after for every feature.
    """
    cols = list(X.columns)
    before = vif(X)
    drop = {}
    while True:
        v = vif(X[cols])
        if v.iloc[0] <= limit:
            break
        worst = v.index[0]
        drop[worst] = f"VIF = {v.iloc[0]:,.1f} (> {limit:g}): explained by the other features (R² = {1 - 1 / v.iloc[0]:.3f})"
        cols.remove(worst)
    after = vif(X[cols])
    table = pd.DataFrame({"VIF before": before, "VIF after": after}).sort_values("VIF before", ascending=False)
    return drop, table


def check_line(name: str, ok: bool, value) -> dict:
    """One line of the pre-modelling checklist."""
    return {"check": name, "result": "PASS" if ok else "FAIL", "value": value}


def note_line(name: str, value) -> dict:
    """A checklist line that is not pass/fail but must be handled when the model is built."""
    return {"check": name, "result": "TO HANDLE IN MODELLING", "value": value}
