# Incivility in tweets by members of Congress

**Source:** Ballard, Andrew O., Ryan DeTamble, Spencer Dorsey, Michael Heseltine and Marcus Johnson (2023). "Dynamics of Polarizing Rhetoric in Congressional Tweets." *Legislative Studies Quarterly* 48(1): 105–144.

**Replication archive:** https://doi.org/10.7910/DVN/2ET6VL (Harvard Dataverse, CC0 1.0)

**Task in the book:** Incivility (binary). **Language:** English.

## Files

- `incivility_tweets_text_labels.xlsx`: the spreadsheet read by the notebooks and scripts. 2,919 rows. Columns: `text`, `uncivil_spencer`, `uncivil_michael`, `uncivil`, `uncivil_2`, `uncivil_final`, `hand_code`, `label_main`, `source_file`. The code reads `text` and `label_main`.
- `ballard_predictions.csv`: row-level predictions of the ten decoder configurations (majority vote over three runs, with disagreement flags) for every row of the spreadsheet; `ballard_covariates.csv`: covariates assembled for the Chapter 5 analyses; `README_ballard_row_level.md`: column definitions of both files. Rows align to the spreadsheet through `row_id` (0-based row number) and `text_hash` (md5 of the text cell).
- `ballard_encoder_oof_predictions.csv`: out-of-fold predictions and logits of the seeded single-pass RoBERTa-large run (notebook in `chapter5_downstream/dsl_ensemble/ballard_incivility/`), the encoder input to Chapter 5.

**Classes (`label_main`):** 0: 2,432, 1: 487. N = 2,919.

## How the spreadsheet was built

Built from `combined_training_ab` in the archive: the hand-coded training tweets, deduplicated, English-only, with tweets whose coders disagreed on the final code removed, giving 2,919 rows. `label_main` is 1 for uncivil and 0 for civil; the coder columns are kept.
