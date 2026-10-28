# Foy-Sutherland row-level files

`foy_predictions.csv` and `foy_covariates.csv` have one row per row of `redbox_text_labels.xlsx`, in the same order. `row_id` is the 0-based row number in the spreadsheet and `text_hash` the md5 of the `text` cell as a UTF-8 string. Merge on `row_id`; `text_hash` is not unique because the same message was sometimes posted in more than one race (59 texts over 65 rows).

## foy_predictions.csv (910 rows)

- `row_id`, `text_hash`.
- `label_main`: the human label (Negative, Contrast, Positive).
- `enc_roberta`: placeholder; `chapter5_downstream/dsl_ensemble/foy_sutherland/01_build_sample_foy.py` fills it from `foy_encoder_oof_predictions.csv`.
- For each of the ten decoder configurations (`gemma_zs`, `gemma_fs`, `llama_zs`, `llama_fs`, `mistral_zs`, `mistral_fs`, `gpt5_zs`, `gpt5_fs`, `gptmini_zs`, `gptmini_fs`; `zs` zero-shot, `fs` few-shot): the label with a strict plurality among the valid labels of the configuration's three runs, empty when there is none, and a `<config>_disagree` flag equal to 1 when the three runs did not all give the same valid label. Three cells are empty, all in mistral_fs (rows 87, 264, 676). Unparseable answers occurred in mistral_fs (18 to 20 per run) and once in gptmini_fs.

Rows where the three runs disagreed: gemma_zs 7, gemma_fs 8, llama_zs 3, llama_fs 11, mistral_zs 2, mistral_fs 53, gpt5_zs 45, gpt5_fs 11, gptmini_zs 71, gptmini_fs 27.

The per-run predictions behind these columns are in `results/foy_sutherland/decoders/`; the model ids and decoding settings are in `chapter4_decoders/README.md`.

## foy_covariates.csv (910 rows)

The rows map positionally onto the 910 tone-coded messages of `JOP Paper Master Data.csv` in the replication archive. Candidate-level variables come from `JOP Paper Regression Analysis.xlsx`, matched on candidate name, state, cycle and chamber; candidate-cycles not in that file, which covers the 2018, 2020 and 2022 federal nominees, were filled from `Original DIME Data.csv`.

Message level, from the master file: `master_row` (0-based row in that file), `cycle`, `state`, `district`, `office_type` (House 724, Senate 157, Governor 20, Mayor 6, City Council 3), `candidate`, `stage` (general, primary, special and runoff variants), `incumbent_challenger` (Challenger 520, Incumbent 269, Open Seat 121), `won_lost`, `personal_microsite` (Personal, the candidate's own site, 367; Microsite 543), `redbox_flag` (1 for 897 rows), `date_raw` (day and month; the year is `cycle`), `self_opponent` (the second annotation in the spreadsheet: Opponent 521, Both 218, Self 161).

Candidate level, from the regression file (720 rows): `bonica_rid`, `party` (DIME codes: 100 Democrat, 200 Republican, 328 Independent), `democrat` (competing as a Democrat), `incumbent` (hand-coded, including redistricted members), `cand_gender`, `cfscore`, `abs_cf`, `competitive` (coded for the 2018 cycle only in the source), `competitive_broad`, `quality_candidate`, `party_target`, `party_spend`, `party_redbox`, `candidate_redbox`. Rows filled from DIME (180) carry `bonica_rid`, `party` and `cand_gender` only.

`dime_recipient_cfscore`: `recipient.cfscore` from the DIME file for every matched candidate (820 rows). `cfscore` is the value in the regression file, which its codebook describes as hand-adjusted; use `cfscore` and `abs_cf` to reproduce the paper and `dime_recipient_cfscore` for the value in the DIME file.

Ad-spend block, from the master file: `adtime_candidate`, `total_spend`, `positive_spend`, `contrast_spend`, `negative_spend`, `pct_negative_contrast`, `pct_negative`, and the `_ext` versions for outside groups. Filled for 169 rows, almost all from the 2020 cycle.

`covar_source`: which file filled the row. Party is filled for 900 rows (D 690, R 206, Independent 4); the ten rows without a candidate match are 2023 municipal races and one 2020 House primary candidate.
