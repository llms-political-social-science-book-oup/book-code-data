# Negativity in politicians' tweets and news text

**Source:** Heseltine, Michael and Bernhard Clemm von Hohenberg (2024). "Large Language Models as a Substitute for Human Experts in Annotating Political Text." *Research & Politics*.

**Replication archive:** https://doi.org/10.7910/DVN/V2P6YL (Harvard Dataverse, CC0 1.0)

**Task in the book:** Negativity (binary). **Language:** English, German, Italian, Spanish.

## Files

- `heseltine_annotation_text_labels.xlsx`: the spreadsheet read by the notebooks and scripts. 2,195 rows. Columns: `source`, `text`, `political`, `negativity_binary`, `negativity_3way`, `ideology`, `label_main`. The code reads `text` and `label_main`.
- `ORIGINAL_data_info_GPT_ResPol.txt`: the README of the replication archive.

**Classes (`label_main`):** 0: 1,569, 1: 626. N = 2,195.

## How the spreadsheet was built

Built from the eight validation files in `Python.rar` (tweets from the United States, Chile, Germany and Italy, and a sample of United States news articles). One row per text with the human labels for the four annotation tasks; `label_main` is the binary negativity label (1 = negative).
