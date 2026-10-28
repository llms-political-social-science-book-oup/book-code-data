"""Merge the rebuilt ad texts with the labels used in the book.

Run merge_texts.R first (it writes fowler_ads_rebuilt_text.csv). This script
joins that file to fowler_ads_labels.csv on page_id and snapshot_id, checks every
text against the stored md5 hash, and writes fowler_ads_text_labels.xlsx with the
columns the notebooks and scripts expect. Requires pandas and openpyxl.
"""
import hashlib, re, sys
import pandas as pd

labels = pd.read_csv("fowler_ads_labels.csv", dtype={"page_id": str, "snapshot_id": str})
texts = pd.read_csv("fowler_ads_rebuilt_text.csv", dtype=str).fillna({"text": ""})
m = labels.merge(texts, on=["page_id", "snapshot_id"], how="left", validate="m:1")
if m["text"].isna().any():
    print(f"WARNING: {int(m['text'].isna().sum())} rows found no text in the archive"); m["text"] = m["text"].fillna("")
# Excel cannot store control characters; the spreadsheet used in the book carries
# them in the _xHHHH_ escape form, so the same form is applied before hashing.
m["text"] = m["text"].map(lambda s: re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", lambda c: "_x%04X_" % ord(c.group()), s))
ok = m["text"].map(lambda s: hashlib.md5(str(s).encode("utf-8")).hexdigest()) == m["text_hash"]
print(f"{int(ok.sum())} of {len(m)} texts match the hash of the text used in the book")
if not ok.all():
    print("row_id of mismatches:", m.loc[~ok, "row_id"].tolist()[:50])
cols = ["source", "text"] + [c for c in labels.columns if c not in ("row_id", "text_hash", "source", "page_id", "snapshot_id", "translated_in_en_file")]
m.sort_values("row_id")[cols].to_excel("fowler_ads_text_labels.xlsx", index=False)
print("wrote fowler_ads_text_labels.xlsx")
n_tr = int(labels["translated_in_en_file"].sum())
print(f"Note: the encoder notebook read fowler_ads_text_labels_en.xlsx, in which {n_tr} Spanish-language ads "
      "(translated_in_en_file == 1) were machine-translated to English; the decoder scripts used the untranslated file.")
