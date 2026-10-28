# Results

The per-run outputs behind every table cell, one folder per task, plus the cross-dataset tables built from them.

## Cross-dataset tables

- `ENCODER_RESULTS_all.csv` / `.md`: every encoder run in Section 3.7 (overall and per-class rows; means and standard deviations across the ten runs).
- `DECODER_RESULTS_all.csv` / `.md`: every decoder cell in Section 4.6 (mean and population standard deviation of macro F1 over the three runs, number of valid and invalid outputs).
- `DECODER_PERCLASS_all.csv` / `.md`: per-class precision, recall and F1 for every decoder cell.
- `DECODER_vs_ENCODER_perclass_delta.md`: per-class comparison of the best decoder and the best encoder per task.
- `MASTER_cross_dataset_summary.csv`: best encoder and best decoder per task.

## Per-task folders

`encoders/<model>/`: one `*_results_10_<timestamp>.txt` per run (JSON: per-class F1, precision and recall averaged over the ten folds, with the hyperparameters) and one `*_final_summary_<timestamp>.txt` (JSON with the list of runs it averages and the cross-run means and standard deviations), plus a short `.rtf` summary.

`decoders/<zero_shot|few_shot>/<model>/`: for each of the three runs, `*_metrics_<k>.json` (per-class precision, recall and F1, macro F1, valid and invalid counts) and `*_preds_<k>.csv.gz` (one row per text: `text`, `true_label`, `predicted`, `raw_response`; gzip-compressed, `pandas.read_csv` opens it directly). Exceptions:

- `fowler_ads`: the prediction files carry `row_id` instead of `text`; `row_id` is the row of `data/fowler_ads/fowler_ads_labels.csv`.
- `parlacap`: metrics files only.
- `dietrich`: one run with each GPT model; the GPT-5.5 few-shot file holds the raw model responses for the first 37,469 of the 52,744 texts, in order (`gpt5_aidmentions_raw_responses_fs_1_partial.jsonl.gz`).
- Proksch et al.: the five-point scale after collapsing the nine coder-mean values.

`qlora/run1/` and `qlora/run2_10epochs/`: `cv_results_final.csv` (one row per fold: best epoch, training loss, macro, weighted and per-class F1), `cv_results_running.csv`, and an `.rtf` summary. `chapter4_decoders/README.md` says which run the table reports.

`downstream/`: the analysis samples, sweep results, DSL results and figures of Chapter 5 for the three tasks it uses, and the single-pass encoder run that produced the out-of-fold predictions.

`synthesis/`: per-task synthesis tables of all models (CSV and Markdown); for ParlaCAP also the confusion matrices.

Only the runs behind the tables are included.
