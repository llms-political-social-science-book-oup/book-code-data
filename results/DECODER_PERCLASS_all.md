# Decoder results — per-category, all datasets

Decoder LLMs, zero-shot & few-shot. Metrics = mean over **3 runs** (SD in parentheses for F1); **Dietrich GPT cells are 1 run** so SD shows `(–)`. Per-class P/R/F1, macro/weighted-F1, accuracy, and n_valid are computed directly from the prediction files.

`‡` = GPT-5.5 few-shot Dietrich, computed on the first 37,469 of 52,744 rows.


## American Politics

### Fowler  (3 classes)

| Config | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R | Acc | n_valid |
|---|---|---|---|---|---|---|
| gemma zero-shot | 0.731 (0.001) | 0.851 | 0.702 | 0.781 | 0.840 | 14,445 |
| gemma few-shot | 0.759 (0.001) | 0.858 | 0.717 | 0.829 | 0.849 | 14,438 |
| gpt-5.5 zero-shot | 0.786 (0.001) | 0.872 | 0.740 | 0.860 | 0.863 | 14,445 |
| gpt-5.5 few-shot | 0.764 (0.002) | 0.848 | 0.720 | 0.839 | 0.837 | 14,445 |
| gpt-mini zero-shot | 0.673 (0.001) | 0.836 | 0.694 | 0.767 | 0.823 | 14,445 |
| gpt-mini few-shot | 0.755 (0.001) | 0.861 | 0.721 | 0.816 | 0.854 | 14,445 |
| llama zero-shot | 0.709 (0.001) | 0.850 | 0.706 | 0.727 | 0.843 | 14,444 |
| llama few-shot | 0.747 (0.001) | 0.864 | 0.738 | 0.778 | 0.864 | 14,444 |
| mistral zero-shot | 0.680 (0.000) | 0.795 | 0.646 | 0.766 | 0.773 | 14,445 |
| mistral few-shot | 0.701 (0.001) | 0.839 | 0.693 | 0.776 | 0.835 | 14,434 |

_Per-class F1 (SD) / Precision / Recall:_

| Config | Class | F1 (SD) | P | R | support |
|---|---|---|---|---|---|
| gemma zero-shot | Attack | 0.582 (0.003) | 0.540 | 0.631 | 1,066 |
| gemma zero-shot | Contrast | 0.695 (0.000) | 0.585 | 0.856 | 2,563 |
| gemma zero-shot | Promote | 0.915 (0.000) | 0.981 | 0.857 | 10,816 |
| gemma few-shot | Attack | 0.675 (0.001) | 0.554 | 0.862 | 1,066 |
| gemma few-shot | Contrast | 0.686 (0.001) | 0.628 | 0.754 | 2,563 |
| gemma few-shot | Promote | 0.917 (0.000) | 0.969 | 0.870 | 10,809 |
| gpt-5.5 zero-shot | Attack | 0.719 (0.002) | 0.599 | 0.899 | 1,066 |
| gpt-5.5 zero-shot | Contrast | 0.714 (0.001) | 0.639 | 0.808 | 2,563 |
| gpt-5.5 zero-shot | Promote | 0.925 (0.000) | 0.983 | 0.873 | 10,816 |
| gpt-5.5 few-shot | Attack | 0.724 (0.003) | 0.614 | 0.880 | 1,066 |
| gpt-5.5 few-shot | Contrast | 0.664 (0.002) | 0.571 | 0.795 | 2,563 |
| gpt-5.5 few-shot | Promote | 0.904 (0.001) | 0.974 | 0.842 | 10,816 |
| gpt-mini zero-shot | Attack | 0.518 (0.001) | 0.356 | 0.945 | 1,066 |
| gpt-mini zero-shot | Contrast | 0.572 (0.002) | 0.760 | 0.459 | 2,563 |
| gpt-mini zero-shot | Promote | 0.930 (0.001) | 0.964 | 0.898 | 10,816 |
| gpt-mini few-shot | Attack | 0.666 (0.002) | 0.540 | 0.868 | 1,066 |
| gpt-mini few-shot | Contrast | 0.676 (0.001) | 0.663 | 0.690 | 2,563 |
| gpt-mini few-shot | Promote | 0.924 (0.001) | 0.958 | 0.892 | 10,816 |
| llama zero-shot | Attack | 0.539 (0.002) | 0.584 | 0.500 | 1,066 |
| llama zero-shot | Contrast | 0.663 (0.001) | 0.569 | 0.792 | 2,563 |
| llama zero-shot | Promote | 0.925 (0.000) | 0.964 | 0.888 | 10,815 |
| llama few-shot | Attack | 0.658 (0.002) | 0.551 | 0.815 | 1,065 |
| llama few-shot | Contrast | 0.648 (0.002) | 0.726 | 0.585 | 2,563 |
| llama few-shot | Promote | 0.935 (0.000) | 0.936 | 0.934 | 10,816 |
| mistral zero-shot | Attack | 0.586 (0.001) | 0.488 | 0.733 | 1,066 |
| mistral zero-shot | Contrast | 0.590 (0.000) | 0.469 | 0.795 | 2,563 |
| mistral zero-shot | Promote | 0.864 (0.000) | 0.982 | 0.771 | 10,816 |
| mistral few-shot | Attack | 0.607 (0.001) | 0.450 | 0.930 | 1,066 |
| mistral few-shot | Contrast | 0.571 (0.001) | 0.685 | 0.490 | 2,563 |
| mistral few-shot | Promote | 0.925 (0.000) | 0.943 | 0.908 | 10,805 |

### van der Veen  (3 classes)

| Config | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R | Acc | n_valid |
|---|---|---|---|---|---|---|
| gemma zero-shot | 0.573 (0.002) | 0.580 | 0.706 | 0.584 | 0.582 | 3,624 |
| gemma few-shot | 0.596 (0.002) | 0.604 | 0.699 | 0.603 | 0.602 | 3,624 |
| gpt-5.5 zero-shot | 0.516 (0.001) | 0.515 | 0.716 | 0.539 | 0.527 | 3,624 |
| gpt-5.5 few-shot | 0.544 (0.003) | 0.543 | 0.693 | 0.561 | 0.548 | 3,624 |
| gpt-mini zero-shot | 0.528 (0.003) | 0.541 | 0.704 | 0.548 | 0.553 | 3,619 |
| gpt-mini few-shot | 0.529 (0.000) | 0.533 | 0.698 | 0.549 | 0.540 | 3,624 |
| llama zero-shot | 0.606 (0.001) | 0.616 | 0.634 | 0.604 | 0.612 | 3,624 |
| llama few-shot | 0.597 (0.001) | 0.609 | 0.638 | 0.596 | 0.608 | 3,624 |
| mistral zero-shot | 0.513 (0.001) | 0.509 | 0.693 | 0.541 | 0.524 | 3,624 |
| mistral few-shot | 0.584 (0.002) | 0.596 | 0.640 | 0.584 | 0.595 | 3,624 |

_Per-class F1 (SD) / Precision / Recall:_

| Config | Class | F1 (SD) | P | R | support |
|---|---|---|---|---|---|
| gemma zero-shot | neutral | 0.579 (0.001) | 0.431 | 0.878 | 1,122 |
| gemma zero-shot | pluralist | 0.512 (0.002) | 0.861 | 0.364 | 1,046 |
| gemma zero-shot | populist | 0.630 (0.004) | 0.825 | 0.509 | 1,456 |
| gemma few-shot | neutral | 0.588 (0.002) | 0.447 | 0.858 | 1,122 |
| gemma few-shot | pluralist | 0.539 (0.004) | 0.812 | 0.403 | 1,046 |
| gemma few-shot | populist | 0.663 (0.002) | 0.839 | 0.548 | 1,456 |
| gpt-5.5 zero-shot | neutral | 0.553 (0.001) | 0.395 | 0.925 | 1,122 |
| gpt-5.5 zero-shot | pluralist | 0.489 (0.004) | 0.883 | 0.338 | 1,046 |
| gpt-5.5 zero-shot | populist | 0.505 (0.003) | 0.872 | 0.356 | 1,456 |
| gpt-5.5 few-shot | neutral | 0.561 (0.002) | 0.409 | 0.895 | 1,122 |
| gpt-5.5 few-shot | pluralist | 0.536 (0.002) | 0.783 | 0.408 | 1,046 |
| gpt-5.5 few-shot | populist | 0.533 (0.007) | 0.888 | 0.381 | 1,456 |
| gpt-mini zero-shot | neutral | 0.557 (0.001) | 0.410 | 0.866 | 1,120 |
| gpt-mini zero-shot | pluralist | 0.390 (0.010) | 0.903 | 0.248 | 1,045 |
| gpt-mini zero-shot | populist | 0.638 (0.004) | 0.800 | 0.531 | 1,453 |
| gpt-mini few-shot | neutral | 0.557 (0.001) | 0.403 | 0.905 | 1,122 |
| gpt-mini few-shot | pluralist | 0.472 (0.004) | 0.808 | 0.333 | 1,046 |
| gpt-mini few-shot | populist | 0.558 (0.002) | 0.883 | 0.408 | 1,456 |
| llama zero-shot | neutral | 0.553 (0.001) | 0.471 | 0.670 | 1,122 |
| llama zero-shot | pluralist | 0.567 (0.001) | 0.686 | 0.483 | 1,046 |
| llama zero-shot | populist | 0.700 (0.002) | 0.745 | 0.660 | 1,456 |
| llama few-shot | neutral | 0.552 (0.003) | 0.463 | 0.682 | 1,122 |
| llama few-shot | pluralist | 0.525 (0.002) | 0.711 | 0.417 | 1,046 |
| llama few-shot | populist | 0.713 (0.001) | 0.738 | 0.690 | 1,456 |
| mistral zero-shot | neutral | 0.558 (0.000) | 0.399 | 0.927 | 1,122 |
| mistral zero-shot | pluralist | 0.505 (0.001) | 0.789 | 0.371 | 1,046 |
| mistral zero-shot | populist | 0.475 (0.002) | 0.892 | 0.324 | 1,456 |
| mistral few-shot | neutral | 0.544 (0.002) | 0.448 | 0.693 | 1,122 |
| mistral few-shot | pluralist | 0.518 (0.006) | 0.750 | 0.396 | 1,046 |
| mistral few-shot | populist | 0.691 (0.000) | 0.722 | 0.662 | 1,456 |

