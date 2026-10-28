# Decoder results — macro-F1, mean (SD) over 3 runs

Each cell is `macro-F1 (SD)`.

`n/r` = no complete run (GPT-5.5 few-shot Dietrich). Dietrich GPT cells are 1 run (SD n/a); all others are 3.

**Proksch** is reported on the **5-class** scale (decoders were run 9-level; predictions collapsed 9→5 via `ceil((x+1)/2)` to match the encoder and the original coders).


## American Politics

### Fowler

| Model | Zero-shot | Few-shot |
|---|---|---|
| gemma | 0.731 (0.001) | 0.759 (0.001) |
| gpt5 | 0.786 (0.001) | 0.764 (0.002) |
| gpt_mini | 0.673 (0.001) | 0.755 (0.001) |
| llama | 0.709 (0.001) | 0.747 (0.001) |
| mistral | 0.680 (0.000) | 0.701 (0.001) |

### van der Veen

| Model | Zero-shot | Few-shot |
|---|---|---|
| gemma | 0.574 (0.002) | 0.596 (0.002) |
| gpt5 | 0.516 (0.001) | 0.544 (0.003) |
| gpt_mini | 0.528 (0.003) | 0.529 (0.000) |
| llama | 0.606 (0.001) | 0.597 (0.001) |
| mistral | 0.513 (0.001) | 0.584 (0.002) |

### Ballard

| Model | Zero-shot | Few-shot |
|---|---|---|
| gemma | 0.602 (0.001) | 0.643 (0.001) |
| gpt5 | 0.609 (0.001) | 0.651 (0.002) |
| gpt_mini | 0.499 (0.003) | 0.655 (0.004) |
| llama | 0.572 (0.001) | 0.640 (0.002) |
| mistral | 0.612 (0.001) | 0.608 (0.001) |

### Foy

| Model | Zero-shot | Few-shot |
|---|---|---|
| gemma | 0.892 (0.001) | 0.930 (0.002) |
| gpt5 | 0.839 (0.003) | 0.834 (0.001) |
| gpt_mini | 0.887 (0.003) | 0.834 (0.005) |
| llama | 0.808 (0.001) | 0.837 (0.001) |
| mistral | 0.847 (0.001) | 0.869 (0.000) |

## International Relations

### Dietrich

| Model | Zero-shot | Few-shot |
|---|---|---|
| gemma | 0.836 (0.000) | 0.836 (0.000) |
| gpt5 | 0.853 (0.000) | 0.854‡ |
| gpt_mini | 0.841 (0.000) | 0.841 (0.000) |
| llama | 0.823 (0.000) | 0.838 (0.000) |
| mistral | 0.814 (0.000) | 0.835 (0.000) |

### Goes

| Model | Zero-shot | Few-shot |
|---|---|---|
| gemma | 0.842 (0.002) | 0.835 (0.004) |
| gpt5 | 0.833 (0.002) | 0.840 (0.005) |
| gpt_mini | 0.806 (0.005) | 0.768 (0.008) |
| llama | 0.801 (0.002) | 0.805 (0.003) |
| mistral | 0.644 (0.000) | 0.758 (0.002) |

### Kostovicova

| Model | Zero-shot | Few-shot |
|---|---|---|
| gemma | 0.529 (0.003) | 0.536 (0.001) |
| gpt5 | 0.449 (0.010) | 0.546 (0.004) |
| gpt_mini | 0.437 (0.003) | 0.519 (0.007) |
| llama | 0.524 (0.003) | 0.541 (0.003) |
| mistral | 0.472 (0.001) | 0.431 (0.010) |

### Trubowitz

| Model | Zero-shot | Few-shot |
|---|---|---|
| gemma | 0.515 (0.004) | 0.549 (0.004) |
| gpt5 | 0.466 (0.006) | 0.551 (0.002) |
| gpt_mini | 0.490 (0.009) | 0.482 (0.006) |
| llama | 0.479 (0.002) | 0.492 (0.001) |
| mistral | 0.473 (0.001) | 0.513 (0.003) |

## Comparative Politics

### PopBERT

| Model | Zero-shot | Few-shot |
|---|---|---|
| gemma | 0.703 (0.001) | 0.691 (0.001) |
| gpt5 | 0.709 (0.001) | 0.684 (0.002) |
| gpt_mini | 0.734 (0.001) | 0.651 (0.000) |
| llama | 0.716 (0.000) | 0.717 (0.001) |
| mistral | 0.625 (0.001) | 0.706 (0.001) |

### ParlaCAP

| Model | Zero-shot | Few-shot |
|---|---|---|
| gemma | 0.682 (0.001) | 0.693 (0.003) |
| gpt5 | 0.696 (0.000) | 0.701 (0.004) |
| gpt_mini | 0.630 (0.002) | 0.640 (0.002) |
| llama | 0.594 (0.001) | 0.632 (0.001) |
| mistral | 0.552 (0.000) | 0.610 (0.004) |

### Heseltine

| Model | Zero-shot | Few-shot |
|---|---|---|
| gemma | 0.832 (0.002) | 0.810 (0.002) |
| gpt5 | 0.813 (0.001) | 0.815 (0.003) |
| gpt_mini | 0.787 (0.005) | 0.854 (0.002) |
| llama | 0.851 (0.001) | 0.837 (0.001) |
| mistral | 0.863 (0.000) | 0.820 (0.002) |

### Proksch

| Model | Zero-shot | Few-shot |
|---|---|---|
| gemma | 0.597 (0.010) | 0.622 (0.008) |
| gpt5 | 0.568 (0.005) | 0.632 (0.015) |
| gpt_mini | 0.525 (0.011) | 0.440 (0.019) |
| llama | 0.509 (0.002) | 0.426 (0.020) |
| mistral | 0.339 (0.006) | 0.350 (0.004) |
