# LLMs in Political and Social Science: Principles and Applications of Transformer Models

Joan C. Timoneda and Sebastián Vallejo Vera

Data, code and per-run results for the twelve annotation tasks tested in the book, the appendix workflow scripts, and the downstream analyses of Chapter 5. Published by Oxford University Press (link TBD).

## What is here

```
appendices/            the two workflow scripts printed in Appendices 3.A and 4.A, with their helper module
chapter3_encoders/     one folder per task: the notebooks that fine-tuned RoBERTa, XLM-R and BERT (Section 3.7)
chapter4_decoders/     one folder per task: the zero-shot and few-shot scripts for the five decoders (Section 4.6),
                       the prompts (prompts/), and the QLoRA fine-tuning notebooks (qlora/, Section 4.9)
chapter5_downstream/   error-structure and DSL/ensemble scripts for the three Chapter 5 tasks (Sections 5.5 and 5.6)
data/                  the labeled text used in the book, one folder per task, with provenance and license
results/               the per-run outputs behind every table cell, one folder per task, and the cross-dataset tables
requirements.txt       Python packages and the versions used
LICENSE                MIT for the code; the datasets keep the licenses of their archives
```

Each folder has its own README with the mapping from files to tables.

## Datasets

| Folder | Source | N | Classes | Redistributed | License of the archive |
|---|---|---|---|---|---|
| `erhard_popbert` | Erhard, Hanke, Remer, Falenska and Heiberger (2025), *Political Analysis*; archive doi:10.7910/DVN/HZMSUR | 8,795 | 2 | full | CC0 1.0 |
| `parlacap` | Pungeršek, Rupnik, Širinić and Ljubešić (2026), arXiv:2602.16516 | 3,443 | 22 | not included | available from the authors |
| `heseltine` | Heseltine and Clemm von Hohenberg (2024), *Research & Politics*; archive doi:10.7910/DVN/V2P6YL | 2,195 | 2 | full | CC0 1.0 |
| `proksch` | Proksch, Lowe, Wäckerle and Soroka (2019), *Legislative Studies Quarterly*, doi:10.1111/lsq.12218; archive doi:10.7910/DVN/ALFLK6 | 301 | 5 | full | CC0 1.0 |
| `fowler_ads` | Fowler, Franz, Martin, Peskowitz and Ridout (2021), *American Political Science Review*, doi:10.1017/S0003055420000696; archive doi:10.7910/DVN/IR9XGC | 14,445 | 3 | labels only | custom terms, no redistribution |
| `vanderveen_populism` | van der Veen, Dzebo, Littvay, Hawkins and Dar (2024), arXiv:2408.15213; archive doi:10.7910/DVN/ZOHMVO | 3,624 | 3 | full | CC0 1.0 |
| `ballard_incivility` | Ballard, DeTamble, Dorsey, Heseltine and Johnson (2023), *Legislative Studies Quarterly*; archive doi:10.7910/DVN/2ET6VL | 2,919 | 2 | full | CC0 1.0 |
| `foy_sutherland` | Foy-Sutherland (2025), *Journal of Politics*; archive doi:10.7910/DVN/5DKNDD | 910 | 3 | full | CC0 1.0 |
| `kostovicova_paskhalis` | Kostovicova and Paskhalis (2021), *International Studies Quarterly*; archives doi:10.7910/DVN/FC6WAO and doi:10.7910/DVN/PMICO2 | 1,211 | 4 | full | CC0 1.0 |
| `dietrich` | Dietrich, Milner and Slapin (2020), *International Studies Quarterly*; archive doi:10.7910/DVN/ICTZ1A | 52,744 | 2 | full | CC0 1.0 |
| `goes_chapman` | Goes and Chapman (2024), *International Studies Quarterly*, doi:10.1093/isq/sqae048; archive doi:10.7910/DVN/U2DEKY | 700 | 2 | full | CC0 1.0 |
| `trubowitz_watanabe` | Trubowitz and Watanabe (2021), *International Studies Quarterly*, doi:10.1093/isq/sqab029; archive doi:10.7910/DVN/9QPZ43 | 1,700 | 3 | full | CC0 1.0 |

