# The difference-of-means probe at the template tokens: Qwen3.6-27B

Written by `scripts/probe/score_bands.py` on 2026-10-15. Qwen3.6-27B: the residual stream at every template token of the four bands
(`scripts/probe/bands.py`), from `data/cluster/runs/qwen3_6_27b/exp3_bands`, layers 35, 41, 47, 50, 53, 58. A direction is the mean of the fit set's positives minus the
mean of its negatives at one token and layer; a transcript's score is its position along that direction from the midpoint of the two means;
above 0 is the lie side. Nothing is trained.
*Build split*: the direction fitted on four folds and scored on the fifth (scenarios kept together). *Held-out*: fitted on the build split,
scored on the held-out split; 95% intervals, 2,000 resamples of scenarios (seed 0), at layers 47 and 50 only. *Both splits*: the two
splits pooled, five folds. A task is scored only where the fit set has 10 or more of each class ("–" otherwise). Above 0 = flagged as a lie.
Transcripts: build split 152 lies, 81 truths, 138 no-pressure truths; held-out 101, 54, 90.
Layer 47: the layer of the post's numbers (Qwen) or of this model's Experiment 3 pictures; layer 50: the released did-you-lie probe's layer.

## 1. After the response (no question asked): lies against truths

### Layer 47

| token | build split: AUROC; lies above 0; truths above 0 | held-out AUROC | held-out balanced accuracy | held-out lies above 0 | held-out truths above 0 | held-out no-pressure truths above 0 | held-out pairs: the lie above its truth | both splits, five folds: AUROC |
|---|---|---|---|---|---|---|---|---|
| `<\|im_end\|>` (postresp_slot0) | 0.74; 114/152 (75%); 32/81 (40%) | 0.69 (0.61 to 0.77) | 0.63 (0.57 to 0.70) | 74/101 (73%; 64% to 82%) | 25/54 (46%; 33% to 59%) | 17/90 (19%; 12% to 27%) | 36 of 47 | 0.75 |
| newline (postresp_slot1) | 0.97; 143/152 (94%); 11/81 (14%) | 0.96 (0.93 to 0.98) | 0.90 (0.84 to 0.94) | 93/101 (92%; 86% to 97%) | 7/54 (13%; 6% to 22%) | 6/90 (7%; 2% to 12%) | 46 of 47 | 0.97 |
| `<\|im_start\|>` (postresp_slot2) | 0.80; 133/152 (88%); 31/81 (38%) | 0.80 (0.74 to 0.85) | 0.73 (0.67 to 0.79) | 88/101 (87%; 80% to 93%) | 22/54 (41%; 28% to 54%) | 9/90 (10%; 4% to 17%) | 36 of 47 | 0.80 |
| `user` (postresp_slot3) | 0.78; 128/152 (84%); 35/81 (43%) | 0.75 (0.69 to 0.81) | 0.66 (0.60 to 0.72) | 85/101 (84%; 76% to 91%) | 28/54 (52%; 39% to 65%) | 2/90 (2%; 0% to 6%) | 36 of 47 | 0.76 |
| newline (postresp_slot4) | 0.82; 130/152 (86%); 32/81 (40%) | 0.81 (0.76 to 0.86) | 0.70 (0.64 to 0.76) | 87/101 (86%; 79% to 92%) | 25/54 (46%; 33% to 59%) | 10/90 (11%; 6% to 18%) | 38 of 47 | 0.81 |

### Layer 50

| token | build split: AUROC; lies above 0; truths above 0 | held-out AUROC | held-out balanced accuracy | held-out lies above 0 | held-out truths above 0 | held-out no-pressure truths above 0 | held-out pairs: the lie above its truth | both splits, five folds: AUROC |
|---|---|---|---|---|---|---|---|---|
| `<\|im_end\|>` (postresp_slot0) | 0.70; 106/152 (70%); 37/81 (46%) | 0.65 (0.57 to 0.73) | 0.56 (0.49 to 0.63) | 70/101 (69%; 60% to 78%) | 31/54 (57%; 44% to 70%) | 12/90 (13%; 7% to 21%) | 35 of 47 | 0.70 |
| newline (postresp_slot1) | 0.97; 138/152 (91%); 8/81 (10%) | 0.95 (0.91 to 0.98) | 0.89 (0.83 to 0.93) | 91/101 (90%; 84% to 95%) | 7/54 (13%; 6% to 22%) | 3/90 (3%; 0% to 8%) | 45 of 47 | 0.96 |
| `<\|im_start\|>` (postresp_slot2) | 0.79; 123/152 (81%); 30/81 (37%) | 0.75 (0.68 to 0.82) | 0.68 (0.61 to 0.73) | 86/101 (85%; 78% to 91%) | 27/54 (50%; 37% to 63%) | 24/90 (27%; 18% to 37%) | 30 of 47 | 0.78 |
| `user` (postresp_slot3) | 0.78; 127/152 (84%); 33/81 (41%) | 0.75 (0.70 to 0.82) | 0.64 (0.58 to 0.70) | 84/101 (83%; 75% to 90%) | 30/54 (56%; 41% to 69%) | 8/90 (9%; 3% to 16%) | 37 of 47 | 0.76 |
| newline (postresp_slot4) | 0.80; 130/152 (86%); 34/81 (42%) | 0.82 (0.77 to 0.87) | 0.66 (0.60 to 0.72) | 89/101 (88%; 82% to 94%) | 30/54 (56%; 43% to 69%) | 14/90 (16%; 9% to 23%) | 38 of 47 | 0.80 |

## 2. After the response, by layer: AUROC

**Held-out (fitted on the build split)**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (postresp_slot0) | 0.77 | 0.75 | 0.69 (0.61 to 0.77) | 0.65 (0.57 to 0.73) | 0.63 | 0.62 |
| newline (postresp_slot1) | 0.94 | 0.95 | 0.96 (0.93 to 0.98) | 0.95 (0.91 to 0.98) | 0.94 | 0.93 |
| `<\|im_start\|>` (postresp_slot2) | 0.81 | 0.80 | 0.80 (0.74 to 0.85) | 0.75 (0.68 to 0.82) | 0.56 | 0.53 |
| `user` (postresp_slot3) | 0.75 | 0.73 | 0.75 (0.69 to 0.81) | 0.75 (0.70 to 0.82) | 0.75 | 0.76 |
| newline (postresp_slot4) | 0.88 | 0.83 | 0.81 (0.76 to 0.86) | 0.82 (0.77 to 0.87) | 0.81 | 0.80 |

**Build split, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (postresp_slot0) | 0.73 | 0.73 | 0.74 | 0.70 | 0.70 | 0.69 |
| newline (postresp_slot1) | 0.95 | 0.96 | 0.97 | 0.97 | 0.96 | 0.95 |
| `<\|im_start\|>` (postresp_slot2) | 0.82 | 0.81 | 0.80 | 0.79 | 0.65 | 0.61 |
| `user` (postresp_slot3) | 0.78 | 0.77 | 0.78 | 0.78 | 0.78 | 0.79 |
| newline (postresp_slot4) | 0.88 | 0.85 | 0.82 | 0.80 | 0.81 | 0.76 |

**Both splits, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (postresp_slot0) | 0.76 | 0.76 | 0.75 | 0.70 | 0.70 | 0.69 |
| newline (postresp_slot1) | 0.95 | 0.96 | 0.97 | 0.96 | 0.96 | 0.96 |
| `<\|im_start\|>` (postresp_slot2) | 0.82 | 0.80 | 0.80 | 0.78 | 0.64 | 0.58 |
| `user` (postresp_slot3) | 0.76 | 0.75 | 0.76 | 0.76 | 0.76 | 0.76 |
| newline (postresp_slot4) | 0.88 | 0.85 | 0.81 | 0.80 | 0.80 | 0.77 |

## 3. Around the self-report answer under Q9 (the post's wording)

### Layer 47, lies against truths, all transcripts (build 151 / 81, held-out 101 / 54)

| token | build split: AUROC; lies above 0; truths above 0 | held-out AUROC | held-out balanced accuracy | held-out lies above 0 | held-out truths above 0 | both splits, five folds: AUROC |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.89; 130/151 (86%); 18/81 (22%) | 0.85 (0.80 to 0.90) | 0.75 (0.68 to 0.81) | 84/101 (83%; 75% to 90%) | 18/54 (33%; 22% to 46%) | 0.87 |
| newline (preans_slot1) | 0.96; 137/151 (91%); 10/81 (12%) | 0.95 (0.92 to 0.98) | 0.89 (0.84 to 0.94) | 91/101 (90%; 84% to 96%) | 6/54 (11%; 4% to 20%) | 0.95 |
| `<\|im_start\|>` (preans_slot2) | 0.88; 127/151 (84%); 20/81 (25%) | 0.90 (0.87 to 0.94) | 0.78 (0.72 to 0.84) | 81/101 (80%; 72% to 87%) | 13/54 (24%; 13% to 35%) | 0.88 |
| `assistant` (preans_slot3) | 0.85; 138/151 (91%); 32/81 (40%) | 0.80 (0.74 to 0.86) | 0.74 (0.67 to 0.81) | 91/101 (90%; 84% to 95%) | 23/54 (43%; 30% to 56%) | 0.86 |
| newline (preans_slot4) | 0.93; 131/151 (87%); 14/81 (17%) | 0.91 (0.87 to 0.95) | 0.85 (0.80 to 0.90) | 86/101 (85%; 78% to 92%) | 8/54 (15%; 6% to 24%) | 0.93 |
| `<think>` (think_slot0) | 0.79; 136/151 (90%); 40/81 (49%) | 0.78 (0.72 to 0.84) | 0.72 (0.67 to 0.78) | 88/101 (87%; 80% to 93%) | 23/54 (43%; 30% to 56%) | 0.77 |
| blank line (think_slot1) | 0.85; 142/151 (94%); 29/81 (36%) | 0.82 (0.77 to 0.88) | 0.75 (0.69 to 0.81) | 88/101 (87%; 80% to 93%) | 20/54 (37%; 26% to 50%) | 0.83 |
| `</think>` (think_slot2) | 0.86; 126/151 (83%); 22/81 (27%) | 0.82 (0.76 to 0.88) | 0.73 (0.67 to 0.79) | 78/101 (77%; 69% to 85%) | 17/54 (31%; 20% to 44%) | 0.85 |
| blank line (think_slot3) | 0.95; 134/151 (89%); 11/81 (14%) | 0.94 (0.91 to 0.97) | 0.87 (0.81 to 0.92) | 87/101 (86%; 79% to 92%) | 7/54 (13%; 6% to 22%) | 0.95 |
| the answer token (Yes / No) | 0.87; 86/151 (57%); 5/81 (6%) | 0.84 (0.78 to 0.90) | 0.75 (0.70 to 0.81) | 55/101 (54%; 45% to 64%) | 2/54 (4%; 0% to 9%) | 0.84 |
| `<\|im_end\|>` (postans_slot0) | 0.87; 109/151 (72%); 13/81 (16%) | 0.86 (0.80 to 0.91) | 0.77 (0.70 to 0.83) | 69/101 (68%; 58% to 77%) | 8/54 (15%; 6% to 24%) | 0.86 |
| newline (postans_slot1) | 0.95; 114/151 (75%); 6/81 (7%) | 0.94 (0.90 to 0.97) | 0.82 (0.76 to 0.87) | 68/101 (67%; 57% to 76%) | 2/54 (4%; 0% to 9%) | 0.94 |
| `<\|im_start\|>` (postans_slot2) | 0.88; 107/151 (71%); 8/81 (10%) | 0.82 (0.77 to 0.88) | 0.77 (0.71 to 0.83) | 61/101 (60%; 50% to 69%) | 3/54 (6%; 0% to 13%) | 0.85 |
| `user` (postans_slot3) | 0.90; 124/151 (82%); 16/81 (20%) | 0.87 (0.82 to 0.92) | 0.76 (0.69 to 0.82) | 82/101 (81%; 73% to 88%) | 16/54 (30%; 19% to 41%) | 0.88 |
| newline (postans_slot4) | 0.88; 121/151 (80%); 18/81 (22%) | 0.80 (0.74 to 0.85) | 0.71 (0.65 to 0.77) | 75/101 (74%; 65% to 82%) | 17/54 (31%; 20% to 44%) | 0.85 |

