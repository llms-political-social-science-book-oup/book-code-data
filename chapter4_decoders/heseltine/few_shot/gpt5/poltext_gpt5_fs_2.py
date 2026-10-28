from openai import OpenAI
from tqdm import tqdm, trange
import pandas as pd
import os
import re
import time
import json
from sklearn.metrics import confusion_matrix, f1_score, recall_score, precision_score, ConfusionMatrixDisplay


# config

RESULTS_DIR = "results_poltext_gpt5_fs"
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

system_prompt = "You are an expert at political text annotation. Your task is to classify whether a political text \
        conveys NEGATIVE messaging or not. The text is a tweet from a politician (in the United States, Germany, \
        Chile, or Italy) or a U.S. news-media article, and it may be in English, German, Spanish, or Italian -- \
        judge the messaging regardless of language. \
        A text contains NEGATIVE messaging if it expresses negativity -- for example, criticism, attacks, blame, \
        complaints, outrage, or other hostile or disapproving language toward a person, group, party, policy, or \
        event. A text is NOT NEGATIVE if its messaging is neutral (e.g., factual or informational) or positive \
        (e.g., praise, support, celebration, or good news). \
        Classify the text as 'Negative' or 'Not negative'. \
        Here are some examples: \n \
        Text: On @570KLIF: Courts have ruled that #POTUS has abused his executive authority time and time again. \n \
        Reasoning: The tweet criticizes the President, asserting that courts have repeatedly found he \"abused his executive authority.\" This is a clear attack on a political figure, so it conveys negative messaging. \n Answer: Negative \n \
        Text: Big news #KCMO will host the 2019 USA Gymnastics Championships for the first time since 1987 \n \
        Reasoning: The tweet shares upbeat news that the city will host a national gymnastics championship for the first time since 1987. The celebratory, good-news tone contains no negativity. \n Answer: Not negative \n \
        Text: RT @SenBooker: .@CoryBooker slams Trump's 'all-out assault' on LGBTQ Americans: \n \
        Reasoning: The tweet amplifies a senator who \"slams\" what he calls an \"all-out assault\" on LGBTQ Americans. The hostile, accusatory framing toward the administration is negative messaging. \n Answer: Negative \n \
        Text: The fight against HIV/AIDS must continue. Prevention + care will help create #healthiestgeneration ever #WAD2014 \n \
        Reasoning: Although the tweet mentions the \"fight\" against HIV/AIDS, its message is hopeful and constructive -- prevention and care will help create the healthiest generation ever. It promotes a positive cause rather than attacking anyone, so it is not negative. \n Answer: Not negative \n \
        Text: Der zuständige Minister fordert bessere Bedingungen oder Bezahlung, wäre sein Job das JETZT zu tun. Stattdessen: Personalbemessung vertagt. \n \
        Reasoning: The German tweet criticizes the responsible minister for failing to act -- noting that instead of doing his job now, the staffing decision was postponed. This reproachful tone toward a politician is negative messaging. \n Answer: Negative \n \
        Text: Wie kann man die kleinen Kneipen im ländlichen Raum erhalten? Heute diskutiere ich in Gaugrehweiler mit... \n \
        Reasoning: The German tweet poses a constructive question about preserving small rural pubs and announces a discussion event. It is neutral and informational, with no negative messaging. \n Answer: Not negative \n \
        Text: @Azkintuwe @sebastian_gray Son una vergüenza, pienses lo que pienses nadie puede negar que la extrema derecha de patria y libertad fue sádica, inhumana y aprovechadora \n \
        Reasoning: The Spanish-language tweet calls the far right \"una vergüenza\" (a disgrace) and describes it as \"sádica, inhumana y aprovechadora\" (sadistic, inhuman, and exploitative). This is strongly hostile, condemnatory language, so it conveys negative messaging. \n Answer: Negative \n \
        Text: Muy bien el Senado aprobando la ley de tenencia responsable de mascotas, 12 modificaciones q contribuyen a cuidar a nuestros fieles amigos \n \
        Reasoning: The Spanish-language tweet praises the Senate (\"Muy bien\") for approving a responsible pet-ownership law that helps care for animals. The approving, positive tone contains no negativity. \n Answer: Not negative \n \
        Text: Il #Senato di #Renzi riduce la #democrazia perché abolisce il #voto dei #cittadini! #Referendum #iovotoNO \n \
        Reasoning: The Italian tweet attacks Renzi's Senate reform, claiming it \"reduces democracy\" by abolishing citizens' vote, and urges a No vote. The critical, oppositional framing is negative messaging. \n Answer: Negative \n \
        Text: Piemonte al primo posto per la qualità delle prestazioni sanitarie - La voce di Novara \n \
        Reasoning: The Italian tweet reports the positive news that Piedmont ranks first for the quality of its healthcare services. This is favorable, neutral-to-positive reporting with no negative messaging. \n \n Answer: Not negative \n \
        Now classify whether the following political text conveys negative messaging. First give your reasoning in 2-3 sentences, then give your final classification on a new line in exactly this format: \n Answer: Negative \n or \n Answer: Not negative"


# helper

def parse_label(response):
    if "Answer:" not in response:
        return -1
    answer = response.split("Answer:")[-1].strip().upper()
    if "NOT NEGATIVE" in answer or "NOTNEGATIVE" in answer or "NON-NEGATIVE" in answer:
        return 0
    elif "NEGATIVE" in answer:
        return 1
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Text: "{text}"\n\nClassification:'}
        ],
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
results_df.to_csv(f"{RESULTS_DIR}/gpt5_poltext_preds_fs_2.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

f1_notnegative = f1_score(valid["true_label"], valid["predicted"], pos_label=0)
f1_negative = f1_score(valid["true_label"], valid["predicted"], pos_label=1)
f1_macro = f1_score(valid["true_label"], valid["predicted"], average="macro")
prec_notnegative = precision_score(valid["true_label"], valid["predicted"], pos_label=0)
rec_notnegative = recall_score(valid["true_label"], valid["predicted"], pos_label=0)
prec_negative = precision_score(valid["true_label"], valid["predicted"], pos_label=1)
rec_negative = recall_score(valid["true_label"], valid["predicted"], pos_label=1)

print(f"\n=== GPT5 Political Text ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
print(f"  Notnegative -> P: {prec_notnegative:.3f}  R: {rec_notnegative:.3f}  F1: {f1_notnegative:.3f}")
print(f"  Negative    -> P: {prec_negative:.3f}  R: {rec_negative:.3f}  F1: {f1_negative:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "openai/gpt-5.5",
    "condition": "prompting_fewshot_openai",
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

with open(f"{RESULTS_DIR}/gpt5_poltext_metrics_fs_2.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
