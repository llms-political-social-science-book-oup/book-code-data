##
## GPT Mini: Populism Classification
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

RESULTS_DIR = "results_popbert_gpt_mini_zs"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"]) 

models = client.models.list()
for model in models:
    print(model.id) ## shows you all available model names. Use these in "model = ..." below.
    
    
# load data

df = pd.read_excel("../../../../data/erhard_popbert/popbert_text_labels.xlsx")
texts = [str(t) for t in df["text"].tolist()]
labels = df["label_main"].tolist()

print(f"Loaded {len(texts)} sentences")

# system prompt

system_prompt = """You are an expert at political text annotation. Your task is to classify sentences \
from plenary speeches in the German Bundestag as either POPULIST or NONPOPULIST.

A sentence is POPULIST if it contains any of the following:
1. Anti-elitism: criticizing, blaming, or denigrating political, economic, or media elites \
as corrupt, self-serving, dishonest, or working against the common good
2. People-centrism: appealing to the common people, the ordinary citizens, or the popular \
will as a virtuous and unified body that politics should serve

A sentence is NONPOPULIST if it does not contain any of the above. Note that ordinary policy \
debate, factual statements, technical points, or substantive disagreement are NOT populist \
unless they invoke a moral opposition between a virtuous people and a corrupt elite.

Respond with exactly one word: POPULIST or NONPOPULIST. Nothing else."""

# helper

def parse_label(response):
    r = response.upper().strip()
    if "NONPOPULIST" in r or "NON-POPULIST" in r:
        return 0
    elif "POPULIST" in r:
        return 1
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Sentence: "{text}"\n\nClassification:'}
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
results_df.to_csv(f"{RESULTS_DIR}/gpt_mini_popbert_preds_2.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

f1_nonpopulist = f1_score(valid["true_label"], valid["predicted"], pos_label=0)
f1_populist = f1_score(valid["true_label"], valid["predicted"], pos_label=1)
f1_macro = f1_score(valid["true_label"], valid["predicted"], average="macro")
prec_nonpopulist = precision_score(valid["true_label"], valid["predicted"], pos_label=0)
rec_nonpopulist = recall_score(valid["true_label"], valid["predicted"], pos_label=0)
prec_populist = precision_score(valid["true_label"], valid["predicted"], pos_label=1)
rec_populist = recall_score(valid["true_label"], valid["predicted"], pos_label=1)

print(f"\n=== GPT Mini Popbert ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
print(f"  Nonpopulist -> P: {prec_nonpopulist:.3f}  R: {rec_nonpopulist:.3f}  F1: {f1_nonpopulist:.3f}")
print(f"  Populist    -> P: {prec_populist:.3f}  R: {rec_populist:.3f}  F1: {f1_populist:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "openai/gpt-5.4-mini",
    "condition": "prompting_zeroshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
    "prec_nonpopulist": round(prec_nonpopulist, 4),
    "rec_nonpopulist": round(rec_nonpopulist, 4),
    "f1_nonpopulist": round(f1_nonpopulist, 4),
    "prec_populist": round(prec_populist, 4),
    "rec_populist": round(rec_populist, 4),
    "f1_populist": round(f1_populist, 4),
    "f1_macro": round(f1_macro, 4)
}

with open(f"{RESULTS_DIR}/gpt_mini_popbert_metrics_2.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
