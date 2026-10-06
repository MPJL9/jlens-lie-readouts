# Tokens around the self-report answer: does the newline matter?

Qwen3.6-27B, wording Q9. A direction is the mean of the build split's positives minus the mean of its negatives at one
token and layer; threshold 0, the midpoint; nothing is trained. Build split: fitted on four folds, scored on the fifth.
Held-out: fitted on the build split, scored on the held-out scenarios; 95% intervals, 2,000 resamples of scenarios.
Tasks: lies against truths over all transcripts (held-out 101 / 54), and among the No answers (46 / 52).

## Layer 50

| token | task | build split: AUROC; lies flagged; truths flagged | held-out AUROC | held-out balanced accuracy | held-out lies flagged | held-out truths flagged |
|---|---|---|---|---|---|---|
| the last token before the answer (the released probe's token) | all transcripts | 0.95; 134/151 (89%); 11/81 (14%) | 0.93 (0.89 to 0.96) | 0.84 (0.78 to 0.90) | 84/101 (83%) | 8/54 (15%) |
| the last token before the answer (the released probe's token) | among the No answers | 0.94; 58/65 (89%); 14/76 (18%) | 0.88 (0.82 to 0.94) | 0.77 (0.70 to 0.83) | 39/46 (85%) | 16/52 (31%) |
| the answer token (Yes / No) | all transcripts | 0.89; 86/151 (57%); 5/81 (6%) | 0.90 (0.84 to 0.94) | 0.75 (0.70 to 0.81) | 55/101 (54%) | 2/54 (4%) |
| the answer token (Yes / No) | among the No answers | 0.88; 55/65 (85%); 19/76 (25%) | 0.81 (0.74 to 0.87) | 0.76 (0.70 to 0.82) | 34/46 (74%) | 11/52 (21%) |
| `<|im_end|>` after the answer | all transcripts | 0.87; 110/151 (73%); 15/81 (19%) | 0.86 (0.80 to 0.91) | 0.78 (0.71 to 0.84) | 71/101 (70%) | 8/54 (15%) |
| `<|im_end|>` after the answer | among the No answers | 0.75; 51/65 (78%); 32/76 (42%) | 0.73 (0.65 to 0.81) | 0.66 (0.57 to 0.74) | 33/46 (72%) | 21/52 (40%) |
| the newline after it | all transcripts | 0.95; 113/151 (75%); 5/81 (6%) | 0.93 (0.89 to 0.97) | 0.81 (0.76 to 0.86) | 67/101 (66%) | 2/54 (4%) |
| the newline after it | among the No answers | 0.94; 55/65 (85%); 9/76 (12%) | 0.91 (0.86 to 0.95) | 0.80 (0.73 to 0.86) | 37/46 (80%) | 11/52 (21%) |
| `<|im_start|>` | all transcripts | 0.88; 106/151 (70%); 9/81 (11%) | 0.84 (0.78 to 0.89) | 0.79 (0.74 to 0.84) | 63/101 (62%) | 2/54 (4%) |
| `<|im_start|>` | among the No answers | 0.80; 55/65 (85%); 25/76 (33%) | 0.74 (0.67 to 0.81) | 0.66 (0.58 to 0.74) | 31/46 (67%) | 18/52 (35%) |
| `user` | all transcripts | 0.90; 121/151 (80%); 13/81 (16%) | 0.87 (0.82 to 0.92) | 0.77 (0.70 to 0.83) | 76/101 (75%) | 12/54 (22%) |
| `user` | among the No answers | 0.79; 56/65 (86%); 28/76 (37%) | 0.73 (0.65 to 0.80) | 0.65 (0.57 to 0.73) | 34/46 (74%) | 23/52 (44%) |
| the newline after `user` | all transcripts | 0.86; 118/151 (78%); 19/81 (23%) | 0.78 (0.73 to 0.83) | 0.70 (0.64 to 0.76) | 72/101 (71%) | 17/54 (31%) |
| the newline after `user` | among the No answers | 0.77; 47/65 (72%); 22/76 (29%) | 0.69 (0.61 to 0.77) | 0.66 (0.58 to 0.73) | 32/46 (70%) | 20/52 (38%) |

## Layer 47

| token | task | build split: AUROC; lies flagged; truths flagged | held-out AUROC | held-out balanced accuracy | held-out lies flagged | held-out truths flagged |
|---|---|---|---|---|---|---|
| the last token before the answer (the released probe's token) | all transcripts | 0.95; 134/151 (89%); 11/81 (14%) | 0.94 (0.91 to 0.97) | 0.87 (0.81 to 0.92) | 87/101 (86%) | 7/54 (13%) |
| the last token before the answer (the released probe's token) | among the No answers | 0.94; 59/65 (91%); 14/76 (18%) | 0.90 (0.84 to 0.95) | 0.80 (0.74 to 0.85) | 40/46 (87%) | 14/52 (27%) |
| the answer token (Yes / No) | all transcripts | 0.87; 86/151 (57%); 5/81 (6%) | 0.84 (0.78 to 0.90) | 0.75 (0.70 to 0.81) | 55/101 (54%) | 2/54 (4%) |
| the answer token (Yes / No) | among the No answers | 0.89; 55/65 (85%); 18/76 (24%) | 0.82 (0.75 to 0.87) | 0.73 (0.67 to 0.79) | 32/46 (70%) | 12/52 (23%) |
| `<|im_end|>` after the answer | all transcripts | 0.87; 109/151 (72%); 13/81 (16%) | 0.86 (0.80 to 0.91) | 0.77 (0.70 to 0.83) | 69/101 (68%) | 8/54 (15%) |
| `<|im_end|>` after the answer | among the No answers | 0.74; 52/65 (80%); 33/76 (43%) | 0.73 (0.65 to 0.81) | 0.66 (0.57 to 0.73) | 32/46 (70%) | 20/52 (38%) |
| the newline after it | all transcripts | 0.95; 114/151 (75%); 6/81 (7%) | 0.94 (0.90 to 0.97) | 0.82 (0.76 to 0.87) | 68/101 (67%) | 2/54 (4%) |
| the newline after it | among the No answers | 0.94; 55/65 (85%); 8/76 (11%) | 0.91 (0.87 to 0.95) | 0.80 (0.74 to 0.86) | 36/46 (78%) | 10/52 (19%) |
| `<|im_start|>` | all transcripts | 0.88; 107/151 (71%); 8/81 (10%) | 0.82 (0.77 to 0.88) | 0.77 (0.71 to 0.83) | 61/101 (60%) | 3/54 (6%) |
| `<|im_start|>` | among the No answers | 0.77; 50/65 (77%); 23/76 (30%) | 0.71 (0.63 to 0.78) | 0.64 (0.55 to 0.73) | 29/46 (63%) | 18/52 (35%) |
| `user` | all transcripts | 0.90; 124/151 (82%); 16/81 (20%) | 0.87 (0.82 to 0.92) | 0.76 (0.69 to 0.82) | 82/101 (81%) | 16/54 (30%) |
| `user` | among the No answers | 0.76; 57/65 (88%); 28/76 (37%) | 0.69 (0.62 to 0.76) | 0.61 (0.54 to 0.69) | 29/46 (63%) | 21/52 (40%) |
| the newline after `user` | all transcripts | 0.88; 121/151 (80%); 18/81 (22%) | 0.80 (0.74 to 0.85) | 0.71 (0.65 to 0.77) | 75/101 (74%) | 17/54 (31%) |
| the newline after `user` | among the No answers | 0.80; 50/65 (77%); 23/76 (30%) | 0.70 (0.63 to 0.78) | 0.66 (0.59 to 0.73) | 31/46 (67%) | 18/52 (35%) |
