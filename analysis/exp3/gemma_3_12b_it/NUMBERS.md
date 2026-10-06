# Experiment 3: numbers behind the pictures (Gemma-3-12B, build split, in-sample)

Written by `scripts/exp3/pictures.py`. Every number is cross-validated in five folds with scenarios kept together.
*line* = AUROC of a straight-line split of lies against truths in the two drawn dimensions. *direction* = AUROC of the
lie-minus-truth direction in the full space. *pairs* = scenarios with both a lie and a truth in which the lie scores above
its truth. 0.50 is chance. Transcripts: 49 lies, 32 truths, 135 no-pressure truths, 179 unrelated chats.

**Scaled.** Before every fit, each dimension of the residual stream is divided by its spread (standard deviation) in the
unrelated chats at the same position and layer (after the question: the spread within each wording). The lengths in
Section 5 are those of the scaled vectors.

## 1. Before the question, layer 29

| position | measure | AUROC (95% interval over scenarios) | pairs |
|---|---|---|---|
| the newline after the response | line, fit on unrelated chats | 0.45 (0.35 to 0.58) | 7 of 16 |
| the newline after the response | line, fit on pressured transcripts | 0.69 (0.59 to 0.78) | 8 of 16 |
| the newline after the response | direction, full space | 0.71 (0.61 to 0.80) | 6 of 16 |
| control: the turn-end token after the response | line, fit on unrelated chats | 0.61 (0.51 to 0.69) | 9 of 16 |
| control: the turn-end token after the response | line, fit on pressured transcripts | 0.64 (0.53 to 0.72) | 10 of 16 |
| control: the turn-end token after the response | direction, full space | 0.67 (0.58 to 0.76) | 14 of 16 |
| control: the newline before the response | line, fit on unrelated chats | 0.46 (0.36 to 0.56) | 5 of 16 (9 ties) |
| control: the newline before the response | line, fit on pressured transcripts | 0.48 (0.38 to 0.60) | 3 of 16 (9 ties) |
| control: the newline before the response | direction, full space | 0.58 (0.47 to 0.67) | 4 of 16 (9 ties) |

Along the direction (0 = midpoint between the two means of the other folds):

| position | missed lies on the truth side | other lies on the truth side | truths on the lie side |
|---|---|---|---|
| the newline after the response | 11 / 19 | 6 / 30 | 11 / 32 |
| control: the turn-end token after the response | 7 / 19 | 11 / 30 | 13 / 32 |
| control: the newline before the response | 6 / 19 | 11 / 30 | 17 / 32 |

## 2. Before the question, by layer

| position | measure | layer 17 | layer 23 | layer 29 | layer 35 | layer 40 |
|---|---|---|---|---|---|---|
| the newline after the response | line, fit on unrelated chats | 0.57 | 0.53 | 0.45 | 0.47 | 0.49 |
| the newline after the response | line, fit on pressured transcripts | 0.52 | 0.68 | 0.69 | 0.67 | 0.55 |
| the newline after the response | direction, full space | 0.68 | 0.82 | 0.71 | 0.67 | 0.63 |
| control: the turn-end token after the response | line, fit on unrelated chats | 0.60 | 0.60 | 0.61 | 0.57 | 0.54 |
| control: the turn-end token after the response | line, fit on pressured transcripts | 0.47 | 0.61 | 0.64 | 0.65 | 0.62 |
| control: the turn-end token after the response | direction, full space | 0.61 | 0.67 | 0.67 | 0.66 | 0.64 |
| control: the newline before the response | line, fit on unrelated chats | 0.52 | 0.56 | 0.46 | 0.50 | 0.56 |
| control: the newline before the response | line, fit on pressured transcripts | 0.60 | 0.55 | 0.48 | 0.47 | 0.47 |
| control: the newline before the response | direction, full space | 0.63 | 0.60 | 0.58 | 0.53 | 0.55 |

UMAP of the pressured transcripts (check; line AUROC for seeds 0, 1, 2): the newline after the response: 0.56, 0.57, 0.44; control: the turn-end token after the response: 0.62, 0.65, 0.62; control: the newline before the response: 0.46, 0.51, 0.50.

## 3. After the question, layer 29

