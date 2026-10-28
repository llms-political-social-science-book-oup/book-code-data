# Ballard et al. row-level files

`ballard_predictions.csv` and `ballard_covariates.csv` have one row per row of `incivility_tweets_text_labels.xlsx`, in the same order. `row_id` is the 0-based row number in the spreadsheet and `text_hash` the md5 of the `text` cell as a UTF-8 string. The two files merge 1:1 on `row_id`.

## ballard_predictions.csv (2,919 rows)

- `row_id`, `text_hash`.
- `label_main`: the human label (0 civil, 1 uncivil).
- `enc_roberta`: placeholder; `chapter5_downstream/dsl_ensemble/ballard_incivility/01_build_sample.py` fills it from `ballard_encoder_oof_predictions.csv`.
- For each of the ten decoder configurations (`gemma_zs`, `gemma_fs`, `llama_zs`, `llama_fs`, `mistral_zs`, `mistral_fs`, `gpt5_zs`, `gpt5_fs`, `gptmini_zs`, `gptmini_fs`; `zs` zero-shot, `fs` few-shot): the majority label over the configuration's three runs, and a `<config>_disagree` flag equal to 1 when the three runs were not unanimous. Every run produced a valid label on every row, so every vote is 3-of-3 or 2-of-3.

Rows where the three runs disagreed: gemma_zs 68, gemma_fs 55, llama_zs 32, llama_fs 191, mistral_zs 19, mistral_fs 157, gpt5_zs 244, gpt5_fs 212, gptmini_zs 443, gptmini_fs 342.

The per-run predictions behind these columns are in `results/ballard_incivility/decoders/`; the model ids and decoding settings are in `chapter4_decoders/README.md`.

## ballard_covariates.csv (2,919 rows)

Each tweet was matched by text to `combined_training_ab.csv` in the replication archive, which gives the handle and tweet id. The handle was matched to `US Congress Handles Master List.csv`, which gives the member, party, chamber, state and gender. The member's ICPSR id was matched to Voteview's `HSall_members2021.csv` (Congresses 111 to 116), which gives `bioguide_id` and the first-dimension DW-NOMINATE score from the member's most recent Congress in that window.

- `screen_name`: Twitter handle, as in the archive.
- `tweet_id_raw`: tweet id as stored in the archive; many values are in scientific notation or 0, so `screen_name` is the usable identifier.
- `member_name`, `icpsr`, `bioguide_id`, `party`, `chamber`, `gender`, `state`, `dw_nominate`.
- `covar_source`: which merge steps filled the row.

Party, chamber and gender are filled for 2,915 rows and the member-level fields for 2,906 (581 members). Four rows have no handle in the archive and carry no covariates. Nine tweets come from the @GOPLeader institutional account, held by three members over the period; they carry party, chamber and gender only.