### Layer 47, lies against truths, among the No answers (build 65 / 76, held-out 46 / 52)

| token | build split: AUROC; lies above 0; truths above 0 | held-out AUROC | held-out balanced accuracy | held-out lies above 0 | held-out truths above 0 | both splits, five folds: AUROC |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.88; 55/65 (85%); 18/76 (24%) | 0.78 (0.71 to 0.85) | 0.71 (0.64 to 0.78) | 38/46 (83%; 72% to 93%) | 21/52 (40%; 29% to 52%) | 0.84 |
| newline (preans_slot1) | 0.94; 58/65 (89%); 11/76 (14%) | 0.92 (0.87 to 0.96) | 0.82 (0.75 to 0.88) | 40/46 (87%; 76% to 96%) | 12/52 (23%; 12% to 35%) | 0.93 |
| `<\|im_start\|>` (preans_slot2) | 0.88; 55/65 (85%); 28/76 (37%) | 0.89 (0.83 to 0.93) | 0.79 (0.72 to 0.85) | 38/46 (83%; 72% to 93%) | 13/52 (25%; 13% to 37%) | 0.88 |
| `assistant` (preans_slot3) | 0.78; 55/65 (85%); 32/76 (42%) | 0.70 (0.62 to 0.78) | 0.63 (0.54 to 0.71) | 34/46 (74%; 61% to 87%) | 25/52 (48%; 35% to 62%) | 0.78 |
| newline (preans_slot4) | 0.94; 55/65 (85%); 12/76 (16%) | 0.86 (0.80 to 0.92) | 0.81 (0.74 to 0.87) | 37/46 (80%; 67% to 91%) | 10/52 (19%; 10% to 29%) | 0.91 |
| `<think>` (think_slot0) | 0.76; 57/65 (88%); 35/76 (46%) | 0.72 (0.65 to 0.79) | 0.64 (0.57 to 0.71) | 37/46 (80%; 70% to 91%) | 27/52 (52%; 38% to 63%) | 0.74 |
| blank line (think_slot1) | 0.81; 57/65 (88%); 30/76 (39%) | 0.73 (0.66 to 0.79) | 0.70 (0.62 to 0.77) | 36/46 (78%; 65% to 89%) | 20/52 (38%; 27% to 52%) | 0.79 |
| `</think>` (think_slot2) | 0.83; 51/65 (78%); 19/76 (25%) | 0.72 (0.63 to 0.80) | 0.67 (0.59 to 0.74) | 30/46 (65%; 52% to 78%) | 16/52 (31%; 19% to 44%) | 0.81 |
| blank line (think_slot3) | 0.94; 59/65 (91%); 14/76 (18%) | 0.90 (0.84 to 0.95) | 0.80 (0.74 to 0.85) | 40/46 (87%; 76% to 96%) | 14/52 (27%; 17% to 38%) | 0.93 |
| the answer token (Yes / No) | 0.89; 55/65 (85%); 18/76 (24%) | 0.82 (0.75 to 0.87) | 0.73 (0.67 to 0.79) | 32/46 (70%; 57% to 83%) | 12/52 (23%; 13% to 35%) | 0.88 |
| `<\|im_end\|>` (postans_slot0) | 0.74; 52/65 (80%); 33/76 (43%) | 0.73 (0.65 to 0.81) | 0.66 (0.57 to 0.73) | 32/46 (70%; 57% to 83%) | 20/52 (38%; 27% to 52%) | 0.77 |
| newline (postans_slot1) | 0.94; 55/65 (85%); 8/76 (11%) | 0.91 (0.87 to 0.95) | 0.80 (0.74 to 0.86) | 36/46 (78%; 67% to 89%) | 10/52 (19%; 10% to 29%) | 0.93 |
| `<\|im_start\|>` (postans_slot2) | 0.77; 50/65 (77%); 23/76 (30%) | 0.71 (0.63 to 0.78) | 0.64 (0.55 to 0.73) | 29/46 (63%; 50% to 76%) | 18/52 (35%; 21% to 48%) | 0.77 |
| `user` (postans_slot3) | 0.76; 57/65 (88%); 28/76 (37%) | 0.69 (0.62 to 0.76) | 0.61 (0.54 to 0.69) | 29/46 (63%; 48% to 76%) | 21/52 (40%; 27% to 54%) | 0.75 |
| newline (postans_slot4) | 0.80; 50/65 (77%); 23/76 (30%) | 0.70 (0.63 to 0.78) | 0.66 (0.59 to 0.73) | 31/46 (67%; 54% to 80%) | 18/52 (35%; 23% to 48%) | 0.76 |

### Layer 50, lies against truths, all transcripts (build 151 / 81, held-out 101 / 54)

| token | build split: AUROC; lies above 0; truths above 0 | held-out AUROC | held-out balanced accuracy | held-out lies above 0 | held-out truths above 0 | both splits, five folds: AUROC |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.87; 129/151 (85%); 19/81 (23%) | 0.81 (0.75 to 0.87) | 0.73 (0.66 to 0.80) | 86/101 (85%; 77% to 92%) | 21/54 (39%; 26% to 52%) | 0.85 |
| newline (preans_slot1) | 0.95; 138/151 (91%); 11/81 (14%) | 0.94 (0.90 to 0.97) | 0.88 (0.82 to 0.92) | 89/101 (88%; 81% to 94%) | 7/54 (13%; 6% to 22%) | 0.94 |
| `<\|im_start\|>` (preans_slot2) | 0.85; 122/151 (81%); 29/81 (36%) | 0.87 (0.83 to 0.92) | 0.73 (0.67 to 0.80) | 79/101 (78%; 70% to 86%) | 17/54 (31%; 20% to 44%) | 0.85 |
| `assistant` (preans_slot3) | 0.92; 142/151 (94%); 22/81 (27%) | 0.87 (0.82 to 0.92) | 0.78 (0.72 to 0.85) | 91/101 (90%; 84% to 96%) | 18/54 (33%; 20% to 46%) | 0.91 |
| newline (preans_slot4) | 0.93; 126/151 (83%); 14/81 (17%) | 0.91 (0.87 to 0.95) | 0.85 (0.79 to 0.90) | 85/101 (84%; 77% to 91%) | 8/54 (15%; 6% to 26%) | 0.92 |
| `<think>` (think_slot0) | 0.80; 135/151 (89%); 41/81 (51%) | 0.79 (0.74 to 0.85) | 0.73 (0.67 to 0.78) | 87/101 (86%; 79% to 92%) | 22/54 (41%; 28% to 52%) | 0.79 |
| blank line (think_slot1) | 0.84; 138/151 (91%); 30/81 (37%) | 0.81 (0.75 to 0.87) | 0.72 (0.65 to 0.78) | 85/101 (84%; 77% to 91%) | 22/54 (41%; 28% to 54%) | 0.82 |
| `</think>` (think_slot2) | 0.90; 135/151 (89%); 21/81 (26%) | 0.86 (0.81 to 0.91) | 0.76 (0.70 to 0.82) | 82/101 (81%; 73% to 88%) | 16/54 (30%; 19% to 41%) | 0.89 |
| blank line (think_slot3) | 0.95; 134/151 (89%); 11/81 (14%) | 0.93 (0.89 to 0.96) | 0.84 (0.78 to 0.90) | 84/101 (83%; 76% to 90%) | 8/54 (15%; 6% to 24%) | 0.94 |
| the answer token (Yes / No) | 0.89; 86/151 (57%); 5/81 (6%) | 0.90 (0.84 to 0.94) | 0.75 (0.70 to 0.81) | 55/101 (54%; 45% to 64%) | 2/54 (4%; 0% to 9%) | 0.88 |
| `<\|im_end\|>` (postans_slot0) | 0.87; 110/151 (73%); 15/81 (19%) | 0.86 (0.80 to 0.91) | 0.78 (0.71 to 0.84) | 71/101 (70%; 60% to 78%) | 8/54 (15%; 6% to 24%) | 0.86 |
| newline (postans_slot1) | 0.95; 113/151 (75%); 5/81 (6%) | 0.93 (0.89 to 0.97) | 0.81 (0.76 to 0.86) | 67/101 (66%; 56% to 75%) | 2/54 (4%; 0% to 9%) | 0.94 |
| `<\|im_start\|>` (postans_slot2) | 0.88; 106/151 (70%); 9/81 (11%) | 0.84 (0.78 to 0.89) | 0.79 (0.74 to 0.84) | 63/101 (62%; 52% to 71%) | 2/54 (4%; 0% to 9%) | 0.86 |
| `user` (postans_slot3) | 0.90; 121/151 (80%); 13/81 (16%) | 0.87 (0.82 to 0.92) | 0.77 (0.70 to 0.83) | 76/101 (75%; 66% to 83%) | 12/54 (22%; 13% to 33%) | 0.88 |
| newline (postans_slot4) | 0.86; 118/151 (78%); 19/81 (23%) | 0.78 (0.73 to 0.83) | 0.70 (0.64 to 0.76) | 72/101 (71%; 62% to 79%) | 17/54 (31%; 20% to 43%) | 0.83 |

### Layer 50, lies against truths, among the No answers (build 65 / 76, held-out 46 / 52)

