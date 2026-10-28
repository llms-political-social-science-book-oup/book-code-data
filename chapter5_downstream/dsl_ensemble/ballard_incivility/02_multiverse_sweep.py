"""
02_multiverse_sweep.py — The twelve-config OLS sweep (measurement-choice sensitivity).

Spec: uncivil ~ republican + senate + female   (LPM, HC1 robust SEs)
Twelve label sources: gold, RoBERTa OOF, 10 decoder configs.
beta of interest: republican.

Input : ballard_analysis_sample.csv   (from 01_build_sample.py)
Output: ballard_sweep_results.csv     (beta, SE, p, distortion, flags per config)
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm
import os 


IN  = "ballard_analysis_sample.csv"
OUT = "ballard_sweep_results.csv"

CONFIGS = ["label_main", "enc_roberta",
           "gemma_zs", "gemma_fs", "llama_zs", "llama_fs",
           "mistral_zs", "mistral_fs", "gpt5_zs", "gpt5_fs",
           "gptmini_zs", "gptmini_fs"]
NAMES = {"label_main": "GOLD (human labels)", "enc_roberta": "RoBERTa (FT)",
         "gemma_zs": "Gemma ZS", "gemma_fs": "Gemma FS",
         "llama_zs": "Llama ZS", "llama_fs": "Llama FS",
         "mistral_zs": "Mistral ZS", "mistral_fs": "Mistral FS",
         "gpt5_zs": "GPT-5.5 ZS", "gpt5_fs": "GPT-5.5 FS",
         "gptmini_zs": "GPT-5.5-mini ZS", "gptmini_fs": "GPT-5.5-mini FS"}

s = pd.read_csv(IN)
X = sm.add_constant(s[["republican", "senate", "female"]])

rows = []
for cfg in CONFIGS:
    m = sm.OLS(s[cfg], X).fit(cov_type="HC1")
    rows.append({"config": NAMES[cfg], "col": cfg,
                 "beta_rep": m.params["republican"],
                 "se": m.bse["republican"],
                 "p": m.pvalues["republican"],
                 "ci_lo": m.conf_int().loc["republican", 0],
                 "ci_hi": m.conf_int().loc["republican", 1],
                 "mean_dv": s[cfg].mean(),
                 "n": int(m.nobs)})

res = pd.DataFrame(rows)
gold = res.loc[res["col"] == "label_main", "beta_rep"].iloc[0]
res["distortion"] = res["beta_rep"] - gold
res["sign_flip"]  = np.sign(res["beta_rep"]) != np.sign(gold)
res["sig_05"]     = res["p"] < 0.05

res.to_csv(OUT, index=False)
with pd.option_context("display.float_format", lambda v: f"{v: .4f}"):
    print(res[["config", "beta_rep", "se", "p", "mean_dv", "distortion",
               "sign_flip", "sig_05"]].to_string(index=False))
print(f"\ngold beta_republican = {gold:.4f}")
print(f"wrote {OUT}")
