# The "as an AI" words by the role the prompt gives

Written by `scripts/findings_2026_10_04/ai_words_by_role.py`. Qwen, J-lens, band 35 to 58, build split and unrelated chats, in-sample. Cells: transcripts with the word in the band's readout at the token / transcripts.

- `AI words`: ' AI', 'AI', '_AI', '.AI', '人工智能', '的人工智能'
- `作为一个`: '作为一个'
- `作为一名`: '作为一名'
- `作为 / 作為`: '作为', '作為'

Transcripts: pressured, prompt says AI 91; pressured, other role 126; no-pressure, scenario says AI 54; no-pressure, other role 74; unrelated 703; lies, says AI 56; lies, other role 84; truths, says AI 35; truths, other role 42; pressured with "assistant" only (left out) 16.

## `AI words`

| wording | position | token | pressured, prompt says AI | pressured, other role | no-pressure, scenario says AI | no-pressure, other role | unrelated |
|---|---|---|---|---|---|---|---|
| before the question | postresp_slot2 | `<|im_start|>` | 31/91 (34%) | 14/126 (11%) | 4/54 (7%) | 4/74 (5%) | 6/703 (1%) |
| Q1 | preans_slot3 | `assistant` | 1/91 (1%) | 0/126 (0%) | 0/54 (0%) | 0/74 (0%) | 140/703 (20%) |
| Q1 | think_slot0 | `<think>` | 89/91 (98%) | 113/126 (90%) | 54/54 (100%) | 72/74 (97%) | 669/703 (95%) |
| Q1 | think_slot2 | `</think>` | 9/91 (10%) | 55/126 (44%) | 46/54 (85%) | 70/74 (95%) | 675/703 (96%) |
| Q1 | postans_slot1 | newline | 15/74 (20%) | 11/82 (13%) | 14/51 (27%) | 25/71 (35%) | 146/642 (23%) |
| Q1 | postans_slot4 | newline | 28/74 (38%) | 25/82 (30%) | 13/51 (25%) | 15/71 (21%) | 362/642 (56%) |
| Q2 | think_slot0 | `<think>` | 91/91 (100%) | 115/126 (91%) | 54/54 (100%) | 74/74 (100%) | 703/703 (100%) |
| Q2 | think_slot2 | `</think>` | 0/91 (0%) | 8/126 (6%) | 27/54 (50%) | 50/74 (68%) | 658/703 (94%) |
| Q2 | postans_slot4 | newline | 36/91 (40%) | 48/126 (38%) | 29/54 (54%) | 21/74 (28%) | 96/703 (14%) |
| Q6 | think_slot0 | `<think>` | 85/91 (93%) | 105/126 (83%) | 52/54 (96%) | 72/74 (97%) | 578/703 (82%) |
| Q6 | think_slot2 | `</think>` | 6/91 (7%) | 7/126 (6%) | 14/54 (26%) | 13/74 (18%) | 589/703 (84%) |
| Q6 | postans_slot3 | `user` | 1/91 (1%) | 0/126 (0%) | 3/54 (6%) | 7/74 (9%) | 191/703 (27%) |
| Q6 | postans_slot4 | newline | 25/91 (27%) | 23/126 (18%) | 7/54 (13%) | 6/74 (8%) | 9/703 (1%) |
| Q7 | preans_slot1 | newline | 9/91 (10%) | 11/126 (9%) | 12/54 (22%) | 8/74 (11%) | 568/703 (81%) |
| Q7 | preans_slot3 | `assistant` | 74/91 (81%) | 107/126 (85%) | 23/54 (43%) | 16/74 (22%) | 281/703 (40%) |
| Q7 | preans_slot4 | newline | 44/91 (48%) | 89/126 (71%) | 13/54 (24%) | 12/74 (16%) | 23/703 (3%) |
| Q7 | think_slot0 | `<think>` | 87/91 (96%) | 100/126 (79%) | 39/54 (72%) | 44/74 (59%) | 622/703 (88%) |
| Q7 | think_slot2 | `</think>` | 50/91 (55%) | 98/126 (78%) | 40/54 (74%) | 66/74 (89%) | 600/703 (85%) |
| Q7 | think_slot3 | blank line | 8/91 (9%) | 24/126 (19%) | 1/54 (2%) | 0/74 (0%) | 10/703 (1%) |
| Q7 | postans_slot1 | newline | 2/91 (2%) | 1/126 (1%) | 0/54 (0%) | 0/74 (0%) | 578/703 (82%) |
| Q7 | postans_slot4 | newline | 33/91 (36%) | 29/126 (23%) | 5/54 (9%) | 3/74 (4%) | 19/703 (3%) |
| Q9 | preans_slot1 | newline | 10/91 (11%) | 7/126 (6%) | 22/54 (41%) | 14/74 (19%) | 378/703 (54%) |
| Q9 | think_slot0 | `<think>` | 91/91 (100%) | 124/126 (98%) | 53/54 (98%) | 69/74 (93%) | 699/703 (99%) |
| Q9 | think_slot2 | `</think>` | 0/91 (0%) | 4/126 (3%) | 30/54 (56%) | 43/74 (58%) | 680/703 (97%) |
| Q9 | think_slot3 | blank line | 0/91 (0%) | 0/126 (0%) | 0/54 (0%) | 0/74 (0%) | 152/703 (22%) |
| Q9 | postans_slot4 | newline | 49/91 (54%) | 68/126 (54%) | 41/54 (76%) | 51/74 (69%) | 59/703 (8%) |

