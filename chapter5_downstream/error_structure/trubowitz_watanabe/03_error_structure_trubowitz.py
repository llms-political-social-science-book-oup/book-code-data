"""
03_error_structure_foy.py — Error structure for Foy (binarized negative-vs-rest).
FPR/FNR by the coefficient-of-interest group, pairwise error overlap (on the
3-class predictions, not the binarization), disagreement diagnostics.
"""
import pandas as pd, numpy as np
from itertools import combinations

GROUP = "decade"   # era-correlated error is the hypothesis here   # edit with COEF_OF_INTEREST
s = pd.read_csv("../../dsl_ensemble/trubowitz_watanabe/trubowitz_analysis_sample.csv")
DEC = ["enc_roberta","gemma_zs","gemma_fs","llama_zs","llama_fs","mistral_zs",
       "mistral_fs","gpt5_zs","gpt5_fs","gptmini_zs","gptmini_fs"]

rows=[]
for cfg in DEC:
    r={"config":cfg}
    for g in sorted(s[GROUP].unique()):
        sub=s[s[GROUP]==g]
        rest=sub[sub["label_main_bin"]==0]; neg=sub[sub["label_main_bin"]==1]
        r[f"FPR_{g}"]=(rest[cfg+"_bin"]==1).mean()
        r[f"FNR_{g}"]=(neg[cfg+"_bin"]==0).mean()
    gs=sorted(s[GROUP].unique())
    r["FPR_gap"]=r[f"FPR_{gs[-1]}"]-r[f"FPR_{gs[0]}"]
    r["FNR_gap"]=r[f"FNR_{gs[-1]}"]-r[f"FNR_{gs[0]}"]
    rows.append(r)
es=pd.DataFrame(rows); es.to_csv("trubowitz_error_structure.csv",index=False)
with pd.option_context("display.float_format", lambda v: f"{v: .3f}"):
    print(es.to_string(index=False))

err={c:set(s.index[s[c]!=s["label_main"]]) for c in DEC}   # 3-class errors
rows=[{"a":a,"b":b,"jaccard":len(err[a]&err[b])/max(len(err[a]|err[b]),1)}
      for a,b in combinations(DEC,2)]
ov=pd.DataFrame(rows).sort_values("jaccard",ascending=False)
ov.to_csv("trubowitz_error_overlap.csv",index=False)
print("\noverlap top/bottom:")
print(ov.head(3).to_string(index=False)); print(ov.tail(3).to_string(index=False))

rows=[]
for cfg in [c for c in DEC if c!="enc_roberta"]:
    f=f"{cfg}_disagree"
    if f not in s.columns: continue
    a=(s.loc[s[f]==0,cfg]!=s.loc[s[f]==0,"label_main"]).mean()
    d=(s.loc[s[f]==1,cfg]!=s.loc[s[f]==1,"label_main"]).mean()
    rows.append({"config":cfg,"n_disagree":int(s[f].sum()),
                 "err_agree":a,"err_disagree":d,"risk_ratio":d/a if a else np.nan})
pd.DataFrame(rows).to_csv("trubowitz_disagreement_diag.csv",index=False)
print("\ndisagreement diag written")
