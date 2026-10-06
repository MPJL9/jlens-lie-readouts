# Our two directions under Q9: rates at the midpoint, build split only

Qwen3.6-27B, Q9, lie against truth among the transcripts that answer No. The direction is fitted on four folds
and scored on the fifth (the folds of the write-up); the threshold is 0, the midpoint between the two means.
Nothing held-out is read. For comparison, the released probe at its shipped threshold on the same transcripts.

| detector | token (layer) | balanced accuracy | true-positive rate | false-positive rate | AUROC |
|---|---|---|---|---|---|
| our direction | the last token before the answer (where the released probe reads), layer 50 | 0.85 | 58/65 (89%) | 14/76 (18%) | 0.94 |
| our direction | the newline after the self-report answer, layer 47 | 0.87 | 55/65 (85%) | 8/76 (11%) | 0.94 |
| the released probe, at its shipped threshold | the last token before the answer (50) | 0.46 | 58/65 (89%) | 74/76 (97%) | 0.55 |
