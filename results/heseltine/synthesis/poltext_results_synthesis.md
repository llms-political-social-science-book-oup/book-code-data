# Annotating Political Text (Heseltine & von Hohenberg 2024) — model synthesis (all models)
Binary task: **notnegative / negative** (0 = notnegative, 1 = negative). Test set N=2,195 (notnegative 1,569 · negative 626).
Decoders: mean over 3 runs. Encoders: mean over 10×10-fold CV (multilingual variants). _Accuracy = mean only; F1/Precision/Recall = mean ± SD._

## Overall
| Model | Type | Condition | N | Accuracy | Macro F1 (Unweighted) | Weighted F1 |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.848 | 0.832 ± 0.002 | 0.854 ± 0.001 |
| gpt5 | decoder | zero-shot | 3 | 0.826 | 0.813 ± 0.001 | 0.834 ± 0.001 |
| gpt-mini | decoder | zero-shot | 3 | 0.800 | 0.787 ± 0.005 | 0.810 ± 0.005 |
| llama | decoder | zero-shot | 3 | 0.878 | 0.851 ± 0.001 | 0.878 ± 0.001 |
| mistral | decoder | zero-shot | 3 | 0.890 | 0.863 ± 0.000 | 0.889 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.824 | 0.810 ± 0.001 | 0.832 ± 0.001 |
| gpt5 | decoder | few-shot | 3 | 0.829 | 0.815 ± 0.003 | 0.837 ± 0.003 |
| gpt-mini | decoder | few-shot | 3 | 0.873 | 0.854 ± 0.002 | 0.877 ± 0.002 |
| llama | decoder | few-shot | 3 | 0.859 | 0.837 ± 0.001 | 0.863 ± 0.001 |
| mistral | decoder | few-shot | 3 | 0.837 | 0.820 ± 0.002 | 0.844 ± 0.002 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.872 | 0.841 ± 0.004 | 0.871 ± 0.003 |
| xlm-roberta-base | encoder | fine-tuned | 10 | 0.847 | 0.809 ± 0.003 | 0.845 ± 0.002 |
| bert-multilingual | encoder | fine-tuned | 10 | 0.810 | 0.760 ± 0.009 | 0.807 ± 0.006 |

## F1 per Category
| Model | Type | Condition | N | F1 Notnegative | F1 Negative |
|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.883 ± 0.001 | 0.781 ± 0.002 |
| gpt5 | decoder | zero-shot | 3 | 0.863 ± 0.001 | 0.762 ± 0.001 |
| gpt-mini | decoder | zero-shot | 3 | 0.840 ± 0.004 | 0.735 ± 0.005 |
| llama | decoder | zero-shot | 3 | 0.914 ± 0.000 | 0.788 ± 0.001 |
| mistral | decoder | zero-shot | 3 | 0.923 ± 0.000 | 0.802 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.861 ± 0.001 | 0.760 ± 0.002 |
| gpt5 | decoder | few-shot | 3 | 0.865 ± 0.002 | 0.765 ± 0.003 |
| gpt-mini | decoder | few-shot | 3 | 0.907 ± 0.002 | 0.800 ± 0.002 |
| llama | decoder | few-shot | 3 | 0.897 ± 0.001 | 0.777 ± 0.002 |
| mistral | decoder | few-shot | 3 | 0.875 ± 0.002 | 0.765 ± 0.002 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.911 ± 0.003 | 0.771 ± 0.007 |
| xlm-roberta-base | encoder | fine-tuned | 10 | 0.893 ± 0.004 | 0.724 ± 0.007 |
| bert-multilingual | encoder | fine-tuned | 10 | 0.868 ± 0.004 | 0.652 ± 0.016 |

