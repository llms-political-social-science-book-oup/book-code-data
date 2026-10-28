"""
02_multiverse_sweep_foy.py — Twelve-config OLS sweep for Foy (negative-vs-rest).

PROVISIONAL spec (pending covariate inventory):
    negative ~ republican + incumbent + female     (LPM, HC1)
Coefficient of interest: incumbent if available (negative-campaigning literature:
challengers go negative), else republican. Edit COEF_OF_INTEREST when real
covariates arrive.
"""
import pandas as pd, numpy as np, statsmodels.api as sm

COEF_OF_INTEREST = "year_c"
RHS = ["year_c", "foreign"]

CONFIGS = ["label_main","enc_roberta","gemma_zs","gemma_fs","llama_zs","llama_fs",
           "mistral_zs","mistral_fs","gpt5_zs","gpt5_fs","gptmini_zs","gptmini_fs"]
NAMES = {"label_main":"GOLD (human labels)","enc_roberta":"RoBERTa (FT)",
         "gemma_zs":"Gemma ZS","gemma_fs":"Gemma FS","llama_zs":"Llama ZS",
         "llama_fs":"Llama FS","mistral_zs":"Mistral ZS","mistral_fs":"Mistral FS",
         "gpt5_zs":"GPT-5.5 ZS","gpt5_fs":"GPT-5.5 FS",
         "gptmini_zs":"GPT-5.5-mini ZS","gptmini_fs":"GPT-5.5-mini FS"}

s = pd.read_csv("trubowitz_analysis_sample.csv")
X = sm.add_constant(s[RHS])
rows = []
for cfg in CONFIGS:
    valid = s[cfg + "_bin"].notna()
    m = sm.OLS(s.loc[valid, cfg + "_bin"], X.loc[valid]).fit(cov_type="HC1")
    ci = m.conf_int().loc[COEF_OF_INTEREST]
    rows.append({"config": NAMES[cfg], "col": cfg,
                 "beta": m.params[COEF_OF_INTEREST], "se": m.bse[COEF_OF_INTEREST],
                 "p": m.pvalues[COEF_OF_INTEREST], "ci_lo": ci[0], "ci_hi": ci[1],
                 "mean_dv": s[cfg + "_bin"].mean(), "n": int(m.nobs)})
res = pd.DataFrame(rows)
gold = res.loc[res.col=="label_main","beta"].iloc[0]
res["distortion"] = res["beta"] - gold
res["sign_flip"]  = np.sign(res["beta"]) != np.sign(gold)
res["sig_05"]     = res["p"] < .05
res.to_csv("trubowitz_sweep_results.csv", index=False)
with pd.option_context("display.float_format", lambda v: f"{v: .4f}"):
    print(res[["config","beta","se","p","mean_dv","distortion","sign_flip","sig_05"]].to_string(index=False))
print(f"\ngold beta_{COEF_OF_INTEREST} = {gold:.4f}")
