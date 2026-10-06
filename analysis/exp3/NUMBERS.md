# Experiment 3: numbers behind the pictures (Qwen3.6-27B, build split, in-sample)

Written by `scripts/exp3/pictures.py`. Every number is cross-validated in five folds with scenarios kept together.
*line* = AUROC of a straight-line split of lies against truths in the two drawn dimensions. *direction* = AUROC of the
lie-minus-truth direction in the full space. *pairs* = scenarios with both a lie and a truth in which the lie scores above
its truth. 0.50 is chance. Transcripts: 152 lies, 81 truths, 138 no-pressure truths, 703 unrelated chats.

## 1. Before the question, layer 47

| position | measure | AUROC (95% interval over scenarios) | pairs |
|---|---|---|---|
| the newline after the response | line, fit on unrelated chats | 0.77 (0.71 to 0.82) | 53 of 70 |
| the newline after the response | line, fit on pressured transcripts | 0.96 (0.93 to 0.98) | 67 of 70 |
| the newline after the response | direction, full space | 0.97 (0.95 to 0.99) | 67 of 70 |
| control: the turn-end token after the response | line, fit on unrelated chats | 0.66 (0.59 to 0.73) | 46 of 70 |
| control: the turn-end token after the response | line, fit on pressured transcripts | 0.63 (0.55 to 0.69) | 42 of 70 |
| control: the turn-end token after the response | direction, full space | 0.74 (0.67 to 0.80) | 55 of 70 |
| control: the newline before the response | line, fit on unrelated chats | 0.52 (0.47 to 0.57) | 7 of 70 (54 ties) |
| control: the newline before the response | line, fit on pressured transcripts | 0.58 (0.53 to 0.62) | 7 of 70 (54 ties) |
| control: the newline before the response | direction, full space | 0.61 (0.56 to 0.65) | 9 of 70 (54 ties) |

Along the direction (0 = midpoint between the two means of the other folds):

| position | missed lies on the truth side | other lies on the truth side | truths on the lie side |
|---|---|---|---|
| the newline after the response | 5 / 19 | 4 / 133 | 11 / 81 |
| control: the turn-end token after the response | 8 / 19 | 30 / 133 | 32 / 81 |
| control: the newline before the response | 9 / 19 | 51 / 133 | 37 / 81 |

## 2. Before the question, by layer

| position | measure | layer 35 | layer 41 | layer 47 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| the newline after the response | line, fit on unrelated chats | 0.77 | 0.74 | 0.77 | 0.73 | 0.65 |
| the newline after the response | line, fit on pressured transcripts | 0.93 | 0.95 | 0.96 | 0.95 | 0.96 |
| the newline after the response | direction, full space | 0.95 | 0.96 | 0.97 | 0.96 | 0.95 |
| control: the turn-end token after the response | line, fit on unrelated chats | 0.64 | 0.62 | 0.66 | 0.64 | 0.62 |
| control: the turn-end token after the response | line, fit on pressured transcripts | 0.59 | 0.57 | 0.63 | 0.62 | 0.61 |
| control: the turn-end token after the response | direction, full space | 0.73 | 0.73 | 0.74 | 0.70 | 0.69 |
| control: the newline before the response | line, fit on unrelated chats | 0.51 | 0.53 | 0.52 | 0.55 | 0.51 |
| control: the newline before the response | line, fit on pressured transcripts | 0.61 | 0.60 | 0.58 | 0.58 | 0.57 |
| control: the newline before the response | direction, full space | 0.63 | 0.62 | 0.61 | 0.60 | 0.61 |

UMAP of the pressured transcripts (check; line AUROC for seeds 0, 1, 2): the newline after the response: 0.96, 0.96, 0.96; control: the turn-end token after the response: 0.52, 0.56, 0.54; control: the newline before the response: 0.58, 0.56, 0.56.

## 3. After the question, layer 47

