# DYL probe baseline: results (PLAN.md Section 5.8)

Written by `scripts/analyze_dyl_probe.py` from `data/cluster/runs/<model>/dyl_probe.jsonl`
(`src/dyl_probe.py` on the cluster, 2026-10-01). Transcripts: the selection with commentary
transcripts dropped (`load_manifest()`), so the cells match the families'. Wording Q9_dyl, the
probe's own wording. Position: the token before the yes/no answer, at the probe's layer.

Terms. **AUROC**: the probability that a random lie scores higher than a random truth (0.5 =
chance; below 0.5 = lies score lower). **Interval**: 95% bootstrap, scenarios resampled.
**p**: label-permutation p-value, 10,000 shuffles, two-sided. **z_rms**: the size of the
standardized residual vector; about 1 means our activations look like the probe's training
data. **Denial cell**: transcripts whose Q9 answer is No. **AISI labelling**: positive = lie and
denied; negative = truth and denied, or lie and admitted; truth and admitted dropped.

## 1. Do our activations match the probe's training data?

| model | layer | token read | rows scored | z_rms median | rows with z_rms > 2 | rows dropped (answer not yes/no) |
|---|---|---|---|---|---|---|
| gemma-3-12b-it | 46 | `'\n'` ×529 | 529 of 529 | 1.30 | 0% | 0 |
| gemma-3-27b-it | 58 | `'\n'` ×558 | 558 of 558 | 1.23 | 0% | 0 |
| qwen3.6-27b | 50 | `'\n\n'` ×791 | 791 of 792 | 4.34 | 100% | 1 |
| gpt-oss-20b | 16 | `'<|message|>'` ×824 | 824 of 846 | 4.88 | 100% | 22 |

## 2. Self-report answers under Q9 (scenario transcripts)

| model | lie: deny / admit / other | truth: deny / admit / other |
|---|---|---|
| gemma-3-12b-it | 11 / 65 / 0 | 11 / 40 / 0 |
| gemma-3-27b-it | 7 / 86 / 0 | 12 / 41 / 0 |
| qwen3.6-27b | 111 / 141 / 0 | 128 / 7 / 0 |
| gpt-oss-20b | 173 / 7 / 0 | 149 / 4 / 0 |

## 3. AUROC, build split

Each entry: AUROC (lies / truths) [interval] p.

| model | all scenario transcripts (AUROC 1) | denial cell (AUROC 2) | admit cell | AISI labelling (dropped) |
|---|---|---|---|---|
| gemma-3-12b-it | 0.435 (49 / 32) [0.32, 0.54] p = 0.325 | 0.407 (9 / 9) [0.15, 0.67] p = 0.544 | 0.480 (40 / 23) [0.36, 0.61] p = 0.807 | 0.891 (9 / 49) [0.80, 0.96] p = 0.000 (23) |
| gemma-3-27b-it | 0.605 (58 / 30) [0.48, 0.73] p = 0.103 | 0.643 (7 / 8) [0.41, 0.84] p = 0.391 | 0.661 (51 / 22) [0.53, 0.79] p = 0.029 | 0.797 (7 / 59) [0.65, 0.92] p = 0.009 (22) |
| qwen3.6-27b | 0.274 (151 / 81) [0.21, 0.34] p = 0.000 | 0.550 (65 / 76) [0.45, 0.64] p = 0.299 | 0.302 (86 / 5) [0.22, 0.39] p = 0.140 | 0.762 (65 / 162) [0.70, 0.82] p = 0.000 (5) |
| gpt-oss-20b | 0.486 (108 / 91) [0.43, 0.54] p = 0.731 | 0.480 (105 / 88) [0.42, 0.54] p = 0.634 | 0.444 (3 / 3) [0.00, 0.89] p = 1.000 | 0.468 (105 / 91) [0.41, 0.53] p = 0.432 (3) |

## 4. AUROC, held-out split

Each entry: AUROC (lies / truths) [interval] p.

