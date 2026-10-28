# Deliberative quality of speech acts in transitional-justice consultations

**Source:** Kostovicova, Denisa and Tom Paskhalis (2021). "Gender, Justice and Deliberation: Why Women Don't Influence Peacemaking." *International Studies Quarterly* 65(2): 263–276.

**Replication archive:** https://doi.org/10.7910/DVN/FC6WAO (data) and https://doi.org/10.7910/DVN/PMICO2 (code and results); Harvard Dataverse, CC0 1.0

**Task in the book:** Level of justification, Discourse Quality Index (0–3). **Language:** Bosnian, Croatian, Serbian.

## Files

- `kostovicova_dqi_text_labels.xlsx`: the spreadsheet read by the notebooks and scripts. 1,211 rows. Columns: `cid`, `speech_act`, `text`, `PART`, `JUST_RAT`, `CONT_COLL`, `CONT_DIFF`, `CONT_APR`, `RES_PAR`, `RES_GR`, `STO_JUS`, `label_main`. The code reads `text` and `label_main`.

**Classes (`label_main`):** 2: 658, 1: 240, 3: 224, 0: 89. N = 1,211.

## How the spreadsheet was built

Built from `dqiCorpus.RData` (texts) and `DQITJ1_ Master.tab` (hand-coded Discourse Quality Index components) in the data deposit. The two files share no key; speech acts were matched within each of the 20 consultations by order, which the gender field present in both files confirms for 1,197 of 1,211 rows. `label_main` is `JUST_RAT`, the level-of-justification component; the other components are kept.
