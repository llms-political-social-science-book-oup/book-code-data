# Political Advertising (Fowler et al. 2020) — model synthesis (all models)
Classes: **Promote / Contrast / Attack**. Test set N=14,445 (Promote 10,816 · Contrast 2,563 · Attack 1,066).
Decoders: mean over 3 runs. Encoder: mean over 10×10-fold CV. _Accuracy = mean only; F1/Precision/Recall = mean ± SD._

## Overall
| Model | Type | Condition | N | Accuracy | Macro F1 (Unweighted) | Weighted F1 |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.840 | 0.731 ± 0.001 | 0.851 ± 0.000 |
| gpt5 | decoder | zero-shot | 3 | 0.863 | 0.786 ± 0.001 | 0.872 ± 0.001 |
| gpt-mini | decoder | zero-shot | 3 | 0.823 | 0.673 ± 0.001 | 0.836 ± 0.001 |
| llama | decoder | zero-shot | 3 | 0.843 | 0.709 ± 0.001 | 0.850 ± 0.000 |
| mistral | decoder | zero-shot | 3 | 0.773 | 0.680 ± 0.000 | 0.795 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.849 | 0.759 ± 0.001 | 0.858 ± 0.000 |
| gpt5 | decoder | few-shot | 3 | 0.837 | 0.764 ± 0.002 | 0.848 ± 0.001 |
| gpt-mini | decoder | few-shot | 3 | 0.854 | 0.755 ± 0.001 | 0.861 ± 0.001 |
| llama | decoder | few-shot | 3 | 0.864 | 0.747 ± 0.001 | 0.864 ± 0.001 |
| mistral | decoder | few-shot | 3 | 0.835 | 0.701 ± 0.001 | 0.839 ± 0.000 |
| roberta-large | encoder | fine-tuned | 10 | 0.908 | 0.825 ± 0.003 | 0.908 ± 0.001 |

## F1 per Category
| Model | Type | Condition | N | F1 Promote | F1 Contrast | F1 Attack |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.915 ± 0.000 | 0.695 ± 0.000 | 0.582 ± 0.003 |
| gpt5 | decoder | zero-shot | 3 | 0.925 ± 0.000 | 0.714 ± 0.001 | 0.719 ± 0.002 |
| gpt-mini | decoder | zero-shot | 3 | 0.930 ± 0.001 | 0.572 ± 0.002 | 0.518 ± 0.001 |
| llama | decoder | zero-shot | 3 | 0.925 ± 0.000 | 0.663 ± 0.001 | 0.539 ± 0.002 |
| mistral | decoder | zero-shot | 3 | 0.864 ± 0.000 | 0.590 ± 0.000 | 0.586 ± 0.001 |
| gemma | decoder | few-shot | 3 | 0.917 ± 0.000 | 0.686 ± 0.001 | 0.675 ± 0.001 |
| gpt5 | decoder | few-shot | 3 | 0.904 ± 0.001 | 0.664 ± 0.002 | 0.724 ± 0.003 |
| gpt-mini | decoder | few-shot | 3 | 0.924 ± 0.001 | 0.676 ± 0.001 | 0.666 ± 0.002 |
| llama | decoder | few-shot | 3 | 0.935 ± 0.000 | 0.648 ± 0.002 | 0.658 ± 0.002 |
| mistral | decoder | few-shot | 3 | 0.925 ± 0.000 | 0.571 ± 0.001 | 0.607 ± 0.001 |
| roberta-large | encoder | fine-tuned | 10 | 0.958 ± 0.001 | 0.762 ± 0.004 | 0.754 ± 0.008 |

## Precision per Category
| Model | Type | Condition | N | Precision Promote | Precision Contrast | Precision Attack |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.981 ± 0.000 | 0.585 ± 0.000 | 0.540 ± 0.003 |
| gpt5 | decoder | zero-shot | 3 | 0.983 ± 0.000 | 0.639 ± 0.002 | 0.599 ± 0.002 |
| gpt-mini | decoder | zero-shot | 3 | 0.964 ± 0.000 | 0.760 ± 0.003 | 0.356 ± 0.000 |
| llama | decoder | zero-shot | 3 | 0.964 ± 0.000 | 0.569 ± 0.001 | 0.584 ± 0.001 |
| mistral | decoder | zero-shot | 3 | 0.982 ± 0.000 | 0.469 ± 0.000 | 0.488 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.969 ± 0.000 | 0.628 ± 0.000 | 0.554 ± 0.001 |
| gpt5 | decoder | few-shot | 3 | 0.974 ± 0.000 | 0.571 ± 0.002 | 0.614 ± 0.004 |
| gpt-mini | decoder | few-shot | 3 | 0.958 ± 0.001 | 0.663 ± 0.001 | 0.540 ± 0.002 |
| llama | decoder | few-shot | 3 | 0.936 ± 0.000 | 0.726 ± 0.001 | 0.551 ± 0.002 |
| mistral | decoder | few-shot | 3 | 0.943 ± 0.001 | 0.685 ± 0.002 | 0.450 ± 0.001 |
| roberta-large | encoder | fine-tuned | 10 | 0.959 ± 0.002 | 0.764 ± 0.007 | 0.753 ± 0.011 |