| token | build split: AUROC; lies above 0; truths above 0 | held-out AUROC | held-out balanced accuracy | held-out lies above 0 | held-out truths above 0 | both splits, five folds: AUROC |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.85; 53/65 (82%); 17/76 (22%) | 0.76 (0.69 to 0.83) | 0.69 (0.61 to 0.76) | 36/46 (78%; 65% to 89%) | 21/52 (40%; 29% to 54%) | 0.81 |
| newline (preans_slot1) | 0.93; 59/65 (91%); 15/76 (20%) | 0.91 (0.86 to 0.96) | 0.81 (0.74 to 0.88) | 38/46 (83%; 72% to 93%) | 11/52 (21%; 12% to 33%) | 0.92 |
| `<\|im_start\|>` (preans_slot2) | 0.82; 55/65 (85%); 32/76 (42%) | 0.87 (0.81 to 0.92) | 0.73 (0.65 to 0.79) | 34/46 (74%; 61% to 85%) | 15/52 (29%; 17% to 40%) | 0.84 |
| `assistant` (preans_slot3) | 0.83; 57/65 (88%); 28/76 (37%) | 0.74 (0.67 to 0.82) | 0.70 (0.62 to 0.77) | 36/46 (78%; 65% to 89%) | 20/52 (38%; 27% to 52%) | 0.82 |
| newline (preans_slot4) | 0.93; 57/65 (88%); 13/76 (17%) | 0.85 (0.79 to 0.91) | 0.81 (0.75 to 0.87) | 39/46 (85%; 74% to 93%) | 12/52 (23%; 13% to 35%) | 0.90 |
| `<think>` (think_slot0) | 0.77; 57/65 (88%); 37/76 (49%) | 0.72 (0.64 to 0.79) | 0.64 (0.57 to 0.71) | 37/46 (80%; 70% to 91%) | 27/52 (52%; 38% to 63%) | 0.74 |
| blank line (think_slot1) | 0.81; 58/65 (89%); 30/76 (39%) | 0.73 (0.66 to 0.80) | 0.69 (0.62 to 0.76) | 38/46 (83%; 72% to 93%) | 23/52 (44%; 33% to 58%) | 0.78 |
| `</think>` (think_slot2) | 0.85; 54/65 (83%); 22/76 (29%) | 0.75 (0.67 to 0.82) | 0.68 (0.61 to 0.76) | 31/46 (67%; 54% to 80%) | 16/52 (31%; 19% to 44%) | 0.83 |
| blank line (think_slot3) | 0.94; 58/65 (89%); 14/76 (18%) | 0.88 (0.82 to 0.94) | 0.77 (0.70 to 0.83) | 39/46 (85%; 74% to 93%) | 16/52 (31%; 19% to 44%) | 0.92 |
| the answer token (Yes / No) | 0.88; 55/65 (85%); 19/76 (25%) | 0.81 (0.74 to 0.87) | 0.76 (0.70 to 0.82) | 34/46 (74%; 61% to 85%) | 11/52 (21%; 12% to 33%) | 0.88 |
| `<\|im_end\|>` (postans_slot0) | 0.75; 51/65 (78%); 32/76 (42%) | 0.73 (0.65 to 0.81) | 0.66 (0.57 to 0.74) | 33/46 (72%; 59% to 85%) | 21/52 (40%; 27% to 54%) | 0.77 |
| newline (postans_slot1) | 0.94; 55/65 (85%); 9/76 (12%) | 0.91 (0.86 to 0.95) | 0.80 (0.73 to 0.86) | 37/46 (80%; 70% to 89%) | 11/52 (21%; 12% to 33%) | 0.92 |
| `<\|im_start\|>` (postans_slot2) | 0.80; 55/65 (85%); 25/76 (33%) | 0.74 (0.67 to 0.81) | 0.66 (0.58 to 0.74) | 31/46 (67%; 54% to 80%) | 18/52 (35%; 21% to 48%) | 0.80 |
| `user` (postans_slot3) | 0.79; 56/65 (86%); 28/76 (37%) | 0.73 (0.65 to 0.80) | 0.65 (0.57 to 0.73) | 34/46 (74%; 61% to 85%) | 23/52 (44%; 31% to 58%) | 0.80 |
| newline (postans_slot4) | 0.77; 47/65 (72%); 22/76 (29%) | 0.69 (0.61 to 0.77) | 0.66 (0.58 to 0.73) | 32/46 (70%; 57% to 83%) | 20/52 (38%; 25% to 52%) | 0.74 |

**The released did-you-lie probe** on the same transcripts (its own layer 50, the token before the answer), AUROC and, at its shipped threshold, the lies and truths flagged:

| task | build split: AUROC; lies flagged; truths flagged | held-out: AUROC; lies flagged; truths flagged |
|---|---|---|
| lies against truths, all transcripts | 0.27 (0.21 to 0.34); 69/151 (46%); 74/81 (91%) | 0.25 (0.19 to 0.32); 43/101 (43%); 50/54 (93%) |
| lies against truths, among the No answers | 0.55 (0.45 to 0.64); 58/65 (89%); 74/76 (97%) | 0.50 (0.40 to 0.61); 39/46 (85%); 50/52 (96%) |

## 4. Around the self-report answer, every wording, by layer: AUROC

Per wording and task, the tokens from the question to after the answer. Counts are the fit set's lies / truths (build split) and the held-out split's.

### Q1, lies against truths, all transcripts (build 95 / 61, held-out 63 / 41)

**Held-out (fitted on the build split)**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.91 | 0.92 | 0.93 (0.88 to 0.97) | 0.92 (0.87 to 0.97) | 0.89 | 0.85 |
| newline (preans_slot1) | 0.98 | 0.98 | 0.98 (0.95 to 1.00) | 0.97 (0.94 to 0.99) | 0.97 | 0.97 |
| `<\|im_start\|>` (preans_slot2) | 0.90 | 0.89 | 0.90 (0.85 to 0.95) | 0.83 (0.75 to 0.90) | 0.82 | 0.81 |
| `assistant` (preans_slot3) | 0.76 | 0.78 | 0.84 (0.76 to 0.91) | 0.86 (0.78 to 0.92) | 0.87 | 0.88 |
| newline (preans_slot4) | 0.94 | 0.92 | 0.92 (0.88 to 0.96) | 0.89 (0.84 to 0.94) | 0.86 | 0.84 |
| `<think>` (think_slot0) | 0.73 | 0.73 | 0.75 (0.66 to 0.83) | 0.76 (0.67 to 0.84) | 0.77 | 0.81 |
| blank line (think_slot1) | 0.76 | 0.78 | 0.80 (0.73 to 0.88) | 0.82 (0.75 to 0.89) | 0.84 | 0.83 |
| `</think>` (think_slot2) | 0.72 | 0.69 | 0.74 (0.65 to 0.82) | 0.75 (0.66 to 0.83) | 0.77 | 0.78 |
| blank line (think_slot3) | 0.87 | 0.86 | 0.91 (0.86 to 0.96) | 0.89 (0.83 to 0.94) | 0.88 | 0.87 |
| the answer token (Yes / No) | 0.91 | 0.88 | 0.86 (0.80 to 0.92) | 0.86 (0.79 to 0.91) | 0.85 | 0.85 |
| `<\|im_end\|>` (postans_slot0) | 0.73 | 0.73 | 0.75 (0.66 to 0.83) | 0.74 (0.66 to 0.82) | 0.70 | 0.70 |
| newline (postans_slot1) | 0.93 | 0.95 | 0.96 (0.92 to 0.99) | 0.96 (0.92 to 0.99) | 0.92 | 0.75 |
| `<\|im_start\|>` (postans_slot2) | 0.77 | 0.79 | 0.84 (0.77 to 0.91) | 0.85 (0.78 to 0.92) | 0.80 | 0.54 |
| `user` (postans_slot3) | 0.81 | 0.82 | 0.83 (0.75 to 0.89) | 0.85 (0.79 to 0.91) | 0.86 | 0.81 |
| newline (postans_slot4) | 0.87 | 0.78 | 0.77 (0.68 to 0.85) | 0.75 (0.66 to 0.83) | 0.73 | 0.73 |

**Build split, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.90 | 0.90 | 0.92 | 0.92 | 0.88 | 0.86 |
| newline (preans_slot1) | 0.97 | 0.98 | 0.97 | 0.97 | 0.96 | 0.96 |
| `<\|im_start\|>` (preans_slot2) | 0.92 | 0.91 | 0.91 | 0.87 | 0.86 | 0.84 |
| `assistant` (preans_slot3) | 0.78 | 0.82 | 0.85 | 0.87 | 0.89 | 0.90 |
| newline (preans_slot4) | 0.95 | 0.93 | 0.92 | 0.90 | 0.89 | 0.88 |
| `<think>` (think_slot0) | 0.70 | 0.72 | 0.76 | 0.76 | 0.79 | 0.82 |
| blank line (think_slot1) | 0.71 | 0.75 | 0.77 | 0.76 | 0.80 | 0.83 |
| `</think>` (think_slot2) | 0.74 | 0.72 | 0.79 | 0.80 | 0.81 | 0.82 |
| blank line (think_slot3) | 0.90 | 0.90 | 0.93 | 0.91 | 0.90 | 0.89 |
| the answer token (Yes / No) | 0.91 | 0.89 | 0.87 | 0.87 | 0.87 | 0.87 |
| `<\|im_end\|>` (postans_slot0) | 0.75 | 0.75 | 0.76 | 0.74 | 0.73 | 0.74 |
| newline (postans_slot1) | 0.94 | 0.94 | 0.95 | 0.94 | 0.91 | 0.76 |
| `<\|im_start\|>` (postans_slot2) | 0.78 | 0.79 | 0.82 | 0.84 | 0.74 | 0.48 |
| `user` (postans_slot3) | 0.81 | 0.80 | 0.83 | 0.86 | 0.86 | 0.84 |
| newline (postans_slot4) | 0.91 | 0.83 | 0.80 | 0.78 | 0.76 | 0.74 |

**Both splits, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.89 | 0.89 | 0.91 | 0.91 | 0.88 | 0.86 |
| newline (preans_slot1) | 0.97 | 0.98 | 0.97 | 0.97 | 0.96 | 0.96 |
| `<\|im_start\|>` (preans_slot2) | 0.91 | 0.90 | 0.90 | 0.86 | 0.84 | 0.81 |
| `assistant` (preans_slot3) | 0.79 | 0.83 | 0.86 | 0.88 | 0.89 | 0.89 |
| newline (preans_slot4) | 0.95 | 0.93 | 0.92 | 0.91 | 0.89 | 0.87 |
| `<think>` (think_slot0) | 0.72 | 0.72 | 0.74 | 0.75 | 0.77 | 0.81 |
| blank line (think_slot1) | 0.75 | 0.77 | 0.79 | 0.79 | 0.82 | 0.82 |
| `</think>` (think_slot2) | 0.76 | 0.73 | 0.80 | 0.82 | 0.83 | 0.84 |
| blank line (think_slot3) | 0.91 | 0.91 | 0.92 | 0.90 | 0.89 | 0.88 |
| the answer token (Yes / No) | 0.91 | 0.89 | 0.87 | 0.87 | 0.86 | 0.86 |
| `<\|im_end\|>` (postans_slot0) | 0.72 | 0.73 | 0.74 | 0.74 | 0.72 | 0.73 |
| newline (postans_slot1) | 0.93 | 0.94 | 0.95 | 0.93 | 0.87 | 0.81 |
| `<\|im_start\|>` (postans_slot2) | 0.78 | 0.79 | 0.81 | 0.82 | 0.76 | 0.53 |
| `user` (postans_slot3) | 0.80 | 0.78 | 0.79 | 0.82 | 0.84 | 0.81 |
| newline (postans_slot4) | 0.89 | 0.82 | 0.80 | 0.78 | 0.76 | 0.75 |

### Q1, lies against truths, among the No answers (build 43 / 57, held-out 32 / 40)

