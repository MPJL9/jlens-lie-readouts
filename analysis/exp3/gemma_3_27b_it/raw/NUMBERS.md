# Experiment 3: numbers behind the pictures (Gemma-3-27B, build split, in-sample)

Written by `scripts/exp3/pictures.py`. Every number is cross-validated in five folds with scenarios kept together.
*line* = AUROC of a straight-line split of lies against truths in the two drawn dimensions. *direction* = AUROC of the
lie-minus-truth direction in the full space. *pairs* = scenarios with both a lie and a truth in which the lie scores above
its truth. 0.50 is chance. Transcripts: 58 lies, 30 truths, 133 no-pressure truths, 199 unrelated chats.

## 1. Before the question, layer 39

| position | measure | AUROC (95% interval over scenarios) | pairs |
|---|---|---|---|
| the newline after the response | line, fit on unrelated chats | 0.53 (0.41 to 0.65) | 8 of 11 |
| the newline after the response | line, fit on pressured transcripts | 0.52 (0.41 to 0.65) | 8 of 11 |
| the newline after the response | direction, full space | 0.54 (0.43 to 0.67) | 8 of 11 |
| control: the turn-end token after the response | line, fit on unrelated chats | 0.48 (0.37 to 0.60) | 6 of 11 |
| control: the turn-end token after the response | line, fit on pressured transcripts | 0.58 (0.46 to 0.70) | 4 of 11 |
| control: the turn-end token after the response | direction, full space | 0.65 (0.53 to 0.76) | 8 of 11 |
| control: the newline before the response | line, fit on unrelated chats | 0.51 (0.40 to 0.62) | 0 of 11 (11 ties) |
| control: the newline before the response | line, fit on pressured transcripts | 0.54 (0.44 to 0.66) | 0 of 11 (11 ties) |
| control: the newline before the response | direction, full space | 0.57 (0.46 to 0.68) | 0 of 11 (11 ties) |

Along the direction (0 = midpoint between the two means of the other folds):

| position | missed lies on the truth side | other lies on the truth side | truths on the lie side |
|---|---|---|---|
| the newline after the response | 10 / 34 | 8 / 24 | 17 / 30 |
| control: the turn-end token after the response | 7 / 34 | 7 / 24 | 17 / 30 |
| control: the newline before the response | 12 / 34 | 8 / 24 | 17 / 30 |

## 2. Before the question, by layer

| position | measure | layer 27 | layer 33 | layer 39 | layer 46 | layer 52 |
|---|---|---|---|---|---|---|
| the newline after the response | line, fit on unrelated chats | 0.47 | 0.37 | 0.53 | 0.53 | 0.53 |
| the newline after the response | line, fit on pressured transcripts | 0.53 | 0.41 | 0.52 | 0.52 | 0.52 |
| the newline after the response | direction, full space | 0.68 | 0.49 | 0.54 | 0.54 | 0.52 |
| control: the turn-end token after the response | line, fit on unrelated chats | 0.50 | 0.44 | 0.48 | 0.53 | 0.52 |
| control: the turn-end token after the response | line, fit on pressured transcripts | 0.50 | 0.53 | 0.58 | 0.59 | 0.57 |
| control: the turn-end token after the response | direction, full space | 0.58 | 0.65 | 0.65 | 0.66 | 0.64 |
| control: the newline before the response | line, fit on unrelated chats | 0.49 | 0.49 | 0.51 | 0.52 | 0.52 |
| control: the newline before the response | line, fit on pressured transcripts | 0.52 | 0.51 | 0.54 | 0.53 | 0.54 |
| control: the newline before the response | direction, full space | 0.54 | 0.55 | 0.57 | 0.57 | 0.57 |

UMAP of the pressured transcripts (check; line AUROC for seeds 0, 1, 2): the newline after the response: 0.52, 0.55, 0.53; control: the turn-end token after the response: 0.58, 0.61, 0.63; control: the newline before the response: 0.52, 0.45, 0.59.

## 3. After the question, layer 39

Lies / truths in brackets. *deniers* = transcripts that answer No; the line is fitted among deniers.

