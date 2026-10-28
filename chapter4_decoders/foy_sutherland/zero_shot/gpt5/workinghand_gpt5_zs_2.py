##
## GPT5: Redbox Message Tone (Foy & Sutherland)
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

RESULTS_DIR = "results_workinghand_gpt5_zs"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"]) 

models = client.models.list()
for model in models:
    print(model.id) ## shows you all available model names. Use these in "model = ..." below.
    

# load data

df = pd.read_excel("../../../../data/foy_sutherland/redbox_text_labels.xlsx")
texts = [str(t) for t in df["text"].tolist()]
labels = df["label_main"].tolist()

print(f"Loaded {len(texts)} redbox messages")

# system prompt

class_labels = ["Positive", "Contrast", "Negative"]

system_prompt = """You are an expert at political text annotation. Your task is to classify the tone of a "red box" \
message, an instruction a US congressional campaign posts on its website to signal to allied super PACs \
what advertising to run, as POSITIVE, CONTRAST, or NEGATIVE, based on which candidate it focuses on.

POSITIVE: the message refers only to the favored or sponsoring candidate, presenting them favorably.
CONTRAST: the message refers to both the favored candidate and an opponent, comparing them.
NEGATIVE: the message refers only to an opponent, presenting them unfavorably or attacking them.

Respond with exactly one word: POSITIVE, CONTRAST, or NEGATIVE. Nothing else."""

# helper

def parse_label(response):
    r = response.upper().strip()
    if "POSITIVE" in r:
        return "Positive"
    elif "CONTRAST" in r:
        return "Contrast"
    elif "NEGATIVE" in r:
        return "Negative"
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Message: "{text}"\n\nTone:'}
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

# run classification on all messages

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
results_df.to_csv(f"{RESULTS_DIR}/gpt5_workinghand_preds_2.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

prec = precision_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
rec = recall_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1 = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1_macro = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average="macro", zero_division=0)

print(f"\n=== GPT5 Working Hand ===")
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

with open(f"{RESULTS_DIR}/gpt5_workinghand_metrics_2.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
