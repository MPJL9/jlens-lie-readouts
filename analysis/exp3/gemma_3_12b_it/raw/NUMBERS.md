# Experiment 3: numbers behind the pictures (Gemma-3-12B, build split, in-sample)

Written by `scripts/exp3/pictures.py`. Every number is cross-validated in five folds with scenarios kept together.
*line* = AUROC of a straight-line split of lies against truths in the two drawn dimensions. *direction* = AUROC of the
lie-minus-truth direction in the full space. *pairs* = scenarios with both a lie and a truth in which the lie scores above
its truth. 0.50 is chance. Transcripts: 49 lies, 32 truths, 135 no-pressure truths, 179 unrelated chats.

## 1. Before the question, layer 29

| position | measure | AUROC (95% interval over scenarios) | pairs |
|---|---|---|---|
| the newline after the response | line, fit on unrelated chats | 0.47 (0.35 to 0.59) | 8 of 16 |
| the newline after the response | line, fit on pressured transcripts | 0.53 (0.39 to 0.64) | 6 of 16 |
| the newline after the response | direction, full space | 0.60 (0.48 to 0.71) | 8 of 16 |
| control: the turn-end token after the response | line, fit on unrelated chats | 0.48 (0.38 to 0.58) | 7 of 16 |
| control: the turn-end token after the response | line, fit on pressured transcripts | 0.48 (0.38 to 0.59) | 6 of 16 |
| control: the turn-end token after the response | direction, full space | 0.67 (0.57 to 0.76) | 12 of 16 |
| control: the newline before the response | line, fit on unrelated chats | 0.52 (0.41 to 0.64) | 3 of 16 (9 ties) |
| control: the newline before the response | line, fit on pressured transcripts | 0.53 (0.42 to 0.64) | 3 of 16 (9 ties) |
| control: the newline before the response | direction, full space | 0.58 (0.48 to 0.68) | 2 of 16 (9 ties) |

Along the direction (0 = midpoint between the two means of the other folds):

| position | missed lies on the truth side | other lies on the truth side | truths on the lie side |
|---|---|---|---|
| the newline after the response | 6 / 19 | 3 / 30 | 23 / 32 |
| control: the turn-end token after the response | 6 / 19 | 13 / 30 | 13 / 32 |
| control: the newline before the response | 5 / 19 | 12 / 30 | 16 / 32 |

## 2. Before the question, by layer

| position | measure | layer 17 | layer 23 | layer 29 | layer 35 | layer 40 |
|---|---|---|---|---|---|---|
| the newline after the response | line, fit on unrelated chats | 0.59 | 0.57 | 0.47 | 0.45 | 0.48 |
| the newline after the response | line, fit on pressured transcripts | 0.56 | 0.57 | 0.53 | 0.58 | 0.53 |
| the newline after the response | direction, full space | 0.58 | 0.61 | 0.60 | 0.58 | 0.62 |
| control: the turn-end token after the response | line, fit on unrelated chats | 0.61 | 0.52 | 0.48 | 0.63 | 0.47 |
| control: the turn-end token after the response | line, fit on pressured transcripts | 0.51 | 0.52 | 0.48 | 0.63 | 0.53 |
| control: the turn-end token after the response | direction, full space | 0.55 | 0.58 | 0.67 | 0.66 | 0.60 |
| control: the newline before the response | line, fit on unrelated chats | 0.57 | 0.58 | 0.52 | 0.50 | 0.53 |
| control: the newline before the response | line, fit on pressured transcripts | 0.61 | 0.58 | 0.53 | 0.46 | 0.47 |
| control: the newline before the response | direction, full space | 0.60 | 0.60 | 0.58 | 0.51 | 0.52 |

UMAP of the pressured transcripts (check; line AUROC for seeds 0, 1, 2): the newline after the response: 0.42, 0.53, 0.41; control: the turn-end token after the response: 0.54, 0.64, 0.57; control: the newline before the response: 0.49, 0.52, 0.49.

## 3. After the question, layer 29

Lies / truths in brackets. *deniers* = transcripts that answer No; the line is fitted among deniers.

