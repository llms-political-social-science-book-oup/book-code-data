from openai import OpenAI
from tqdm import tqdm, trange
import pandas as pd
import os
import re
import time
import json
from sklearn.metrics import confusion_matrix, f1_score, recall_score, precision_score, ConfusionMatrixDisplay


client = OpenAI(
    base_url="https://api.deepinfra.com/v1/openai",
    api_key=os.environ["DEEPINFRA_API_KEY"],
    max_retries=8
)

data = pd.read_excel("../../../../data/kostovicova_paskhalis/kostovicova_dqi_text_labels.xlsx")
data.label_main.value_counts()

texts = data.text.tolist()
labels = data.label_main.tolist()
RESULTS_DIR = "results_gender_llama_fs"
os.makedirs(RESULTS_DIR, exist_ok=True)

# examples now go Reasoning -> Answer (reasoning must come before the answer for CoT to work),
# and the model reasons at inference before giving its label
prompt = "You are an expert at political text annotation. Your task is to classify a speech act from a public \
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


# helper

def parse_label(response):
    if "Answer:" not in response:
        return -1
    seg = response.split("Answer:")[-1]
    m = re.findall(r"[0-3]", seg)
    if not m:
        m = re.findall(r"[0-3]", response)
    if not m:
        return -1
    return int(m[0])

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f'Sentence: "{text}"\n\nClassification:'}
        ],
        temperature=0,
        #max_tokens=10,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].message.content.strip()

# quick test

test_response = classify(prompt, texts[0])
print(f"Test response: '{test_response.split('Answer: ')[1]}'")
print(f"True label: {labels[0]}")
print(f"Parsed: {parse_label(test_response)}")

# run classification on all sentences

t0 = time.time()
raw_responses = [classify(prompt, text) for text in tqdm(texts)]
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
results_df.to_csv(f"{RESULTS_DIR}/llama_gender_preds_fs_2.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

class_labels = [0, 1, 2, 3]
prec = precision_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
rec = recall_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1 = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1_macro = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average="macro", zero_division=0)

print(f"\n=== Llama Gender ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
for i, c in enumerate(class_labels):
    print(f"  Level {c} -> P: {prec[i]:.3f}  R: {rec[i]:.3f}  F1: {f1[i]:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    "condition": "prompting_zeroshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
    "prec_0": round(float(prec[0]), 4),
    "rec_0": round(float(rec[0]), 4),
    "f1_0": round(float(f1[0]), 4),
    "prec_1": round(float(prec[1]), 4),
    "rec_1": round(float(rec[1]), 4),
    "f1_1": round(float(f1[1]), 4),
    "prec_2": round(float(prec[2]), 4),
    "rec_2": round(float(rec[2]), 4),
    "f1_2": round(float(f1[2]), 4),
    "prec_3": round(float(prec[3]), 4),
    "rec_3": round(float(rec[3]), 4),
    "f1_3": round(float(f1[3]), 4),
    "f1_macro": round(float(f1_macro), 4)
}

with open(f"{RESULTS_DIR}/llama_gender_metrics_fs_2.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
