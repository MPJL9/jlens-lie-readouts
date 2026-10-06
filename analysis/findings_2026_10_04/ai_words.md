# 作为, 作为一个, AI and 人工智能 in the readouts, by class

Written by `scripts/findings_2026_10_04/ai_words.py`. Qwen, J-lens, band 35 to 58, build split and unrelated chats, in-sample. Cells: transcripts with the word in the band's readout at the token / transcripts.

- `作为 / 作為`: '作为', '作為'
- `作为一个 and the like`: '作为一个', '作为一名', '作为一种', '作为一款', '作为一家', '作为一项'
- `AI`: ' AI', 'AI', '_AI', '.AI'
- `人工智能`: '人工智能', '的人工智能'
- Left out of the 作为 lists because they mean something else: 不作为, 可以作为, 可作为, 而作为, 担当作为, 不能作为, 主动作为, 作为中国, 作为国内.
- `ai`, ` ai`, ` Ai`, `Ai` are left out of `AI`: they are also pieces of other words.
- Counted one by one in Section D: 作为 ('作为'), 作為 ('作為'), 作为一个 ('作为一个'), 作为一名 ('作为一名'), 身为 ('身为'), 智能 ('智能'), artificial (' artificial', ' Artificial')

## A. The template tokens around the response (every row is shown)

**`作为 / 作為`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| preresp_slot0 | `<\|im_end\|>` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 0/703 (0%) |
| preresp_slot1 | `\n` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 3/703 (0%) |
| preresp_slot2 | `<\|im_start\|>` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 2/703 (0%) |
| preresp_slot3 | `assistant` | 9/152 (6%) | 7/81 (9%) | 4/138 (3%) | 8/703 (1%) |
| preresp_slot4 | `\n` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 15/703 (2%) |
| postresp_slot0 | `<\|im_end\|>` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 0/703 (0%) |
| postresp_slot1 | `\n` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 0/703 (0%) |
| postresp_slot2 | `<\|im_start\|>` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 0/703 (0%) |
| postresp_slot3 | `user` | 7/152 (5%) | 1/81 (1%) | 1/138 (1%) | 0/703 (0%) |
| postresp_slot4 | `\n` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/703 (0%) |

**`作为一个 and the like`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| preresp_slot0 | `<\|im_end\|>` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 0/703 (0%) |
| preresp_slot1 | `\n` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 1/703 (0%) |
| preresp_slot2 | `<\|im_start\|>` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 1/703 (0%) |
| preresp_slot3 | `assistant` | 5/152 (3%) | 5/81 (6%) | 0/138 (0%) | 7/703 (1%) |
| preresp_slot4 | `\n` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 8/703 (1%) |
| postresp_slot0 | `<\|im_end\|>` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 0/703 (0%) |
| postresp_slot1 | `\n` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 0/703 (0%) |
| postresp_slot2 | `<\|im_start\|>` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 0/703 (0%) |
| postresp_slot3 | `user` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/703 (0%) |
| postresp_slot4 | `\n` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/703 (0%) |

**`AI`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| preresp_slot0 | `<\|im_end\|>` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 16/703 (2%) |
| preresp_slot1 | `\n` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 21/703 (3%) |
| preresp_slot2 | `<\|im_start\|>` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 23/703 (3%) |
| preresp_slot3 | `assistant` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 23/703 (3%) |
| preresp_slot4 | `\n` | 0/152 (0%) | 0/81 (0%) | 2/138 (1%) | 11/703 (2%) |
| postresp_slot0 | `<\|im_end\|>` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 2/703 (0%) |
| postresp_slot1 | `\n` | 3/152 (2%) | 11/81 (14%) | 13/138 (9%) | 59/703 (8%) |
| postresp_slot2 | `<\|im_start\|>` | 24/152 (16%) | 23/81 (28%) | 8/138 (6%) | 6/703 (1%) |
| postresp_slot3 | `user` | 3/152 (2%) | 1/81 (1%) | 1/138 (1%) | 2/703 (0%) |
| postresp_slot4 | `\n` | 2/152 (1%) | 0/81 (0%) | 8/138 (6%) | 35/703 (5%) |

