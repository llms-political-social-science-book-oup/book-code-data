"""
03_error_structure.py — Error-structure decomposition by party (Section 5.6).

Per config: false-positive rate (civil tweets flagged uncivil) and
false-negative rate (uncivil tweets missed), separately by party, plus gaps.
Also: pairwise error-overlap (Jaccard) between configs, and disagreement-flag
diagnostics (are rows where a config's 3 runs disagreed more error-prone?).

Input : ballard_analysis_sample.csv
Outputs: ballard_error_structure.csv, ballard_error_overlap.csv,
         ballard_disagreement_diag.csv
"""
import pandas as pd
import numpy as np
from itertools import combinations
import os 


IN = "../../dsl_ensemble/ballard_incivility/ballard_analysis_sample.csv"
s  = pd.read_csv(IN)

CONFIGS = ["enc_roberta", "gemma_zs", "gemma_fs", "llama_zs", "llama_fs",
           "mistral_zs", "mistral_fs", "gpt5_zs", "gpt5_fs",
           "gptmini_zs", "gptmini_fs"]

# ---- 1. FPR/FNR by party ----
rows = []
for cfg in CONFIGS:
    r = {"config": cfg}
    for p in ["D", "R"]:
        sub   = s[s["party"] == p]
        civil = sub[sub["label_main"] == 0]
        unciv = sub[sub["label_main"] == 1]
        r[f"FPR_{p}"] = (civil[cfg] == 1).mean()
        r[f"FNR_{p}"] = (unciv[cfg] == 0).mean()
    r["FPR_gap_RminusD"] = r["FPR_R"] - r["FPR_D"]
    r["FNR_gap_RminusD"] = r["FNR_R"] - r["FNR_D"]
    rows.append(r)
es = pd.DataFrame(rows)
es.to_csv("ballard_error_structure.csv", index=False)
print("=== FPR/FNR by party ===")
with pd.option_context("display.float_format", lambda v: f"{v: .3f}"):
    print(es.to_string(index=False))

# ---- 2. pairwise error overlap (Jaccard over error sets) ----
err = {cfg: set(s.index[s[cfg] != s["label_main"]]) for cfg in CONFIGS}
rows = []
for a, b in combinations(CONFIGS, 2):
    inter = len(err[a] & err[b]); union = len(err[a] | err[b])
    rows.append({"config_a": a, "config_b": b,
                 "jaccard": inter / union if union else np.nan,
                 "n_err_a": len(err[a]), "n_err_b": len(err[b]),
                 "n_shared": inter})
ov = pd.DataFrame(rows).sort_values("jaccard", ascending=False)
ov.to_csv("ballard_error_overlap.csv", index=False)
print("\n=== error overlap: top and bottom 5 pairs (Jaccard) ===")
print(ov.head(5).to_string(index=False))
print(ov.tail(5).to_string(index=False))

# ---- 3. disagreement flags as risk signal ----
rows = []
for cfg in [c for c in CONFIGS if c != "enc_roberta"]:
    flag = f"{cfg}_disagree"
    if flag not in s.columns:
        continue
    agree_err    = (s.loc[s[flag] == 0, cfg] != s.loc[s[flag] == 0, "label_main"]).mean()
    disagree_err = (s.loc[s[flag] == 1, cfg] != s.loc[s[flag] == 1, "label_main"]).mean()
    rows.append({"config": cfg, "n_disagree": int(s[flag].sum()),
                 "err_rate_agree": agree_err, "err_rate_disagree": disagree_err,
                 "risk_ratio": disagree_err / agree_err if agree_err else np.nan})
dd = pd.DataFrame(rows)
dd.to_csv("ballard_disagreement_diag.csv", index=False)
print("\n=== run-disagreement as error signal ===")
with pd.option_context("display.float_format", lambda v: f"{v: .3f}"):
    print(dd.to_string(index=False))
