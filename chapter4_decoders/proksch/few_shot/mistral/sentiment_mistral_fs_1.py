from openai import OpenAI 
from tqdm import tqdm, trange 
import pandas as pd
import os 
import re
import time
import json
from sklearn.metrics import confusion_matrix, f1_score, recall_score, precision_score, ConfusionMatrixDisplay


client = OpenAI(
           base_url = "https://api.deepinfra.com/v1/openai",
           api_key=os.environ["DEEPINFRA_API_KEY"]
        )

data = pd.read_excel("../../../../data/proksch/soteu2010_text_labels.xlsx")
# recode the averaged 1-5 handcoded scale (1, 1.5, 2, 2.5, ... 5) to 9 ordinal categories (1, 2, ... 9)
data["sentiment9"] = (data["label_main"] * 2 - 1).astype(int)
data.sentiment9.value_counts()

texts = data.Text.tolist()
labels = data.sentiment9.tolist()

RESULTS_DIR = "results_sentiment_mistral_fs"
os.makedirs(RESULTS_DIR, exist_ok=True)

# examples now go Reasoning -> Answer (reasoning must come before the answer for CoT to work),
# and the model reasons at inference before giving its label
prompt = "You are an expert at political text annotation. Your task is to classify a paragraph from a \
        parliamentary debate speech according to its SENTIMENT on a 9-point scale from 1 to 9. \
        These paragraphs come from the State of the Union debate in the European Parliament, and the \
        paragraph may be in any language, since this corpus spans many European languages. Judge the \
        sentiment from the meaning regardless of language. \
        SENTIMENT here means the overall tone the speaker expresses: how positive (approving, optimistic, \
        praising, confident) or negative (critical, pessimistic, disapproving, hostile) the paragraph is, \
        taken as a whole. Use the full 1 to 9 scale: \
        1 = very negative: strongly critical, hostile, or pessimistic throughout \
        2 = mostly negative: predominantly critical, with little to offset it \
        3 = negative: clearly critical but measured in tone \
        4 = slightly negative: positive and negative elements are both present, but negativity dominates \
        5 = neutral or balanced: even-handed and matter-of-fact, or positive and negative roughly cancel out \
        6 = slightly positive: positive and negative elements are both present, but positivity dominates \
        7 = positive: clearly approving or optimistic but measured in tone \
        8 = mostly positive: predominantly approving, with little to offset it \
        9 = very positive: strongly approving, celebratory, or optimistic throughout \
        Here are some examples: \n \
        Text: Madam President, the President of the Commission talked about sustainable growth and a target of 75% employment across the EU, a goal we would all agree with. Yet across the EU, drastic cuts in public services are adding to the numbers of unemployed, taking money out of the economy and reducing essential services. How does this help the economy and avoid a job crisis? It really does not make sense. \n \
        Reasoning: The speaker briefly concedes a shared goal but immediately turns to a sustained, sharp criticism. The language is strongly negative throughout - 'drastic cuts', services that swell unemployment and drain the economy - and it closes with dismissive rhetorical questions and the flat verdict that it does not make sense. The overwhelmingly disapproving tone places this at the most negative end of the scale. \n Answer: 1 \n \
        Text: It will clearly be a very complex debate, in an extremely difficult economic situation. If the Member States cannot increase their contribution, resources will have to be found so that the European Union can deliver results. What we cannot do is ask Europe to deliver results without giving it the resources to do so. It would be impossible to do that, and so we must have an extremely serious debate on this issue of solidarity and subsidiarity. \n \
        Reasoning: The tone is heavy and predominantly negative, dominated by the framing of difficulty and constraint - very complex, extremely difficult, impossible, extremely serious. It is not purely bleak, however, since it points toward finding resources and holding a serious debate, a constructive edge that lifts it slightly above the darkest framing. Negative on balance with a faint constructive note. \n Answer: 2 \n \
        Text: However, you will have three quarters of the members of the Council against you if you talk about own resources. I am now eager to see whether you follow what you have said today with action and take up the fight against the intergovernmentalisation of the European Union. I will give you an example. I agree with you that Europe will only succeed if we defend our elementary values. \n \
        Reasoning: The passage is skeptical and challenging, warning of strong opposition with three quarters of the Council against the proposal and pointedly questioning whether words will be followed by action. The negativity is clear but measured and businesslike rather than hostile, and it ends on a note of agreement about defending shared values. A clearly negative but restrained, critical stance. \n Answer: 3 \n \
        Text: Debt and deficit lead to boom and bust and they unravel the social safety net. Money that is spent on servicing debt is money that cannot be spent on the social good nor to prepare ourselves for the costs of an ageing population. A debt generation makes an unsustainable nation. Our proposals will strengthen the Stability and Growth Pact through increased surveillance and enforcement. \n \
        Reasoning: The first three sentences are bleak, casting debt and deficits as destabilising and corrosive - boom and bust, unravelling the safety net, an unsustainable nation. The final sentence pivots to a constructive remedy in the strengthened Stability and Growth Pact, which partly offsets the gloom. The mix still leans negative because the alarming diagnosis outweighs the brief solution. \n Answer: 4 \n \
        Text: Even with the Internet, over a third of consumers lack the confidence to make cross-border purchases. At my request, Mario Monti presented an excellent report and has identified 150 missing links and bottlenecks in the internal market. Next month, we will set out how to deepen the Single Market in a comprehensive and ambitious Single Market Act. Energy is a key driver for growth and a central priority for action. \n \
        Reasoning: Negative and positive elements roughly balance here. Problems are stated plainly - weak consumer confidence, missing links and bottlenecks - while positive notes sit alongside them, an excellent report, an ambitious act, energy as a growth driver. The overall register is even-handed and matter-of-fact, neither approving nor disapproving on net. \n Answer: 5 \n \
        Text: It is the cities, towns and villages you come from. When you walk round your constituencies, you can point to the European projects that are so important for their prosperity. At the end of the day, we are all in the same boat - the European institutions, Member States and regions. The Union will not achieve its objectives in Europe without the Member States and the Member States will not achieve their objectives in the world without the European Union. \n \
        Reasoning: The tone is warm and unifying, stressing tangible benefits to local communities and a shared purpose captured by the image of everyone in the same boat. It is positive overall, though the closing sentence about mutual dependence is more even and explanatory than celebratory, which keeps it modestly rather than strongly positive. \n Answer: 6 \n \
        Text: We will match monetary union with true economic union. If implemented as we propose, these reforms will also guarantee the long-term stability of the euro. It is key to our economic success. For the economy to grow, we also need a strong and sound financial sector - a sector that serves the real economy and that prides itself on proper regulation and proper supervision. \n \
        Reasoning: The passage is confident and forward-looking, presenting reforms that will guarantee the long-term stability of the euro and are key to economic success. The vocabulary is consistently affirmative - strength, soundness, success, proper regulation - with no countervailing negativity. A clearly positive, optimistic tone that stops short of the most exuberant register. \n Answer: 7 \n \
        Text: The economic outlook in the European Union today is better than it was a year ago, not least as a result of our determined action. The recovery is gathering pace, albeit unevenly within the Union. Growth this year will be higher than initially forecast. The unemployment rate, whilst still much too high, has stopped increasing. \n \
        Reasoning: The message is strongly upbeat - an improved outlook, an accelerating recovery, and growth above forecast, all credited to determined action. Two brief caveats, that the recovery is uneven and unemployment is still too high, add realism without denting the dominant optimism. Very positive overall, just short of unqualified celebration. \n Answer: 8 \n \
        Text: Mr President, honourable Members, it is a great privilege to deliver the first State of the Union address before this House. From now on, the State of the Union address will be the occasion when we will chart our work for the next 12 months. Many of the decisions we will take in the next year will have long-term implications. They will define the kind of Europe we want. \n \
        Reasoning: The tone is elevated and wholly affirmative. The speaker frames the moment as a great privilege and an historic first, looking ahead with aspiration to decisions that will define the kind of Europe we want. There is no negativity at all; the register is celebratory and visionary, placing it at the most positive end of the scale. \n \n Answer: 9 \n \
        Now classify the following paragraph on the 1 to 9 sentiment scale. First give your reasoning in 2-3 sentences, then give your final classification on a new line in exactly this format: \n Answer: 5 \n (where the number is a whole number from 1 to 9)"