## Recall per Category
| Model | Type | Condition | N | Recall Promote | Recall Contrast | Recall Attack |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.857 ± 0.000 | 0.856 ± 0.001 | 0.631 ± 0.004 |
| gpt5 | decoder | zero-shot | 3 | 0.873 ± 0.001 | 0.808 ± 0.000 | 0.899 ± 0.002 |
| gpt-mini | decoder | zero-shot | 3 | 0.898 ± 0.001 | 0.459 ± 0.002 | 0.945 ± 0.004 |
| llama | decoder | zero-shot | 3 | 0.888 ± 0.000 | 0.792 ± 0.001 | 0.500 ± 0.002 |
| mistral | decoder | zero-shot | 3 | 0.771 ± 0.000 | 0.795 ± 0.001 | 0.733 ± 0.002 |
| gemma | decoder | few-shot | 3 | 0.870 ± 0.000 | 0.754 ± 0.002 | 0.862 ± 0.002 |
| gpt5 | decoder | few-shot | 3 | 0.842 ± 0.001 | 0.795 ± 0.004 | 0.880 ± 0.001 |
| gpt-mini | decoder | few-shot | 3 | 0.892 ± 0.000 | 0.690 ± 0.003 | 0.868 ± 0.001 |
| llama | decoder | few-shot | 3 | 0.934 ± 0.000 | 0.585 ± 0.003 | 0.815 ± 0.003 |
| mistral | decoder | few-shot | 3 | 0.908 ± 0.000 | 0.490 ± 0.002 | 0.930 ± 0.001 |
| roberta-large | encoder | fine-tuned | 10 | 0.957 ± 0.002 | 0.762 ± 0.012 | 0.765 ± 0.018 |

## Confusion Matrices (decoders: averaged over 3 runs; rows = true, cols = predicted)

### gemma — zero-shot
| true \ pred | Promote | Contrast | Attack |
|---|---|---|---|
| **Promote** | 9268 | 1174 | 374 |
| **Contrast** | 168 | 2195 | 200 |
| **Attack** | 12 | 381 | 673 |

### gpt5 — zero-shot
| true \ pred | Promote | Contrast | Attack |
|---|---|---|---|
| **Promote** | 9439 | 1072 | 305 |
| **Contrast** | 153 | 2072 | 338 |
| **Attack** | 10 | 97 | 959 |

### gpt-mini — zero-shot
| true \ pred | Promote | Contrast | Attack |
|---|---|---|---|
| **Promote** | 9712 | 326 | 779 |
| **Contrast** | 347 | 1175 | 1041 |
| **Attack** | 13 | 45 | 1008 |

### llama — zero-shot
| true \ pred | Promote | Contrast | Attack |
|---|---|---|---|
| **Promote** | 9608 | 1027 | 180 |
| **Contrast** | 333 | 2031 | 199 |
| **Attack** | 25 | 508 | 533 |

### mistral — zero-shot
| true \ pred | Promote | Contrast | Attack |
|---|---|---|---|
| **Promote** | 8342 | 2035 | 439 |
| **Contrast** | 144 | 2038 | 381 |
| **Attack** | 9 | 276 | 781 |

### gemma — few-shot
| true \ pred | Promote | Contrast | Attack |
|---|---|---|---|
| **Promote** | 9402 | 1012 | 395 |
| **Contrast** | 286 | 1934 | 344 |
| **Attack** | 15 | 132 | 919 |

### gpt5 — few-shot
| true \ pred | Promote | Contrast | Attack |
|---|---|---|---|
| **Promote** | 9111 | 1413 | 292 |
| **Contrast** | 230 | 2037 | 296 |
| **Attack** | 9 | 120 | 938 |

### gpt-mini — few-shot
| true \ pred | Promote | Contrast | Attack |
|---|---|---|---|
| **Promote** | 9645 | 774 | 397 |
| **Contrast** | 404 | 1768 | 391 |
| **Attack** | 19 | 122 | 925 |

### llama — few-shot
| true \ pred | Promote | Contrast | Attack |
|---|---|---|---|
| **Promote** | 10107 | 398 | 311 |
| **Contrast** | 666 | 1499 | 398 |
| **Attack** | 31 | 166 | 869 |

### mistral — few-shot
| true \ pred | Promote | Contrast | Attack |
|---|---|---|---|
| **Promote** | 9808 | 524 | 474 |
| **Contrast** | 570 | 1256 | 738 |
| **Attack** | 20 | 54 | 992 |

### roberta-large — fine-tuned
_Not available: the 10×10 CV runs saved summary statistics only, not out-of-fold predictions, so no confusion matrix can be reconstructed._