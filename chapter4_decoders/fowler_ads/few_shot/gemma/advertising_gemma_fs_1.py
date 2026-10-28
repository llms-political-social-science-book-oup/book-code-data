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

data = pd.read_excel("../../../../data/fowler_ads/fowler_ads_text_labels.xlsx")
data.label_main.value_counts()

texts = data.text.tolist()
labels = data.label_main.tolist()
RESULTS_DIR = "results_advertising_gemma_fs"
os.makedirs(RESULTS_DIR, exist_ok=True)

# examples now go Reasoning -> Answer (reasoning must come before the answer for CoT to work),
# and the model reasons at inference before giving its label
prompt = "You are an expert at political text annotation. Your task is to classify the TONE of a political \
        advertisement -- the text or audio transcript of a campaign ad that ran on Facebook or television. \
        The ad may be in any language. Classify the tone as one of: \
        Promote: the ad promotes or favors one candidate -- focusing on that candidate's positive qualities, \
        record, positions, or campaign -- without attacking an opponent. \
        Attack: the ad attacks or opposes the opponent -- focusing on the opponent's flaws, record, or positions \
        -- without promoting the favored candidate. \
        Contrast: the ad does both -- it promotes the favored candidate AND attacks the opponent. \
        Here are some examples: \n \
        Text: Tomorrow is election day! I ask for your support to move our state forward and bring Wyoming values back to Washington, DC. \n \
        Reasoning: The ad simply asks voters for their support and frames the candidate around bringing \"Wyoming values\" to Washington. It promotes the favored candidate positively and never mentions or attacks an opponent, so the tone is promote. \n Answer: Promote \n \
        Text: We can't trust Knute Buehler. He took money from drug companies, and voted against lowering drug prices. He also voted to strip health care away from hundreds of thousands of people. Knute Buehler's actions speak louder than words. \n \
        Reasoning: The ad focuses entirely on attacking the opponent, Knute Buehler, over drug-company money and votes on drug prices and health care. It criticizes the opponent without promoting any favored candidate, so the tone is attack. \n Answer: Attack \n \
        Text: Our families are now able to keep more of what they earn thanks to the recent tax cuts. And, some businesses are even using the money they've saved to give employees raises and bonuses. My opponents want to undo the tax cuts that have helped WA families--I won't let them. SIGN UP to support! \n \
        Reasoning: The ad promotes the candidate's own record on tax cuts and the benefits to families, and also attacks the opponents who want to undo those tax cuts. Because it both praises the favored candidate and attacks the opposition, the tone is contrast. \n Answer: Contrast \n \
        Text: Idaho is blessed to have strong Republican candidates running for office. Please help us #KeepIdahoConservative by voting Republican in this critical election! \n \
        Reasoning: The ad praises the slate of Republican candidates and urges voters to keep Idaho conservative by voting Republican. It promotes favored candidates positively with no attack on any opponent, so the tone is promote. \n Answer: Promote \n \
        Text: Jacqui Irwin and her Sacramento special interest handlers worked hand-in-hand to pass their $52 billion gas and car tax last year. We can't continue to let Jacqui Irwin sell us out for special interest contributions. We deserve better than a legislator in the pocket of Big Sacramento! \n \
        Reasoning: The ad is devoted to attacking the opponent, Jacqui Irwin, over a gas and car tax and ties to special-interest donors. It criticizes the opponent without promoting a favored candidate, so the tone is attack. \n Answer: Attack \n \
        Text: I've been named by Numbers USA as a \"True Reformer\" when it comes to my stances on immigration. Meanwhile, Tim Harris won't take their survey nor tell the voters of OK-01 his plan for securing our border and protecting American jobs. \n \
        Reasoning: The ad promotes the candidate's own immigration record as a \"True Reformer\" while also attacking the opponent, Tim Harris, for ducking the issue. Pairing self-promotion with an attack on the opponent makes the tone contrast. \n Answer: Contrast \n \
        Text: Great Seeing my Congressman Tim Ryan at the Youngstown Brier Hill Italian Fest-he's always fighting for working families. \n \
        Reasoning: The ad is a friendly, positive note praising Congressman Tim Ryan as someone who is always fighting for working families. It promotes the favored candidate with no mention of an opponent, so the tone is promote. \n Answer: Promote \n \
        Text: Liz Watson doesn't believe we need to secure our border and she won't stop sanctuary cities from harboring dangerous criminals, but she will give amnesty to illegal immigrants. Don't let Liz Watson's liberal policies put our country in harm's way! \n \
        Reasoning: The ad focuses on attacking the opponent, Liz Watson, over border security, sanctuary cities, and immigration. It criticizes the opponent without promoting a favored candidate, so the tone is attack. \n Answer: Attack \n \
        Text: Martha McSally has run a dirty and misleading campaign -- she doesn't belong in the U.S. Senate. Republican leaders like Grant Woods are supporting Kyrsten Sinema because she's a great leader who will stand up for Arizona. \n \
        Reasoning: The ad attacks the opponent, Martha McSally, as having run a dirty and misleading campaign, and promotes Kyrsten Sinema as a great leader for Arizona. Because it both attacks the opponent and praises the favored candidate, the tone is contrast. \n Answer: Contrast \n \
        Text: Jenni & Aaron of To Share Brewing Company have all the right ingredients to make their entrepreneurial dream into a reality. I'm proud to have their support. I'm committed to doing everything I can make sure our State Government is doing everything it can to help them succeed. \n \
        Reasoning: The ad highlights the candidate's pride in local small-business support and commitment to helping businesses succeed. It promotes the favored candidate positively without attacking an opponent, so the tone is promote. \n Answer: Promote \n \
        Text: Tina Smith has made it clear she is willing to put extreme partisan politics ahead of her principles by standing with her longtime friend and political ally, Keith Ellison. \n \
        Reasoning: The ad focuses on attacking the opponent, Tina Smith, for putting partisan politics ahead of principle by allying with Keith Ellison. It criticizes the opponent without promoting a favored candidate, so the tone is attack. \n Answer: Attack \n \
        Text: Kris Kobach has made a name for himself by putting divisive policies and rigid ideology ahead of common sense solutions that improve people's lives. Kris Kobach has always been about what helps him, not you. Chip in $3 or more now to help Laura Kelly and stop him from taking the governor's office. \n \
        Reasoning: The ad attacks the opponent, Kris Kobach, as divisive and self-serving, and promotes Laura Kelly while asking voters to help stop him. Combining an attack on the opponent with promotion of the favored candidate makes the tone contrast. \n Answer: Contrast \n \
        Text: I had the pleasure of starting my day having breakfast with the Greene County Democrats, Representative Eddie Yokley, and the Greene County Teachers. While enjoying our meal we talked about strengthening our educational system and what we need to do to move forward in our great state. \n \
        Reasoning: The ad describes the candidate's positive campaign activity meeting with local Democrats and teachers to discuss strengthening education. It promotes the favored candidate's engagement with no attack on an opponent, so the tone is promote. \n Answer: Promote \n \
        Text: Former lobbyist Cary Kennedy went back on her promise to run a clean campaign when she ran a false ad attacking Jared Polis. Shaun Boyd of Reality Check sets the record straight: Cary Kennedy is misleading voters. \n \
        Reasoning: The ad focuses on attacking the opponent, Cary Kennedy, as a former lobbyist who broke a clean-campaign promise and is misleading voters. It criticizes the opponent without promoting a favored candidate, so the tone is attack. \n Answer: Attack \n \
        Text: I stand with #AZ police + the Border Strike Force, an elite law enforcement unit that fights dangerous drugs and human trafficking at the border. But my liberal opponent wants to end cooperation between local law enforcement and ICE. Return your ballot or vote Nov 6 for J.D. Mesnard #LD17 #VOTE \n \
        Reasoning: The ad promotes the candidate's own stance standing with police and the Border Strike Force, and attacks the \"liberal opponent\" who wants to end cooperation with ICE. Because it both promotes the favored candidate and attacks the opponent, the tone is contrast. \n \n Answer: Contrast \n \
        Now classify the tone of the following political ad as 'Promote', 'Attack', or 'Contrast'. First give your reasoning in 2-3 sentences, then give your final classification on a new line in exactly this format: \n Answer: Promote \n or \n Answer: Attack \n or \n Answer: Contrast"


