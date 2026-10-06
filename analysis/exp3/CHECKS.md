# Experiment 3: checks (Qwen3.6-27B, layer 47, build split, in-sample)

Written by `scripts/exp3/checks.py`.

## 1. The pre-response control: a scenario's lie and truth

- Pairs (scenarios with both a lie and a truth): 70. Identical vectors: 54.
- The other 16 pairs differ by 1.2% of the vector's length (median; largest 1.7%). A lie and a truth from different scenarios differ by 60% (median of 60).
- So the pairs that are not exact ties differ by rounding in the forward pass, and their order in the pair counts is noise.

## 2. The newline after the response: family count against the residual direction

| score | AUROC, lies against truths |
|---|---|
| number of the eight families in the readout | 0.91 |
| residual direction (lie minus truth, fitted without the scenario) | 0.97 |

| | lies | truths |
|---|---|---|
| one or more of the eight | 133 / 152 | 10 / 81 |
| on the lie side of the direction | 143 / 152 | 11 / 81 |
| both | 129 / 152 | 7 / 81 |
| either | 147 / 152 | 14 / 81 |

- Lies with none of the eight (the misses): 14 of 19 are on the lie side of the direction.
- Truths with one or more of the eight: 7 of 10 are on the lie side. Truths with none: 4 of 71.
- Spearman correlation between the count and the direction score: 0.85 among all pressured transcripts, 0.66 among lies, 0.54 among truths.
- With the direction fitted on all pressured transcripts, on the lie side: 8 of 138 no-pressure truths, 1 of 703 unrelated chats.

Where each group sits on the direction (score; 0 = midpoint between the two means):

| group | transcripts | median | quartiles |
|---|---|---|---|
| lies with two or more of the eight | 126 | 15.9 | 12.4 to 18.4 |
| lies with one | 7 | 3.9 | 1.5 to 8.7 |
| lies with none (the misses) | 19 | 4.1 | 0.4 to 6.3 |
| truths with one or more | 10 | 3.9 | -0.2 to 9.3 |
| truths with none | 71 | -14.9 | -21.7 to -10.4 |

- The first principal component of the pressured transcripts alone, with nothing fitted on labels: AUROC 0.97 (14% of the variance).