ParlaCAP is not included: the corresponding authors withhold the human-labeled test sets to keep them out of LLM training data and provide them on request; our code for it runs on the data once obtained. The Fowler et al. archive restricts distribution to Dataverse, so `data/fowler_ads/` holds the labels and identifiers with code that rebuilds the texts from the archive. Full citations, class counts and the construction of every spreadsheet are in `data/<task>/README.md`.

## How to run

Set up a Python 3.12 environment and install the packages:

```
pip install -r requirements.txt
```

The scripts read API keys from environment variables and contain none:

```
export DEEPINFRA_API_KEY=...   # Gemma, Llama and Mistral through DeepInfra
export OPENAI_API_KEY=...      # GPT-5.5 and GPT-5.5-mini
export HF_TOKEN=...            # gated Gemma weights, QLoRA notebooks only
```

Every script and notebook runs from its own folder and reads the data through relative paths into `data/`. Outputs are written next to the script. The encoder notebooks need one GPU with 16 GB or more; the QLoRA notebooks need one GPU with 48 GB or more and a Hugging Face token for the gated Gemma weights; the decoder scripts and the Chapter 5 scripts need no GPU.

### Chapter 3

`chapter3_encoders/<task>/` holds the notebooks that fine-tuned the large encoder (RoBERTa-large, or XLM-RoBERTa-large for the multilingual tasks) on every task and the base encoders on seven tasks, with ten independent runs of 10-fold cross-validation. They produce the overall and per-class encoder tables of Section 3.7, including the ParlaCAP per-class table. The run files are in `results/<task>/encoders/`.

### Chapter 4

`chapter4_decoders/<task>/zero_shot/` and `few_shot/` hold the 360 scripts behind the decoder table of Section 4.6: five models, two prompting conditions, three runs per cell. The prompts are in `chapter4_decoders/prompts/`. `chapter4_decoders/qlora/` holds the six QLoRA notebooks behind the table of Section 4.9. The run files are in `results/<task>/decoders/` and `results/<task>/qlora/`.

### Chapter 5

`chapter5_downstream/` holds the scripts for Ballard et al., Foy-Sutherland and Trubowitz-Watanabe: the seeded encoder runs that keep out-of-fold predictions, the analysis-sample builders, the error-overlap and per-class miss-rate computations (Section 5.5), and the DSL and ensemble estimates with their forest plots (Section 5.6). Their inputs are the row-level files in `data/<task>/`; their outputs are in `results/<task>/downstream/`.

## Appendices

`appendices/appendix_3A_roberta_workflow.py` (with `helper_functions.py`) and `appendices/appendix_4A_decoder_workflow.py` are the scripts printed in the chapter appendices. Both read `vanderveen_populism_text_labels.xlsx` from their working directory; copy it there from `data/vanderveen_populism/`.

- Appendix 3.A fine-tunes RoBERTa-large with ten-times repeated 10-fold cross-validation. One 10-fold run takes well under an hour on a Colab T4; the ten-times repeated protocol takes most of a day. Expected output: macro F1 0.742, standard deviation 0.004 across runs; per-class F1 0.671 (neutral), 0.705 (pluralist), 0.849 (populist).
- Appendix 4.A labels the same sentences with a prompted decoder three times and combines the runs by majority vote. It needs an API key and no GPU; three runs cost a dollar or two with an open-weight model. Expected output for the zero-shot Llama cell of Section 4.6: macro F1 0.606, standard deviation 0.001; per-class F1 0.553 (neutral), 0.567 (pluralist), 0.700 (populist).

## Citation

```
@book{timoneda2027llms,
  title     = {LLMs in Political and Social Science: Principles and Applications of Transformer Models},
  author    = {Timoneda, Joan C. and Vallejo Vera, Sebasti{\'a}n},
  publisher = {Oxford University Press},
  year      = {2027}
}
```

## Contact

Joan C. Timoneda, Purdue University, timoneda@purdue.edu

Sebastián Vallejo Vera, University of Western Ontario, sebastian.vallejo@uwo.ca
