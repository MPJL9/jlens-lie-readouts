# Other models and every self-report wording: a first look (J-lens)

Written by `scripts/other_models.py`. Build split only; every number is in-sample. Bands: gemma-3-12b-it 17-40, gemma-3-27b-it 27-52, qwen3.6-27b 35-58, gpt-oss-20b 10-20.

## 1. How each model answers the self-report question

Cells are `admit / deny / other`.

| model | wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| gemma-3-12b-it | Q1 | 15 / 3 / 31 | 6 / 5 / 21 | 4 / 0 / 131 | 0 / 0 / 179 |
| gemma-3-12b-it | Q2 | 42 / 7 / 0 | 23 / 9 / 0 | 34 / 101 / 0 | 13 / 166 / 0 |
| gemma-3-12b-it | Q6 | 41 / 8 / 0 | 14 / 18 / 0 | 10 / 125 / 0 | 46 / 133 / 0 |
| gemma-3-12b-it | Q7 | 33 / 16 / 0 | 21 / 11 / 0 | 22 / 113 / 0 | 8 / 171 / 0 |
| gemma-3-12b-it | Q9 | 40 / 9 / 0 | 23 / 9 / 0 | 15 / 120 / 0 | 6 / 173 / 0 |
| gemma-3-27b-it | Q1 | 36 / 1 / 21 | 10 / 4 / 16 | 9 / 2 / 122 | 0 / 0 / 199 |
| gemma-3-27b-it | Q2 | 56 / 2 / 0 | 30 / 0 / 0 | 96 / 37 / 0 | 36 / 163 / 0 |
| gemma-3-27b-it | Q6 | 56 / 2 / 0 | 26 / 4 / 0 | 111 / 22 / 0 | 170 / 29 / 0 |
| gemma-3-27b-it | Q7 | 42 / 16 / 0 | 18 / 12 / 0 | 7 / 126 / 0 | 2 / 197 / 0 |
| gemma-3-27b-it | Q9 | 51 / 7 / 0 | 22 / 8 / 0 | 35 / 98 / 0 | 25 / 174 / 0 |
| qwen3.6-27b | Q1 | 79 / 53 / 20 | 6 / 74 / 1 | 2 / 136 / 0 | 0 / 158 / 0 |
| qwen3.6-27b | Q2 | 105 / 47 / 0 | 4 / 77 / 0 | 0 / 138 / 0 | 0 / 158 / 0 |
| qwen3.6-27b | Q6 | 109 / 43 / 0 | 8 / 73 / 0 | 2 / 136 / 0 | 3 / 155 / 0 |
| qwen3.6-27b | Q7 | 73 / 79 / 0 | 4 / 77 / 0 | 0 / 138 / 0 | 0 / 158 / 0 |
| qwen3.6-27b | Q9 | 86 / 65 / 1 | 5 / 76 / 0 | 0 / 138 / 0 | 0 / 158 / 0 |
| gpt-oss-20b | Q1 | 0 / 49 / 67 | 1 / 42 / 51 | 1 / 121 / 5 | 0 / 264 / 1 |
| gpt-oss-20b | Q2 | 4 / 112 / 0 | 5 / 87 / 2 | 0 / 127 / 0 | 0 / 265 / 0 |
| gpt-oss-20b | Q6 | 39 / 75 / 2 | 23 / 67 / 4 | 5 / 122 / 0 | 8 / 257 / 0 |
| gpt-oss-20b | Q7 | 11 / 102 / 3 | 2 / 90 / 2 | 0 / 126 / 1 | 3 / 262 / 0 |
| gpt-oss-20b | Q9 | 3 / 105 / 8 | 3 / 88 / 3 | 5 / 122 / 0 | 2 / 263 / 0 |

## 2. Post-response slots (before the question)

Tokens are shown as `token share of lies/share of truths` in percent.

| model | position | lies / truths | best gap | shuffled | strong tokens | tokens with the largest gap |
|---|---|---|---|---|---|---|
| gemma-3-12b-it | postresp_slot0 | 49 / 32 | 22 | 27 | 0 | `🕵` 59/38, `😊` 51/31, `😄` 24/6, `␣explicação` 43/25, `\n` 96/78 |
| gemma-3-12b-it | postresp_slot1 | 49 / 32 | 38 | 26 | 1 | `謊` 41/3, `␣মিথ্যা` 33/3, `谎` 24/0, `🤫` 57/34, `␣obfusc` 31/9 |
| gemma-3-12b-it | postresp_slot2 | 49 / 32 | 25 | 24 | 0 | `␣knowingly` 29/3, `␣😏` 27/3, `␣misinformation` 29/6, `🤐` 35/12, `␣obfusc` 37/16 |
| gemma-3-12b-it | postresp_slot3 | 49 / 32 | 23 | 29 | 0 | `␣conversación` 45/22, `␣pertanyaan` 41/19, `␣আমার` 43/22, `Thanks` 39/19, `␣Bạn` 22/3 |
| gemma-3-12b-it | postresp_slot4 | 49 / 32 | 24 | 26 | 0 | `␣pregunta` 84/59, `我知道` 37/12, `␣ถาม` 57/38, `That` 67/50, `␣suspicions` 20/3 |
| gemma-3-27b-it | postresp_slot0 | 58 / 30 | 25 | 25 | 0 | `❓` 59/33, `🔐` 59/33, `🟢` 64/40, `📧` 60/40, `🟡` 43/23 |
| gemma-3-27b-it | postresp_slot1 | 58 / 30 | 31 | 25 | 1 | `😏` 38/7, `␣মিথ্যা` 28/0, `🥰` 55/33, `🤫` 55/33, `rawdę` 55/33 |
| gemma-3-27b-it | postresp_slot2 | 58 / 30 | 25 | 23 | 0 | `🤥` 52/27, `😰` 29/7, `␣خفیہ` 43/23, `!!!!` 86/67, `!!!!!` 98/80 |
| gemma-3-27b-it | postresp_slot3 | 58 / 30 | 27 | 26 | 0 | `␣Continuation` 47/20, `␣말투` 52/27, `␣продовжу` 83/60, `伱` 33/10, `␣继续` 81/60 |
| gemma-3-27b-it | postresp_slot4 | 58 / 30 | 35 | 26 | 0 | `␣REALLY` 48/13, `␣grumpy` 69/40, `质疑` 59/37, `␣sneaky` 48/27, `␣complaining` 41/20 |
| qwen3.6-27b | postresp_slot0 | 152 / 81 | 28 | 15 | 0 | `……` 49/21, `…*` 41/17, `interpreter` 45/26, `␣   \n\n` 41/22, `”**` 48/30 |
| qwen3.6-27b | postresp_slot1 | 152 / 81 | 74 | 15 | 19 | `谎言` 82/7, `说谎` 80/9, `fake` 73/6, `虚假` 66/2, `␣falsehood` 59/0 |
| qwen3.6-27b | postresp_slot2 | 152 / 81 | 19 | 15 | 0 | `Reply` 71/52, `名` 53/35, `小` 39/21, `LI` 61/43, `水` 29/11 |
| qwen3.6-27b | postresp_slot3 | 152 / 81 | 31 | 16 | 0 | `␣Questions` 70/38, `␣preguntas` 54/27, `Yes` 54/30, `Okay` 74/49, `␣questions` 62/38 |
| qwen3.6-27b | postresp_slot4 | 152 / 81 | 48 | 13 | 0 | `质疑` 71/23, `␣questioning` 78/38, `␣skepticism` 64/26, `␣skept` 55/21, `␣skeptical` 51/19 |
| gpt-oss-20b | postresp_slot0 | 116 / 94 | 16 | 15 | 0 | `/chat` 68/52, `回复` 91/76, `elő` 47/32, `␣fó` 57/43, `!”\n` 25/13 |
| gpt-oss-20b | postresp_slot1 | 116 / 94 | 12 | 15 | 0 | `ólogo` 67/55, `prepend` 22/13, `客服` 73/64, `返信` 37/28, `␣dialogue` 51/41 |
| gpt-oss-20b | postresp_slot2 | 116 / 94 | 12 | 15 | 0 | `␣asked` 25/13, `␣greetings` 48/38, `␣joking` 48/38, `:)\n` 78/68, `举报` 74/65 |
| gpt-oss-20b | postresp_slot3 | 116 / 94 | 14 | 15 | 0 | `yeah` 34/20, `␣couldn` 59/45, `␣didn` 46/32, `␣asker` 42/29, `␣Aunt` 42/30 |

