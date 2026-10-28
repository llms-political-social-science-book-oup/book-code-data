##
## GPT Mini: Negativity Classification
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

RESULTS_DIR = "results_poltext_gpt_mini_zs"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"]) 

models = client.models.list()
for model in models:
    print(model.id) ## shows you all available model names. Use these in "model = ..." below.
    

# load data

df = pd.read_excel("../../../../data/heseltine/heseltine_annotation_text_labels.xlsx")
texts = [str(t) for t in df["text"].tolist()]
labels = df["label_main"].tolist()

print(f"Loaded {len(texts)} texts")

# system prompt

system_prompt = """You are an expert at political text annotation. Your task is to classify texts \
from politicians (tweets from the United States, Germany, Chile, and Italy) and U.S. \
news-media articles as either NEGATIVE or NOTNEGATIVE. Texts may be in English, German, \
Spanish, or Italian.

A text is NEGATIVE if it attacks, criticizes, blames, or speaks unfavorably about a \
political opponent, party, group, institution, policy, or person, or if it conveys anger, \
fear, or other clearly negative sentiment about a political subject.

A text is NOTNEGATIVE if it does not do any of the above, for example if it is positive, \
celebratory, promotional, neutral, informational, or a factual announcement.

Respond with exactly one word: NEGATIVE or NOTNEGATIVE. Nothing else."""

# helper

def parse_label(response):
    r = response.upper().strip()
    if "NOTNEGATIVE" in r or "NOT NEGATIVE" in r or "NON-NEGATIVE" in r:
        return 0
    elif "NEGATIVE" in r:
        return 1
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Text: "{text}"\n\nClassification:'}
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
results_df.to_csv(f"{RESULTS_DIR}/gpt_mini_poltext_preds_3.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

f1_notnegative = f1_score(valid["true_label"], valid["predicted"], pos_label=0)
f1_negative = f1_score(valid["true_label"], valid["predicted"], pos_label=1)
f1_macro = f1_score(valid["true_label"], valid["predicted"], average="macro")
prec_notnegative = precision_score(valid["true_label"], valid["predicted"], pos_label=0)
rec_notnegative = recall_score(valid["true_label"], valid["predicted"], pos_label=0)
prec_negative = precision_score(valid["true_label"], valid["predicted"], pos_label=1)
rec_negative = recall_score(valid["true_label"], valid["predicted"], pos_label=1)

print(f"\n=== GPT Mini Political Text ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
print(f"  Notnegative -> P: {prec_notnegative:.3f}  R: {rec_notnegative:.3f}  F1: {f1_notnegative:.3f}")
print(f"  Negative    -> P: {prec_negative:.3f}  R: {rec_negative:.3f}  F1: {f1_negative:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "openai/gpt-5.4-mini",
    "condition": "prompting_zeroshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
    "prec_notnegative": round(prec_notnegative, 4),
    "rec_notnegative": round(rec_notnegative, 4),
    "f1_notnegative": round(f1_notnegative, 4),
    "prec_negative": round(prec_negative, 4),
    "rec_negative": round(rec_negative, 4),
    "f1_negative": round(f1_negative, 4),
    "f1_macro": round(f1_macro, 4)
}

with open(f"{RESULTS_DIR}/gpt_mini_poltext_metrics_3.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
