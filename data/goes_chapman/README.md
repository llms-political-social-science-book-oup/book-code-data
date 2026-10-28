# Governance advice in IMF Article IV staff appraisals

**Source:** Goes, Iasmin and Terrence L. Chapman (2024). "Can 'Soft' Advice from International Organizations Catalyze Natural Resource Sector Reform?" *International Studies Quarterly* 68(2). https://doi.org/10.1093/isq/sqae048

**Replication archive:** https://doi.org/10.7910/DVN/U2DEKY (Harvard Dataverse, CC0 1.0; an earlier deposit of the same materials is https://doi.org/10.7910/DVN/V5MWRF)

**Task in the book:** Promotes governance reform (binary). **Language:** English.

## Files

- `goes_chapman_articleiv_text_labels.xlsx`: the spreadsheet read by the notebooks and scripts. 700 rows. Columns: `iso3c`, `year`, `text`, `label_main`. The code reads `text` and `label_main`.

**Classes (`label_main`):** 0: 447, 1: 253. N = 700.

## How the spreadsheet was built

Built from `data/article_iv_corpus.Rdata` (the staff-appraisal texts of 700 consultations) joined to `data/covariates` on country code and year. `label_main` is the authors' manual coding `article_iv_promotes_governance`.
