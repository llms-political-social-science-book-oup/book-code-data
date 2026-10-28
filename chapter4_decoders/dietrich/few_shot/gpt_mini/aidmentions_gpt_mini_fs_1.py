from openai import OpenAI
from tqdm import tqdm, trange
import pandas as pd
import os
import re
import time
import json
from sklearn.metrics import confusion_matrix, f1_score, recall_score, precision_score, ConfusionMatrixDisplay


# config

RESULTS_DIR = "results_aidmentions_gpt_mini_fs"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"], max_retries=8, timeout=120) 

models = client.models.list()
for model in models:
    print(model.id) ## shows you all available model names. Use these in "model = ..." below.


# load data

df = pd.read_excel("../../../../data/dietrich/dietrich_aidmentions_text_labels.xlsx")
texts = [str(t) for t in df["text"].tolist()]
labels = df["label_main"].tolist()

print(f"Loaded {len(texts)} sentences")

system_prompt = "You are an expert at political text annotation. Your task is to classify a sentence from a \
        party election manifesto according to whether it MENTIONS FOREIGN AID. \
        The sentence may be in any language, since these manifestos come from 13 donor democracies in their \
        original languages. Judge the meaning regardless of language.\
        A sentence MENTIONS FOREIGN AID if it refers to foreign aid or official development assistance given \
        by a donor government to other, developing, or poor countries. This includes references to: \
        1. Foreign aid, development aid, development assistance, or development cooperation \
        2. Financial, technical, humanitarian, or food assistance to developing or poor countries \
        3. Aid budgets, aid spending, or aid agencies and ministries for development cooperation \
        4. Commitments or targets for giving aid (e.g., the 0.7% of GNI target) \
        Here are some examples: \n \
        Text: We will make aid more effective, work more closely with non-governmental agencies, put women at the heart of our programme and, in co-ordination with other donors, reduce the share of tied aid. \n \
        Reasoning: The sentence is explicitly about the donor government\'s aid programme, pledging to make aid more effective, coordinate with other donors, and reduce the share of tied aid. \
        References to aid, other donors, and tied aid place it squarely within development assistance policy. This is a direct mention of foreign aid. \n Answer: aid \n \
        Text: We welcome the emerging new nations of Africa to the world community. \n \
        Reasoning: The sentence expresses diplomatic recognition and welcome toward newly emerging African nations joining the international community. It concerns foreign relations and recognition \
        rather than the provision of financial, technical, or development assistance. No aid budget, aid programme, or development cooperation is referenced. \n Answer: no_aid \n \
        Text: Our aid is still small and largely confined to New Guinea. \n \
        Reasoning: The sentence comments directly on the size and geographic concentration of the donor\'s aid programme, noting it remains small and largely confined to New Guinea. \
        The explicit reference to our aid given to a recipient territory identifies it as foreign aid. This is a clear aid mention. \n Answer: aid \n \
        Text: In regional security we are firmly committed to closer defence relations with Australia, to the Five Power Defence Arrangement and the ASEAN Regional Forum. \n \
        Reasoning: The sentence describes defence and security cooperation through alliances such as the Five Power Defence Arrangement and the ASEAN Regional Forum. It concerns military and strategic \
        relationships, not financial, technical, or humanitarian assistance to developing countries. No development aid or aid spending is mentioned. \n Answer: no_aid \n \
        Text: This aid will be aimed at promoting renewable energy and surtainable agriculture projects. \n \
        Reasoning: The sentence specifies how aid will be directed, targeting renewable energy and sustainable agriculture projects. The explicit mention of aid funding development projects identifies \
        it as development assistance. This is a direct mention of foreign aid. \n Answer: aid \n \
        Text: We need to rebuild Canada\'s crumbling highway system, and especially develop trade corridors linking Canada with our NAFTA partners, the United States and Mexico. \n \
        Reasoning: The sentence addresses domestic infrastructure and the development of trade corridors with NAFTA partners. Although it uses the word develop, it refers to commercial trade routes \
        and highways at home, not assistance given to developing or poor countries. No foreign aid or development cooperation is involved. \n Answer: no_aid \n \
        Text: The position of the world\'s largest contributor is well within our grasp, involving an increase to approximately 1% of GNP. \n \
        Reasoning: In the context of development cooperation, the sentence frames the country as an aid contributor and sets a target of raising contributions to about 1% of GNP. This references a \
        commitment to an aid-spending target measured as a share of national income, comparable to the GNI aid targets. It therefore mentions foreign aid. \n Answer: aid \n \
        Text: It also allows for the setting up of the Political and Security Committee, the EU Military Committee and the EU Military Staff Organisation to run this force. \n \
        Reasoning: The sentence concerns the creation of EU political, security, and military bodies to operate a military force. It is about defence and security institutions rather than financial, \
        technical, or humanitarian assistance to developing countries. No aid budget or development cooperation is referenced. \n Answer: no_aid \n \
        Text: Die Schaffung marktwirtschaftlicher Strukturen muss zur vorrangigen Aufgabe öffentlicher Entwicklungshilfe werden. \n \
        Reasoning: The German sentence states that creating market-economy structures must become a priority task of public development aid (\"öffentliche Entwicklungshilfe\"). The explicit reference \
        to official, public development assistance identifies it as a foreign aid mention. The meaning is clear regardless of language. \n Answer: aid \n \
        Text: EUROPOL muss als Kompetenzzentrum für Informationen und koordinierende Unterstützung weiter entwickelt werden. \n \
        Reasoning: The German sentence calls for EUROPOL to be further developed as a competence centre for information and coordinating support. Although it uses the words support (\"Unterstützung\") \
        and developed (\"entwickelt\"), it refers to European police cooperation and internal security, not development assistance to poor or developing countries. It is therefore not an aid mention. \n \n Answer: no_aid \n \
        Now classify the following sentence as 'aid' or 'no_aid'. First give your reasoning in 2-3 sentences, then give your final classification on a new line in exactly this format: \n Answer: aid \n or \n Answer: no_aid"


