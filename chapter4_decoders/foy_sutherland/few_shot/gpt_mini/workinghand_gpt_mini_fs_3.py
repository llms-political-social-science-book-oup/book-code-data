from openai import OpenAI
from tqdm import tqdm, trange
import pandas as pd
import os
import re
import time
import json
from sklearn.metrics import confusion_matrix, f1_score, recall_score, precision_score, ConfusionMatrixDisplay


# config

RESULTS_DIR = "results_workinghand_gpt_mini_fs"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"]) 

models = client.models.list()
for model in models:
    print(model.id) ## shows you all available model names. Use these in "model = ..." below.


# load data

df = pd.read_excel("../../../../data/foy_sutherland/redbox_text_labels.xlsx")
texts = [str(t) for t in df["text"].tolist()]
labels = df["label_main"].tolist()

print(f"Loaded {len(texts)} redbox messages")

system_prompt = "You are an expert at political text annotation. Your task is to classify the TONE of a 'redbox' message \
        posted on a U.S. congressional candidate's or party committee's campaign website. A redbox is a public \
        message that signals to allied super PACs what advertising to run on the candidate's behalf. \
        Classify the tone as one of: \
        Positive: the message promotes the sponsoring candidate -- highlighting their own background, record, \
        qualities, or positions -- without attacking an opponent. \
        Negative: the message attacks or criticizes the opponent -- their record, votes, character, or positions \
        -- without promoting the sponsoring candidate. \
        Contrast: the message does both -- it promotes the sponsoring candidate AND attacks the opponent. \
        Here are some examples: \n \
        Text: Swing voters are seeing in the mailboxes that Jen Kiggans is a Naval Aviator, wife of a retired Navy Pilot, Mom, Nurse Practitioner, and state senator who will fight for Virginians to lower the cost of living, keep our community safe and stand strong for our service members. \n \
        Reasoning: The message highlights only Jen Kiggans's own background and promises -- her military service, family, professional roles, and pledges to lower costs and keep the community safe. It promotes the sponsoring candidate without attacking any opponent, so the tone is positive. \n Answer: Positive \n \
        Text: Colin Allred voted for Nancy Pelosi's anti-police bill that could restrict funding for local police departments. He also stood by as the City of Dallas cut seven million dollars in overtime pay from the police force. Colin Allred has failed to lead while cities across the country work to defund our police. \n \
        Reasoning: The message focuses entirely on attacking the opponent, Colin Allred, over his vote on a policing bill and his record on police funding. It criticizes the opponent without promoting any candidate of its own, so the tone is negative. \n Answer: Negative \n \
        Text: Voters will learn Tony Vargas is a self-serving tax and spend liberal. Vargas was the main proponent to increase the state income tax and then turned around and attempted to give himself a taxpayer funded pay raise. Don Bacon is fighting to make America energy independent, to lower our cost of living, and to stop runaway spending. \n \
        Reasoning: The message attacks the opponent, Tony Vargas, as a self-serving tax-and-spend liberal while also promoting Don Bacon's positions on energy and spending. Because it both criticizes the opponent and praises the sponsoring candidate, the tone is contrast. \n Answer: Contrast \n \
        Text: Starting in August, voters should see how Patty Murray is focused on reducing prices and bringing down costs to help Washington's workers and families. She is leading the fight to bring down prescription drug prices, hold big oil companies making record profits accountable for price hikes, and is making child care more affordable for Washington's working families. \n \
        Reasoning: The message describes only Patty Murray's own priorities and accomplishments -- reducing prices, lowering prescription drug costs, and making child care affordable. It promotes the candidate with no reference to or attack on an opponent, so the tone is positive. \n Answer: Positive \n \
        Text: Voters in the Philadelphia DMA need to know: Disgraced Senator Bob Menendez was indicted by the Obama Justice Department for accepting lavish bribes from convicted felon Salomon Melgen. The Senate Ethics Committee issued a bipartisan report severely admonishing Menendez for his corruption. Bob Menendez is a crook and does not deserve to be a U.S. Senator. \n \
        Reasoning: The message is devoted to attacking the opponent, Bob Menendez, over an indictment, an ethics admonishment, and corruption, calling him a crook. It criticizes the opponent without promoting any other candidate, so the tone is negative. \n Answer: Negative \n \
        Text: Voters will learn Katie Porter is a left-wing liberal who is just a rubber stamp for Joe Biden and Nancy Pelosi. Porter supports Biden's liberal agenda that has caused record high inflation, skyrocketing gas prices, and surging crime rates. Scott Baugh is a businessman and will go to Washington to fight against runaway spending, repeal the gas tax, and get our country back on track. \n \
        Reasoning: The message attacks the opponent, Katie Porter, as a rubber stamp for the Biden agenda while also promoting Scott Baugh as a businessman who will fight spending. Combining an attack on the opponent with promotion of the sponsoring candidate makes the tone contrast. \n Answer: Contrast \n \
        Text: Voters need to see and hear that after losing her son to gun violence, Lucy McBath ran for office to prevent another parent from suffering such a tragedy. Today, she is a leader on gun violence prevention in Congress, passing background checks for gun purchases, and steering efforts to prevent those who pose a threat to themselves or others from having access to firearms. \n \
        Reasoning: The message tells voters only about Lucy McBath's personal story and her record on gun violence prevention in Congress. It promotes the candidate's biography and accomplishments without attacking an opponent, so the tone is positive. \n Answer: Positive \n \
        Text: As this race closes, voters MUST be reminded Don Bacon bragged that he was voting \"hell yes\" to gut protections for pre-existing conditions; allow insurance companies to charge an \"age tax\" on older Americans; increase premiums; and leave 175,500 more Nebraskans without health insurance. \n \
        Reasoning: The message focuses on attacking the opponent, Don Bacon, over votes on pre-existing conditions, premiums, and health coverage. It criticizes the opponent's record without promoting any candidate of its own, so the tone is negative. \n Answer: Negative \n \
        Text: Ashley Hinson cares for our veterans and helped lead the fight to expand mental health services for veterans. Swing voters will see in their mailbox that Ashley Hinson is bringing Iowa commonsense leadership to Washington. She is an effective voice for Iowans while Democrats like Liz Mathis are beholden to Nancy Pelosi and her policies that are driving America in the wrong direction. \n \
        Reasoning: The message promotes Ashley Hinson's work for veterans and commonsense leadership while also attacking Liz Mathis as beholden to party leadership driving the country the wrong way. Because it praises the sponsoring candidate and criticizes the opponent, the tone is contrast. \n Answer: Contrast \n \
        Text: Voters will only see on cable and OTT through September that Jennifer-Ruth Green is a combat veteran and non-profit founder and is accepting the challenge to take on the problems that career politicians have been ignoring by working to fix our economy and fight crime in our communities. \n \
        Reasoning: The message presents only Jennifer-Ruth Green's credentials and goals -- a combat veteran and non-profit founder who will work on the economy and crime. It promotes the candidate without attacking a specific opponent, so the tone is positive. \n Answer: Positive \n \
        Text: Voters should know the specifics on Joe's liberal votes. Joe Cunningham worked for a law firm that represented clients with anti-environment records including the subsidiary of a company that finances the offshore drilling industry. \n \
        Reasoning: The message focuses on attacking the opponent, Joe Cunningham, over his liberal votes and his past work for a law firm tied to the offshore drilling industry. It criticizes the opponent without promoting any candidate of its own, so the tone is negative. \n Answer: Negative \n \
        Text: Voters need to know that Lori Torres Whitt's top backers called for defunding the police and replacing police and prisons. They bought her vote and will make Chicago less safe. Gil Villegas is a progressive who has combated crime by replacing vacant lots with new housing and businesses, funding better mental health care, and reversing historic disinvestment in communities left behind. \n \
        Reasoning: The message attacks the opponent, Lori Torres Whitt, over backers who favor defunding the police while also promoting Gil Villegas's record on crime and communities. Pairing an attack on the opponent with promotion of the sponsoring candidate makes the tone contrast. \n Answer: Contrast \n \
        Text: Progressive women all across Denver need to hear Mike Johnston's positive message for the city. Mike Johnston will make solving homelessness his number one priority. Mike Johnston believes no one should ever be homeless in Denver. Johnston will build housing with mental health, drug treatment, and job training programs. \n \
        Reasoning: The message conveys only Mike Johnston's positive message and plans to address homelessness with housing and treatment programs. It promotes the candidate's agenda without attacking an opponent, so the tone is positive. \n Answer: Positive \n \
        Text: What likely Democratic voters in NY-25 need to read, see, and see-on-the go: Joe's opponent La'Ron Singletary will stand with MAGA Republicans who are prioritizing eliminating Social Security and Medicare drug reforms and want to cut taxes for drug companies and big oil who are already gouging hard-working families. Our community can't afford these dangerous ideas. \n \
        Reasoning: The message focuses on attacking the opponent, La'Ron Singletary, by tying him to positions on Social Security, Medicare, and tax cuts framed as harmful. It criticizes the opponent without promoting the sponsoring candidate, so the tone is negative. \n Answer: Negative \n \
        Text: Our rights are under attacks from Trump Republicans like Madison Gesiotto Gilbert. While white supremacist groups attacked the U.S. Capitol, she expressed sympathy for the rioters and continued to spread Trump's lies about the 2020 election - hoping our votes were thrown out. Emilia Sykes understands the sacrifices that we have made for the right to vote and will always defend our democracy. \n \
        Reasoning: The message attacks the opponent, Madison Gesiotto Gilbert, over the Capitol attack and election claims while also promoting Emilia Sykes as a defender of democracy. Because it both criticizes the opponent and praises the sponsoring candidate, the tone is contrast. \n \n Answer: Contrast \n \
        Now classify the tone of the following redbox message as 'Positive', 'Negative', or 'Contrast'. First give your reasoning in 2-3 sentences, then give your final classification on a new line in exactly this format: \n Answer: Positive \n or \n Answer: Negative \n or \n Answer: Contrast"

