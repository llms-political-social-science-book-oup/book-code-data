# Gender / DQI (Kostovicova & Paskhalis 2021) — model synthesis (all models)
**4-class** task (labels 0,1,2,3). Test set N=1,211 (class 2:658 · 1:240 · 3:224 · 0:89).
Decoders: mean over 3 runs. Encoders: mean over 10×10-fold CV (multilingual variants). _Accuracy = mean only; F1/Precision/Recall = mean ± SD._

## Overall
| Model | Type | Condition | N | Accuracy | Macro F1 (Unweighted) | Weighted F1 |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.610 | 0.529 ± 0.003 | 0.589 ± 0.001 |
| gpt5 | decoder | zero-shot | 3 | 0.486 | 0.449 ± 0.010 | 0.460 ± 0.008 |
| gpt-mini | decoder | zero-shot | 3 | 0.481 | 0.437 ± 0.003 | 0.474 ± 0.005 |
| llama | decoder | zero-shot | 3 | 0.603 | 0.524 ± 0.003 | 0.594 ± 0.003 |
| mistral | decoder | zero-shot | 3 | 0.573 | 0.472 ± 0.001 | 0.542 ± 0.001 |
| gemma | decoder | few-shot | 3 | 0.551 | 0.536 ± 0.001 | 0.552 ± 0.002 |
| gpt5 | decoder | few-shot | 3 | 0.544 | 0.546 ± 0.004 | 0.545 ± 0.005 |
| gpt-mini | decoder | few-shot | 3 | 0.499 | 0.519 ± 0.007 | 0.500 ± 0.007 |
| llama | decoder | few-shot | 3 | 0.577 | 0.541 ± 0.003 | 0.578 ± 0.004 |
| mistral | decoder | few-shot | 3 | 0.415 | 0.431 ± 0.010 | 0.396 ± 0.007 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.624 | 0.525 ± 0.020 | 0.606 ± 0.012 |
| xlm-roberta-base | encoder | fine-tuned | 10 | 0.609 | 0.484 ± 0.008 | 0.580 ± 0.008 |
| bert-multilingual | encoder | fine-tuned | 10 | 0.588 | 0.482 ± 0.013 | 0.574 ± 0.008 |

## F1 per Class
| Model | Type | Condition | N | Class 0 | Class 1 | Class 2 | Class 3 |
|---|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.579 ± 0.009 | 0.284 ± 0.004 | 0.720 ± 0.001 | 0.533 ± 0.000 |
| gpt5 | decoder | zero-shot | 3 | 0.590 ± 0.017 | 0.161 ± 0.021 | 0.535 ± 0.009 | 0.513 ± 0.001 |
| gpt-mini | decoder | zero-shot | 3 | 0.376 ± 0.010 | 0.341 ± 0.016 | 0.525 ± 0.007 | 0.505 ± 0.008 |
| llama | decoder | zero-shot | 3 | 0.424 ± 0.006 | 0.405 ± 0.002 | 0.695 ± 0.002 | 0.571 ± 0.003 |
| mistral | decoder | zero-shot | 3 | 0.529 ± 0.000 | 0.457 ± 0.001 | 0.687 ± 0.000 | 0.212 ± 0.003 |
| gemma | decoder | few-shot | 3 | 0.557 ± 0.005 | 0.444 ± 0.003 | 0.589 ± 0.002 | 0.554 ± 0.004 |
| gpt5 | decoder | few-shot | 3 | 0.610 ± 0.012 | 0.460 ± 0.012 | 0.566 ± 0.008 | 0.550 ± 0.003 |
| gpt-mini | decoder | few-shot | 3 | 0.626 ± 0.010 | 0.440 ± 0.010 | 0.500 ± 0.010 | 0.511 ± 0.009 |
| llama | decoder | few-shot | 3 | 0.519 ± 0.008 | 0.413 ± 0.011 | 0.642 ± 0.006 | 0.589 ± 0.011 |
| mistral | decoder | few-shot | 3 | 0.541 ± 0.031 | 0.340 ± 0.011 | 0.371 ± 0.009 | 0.473 ± 0.006 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.439 ± 0.070 | 0.426 ± 0.026 | 0.727 ± 0.009 | 0.508 ± 0.021 |
| xlm-roberta-base | encoder | fine-tuned | 10 | 0.395 ± 0.033 | 0.440 ± 0.020 | 0.725 ± 0.009 | 0.378 ± 0.022 |
| bert-multilingual | encoder | fine-tuned | 10 | 0.325 ± 0.047 | 0.422 ± 0.020 | 0.692 ± 0.009 | 0.488 ± 0.019 |