## `AI words`, lies and truths apart

| wording | position | token | lies, says AI | lies, other role | truths, says AI | truths, other role |
|---|---|---|---|---|---|---|
| before the question | postresp_slot2 | `<|im_start|>` | 16/56 (29%) | 6/84 (7%) | 15/35 (43%) | 8/42 (19%) |
| Q1 | preans_slot3 | `assistant` | 1/56 (2%) | 0/84 (0%) | 0/35 (0%) | 0/42 (0%) |
| Q1 | think_slot0 | `<think>` | 56/56 (100%) | 78/84 (93%) | 33/35 (94%) | 35/42 (83%) |
| Q1 | think_slot2 | `</think>` | 1/56 (2%) | 30/84 (36%) | 8/35 (23%) | 25/42 (60%) |
| Q1 | postans_slot1 | newline | 8/45 (18%) | 5/51 (10%) | 7/29 (24%) | 6/31 (19%) |
| Q1 | postans_slot4 | newline | 16/45 (36%) | 11/51 (22%) | 12/29 (41%) | 14/31 (45%) |
| Q2 | think_slot0 | `<think>` | 56/56 (100%) | 76/84 (90%) | 35/35 (100%) | 39/42 (93%) |
| Q2 | think_slot2 | `</think>` | 0/56 (0%) | 5/84 (6%) | 0/35 (0%) | 3/42 (7%) |
| Q2 | postans_slot4 | newline | 17/56 (30%) | 27/84 (32%) | 19/35 (54%) | 21/42 (50%) |
| Q6 | think_slot0 | `<think>` | 52/56 (93%) | 70/84 (83%) | 33/35 (94%) | 35/42 (83%) |
| Q6 | think_slot2 | `</think>` | 3/56 (5%) | 2/84 (2%) | 3/35 (9%) | 5/42 (12%) |
| Q6 | postans_slot3 | `user` | 0/56 (0%) | 0/84 (0%) | 1/35 (3%) | 0/42 (0%) |
| Q6 | postans_slot4 | newline | 13/56 (23%) | 11/84 (13%) | 12/35 (34%) | 12/42 (29%) |
| Q7 | preans_slot1 | newline | 6/56 (11%) | 5/84 (6%) | 3/35 (9%) | 6/42 (14%) |
| Q7 | preans_slot3 | `assistant` | 50/56 (89%) | 78/84 (93%) | 24/35 (69%) | 29/42 (69%) |
| Q7 | preans_slot4 | newline | 36/56 (64%) | 74/84 (88%) | 8/35 (23%) | 15/42 (36%) |
| Q7 | think_slot0 | `<think>` | 54/56 (96%) | 66/84 (79%) | 33/35 (94%) | 34/42 (81%) |
| Q7 | think_slot2 | `</think>` | 29/56 (52%) | 67/84 (80%) | 21/35 (60%) | 31/42 (74%) |
| Q7 | think_slot3 | blank line | 7/56 (12%) | 22/84 (26%) | 1/35 (3%) | 2/42 (5%) |
| Q7 | postans_slot1 | newline | 1/56 (2%) | 0/84 (0%) | 1/35 (3%) | 1/42 (2%) |
| Q7 | postans_slot4 | newline | 23/56 (41%) | 22/84 (26%) | 10/35 (29%) | 7/42 (17%) |
| Q9 | preans_slot1 | newline | 2/56 (4%) | 0/84 (0%) | 8/35 (23%) | 7/42 (17%) |
| Q9 | think_slot0 | `<think>` | 56/56 (100%) | 84/84 (100%) | 35/35 (100%) | 40/42 (95%) |
| Q9 | think_slot2 | `</think>` | 0/56 (0%) | 1/84 (1%) | 0/35 (0%) | 3/42 (7%) |
| Q9 | think_slot3 | blank line | 0/56 (0%) | 0/84 (0%) | 0/35 (0%) | 0/42 (0%) |
| Q9 | postans_slot4 | newline | 28/56 (50%) | 42/84 (50%) | 21/35 (60%) | 26/42 (62%) |