class_labels = ["Positive", "Contrast", "Negative"]

# helper

def parse_label(response):
    if "Answer:" not in response:
        return -1
    answer = response.split("Answer:")[-1].strip().upper()
    if "POSITIVE" in answer:
        return "Positive"
    elif "CONTRAST" in answer:
        return "Contrast"
    elif "NEGATIVE" in answer:
        return "Negative"
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Message: "{text}"\n\nTone:'}
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
results_df.to_csv(f"{RESULTS_DIR}/gpt_mini_workinghand_preds_fs_3.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

prec = precision_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
rec = recall_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1 = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1_macro = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average="macro", zero_division=0)

print(f"\n=== GPT Mini Working Hand ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
for i, c in enumerate(class_labels):
    print(f"  {c:<10}-> P: {prec[i]:.3f}  R: {rec[i]:.3f}  F1: {f1[i]:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "openai/gpt-5.4-mini",
    "condition": "prompting_fewshot_openai",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
}
for i, c in enumerate(class_labels):
    metrics[f"prec_{c}"] = round(float(prec[i]), 4)
    metrics[f"rec_{c}"] = round(float(rec[i]), 4)
    metrics[f"f1_{c}"] = round(float(f1[i]), 4)
metrics["f1_macro"] = round(float(f1_macro), 4)

with open(f"{RESULTS_DIR}/gpt_mini_workinghand_metrics_fs_3.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)
