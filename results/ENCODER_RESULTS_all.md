# Encoder results — all datasets

Fine-tuned encoder classifiers; metrics are the mean over 10 runs (SD in parentheses for F1). Macro/weighted F1 are unweighted/support-weighted averages across classes. Backbone is RoBERTa-large for English tasks and XLM-R-large for multilingual tasks (with -base and BERT/mBERT variants where available).


## American Politics


### Fowler et al. (2020) — Ad tone

| Model | Acc | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R |
|---|---|---|---|---|---|
| roberta-large | 0.908 | 0.825 (0.003) | 0.908 | 0.825 | 0.828 |

_Per-class F1 (SD) / Precision / Recall:_

| Model | Class | F1 (SD) | P | R |
|---|---|---|---|---|
| roberta-large | Attack | 0.754 (0.009) | 0.753 | 0.765 |
| roberta-large | Contrast | 0.762 (0.004) | 0.764 | 0.762 |
| roberta-large | Promote | 0.958 (0.001) | 0.959 | 0.957 |

### van der Veen (2024) — Populist language

| Model | Acc | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R |
|---|---|---|---|---|---|
| roberta-large | 0.754 | 0.742 (0.004) | 0.753 | 0.747 | 0.743 |
| roberta-base | 0.737 | 0.725 (0.004) | 0.736 | 0.729 | 0.727 |
| bert-base-uncased | 0.650 | 0.636 (0.005) | 0.646 | 0.641 | 0.639 |

_Per-class F1 (SD) / Precision / Recall:_

| Model | Class | F1 (SD) | P | R |
|---|---|---|---|---|
| roberta-large | neutral | 0.671 (0.008) | 0.674 | 0.677 |
| roberta-large | pluralist | 0.705 (0.007) | 0.715 | 0.704 |
| roberta-large | populist | 0.849 (0.004) | 0.853 | 0.849 |
| roberta-base | neutral | 0.649 (0.009) | 0.662 | 0.643 |
| roberta-base | pluralist | 0.684 (0.008) | 0.679 | 0.698 |
| roberta-base | populist | 0.842 (0.004) | 0.846 | 0.839 |
| bert-base-uncased | neutral | 0.549 (0.010) | 0.594 | 0.516 |
| bert-base-uncased | pluralist | 0.627 (0.009) | 0.618 | 0.642 |
| bert-base-uncased | populist | 0.733 (0.004) | 0.711 | 0.759 |

### Ballard et al. (2023) — Incivility

| Model | Acc | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R |
|---|---|---|---|---|---|
| roberta-large | 0.846 | 0.720 (0.007) | 0.845 | 0.732 | 0.724 |

_Per-class F1 (SD) / Precision / Recall:_

| Model | Class | F1 (SD) | P | R |
|---|---|---|---|---|
| roberta-large | 0 | 0.907 (0.004) | 0.909 | 0.907 |
| roberta-large | 1 | 0.534 (0.012) | 0.556 | 0.541 |

### Foy-Sutherland (2025) — Message tone

| Model | Acc | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R |
|---|---|---|---|---|---|
| roberta-large | 0.916 | 0.903 (0.006) | 0.915 | 0.904 | 0.909 |
| roberta-base | 0.896 | 0.876 (0.012) | 0.894 | 0.882 | 0.879 |
| bert-base-uncased | 0.843 | 0.800 (0.017) | 0.834 | 0.818 | 0.801 |

_Per-class F1 (SD) / Precision / Recall:_

| Model | Class | F1 (SD) | P | R |
|---|---|---|---|---|
| roberta-large | Contrast | 0.836 (0.012) | 0.823 | 0.861 |
| roberta-large | Negative | 0.944 (0.005) | 0.953 | 0.937 |
| roberta-large | Positive | 0.929 (0.009) | 0.937 | 0.928 |
| roberta-base | Contrast | 0.796 (0.018) | 0.799 | 0.807 |
| roberta-base | Negative | 0.933 (0.008) | 0.939 | 0.930 |
| roberta-base | Positive | 0.898 (0.016) | 0.908 | 0.900 |
| bert-base-uncased | Contrast | 0.655 (0.028) | 0.753 | 0.594 |
| bert-base-uncased | Negative | 0.908 (0.006) | 0.884 | 0.937 |
| bert-base-uncased | Positive | 0.836 (0.023) | 0.817 | 0.871 |

## International Relations


### Dietrich et al. (2020) — Aid mention

| Model | Acc | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R |
|---|---|---|---|---|---|
| xlm-roberta-large | 0.955 | 0.874 (0.002) | 0.955 | 0.885 | 0.867 |

_Per-class F1 (SD) / Precision / Recall:_

| Model | Class | F1 (SD) | P | R |
|---|---|---|---|---|
| xlm-roberta-large | 0 | 0.975 (0.001) | 0.973 | 0.977 |
| xlm-roberta-large | 1 | 0.772 (0.003) | 0.796 | 0.757 |

### Goes-Chapman (2024) — Governance advice