### Ballard  (2 classes)

| Config | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R | Acc | n_valid |
|---|---|---|---|---|---|---|
| gemma zero-shot | 0.602 (0.001) | 0.703 | 0.629 | 0.730 | 0.660 | 2,919 |
| gemma few-shot | 0.643 (0.001) | 0.762 | 0.636 | 0.716 | 0.733 | 2,919 |
| gpt-5.5 zero-shot | 0.609 (0.001) | 0.709 | 0.635 | 0.740 | 0.667 | 2,919 |
| gpt-5.5 few-shot | 0.651 (0.002) | 0.761 | 0.647 | 0.744 | 0.729 | 2,919 |
| gpt-mini zero-shot | 0.499 (0.003) | 0.574 | 0.602 | 0.674 | 0.525 | 2,919 |
| gpt-mini few-shot | 0.655 (0.004) | 0.793 | 0.642 | 0.682 | 0.780 | 2,919 |
| llama zero-shot | 0.572 (0.001) | 0.676 | 0.608 | 0.694 | 0.628 | 2,919 |
| llama few-shot | 0.640 (0.002) | 0.765 | 0.631 | 0.702 | 0.738 | 2,919 |
| mistral zero-shot | 0.612 (0.001) | 0.773 | 0.605 | 0.624 | 0.763 | 2,919 |
| mistral few-shot | 0.608 (0.001) | 0.755 | 0.600 | 0.641 | 0.733 | 2,919 |

_Per-class F1 (SD) / Precision / Recall:_

| Config | Class | F1 (SD) | P | R | support |
|---|---|---|---|---|---|
| gemma zero-shot | 0 | 0.754 (0.001) | 0.950 | 0.624 | 2,432 |
| gemma zero-shot | 1 | 0.450 (0.002) | 0.308 | 0.836 | 487 |
| gemma few-shot | 0 | 0.822 (0.001) | 0.923 | 0.741 | 2,432 |
| gemma few-shot | 1 | 0.464 (0.002) | 0.349 | 0.692 | 487 |
| gpt-5.5 zero-shot | 0 | 0.759 (0.001) | 0.954 | 0.630 | 2,432 |
| gpt-5.5 zero-shot | 1 | 0.459 (0.002) | 0.315 | 0.849 | 487 |
| gpt-5.5 few-shot | 0 | 0.816 (0.002) | 0.939 | 0.722 | 2,432 |
| gpt-5.5 few-shot | 1 | 0.486 (0.002) | 0.356 | 0.767 | 487 |
| gpt-mini zero-shot | 0 | 0.612 (0.002) | 0.957 | 0.450 | 2,432 |
| gpt-mini zero-shot | 1 | 0.387 (0.003) | 0.246 | 0.899 | 487 |
| gpt-mini few-shot | 0 | 0.863 (0.001) | 0.899 | 0.829 | 2,432 |
| gpt-mini few-shot | 1 | 0.448 (0.006) | 0.385 | 0.535 | 487 |
| llama zero-shot | 0 | 0.728 (0.001) | 0.934 | 0.596 | 2,432 |
| llama zero-shot | 1 | 0.415 (0.001) | 0.282 | 0.791 | 487 |
| llama few-shot | 0 | 0.828 (0.001) | 0.915 | 0.756 | 2,432 |
| llama few-shot | 1 | 0.452 (0.004) | 0.347 | 0.648 | 487 |
| mistral zero-shot | 0 | 0.854 (0.000) | 0.877 | 0.833 | 2,432 |
| mistral zero-shot | 1 | 0.369 (0.001) | 0.332 | 0.415 | 487 |
| mistral few-shot | 0 | 0.830 (0.001) | 0.887 | 0.779 | 2,432 |
| mistral few-shot | 1 | 0.385 (0.001) | 0.313 | 0.502 | 487 |

### Foy  (3 classes)

| Config | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R | Acc | n_valid |
|---|---|---|---|---|---|---|
| gemma zero-shot | 0.892 (0.001) | 0.913 | 0.896 | 0.900 | 0.911 | 910 |
| gemma few-shot | 0.930 (0.002) | 0.940 | 0.924 | 0.940 | 0.939 | 910 |
| gpt-5.5 zero-shot | 0.839 (0.003) | 0.868 | 0.821 | 0.871 | 0.864 | 910 |
| gpt-5.5 few-shot | 0.834 (0.001) | 0.860 | 0.812 | 0.877 | 0.855 | 910 |
| gpt-mini zero-shot | 0.887 (0.003) | 0.902 | 0.878 | 0.899 | 0.901 | 910 |
| gpt-mini few-shot | 0.834 (0.005) | 0.860 | 0.813 | 0.874 | 0.855 | 909 |
| llama zero-shot | 0.809 (0.001) | 0.834 | 0.788 | 0.847 | 0.829 | 910 |
| llama few-shot | 0.837 (0.001) | 0.859 | 0.816 | 0.880 | 0.853 | 910 |
| mistral zero-shot | 0.847 (0.001) | 0.853 | 0.851 | 0.862 | 0.846 | 910 |
| mistral few-shot | 0.869 (0.000) | 0.875 | 0.859 | 0.886 | 0.871 | 891 |

_Per-class F1 (SD) / Precision / Recall:_

| Config | Class | F1 (SD) | P | R | support |
|---|---|---|---|---|---|
| gemma zero-shot | Contrast | 0.849 (0.001) | 0.758 | 0.964 | 220 |
| gemma zero-shot | Negative | 0.952 (0.001) | 0.990 | 0.917 | 529 |
| gemma zero-shot | Positive | 0.875 (0.002) | 0.940 | 0.818 | 161 |
| gemma few-shot | Contrast | 0.892 (0.002) | 0.834 | 0.959 | 220 |
| gemma few-shot | Negative | 0.961 (0.002) | 0.989 | 0.934 | 529 |
| gemma few-shot | Positive | 0.937 (0.002) | 0.947 | 0.928 | 161 |
| gpt-5.5 zero-shot | Contrast | 0.849 (0.001) | 0.755 | 0.968 | 220 |
| gpt-5.5 zero-shot | Negative | 0.910 (0.001) | 0.995 | 0.839 | 529 |
| gpt-5.5 zero-shot | Positive | 0.758 (0.005) | 0.714 | 0.807 | 161 |
| gpt-5.5 few-shot | Contrast | 0.866 (0.001) | 0.783 | 0.968 | 220 |
| gpt-5.5 few-shot | Negative | 0.893 (0.001) | 0.998 | 0.808 | 529 |
| gpt-5.5 few-shot | Positive | 0.743 (0.003) | 0.657 | 0.855 | 161 |
| gpt-mini zero-shot | Contrast | 0.852 (0.007) | 0.826 | 0.879 | 220 |
| gpt-mini zero-shot | Negative | 0.929 (0.004) | 0.951 | 0.908 | 529 |
| gpt-mini zero-shot | Positive | 0.882 (0.009) | 0.856 | 0.909 | 161 |
| gpt-mini few-shot | Contrast | 0.868 (0.006) | 0.804 | 0.942 | 220 |
| gpt-mini few-shot | Negative | 0.894 (0.002) | 0.987 | 0.817 | 528 |
| gpt-mini few-shot | Positive | 0.739 (0.012) | 0.648 | 0.861 | 161 |
| llama zero-shot | Contrast | 0.818 (0.001) | 0.761 | 0.883 | 220 |
| llama zero-shot | Negative | 0.870 (0.000) | 0.958 | 0.796 | 529 |
| llama zero-shot | Positive | 0.738 (0.002) | 0.646 | 0.861 | 161 |
| llama few-shot | Contrast | 0.861 (0.001) | 0.820 | 0.906 | 220 |
| llama few-shot | Negative | 0.887 (0.001) | 0.979 | 0.810 | 529 |
| llama few-shot | Positive | 0.762 (0.003) | 0.648 | 0.923 | 161 |
| mistral zero-shot | Contrast | 0.741 (0.002) | 0.634 | 0.891 | 220 |
| mistral zero-shot | Negative | 0.880 (0.001) | 0.952 | 0.819 | 529 |
| mistral zero-shot | Positive | 0.919 (0.000) | 0.966 | 0.876 | 161 |
| mistral few-shot | Contrast | 0.772 (0.002) | 0.701 | 0.860 | 219 |
| mistral few-shot | Negative | 0.900 (0.002) | 0.953 | 0.853 | 510 |
| mistral few-shot | Positive | 0.934 (0.003) | 0.925 | 0.944 | 160 |

## International Relations

### Dietrich  (2 classes)

