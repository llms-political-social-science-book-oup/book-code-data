# Tone of campaign "redbox" messages

**Source:** Foy-Sutherland, Gabriel (2025). "Working Hand in Hand: Interest Groups and Cooperative Dynamics in Campaigns." *Journal of Politics*.

**Replication archive:** https://doi.org/10.7910/DVN/5DKNDD (Harvard Dataverse, CC0 1.0)

**Task in the book:** Message tone (Negative, Contrast, Positive). **Language:** English.

## Files

- `redbox_text_labels.xlsx`: the spreadsheet read by the notebooks and scripts. 910 rows. Columns: `text`, `Tone`, `Self_Opponent`, `label_main`. The code reads `text` and `label_main`.
- `foy_predictions.csv`: row-level predictions of the ten decoder configurations (majority vote over three runs, with disagreement flags) for every row of the spreadsheet; `foy_covariates.csv`: covariates assembled for the Chapter 5 analyses; `README_foy_row_level.md`: column definitions of both files. Rows align to the spreadsheet through `row_id` (0-based row number) and `text_hash` (md5 of the text cell).
- `foy_encoder_oof_predictions.csv`: out-of-fold predictions and logits of the seeded single-pass RoBERTa-large run (notebook in `chapter5_downstream/dsl_ensemble/foy_sutherland/`), the encoder input to Chapter 5.

**Classes (`label_main`):** Negative: 529, Contrast: 220, Positive: 161. N = 910.

## How the spreadsheet was built

Built from `JOP Paper Master Data.csv` in the archive: the 910 redbox messages with a hand-coded `Tone`, in the order of that file. `label_main` is the `Tone` column; `Self_Opponent` is kept.
