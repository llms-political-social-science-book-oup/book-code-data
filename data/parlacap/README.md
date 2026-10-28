# ParlaCAP: policy topics of parliamentary speeches

**Source:** Pungeršek, Taja Kuzman, Peter Rupnik, Daniela Širinić and Nikola Ljubešić (2026). "Supercharging Agenda Setting Research: The ParlaCAP Dataset of 28 European Parliaments and a Scalable Multilingual LLM-Based Classification." arXiv:2602.16516.

**Task in the book:** Comparative Agendas Project major topic (22 classes). **Language:** English, Bosnian, Croatian, Serbian.

## Not included

The ParlaCAP texts, labels and every file derived from them are not in this repository. The human-labeled test sets are available on request from the corresponding authors of the ParlaCAP paper, who withhold them to keep them out of LLM training data. The dataset used in the book has 3,443 speeches with one Comparative Agendas Project major topic each (21 topics plus Other): 824 from Bosnia and Herzegovina, 876 from the United Kingdom, 869 from Croatia and 874 from Serbia.

Our notebook and scripts for this task are included and run once the data are obtained. Save the speeches as `parlacap_text_labels.xlsx` in this folder with three columns, `lang`, `text` and `label_main` (the topic label as a string, for example `Government Operations`), one row per speech. The encoder notebook is in `chapter3_encoders/parlacap/` and the decoder scripts in `chapter4_decoders/parlacap/`; both read the file at this path.

`results/parlacap/` contains the aggregate metrics of every run (macro F1, per-class F1, precision and recall) but not the per-row predictions, which would reproduce the texts and labels.
