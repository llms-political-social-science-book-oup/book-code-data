# Appendix scripts

The two workflow scripts printed in the chapter appendices, as printed there, plus the helper module the first one imports.

| File | Appendix | What it does |
|---|---|---|
| `appendix_3A_roberta_workflow.py` | 3.A | Fine-tunes RoBERTa-large on the van der Veen (2024) populism sentences with ten-times repeated 10-fold cross-validation, saves the out-of-fold predictions, fine-tunes a final model on all the data, and labels new text. The nine blocks are the listings of the appendix in order. |
| `helper_functions.py` | 3.A | Progress and plotting helpers imported by the script (`good_update_interval`, `format_time`, `plot_distribution`). The same file sits next to every encoder notebook. |
| `appendix_4A_decoder_workflow.py` | 4.A | Labels the same sentences with a prompted decoder through an OpenAI-compatible API, scores three runs against the human labels, combines them by majority vote, and saves predictions and metrics. |

## Running them

Both scripts read `vanderveen_populism_text_labels.xlsx` from the working directory, as printed in the book. Copy it from `../data/vanderveen_populism/` into this folder, or run the scripts from that folder:

```
cp ../data/vanderveen_populism/vanderveen_populism_text_labels.xlsx .
python appendix_3A_roberta_workflow.py
export DEEPINFRA_API_KEY=...   # or OPENAI_API_KEY for OpenAI models
python appendix_4A_decoder_workflow.py
```

`appendix_3A_roberta_workflow.py` needs a GPU. On Google Colab's free T4 runtime one 10-fold run takes well under an hour and the full ten-times repeated protocol (`n_runs = 10`, 100 fine-tuned models) takes most of a day. Set `n_runs = 1` for a first pass. It writes one `vanderveen_results_run<k>.txt` per run, `vanderveen_roberta_cv_results.csv`, `vanderveen_roberta_oof_predictions.csv`, and the final model in `roberta_populism_final/`.

`appendix_4A_decoder_workflow.py` needs no GPU, only an API key in the environment variable named in Block 2. It makes one request per sentence per run, 3 x 3,624 requests in all, which takes a few hours at one request at a time and costs a dollar or two with an open-weight model on DeepInfra. It writes one CSV per run, the majority-vote file and a metrics JSON into `results_populism_baseline/`.

## Expected output

- Appendix 3.A: macro F1 0.742 with a standard deviation of 0.004 across the ten runs; per-class F1 0.671 (neutral), 0.705 (pluralist), 0.849 (populist). This is the RoBERTa-large row for van der Veen (2024) in the encoder table of Section 3.7.
- Appendix 4.A: macro F1 0.606 with a standard deviation of 0.001 across the three runs; per-class F1 0.553 (neutral), 0.567 (pluralist), 0.700 (populist). This is the zero-shot Llama cell for van der Veen (2024) in the decoder table of Section 4.6; the script's `model_name`, `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8`, is the one used by the scripts in `chapter4_decoders/vanderveen_populism/zero_shot/llama/`.