## Precision per Class
| Model | Type | Condition | N | Class 0 | Class 1 | Class 2 | Class 3 |
|---|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.486 ± 0.007 | 0.377 ± 0.002 | 0.659 ± 0.001 | 0.685 ± 0.006 |
| gpt5 | decoder | zero-shot | 3 | 0.688 ± 0.036 | 0.462 ± 0.041 | 0.589 ± 0.007 | 0.361 ± 0.002 |
| gpt-mini | decoder | zero-shot | 3 | 0.825 ± 0.036 | 0.426 ± 0.010 | 0.618 ± 0.001 | 0.358 ± 0.004 |
| llama | decoder | zero-shot | 3 | 0.727 ± 0.004 | 0.445 ± 0.005 | 0.671 ± 0.001 | 0.524 ± 0.004 |
| mistral | decoder | zero-shot | 3 | 0.766 ± 0.000 | 0.399 ± 0.002 | 0.627 ± 0.001 | 0.659 ± 0.006 |
| gemma | decoder | few-shot | 3 | 0.442 ± 0.001 | 0.515 ± 0.005 | 0.738 ± 0.005 | 0.418 ± 0.003 |
| gpt5 | decoder | few-shot | 3 | 0.684 ± 0.007 | 0.491 ± 0.012 | 0.688 ± 0.005 | 0.407 ± 0.001 |
| gpt-mini | decoder | few-shot | 3 | 0.661 ± 0.023 | 0.414 ± 0.018 | 0.673 ± 0.005 | 0.377 ± 0.008 |
| llama | decoder | few-shot | 3 | 0.534 ± 0.016 | 0.431 ± 0.014 | 0.703 ± 0.007 | 0.481 ± 0.007 |
| mistral | decoder | few-shot | 3 | 0.504 ± 0.021 | 0.367 ± 0.019 | 0.641 ± 0.009 | 0.320 ± 0.004 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.673 ± 0.086 | 0.457 ± 0.025 | 0.671 ± 0.010 | 0.621 ± 0.020 |
| xlm-roberta-base | encoder | fine-tuned | 10 | 0.652 ± 0.093 | 0.446 ± 0.018 | 0.651 ± 0.005 | 0.680 ± 0.028 |
| bert-multilingual | encoder | fine-tuned | 10 | 0.508 ± 0.090 | 0.428 ± 0.014 | 0.659 ± 0.009 | 0.545 ± 0.028 |

## Recall per Class
| Model | Type | Condition | N | Class 0 | Class 1 | Class 2 | Class 3 |
|---|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.715 ± 0.011 | 0.228 ± 0.005 | 0.794 ± 0.003 | 0.436 ± 0.002 |
| gpt5 | decoder | zero-shot | 3 | 0.517 ± 0.009 | 0.097 ± 0.014 | 0.489 ± 0.012 | 0.882 ± 0.008 |
| gpt-mini | decoder | zero-shot | 3 | 0.243 ± 0.011 | 0.285 ± 0.017 | 0.457 ± 0.010 | 0.859 ± 0.024 |
| llama | decoder | zero-shot | 3 | 0.300 ± 0.005 | 0.371 ± 0.000 | 0.720 ± 0.004 | 0.628 ± 0.002 |
| mistral | decoder | zero-shot | 3 | 0.404 ± 0.000 | 0.535 ± 0.002 | 0.761 ± 0.001 | 0.126 ± 0.002 |
| gemma | decoder | few-shot | 3 | 0.753 ± 0.016 | 0.390 ± 0.007 | 0.490 ± 0.001 | 0.821 ± 0.006 |
| gpt5 | decoder | few-shot | 3 | 0.551 ± 0.024 | 0.432 ± 0.014 | 0.480 ± 0.010 | 0.851 ± 0.011 |
| gpt-mini | decoder | few-shot | 3 | 0.596 ± 0.016 | 0.469 ± 0.016 | 0.398 ± 0.012 | 0.790 ± 0.007 |
| llama | decoder | few-shot | 3 | 0.506 ± 0.000 | 0.397 ± 0.011 | 0.591 ± 0.007 | 0.757 ± 0.019 |
| mistral | decoder | few-shot | 3 | 0.584 ± 0.046 | 0.317 ± 0.010 | 0.261 ± 0.008 | 0.903 ± 0.012 |
| xlm-roberta-large | encoder | fine-tuned | 10 | 0.359 ± 0.067 | 0.415 ± 0.034 | 0.797 ± 0.015 | 0.450 ± 0.028 |
| xlm-roberta-base | encoder | fine-tuned | 10 | 0.310 ± 0.045 | 0.452 ± 0.029 | 0.823 ± 0.017 | 0.277 ± 0.019 |
| bert-multilingual | encoder | fine-tuned | 10 | 0.267 ± 0.043 | 0.437 ± 0.031 | 0.734 ± 0.014 | 0.465 ± 0.031 |

