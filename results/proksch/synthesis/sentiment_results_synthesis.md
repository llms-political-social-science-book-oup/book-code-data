# Multilingual Sentiment (Proksch et al. 2019, SOTEU 2010) — model synthesis (all models)
Ordinal sentiment, reported on the **unified 5-class scale** (1 = most negative … 5 = most positive). Test set N=301 (class supports 1:47 · 2:76 · 3:72 · 4:69 · 5:37).
**Scale reconciliation:** decoders run on a 9-point recode are collapsed 9→5 ({1→1, 2,3→2, 4,5→3, 6,7→4, 8,9→5}); the encoder was fine-tuned natively on the 5-class round-half-up recode. Collapsing reproduces the encoder's exact 5-class labels, so the two are directly comparable.
Decoders: mean over 3 runs. Encoder: mean over 10×10-fold CV. _Accuracy = mean only; F1/Precision/Recall = mean ± SD. Native 9-class macro F1 shown for decoders as reference._

## Overall
| Model | Type | Condition | N | Accuracy | Macro F1 (Unweighted) | Weighted F1 |
|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.595 | 0.597 ± 0.010 | 0.586 ± 0.010 |
| gpt5 | decoder | zero-shot | 3 | 0.573 | 0.568 ± 0.005 | 0.558 ± 0.005 |
| gpt-mini | decoder | zero-shot | 3 | 0.529 | 0.525 ± 0.011 | 0.523 ± 0.009 |
| llama | decoder | zero-shot | 3 | 0.505 | 0.509 ± 0.002 | 0.492 ± 0.003 |
| mistral | decoder | zero-shot | 3 | 0.427 | 0.339 ± 0.006 | 0.376 ± 0.006 |
| gemma | decoder | few-shot | 3 | 0.620 | 0.622 ± 0.008 | 0.617 ± 0.007 |
| gpt5 | decoder | few-shot | 3 | 0.622 | 0.632 ± 0.015 | 0.617 ± 0.015 |
| gpt-mini | decoder | few-shot | 3 | 0.488 | 0.440 ± 0.019 | 0.459 ± 0.016 |
| llama | decoder | few-shot | 3 | 0.453 | 0.426 ± 0.020 | 0.430 ± 0.016 |
| mistral | decoder | few-shot | 3 | 0.426 | 0.350 ± 0.004 | 0.387 ± 0.004 |
| roberta-large | encoder | fine-tuned | 10 | 0.500 | 0.464 ± 0.033 | 0.474 ± 0.028 |

## Decoders — native 9-class macro F1 (reference, not comparable to encoder)
| Model | Condition | Native 9-class Macro F1 |
|---|---|---|
| gemma | zero-shot | 0.405 |
| gpt5 | zero-shot | 0.352 |
| gpt-mini | zero-shot | 0.300 |
| llama | zero-shot | 0.283 |
| mistral | zero-shot | 0.165 |
| gemma | few-shot | 0.407 |
| gpt5 | few-shot | 0.423 |
| gpt-mini | few-shot | 0.268 |
| llama | few-shot | 0.225 |
| mistral | few-shot | 0.159 |

## F1 per Class (5-class)
| Model | Type | Condition | N | Class 1 | Class 2 | Class 3 | Class 4 | Class 5 |
|---|---|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.676 ± 0.015 | 0.640 ± 0.009 | 0.416 ± 0.018 | 0.618 ± 0.015 | 0.635 ± 0.013 |
| gpt5 | decoder | zero-shot | 3 | 0.571 ± 0.033 | 0.619 ± 0.019 | 0.380 ± 0.017 | 0.617 ± 0.011 | 0.652 ± 0.032 |
| gpt-mini | decoder | zero-shot | 3 | 0.532 ± 0.035 | 0.553 ± 0.013 | 0.422 ± 0.019 | 0.578 ± 0.026 | 0.542 ± 0.049 |
| llama | decoder | zero-shot | 3 | 0.693 ± 0.006 | 0.398 ± 0.004 | 0.417 ± 0.010 | 0.524 ± 0.004 | 0.515 ± 0.008 |
| mistral | decoder | zero-shot | 3 | 0.265 ± 0.015 | 0.350 ± 0.004 | 0.447 ± 0.011 | 0.582 ± 0.006 | 0.051 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.729 ± 0.004 | 0.643 ± 0.002 | 0.498 ± 0.019 | 0.648 ± 0.005 | 0.593 ± 0.025 |
| gpt5 | decoder | few-shot | 3 | 0.732 ± 0.016 | 0.626 ± 0.016 | 0.463 ± 0.023 | 0.652 ± 0.017 | 0.685 ± 0.020 |
| gpt-mini | decoder | few-shot | 3 | 0.234 ± 0.032 | 0.492 ± 0.004 | 0.452 ± 0.032 | 0.609 ± 0.007 | 0.415 ± 0.045 |
| llama | decoder | few-shot | 3 | 0.424 ± 0.021 | 0.302 ± 0.006 | 0.497 ± 0.007 | 0.533 ± 0.025 | 0.376 ± 0.057 |
| mistral | decoder | few-shot | 3 | 0.245 ± 0.016 | 0.411 ± 0.003 | 0.477 ± 0.008 | 0.515 ± 0.012 | 0.103 ± 0.000 |
| roberta-large | encoder | fine-tuned | 10 | 0.553 ± 0.078 | 0.512 ± 0.034 | 0.391 ± 0.040 | 0.549 ± 0.024 | 0.314 ± 0.073 |

