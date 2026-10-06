# The three probe positions at layer 50, the released probe's layer

Qwen3.6-27B. A direction is the mean of the build split's positives minus the mean of its negatives at one token;
threshold 0, the midpoint between the two means; nothing is trained. Build split: fitted on four folds, scored on
the fifth. Held-out: fitted on the build split, scored on the held-out scenarios; 95% intervals, 2,000 resamples of
scenarios. Balanced accuracy = the mean of the true-positive rate and the true-negative rate.

| position | task | build split: AUROC; lies flagged; truths flagged | held-out AUROC | held-out balanced accuracy | held-out lies flagged | held-out truths flagged |
|---|---|---|---|---|---|---|
| the newline after the response | lies against truths, all transcripts | 0.97; 138/152 (91%); 8/81 (10%) | 0.95 (0.91 to 0.98) | 0.89 (0.83 to 0.93) | 91/101 (90%; 84% to 95%) | 7/54 (13%; 6% to 22%) |
| the last token before the answer to Q9 (the released probe's token) | lies against truths, all transcripts | 0.95; 134/151 (89%); 11/81 (14%) | 0.93 (0.89 to 0.96) | 0.84 (0.78 to 0.90) | 84/101 (83%; 76% to 90%) | 8/54 (15%; 6% to 24%) |
| the last token before the answer to Q9 (the released probe's token) | lies against truths, among the No answers | 0.94; 58/65 (89%); 14/76 (18%) | 0.88 (0.82 to 0.94) | 0.77 (0.70 to 0.83) | 39/46 (85%; 74% to 93%) | 16/52 (31%; 19% to 44%) |
| the newline after the self-report answer | lies against truths, all transcripts | 0.95; 113/151 (75%); 5/81 (6%) | 0.93 (0.89 to 0.97) | 0.81 (0.76 to 0.86) | 67/101 (66%; 56% to 75%) | 2/54 (4%; 0% to 9%) |
| the newline after the self-report answer | lies against truths, among the No answers | 0.94; 55/65 (85%); 9/76 (12%) | 0.91 (0.86 to 0.95) | 0.80 (0.73 to 0.86) | 37/46 (80%; 70% to 89%) | 11/52 (21%; 12% to 33%) |

At the newline after the response, no-pressure truths flagged on the held-out set: 3/90 (3%; 0% to 8%); held-out scenarios with a lie and a truth where the lie scores above its truth: 45 of 47. At layer 47 (DIRECTION.md): AUROC 0.96, 93/101, 7/54, 6/90, 46 of 47.