# helper

def parse_label(response):
    if "Answer:" not in response:
        return -1
    answer = response.split("Answer:")[-1].strip().lower()
    if "contrast" in answer:
        return "Contrast"
    elif "attack" in answer:
        return "Attack"
    elif "promote" in answer:
        return "Promote"
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
results_df.to_csv(f"{RESULTS_DIR}/gemma_advertising_preds_fs_1.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

class_labels = ["Promote", "Contrast", "Attack"]
prec = precision_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
rec = recall_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1 = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1_macro = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average="macro", zero_division=0)

print(f"\n=== Gemma Political Advertising ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
for i, c in enumerate(class_labels):
    print(f"  {c:<8}-> P: {prec[i]:.3f}  R: {rec[i]:.3f}  F1: {f1[i]:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "google/gemma-4-31B-it",
    "condition": "prompting_fewshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
    "prec_promote": round(float(prec[0]), 4),
    "rec_promote": round(float(rec[0]), 4),
    "f1_promote": round(float(f1[0]), 4),
    "prec_contrast": round(float(prec[1]), 4),
    "rec_contrast": round(float(rec[1]), 4),
    "f1_contrast": round(float(f1[1]), 4),
    "prec_attack": round(float(prec[2]), 4),
    "rec_attack": round(float(rec[2]), 4),
    "f1_attack": round(float(f1[2]), 4),
    "f1_macro": round(float(f1_macro), 4)
}

with open(f"{RESULTS_DIR}/gemma_advertising_metrics_fs_1.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
