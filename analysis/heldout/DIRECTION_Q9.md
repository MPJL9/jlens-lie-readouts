# Directions after the self-report question Q9, scored on the held-out scenarios

Qwen3.6-27B, wording Q9. A direction is the mean of the fit set's positives minus the mean of its negatives at one
token and layer; nothing is trained. Each cell: AUROC (95% interval, scenarios resampled; positives / negatives).
The build-split column has the direction fitted on four folds and scored on the fifth. Everything was fixed before
the run (the top of `scripts/heldout/score_q9_directions.py`).

## A. the last token before the answer (where the released probe reads), layer 50

| task | build split | held-out scenarios: the direction | held-out scenarios: the released probe |
|---|---|---|---|
| lie against truth, among deniers | 0.94 (65 / 76) | 0.88 (0.82 to 0.94; 46 / 52) | 0.50 (0.40 to 0.61; 46 / 52) |
| AISI's labelling: lied and denied, against the rest | 0.89 (65 / 162) | 0.89 (0.84 to 0.93; 46 / 107) | 0.74 (0.67 to 0.80; 46 / 107) |
| lie against truth, all transcripts | 0.95 (151 / 81) | 0.93 (0.89 to 0.96; 101 / 54) | 0.25 (0.19 to 0.32; 101 / 54) |

## B. the newline after the self-report answer, layer 47

| task | build split | held-out scenarios: the direction | held-out scenarios: the released probe |
|---|---|---|---|
| lie against truth, among deniers | 0.94 (65 / 76) | 0.91 (0.87 to 0.95; 46 / 52) | reads the token before the answer |
| AISI's labelling: lied and denied, against the rest | 0.96 (65 / 162) | 0.95 (0.92 to 0.97; 46 / 107) | reads the token before the answer |
| lie against truth, all transcripts | 0.95 (151 / 81) | 0.94 (0.90 to 0.97; 101 / 54) | reads the token before the answer |
