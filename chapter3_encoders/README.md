# Chapter 3: fine-tuned encoders

One folder per task. Each notebook fine-tunes one encoder with ten independent runs of 10-fold cross-validation, writes one `<task>_results_10_<timestamp>.txt` per run (per-class and overall F1, precision and recall, averaged over the ten folds) and a `<task>_final_summary_<timestamp>.txt` with the means and standard deviations across the ten runs. Those files, as produced for the book, are in `results/<task>/encoders/`. The notebooks import `helper_functions.py` from their own folder and read the spreadsheet from `../../data/<task>/`.

## Which notebook produced which cell

The encoder table of Section 3.7 reports macro F1 (mean and SD across the ten runs) for the large model on all twelve tasks, and for the base models on seven. The per-class table of Section 3.7 reports the large model's per-class F1; ParlaCAP has its own per-class table.

| Folder | Large model (table columns 1–4) | Base model | BERT-base |
|---|---|---|---|
| `erhard_popbert` | `popbert_roberta.ipynb` (xlm-roberta-large) | `popbert_roberta-base.ipynb` (xlm-roberta-base) | `popbert_bert.ipynb` (bert-base-multilingual-uncased) |
| `parlacap` | `parlacap.ipynb` (xlm-roberta-large) | | |
| `heseltine` | `poltext_roberta.ipynb` (xlm-roberta-large) | `poltext_roberta-base.ipynb` (xlm-roberta-base) | `poltext_bert.ipynb` (bert-base-multilingual-uncased) |
| `proksch` | `sentiment_roberta.ipynb` (roberta-large) | | |
| `fowler_ads` | `advertising_roberta.ipynb` (roberta-large) | | |
| `vanderveen_populism` | `vanderveen_populism.ipynb` (roberta-large) | `populism_roberta-base.ipynb` (roberta-base) | `populism_bert.ipynb` (bert-base-uncased) |
| `ballard_incivility` | `rhetoric_roberta.ipynb` (roberta-large) | | |
| `foy_sutherland` | `workinghand_roberta.ipynb` (roberta-large) | `workinghand_roberta-base.ipynb` (roberta-base) | `workinghand_bert.ipynb` (bert-base-uncased) |
| `kostovicova_paskhalis` | `gender_roberta.ipynb` (xlm-roberta-large) | `gender_roberta-base.ipynb` (xlm-roberta-base) | `gender_bert.ipynb` (bert-base-multilingual-uncased) |
| `dietrich` | `aidmentions_roberta.ipynb` (xlm-roberta-large) | | |
| `goes_chapman` | `goes_chapman_articleiv.ipynb` (roberta-large) | `articleiv_roberta-base.ipynb` (roberta-base) | `articleiv_bert.ipynb` (bert-base-uncased) |
| `trubowitz_watanabe` | `geothreats_roberta.ipynb` (roberta-large) | `geothreats_roberta-base.ipynb` (roberta-base) | `geothreats_bert.ipynb` (bert-base-uncased) |

`goes_chapman/goes_modernbert_oof.ipynb` and `helper_functions_modernbert.py` are the ModernBERT-large comparison mentioned in a footnote of Section 3.7; its results are not in the tables.

## Hardware

One GPU with 16 GB or more of memory. The 512-token tasks (Foy-Sutherland, Goes-Chapman, Kostovicova-Paskhalis, ParlaCAP) use batch size 16 to fit. Each notebook's first cell runs `nvidia-smi`.

## Out-of-fold predictions

These notebooks do not keep row-level predictions. The seeded single-pass notebooks that do, for the three Chapter 5 tasks, are in `chapter5_downstream/dsl_ensemble/`.
