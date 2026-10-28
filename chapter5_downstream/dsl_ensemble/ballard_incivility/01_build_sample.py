"""
01_build_sample.py — Merge predictions, encoder OOF, and covariates into the analysis sample.

Inputs  (same directory or edit paths below):
  - ballard_predictions.csv                (row-level decoder predictions, 10 configs + disagree flags)
  - ballard_encoder_oof_predictions.csv    (encoder out-of-fold predictions from the seeded 10-fold run)
  - ballard_covariates.csv                 (party/chamber/gender/state/dw_nominate per tweet)

Output:
  - ballard_analysis_sample.csv            (n=2,887: D/R only, complete party/chamber/gender)

Sample logic:
  2,919 rows total
    - 4 rows with no author identifier (no covariates at all)      -> dropped
    - 28 tweets by Independents                                     -> dropped (party binary)
    - 9 @GOPLeader rows keep era-invariant covariates (R/House/M)   -> KEPT
  = 2,887 analysis rows
"""
import pandas as pd
import os 


PREDS = "../../../data/ballard_incivility/ballard_predictions.csv"
ENC   = "../../../data/ballard_incivility/ballard_encoder_oof_predictions.csv"
COV   = "../../../data/ballard_incivility/ballard_covariates.csv"
OUT   = "ballard_analysis_sample.csv"

preds = pd.read_csv(PREDS)
enc   = pd.read_csv(ENC)
cov   = pd.read_csv(COV)

# --- alignment gates: refuse to run on misaligned inputs ---
assert (preds["row_id"] == enc["row_id"]).all(),        "preds/encoder row_id mismatch"
assert (preds["label_main"] == enc["label_main"]).all(),"preds/encoder gold-label mismatch"
assert (preds["row_id"] == cov["row_id"]).all(),        "preds/covariates row_id mismatch"
assert (preds["text_hash"] == cov["text_hash"]).all(),  "preds/covariates text_hash mismatch"

# the predictions file ships enc_roberta empty; take it from the OOF file
df = (preds.drop(columns=["enc_roberta"])
           .merge(enc[["row_id", "enc_roberta"]], on="row_id", validate="1:1")
           .merge(cov[["row_id", "party", "chamber", "gender", "state",
                       "dw_nominate", "member_name"]], on="row_id", validate="1:1"))

sample = df[df["party"].isin(["D", "R"])
            & df["chamber"].notna()
            & df["gender"].notna()].copy()

sample["republican"] = (sample["party"] == "R").astype(int)
sample["senate"]     = (sample["chamber"] == "Senate").astype(int)
sample["female"]     = (sample["gender"] == "F").astype(int)

print(f"merged rows: {len(df)}   analysis rows: {len(sample)}  (expect 2,887)")
print("party counts:", sample["party"].value_counts().to_dict())
sample.to_csv(OUT, index=False)
print(f"wrote {OUT}")