| Config | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R | Acc | n_valid |
|---|---|---|---|---|---|---|
| gemma zero-shot | 0.836 (0.000) | 0.938 | 0.808 | 0.872 | 0.935 | 52,744 |
| gemma few-shot | 0.836 (0.000) | 0.937 | 0.804 | 0.881 | 0.934 | 52,699 |
| gpt-5.5 zero-shot | 0.853 (–) | 0.947 | 0.854 | 0.853 | 0.947 | 52,744 |
| gpt-5.5 few-shot‡ _(n=37,469)_ | 0.854 (–) | 0.948 | 0.859 | 0.849 | 0.948 | 37,469 |
| gpt-mini zero-shot | 0.841 (–) | 0.945 | 0.868 | 0.819 | 0.947 | 52,744 |
| gpt-mini few-shot | 0.841 (–) | 0.945 | 0.880 | 0.811 | 0.948 | 52,744 |
| llama zero-shot | 0.823 (0.000) | 0.932 | 0.792 | 0.867 | 0.928 | 52,737 |
| llama few-shot | 0.838 (0.000) | 0.940 | 0.821 | 0.858 | 0.939 | 52,699 |
| mistral zero-shot | 0.814 (0.000) | 0.938 | 0.884 | 0.769 | 0.943 | 52,744 |
| mistral few-shot | 0.835 (0.000) | 0.942 | 0.858 | 0.815 | 0.944 | 52,699 |

_Per-class F1 (SD) / Precision / Recall:_

| Config | Class | F1 (SD) | P | R | support |
|---|---|---|---|---|---|
| gemma zero-shot | 0 | 0.963 (0.000) | 0.977 | 0.950 | 47,490 |
| gemma zero-shot | 1 | 0.708 (0.000) | 0.639 | 0.794 | 5,254 |
| gemma few-shot | 0 | 0.962 (0.000) | 0.979 | 0.947 | 47,445 |
| gemma few-shot | 1 | 0.710 (0.000) | 0.629 | 0.815 | 5,254 |
| gpt-5.5 zero-shot | 0 | 0.971 (–) | 0.971 | 0.971 | 47,490 |
| gpt-5.5 zero-shot | 1 | 0.736 (–) | 0.737 | 0.734 | 5,254 |
| gpt-5.5 few-shot‡ | 0 | 0.971 (–) | 0.970 | 0.973 | 33,744 |
| gpt-5.5 few-shot‡ | 1 | 0.736 (–) | 0.748 | 0.724 | 3,725 |
| gpt-mini zero-shot | 0 | 0.971 (–) | 0.963 | 0.979 | 47,490 |
| gpt-mini zero-shot | 1 | 0.711 (–) | 0.774 | 0.659 | 5,254 |
| gpt-mini few-shot | 0 | 0.971 (–) | 0.961 | 0.982 | 47,490 |
| gpt-mini few-shot | 1 | 0.710 (–) | 0.799 | 0.639 | 5,254 |
| llama zero-shot | 0 | 0.959 (0.000) | 0.976 | 0.943 | 47,486 |
| llama zero-shot | 1 | 0.687 (0.000) | 0.607 | 0.791 | 5,251 |
| llama few-shot | 0 | 0.966 (0.000) | 0.973 | 0.959 | 47,445 |
| llama few-shot | 1 | 0.711 (0.001) | 0.669 | 0.758 | 5,254 |
| mistral zero-shot | 0 | 0.969 (0.000) | 0.952 | 0.986 | 47,490 |
| mistral zero-shot | 1 | 0.659 (0.001) | 0.817 | 0.552 | 5,254 |
| mistral few-shot | 0 | 0.969 (0.000) | 0.962 | 0.976 | 47,445 |
| mistral few-shot | 1 | 0.700 (0.000) | 0.754 | 0.654 | 5,254 |

### Goes  (2 classes)

| Config | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R | Acc | n_valid |
|---|---|---|---|---|---|---|
| gemma zero-shot | 0.842 (0.002) | 0.852 | 0.836 | 0.854 | 0.850 | 700 |
| gemma few-shot | 0.835 (0.004) | 0.847 | 0.833 | 0.836 | 0.847 | 700 |
| gpt-5.5 zero-shot | 0.833 (0.002) | 0.842 | 0.829 | 0.854 | 0.839 | 700 |
| gpt-5.5 few-shot | 0.840 (0.005) | 0.852 | 0.840 | 0.840 | 0.852 | 700 |
| gpt-mini zero-shot | 0.806 (0.005) | 0.822 | 0.812 | 0.801 | 0.824 | 700 |
| gpt-mini few-shot | 0.768 (0.008) | 0.795 | 0.833 | 0.751 | 0.808 | 699 |
| llama zero-shot | 0.801 (0.002) | 0.814 | 0.796 | 0.811 | 0.811 | 700 |
| llama few-shot | 0.805 (0.003) | 0.824 | 0.827 | 0.793 | 0.828 | 700 |
| mistral zero-shot | 0.644 (0.000) | 0.695 | 0.821 | 0.645 | 0.740 | 700 |
| mistral few-shot | 0.758 (0.002) | 0.785 | 0.809 | 0.743 | 0.797 | 700 |

_Per-class F1 (SD) / Precision / Recall:_

| Config | Class | F1 (SD) | P | R | support |
|---|---|---|---|---|---|
| gemma zero-shot | 0 | 0.877 (0.002) | 0.919 | 0.839 | 447 |
| gemma zero-shot | 1 | 0.807 (0.003) | 0.753 | 0.870 | 253 |
| gemma few-shot | 0 | 0.879 (0.003) | 0.885 | 0.874 | 447 |
| gemma few-shot | 1 | 0.790 (0.006) | 0.782 | 0.798 | 253 |
| gpt-5.5 zero-shot | 0 | 0.864 (0.001) | 0.938 | 0.801 | 447 |
| gpt-5.5 zero-shot | 1 | 0.803 (0.002) | 0.720 | 0.906 | 253 |
| gpt-5.5 few-shot | 0 | 0.884 (0.003) | 0.884 | 0.885 | 447 |
| gpt-5.5 few-shot | 1 | 0.795 (0.007) | 0.797 | 0.794 | 253 |
| gpt-mini zero-shot | 0 | 0.865 (0.003) | 0.848 | 0.882 | 447 |
| gpt-mini zero-shot | 1 | 0.747 (0.007) | 0.776 | 0.721 | 253 |
| gpt-mini few-shot | 0 | 0.864 (0.004) | 0.787 | 0.957 | 446 |
| gpt-mini few-shot | 1 | 0.672 (0.012) | 0.879 | 0.544 | 253 |
| llama zero-shot | 0 | 0.846 (0.002) | 0.884 | 0.811 | 447 |
| llama zero-shot | 1 | 0.757 (0.002) | 0.709 | 0.812 | 253 |
| llama few-shot | 0 | 0.872 (0.002) | 0.830 | 0.919 | 447 |
| llama few-shot | 1 | 0.737 (0.004) | 0.823 | 0.668 | 253 |
| mistral zero-shot | 0 | 0.829 (0.000) | 0.715 | 0.987 | 447 |
| mistral zero-shot | 1 | 0.458 (0.000) | 0.928 | 0.304 | 253 |
| mistral few-shot | 0 | 0.855 (0.001) | 0.786 | 0.937 | 447 |
| mistral few-shot | 1 | 0.661 (0.003) | 0.832 | 0.548 | 253 |

### Kostovicova  (4 classes)

| Config | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R | Acc | n_valid |
|---|---|---|---|---|---|---|
| gemma zero-shot | 0.529 (0.003) | 0.589 | 0.552 | 0.543 | 0.610 | 1,211 |
| gemma few-shot | 0.536 (0.001) | 0.552 | 0.528 | 0.614 | 0.551 | 1,211 |
| gpt-5.5 zero-shot | 0.449 (0.010) | 0.460 | 0.525 | 0.496 | 0.486 | 1,211 |
| gpt-5.5 few-shot | 0.546 (0.004) | 0.545 | 0.567 | 0.578 | 0.544 | 1,211 |
| gpt-mini zero-shot | 0.437 (0.003) | 0.474 | 0.557 | 0.461 | 0.481 | 1,211 |
| gpt-mini few-shot | 0.519 (0.007) | 0.500 | 0.531 | 0.563 | 0.499 | 1,211 |
| llama zero-shot | 0.524 (0.003) | 0.594 | 0.592 | 0.505 | 0.603 | 1,211 |
| llama few-shot | 0.541 (0.003) | 0.578 | 0.537 | 0.563 | 0.577 | 1,211 |
| mistral zero-shot | 0.472 (0.001) | 0.542 | 0.613 | 0.457 | 0.573 | 1,211 |
| mistral few-shot | 0.431 (0.010) | 0.396 | 0.458 | 0.516 | 0.415 | 1,211 |

_Per-class F1 (SD) / Precision / Recall:_