**Held-out (fitted on the build split)**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.82 | 0.84 | 0.81 (0.73 to 0.88) | 0.80 (0.73 to 0.88) | 0.79 | 0.78 |
| newline (preans_slot1) | 0.96 | 0.96 | 0.95 (0.90 to 1.00) | 0.95 (0.90 to 0.99) | 0.95 | 0.95 |
| `<\|im_start\|>` (preans_slot2) | 0.89 | 0.85 | 0.87 (0.79 to 0.94) | 0.78 (0.68 to 0.86) | 0.77 | 0.76 |
| `assistant` (preans_slot3) | 0.71 | 0.71 | 0.73 (0.64 to 0.82) | 0.73 (0.64 to 0.82) | 0.74 | 0.77 |
| newline (preans_slot4) | 0.88 | 0.86 | 0.90 (0.84 to 0.96) | 0.89 (0.83 to 0.95) | 0.88 | 0.79 |
| `<think>` (think_slot0) | 0.74 | 0.73 | 0.74 (0.66 to 0.82) | 0.74 (0.65 to 0.82) | 0.74 | 0.75 |
| blank line (think_slot1) | 0.67 | 0.69 | 0.71 (0.62 to 0.80) | 0.72 (0.63 to 0.81) | 0.72 | 0.74 |
| `</think>` (think_slot2) | 0.68 | 0.68 | 0.68 (0.59 to 0.78) | 0.68 (0.59 to 0.78) | 0.69 | 0.69 |
| blank line (think_slot3) | 0.76 | 0.76 | 0.78 (0.70 to 0.85) | 0.79 (0.71 to 0.86) | 0.79 | 0.79 |
| the answer token (Yes / No) | 0.74 | 0.72 | 0.72 (0.64 to 0.81) | 0.72 (0.63 to 0.81) | 0.72 | 0.72 |
| `<\|im_end\|>` (postans_slot0) | 0.68 | 0.65 | 0.68 (0.58 to 0.77) | 0.68 (0.58 to 0.77) | 0.68 | 0.69 |
| newline (postans_slot1) | 0.87 | 0.88 | 0.88 (0.82 to 0.94) | 0.81 (0.73 to 0.88) | 0.74 | 0.67 |
| `<\|im_start\|>` (postans_slot2) | 0.72 | 0.73 | 0.74 (0.65 to 0.82) | 0.72 (0.62 to 0.81) | 0.70 | 0.59 |
| `user` (postans_slot3) | 0.70 | 0.69 | 0.71 (0.62 to 0.80) | 0.72 (0.63 to 0.80) | 0.72 | 0.75 |
| newline (postans_slot4) | 0.84 | 0.84 | 0.85 (0.77 to 0.92) | 0.85 (0.77 to 0.93) | 0.84 | 0.82 |

**Build split, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.87 | 0.89 | 0.88 | 0.88 | 0.87 | 0.87 |
| newline (preans_slot1) | 0.97 | 0.97 | 0.96 | 0.96 | 0.95 | 0.95 |
| `<\|im_start\|>` (preans_slot2) | 0.90 | 0.88 | 0.90 | 0.85 | 0.83 | 0.80 |
| `assistant` (preans_slot3) | 0.78 | 0.79 | 0.80 | 0.80 | 0.83 | 0.86 |
| newline (preans_slot4) | 0.92 | 0.91 | 0.94 | 0.92 | 0.91 | 0.90 |
| `<think>` (think_slot0) | 0.75 | 0.77 | 0.77 | 0.77 | 0.78 | 0.79 |
| blank line (think_slot1) | 0.74 | 0.76 | 0.77 | 0.77 | 0.77 | 0.78 |
| `</think>` (think_slot2) | 0.75 | 0.75 | 0.75 | 0.76 | 0.77 | 0.78 |
| blank line (think_slot3) | 0.86 | 0.86 | 0.87 | 0.87 | 0.86 | 0.87 |
| the answer token (Yes / No) | 0.84 | 0.82 | 0.81 | 0.80 | 0.80 | 0.80 |
| `<\|im_end\|>` (postans_slot0) | 0.73 | 0.73 | 0.73 | 0.73 | 0.73 | 0.74 |
| newline (postans_slot1) | 0.90 | 0.91 | 0.91 | 0.86 | 0.81 | 0.76 |
| `<\|im_start\|>` (postans_slot2) | 0.75 | 0.74 | 0.73 | 0.72 | 0.70 | 0.60 |
| `user` (postans_slot3) | 0.74 | 0.75 | 0.75 | 0.77 | 0.79 | 0.80 |
| newline (postans_slot4) | 0.89 | 0.87 | 0.87 | 0.86 | 0.85 | 0.83 |

**Both splits, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.89 | 0.90 | 0.88 | 0.88 | 0.87 | 0.86 |
| newline (preans_slot1) | 0.97 | 0.96 | 0.96 | 0.95 | 0.95 | 0.95 |
| `<\|im_start\|>` (preans_slot2) | 0.90 | 0.88 | 0.89 | 0.83 | 0.80 | 0.78 |
| `assistant` (preans_slot3) | 0.77 | 0.77 | 0.79 | 0.79 | 0.81 | 0.84 |
| newline (preans_slot4) | 0.91 | 0.91 | 0.93 | 0.91 | 0.90 | 0.87 |
| `<think>` (think_slot0) | 0.75 | 0.76 | 0.76 | 0.76 | 0.77 | 0.78 |
| blank line (think_slot1) | 0.73 | 0.75 | 0.76 | 0.77 | 0.77 | 0.79 |
| `</think>` (think_slot2) | 0.73 | 0.73 | 0.73 | 0.73 | 0.74 | 0.75 |
| blank line (think_slot3) | 0.84 | 0.84 | 0.85 | 0.85 | 0.85 | 0.84 |
| the answer token (Yes / No) | 0.81 | 0.80 | 0.79 | 0.78 | 0.79 | 0.78 |
| `<\|im_end\|>` (postans_slot0) | 0.72 | 0.71 | 0.72 | 0.72 | 0.72 | 0.73 |
| newline (postans_slot1) | 0.90 | 0.90 | 0.90 | 0.86 | 0.80 | 0.73 |
| `<\|im_start\|>` (postans_slot2) | 0.75 | 0.75 | 0.74 | 0.74 | 0.70 | 0.60 |
| `user` (postans_slot3) | 0.75 | 0.73 | 0.74 | 0.76 | 0.78 | 0.79 |
| newline (postans_slot4) | 0.88 | 0.87 | 0.86 | 0.86 | 0.84 | 0.83 |

### Q2, lies against truths, all transcripts (build 152 / 81, held-out 101 / 54)

**Held-out (fitted on the build split)**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.84 | 0.85 | 0.88 (0.83 to 0.92) | 0.89 (0.85 to 0.93) | 0.89 | 0.88 |
| newline (preans_slot1) | 0.95 | 0.95 | 0.96 (0.94 to 0.98) | 0.95 (0.92 to 0.98) | 0.95 | 0.95 |
| `<\|im_start\|>` (preans_slot2) | 0.85 | 0.83 | 0.82 (0.77 to 0.88) | 0.77 (0.70 to 0.84) | 0.77 | 0.74 |
| `assistant` (preans_slot3) | 0.72 | 0.70 | 0.79 (0.72 to 0.85) | 0.86 (0.80 to 0.91) | 0.85 | 0.86 |
| newline (preans_slot4) | 0.91 | 0.89 | 0.89 (0.84 to 0.93) | 0.87 (0.82 to 0.92) | 0.85 | 0.85 |
| `<think>` (think_slot0) | 0.78 | 0.79 | 0.81 (0.75 to 0.86) | 0.82 (0.76 to 0.87) | 0.82 | 0.82 |
| blank line (think_slot1) | 0.81 | 0.83 | 0.83 (0.78 to 0.89) | 0.84 (0.78 to 0.89) | 0.84 | 0.84 |
| `</think>` (think_slot2) | 0.83 | 0.81 | 0.80 (0.73 to 0.86) | 0.86 (0.80 to 0.91) | 0.86 | 0.89 |
| blank line (think_slot3) | 0.91 | 0.92 | 0.93 (0.89 to 0.96) | 0.92 (0.88 to 0.95) | 0.91 | 0.90 |
| the answer token (Yes / No) | 0.86 | 0.84 | 0.83 (0.77 to 0.88) | 0.84 (0.78 to 0.89) | 0.86 | 0.86 |
| `<\|im_end\|>` (postans_slot0) | 0.85 | 0.85 | 0.86 (0.80 to 0.91) | 0.85 (0.80 to 0.91) | 0.85 | 0.86 |
| newline (postans_slot1) | 0.88 | 0.88 | 0.89 (0.84 to 0.93) | 0.89 (0.85 to 0.93) | 0.89 | 0.87 |
| `<\|im_start\|>` (postans_slot2) | 0.81 | 0.81 | 0.81 (0.76 to 0.87) | 0.82 (0.77 to 0.87) | 0.79 | 0.72 |
| `user` (postans_slot3) | 0.83 | 0.84 | 0.85 (0.80 to 0.90) | 0.85 (0.80 to 0.90) | 0.83 | 0.84 |
| newline (postans_slot4) | 0.86 | 0.83 | 0.82 (0.76 to 0.87) | 0.79 (0.73 to 0.84) | 0.78 | 0.75 |

**Build split, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.83 | 0.84 | 0.88 | 0.89 | 0.87 | 0.87 |
| newline (preans_slot1) | 0.96 | 0.97 | 0.96 | 0.95 | 0.95 | 0.95 |
| `<\|im_start\|>` (preans_slot2) | 0.88 | 0.86 | 0.88 | 0.85 | 0.81 | 0.79 |
| `assistant` (preans_slot3) | 0.79 | 0.80 | 0.87 | 0.93 | 0.93 | 0.92 |
| newline (preans_slot4) | 0.91 | 0.88 | 0.90 | 0.88 | 0.87 | 0.88 |
| `<think>` (think_slot0) | 0.75 | 0.76 | 0.80 | 0.81 | 0.81 | 0.83 |
| blank line (think_slot1) | 0.80 | 0.84 | 0.86 | 0.85 | 0.86 | 0.86 |
| `</think>` (think_slot2) | 0.83 | 0.84 | 0.87 | 0.92 | 0.92 | 0.93 |
| blank line (think_slot3) | 0.93 | 0.94 | 0.94 | 0.93 | 0.92 | 0.91 |
| the answer token (Yes / No) | 0.91 | 0.91 | 0.88 | 0.86 | 0.90 | 0.88 |
| `<\|im_end\|>` (postans_slot0) | 0.89 | 0.89 | 0.90 | 0.89 | 0.89 | 0.89 |
| newline (postans_slot1) | 0.93 | 0.93 | 0.95 | 0.94 | 0.94 | 0.92 |
| `<\|im_start\|>` (postans_slot2) | 0.85 | 0.85 | 0.85 | 0.86 | 0.85 | 0.81 |
| `user` (postans_slot3) | 0.84 | 0.85 | 0.87 | 0.88 | 0.85 | 0.87 |
| newline (postans_slot4) | 0.88 | 0.88 | 0.85 | 0.81 | 0.79 | 0.74 |

**Both splits, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.82 | 0.83 | 0.87 | 0.87 | 0.86 | 0.85 |
| newline (preans_slot1) | 0.96 | 0.96 | 0.96 | 0.95 | 0.95 | 0.95 |
| `<\|im_start\|>` (preans_slot2) | 0.87 | 0.86 | 0.87 | 0.84 | 0.81 | 0.78 |
| `assistant` (preans_slot3) | 0.82 | 0.83 | 0.88 | 0.91 | 0.91 | 0.91 |
| newline (preans_slot4) | 0.91 | 0.88 | 0.89 | 0.88 | 0.87 | 0.87 |
| `<think>` (think_slot0) | 0.77 | 0.77 | 0.79 | 0.80 | 0.81 | 0.81 |
| blank line (think_slot1) | 0.79 | 0.83 | 0.84 | 0.84 | 0.85 | 0.84 |
| `</think>` (think_slot2) | 0.82 | 0.84 | 0.88 | 0.91 | 0.92 | 0.92 |
| blank line (think_slot3) | 0.92 | 0.93 | 0.93 | 0.92 | 0.91 | 0.90 |
| the answer token (Yes / No) | 0.87 | 0.86 | 0.84 | 0.82 | 0.86 | 0.85 |
| `<\|im_end\|>` (postans_slot0) | 0.86 | 0.87 | 0.87 | 0.87 | 0.87 | 0.88 |
| newline (postans_slot1) | 0.91 | 0.91 | 0.93 | 0.93 | 0.92 | 0.90 |
| `<\|im_start\|>` (postans_slot2) | 0.83 | 0.83 | 0.83 | 0.84 | 0.81 | 0.77 |
| `user` (postans_slot3) | 0.82 | 0.82 | 0.83 | 0.84 | 0.80 | 0.81 |
| newline (postans_slot4) | 0.86 | 0.85 | 0.83 | 0.78 | 0.77 | 0.72 |