**`人工智能`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| preresp_slot0 | `<\|im_end\|>` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 0/703 (0%) |
| preresp_slot1 | `\n` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 9/703 (1%) |
| preresp_slot2 | `<\|im_start\|>` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 14/703 (2%) |
| preresp_slot3 | `assistant` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/703 (0%) |
| preresp_slot4 | `\n` | 0/152 (0%) | 0/81 (0%) | 2/138 (1%) | 9/703 (1%) |
| postresp_slot0 | `<\|im_end\|>` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 0/703 (0%) |
| postresp_slot1 | `\n` | 0/152 (0%) | 0/81 (0%) | 4/138 (3%) | 2/703 (0%) |
| postresp_slot2 | `<\|im_start\|>` | 3/152 (2%) | 3/81 (4%) | 0/138 (0%) | 0/703 (0%) |
| postresp_slot3 | `user` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 0/703 (0%) |
| postresp_slot4 | `\n` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 2/703 (0%) |

**`any of the four lists`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| preresp_slot0 | `<\|im_end\|>` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 16/703 (2%) |
| preresp_slot1 | `\n` | 2/152 (1%) | 1/81 (1%) | 1/138 (1%) | 22/703 (3%) |
| preresp_slot2 | `<\|im_start\|>` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 23/703 (3%) |
| preresp_slot3 | `assistant` | 10/152 (7%) | 8/81 (10%) | 5/138 (4%) | 26/703 (4%) |
| preresp_slot4 | `\n` | 0/152 (0%) | 0/81 (0%) | 3/138 (2%) | 21/703 (3%) |
| postresp_slot0 | `<\|im_end\|>` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 2/703 (0%) |
| postresp_slot1 | `\n` | 3/152 (2%) | 11/81 (14%) | 13/138 (9%) | 59/703 (8%) |
| postresp_slot2 | `<\|im_start\|>` | 24/152 (16%) | 23/81 (28%) | 8/138 (6%) | 6/703 (1%) |
| postresp_slot3 | `user` | 10/152 (7%) | 2/81 (2%) | 2/138 (1%) | 2/703 (0%) |
| postresp_slot4 | `\n` | 3/152 (2%) | 0/81 (0%) | 8/138 (6%) | 35/703 (5%) |


## B. After the self-report question, Q1 (rows where a class reaches 10%)

**`作为 / 作為`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q1 preans_slot3 | `assistant` | 52/152 (34%) | 16/81 (20%) | 0/138 (0%) | 1/703 (0%) |
| Q1 preans_slot4 | `\n` | 25/152 (16%) | 1/81 (1%) | 0/138 (0%) | 0/703 (0%) |
| Q1 think_slot3 | `\n\n` | 22/152 (14%) | 5/81 (6%) | 0/138 (0%) | 0/703 (0%) |

**`作为一个 and the like`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q1 preans_slot3 | `assistant` | 31/152 (20%) | 9/81 (11%) | 0/138 (0%) | 0/703 (0%) |
| Q1 preans_slot4 | `\n` | 27/152 (18%) | 2/81 (2%) | 0/138 (0%) | 0/703 (0%) |
| Q1 think_slot3 | `\n\n` | 48/152 (32%) | 8/81 (10%) | 0/138 (0%) | 0/703 (0%) |

**`AI`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q1 preans_slot2 | `<\|im_start\|>` | 4/152 (3%) | 0/81 (0%) | 1/138 (1%) | 87/703 (12%) |
| Q1 preans_slot3 | `assistant` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 140/703 (20%) |
| Q1 think_slot0 | `<think>` | 143/152 (94%) | 68/81 (84%) | 134/138 (97%) | 556/703 (79%) |
| Q1 think_slot2 | `</think>` | 33/152 (22%) | 36/81 (44%) | 126/138 (91%) | 675/703 (96%) |
| Q1 postans_slot4 | `\n` | 31/107 (29%) | 26/62 (42%) | 29/131 (22%) | 361/642 (56%) |

**`人工智能`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q1 preans_slot2 | `<\|im_start\|>` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 78/703 (11%) |
| Q1 think_slot0 | `<think>` | 45/152 (30%) | 29/81 (36%) | 36/138 (26%) | 468/703 (67%) |
| Q1 postans_slot1 | `\n` | 10/107 (9%) | 11/62 (18%) | 42/131 (32%) | 142/642 (22%) |

