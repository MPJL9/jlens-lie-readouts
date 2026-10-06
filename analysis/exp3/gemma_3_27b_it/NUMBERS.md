# Experiment 3: numbers behind the pictures (Gemma-3-27B, build split, in-sample)

Written by `scripts/exp3/pictures.py`. Every number is cross-validated in five folds with scenarios kept together.
*line* = AUROC of a straight-line split of lies against truths in the two drawn dimensions. *direction* = AUROC of the
lie-minus-truth direction in the full space. *pairs* = scenarios with both a lie and a truth in which the lie scores above
its truth. 0.50 is chance. Transcripts: 58 lies, 30 truths, 133 no-pressure truths, 199 unrelated chats.

**Scaled.** Before every fit, each dimension of the residual stream is divided by its spread (standard deviation) in the
unrelated chats at the same position and layer (after the question: the spread within each wording). The lengths in
Section 5 are those of the scaled vectors.

## 1. Before the question, layer 39

| position | measure | AUROC (95% interval over scenarios) | pairs |
|---|---|---|---|
| the newline after the response | line, fit on unrelated chats | 0.51 (0.39 to 0.64) | 5 of 11 |
| the newline after the response | line, fit on pressured transcripts | 0.51 (0.37 to 0.64) | 6 of 11 |
| the newline after the response | direction, full space | 0.52 (0.39 to 0.65) | 6 of 11 |
| control: the turn-end token after the response | line, fit on unrelated chats | 0.44 (0.32 to 0.55) | 4 of 11 |
| control: the turn-end token after the response | line, fit on pressured transcripts | 0.56 (0.44 to 0.68) | 3 of 11 |
| control: the turn-end token after the response | direction, full space | 0.63 (0.52 to 0.74) | 8 of 11 |
| control: the newline before the response | line, fit on unrelated chats | 0.53 (0.42 to 0.64) | 0 of 11 (11 ties) |
| control: the newline before the response | line, fit on pressured transcripts | 0.55 (0.44 to 0.67) | 0 of 11 (11 ties) |
| control: the newline before the response | direction, full space | 0.58 (0.48 to 0.69) | 0 of 11 (11 ties) |

Along the direction (0 = midpoint between the two means of the other folds):

| position | missed lies on the truth side | other lies on the truth side | truths on the lie side |
|---|---|---|---|
| the newline after the response | 8 / 34 | 8 / 24 | 18 / 30 |
| control: the turn-end token after the response | 9 / 34 | 7 / 24 | 15 / 30 |
| control: the newline before the response | 11 / 34 | 9 / 24 | 16 / 30 |

## 2. Before the question, by layer

| position | measure | layer 27 | layer 33 | layer 39 | layer 46 | layer 52 |
|---|---|---|---|---|---|---|
| the newline after the response | line, fit on unrelated chats | 0.40 | 0.50 | 0.51 | 0.55 | 0.47 |
| the newline after the response | line, fit on pressured transcripts | 0.77 | 0.63 | 0.51 | 0.50 | 0.41 |
| the newline after the response | direction, full space | 0.81 | 0.64 | 0.52 | 0.52 | 0.53 |
| control: the turn-end token after the response | line, fit on unrelated chats | 0.45 | 0.48 | 0.44 | 0.44 | 0.42 |
| control: the turn-end token after the response | line, fit on pressured transcripts | 0.52 | 0.56 | 0.56 | 0.55 | 0.56 |
| control: the turn-end token after the response | direction, full space | 0.74 | 0.68 | 0.63 | 0.63 | 0.63 |
| control: the newline before the response | line, fit on unrelated chats | 0.53 | 0.50 | 0.53 | 0.49 | 0.54 |
| control: the newline before the response | line, fit on pressured transcripts | 0.53 | 0.54 | 0.55 | 0.55 | 0.56 |
| control: the newline before the response | direction, full space | 0.57 | 0.58 | 0.58 | 0.59 | 0.59 |

UMAP of the pressured transcripts (check; line AUROC for seeds 0, 1, 2): the newline after the response: 0.58, 0.56, 0.57; control: the turn-end token after the response: 0.60, 0.57, 0.58; control: the newline before the response: 0.56, 0.59, 0.52.