| Config | Class | F1 (SD) | P | R | support |
|---|---|---|---|---|---|
| gemma zero-shot | 0 | 0.579 (0.009) | 0.486 | 0.715 | 89 |
| gemma zero-shot | 1 | 0.284 (0.004) | 0.377 | 0.228 | 240 |
| gemma zero-shot | 2 | 0.720 (0.001) | 0.659 | 0.794 | 658 |
| gemma zero-shot | 3 | 0.533 (0.000) | 0.685 | 0.436 | 224 |
| gemma few-shot | 0 | 0.557 (0.005) | 0.442 | 0.753 | 89 |
| gemma few-shot | 1 | 0.444 (0.003) | 0.515 | 0.390 | 240 |
| gemma few-shot | 2 | 0.589 (0.002) | 0.738 | 0.490 | 658 |
| gemma few-shot | 3 | 0.554 (0.004) | 0.418 | 0.821 | 224 |
| gpt-5.5 zero-shot | 0 | 0.590 (0.017) | 0.688 | 0.517 | 89 |
| gpt-5.5 zero-shot | 1 | 0.161 (0.021) | 0.462 | 0.097 | 240 |
| gpt-5.5 zero-shot | 2 | 0.535 (0.009) | 0.589 | 0.489 | 658 |
| gpt-5.5 zero-shot | 3 | 0.513 (0.001) | 0.361 | 0.882 | 224 |
| gpt-5.5 few-shot | 0 | 0.610 (0.012) | 0.684 | 0.551 | 89 |
| gpt-5.5 few-shot | 1 | 0.460 (0.012) | 0.491 | 0.432 | 240 |
| gpt-5.5 few-shot | 2 | 0.566 (0.008) | 0.688 | 0.480 | 658 |
| gpt-5.5 few-shot | 3 | 0.550 (0.003) | 0.407 | 0.851 | 224 |
| gpt-mini zero-shot | 0 | 0.376 (0.010) | 0.825 | 0.243 | 89 |
| gpt-mini zero-shot | 1 | 0.341 (0.016) | 0.426 | 0.285 | 240 |
| gpt-mini zero-shot | 2 | 0.525 (0.007) | 0.618 | 0.457 | 658 |
| gpt-mini zero-shot | 3 | 0.505 (0.008) | 0.358 | 0.859 | 224 |
| gpt-mini few-shot | 0 | 0.626 (0.010) | 0.661 | 0.596 | 89 |
| gpt-mini few-shot | 1 | 0.440 (0.010) | 0.414 | 0.469 | 240 |
| gpt-mini few-shot | 2 | 0.500 (0.010) | 0.673 | 0.398 | 658 |
| gpt-mini few-shot | 3 | 0.511 (0.009) | 0.377 | 0.790 | 224 |
| llama zero-shot | 0 | 0.424 (0.006) | 0.727 | 0.300 | 89 |
| llama zero-shot | 1 | 0.405 (0.002) | 0.445 | 0.371 | 240 |
| llama zero-shot | 2 | 0.695 (0.002) | 0.671 | 0.720 | 658 |
| llama zero-shot | 3 | 0.571 (0.003) | 0.524 | 0.628 | 224 |
| llama few-shot | 0 | 0.519 (0.008) | 0.534 | 0.506 | 89 |
| llama few-shot | 1 | 0.413 (0.011) | 0.431 | 0.397 | 240 |
| llama few-shot | 2 | 0.642 (0.006) | 0.703 | 0.591 | 658 |
| llama few-shot | 3 | 0.589 (0.011) | 0.481 | 0.757 | 224 |
| mistral zero-shot | 0 | 0.529 (0.000) | 0.766 | 0.404 | 89 |
| mistral zero-shot | 1 | 0.457 (0.001) | 0.399 | 0.535 | 240 |
| mistral zero-shot | 2 | 0.687 (0.000) | 0.627 | 0.761 | 658 |
| mistral zero-shot | 3 | 0.212 (0.003) | 0.659 | 0.126 | 224 |
| mistral few-shot | 0 | 0.541 (0.031) | 0.504 | 0.584 | 89 |
| mistral few-shot | 1 | 0.340 (0.011) | 0.367 | 0.317 | 240 |
| mistral few-shot | 2 | 0.371 (0.009) | 0.641 | 0.261 | 658 |
| mistral few-shot | 3 | 0.473 (0.006) | 0.320 | 0.903 | 224 |

### Trubowitz  (3 classes)

| Config | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R | Acc | n_valid |
|---|---|---|---|---|---|---|
| gemma zero-shot | 0.515 (0.004) | 0.660 | 0.597 | 0.508 | 0.694 | 1,700 |
| gemma few-shot | 0.549 (0.004) | 0.686 | 0.603 | 0.540 | 0.708 | 1,693 |
| gpt-5.5 zero-shot | 0.466 (0.006) | 0.654 | 0.568 | 0.454 | 0.696 | 1,700 |
| gpt-5.5 few-shot | 0.551 (0.002) | 0.691 | 0.577 | 0.583 | 0.681 | 1,700 |
| gpt-mini zero-shot | 0.490 (0.009) | 0.680 | 0.545 | 0.478 | 0.706 | 1,700 |
| gpt-mini few-shot | 0.482 (0.006) | 0.642 | 0.561 | 0.528 | 0.635 | 1,700 |
| llama zero-shot | 0.479 (0.002) | 0.665 | 0.582 | 0.466 | 0.709 | 1,700 |
| llama few-shot | 0.492 (0.001) | 0.650 | 0.574 | 0.551 | 0.625 | 1,700 |
| mistral zero-shot | 0.473 (0.001) | 0.650 | 0.585 | 0.504 | 0.636 | 1,700 |
| mistral few-shot | 0.513 (0.003) | 0.657 | 0.551 | 0.555 | 0.646 | 1,700 |

_Per-class F1 (SD) / Precision / Recall:_

| Config | Class | F1 (SD) | P | R | support |
|---|---|---|---|---|---|
| gemma zero-shot | No | 0.807 (0.001) | 0.715 | 0.925 | 1,067 |
| gemma zero-shot | Unclear | 0.299 (0.010) | 0.308 | 0.292 | 120 |
| gemma zero-shot | Yes | 0.440 (0.001) | 0.769 | 0.309 | 513 |
| gemma few-shot | No | 0.812 (0.003) | 0.735 | 0.906 | 1,063 |
| gemma few-shot | Unclear | 0.326 (0.011) | 0.324 | 0.328 | 120 |
| gemma few-shot | Yes | 0.510 (0.001) | 0.751 | 0.386 | 510 |
| gpt-5.5 zero-shot | No | 0.800 (0.000) | 0.700 | 0.933 | 1,067 |
| gpt-5.5 zero-shot | Unclear | 0.124 (0.020) | 0.267 | 0.081 | 120 |
| gpt-5.5 zero-shot | Yes | 0.473 (0.005) | 0.737 | 0.348 | 513 |
| gpt-5.5 few-shot | No | 0.796 (0.003) | 0.782 | 0.811 | 1,067 |
| gpt-5.5 few-shot | Unclear | 0.292 (0.009) | 0.210 | 0.481 | 120 |
| gpt-5.5 few-shot | Yes | 0.566 (0.002) | 0.739 | 0.458 | 513 |
| gpt-mini zero-shot | No | 0.813 (0.000) | 0.731 | 0.914 | 1,067 |
| gpt-mini zero-shot | Unclear | 0.124 (0.011) | 0.151 | 0.106 | 120 |
| gpt-mini zero-shot | Yes | 0.533 (0.015) | 0.751 | 0.413 | 513 |
| gpt-mini few-shot | No | 0.795 (0.002) | 0.772 | 0.818 | 1,067 |
| gpt-mini few-shot | Unclear | 0.231 (0.008) | 0.153 | 0.475 | 120 |
| gpt-mini few-shot | Yes | 0.419 (0.010) | 0.758 | 0.290 | 513 |
| llama zero-shot | No | 0.816 (0.000) | 0.713 | 0.954 | 1,067 |
| llama zero-shot | Unclear | 0.148 (0.005) | 0.264 | 0.103 | 120 |
| llama zero-shot | Yes | 0.472 (0.002) | 0.769 | 0.340 | 513 |
| llama few-shot | No | 0.792 (0.002) | 0.804 | 0.780 | 1,067 |
| llama few-shot | Unclear | 0.233 (0.001) | 0.147 | 0.556 | 120 |
| llama few-shot | Yes | 0.451 (0.003) | 0.771 | 0.319 | 513 |
| mistral zero-shot | No | 0.808 (0.001) | 0.786 | 0.831 | 1,067 |
| mistral zero-shot | Unclear | 0.183 (0.004) | 0.119 | 0.394 | 120 |
| mistral zero-shot | Yes | 0.430 (0.001) | 0.850 | 0.288 | 513 |
| mistral few-shot | No | 0.780 (0.001) | 0.770 | 0.792 | 1,067 |
| mistral few-shot | Unclear | 0.267 (0.003) | 0.183 | 0.494 | 120 |
| mistral few-shot | Yes | 0.492 (0.007) | 0.701 | 0.379 | 513 |

## Comparative Politics

### PopBERT  (2 classes)

| Config | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R | Acc | n_valid |
|---|---|---|---|---|---|---|
| gemma zero-shot | 0.703 (0.001) | 0.747 | 0.720 | 0.694 | 0.755 | 8,795 |
| gemma few-shot | 0.691 (0.001) | 0.739 | 0.716 | 0.680 | 0.750 | 8,795 |
| gpt-5.5 zero-shot | 0.709 (0.001) | 0.757 | 0.752 | 0.694 | 0.772 | 8,795 |
| gpt-5.5 few-shot | 0.684 (0.002) | 0.739 | 0.735 | 0.671 | 0.757 | 8,795 |
| gpt-mini zero-shot | 0.734 (0.001) | 0.758 | 0.729 | 0.757 | 0.750 | 8,792 |
| gpt-mini few-shot | 0.651 (0.000) | 0.714 | 0.713 | 0.641 | 0.739 | 8,795 |
| llama zero-shot | 0.716 (0.000) | 0.738 | 0.718 | 0.748 | 0.729 | 8,795 |
| llama few-shot | 0.717 (0.001) | 0.750 | 0.713 | 0.724 | 0.747 | 8,795 |
| mistral zero-shot | 0.625 (0.001) | 0.698 | 0.726 | 0.621 | 0.736 | 8,795 |
| mistral few-shot | 0.706 (0.001) | 0.741 | 0.703 | 0.711 | 0.739 | 8,795 |

_Per-class F1 (SD) / Precision / Recall:_

