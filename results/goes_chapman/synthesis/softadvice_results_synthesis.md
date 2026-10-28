# Soft Advice / Article IV (Goes & Chapman 2024) — model synthesis (all models)
Binary task: **no / yes**. Test set N=700 (no 447 · yes 253).
Decoders: mean over 3 runs. Encoders: mean over 10×10-fold CV. _Accuracy = mean only; F1/Precision/Recall = mean ± SD._

## Overall
| Model | Type | Condition | N | Accuracy | Macro F1 (Unweighted) | Weighted F1 |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.850 | 0.842 ± 0.002 | 0.852 ± 0.002 |
| gpt5 | decoder | zero-shot | 3 | 0.839 | 0.833 ± 0.002 | 0.842 ± 0.002 |
| gpt-mini | decoder | zero-shot | 3 | 0.824 | 0.806 ± 0.005 | 0.822 ± 0.005 |
| llama | decoder | zero-shot | 3 | 0.811 | 0.801 ± 0.002 | 0.814 ± 0.002 |
| mistral | decoder | zero-shot | 3 | 0.740 | 0.644 ± 0.000 | 0.695 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.847 | 0.835 ± 0.004 | 0.847 ± 0.004 |
| gpt5 | decoder | few-shot | 3 | 0.852 | 0.840 ± 0.005 | 0.852 ± 0.004 |
| gpt-mini | decoder | few-shot | 3 | 0.808 | 0.768 ± 0.008 | 0.795 ± 0.007 |
| llama | decoder | few-shot | 3 | 0.828 | 0.805 ± 0.003 | 0.824 ± 0.002 |
| mistral | decoder | few-shot | 3 | 0.797 | 0.758 ± 0.002 | 0.785 ± 0.002 |
| roberta-large | encoder | fine-tuned | 10 | 0.775 | 0.745 ± 0.028 | 0.766 ± 0.024 |
| roberta-base | encoder | fine-tuned | 10 | 0.782 | 0.765 ± 0.014 | 0.780 ± 0.014 |
| bert | encoder | fine-tuned | 10 | 0.768 | 0.745 ± 0.015 | 0.765 ± 0.013 |

## F1 per Category
| Model | Type | Condition | N | F1 No | F1 Yes |
|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.877 ± 0.002 | 0.807 ± 0.003 |
| gpt5 | decoder | zero-shot | 3 | 0.864 ± 0.001 | 0.803 ± 0.002 |
| gpt-mini | decoder | zero-shot | 3 | 0.865 ± 0.003 | 0.747 ± 0.007 |
| llama | decoder | zero-shot | 3 | 0.846 ± 0.002 | 0.757 ± 0.002 |
| mistral | decoder | zero-shot | 3 | 0.829 ± 0.000 | 0.458 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.879 ± 0.003 | 0.790 ± 0.006 |
| gpt5 | decoder | few-shot | 3 | 0.884 ± 0.003 | 0.795 ± 0.007 |
| gpt-mini | decoder | few-shot | 3 | 0.864 ± 0.004 | 0.672 ± 0.012 |
| llama | decoder | few-shot | 3 | 0.872 ± 0.002 | 0.737 ± 0.004 |
| mistral | decoder | few-shot | 3 | 0.855 ± 0.001 | 0.661 ± 0.003 |
| roberta-large | encoder | fine-tuned | 10 | 0.821 ± 0.017 | 0.669 ± 0.047 |
| roberta-base | encoder | fine-tuned | 10 | 0.820 ± 0.016 | 0.711 ± 0.013 |
| bert | encoder | fine-tuned | 10 | 0.817 ± 0.010 | 0.673 ± 0.022 |