## 3. Template positions after the question

Each cell: best gap, the shuffled value in brackets, and one `*` per strong token (at most three). All
scenario transcripts of the build split (lies against truths, whatever the answer).

**gemma-3-12b-it** (lies / truths: 49 / 32)

| position | Q1 | Q2 | Q6 | Q7 | Q9 |
|---|---|---|---|---|---|
| preans_slot0 | 23 (24)  | 20 (26)  | 24 (25)  | 30 (26)  | 24 (25)  |
| preans_slot1 | 47 (23) * | 42 (26)  | 35 (25)  | 36 (25)  | 29 (26)  |
| preans_slot2 | 36 (24) * | 49 (27) ** | 29 (26)  | 41 (26)  | 35 (27) * |
| preans_slot3 | 21 (24)  | 23 (25)  | 27 (24)  | 17 (25)  | 24 (23)  |
| preans_slot4 | 22 (26)  | 39 (26)  | 55 (26) ** | 25 (26)  | 36 (25) * |
| postans_slot0 | 33 (30) * | 35 (25)  | 36 (26)  | 31 (27) * | 33 (27)  |
| postans_slot1 | 34 (30)  | 31 (29)  | 40 (26) * | 27 (25)  | 36 (27)  |
| postans_slot2 | 30 (28)  | 24 (25)  | 30 (24)  | 28 (26)  | 24 (24)  |
| postans_slot3 | 26 (27)  | 28 (26)  | 35 (26)  | 29 (26)  | 24 (28)  |
| postans_slot4 | 24 (30)  | 31 (27)  | 35 (24)  | 28 (27)  | 31 (25) * |

**gemma-3-27b-it** (lies / truths: 58 / 30)

| position | Q1 | Q2 | Q6 | Q7 | Q9 |
|---|---|---|---|---|---|
| preans_slot0 | 29 (26)  | 27 (21)  | 21 (22)  | 21 (23)  | 20 (23)  |
| preans_slot1 | 51 (23)  | 56 (25) *** | 51 (26)  | 51 (27)  | 40 (24) * |
| preans_slot2 | 49 (24) *** | 52 (23) *** | 42 (24)  | 35 (25)  | 33 (24)  |
| preans_slot3 | 28 (25)  | 30 (23)  | 26 (22)  | 19 (20)  | 31 (21)  |
| preans_slot4 | 35 (23) * | 28 (24)  | 30 (20)  | 30 (24)  | 29 (22)  |
| postans_slot0 | – | 33 (26) * | 30 (25)  | 30 (24)  | 33 (24)  |
| postans_slot1 | – | 36 (23)  | 44 (24) * | 33 (24)  | 35 (23) * |
| postans_slot2 | – | 32 (24)  | 35 (24)  | 34 (23)  | 34 (21) * |
| postans_slot3 | – | 41 (25)  | 37 (24)  | 31 (25) * | 31 (25)  |
| postans_slot4 | – | 31 (23) * | 32 (23)  | 27 (25)  | 34 (24)  |

**qwen3.6-27b** (lies / truths: 152 / 81)

| position | Q1 | Q2 | Q6 | Q7 | Q9 |
|---|---|---|---|---|---|
| preans_slot0 | 29 (13)  | 29 (15)  | 24 (13)  | 28 (14)  | 37 (15)  |
| preans_slot1 | 67 (14) *** | 61 (15) *** | 49 (16) * | 41 (14) * | 61 (15) *** |
| preans_slot2 | 37 (13) ** | 34 (14)  | 35 (15) * | 28 (15)  | 44 (16) * |
| preans_slot3 | 33 (12)  | 49 (13)  | 51 (12)  | 44 (15)  | 41 (13) * |
| preans_slot4 | 41 (15) *** | 51 (15)  | 48 (14)  | 54 (15) *** | 48 (14) * |
| think_slot0 | 24 (15)  | 24 (16)  | 29 (17)  | 28 (15)  | 28 (16)  |
| think_slot1 | 28 (17)  | 31 (17)  | 30 (17)  | 32 (16)  | 38 (16)  |
| think_slot2 | 31 (15)  | 56 (17) ** | 52 (17) * | 33 (16)  | 41 (16)  |
| think_slot3 | 44 (13)  | 54 (14) * | 48 (12)  | 50 (13) *** | 54 (13) ** |
| postans_slot0 | 24 (17)  | 39 (14)  | 51 (16)  | 29 (15)  | 27 (14)  |
| postans_slot1 | 33 (16)  | 50 (17) *** | 58 (16) *** | 45 (15) * | 51 (14) * |
| postans_slot2 | 38 (16) * | 38 (14)  | 41 (14)  | 29 (15)  | 35 (16)  |
| postans_slot3 | 28 (16)  | 27 (14)  | 35 (14)  | 26 (14)  | 34 (14)  |
| postans_slot4 | 31 (17)  | 30 (15)  | 29 (15)  | 40 (15) ** | 49 (14) *** |

