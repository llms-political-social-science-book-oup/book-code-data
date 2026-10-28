"""
05_dsl_correction.py — DSL leg: correction vs. selection (Section 5.7, goal 2).

Implements the design-based supervised learning (DSL) bias correction of
Egami et al. for OLS with a surrogate outcome. With a simple random gold
subsample (probability pi), the pseudo-outcome

    y_tilde_i = yhat_i + (R_i / pi) * (y_i - yhat_i)

has expectation y_i regardless of surrogate quality, so OLS of y_tilde on X
is valid for the same estimand as gold OLS. Precision depends on the
surrogate: the (y - yhat) residuals, inflated by 1/pi, enter the variance.
Our surrogates are fixed external predictions (decoder labels never saw the
gold labels; encoder predictions are out-of-fold), so no cross-fitting is
needed.

For each config x gold-fraction {5%, 10%, 20%} x 50 seeded draws:
  - DSL estimate of beta_republican + robust SE + 95% CI
  - comparison baseline: OLS on the gold subsample alone ("gold-only")
Outputs: ballard_dsl_results.csv (draw level), ballard_dsl_summary.csv
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm
import os 


IN  = "ballard_analysis_sample.csv"
s   = pd.read_csv(IN)
X   = sm.add_constant(s[["republican", "senate", "female"]])
y   = s["label_main"].to_numpy(float)
n   = len(s)

CONFIGS = ["enc_roberta", "gemma_zs", "gemma_fs", "llama_zs", "llama_fs",
           "mistral_zs", "mistral_fs", "gpt5_zs", "gpt5_fs",
           "gptmini_zs", "gptmini_fs"]
FRACTIONS = [0.05, 0.10, 0.20]
N_DRAWS   = 50

# benchmark: full-gold OLS
gold_fit  = sm.OLS(y, X).fit(cov_type="HC1")
BETA_GOLD = gold_fit.params["republican"]

rows = []
rng_master = np.random.default_rng(20260708)
seeds = rng_master.integers(0, 2**31, size=N_DRAWS)

for pi in FRACTIONS:
    for d, seed in enumerate(seeds):
        rng = np.random.default_rng(seed)
        m = max(int(round(pi * n)), X.shape[1] + 2)
        idx = rng.choice(n, size=m, replace=False)
        R = np.zeros(n); R[idx] = 1.0

        # gold-only baseline on the subsample
        gsub = sm.OLS(y[idx], X.iloc[idx]).fit(cov_type="HC1")
        rows.append({"config": "GOLD-ONLY subsample", "pi": pi, "draw": d,
                     "beta": gsub.params["republican"],
                     "se": gsub.bse["republican"],
                     "ci_lo": gsub.conf_int().loc["republican", 0],
                     "ci_hi": gsub.conf_int().loc["republican", 1]})

        for cfg in CONFIGS:
            yhat = s[cfg].to_numpy(float)
            y_tilde = yhat + (R / pi) * (y - yhat)
            fit = sm.OLS(y_tilde, X).fit(cov_type="HC1")
            rows.append({"config": cfg, "pi": pi, "draw": d,
                         "beta": fit.params["republican"],
                         "se": fit.bse["republican"],
                         "ci_lo": fit.conf_int().loc["republican", 0],
                         "ci_hi": fit.conf_int().loc["republican", 1]})

res = pd.DataFrame(rows)
res["covers_gold"] = (res.ci_lo <= BETA_GOLD) & (BETA_GOLD <= res.ci_hi)
res["ci_width"]    = res.ci_hi - res.ci_lo
res.to_csv("ballard_dsl_results.csv", index=False)

summ = (res.groupby(["config", "pi"])
          .agg(mean_beta=("beta", "mean"), sd_beta=("beta", "std"),
               mean_ci_width=("ci_width", "mean"),
               coverage=("covers_gold", "mean"))
          .reset_index())
summ["bias_vs_gold"] = summ["mean_beta"] - BETA_GOLD
summ.to_csv("ballard_dsl_summary.csv", index=False)

print(f"benchmark beta_gold = {BETA_GOLD:.4f}\n")
for pi in FRACTIONS:
    sub = summ[summ.pi == pi].copy()
    order = ["GOLD-ONLY subsample", "enc_roberta"] + [c for c in CONFIGS if c != "enc_roberta"]
    sub["o"] = sub.config.map({c: i for i, c in enumerate(order)})
    sub = sub.sort_values("o")
    print(f"=== gold fraction {int(pi*100)}%  (n_gold = {int(round(pi*n))}) ===")
    with pd.option_context("display.float_format", lambda v: f"{v: .4f}"):
        print(sub[["config", "mean_beta", "bias_vs_gold", "sd_beta",
                   "mean_ci_width", "coverage"]].to_string(index=False))
    print()
