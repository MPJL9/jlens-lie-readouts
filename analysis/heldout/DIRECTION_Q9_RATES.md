# Directions under Q9 on the held-out scenarios: rates at the midpoint

Qwen3.6-27B, wording Q9, lies against truths among the transcripts whose answer is No. The directions are those of
`scripts/heldout/score_q9_directions.py` (fitted on the build split; that run declared the AUROC, reproduced here
in step 1). Threshold: 0, the midpoint between the two means, fixed by the fit. Intervals: 95%, 2,000 resamples of
scenarios. The released probe is at its shipped threshold on the same transcripts. Nothing is fitted or chosen here.

| detector | token (layer) | balanced accuracy | true-positive rate | false-positive rate | AUROC |
|---|---|---|---|---|---|
| the released probe, at its shipped threshold | the last token before the answer (50) | 0.44 (0.38 to 0.50) | 39/46 (85%; 74% to 93%) | 50/52 (96%; 90% to 100%) | 0.50 (0.40 to 0.61) |
| our direction | the last token before the answer (where the released probe reads), layer 50 | 0.77 (0.70 to 0.83) | 39/46 (85%; 74% to 93%) | 16/52 (31%; 19% to 44%) | 0.88 (0.82 to 0.94) |
| our direction | the newline after the self-report answer, layer 47 | 0.80 (0.74 to 0.86) | 36/46 (78%; 67% to 89%) | 10/52 (19%; 10% to 29%) | 0.91 (0.87 to 0.95) |
