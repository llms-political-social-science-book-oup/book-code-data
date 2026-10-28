# Populist, pluralist and neutral sentences in governor and presidential speeches

**Source:** van der Veen, Olaf, Semir Dzebo, Levi Littvay, Kirk Hawkins and Oren Dar (2024). "Classifying Populist Language in American Presidential and Governor Speeches Using Automatic Text Analysis." arXiv:2408.15213.

**Replication archive:** https://doi.org/10.7910/DVN/ZOHMVO (Harvard Dataverse, CC0 1.0)

**Task in the book:** Populism (populist, pluralist, neutral). **Language:** English.

## Files

- `vanderveen_populism_text_labels.xlsx`: the spreadsheet read by the notebooks and scripts. 3,624 rows. Columns: `source`, `text`, `label_main`. The code reads `text` and `label_main`.
- `vanderveen_predictions.csv`: row-level predictions of the ten decoder configurations (majority vote over three runs, with disagreement flags) for every row of the spreadsheet; `vanderveen_covariates.csv`: covariates assembled for the Chapter 5 analyses; `README_vanderveen_row_level.md`: column definitions of both files. Rows align to the spreadsheet through `row_id` (0-based row number) and `text_hash` (md5 of the text cell).

**Classes (`label_main`):** populist: 1,456, neutral: 1,122, pluralist: 1,046. N = 3,624.

## How the spreadsheet was built

Built from the authors' hand-coded training sentences: 3,543 sentences from governor speeches (2010–2018) and 81 sentences from 2016 presidential primary candidates (28 presidential rows with empty text were dropped). `source` records which corpus a sentence comes from; `label_main` is the human code.
