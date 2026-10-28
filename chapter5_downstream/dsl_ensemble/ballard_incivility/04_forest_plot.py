"""
04_forest_plot.py — The measurement-choice sensitivity figure (Section 5.7).

Forest plot of beta_republican across the twelve label sources, 95% CIs,
gold estimate as reference line. Configs ordered: gold, encoder, then
decoders by uncivil-class F1 (computed from the sample).

Input : ballard_analysis_sample.csv, ballard_sweep_results.csv
Output: ballard_forest.pdf / ballard_forest.png
"""
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score
import os 


s   = pd.read_csv("ballard_analysis_sample.csv")
res = pd.read_csv("ballard_sweep_results.csv")

# uncivil-class F1 per config (for ordering)
f1u = {row["col"]: (np.nan if row["col"] == "label_main" else
       f1_score(s["label_main"], s[row["col"]], average=None)[1])
       for _, row in res.iterrows()}
res["f1_uncivil"] = res["col"].map(f1u)

gold = res[res["col"] == "label_main"].iloc[0]
rest = res[res["col"] != "label_main"].sort_values("f1_uncivil", ascending=False)
plot_df = pd.concat([gold.to_frame().T, rest]).reset_index(drop=True)
plot_df[["beta_rep","ci_lo","ci_hi","f1_uncivil"]] = plot_df[
    ["beta_rep","ci_lo","ci_hi","f1_uncivil"]].astype(float)

fig, ax = plt.subplots(figsize=(7.5, 5.5))
y = np.arange(len(plot_df))[::-1]

ax.axvline(gold["beta_rep"], color="0.4", lw=1.2, ls="--", zorder=1)
ax.axvline(0, color="0.8", lw=0.8, zorder=0)

for yi, (_, r) in zip(y, plot_df.iterrows()):
    is_gold = r["col"] == "label_main"
    is_enc  = r["col"] == "enc_roberta"
    color   = "black" if is_gold else ("#1a5fb4" if is_enc else "#c01c28")
    marker  = "D" if is_gold else ("s" if is_enc else "o")
    ax.plot([r["ci_lo"], r["ci_hi"]], [yi, yi], color=color, lw=1.6, zorder=2)
    ax.plot(r["beta_rep"], yi, marker=marker, color=color, ms=6, zorder=3)

labels = []
for _, r in plot_df.iterrows():
    lab = r["config"]
    if not pd.isna(r["f1_uncivil"]):
        lab += f"  (F1$_u$ {r['f1_uncivil']:.2f})"
    labels.append(lab)
ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=9)
ax.set_xlabel(r"$\hat{\beta}_{Republican}$  (LPM, 95% CI, HC1 SEs)")
ax.set_title("Measurement-choice sensitivity: one specification, twelve measures",
             fontsize=11)
fig.tight_layout()
fig.savefig("ballard_forest.pdf"); fig.savefig("ballard_forest.png", dpi=200)
print("wrote ballard_forest.pdf / .png")
