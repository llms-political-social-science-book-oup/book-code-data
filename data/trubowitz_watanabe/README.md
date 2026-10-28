# Geopolitical threat in New York Times foreign-affairs articles

**Source:** Trubowitz, Peter and Kohei Watanabe (2021). "The Geopolitical Threat Index: A Text-Based Computational Approach to Identifying Foreign Threats." *International Studies Quarterly* 65(3): 852–865. https://doi.org/10.1093/isq/sqab029

**Replication archive:** https://doi.org/10.7910/DVN/9QPZ43 (Harvard Dataverse, CC0 1.0)

**Task in the book:** Conveys a geopolitical threat (Yes, No, Unclear). **Language:** English.

## Files

- `trubowitz_gti_text_labels.xlsx`: the spreadsheet read by the notebooks and scripts. 1,700 rows. Columns: `sample`, `text`, `threat_coded`, `country_coded`, `label_main`. The code reads `text` and `label_main`.
- `trubowitz_predictions.csv`: row-level predictions of the ten decoder configurations (majority vote over three runs, with disagreement flags) for every row of the spreadsheet; `trubowitz_covariates.csv`: covariates assembled for the Chapter 5 analyses; `README_trubowitz_row_level.md`: column definitions of both files. Rows align to the spreadsheet through `row_id` (0-based row number) and `text_hash` (md5 of the text cell).
- `trubowitz_encoder_oof_predictions.csv`: out-of-fold predictions and logits of the seeded single-pass RoBERTa-large run (notebook in `chapter5_downstream/dsl_ensemble/trubowitz_watanabe/`), the encoder input to Chapter 5.
- `ORIGINAL_Instructions.txt`: the README of the replication archive.

**Classes (`label_main`):** No: 1,067, Yes: 513, Unclear: 120. N = 1,700.

## How the spreadsheet was built

Built from `domestic_coded` and `foreign_coded` in the archive: the authors' two human-coded validation samples of 850 article summaries each (100 per decade, 1860s–2010s). `label_main` is the human threat code; the domestic file's numeric codes 0/1/3 were mapped to No/Yes/Unclear. `sample` records which file a row comes from.