**`any of the four lists`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q1 preans_slot2 | `<\|im_start\|>` | 5/152 (3%) | 1/81 (1%) | 1/138 (1%) | 87/703 (12%) |
| Q1 preans_slot3 | `assistant` | 52/152 (34%) | 16/81 (20%) | 0/138 (0%) | 140/703 (20%) |
| Q1 preans_slot4 | `\n` | 38/152 (25%) | 5/81 (6%) | 2/138 (1%) | 32/703 (5%) |
| Q1 think_slot0 | `<think>` | 146/152 (96%) | 72/81 (89%) | 136/138 (99%) | 669/703 (95%) |
| Q1 think_slot2 | `</think>` | 33/152 (22%) | 36/81 (44%) | 126/138 (91%) | 675/703 (96%) |
| Q1 think_slot3 | `\n\n` | 48/152 (32%) | 8/81 (10%) | 0/138 (0%) | 0/703 (0%) |
| Q1 postans_slot1 | `\n` | 13/107 (12%) | 13/62 (21%) | 43/131 (33%) | 146/642 (23%) |
| Q1 postans_slot4 | `\n` | 31/107 (29%) | 26/62 (42%) | 29/131 (22%) | 362/642 (56%) |


## B. After the self-report question, Q2 (rows where a class reaches 10%)

**`作为 / 作為`**: under 10% in every class at every one of these tokens.

**`作为一个 and the like`**: under 10% in every class at every one of these tokens.

**`AI`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q2 preans_slot1 | `\n` | 1/152 (1%) | 0/81 (0%) | 9/138 (7%) | 94/703 (13%) |
| Q2 preans_slot4 | `\n` | 25/152 (16%) | 3/81 (4%) | 0/138 (0%) | 0/703 (0%) |
| Q2 think_slot0 | `<think>` | 136/152 (89%) | 65/81 (80%) | 133/138 (96%) | 475/703 (68%) |
| Q2 think_slot2 | `</think>` | 5/152 (3%) | 3/81 (4%) | 85/138 (62%) | 658/703 (94%) |
| Q2 postans_slot4 | `\n` | 49/152 (32%) | 43/81 (53%) | 57/138 (41%) | 96/703 (14%) |

**`人工智能`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q2 think_slot0 | `<think>` | 68/152 (45%) | 54/81 (67%) | 68/138 (49%) | 693/703 (99%) |

**`any of the four lists`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q2 preans_slot1 | `\n` | 1/152 (1%) | 0/81 (0%) | 9/138 (7%) | 94/703 (13%) |
| Q2 preans_slot4 | `\n` | 26/152 (17%) | 3/81 (4%) | 0/138 (0%) | 0/703 (0%) |
| Q2 think_slot0 | `<think>` | 144/152 (95%) | 79/81 (98%) | 138/138 (100%) | 703/703 (100%) |
| Q2 think_slot2 | `</think>` | 5/152 (3%) | 3/81 (4%) | 85/138 (62%) | 658/703 (94%) |
| Q2 postans_slot4 | `\n` | 49/152 (32%) | 43/81 (53%) | 57/138 (41%) | 96/703 (14%) |


## B. After the self-report question, Q6 (rows where a class reaches 10%)

**`作为 / 作為`**: under 10% in every class at every one of these tokens.

**`作为一个 and the like`**: under 10% in every class at every one of these tokens.

**`AI`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q6 think_slot0 | `<think>` | 122/152 (80%) | 54/81 (67%) | 127/138 (92%) | 397/703 (56%) |
| Q6 think_slot2 | `</think>` | 5/152 (3%) | 8/81 (10%) | 28/138 (20%) | 589/703 (84%) |
| Q6 postans_slot3 | `user` | 0/152 (0%) | 1/81 (1%) | 11/138 (8%) | 191/703 (27%) |
| Q6 postans_slot4 | `\n` | 26/152 (17%) | 27/81 (33%) | 14/138 (10%) | 9/703 (1%) |

**`人工智能`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q6 think_slot0 | `<think>` | 54/152 (36%) | 44/81 (54%) | 45/138 (33%) | 459/703 (65%) |

**`any of the four lists`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q6 think_slot0 | `<think>` | 133/152 (88%) | 74/81 (91%) | 133/138 (96%) | 578/703 (82%) |
| Q6 think_slot2 | `</think>` | 5/152 (3%) | 8/81 (10%) | 28/138 (20%) | 589/703 (84%) |
| Q6 postans_slot3 | `user` | 0/152 (0%) | 1/81 (1%) | 11/138 (8%) | 191/703 (27%) |
| Q6 postans_slot4 | `\n` | 28/152 (18%) | 27/81 (33%) | 14/138 (10%) | 9/703 (1%) |