| Model | Acc | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R |
|---|---|---|---|---|---|
| roberta-large | 0.797 | 0.775 (0.017) | 0.793 | 0.787 | 0.780 |
| roberta-base | 0.782 | 0.765 (0.014) | 0.780 | 0.770 | 0.775 |
| bert-base-uncased | 0.768 | 0.745 (0.015) | 0.765 | 0.757 | 0.752 |

_Per-class F1 (SD) / Precision / Recall:_

| Model | Class | F1 (SD) | P | R |
|---|---|---|---|---|
| roberta-large | 0 | 0.839 (0.012) | 0.842 | 0.845 |
| roberta-large | 1 | 0.712 (0.023) | 0.733 | 0.715 |
| roberta-base | 0 | 0.820 (0.016) | 0.854 | 0.796 |
| roberta-base | 1 | 0.711 (0.014) | 0.686 | 0.754 |
| bert-base-uncased | 0 | 0.817 (0.011) | 0.823 | 0.820 |
| bert-base-uncased | 1 | 0.673 (0.023) | 0.690 | 0.683 |

### Kostovicova-Paskhalis (2021) — Justification (DQI)

| Model | Acc | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R |
|---|---|---|---|---|---|
| xlm-roberta-large | 0.624 | 0.525 (0.021) | 0.606 | 0.606 | 0.505 |
| xlm-roberta-base | 0.609 | 0.484 (0.008) | 0.580 | 0.607 | 0.466 |
| bert-base-multilingual-uncased | 0.588 | 0.482 (0.014) | 0.574 | 0.535 | 0.476 |

_Per-class F1 (SD) / Precision / Recall:_

| Model | Class | F1 (SD) | P | R |
|---|---|---|---|---|
| xlm-roberta-large | 0 | 0.439 (0.073) | 0.673 | 0.359 |
| xlm-roberta-large | 1 | 0.426 (0.027) | 0.457 | 0.415 |
| xlm-roberta-large | 2 | 0.727 (0.010) | 0.671 | 0.797 |
| xlm-roberta-large | 3 | 0.508 (0.022) | 0.621 | 0.450 |
| xlm-roberta-base | 0 | 0.395 (0.035) | 0.652 | 0.310 |
| xlm-roberta-base | 1 | 0.440 (0.021) | 0.446 | 0.452 |
| xlm-roberta-base | 2 | 0.725 (0.009) | 0.651 | 0.823 |
| xlm-roberta-base | 3 | 0.378 (0.024) | 0.680 | 0.277 |
| bert-base-multilingual-uncased | 0 | 0.325 (0.049) | 0.508 | 0.267 |
| bert-base-multilingual-uncased | 1 | 0.422 (0.021) | 0.428 | 0.437 |
| bert-base-multilingual-uncased | 2 | 0.692 (0.009) | 0.659 | 0.734 |
| bert-base-multilingual-uncased | 3 | 0.488 (0.020) | 0.545 | 0.465 |

### Trubowitz-Watanabe (2021) — Geopolitical threat

| Model | Acc | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R |
|---|---|---|---|---|---|
| roberta-large | 0.759 | 0.597 (0.017) | 0.751 | 0.631 | 0.593 |
| roberta-base | 0.762 | 0.595 (0.010) | 0.752 | 0.635 | 0.591 |
| bert-base-uncased | 0.760 | 0.560 (0.017) | 0.742 | 0.634 | 0.560 |

_Per-class F1 (SD) / Precision / Recall:_

| Model | Class | F1 (SD) | P | R |
|---|---|---|---|---|
| roberta-large | No | 0.831 (0.005) | 0.826 | 0.839 |
| roberta-large | Unclear | 0.262 (0.043) | 0.384 | 0.218 |
| roberta-large | Yes | 0.698 (0.008) | 0.683 | 0.723 |
| roberta-base | No | 0.833 (0.004) | 0.830 | 0.838 |
| roberta-base | Unclear | 0.252 (0.027) | 0.401 | 0.198 |
| roberta-base | Yes | 0.701 (0.006) | 0.674 | 0.736 |
| bert-base-uncased | No | 0.832 (0.003) | 0.815 | 0.851 |
| bert-base-uncased | Unclear | 0.157 (0.043) | 0.421 | 0.103 |
| bert-base-uncased | Yes | 0.691 (0.007) | 0.667 | 0.724 |

## Comparative Politics


### Erhard et al. (2025) — Populism

| Model | Acc | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R |
|---|---|---|---|---|---|
| xlm-roberta-large | 0.804 | 0.778 (0.004) | 0.804 | 0.779 | 0.784 |
| xlm-roberta-base | 0.778 | 0.746 (0.005) | 0.778 | 0.750 | 0.748 |
| bert-base-multilingual-uncased | 0.757 | 0.710 (0.005) | 0.751 | 0.724 | 0.705 |

_Per-class F1 (SD) / Precision / Recall:_