## Precision per Class (5-class)
| Model | Type | Condition | N | Class 1 | Class 2 | Class 3 | Class 4 | Class 5 |
|---|---|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.926 ± 0.002 | 0.553 ± 0.011 | 0.540 ± 0.018 | 0.587 ± 0.019 | 0.562 ± 0.007 |
| gpt5 | decoder | zero-shot | 3 | 0.869 ± 0.009 | 0.575 ± 0.019 | 0.529 ± 0.015 | 0.503 ± 0.009 | 0.630 ± 0.022 |
| gpt-mini | decoder | zero-shot | 3 | 0.871 ± 0.044 | 0.516 ± 0.018 | 0.500 ± 0.020 | 0.495 ± 0.023 | 0.508 ± 0.036 |
| llama | decoder | zero-shot | 3 | 0.607 ± 0.009 | 0.657 ± 0.014 | 0.417 ± 0.010 | 0.454 ± 0.003 | 0.500 ± 0.010 |
| mistral | decoder | zero-shot | 3 | 0.880 ± 0.007 | 0.407 ± 0.003 | 0.378 ± 0.010 | 0.446 ± 0.005 | 0.500 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.849 ± 0.011 | 0.607 ± 0.003 | 0.568 ± 0.013 | 0.555 ± 0.010 | 0.704 ± 0.010 |
| gpt5 | decoder | few-shot | 3 | 0.823 ± 0.014 | 0.639 ± 0.016 | 0.554 ± 0.022 | 0.550 ± 0.014 | 0.677 ± 0.036 |
| gpt-mini | decoder | few-shot | 3 | 0.903 ± 0.071 | 0.462 ± 0.008 | 0.447 ± 0.015 | 0.486 ± 0.002 | 0.642 ± 0.068 |
| llama | decoder | few-shot | 3 | 0.908 ± 0.029 | 0.485 ± 0.000 | 0.360 ± 0.006 | 0.500 ± 0.022 | 0.752 ± 0.037 |
| mistral | decoder | few-shot | 3 | 0.911 ± 0.064 | 0.457 ± 0.003 | 0.353 ± 0.005 | 0.481 ± 0.004 | 1.000 ± 0.000 |
| roberta-large | encoder | fine-tuned | 10 | 0.653 ± 0.048 | 0.566 ± 0.039 | 0.441 ± 0.026 | 0.486 ± 0.027 | 0.424 ± 0.099 |

## Recall per Class (5-class)
| Model | Type | Condition | N | Class 1 | Class 2 | Class 3 | Class 4 | Class 5 |
|---|---|---|---|---|---|---|---|---|
| gemma | decoder | zero-shot | 3 | 0.532 ± 0.017 | 0.759 ± 0.006 | 0.338 ± 0.017 | 0.652 ± 0.012 | 0.730 ± 0.022 |
| gpt5 | decoder | zero-shot | 3 | 0.426 ± 0.035 | 0.671 ± 0.019 | 0.296 ± 0.017 | 0.797 ± 0.012 | 0.676 ± 0.044 |
| gpt-mini | decoder | zero-shot | 3 | 0.383 ± 0.030 | 0.596 ± 0.012 | 0.366 ± 0.017 | 0.696 ± 0.043 | 0.586 ± 0.077 |
| llama | decoder | zero-shot | 3 | 0.809 ± 0.000 | 0.285 ± 0.006 | 0.417 ± 0.011 | 0.618 ± 0.007 | 0.532 ± 0.013 |
| mistral | decoder | zero-shot | 3 | 0.156 ± 0.010 | 0.307 ± 0.006 | 0.546 ± 0.013 | 0.836 ± 0.007 | 0.027 ± 0.000 |
| gemma | decoder | few-shot | 3 | 0.638 ± 0.000 | 0.684 ± 0.000 | 0.444 ± 0.023 | 0.778 ± 0.007 | 0.514 ± 0.038 |
| gpt5 | decoder | few-shot | 3 | 0.660 ± 0.017 | 0.614 ± 0.016 | 0.398 ± 0.024 | 0.802 ± 0.025 | 0.694 ± 0.013 |
| gpt-mini | decoder | few-shot | 3 | 0.135 ± 0.020 | 0.526 ± 0.011 | 0.458 ± 0.052 | 0.816 ± 0.025 | 0.306 ± 0.034 |
| llama | decoder | few-shot | 3 | 0.277 ± 0.017 | 0.219 ± 0.006 | 0.806 ± 0.011 | 0.570 ± 0.030 | 0.252 ± 0.046 |
| mistral | decoder | few-shot | 3 | 0.142 ± 0.010 | 0.373 ± 0.006 | 0.736 ± 0.023 | 0.556 ± 0.030 | 0.054 ± 0.000 |
| roberta-large | encoder | fine-tuned | 10 | 0.564 ± 0.078 | 0.519 ± 0.039 | 0.389 ± 0.065 | 0.708 ± 0.032 | 0.321 ± 0.105 |

