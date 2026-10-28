##
## GPT Mini: Incivility in Congressional Tweets (Ballard et al.)
## Joan Timoneda, March 2026
## Via DeepInfra API
##

from openai import OpenAI
from tqdm import tqdm
import pandas as pd
import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score
import json
import os
import time


# config

RESULTS_DIR = "results_rhetoric_gpt_mini_zs"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"], max_retries=8, timeout=120) 

models = client.models.list()
for model in models:
    print(model.id) ## shows you all available model names. Use these in "model = ..." below.
    

# load data

df = pd.read_excel("../../../../data/ballard_incivility/incivility_tweets_text_labels.xlsx")
df = df[df["label_main"].isin([0, 1])].reset_index(drop=True)
texts = [str(t) for t in df["text"].tolist()]
labels = df["label_main"].tolist()

print(f"Loaded {len(texts)} tweets")

# system prompt

system_prompt = """You are an expert at political text annotation. Your task is to classify tweets \
from members of the US Congress as either CIVIL or INCIVIL.

A tweet is INCIVIL if it contains any of the following:
1. Name-calling, mockery, sarcasm, or character assassination
2. Spin or misrepresentative exaggeration
3. Emotionality or digital stridency
4. Conspiracy theory

A tweet is CIVIL if it does not contain any of the above. Note that strong policy \
disagreement, criticism of legislation, or negative characterizations of policy outcomes \
are NOT incivil unless they involve personal attacks, mockery, or deliberate distortion.

Respond with exactly one word: CIVIL or INCIVIL. Nothing else."""

# helper

def parse_label(response):
    r = response.upper().strip()
    if "INCIVIL" in r:
        return 1
    elif "CIVIL" in r:
        return 0
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Tweet: "{text}"\n\nClassification:'}
        ],
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].message.content.strip()

# quick test

test_response = classify(system_prompt, texts[0])
print(f"Test response: '{test_response}'")
print(f"True label: {labels[0]}")
print(f"Parsed: {parse_label(test_response)}")

# run classification

t0 = time.time()
from concurrent.futures import ThreadPoolExecutor as _TPE
_W = int(os.environ.get("RERUN_WORKERS", "8"))
def _safe(_t):
    try:
        return classify(system_prompt, _t)
    except Exception as _e:
        _m = str(_e).lower()
        if any(k in _m for k in ("authenticat","invalid_api_key","insufficient_quota","exceeded your current quota","billing","no such model","does not exist","model_not_found","401","account is not active")):
            raise
        return ""
with _TPE(max_workers=_W) as _ex:
    raw_responses = list(tqdm(_ex.map(_safe, texts), total=len(texts)))
total_time = time.time() - t0
print(f"\nDone in {int(total_time//60)}m{int(total_time%60):02d}s")

preds = [parse_label(r) for r in raw_responses]

# compute and save metrics

results_df = pd.DataFrame({
    "text": texts,
    "true_label": labels,
    "predicted": preds,
    "raw_response": raw_responses
})
results_df.to_csv(f"{RESULTS_DIR}/gpt_mini_rhetoric_preds_3.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

f1_civil = f1_score(valid["true_label"], valid["predicted"], pos_label=0)
f1_incivil = f1_score(valid["true_label"], valid["predicted"], pos_label=1)
f1_macro = f1_score(valid["true_label"], valid["predicted"], average="macro")
prec_civil = precision_score(valid["true_label"], valid["predicted"], pos_label=0)
rec_civil = recall_score(valid["true_label"], valid["predicted"], pos_label=0)
prec_incivil = precision_score(valid["true_label"], valid["predicted"], pos_label=1)
rec_incivil = recall_score(valid["true_label"], valid["predicted"], pos_label=1)

print(f"\n=== GPT Mini Rhetoric ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
print(f"  Civil     -> P: {prec_civil:.3f}  R: {rec_civil:.3f}  F1: {f1_civil:.3f}")
print(f"  Incivil   -> P: {prec_incivil:.3f}  R: {rec_incivil:.3f}  F1: {f1_incivil:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "openai/gpt-5.4-mini",
    "condition": "prompting_zeroshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
    "prec_civil": round(prec_civil, 4),
    "rec_civil": round(rec_civil, 4),
    "f1_civil": round(f1_civil, 4),
    "prec_incivil": round(prec_incivil, 4),
    "rec_incivil": round(rec_incivil, 4),
    "f1_incivil": round(f1_incivil, 4),
    "f1_macro": round(f1_macro, 4)
}

with open(f"{RESULTS_DIR}/gpt_mini_rhetoric_metrics_3.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