### Q2, lies against truths, among the No answers (build 47 / 77, held-out 33 / 48)

**Held-out (fitted on the build split)**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.70 | 0.72 | 0.74 (0.65 to 0.81) | 0.74 (0.65 to 0.82) | 0.73 | 0.71 |
| newline (preans_slot1) | 0.92 | 0.92 | 0.93 (0.88 to 0.97) | 0.92 (0.86 to 0.97) | 0.91 | 0.91 |
| `<\|im_start\|>` (preans_slot2) | 0.81 | 0.79 | 0.80 (0.73 to 0.87) | 0.74 (0.65 to 0.82) | 0.72 | 0.70 |
| `assistant` (preans_slot3) | 0.69 | 0.69 | 0.71 (0.62 to 0.79) | 0.72 (0.64 to 0.80) | 0.73 | 0.73 |
| newline (preans_slot4) | 0.81 | 0.81 | 0.83 (0.75 to 0.90) | 0.81 (0.73 to 0.89) | 0.81 | 0.81 |
| `<think>` (think_slot0) | 0.65 | 0.66 | 0.68 (0.59 to 0.77) | 0.67 (0.58 to 0.76) | 0.69 | 0.70 |
| blank line (think_slot1) | 0.65 | 0.68 | 0.68 (0.59 to 0.77) | 0.69 (0.60 to 0.78) | 0.69 | 0.69 |
| `</think>` (think_slot2) | 0.65 | 0.66 | 0.67 (0.58 to 0.76) | 0.69 (0.60 to 0.77) | 0.70 | 0.70 |
| blank line (think_slot3) | 0.73 | 0.74 | 0.80 (0.74 to 0.87) | 0.80 (0.74 to 0.86) | 0.79 | 0.78 |
| the answer token (Yes / No) | 0.77 | 0.72 | 0.73 (0.64 to 0.81) | 0.71 (0.62 to 0.79) | 0.69 | 0.69 |
| `<\|im_end\|>` (postans_slot0) | 0.67 | 0.68 | 0.68 (0.59 to 0.76) | 0.68 (0.59 to 0.76) | 0.68 | 0.69 |
| newline (postans_slot1) | 0.85 | 0.86 | 0.86 (0.80 to 0.92) | 0.82 (0.75 to 0.88) | 0.77 | 0.71 |
| `<\|im_start\|>` (postans_slot2) | 0.68 | 0.68 | 0.68 (0.60 to 0.77) | 0.68 (0.59 to 0.77) | 0.68 | 0.62 |
| `user` (postans_slot3) | 0.67 | 0.67 | 0.67 (0.60 to 0.75) | 0.68 (0.61 to 0.76) | 0.67 | 0.67 |
| newline (postans_slot4) | 0.71 | 0.71 | 0.72 (0.63 to 0.81) | 0.72 (0.63 to 0.80) | 0.70 | 0.63 |

**Build split, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.82 | 0.84 | 0.87 | 0.87 | 0.86 | 0.85 |
| newline (preans_slot1) | 0.95 | 0.95 | 0.95 | 0.94 | 0.93 | 0.93 |
| `<\|im_start\|>` (preans_slot2) | 0.85 | 0.82 | 0.86 | 0.84 | 0.81 | 0.80 |
| `assistant` (preans_slot3) | 0.80 | 0.80 | 0.81 | 0.82 | 0.84 | 0.84 |
| newline (preans_slot4) | 0.89 | 0.88 | 0.89 | 0.89 | 0.89 | 0.85 |
| `<think>` (think_slot0) | 0.76 | 0.77 | 0.78 | 0.78 | 0.79 | 0.79 |
| blank line (think_slot1) | 0.76 | 0.79 | 0.80 | 0.80 | 0.79 | 0.80 |
| `</think>` (think_slot2) | 0.79 | 0.80 | 0.83 | 0.84 | 0.84 | 0.85 |
| blank line (think_slot3) | 0.86 | 0.87 | 0.90 | 0.90 | 0.89 | 0.89 |
| the answer token (Yes / No) | 0.87 | 0.85 | 0.86 | 0.84 | 0.83 | 0.82 |
| `<\|im_end\|>` (postans_slot0) | 0.74 | 0.75 | 0.75 | 0.75 | 0.76 | 0.77 |
| newline (postans_slot1) | 0.89 | 0.90 | 0.91 | 0.86 | 0.83 | 0.78 |
| `<\|im_start\|>` (postans_slot2) | 0.75 | 0.74 | 0.74 | 0.75 | 0.76 | 0.74 |
| `user` (postans_slot3) | 0.76 | 0.76 | 0.76 | 0.77 | 0.77 | 0.78 |
| newline (postans_slot4) | 0.82 | 0.83 | 0.82 | 0.77 | 0.75 | 0.71 |

**Both splits, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.79 | 0.81 | 0.84 | 0.83 | 0.82 | 0.80 |
| newline (preans_slot1) | 0.94 | 0.94 | 0.94 | 0.93 | 0.92 | 0.92 |
| `<\|im_start\|>` (preans_slot2) | 0.83 | 0.80 | 0.83 | 0.80 | 0.78 | 0.76 |
| `assistant` (preans_slot3) | 0.76 | 0.76 | 0.78 | 0.79 | 0.81 | 0.81 |
| newline (preans_slot4) | 0.87 | 0.86 | 0.87 | 0.87 | 0.87 | 0.85 |
| `<think>` (think_slot0) | 0.72 | 0.73 | 0.74 | 0.74 | 0.75 | 0.76 |
| blank line (think_slot1) | 0.73 | 0.75 | 0.76 | 0.76 | 0.76 | 0.76 |
| `</think>` (think_slot2) | 0.74 | 0.76 | 0.77 | 0.79 | 0.79 | 0.80 |
| blank line (think_slot3) | 0.82 | 0.83 | 0.88 | 0.88 | 0.86 | 0.85 |
| the answer token (Yes / No) | 0.85 | 0.82 | 0.82 | 0.81 | 0.79 | 0.78 |
| `<\|im_end\|>` (postans_slot0) | 0.72 | 0.72 | 0.72 | 0.72 | 0.73 | 0.73 |
| newline (postans_slot1) | 0.88 | 0.89 | 0.90 | 0.86 | 0.82 | 0.76 |
| `<\|im_start\|>` (postans_slot2) | 0.73 | 0.72 | 0.72 | 0.73 | 0.73 | 0.74 |
| `user` (postans_slot3) | 0.73 | 0.73 | 0.73 | 0.74 | 0.74 | 0.74 |
| newline (postans_slot4) | 0.79 | 0.79 | 0.80 | 0.75 | 0.73 | 0.68 |

### Q6, lies against truths, all transcripts (build 152 / 81, held-out 101 / 54)

**Held-out (fitted on the build split)**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.85 | 0.87 | 0.91 (0.88 to 0.95) | 0.92 (0.88 to 0.95) | 0.90 | 0.89 |
| newline (preans_slot1) | 0.95 | 0.94 | 0.95 (0.92 to 0.98) | 0.94 (0.90 to 0.97) | 0.92 | 0.91 |
| `<\|im_start\|>` (preans_slot2) | 0.86 | 0.82 | 0.82 (0.77 to 0.88) | 0.77 (0.71 to 0.83) | 0.75 | 0.74 |
| `assistant` (preans_slot3) | 0.67 | 0.63 | 0.71 (0.65 to 0.78) | 0.79 (0.74 to 0.85) | 0.75 | 0.78 |
| newline (preans_slot4) | 0.92 | 0.90 | 0.92 (0.88 to 0.95) | 0.90 (0.85 to 0.94) | 0.90 | 0.90 |
| `<think>` (think_slot0) | 0.77 | 0.77 | 0.80 (0.74 to 0.85) | 0.81 (0.75 to 0.86) | 0.80 | 0.80 |
| blank line (think_slot1) | 0.81 | 0.82 | 0.83 (0.77 to 0.88) | 0.84 (0.79 to 0.89) | 0.84 | 0.84 |
| `</think>` (think_slot2) | 0.83 | 0.80 | 0.83 (0.77 to 0.89) | 0.87 (0.82 to 0.92) | 0.88 | 0.89 |
| blank line (think_slot3) | 0.88 | 0.90 | 0.94 (0.90 to 0.97) | 0.92 (0.88 to 0.95) | 0.92 | 0.91 |
| the answer token (Yes / No) | 0.86 | 0.86 | 0.86 (0.82 to 0.91) | 0.86 (0.80 to 0.91) | 0.86 | 0.85 |
| `<\|im_end\|>` (postans_slot0) | 0.84 | 0.85 | 0.86 (0.81 to 0.92) | 0.85 (0.80 to 0.91) | 0.85 | 0.85 |
| newline (postans_slot1) | 0.90 | 0.90 | 0.91 (0.87 to 0.94) | 0.90 (0.86 to 0.94) | 0.89 | 0.86 |
| `<\|im_start\|>` (postans_slot2) | 0.80 | 0.80 | 0.83 (0.78 to 0.88) | 0.83 (0.78 to 0.89) | 0.82 | 0.76 |
| `user` (postans_slot3) | 0.84 | 0.85 | 0.86 (0.81 to 0.91) | 0.84 (0.78 to 0.90) | 0.82 | 0.81 |
| newline (postans_slot4) | 0.86 | 0.85 | 0.81 (0.76 to 0.86) | 0.78 (0.73 to 0.84) | 0.77 | 0.77 |

**Build split, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.82 | 0.84 | 0.89 | 0.89 | 0.85 | 0.85 |
| newline (preans_slot1) | 0.93 | 0.95 | 0.94 | 0.92 | 0.90 | 0.89 |
| `<\|im_start\|>` (preans_slot2) | 0.88 | 0.85 | 0.84 | 0.79 | 0.75 | 0.74 |
| `assistant` (preans_slot3) | 0.76 | 0.74 | 0.82 | 0.89 | 0.87 | 0.87 |
| newline (preans_slot4) | 0.93 | 0.92 | 0.92 | 0.90 | 0.90 | 0.90 |
| `<think>` (think_slot0) | 0.76 | 0.77 | 0.79 | 0.80 | 0.80 | 0.81 |
| blank line (think_slot1) | 0.79 | 0.83 | 0.84 | 0.83 | 0.84 | 0.83 |
| `</think>` (think_slot2) | 0.83 | 0.83 | 0.87 | 0.91 | 0.91 | 0.91 |
| blank line (think_slot3) | 0.92 | 0.93 | 0.95 | 0.93 | 0.92 | 0.91 |
| the answer token (Yes / No) | 0.88 | 0.89 | 0.88 | 0.86 | 0.88 | 0.88 |
| `<\|im_end\|>` (postans_slot0) | 0.86 | 0.86 | 0.87 | 0.87 | 0.87 | 0.88 |
| newline (postans_slot1) | 0.92 | 0.92 | 0.92 | 0.91 | 0.91 | 0.88 |
| `<\|im_start\|>` (postans_slot2) | 0.82 | 0.84 | 0.86 | 0.86 | 0.85 | 0.84 |
| `user` (postans_slot3) | 0.85 | 0.88 | 0.89 | 0.88 | 0.87 | 0.88 |
| newline (postans_slot4) | 0.88 | 0.86 | 0.79 | 0.76 | 0.75 | 0.76 |

