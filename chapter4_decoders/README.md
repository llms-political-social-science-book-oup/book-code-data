# Chapter 4: prompted decoders and QLoRA fine-tuning

## Prompted decoders (Section 4.6)

`<task>/zero_shot/<model>/` and `<task>/few_shot/<model>/` hold the scripts behind the decoder table of Section 4.6: five models, two prompting conditions, three runs per cell, one script per run (360 scripts). Each script reads the task's spreadsheet from `../../../../data/<task>/`, sends every text to the model, parses the answer, saves the raw responses and predictions to `<model>_<task>_preds[_fs]_<run>.csv` and the metrics to `<model>_<task>_metrics[_fs]_<run>.json`, in a `results_*` folder created next to the script. The files produced for the book are in `results/<task>/decoders/`.

| Folder | Model id in the scripts | Provider | Name in the book |
|---|---|---|---|
| `gemma` | `google/gemma-4-31B-it` | DeepInfra | Gemma |
| `llama` | `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | DeepInfra | Llama |
| `mistral` | `mistralai/Mistral-Small-3.2-24B-Instruct-2506` | DeepInfra | Mistral |
| `gpt5` | `gpt-5.5` | OpenAI | GPT-5.5 |
| `gpt_mini` | `gpt-5.4-mini` | OpenAI | GPT-5.5-mini |

Open-weight models are called with temperature 0 and top-p 1. GPT models were called with the API's default sampling settings. Keys are read from `DEEPINFRA_API_KEY` and `OPENAI_API_KEY`.

Within a task, the fifteen zero-shot scripts share one system prompt and the fifteen few-shot scripts share another; the scripts differ in the client, model id and run number. The prompts are in `prompts/<task>_zero_shot.txt` and `prompts/<task>_few_shot_cot.txt`, with the user-message template at the end of each file. The few-shot prompts carry labeled examples with reasoning chains taken from each dataset.

## QLoRA fine-tuning (Section 4.9)

`qlora/<task>/` holds the notebooks behind the QLoRA table of Section 4.9: Gemma-4 31B for five tasks and Mistral-Small 3.2 24B for Heseltine et al., fine-tuned with 4-bit NF4 quantization, LoRA adapters of rank 16 and alpha 32 on the attention projections, learning rate 2e-4, five-fold stratified cross-validation (seed 42) with early stopping on validation macro F1, and single-token scoring of the class words at inference. Each notebook reads its spreadsheet from `../../../data/<task>/` and writes `cv_results_running.csv` and `cv_results_final.csv` into a `results_qlora_*` folder.

The epoch cap was selected per task by cross-validated macro F1 from two settings: 6 epochs with patience 2 and batch size 16 (the notebooks with the `_6epochs` suffix, and `poltext_qlora_mistralsmall24b.ipynb`; outputs in `results/<task>/qlora/run1/`), and 10 epochs with patience 3 and batch size 2 with gradient accumulation of 8 (the notebooks without the suffix; outputs in `results/<task>/qlora/run2_10epochs/`). The table reports the selected setting for each task:

| Task | Base model | Epoch cap | Macro F1 |
|---|---|---|---|
| `heseltine` | Mistral-Small 3.2 24B | 6 | 0.875 |
| `vanderveen_populism` | Gemma-4 31B | 6 | 0.751 |
| `foy_sutherland` | Gemma-4 31B | 10 | 0.919 |
| `kostovicova_paskhalis` | Gemma-4 31B | 6 | 0.513 |
| `goes_chapman` | Gemma-4 31B | 6 | 0.784 |
| `trubowitz_watanabe` | Gemma-4 31B | 10 | 0.644 |

The Mistral notebook tokenizes with `mistral-common`. Every notebook fits on one GPU with 48 GB or more; `google/gemma-4-31b-it` is gated on Hugging Face and needs an accepted license and an `HF_TOKEN`. The fold adapters are not in the repository.
