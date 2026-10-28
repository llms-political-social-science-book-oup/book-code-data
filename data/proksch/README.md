# Sentiment of 2010 State of the European Union debate paragraphs

**Source:** Proksch, Sven-Oliver, Will Lowe, Jens Wäckerle and Stuart Soroka (2019). "Multilingual Sentiment Analysis: A New Approach to Measuring Conflict in Legislative Speeches." *Legislative Studies Quarterly* 44(1): 97–131. https://doi.org/10.1111/lsq.12218

**Replication archive:** https://doi.org/10.7910/DVN/ALFLK6 (Harvard Dataverse, CC0 1.0)

**Task in the book:** Sentiment, five-point scale. **Language:** English.

## Files

- `soteu2010_text_labels.xlsx`: the spreadsheet read by the notebooks and scripts. 301 rows. Columns: `Text`, `coding_a`, `coding_b`, `coding_c`, `label_main`. The code reads `text` and `label_main`.
- `ORIGINAL_Replication_Readme.pdf`: the README of the replication archive.

**Classes (`label_main`):** 4.0: 50, 2.0: 50, 1.0: 47, 2.5: 40, 3.0: 32, 1.5: 26, 4.5: 25, 3.5: 19, 5.0: 12. N = 301.

## How the spreadsheet was built

Built from `1_coding_a_2010`, `1_coding_b_2010` and `1_coding_c_2010` in the archive, joined on the paragraph number. Each paragraph was scored by two of three coders on a 1–5 scale; `label_main` is their mean, so it takes nine values (1, 1.5, ..., 5). The notebooks and scripts collapse it to five classes.
