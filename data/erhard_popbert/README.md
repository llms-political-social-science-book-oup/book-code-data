# PopBERT: populism in Bundestag speeches

**Source:** Erhard, Lukas, Sara Hanke, Uwe Remer, Agnieszka Falenska and Raphael Heiko Heiberger (2025). "PopBERT. Detecting Populism and Its Host Ideologies in the German Bundestag." *Political Analysis* 33(1): 1–17. Preprint: arXiv:2309.14355.

**Replication archive:** https://doi.org/10.7910/DVN/HZMSUR (Harvard Dataverse, CC0 1.0)

**Task in the book:** Populism (binary). **Language:** German.

## Files

- `popbert_text_labels.xlsx`: the spreadsheet read by the notebooks and scripts. 8,795 rows. Columns: `text`, `anti_elitism_coder0`, `anti_elitism_coder1`, `anti_elitism_coder2`, `anti_elitism_coder3`, `anti_elitism_coder4`, `anti_elitism_n`, `anti_elitism`, `people_centrism_coder0`, `people_centrism_coder1`, `people_centrism_coder2`, `people_centrism_coder3`, `people_centrism_coder4`, `people_centrism_n`, `people_centrism`, `left_wing_coder0`, `left_wing_coder1`, `left_wing_coder2`, `left_wing_coder3`, `left_wing_coder4`, `left_wing_n`, `left_wing`, `right_wing_coder0`, `right_wing_coder1`, `right_wing_coder2`, `right_wing_coder3`, `right_wing_coder4`, `right_wing_n`, `right_wing`, `label_main`. The code reads `text` and `label_main`.

**Classes (`label_main`):** 0: 5,969, 1: 2,826. N = 8,795.

## How the spreadsheet was built

Built from `labelled_data` in the archive. Each sentence carries five coders' booleans on four dimensions (anti-elitism, people-centrism, left-wing, right-wing). `label_main` is 1 when at least two of the five coders marked anti-elitism or people-centrism, 0 otherwise; the per-coder columns and per-dimension counts are kept.