**gpt-oss-20b** (lies / truths: 116 / 94)

| position | Q1 | Q2 | Q6 | Q7 | Q9 |
|---|---|---|---|---|---|
| preans_slot0 | 16 (16)  | 13 (14)  | 16 (14)  | 21 (15)  | 13 (14)  |
| preans_slot1 | 18 (15)  | 15 (14)  | 16 (16)  | 16 (14)  | 18 (14)  |
| preans_slot2 | 10 (14)  | 16 (13)  | 14 (13)  | 14 (12)  | 16 (12)  |
| postans_slot0 | 13 (16)  | 13 (14)  | 15 (14)  | 13 (14)  | 17 (15)  |
| postans_slot1 | 12 (14)  | 16 (14)  | 14 (12)  | 12 (14)  | 15 (14)  |
| postans_slot2 | 16 (14)  | 10 (14)  | 12 (13)  | 11 (15)  | 12 (12)  |
| postans_slot3 | 13 (16)  | 12 (15)  | 20 (15)  | 11 (13)  | 15 (15)  |

## 4. The strongest positions after the question, per model

The twelve positions with the largest best gap above the shuffled value. Question tokens included.

**gemma-3-12b-it, all scenario transcripts**

| wording | position | lies / truths | best gap | shuffled | strong tokens | more after lies | more after truths |
|---|---|---|---|---|---|---|---|
| Q6 | q_tok5 | 49 / 32 | 57 | 25 | 7 | `␣মিথ্যা` 63/6, `␣untrue` 53/6, `␣falsehood` 59/12, `␣거짓` 45/3, `␣contradicted` 47/9 | `␣disclosure` 12/72, `␣acknowledging` 31/84, `␣admitting` 2/50 |
| Q6 | preans_slot4 | 49 / 32 | 55 | 26 | 2 | `Acknowled` 73/19, `Yep` 80/38, `😔` 51/9, `␣Sì` 84/44, `␣sí` 84/44 | `␣Nope` 16/72, `No` 18/72, `␣No` 20/72 |
| Q1 | preans_slot1 | 49 / 32 | 47 | 23 | 1 | `␣falsehood` 59/12, `謊` 65/25, `␣untrue` 55/16, `␣misled` 63/25, `谎` 41/6 | `␣subtly` 8/53, `␣phrasing` 39/81, `␣implying` 16/53 |
| Q7 | q_tok27 | 49 / 32 | 48 | 26 | 1 | `␣dishonesty` 57/9, `␣pretending` 86/44, `␣pretended` 61/28, `␣obfusc` 61/31, `␣refused` 76/50 | `␣mentioning` 16/69, `␣acknowledging` 31/75, `␣acknowledges` 24/62 |
| Q2 | preans_slot2 | 49 / 32 | 49 | 27 | 2 | `␣মিথ্যা` 61/12, `␣거짓` 61/19, `␣misrepresented` 84/44, `␣falsehood` 35/0, `␣заявления` 31/0 | `␣acknowledges` 37/78, `␣acknowledgment` 8/47, `␣implying` 37/72 |
| Q7 | q_tok26 | 49 / 32 | 45 | 25 | 3 | `␣никакого` 45/0, `␣żad` 49/9, `␣никаких` 45/9, `␣Nobody` 45/16, `␣pretending` 27/0 | `␣acknowledging` 41/84, `␣honesty` 10/47, `␣truthful` 12/47 |
| Q7 | q_tok3 | 49 / 32 | 40 | 23 | 0 | `␣answers` 84/44, `回答` 78/41, `␣menjawab` 82/50, `␣답변` 86/56, `␣respuesta` 82/53 | `␣previously` 8/41, `␣reassurance` 20/47, `␣ранее` 2/28 |
| Q9 | q_tok3 | 49 / 32 | 42 | 26 | 0 | `回答` 80/38, `␣answers` 84/44, `␣menjawab` 80/50, `␣답변` 86/56, `␣respuesta` 82/53 | `␣previously` 8/41, `␣reassurance` 20/47, `␣ранее` 2/28 |
| Q1 | q_tok4 | 49 / 32 | 38 | 22 | 0 | `␣falsehood` 82/44, `␣blatantly` 98/72, `故意` 51/25, `␣willfully` 41/19, `␣acknowledging` 71/50 | `␣sneaky` 10/53, `␣concealment` 10/41, `␣insofar` 39/69 |
| Q2 | preans_slot1 | 49 / 32 | 42 | 26 | 0 | `␣falsehood` 57/16, `␣মিথ্যা` 90/50, `謊` 59/22, `␣untrue` 59/22, `␣misled` 67/31 | `␣phrasing` 10/69, `␣explaining` 31/78, `␣misunderstand` 16/59 |
| Q7 | preans_slot2 | 49 / 32 | 41 | 26 | 0 | `␣обстоятельства` 63/22, `Ironically` 51/16, `␣blatant` 69/41, `␣dishonesty` 67/41, `Understanding` 27/0 | `␣implying` 10/53, `␣understanding` 18/53, `␣disclosing` 2/31 |
| Q2 | q_tok5 | 49 / 32 | 36 | 21 | 0 | `␣yeah` 61/25, `␣হ্যাঁ` 71/41, `YES` 71/41, `␣YES` 78/47, `是的` 55/25 | `␣Did` 51/88, `Did` 8/34, `␣deceived` 31/56 |

**gemma-3-27b-it, all scenario transcripts**