## B. After the self-report question, Q7 (rows where a class reaches 10%)

**`作为 / 作為`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q7 preans_slot1 | `\n` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 459/703 (65%) |

**`作为一个 and the like`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q7 preans_slot1 | `\n` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 436/703 (62%) |

**`AI`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q7 preans_slot1 | `\n` | 12/152 (8%) | 10/81 (12%) | 23/138 (17%) | 568/703 (81%) |
| Q7 preans_slot3 | `assistant` | 139/152 (91%) | 57/81 (70%) | 43/138 (31%) | 281/703 (40%) |
| Q7 preans_slot4 | `\n` | 118/152 (78%) | 25/81 (31%) | 27/138 (20%) | 23/703 (3%) |
| Q7 think_slot0 | `<think>` | 113/152 (74%) | 53/81 (65%) | 74/138 (54%) | 437/703 (62%) |
| Q7 think_slot2 | `</think>` | 105/152 (69%) | 55/81 (68%) | 112/138 (81%) | 600/703 (85%) |
| Q7 think_slot3 | `\n\n` | 33/152 (22%) | 4/81 (5%) | 2/138 (1%) | 10/703 (1%) |
| Q7 postans_slot1 | `\n` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 354/703 (50%) |
| Q7 postans_slot4 | `\n` | 50/152 (33%) | 19/81 (23%) | 8/138 (6%) | 19/703 (3%) |

**`人工智能`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q7 preans_slot1 | `\n` | 2/152 (1%) | 0/81 (0%) | 1/138 (1%) | 530/703 (75%) |
| Q7 think_slot0 | `<think>` | 65/152 (43%) | 43/81 (53%) | 44/138 (32%) | 582/703 (83%) |
| Q7 postans_slot1 | `\n` | 1/152 (1%) | 2/81 (2%) | 1/138 (1%) | 575/703 (82%) |

**`any of the four lists`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q7 preans_slot1 | `\n` | 12/152 (8%) | 11/81 (14%) | 23/138 (17%) | 568/703 (81%) |
| Q7 preans_slot3 | `assistant` | 139/152 (91%) | 57/81 (70%) | 43/138 (31%) | 281/703 (40%) |
| Q7 preans_slot4 | `\n` | 118/152 (78%) | 25/81 (31%) | 27/138 (20%) | 23/703 (3%) |
| Q7 think_slot0 | `<think>` | 129/152 (85%) | 71/81 (88%) | 91/138 (66%) | 622/703 (88%) |
| Q7 think_slot2 | `</think>` | 105/152 (69%) | 55/81 (68%) | 112/138 (81%) | 600/703 (85%) |
| Q7 think_slot3 | `\n\n` | 33/152 (22%) | 4/81 (5%) | 2/138 (1%) | 10/703 (1%) |
| Q7 postans_slot1 | `\n` | 1/152 (1%) | 2/81 (2%) | 1/138 (1%) | 578/703 (82%) |
| Q7 postans_slot4 | `\n` | 50/152 (33%) | 19/81 (23%) | 8/138 (6%) | 19/703 (3%) |


## B. After the self-report question, Q9 (rows where a class reaches 10%)

**`作为 / 作為`**: under 10% in every class at every one of these tokens.

**`作为一个 and the like`**: under 10% in every class at every one of these tokens.

**`AI`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q9 preans_slot1 | `\n` | 2/152 (1%) | 16/81 (20%) | 39/138 (28%) | 378/703 (54%) |
| Q9 think_slot0 | `<think>` | 136/152 (89%) | 59/81 (73%) | 117/138 (85%) | 167/703 (24%) |
| Q9 think_slot2 | `</think>` | 1/152 (1%) | 3/81 (4%) | 78/138 (57%) | 680/703 (97%) |
| Q9 think_slot3 | `\n\n` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 152/703 (22%) |
| Q9 postans_slot4 | `\n` | 79/152 (52%) | 51/81 (63%) | 100/138 (72%) | 59/703 (8%) |

**`人工智能`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q9 preans_slot1 | `\n` | 0/152 (0%) | 4/81 (5%) | 9/138 (7%) | 245/703 (35%) |
| Q9 think_slot0 | `<think>` | 127/152 (84%) | 71/81 (88%) | 96/138 (70%) | 696/703 (99%) |