**Both splits, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.82 | 0.84 | 0.88 | 0.88 | 0.85 | 0.84 |
| newline (preans_slot1) | 0.94 | 0.95 | 0.95 | 0.92 | 0.90 | 0.89 |
| `<\|im_start\|>` (preans_slot2) | 0.88 | 0.86 | 0.86 | 0.81 | 0.78 | 0.76 |
| `assistant` (preans_slot3) | 0.76 | 0.74 | 0.83 | 0.90 | 0.87 | 0.88 |
| newline (preans_slot4) | 0.93 | 0.91 | 0.92 | 0.90 | 0.90 | 0.89 |
| `<think>` (think_slot0) | 0.77 | 0.77 | 0.79 | 0.80 | 0.80 | 0.79 |
| blank line (think_slot1) | 0.79 | 0.82 | 0.84 | 0.83 | 0.83 | 0.82 |
| `</think>` (think_slot2) | 0.83 | 0.84 | 0.88 | 0.91 | 0.91 | 0.91 |
| blank line (think_slot3) | 0.92 | 0.93 | 0.94 | 0.93 | 0.92 | 0.91 |
| the answer token (Yes / No) | 0.86 | 0.87 | 0.87 | 0.85 | 0.87 | 0.87 |
| `<\|im_end\|>` (postans_slot0) | 0.85 | 0.86 | 0.87 | 0.87 | 0.87 | 0.87 |
| newline (postans_slot1) | 0.91 | 0.92 | 0.92 | 0.91 | 0.91 | 0.86 |
| `<\|im_start\|>` (postans_slot2) | 0.81 | 0.82 | 0.84 | 0.84 | 0.83 | 0.80 |
| `user` (postans_slot3) | 0.83 | 0.85 | 0.86 | 0.86 | 0.84 | 0.85 |
| newline (postans_slot4) | 0.87 | 0.84 | 0.78 | 0.75 | 0.74 | 0.74 |

### Q6, lies against truths, among the No answers (build 43 / 73, held-out 21 / 45)

**Held-out (fitted on the build split)**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.67 | 0.67 | 0.68 (0.57 to 0.78) | 0.66 (0.54 to 0.77) | 0.68 | 0.65 |
| newline (preans_slot1) | 0.86 | 0.86 | 0.87 (0.77 to 0.95) | 0.86 (0.76 to 0.94) | 0.86 | 0.86 |
| `<\|im_start\|>` (preans_slot2) | 0.80 | 0.73 | 0.71 (0.58 to 0.83) | 0.67 (0.54 to 0.78) | 0.61 | 0.62 |
| `assistant` (preans_slot3) | 0.66 | 0.65 | 0.65 (0.52 to 0.77) | 0.64 (0.51 to 0.76) | 0.64 | 0.64 |
| newline (preans_slot4) | 0.77 | 0.79 | 0.81 (0.71 to 0.89) | 0.80 (0.69 to 0.89) | 0.77 | 0.77 |
| `<think>` (think_slot0) | 0.66 | 0.66 | 0.66 (0.55 to 0.77) | 0.67 (0.56 to 0.78) | 0.68 | 0.69 |
| blank line (think_slot1) | 0.64 | 0.66 | 0.66 (0.54 to 0.77) | 0.66 (0.54 to 0.77) | 0.66 | 0.66 |
| `</think>` (think_slot2) | 0.64 | 0.64 | 0.66 (0.55 to 0.77) | 0.67 (0.55 to 0.78) | 0.68 | 0.69 |
| blank line (think_slot3) | 0.70 | 0.71 | 0.76 (0.66 to 0.86) | 0.78 (0.68 to 0.87) | 0.76 | 0.77 |
| the answer token (Yes / No) | 0.74 | 0.72 | 0.73 (0.64 to 0.82) | 0.70 (0.60 to 0.79) | 0.67 | 0.67 |
| `<\|im_end\|>` (postans_slot0) | 0.63 | 0.63 | 0.65 (0.53 to 0.75) | 0.65 (0.53 to 0.75) | 0.66 | 0.67 |
| newline (postans_slot1) | 0.83 | 0.83 | 0.84 (0.76 to 0.92) | 0.78 (0.69 to 0.87) | 0.74 | 0.68 |
| `<\|im_start\|>` (postans_slot2) | 0.66 | 0.65 | 0.66 (0.54 to 0.76) | 0.66 (0.55 to 0.77) | 0.65 | 0.66 |
| `user` (postans_slot3) | 0.63 | 0.62 | 0.63 (0.52 to 0.74) | 0.62 (0.51 to 0.73) | 0.60 | 0.58 |
| newline (postans_slot4) | 0.68 | 0.66 | 0.65 (0.54 to 0.75) | 0.63 (0.53 to 0.73) | 0.61 | 0.58 |

**Build split, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.77 | 0.77 | 0.79 | 0.78 | 0.78 | 0.78 |
| newline (preans_slot1) | 0.92 | 0.93 | 0.93 | 0.91 | 0.91 | 0.90 |
| `<\|im_start\|>` (preans_slot2) | 0.87 | 0.83 | 0.82 | 0.79 | 0.76 | 0.75 |
| `assistant` (preans_slot3) | 0.78 | 0.78 | 0.79 | 0.81 | 0.82 | 0.82 |
| newline (preans_slot4) | 0.88 | 0.89 | 0.89 | 0.88 | 0.90 | 0.90 |
| `<think>` (think_slot0) | 0.76 | 0.77 | 0.78 | 0.78 | 0.78 | 0.79 |
| blank line (think_slot1) | 0.75 | 0.77 | 0.78 | 0.78 | 0.77 | 0.78 |
| `</think>` (think_slot2) | 0.76 | 0.76 | 0.78 | 0.78 | 0.78 | 0.80 |
| blank line (think_slot3) | 0.84 | 0.85 | 0.89 | 0.90 | 0.90 | 0.87 |
| the answer token (Yes / No) | 0.85 | 0.82 | 0.84 | 0.83 | 0.79 | 0.79 |
| `<\|im_end\|>` (postans_slot0) | 0.72 | 0.73 | 0.73 | 0.73 | 0.74 | 0.75 |
| newline (postans_slot1) | 0.90 | 0.90 | 0.91 | 0.86 | 0.83 | 0.77 |
| `<\|im_start\|>` (postans_slot2) | 0.73 | 0.72 | 0.72 | 0.73 | 0.73 | 0.74 |
| `user` (postans_slot3) | 0.74 | 0.74 | 0.74 | 0.74 | 0.73 | 0.73 |
| newline (postans_slot4) | 0.79 | 0.78 | 0.71 | 0.66 | 0.65 | 0.61 |

**Both splits, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.74 | 0.75 | 0.77 | 0.76 | 0.75 | 0.74 |
| newline (preans_slot1) | 0.91 | 0.91 | 0.91 | 0.89 | 0.90 | 0.90 |
| `<\|im_start\|>` (preans_slot2) | 0.88 | 0.84 | 0.82 | 0.78 | 0.73 | 0.71 |
| `assistant` (preans_slot3) | 0.73 | 0.73 | 0.74 | 0.75 | 0.75 | 0.76 |
| newline (preans_slot4) | 0.85 | 0.85 | 0.87 | 0.85 | 0.86 | 0.86 |
| `<think>` (think_slot0) | 0.72 | 0.73 | 0.73 | 0.74 | 0.74 | 0.74 |
| blank line (think_slot1) | 0.71 | 0.73 | 0.74 | 0.74 | 0.74 | 0.73 |
| `</think>` (think_slot2) | 0.72 | 0.72 | 0.74 | 0.75 | 0.75 | 0.76 |
| blank line (think_slot3) | 0.79 | 0.80 | 0.86 | 0.86 | 0.85 | 0.83 |
| the answer token (Yes / No) | 0.82 | 0.80 | 0.82 | 0.80 | 0.76 | 0.75 |
| `<\|im_end\|>` (postans_slot0) | 0.69 | 0.69 | 0.70 | 0.70 | 0.71 | 0.72 |
| newline (postans_slot1) | 0.88 | 0.89 | 0.89 | 0.84 | 0.80 | 0.74 |
| `<\|im_start\|>` (postans_slot2) | 0.71 | 0.70 | 0.70 | 0.70 | 0.71 | 0.70 |
| `user` (postans_slot3) | 0.70 | 0.70 | 0.70 | 0.69 | 0.68 | 0.68 |
| newline (postans_slot4) | 0.76 | 0.75 | 0.71 | 0.65 | 0.64 | 0.60 |

### Q7, lies against truths, all transcripts (build 152 / 81, held-out 101 / 54)

**Held-out (fitted on the build split)**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.84 | 0.84 | 0.90 (0.85 to 0.94) | 0.91 (0.87 to 0.95) | 0.88 | 0.87 |
| newline (preans_slot1) | 0.89 | 0.87 | 0.84 (0.79 to 0.89) | 0.83 (0.77 to 0.88) | 0.80 | 0.80 |
| `<\|im_start\|>` (preans_slot2) | 0.84 | 0.79 | 0.82 (0.76 to 0.87) | 0.76 (0.70 to 0.82) | 0.75 | 0.74 |
| `assistant` (preans_slot3) | 0.75 | 0.70 | 0.83 (0.77 to 0.89) | 0.85 (0.79 to 0.90) | 0.83 | 0.81 |
| newline (preans_slot4) | 0.92 | 0.89 | 0.86 (0.81 to 0.91) | 0.84 (0.79 to 0.90) | 0.85 | 0.83 |
| `<think>` (think_slot0) | 0.79 | 0.80 | 0.81 (0.76 to 0.87) | 0.82 (0.77 to 0.87) | 0.82 | 0.81 |
| blank line (think_slot1) | 0.82 | 0.83 | 0.83 (0.77 to 0.88) | 0.83 (0.78 to 0.89) | 0.83 | 0.83 |
| `</think>` (think_slot2) | 0.84 | 0.83 | 0.85 (0.79 to 0.91) | 0.86 (0.81 to 0.92) | 0.86 | 0.87 |
| blank line (think_slot3) | 0.89 | 0.89 | 0.90 (0.85 to 0.94) | 0.86 (0.81 to 0.92) | 0.85 | 0.86 |
| the answer token (Yes / No) | 0.85 | 0.84 | 0.85 (0.78 to 0.91) | 0.87 (0.80 to 0.93) | 0.84 | 0.83 |
| `<\|im_end\|>` (postans_slot0) | 0.83 | 0.82 | 0.85 (0.79 to 0.90) | 0.86 (0.80 to 0.91) | 0.85 | 0.86 |
| newline (postans_slot1) | 0.90 | 0.91 | 0.91 (0.85 to 0.96) | 0.91 (0.85 to 0.95) | 0.91 | 0.89 |
| `<\|im_start\|>` (postans_slot2) | 0.86 | 0.85 | 0.86 (0.80 to 0.91) | 0.87 (0.81 to 0.92) | 0.88 | 0.87 |
| `user` (postans_slot3) | 0.81 | 0.82 | 0.82 (0.76 to 0.87) | 0.83 (0.77 to 0.89) | 0.82 | 0.83 |
| newline (postans_slot4) | 0.84 | 0.82 | 0.83 (0.78 to 0.88) | 0.81 (0.75 to 0.87) | 0.80 | 0.76 |