| Config | Class | F1 (SD) | P | R | support |
|---|---|---|---|---|---|
| gemma zero-shot | 0 | 0.827 (0.000) | 0.793 | 0.865 | 5,969 |
| gemma zero-shot | 1 | 0.578 (0.002) | 0.646 | 0.523 | 2,826 |
| gemma few-shot | 0 | 0.827 (0.000) | 0.782 | 0.877 | 5,969 |
| gemma few-shot | 1 | 0.554 (0.001) | 0.650 | 0.483 | 2,826 |
| gpt-5.5 zero-shot | 0 | 0.844 (0.001) | 0.787 | 0.910 | 5,969 |
| gpt-5.5 zero-shot | 1 | 0.574 (0.002) | 0.716 | 0.478 | 2,826 |
| gpt-5.5 few-shot | 0 | 0.836 (0.001) | 0.772 | 0.912 | 5,969 |
| gpt-5.5 few-shot | 1 | 0.532 (0.004) | 0.699 | 0.430 | 2,826 |
| gpt-mini zero-shot | 0 | 0.801 (0.001) | 0.874 | 0.738 | 5,967 |
| gpt-mini zero-shot | 1 | 0.666 (0.001) | 0.584 | 0.776 | 2,824 |
| gpt-mini few-shot | 0 | 0.827 (0.001) | 0.754 | 0.915 | 5,969 |
| gpt-mini few-shot | 1 | 0.475 (0.001) | 0.673 | 0.368 | 2,826 |
| llama zero-shot | 0 | 0.777 (0.001) | 0.881 | 0.694 | 5,969 |
| llama zero-shot | 1 | 0.655 (0.001) | 0.554 | 0.802 | 2,826 |
| llama few-shot | 0 | 0.809 (0.001) | 0.830 | 0.788 | 5,969 |
| llama few-shot | 1 | 0.626 (0.001) | 0.596 | 0.659 | 2,826 |
| mistral zero-shot | 0 | 0.829 (0.000) | 0.740 | 0.942 | 5,969 |
| mistral zero-shot | 1 | 0.422 (0.001) | 0.711 | 0.300 | 2,826 |
| mistral few-shot | 0 | 0.804 (0.001) | 0.820 | 0.788 | 5,969 |
| mistral few-shot | 1 | 0.609 (0.001) | 0.586 | 0.635 | 2,826 |

### ParlaCAP  (22 classes)

| Config | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R | Acc | n_valid |
|---|---|---|---|---|---|---|
| gemma zero-shot | 0.682 (0.001) | 0.666 | 0.710 | 0.682 | 0.665 | 3,443 |
| gemma few-shot | 0.693 (0.003) | 0.678 | 0.700 | 0.697 | 0.676 | 3,443 |
| gpt-5.5 zero-shot | 0.696 (0.000) | 0.683 | 0.710 | 0.701 | 0.683 | 3,443 |
| gpt-5.5 few-shot | 0.701 (0.004) | 0.690 | 0.712 | 0.709 | 0.690 | 3,443 |
| gpt-mini zero-shot | 0.630 (0.002) | 0.618 | 0.650 | 0.650 | 0.625 | 3,438 |
| gpt-mini few-shot | 0.640 (0.002) | 0.627 | 0.666 | 0.641 | 0.625 | 3,443 |
| llama zero-shot | 0.594 (0.001) | 0.579 | 0.653 | 0.595 | 0.574 | 3,440 |
| llama few-shot | 0.632 (0.001) | 0.619 | 0.660 | 0.638 | 0.614 | 3,443 |
| mistral zero-shot | 0.552 (0.000) | 0.528 | 0.632 | 0.543 | 0.518 | 3,433 |
| mistral few-shot | 0.610 (0.004) | 0.591 | 0.652 | 0.609 | 0.583 | 3,443 |

_Per-class F1 (SD) / Precision / Recall:_

