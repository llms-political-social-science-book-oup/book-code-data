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

data = pd.read_excel("../../../../data/trubowitz_watanabe/trubowitz_gti_text_labels.xlsx")
data.label_main.value_counts()

texts = data.text.tolist()
labels = data.label_main.tolist()
RESULTS_DIR = "results_geothreats_gemma_fs"
os.makedirs(RESULTS_DIR, exist_ok=True)

# examples now go Reasoning -> Answer (reasoning must come before the answer for CoT to work),
# and the model reasons at inference before giving its label
prompt = "You are an expert at political text annotation. Your task is to classify a news article from the \
        New York Times about foreign affairs according to whether it CONVEYS A GEOPOLITICAL THREAT to the \
        United States. The article is a short summary or lead passage, and may be from any period between \
        1861 and 2017. \
        An article CONVEYS A GEOPOLITICAL THREAT if it portrays a foreign country, regime, or actor as hostile, \
        aggressive, or dangerous to the United States or its allies and interests. This includes references to: \
        1. War, invasion, armed conflict, or military attack involving a foreign power \
        2. Military buildup, aggression, expansionism, or hostile threats by a foreign state \
        3. Subversion, terrorism, insurgency, or an adversary\'s hostile intentions or actions \
        4. Hostility or menace directed at the United States, its forces, or its allies \
        Answer 'No' if the article is about foreign affairs but does not convey such a threat, such as diplomacy, \
        cooperation, trade, alliances, cultural matters, or neutral reporting. \
        Answer 'Unclear' if the article is too vague or ambiguous to determine whether a geopolitical threat is conveyed. \
        Here are some examples: \n \
        Text: TAIPEI, Taiwan, Nov. 7 -- Chinese Communist coastal artillery broke a twenty-seven-hour silence at 12:30 A. M. today. Firing fifty-five shells at the Quemoy islands in the predawn hours, the Chinese Reds once more gave notice that their... \n \
        Reasoning: The article reports that Chinese Communist artillery shelled the Quemoy islands, an act of overt military aggression. It portrays a hostile foreign power using force against a defended position, which conveys a clear geopolitical threat. \n Answer: Yes \n \
        Text: Already committed to forming the world\'s largest trading bloc in 1993, the 12-nation European Community took a major step toward economic unity today, agreeing to create a single currency and a regional central bank no later than 1999. \n \
        Reasoning: The article describes the European Community moving toward economic unity with a single currency and a central bank. This is cooperative economic integration among allied states, not a hostile or aggressive act, so it conveys no geopolitical threat. \n Answer: No \n \
        Text: The United States and Britain seemed last week to have settled upon a fresh approach to the Middle Eastern situation. \n \
        Reasoning: The article only states that the United States and Britain have settled on a fresh approach to the Middle East, without describing any hostile actor or aggressive action. There is not enough information to tell whether a foreign threat is involved, so the case is ambiguous. \n Answer: Unclear \n \
        Text: A suicide bomber disguised as an Israeli soldier blew himself apart in Netanya, killing 3 Israelis and wounding more than 50 with a shrapnel-packed bomb. \n \
        Reasoning: The article reports a suicide bombing that killed and wounded many people. This is an act of deadly violence by a hostile actor, which conveys a clear geopolitical threat. \n Answer: Yes \n \
        Text: WASHINGTON, June 24.--Minister Romero, who is very much interested in the postal treaty which he and Postmaster-General Vilas have signed, and which is to take effect in July, talks enthusiastically about the trade benefits it is to confer upon... \n \
        Reasoning: The article concerns a postal treaty and the trade benefits it will bring to both countries. It describes friendly cooperation and mutual economic gain, not hostility, so no geopolitical threat is conveyed. \n Answer: No \n \
        Text: PARIS, June 4 -- The conduct of Premier Khrushchev and his newest disarmament proposals were being subjected to cautious, hard-eyed appraisal in allied diplomatic circles here. \n \
        Reasoning: The article notes that Khrushchev\'s disarmament proposals were being appraised cautiously in allied diplomatic circles, without indicating whether they signal hostility or accommodation. The framing is too tentative to judge, so whether a threat is present is unclear. \n Answer: Unclear \n \
        Text: HONG KONG, Aug. 24--Premier Chou En-lai\'s demand tonight that the United Nations Security Council force the withdrawal of the United States Seventh Fleet from Formosa Strait was part of a double-barreled blast in which the Chinese Communists accused... \n \
        Reasoning: The article reports the Chinese Communists demanding the withdrawal of the U.S. Seventh Fleet and launching what it calls a hostile blast against the United States. This portrays an adversary acting against U.S. interests, conveying a geopolitical threat. \n Answer: Yes \n \
        Text: Evening, A pacific note has been issued from the Prussian Foreign Office, in which the recent note of M, MOUSTTER, the French Foreign Minister, is alluded to as highly satisfactory to the Prussian Government. \n \
        Reasoning: The article describes a \"pacific note\" from the Prussian Foreign Office that treats the French minister\'s note as highly satisfactory. The tone is explicitly conciliatory and friendly, so no geopolitical threat is conveyed. \n Answer: No \n \
        Text: The European Union needs a grand bargain to rescue itself from an accumulation of crises that threaten to blow apart its model of integration. \n \
        Reasoning: The article says the European Union faces crises that \"threaten to blow apart\" its integration, but this refers to internal strains within the bloc rather than a foreign power menacing the United States. Because the threat language is about the EU\'s own cohesion, whether it counts as a geopolitical threat is ambiguous. \n Answer: Unclear \n \
        Text: MIAMI, Sept. 5 -- Gen. Laurence S. Kuter, until recently the Air Force commander in the Far East, described the crisis in Laos today as characteristic of Communist probing efforts throughout Asia. \n \
        Reasoning: The article reports a U.S. commander characterizing the crisis in Laos as part of Communist probing efforts across Asia. It frames a hostile adversary actively pressing in the region, which conveys a geopolitical threat. \n Answer: Yes \n \
        Text: LEAD: Foreign Minister Eduard A. Shevardnadze told the Soviet legislature today that the nine-year Soviet military role in Afghanistan had violated Soviet law and international norms of behavior. \n \
        Reasoning: The article reports a Soviet foreign minister conceding that the Soviet military role in Afghanistan had violated Soviet law and international norms. This is a self-critical admission rather than a portrayal of a foreign power threatening the United States, so no threat is conveyed. \n Answer: No \n \
        Text: The office of Prime Minister Benjamin Netanyahu rejected criticism of Israel\'s plans from President Obama and others. \n \
        Reasoning: The article only states that Netanyahu\'s office rejected criticism of Israel\'s plans from President Obama, describing diplomatic friction without any hostile or aggressive action. There is too little detail to determine whether a geopolitical threat is present, so the case is ambiguous. \n Answer: Unclear \n \
        Text: Prime Minister Wen Jiabao defended a newly approved law that could authorize a military attack to stop Taiwan from pursuing independence. \n \
        Reasoning: The article reports that China approved a law authorizing a military attack to stop Taiwan from pursuing independence. It describes an explicit threat of military force, which conveys a clear geopolitical threat. \n Answer: Yes \n \
        Text: Poland, forever at odds with herself and her place on the map, appears more at peace than she has been since World War II. \n \
        Reasoning: The article characterizes Poland as more at peace than at any time since World War II. It explicitly conveys stability and the absence of conflict, so no geopolitical threat is present. \n Answer: No \n \
        Text: Now that Jean-Claude Duvalier has been forced by the Haitian people to abandon his inherited dictatorship, the United States has an opportunity to improve its policy toward Haiti and help the junta that controls it. \n \
        Reasoning: The article frames the fall of Duvalier as an opportunity for the United States to improve its policy toward Haiti, mentioning the former dictatorship and a controlling junta but not portraying an active foreign threat. Because it is framed around policy opportunity rather than menace, whether a threat is conveyed is ambiguous. \n \n Answer: Unclear \n \
        Now classify the following article as 'Yes', 'No', or 'Unclear'. First give your reasoning in 2-3 sentences, then give your final classification on a new line in exactly this format: \n Answer: Yes \n or \n Answer: No \n or \n Answer: Unclear"


