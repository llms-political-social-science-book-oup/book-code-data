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

data = pd.read_excel("../../../../data/erhard_popbert/popbert_text_labels.xlsx")
data.label_main.value_counts()

texts = data.text.tolist()
labels = data.label_main.tolist()
RESULTS_DIR = "results_popbert_llama_fs"
os.makedirs(RESULTS_DIR, exist_ok=True)

# examples now go Reasoning -> Answer (reasoning must come before the answer for CoT to work),
# and the model reasons at inference before giving its label
prompt = "You are an expert at political text annotation. Your task is to classify whether a sentence from a \
        speech in the German Bundestag conveys POPULISM, following the ideational approach. The sentence is in \
        German -- judge the content regardless of language. A sentence is POPULIST if it expresses either of the \
        two core populist dimensions: \
        (1) Anti-elitism: it criticizes or blames \"the elite\" -- such as the government, established parties, \
        the EU/Brussels, lobbies, or the powerful -- portraying them as corrupt, self-serving, or acting against \
        the interests of ordinary people. \
        (2) People-centrism: it appeals to \"the people\" -- das Volk, the citizens, taxpayers, ordinary \
        hardworking people -- as a homogeneous, virtuous group whose will or interests should be sovereign. \
        A sentence is NOT POPULIST if it shows neither dimension -- for example, ordinary policy, factual, or \
        procedural statements, even when they criticize a specific actor on grounds other than being a corrupt elite. \
        Classify the sentence as 'Populist' or 'Not populist'. \
        Here are some examples: \n \
        Text: Die Bundesregierung muss endlich aufhören, sich beim Klimaschutz selbst im Weg zu stehen und immer wieder vor der Industrielobby einzuknicken. \n \
        Reasoning: The sentence attacks the federal government for repeatedly caving to the \"industry lobby\" on climate protection. By blaming the governing elite for serving lobby interests, it expresses anti-elitism, a core populist dimension, so it is populist. \n Answer: Populist \n \
        Text: Die SPD-Bundestagsfraktion hat ihre Hausaufgaben gemacht und zeigt den politischen Willen, zu einer zügigen Lösung in Sachen Wahlrechtsreform zu kommen. \n \
        Reasoning: The sentence simply states that the SPD parliamentary group has done its work and wants a swift solution on electoral reform. It is ordinary parliamentary self-description with no attack on an elite and no appeal to the virtuous people, so it is not populist. \n Answer: Not populist \n \
        Text: Aber Sie wollen eben was ganz anders – klassisch Altparteien! –: Sie wollen massive Eingriffe in die Meinungsfreiheit. \n \
        Reasoning: The sentence derides the established parties (\"klassisch Altparteien\") and accuses them of wanting to massively curtail free speech. This moralized attack on the political establishment is anti-elitism, so it is populist. \n Answer: Populist \n \
        Text: Die neuen Freibeträge beim Wohngeld und für die gesetzliche Rente bei der Grundsicherung, dem Rentner-Hartz IV, werden viele Betroffene im Geldbeutel spüren. \n \
        Reasoning: The sentence factually describes new allowances for housing benefit and pensions that affected people will feel financially. It is neutral policy information with neither anti-elitism nor people-centrism, so it is not populist. \n Answer: Not populist \n \
        Text: Zu tun hat sie vielmehr mit dem in Brüssel quasi veruntreuten Geld europäischer Normalverdiener zugunsten irgendwelcher Eliten in anderen Weltteilen oder aber Lobbygruppen in EU-Europa bzw. Deutschland selbst. \n \
        Reasoning: The sentence claims that ordinary European earners' money is embezzled in Brussels to benefit \"some elites\" and lobby groups. Pitting the common people against self-serving elites is classic anti-elitism, so it is populist. \n Answer: Populist \n \
        Text: Die konventionelle Grüne Gentechnik - so nenne ich sie jetzt einmal - ist eigentlich schon vorbei. \n \
        Reasoning: The sentence makes a topical observation that conventional green genetic engineering is essentially a thing of the past. It is a substantive remark with no populist framing, so it is not populist. \n Answer: Not populist \n \
        Text: Jede Lösung muss sich an den Interessen des deutschen Volkes und nicht an den Interessen der EU orientieren. \n \
        Reasoning: The sentence demands that every solution be guided by \"the interests of the German people\" rather than those of the EU. Invoking the people as the sovereign whose interests must prevail is people-centrism, a core populist dimension, so it is populist. \n Answer: Populist \n \
        Text: Die große Mehrheit der Arbeitgeber weiß das zu schätzen. \n \
        Reasoning: The sentence notes that the great majority of employers appreciate this. It references a group but does not cast \"the people\" as a virtuous sovereign or attack an elite, so it is not populist. \n Answer: Not populist \n \
        Text: Was deutsche Steuerzahler hart erarbeiten, das muss eingesetzt werden, um Wohlstand in Deutschland zu mehren. \n \
        Reasoning: The sentence elevates what \"German taxpayers work hard to earn\" as what must guide spending. Appealing to ordinary, hardworking citizens as the virtuous reference point is people-centrism, so it is populist. \n Answer: Populist \n \
        Text: Das ist unehrlich den Soldatinnen und Soldaten gegenüber. \n \
        Reasoning: Although the sentence is critical -- calling something dishonest toward soldiers -- it targets a specific unfairness rather than blaming a corrupt elite or invoking the will of the people. With neither populist dimension present, it is not populist. \n \n Answer: Not populist \n \
        Now classify whether the following Bundestag sentence conveys populism. First give your reasoning in 2-3 sentences, then give your final classification on a new line in exactly this format: \n Answer: Populist \n or \n Answer: Not populist"


# helper

def parse_label(response):
    if "Answer:" not in response:
        return -1
    answer = response.split("Answer:")[-1].strip().lower()
    if "not populist" in answer or "not populism" in answer:
        return 0
    elif "populist" in answer or "populism" in answer:
        return 1
    return -1

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
results_df.to_csv(f"{RESULTS_DIR}/llama_popbert_preds_fs_3.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

f1_nonpopulist = f1_score(valid["true_label"], valid["predicted"], pos_label=0)
f1_populist = f1_score(valid["true_label"], valid["predicted"], pos_label=1)
f1_macro = f1_score(valid["true_label"], valid["predicted"], average="macro")
prec_nonpopulist = precision_score(valid["true_label"], valid["predicted"], pos_label=0)
rec_nonpopulist = recall_score(valid["true_label"], valid["predicted"], pos_label=0)
prec_populist = precision_score(valid["true_label"], valid["predicted"], pos_label=1)
rec_populist = recall_score(valid["true_label"], valid["predicted"], pos_label=1)

print(f"\n=== Llama Popbert ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
print(f"  Nonpopulist -> P: {prec_nonpopulist:.3f}  R: {rec_nonpopulist:.3f}  F1: {f1_nonpopulist:.3f}")
print(f"  Populist    -> P: {prec_populist:.3f}  R: {rec_populist:.3f}  F1: {f1_populist:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    "condition": "prompting_fewshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
    "prec_nonpopulist": round(prec_nonpopulist, 4),
    "rec_nonpopulist": round(rec_nonpopulist, 4),
    "f1_nonpopulist": round(f1_nonpopulist, 4),
    "prec_populist": round(prec_populist, 4),
    "rec_populist": round(rec_populist, 4),
    "f1_populist": round(f1_populist, 4),
    "f1_macro": round(f1_macro, 4)
}

with open(f"{RESULTS_DIR}/llama_popbert_metrics_fs_3.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
