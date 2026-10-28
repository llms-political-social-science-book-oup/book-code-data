# Trubowitz and Watanabe row-level files

`trubowitz_predictions.csv` and `trubowitz_covariates.csv` have one row per row of `trubowitz_gti_text_labels.xlsx`, in the same order: rows 0 to 849 are the domestic sample and rows 850 to 1699 the foreign sample. `row_id` is the 0-based row number in the spreadsheet and `text_hash` the md5 of the `text` cell as a UTF-8 string. Merge on `row_id`. The texts are the article summaries as stored in the archive's coded CSVs, capped at 250 characters; the full summaries are in `corpus_nytimes_summary.RDS`, keyed by `docid`.

## trubowitz_predictions.csv (1,700 rows)

- `row_id`, `text_hash`.
- `label_main`: the human label (Yes, No, Unclear).
- `enc_roberta`: placeholder; `chapter5_downstream/dsl_ensemble/trubowitz_watanabe/01_build_sample_trubowitz.py` fills it from `trubowitz_encoder_oof_predictions.csv`.
- For each of the ten decoder configurations (`gemma_zs`, `gemma_fs`, `llama_zs`, `llama_fs`, `mistral_zs`, `mistral_fs`, `gpt5_zs`, `gpt5_fs`, `gptmini_zs`, `gptmini_fs`; `zs` zero-shot, `fs` few-shot): the label with a strict plurality among the valid labels of the configuration's three runs, empty when there is none, and a `<config>_disagree` flag equal to 1 when the three runs did not all give the same valid label. Fifty-two cells are empty (gemma_zs 1, gemma_fs 4, llama_fs 1, mistral_fs 4, gpt5_zs 7, gpt5_fs 4, gptmini_zs 18, gptmini_fs 13), almost all three-way splits; unparseable answers occurred in one gemma_fs run (19 rows).

Rows where the three runs disagreed: gemma_zs 35, gemma_fs 90, llama_zs 5, llama_fs 114, mistral_zs 33, mistral_fs 175, gpt5_zs 91, gpt5_fs 169, gptmini_zs 252, gptmini_fs 314.

The per-run predictions behind these columns are in `results/trubowitz_watanabe/decoders/`; the model ids and decoding settings are in `chapter4_decoders/README.md`.

## trubowitz_covariates.csv (1,700 rows)

Rows 0 to 849 are `domestic_coded.csv` and rows 850 to 1699 `foreign_coded.csv` from the replication archive, in order. All columns are carried from those files.

- `sample` (domestic_US, foreign), `source_file`, `source_row` (0-based row in that file).
- `docid`: article id in `corpus_nytimes_summary.RDS`.
- `year` (1861 to 2017), `decade`. The sample has 100 articles per decade, 50 from each file.
- `country_class`: the country assigned by the authors' newsmap classifier (us for every domestic row); `country_name` (foreign file only); `country_confidence_fit`.
- `lss`: the paper's Latent Semantic Scaling threat score (NA for 61 rows); `lss_threat`: the binary threat classification carried in the source files (NA for the same rows), the output of the authors' pipeline rather than a threshold on `lss`.
- `exclude` (foreign file, all FALSE), `coded_raw` (the domestic file's original 0/1/3 code), `country_name_coded` (the foreign file's human check of the country assignment: Yes 477, No 273, Unclear 99, two other values as in the source).
- `covar_source`.