Lies / truths in brackets. *deniers* = transcripts that answer No; the line is fitted among deniers.

**the newline after the question** (`preans_slot1`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.58 (49 / 32) | – | 0.84 (49 / 32) | – | 0.81, 0.80, 0.76 |
| Q2 | 0.60 (49 / 32) | – | 0.84 (49 / 32) | – | 0.81, 0.81, 0.77 |
| Q6 | 0.53 (49 / 32) | – | 0.80 (49 / 32) | – | 0.80, 0.80, 0.79 |
| Q7 | 0.63 (49 / 32) | 0.66 (16 / 11) | 0.84 (49 / 32) | 0.72 (16 / 11) | 0.59, 0.57, 0.65 |
| Q9 | 0.57 (49 / 32) | – | 0.85 (49 / 32) | – | 0.80, 0.79, 0.76 |

**the turn-start token after the question** (`preans_slot2`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.58 (49 / 32) | – | 0.74 (49 / 32) | – | 0.77, 0.76, 0.77 |
| Q2 | 0.60 (49 / 32) | – | 0.78 (49 / 32) | – | 0.79, 0.78, 0.78 |
| Q6 | 0.60 (49 / 32) | – | 0.78 (49 / 32) | – | 0.80, 0.78, 0.79 |
| Q7 | 0.59 (49 / 32) | 0.60 (16 / 11) | 0.72 (49 / 32) | 0.54 (16 / 11) | 0.72, 0.70, 0.72 |
| Q9 | 0.54 (49 / 32) | – | 0.80 (49 / 32) | – | 0.81, 0.75, 0.76 |

**the newline after `model`** (`preans_slot4`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.44 (49 / 32) | – | 0.50 (49 / 32) | – | 0.49, 0.47, 0.49 |
| Q2 | 0.52 (49 / 32) | – | 0.71 (49 / 32) | – | 0.77, 0.75, 0.75 |
| Q6 | 0.68 (49 / 32) | – | 0.72 (49 / 32) | – | 0.77, 0.77, 0.78 |
| Q7 | 0.67 (49 / 32) | 0.63 (16 / 11) | 0.52 (49 / 32) | 0.41 (16 / 11) | 0.59, 0.55, 0.57 |
| Q9 | 0.69 (49 / 32) | – | 0.68 (49 / 32) | – | 0.74, 0.73, 0.73 |

**the first newline after the self-report answer** (`postans_slot1`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.57 (41 / 25) | – | 0.48 (41 / 25) | – | 0.60, 0.59, 0.61 |
| Q2 | 0.57 (49 / 32) | – | 0.43 (49 / 32) | – | 0.39, 0.41, 0.40 |
| Q6 | 0.56 (49 / 32) | – | 0.59 (49 / 32) | – | 0.59, 0.57, 0.60 |
| Q7 | 0.51 (49 / 32) | 0.48 (16 / 11) | 0.49 (49 / 32) | 0.74 (16 / 11) | 0.41, 0.41, 0.41 |
| Q9 | 0.65 (49 / 32) | – | 0.64 (49 / 32) | – | 0.53, 0.51, 0.50 |

**the last newline after the self-report answer** (`postans_slot4`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.62 (41 / 25) | – | 0.51 (41 / 25) | – | 0.43, 0.45, 0.41 |
| Q2 | 0.57 (49 / 32) | – | 0.59 (49 / 32) | – | 0.50, 0.48, 0.49 |
| Q6 | 0.59 (49 / 32) | – | 0.62 (49 / 32) | – | 0.62, 0.65, 0.62 |
| Q7 | 0.63 (49 / 32) | 0.54 (16 / 11) | 0.64 (49 / 32) | 0.56 (16 / 11) | 0.54, 0.43, 0.52 |
| Q9 | 0.55 (49 / 32) | – | 0.64 (49 / 32) | – | 0.53, 0.54, 0.54 |

## 4. After the question, by layer (line AUROC; all, then deniers)

**the newline after the question** (`preans_slot1`)

| wording | fit | layer 17 | layer 23 | layer 29 | layer 35 | layer 40 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.43, – | 0.46, – | 0.58, – | 0.66, – | 0.68, – |
| Q1 | pressured | 0.47, – | 0.88, – | 0.84, – | 0.80, – | 0.79, – |
| Q2 | unrelated | 0.43, – | 0.57, – | 0.60, – | 0.60, – | 0.64, – |
| Q2 | pressured | 0.50, – | 0.85, – | 0.84, – | 0.80, – | 0.77, – |
| Q6 | unrelated | 0.52, – | 0.35, – | 0.53, – | 0.53, – | 0.50, – |
| Q6 | pressured | 0.47, – | 0.83, – | 0.80, – | 0.67, – | 0.68, – |
| Q7 | unrelated | 0.54, 0.48 | 0.56, 0.53 | 0.63, 0.66 | 0.71, 0.55 | 0.68, 0.64 |
| Q7 | pressured | 0.55, 0.50 | 0.75, 0.73 | 0.84, 0.72 | 0.57, 0.36 | 0.60, 0.55 |
| Q9 | unrelated | 0.47, – | 0.56, – | 0.57, – | 0.58, – | 0.58, – |
| Q9 | pressured | 0.56, – | 0.84, – | 0.85, – | 0.77, – | 0.77, – |

**the turn-start token after the question** (`preans_slot2`)

| wording | fit | layer 17 | layer 23 | layer 29 | layer 35 | layer 40 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.40, – | 0.51, – | 0.58, – | 0.64, – | 0.67, – |
| Q1 | pressured | 0.47, – | 0.81, – | 0.74, – | 0.62, – | 0.56, – |
| Q2 | unrelated | 0.38, – | 0.58, – | 0.60, – | 0.70, – | 0.70, – |
| Q2 | pressured | 0.46, – | 0.87, – | 0.78, – | 0.68, – | 0.65, – |
| Q6 | unrelated | 0.49, – | 0.68, – | 0.60, – | 0.66, – | 0.66, – |
| Q6 | pressured | 0.49, – | 0.85, – | 0.78, – | 0.69, – | 0.62, – |
| Q7 | unrelated | 0.52, 0.45 | 0.56, 0.57 | 0.59, 0.60 | 0.62, 0.53 | 0.60, 0.53 |
| Q7 | pressured | 0.48, 0.34 | 0.81, 0.79 | 0.72, 0.54 | 0.62, 0.41 | 0.60, 0.41 |
| Q9 | unrelated | 0.44, – | 0.42, – | 0.54, – | 0.52, – | 0.53, – |
| Q9 | pressured | 0.46, – | 0.85, – | 0.80, – | 0.66, – | 0.57, – |

**the newline after `model`** (`preans_slot4`)

| wording | fit | layer 17 | layer 23 | layer 29 | layer 35 | layer 40 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.49, – | 0.56, – | 0.44, – | 0.49, – | 0.50, – |
| Q1 | pressured | 0.48, – | 0.53, – | 0.50, – | 0.54, – | 0.52, – |
| Q2 | unrelated | 0.48, – | 0.52, – | 0.52, – | 0.62, – | 0.62, – |
| Q2 | pressured | 0.50, – | 0.54, – | 0.71, – | 0.67, – | 0.64, – |
| Q6 | unrelated | 0.50, – | 0.48, – | 0.68, – | 0.71, – | 0.70, – |
| Q6 | pressured | 0.48, – | 0.59, – | 0.72, – | 0.73, – | 0.71, – |
| Q7 | unrelated | 0.52, 0.25 | 0.56, 0.55 | 0.67, 0.63 | 0.64, 0.60 | 0.68, 0.61 |
| Q7 | pressured | 0.49, 0.32 | 0.54, 0.67 | 0.52, 0.41 | 0.49, 0.22 | 0.60, 0.70 |
| Q9 | unrelated | 0.54, – | 0.58, – | 0.69, – | 0.63, – | 0.62, – |
| Q9 | pressured | 0.48, – | 0.58, – | 0.68, – | 0.60, – | 0.59, – |

**the first newline after the self-report answer** (`postans_slot1`)

| wording | fit | layer 17 | layer 23 | layer 29 | layer 35 | layer 40 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.38, – | 0.50, – | 0.57, – | 0.63, – | 0.63, – |
| Q1 | pressured | 0.34, – | 0.48, – | 0.48, – | 0.47, – | 0.48, – |
| Q2 | unrelated | 0.45, – | 0.44, – | 0.57, – | 0.57, – | 0.56, – |
| Q2 | pressured | 0.53, – | 0.52, – | 0.43, – | 0.52, – | 0.47, – |
| Q6 | unrelated | 0.64, – | 0.68, – | 0.56, – | 0.54, – | 0.56, – |
| Q6 | pressured | 0.69, – | 0.68, – | 0.59, – | 0.62, – | 0.56, – |
| Q7 | unrelated | 0.34, 0.73 | 0.55, 0.43 | 0.51, 0.48 | 0.43, 0.43 | 0.44, 0.42 |
| Q7 | pressured | 0.37, 0.38 | 0.37, 0.75 | 0.49, 0.74 | 0.50, 0.59 | 0.50, 0.41 |
| Q9 | unrelated | 0.55, – | 0.46, – | 0.65, – | 0.65, – | 0.62, – |
| Q9 | pressured | 0.56, – | 0.46, – | 0.64, – | 0.63, – | 0.59, – |

**the last newline after the self-report answer** (`postans_slot4`)

| wording | fit | layer 17 | layer 23 | layer 29 | layer 35 | layer 40 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.51, – | 0.33, – | 0.62, – | 0.63, – | 0.57, – |
| Q1 | pressured | 0.56, – | 0.54, – | 0.51, – | 0.53, – | 0.45, – |
| Q2 | unrelated | 0.64, – | 0.42, – | 0.57, – | 0.57, – | 0.57, – |
| Q2 | pressured | 0.59, – | 0.56, – | 0.59, – | 0.59, – | 0.59, – |
| Q6 | unrelated | 0.71, – | 0.59, – | 0.59, – | 0.45, – | 0.45, – |
| Q6 | pressured | 0.60, – | 0.67, – | 0.62, – | 0.59, – | 0.60, – |
| Q7 | unrelated | 0.61, 0.39 | 0.49, 0.27 | 0.63, 0.54 | 0.59, 0.20 | 0.58, 0.28 |
| Q7 | pressured | 0.52, 0.52 | 0.53, 0.68 | 0.64, 0.56 | 0.63, 0.51 | 0.64, 0.52 |
| Q9 | unrelated | 0.63, – | 0.44, – | 0.55, – | 0.51, – | 0.44, – |
| Q9 | pressured | 0.56, – | 0.52, – | 0.64, – | 0.63, – | 0.64, – |

## 5. Vector lengths, layer 29

Mean length of the residual vectors and its spread (standard deviation / mean). A small spread means that a fit on
vectors scaled to length 1 (the cosine view) would show nearly the same picture as the PCA drawn here. After the
question: the mean over the five wordings.

| position | pressured: mean length | pressured: spread | unrelated: mean length | unrelated: spread |
|---|---|---|---|---|
| the newline after the response | 80 | 10.9% | 77 | 16.8% |
| control: the turn-end token after the response | 165 | 2.5% | 166 | 2.9% |
| control: the newline before the response | 82 | 7.3% | 83 | 6.3% |
| the newline after the question | 111 | 5.4% | 109 | 5.0% |
| the turn-start token after the question | 91 | 6.6% | 90 | 5.5% |
| the newline after `model` | 237 | 3.4% | 241 | 2.3% |
| the first newline after the self-report answer | 138 | 18.5% | 134 | 5.3% |
| the last newline after the self-report answer | 186 | 4.3% | 185 | 3.5% |

## 6. Lies against truths within the first k principal components of the unrelated chats, layer 29

AUROC of the lie-minus-truth direction fitted within the first k components (on other scenarios than the one scored).
*full space* = the same direction with no restriction. After the question: the mean over the wordings; *deniers* over the
wordings with 10 or more lying and 10 or more truthful deniers. The last k is all components when there are 1,000 or fewer.

| position | k = 1 | k = 2 | k = 3 | k = 5 | k = 10 | k = 20 | k = 50 | k = 100 | k = 178 | k = 200 | k = 500 | k = 814 | k = 890 | full space |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| the newline after the response | 0.45 | 0.45 | 0.43 | 0.50 | 0.52 | 0.54 | 0.55 | 0.57 | 0.59 | – | – | – | – | 0.71 |
| control: the turn-end token after the response | 0.44 | 0.59 | 0.58 | 0.58 | 0.61 | 0.62 | 0.62 | 0.62 | 0.64 | – | – | – | – | 0.67 |
| control: the newline before the response | 0.55 | 0.55 | 0.55 | 0.54 | 0.54 | 0.55 | 0.54 | 0.54 | 0.54 | – | – | – | – | 0.58 |
| the newline after the question | 0.53 | 0.58 | 0.62 | 0.64 | 0.70 | 0.78 | 0.80 | 0.81 | – | 0.82 | 0.83 | – | 0.84 | 0.85 |
| the newline after the question, deniers | 0.70 | 0.71 | 0.82 | 0.70 | 0.74 | 0.69 | 0.68 | 0.70 | – | 0.73 | 0.77 | – | 0.77 | 0.77 |
| the turn-start token after the question | 0.57 | 0.60 | 0.61 | 0.63 | 0.64 | 0.77 | 0.79 | 0.80 | – | 0.82 | 0.83 | – | 0.84 | 0.86 |
| the turn-start token after the question, deniers | 0.58 | 0.63 | 0.64 | 0.59 | 0.60 | 0.64 | 0.71 | 0.70 | – | 0.71 | 0.70 | – | 0.69 | 0.70 |
| the newline after `model` | 0.56 | 0.62 | 0.68 | 0.70 | 0.71 | 0.72 | 0.73 | 0.74 | – | 0.74 | 0.75 | – | 0.75 | 0.76 |
| the newline after `model`, deniers | 0.25 | 0.68 | 0.70 | 0.68 | 0.68 | 0.66 | 0.67 | 0.69 | – | 0.70 | 0.72 | – | 0.72 | 0.74 |
| the first newline after the self-report answer | 0.54 | 0.56 | 0.57 | 0.59 | 0.60 | 0.60 | 0.60 | 0.61 | – | 0.63 | 0.63 | 0.64 | – | 0.66 |
| the first newline after the self-report answer, deniers | 0.64 | 0.60 | 0.60 | 0.61 | 0.75 | 0.55 | 0.61 | 0.73 | – | 0.79 | 0.82 | 0.83 | – | 0.87 |
| the last newline after the self-report answer | 0.60 | 0.58 | 0.59 | 0.58 | 0.61 | 0.62 | 0.64 | 0.63 | – | 0.65 | 0.66 | 0.66 | – | 0.67 |
| the last newline after the self-report answer, deniers | 0.63 | 0.54 | 0.51 | 0.53 | 0.56 | 0.55 | 0.65 | 0.68 | – | 0.68 | 0.70 | 0.69 | – | 0.72 |

Share of the unrelated chats' variance held by the first k components:

| position | k = 1 | k = 2 | k = 3 | k = 5 | k = 10 | k = 20 | k = 50 | k = 100 | k = 178 | k = 200 | k = 500 | k = 814 | k = 890 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| the newline after the response | 23% | 33% | 38% | 44% | 53% | 64% | 80% | 94% | 100% | – | – | – | – |
| control: the turn-end token after the response | 17% | 28% | 36% | 45% | 58% | 70% | 85% | 95% | 100% | – | – | – | – |
| control: the newline before the response | 12% | 18% | 22% | 30% | 43% | 56% | 76% | 92% | 100% | – | – | – | – |
| the newline after the question | 7% | 12% | 16% | 22% | 32% | 44% | 61% | 74% | – | 87% | 98% | – | 100% |
| the turn-start token after the question | 6% | 10% | 14% | 20% | 29% | 40% | 57% | 70% | – | 83% | 97% | – | 100% |
| the newline after `model` | 18% | 27% | 33% | 42% | 54% | 66% | 79% | 87% | – | 94% | 99% | – | 100% |
| the first newline after the self-report answer | 19% | 28% | 33% | 41% | 51% | 61% | 75% | 86% | – | 94% | 99% | 100% | – |
| the last newline after the self-report answer | 23% | 31% | 37% | 44% | 55% | 66% | 79% | 87% | – | 94% | 99% | 100% | – |
