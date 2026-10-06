# The released probe: the label or the coming answer, by split

Qwen3.6-27B, Q9, the token before the answer, the probe's layer. Each cell: AUROC (positives / negatives)
[95% interval, scenarios resampled]. Positives are lies in the first three rows and denials in the last three.

| comparison | exploratory set | held-out set | both |
|---|---|---|---|
| lie against truth, all transcripts | 0.274 (151 / 81) [0.21, 0.34] | 0.250 (101 / 54) [0.19, 0.32] | 0.264 (252 / 135) [0.22, 0.31] |
| lie against truth, among deniers | 0.550 (65 / 76) [0.45, 0.64] | 0.499 (46 / 52) [0.40, 0.61] | 0.529 (111 / 128) [0.46, 0.60] |
| AISI's labelling (lied and denied, against the rest) | 0.762 (65 / 162) [0.70, 0.82] | 0.739 (46 / 107) [0.67, 0.80] | 0.752 (111 / 269) [0.71, 0.79] |
| deny against admit, all transcripts | 0.962 (141 / 91) [0.94, 0.98] | 0.976 (98 / 57) [0.95, 0.99] | 0.967 (239 / 148) [0.95, 0.98] |
| deny against admit, among lies | 0.949 (65 / 86) [0.91, 0.98] | 0.966 (46 / 55) [0.93, 0.99] | 0.955 (111 / 141) [0.93, 0.98] |
| deny against admit, among truths | 0.989 (76 / 5) [0.96, 1.00] | 1.000 (52 / 2) [1.00, 1.00] | 0.994 (128 / 7) [0.98, 1.00] |

## Balanced accuracy at the shipped threshold

The threshold is AISI's, set to flag 1% of Alpaca completions; nothing is calibrated on our data. Each cell:
balanced accuracy (true-positive rate / false-positive rate; positives / negatives) [95% interval, scenarios
resampled]. Balanced accuracy is the mean of the true-positive rate and the true-negative rate.

| comparison | exploratory set | held-out set | both |
|---|---|---|---|
| AISI's labelling (lied and denied, against the rest) | 0.68 (0.89 / 0.52; 65 / 162) [0.64, 0.73] | 0.67 (0.85 / 0.50; 46 / 107) [0.61, 0.73] | 0.68 (0.87 / 0.52; 111 / 269) [0.64, 0.71] |
| lie against truth, all transcripts | 0.27 (0.46 / 0.91; 151 / 81) [0.23, 0.32] | 0.25 (0.43 / 0.93; 101 / 54) [0.20, 0.31] | 0.26 (0.44 / 0.92; 252 / 135) [0.23, 0.30] |
| lie against truth, among deniers | 0.46 (0.89 / 0.97; 65 / 76) [0.42, 0.50] | 0.44 (0.85 / 0.96; 46 / 52) [0.38, 0.50] | 0.45 (0.87 / 0.97; 111 / 128) [0.42, 0.48] |
