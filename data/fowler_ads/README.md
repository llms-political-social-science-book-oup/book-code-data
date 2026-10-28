# Tone of 2018 television and Facebook political ads

**Source:** Fowler, Erika Franklin, Michael M. Franz, Gregory J. Martin, Zachary Peskowitz and Travis N. Ridout (2021). "Political Advertising Online and Offline." *American Political Science Review*. https://doi.org/10.1017/S0003055420000696

**Replication archive:** https://doi.org/10.7910/DVN/IR9XGC (American Political Science Review Dataverse). Terms of use: "This dataset not to be distributed/posted outside of the Harvard Dataverse. All downloads should take place directly on Harvard Dataverse to ensure data integrity."

**Task in the book:** Ad tone (Promote, Contrast, Attack). **Language:** English (123 ads in Spanish).

## What is here

The terms of the replication archive do not allow the ad texts to be posted elsewhere, so this folder contains the labels we used, the identifiers needed to recover the texts from the archive, and the code that rebuilds the spreadsheet the notebooks and scripts read.

- `fowler_ads_labels.csv`: 14,445 rows, one per ad in the order used in the book. `row_id` is the 0-based row number; `text_hash` is the md5 of the text cell; `source` is `fb` (Facebook) or `tv`; `page_id` and `snapshot_id` identify the ad in the archive (`page_id` is `TV` for television ads); `translated_in_en_file` marks the 123 Spanish-language ads that were machine-translated for the encoder run (see below). The remaining columns are the human codes: `ad_tone` with its three indicator columns, the four `goal_*` columns and the thirteen `iss_*` issue columns, and `label_main`, which equals `ad_tone`.
- `merge_texts.R` and `merge_texts.py`: rebuild `fowler_ads_text_labels.xlsx` from the archive.

**Classes (`label_main`):** Promote: 10,816, Contrast: 2,563, Attack: 1,066. N = 14,445.

## Rebuilding the texts

1. Download `ads_online_offline_replication.tar.gz` from the archive and extract it.
2. `Rscript merge_texts.R /path/to/ads_online_offline_replication/data` writes `fowler_ads_rebuilt_text.csv` (needs R with `dplyr`). The text of an ad is the concatenation, separated by one space, of the distinct non-missing text features the archive stores for it (Facebook creative body, image text, video transcript, video frame text), grouped by `page_id` and `snapshot_id`, which is the archive's own recipe in `read_ad_features.R` with repeated segments kept once.
3. `python merge_texts.py` joins the texts to the labels, checks every text against `text_hash`, and writes `fowler_ads_text_labels.xlsx` with the columns `source`, `text`, the codes and `label_main`. On the archive version of August 2020 all 14,445 texts match.

The decoder scripts read `fowler_ads_text_labels.xlsx`. The encoder notebook read `fowler_ads_text_labels_en.xlsx`, a copy in which the 123 ads with `translated_in_en_file = 1` (113 television, 10 Facebook) carry an English machine translation instead of the Spanish original; the labels are the same. To rerun the encoder, translate those rows or point the notebook at the untranslated file.
