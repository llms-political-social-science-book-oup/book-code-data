##
## GPT Mini: Geopolitical Threat (Trubowitz & Watanabe)
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

RESULTS_DIR = "results_geothreats_gpt_mini_zs"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"]) 

models = client.models.list()
for model in models:
    print(model.id) ## shows you all available model names. Use these in "model = ..." below.
    
    
# load data

df = pd.read_excel("../../../../data/trubowitz_watanabe/trubowitz_gti_text_labels.xlsx")
texts = [str(t) for t in df["text"].tolist()]
labels = df["label_main"].tolist()

print(f"Loaded {len(texts)} articles")

# system prompt

class_labels = ["No", "Yes", "Unclear"]

system_prompt = """You are an expert at political text annotation. Your task is to classify a New York Times article \
excerpt according to whether it conveys a GEOPOLITICAL THREAT to the United States.

A geopolitical threat is a portrayal of a foreign state or actor as hostile, aggressive, or dangerous to \
the United States or its interests, for example through military conflict, war, aggression, rivalry, or \
other security threats from abroad.

Classify the excerpt as:
Yes = it conveys a geopolitical threat (it portrays a foreign state or actor as hostile, aggressive, or dangerous).
No = it does not convey a geopolitical threat (e.g., it describes peaceful, cooperative, or neutral relations, or is not about a foreign threat at all).
Unclear = it is ambiguous or there is not enough information to tell.

Respond with exactly one word: Yes, No, or Unclear. Nothing else."""

# helper

def parse_label(response):
    r = response.upper().strip()
    if "UNCLEAR" in r:
        return "Unclear"
    elif "YES" in r:
        return "Yes"
    elif "NO" in r:
        return "No"
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Article: "{text}"\n\nClassification:'}
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
results_df.to_csv(f"{RESULTS_DIR}/gpt_mini_geothreats_preds_3.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

prec = precision_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
rec = recall_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1 = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1_macro = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average="macro", zero_division=0)

print(f"\n=== GPT Mini Geopolitical Threat ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
for i, c in enumerate(class_labels):
    print(f"  {c:<8}-> P: {prec[i]:.3f}  R: {rec[i]:.3f}  F1: {f1[i]:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "openai/gpt-5.4-mini",
    "condition": "prompting_zeroshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
}
for i, c in enumerate(class_labels):
    metrics[f"prec_{c}"] = round(float(prec[i]), 4)
    metrics[f"rec_{c}"] = round(float(rec[i]), 4)
    metrics[f"f1_{c}"] = round(float(f1[i]), 4)
metrics["f1_macro"] = round(float(f1_macro), 4)

with open(f"{RESULTS_DIR}/gpt_mini_geothreats_metrics_3.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