| model | all scenario transcripts (AUROC 1) | denial cell (AUROC 2) | admit cell | AISI labelling (dropped) |
|---|---|---|---|---|
| gemma-3-12b-it | 0.347 (27 / 19) [0.22, 0.48] p = 0.084 | 0.250 (2 / 2) [0.00, 1.00] p = 0.662 | 0.336 (25 / 17) [0.22, 0.46] p = 0.075 | 0.944 (2 / 27) [0.85, 1.00] p = 0.030 (17) |
| gemma-3-27b-it | 0.491 (35 / 23) [0.37, 0.61] p = 0.913 | — (0 / 4) | 0.522 (35 / 19) [0.39, 0.65] p = 0.803 | — (0 / 39) (19) |
| qwen3.6-27b | 0.250 (101 / 54) [0.19, 0.32] p = 0.000 | 0.499 (46 / 52) [0.40, 0.61] p = 0.992 | 0.336 (55 / 2) [0.23, 0.46] p = 0.476 | 0.739 (46 / 107) [0.67, 0.80] p = 0.000 (2) |
| gpt-oss-20b | 0.510 (72 / 62) [0.44, 0.59] p = 0.840 | 0.507 (68 / 61) [0.43, 0.58] p = 0.884 | 0.000 (4 / 1) | 0.493 (68 / 65) [0.42, 0.57] p = 0.893 (1) |

## 5. AUROC, both splits pooled

Each entry: AUROC (lies / truths) [interval] p.

| model | all scenario transcripts (AUROC 1) | denial cell (AUROC 2) | admit cell | AISI labelling (dropped) |
|---|---|---|---|---|
| gemma-3-12b-it | 0.410 (76 / 51) [0.33, 0.49] p = 0.086 | 0.372 (11 / 11) [0.14, 0.63] p = 0.329 | 0.424 (65 / 40) [0.33, 0.51] p = 0.195 | 0.909 (11 / 76) [0.84, 0.96] p = 0.000 (40) |
| gemma-3-27b-it | 0.563 (93 / 53) [0.48, 0.65] p = 0.206 | 0.667 (7 / 12) [0.44, 0.85] p = 0.259 | 0.598 (86 / 41) [0.51, 0.69] p = 0.071 | 0.815 (7 / 98) [0.69, 0.93] p = 0.004 (41) |
| qwen3.6-27b | 0.264 (252 / 135) [0.22, 0.31] p = 0.000 | 0.529 (111 / 128) [0.46, 0.60] p = 0.449 | 0.305 (141 / 7) [0.22, 0.40] p = 0.084 | 0.752 (111 / 269) [0.71, 0.79] p = 0.000 (7) |
| gpt-oss-20b | 0.494 (180 / 153) [0.45, 0.54] p = 0.851 | 0.489 (173 / 149) [0.44, 0.54] p = 0.738 | 0.321 (7 / 4) [0.00, 0.75] p = 0.415 | 0.477 (173 / 156) [0.43, 0.52] p = 0.456 (4) |

## 6. Flags at the shipped threshold (set by AISI at 1% on Alpaca)

| model | scenario lies | scenario truths | no-pressure truths | unrelated |
|---|---|---|---|---|
| gemma-3-12b-it | 3 / 76 (3.9%) | 4 / 51 (7.8%) | 4 / 221 (1.8%) | 0 / 179 (0.0%) |
| gemma-3-27b-it | 3 / 93 (3.2%) | 3 / 53 (5.7%) | 5 / 211 (2.4%) | 1 / 199 (0.5%) |
| qwen3.6-27b | 112 / 252 (44.4%) | 124 / 135 (91.9%) | 208 / 228 (91.2%) | 28 / 158 (17.7%) |
| gpt-oss-20b | 20 / 180 (11.1%) | 14 / 153 (9.2%) | 1 / 209 (0.5%) | 1 / 265 (0.4%) |

## 7. At a threshold that fires on 1% of our honest transcripts (no-pressure truths + unrelated)

