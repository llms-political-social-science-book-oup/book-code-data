##
## Gemma: ParlaCAP Topic Classification
## Joan Timoneda, March 2026
## Via DeepInfra API
##

from openai import OpenAI
from tqdm import tqdm
import pandas as pd
import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score
import json
import os
import time


# config

RESULTS_DIR = "results_parlacap_gemma_zs"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = OpenAI(
    base_url="https://api.deepinfra.com/v1/openai",
    api_key=os.environ["DEEPINFRA_API_KEY"]
)

# load data

df = pd.read_excel("../../../../data/parlacap/parlacap_text_labels.xlsx")
texts = [str(t) for t in df["text"].tolist()]
labels = df["label_main"].tolist()

print(f"Loaded {len(texts)} speeches")

# system prompt

class_labels = ["Macroeconomics", "Civil Rights", "Health", "Agriculture", "Labor",
                "Education", "Environment", "Energy", "Immigration", "Transportation",
                "Law and Crime", "Social Welfare", "Housing", "Domestic Commerce", "Defense",
                "Technology", "Foreign Trade", "International Affairs", "Government Operations",
                "Public Lands", "Culture", "Other"]

system_prompt = """You are are an expert at political text annotation. Your task is to classify parliamentary \
speeches into one Comparative Agendas Project (CAP) major policy topic. The speeches come from \
the parliaments of the United Kingdom, Bosnia-Herzegovina, Croatia, and Serbia, and may be in \
English, Bosnian, Croatian, or Serbian.

Assign exactly one of the following topics, using these descriptions:

Macroeconomics: domestic macroeconomic policy, such as the national economy, economic policy, inflation, interest rates, monetary policy, cost of living, unemployment rate, national budget, public debt, price control, tax enforcement, industrial growth.
Civil Rights: civil and minority rights, discrimination by race, gender, sexual orientation, or disability, voting rights, freedom of speech, religious freedoms, privacy and data protection, abortion rights, anti-government activity groups, religion and the Church.
Health: health care, health reforms, health insurance, the drug industry, medical facilities and workers, disease prevention and treatment, drug and alcohol abuse, mental health, medical research, medical liability.
Agriculture: agriculture policy, fishing, agricultural foreign trade, food marketing, subsidies to farmers, food inspection and safety, animal and crop disease, pest control, animal welfare, veterinary medicine, agricultural research.
Labor: labor and employment, employment programs, employee benefits, pensions, minimum wage, labor law, job training, labor unions, worker safety, youth and seasonal workers.
Education: education policy, primary and secondary schools, student loans and education finance, colleges and universities, school reforms, teachers, vocational training, school safety, libraries and teaching material, education research.
Environment: environmental policy, drinking water safety, air, noise and soil pollution, waste disposal, recycling, climate change, environmental hazards, species and forest protection, marine and freshwater environment, hunting, conservation, environmental research.
Energy: energy policy, electricity and utilities, nuclear energy and waste, natural gas and oil, drilling, oil spills, oil and gas prices, heat supply, gasoline regulation, coal, alternative and renewable energy, energy conservation and efficiency, energy research.
Immigration: immigration, refugees, citizenship, integration, residence permits, asylum applications, and offences or diseases linked to immigration.
Transportation: mass transportation, bus transport, motor vehicles, road construction and safety, parking, traffic accidents, air travel, rail travel and freight, maritime transport, inland waterways, transportation research.
Law and Crime: the control, prevention, and impact of crime, law enforcement agencies including border and customs, police, courts and prisons, terrorism, white collar crime, fraud, cyber-crime, drug trafficking, domestic violence, child welfare, family law, juvenile crime.
Social Welfare: social welfare policy, social services, poverty assistance for low-income families and the elderly, parental leave and child care, assistance for people with disabilities, discounts on public services, volunteer associations, charities, youth organizations.
Housing: housing, urban affairs and community development, the housing market, property tax, spatial planning, rural development, permits, construction inspection, illegal construction, low-income, rental, elderly and homeless housing, housing research.
Domestic Commerce: banking, finance and internal commerce, the stock exchange, investments, consumer finance, mortgages, credit, insurance, accounting regulation, bankruptcies, small business promotion, copyrights and patents, intellectual property, disaster preparedness and relief, consumer safety, regulation of tourism, sports and gambling, commerce research.
Defense: defense policy, military intelligence, espionage, weapons, military personnel and reserves, military buildings and courts, nuclear weapons, civil defense including firefighters and mountain rescue, homeland security, military aid and arms sales, prisoners of war, military waste disposal, defense alliances and operations, defense research.
Technology: science and technology transfer and cooperation, research policy, space programs, telecommunication regulation, broadcast media such as television, radio, newspapers and film, weather forecasting, geological surveys, the computer industry, cyber security.
Foreign Trade: foreign trade, trade negotiations, free trade agreements, import regulation, export promotion, subsidies, private business investment and corporate development, competitiveness, exchange rates, foreign investment and sales of companies abroad.
International Affairs: foreign policy and relations to other countries, the Ministry of Foreign Affairs, foreign aid, international agreements, international organizations such as the United Nations, NGOs, diplomacy, embassies, citizens abroad, border control, international finance including the World Bank and IMF and the finances of the EU, issues in a foreign country that do not impact the home country, human rights abroad, international terrorism.
Government Operations: general government operations, the work of multiple departments, public employees, postal services, nominations and appointments, mints, medals and coins, management of government property, government procurement, public scandal and impeachment, claims against the government, the state inspectorate and audit, anti-corruption policies, regulation of political campaigns and voter registration, census and statistics, local government and municipalities, decentralization, national holidays.
Public Lands: national parks, memorials, historic sites and protected areas, cultural sites and museums, use of public lands and forests, harbors and marinas, flood control, forest fires, livestock grazing.
Culture: cultural policy, the Ministry of Culture, public spending on culture, cultural employees, support of theatres and artists, allocation of national lottery funds, cultural heritage.
Other: speeches that do not address a policy agenda, including parliamentary procedure such as points of order, voting procedures and meeting logistics, interpersonal speech such as greetings, personal stories, tributes, interjections and arguments between members, and rhetorical speech such as jokes and literary references.

Respond with exactly one of the topic names above. Nothing else."""