**the newline after the question** (`preans_slot1`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.45 (49 / 32) | – | 0.75 (49 / 32) | – | 0.64, 0.68, 0.66 |
| Q2 | 0.61 (49 / 32) | – | 0.81 (49 / 32) | – | 0.67, 0.72, 0.71 |
| Q6 | 0.64 (49 / 32) | – | 0.71 (49 / 32) | – | 0.67, 0.70, 0.70 |
| Q7 | 0.67 (49 / 32) | 0.74 (16 / 11) | 0.72 (49 / 32) | 0.69 (16 / 11) | 0.70, 0.71, 0.69 |
| Q9 | 0.54 (49 / 32) | – | 0.66 (49 / 32) | – | 0.56, 0.60, 0.58 |

**the turn-start token after the question** (`preans_slot2`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.49 (49 / 32) | – | 0.42 (49 / 32) | – | 0.53, 0.77, 0.52 |
| Q2 | 0.56 (49 / 32) | – | 0.45 (49 / 32) | – | 0.52, 0.79, 0.52 |
| Q6 | 0.66 (49 / 32) | – | 0.63 (49 / 32) | – | 0.58, 0.78, 0.54 |
| Q7 | 0.53 (49 / 32) | 0.50 (16 / 11) | 0.48 (49 / 32) | 0.49 (16 / 11) | 0.52, 0.60, 0.53 |
| Q9 | 0.63 (49 / 32) | – | 0.60 (49 / 32) | – | 0.50, 0.83, 0.50 |

**the newline after `model`** (`preans_slot4`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.54 (49 / 32) | – | 0.46 (49 / 32) | – | 0.52, 0.50, 0.49 |
| Q2 | 0.53 (49 / 32) | – | 0.64 (49 / 32) | – | 0.67, 0.67, 0.67 |
| Q6 | 0.68 (49 / 32) | – | 0.72 (49 / 32) | – | 0.72, 0.72, 0.72 |
| Q7 | 0.60 (49 / 32) | 0.54 (16 / 11) | 0.60 (49 / 32) | 0.57 (16 / 11) | 0.61, 0.57, 0.49 |
| Q9 | 0.60 (49 / 32) | – | 0.63 (49 / 32) | – | 0.64, 0.64, 0.64 |

**the first newline after the self-report answer** (`postans_slot1`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.50 (41 / 25) | – | 0.48 (41 / 25) | – | 0.42, 0.72, 0.48 |
| Q2 | 0.50 (49 / 32) | – | 0.44 (49 / 32) | – | 0.37, 0.41, 0.39 |
| Q6 | 0.41 (49 / 32) | – | 0.41 (49 / 32) | – | 0.48, 0.50, 0.49 |
| Q7 | 0.52 (49 / 32) | 0.56 (16 / 11) | 0.51 (49 / 32) | 0.68 (16 / 11) | 0.46, 0.46, 0.45 |
| Q9 | 0.61 (49 / 32) | – | 0.61 (49 / 32) | – | 0.60, 0.57, 0.55 |

**the last newline after the self-report answer** (`postans_slot4`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.51 (41 / 25) | – | 0.37 (41 / 25) | – | 0.48, 0.48, 0.49 |
| Q2 | 0.45 (49 / 32) | – | 0.46 (49 / 32) | – | 0.45, 0.46, 0.42 |
| Q6 | 0.51 (49 / 32) | – | 0.58 (49 / 32) | – | 0.58, 0.58, 0.56 |
| Q7 | 0.57 (49 / 32) | 0.33 (16 / 11) | 0.39 (49 / 32) | 0.26 (16 / 11) | 0.41, 0.40, 0.42 |
| Q9 | 0.64 (49 / 32) | – | 0.60 (49 / 32) | – | 0.57, 0.56, 0.56 |

## 4. After the question, by layer (line AUROC; all, then deniers)

**the newline after the question** (`preans_slot1`)

| wording | fit | layer 17 | layer 23 | layer 29 | layer 35 | layer 40 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.52, – | 0.42, – | 0.45, – | 0.59, – | 0.55, – |
| Q1 | pressured | 0.52, – | 0.81, – | 0.75, – | 0.71, – | 0.71, – |
| Q2 | unrelated | 0.39, – | 0.59, – | 0.61, – | 0.51, – | 0.48, – |
| Q2 | pressured | 0.48, – | 0.75, – | 0.81, – | 0.69, – | 0.74, – |
| Q6 | unrelated | 0.46, – | 0.61, – | 0.64, – | 0.55, – | 0.49, – |
| Q6 | pressured | 0.48, – | 0.71, – | 0.71, – | 0.48, – | 0.57, – |
| Q7 | unrelated | 0.59, 0.56 | 0.61, 0.53 | 0.67, 0.74 | 0.72, 0.65 | 0.67, 0.55 |
| Q7 | pressured | 0.57, 0.48 | 0.67, 0.56 | 0.72, 0.69 | 0.66, 0.63 | 0.38, 0.43 |
| Q9 | unrelated | 0.49, – | 0.60, – | 0.54, – | 0.54, – | 0.63, – |
| Q9 | pressured | 0.55, – | 0.72, – | 0.66, – | 0.75, – | 0.75, – |

**the turn-start token after the question** (`preans_slot2`)

| wording | fit | layer 17 | layer 23 | layer 29 | layer 35 | layer 40 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.49, – | 0.47, – | 0.49, – | 0.52, – | 0.55, – |
| Q1 | pressured | 0.49, – | 0.74, – | 0.42, – | 0.43, – | 0.47, – |
| Q2 | unrelated | 0.52, – | 0.53, – | 0.56, – | 0.59, – | 0.63, – |
| Q2 | pressured | 0.55, – | 0.82, – | 0.45, – | 0.60, – | 0.57, – |
| Q6 | unrelated | 0.49, – | 0.53, – | 0.66, – | 0.63, – | 0.62, – |
| Q6 | pressured | 0.47, – | 0.77, – | 0.63, – | 0.67, – | 0.50, – |
| Q7 | unrelated | 0.52, 0.31 | 0.55, 0.56 | 0.53, 0.50 | 0.51, 0.32 | 0.57, 0.44 |
| Q7 | pressured | 0.47, 0.37 | 0.80, 0.76 | 0.48, 0.49 | 0.61, 0.39 | 0.60, 0.45 |
| Q9 | unrelated | 0.51, – | 0.71, – | 0.63, – | 0.68, – | 0.53, – |
| Q9 | pressured | 0.52, – | 0.84, – | 0.60, – | 0.77, – | 0.64, – |

**the newline after `model`** (`preans_slot4`)

| wording | fit | layer 17 | layer 23 | layer 29 | layer 35 | layer 40 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.40, – | 0.57, – | 0.54, – | 0.52, – | 0.53, – |
| Q1 | pressured | 0.48, – | 0.56, – | 0.46, – | 0.53, – | 0.53, – |
| Q2 | unrelated | 0.39, – | 0.46, – | 0.53, – | 0.56, – | 0.56, – |
| Q2 | pressured | 0.44, – | 0.49, – | 0.64, – | 0.59, – | 0.62, – |
| Q6 | unrelated | 0.38, – | 0.48, – | 0.68, – | 0.74, – | 0.73, – |
| Q6 | pressured | 0.43, – | 0.52, – | 0.72, – | 0.75, – | 0.74, – |
| Q7 | unrelated | 0.46, 0.25 | 0.46, 0.59 | 0.60, 0.54 | 0.66, 0.55 | 0.59, 0.42 |
| Q7 | pressured | 0.48, 0.35 | 0.44, 0.52 | 0.60, 0.57 | 0.65, 0.63 | 0.60, 0.46 |
| Q9 | unrelated | 0.42, – | 0.48, – | 0.60, – | 0.71, – | 0.64, – |
| Q9 | pressured | 0.47, – | 0.50, – | 0.63, – | 0.71, – | 0.63, – |

**the first newline after the self-report answer** (`postans_slot1`)

| wording | fit | layer 17 | layer 23 | layer 29 | layer 35 | layer 40 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.53, – | 0.27, – | 0.50, – | 0.47, – | 0.42, – |
| Q1 | pressured | 0.54, – | 0.32, – | 0.48, – | 0.49, – | 0.47, – |
| Q2 | unrelated | 0.45, – | 0.51, – | 0.50, – | 0.46, – | 0.41, – |
| Q2 | pressured | 0.47, – | 0.53, – | 0.44, – | 0.43, – | 0.43, – |
| Q6 | unrelated | 0.62, – | 0.64, – | 0.41, – | 0.38, – | 0.40, – |
| Q6 | pressured | 0.62, – | 0.66, – | 0.41, – | 0.40, – | 0.42, – |
| Q7 | unrelated | 0.36, 0.66 | 0.45, 0.47 | 0.52, 0.56 | 0.47, 0.56 | 0.45, 0.37 |
| Q7 | pressured | 0.46, 0.74 | 0.39, 0.72 | 0.51, 0.68 | 0.47, 0.45 | 0.49, 0.30 |
| Q9 | unrelated | 0.52, – | 0.46, – | 0.61, – | 0.65, – | 0.66, – |
| Q9 | pressured | 0.54, – | 0.51, – | 0.61, – | 0.64, – | 0.66, – |

**the last newline after the self-report answer** (`postans_slot4`)

| wording | fit | layer 17 | layer 23 | layer 29 | layer 35 | layer 40 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.55, – | 0.60, – | 0.51, – | 0.58, – | 0.56, – |
| Q1 | pressured | 0.55, – | 0.57, – | 0.37, – | 0.54, – | 0.54, – |
| Q2 | unrelated | 0.52, – | 0.54, – | 0.45, – | 0.56, – | 0.57, – |
| Q2 | pressured | 0.58, – | 0.52, – | 0.46, – | 0.48, – | 0.43, – |
| Q6 | unrelated | 0.50, – | 0.61, – | 0.51, – | 0.45, – | 0.48, – |
| Q6 | pressured | 0.60, – | 0.59, – | 0.58, – | 0.58, – | 0.57, – |
| Q7 | unrelated | 0.53, 0.21 | 0.46, 0.51 | 0.57, 0.33 | 0.60, 0.53 | 0.60, 0.40 |
| Q7 | pressured | 0.52, 0.27 | 0.44, 0.64 | 0.39, 0.26 | 0.54, 0.49 | 0.54, 0.39 |
| Q9 | unrelated | 0.46, – | 0.48, – | 0.64, – | 0.62, – | 0.62, – |
| Q9 | pressured | 0.52, – | 0.55, – | 0.60, – | 0.58, – | 0.56, – |

## 5. Vector lengths, layer 29

Mean length of the residual vectors and its spread (standard deviation / mean). A small spread means that a fit on
vectors scaled to length 1 (the cosine view) would show nearly the same picture as the PCA drawn here. After the
question: the mean over the five wordings.

| position | pressured: mean length | pressured: spread | unrelated: mean length | unrelated: spread |
|---|---|---|---|---|
| the newline after the response | 54454 | 9.0% | 56809 | 43.1% |
| control: the turn-end token after the response | 60740 | 3.1% | 60968 | 3.6% |
| control: the newline before the response | 79414 | 7.8% | 77343 | 7.9% |
| the newline after the question | 61819 | 5.5% | 61429 | 4.5% |
| the turn-start token after the question | 57837 | 6.9% | 59120 | 6.1% |
| the newline after `model` | 74270 | 4.0% | 75186 | 2.2% |
| the first newline after the self-report answer | 55125 | 7.5% | 52286 | 5.1% |
| the last newline after the self-report answer | 63880 | 4.9% | 61183 | 3.9% |

## 6. Lies against truths within the first k principal components of the unrelated chats, layer 29

AUROC of the lie-minus-truth direction fitted within the first k components (on other scenarios than the one scored).
*full space* = the same direction with no restriction. After the question: the mean over the wordings; *deniers* over the
wordings with 10 or more lying and 10 or more truthful deniers. The last k is all components when there are 1,000 or fewer.

| position | k = 1 | k = 2 | k = 3 | k = 5 | k = 10 | k = 20 | k = 50 | k = 100 | k = 178 | k = 200 | k = 500 | k = 814 | k = 890 | full space |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| the newline after the response | 0.39 | 0.46 | 0.42 | 0.42 | 0.42 | 0.43 | 0.44 | 0.45 | 0.46 | – | – | – | – | 0.60 |
| control: the turn-end token after the response | 0.49 | 0.49 | 0.48 | 0.52 | 0.55 | 0.56 | 0.57 | 0.59 | 0.60 | – | – | – | – | 0.67 |
| control: the newline before the response | 0.59 | 0.58 | 0.59 | 0.59 | 0.59 | 0.58 | 0.58 | 0.58 | 0.58 | – | – | – | – | 0.58 |
| the newline after the question | 0.56 | 0.56 | 0.57 | 0.59 | 0.62 | 0.67 | 0.71 | 0.72 | – | 0.74 | 0.76 | – | 0.77 | 0.80 |
| the newline after the question, deniers | 0.72 | 0.72 | 0.72 | 0.73 | 0.74 | 0.76 | 0.76 | 0.79 | – | 0.80 | 0.79 | – | 0.79 | 0.81 |
| the turn-start token after the question | 0.54 | 0.54 | 0.54 | 0.56 | 0.57 | 0.62 | 0.65 | 0.66 | – | 0.68 | 0.69 | – | 0.71 | 0.74 |
| the turn-start token after the question, deniers | 0.64 | 0.63 | 0.63 | 0.61 | 0.62 | 0.62 | 0.61 | 0.60 | – | 0.61 | 0.62 | – | 0.63 | 0.65 |
| the newline after `model` | 0.52 | 0.61 | 0.61 | 0.64 | 0.67 | 0.67 | 0.68 | 0.69 | – | 0.70 | 0.70 | – | 0.70 | 0.71 |
| the newline after `model`, deniers | 0.71 | 0.67 | 0.67 | 0.66 | 0.65 | 0.65 | 0.66 | 0.67 | – | 0.68 | 0.68 | – | 0.68 | 0.68 |
| the first newline after the self-report answer | 0.51 | 0.53 | 0.53 | 0.53 | 0.55 | 0.56 | 0.56 | 0.56 | – | 0.58 | 0.59 | 0.59 | – | 0.61 |
| the first newline after the self-report answer, deniers | 0.51 | 0.55 | 0.55 | 0.56 | 0.59 | 0.57 | 0.62 | 0.65 | – | 0.69 | 0.72 | 0.73 | – | 0.78 |
| the last newline after the self-report answer | 0.48 | 0.50 | 0.50 | 0.51 | 0.53 | 0.54 | 0.55 | 0.56 | – | 0.57 | 0.59 | 0.59 | – | 0.61 |
| the last newline after the self-report answer, deniers | 0.27 | 0.27 | 0.27 | 0.26 | 0.23 | 0.24 | 0.27 | 0.31 | – | 0.32 | 0.37 | 0.36 | – | 0.44 |

Share of the unrelated chats' variance held by the first k components:

| position | k = 1 | k = 2 | k = 3 | k = 5 | k = 10 | k = 20 | k = 50 | k = 100 | k = 178 | k = 200 | k = 500 | k = 814 | k = 890 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| the newline after the response | 90% | 94% | 96% | 97% | 97% | 98% | 99% | 100% | 100% | – | – | – | – |
| control: the turn-end token after the response | 29% | 43% | 50% | 58% | 68% | 78% | 89% | 96% | 100% | – | – | – | – |
| control: the newline before the response | 41% | 46% | 50% | 56% | 64% | 73% | 86% | 95% | 100% | – | – | – | – |
| the newline after the question | 23% | 29% | 33% | 38% | 47% | 58% | 71% | 82% | – | 91% | 98% | – | 100% |
| the turn-start token after the question | 27% | 32% | 35% | 41% | 49% | 57% | 70% | 79% | – | 89% | 98% | – | 100% |
| the newline after `model` | 31% | 43% | 49% | 57% | 68% | 76% | 86% | 92% | – | 96% | 99% | – | 100% |
| the first newline after the self-report answer | 36% | 50% | 56% | 62% | 70% | 76% | 85% | 92% | – | 96% | 100% | 100% | – |
| the last newline after the self-report answer | 45% | 57% | 61% | 67% | 74% | 81% | 88% | 93% | – | 97% | 100% | 100% | – |
