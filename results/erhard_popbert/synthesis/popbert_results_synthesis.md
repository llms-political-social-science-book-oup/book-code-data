# PopBERT (Erhard et al. 2025) — model synthesis (all models)
Binary task: **nonpopulist / populist** (0 = nonpopulist, 1 = populist). German text. Test set N=8,795 (nonpopulist 5,969 · populist 2,826).
Decoders: mean over 3 runs. Encoders: mean over 10×10-fold CV (multilingual variants). _Accuracy = mean only; F1/Precision/Recall = mean ± SD._

## Overall
| Model | Type | Condition | N | Accuracy | Macro F1 (Unweighted) | Weighted F1 |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.755 | 0.703 ± 0.001 | 0.747 ± 0.001 |
| gpt5 | decoder | zero-shot | 3 | 0.772 | 0.709 ± 0.001 | 0.757 ± 0.001 |
| gpt-mini | decoder | zero-shot | 3 | 0.750 | 0.734 ± 0.001 | 0.758 ± 0.001 |
| llama | decoder | zero-shot | 3 | 0.729 | 0.716 ± 0.000 | 0.738 ± 0.000 |
| mistral | decoder | zero-shot | 3 | 0.736 | 0.625 ± 0.001 | 0.698 ± 0.001 |
| gemma | decoder | few-shot | 3 | 0.750 | 0.691 ± 0.001 | 0.739 ± 0.001 |
| gpt5 | decoder | few-shot | 3 | 0.757 | 0.684 ± 0.002 | 0.739 ± 0.002 |
| gpt-mini | decoder | few-shot | 3 | 0.739 | 0.651 ± 0.000 | 0.714 ± 0.000 |
| llama | decoder | few-shot | 3 | 0.747 | 0.717 ± 0.001 | 0.750 ± 0.001 |
| mistral | decoder | few-shot | 3 | 0.739 | 0.706 ± 0.001 | 0.741 ± 0.001 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.804 | 0.778 ± 0.004 | 0.804 ± 0.004 |
| xlm-roberta-base | encoder | fine-tuned | 10 | 0.778 | 0.746 ± 0.005 | 0.778 ± 0.004 |
| bert-multilingual | encoder | fine-tuned | 10 | 0.757 | 0.710 ± 0.004 | 0.751 ± 0.003 |

## F1 per Category
| Model | Type | Condition | N | F1 Nonpopulist | F1 Populist |
|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.827 ± 0.000 | 0.578 ± 0.002 |
| gpt5 | decoder | zero-shot | 3 | 0.844 ± 0.001 | 0.574 ± 0.002 |
| gpt-mini | decoder | zero-shot | 3 | 0.801 ± 0.001 | 0.666 ± 0.001 |
| llama | decoder | zero-shot | 3 | 0.777 ± 0.001 | 0.655 ± 0.001 |
| mistral | decoder | zero-shot | 3 | 0.829 ± 0.000 | 0.422 ± 0.001 |
| gemma | decoder | few-shot | 3 | 0.827 ± 0.000 | 0.554 ± 0.001 |
| gpt5 | decoder | few-shot | 3 | 0.836 ± 0.001 | 0.532 ± 0.004 |
| gpt-mini | decoder | few-shot | 3 | 0.827 ± 0.001 | 0.475 ± 0.001 |
| llama | decoder | few-shot | 3 | 0.809 ± 0.001 | 0.626 ± 0.001 |
| mistral | decoder | few-shot | 3 | 0.804 ± 0.001 | 0.609 ± 0.001 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.853 ± 0.004 | 0.703 ± 0.007 |
| xlm-roberta-base | encoder | fine-tuned | 10 | 0.836 ± 0.004 | 0.656 ± 0.008 |
| bert-multilingual | encoder | fine-tuned | 10 | 0.826 ± 0.004 | 0.595 ± 0.009 |

