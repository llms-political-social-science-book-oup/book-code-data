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

data = pd.read_excel("../../../../data/vanderveen_populism/vanderveen_populism_text_labels.xlsx")
data.label_main.value_counts()

texts = data.text.tolist()
labels = data.label_main.tolist()
RESULTS_DIR = "results_populism_gemma_fs"
os.makedirs(RESULTS_DIR, exist_ok=True)

# examples now go Reasoning -> Answer (reasoning must come before the answer for CoT to work),
# and the model reasons at inference before giving its label
prompt = "You are an expert at political text annotation. Your task is to classify a sentence from an American political speech (by a U.S. state governor or presidential candidate) as POPULIST, PLURALIST, or NEUTRAL, based on the kind of language it uses. Populist: the sentence frames politics as a moral struggle between a virtuous, unified 'the people' and a corrupt, self-serving elite or establishment -- praising the will of ordinary people and/or attacking elites, the government, the media, or political opponents as betraying or exploiting the people. Pluralist: the sentence expresses the opposite -- it embraces diversity, compromise, and cooperation across different groups, recognizes the legitimacy of disagreement and multiple interests, and calls for working together (for example, across parties) rather than dividing the people against an enemy. Neutral: the sentence is neither populist nor pluralist -- ordinary descriptive, factual, or policy language with no us-versus-them framing and no emphasis on diversity or cooperation. \
        Here are some examples: \n \
        Text: The people have spoken and a new direction has been decided \n \
        Reasoning: The sentence invokes \"the people\" as a unified body whose collective voice has decided the way forward. This appeal to the will of the ordinary people is a hallmark of populist language. \n Answer: Populist \n \
        Text: I know Washingtonians, and I know what we are capable of doing when we work together \n \
        Reasoning: The sentence emphasizes what people can accomplish when they work together. Stressing cooperation rather than division is pluralist. \n Answer: Pluralist \n \
        Text: Our reserves are up, our exports are up, our state GDP is up \n \
        Reasoning: The sentence simply reports that reserves, exports, and state GDP are all up. It is a factual statement with no us-versus-them framing and no appeal to diversity or cooperation, so it is neutral. \n Answer: Neutral \n \
        Text: And when I'm governor, we're going to clean up Jefferson City \n \
        Reasoning: The speaker promises to clean up the state capital, casting the political establishment there as corrupt and in need of being purged on behalf of the people. This anti-establishment framing is populist. \n Answer: Populist \n \
        Text: May we never forget however that are honest disagreements and our freedom to express them are the essential rights and the great strengths of our great democracy \n \
        Reasoning: The sentence celebrates honest disagreement and the freedom to express it as essential rights and strengths of democracy. Valuing diversity of views and legitimate disagreement is the essence of pluralism. \n Answer: Pluralist \n \
        Text: Three years ago, I promised Delawareans that at the end of my term, our economy would be stronger \n \
        Reasoning: The sentence recounts a past promise that the economy would be stronger by the end of the term. It is ordinary descriptive language without populist or pluralist framing, so it is neutral. \n Answer: Neutral \n \
        Text: Instead government has taken more and more of our family's hard working income away to serve some people's political and/or financial self interests \n \
        Reasoning: The sentence accuses the government of taking hardworking families' income to serve elites' political and financial self-interest. Pitting ordinary, hardworking people against a self-serving elite is classic populist language. \n Answer: Populist \n \
        Text: Let's work together on a bipartisan basis to put in place common-sense solutions that are sustainable: by adapting best practices that work and by innovating to find new approaches that fit Iowa \n \
        Reasoning: The speaker calls for working together on a bipartisan basis to find sustainable, common-sense solutions. This appeal to cross-party cooperation and compromise is pluralist. \n Answer: Pluralist \n \
        Text: In the last six years the accomplishments of this system are very, very impressive \n \
        Reasoning: The sentence describes the accomplishments of a system over six years as very impressive. This is plain evaluative description with neither populist nor pluralist content, so it is neutral. \n Answer: Neutral \n \
        Text: It is nothing but a dog and pony show for the media \n \
        Reasoning: The sentence dismisses something as a staged \"dog and pony show for the media,\" portraying the establishment and press as putting on a cynical performance. This contemptuous anti-elite framing is populist. \n Answer: Populist \n \
        Text: the question ultimately comes down to though who can take us to where we collectively want to go Republicans, Democrats, independents alike \n \
        Reasoning: The sentence frames the goal as where the speaker says we collectively want to go, including Republicans, Democrats, and independents alike. Embracing all political groups together is pluralist. \n Answer: Pluralist \n \
        Text: People across America are watching Arizona, seeing how we implement this law, ready to jump on even the slightest misstep \n \
        Reasoning: The sentence observes that people across America are watching how Arizona implements a law. It is a descriptive observation with no people-versus-elite framing and no emphasis on cooperation, so it is neutral. \n Answer: Neutral \n \
        Text: But the most devastating thing they have tried to do is redefine the American Dream \n \
        Reasoning: The sentence casts an undefined \"they\" as having tried to do something devastating -- redefining the American Dream -- setting an elite enemy against the people's shared values. This us-versus-them framing is populist. \n Answer: Populist \n \
        Text: Rather, there is a very clear realization that we are all in this together, and an equally clear commitment to going our own way, in our own time, and within our own means \n \
        Reasoning: The sentence stresses that we are all in this together while respecting that each can go their own way in their own time. Combining shared purpose with respect for differences is pluralist. \n Answer: Pluralist \n \
        Text: Its members are executives and business leaders who live and work in Nebraska \n \
        Reasoning: The sentence factually describes a group's members as executives and business leaders who live and work in Nebraska. This is purely descriptive with no populist or pluralist framing, so it is neutral. \n Answer: Neutral \n \
        Now classify the following sentence as 'Populist', 'Pluralist', or 'Neutral'. First give your reasoning in 1-2 sentences, then give your final classification on a new line in exactly this format: \\n Answer: Populist \\n or \\n Answer: Pluralist \\n or \\n Answer: Neutral"


# helper

def parse_label(response):
    if "Answer:" not in response:
        return -1
    answer = response.split("Answer:")[-1].strip().lower()
    if "populist" in answer:
        return "populist"
    elif "pluralist" in answer:
        return "pluralist"
    elif "neutral" in answer:
        return "neutral"
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
results_df.to_csv(f"{RESULTS_DIR}/gemma_populism_preds_fs_1.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

class_labels = ["populist", "pluralist", "neutral"]
prec = precision_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
rec = recall_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1 = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1_macro = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average="macro", zero_division=0)

print(f"\n=== Gemma Populism ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
for i, c in enumerate(class_labels):
    print(f"  {c:<10}-> P: {prec[i]:.3f}  R: {rec[i]:.3f}  F1: {f1[i]:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "google/gemma-4-31B-it",
    "condition": "prompting_fewshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
    "prec_populist": round(float(prec[0]), 4),
    "rec_populist": round(float(rec[0]), 4),
    "f1_populist": round(float(f1[0]), 4),
    "prec_pluralist": round(float(prec[1]), 4),
    "rec_pluralist": round(float(rec[1]), 4),
    "f1_pluralist": round(float(f1[1]), 4),
    "prec_neutral": round(float(prec[2]), 4),
    "rec_neutral": round(float(rec[2]), 4),
    "f1_neutral": round(float(f1[2]), 4),
    "f1_macro": round(float(f1_macro), 4)
}

with open(f"{RESULTS_DIR}/gemma_populism_metrics_fs_1.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