| Config | Class | F1 (SD) | P | R | support |
|---|---|---|---|---|---|
| gemma zero-shot | Agriculture | 0.813 (0.004) | 0.842 | 0.786 | 156 |
| gemma zero-shot | Civil Rights | 0.472 (0.001) | 0.784 | 0.338 | 143 |
| gemma zero-shot | Culture | 0.652 (0.007) | 0.583 | 0.741 | 76 |
| gemma zero-shot | Defense | 0.692 (0.011) | 0.846 | 0.585 | 179 |
| gemma zero-shot | Domestic Commerce | 0.632 (0.005) | 0.699 | 0.577 | 190 |
| gemma zero-shot | Education | 0.804 (0.004) | 0.845 | 0.766 | 147 |
| gemma zero-shot | Energy | 0.842 (0.002) | 0.831 | 0.854 | 155 |
| gemma zero-shot | Environment | 0.799 (0.006) | 0.751 | 0.854 | 112 |
| gemma zero-shot | Foreign Trade | 0.671 (0.004) | 0.638 | 0.706 | 110 |
| gemma zero-shot | Government Operations | 0.473 (0.005) | 0.422 | 0.539 | 261 |
| gemma zero-shot | Health | 0.871 (0.003) | 0.875 | 0.867 | 140 |
| gemma zero-shot | Housing | 0.720 (0.003) | 0.718 | 0.723 | 143 |
| gemma zero-shot | Immigration | 0.705 (0.006) | 0.599 | 0.856 | 74 |
| gemma zero-shot | International Affairs | 0.538 (0.006) | 0.574 | 0.505 | 182 |
| gemma zero-shot | Labor | 0.703 (0.002) | 0.667 | 0.743 | 145 |
| gemma zero-shot | Law and Crime | 0.592 (0.011) | 0.739 | 0.494 | 197 |
| gemma zero-shot | Macroeconomics | 0.543 (0.009) | 0.671 | 0.456 | 209 |
| gemma zero-shot | Other | 0.573 (0.002) | 0.437 | 0.830 | 255 |
| gemma zero-shot | Public Lands | 0.711 (0.005) | 0.902 | 0.586 | 141 |
| gemma zero-shot | Social Welfare | 0.606 (0.008) | 0.592 | 0.621 | 123 |
| gemma zero-shot | Technology | 0.756 (0.008) | 0.836 | 0.690 | 173 |
| gemma zero-shot | Transportation | 0.830 (0.008) | 0.775 | 0.894 | 132 |
| gemma few-shot | Agriculture | 0.836 (0.002) | 0.855 | 0.818 | 156 |
| gemma few-shot | Civil Rights | 0.591 (0.004) | 0.699 | 0.513 | 143 |
| gemma few-shot | Culture | 0.664 (0.004) | 0.580 | 0.776 | 76 |
| gemma few-shot | Defense | 0.733 (0.010) | 0.822 | 0.661 | 179 |
| gemma few-shot | Domestic Commerce | 0.641 (0.005) | 0.665 | 0.619 | 190 |
| gemma few-shot | Education | 0.810 (0.005) | 0.838 | 0.785 | 147 |
| gemma few-shot | Energy | 0.840 (0.005) | 0.857 | 0.824 | 155 |
| gemma few-shot | Environment | 0.770 (0.009) | 0.729 | 0.815 | 112 |
| gemma few-shot | Foreign Trade | 0.649 (0.006) | 0.649 | 0.648 | 110 |
| gemma few-shot | Government Operations | 0.460 (0.010) | 0.410 | 0.525 | 261 |
| gemma few-shot | Health | 0.863 (0.001) | 0.877 | 0.850 | 140 |
| gemma few-shot | Housing | 0.720 (0.010) | 0.773 | 0.674 | 143 |
| gemma few-shot | Immigration | 0.652 (0.008) | 0.517 | 0.883 | 74 |
| gemma few-shot | International Affairs | 0.533 (0.012) | 0.634 | 0.460 | 182 |
| gemma few-shot | Labor | 0.745 (0.005) | 0.720 | 0.772 | 145 |
| gemma few-shot | Law and Crime | 0.645 (0.007) | 0.700 | 0.599 | 197 |
| gemma few-shot | Macroeconomics | 0.563 (0.007) | 0.585 | 0.542 | 209 |
| gemma few-shot | Other | 0.563 (0.002) | 0.516 | 0.620 | 255 |
| gemma few-shot | Public Lands | 0.707 (0.012) | 0.796 | 0.636 | 141 |
| gemma few-shot | Social Welfare | 0.601 (0.005) | 0.559 | 0.650 | 123 |
| gemma few-shot | Technology | 0.821 (0.002) | 0.835 | 0.807 | 173 |
| gemma few-shot | Transportation | 0.829 (0.002) | 0.794 | 0.866 | 132 |
| gpt-5.5 zero-shot | Agriculture | 0.830 (0.007) | 0.835 | 0.825 | 156 |
| gpt-5.5 zero-shot | Civil Rights | 0.547 (0.004) | 0.641 | 0.478 | 143 |
| gpt-5.5 zero-shot | Culture | 0.665 (0.015) | 0.609 | 0.732 | 76 |
| gpt-5.5 zero-shot | Defense | 0.731 (0.007) | 0.796 | 0.676 | 179 |
| gpt-5.5 zero-shot | Domestic Commerce | 0.670 (0.005) | 0.671 | 0.668 | 190 |
| gpt-5.5 zero-shot | Education | 0.808 (0.011) | 0.863 | 0.760 | 147 |
| gpt-5.5 zero-shot | Energy | 0.846 (0.005) | 0.830 | 0.862 | 155 |
| gpt-5.5 zero-shot | Environment | 0.799 (0.004) | 0.767 | 0.833 | 112 |
| gpt-5.5 zero-shot | Foreign Trade | 0.693 (0.009) | 0.682 | 0.706 | 110 |
| gpt-5.5 zero-shot | Government Operations | 0.517 (0.010) | 0.505 | 0.529 | 261 |
| gpt-5.5 zero-shot | Health | 0.840 (0.009) | 0.797 | 0.888 | 140 |
| gpt-5.5 zero-shot | Housing | 0.697 (0.006) | 0.739 | 0.660 | 143 |
| gpt-5.5 zero-shot | Immigration | 0.616 (0.008) | 0.481 | 0.856 | 74 |
| gpt-5.5 zero-shot | International Affairs | 0.603 (0.007) | 0.711 | 0.524 | 182 |
| gpt-5.5 zero-shot | Labor | 0.705 (0.014) | 0.691 | 0.720 | 145 |
| gpt-5.5 zero-shot | Law and Crime | 0.624 (0.008) | 0.736 | 0.541 | 197 |
| gpt-5.5 zero-shot | Macroeconomics | 0.527 (0.011) | 0.701 | 0.423 | 209 |
| gpt-5.5 zero-shot | Other | 0.577 (0.003) | 0.458 | 0.780 | 255 |
| gpt-5.5 zero-shot | Public Lands | 0.723 (0.006) | 0.860 | 0.624 | 141 |
| gpt-5.5 zero-shot | Social Welfare | 0.653 (0.016) | 0.630 | 0.678 | 123 |
| gpt-5.5 zero-shot | Technology | 0.785 (0.009) | 0.821 | 0.751 | 173 |
| gpt-5.5 zero-shot | Transportation | 0.848 (0.005) | 0.793 | 0.912 | 132 |
| gpt-5.5 few-shot | Agriculture | 0.835 (0.006) | 0.853 | 0.818 | 156 |
| gpt-5.5 few-shot | Civil Rights | 0.572 (0.008) | 0.666 | 0.501 | 143 |
| gpt-5.5 few-shot | Culture | 0.634 (0.019) | 0.561 | 0.728 | 76 |
| gpt-5.5 few-shot | Defense | 0.732 (0.005) | 0.788 | 0.683 | 179 |
| gpt-5.5 few-shot | Domestic Commerce | 0.654 (0.005) | 0.647 | 0.661 | 190 |
| gpt-5.5 few-shot | Education | 0.814 (0.010) | 0.875 | 0.762 | 147 |
| gpt-5.5 few-shot | Energy | 0.857 (0.003) | 0.831 | 0.886 | 155 |
| gpt-5.5 few-shot | Environment | 0.798 (0.010) | 0.759 | 0.842 | 112 |
| gpt-5.5 few-shot | Foreign Trade | 0.703 (0.008) | 0.659 | 0.755 | 110 |
| gpt-5.5 few-shot | Government Operations | 0.528 (0.001) | 0.490 | 0.572 | 261 |
| gpt-5.5 few-shot | Health | 0.854 (0.004) | 0.826 | 0.883 | 140 |
| gpt-5.5 few-shot | Housing | 0.708 (0.004) | 0.770 | 0.655 | 143 |
| gpt-5.5 few-shot | Immigration | 0.619 (0.007) | 0.480 | 0.869 | 74 |
| gpt-5.5 few-shot | International Affairs | 0.608 (0.017) | 0.704 | 0.535 | 182 |
| gpt-5.5 few-shot | Labor | 0.707 (0.010) | 0.712 | 0.703 | 145 |
| gpt-5.5 few-shot | Law and Crime | 0.637 (0.012) | 0.710 | 0.577 | 197 |
| gpt-5.5 few-shot | Macroeconomics | 0.527 (0.008) | 0.719 | 0.416 | 209 |
| gpt-5.5 few-shot | Other | 0.588 (0.012) | 0.501 | 0.711 | 255 |
| gpt-5.5 few-shot | Public Lands | 0.731 (0.008) | 0.852 | 0.641 | 141 |
| gpt-5.5 few-shot | Social Welfare | 0.657 (0.003) | 0.629 | 0.688 | 123 |
| gpt-5.5 few-shot | Technology | 0.812 (0.001) | 0.831 | 0.794 | 173 |
| gpt-5.5 few-shot | Transportation | 0.856 (0.000) | 0.797 | 0.924 | 132 |
| gpt-mini zero-shot | Agriculture | 0.804 (0.009) | 0.798 | 0.810 | 156 |
| gpt-mini zero-shot | Civil Rights | 0.543 (0.011) | 0.572 | 0.517 | 143 |
| gpt-mini zero-shot | Culture | 0.538 (0.010) | 0.410 | 0.781 | 76 |
| gpt-mini zero-shot | Defense | 0.714 (0.013) | 0.850 | 0.615 | 177 |
| gpt-mini zero-shot | Domestic Commerce | 0.481 (0.029) | 0.488 | 0.475 | 189 |
| gpt-mini zero-shot | Education | 0.826 (0.008) | 0.807 | 0.846 | 147 |
| gpt-mini zero-shot | Energy | 0.809 (0.006) | 0.858 | 0.766 | 155 |
| gpt-mini zero-shot | Environment | 0.671 (0.003) | 0.571 | 0.812 | 112 |
| gpt-mini zero-shot | Foreign Trade | 0.599 (0.003) | 0.524 | 0.700 | 110 |
| gpt-mini zero-shot | Government Operations | 0.440 (0.000) | 0.435 | 0.445 | 260 |
| gpt-mini zero-shot | Health | 0.839 (0.016) | 0.773 | 0.917 | 140 |
| gpt-mini zero-shot | Housing | 0.713 (0.003) | 0.700 | 0.727 | 143 |
| gpt-mini zero-shot | Immigration | 0.644 (0.019) | 0.582 | 0.721 | 74 |
| gpt-mini zero-shot | International Affairs | 0.537 (0.020) | 0.682 | 0.442 | 181 |
| gpt-mini zero-shot | Labor | 0.662 (0.010) | 0.599 | 0.740 | 144 |
| gpt-mini zero-shot | Law and Crime | 0.599 (0.001) | 0.627 | 0.573 | 196 |
| gpt-mini zero-shot | Macroeconomics | 0.454 (0.005) | 0.605 | 0.363 | 208 |
| gpt-mini zero-shot | Other | 0.526 (0.009) | 0.462 | 0.610 | 254 |
| gpt-mini zero-shot | Public Lands | 0.269 (0.023) | 0.828 | 0.161 | 141 |
| gpt-mini zero-shot | Social Welfare | 0.583 (0.013) | 0.534 | 0.642 | 123 |
| gpt-mini zero-shot | Technology | 0.784 (0.024) | 0.844 | 0.732 | 172 |
| gpt-mini zero-shot | Transportation | 0.817 (0.004) | 0.748 | 0.899 | 132 |
| gpt-mini few-shot | Agriculture | 0.771 (0.009) | 0.847 | 0.707 | 156 |
| gpt-mini few-shot | Civil Rights | 0.566 (0.008) | 0.660 | 0.497 | 143 |
| gpt-mini few-shot | Culture | 0.557 (0.029) | 0.454 | 0.719 | 76 |
| gpt-mini few-shot | Defense | 0.673 (0.007) | 0.857 | 0.555 | 179 |
| gpt-mini few-shot | Domestic Commerce | 0.550 (0.008) | 0.500 | 0.612 | 190 |
| gpt-mini few-shot | Education | 0.785 (0.013) | 0.850 | 0.730 | 147 |
| gpt-mini few-shot | Energy | 0.811 (0.003) | 0.883 | 0.751 | 155 |
| gpt-mini few-shot | Environment | 0.716 (0.006) | 0.670 | 0.768 | 112 |
| gpt-mini few-shot | Foreign Trade | 0.631 (0.011) | 0.594 | 0.673 | 110 |
| gpt-mini few-shot | Government Operations | 0.470 (0.013) | 0.409 | 0.553 | 261 |
| gpt-mini few-shot | Health | 0.827 (0.003) | 0.801 | 0.855 | 140 |
| gpt-mini few-shot | Housing | 0.689 (0.010) | 0.825 | 0.592 | 143 |
| gpt-mini few-shot | Immigration | 0.648 (0.011) | 0.568 | 0.757 | 74 |
| gpt-mini few-shot | International Affairs | 0.501 (0.007) | 0.629 | 0.416 | 182 |
| gpt-mini few-shot | Labor | 0.669 (0.003) | 0.595 | 0.763 | 145 |
| gpt-mini few-shot | Law and Crime | 0.569 (0.009) | 0.691 | 0.484 | 197 |
| gpt-mini few-shot | Macroeconomics | 0.499 (0.014) | 0.572 | 0.443 | 209 |
| gpt-mini few-shot | Other | 0.525 (0.004) | 0.429 | 0.677 | 255 |
| gpt-mini few-shot | Public Lands | 0.462 (0.009) | 0.664 | 0.355 | 141 |
| gpt-mini few-shot | Social Welfare | 0.598 (0.006) | 0.553 | 0.650 | 123 |
| gpt-mini few-shot | Technology | 0.778 (0.021) | 0.825 | 0.736 | 173 |
| gpt-mini few-shot | Transportation | 0.788 (0.005) | 0.771 | 0.806 | 132 |
| llama zero-shot | Agriculture | 0.743 (0.002) | 0.828 | 0.673 | 155 |
| llama zero-shot | Civil Rights | 0.571 (0.002) | 0.716 | 0.476 | 143 |
| llama zero-shot | Culture | 0.463 (0.005) | 0.333 | 0.759 | 76 |
| llama zero-shot | Defense | 0.628 (0.000) | 0.888 | 0.486 | 179 |
| llama zero-shot | Domestic Commerce | 0.489 (0.001) | 0.568 | 0.429 | 188 |
| llama zero-shot | Education | 0.792 (0.002) | 0.799 | 0.785 | 147 |
| llama zero-shot | Energy | 0.815 (0.000) | 0.869 | 0.768 | 155 |
| llama zero-shot | Environment | 0.671 (0.002) | 0.547 | 0.866 | 112 |
| llama zero-shot | Foreign Trade | 0.555 (0.004) | 0.706 | 0.458 | 110 |
| llama zero-shot | Government Operations | 0.375 (0.001) | 0.277 | 0.584 | 261 |
| llama zero-shot | Health | 0.846 (0.000) | 0.797 | 0.900 | 140 |
| llama zero-shot | Housing | 0.629 (0.003) | 0.919 | 0.478 | 143 |
| llama zero-shot | Immigration | 0.622 (0.002) | 0.557 | 0.703 | 74 |
| llama zero-shot | International Affairs | 0.508 (0.001) | 0.511 | 0.505 | 182 |
| llama zero-shot | Labor | 0.635 (0.001) | 0.569 | 0.717 | 145 |
| llama zero-shot | Law and Crime | 0.538 (0.002) | 0.486 | 0.604 | 197 |
| llama zero-shot | Macroeconomics | 0.512 (0.006) | 0.538 | 0.488 | 209 |
| llama zero-shot | Other | 0.421 (0.003) | 0.449 | 0.396 | 255 |
| llama zero-shot | Public Lands | 0.354 (0.007) | 0.800 | 0.227 | 141 |
| llama zero-shot | Social Welfare | 0.569 (0.001) | 0.578 | 0.561 | 123 |
| llama zero-shot | Technology | 0.519 (0.003) | 0.831 | 0.378 | 173 |
| llama zero-shot | Transportation | 0.824 (0.002) | 0.803 | 0.846 | 132 |
| llama few-shot | Agriculture | 0.768 (0.002) | 0.809 | 0.731 | 156 |
| llama few-shot | Civil Rights | 0.512 (0.006) | 0.732 | 0.394 | 143 |
| llama few-shot | Culture | 0.507 (0.005) | 0.374 | 0.785 | 76 |
| llama few-shot | Defense | 0.661 (0.004) | 0.837 | 0.546 | 179 |
| llama few-shot | Domestic Commerce | 0.522 (0.010) | 0.571 | 0.481 | 190 |
| llama few-shot | Education | 0.784 (0.009) | 0.777 | 0.791 | 147 |
| llama few-shot | Energy | 0.819 (0.007) | 0.825 | 0.813 | 155 |
| llama few-shot | Environment | 0.740 (0.006) | 0.658 | 0.845 | 112 |
| llama few-shot | Foreign Trade | 0.678 (0.007) | 0.683 | 0.673 | 110 |
| llama few-shot | Government Operations | 0.406 (0.006) | 0.321 | 0.554 | 261 |
| llama few-shot | Health | 0.835 (0.004) | 0.827 | 0.843 | 140 |
| llama few-shot | Housing | 0.660 (0.007) | 0.858 | 0.536 | 143 |
| llama few-shot | Immigration | 0.623 (0.004) | 0.504 | 0.815 | 74 |
| llama few-shot | International Affairs | 0.527 (0.004) | 0.579 | 0.484 | 182 |
| llama few-shot | Labor | 0.618 (0.003) | 0.565 | 0.683 | 145 |
| llama few-shot | Law and Crime | 0.574 (0.004) | 0.573 | 0.575 | 197 |
| llama few-shot | Macroeconomics | 0.539 (0.005) | 0.687 | 0.443 | 209 |
| llama few-shot | Other | 0.518 (0.016) | 0.502 | 0.536 | 255 |
| llama few-shot | Public Lands | 0.465 (0.004) | 0.665 | 0.357 | 141 |
| llama few-shot | Social Welfare | 0.583 (0.008) | 0.536 | 0.640 | 123 |
| llama few-shot | Technology | 0.760 (0.011) | 0.859 | 0.682 | 173 |
| llama few-shot | Transportation | 0.798 (0.006) | 0.776 | 0.821 | 132 |
| mistral zero-shot | Agriculture | 0.731 (0.001) | 0.813 | 0.665 | 155 |
| mistral zero-shot | Civil Rights | 0.510 (0.003) | 0.432 | 0.622 | 143 |
| mistral zero-shot | Culture | 0.473 (0.004) | 0.372 | 0.649 | 76 |
| mistral zero-shot | Defense | 0.614 (0.002) | 0.878 | 0.473 | 177 |
| mistral zero-shot | Domestic Commerce | 0.391 (0.002) | 0.362 | 0.425 | 189 |
| mistral zero-shot | Education | 0.765 (0.003) | 0.842 | 0.701 | 147 |
| mistral zero-shot | Energy | 0.706 (0.002) | 0.900 | 0.581 | 155 |
| mistral zero-shot | Environment | 0.647 (0.002) | 0.550 | 0.786 | 112 |
| mistral zero-shot | Foreign Trade | 0.554 (0.003) | 0.526 | 0.585 | 110 |
| mistral zero-shot | Government Operations | 0.303 (0.001) | 0.203 | 0.604 | 261 |
| mistral zero-shot | Health | 0.820 (0.002) | 0.758 | 0.893 | 140 |
| mistral zero-shot | Housing | 0.530 (0.003) | 0.914 | 0.373 | 143 |
| mistral zero-shot | Immigration | 0.609 (0.003) | 0.619 | 0.599 | 74 |
| mistral zero-shot | International Affairs | 0.476 (0.004) | 0.479 | 0.473 | 182 |
| mistral zero-shot | Labor | 0.592 (0.004) | 0.648 | 0.545 | 145 |
| mistral zero-shot | Law and Crime | 0.532 (0.001) | 0.512 | 0.553 | 197 |
| mistral zero-shot | Macroeconomics | 0.409 (0.003) | 0.528 | 0.334 | 208 |
| mistral zero-shot | Other | 0.269 (0.004) | 0.575 | 0.175 | 255 |
| mistral zero-shot | Public Lands | 0.383 (0.000) | 0.706 | 0.263 | 137 |
| mistral zero-shot | Social Welfare | 0.640 (0.000) | 0.625 | 0.656 | 122 |
| mistral zero-shot | Technology | 0.437 (0.003) | 0.812 | 0.299 | 173 |
| mistral zero-shot | Transportation | 0.758 (0.002) | 0.850 | 0.684 | 132 |
| mistral few-shot | Agriculture | 0.769 (0.014) | 0.854 | 0.699 | 156 |
| mistral few-shot | Civil Rights | 0.548 (0.006) | 0.452 | 0.697 | 143 |
| mistral few-shot | Culture | 0.528 (0.012) | 0.420 | 0.711 | 76 |
| mistral few-shot | Defense | 0.657 (0.007) | 0.884 | 0.523 | 179 |
| mistral few-shot | Domestic Commerce | 0.502 (0.004) | 0.569 | 0.449 | 190 |
| mistral few-shot | Education | 0.758 (0.007) | 0.848 | 0.685 | 147 |
| mistral few-shot | Energy | 0.786 (0.002) | 0.874 | 0.714 | 155 |
| mistral few-shot | Environment | 0.655 (0.000) | 0.532 | 0.854 | 112 |
| mistral few-shot | Foreign Trade | 0.645 (0.013) | 0.652 | 0.639 | 110 |
| mistral few-shot | Government Operations | 0.342 (0.009) | 0.245 | 0.563 | 261 |
| mistral few-shot | Health | 0.853 (0.005) | 0.817 | 0.893 | 140 |
| mistral few-shot | Housing | 0.630 (0.010) | 0.882 | 0.490 | 143 |
| mistral few-shot | Immigration | 0.626 (0.029) | 0.576 | 0.685 | 74 |
| mistral few-shot | International Affairs | 0.498 (0.008) | 0.626 | 0.414 | 182 |
| mistral few-shot | Labor | 0.664 (0.004) | 0.625 | 0.708 | 145 |
| mistral few-shot | Law and Crime | 0.585 (0.013) | 0.627 | 0.548 | 197 |
| mistral few-shot | Macroeconomics | 0.529 (0.005) | 0.523 | 0.536 | 209 |
| mistral few-shot | Other | 0.343 (0.015) | 0.514 | 0.258 | 255 |
| mistral few-shot | Public Lands | 0.383 (0.020) | 0.591 | 0.284 | 141 |
| mistral few-shot | Social Welfare | 0.588 (0.009) | 0.581 | 0.596 | 123 |
| mistral few-shot | Technology | 0.762 (0.008) | 0.860 | 0.684 | 173 |
| mistral few-shot | Transportation | 0.778 (0.015) | 0.796 | 0.760 | 132 |