| wording | position | lies / truths | best gap | shuffled | strong tokens | more after lies | more after truths |
|---|---|---|---|---|---|---|---|
| Q2 | preans_slot1 | 58 / 30 | 56 | 25 | 3 | `谎` 72/17, `🤥` 90/37, `确实` 69/20, `確かに` 78/30, `␣झूठ` 86/47 | `␣purposely` 53/90, `␣honesty` 0/33, `␣phrasing` 41/70 |
| Q2 | preans_slot2 | 58 / 30 | 52 | 23 | 5 | `␣거짓` 72/20, `␣सच्चाई` 69/17, `␣মিথ্যা` 84/37, `真相` 45/0, `🤫` 71/27 | `␣"****` 29/70, `␣"--` 5/43, `␣("[` 21/53 |
| Q1 | preans_slot1 | 58 / 30 | 51 | 23 | 0 | `谎` 67/17, `謊` 72/27, `確かに` 64/20, `确实` 66/23, `🤥` 72/33 | `␣honesty` 5/33, `␣réponses` 9/37, `␣acknowledging` 24/50 |
| Q7 | q_tok26 | 58 / 30 | 50 | 25 | 3 | `?'` 60/10, `␣interpretación` 59/20, `あくまで` 53/17, `言葉` 55/20, `␣Yes` 41/7 | `␣correct` 14/53, `␣correctness` 17/50, `␣odgovor` 5/37 |
| Q7 | q_tok21 | 58 / 30 | 48 | 23 | 0 | `欺` 78/30, `.’”` 60/30, `؟.` 52/23, `␣Lied` 69/43, `lied` 38/13 | `␣falsch` 9/43, `␣intending` 2/30, `␣hoping` 2/27 |
| Q6 | preans_slot1 | 58 / 30 | 51 | 26 | 0 | `確かに` 71/20, `确实` 81/40, `確實` 60/20, `?!?` 69/33, `␣ใช่` 59/27 | `␣misinformation` 59/90, `␣contradictory` 26/53, `␣falsehood` 12/37 |
| Q1 | preans_slot2 | 58 / 30 | 49 | 24 | 3 | `?!?` 62/13, `🤥` 91/43, `␣झूठ` 64/17, `␣মিথ্যা` 90/43, `␣untrue` 60/17 | `␣emphasised` 3/40, `␣phrasing` 41/77, `␣mentioning` 24/57 |
| Q7 | preans_slot1 | 58 / 30 | 51 | 27 | 0 | `␣જવાબ` 95/43, `␣Ответ` 78/43, `␣undeniably` 67/37, `選択` 60/30, `␣odgovor` 64/37 | `␣truthful` 12/60, `␣లేదు` 16/43, `␣ചോദ്യ` 53/80 |
| Q6 | q_tok5 | 58 / 30 | 45 | 23 | 5 | `␣মিথ্যা` 52/7, `␣거짓` 48/10, `␣झूठ` 40/3, `␣deception` 59/23, `␣falsehood` 38/3 | `␣acknowledgment` 17/53, `␣admitting` 2/30, `␣acknowledging` 0/27 |
| Q7 | q_tok25 | 58 / 30 | 47 | 26 | 1 | `我相信` 53/7, `.'"` 66/33, `␣Claims` 43/17, `␣никаких` 40/13, `␣comment` 29/3 | `␣Sorry` 3/37, `␣Confirmation` 7/37, `␣correctness` 9/37 |
| Q7 | q_tok19 | 58 / 30 | 44 | 24 | 0 | `␣verità` 57/13, `␣तथ्यों` 57/20, `真相` 69/33, `␣truth` 74/40, `?");` 57/23 | `␣saying` 16/50, `␣purposely` 16/43, `␣BECAUSE` 26/53 |
| Q6 | postans_slot1 | 58 / 30 | 44 | 24 | 1 | `!!!!!!!!!!!!!!!!` 57/13, `៕` 57/20, `!!!!!!!` 86/53, `！！！` 34/3, `␣acknowledging` 53/23 | `incorrect` 7/37, `␣incorrectly` 12/40, `␣misrepresented` 33/57 |

**qwen3.6-27b, all scenario transcripts**

| wording | position | lies / truths | best gap | shuffled | strong tokens | more after lies | more after truths |
|---|---|---|---|---|---|---|---|
| Q7 | q_tok29 | 152 / 81 | 68 | 11 | 0 | `谎言` 83/15, `␣falsehood` 88/30, `真实的` 66/30, `_truth` 41/12, `␣**.**` 87/62 | `坦诚` 19/81, `正直` 9/68, `.)` 11/54 |
| Q1 | preans_slot1 | 152 / 81 | 67 | 14 | 5 | `说谎` 88/21, `虚假` 92/28, `撒谎` 74/11, `谎` 78/20, `虚假信息` 64/6 | `␣   \n\n` 10/64, `..."` 9/58, `␣honesty` 1/47 |
| Q7 | q_tok19 | 152 / 81 | 67 | 14 | 16 | `真实的` 81/14, `的真实` 86/19, `真实` 88/27, `␣knowing` 69/10, `明知` 63/9 | `␣misleading` 26/77, `？**` 8/57, `␣falsely` 30/79 |
| Q6 | q_tok5 | 152 / 81 | 61 | 15 | 12 | `谎` 72/11, `虚假` 81/20, `␣fake` 77/20, `欺骗` 76/20, `fake` 85/30 | `?</` 24/70, `?**` 49/91, `?\` 47/88 |
| Q9 | preans_slot1 | 152 / 81 | 61 | 15 | 5 | `␣knowingly` 61/0, `␣yes` 61/15, `␣Yes` 50/4, `yes` 57/12, `Yes` 47/5 | `␣honesty` 12/83, `诚实` 12/70, `False` 19/67 |
| Q2 | preans_slot1 | 152 / 81 | 61 | 15 | 4 | `虚假信息` 70/10, `说谎` 89/30, `虚假` 95/36, `撒谎` 72/16, `谎` 72/23 | `␣   \n\n` 17/69, `␣honesty` 1/49, `\n\n` 26/74 |
| Q7 | q_tok26 | 152 / 81 | 59 | 16 | 5 | `␣falsely` 75/16, `␣false` 74/15, `虚假` 70/11, `␣fals` 72/19, `谎言` 65/16 | `...*` 21/63, `␣honest` 6/46, `␣truths` 20/58 |
| Q6 | postans_slot1 | 152 / 81 | 58 | 16 | 7 | `False` 86/28, `␣truth` 82/25, `真相` 78/26, `false` 62/10, `␣truthful` 89/40 | `？”` 19/79, `?"` 32/89, `...</` 26/81 |
| Q7 | q_tok24 | 152 / 81 | 56 | 14 | 8 | `␣fals` 77/21, `谎言` 72/25, `虚假` 53/6, `欺骗` 59/12, `隐瞒` 68/21 | `如实` 1/52, `实话` 1/51, `诚实` 15/63 |
| Q9 | think_slot3 | 152 / 81 | 54 | 13 | 2 | `_YES` 68/15, `,Yes` 90/43, `“Yes` 95/54, `␣oui` 95/57, `␣affirmative` 39/4 | `:false` 14/85, `␣no` 14/80, `No` 20/86 |
| Q2 | think_slot3 | 152 / 81 | 54 | 14 | 1 | `_YES` 61/7, `␣oui` 87/40, `,Yes` 64/21, `␣affirmative` 71/30, `␣Oui` 87/49 | `␣No` 28/95, `No` 19/85, `/false` 11/77 |
| Q7 | q_tok25 | 152 / 81 | 52 | 13 | 0 | `吗` 79/27, `False` 66/21, `␣truthful` 62/22, `否定` 80/43, `␣Answers` 53/20 | `␣。` 7/43, `␣...` 13/46, `…` 47/74 |