## 3. After the question, layer 39

Lies / truths in brackets. *deniers* = transcripts that answer No; the line is fitted among deniers.

**the newline after the question** (`preans_slot1`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.65 (58 / 30) | – | 0.76 (58 / 30) | – | 0.72, 0.75, 0.73 |
| Q2 | 0.65 (58 / 30) | – | 0.81 (58 / 30) | – | 0.73, 0.76, 0.75 |
| Q6 | 0.44 (58 / 30) | – | 0.77 (58 / 30) | – | 0.75, 0.75, 0.75 |
| Q7 | 0.64 (58 / 30) | 0.46 (16 / 12) | 0.62 (58 / 30) | 0.43 (16 / 12) | 0.61, 0.65, 0.52 |
| Q9 | 0.70 (58 / 30) | – | 0.65 (58 / 30) | – | 0.63, 0.65, 0.64 |

**the turn-start token after the question** (`preans_slot2`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.57 (58 / 30) | – | 0.79 (58 / 30) | – | 0.81, 0.83, 0.82 |
| Q2 | 0.63 (58 / 30) | – | 0.79 (58 / 30) | – | 0.81, 0.82, 0.83 |
| Q6 | 0.78 (58 / 30) | – | 0.82 (58 / 30) | – | 0.80, 0.80, 0.80 |
| Q7 | 0.64 (58 / 30) | 0.54 (16 / 12) | 0.68 (58 / 30) | 0.58 (16 / 12) | 0.74, 0.73, 0.72 |
| Q9 | 0.59 (58 / 30) | – | 0.79 (58 / 30) | – | 0.79, 0.78, 0.78 |

**the newline after `model`** (`preans_slot4`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.38 (58 / 30) | – | 0.74 (58 / 30) | – | 0.59, 0.54, 0.59 |
| Q2 | 0.68 (58 / 30) | – | 0.74 (58 / 30) | – | 0.57, 0.54, 0.55 |
| Q6 | 0.66 (58 / 30) | – | 0.74 (58 / 30) | – | 0.58, 0.54, 0.56 |
| Q7 | 0.69 (58 / 30) | 0.67 (16 / 12) | 0.69 (58 / 30) | 0.67 (16 / 12) | 0.57, 0.59, 0.57 |
| Q9 | 0.75 (58 / 30) | – | 0.73 (58 / 30) | – | 0.58, 0.55, 0.56 |

**the first newline after the self-report answer** (`postans_slot1`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.53 (40 / 17) | – | 0.62 (40 / 17) | – | 0.49, 0.60, 0.55 |
| Q2 | 0.56 (58 / 30) | – | 0.64 (58 / 30) | – | 0.60, 0.67, 0.58 |
| Q6 | 0.44 (58 / 30) | – | 0.50 (58 / 30) | – | 0.51, 0.48, 0.40 |
| Q7 | 0.61 (58 / 30) | 0.48 (16 / 12) | 0.35 (58 / 30) | 0.50 (16 / 12) | 0.52, 0.42, 0.45 |
| Q9 | 0.58 (58 / 30) | – | 0.60 (58 / 30) | – | 0.54, 0.45, 0.57 |

**the last newline after the self-report answer** (`postans_slot4`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.61 (40 / 17) | – | 0.65 (40 / 17) | – | 0.60, 0.60, 0.63 |
| Q2 | 0.63 (58 / 30) | – | 0.59 (58 / 30) | – | 0.55, 0.48, 0.49 |
| Q6 | 0.74 (58 / 30) | – | 0.57 (58 / 30) | – | 0.57, 0.57, 0.55 |
| Q7 | 0.61 (58 / 30) | 0.43 (16 / 12) | 0.59 (58 / 30) | 0.24 (16 / 12) | 0.59, 0.54, 0.48 |
| Q9 | 0.56 (58 / 30) | – | 0.60 (58 / 30) | – | 0.59, 0.57, 0.56 |

## 4. After the question, by layer (line AUROC; all, then deniers)

**the newline after the question** (`preans_slot1`)

| wording | fit | layer 27 | layer 33 | layer 39 | layer 46 | layer 52 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.38, – | 0.51, – | 0.65, – | 0.61, – | 0.61, – |
| Q1 | pressured | 0.72, – | 0.80, – | 0.76, – | 0.74, – | 0.71, – |
| Q2 | unrelated | 0.57, – | 0.40, – | 0.65, – | 0.54, – | 0.58, – |
| Q2 | pressured | 0.73, – | 0.84, – | 0.81, – | 0.80, – | 0.80, – |
| Q6 | unrelated | 0.49, – | 0.35, – | 0.44, – | 0.43, – | 0.42, – |
| Q6 | pressured | 0.72, – | 0.84, – | 0.77, – | 0.73, – | 0.70, – |
| Q7 | unrelated | 0.43, 0.42 | 0.51, 0.34 | 0.64, 0.46 | 0.53, 0.28 | 0.61, 0.21 |
| Q7 | pressured | 0.71, 0.67 | 0.75, 0.79 | 0.62, 0.43 | 0.58, 0.33 | 0.56, 0.46 |
| Q9 | unrelated | 0.59, – | 0.47, – | 0.70, – | 0.68, – | 0.59, – |
| Q9 | pressured | 0.79, – | 0.80, – | 0.65, – | 0.60, – | 0.58, – |

**the turn-start token after the question** (`preans_slot2`)

| wording | fit | layer 27 | layer 33 | layer 39 | layer 46 | layer 52 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.62, – | 0.37, – | 0.57, – | 0.56, – | 0.55, – |
| Q1 | pressured | 0.87, – | 0.87, – | 0.79, – | 0.74, – | 0.70, – |
| Q2 | unrelated | 0.64, – | 0.28, – | 0.63, – | 0.58, – | 0.53, – |
| Q2 | pressured | 0.88, – | 0.89, – | 0.79, – | 0.72, – | 0.69, – |
| Q6 | unrelated | 0.57, – | 0.45, – | 0.78, – | 0.76, – | 0.71, – |
| Q6 | pressured | 0.87, – | 0.88, – | 0.82, – | 0.77, – | 0.75, – |
| Q7 | unrelated | 0.61, 0.85 | 0.51, 0.29 | 0.64, 0.54 | 0.61, 0.48 | 0.60, 0.59 |
| Q7 | pressured | 0.87, 0.86 | 0.79, 0.77 | 0.68, 0.58 | 0.65, 0.56 | 0.65, 0.57 |
| Q9 | unrelated | 0.52, – | 0.45, – | 0.59, – | 0.63, – | 0.65, – |
| Q9 | pressured | 0.85, – | 0.84, – | 0.79, – | 0.71, – | 0.66, – |

**the newline after `model`** (`preans_slot4`)

| wording | fit | layer 27 | layer 33 | layer 39 | layer 46 | layer 52 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.47, – | 0.49, – | 0.38, – | 0.52, – | 0.53, – |
| Q1 | pressured | 0.59, – | 0.80, – | 0.74, – | 0.70, – | 0.69, – |
| Q2 | unrelated | 0.49, – | 0.61, – | 0.68, – | 0.60, – | 0.56, – |
| Q2 | pressured | 0.57, – | 0.72, – | 0.74, – | 0.70, – | 0.71, – |
| Q6 | unrelated | 0.55, – | 0.58, – | 0.66, – | 0.53, – | 0.54, – |
| Q6 | pressured | 0.59, – | 0.74, – | 0.74, – | 0.68, – | 0.69, – |
| Q7 | unrelated | 0.50, 0.58 | 0.58, 0.60 | 0.69, 0.67 | 0.48, 0.58 | 0.54, 0.40 |
| Q7 | pressured | 0.59, 0.80 | 0.72, 0.85 | 0.69, 0.67 | 0.63, 0.51 | 0.66, 0.62 |
| Q9 | unrelated | 0.52, – | 0.61, – | 0.75, – | 0.68, – | 0.54, – |
| Q9 | pressured | 0.62, – | 0.72, – | 0.73, – | 0.67, – | 0.69, – |

**the first newline after the self-report answer** (`postans_slot1`)

| wording | fit | layer 27 | layer 33 | layer 39 | layer 46 | layer 52 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.51, – | 0.38, – | 0.53, – | 0.56, – | 0.56, – |
| Q1 | pressured | 0.68, – | 0.66, – | 0.62, – | 0.57, – | 0.62, – |
| Q2 | unrelated | 0.66, – | 0.68, – | 0.56, – | 0.51, – | 0.48, – |
| Q2 | pressured | 0.65, – | 0.66, – | 0.64, – | 0.64, – | 0.67, – |
| Q6 | unrelated | 0.40, – | 0.40, – | 0.44, – | 0.46, – | 0.47, – |
| Q6 | pressured | 0.60, – | 0.54, – | 0.50, – | 0.53, – | 0.52, – |
| Q7 | unrelated | 0.58, 0.34 | 0.47, 0.42 | 0.61, 0.48 | 0.57, 0.26 | 0.52, 0.22 |
| Q7 | pressured | 0.51, 0.52 | 0.49, 0.43 | 0.35, 0.50 | 0.36, 0.61 | 0.47, 0.32 |
| Q9 | unrelated | 0.60, – | 0.59, – | 0.58, – | 0.51, – | 0.55, – |
| Q9 | pressured | 0.66, – | 0.64, – | 0.60, – | 0.61, – | 0.63, – |

**the last newline after the self-report answer** (`postans_slot4`)

| wording | fit | layer 27 | layer 33 | layer 39 | layer 46 | layer 52 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.17, – | 0.46, – | 0.61, – | 0.55, – | 0.57, – |
| Q1 | pressured | 0.68, – | 0.71, – | 0.65, – | 0.61, – | 0.62, – |
| Q2 | unrelated | 0.54, – | 0.50, – | 0.63, – | 0.61, – | 0.60, – |
| Q2 | pressured | 0.66, – | 0.59, – | 0.59, – | 0.60, – | 0.59, – |
| Q6 | unrelated | 0.51, – | 0.69, – | 0.74, – | 0.70, – | 0.68, – |
| Q6 | pressured | 0.54, – | 0.56, – | 0.57, – | 0.58, – | 0.58, – |
| Q7 | unrelated | 0.46, 0.48 | 0.66, 0.40 | 0.61, 0.43 | 0.57, 0.31 | 0.56, 0.29 |
| Q7 | pressured | 0.51, 0.49 | 0.53, 0.41 | 0.59, 0.24 | 0.62, 0.22 | 0.62, 0.29 |
| Q9 | unrelated | 0.49, – | 0.65, – | 0.56, – | 0.55, – | 0.51, – |
| Q9 | pressured | 0.52, – | 0.60, – | 0.60, – | 0.63, – | 0.62, – |

## 5. Vector lengths, layer 39

Mean length of the residual vectors and its spread (standard deviation / mean). A small spread means that a fit on
vectors scaled to length 1 (the cosine view) would show nearly the same picture as the PCA drawn here. After the
question: the mean over the five wordings.

| position | pressured: mean length | pressured: spread | unrelated: mean length | unrelated: spread |
|---|---|---|---|---|
| the newline after the response | 124 | 24.0% | 101 | 30.7% |
| control: the turn-end token after the response | 181 | 3.1% | 191 | 3.2% |
| control: the newline before the response | 100 | 8.2% | 97 | 6.3% |
| the newline after the question | 136 | 5.2% | 136 | 4.2% |
| the turn-start token after the question | 106 | 8.8% | 105 | 7.0% |
| the newline after `model` | 266 | 3.7% | 277 | 1.9% |
| the first newline after the self-report answer | 118 | 21.3% | 111 | 17.4% |
| the last newline after the self-report answer | 222 | 3.8% | 202 | 2.7% |

## 6. Lies against truths within the first k principal components of the unrelated chats, layer 39

AUROC of the lie-minus-truth direction fitted within the first k components (on other scenarios than the one scored).
*full space* = the same direction with no restriction. After the question: the mean over the wordings; *deniers* over the
wordings with 10 or more lying and 10 or more truthful deniers. The last k is all components when there are 1,000 or fewer.

| position | k = 1 | k = 2 | k = 3 | k = 5 | k = 10 | k = 20 | k = 50 | k = 100 | k = 198 | k = 200 | k = 500 | k = 902 | k = 990 | full space |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| the newline after the response | 0.53 | 0.53 | 0.52 | 0.52 | 0.52 | 0.52 | 0.52 | 0.52 | 0.52 | – | – | – | – | 0.52 |
| control: the turn-end token after the response | 0.40 | 0.41 | 0.53 | 0.56 | 0.56 | 0.57 | 0.55 | 0.56 | 0.57 | – | – | – | – | 0.63 |
| control: the newline before the response | 0.55 | 0.53 | 0.53 | 0.52 | 0.53 | 0.52 | 0.51 | 0.52 | 0.53 | – | – | – | – | 0.58 |
| the newline after the question | 0.59 | 0.61 | 0.60 | 0.61 | 0.73 | 0.76 | 0.76 | 0.77 | – | 0.78 | 0.79 | – | 0.80 | 0.82 |
| the newline after the question, deniers | 0.62 | 0.53 | 0.51 | 0.57 | 0.67 | 0.72 | 0.74 | 0.78 | – | 0.85 | 0.87 | – | 0.90 | 0.91 |
| the turn-start token after the question | 0.51 | 0.62 | 0.61 | 0.65 | 0.71 | 0.76 | 0.79 | 0.80 | – | 0.81 | 0.83 | – | 0.84 | 0.86 |
| the turn-start token after the question, deniers | 0.42 | 0.58 | 0.50 | 0.50 | 0.41 | 0.56 | 0.65 | 0.71 | – | 0.75 | 0.80 | – | 0.83 | 0.86 |
| the newline after `model` | 0.49 | 0.63 | 0.68 | 0.70 | 0.71 | 0.72 | 0.72 | 0.72 | – | 0.73 | 0.74 | – | 0.74 | 0.75 |
| the newline after `model`, deniers | 0.43 | 0.69 | 0.68 | 0.76 | 0.76 | 0.81 | 0.82 | 0.83 | – | 0.85 | 0.87 | – | 0.88 | 0.90 |
| the first newline after the self-report answer | 0.50 | 0.52 | 0.52 | 0.52 | 0.56 | 0.60 | 0.60 | 0.60 | – | 0.61 | 0.62 | 0.63 | – | 0.65 |
| the first newline after the self-report answer, deniers | 0.30 | 0.41 | 0.42 | 0.61 | 0.70 | 0.66 | 0.68 | 0.69 | – | 0.74 | 0.74 | 0.76 | – | 0.78 |
| the last newline after the self-report answer | 0.65 | 0.64 | 0.62 | 0.62 | 0.63 | 0.63 | 0.66 | 0.67 | – | 0.68 | 0.69 | 0.69 | – | 0.70 |
| the last newline after the self-report answer, deniers | 0.64 | 0.58 | 0.59 | 0.58 | 0.50 | 0.48 | 0.61 | 0.68 | – | 0.69 | 0.72 | 0.74 | – | 0.77 |

Share of the unrelated chats' variance held by the first k components:

| position | k = 1 | k = 2 | k = 3 | k = 5 | k = 10 | k = 20 | k = 50 | k = 100 | k = 198 | k = 200 | k = 500 | k = 902 | k = 990 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| the newline after the response | 63% | 68% | 71% | 75% | 79% | 85% | 92% | 97% | 100% | – | – | – | – |
| control: the turn-end token after the response | 18% | 26% | 31% | 40% | 53% | 66% | 82% | 92% | 100% | – | – | – | – |
| control: the newline before the response | 11% | 16% | 21% | 28% | 40% | 53% | 73% | 89% | 100% | – | – | – | – |
| the newline after the question | 8% | 13% | 18% | 23% | 34% | 45% | 61% | 74% | – | 85% | 96% | – | 100% |
| the turn-start token after the question | 5% | 10% | 13% | 19% | 28% | 38% | 54% | 68% | – | 81% | 95% | – | 100% |
| the newline after `model` | 18% | 25% | 31% | 40% | 52% | 64% | 77% | 85% | – | 92% | 98% | – | 100% |
| the first newline after the self-report answer | 33% | 39% | 44% | 49% | 56% | 64% | 74% | 82% | – | 89% | 98% | 100% | – |
| the last newline after the self-report answer | 14% | 23% | 30% | 39% | 51% | 63% | 76% | 85% | – | 92% | 98% | 100% | – |