# helper

def parse_label(response):
    if "Answer:" not in response:
        return -1
    answer = response.split("Answer:")[-1].strip().lower()
    if "no_aid" in answer or "no aid" in answer:
        return 0
    elif "aid" in answer:
        return 1
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Sentence: "{text}"\n\nClassification:'}
        ],
    )
    return response.choices[0].message.content.strip()

# quick test

test_response = classify(system_prompt, texts[0])
print(f"Test response: '{test_response}'")
print(f"True label: {labels[0]}")
print(f"Parsed: {parse_label(test_response)}")

# run classification on all sentences

t0 = time.time()
# --- resumable checkpoint (added: survive API errors without losing progress) ---
import json as _json
_ckpt = f"{RESULTS_DIR}/_ckpt_raw.jsonl"
raw_responses = []
if os.path.exists(_ckpt):
    with open(_ckpt, encoding="utf-8") as _f:
        raw_responses = [_json.loads(_l)["r"] for _l in _f if _l.strip()]
_done = len(raw_responses)
if _done:
    print(f"resuming from {_done}/{len(texts)}")
from concurrent.futures import ThreadPoolExecutor as _TPE
_W = int(os.environ.get("RERUN_WORKERS", "8"))
def _safe(_t):
    try:
        return classify(system_prompt, _t)
    except Exception as _e:
        _m = str(_e).lower()
        if any(k in _m for k in ("authenticat","invalid_api_key","insufficient_quota","exceeded your current quota","billing","no such model","does not exist","model_not_found","401","account is not active")):
            raise
        return ""
with _TPE(max_workers=_W) as _ex, open(_ckpt, "a", encoding="utf-8") as _f:
    for _r in tqdm(_ex.map(_safe, texts[_done:]), total=len(texts)-_done):
        raw_responses.append(_r)
        _f.write(_json.dumps({"r": _r}) + "\n"); _f.flush()
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
results_df.to_csv(f"{RESULTS_DIR}/gpt_mini_aidmentions_preds_fs_1.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

f1_no = f1_score(valid["true_label"], valid["predicted"], pos_label=0)
f1_yes = f1_score(valid["true_label"], valid["predicted"], pos_label=1)
f1_macro = f1_score(valid["true_label"], valid["predicted"], average="macro")
prec_no = precision_score(valid["true_label"], valid["predicted"], pos_label=0)
rec_no = recall_score(valid["true_label"], valid["predicted"], pos_label=0)
prec_yes = precision_score(valid["true_label"], valid["predicted"], pos_label=1)
rec_yes = recall_score(valid["true_label"], valid["predicted"], pos_label=1)

print(f"\n=== GPT Mini Aid Mentions ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
print(f"  No aid (0)        -> P: {prec_no:.3f}  R: {rec_no:.3f}  F1: {f1_no:.3f}")
print(f"  Aid mention (1)   -> P: {prec_yes:.3f}  R: {rec_yes:.3f}  F1: {f1_yes:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "openai/gpt-5.4-mini",
    "condition": "prompting_fewshot_openai",
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

with open(f"{RESULTS_DIR}/gpt_mini_aidmentions_metrics_fs_1.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
