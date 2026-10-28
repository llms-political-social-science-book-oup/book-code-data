# Chapter 5: error structure and downstream estimates

The scripts behind Sections 5.5 and 5.6 for the three tasks they use: Ballard et al. (2023), Foy-Sutherland (2025) and Trubowitz-Watanabe (2021). Each task's pipeline reads the row-level files in `data/<task>/` (decoder predictions, encoder out-of-fold predictions, covariates) and writes its outputs into the folder it runs from. The outputs produced for the book are in `results/<task>/downstream/`.

## Run order

```
dsl_ensemble/<task>/    00  <encoder>_oof.ipynb   seeded single-pass RoBERTa-large, writes <task>_encoder_oof_predictions.csv (already in data/<task>/)
                        01  build sample          merges predictions, encoder OOF and covariates -> <task>_analysis_sample.csv
                        02  multiverse sweep      naive regressions for every configuration and gold budget -> <task>_sweep_results.csv
error_structure/<task>/ 03  error structure       pairwise error overlap, per-class miss rates, disagreement diagnostics (Section 5.5)
dsl_ensemble/<task>/    04  forest plot           (Ballard only) naive forest plot
                        05  DSL correction        design-based supervised learning estimates -> <task>_dsl_results.csv, <task>_dsl_summary.csv
                        06  forest, all           DSL versus naive forest plots at each gold budget (Section 5.6)
```

Step 03 reads `<task>_analysis_sample.csv` from the task's `dsl_ensemble` folder, so run 01 first. Steps 05 and 06 need 01 and 02. The scripts use pandas, numpy, statsmodels, scikit-learn and matplotlib.

## Figures

`error_structure/figures/` holds the three panels of Section 5.5 as printed (`error_overlap_panel.pdf`, `class_accuracy_heatmap.pdf`, `per_class_rescue.pdf`) and the per-task anatomy and overlap figures, assembled from the CSV outputs of step 03. The forest and lottery figures of Section 5.6 are in `results/<task>/downstream/`.

## Analysis samples

Ballard et al.: 2,887 of 2,919 tweets (Democrats and Republicans with complete party, chamber and gender). Foy-Sutherland: 910 messages, outcome negative versus other, coefficient of interest incumbency. Trubowitz-Watanabe: 1,700 articles, outcome threat versus other, coefficient of interest year. The settings are at the top of each `01` and `05` script.