### Heseltine  (2 classes)

| Config | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R | Acc | n_valid |
|---|---|---|---|---|---|---|
| gemma zero-shot | 0.832 (0.002) | 0.854 | 0.819 | 0.879 | 0.848 | 2,195 |
| gemma few-shot | 0.810 (0.001) | 0.832 | 0.805 | 0.869 | 0.824 | 2,195 |
| gpt-5.5 zero-shot | 0.813 (0.001) | 0.834 | 0.806 | 0.871 | 0.826 | 2,195 |
| gpt-5.5 few-shot | 0.815 (0.003) | 0.837 | 0.808 | 0.874 | 0.829 | 2,195 |
| gpt-mini zero-shot | 0.787 (0.005) | 0.810 | 0.788 | 0.851 | 0.800 | 2,194 |
| gpt-mini few-shot | 0.854 (0.002) | 0.877 | 0.839 | 0.877 | 0.873 | 2,193 |
| llama zero-shot | 0.851 (0.001) | 0.878 | 0.849 | 0.854 | 0.878 | 2,195 |
| llama few-shot | 0.837 (0.001) | 0.862 | 0.823 | 0.860 | 0.859 | 2,195 |
| mistral zero-shot | 0.863 (0.000) | 0.889 | 0.868 | 0.858 | 0.890 | 2,195 |
| mistral few-shot | 0.820 (0.002) | 0.844 | 0.808 | 0.866 | 0.837 | 2,195 |

