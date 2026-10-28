# van der Veen et al. row-level files

`vanderveen_predictions.csv` and `vanderveen_covariates.csv` have one row per row of `vanderveen_populism_text_labels.xlsx`, in the same order: rows 0 to 80 are the presidential sentences and rows 81 to 3623 the governor sentences. `row_id` is the 0-based row number in the spreadsheet and `text_hash` the md5 of the `text` cell as a UTF-8 string. Merge on `row_id`; `text_hash` is not unique because some stock sentences recur (90 texts over 177 rows).

## vanderveen_predictions.csv (3,624 rows)

- `row_id`, `text_hash`.
- `label_main`: the human label (populist, pluralist, neutral).
- For each of the ten decoder configurations (`gemma_zs`, `gemma_fs`, `llama_zs`, `llama_fs`, `mistral_zs`, `mistral_fs`, `gpt5_zs`, `gpt5_fs`, `gptmini_zs`, `gptmini_fs`; `zs` zero-shot, `fs` few-shot): the label with a strict plurality among the valid labels of the configuration's three runs, empty when there is none, and a `<config>_disagree` flag equal to 1 when the three runs did not all give the same valid label. Seventeen cells are empty (gemma_fs 1, llama_fs 3, mistral_fs 3, gptmini_zs 10); gptmini_zs is the only configuration with unparseable answers.

Rows where the three runs disagreed: gemma_zs 58, gemma_fs 64, llama_zs 36, llama_fs 184, mistral_zs 36, mistral_fs 220, gpt5_zs 206, gpt5_fs 143, gptmini_zs 406, gptmini_fs 336.

The per-run predictions behind these columns are in `results/vanderveen_populism/decoders/`; the model ids and decoding settings are in `chapter4_decoders/README.md`.

## vanderveen_covariates.csv (3,624 rows)

- `source`: presidential or governor.
- `source_file`, `source_index`: the file in the replication archive the sentence comes from (`Importing/Output/pres_sentences.csv` or `Importing/Output/sentences_2010_2018.csv`) and the sentence's index there.
- `source_doc`: the speech document the sentence was extracted from, where the archive records one.
- `state`, `speaker`, `party`, `speech_type` (Famous, Campaign, State of the State, Ribbon cutting, International), `term_num`, `date_raw` (day and month as in the source), `year`.
- `covar_source`: how the row was filled.

Presidential rows (81): speaker, date and year come from the source document names (2016 primary speeches by Trump, Clinton, Sanders, Cruz, Kasich, Carson and Rubio, and the Republican Party platform); `party` is R or D by speaker.

Governor rows (3,543): the archive stores the pluralist and neutral sentences in two aggregate documents without speech or speaker markers, so only the 1,413 populist sentences, which come from per-speech documents, carry `source_doc`, `state`, `speech_type`, `speaker` (1,357 rows) and `term_num` (1,259 rows). Governor party is not coded in the archive. Analyses that condition on these covariates are therefore limited to the populist governor sentences or the presidential sample.