# helper

def parse_label(response):
    r = response.upper().strip()
    for label in class_labels:
        if label.upper() in r:
            return label
    return -1

def classify(system_prompt, text):
    response = client.chat.completions.create(
        model="google/gemma-4-31B-it",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f'Speech: "{text}"\n\nClassification:'}
        ],
        temperature=0,
        max_tokens=10,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].message.content.strip()

# quick test

test_response = classify(system_prompt, texts[0])
print(f"Test response: '{test_response}'")
print(f"True label: {labels[0]}")
print(f"Parsed: {parse_label(test_response)}")

# run classification on all speeches

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
results_df.to_csv(f"{RESULTS_DIR}/gemma31b_parlacap_preds_1.csv", index=False)

valid = results_df[results_df["predicted"] != -1].copy()
n_invalid = (results_df["predicted"] == -1).sum()

prec = precision_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
rec = recall_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1 = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average=None, zero_division=0)
f1_macro = f1_score(valid["true_label"], valid["predicted"], labels=class_labels, average="macro", zero_division=0)

print(f"\n=== Gemma 4 31B ParlaCAP ===")
print(f"Valid: {len(valid)}/{len(results_df)} (unparseable: {n_invalid})")
for i, c in enumerate(class_labels):
    print(f"  {c:<22}-> P: {prec[i]:.3f}  R: {rec[i]:.3f}  F1: {f1[i]:.3f}")
print(f"\n  Macro F1: {f1_macro:.3f}")

metrics = {
    "model": "google/gemma-4-31B-it",
    "condition": "prompting_zeroshot_deepinfra",
    "n_valid": int(len(valid)),
    "n_invalid": int(n_invalid),
}
for i, c in enumerate(class_labels):
    metrics[f"prec_{c}"] = round(float(prec[i]), 4)
    metrics[f"rec_{c}"] = round(float(rec[i]), 4)
    metrics[f"f1_{c}"] = round(float(f1[i]), 4)
metrics["f1_macro"] = round(float(f1_macro), 4)

with open(f"{RESULTS_DIR}/gemma31b_parlacap_metrics_1.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved to", RESULTS_DIR)