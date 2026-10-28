##
## Gemma: Article IV Natural-Resource Governance
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

RESULTS_DIR = "results_articleiv_gemma_zs"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(
    base_url="https://api.deepinfra.com/v1/openai",
    api_key=os.environ["DEEPINFRA_API_KEY"]
)

# load data

df = pd.read_excel("../../../../data/goes_chapman/goes_chapman_articleiv_text_labels.xlsx")
texts = [str(t) for t in df["text"].tolist()]
labels = df["label_main"].tolist()

print(f"Loaded {len(texts)} staff appraisals")

# system prompt

system_prompt = """You are an expert at political text annotation. Your task is to classify the staff-appraisal \
section of an IMF Article IV consultation report according to whether it PROMOTES NATURAL-RESOURCE \
GOVERNANCE.

A staff appraisal PROMOTES natural-resource governance if it contains IMF advice, recommendations, \
or encouragement aimed at improving the governance, management, transparency, or reform of the \
country's natural-resource sector (oil, gas, mining, minerals, and other extractive industries). \
This includes calls to:
1. Improve transparency or accountability in the resource sector (e.g., EITI, publishing resource contracts or revenues)
2. Strengthen the management of natural-resource revenues or wealth (e.g., sovereign wealth or natural-resource funds, fiscal rules for resource income)
3. Reform the legal, regulatory, or institutional framework governing extractive industries
4. Reduce corruption or improve oversight in the natural-resource sector

A staff appraisal does NOT promote natural-resource governance if it offers no such advice. Merely \
mentioning natural resources, oil, or mining in passing, without advice aimed at governing or \
reforming the sector, does NOT count as promoting governance.

Does this staff appraisal promote natural-resource governance? Respond with exactly one word: YES or NO. \
Nothing else."""

# helper

def parse_label(response):
    r = response.upper().strip()
    if "YES" in r:
        return 1
    elif "NO" in r:
        return 0
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="google/gemma-4-31B-it",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Staff appraisal: "{text}"\n\nClassification:'}
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

# run classification on all texts

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
results_df.to_csv(f"{RESULTS_DIR}/gemma_articleiv_preds_1.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

f1_no = f1_score(valid["true_label"], valid["predicted"], pos_label=0)
f1_yes = f1_score(valid["true_label"], valid["predicted"], pos_label=1)
f1_macro = f1_score(valid["true_label"], valid["predicted"], average="macro")
prec_no = precision_score(valid["true_label"], valid["predicted"], pos_label=0)
rec_no = recall_score(valid["true_label"], valid["predicted"], pos_label=0)
prec_yes = precision_score(valid["true_label"], valid["predicted"], pos_label=1)
rec_yes = recall_score(valid["true_label"], valid["predicted"], pos_label=1)

print(f"\n=== Gemma Article IV ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
print(f"  No governance (0)  -> P: {prec_no:.3f}  R: {rec_no:.3f}  F1: {f1_no:.3f}")
print(f"  Promotes gov. (1)  -> P: {prec_yes:.3f}  R: {rec_yes:.3f}  F1: {f1_yes:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "google/gemma-4-31B-it",
    "condition": "prompting_zeroshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
    "prec_no": round(prec_no, 4),
    "rec_no": round(rec_no, 4),
    "f1_no": round(f1_no, 4),
    "prec_yes": round(prec_yes, 4),
    "rec_yes": round(rec_yes, 4),
    "f1_yes": round(f1_yes, 4),
    "f1_macro": round(f1_macro, 4)
}

with open(f"{RESULTS_DIR}/gemma_articleiv_metrics_1.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