_Per-class F1 (SD) / Precision / Recall:_

| Config | Class | F1 (SD) | P | R | support |
|---|---|---|---|---|---|
| gemma zero-shot | 0 | 0.883 (0.001) | 0.977 | 0.806 | 1,569 |
| gemma zero-shot | 1 | 0.781 (0.002) | 0.662 | 0.952 | 626 |
| gemma few-shot | 0 | 0.861 (0.001) | 0.987 | 0.764 | 1,569 |
| gemma few-shot | 1 | 0.760 (0.002) | 0.622 | 0.975 | 626 |
| gpt-5.5 zero-shot | 0 | 0.863 (0.001) | 0.987 | 0.767 | 1,569 |
| gpt-5.5 zero-shot | 1 | 0.762 (0.001) | 0.625 | 0.976 | 626 |
| gpt-5.5 few-shot | 0 | 0.865 (0.002) | 0.989 | 0.769 | 1,569 |
| gpt-5.5 few-shot | 1 | 0.765 (0.003) | 0.628 | 0.978 | 626 |
| gpt-mini zero-shot | 0 | 0.840 (0.004) | 0.984 | 0.732 | 1,568 |
| gpt-mini zero-shot | 1 | 0.735 (0.005) | 0.591 | 0.971 | 625 |
| gpt-mini few-shot | 0 | 0.907 (0.002) | 0.951 | 0.868 | 1,569 |
| gpt-mini few-shot | 1 | 0.800 (0.002) | 0.728 | 0.887 | 624 |
| llama zero-shot | 0 | 0.914 (0.000) | 0.918 | 0.909 | 1,569 |
| llama zero-shot | 1 | 0.788 (0.001) | 0.779 | 0.798 | 626 |
| llama few-shot | 0 | 0.897 (0.001) | 0.940 | 0.857 | 1,569 |
| llama few-shot | 1 | 0.777 (0.002) | 0.707 | 0.863 | 626 |
| mistral zero-shot | 0 | 0.923 (0.000) | 0.915 | 0.932 | 1,569 |
| mistral zero-shot | 1 | 0.802 (0.000) | 0.821 | 0.784 | 626 |
| mistral few-shot | 0 | 0.875 (0.002) | 0.968 | 0.798 | 1,569 |
| mistral few-shot | 1 | 0.765 (0.002) | 0.649 | 0.933 | 626 |

### Proksch  (5 classes)

_Reported on the 5-class scale (matches the encoder & original coders). Decoders were run on the 9-level scale; predictions collapsed 9→5 via `ceil((x+1)/2)`._

| Config | Macro-F1 (SD) | Weighted-F1 | Macro-P | Macro-R | Acc | n_valid |
|---|---|---|---|---|---|---|
| gemma zero-shot | 0.597 (0.010) | 0.586 | 0.634 | 0.602 | 0.595 | 301 |
| gemma few-shot | 0.622 (0.008) | 0.617 | 0.657 | 0.612 | 0.620 | 301 |
| gpt-5.5 zero-shot | 0.568 (0.005) | 0.558 | 0.621 | 0.573 | 0.573 | 301 |
| gpt-5.5 few-shot | 0.632 (0.015) | 0.617 | 0.649 | 0.633 | 0.622 | 301 |
| gpt-mini zero-shot | 0.525 (0.011) | 0.523 | 0.578 | 0.525 | 0.529 | 301 |
| gpt-mini few-shot | 0.440 (0.019) | 0.459 | 0.588 | 0.448 | 0.488 | 301 |
| llama zero-shot | 0.509 (0.002) | 0.492 | 0.527 | 0.532 | 0.505 | 301 |
| llama few-shot | 0.426 (0.020) | 0.430 | 0.601 | 0.425 | 0.453 | 301 |
| mistral zero-shot | 0.339 (0.006) | 0.376 | 0.522 | 0.374 | 0.427 | 301 |
| mistral few-shot | 0.350 (0.004) | 0.387 | 0.640 | 0.372 | 0.426 | 301 |

_Per-class F1 (SD) / Precision / Recall:_

| Config | Class | F1 (SD) | P | R | support |
|---|---|---|---|---|---|
| gemma zero-shot | 1 | 0.676 (0.015) | 0.926 | 0.532 | 47 |
| gemma zero-shot | 2 | 0.640 (0.009) | 0.553 | 0.759 | 76 |
| gemma zero-shot | 3 | 0.416 (0.018) | 0.540 | 0.338 | 72 |
| gemma zero-shot | 4 | 0.618 (0.015) | 0.587 | 0.652 | 69 |
| gemma zero-shot | 5 | 0.635 (0.013) | 0.562 | 0.730 | 37 |
| gemma few-shot | 1 | 0.729 (0.004) | 0.849 | 0.638 | 47 |
| gemma few-shot | 2 | 0.643 (0.002) | 0.607 | 0.684 | 76 |
| gemma few-shot | 3 | 0.498 (0.019) | 0.568 | 0.444 | 72 |
| gemma few-shot | 4 | 0.648 (0.005) | 0.555 | 0.778 | 69 |
| gemma few-shot | 5 | 0.593 (0.025) | 0.704 | 0.514 | 37 |
| gpt-5.5 zero-shot | 1 | 0.571 (0.033) | 0.869 | 0.426 | 47 |
| gpt-5.5 zero-shot | 2 | 0.619 (0.019) | 0.575 | 0.671 | 76 |
| gpt-5.5 zero-shot | 3 | 0.380 (0.017) | 0.529 | 0.296 | 72 |
| gpt-5.5 zero-shot | 4 | 0.617 (0.011) | 0.503 | 0.797 | 69 |
| gpt-5.5 zero-shot | 5 | 0.652 (0.032) | 0.630 | 0.676 | 37 |
| gpt-5.5 few-shot | 1 | 0.732 (0.016) | 0.823 | 0.660 | 47 |
| gpt-5.5 few-shot | 2 | 0.626 (0.016) | 0.639 | 0.614 | 76 |
| gpt-5.5 few-shot | 3 | 0.463 (0.023) | 0.554 | 0.398 | 72 |
| gpt-5.5 few-shot | 4 | 0.652 (0.017) | 0.550 | 0.802 | 69 |
| gpt-5.5 few-shot | 5 | 0.685 (0.020) | 0.677 | 0.694 | 37 |
| gpt-mini zero-shot | 1 | 0.532 (0.035) | 0.871 | 0.383 | 47 |
| gpt-mini zero-shot | 2 | 0.553 (0.013) | 0.516 | 0.596 | 76 |
| gpt-mini zero-shot | 3 | 0.422 (0.019) | 0.500 | 0.366 | 72 |
| gpt-mini zero-shot | 4 | 0.578 (0.026) | 0.495 | 0.696 | 69 |
| gpt-mini zero-shot | 5 | 0.542 (0.049) | 0.508 | 0.586 | 37 |
| gpt-mini few-shot | 1 | 0.234 (0.032) | 0.903 | 0.135 | 47 |
| gpt-mini few-shot | 2 | 0.492 (0.004) | 0.462 | 0.526 | 76 |
| gpt-mini few-shot | 3 | 0.452 (0.032) | 0.447 | 0.458 | 72 |
| gpt-mini few-shot | 4 | 0.609 (0.007) | 0.486 | 0.816 | 69 |
| gpt-mini few-shot | 5 | 0.415 (0.045) | 0.642 | 0.306 | 37 |
| llama zero-shot | 1 | 0.693 (0.006) | 0.607 | 0.809 | 47 |
| llama zero-shot | 2 | 0.398 (0.004) | 0.657 | 0.285 | 76 |
| llama zero-shot | 3 | 0.417 (0.010) | 0.417 | 0.417 | 72 |
| llama zero-shot | 4 | 0.524 (0.004) | 0.454 | 0.618 | 69 |
| llama zero-shot | 5 | 0.515 (0.008) | 0.500 | 0.532 | 37 |
| llama few-shot | 1 | 0.424 (0.021) | 0.908 | 0.277 | 47 |
| llama few-shot | 2 | 0.302 (0.006) | 0.485 | 0.219 | 76 |
| llama few-shot | 3 | 0.497 (0.007) | 0.360 | 0.806 | 72 |
| llama few-shot | 4 | 0.533 (0.025) | 0.500 | 0.570 | 69 |
| llama few-shot | 5 | 0.376 (0.057) | 0.752 | 0.252 | 37 |
| mistral zero-shot | 1 | 0.265 (0.015) | 0.880 | 0.156 | 47 |
| mistral zero-shot | 2 | 0.350 (0.004) | 0.407 | 0.307 | 76 |
| mistral zero-shot | 3 | 0.447 (0.011) | 0.378 | 0.546 | 72 |
| mistral zero-shot | 4 | 0.582 (0.006) | 0.446 | 0.836 | 69 |
| mistral zero-shot | 5 | 0.051 (0.000) | 0.500 | 0.027 | 37 |
| mistral few-shot | 1 | 0.245 (0.016) | 0.911 | 0.142 | 47 |
| mistral few-shot | 2 | 0.411 (0.003) | 0.457 | 0.373 | 76 |
| mistral few-shot | 3 | 0.477 (0.008) | 0.353 | 0.736 | 72 |
| mistral few-shot | 4 | 0.515 (0.012) | 0.481 | 0.556 | 69 |
| mistral few-shot | 5 | 0.103 (0.000) | 1.000 | 0.054 | 37 |