# helper
def parse_label(response):
    if "Answer:" not in response:
        return -1
    seg = response.split("Answer:")[-1]
    m = re.findall(r"[1-9]", seg)
    if not m:
        m = re.findall(r"[1-9]", response)
    if not m:
        return -1
    return int(m[0])

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="mistralai/Mistral-Small-3.2-24B-Instruct-2506",
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
results_df.to_csv(f"{RESULTS_DIR}/mistral_sentiment_preds_fs_1.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

class_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
prec = precision_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
rec = recall_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1 = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1_macro = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average="macro", zero_division=0)

print(f"\n=== Mistral Sentiment ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
for i, c in enumerate(class_labels):
    print(f"  Level {c} -> P: {prec[i]:.3f}  R: {rec[i]:.3f}  F1: {f1[i]:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "mistralai/Mistral-Small-3.2-24B-Instruct-2506",
    "condition": "prompting_fewshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
    "prec_1": round(float(prec[0]), 4),
    "rec_1": round(float(rec[0]), 4),
    "f1_1": round(float(f1[0]), 4),
    "prec_2": round(float(prec[1]), 4),
    "rec_2": round(float(rec[1]), 4),
    "f1_2": round(float(f1[1]), 4),
    "prec_3": round(float(prec[2]), 4),
    "rec_3": round(float(rec[2]), 4),
    "f1_3": round(float(f1[2]), 4),
    "prec_4": round(float(prec[3]), 4),
    "rec_4": round(float(rec[3]), 4),
    "f1_4": round(float(f1[3]), 4),
    "prec_5": round(float(prec[4]), 4),
    "rec_5": round(float(rec[4]), 4),
    "f1_5": round(float(f1[4]), 4),
    "prec_6": round(float(prec[5]), 4),
    "rec_6": round(float(rec[5]), 4),
    "f1_6": round(float(f1[5]), 4),
    "prec_7": round(float(prec[6]), 4),
    "rec_7": round(float(rec[6]), 4),
    "f1_7": round(float(f1[6]), 4),
    "prec_8": round(float(prec[7]), 4),
    "rec_8": round(float(rec[7]), 4),
    "f1_8": round(float(f1[7]), 4),
    "prec_9": round(float(prec[8]), 4),
    "rec_9": round(float(rec[8]), 4),
    "f1_9": round(float(f1[8]), 4),
    "f1_macro": round(float(f1_macro), 4)
}
with open(f"{RESULTS_DIR}/mistral_sentiment_metrics_fs_1.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