## Confusion Matrices — 5-class (decoders: averaged over 3 runs; rows = true, cols = predicted)

### gemma — zero-shot
| true \ pred | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **1** | 25 | 21 | 1 | 0 | 0 |
| **2** | 2 | 58 | 13 | 3 | 1 |
| **3** | 0 | 26 | 24 | 20 | 2 |
| **4** | 0 | 0 | 6 | 45 | 18 |
| **5** | 0 | 0 | 1 | 9 | 27 |

### gpt5 — zero-shot
| true \ pred | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **1** | 20 | 25 | 2 | 0 | 0 |
| **2** | 3 | 51 | 16 | 6 | 0 |
| **3** | 0 | 13 | 21 | 37 | 1 |
| **4** | 0 | 0 | 1 | 55 | 13 |
| **5** | 0 | 0 | 0 | 12 | 25 |

### gpt-mini — zero-shot
| true \ pred | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **1** | 18 | 27 | 1 | 1 | 0 |
| **2** | 3 | 45 | 22 | 6 | 0 |
| **3** | 0 | 16 | 26 | 27 | 3 |
| **4** | 0 | 0 | 3 | 48 | 18 |
| **5** | 0 | 0 | 1 | 15 | 22 |

### llama — zero-shot
| true \ pred | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **1** | 38 | 5 | 4 | 0 | 0 |
| **2** | 20 | 22 | 27 | 7 | 0 |
| **3** | 4 | 7 | 30 | 28 | 3 |
| **4** | 0 | 0 | 10 | 43 | 16 |
| **5** | 0 | 0 | 1 | 16 | 20 |

### mistral — zero-shot
| true \ pred | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **1** | 7 | 32 | 6 | 2 | 0 |
| **2** | 1 | 23 | 48 | 4 | 0 |
| **3** | 0 | 2 | 39 | 30 | 1 |
| **4** | 0 | 0 | 11 | 58 | 0 |
| **5** | 0 | 0 | 0 | 36 | 1 |

### gemma — few-shot
| true \ pred | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **1** | 30 | 15 | 2 | 0 | 0 |
| **2** | 5 | 52 | 14 | 5 | 0 |
| **3** | 0 | 19 | 32 | 20 | 1 |
| **4** | 0 | 0 | 8 | 54 | 7 |
| **5** | 0 | 0 | 0 | 18 | 19 |

### gpt5 — few-shot
| true \ pred | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **1** | 31 | 14 | 2 | 0 | 0 |
| **2** | 7 | 47 | 19 | 4 | 0 |
| **3** | 0 | 12 | 29 | 30 | 1 |
| **4** | 0 | 0 | 2 | 55 | 12 |
| **5** | 0 | 0 | 0 | 11 | 26 |

### gpt-mini — few-shot
| true \ pred | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **1** | 6 | 38 | 3 | 0 | 0 |
| **2** | 1 | 40 | 30 | 6 | 0 |
| **3** | 0 | 9 | 33 | 29 | 1 |
| **4** | 0 | 0 | 8 | 56 | 5 |
| **5** | 0 | 0 | 0 | 25 | 11 |

### llama — few-shot
| true \ pred | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **1** | 13 | 16 | 18 | 0 | 0 |
| **2** | 1 | 17 | 57 | 1 | 0 |
| **3** | 0 | 1 | 58 | 12 | 0 |
| **4** | 0 | 0 | 27 | 39 | 3 |
| **5** | 0 | 0 | 2 | 26 | 9 |

### mistral — few-shot
| true \ pred | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **1** | 7 | 31 | 9 | 0 | 0 |
| **2** | 1 | 28 | 45 | 2 | 0 |
| **3** | 0 | 3 | 53 | 16 | 0 |
| **4** | 0 | 0 | 31 | 38 | 0 |
| **5** | 0 | 0 | 12 | 23 | 2 |

### roberta-large — fine-tuned
_Not available: the 10×10 CV runs saved summary statistics only, not out-of-fold predictions, so no confusion matrix can be reconstructed._