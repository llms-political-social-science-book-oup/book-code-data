# Working Hand (Foy-Sutherland 2025) — model synthesis (all models)
Classes: **Positive / Contrast / Negative**. Test set N=910 (Negative 529 · Contrast 220 · Positive 161).
Decoders: mean over 3 runs. Encoders: mean over 10×10-fold CV. _Accuracy = mean only; F1/Precision/Recall = mean ± SD._

## Overall
| Model | Type | Condition | N | Accuracy | Macro F1 (Unweighted) | Weighted F1 |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.911 | 0.892 ± 0.001 | 0.913 ± 0.001 |
| gpt5 | decoder | zero-shot | 3 | 0.864 | 0.839 ± 0.003 | 0.868 ± 0.002 |
| gpt-mini | decoder | zero-shot | 3 | 0.901 | 0.887 ± 0.003 | 0.902 ± 0.003 |
| llama | decoder | zero-shot | 3 | 0.829 | 0.809 ± 0.001 | 0.834 ± 0.000 |
| mistral | decoder | zero-shot | 3 | 0.846 | 0.847 ± 0.001 | 0.853 ± 0.001 |
| gemma | decoder | few-shot | 3 | 0.939 | 0.930 ± 0.002 | 0.940 ± 0.002 |
| gpt5 | decoder | few-shot | 3 | 0.855 | 0.834 ± 0.001 | 0.860 ± 0.001 |
| gpt-mini | decoder | few-shot | 3 | 0.855 | 0.834 ± 0.005 | 0.860 ± 0.002 |
| llama | decoder | few-shot | 3 | 0.853 | 0.837 ± 0.001 | 0.859 ± 0.000 |
| mistral | decoder | few-shot | 3 | 0.871 | 0.869 ± 0.000 | 0.875 ± 0.001 |
| roberta-large | encoder | fine-tuned | 10 | 0.916 | 0.903 ± 0.006 | 0.915 ± 0.005 |
| roberta-base | encoder | fine-tuned | 10 | 0.896 | 0.876 ± 0.011 | 0.894 ± 0.009 |
| bert | encoder | fine-tuned | 10 | 0.843 | 0.800 ± 0.016 | 0.834 ± 0.012 |

## F1 per Category
| Model | Type | Condition | N | F1 Positive | F1 Contrast | F1 Negative |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.875 ± 0.002 | 0.849 ± 0.001 | 0.952 ± 0.001 |
| gpt5 | decoder | zero-shot | 3 | 0.758 ± 0.005 | 0.849 ± 0.001 | 0.910 ± 0.001 |
| gpt-mini | decoder | zero-shot | 3 | 0.882 ± 0.009 | 0.852 ± 0.007 | 0.929 ± 0.004 |
| llama | decoder | zero-shot | 3 | 0.738 ± 0.002 | 0.818 ± 0.001 | 0.870 ± 0.000 |
| mistral | decoder | zero-shot | 3 | 0.919 ± 0.000 | 0.741 ± 0.002 | 0.880 ± 0.001 |
| gemma | decoder | few-shot | 3 | 0.937 ± 0.002 | 0.892 ± 0.002 | 0.961 ± 0.002 |
| gpt5 | decoder | few-shot | 3 | 0.743 ± 0.003 | 0.866 ± 0.001 | 0.893 ± 0.001 |
| gpt-mini | decoder | few-shot | 3 | 0.739 ± 0.012 | 0.868 ± 0.006 | 0.894 ± 0.002 |
| llama | decoder | few-shot | 3 | 0.762 ± 0.003 | 0.861 ± 0.001 | 0.887 ± 0.001 |
| mistral | decoder | few-shot | 3 | 0.934 ± 0.003 | 0.772 ± 0.002 | 0.900 ± 0.002 |
| roberta-large | encoder | fine-tuned | 10 | 0.929 ± 0.008 | 0.836 ± 0.011 | 0.944 ± 0.004 |
| roberta-base | encoder | fine-tuned | 10 | 0.898 ± 0.016 | 0.796 ± 0.017 | 0.933 ± 0.008 |
| bert | encoder | fine-tuned | 10 | 0.836 ± 0.022 | 0.655 ± 0.027 | 0.908 ± 0.005 |

## Precision per Category
| Model | Type | Condition | N | Precision Positive | Precision Contrast | Precision Negative |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.940 ± 0.003 | 0.758 ± 0.001 | 0.990 ± 0.000 |
| gpt5 | decoder | zero-shot | 3 | 0.714 ± 0.004 | 0.755 ± 0.002 | 0.995 ± 0.001 |
| gpt-mini | decoder | zero-shot | 3 | 0.856 ± 0.014 | 0.826 ± 0.007 | 0.951 ± 0.007 |
| llama | decoder | zero-shot | 3 | 0.646 ± 0.001 | 0.761 ± 0.002 | 0.958 ± 0.001 |
| mistral | decoder | zero-shot | 3 | 0.966 ± 0.000 | 0.634 ± 0.001 | 0.952 ± 0.002 |
| gemma | decoder | few-shot | 3 | 0.947 ± 0.007 | 0.834 ± 0.003 | 0.989 ± 0.001 |
| gpt5 | decoder | few-shot | 3 | 0.657 ± 0.002 | 0.783 ± 0.002 | 0.998 ± 0.000 |
| gpt-mini | decoder | few-shot | 3 | 0.648 ± 0.004 | 0.804 ± 0.011 | 0.987 ± 0.002 |
| llama | decoder | few-shot | 3 | 0.648 ± 0.004 | 0.820 ± 0.003 | 0.979 ± 0.000 |
| mistral | decoder | few-shot | 3 | 0.925 ± 0.003 | 0.701 ± 0.003 | 0.953 ± 0.004 |
| roberta-large | encoder | fine-tuned | 10 | 0.937 ± 0.012 | 0.823 ± 0.011 | 0.953 ± 0.009 |
| roberta-base | encoder | fine-tuned | 10 | 0.908 ± 0.018 | 0.799 ± 0.026 | 0.939 ± 0.008 |
| bert | encoder | fine-tuned | 10 | 0.817 ± 0.027 | 0.753 ± 0.037 | 0.884 ± 0.009 |