## Precision per Category
| Model | Type | Condition | N | Precision Notnegative | Precision Negative |
|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.977 ± 0.001 | 0.662 ± 0.002 |
| gpt5 | decoder | zero-shot | 3 | 0.987 ± 0.001 | 0.625 ± 0.001 |
| gpt-mini | decoder | zero-shot | 3 | 0.984 ± 0.003 | 0.591 ± 0.006 |
| llama | decoder | zero-shot | 3 | 0.918 ± 0.000 | 0.779 ± 0.002 |
| mistral | decoder | zero-shot | 3 | 0.915 ± 0.001 | 0.821 ± 0.002 |
| gemma | decoder | few-shot | 3 | 0.987 ± 0.000 | 0.622 ± 0.002 |
| gpt5 | decoder | few-shot | 3 | 0.989 ± 0.001 | 0.628 ± 0.004 |
| gpt-mini | decoder | few-shot | 3 | 0.951 ± 0.001 | 0.728 ± 0.005 |
| llama | decoder | few-shot | 3 | 0.940 ± 0.002 | 0.706 ± 0.001 |
| mistral | decoder | few-shot | 3 | 0.968 ± 0.000 | 0.649 ± 0.003 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.908 ± 0.007 | 0.793 ± 0.019 |
| xlm-roberta-base | encoder | fine-tuned | 10 | 0.890 ± 0.008 | 0.747 ± 0.021 |
| bert-multilingual | encoder | fine-tuned | 10 | 0.859 ± 0.008 | 0.690 ± 0.019 |

## Recall per Category
| Model | Type | Condition | N | Recall Notnegative | Recall Negative |
|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.806 ± 0.002 | 0.952 ± 0.002 |
| gpt5 | decoder | zero-shot | 3 | 0.767 ± 0.001 | 0.976 ± 0.003 |
| gpt-mini | decoder | zero-shot | 3 | 0.732 ± 0.007 | 0.971 ± 0.006 |
| llama | decoder | zero-shot | 3 | 0.909 ± 0.001 | 0.798 ± 0.001 |
| mistral | decoder | zero-shot | 3 | 0.932 ± 0.001 | 0.784 ± 0.002 |
| gemma | decoder | few-shot | 3 | 0.764 ± 0.002 | 0.975 ± 0.001 |
| gpt5 | decoder | few-shot | 3 | 0.769 ± 0.003 | 0.978 ± 0.002 |
| gpt-mini | decoder | few-shot | 3 | 0.868 ± 0.003 | 0.887 ± 0.002 |
| llama | decoder | few-shot | 3 | 0.857 ± 0.001 | 0.864 ± 0.004 |
| mistral | decoder | few-shot | 3 | 0.798 ± 0.003 | 0.933 ± 0.001 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.916 ± 0.011 | 0.762 ± 0.025 |
| xlm-roberta-base | encoder | fine-tuned | 10 | 0.899 ± 0.015 | 0.716 ± 0.029 |
| bert-multilingual | encoder | fine-tuned | 10 | 0.881 ± 0.013 | 0.634 ± 0.032 |

## Confusion Matrices (decoders: averaged over 3 runs; rows = true, cols = predicted)

### gemma — zero-shot
| true \ pred | Notnegative | Negative |
|---|---|---|
| **Notnegative** | 1265 | 304 |
| **Negative** | 30 | 596 |

### gpt5 — zero-shot
| true \ pred | Notnegative | Negative |
|---|---|---|
| **Notnegative** | 1203 | 366 |
| **Negative** | 15 | 611 |

### gpt-mini — zero-shot
| true \ pred | Notnegative | Negative |
|---|---|---|
| **Notnegative** | 1148 | 420 |
| **Negative** | 18 | 607 |

### llama — zero-shot
| true \ pred | Notnegative | Negative |
|---|---|---|
| **Notnegative** | 1427 | 142 |
| **Negative** | 127 | 499 |

### mistral — zero-shot
| true \ pred | Notnegative | Negative |
|---|---|---|
| **Notnegative** | 1462 | 107 |
| **Negative** | 135 | 491 |

### gemma — few-shot
| true \ pred | Notnegative | Negative |
|---|---|---|
| **Notnegative** | 1198 | 371 |
| **Negative** | 16 | 610 |

### gpt5 — few-shot
| true \ pred | Notnegative | Negative |
|---|---|---|
| **Notnegative** | 1206 | 363 |
| **Negative** | 14 | 612 |

### gpt-mini — few-shot
| true \ pred | Notnegative | Negative |
|---|---|---|
| **Notnegative** | 1362 | 207 |
| **Negative** | 71 | 554 |

### llama — few-shot
| true \ pred | Notnegative | Negative |
|---|---|---|
| **Notnegative** | 1344 | 225 |
| **Negative** | 85 | 541 |

### mistral — few-shot
| true \ pred | Notnegative | Negative |
|---|---|---|
| **Notnegative** | 1252 | 317 |
| **Negative** | 42 | 584 |

### encoders (xlm-roberta-large, xlm-roberta-base, bert-multilingual) — fine-tuned
_Not available: the 10×10 CV runs saved summary statistics only, not out-of-fold predictions, so no confusion matrix can be reconstructed._