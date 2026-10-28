## Per-class F1: decoder champion vs encoder champion  (Δ = decoder − encoder)

For each task, the winning encoder vs winning decoder (by macro-F1). Δ>0 means the LLM wins that class. Proksch is on the 5-class scale (decoder collapsed 9→5).

### Matchups (macro-F1)

| Task | Encoder champ | Decoder champ | Overall Δ |
|---|---|---|---|
| Fowler | roberta-large (0.825) | gpt-5.5 zero-shot (0.786) | -0.039 🔴 encoder |
| van der Veen | roberta-large (0.742) | llama zero-shot (0.606) | -0.136 🔴 encoder |
| Ballard | roberta-large (0.720) | gpt-mini few-shot (0.655) | -0.065 🔴 encoder |
| Foy | roberta-large (0.903) | gemma few-shot (0.930) | +0.027 🟢 decoder |
| Dietrich | xlm-roberta-large (0.874) | gpt-5.5 few-shot (0.854) | -0.020 🔴 encoder |
| Goes | roberta-large (0.775) | gemma zero-shot (0.842) | +0.067 🟢 decoder |
| Kostovicova | xlm-roberta-large (0.525) | gpt-5.5 few-shot (0.546) | +0.021 🟢 decoder |
| Trubowitz | roberta-large (0.597) | gpt-5.5 few-shot (0.551) | -0.046 🔴 encoder |
| Heseltine | xlm-roberta-large (0.841) | mistral zero-shot (0.863) | +0.022 🟢 decoder |
| Proksch | roberta-large (0.464) | gpt-5.5 few-shot (0.632) | +0.168 🟢 decoder |

### Per-class breakdown

| Task | Class | Enc F1 | Dec F1 | Δ |
|---|---|---|---|---|
| Fowler | Attack | 0.754 | 0.719 | -0.036 |
| Fowler | Contrast | 0.762 | 0.714 | -0.048 |
| Fowler | Promote | 0.958 | 0.925 | -0.033 |
| van der Veen | neutral | 0.671 | 0.553 | -0.118 |
| van der Veen | pluralist | 0.705 | 0.567 | -0.139 |
| van der Veen | populist | 0.849 | 0.700 | -0.150 |
| Ballard | civil | 0.907 | 0.863 | -0.045 |
| Ballard | uncivil | 0.534 | 0.448 | -0.086 |
| Foy | Contrast | 0.836 | 0.892 | +0.056 |
| Foy | Negative | 0.944 | 0.961 | +0.017 |
| Foy | Positive | 0.929 | 0.937 | +0.008 |
| Dietrich | no-aid | 0.975 | 0.971 | -0.004 |
| Dietrich | aid | 0.772 | 0.736 | -0.036 |
| Goes | no-advice | 0.839 | 0.877 | +0.038 |
| Goes | advice | 0.712 | 0.807 | +0.096 |
| Kostovicova | 0 none | 0.439 | 0.610 | +0.171 |
| Kostovicova | 1 | 0.426 | 0.460 | +0.033 |
| Kostovicova | 2 | 0.727 | 0.566 | -0.161 |
| Kostovicova | 3 high | 0.508 | 0.550 | +0.042 |
| Trubowitz | No | 0.831 | 0.796 | -0.035 |
| Trubowitz | Unclear | 0.262 | 0.292 | +0.030 |
| Trubowitz | Yes | 0.698 | 0.566 | -0.133 |
| Heseltine | not-neg | 0.911 | 0.923 | +0.013 |
| Heseltine | negative | 0.771 | 0.802 | +0.031 |
| Proksch | 1 (neg) | 0.553 | 0.732 | +0.179 |
| Proksch | 2 | 0.512 | 0.626 | +0.114 |
| Proksch | 3 | 0.391 | 0.463 | +0.072 |
| Proksch | 4 | 0.549 | 0.652 | +0.103 |
| Proksch | 5 (pos) | 0.314 | 0.685 | +0.371 |