## Confusion Matrices (decoders: averaged over 3 runs; rows = true, cols = predicted)

### gemma — zero-shot
| true \ pred | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 64 | 10 | 15 | 0 |
| **1** | 44 | 55 | 137 | 4 |
| **2** | 22 | 73 | 522 | 41 |
| **3** | 2 | 7 | 118 | 98 |

### gpt5 — zero-shot
| true \ pred | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 46 | 9 | 30 | 4 |
| **1** | 20 | 23 | 169 | 28 |
| **2** | 1 | 17 | 322 | 318 |
| **3** | 0 | 1 | 25 | 198 |

### gpt-mini — zero-shot
| true \ pred | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 22 | 47 | 16 | 4 |
| **1** | 3 | 68 | 140 | 28 |
| **2** | 1 | 43 | 301 | 313 |
| **3** | 0 | 2 | 30 | 192 |

### llama — zero-shot
| true \ pred | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 27 | 47 | 14 | 2 |
| **1** | 7 | 89 | 136 | 8 |
| **2** | 3 | 63 | 474 | 118 |
| **3** | 0 | 1 | 82 | 141 |

### mistral — zero-shot
| true \ pred | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 36 | 40 | 11 | 2 |
| **1** | 8 | 128 | 103 | 1 |
| **2** | 3 | 142 | 501 | 12 |
| **3** | 0 | 10 | 185 | 28 |

### gemma — few-shot
| true \ pred | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 67 | 13 | 8 | 1 |
| **1** | 54 | 94 | 74 | 18 |
| **2** | 28 | 70 | 323 | 237 |
| **3** | 2 | 6 | 32 | 184 |

### gpt5 — few-shot
| true \ pred | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 49 | 25 | 13 | 2 |
| **1** | 20 | 104 | 102 | 14 |
| **2** | 2 | 77 | 316 | 262 |
| **3** | 0 | 5 | 29 | 191 |

### gpt-mini — few-shot
| true \ pred | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 53 | 26 | 7 | 2 |
| **1** | 22 | 113 | 86 | 20 |
| **2** | 5 | 121 | 262 | 270 |
| **3** | 0 | 13 | 34 | 177 |

### llama — few-shot
| true \ pred | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 45 | 35 | 7 | 1 |
| **1** | 23 | 95 | 112 | 9 |
| **2** | 15 | 82 | 389 | 172 |
| **3** | 1 | 9 | 45 | 170 |

### mistral — few-shot
| true \ pred | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 52 | 25 | 7 | 4 |
| **1** | 37 | 76 | 78 | 49 |
| **2** | 14 | 96 | 172 | 376 |
| **3** | 0 | 10 | 11 | 202 |

### encoders (xlm-roberta-large, xlm-roberta-base, bert-multilingual) — fine-tuned
_Not available: the 10×10 CV runs saved summary statistics only, not out-of-fold predictions, so no confusion matrix can be reconstructed._