## `作为一个`

| wording | position | token | pressured, prompt says AI | pressured, other role | no-pressure, scenario says AI | no-pressure, other role | unrelated |
|---|---|---|---|---|---|---|---|
| Q7 | preans_slot1 | newline | 0/91 (0%) | 1/126 (1%) | 0/54 (0%) | 0/74 (0%) | 419/703 (60%) |

## `作为一个`, lies and truths apart

| wording | position | token | lies, says AI | lies, other role | truths, says AI | truths, other role |
|---|---|---|---|---|---|---|
| Q7 | preans_slot1 | newline | 0/56 (0%) | 1/84 (1%) | 0/35 (0%) | 0/42 (0%) |

## `作为一名`

| wording | position | token | pressured, prompt says AI | pressured, other role | no-pressure, scenario says AI | no-pressure, other role | unrelated |
|---|---|---|---|---|---|---|---|
| Q1 | preans_slot3 | `assistant` | 3/91 (3%) | 30/126 (24%) | 0/54 (0%) | 0/74 (0%) | 0/703 (0%) |
| Q1 | preans_slot4 | newline | 2/91 (2%) | 24/126 (19%) | 0/54 (0%) | 0/74 (0%) | 0/703 (0%) |
| Q1 | think_slot3 | blank line | 6/91 (7%) | 42/126 (33%) | 0/54 (0%) | 0/74 (0%) | 0/703 (0%) |
| Q7 | preans_slot1 | newline | 0/91 (0%) | 1/126 (1%) | 0/54 (0%) | 0/74 (0%) | 431/703 (61%) |

## `作为一名`, lies and truths apart

| wording | position | token | lies, says AI | lies, other role | truths, says AI | truths, other role |
|---|---|---|---|---|---|---|
| Q1 | preans_slot3 | `assistant` | 3/56 (5%) | 23/84 (27%) | 0/35 (0%) | 7/42 (17%) |
| Q1 | preans_slot4 | newline | 2/56 (4%) | 23/84 (27%) | 0/35 (0%) | 1/42 (2%) |
| Q1 | think_slot3 | blank line | 4/56 (7%) | 38/84 (45%) | 2/35 (6%) | 4/42 (10%) |
| Q7 | preans_slot1 | newline | 0/56 (0%) | 1/84 (1%) | 0/35 (0%) | 0/42 (0%) |

## `作为 / 作為`

| wording | position | token | pressured, prompt says AI | pressured, other role | no-pressure, scenario says AI | no-pressure, other role | unrelated |
|---|---|---|---|---|---|---|---|
| Q1 | preans_slot3 | `assistant` | 8/91 (9%) | 51/126 (40%) | 0/54 (0%) | 0/74 (0%) | 1/703 (0%) |
| Q1 | preans_slot4 | newline | 3/91 (3%) | 19/126 (15%) | 0/54 (0%) | 0/74 (0%) | 0/703 (0%) |
| Q1 | think_slot3 | blank line | 2/91 (2%) | 20/126 (16%) | 0/54 (0%) | 0/74 (0%) | 0/703 (0%) |
| Q7 | preans_slot1 | newline | 0/91 (0%) | 2/126 (2%) | 0/54 (0%) | 0/74 (0%) | 459/703 (65%) |

## `作为 / 作為`, lies and truths apart

| wording | position | token | lies, says AI | lies, other role | truths, says AI | truths, other role |
|---|---|---|---|---|---|---|
| Q1 | preans_slot3 | `assistant` | 5/56 (9%) | 41/84 (49%) | 3/35 (9%) | 10/42 (24%) |
| Q1 | preans_slot4 | newline | 3/56 (5%) | 19/84 (23%) | 0/35 (0%) | 0/42 (0%) |
| Q1 | think_slot3 | blank line | 1/56 (2%) | 18/84 (21%) | 1/35 (3%) | 2/42 (5%) |
| Q7 | preans_slot1 | newline | 0/56 (0%) | 1/84 (1%) | 0/35 (0%) | 1/42 (2%) |