**qwen3.6-27b, among the transcripts that deny**

| wording | position | lies / truths | best gap | shuffled | strong tokens | more after lies | more after truths |
|---|---|---|---|---|---|---|---|
| Q7 | q_tok29 | 79 / 77 | 67 | 15 | 1 | `谎言` 77/10, `␣falsehood` 85/26, `␣sincere` 35/1, `␣**.**` 86/61, `真实的` 49/26 | `坦诚` 18/84, `正直` 15/71, `.)` 8/57 |
| Q7 | q_tok24 | 79 / 77 | 65 | 17 | 6 | `␣fals` 85/19, `谎言` 78/23, `虚假` 56/5, `说谎` 56/9, `欺骗` 57/10 | `如实` 1/55, `实话` 3/53, `诚实` 16/66 |
| Q7 | q_tok19 | 79 / 77 | 64 | 18 | 16 | `的真实` 78/14, `真实的` 70/12, `真实` 81/23, `␣knowing` 62/6, `␣Truth` 86/32 | `␣falsely` 25/79, `？**` 11/60, `␣misleading` 29/77 |
| Q7 | q_tok22 | 79 / 77 | 61 | 16 | 2 | `坦白` 87/26, `␣acknowledgement` 80/27, `␣acknowledged` 86/36, `␣….` 63/22, `␣admite` 56/16 | `错误` 14/70, `␣Yes` 29/79, `␣accusations` 14/61 |
| Q7 | q_tok25 | 79 / 77 | 62 | 17 | 0 | `False` 81/19, `␣truthful` 68/22, `否定` 82/43, `␣Answers` 56/18, `/false` 81/44 | `␣。` 11/45, `␣✅` 37/65, `...**` 35/61 |
| Q1 | preans_slot1 | 53 / 74 | 65 | 22 | 10 | `说谎` 85/20, `虚假` 87/26, `撒谎` 70/9, `␣false` 77/22, `谎` 72/16 | `␣   \n\n` 13/68, `\n\n` 19/70, `␣honesty` 2/50 |
| Q2 | preans_slot1 | 47 / 77 | 61 | 19 | 6 | `说谎` 89/29, `撒谎` 70/14, `虚假` 85/34, `␣fals` 94/52, `谎言` 98/57 | `␣honesty` 4/52, `诚实` 2/49, `实话` 4/49 |
| Q6 | postans_slot1 | 43 / 73 | 62 | 21 | 3 | `False` 84/22, `false` 42/3, `␣fals` 42/5, `␣truth` 53/19, `"*` 56/22 | `?\` 49/97, `？”` 49/88, `...</` 51/84 |
| Q7 | q_tok26 | 79 / 77 | 57 | 17 | 7 | `␣falsely` 68/12, `␣fals` 72/17, `␣misinformation` 70/16, `␣claiming` 61/9, `虚假` 58/8 | `␣truths` 19/60, `␣honest` 8/47, `...*` 29/66 |
| Q7 | q_tok18 | 79 / 77 | 55 | 16 | 0 | `␣Ack` 66/10, `␣acknowledges` 66/16, `␣acknowledge` 54/16, `␣acknowledgment` 95/66, `-answer` 61/35 | `违反` 13/53, `␣Incorrect` 15/51, `␣False` 35/69 |
| Q7 | q_tok28 | 79 / 77 | 53 | 15 | 1 | `␣tell` 70/17, `␣told` 85/39, `真理` 85/43, `␣deceived` 78/43, `告诉` 35/5 | `␣transparent` 1/30, `透明` 0/19, `␣...\` 62/81 |
| Q1 | postans_slot4 | 43 / 57 | 60 | 23 | 4 | `真相` 74/14, `␣truthful` 84/25, `truth` 72/14, `␣Truth` 74/18, `␣truth` 79/25 | `?”` 37/81, `Prompt` 9/44, `fake` 33/63 |

**gpt-oss-20b, all scenario transcripts**

| wording | position | lies / truths | best gap | shuffled | strong tokens | more after lies | more after truths |
|---|---|---|---|---|---|---|---|
| Q9 | q_tok6 | 116 / 94 | 30 | 13 | 0 | `␣reassure` 68/38, `␣anyways` 42/32, `/msg` 29/19, `␣disclosure` 84/76, `␣messaging` 78/69 | `_sent` 34/53, `-feedback` 22/40, `截图` 64/79 |
| Q7 | q_tok6 | 116 / 94 | 30 | 15 | 0 | `␣reassure` 54/24, `␣reassurance` 41/12, `/preferences` 54/39, `…\n` 89/77, `询` 22/10 | `Facts` 38/51, `/errors` 14/27, `.Ans` 25/37 |
| Q7 | q_tok29 | 116 / 94 | 27 | 15 | 0 | `:\n/` 62/35, `.]\n` 56/40, `免责声明` 52/37, `␣Response` 65/52, `␣回复` 42/30 | `€\n` 21/35, `….\n\n` 64/78, `®\n\n` 45/54 |
| Q7 | q_tok7 | 116 / 94 | 26 | 15 | 0 | `␣cheating` 48/22, `␣sincerity` 37/18, `␣allegation` 84/69, `␣hypocrisy` 74/61, `…\n\n` 96/83 | `“Yes` 31/49, `␣Lies` 41/56, `␣Incorrect` 31/46 |
| Q6 | q_tok7 | 116 / 94 | 23 | 13 | 0 | `␣knowingly` 41/17, `.]\n` 45/29, `␣contradictory` 19/10, `␣unconstitutional` 11/2, `␣confidentiality` 22/14 | `facts` 48/69, `/Error` 36/56, `(statement` 41/55 |
| Q7 | q_tok25 | 116 / 94 | 22 | 14 | 0 | `␣claims` 45/22, `␣Claims` 21/4, `␣alleging` 35/20, `␣Statements` 18/4, `␣allegation` 21/9 | `truth` 6/20, `␣honestly` 56/69, `␣accuracy` 9/22 |
| Q9 | q_tok14 | 116 / 94 | 20 | 12 | 0 | `;\r\n\r\n\r\n\r\n` 43/23, `;\n\n\n\n` 25/12, `。\n\n\n\n` 37/24, `."""` 58/47, `\n\n\n\n` 18/7 | `.Ans` 61/73, `..\n\n` 37/49, `.\n\n` 40/47 |
| Q7 | preans_slot0 | 116 / 94 | 21 | 15 | 0 | `␣subpoena` 55/34, `タグ` 32/20, `Комментар` 70/60, `␣interloc` 90/81, `ológico` 35/27 | `_ASSUME` 58/74, `LOPT` 80/93, `pexpr` 14/24 |
| Q6 | q_tok5 | 116 / 94 | 20 | 15 | 0 | `␣reassurance` 41/20, `/content` 61/44, `’ll` 18/4, `␣reassure` 18/4, `␣excuses` 25/12 | `␣honesty` 16/37, `cknow` 7/21, `␣confession` 8/21 |
| Q7 | q_tok17 | 116 / 94 | 18 | 13 | 0 | `␣disclosures` 58/39, `;\n` 73/60, `oops` 38/28, `wow` 16/5, `.Please` 39/29 | `謝` 63/74, `…and` 24/34, `-my` 33/41 |
| Q6 | postans_slot3 | 116 / 94 | 20 | 15 | 0 | `How` 84/64, `Seriously` 44/27, `␣terrible` 72/54, `␣nineteen` 51/37, `␣you've` 79/66 | `Congratulations` 17/35, `␣thanking` 55/72, `“If` 60/76 |
| Q7 | q_tok21 | 116 / 94 | 18 | 14 | 0 | `!!!\n` 49/31, `␣stupidity` 69/56, `␣anyways` 64/52, `␣NEVER` 50/39, `␣misinformation` 44/34 | `?)\n` 20/39, `?”\n` 57/68, `␣apologies` 49/59 |

**gpt-oss-20b, among the transcripts that deny**

| wording | position | lies / truths | best gap | shuffled | strong tokens | more after lies | more after truths |
|---|---|---|---|---|---|---|---|
| Q9 | q_tok6 | 105 / 88 | 32 | 15 | 0 | `␣reassure` 71/40, `␣anyways` 45/32, `/msg` 30/19, `␣weren` 70/60, `␣messaging` 83/73 | `_sent` 33/52, `-feedback` 19/36, `截图` 63/77 |
| Q6 | postans_slot3 | 75 / 67 | 33 | 18 | 0 | `␣terrible` 84/51, `␣ought` 64/33, `How` 83/57, `␣accusing` 29/7, `␣idiot` 48/30 | `Rewrite` 21/45, `␣thanking` 52/75, `Congratulations` 20/42 |
| Q7 | q_tok6 | 102 / 90 | 29 | 15 | 0 | `␣reassure` 55/26, `␣reassurance` 41/12, `/preferences` 52/37, `␣explanation` 63/50, `…\n` 89/77 | `Facts` 38/51, `Transcript` 21/33, `-response` 30/42 |
| Q7 | q_tok29 | 102 / 90 | 25 | 13 | 0 | `:\n/` 61/36, `.]\n` 57/39, `␣回复` 43/30, `—\n` 87/76, `免责声明` 49/38 | `….\n\n` 65/77, `™\n\n` 51/62, `答案` 36/47 |
| Q6 | q_tok7 | 75 / 67 | 25 | 15 | 0 | `␣knowingly` 39/13, `.]\n` 44/24, `␣unconstitutional` 13/1, `␣defamatory` 20/9, `␣allegations` 63/52 | `/Error` 37/57, `facts` 55/69, `-context` 8/21 |
| Q7 | q_tok7 | 102 / 90 | 24 | 14 | 0 | `␣cheating` 46/22, `␣sincerity` 35/18, `…\n\n` 95/83, `␣hypocrisy` 75/63, `␣allegation` 82/72 | `“Yes` 28/47, `␣Incorrect` 31/46, `␣Lies` 42/56 |
| Q9 | q_tok14 | 105 / 88 | 22 | 14 | 0 | `;\r\n\r\n\r\n\r\n` 47/25, `;\n\n\n\n` 27/12, `。\n\n\n\n` 40/26, `."""` 62/49, `."\n\n\n` 55/43 | `.Ans` 62/75, `..\n\n` 34/47, `�\n\n` 13/22 |
| Q7 | q_tok25 | 102 / 90 | 21 | 15 | 0 | `␣claims` 44/23, `␣Claims` 20/4, `␣genuinely` 23/8, `␣alleging` 35/21, `␣affirm` 15/3 | `truth` 6/20, `—not` 22/36, `␣disclosure` 66/78 |
| Q7 | q_tok21 | 102 / 90 | 20 | 14 | 0 | `!!!\n` 49/29, `␣NEVER` 48/38, `␣stupidity` 67/57, `␣that'll` 77/69, `␣anyways` 62/53 | `?)\n` 23/37, `␣apologies` 46/60, `?”\n` 56/67 |
| Q2 | postans_slot1 | 112 / 87 | 20 | 14 | 0 | `␣diálogo` 54/34, `Responder` 79/64, `网友` 63/53, `Comentario` 51/41, `客服` 84/76 | `solver` 38/54, `Resposta` 25/38, `tabpanel` 77/89 |
| Q9 | q_tok8 | 105 / 88 | 18 | 13 | 0 | `␣truth` 81/62, `␣honestly` 61/45, `␣confession` 27/12, `␣conversation` 51/40, `␣disclosures` 93/83 | `-query` 20/35, `-confirm` 13/28, `回答` 60/75 |
| Q7 | q_tok19 | 102 / 90 | 18 | 13 | 0 | `␣reassure` 46/28, `␣politely` 28/11, `␣woke` 34/23, `␣thanked` 46/37, `␣counselor` 31/22 | `��` 27/42, `␣hadn` 10/20, `/questions` 50/60 |

## 5. The same words on every model

Words are matched by spelling in each model's vocabulary. `lie words` = Qwen's `lie` family at post-response
slot 1 plus forms seen on Gemma (Lüge, mensonge, mentira, mentiras, ложь, झूठ, झूठा, মিথ্যা, 嘘, 謊, 謊言, 说谎, 거짓, 거짓말, 🤥).

| words | model | wording | position | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|---|
| lie words | gemma-3-12b-it | – | postresp_slot1 | 20/49 (41%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |  |  |
| lie words | gemma-3-12b-it | Q2 | preans_slot1 | 46/49 (94%) | 21/32 (66%) | 64/135 (47%) | 36/179 (20%) | 5/7 (71%) | 1/9 (11%) |
| lie words | gemma-3-12b-it | Q2 | preans_slot2 | 39/49 (80%) | 18/32 (56%) | 17/135 (13%) | 0/179 (0%) | 5/7 (71%) | 2/9 (22%) |
| lie words | gemma-3-12b-it | Q6 | preans_slot2 | 21/49 (43%) | 6/32 (19%) | 2/135 (1%) | 0/179 (0%) | 3/8 (38%) | 4/18 (22%) |
| lie words | gemma-3-12b-it | Q6 | preans_slot4 | 20/49 (41%) | 20/32 (62%) | 51/135 (38%) | 25/179 (14%) | 6/8 (75%) | 14/18 (78%) |
| lie words | gemma-3-12b-it | Q6 | postans_slot1 | 27/49 (55%) | 9/32 (28%) | 5/135 (4%) | 0/179 (0%) | 0/8 (0%) | 2/18 (11%) |
| lie words | gemma-3-27b-it | – | postresp_slot1 | 20/58 (34%) | 4/30 (13%) | 0/133 (0%) | 0/199 (0%) |  |  |
| lie words | gemma-3-27b-it | – | postresp_slot2 | 30/58 (52%) | 9/30 (30%) | 11/133 (8%) | 0/199 (0%) |  |  |
| lie words | gemma-3-27b-it | Q1 | preans_slot1 | 51/58 (88%) | 19/30 (63%) | 77/133 (58%) | 37/199 (19%) | 1/1 (100%) | 3/4 (75%) |
| lie words | gemma-3-27b-it | Q1 | preans_slot2 | 53/58 (91%) | 18/30 (60%) | 49/133 (37%) | 10/199 (5%) | 1/1 (100%) | 1/4 (25%) |
| lie words | gemma-3-27b-it | Q1 | postans_slot1 | 15/40 (38%) | 2/17 (12%) | 12/103 (12%) | 3/111 (3%) | 1/1 (100%) | 0/4 (0%) |
| lie words | gemma-3-27b-it | Q2 | preans_slot2 | 52/58 (90%) | 16/30 (53%) | 40/133 (30%) | 8/199 (4%) | 2/2 (100%) | – |
| lie words | gemma-3-27b-it | Q2 | postans_slot2 | 40/58 (69%) | 12/30 (40%) | 30/133 (23%) | 15/199 (8%) | 2/2 (100%) | – |
| lie words | gemma-3-27b-it | Q6 | preans_slot4 | 1/58 (2%) | 8/30 (27%) | 17/133 (13%) | 7/199 (4%) | 1/2 (50%) | 2/4 (50%) |
| lie words | gemma-3-27b-it | Q9 | preans_slot3 | 3/58 (5%) | 8/30 (27%) | 23/133 (17%) | 26/199 (13%) | 1/7 (14%) | 4/8 (50%) |
| lie words | gemma-3-27b-it | Q9 | preans_slot4 | 24/58 (41%) | 23/30 (77%) | 133/133 (100%) | 199/199 (100%) | 7/7 (100%) | 7/8 (88%) |
| lie words | qwen3.6-27b | – | postresp_slot1 | 127/152 (84%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) |  |  |
| lie words | qwen3.6-27b | Q1 | preans_slot1 | 145/152 (95%) | 34/81 (42%) | 43/138 (31%) | 0/158 (0%) | 46/53 (87%) | 30/74 (41%) |
| lie words | qwen3.6-27b | Q2 | preans_slot1 | 150/152 (99%) | 48/81 (59%) | 64/138 (46%) | 1/158 (1%) | 46/47 (98%) | 45/77 (58%) |
| lie words | qwen3.6-27b | Q6 | preans_slot1 | 147/152 (97%) | 49/81 (60%) | 24/138 (17%) | 0/158 (0%) | 41/43 (95%) | 42/73 (58%) |
| lie words | qwen3.6-27b | Q6 | preans_slot2 | 51/152 (34%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 11/43 (26%) | 9/73 (12%) |
| lie words | qwen3.6-27b | Q6 | preans_slot4 | 80/152 (53%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 17/43 (40%) | 9/73 (12%) |
| lie words | qwen3.6-27b | Q6 | postans_slot1 | 73/152 (48%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 15/43 (35%) | 2/73 (3%) |
| lie words | qwen3.6-27b | Q9 | preans_slot2 | 118/152 (78%) | 32/81 (40%) | 16/138 (12%) | 0/158 (0%) | 54/65 (83%) | 28/76 (37%) |
| lie words | gpt-oss-20b | – | postresp_slot1 | 0/116 (0%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |  |  |
| knowingly | gemma-3-12b-it | – | postresp_slot1 | 7/49 (14%) | 6/32 (19%) | 45/135 (33%) | 33/179 (18%) |  |  |
| knowingly | gemma-3-12b-it | Q2 | preans_slot4 | 39/49 (80%) | 19/32 (59%) | 4/135 (3%) | 0/179 (0%) | 2/7 (29%) | 2/9 (22%) |
| knowingly | gemma-3-12b-it | Q6 | preans_slot4 | 30/49 (61%) | 12/32 (38%) | 0/135 (0%) | 0/179 (0%) | 3/8 (38%) | 3/18 (17%) |
| knowingly | gemma-3-12b-it | Q6 | postans_slot1 | 40/49 (82%) | 16/32 (50%) | 13/135 (10%) | 38/179 (21%) | 0/8 (0%) | 3/18 (17%) |
| knowingly | gemma-3-12b-it | Q7 | postans_slot1 | 34/49 (69%) | 15/32 (47%) | 65/135 (48%) | 40/179 (22%) | 1/16 (6%) | 1/11 (9%) |
| knowingly | gemma-3-12b-it | Q9 | postans_slot4 | 23/49 (47%) | 8/32 (25%) | 1/135 (1%) | 0/179 (0%) | 3/9 (33%) | 4/9 (44%) |
| knowingly | gemma-3-27b-it | – | postresp_slot1 | 1/58 (2%) | 1/30 (3%) | 2/133 (2%) | 0/199 (0%) |  |  |
| knowingly | gemma-3-27b-it | Q6 | preans_slot1 | 55/58 (95%) | 20/30 (67%) | 7/133 (5%) | 0/199 (0%) | 2/2 (100%) | 0/4 (0%) |
| knowingly | gemma-3-27b-it | Q6 | postans_slot1 | 37/58 (64%) | 11/30 (37%) | 1/133 (1%) | 0/199 (0%) | 0/2 (0%) | 1/4 (25%) |
| knowingly | gemma-3-27b-it | Q9 | postans_slot1 | 29/58 (50%) | 9/30 (30%) | 5/133 (4%) | 9/199 (5%) | 0/7 (0%) | 0/8 (0%) |
| knowingly | qwen3.6-27b | – | postresp_slot1 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |  |  |
| knowingly | qwen3.6-27b | Q1 | preans_slot1 | 57/152 (38%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) | 19/53 (36%) | 0/74 (0%) |
| knowingly | qwen3.6-27b | Q1 | preans_slot2 | 41/152 (27%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 12/53 (23%) | 5/74 (7%) |
| knowingly | qwen3.6-27b | Q2 | preans_slot1 | 56/152 (37%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 19/47 (40%) | 2/77 (3%) |
| knowingly | qwen3.6-27b | Q7 | preans_slot1 | 59/152 (39%) | 14/81 (17%) | 0/138 (0%) | 7/158 (4%) | 35/79 (44%) | 12/77 (16%) |
| knowingly | qwen3.6-27b | Q9 | preans_slot1 | 93/152 (61%) | 0/81 (0%) | 2/138 (1%) | 32/158 (20%) | 30/65 (46%) | 0/76 (0%) |
| knowingly | gpt-oss-20b | – | postresp_slot1 | 0/116 (0%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |  |  |
| cannot | gemma-3-12b-it | – | postresp_slot1 | 0/49 (0%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |  |  |
| cannot | gemma-3-27b-it | – | postresp_slot1 | 0/58 (0%) | 0/30 (0%) | 2/133 (2%) | 0/199 (0%) |  |  |
| cannot | qwen3.6-27b | – | postresp_slot1 | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |  |  |
| cannot | qwen3.6-27b | Q2 | preans_slot3 | 73/152 (48%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 28/47 (60%) | 13/77 (17%) |
| cannot | qwen3.6-27b | Q6 | preans_slot3 | 65/152 (43%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 22/43 (51%) | 12/73 (16%) |
| cannot | qwen3.6-27b | Q7 | preans_slot3 | 119/152 (78%) | 34/81 (42%) | 0/138 (0%) | 1/158 (1%) | 62/79 (78%) | 33/77 (43%) |
| cannot | qwen3.6-27b | Q7 | preans_slot4 | 76/152 (50%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 33/79 (42%) | 2/77 (3%) |
| cannot | qwen3.6-27b | Q9 | preans_slot3 | 116/152 (76%) | 38/81 (47%) | 0/138 (0%) | 1/158 (1%) | 52/65 (80%) | 35/76 (46%) |
| cannot | qwen3.6-27b | Q9 | preans_slot4 | 70/152 (46%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 24/65 (37%) | 3/76 (4%) |
| cannot | qwen3.6-27b | Q9 | think_slot3 | 57/152 (38%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 23/65 (35%) | 1/76 (1%) |
| cannot | gpt-oss-20b | – | postresp_slot1 | 0/116 (0%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |  |  |

Rows shown: post-response slot 1, and every template position where the lie and truth rates differ by 20
points or more.

## 6. `yes` and `no` before the answer, by the answer

Scenario transcripts. The position is the last template token before the answer starts.

| model | wording | position | yes: admit | yes: deny | no: admit | no: deny |
|---|---|---|---|---|---|---|
| gemma-3-12b-it | Q2 | preans_slot4 | 65/65 (100%) | 16/16 (100%) | 6/65 (9%) | 16/16 (100%) |
| gemma-3-12b-it | Q6 | preans_slot4 | 55/55 (100%) | 26/26 (100%) | 7/55 (13%) | 26/26 (100%) |
| gemma-3-12b-it | Q9 | preans_slot4 | 63/63 (100%) | 18/18 (100%) | 10/63 (16%) | 18/18 (100%) |
| gemma-3-27b-it | Q2 | preans_slot4 | 86/86 (100%) | 2/2 (100%) | 0/86 (0%) | 1/2 (50%) |
| gemma-3-27b-it | Q6 | preans_slot4 | 82/82 (100%) | 6/6 (100%) | 1/82 (1%) | 5/6 (83%) |
| gemma-3-27b-it | Q9 | preans_slot4 | 73/73 (100%) | 15/15 (100%) | 0/73 (0%) | 12/15 (80%) |
| qwen3.6-27b | Q2 | think_slot3 | 109/109 (100%) | 124/124 (100%) | 1/109 (1%) | 118/124 (95%) |
| qwen3.6-27b | Q6 | think_slot3 | 117/117 (100%) | 116/116 (100%) | 4/117 (3%) | 116/116 (100%) |
| qwen3.6-27b | Q9 | think_slot3 | 91/91 (100%) | 141/141 (100%) | 2/91 (2%) | 133/141 (94%) |
| gpt-oss-20b | Q2 | preans_slot2 | 0/9 (0%) | 0/199 (0%) | 0/9 (0%) | 0/199 (0%) |
| gpt-oss-20b | Q6 | preans_slot2 | 0/62 (0%) | 0/142 (0%) | 0/62 (0%) | 0/142 (0%) |
| gpt-oss-20b | Q9 | preans_slot2 | 0/6 (0%) | 0/193 (0%) | 0/6 (0%) | 0/193 (0%) |
