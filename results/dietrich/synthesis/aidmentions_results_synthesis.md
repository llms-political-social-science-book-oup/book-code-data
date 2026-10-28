# Aid Mentions (Dietrich et al. 2020) — model synthesis (all models)
Binary task: **no / yes** (does the text mention foreign aid). Test set N=52,744 (no 47,490 · yes 5,254 — ~10:1 imbalance).
Decoders: mean over 3 runs. Encoder: mean over 10×10-fold CV (xlm-roberta-large). _Accuracy = mean only; F1/Precision/Recall = mean ± SD._

## Overall
| Model | Type | Condition | N | Accuracy | Macro F1 (Unweighted) | Weighted F1 |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.935 | 0.836 ± 0.000 | 0.938 ± 0.000 |
| llama | decoder | zero-shot | 3 | 0.928 | 0.823 ± 0.000 | 0.932 ± 0.000 |
| mistral | decoder | zero-shot | 3 | 0.943 | 0.814 ± 0.000 | 0.938 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.934 | 0.836 ± 0.000 | 0.937 ± 0.000 |
| llama | decoder | few-shot | 3 | 0.939 | 0.838 ± 0.000 | 0.940 ± 0.000 |
| mistral | decoder | few-shot | 3 | 0.944 | 0.835 ± 0.000 | 0.942 ± 0.000 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.955 | 0.874 ± 0.002 | 0.955 ± 0.001 |

## F1 per Category
| Model | Type | Condition | N | F1 No | F1 Yes |
|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.963 ± 0.000 | 0.708 ± 0.000 |
| llama | decoder | zero-shot | 3 | 0.959 ± 0.000 | 0.687 ± 0.000 |
| mistral | decoder | zero-shot | 3 | 0.969 ± 0.000 | 0.659 ± 0.001 |
| gemma | decoder | few-shot | 3 | 0.962 ± 0.000 | 0.710 ± 0.000 |
| llama | decoder | few-shot | 3 | 0.966 ± 0.000 | 0.711 ± 0.001 |
| mistral | decoder | few-shot | 3 | 0.969 ± 0.000 | 0.700 ± 0.000 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.975 ± 0.001 | 0.772 ± 0.003 |

## Precision per Category
| Model | Type | Condition | N | Precision No | Precision Yes |
|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.977 ± 0.000 | 0.639 ± 0.000 |
| llama | decoder | zero-shot | 3 | 0.976 ± 0.000 | 0.607 ± 0.000 |
| mistral | decoder | zero-shot | 3 | 0.952 ± 0.000 | 0.817 ± 0.001 |
| gemma | decoder | few-shot | 3 | 0.979 ± 0.000 | 0.629 ± 0.000 |
| llama | decoder | few-shot | 3 | 0.973 ± 0.000 | 0.669 ± 0.000 |
| mistral | decoder | few-shot | 3 | 0.962 ± 0.000 | 0.754 ± 0.001 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.973 ± 0.002 | 0.796 ± 0.017 |

## Recall per Category
| Model | Type | Condition | N | Recall No | Recall Yes |
|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.950 ± 0.000 | 0.794 ± 0.001 |
| llama | decoder | zero-shot | 3 | 0.943 ± 0.000 | 0.791 ± 0.000 |
| mistral | decoder | zero-shot | 3 | 0.986 ± 0.000 | 0.552 ± 0.001 |
| gemma | decoder | few-shot | 3 | 0.947 ± 0.000 | 0.815 ± 0.000 |
| llama | decoder | few-shot | 3 | 0.959 ± 0.000 | 0.758 ± 0.001 |
| mistral | decoder | few-shot | 3 | 0.976 ± 0.000 | 0.654 ± 0.001 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.977 ± 0.003 | 0.757 ± 0.015 |

## Confusion Matrices (decoders: averaged over 3 runs; rows = true, cols = predicted)

### gemma — zero-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 45131 | 2359 |
| **Yes** | 1082 | 4172 |

### llama — zero-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 44803 | 2683 |
| **Yes** | 1099 | 4152 |

### mistral — zero-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 46839 | 651 |
| **Yes** | 2352 | 2902 |

### gemma — few-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 44914 | 2531 |
| **Yes** | 971 | 4283 |

### llama — few-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 45477 | 1968 |
| **Yes** | 1269 | 3985 |

### mistral — few-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 46327 | 1118 |
| **Yes** | 1820 | 3434 |

### xlm-roberta-large — fine-tuned
_Not available: the 10×10 CV runs saved summary statistics only, not out-of-fold predictions, so no confusion matrix can be reconstructed._