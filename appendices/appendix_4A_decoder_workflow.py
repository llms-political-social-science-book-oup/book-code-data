"""
Appendix 4.A -- An annotated decoder annotation workflow (Chapter 4).

Labels the van der Veen (2024) populism sentences with a prompted decoder LLM
through an OpenAI-compatible API (DeepInfra by default), scores each of three
runs against the human labels, combines them by majority vote, and saves the
predictions for the downstream analyses of Chapter 5.

Requirements: pip install openai tqdm pandas numpy scikit-learn openpyxl
The API key is read from the DEEPINFRA_API_KEY environment variable.
"""

# ========================================================================
# Block 1. Libraries
# ========================================================================
from openai import OpenAI
from tqdm import tqdm
import pandas as pd
import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score
import json
import os
import time


# ========================================================================
# Block 2. Provider, model, and API key
# ========================================================================
RESULTS_DIR = "results_populism_baseline"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(base_url="https://api.deepinfra.com/v1/openai",
                api_key=os.environ["DEEPINFRA_API_KEY"])

model_name = "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8"
# model_name = "google/gemma-4-31B-it"
# model_name = "mistralai/Mistral-Small-3.2-24B-Instruct-2506"
# For OpenAI's models: client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
#                      model_name = "gpt-5.5"

n_runs = 3   # a distribution of results, not a single draw (Section 5.2)


# ========================================================================
# Block 3. Data
# ========================================================================
df = pd.read_excel("vanderveen_populism_text_labels.xlsx")
texts = [str(t) for t in df["text"].tolist()]
labels = df["label_main"].tolist()
print(f"Loaded {len(texts)} sentences")


# ========================================================================
# Block 4. The prompt
# ========================================================================
system_prompt = """You are a political text classifier. Your task is to classify \
sentences from US governor and presidential candidate speeches as POPULIST, \
PLURALIST, or NEUTRAL.

This follows the ideational approach to populism, which treats populism as a \
discursive frame built on a Manichean moral struggle between the virtuous \
"people" and the corrupt "elite".

A sentence is POPULIST if it expresses any of the following:
1. Valorization of "the people", the common or ordinary people, or their will
2. Denigration of "the elite", the establishment, or those in power as corrupt \
or self-serving
3. A framing of politics as a moral struggle between the virtuous people and a \
corrupt elite

A sentence is PLURALIST if it expresses the opposite of populism, such as:
1. Politics as legitimate competition or cooperation among diverse groups and \
interests
2. Recognition of the legitimacy of opponents, compromise, or shared institutions
3. Rejection of the idea of a single unified people opposed to a corrupt elite

A sentence is NEUTRAL if it expresses neither populist nor pluralist rhetoric, \
for example ordinary policy, factual, or procedural content.

Respond with exactly one word: POPULIST, PLURALIST, or NEUTRAL. Nothing else."""

# Few-shot prompting: append labeled examples here, after the definitions.


# ========================================================================
# Block 5. Two helper functions
# ========================================================================
class_labels = ["populist", "pluralist", "neutral"]

def parse_label(response):
    r = response.upper().strip()
    if "POPULIST" in r:
        return "populist"
    elif "PLURALIST" in r:
        return "pluralist"
    elif "NEUTRAL" in r:
        return "neutral"
    return -1   # invalid answer: reported, never guessed

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model=model_name,
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


# ========================================================================
# Block 6. A quick test
# ========================================================================
test_response = classify(system_prompt, texts[0])
print(f"Test response: '{test_response}'")
print(f"True label: {labels[0]}")
print(f"Parsed: {parse_label(test_response)}")


# ========================================================================
# Block 7. Three runs, scored one at a time
# ========================================================================
all_preds = pd.DataFrame({"text": texts, "true_label": labels})
run_f1 = []

for run in range(1, n_runs + 1):
    print(f"\n=== Run {run} of {n_runs}: {model_name} ===")
    t0 = time.time()
    raw_responses = [classify(system_prompt, text) for text in tqdm(texts)]
    total_time = time.time() - t0
    print(f"Done in {int(total_time // 60)}m{int(total_time % 60):02d}s")

    preds = [parse_label(r) for r in raw_responses]
    all_preds[f"raw_run{run}"] = raw_responses
    all_preds[f"pred_run{run}"] = preds

    results_df = pd.DataFrame({"text": texts, "true_label": labels,
                               "predicted": preds, "raw_response": raw_responses})
    results_df.to_csv(f"{RESULTS_DIR}/populism_zeroshot_run{run}.csv", index=False)

    valid = results_df[results_df["predicted"] != -1].copy()
    n_invalid = (results_df["predicted"] == -1).sum()

    prec = precision_score(valid["true_label"], valid["predicted"],
                           labels=class_labels, average=None, zero_division=0)
    rec = recall_score(valid["true_label"], valid["predicted"],
                       labels=class_labels, average=None, zero_division=0)
    f1 = f1_score(valid["true_label"], valid["predicted"],
                  labels=class_labels, average=None, zero_division=0)
    f1_macro = f1_score(valid["true_label"], valid["predicted"],
                        labels=class_labels, average="macro", zero_division=0)

    print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
    for i, c in enumerate(class_labels):
        print(f"  {c:<10}-> P: {prec[i]:.3f}  R: {rec[i]:.3f}  F1: {f1[i]:.3f}")
    print(f"  Macro F1: {f1_macro:.3f}")
    run_f1.append(f1_macro)

print(f"\nMacro F1 over {n_runs} runs: mean {np.mean(run_f1):.3f}, "
      f"SD {np.std(run_f1):.3f}")


# ========================================================================
# Block 8. Majority vote across runs
# ========================================================================
majority = []
for i in range(len(texts)):
    votes = []
    for run in range(1, n_runs + 1):
        vote = all_preds.loc[i, f"pred_run{run}"]
        if vote != -1:
            votes.append(vote)
    winner = -1
    for c in class_labels:
        if votes.count(c) > len(votes) / 2:
            winner = c
    majority.append(winner)

all_preds["pred_majority"] = majority
n_unresolved = majority.count(-1)
resolved = all_preds[all_preds["pred_majority"] != -1]
f1_majority = f1_score(resolved["true_label"], resolved["pred_majority"],
                       labels=class_labels, average="macro", zero_division=0)
print(f"Majority vote: macro F1 {f1_majority:.3f} "
      f"(unresolved: {n_unresolved} of {len(texts)})")

all_preds.to_csv(f"{RESULTS_DIR}/populism_zeroshot_predictions.csv", index=False)


# ========================================================================
# Block 9. Saving the metrics
# ========================================================================
metrics = {
    "model": model_name,
    "condition": "prompting_baseline_zeroshot_deepinfra",
    "n_runs": n_runs,
    "f1_macro_mean": round(float(np.mean(run_f1)), 4),
    "f1_macro_sd": round(float(np.std(run_f1)), 4),
    "f1_macro_majority": round(float(f1_majority), 4),
    "n_unresolved": int(n_unresolved),
}
for i, c in enumerate(class_labels):
    metrics[f"prec_{c}"] = round(float(prec[i]), 4)   # last run
    metrics[f"rec_{c}"] = round(float(rec[i]), 4)
    metrics[f"f1_{c}"] = round(float(f1[i]), 4)

with open(f"{RESULTS_DIR}/populism_zeroshot_metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)


