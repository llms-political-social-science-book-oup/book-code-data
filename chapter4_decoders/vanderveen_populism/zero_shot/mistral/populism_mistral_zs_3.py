##
## Mistral: Populism Classification
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

RESULTS_DIR = "results_populism_mistral_zs"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(
    base_url="https://api.deepinfra.com/v1/openai",
    api_key=os.environ["DEEPINFRA_API_KEY"]
)

# load data

df = pd.read_excel("../../../../data/vanderveen_populism/vanderveen_populism_text_labels.xlsx")
texts = [str(t) for t in df["text"].tolist()]
labels = df["label_main"].tolist()

print(f"Loaded {len(texts)} sentences")

# Zero-shot: explanation but no examples 

system_prompt = """You are an expert at political text annotation. Your task is to classify sentences \
from US governor and presidential candidate speeches as POPULIST, PLURALIST, or NEUTRAL.

This follows the ideational approach to populism, which treats populism as a discursive frame \
built on a Manichean moral struggle between the virtuous "people" and the corrupt "elite".

A sentence is POPULIST if it expresses any of the following:
1. Valorization of "the people", the common or ordinary people, or their will
2. Denigration of "the elite", the establishment, or those in power as corrupt or self-serving
3. A framing of politics as a moral struggle between the virtuous people and a corrupt elite

A sentence is PLURALIST if it expresses the opposite of populism, such as:
1. Politics as legitimate competition or cooperation among diverse groups and interests
2. Recognition of the legitimacy of opponents, compromise, or shared institutions
3. Rejection of the idea of a single unified people opposed to a corrupt elite

A sentence is NEUTRAL if it expresses neither populist nor pluralist rhetoric, for example \
ordinary policy, factual, or procedural content.

Respond with exactly one word: POPULIST, PLURALIST, or NEUTRAL. Nothing else."""

# helper

class_labels = ["populist", "pluralist", "neutral"]

def parse_label(response):
    r = response.upper().strip()
    if "POPULIST" in r:
        return "populist"
    elif "PLURALIST" in r:
        return "pluralist"
    elif "NEUTRAL" in r:
        return "neutral"
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="mistralai/Mistral-Small-3.2-24B-Instruct-2506",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Sentence: "{text}"\n\nClassification:'}
        ],
        temperature=0,
        max_tokens=10,
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

# run classification on all sentences

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

results_df.to_csv(f"{RESULTS_DIR}/mistral_populism_preds_3.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

prec = precision_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
rec = recall_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1 = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1_macro = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average="macro", zero_division=0)

print(f"\n=== Mistral Small 24B Populism Baseline ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
for i, c in enumerate(class_labels):
    print(f"  {c:<10}-> P: {prec[i]:.3f}  R: {rec[i]:.3f}  F1: {f1[i]:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "mistralai/Mistral-Small-3.2-24B-Instruct-2506",
    "condition": "prompting_baseline_zeroshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
}
for i, c in enumerate(class_labels):
    metrics[f"prec_{c}"] = round(float(prec[i]), 4)
    metrics[f"rec_{c}"] = round(float(rec[i]), 4)
    metrics[f"f1_{c}"] = round(float(f1[i]), 4)
metrics["f1_macro"] = round(float(f1_macro), 4)


with open(f"{RESULTS_DIR}/mistral_populism_metrics_3.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
