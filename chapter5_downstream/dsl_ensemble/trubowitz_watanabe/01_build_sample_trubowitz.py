"""
01_build_sample_foy.py — Merge Foy predictions, encoder OOF, and covariates.

SPEC (final): threat_yes ~ year_c + foreign   (LPM, HC1)
Sample: all 1,700 validation rows (100 per decade by construction).
DV: Yes = 1 vs rest (No and Unclear). year_c = (year-1939)/100, per-century.
The 52 empty majority-vote cells stay NaN (dropped per-config), never coded 0.
"""
import pandas as pd
import numpy as np

preds = pd.read_csv("../../../data/trubowitz_watanabe/trubowitz_predictions.csv")
enc   = pd.read_csv("../../../data/trubowitz_watanabe/trubowitz_encoder_oof_predictions.csv")
cov   = pd.read_csv("../../../data/trubowitz_watanabe/trubowitz_covariates.csv")

assert (preds["row_id"] == enc["row_id"]).all(),         "preds/encoder row_id mismatch"
assert (preds["label_main"] == enc["label_main"]).all(), "preds/encoder gold-label mismatch"
assert (preds["row_id"] == cov["row_id"]).all(),         "preds/covariates row_id mismatch"
assert (preds["text_hash"] == cov["text_hash"]).all(),   "preds/covariates text_hash mismatch"

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

# NaN-safe binarization: empty cells stay NaN
for col in ["label_main","enc_roberta"] + DEC:
    v = df[col].astype("string").str.strip().str.lower()
    df[col + "_bin"] = np.where(v.isna(), np.nan, (v == "yes").astype(float))

# full validation set: covariates complete by construction
sample = df.copy()
sample["year_c"]  = (sample["year"] - 1939) / 100.0   # per-century units, centered
sample["foreign"] = (sample["sample"] == "foreign").astype(int)

print(f"merged {len(df)} -> analysis sample {len(sample)} (expect 1700)")
print("gold negative rate:", round(sample["label_main_bin"].mean(), 3))
print("mistral_fs NaN in sample:", int(sample["mistral_fs_bin"].isna().sum()))
sample.to_csv("trubowitz_analysis_sample.csv", index=False)
print("wrote trubowitz_analysis_sample.csv")