## Recall per Category
| Model | Type | Condition | N | Recall Positive | Recall Contrast | Recall Negative |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.818 ± 0.003 | 0.964 ± 0.000 | 0.917 ± 0.002 |
| gpt5 | decoder | zero-shot | 3 | 0.807 ± 0.009 | 0.968 ± 0.000 | 0.839 ± 0.002 |
| gpt-mini | decoder | zero-shot | 3 | 0.909 ± 0.011 | 0.879 ± 0.020 | 0.908 ± 0.009 |
| llama | decoder | zero-shot | 3 | 0.861 ± 0.003 | 0.883 ± 0.002 | 0.796 ± 0.001 |
| mistral | decoder | zero-shot | 3 | 0.876 ± 0.000 | 0.891 ± 0.004 | 0.819 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.928 ± 0.003 | 0.959 ± 0.000 | 0.934 ± 0.004 |
| gpt5 | decoder | few-shot | 3 | 0.855 ± 0.006 | 0.968 ± 0.000 | 0.808 ± 0.001 |
| gpt-mini | decoder | few-shot | 3 | 0.861 ± 0.026 | 0.942 ± 0.004 | 0.817 ± 0.002 |
| llama | decoder | few-shot | 3 | 0.923 ± 0.003 | 0.906 ± 0.002 | 0.810 ± 0.002 |
| mistral | decoder | few-shot | 3 | 0.944 ± 0.005 | 0.860 ± 0.008 | 0.853 ± 0.002 |
| roberta-large | encoder | fine-tuned | 10 | 0.928 ± 0.012 | 0.861 ± 0.018 | 0.937 ± 0.006 |
| roberta-base | encoder | fine-tuned | 10 | 0.900 ± 0.020 | 0.807 ± 0.027 | 0.930 ± 0.013 |
| bert | encoder | fine-tuned | 10 | 0.871 ± 0.024 | 0.594 ± 0.030 | 0.937 ± 0.009 |

## Confusion Matrices (decoders: averaged over 3 runs; rows = true, cols = predicted)

### gemma — zero-shot
| true \ pred | Positive | Contrast | Negative |
|---|---|---|---|
| **Positive** | 132 | 28 | 1 |
| **Contrast** | 4 | 212 | 4 |
| **Negative** | 4 | 39 | 485 |

### gpt5 — zero-shot
| true \ pred | Positive | Contrast | Negative |
|---|---|---|---|
| **Positive** | 130 | 31 | 0 |
| **Contrast** | 5 | 213 | 2 |
| **Negative** | 47 | 38 | 444 |

### gpt-mini — zero-shot
| true \ pred | Positive | Contrast | Negative |
|---|---|---|---|
| **Positive** | 146 | 12 | 2 |
| **Contrast** | 4 | 193 | 22 |
| **Negative** | 20 | 28 | 480 |

### llama — zero-shot
| true \ pred | Positive | Contrast | Negative |
|---|---|---|---|
| **Positive** | 139 | 22 | 0 |
| **Contrast** | 7 | 194 | 19 |
| **Negative** | 69 | 39 | 421 |

### mistral — zero-shot
| true \ pred | Positive | Contrast | Negative |
|---|---|---|---|
| **Positive** | 141 | 19 | 1 |
| **Contrast** | 3 | 196 | 21 |
| **Negative** | 2 | 94 | 433 |

### gemma — few-shot
| true \ pred | Positive | Contrast | Negative |
|---|---|---|---|
| **Positive** | 149 | 10 | 1 |
| **Contrast** | 5 | 211 | 4 |
| **Negative** | 3 | 32 | 494 |

### gpt5 — few-shot
| true \ pred | Positive | Contrast | Negative |
|---|---|---|---|
| **Positive** | 138 | 23 | 0 |
| **Contrast** | 6 | 213 | 1 |
| **Negative** | 66 | 36 | 427 |

### gpt-mini — few-shot
| true \ pred | Positive | Contrast | Negative |
|---|---|---|---|
| **Positive** | 139 | 22 | 0 |
| **Contrast** | 7 | 207 | 6 |
| **Negative** | 68 | 28 | 432 |

### llama — few-shot
| true \ pred | Positive | Contrast | Negative |
|---|---|---|---|
| **Positive** | 149 | 12 | 0 |
| **Contrast** | 12 | 199 | 9 |
| **Negative** | 69 | 31 | 429 |

### mistral — few-shot
| true \ pred | Positive | Contrast | Negative |
|---|---|---|---|
| **Positive** | 152 | 9 | 0 |
| **Contrast** | 9 | 189 | 21 |
| **Negative** | 3 | 72 | 436 |

### encoders (roberta-large, roberta-base, bert) — fine-tuned
_Not available: the 10×10 CV runs saved summary statistics only, not out-of-fold predictions, so no confusion matrix can be reconstructed._