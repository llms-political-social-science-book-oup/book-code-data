"""
06_forest_dsl_all.py — Naive vs. DSL-corrected forest plots (Section 5.7).

Generates the full set of figures in one run, one per gold fraction:
    trubowitz_forest_dsl_5.(pdf|png)     5% gold   (n =   144)
    trubowitz_forest_dsl_10.(pdf|png)   10% gold   (n =   289)
    trubowitz_forest_dsl_eq.(pdf|png) 18.8% gold   (n =   542)  <- fraction at which the
                                     average decoder's DSL CI width matches RoBERTa's at 10%
    trubowitz_forest_dsl_20.(pdf|png)   20% gold   (n =   577)
    trubowitz_forest_dsl_50.(pdf|png)   50% gold   (n = 1,444)
    trubowitz_forest_dsl_100.(pdf|png) 100% gold   (degenerate: DSL reduces to the gold
                                     regression, all configs identical by construction)

Each figure: per config, the naive full-corpus OLS estimate (red circle) and the
DSL-corrected estimate at that fraction (blue square; mean over draws), 95% CIs,
gold-label benchmark as dashed reference, gold-only-subsample estimator on top.
Configs ordered by negative-class F1 (descending), encoder first.

Inputs : trubowitz_analysis_sample.csv, trubowitz_sweep_results.csv,
         trubowitz_dsl_results.csv  (draw-level; missing fractions are computed
         on the fly and appended, 50 seeded draws each, deterministic)
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score

FRACTIONS = {0.05: "_5", 0.10: "_10", 0.188: "_eq", 0.20: "_20", 0.50: "_50", 1.0: "_100"}
N_DRAWS   = 50
MASTER_SEED = 20260708

SAMPLE = "trubowitz_analysis_sample.csv"
SWEEP  = "trubowitz_sweep_results.csv"
DSL    = "trubowitz_dsl_results.csv"

CONFIGS = ["enc_roberta", "gemma_zs", "gemma_fs", "llama_zs", "llama_fs",
           "mistral_zs", "mistral_fs", "gpt5_zs", "gpt5_fs",
           "gptmini_zs", "gptmini_fs"]
DISP = {"enc_roberta": "RoBERTa (FT)", "gemma_zs": "Gemma ZS", "gemma_fs": "Gemma FS",
        "llama_zs": "Llama ZS", "llama_fs": "Llama FS", "mistral_zs": "Mistral ZS",
        "mistral_fs": "Mistral FS", "gpt5_zs": "GPT-5.5 ZS", "gpt5_fs": "GPT-5.5 FS",
        "gptmini_zs": "GPT-5.5-mini ZS", "gptmini_fs": "GPT-5.5-mini FS"}

s     = pd.read_csv(SAMPLE)
sweep = pd.read_csv(SWEEP)
X = sm.add_constant(s[["year_c", "foreign"]])
y = s["label_main_bin"].to_numpy(float)
n = len(s)
gold_beta = sweep.loc[sweep.col == "label_main", "beta"].iloc[0]

# ---------- ensure draw-level DSL results exist for every fraction ----------
try:
    dsl = pd.read_csv(DSL)
except FileNotFoundError:
    dsl = pd.DataFrame(columns=["config", "pi", "draw", "beta", "se", "ci_lo", "ci_hi"])

seeds = np.random.default_rng(MASTER_SEED).integers(0, 2**31, size=N_DRAWS)

def run_fraction(pi):
    rows = []
    draws = [0] if pi >= 1.0 else range(N_DRAWS)
    for d in draws:
        rng = np.random.default_rng(seeds[d])
        if pi >= 1.0:
            R = np.ones(n); idx = np.arange(n)
        else:
            idx = rng.choice(n, size=int(round(pi * n)), replace=False)
            R = np.zeros(n); R[idx] = 1.0
        g = sm.OLS(y[idx], X.iloc[idx]).fit(cov_type="HC1")
        ci = g.conf_int().loc["year_c"]
        rows.append({"config": "GOLD-ONLY subsample", "pi": pi, "draw": d,
                     "beta": g.params["year_c"], "se": g.bse["year_c"],
                     "ci_lo": ci[0], "ci_hi": ci[1]})
        for cfg in CONFIGS:
            yhat = s[cfg + "_bin"].to_numpy(float)
            ok = ~np.isnan(yhat)
            y_tilde = yhat[ok] + (R[ok] / pi) * (y[ok] - yhat[ok])
            f = sm.OLS(y_tilde, X.loc[ok]).fit(cov_type="HC1")
            ci = f.conf_int().loc["year_c"]
            rows.append({"config": cfg, "pi": pi, "draw": d,
                         "beta": f.params["year_c"], "se": f.bse["year_c"],
                         "ci_lo": ci[0], "ci_hi": ci[1]})
            assert ci[0] <= f.params["year_c"] <= ci[1], "beta outside its own CI - key mismatch"
    return pd.DataFrame(rows)

for pi in FRACTIONS:
    if not np.isclose(dsl["pi"], pi).any():
        print(f"computing DSL draws for pi={pi} ...")
        dsl = pd.concat([dsl, run_fraction(pi)], ignore_index=True)
dsl.to_csv(DSL, index=False)

# ---------- config ordering by negative-class F1 ----------
f1u = {c: f1_score(s.loc[s[c+'_bin'].notna(),'label_main_bin'], s.loc[s[c+'_bin'].notna(), c+'_bin'], average=None)[1] for c in CONFIGS}
order = ["GOLD-ONLY subsample", "enc_roberta"] + sorted(
    [c for c in CONFIGS if c != "enc_roberta"], key=lambda c: -f1u[c])
naive = sweep.set_index("col")

# ---------- one figure per fraction ----------
for pi, suffix in FRACTIONS.items():
    d = (dsl[np.isclose(dsl.pi, pi)].groupby("config")
           .agg(beta=("beta", "mean"), ci_lo=("ci_lo", "mean"), ci_hi=("ci_hi", "mean"))
           .reset_index())

    fig, ax = plt.subplots(figsize=(8.2, 6.4))
    ypos = np.arange(len(order))[::-1]
    ax.axvline(gold_beta, color="0.35", lw=1.2, ls="--", zorder=1,
               label=fr"gold benchmark $\hat\beta$ = {gold_beta:.3f}")
    ax.axvline(0, color="0.85", lw=0.8, zorder=0)

    OFF = 0.16
    for yi, cfg in zip(ypos, order):
        row = d[d.config == cfg].iloc[0]
        ax.plot([row.ci_lo, row.ci_hi], [yi - OFF, yi - OFF],
                color="#1a5fb4", lw=1.7, zorder=2)
        ax.plot(row.beta, yi - OFF, "s", color="#1a5fb4", ms=5.5, zorder=3)
        if cfg in naive.index and cfg != "GOLD-ONLY subsample":
            nr = naive.loc[cfg]
            ax.plot([nr.ci_lo, nr.ci_hi], [yi + OFF, yi + OFF],
                    color="#c01c28", lw=1.7, zorder=2)
            ax.plot(nr.beta, yi + OFF, "o", color="#c01c28", ms=5.5, zorder=3)

    labels = []
    for cfg in order:
        if cfg == "GOLD-ONLY subsample":
            labels.append(f"Gold-only subsample ({pi:.0%})")
        else:
            labels.append(f"{DISP[cfg]}  (F1$_{{yes}}$ {f1u[cfg]:.2f})")
    ax.set_yticks(ypos); ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel(r"$\hat{\beta}_{Year}$")

    dsl_lab = (f"DSL-corrected ({pi:.1%} gold, mean of {N_DRAWS} draws)"
               if pi < 1.0 else "DSL-corrected (full corpus hand-labeled)")
    ax.plot([], [], "o", color="#c01c28", label="naive (full-corpus LLM labels)")
    ax.plot([], [], "s", color="#1a5fb4", label=dsl_lab)

    handles, leg_labels = ax.get_legend_handles_labels()
    leg1 = ax.legend(handles[:2], leg_labels[:2], loc="upper center",
                     bbox_to_anchor=(0.5, -0.10), ncol=2, fontsize=8.5, frameon=False)
    ax.add_artist(leg1)
    ax.legend(handles[2:], leg_labels[2:], loc="upper center",
              bbox_to_anchor=(0.5, -0.155), ncol=1, fontsize=8.5, frameon=False)

    ax.set_title("Naive vs. DSL-corrected estimates across measurement choices",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    fig.savefig(f"trubowitz_forest_dsl{suffix}.pdf")
    fig.savefig(f"trubowitz_forest_dsl{suffix}.png", dpi=200)
    plt.close(fig)
    print(f"wrote trubowitz_forest_dsl{suffix}.pdf / .png")
