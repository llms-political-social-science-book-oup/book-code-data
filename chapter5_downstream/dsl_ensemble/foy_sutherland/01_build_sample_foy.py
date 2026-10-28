"""
01_build_sample_foy.py — Merge Foy predictions, encoder OOF, and covariates.

DV construction: NEGATIVE = 1 vs. rest (binarized from the 3-class scheme).
The encoder OOF file stores label CODES; the mapping code->name is taken from
its label_main/label_code pairing, so no hardcoded assumption about ordering.

Inputs : foy_predictions.csv, foy_encoder_oof_predictions.csv, foy_covariates.csv
Output : foy_analysis_sample.csv
NOTE   : covariate fields and sample filters are PROVISIONAL until the real
         covariate inventory arrives; edit the COVARS list and FILTER section.
"""
import pandas as pd

preds = pd.read_csv("../../../data/foy_sutherland/foy_predictions.csv")
enc   = pd.read_csv("../../../data/foy_sutherland/foy_encoder_oof_predictions.csv")
cov   = pd.read_csv("../../../data/foy_sutherland/foy_covariates.csv")

# --- alignment gates ---
assert (preds["row_id"] == enc["row_id"]).all(),         "preds/encoder row_id mismatch"
assert (preds["label_main"] == enc["label_main"]).all(), "preds/encoder gold-label mismatch"
assert (preds["row_id"] == cov["row_id"]).all(),         "preds/covariates row_id mismatch"
assert (preds["text_hash"] == cov["text_hash"]).all(),   "preds/covariates text_hash mismatch"

# --- decode the encoder's predicted codes back to label names ---
code_map = (enc[["label_code", "label_main"]].drop_duplicates()
            .set_index("label_code")["label_main"].to_dict())
enc["enc_roberta_name"] = enc["enc_roberta"].map(code_map)
assert enc["enc_roberta_name"].notna().all(), "unmapped encoder prediction code"

DEC = ["gemma_zs","gemma_fs","llama_zs","llama_fs","mistral_zs","mistral_fs",
       "gpt5_zs","gpt5_fs","gptmini_zs","gptmini_fs"]

df = (preds.drop(columns=["enc_roberta"])
        .merge(enc[["row_id","enc_roberta_name"]], on="row_id", validate="1:1")
        .rename(columns={"enc_roberta_name":"enc_roberta"})
        .merge(cov.drop(columns=["text_hash"]), on="row_id", validate="1:1"))

# --- binarize every label source: NEGATIVE vs rest ---
for col in ["label_main","enc_roberta"] + DEC:
    df[col + "_bin"] = (df[col].str.strip().str.lower() == "negative").astype(int)

# --- PROVISIONAL covariates/filters (edit after inventory) ---
COVARS = ["party","incumbent","gender"]
sample = df[df["party"].isin(["D","R"])].dropna(subset=COVARS).copy()
sample["republican"] = (sample["party"]=="R").astype(int)
sample["female"]     = (sample["gender"]=="F").astype(int)

print(f"merged {len(df)} rows -> analysis sample {len(sample)}")
print("gold negative rate:", round(sample["label_main_bin"].mean(),3))
sample.to_csv("foy_analysis_sample.csv", index=False)
print("wrote foy_analysis_sample.csv")
