# The lie-minus-truth direction at the newline after the response, scored on the held-out scenarios

Qwen3.6-27B, the residual stream at the newline after the response, layer 47. The direction is the mean of the
lies minus the mean of the truths of the fit set (152 lies, 81 truths); nothing is trained. A transcript's
score is its position along that direction, measured from the midpoint of the two means; above 0 is the lie side.
Intervals: 95%, 2,000 resamples of scenarios. Everything was fixed before the run (the top of
`scripts/heldout/score_newline_direction.py`).

## The test

| quantity | value (95% interval) |
|---|---|
| AUROC, lies against truths | 0.96 (0.93 to 0.98) |
| lies above the threshold 0 | 93/101 (92%; 86% to 97%) |
| truths above it | 7/54 (13%; 6% to 22%) |
| no-pressure truths above it | 6/90 (7%; 2% to 12%) |
| scenarios with a lie and a truth: the lie scores above its truth | 46 of 47 |

For comparison, on the build split with the direction fitted on four folds and scored on the fifth: AUROC 0.97
(152 lies, 81 truths); the lie is above its truth in 67 of 70 pairs.

## Not the test: the same procedure at the control positions and the other layers

| position | layer | AUROC, lies against truths (95% interval) | lies above 0 | truths above 0 |
|---|---|---|---|---|
| the newline before the response (the prompt alone) | 47 | 0.67 (0.62 to 0.71) | 65/101 (64%; 55% to 73%) | 23/54 (43%; 30% to 56%) |
| the turn-end token after the response | 47 | 0.69 (0.61 to 0.77) | 74/101 (73%; 64% to 82%) | 25/54 (46%; 33% to 59%) |
| the newline after the response | 35 | 0.94 (0.91 to 0.98) | 96/101 (95%; 91% to 99%) | 11/54 (20%; 11% to 31%) |
| the newline after the response | 41 | 0.95 (0.92 to 0.98) | 91/101 (90%; 84% to 95%) | 9/54 (17%; 7% to 26%) |
| the newline after the response | 53 | 0.94 (0.90 to 0.97) | 90/101 (89%; 83% to 94%) | 7/54 (13%; 6% to 22%) |
| the newline after the response | 58 | 0.93 (0.88 to 0.97) | 89/101 (88%; 82% to 94%) | 6/54 (11%; 4% to 20%) |