| Model | Class | F1 (SD) | P | R |
|---|---|---|---|---|
| xlm-roberta-large | 0 | 0.853 (0.005) | 0.869 | 0.840 |
| xlm-roberta-large | 1 | 0.703 (0.007) | 0.689 | 0.728 |
| xlm-roberta-base | 0 | 0.836 (0.005) | 0.841 | 0.834 |
| xlm-roberta-base | 1 | 0.656 (0.009) | 0.659 | 0.662 |
| bert-base-multilingual-uncased | 0 | 0.826 (0.004) | 0.805 | 0.849 |
| bert-base-multilingual-uncased | 1 | 0.595 (0.009) | 0.643 | 0.561 |

### Ljubešić (2026) — CAP policy topic

| Model | Acc | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R |
|---|---|---|---|---|---|
| xlm-roberta-large | 0.713 | 0.722 (0.005) | 0.708 | 0.729 | 0.733 |

_Per-class F1 (SD) / Precision / Recall:_

| Model | Class | F1 (SD) | P | R |
|---|---|---|---|---|
| xlm-roberta-large | Agriculture | 0.848 (0.007) | 0.817 | 0.889 |
| xlm-roberta-large | Civil Rights | 0.602 (0.028) | 0.656 | 0.577 |
| xlm-roberta-large | Culture | 0.743 (0.018) | 0.731 | 0.778 |
| xlm-roberta-large | Defense | 0.799 (0.016) | 0.786 | 0.822 |
| xlm-roberta-large | Domestic Commerce | 0.632 (0.014) | 0.674 | 0.605 |
| xlm-roberta-large | Education | 0.822 (0.015) | 0.833 | 0.821 |
| xlm-roberta-large | Energy | 0.837 (0.011) | 0.806 | 0.882 |
| xlm-roberta-large | Environment | 0.760 (0.022) | 0.782 | 0.756 |
| xlm-roberta-large | Foreign Trade | 0.729 (0.013) | 0.723 | 0.758 |
| xlm-roberta-large | Government Operations | 0.506 (0.013) | 0.565 | 0.475 |
| xlm-roberta-large | Health | 0.842 (0.015) | 0.833 | 0.860 |
| xlm-roberta-large | Housing | 0.782 (0.017) | 0.758 | 0.822 |
| xlm-roberta-large | Immigration | 0.689 (0.032) | 0.655 | 0.763 |
| xlm-roberta-large | International Affairs | 0.545 (0.020) | 0.604 | 0.514 |
| xlm-roberta-large | Labor | 0.702 (0.015) | 0.720 | 0.701 |
| xlm-roberta-large | Law and Crime | 0.671 (0.018) | 0.697 | 0.658 |
| xlm-roberta-large | Macroeconomics | 0.593 (0.012) | 0.608 | 0.601 |
| xlm-roberta-large | Other | 0.663 (0.015) | 0.729 | 0.622 |
| xlm-roberta-large | Public Lands | 0.763 (0.012) | 0.746 | 0.794 |
| xlm-roberta-large | Social Welfare | 0.708 (0.013) | 0.698 | 0.733 |
| xlm-roberta-large | Technology | 0.836 (0.015) | 0.839 | 0.842 |
| xlm-roberta-large | Transportation | 0.807 (0.013) | 0.777 | 0.854 |

### Heseltine & Clemm von Hohenberg (2024) — Negativity

| Model | Acc | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R |
|---|---|---|---|---|---|
| xlm-roberta-large | 0.872 | 0.841 (0.004) | 0.871 | 0.851 | 0.839 |
| xlm-roberta-base | 0.847 | 0.809 (0.003) | 0.845 | 0.819 | 0.808 |
| bert-base-multilingual-uncased | 0.810 | 0.760 (0.009) | 0.807 | 0.775 | 0.757 |

_Per-class F1 (SD) / Precision / Recall:_

| Model | Class | F1 (SD) | P | R |
|---|---|---|---|---|
| xlm-roberta-large | 0 | 0.911 (0.003) | 0.908 | 0.916 |
| xlm-roberta-large | 1 | 0.771 (0.008) | 0.793 | 0.762 |
| xlm-roberta-base | 0 | 0.893 (0.004) | 0.890 | 0.899 |
| xlm-roberta-base | 1 | 0.724 (0.007) | 0.747 | 0.716 |
| bert-base-multilingual-uncased | 0 | 0.868 (0.004) | 0.859 | 0.881 |
| bert-base-multilingual-uncased | 1 | 0.652 (0.017) | 0.690 | 0.634 |

### Proksch et al. (2019) — Sentiment

| Model | Acc | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R |
|---|---|---|---|---|---|
| roberta-large | 0.500 | 0.464 (0.035) | 0.474 | 0.514 | 0.500 |

_Per-class F1 (SD) / Precision / Recall:_

| Model | Class | F1 (SD) | P | R |
|---|---|---|---|---|
| roberta-large | 1 | 0.553 (0.082) | 0.653 | 0.564 |
| roberta-large | 2 | 0.512 (0.035) | 0.566 | 0.519 |
| roberta-large | 3 | 0.391 (0.043) | 0.441 | 0.389 |
| roberta-large | 4 | 0.549 (0.026) | 0.486 | 0.708 |
| roberta-large | 5 | 0.314 (0.077) | 0.424 | 0.321 |