**the newline after the question** (`preans_slot1`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.65 (58 / 30) | – | 0.74 (58 / 30) | – | 0.73, 0.74, 0.74 |
| Q2 | 0.63 (58 / 30) | – | 0.83 (58 / 30) | – | 0.73, 0.75, 0.73 |
| Q6 | 0.54 (58 / 30) | – | 0.74 (58 / 30) | – | 0.71, 0.72, 0.71 |
| Q7 | 0.69 (58 / 30) | 0.61 (16 / 12) | 0.66 (58 / 30) | 0.57 (16 / 12) | 0.55, 0.56, 0.61 |
| Q9 | 0.57 (58 / 30) | – | 0.60 (58 / 30) | – | 0.61, 0.68, 0.63 |

**the turn-start token after the question** (`preans_slot2`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.54 (58 / 30) | – | 0.55 (58 / 30) | – | 0.53, 0.53, 0.54 |
| Q2 | 0.58 (58 / 30) | – | 0.55 (58 / 30) | – | 0.54, 0.52, 0.54 |
| Q6 | 0.76 (58 / 30) | – | 0.56 (58 / 30) | – | 0.62, 0.59, 0.61 |
| Q7 | 0.62 (58 / 30) | 0.50 (16 / 12) | 0.53 (58 / 30) | 0.69 (16 / 12) | 0.54, 0.52, 0.57 |
| Q9 | 0.59 (58 / 30) | – | 0.51 (58 / 30) | – | 0.46, 0.54, 0.51 |

**the newline after `model`** (`preans_slot4`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.44 (58 / 30) | – | 0.48 (58 / 30) | – | 0.55, 0.51, 0.53 |
| Q2 | 0.43 (58 / 30) | – | 0.59 (58 / 30) | – | 0.63, 0.56, 0.60 |
| Q6 | 0.37 (58 / 30) | – | 0.62 (58 / 30) | – | 0.63, 0.58, 0.63 |
| Q7 | 0.47 (58 / 30) | 0.54 (16 / 12) | 0.57 (58 / 30) | 0.50 (16 / 12) | 0.54, 0.53, 0.53 |
| Q9 | 0.60 (58 / 30) | – | 0.63 (58 / 30) | – | 0.65, 0.58, 0.61 |

**the first newline after the self-report answer** (`postans_slot1`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.58 (40 / 17) | – | 0.57 (40 / 17) | – | 0.50, 0.56, 0.52 |
| Q2 | 0.65 (58 / 30) | – | 0.65 (58 / 30) | – | 0.56, 0.59, 0.59 |
| Q6 | 0.54 (58 / 30) | – | 0.55 (58 / 30) | – | 0.54, 0.40, 0.35 |
| Q7 | 0.51 (58 / 30) | 0.47 (16 / 12) | 0.50 (58 / 30) | 0.47 (16 / 12) | 0.35, 0.36, 0.36 |
| Q9 | 0.45 (58 / 30) | – | 0.45 (58 / 30) | – | 0.56, 0.49, 0.50 |

**the last newline after the self-report answer** (`postans_slot4`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.70 (40 / 17) | – | 0.70 (40 / 17) | – | 0.58, 0.60, 0.58 |
| Q2 | 0.56 (58 / 30) | – | 0.66 (58 / 30) | – | 0.54, 0.51, 0.48 |
| Q6 | 0.79 (58 / 30) | – | 0.71 (58 / 30) | – | 0.55, 0.55, 0.55 |
| Q7 | 0.57 (58 / 30) | 0.25 (16 / 12) | 0.63 (58 / 30) | 0.40 (16 / 12) | 0.55, 0.54, 0.47 |
| Q9 | 0.59 (58 / 30) | – | 0.57 (58 / 30) | – | 0.58, 0.58, 0.54 |

## 4. After the question, by layer (line AUROC; all, then deniers)

**the newline after the question** (`preans_slot1`)

| wording | fit | layer 27 | layer 33 | layer 39 | layer 46 | layer 52 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.49, – | 0.38, – | 0.65, – | 0.65, – | 0.56, – |
| Q1 | pressured | 0.62, – | 0.74, – | 0.74, – | 0.73, – | 0.68, – |
| Q2 | unrelated | 0.39, – | 0.53, – | 0.63, – | 0.59, – | 0.55, – |
| Q2 | pressured | 0.63, – | 0.79, – | 0.83, – | 0.82, – | 0.80, – |
| Q6 | unrelated | 0.52, – | 0.73, – | 0.54, – | 0.52, – | 0.58, – |
| Q6 | pressured | 0.56, – | 0.77, – | 0.74, – | 0.69, – | 0.69, – |
| Q7 | unrelated | 0.51, 0.53 | 0.59, 0.52 | 0.69, 0.61 | 0.57, 0.38 | 0.59, 0.37 |
| Q7 | pressured | 0.56, 0.55 | 0.57, 0.51 | 0.66, 0.57 | 0.59, 0.44 | 0.59, 0.61 |
| Q9 | unrelated | 0.58, – | 0.64, – | 0.57, – | 0.59, – | 0.59, – |
| Q9 | pressured | 0.63, – | 0.66, – | 0.60, – | 0.59, – | 0.61, – |

**the turn-start token after the question** (`preans_slot2`)

| wording | fit | layer 27 | layer 33 | layer 39 | layer 46 | layer 52 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.51, – | 0.74, – | 0.54, – | 0.46, – | 0.52, – |
| Q1 | pressured | 0.63, – | 0.76, – | 0.55, – | 0.57, – | 0.60, – |
| Q2 | unrelated | 0.54, – | 0.70, – | 0.58, – | 0.52, – | 0.50, – |
| Q2 | pressured | 0.66, – | 0.73, – | 0.55, – | 0.58, – | 0.61, – |
| Q6 | unrelated | 0.43, – | 0.65, – | 0.76, – | 0.72, – | 0.64, – |
| Q6 | pressured | 0.55, – | 0.67, – | 0.56, – | 0.50, – | 0.48, – |
| Q7 | unrelated | 0.57, 0.56 | 0.48, 0.57 | 0.62, 0.50 | 0.60, 0.52 | 0.61, 0.52 |
| Q7 | pressured | 0.72, 0.76 | 0.48, 0.65 | 0.53, 0.69 | 0.60, 0.70 | 0.51, 0.70 |
| Q9 | unrelated | 0.55, – | 0.66, – | 0.59, – | 0.57, – | 0.50, – |
| Q9 | pressured | 0.67, – | 0.67, – | 0.51, – | 0.58, – | 0.57, – |

**the newline after `model`** (`preans_slot4`)

| wording | fit | layer 27 | layer 33 | layer 39 | layer 46 | layer 52 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.50, – | 0.61, – | 0.44, – | 0.50, – | 0.54, – |
| Q1 | pressured | 0.52, – | 0.58, – | 0.48, – | 0.57, – | 0.55, – |
| Q2 | unrelated | 0.53, – | 0.65, – | 0.43, – | 0.60, – | 0.65, – |
| Q2 | pressured | 0.54, – | 0.68, – | 0.59, – | 0.64, – | 0.64, – |
| Q6 | unrelated | 0.53, – | 0.60, – | 0.37, – | 0.62, – | 0.68, – |
| Q6 | pressured | 0.53, – | 0.61, – | 0.62, – | 0.66, – | 0.68, – |
| Q7 | unrelated | 0.44, 0.55 | 0.65, 0.69 | 0.47, 0.54 | 0.57, 0.35 | 0.54, 0.33 |
| Q7 | pressured | 0.49, 0.55 | 0.77, 0.84 | 0.57, 0.50 | 0.59, 0.34 | 0.58, 0.24 |
| Q9 | unrelated | 0.39, – | 0.69, – | 0.60, – | 0.64, – | 0.62, – |
| Q9 | pressured | 0.41, – | 0.66, – | 0.63, – | 0.65, – | 0.64, – |

**the first newline after the self-report answer** (`postans_slot1`)

| wording | fit | layer 27 | layer 33 | layer 39 | layer 46 | layer 52 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.50, – | 0.54, – | 0.58, – | 0.57, – | 0.59, – |
| Q1 | pressured | 0.72, – | 0.54, – | 0.57, – | 0.57, – | 0.58, – |
| Q2 | unrelated | 0.65, – | 0.54, – | 0.65, – | 0.64, – | 0.56, – |
| Q2 | pressured | 0.69, – | 0.63, – | 0.65, – | 0.64, – | 0.56, – |
| Q6 | unrelated | 0.56, – | 0.41, – | 0.54, – | 0.61, – | 0.59, – |
| Q6 | pressured | 0.61, – | 0.50, – | 0.55, – | 0.61, – | 0.59, – |
| Q7 | unrelated | 0.46, 0.59 | 0.49, 0.53 | 0.51, 0.47 | 0.47, 0.40 | 0.48, 0.21 |
| Q7 | pressured | 0.57, 0.30 | 0.51, 0.52 | 0.50, 0.47 | 0.46, 0.38 | 0.47, 0.25 |
| Q9 | unrelated | 0.50, – | 0.56, – | 0.45, – | 0.43, – | 0.55, – |
| Q9 | pressured | 0.58, – | 0.56, – | 0.45, – | 0.43, – | 0.54, – |

**the last newline after the self-report answer** (`postans_slot4`)

| wording | fit | layer 27 | layer 33 | layer 39 | layer 46 | layer 52 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.45, – | 0.58, – | 0.70, – | 0.68, – | 0.73, – |
| Q1 | pressured | 0.62, – | 0.61, – | 0.70, – | 0.67, – | 0.69, – |
| Q2 | unrelated | 0.70, – | 0.60, – | 0.56, – | 0.57, – | 0.53, – |
| Q2 | pressured | 0.59, – | 0.51, – | 0.66, – | 0.63, – | 0.61, – |
| Q6 | unrelated | 0.58, – | 0.58, – | 0.79, – | 0.63, – | 0.63, – |
| Q6 | pressured | 0.54, – | 0.29, – | 0.71, – | 0.62, – | 0.58, – |
| Q7 | unrelated | 0.57, 0.80 | 0.60, 0.37 | 0.57, 0.25 | 0.60, 0.38 | 0.58, 0.36 |
| Q7 | pressured | 0.57, 0.83 | 0.52, 0.38 | 0.63, 0.40 | 0.63, 0.35 | 0.64, 0.20 |
| Q9 | unrelated | 0.61, – | 0.55, – | 0.59, – | 0.55, – | 0.54, – |
| Q9 | pressured | 0.62, – | 0.64, – | 0.57, – | 0.57, – | 0.61, – |

## 5. Vector lengths, layer 39

Mean length of the residual vectors and its spread (standard deviation / mean). A small spread means that a fit on
vectors scaled to length 1 (the cosine view) would show nearly the same picture as the PCA drawn here. After the
question: the mean over the five wordings.

| position | pressured: mean length | pressured: spread | unrelated: mean length | unrelated: spread |
|---|---|---|---|---|
| the newline after the response | 43892 | 18.2% | 44127 | 25.7% |
| control: the turn-end token after the response | 39655 | 4.6% | 40852 | 3.3% |
| control: the newline before the response | 59187 | 9.9% | 55279 | 7.2% |
| the newline after the question | 46578 | 7.7% | 45563 | 5.4% |
| the turn-start token after the question | 42930 | 8.9% | 42409 | 8.4% |
| the newline after `model` | 52862 | 4.1% | 52200 | 2.3% |
| the first newline after the self-report answer | 42595 | 14.1% | 41269 | 12.6% |
| the last newline after the self-report answer | 59537 | 4.3% | 52977 | 3.2% |

## 6. Lies against truths within the first k principal components of the unrelated chats, layer 39

AUROC of the lie-minus-truth direction fitted within the first k components (on other scenarios than the one scored).
*full space* = the same direction with no restriction. After the question: the mean over the wordings; *deniers* over the
wordings with 10 or more lying and 10 or more truthful deniers. The last k is all components when there are 1,000 or fewer.

| position | k = 1 | k = 2 | k = 3 | k = 5 | k = 10 | k = 20 | k = 50 | k = 100 | k = 198 | k = 200 | k = 500 | k = 902 | k = 990 | full space |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| the newline after the response | 0.57 | 0.56 | 0.56 | 0.56 | 0.56 | 0.56 | 0.55 | 0.55 | 0.56 | – | – | – | – | 0.54 |
| control: the turn-end token after the response | 0.48 | 0.45 | 0.57 | 0.57 | 0.58 | 0.57 | 0.58 | 0.59 | 0.59 | – | – | – | – | 0.65 |
| control: the newline before the response | 0.57 | 0.56 | 0.56 | 0.56 | 0.56 | 0.56 | 0.56 | 0.56 | 0.57 | – | – | – | – | 0.57 |
| the newline after the question | 0.60 | 0.60 | 0.61 | 0.61 | 0.63 | 0.66 | 0.67 | 0.69 | – | 0.70 | 0.72 | – | 0.74 | 0.77 |
| the newline after the question, deniers | 0.64 | 0.65 | 0.65 | 0.65 | 0.65 | 0.68 | 0.68 | 0.70 | – | 0.75 | 0.80 | – | 0.84 | 0.91 |
| the turn-start token after the question | 0.57 | 0.58 | 0.58 | 0.58 | 0.61 | 0.63 | 0.65 | 0.67 | – | 0.68 | 0.70 | – | 0.71 | 0.75 |
| the turn-start token after the question, deniers | 0.65 | 0.64 | 0.64 | 0.64 | 0.62 | 0.63 | 0.63 | 0.63 | – | 0.64 | 0.66 | – | 0.67 | 0.69 |
| the newline after `model` | 0.50 | 0.48 | 0.55 | 0.66 | 0.67 | 0.68 | 0.69 | 0.70 | – | 0.71 | 0.71 | – | 0.72 | 0.73 |
| the newline after `model`, deniers | 0.38 | 0.63 | 0.64 | 0.76 | 0.74 | 0.76 | 0.79 | 0.79 | – | 0.85 | 0.85 | – | 0.87 | 0.88 |
| the first newline after the self-report answer | 0.58 | 0.56 | 0.57 | 0.57 | 0.57 | 0.58 | 0.58 | 0.59 | – | 0.60 | 0.60 | 0.61 | – | 0.63 |
| the first newline after the self-report answer, deniers | 0.43 | 0.44 | 0.45 | 0.45 | 0.46 | 0.48 | 0.48 | 0.49 | – | 0.51 | 0.52 | 0.57 | – | 0.60 |
| the last newline after the self-report answer | 0.55 | 0.61 | 0.64 | 0.65 | 0.66 | 0.66 | 0.67 | 0.68 | – | 0.69 | 0.69 | 0.70 | – | 0.71 |
| the last newline after the self-report answer, deniers | 0.20 | 0.27 | 0.46 | 0.46 | 0.45 | 0.43 | 0.47 | 0.54 | – | 0.56 | 0.60 | 0.61 | – | 0.66 |

Share of the unrelated chats' variance held by the first k components:

| position | k = 1 | k = 2 | k = 3 | k = 5 | k = 10 | k = 20 | k = 50 | k = 100 | k = 198 | k = 200 | k = 500 | k = 902 | k = 990 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| the newline after the response | 62% | 93% | 94% | 95% | 96% | 97% | 98% | 99% | 100% | – | – | – | – |
| control: the turn-end token after the response | 23% | 31% | 38% | 47% | 59% | 71% | 85% | 94% | 100% | – | – | – | – |
| control: the newline before the response | 18% | 27% | 31% | 39% | 50% | 62% | 78% | 91% | 100% | – | – | – | – |
| the newline after the question | 16% | 23% | 28% | 35% | 45% | 55% | 69% | 79% | – | 88% | 97% | – | 100% |
| the turn-start token after the question | 23% | 27% | 31% | 37% | 45% | 54% | 66% | 76% | – | 86% | 97% | – | 100% |
| the newline after `model` | 21% | 32% | 39% | 49% | 61% | 71% | 82% | 89% | – | 94% | 99% | – | 100% |
| the first newline after the self-report answer | 47% | 63% | 67% | 71% | 76% | 81% | 86% | 91% | – | 94% | 99% | 100% | – |
| the last newline after the self-report answer | 19% | 28% | 37% | 48% | 60% | 70% | 81% | 88% | – | 94% | 99% | 100% | – |