**Build split, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.83 | 0.83 | 0.88 | 0.89 | 0.88 | 0.88 |
| newline (preans_slot1) | 0.89 | 0.88 | 0.85 | 0.84 | 0.81 | 0.80 |
| `<\|im_start\|>` (preans_slot2) | 0.87 | 0.82 | 0.83 | 0.78 | 0.76 | 0.74 |
| `assistant` (preans_slot3) | 0.80 | 0.77 | 0.90 | 0.91 | 0.90 | 0.88 |
| newline (preans_slot4) | 0.93 | 0.89 | 0.88 | 0.88 | 0.87 | 0.85 |
| `<think>` (think_slot0) | 0.78 | 0.79 | 0.80 | 0.81 | 0.82 | 0.81 |
| blank line (think_slot1) | 0.82 | 0.85 | 0.86 | 0.87 | 0.87 | 0.85 |
| `</think>` (think_slot2) | 0.86 | 0.86 | 0.89 | 0.90 | 0.90 | 0.90 |
| blank line (think_slot3) | 0.94 | 0.94 | 0.91 | 0.89 | 0.87 | 0.87 |
| the answer token (Yes / No) | 0.85 | 0.84 | 0.86 | 0.90 | 0.88 | 0.86 |
| `<\|im_end\|>` (postans_slot0) | 0.81 | 0.81 | 0.85 | 0.86 | 0.87 | 0.87 |
| newline (postans_slot1) | 0.92 | 0.93 | 0.94 | 0.94 | 0.94 | 0.91 |
| `<\|im_start\|>` (postans_slot2) | 0.87 | 0.86 | 0.89 | 0.89 | 0.88 | 0.89 |
| `user` (postans_slot3) | 0.82 | 0.84 | 0.83 | 0.84 | 0.81 | 0.81 |
| newline (postans_slot4) | 0.86 | 0.86 | 0.85 | 0.82 | 0.81 | 0.76 |

**Both splits, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.82 | 0.82 | 0.88 | 0.90 | 0.87 | 0.87 |
| newline (preans_slot1) | 0.89 | 0.87 | 0.85 | 0.83 | 0.80 | 0.79 |
| `<\|im_start\|>` (preans_slot2) | 0.87 | 0.83 | 0.83 | 0.80 | 0.78 | 0.76 |
| `assistant` (preans_slot3) | 0.81 | 0.77 | 0.89 | 0.89 | 0.89 | 0.87 |
| newline (preans_slot4) | 0.92 | 0.89 | 0.88 | 0.87 | 0.86 | 0.84 |
| `<think>` (think_slot0) | 0.78 | 0.78 | 0.80 | 0.80 | 0.81 | 0.80 |
| blank line (think_slot1) | 0.81 | 0.84 | 0.83 | 0.84 | 0.84 | 0.83 |
| `</think>` (think_slot2) | 0.84 | 0.87 | 0.90 | 0.90 | 0.90 | 0.90 |
| blank line (think_slot3) | 0.93 | 0.93 | 0.90 | 0.88 | 0.87 | 0.86 |
| the answer token (Yes / No) | 0.85 | 0.83 | 0.84 | 0.88 | 0.87 | 0.86 |
| `<\|im_end\|>` (postans_slot0) | 0.81 | 0.82 | 0.85 | 0.86 | 0.86 | 0.87 |
| newline (postans_slot1) | 0.91 | 0.92 | 0.93 | 0.93 | 0.92 | 0.90 |
| `<\|im_start\|>` (postans_slot2) | 0.87 | 0.86 | 0.88 | 0.88 | 0.86 | 0.86 |
| `user` (postans_slot3) | 0.81 | 0.83 | 0.83 | 0.83 | 0.81 | 0.82 |
| newline (postans_slot4) | 0.86 | 0.85 | 0.84 | 0.84 | 0.82 | 0.80 |

### Q7, lies against truths, among the No answers (build 79 / 77, held-out 54 / 50)

**Held-out (fitted on the build split)**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.78 | 0.77 | 0.80 (0.74 to 0.87) | 0.78 (0.70 to 0.84) | 0.79 | 0.77 |
| newline (preans_slot1) | 0.88 | 0.85 | 0.82 (0.75 to 0.88) | 0.79 (0.72 to 0.86) | 0.76 | 0.76 |
| `<\|im_start\|>` (preans_slot2) | 0.87 | 0.84 | 0.84 (0.78 to 0.90) | 0.80 (0.72 to 0.87) | 0.76 | 0.73 |
| `assistant` (preans_slot3) | 0.70 | 0.69 | 0.76 (0.69 to 0.84) | 0.78 (0.71 to 0.85) | 0.77 | 0.77 |
| newline (preans_slot4) | 0.88 | 0.90 | 0.91 (0.85 to 0.95) | 0.89 (0.84 to 0.94) | 0.88 | 0.87 |
| `<think>` (think_slot0) | 0.73 | 0.75 | 0.77 (0.70 to 0.84) | 0.78 (0.72 to 0.85) | 0.78 | 0.81 |
| blank line (think_slot1) | 0.71 | 0.74 | 0.74 (0.67 to 0.81) | 0.77 (0.71 to 0.84) | 0.77 | 0.79 |
| `</think>` (think_slot2) | 0.72 | 0.71 | 0.73 (0.64 to 0.81) | 0.76 (0.68 to 0.84) | 0.75 | 0.75 |
| blank line (think_slot3) | 0.79 | 0.80 | 0.87 (0.81 to 0.92) | 0.84 (0.77 to 0.90) | 0.82 | 0.83 |
| the answer token (Yes / No) | 0.82 | 0.73 | 0.78 (0.72 to 0.85) | 0.82 (0.76 to 0.88) | 0.78 | 0.75 |
| `<\|im_end\|>` (postans_slot0) | 0.66 | 0.66 | 0.69 (0.61 to 0.78) | 0.71 (0.63 to 0.79) | 0.75 | 0.80 |
| newline (postans_slot1) | 0.91 | 0.92 | 0.92 (0.88 to 0.95) | 0.90 (0.86 to 0.94) | 0.91 | 0.89 |
| `<\|im_start\|>` (postans_slot2) | 0.73 | 0.73 | 0.74 (0.67 to 0.81) | 0.76 (0.70 to 0.83) | 0.75 | 0.75 |
| `user` (postans_slot3) | 0.67 | 0.64 | 0.64 (0.56 to 0.71) | 0.66 (0.58 to 0.73) | 0.62 | 0.63 |
| newline (postans_slot4) | 0.72 | 0.76 | 0.79 (0.73 to 0.86) | 0.79 (0.72 to 0.85) | 0.78 | 0.70 |

**Build split, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.82 | 0.80 | 0.82 | 0.81 | 0.82 | 0.81 |
| newline (preans_slot1) | 0.91 | 0.88 | 0.86 | 0.83 | 0.79 | 0.78 |
| `<\|im_start\|>` (preans_slot2) | 0.89 | 0.84 | 0.83 | 0.77 | 0.75 | 0.73 |
| `assistant` (preans_slot3) | 0.75 | 0.75 | 0.81 | 0.83 | 0.83 | 0.83 |
| newline (preans_slot4) | 0.92 | 0.93 | 0.93 | 0.91 | 0.91 | 0.90 |
| `<think>` (think_slot0) | 0.75 | 0.76 | 0.79 | 0.80 | 0.81 | 0.81 |
| blank line (think_slot1) | 0.76 | 0.77 | 0.79 | 0.80 | 0.81 | 0.81 |
| `</think>` (think_slot2) | 0.78 | 0.77 | 0.79 | 0.82 | 0.81 | 0.82 |
| blank line (think_slot3) | 0.86 | 0.86 | 0.89 | 0.85 | 0.83 | 0.83 |
| the answer token (Yes / No) | 0.87 | 0.80 | 0.84 | 0.86 | 0.82 | 0.80 |
| `<\|im_end\|>` (postans_slot0) | 0.71 | 0.70 | 0.74 | 0.76 | 0.78 | 0.81 |
| newline (postans_slot1) | 0.94 | 0.95 | 0.95 | 0.94 | 0.94 | 0.91 |
| `<\|im_start\|>` (postans_slot2) | 0.78 | 0.77 | 0.79 | 0.81 | 0.80 | 0.80 |
| `user` (postans_slot3) | 0.72 | 0.70 | 0.70 | 0.71 | 0.70 | 0.71 |
| newline (postans_slot4) | 0.79 | 0.82 | 0.85 | 0.77 | 0.75 | 0.69 |

**Both splits, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.87 | 0.83 | 0.85 | 0.82 | 0.85 | 0.84 |
| newline (preans_slot1) | 0.90 | 0.87 | 0.84 | 0.81 | 0.77 | 0.75 |
| `<\|im_start\|>` (preans_slot2) | 0.89 | 0.85 | 0.84 | 0.79 | 0.76 | 0.74 |
| `assistant` (preans_slot3) | 0.74 | 0.74 | 0.80 | 0.82 | 0.82 | 0.82 |
| newline (preans_slot4) | 0.92 | 0.93 | 0.92 | 0.90 | 0.90 | 0.90 |
| `<think>` (think_slot0) | 0.75 | 0.78 | 0.80 | 0.81 | 0.81 | 0.82 |
| blank line (think_slot1) | 0.78 | 0.79 | 0.81 | 0.82 | 0.82 | 0.83 |
| `</think>` (think_slot2) | 0.79 | 0.77 | 0.80 | 0.82 | 0.81 | 0.82 |
| blank line (think_slot3) | 0.86 | 0.86 | 0.87 | 0.84 | 0.82 | 0.82 |
| the answer token (Yes / No) | 0.89 | 0.80 | 0.85 | 0.87 | 0.82 | 0.80 |
| `<\|im_end\|>` (postans_slot0) | 0.71 | 0.70 | 0.75 | 0.76 | 0.79 | 0.83 |
| newline (postans_slot1) | 0.93 | 0.93 | 0.94 | 0.93 | 0.93 | 0.89 |
| `<\|im_start\|>` (postans_slot2) | 0.78 | 0.78 | 0.79 | 0.81 | 0.81 | 0.79 |
| `user` (postans_slot3) | 0.72 | 0.69 | 0.68 | 0.71 | 0.68 | 0.69 |
| newline (postans_slot4) | 0.80 | 0.82 | 0.84 | 0.81 | 0.79 | 0.74 |

### Q9, lies against truths, all transcripts (build 151 / 81, held-out 101 / 54)

**Held-out (fitted on the build split)**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.84 | 0.84 | 0.85 (0.80 to 0.90) | 0.81 (0.75 to 0.87) | 0.80 | 0.78 |
| newline (preans_slot1) | 0.95 | 0.95 | 0.95 (0.92 to 0.98) | 0.94 (0.90 to 0.97) | 0.94 | 0.93 |
| `<\|im_start\|>` (preans_slot2) | 0.93 | 0.92 | 0.90 (0.87 to 0.94) | 0.87 (0.83 to 0.92) | 0.86 | 0.84 |
| `assistant` (preans_slot3) | 0.73 | 0.69 | 0.80 (0.74 to 0.86) | 0.87 (0.82 to 0.92) | 0.84 | 0.81 |
| newline (preans_slot4) | 0.91 | 0.91 | 0.91 (0.87 to 0.95) | 0.91 (0.87 to 0.95) | 0.90 | 0.88 |
| `<think>` (think_slot0) | 0.77 | 0.77 | 0.78 (0.72 to 0.84) | 0.79 (0.74 to 0.85) | 0.80 | 0.80 |
| blank line (think_slot1) | 0.82 | 0.81 | 0.82 (0.77 to 0.88) | 0.81 (0.75 to 0.87) | 0.82 | 0.82 |
| `</think>` (think_slot2) | 0.84 | 0.84 | 0.82 (0.76 to 0.88) | 0.86 (0.81 to 0.91) | 0.86 | 0.87 |
| blank line (think_slot3) | 0.91 | 0.92 | 0.94 (0.91 to 0.97) | 0.93 (0.89 to 0.96) | 0.92 | 0.92 |
| the answer token (Yes / No) | 0.87 | 0.85 | 0.84 (0.78 to 0.90) | 0.90 (0.84 to 0.94) | 0.89 | 0.85 |
| `<\|im_end\|>` (postans_slot0) | 0.85 | 0.86 | 0.86 (0.80 to 0.91) | 0.86 (0.80 to 0.91) | 0.87 | 0.86 |
| newline (postans_slot1) | 0.92 | 0.92 | 0.94 (0.90 to 0.97) | 0.93 (0.89 to 0.97) | 0.92 | 0.85 |
| `<\|im_start\|>` (postans_slot2) | 0.84 | 0.82 | 0.82 (0.77 to 0.88) | 0.84 (0.78 to 0.89) | 0.83 | 0.76 |
| `user` (postans_slot3) | 0.85 | 0.86 | 0.87 (0.82 to 0.92) | 0.87 (0.82 to 0.92) | 0.84 | 0.82 |
| newline (postans_slot4) | 0.85 | 0.81 | 0.80 (0.74 to 0.85) | 0.78 (0.73 to 0.83) | 0.79 | 0.77 |