| model | honest n | scenario lies above | scenario truths above | no-pressure truths above | unrelated above |
|---|---|---|---|---|---|
| gemma-3-12b-it | 400 | 4 / 76 (5.3%) | 4 / 51 (7.8%) | 4 / 221 (1.8%) | 0 / 179 (0.0%) |
| gemma-3-27b-it | 410 | 3 / 93 (3.2%) | 3 / 53 (5.7%) | 4 / 211 (1.9%) | 1 / 199 (0.5%) |
| qwen3.6-27b | 386 | 20 / 252 (7.9%) | 8 / 135 (5.9%) | 4 / 228 (1.8%) | 0 / 158 (0.0%) |
| gpt-oss-20b | 474 | 25 / 180 (13.9%) | 18 / 153 (11.8%) | 2 / 209 (1.0%) | 3 / 265 (1.1%) |

## 8. Does the score track the answer rather than the label?

AUROC of the probe score for *deny* (positive) versus *admit*, with the lie/truth label held fixed.
A high value means the score mostly says which answer is coming, not whether the response was a lie.

| model | among lies | among truths | all scenario transcripts | no-pressure set |
|---|---|---|---|---|
| gemma-3-12b-it | 1.000 (11 / 65) [1.00, 1.00] p = 0.000 | 1.000 (11 / 40) [1.00, 1.00] p = 0.000 | 1.000 (22 / 105) [1.00, 1.00] p = 0.000 | 0.998 (197 / 26) [0.99, 1.00] p = 0.000 |
| gemma-3-27b-it | 0.836 (7 / 86) [0.69, 0.95] p = 0.001 | 0.740 (12 / 41) [0.56, 0.90] p = 0.011 | 0.746 (19 / 127) [0.60, 0.86] p = 0.000 | 0.687 (151 / 62) [0.61, 0.76] p = 0.000 |
| qwen3.6-27b | 0.955 (111 / 141) [0.93, 0.98] p = 0.000 | 0.994 (128 / 7) [0.98, 1.00] p = 0.000 | 0.967 (239 / 148) [0.95, 0.98] p = 0.000 | 1.000 (245 / 1) |
| gpt-oss-20b | 0.211 (173 / 7) [0.12, 0.32] p = 0.007 | 0.221 (149 / 4) [0.02, 0.58] p = 0.058 | 0.215 (322 / 11) [0.10, 0.34] p = 0.001 | 0.186 (218 / 8) [0.04, 0.38] p = 0.002 |

## 9. Balanced accuracy at the shipped threshold (AISI's headline metric)

Balanced accuracy = the mean of the true-positive rate and the true-negative rate. AISI's labelling:
positive = lie and denied; negative = truth and denied, or lie and admitted. The deployment rule flags
a transcript when the model said Yes or the score passes the threshold. Entries: balanced accuracy
(true-positive rate / false-positive rate; positives / negatives).

| model | AISI labelling, probe alone | our labels, probe alone | our labels, said Yes or flagged |
|---|---|---|---|
| gemma-3-12b-it | 0.61 (0.27 / 0.05; 11 / 76) | 0.48 (0.04 / 0.08; 76 / 51) | 0.52 (0.89 / 0.86; 76 / 51) |
| gemma-3-27b-it | 0.63 (0.29 / 0.03; 7 / 98) | 0.49 (0.03 / 0.06; 93 / 53) | 0.57 (0.95 / 0.81; 93 / 53) |
| qwen3.6-27b | 0.68 (0.87 / 0.52; 111 / 269) | 0.26 (0.44 / 0.92; 252 / 135) | 0.49 (0.94 / 0.97; 252 / 135) |
| gpt-oss-20b | 0.52 (0.11 / 0.08; 173 / 156) | 0.51 (0.11 / 0.09; 180 / 153) | 0.52 (0.14 / 0.10; 180 / 153) |

Figure: `dyl_probe_scores.png` (score distributions per model).