Lies / truths in brackets. *deniers* = transcripts that answer No; the line is fitted among deniers.

**the newline after the question** (`preans_slot1`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.89 (152 / 81) | 0.88 (53 / 74) | 0.96 (152 / 81) | 0.93 (53 / 74) | 0.96, 0.94, 0.95 |
| Q2 | 0.88 (152 / 81) | 0.86 (47 / 77) | 0.96 (152 / 81) | 0.92 (47 / 77) | 0.97, 0.95, 0.95 |
| Q6 | 0.79 (152 / 81) | 0.81 (43 / 73) | 0.93 (152 / 81) | 0.90 (43 / 73) | 0.95, 0.93, 0.94 |
| Q7 | 0.69 (152 / 81) | 0.70 (79 / 77) | 0.77 (152 / 81) | 0.81 (79 / 77) | 0.77, 0.79, 0.79 |
| Q9 | 0.71 (152 / 81) | 0.76 (65 / 76) | 0.95 (152 / 81) | 0.91 (65 / 76) | 0.95, 0.95, 0.95 |

**the newline after `assistant`** (`preans_slot4`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.75 (152 / 81) | 0.68 (53 / 74) | 0.90 (152 / 81) | 0.90 (53 / 74) | 0.90, 0.90, 0.90 |
| Q2 | 0.77 (152 / 81) | 0.65 (47 / 77) | 0.89 (152 / 81) | 0.85 (47 / 77) | 0.90, 0.91, 0.90 |
| Q6 | 0.66 (152 / 81) | 0.64 (43 / 73) | 0.89 (152 / 81) | 0.87 (43 / 73) | 0.92, 0.92, 0.92 |
| Q7 | 0.69 (152 / 81) | 0.62 (79 / 77) | 0.91 (152 / 81) | 0.90 (79 / 77) | 0.90, 0.90, 0.90 |
| Q9 | 0.69 (152 / 81) | 0.59 (65 / 76) | 0.88 (152 / 81) | 0.84 (65 / 76) | 0.91, 0.92, 0.91 |

**`</think>`** (`think_slot2`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.59 (152 / 81) | 0.71 (53 / 74) | 0.67 (152 / 81) | 0.75 (53 / 74) | 0.71, 0.68, 0.68 |
| Q2 | 0.62 (152 / 81) | 0.77 (47 / 77) | 0.57 (152 / 81) | 0.77 (47 / 77) | 0.61, 0.61, 0.60 |
| Q6 | 0.60 (152 / 81) | 0.67 (43 / 73) | 0.59 (152 / 81) | 0.69 (43 / 73) | 0.62, 0.61, 0.61 |
| Q7 | 0.65 (152 / 81) | 0.67 (79 / 77) | 0.54 (152 / 81) | 0.66 (79 / 77) | 0.61, 0.59, 0.60 |
| Q9 | 0.63 (152 / 81) | 0.65 (65 / 76) | 0.63 (152 / 81) | 0.69 (65 / 76) | 0.61, 0.60, 0.60 |

**the first newline after the self-report answer** (`postans_slot1`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.67 (107 / 62) | 0.48 (43 / 57) | 0.93 (107 / 62) | 0.91 (43 / 57) | 0.90, 0.90, 0.90 |
| Q2 | 0.73 (152 / 81) | 0.69 (47 / 77) | 0.94 (152 / 81) | 0.88 (47 / 77) | 0.93, 0.94, 0.93 |
| Q6 | 0.76 (152 / 81) | 0.63 (43 / 73) | 0.92 (152 / 81) | 0.88 (43 / 73) | 0.92, 0.90, 0.88 |
| Q7 | 0.67 (152 / 81) | 0.71 (79 / 77) | 0.93 (152 / 81) | 0.91 (79 / 77) | 0.93, 0.93, 0.92 |
| Q9 | 0.66 (152 / 81) | 0.70 (65 / 76) | 0.93 (152 / 81) | 0.90 (65 / 76) | 0.92, 0.93, 0.90 |

**the last newline after the self-report answer** (`postans_slot4`)

| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |
|---|---|---|---|---|---|
| Q1 | 0.57 (107 / 62) | 0.68 (43 / 57) | 0.67 (107 / 62) | 0.71 (43 / 57) | 0.66, 0.65, 0.65 |
| Q2 | 0.67 (152 / 81) | 0.48 (47 / 77) | 0.73 (152 / 81) | 0.62 (47 / 77) | 0.80, 0.78, 0.78 |
| Q6 | 0.63 (152 / 81) | 0.56 (43 / 73) | 0.67 (152 / 81) | 0.57 (43 / 73) | 0.75, 0.75, 0.74 |
| Q7 | 0.63 (152 / 81) | 0.65 (79 / 77) | 0.62 (152 / 81) | 0.49 (79 / 77) | 0.68, 0.68, 0.67 |
| Q9 | 0.69 (152 / 81) | 0.68 (65 / 76) | 0.76 (152 / 81) | 0.67 (65 / 76) | 0.78, 0.78, 0.78 |

## 4. After the question, by layer (line AUROC; all, then deniers)

**the newline after the question** (`preans_slot1`)

| wording | fit | layer 35 | layer 41 | layer 47 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.91, 0.88 | 0.94, 0.92 | 0.89, 0.88 | 0.88, 0.82 | 0.72, 0.66 |
| Q1 | pressured | 0.95, 0.94 | 0.97, 0.95 | 0.96, 0.93 | 0.94, 0.91 | 0.94, 0.91 |
| Q2 | unrelated | 0.90, 0.85 | 0.94, 0.90 | 0.88, 0.86 | 0.87, 0.85 | 0.69, 0.72 |
| Q2 | pressured | 0.95, 0.91 | 0.97, 0.94 | 0.96, 0.92 | 0.93, 0.88 | 0.92, 0.86 |
| Q6 | unrelated | 0.83, 0.80 | 0.88, 0.83 | 0.79, 0.81 | 0.70, 0.79 | 0.58, 0.68 |
| Q6 | pressured | 0.92, 0.88 | 0.94, 0.90 | 0.93, 0.90 | 0.89, 0.84 | 0.85, 0.81 |
| Q7 | unrelated | 0.83, 0.87 | 0.80, 0.85 | 0.69, 0.70 | 0.75, 0.76 | 0.80, 0.80 |
| Q7 | pressured | 0.85, 0.88 | 0.83, 0.86 | 0.77, 0.81 | 0.77, 0.73 | 0.74, 0.69 |
| Q9 | unrelated | 0.86, 0.83 | 0.84, 0.82 | 0.71, 0.76 | 0.55, 0.54 | 0.67, 0.64 |
| Q9 | pressured | 0.93, 0.89 | 0.94, 0.91 | 0.95, 0.91 | 0.94, 0.90 | 0.91, 0.88 |

**the newline after `assistant`** (`preans_slot4`)

| wording | fit | layer 35 | layer 41 | layer 47 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.68, 0.73 | 0.73, 0.72 | 0.75, 0.68 | 0.70, 0.46 | 0.77, 0.58 |
| Q1 | pressured | 0.92, 0.91 | 0.91, 0.92 | 0.90, 0.90 | 0.71, 0.73 | 0.76, 0.66 |
| Q2 | unrelated | 0.70, 0.74 | 0.76, 0.69 | 0.77, 0.65 | 0.77, 0.50 | 0.82, 0.65 |
| Q2 | pressured | 0.91, 0.89 | 0.91, 0.89 | 0.89, 0.85 | 0.77, 0.66 | 0.82, 0.72 |
| Q6 | unrelated | 0.63, 0.68 | 0.71, 0.64 | 0.66, 0.64 | 0.67, 0.56 | 0.78, 0.77 |
| Q6 | pressured | 0.92, 0.89 | 0.91, 0.91 | 0.89, 0.87 | 0.79, 0.73 | 0.86, 0.81 |
| Q7 | unrelated | 0.73, 0.73 | 0.73, 0.70 | 0.69, 0.62 | 0.79, 0.70 | 0.72, 0.72 |
| Q7 | pressured | 0.93, 0.93 | 0.94, 0.94 | 0.91, 0.90 | 0.92, 0.90 | 0.87, 0.83 |
| Q9 | unrelated | 0.64, 0.55 | 0.65, 0.47 | 0.69, 0.59 | 0.76, 0.71 | 0.83, 0.83 |
| Q9 | pressured | 0.92, 0.91 | 0.92, 0.91 | 0.88, 0.84 | 0.84, 0.85 | 0.86, 0.84 |

**`</think>`** (`think_slot2`)

| wording | fit | layer 35 | layer 41 | layer 47 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.60, 0.71 | 0.60, 0.71 | 0.59, 0.71 | 0.55, 0.69 | 0.63, 0.74 |
| Q1 | pressured | 0.49, 0.73 | 0.59, 0.73 | 0.67, 0.75 | 0.70, 0.78 | 0.72, 0.78 |
| Q2 | unrelated | 0.61, 0.66 | 0.62, 0.64 | 0.62, 0.77 | 0.61, 0.70 | 0.60, 0.71 |
| Q2 | pressured | 0.56, 0.75 | 0.50, 0.76 | 0.57, 0.77 | 0.65, 0.78 | 0.75, 0.78 |
| Q6 | unrelated | 0.61, 0.68 | 0.61, 0.67 | 0.60, 0.67 | 0.64, 0.69 | 0.64, 0.71 |
| Q6 | pressured | 0.56, 0.68 | 0.51, 0.69 | 0.59, 0.69 | 0.68, 0.70 | 0.77, 0.70 |
| Q7 | unrelated | 0.62, 0.65 | 0.63, 0.69 | 0.65, 0.67 | 0.68, 0.68 | 0.62, 0.61 |
| Q7 | pressured | 0.59, 0.60 | 0.52, 0.63 | 0.54, 0.66 | 0.59, 0.68 | 0.61, 0.68 |
| Q9 | unrelated | 0.62, 0.66 | 0.62, 0.64 | 0.63, 0.65 | 0.58, 0.57 | 0.59, 0.61 |
| Q9 | pressured | 0.58, 0.58 | 0.57, 0.63 | 0.63, 0.69 | 0.72, 0.75 | 0.79, 0.76 |

**the first newline after the self-report answer** (`postans_slot1`)

| wording | fit | layer 35 | layer 41 | layer 47 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.71, 0.56 | 0.68, 0.56 | 0.67, 0.48 | 0.51, 0.59 | 0.52, 0.69 |
| Q1 | pressured | 0.88, 0.85 | 0.92, 0.91 | 0.93, 0.91 | 0.83, 0.78 | 0.79, 0.78 |
| Q2 | unrelated | 0.80, 0.62 | 0.63, 0.69 | 0.73, 0.69 | 0.58, 0.61 | 0.54, 0.63 |
| Q2 | pressured | 0.91, 0.82 | 0.94, 0.88 | 0.94, 0.88 | 0.89, 0.73 | 0.88, 0.70 |
| Q6 | unrelated | 0.81, 0.61 | 0.78, 0.68 | 0.76, 0.63 | 0.65, 0.66 | 0.75, 0.66 |
| Q6 | pressured | 0.89, 0.79 | 0.92, 0.87 | 0.92, 0.88 | 0.89, 0.73 | 0.87, 0.70 |
| Q7 | unrelated | 0.81, 0.68 | 0.81, 0.78 | 0.67, 0.71 | 0.60, 0.61 | 0.70, 0.72 |
| Q7 | pressured | 0.88, 0.84 | 0.93, 0.91 | 0.93, 0.91 | 0.84, 0.78 | 0.82, 0.75 |
| Q9 | unrelated | 0.81, 0.63 | 0.75, 0.68 | 0.66, 0.70 | 0.67, 0.56 | 0.79, 0.64 |
| Q9 | pressured | 0.87, 0.78 | 0.91, 0.88 | 0.93, 0.90 | 0.84, 0.69 | 0.84, 0.69 |

**the last newline after the self-report answer** (`postans_slot4`)

| wording | fit | layer 35 | layer 41 | layer 47 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| Q1 | unrelated | 0.66, 0.66 | 0.54, 0.71 | 0.57, 0.68 | 0.59, 0.56 | 0.60, 0.57 |
| Q1 | pressured | 0.58, 0.73 | 0.77, 0.83 | 0.67, 0.71 | 0.61, 0.58 | 0.61, 0.56 |
| Q2 | unrelated | 0.68, 0.52 | 0.69, 0.50 | 0.67, 0.48 | 0.58, 0.59 | 0.59, 0.54 |
| Q2 | pressured | 0.61, 0.69 | 0.84, 0.77 | 0.73, 0.62 | 0.67, 0.56 | 0.65, 0.58 |
| Q6 | unrelated | 0.69, 0.58 | 0.63, 0.56 | 0.63, 0.56 | 0.60, 0.60 | 0.60, 0.56 |
| Q6 | pressured | 0.67, 0.66 | 0.82, 0.73 | 0.67, 0.57 | 0.63, 0.59 | 0.59, 0.58 |
| Q7 | unrelated | 0.68, 0.67 | 0.65, 0.64 | 0.63, 0.65 | 0.56, 0.57 | 0.54, 0.52 |
| Q7 | pressured | 0.70, 0.65 | 0.80, 0.76 | 0.62, 0.49 | 0.66, 0.56 | 0.68, 0.58 |
| Q9 | unrelated | 0.74, 0.73 | 0.76, 0.73 | 0.69, 0.68 | 0.54, 0.53 | 0.57, 0.56 |
| Q9 | pressured | 0.72, 0.70 | 0.88, 0.81 | 0.76, 0.67 | 0.66, 0.63 | 0.64, 0.64 |

## 5. Vector lengths, layer 47

Mean length of the residual vectors and its spread (standard deviation / mean). A small spread means that a fit on
vectors scaled to length 1 (the cosine view) would show nearly the same picture as the PCA drawn here. After the
question: the mean over the five wordings.

| position | pressured: mean length | pressured: spread | unrelated: mean length | unrelated: spread |
|---|---|---|---|---|
| the newline after the response | 98 | 3.7% | 88 | 6.7% |
| control: the turn-end token after the response | 76 | 4.3% | 81 | 2.9% |
| control: the newline before the response | 95 | 3.6% | 100 | 5.3% |
| the newline after the question | 99 | 3.5% | 98 | 3.4% |
| the newline after `assistant` | 91 | 2.9% | 95 | 1.7% |
| `</think>` | 90 | 2.0% | 87 | 2.3% |
| the first newline after the self-report answer | 85 | 3.2% | 79 | 1.8% |
| the last newline after the self-report answer | 95 | 5.4% | 86 | 4.4% |

## 6. Lies against truths within the first k principal components of the unrelated chats, layer 47

AUROC of the lie-minus-truth direction fitted within the first k components (on other scenarios than the one scored).
*full space* = the same direction with no restriction. After the question: the mean over the wordings; *deniers* over the
wordings with 10 or more lying and 10 or more truthful deniers. The last k is all components when there are 1,000 or fewer.

| position | k = 1 | k = 2 | k = 3 | k = 5 | k = 10 | k = 20 | k = 50 | k = 100 | k = 200 | k = 500 | k = 702 | full space |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| the newline after the response | 0.76 | 0.76 | 0.76 | 0.79 | 0.83 | 0.84 | 0.92 | 0.93 | 0.94 | 0.96 | 0.96 | 0.97 |
| control: the turn-end token after the response | 0.62 | 0.64 | 0.63 | 0.63 | 0.62 | 0.61 | 0.62 | 0.63 | 0.65 | 0.68 | 0.69 | 0.74 |
| control: the newline before the response | 0.48 | 0.52 | 0.57 | 0.57 | 0.58 | 0.59 | 0.60 | 0.60 | 0.60 | 0.60 | 0.60 | 0.61 |
| the newline after the question | 0.58 | 0.77 | 0.83 | 0.84 | 0.87 | 0.90 | 0.91 | 0.92 | 0.92 | 0.93 | – | 0.94 |
| the newline after the question, deniers | 0.59 | 0.78 | 0.83 | 0.84 | 0.85 | 0.89 | 0.89 | 0.90 | 0.91 | 0.91 | – | 0.93 |
| the newline after `assistant` | 0.59 | 0.71 | 0.73 | 0.77 | 0.82 | 0.84 | 0.86 | 0.87 | 0.88 | 0.89 | – | 0.91 |
| the newline after `assistant`, deniers | 0.62 | 0.63 | 0.66 | 0.70 | 0.78 | 0.83 | 0.86 | 0.87 | 0.89 | 0.90 | – | 0.91 |
| `</think>` | 0.62 | 0.63 | 0.63 | 0.63 | 0.63 | 0.65 | 0.74 | 0.80 | 0.82 | 0.84 | – | 0.87 |
| `</think>`, deniers | 0.69 | 0.70 | 0.71 | 0.72 | 0.72 | 0.73 | 0.76 | 0.77 | 0.78 | 0.78 | – | 0.79 |
| the first newline after the self-report answer | 0.59 | 0.70 | 0.71 | 0.79 | 0.87 | 0.90 | 0.92 | 0.92 | 0.93 | 0.93 | – | 0.94 |
| the first newline after the self-report answer, deniers | 0.59 | 0.62 | 0.62 | 0.67 | 0.84 | 0.90 | 0.91 | 0.91 | 0.92 | 0.92 | – | 0.92 |
| the last newline after the self-report answer | 0.61 | 0.65 | 0.66 | 0.69 | 0.76 | 0.77 | 0.78 | 0.79 | 0.80 | 0.81 | – | 0.83 |
| the last newline after the self-report answer, deniers | 0.58 | 0.63 | 0.62 | 0.64 | 0.72 | 0.74 | 0.76 | 0.77 | 0.78 | 0.79 | – | 0.81 |

Share of the unrelated chats' variance held by the first k components:

| position | k = 1 | k = 2 | k = 3 | k = 5 | k = 10 | k = 20 | k = 50 | k = 100 | k = 200 | k = 500 | k = 702 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| the newline after the response | 13% | 23% | 27% | 34% | 45% | 55% | 69% | 80% | 89% | 98% | 100% |
| control: the turn-end token after the response | 21% | 31% | 39% | 45% | 54% | 62% | 73% | 81% | 89% | 98% | 100% |
| control: the newline before the response | 10% | 16% | 20% | 26% | 37% | 47% | 62% | 74% | 85% | 97% | 100% |
| the newline after the question | 9% | 15% | 20% | 28% | 39% | 50% | 65% | 75% | 83% | 93% | – |
| the newline after `assistant` | 15% | 30% | 36% | 44% | 57% | 68% | 80% | 86% | 91% | 96% | – |
| `</think>` | 8% | 15% | 19% | 26% | 38% | 50% | 64% | 74% | 83% | 92% | – |
| the first newline after the self-report answer | 12% | 19% | 25% | 34% | 46% | 57% | 71% | 79% | 86% | 94% | – |
| the last newline after the self-report answer | 13% | 22% | 27% | 33% | 43% | 53% | 66% | 74% | 82% | 92% | – |
