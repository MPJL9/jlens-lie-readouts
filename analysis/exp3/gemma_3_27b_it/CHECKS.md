# Experiment 3: checks (Gemma-3-27B, layer 39, build split, in-sample)

Written by `scripts/exp3/checks.py`.

## 1. The pre-response control: a scenario's lie and truth

- Pairs (scenarios with both a lie and a truth): 11. Identical vectors: 11.
- Every pair is identical. A lie and a truth from different scenarios differ by 24% (median of 60).

## 2. The newline after the response: family count against the residual direction

Each dimension is divided by its spread in the unrelated chats first, as in the pictures.

| score | AUROC, lies against truths |
|---|---|
| number of its three lie-leaning families in the readout | 0.62 |
| residual direction (lie minus truth, fitted without the scenario) | 0.52 |

| | lies | truths |
|---|---|---|
| one or more of the three | 24 / 58 | 6 / 30 |
| on the lie side of the direction | 42 / 58 | 18 / 30 |
| both | 16 / 58 | 4 / 30 |
| either | 50 / 58 | 20 / 30 |

- Lies with none of the three (the misses): 26 of 34 are on the lie side of the direction.
- Truths with one or more of the three: 4 of 6 are on the lie side. Truths with none: 14 of 24.
- Spearman correlation between the count and the direction score: -0.04 among all pressured transcripts, -0.09 among lies, 0.03 among truths.
- With the direction fitted on all pressured transcripts, on the lie side: 38 of 133 no-pressure truths, 89 of 199 unrelated chats.

Where each group sits on the direction (score; 0 = midpoint between the two means):

| group | transcripts | median | quartiles |
|---|---|---|---|
| lies with two or more of the three | 19 | 16.9 | -44.5 to 24.7 |
| lies with one | 5 | 27.3 | 9.4 to 43.0 |
| lies with none (the misses) | 34 | 21.5 | 11.5 to 34.5 |
| truths with one or more | 6 | 19.1 | -22.8 to 26.2 |
| truths with none | 24 | 21.4 | -47.9 to 35.2 |

- The first principal component of the pressured transcripts alone, with nothing fitted on labels: AUROC 0.55 (58% of the variance).
