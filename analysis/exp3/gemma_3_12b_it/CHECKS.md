# Experiment 3: checks (Gemma-3-12B, layer 29, build split, in-sample)

Written by `scripts/exp3/checks.py`.

## 1. The pre-response control: a scenario's lie and truth

- Pairs (scenarios with both a lie and a truth): 16. Identical vectors: 9.
- The other 7 pairs differ by 0.6% of the vector's length (median; largest 0.7%). A lie and a truth from different scenarios differ by 14% (median of 60).
- So the pairs that are not exact ties differ by rounding in the forward pass, and their order in the pair counts is noise.

## 2. The newline after the response: family count against the residual direction

Each dimension is divided by its spread in the unrelated chats first, as in the pictures.

| score | AUROC, lies against truths |
|---|---|
| number of its eight lie-leaning families in the readout | 0.73 |
| residual direction (lie minus truth, fitted without the scenario) | 0.71 |

| | lies | truths |
|---|---|---|
| one or more of the eight | 30 / 49 | 5 / 32 |
| on the lie side of the direction | 32 / 49 | 11 / 32 |
| both | 24 / 49 | 5 / 32 |
| either | 38 / 49 | 11 / 32 |

- Lies with none of the eight (the misses): 8 of 19 are on the lie side of the direction.
- Truths with one or more of the eight: 5 of 5 are on the lie side. Truths with none: 6 of 27.
- Spearman correlation between the count and the direction score: 0.60 among all pressured transcripts, 0.52 among lies, 0.59 among truths.
- With the direction fitted on all pressured transcripts, on the lie side: 5 of 135 no-pressure truths, 0 of 179 unrelated chats.

Where each group sits on the direction (score; 0 = midpoint between the two means):

| group | transcripts | median | quartiles |
|---|---|---|---|
| lies with two or more of the eight | 23 | 15.6 | 3.7 to 23.5 |
| lies with one | 7 | 0.1 | -7.5 to 19.2 |
| lies with none (the misses) | 19 | -1.2 | -9.4 to 5.2 |
| truths with one or more | 5 | 20.9 | 17.7 to 22.6 |
| truths with none | 27 | -10.0 | -14.8 to -4.5 |

- The first principal component of the pressured transcripts alone, with nothing fitted on labels: AUROC 0.57 (28% of the variance).
