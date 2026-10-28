"""
05_dsl_foy.py — DSL correction leg for Foy (negative-vs-rest).
Identical estimator to Ballard's 05: pseudo-outcome y~ = yhat + (R/pi)(y - yhat),
gold fractions {5%,10%,20%}, 50 seeded draws, gold-only baseline.
THE TEST: with error rates ~.07-.15 and outcome variance ~.24, DSL should now
BEAT the gold-only subsample — the reverse of Ballard.
"""
import pandas as pd, numpy as np, statsmodels.api as sm

COEF = "year_c"
RHS  = ["year_c","foreign"]
FRACTIONS = [0.05,0.10,0.20]; N_DRAWS=50; MASTER=20260708

s = pd.read_csv("trubowitz_analysis_sample.csv")
X = sm.add_constant(s[RHS]); y = s["label_main_bin"].to_numpy(float); n=len(s)
CONFIGS = ["enc_roberta","gemma_zs","gemma_fs","llama_zs","llama_fs","mistral_zs",
           "mistral_fs","gpt5_zs","gpt5_fs","gptmini_zs","gptmini_fs"]
gold = sm.OLS(y,X).fit(cov_type="HC1").params[COEF]
seeds = np.random.default_rng(MASTER).integers(0,2**31,N_DRAWS)
rows=[]
for pi in FRACTIONS:
    for d,seed in enumerate(seeds):
        rng=np.random.default_rng(seed)
        m=max(int(round(pi*n)), X.shape[1]+2)
        idx=rng.choice(n,size=m,replace=False)
        R=np.zeros(n); R[idx]=1.0
        g=sm.OLS(y[idx],X.iloc[idx]).fit(cov_type="HC1")
        ci=g.conf_int().loc[COEF]
        rows.append({"config":"GOLD-ONLY subsample","pi":pi,"draw":d,"beta":g.params[COEF],
                     "ci_lo":ci[0],"ci_hi":ci[1]})
        for cfg in CONFIGS:
            yh=s[cfg+"_bin"].to_numpy(float)
            ok=~np.isnan(yh)
            yt=yh[ok]+(R[ok]/pi)*(y[ok]-yh[ok])
            f=sm.OLS(yt,X.loc[ok]).fit(cov_type="HC1"); ci=f.conf_int().loc[COEF]
            rows.append({"config":cfg,"pi":pi,"draw":d,"beta":f.params[COEF],
                         "ci_lo":ci[0],"ci_hi":ci[1]})
res=pd.DataFrame(rows)
res["covers_gold"]=(res.ci_lo<=gold)&(gold<=res.ci_hi)
res["ci_width"]=res.ci_hi-res.ci_lo
res.to_csv("trubowitz_dsl_results.csv",index=False)
summ=(res.groupby(["config","pi"]).agg(mean_beta=("beta","mean"),
      mean_ci_width=("ci_width","mean"),coverage=("covers_gold","mean")).reset_index())
summ["bias"]=summ.mean_beta-gold
summ.to_csv("trubowitz_dsl_summary.csv",index=False)
print(f"gold beta = {gold:.4f}")
sub=summ[summ.pi==0.10].sort_values("mean_ci_width")
with pd.option_context("display.float_format", lambda v:f"{v: .4f}"):
    print(sub[["config","mean_beta","bias","mean_ci_width","coverage"]].to_string(index=False))
