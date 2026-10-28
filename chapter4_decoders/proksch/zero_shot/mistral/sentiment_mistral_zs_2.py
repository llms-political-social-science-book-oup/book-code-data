##
## Mistral: Multilingual Sentiment
## Joan Timoneda, March 2026
## Via DeepInfra API
##

from openai import OpenAI
from tqdm import tqdm
import pandas as pd
import json
import os
import time
from sklearn.metrics import confusion_matrix, f1_score, recall_score, precision_score, ConfusionMatrixDisplay


# config

RESULTS_DIR = "results_sentiment_mistral_zs"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(
    base_url="https://api.deepinfra.com/v1/openai",
    api_key=os.environ["DEEPINFRA_API_KEY"]
)

# load data

df = pd.read_excel("../../../../data/proksch/soteu2010_text_labels.xlsx")
texts = [str(t) for t in df["Text"].tolist()]
labels = [int(round(x * 2 - 1)) for x in df["label_main"].tolist()]

print(f"Loaded {len(texts)} sentences")

# system prompt

system_prompt = """You are an expert at political text annotation. Your task is to classify the sentiment of a \
paragraph from a legislative speech in the 2010 State of the European Union debate. The paragraph may be in \
any language; judge the sentiment regardless of language.

Rate the sentiment on a 9-point scale from 1 to 9:
1: very negative (strong criticism, conflict, opposition, or hostility)
3: somewhat negative
5: neutral (balanced, factual, or mixed, with no clear positive or negative sentiment)
7: somewhat positive
9: very positive (strong praise, support, optimism, or agreement)
Use the even-numbered values (2, 4, 6, 8) for sentiment that falls between these anchors.

Respond with exactly one number from 1 to 9. Nothing else."""

# helper

def parse_label(response):
    for ch in response.strip():
        if ch in "123456789":
            return int(ch)
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="mistralai/Mistral-Small-3.2-24B-Instruct-2506",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Sentence: "{text}"\n\nSentiment:'}
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

results_df.to_csv(f"{RESULTS_DIR}/mistral_sentiment_preds_2.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

f1_macro = f1_score(valid["true_label"], valid["predicted"], average="macro")
f1_weighted = f1_score(valid["true_label"], valid["predicted"], average="weighted")
prec_macro = precision_score(valid["true_label"], valid["predicted"], average="macro", zero_division=0)
rec_macro = recall_score(valid["true_label"], valid["predicted"], average="macro", zero_division=0)
accuracy = (valid["true_label"] == valid["predicted"]).mean()

print(f"\n=== Mistral Sentiment ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
print(f"  Accuracy:    {accuracy:.3f}")
print(f"  Macro     -> P: {prec_macro:.3f}  R: {rec_macro:.3f}  F1: {f1_macro:.3f}")
print(f"  Weighted F1: {f1_weighted:.3f}")

metrics = {
    "model": "mistralai/Mistral-Small-3.2-24B-Instruct-2506",
    "condition": "prompting_zeroshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
    "accuracy": round(float(accuracy), 4),
    "prec_macro": round(float(prec_macro), 4),
    "rec_macro": round(float(rec_macro), 4),
    "f1_macro": round(float(f1_macro), 4),
    "f1_weighted": round(float(f1_weighted), 4)
}


with open(f"{RESULTS_DIR}/mistral_sentiment_metrics_2.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