## Precision per Category
| Model | Type | Condition | N | Precision No | Precision Yes |
|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.919 ± 0.002 | 0.753 ± 0.004 |
| gpt5 | decoder | zero-shot | 3 | 0.938 ± 0.003 | 0.720 ± 0.002 |
| gpt-mini | decoder | zero-shot | 3 | 0.848 ± 0.004 | 0.776 ± 0.006 |
| llama | decoder | zero-shot | 3 | 0.884 ± 0.001 | 0.709 ± 0.003 |
| mistral | decoder | zero-shot | 3 | 0.715 ± 0.000 | 0.928 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.885 ± 0.004 | 0.782 ± 0.005 |
| gpt5 | decoder | few-shot | 3 | 0.884 ± 0.006 | 0.797 ± 0.008 |
| gpt-mini | decoder | few-shot | 3 | 0.787 ± 0.005 | 0.879 ± 0.011 |
| llama | decoder | few-shot | 3 | 0.830 ± 0.002 | 0.823 ± 0.004 |
| mistral | decoder | few-shot | 3 | 0.786 ± 0.001 | 0.832 ± 0.001 |
| roberta-large | encoder | fine-tuned | 10 | 0.846 ± 0.021 | 0.650 ± 0.037 |
| roberta-base | encoder | fine-tuned | 10 | 0.854 ± 0.008 | 0.686 ± 0.025 |
| bert | encoder | fine-tuned | 10 | 0.823 ± 0.012 | 0.690 ± 0.018 |

## Recall per Category
| Model | Type | Condition | N | Recall No | Recall Yes |
|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.839 ± 0.003 | 0.870 ± 0.003 |
| gpt5 | decoder | zero-shot | 3 | 0.801 ± 0.002 | 0.906 ± 0.005 |
| gpt-mini | decoder | zero-shot | 3 | 0.882 ± 0.003 | 0.721 ± 0.008 |
| llama | decoder | zero-shot | 3 | 0.811 ± 0.002 | 0.812 ± 0.002 |
| mistral | decoder | zero-shot | 3 | 0.987 ± 0.000 | 0.304 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.874 ± 0.003 | 0.798 ± 0.006 |
| gpt5 | decoder | few-shot | 3 | 0.885 ± 0.006 | 0.794 ± 0.012 |
| gpt-mini | decoder | few-shot | 3 | 0.957 ± 0.004 | 0.544 ± 0.011 |
| llama | decoder | few-shot | 3 | 0.919 ± 0.002 | 0.668 ± 0.003 |
| mistral | decoder | few-shot | 3 | 0.937 ± 0.000 | 0.548 ± 0.004 |
| roberta-large | encoder | fine-tuned | 10 | 0.812 ± 0.029 | 0.711 ± 0.061 |
| roberta-base | encoder | fine-tuned | 10 | 0.796 ± 0.029 | 0.754 ± 0.019 |
| bert | encoder | fine-tuned | 10 | 0.820 ± 0.018 | 0.683 ± 0.033 |

## Confusion Matrices (decoders: averaged over 3 runs; rows = true, cols = predicted)

### gemma — zero-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 375 | 72 |
| **Yes** | 33 | 220 |

### gpt5 — zero-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 358 | 89 |
| **Yes** | 24 | 229 |

### gpt-mini — zero-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 394 | 53 |
| **Yes** | 71 | 182 |

### llama — zero-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 363 | 84 |
| **Yes** | 48 | 205 |

### mistral — zero-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 441 | 6 |
| **Yes** | 176 | 77 |

### gemma — few-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 391 | 56 |
| **Yes** | 51 | 202 |

### gpt5 — few-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 396 | 51 |
| **Yes** | 52 | 201 |

### gpt-mini — few-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 427 | 19 |
| **Yes** | 115 | 138 |

### llama — few-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 411 | 36 |
| **Yes** | 84 | 169 |

### mistral — few-shot
| true \ pred | No | Yes |
|---|---|---|
| **No** | 419 | 28 |
| **Yes** | 114 | 139 |

### encoders (roberta-large, roberta-base, bert) — fine-tuned
_Not available: the 10×10 CV runs saved summary statistics only, not out-of-fold predictions, so no confusion matrix can be reconstructed._