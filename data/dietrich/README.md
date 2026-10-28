# Aid mentions in party manifesto sentences

**Source:** Dietrich, Simone, Helen V. Milner and Jonathan B. Slapin (2020). "From Text to Political Positions on Foreign Aid: Analysis of Aid Mentions in Party Manifestos from 1960 to 2015." *International Studies Quarterly* 64(4): 980–990.

**Replication archive:** https://doi.org/10.7910/DVN/ICTZ1A (Harvard Dataverse, CC0 1.0)

**Task in the book:** Aid mention (binary). **Language:** English, German, Norwegian, Spanish, Danish, Swedish, Finnish, French.

## Files

- `dietrich_aidmentions_text_labels.xlsx`: the spreadsheet read by the notebooks and scripts. 52,744 rows. Columns: `cty`, `text`, `aid_c1`, `aid_c2`, `proaid_c1`, `proaid_c2`, `negaid_c1`, `negaid_c2`, `label_main`. The code reads `text` and `label_main`.
- `ORIGINAL_README_Replication_Materials.rtf`: the README of the replication archive.

**Classes (`label_main`):** 0: 47,490, 1: 5,254. N = 52,744.

## How the spreadsheet was built

Built from `input/manifesto_rawcoding` in the archive (53,684 hand-coded sentences; 939 rows with empty text dropped, 45 further rows have a missing text cell and are dropped by the notebooks). `label_main` is 1 when the sentence is coded as an aid mention, following the first coder; both coders' columns are kept.