# helper

def parse_label(response):
    if "Answer:" not in response:
        return -1
    answer = response.split("Answer:")[-1].strip().lower()
    if "unclear" in answer:
        return "Unclear"
    elif "yes" in answer:
        return "Yes"
    elif "no" in answer:
        return "No"
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="google/gemma-4-31B-it",
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
from concurrent.futures import ThreadPoolExecutor as _TPE
_W = int(os.environ.get("RERUN_WORKERS", "8"))
def _safe(_t):
    try:
        return classify(prompt, _t)
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
results_df.to_csv(f"{RESULTS_DIR}/gemma_geothreats_preds_fs_1.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

class_labels = ["No", "Yes", "Unclear"]
prec = precision_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
rec = recall_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1 = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1_macro = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average="macro", zero_division=0)

print(f"\n=== Gemma Geopolitical Threats ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
for i, c in enumerate(class_labels):
    print(f"  {c:<8}-> P: {prec[i]:.3f}  R: {rec[i]:.3f}  F1: {f1[i]:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "google/gemma-4-31B-it",
    "condition": "prompting_fewshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
    "prec_no": round(float(prec[0]), 4),
    "rec_no": round(float(rec[0]), 4),
    "f1_no": round(float(f1[0]), 4),
    "prec_yes": round(float(prec[1]), 4),
    "rec_yes": round(float(rec[1]), 4),
    "f1_yes": round(float(f1[1]), 4),
    "prec_unclear": round(float(prec[2]), 4),
    "rec_unclear": round(float(rec[2]), 4),
    "f1_unclear": round(float(f1[2]), 4),
    "f1_macro": round(float(f1_macro), 4)
}

with open(f"{RESULTS_DIR}/gemma_geothreats_metrics_fs_1.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
