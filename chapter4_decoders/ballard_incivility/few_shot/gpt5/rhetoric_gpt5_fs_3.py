from openai import OpenAI
from tqdm import tqdm, trange
import pandas as pd
import os
import re
import time
import json
from sklearn.metrics import confusion_matrix, f1_score, recall_score, precision_score, ConfusionMatrixDisplay


# config

RESULTS_DIR = "results_rhetoric_gpt5_fs"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"], max_retries=8, timeout=120)

models = client.models.list()
for model in models:
    print(model.id) ## shows you all available model names. Use these in "model = ..." below.


# load data

df = pd.read_excel("../../../../data/ballard_incivility/incivility_tweets_text_labels.xlsx")
df = df[df["label_main"].isin([0, 1])].reset_index(drop=True)
texts = [str(t) for t in df["text"].tolist()]
labels = df["label_main"].tolist()

print(f"Loaded {len(texts)} tweets")

system_prompt = 'You are an expert at political text annotation. Your task is to classify tweets from members of the US Congress as either CIVIL or UNCIVIL.\n\nA tweet is UNCIVIL if it contains any of the following:\n1. Name-calling, mockery, sarcasm, or character assassination\n2. Spin or misrepresentative exaggeration\n3. Emotionality or digital stridency\n4. Conspiracy theory\n\nA tweet is CIVIL if it does not contain any of the above. Note that strong policy disagreement, criticism of legislation, or negative characterizations of policy outcomes are NOT uncivil unless they involve personal attacks, mockery, or deliberate distortion.\n\nHere are some examples: \n         Text: Rick Santorum has said many dumb things but I think this one may rank in the top 10. So proud my state booted him out of office by 20 points. \n         Reasoning: The tweet calls a named politician\'s statements "dumb things" and gloats that the state booted him out of office. This uses ridicule and derogatory characterization of an individual rather than substantive engagement, which makes it uncivil. \n Answer: uncivil \n         Text: #Renewables are critical for future - #fossilfuels are finite! I applaud the President on #energy strategy that leads, not follows. #SOTU \n         Reasoning: The tweet states a policy position on renewable energy and praises the President\'s energy strategy. It advocates respectfully and even commends an official, with no insulting or demeaning language, so it is civil. \n Answer: civil \n         Text: Another ploy of desperate Democrats trying to change the subject from Obamacare and push populist politics ahead \n         Reasoning: The tweet dismisses the opposing party as desperate Democrats engaged in a ploy, attributing bad faith through derogatory labeling. This contemptuous characterization of a group is uncivil. \n Answer: uncivil \n         Text: Right now there are a lot of people whose rights are threatened by the Trump administration. We must work together to protect them. \n         Reasoning: The tweet voices concern that some people\'s rights are threatened and calls for working together to protect them. It is critical of the administration but expressed respectfully and constructively, so it is civil. \n Answer: civil \n         Text: Repeal & replace = scam & sham! Ask Trump\'s @GOP #WhatsYourPlan \n         Reasoning: The tweet mocks the policy as a "scam & sham" and tags opponents derisively. The jeering, contemptuous framing attacks rather than argues, which makes it uncivil. \n Answer: uncivil \n         Text: Common sense: if you are too dangerous to fly, you\'re too dangerous to buy weapons of war. Need bipartisan bill 2 make #NoFlyNoBuy a reality \n         Reasoning: The tweet makes a gun-policy argument and calls for a bipartisan bill. It states a position and even seeks cooperation across parties without any insulting language, so it is civil. \n Answer: civil \n         Text: Leave my family out of it Sen. McCain. Your blood relatives may approve of this Congress but mine are smarter than that \n         Reasoning: The tweet tells Senator McCain to leave the speaker\'s family alone and jabs that the speaker\'s relatives are smarter than that. The personal, belittling dig at the senator makes it uncivil. \n Answer: uncivil \n         Text: #GOP budget - ends Medicare guarantee for seniors and slashes care for seniors in nursing homes. \n         Reasoning: The tweet criticizes a budget proposal for ending the Medicare guarantee and cutting care for seniors. It is a pointed but substantive policy criticism with no personal insults or demeaning language, so it is civil. \n Answer: civil \n         Text: Dewhurst doubling-down on deceiving TX voters w/ another shameless distortion of facts. Read & RT the truth: #TXSen \n         Reasoning: The tweet accuses a named candidate of deceiving voters with a "shameless distortion of facts." Framing an opponent as shamelessly dishonest is a personal character attack, which makes it uncivil. \n Answer: uncivil \n         Text: Americans suffer when members of Congress fail to respect local control, limited government, and personal freedom. #COPolitics \n         Reasoning: The tweet argues that Americans suffer when Congress fails to respect local control, limited government, and personal freedom. It states a values-based critique in respectful terms without attacking anyone, so it is civil. \n \n Answer: civil \n         Now classify the following tweet as \'civil\' or \'uncivil\'. First give your reasoning in 2-3 sentences, then give your final classification on a new line in exactly this format: \n Answer: civil \n or \n Answer: uncivil'


# helper

def parse_label(response):
    if "Answer:" not in response:
        return -1
    answer = response.split("Answer:")[-1].strip().lower()
    if "incivil" in answer or "uncivil" in answer:
        return 1
    elif "civil" in answer:
        return 0
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Tweet: "{text}"\n\nClassification:'}
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
with _TPE(max_workers=_W) as _ex:
    raw_responses = list(tqdm(_ex.map(_safe, texts), total=len(texts)))
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
results_df.to_csv(f"{RESULTS_DIR}/gpt5_rhetoric_preds_fs_3.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

f1_civil = f1_score(valid["true_label"], valid["predicted"], pos_label=0)
f1_incivil = f1_score(valid["true_label"], valid["predicted"], pos_label=1)
f1_macro = f1_score(valid["true_label"], valid["predicted"], average="macro")
prec_civil = precision_score(valid["true_label"], valid["predicted"], pos_label=0)
rec_civil = recall_score(valid["true_label"], valid["predicted"], pos_label=0)
prec_incivil = precision_score(valid["true_label"], valid["predicted"], pos_label=1)
rec_incivil = recall_score(valid["true_label"], valid["predicted"], pos_label=1)

print(f"\n=== GPT5 Rhetoric ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
print(f"  Civil     -> P: {prec_civil:.3f}  R: {rec_civil:.3f}  F1: {f1_civil:.3f}")
print(f"  Incivil   -> P: {prec_incivil:.3f}  R: {rec_incivil:.3f}  F1: {f1_incivil:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "openai/gpt-5.5",
    "condition": "prompting_fewshot_openai",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
    "prec_civil": round(prec_civil, 4),
    "rec_civil": round(rec_civil, 4),
    "f1_civil": round(f1_civil, 4),
    "prec_incivil": round(prec_incivil, 4),
    "rec_incivil": round(rec_incivil, 4),
    "f1_incivil": round(f1_incivil, 4),
    "f1_macro": round(f1_macro, 4)
}

with open(f"{RESULTS_DIR}/gpt5_rhetoric_metrics_fs_3.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
