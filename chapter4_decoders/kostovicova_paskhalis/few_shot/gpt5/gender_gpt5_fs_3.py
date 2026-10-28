from openai import OpenAI
from tqdm import tqdm, trange
import pandas as pd
import os
import re
import time
import json
from sklearn.metrics import confusion_matrix, f1_score, recall_score, precision_score, ConfusionMatrixDisplay


# config

RESULTS_DIR = "results_gender_gpt5_fs"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

models = client.models.list()
for model in models:
    print(model.id) ## shows you all available model names. Use these in "model = ..." below.


# load data

df = pd.read_excel("../../../../data/kostovicova_paskhalis/kostovicova_dqi_text_labels.xlsx")
texts = [str(t) for t in df["text"].tolist()]
labels = df["label_main"].tolist()

print(f"Loaded {len(texts)} speech acts")


system_prompt = "You are an expert at political text annotation. Your task is to classify a speech act from a public \
        consultation on transitional justice in the former Yugoslavia (the RECOM process) according to its \
        LEVEL OF JUSTIFICATION, following the Discourse Quality Index (DQI). The speech act is in Serbian/BCS; \
        judge the argumentative structure regardless of language. \
        The level of justification measures how thoroughly a speaker justifies a demand or position (for example, \
        that something should or should not be done, or that a term, article, or procedure should be changed). \
        Use the following 4-level scale: \
        0 (No justification): the speaker makes a demand or states a position but gives no reason for it; mere \
        agreement, disagreement, or assertion. \
        1 (Inferior justification): a reason is given for the demand, but the link between the reason and the \
        demand is incomplete -- the inference is only asserted, mentioned in passing, or left implicit. \
        2 (Qualified justification): one complete justification is given -- the speaker states a reason and makes \
        the linkage explicit, explaining why the reason supports the demand. \
        3 (Sophisticated justification): at least two complete justifications are given -- either two complete \
        reasons for the same demand, or complete reasons for two different demands. \
        Here are some examples: \n \
        Text: Delim misljenje ovo za visoku strucnu spremu od kolege Branka Vorkapica. \n \
        Reasoning: The speaker simply states that he shares a colleague\'s opinion about the higher-qualification \
        requirement. He endorses a position but gives no reason of his own to support it, so no justification is present. \n Answer: 0 \n \
        Text: ili da osoba mora biti diplomirana osoba, jer time mi odbijamo ljude koji su humanisti, a nisu mozda visoko obrazovani. \n \
        Reasoning: The speaker opposes requiring candidates to hold a degree and offers a reason -- that this would \
        exclude people who are humanists but not formally highly educated. A reason is given, but it is asserted in a \
        single clause and the inference is not fully developed, so the justification is inferior. \n Answer: 1 \n \
        Text: Slazem se da su i ratni zlocini krsenja ljudskih prava, ali mislim da je krsenja prava previse siroko. Ja bih stavio krsenja ljudskih prava u nadleznosti komisije, jer krsenja ljudskih prava takodje podrazumevaju i ratne zlocine i genocid i zlocine protiv covecnosti. \n \
        Reasoning: The speaker proposes putting \"human rights violations\" within the commission\'s jurisdiction and gives \
        a complete reason: that this term already encompasses war crimes, genocide, and crimes against humanity. The demand \
        is linked to an explicit, fully articulated reason, forming one complete justification. \n Answer: 2 \n \
        Text: Ja bih mozda menjao ovaj termin naroda posto ce bit konfuzan u termin gradjani. Stav 2. clan 12. Da, u gradjana. Mislim da taj termin cesto  -  narod, puk, nacija  -  politicki atributi i ostale stvari da to cesto moze biti konfuzno. Ovo kad kazemo gradjani, pravno je determinisano pa znamo na sta se odnosi. \n \
        Reasoning: The speaker proposes replacing the term \"narod\" (people) with \"gradjani\" (citizens) and supports it with \
        two complete reasons: first, that \"narod\", \"puk\", and \"nacija\" carry political connotations and are often confusing, \
        and second, that \"gradjani\" is legally defined so its referent is clear. Two complete justifications are given for the same demand. \n \n Answer: 3 \n \
        Now classify the level of justification of the following speech act as 0, 1, 2, or 3. First give your reasoning in 2-3 sentences, then give your final classification on a new line in exactly this format: \n Answer: 0 \n or \n Answer: 1 \n or \n Answer: 2 \n or \n Answer: 3"

class_labels = [0, 1, 2, 3]
level_names = {0: "None", 1: "Inferior", 2: "Qualified", 3: "Sophisticated"}

# helper

def parse_label(response):
    if "Answer:" not in response:
        return -1
    answer = response.split("Answer:")[-1].strip()
    for ch in answer:
        if ch in "0123":
            return int(ch)
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Speech act: "{text}"\n\nLevel:'}
        ],
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
results_df.to_csv(f"{RESULTS_DIR}/gpt5_gender_preds_fs_3.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

prec = precision_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
rec = recall_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1 = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1_macro = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average="macro", zero_division=0)

print(f"\n=== GPT5 Gender ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
for i, c in enumerate(class_labels):
    print(f"  {c} {level_names[c]:<13}-> P: {prec[i]:.3f}  R: {rec[i]:.3f}  F1: {f1[i]:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "openai/gpt-5.5",
    "condition": "prompting_fewshot_openai",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
}
for i, c in enumerate(class_labels):
    metrics[f"prec_{c}"] = round(float(prec[i]), 4)
    metrics[f"rec_{c}"] = round(float(rec[i]), 4)
    metrics[f"f1_{c}"] = round(float(f1[i]), 4)
metrics["f1_macro"] = round(float(f1_macro), 4)

with open(f"{RESULTS_DIR}/gpt5_gender_metrics_fs_3.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