## Precision per Category
| Model | Type | Condition | N | Precision Nonpopulist | Precision Populist |
|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.793 ± 0.001 | 0.646 ± 0.001 |
| gpt5 | decoder | zero-shot | 3 | 0.787 ± 0.001 | 0.716 ± 0.004 |
| gpt-mini | decoder | zero-shot | 3 | 0.874 ± 0.001 | 0.584 ± 0.001 |
| llama | decoder | zero-shot | 3 | 0.881 ± 0.001 | 0.554 ± 0.001 |
| mistral | decoder | zero-shot | 3 | 0.740 ± 0.000 | 0.711 ± 0.001 |
| gemma | decoder | few-shot | 3 | 0.782 ± 0.000 | 0.650 ± 0.001 |
| gpt5 | decoder | few-shot | 3 | 0.772 ± 0.001 | 0.699 ± 0.003 |
| gpt-mini | decoder | few-shot | 3 | 0.754 ± 0.000 | 0.673 ± 0.005 |
| llama | decoder | few-shot | 3 | 0.830 ± 0.000 | 0.596 ± 0.002 |
| mistral | decoder | few-shot | 3 | 0.820 ± 0.001 | 0.586 ± 0.002 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.869 ± 0.007 | 0.689 ± 0.013 |
| xlm-roberta-base | encoder | fine-tuned | 10 | 0.841 ± 0.007 | 0.659 ± 0.009 |
| bert-multilingual | encoder | fine-tuned | 10 | 0.805 ± 0.005 | 0.643 ± 0.011 |

## Recall per Category
| Model | Type | Condition | N | Recall Nonpopulist | Recall Populist |
|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.865 ± 0.000 | 0.523 ± 0.002 |
| gpt5 | decoder | zero-shot | 3 | 0.910 ± 0.002 | 0.478 ± 0.001 |
| gpt-mini | decoder | zero-shot | 3 | 0.738 ± 0.002 | 0.776 ± 0.001 |
| llama | decoder | zero-shot | 3 | 0.694 ± 0.001 | 0.802 ± 0.001 |
| mistral | decoder | zero-shot | 3 | 0.942 ± 0.000 | 0.300 ± 0.001 |
| gemma | decoder | few-shot | 3 | 0.877 ± 0.000 | 0.483 ± 0.001 |
| gpt5 | decoder | few-shot | 3 | 0.912 ± 0.001 | 0.430 ± 0.005 |
| gpt-mini | decoder | few-shot | 3 | 0.915 ± 0.002 | 0.368 ± 0.003 |
| llama | decoder | few-shot | 3 | 0.788 ± 0.002 | 0.659 ± 0.001 |
| mistral | decoder | few-shot | 3 | 0.788 ± 0.002 | 0.635 ± 0.001 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.840 ± 0.013 | 0.728 ± 0.021 |
| xlm-roberta-base | encoder | fine-tuned | 10 | 0.834 ± 0.012 | 0.662 ± 0.020 |
| bert-multilingual | encoder | fine-tuned | 10 | 0.849 ± 0.012 | 0.561 ± 0.019 |

## Confusion Matrices (decoders: averaged over 3 runs; rows = true, cols = predicted)

### gemma — zero-shot
| true \ pred | Nonpopulist | Populist |
|---|---|---|
| **Nonpopulist** | 5161 | 808 |
| **Populist** | 1349 | 1477 |

### gpt5 — zero-shot
| true \ pred | Nonpopulist | Populist |
|---|---|---|
| **Nonpopulist** | 5434 | 535 |
| **Populist** | 1474 | 1352 |

### gpt-mini — zero-shot
| true \ pred | Nonpopulist | Populist |
|---|---|---|
| **Nonpopulist** | 4406 | 1562 |
| **Populist** | 632 | 2192 |

### llama — zero-shot
| true \ pred | Nonpopulist | Populist |
|---|---|---|
| **Nonpopulist** | 4143 | 1826 |
| **Populist** | 558 | 2268 |

### mistral — zero-shot
| true \ pred | Nonpopulist | Populist |
|---|---|---|
| **Nonpopulist** | 5625 | 344 |
| **Populist** | 1978 | 848 |

### gemma — few-shot
| true \ pred | Nonpopulist | Populist |
|---|---|---|
| **Nonpopulist** | 5235 | 734 |
| **Populist** | 1460 | 1366 |

### gpt5 — few-shot
| true \ pred | Nonpopulist | Populist |
|---|---|---|
| **Nonpopulist** | 5446 | 523 |
| **Populist** | 1611 | 1215 |

### gpt-mini — few-shot
| true \ pred | Nonpopulist | Populist |
|---|---|---|
| **Nonpopulist** | 5463 | 506 |
| **Populist** | 1787 | 1039 |

### llama — few-shot
| true \ pred | Nonpopulist | Populist |
|---|---|---|
| **Nonpopulist** | 4705 | 1264 |
| **Populist** | 964 | 1862 |

### mistral — few-shot
| true \ pred | Nonpopulist | Populist |
|---|---|---|
| **Nonpopulist** | 4702 | 1267 |
| **Populist** | 1032 | 1794 |

### encoders (xlm-roberta-large, xlm-roberta-base, bert-multilingual) — fine-tuned
_Not available: the 10×10 CV runs saved summary statistics only, not out-of-fold predictions, so no confusion matrix can be reconstructed._