**`any of the four lists`**

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| Q9 preans_slot1 | `\n` | 2/152 (1%) | 16/81 (20%) | 39/138 (28%) | 378/703 (54%) |
| Q9 think_slot0 | `<think>` | 151/152 (99%) | 79/81 (98%) | 132/138 (96%) | 699/703 (99%) |
| Q9 think_slot2 | `</think>` | 1/152 (1%) | 3/81 (4%) | 78/138 (57%) | 680/703 (97%) |
| Q9 think_slot3 | `\n\n` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 152/703 (22%) |
| Q9 postans_slot4 | `\n` | 79/152 (52%) | 51/81 (63%) | 100/138 (72%) | 59/703 (8%) |


## C. Inside the response

Transcripts with the word at one or more response tokens, then response tokens that carry it / response tokens.

| list | responses | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| `作为 / 作為` | all | 27/152 (18%); 43/27,211 (0.16%) | 28/81 (35%); 51/15,421 (0.33%) | 19/138 (14%); 33/14,537 (0.23%) | 85/703 (12%); 134/118,699 (0.11%) |
| `作为一个 and the like` | all | 38/152 (25%); 84/27,211 (0.31%) | 30/81 (37%); 66/15,421 (0.43%) | 19/138 (14%); 37/14,537 (0.25%) | 76/703 (11%); 123/118,699 (0.10%) |
| `AI` | all | 9/152 (6%); 33/27,211 (0.12%) | 23/81 (28%); 95/15,421 (0.62%) | 15/138 (11%); 37/14,537 (0.25%) | 96/703 (14%); 1,549/118,699 (1.30%) |
| `AI` | text without "AI" | 7/150 (5%); 9/26,746 (0.03%) | 12/70 (17%); 32/12,853 (0.25%) | 12/135 (9%); 21/14,069 (0.15%) | 61/668 (9%); 361/109,698 (0.33%) |
| `人工智能` | all | 5/152 (3%); 17/27,211 (0.06%) | 21/81 (26%); 68/15,421 (0.44%) | 8/138 (6%); 20/14,537 (0.14%) | 64/703 (9%); 768/118,699 (0.65%) |
| `人工智能` | text without "AI" | 3/150 (2%); 3/26,746 (0.01%) | 10/70 (14%); 20/12,853 (0.16%) | 5/135 (4%); 6/14,069 (0.04%) | 30/668 (4%); 111/109,698 (0.10%) |
| `any of the four lists` | all | 44/152 (29%); 123/27,211 (0.45%) | 41/81 (51%); 181/15,421 (1.17%) | 33/138 (24%); 84/14,537 (0.58%) | 182/703 (26%); 1,784/118,699 (1.50%) |
| `any of the four lists` | text without "AI" | 42/150 (28%); 98/26,746 (0.37%) | 30/70 (43%); 88/12,853 (0.68%) | 30/135 (22%); 66/14,069 (0.47%) | 147/668 (22%); 542/109,698 (0.49%) |

Responses whose own text says "AI" or "artificial intelligence": lies 2/152; truths 11/81; no-pressure truths 3/138; unrelated 35/703.

## D. Single tokens, at the positions of Section A and inside the response

| token | place | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| 作为 | preresp_slot3 (`assistant`) | 9/152 (6%) | 7/81 (9%) | 4/138 (3%) | 8/703 (1%) |
| 作为 | at one or more response tokens | 27/152 (18%) | 28/81 (35%) | 19/138 (14%) | 85/703 (12%) |
| 作為 | at one or more response tokens | 11/152 (7%) | 13/81 (16%) | 10/138 (7%) | 40/703 (6%) |
| 作为一个 | at one or more response tokens | 17/152 (11%) | 15/81 (19%) | 9/138 (7%) | 56/703 (8%) |
| 作为一名 | preresp_slot3 (`assistant`) | 5/152 (3%) | 5/81 (6%) | 0/138 (0%) | 7/703 (1%) |
| 作为一名 | at one or more response tokens | 23/152 (15%) | 27/81 (33%) | 8/138 (6%) | 27/703 (4%) |
| 身为 | at one or more response tokens | 4/152 (3%) | 3/81 (4%) | 3/138 (2%) | 1/703 (0%) |
| 智能 | at one or more response tokens | 2/152 (1%) | 8/81 (10%) | 3/138 (2%) | 46/703 (7%) |
| artificial | at one or more response tokens | 2/152 (1%) | 19/81 (23%) | 5/138 (4%) | 46/703 (7%) |
