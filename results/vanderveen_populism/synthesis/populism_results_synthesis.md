# Classifying Populist Language (van der Veen 2024) — model synthesis (all models)
Classes: **populist / pluralist / neutral**. Test set N=3,624 (populist 1,456 · neutral 1,122 · pluralist 1,046).
Decoders: mean over 3 runs. Encoders: mean over 10×10-fold CV. _Accuracy = mean only; F1/Precision/Recall = mean ± SD._

## Overall
| Model | Type | Condition | N | Accuracy | Macro F1 (Unweighted) | Weighted F1 |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.583 | 0.575 ± 0.001 | 0.581 ± 0.001 |
| gpt5 | decoder | zero-shot | 3 | 0.527 | 0.516 ± 0.001 | 0.515 ± 0.001 |
| gpt-mini | decoder | zero-shot | 3 | 0.553 | 0.528 ± 0.003 | 0.541 ± 0.003 |
| llama | decoder | zero-shot | 3 | 0.612 | 0.606 ± 0.001 | 0.616 ± 0.001 |
| mistral | decoder | zero-shot | 3 | 0.524 | 0.513 ± 0.001 | 0.509 ± 0.001 |
| gemma | decoder | few-shot | 3 | 0.602 | 0.596 ± 0.002 | 0.604 ± 0.002 |
| gpt5 | decoder | few-shot | 3 | 0.548 | 0.544 ± 0.003 | 0.543 ± 0.003 |
| gpt-mini | decoder | few-shot | 3 | 0.540 | 0.529 ± 0.000 | 0.533 ± 0.000 |
| llama | decoder | few-shot | 3 | 0.608 | 0.597 ± 0.001 | 0.609 ± 0.001 |
| mistral | decoder | few-shot | 3 | 0.595 | 0.584 ± 0.002 | 0.596 ± 0.002 |
| roberta-large | encoder | fine-tuned | 10 | 0.754 | 0.742 ± 0.004 | 0.753 ± 0.004 |
| roberta-base | encoder | fine-tuned | 10 | 0.737 | 0.725 ± 0.004 | 0.736 ± 0.004 |
| bert | encoder | fine-tuned | 10 | 0.650 | 0.636 ± 0.005 | 0.646 ± 0.005 |

## F1 per Category
| Model | Type | Condition | N | F1 Populist | F1 Pluralist | F1 Neutral |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.632 ± 0.001 | 0.513 ± 0.001 | 0.579 ± 0.001 |
| gpt5 | decoder | zero-shot | 3 | 0.505 ± 0.003 | 0.489 ± 0.004 | 0.553 ± 0.001 |
| gpt-mini | decoder | zero-shot | 3 | 0.638 ± 0.004 | 0.390 ± 0.010 | 0.557 ± 0.001 |
| llama | decoder | zero-shot | 3 | 0.700 ± 0.002 | 0.567 ± 0.001 | 0.553 ± 0.001 |
| mistral | decoder | zero-shot | 3 | 0.475 ± 0.002 | 0.505 ± 0.001 | 0.558 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.663 ± 0.002 | 0.539 ± 0.004 | 0.588 ± 0.002 |
| gpt5 | decoder | few-shot | 3 | 0.533 ± 0.007 | 0.536 ± 0.002 | 0.561 ± 0.002 |
| gpt-mini | decoder | few-shot | 3 | 0.558 ± 0.002 | 0.472 ± 0.004 | 0.557 ± 0.001 |
| llama | decoder | few-shot | 3 | 0.713 ± 0.001 | 0.525 ± 0.002 | 0.552 ± 0.003 |
| mistral | decoder | few-shot | 3 | 0.691 ± 0.000 | 0.518 ± 0.006 | 0.544 ± 0.002 |
| roberta-large | encoder | fine-tuned | 10 | 0.849 ± 0.004 | 0.705 ± 0.007 | 0.671 ± 0.007 |
| roberta-base | encoder | fine-tuned | 10 | 0.842 ± 0.003 | 0.684 ± 0.008 | 0.649 ± 0.008 |
| bert | encoder | fine-tuned | 10 | 0.733 ± 0.004 | 0.627 ± 0.008 | 0.549 ± 0.010 |

## Precision per Category
| Model | Type | Condition | N | Precision Populist | Precision Pluralist | Precision Neutral |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.825 ± 0.000 | 0.861 ± 0.003 | 0.432 ± 0.001 |
| gpt5 | decoder | zero-shot | 3 | 0.872 ± 0.007 | 0.883 ± 0.002 | 0.395 ± 0.001 |
| gpt-mini | decoder | zero-shot | 3 | 0.800 ± 0.006 | 0.903 ± 0.009 | 0.410 ± 0.000 |
| llama | decoder | zero-shot | 3 | 0.745 ± 0.002 | 0.686 ± 0.000 | 0.471 ± 0.002 |
| mistral | decoder | zero-shot | 3 | 0.892 ± 0.001 | 0.789 ± 0.001 | 0.399 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.839 ± 0.001 | 0.812 ± 0.004 | 0.447 ± 0.002 |
| gpt5 | decoder | few-shot | 3 | 0.888 ± 0.005 | 0.783 ± 0.005 | 0.409 ± 0.002 |
| gpt-mini | decoder | few-shot | 3 | 0.883 ± 0.003 | 0.808 ± 0.003 | 0.403 ± 0.001 |
| llama | decoder | few-shot | 3 | 0.738 ± 0.004 | 0.711 ± 0.005 | 0.463 ± 0.001 |
| mistral | decoder | few-shot | 3 | 0.722 ± 0.002 | 0.750 ± 0.007 | 0.448 ± 0.001 |
| roberta-large | encoder | fine-tuned | 10 | 0.853 ± 0.007 | 0.715 ± 0.013 | 0.674 ± 0.010 |
| roberta-base | encoder | fine-tuned | 10 | 0.846 ± 0.006 | 0.679 ± 0.013 | 0.662 ± 0.009 |
| bert | encoder | fine-tuned | 10 | 0.711 ± 0.005 | 0.618 ± 0.011 | 0.594 ± 0.011 |

