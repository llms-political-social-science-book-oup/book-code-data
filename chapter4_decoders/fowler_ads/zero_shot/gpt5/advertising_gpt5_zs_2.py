##
## GPT5: Political Ad Tone (Fowler et al.)
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

RESULTS_DIR = "results_advertising_gpt5_zs"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])  # my key, do not share.

models = client.models.list()
for model in models:
    print(model.id) ## shows you all available model names. Use these in "model = ..." below.


# load data

df = pd.read_excel("../../../../data/fowler_ads/fowler_ads_text_labels.xlsx")
texts = [str(t) for t in df["text"].tolist()]
labels = df["label_main"].tolist()

print(f"Loaded {len(texts)} ads")

# system prompt

class_labels = ["Promote", "Contrast", "Attack"]

system_prompt = """You are an expert at political text annotation. Your task is to classify the tone of a political \
campaign advertisement as PROMOTE, CONTRAST, or ATTACK, based on which candidates the ad references.

PROMOTE: the ad refers only to the favored or sponsoring candidate and does not mention an opponent.
CONTRAST: the ad mentions both the favored candidate and an opponent, comparing them.
ATTACK: the ad refers only to an opponent, criticizing them, apart from naming the sponsor.

Respond with exactly one word: PROMOTE, CONTRAST, or ATTACK. Nothing else."""

# helper

def parse_label(response):
    r = response.upper().strip()
    if "PROMOT" in r:
        return "Promote"
    elif "CONTRAST" in r:
        return "Contrast"
    elif "ATTACK" in r:
        return "Attack"
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="gpt-5.5",  # let's use 5.5 for all the runs
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Advertisement: "{text}"\n\nTone:'}
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

# run classification on all ads

t0 = time.time()
raw_responses = [classify(system_prompt, text) for text in tqdm(texts)]
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
results_df.to_csv(f"{RESULTS_DIR}/gpt5_advertising_preds_2.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

prec = precision_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
rec = recall_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1 = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1_macro = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average="macro", zero_division=0)

print(f"\n=== GPT5 Ad Tone ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
for i, c in enumerate(class_labels):
    print(f"  {c:<10}-> P: {prec[i]:.3f}  R: {rec[i]:.3f}  F1: {f1[i]:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "openai/gpt-5.5",
    "condition": "prompting_zeroshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
}
for i, c in enumerate(class_labels):
    metrics[f"prec_{c}"] = round(float(prec[i]), 4)
    metrics[f"rec_{c}"] = round(float(rec[i]), 4)
    metrics[f"f1_{c}"] = round(float(f1[i]), 4)
metrics["f1_macro"] = round(float(f1_macro), 4)

with open(f"{RESULTS_DIR}/gpt5_advertising_metrics_2.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