**Build split, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.86 | 0.87 | 0.89 | 0.87 | 0.86 | 0.83 |
| newline (preans_slot1) | 0.94 | 0.96 | 0.96 | 0.95 | 0.95 | 0.94 |
| `<\|im_start\|>` (preans_slot2) | 0.91 | 0.91 | 0.88 | 0.85 | 0.82 | 0.81 |
| `assistant` (preans_slot3) | 0.79 | 0.76 | 0.85 | 0.92 | 0.90 | 0.88 |
| newline (preans_slot4) | 0.94 | 0.94 | 0.93 | 0.93 | 0.93 | 0.90 |
| `<think>` (think_slot0) | 0.77 | 0.78 | 0.79 | 0.80 | 0.81 | 0.81 |
| blank line (think_slot1) | 0.81 | 0.83 | 0.85 | 0.84 | 0.85 | 0.84 |
| `</think>` (think_slot2) | 0.84 | 0.86 | 0.86 | 0.90 | 0.90 | 0.91 |
| blank line (think_slot3) | 0.93 | 0.95 | 0.95 | 0.95 | 0.94 | 0.93 |
| the answer token (Yes / No) | 0.90 | 0.89 | 0.87 | 0.89 | 0.87 | 0.85 |
| `<\|im_end\|>` (postans_slot0) | 0.86 | 0.87 | 0.87 | 0.87 | 0.87 | 0.88 |
| newline (postans_slot1) | 0.93 | 0.94 | 0.95 | 0.95 | 0.93 | 0.89 |
| `<\|im_start\|>` (postans_slot2) | 0.88 | 0.87 | 0.88 | 0.88 | 0.87 | 0.78 |
| `user` (postans_slot3) | 0.87 | 0.88 | 0.90 | 0.90 | 0.89 | 0.88 |
| newline (postans_slot4) | 0.91 | 0.90 | 0.88 | 0.86 | 0.85 | 0.82 |

**Both splits, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.84 | 0.85 | 0.87 | 0.85 | 0.84 | 0.82 |
| newline (preans_slot1) | 0.94 | 0.95 | 0.95 | 0.94 | 0.94 | 0.94 |
| `<\|im_start\|>` (preans_slot2) | 0.91 | 0.90 | 0.88 | 0.85 | 0.83 | 0.83 |
| `assistant` (preans_slot3) | 0.80 | 0.77 | 0.86 | 0.91 | 0.90 | 0.88 |
| newline (preans_slot4) | 0.93 | 0.93 | 0.93 | 0.92 | 0.92 | 0.89 |
| `<think>` (think_slot0) | 0.76 | 0.77 | 0.77 | 0.79 | 0.80 | 0.80 |
| blank line (think_slot1) | 0.80 | 0.81 | 0.83 | 0.82 | 0.82 | 0.81 |
| `</think>` (think_slot2) | 0.83 | 0.85 | 0.85 | 0.89 | 0.89 | 0.90 |
| blank line (think_slot3) | 0.93 | 0.94 | 0.95 | 0.94 | 0.94 | 0.93 |
| the answer token (Yes / No) | 0.89 | 0.87 | 0.84 | 0.88 | 0.88 | 0.85 |
| `<\|im_end\|>` (postans_slot0) | 0.85 | 0.86 | 0.86 | 0.86 | 0.86 | 0.87 |
| newline (postans_slot1) | 0.92 | 0.93 | 0.94 | 0.94 | 0.92 | 0.87 |
| `<\|im_start\|>` (postans_slot2) | 0.86 | 0.85 | 0.85 | 0.86 | 0.83 | 0.76 |
| `user` (postans_slot3) | 0.85 | 0.86 | 0.88 | 0.88 | 0.87 | 0.87 |
| newline (postans_slot4) | 0.88 | 0.86 | 0.85 | 0.83 | 0.82 | 0.80 |

### Q9, lies against truths, among the No answers (build 65 / 76, held-out 46 / 52)

**Held-out (fitted on the build split)**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.79 | 0.78 | 0.78 (0.71 to 0.85) | 0.76 (0.69 to 0.83) | 0.74 | 0.72 |
| newline (preans_slot1) | 0.91 | 0.90 | 0.92 (0.87 to 0.96) | 0.91 (0.86 to 0.96) | 0.90 | 0.90 |
| `<\|im_start\|>` (preans_slot2) | 0.89 | 0.87 | 0.89 (0.83 to 0.93) | 0.87 (0.81 to 0.92) | 0.88 | 0.87 |
| `assistant` (preans_slot3) | 0.66 | 0.65 | 0.70 (0.62 to 0.78) | 0.74 (0.67 to 0.82) | 0.72 | 0.70 |
| newline (preans_slot4) | 0.85 | 0.85 | 0.86 (0.80 to 0.92) | 0.85 (0.79 to 0.91) | 0.84 | 0.85 |
| `<think>` (think_slot0) | 0.69 | 0.71 | 0.72 (0.65 to 0.79) | 0.72 (0.64 to 0.79) | 0.73 | 0.74 |
| blank line (think_slot1) | 0.71 | 0.72 | 0.73 (0.66 to 0.79) | 0.73 (0.66 to 0.80) | 0.74 | 0.75 |
| `</think>` (think_slot2) | 0.73 | 0.73 | 0.72 (0.63 to 0.80) | 0.75 (0.67 to 0.82) | 0.75 | 0.75 |
| blank line (think_slot3) | 0.80 | 0.82 | 0.90 (0.84 to 0.95) | 0.88 (0.82 to 0.94) | 0.87 | 0.86 |
| the answer token (Yes / No) | 0.84 | 0.83 | 0.82 (0.75 to 0.87) | 0.81 (0.74 to 0.87) | 0.78 | 0.75 |
| `<\|im_end\|>` (postans_slot0) | 0.72 | 0.71 | 0.73 (0.65 to 0.81) | 0.73 (0.65 to 0.81) | 0.74 | 0.74 |
| newline (postans_slot1) | 0.90 | 0.90 | 0.91 (0.87 to 0.95) | 0.91 (0.86 to 0.95) | 0.90 | 0.86 |
| `<\|im_start\|>` (postans_slot2) | 0.72 | 0.70 | 0.71 (0.63 to 0.78) | 0.74 (0.67 to 0.81) | 0.68 | 0.63 |
| `user` (postans_slot3) | 0.69 | 0.68 | 0.69 (0.62 to 0.76) | 0.73 (0.65 to 0.80) | 0.74 | 0.75 |
| newline (postans_slot4) | 0.79 | 0.75 | 0.70 (0.63 to 0.78) | 0.69 (0.61 to 0.77) | 0.67 | 0.65 |

**Build split, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.86 | 0.87 | 0.88 | 0.85 | 0.83 | 0.81 |
| newline (preans_slot1) | 0.93 | 0.93 | 0.94 | 0.93 | 0.92 | 0.91 |
| `<\|im_start\|>` (preans_slot2) | 0.90 | 0.90 | 0.88 | 0.82 | 0.79 | 0.76 |
| `assistant` (preans_slot3) | 0.77 | 0.75 | 0.78 | 0.83 | 0.82 | 0.84 |
| newline (preans_slot4) | 0.93 | 0.93 | 0.94 | 0.93 | 0.92 | 0.91 |
| `<think>` (think_slot0) | 0.73 | 0.75 | 0.76 | 0.77 | 0.78 | 0.78 |
| blank line (think_slot1) | 0.76 | 0.80 | 0.81 | 0.81 | 0.82 | 0.81 |
| `</think>` (think_slot2) | 0.81 | 0.82 | 0.83 | 0.85 | 0.85 | 0.85 |
| blank line (think_slot3) | 0.90 | 0.92 | 0.94 | 0.94 | 0.93 | 0.92 |
| the answer token (Yes / No) | 0.91 | 0.90 | 0.89 | 0.88 | 0.86 | 0.85 |
| `<\|im_end\|>` (postans_slot0) | 0.71 | 0.71 | 0.74 | 0.75 | 0.76 | 0.77 |
| newline (postans_slot1) | 0.92 | 0.93 | 0.94 | 0.94 | 0.92 | 0.89 |
| `<\|im_start\|>` (postans_slot2) | 0.77 | 0.77 | 0.77 | 0.80 | 0.77 | 0.72 |
| `user` (postans_slot3) | 0.76 | 0.77 | 0.76 | 0.79 | 0.80 | 0.81 |
| newline (postans_slot4) | 0.88 | 0.85 | 0.80 | 0.77 | 0.74 | 0.71 |

**Both splits, five folds**

| token | layer 35 | layer 41 | layer 47 | layer 50 | layer 53 | layer 58 |
|---|---|---|---|---|---|---|
| `<\|im_end\|>` (preans_slot0) | 0.83 | 0.83 | 0.84 | 0.81 | 0.80 | 0.78 |
| newline (preans_slot1) | 0.92 | 0.92 | 0.93 | 0.92 | 0.91 | 0.90 |
| `<\|im_start\|>` (preans_slot2) | 0.89 | 0.89 | 0.88 | 0.84 | 0.83 | 0.83 |
| `assistant` (preans_slot3) | 0.75 | 0.73 | 0.78 | 0.82 | 0.81 | 0.81 |
| newline (preans_slot4) | 0.90 | 0.89 | 0.91 | 0.90 | 0.89 | 0.89 |
| `<think>` (think_slot0) | 0.72 | 0.73 | 0.74 | 0.74 | 0.75 | 0.75 |
| blank line (think_slot1) | 0.76 | 0.78 | 0.79 | 0.78 | 0.79 | 0.78 |
| `</think>` (think_slot2) | 0.81 | 0.81 | 0.81 | 0.83 | 0.83 | 0.83 |
| blank line (think_slot3) | 0.88 | 0.90 | 0.93 | 0.92 | 0.91 | 0.89 |
| the answer token (Yes / No) | 0.90 | 0.89 | 0.88 | 0.88 | 0.86 | 0.83 |
| `<\|im_end\|>` (postans_slot0) | 0.75 | 0.75 | 0.77 | 0.77 | 0.78 | 0.78 |
| newline (postans_slot1) | 0.91 | 0.92 | 0.93 | 0.92 | 0.91 | 0.88 |
| `<\|im_start\|>` (postans_slot2) | 0.78 | 0.77 | 0.77 | 0.80 | 0.73 | 0.68 |
| `user` (postans_slot3) | 0.77 | 0.76 | 0.75 | 0.80 | 0.79 | 0.80 |
| newline (postans_slot4) | 0.83 | 0.81 | 0.76 | 0.74 | 0.71 | 0.68 |