## Recall per Category
| Model | Type | Condition | N | Recall Populist | Recall Pluralist | Recall Neutral |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.512 ± 0.002 | 0.366 ± 0.000 | 0.877 ± 0.001 |
| gpt5 | decoder | zero-shot | 3 | 0.356 ± 0.002 | 0.338 ± 0.004 | 0.925 ± 0.001 |
| gpt-mini | decoder | zero-shot | 3 | 0.531 ± 0.004 | 0.248 ± 0.007 | 0.866 ± 0.004 |
| llama | decoder | zero-shot | 3 | 0.660 ± 0.002 | 0.483 ± 0.001 | 0.670 ± 0.001 |
| mistral | decoder | zero-shot | 3 | 0.324 ± 0.002 | 0.371 ± 0.002 | 0.927 ± 0.001 |
| gemma | decoder | few-shot | 3 | 0.548 ± 0.002 | 0.403 ± 0.004 | 0.858 ± 0.002 |
| gpt5 | decoder | few-shot | 3 | 0.381 ± 0.006 | 0.408 ± 0.001 | 0.895 ± 0.002 |
| gpt-mini | decoder | few-shot | 3 | 0.408 ± 0.001 | 0.333 ± 0.004 | 0.905 ± 0.003 |
| llama | decoder | few-shot | 3 | 0.690 ± 0.002 | 0.417 ± 0.002 | 0.682 ± 0.005 |
| mistral | decoder | few-shot | 3 | 0.662 ± 0.002 | 0.396 ± 0.005 | 0.693 ± 0.004 |
| roberta-large | encoder | fine-tuned | 10 | 0.849 ± 0.006 | 0.704 ± 0.020 | 0.677 ± 0.019 |
| roberta-base | encoder | fine-tuned | 10 | 0.839 ± 0.010 | 0.698 ± 0.017 | 0.643 ± 0.022 |
| bert | encoder | fine-tuned | 10 | 0.759 ± 0.008 | 0.642 ± 0.014 | 0.516 ± 0.014 |

## Confusion Matrices (decoders: averaged over 3 runs; rows = true, cols = predicted)

### gemma — zero-shot
| true \ pred | Populist | Pluralist | Neutral |
|---|---|---|---|
| **Populist** | 746 | 21 | 689 |
| **Pluralist** | 61 | 382 | 603 |
| **Neutral** | 97 | 41 | 984 |

### gpt5 — zero-shot
| true \ pred | Populist | Pluralist | Neutral |
|---|---|---|---|
| **Populist** | 518 | 18 | 920 |
| **Pluralist** | 21 | 353 | 672 |
| **Neutral** | 55 | 29 | 1038 |

### gpt-mini — zero-shot
| true \ pred | Populist | Pluralist | Neutral |
|---|---|---|---|
| **Populist** | 771 | 12 | 670 |
| **Pluralist** | 59 | 260 | 726 |
| **Neutral** | 134 | 16 | 971 |

### llama — zero-shot
| true \ pred | Populist | Pluralist | Neutral |
|---|---|---|---|
| **Populist** | 961 | 92 | 403 |
| **Pluralist** | 99 | 505 | 442 |
| **Neutral** | 231 | 140 | 752 |

### mistral — zero-shot
| true \ pred | Populist | Pluralist | Neutral |
|---|---|---|---|
| **Populist** | 472 | 62 | 923 |
| **Pluralist** | 17 | 388 | 641 |
| **Neutral** | 40 | 42 | 1040 |

### gemma — few-shot
| true \ pred | Populist | Pluralist | Neutral |
|---|---|---|---|
| **Populist** | 798 | 36 | 622 |
| **Pluralist** | 55 | 422 | 569 |
| **Neutral** | 98 | 62 | 962 |

### gpt5 — few-shot
| true \ pred | Populist | Pluralist | Neutral |
|---|---|---|---|
| **Populist** | 555 | 54 | 847 |
| **Pluralist** | 16 | 427 | 603 |
| **Neutral** | 54 | 65 | 1004 |

### gpt-mini — few-shot
| true \ pred | Populist | Pluralist | Neutral |
|---|---|---|---|
| **Populist** | 594 | 35 | 827 |
| **Pluralist** | 19 | 348 | 678 |
| **Neutral** | 59 | 48 | 1015 |

### llama — few-shot
| true \ pred | Populist | Pluralist | Neutral |
|---|---|---|---|
| **Populist** | 1004 | 58 | 394 |
| **Pluralist** | 118 | 436 | 492 |
| **Neutral** | 238 | 119 | 765 |

### mistral — few-shot
| true \ pred | Populist | Pluralist | Neutral |
|---|---|---|---|
| **Populist** | 964 | 43 | 449 |
| **Pluralist** | 121 | 414 | 511 |
| **Neutral** | 249 | 95 | 778 |

### encoders (roberta-large, roberta-base, bert) — fine-tuned
_Not available: the 10×10 CV runs saved summary statistics only, not out-of-fold predictions, so no confusion matrix can be reconstructed._