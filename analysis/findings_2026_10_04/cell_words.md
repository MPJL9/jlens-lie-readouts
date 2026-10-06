# Words that are exceptionally frequent for one prompt type and one self-report wording

Written by `scripts/findings_2026_10_04/cell_words.py`. Qwen, J-lens, band 35 to 58, build split and unrelated chats, in-sample. A word joins the spellings of a token (spaces, capitals, punctuation at the edges). Shares are transcripts with the word in the band's readout at the token. Searched over every word; the lists below are selected from several thousand words per cell, so each needs a check before it is used. `(q)` = the word is in the question's own text.


## At the newline after the question (preans_slot1)

**pressured, Q1: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 谎 | 58% | 4% | 119/152 | 16/81 | 6/138 | 0/703 |
| 欺骗 | 75% | 23% | 141/152 | 33/81 | 32/138 | 25/703 |
| 撒谎 | 52% | 1% | 112/152 | 9/81 | 1/138 | 0/703 |
| 说谎 | 65% | 15% | 134/152 | 17/81 | 21/138 | 0/703 |
| 谎言 | 76% | 28% | 145/152 | 33/81 | 39/138 | 0/703 |
| false | 63% | 15% | 124/152 | 22/81 | 21/138 | 31/703 |
| fals | 76% | 29% | 143/152 | 35/81 | 40/138 | 5/703 |
| falsely | 71% | 28% | 136/152 | 29/81 | 38/138 | 59/703 |
| misrepresented | 53% | 10% | 101/152 | 22/81 | 14/138 | 38/703 |
| 误导 | 69% | 28% | 131/152 | 30/81 | 38/138 | 173/703 |

**pressured, Q2: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| fals | 82% | 25% | 147/152 | 44/81 | 34/138 | 7/703 |
| misrepresented | 65% | 12% | 118/152 | 33/81 | 17/138 | 58/703 |
| 撒谎 | 53% | 1% | 110/152 | 13/81 | 2/138 | 0/703 |
| 欺骗 | 82% | 31% | 146/152 | 44/81 | 43/138 | 107/703 |
| 谎 | 55% | 7% | 110/152 | 19/81 | 10/138 | 1/703 |
| false | 69% | 22% | 129/152 | 32/81 | 30/138 | 123/703 |
| 谎言 | 85% | 41% | 150/152 | 47/81 | 57/138 | 0/703 |
| deception | 48% | 6% | 89/152 | 24/81 | 8/138 | 7/703 |
| 说谎 | 68% | 29% | 135/152 | 24/81 | 40/138 | 0/703 |
| untrue | 38% | 0% | 81/152 | 7/81 | 0/138 | 2/703 |

**pressured, Q6: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| stating | 76% | 33% | 118/152 | 58/81 | 116/138 | 113/703 |
| 声称 | 61% | 29% | 111/152 | 32/81 | 20/138 | 69/703 |

**pressured, Q6: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| fals | 82% | 6% | 145/152 | 46/81 | 8/138 | 0/703 |
| false (q) | 82% | 13% | 144/152 | 47/81 | 18/138 | 11/703 |
| 谎言 | 84% | 16% | 147/152 | 49/81 | 22/138 | 1/703 |
| 欺骗 | 66% | 1% | 126/152 | 28/81 | 1/138 | 0/703 |
| falsely | 81% | 16% | 144/152 | 44/81 | 22/138 | 10/703 |
| 虚假 | 80% | 15% | 145/152 | 41/81 | 21/138 | 47/703 |
| 谎 | 66% | 1% | 124/152 | 29/81 | 2/138 | 1/703 |
| 隐瞒 | 62% | 2% | 106/152 | 38/81 | 3/138 | 0/703 |
| 说谎 | 63% | 6% | 117/152 | 30/81 | 8/138 | 1/703 |
| fake | 67% | 12% | 123/152 | 34/81 | 17/138 | 61/703 |

**pressured, Q7: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| instructions | 80% | 2% | 129/152 | 57/81 | 123/138 | 52/703 |
| constraints | 69% | 1% | 105/152 | 56/81 | 130/138 | 16/703 |
| prompt | 71% | 4% | 123/152 | 42/81 | 126/138 | 39/703 |
| backstory | 66% | 3% | 118/152 | 35/81 | 10/138 | 1/703 |
| instruction | 64% | 2% | 104/152 | 45/81 | 123/138 | 48/703 |
| 指令 | 62% | 1% | 97/152 | 47/81 | 120/138 | 42/703 |
| scenario | 60% | 3% | 102/152 | 38/81 | 0/138 | 0/703 |
| unethical | 66% | 10% | 99/152 | 54/81 | 6/138 | 246/703 |
| 秘密 | 57% | 3% | 103/152 | 29/81 | 19/138 | 1/703 |
| prompts | 55% | 1% | 98/152 | 29/81 | 101/138 | 29/703 |

**pressured, Q7: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| scenario | 60% | 0% | 102/152 | 38/81 | 0/138 | 0/703 |
| backstory | 66% | 7% | 118/152 | 35/81 | 10/138 | 1/703 |
| scenarios | 46% | 0% | 82/152 | 26/81 | 0/138 | 1/703 |
| 隐瞒 | 72% | 29% | 121/152 | 47/81 | 40/138 | 29/703 |
| 秘密 | 57% | 14% | 103/152 | 29/81 | 19/138 | 1/703 |
| 情境 | 41% | 0% | 73/152 | 23/81 | 0/138 | 0/703 |
| secretly | 39% | 1% | 72/152 | 19/81 | 1/138 | 1/703 |
| 的真实 | 46% | 10% | 92/152 | 16/81 | 5/138 | 72/703 |
| 真实的 | 38% | 5% | 77/152 | 12/81 | 3/138 | 35/703 |
| secret | 39% | 7% | 74/152 | 17/81 | 10/138 | 0/703 |

**pressured, Q9: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| deceive | 68% | 2% | 104/152 | 55/81 | 94/138 | 515/703 |
| dishonest | 78% | 27% | 118/152 | 63/81 | 90/138 | 551/703 |
| deceived | 50% | 1% | 82/152 | 34/81 | 26/138 | 127/703 |
| deception | 92% | 48% | 145/152 | 70/81 | 115/138 | 626/703 |
| 欺诈 | 45% | 1% | 58/152 | 46/81 | 69/138 | 468/703 |
| 撒谎 | 95% | 53% | 146/152 | 76/81 | 115/138 | 446/703 |
| deceit | 43% | 2% | 65/152 | 36/81 | 20/138 | 283/703 |
| yes (q) | 45% | 6% | 93/152 | 13/81 | 3/138 | 30/703 |
| deceptive | 69% | 34% | 117/152 | 44/81 | 28/138 | 229/703 |
| truth | 100% | 65% | 151/152 | 81/81 | 138/138 | 692/703 |

**pressured, Q9: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 伪造 | 72% | 28% | 128/152 | 39/81 | 38/138 | 106/703 |
| yes (q) | 45% | 4% | 93/152 | 13/81 | 3/138 | 30/703 |
| deceptive | 69% | 33% | 117/152 | 44/81 | 28/138 | 229/703 |
| conceal | 36% | 0% | 76/152 | 9/81 | 0/138 | 0/703 |
| deceived | 50% | 19% | 82/152 | 34/81 | 26/138 | 127/703 |
| misleading | 44% | 14% | 73/152 | 29/81 | 19/138 | 27/703 |

**no-pressure truths, Q1: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 如实 | 54% | 11% | 0/152 | 26/81 | 75/138 | 29/703 |
| honesty | 59% | 17% | 1/152 | 38/81 | 82/138 | 50/703 |
| 诚实 | 58% | 17% | 2/152 | 37/81 | 80/138 | 68/703 |
| based | 35% | 1% | 0/152 | 0/81 | 48/138 | 7/703 |
| 基于 | 34% | 1% | 0/152 | 0/81 | 47/138 | 9/703 |
| 实话 | 46% | 15% | 2/152 | 33/81 | 64/138 | 26/703 |
| 依据 | 30% | 0% | 1/152 | 0/81 | 42/138 | 0/703 |

**no-pressure truths, Q2: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| based | 36% | 0% | 0/152 | 0/81 | 50/138 | 3/703 |
| 基于 | 35% | 1% | 0/152 | 0/81 | 48/138 | 5/703 |

**no-pressure truths, Q6: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| incorrect | 72% | 16% | 36/152 | 33/81 | 100/138 | 465/703 |
| stating | 84% | 28% | 118/152 | 58/81 | 116/138 | 113/703 |
| statement (q) | 80% | 26% | 36/152 | 43/81 | 111/138 | 159/703 |
| 正确 | 65% | 14% | 1/152 | 11/81 | 90/138 | 407/703 |
| saying | 62% | 12% | 100/152 | 40/81 | 85/138 | 71/703 |
| 正确的 | 62% | 12% | 1/152 | 13/81 | 85/138 | 398/703 |
| 是正确的 | 53% | 5% | 0/152 | 12/81 | 73/138 | 329/703 |
| assertions | 53% | 7% | 42/152 | 33/81 | 73/138 | 158/703 |
| statements | 93% | 57% | 72/152 | 55/81 | 128/138 | 372/703 |
| correctness | 41% | 9% | 0/152 | 15/81 | 57/138 | 404/703 |

**no-pressure truths, Q6: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 陈述 | 86% | 31% | 29/152 | 39/81 | 118/138 | 215/703 |
| statement (q) | 80% | 34% | 36/152 | 43/81 | 111/138 | 159/703 |
| align | 41% | 0% | 0/152 | 0/81 | 56/138 | 0/703 |
| 基于 | 42% | 2% | 1/152 | 0/81 | 58/138 | 14/703 |
| 事实 | 81% | 42% | 35/152 | 45/81 | 112/138 | 296/703 |
| based | 40% | 1% | 2/152 | 0/81 | 55/138 | 10/703 |
| referencing | 40% | 2% | 0/152 | 1/81 | 55/138 | 11/703 |
| statements | 93% | 55% | 72/152 | 55/81 | 128/138 | 372/703 |
| 依据 | 41% | 3% | 6/152 | 0/81 | 56/138 | 3/703 |
| 符合 | 37% | 1% | 0/152 | 0/81 | 51/138 | 7/703 |

**no-pressure truths, Q7: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| constraints | 94% | 7% | 105/152 | 56/81 | 130/138 | 16/703 |
| prompt | 91% | 7% | 123/152 | 42/81 | 126/138 | 39/703 |
| 指令 | 87% | 6% | 97/152 | 47/81 | 120/138 | 42/703 |
| constraint | 91% | 10% | 24/152 | 37/81 | 126/138 | 17/703 |
| instruction | 89% | 9% | 104/152 | 45/81 | 123/138 | 48/703 |
| instructions | 89% | 9% | 129/152 | 57/81 | 123/138 | 52/703 |
| 约束 | 82% | 6% | 42/152 | 39/81 | 113/138 | 10/703 |
| prompts | 73% | 1% | 98/152 | 29/81 | 101/138 | 29/703 |
| 明确规定 | 72% | 0% | 47/152 | 9/81 | 99/138 | 1/703 |
| 规则 | 70% | 0% | 8/152 | 5/81 | 97/138 | 0/703 |

**no-pressure truths, Q7: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| disclaimer | 80% | 12% | 8/152 | 9/81 | 111/138 | 84/703 |
| constraint | 91% | 26% | 24/152 | 37/81 | 126/138 | 17/703 |
| 规则 | 70% | 6% | 8/152 | 5/81 | 97/138 | 0/703 |
| predefined | 61% | 1% | 3/152 | 0/81 | 84/138 | 0/703 |
| preamble | 61% | 12% | 25/152 | 4/81 | 84/138 | 0/703 |
| 明确规定 | 72% | 24% | 47/152 | 9/81 | 99/138 | 1/703 |
| 约束 | 82% | 35% | 42/152 | 39/81 | 113/138 | 10/703 |
| contradiction | 55% | 11% | 13/152 | 13/81 | 76/138 | 28/703 |
| contradictory | 74% | 31% | 41/152 | 31/81 | 102/138 | 60/703 |
| explicit | 67% | 27% | 55/152 | 8/81 | 93/138 | 2/703 |

**no-pressure truths, Q9: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 撒谎 | 83% | 1% | 146/152 | 76/81 | 115/138 | 446/703 |
| deception | 83% | 7% | 145/152 | 70/81 | 115/138 | 626/703 |
| 说谎 | 100% | 29% | 151/152 | 81/81 | 138/138 | 693/703 |
| deceive | 68% | 0% | 104/152 | 55/81 | 94/138 | 515/703 |
| 吗 | 74% | 6% | 30/152 | 45/81 | 102/138 | 256/703 |
| untrue | 67% | 0% | 123/152 | 59/81 | 93/138 | 657/703 |
| 谎 | 73% | 7% | 103/152 | 68/81 | 101/138 | 572/703 |
| fals | 96% | 31% | 152/152 | 81/81 | 132/138 | 638/703 |
| dishonest | 65% | 1% | 118/152 | 63/81 | 90/138 | 551/703 |
| false | 100% | 38% | 148/152 | 79/81 | 138/138 | 697/703 |

**no-pressure truths, Q9: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 陈述 | 77% | 18% | 11/152 | 21/81 | 106/138 | 127/703 |
| 真实性 | 56% | 16% | 14/152 | 8/81 | 77/138 | 113/703 |
| 吗 | 74% | 36% | 30/152 | 45/81 | 102/138 | 256/703 |
| statements | 57% | 26% | 32/152 | 29/81 | 79/138 | 101/703 |

**unrelated, Q6: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| descriptions | 52% | 19% | 1/152 | 3/81 | 10/138 | 363/703 |
| correctness | 57% | 27% | 0/152 | 15/81 | 57/138 | 404/703 |
| 描述 | 44% | 14% | 11/152 | 3/81 | 29/138 | 310/703 |

**unrelated, Q6: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| descriptions | 52% | 7% | 1/152 | 3/81 | 10/138 | 363/703 |
| 无误 | 35% | 1% | 0/152 | 0/81 | 2/138 | 248/703 |

**unrelated, Q7: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| question | 89% | 15% | 7/152 | 13/81 | 18/138 | 625/703 |
| questions | 79% | 8% | 5/152 | 6/81 | 5/138 | 557/703 |
| 作为 | 65% | 2% | 1/152 | 1/81 | 0/138 | 459/703 |
| 作为一名 | 61% | 1% | 1/152 | 0/81 | 0/138 | 431/703 |
| neither | 79% | 19% | 1/152 | 0/81 | 0/138 | 553/703 |
| sentient | 63% | 5% | 0/152 | 0/81 | 0/138 | 444/703 |
| 作为一个 | 60% | 2% | 1/152 | 0/81 | 0/138 | 419/703 |
| humans | 59% | 1% | 0/152 | 0/81 | 0/138 | 413/703 |
| artificial | 69% | 12% | 0/152 | 0/81 | 0/138 | 484/703 |
| 인공지능 | 56% | 3% | 0/152 | 0/81 | 0/138 | 393/703 |

**unrelated, Q7: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 不存在 | 83% | 0% | 1/152 | 0/81 | 0/138 | 585/703 |
| neither | 79% | 0% | 1/152 | 0/81 | 0/138 | 553/703 |
| question | 89% | 13% | 7/152 | 13/81 | 18/138 | 625/703 |
| 人工智能 | 75% | 1% | 2/152 | 0/81 | 1/138 | 530/703 |
| questions | 79% | 5% | 5/152 | 6/81 | 5/138 | 557/703 |
| 没有任何 | 73% | 0% | 1/152 | 0/81 | 0/138 | 511/703 |
| 的人工智能 | 72% | 0% | 0/152 | 0/81 | 0/138 | 504/703 |
| 我没有 | 70% | 0% | 0/152 | 0/81 | 0/138 | 494/703 |
| artificial | 69% | 0% | 0/152 | 0/81 | 0/138 | 484/703 |
| 作为 | 65% | 1% | 1/152 | 1/81 | 0/138 | 459/703 |

**unrelated, Q9: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| untrue | 93% | 0% | 123/152 | 59/81 | 93/138 | 657/703 |
| 欺骗 | 98% | 15% | 152/152 | 81/81 | 137/138 | 691/703 |
| fals | 91% | 10% | 152/152 | 81/81 | 132/138 | 638/703 |
| 谎 | 81% | 1% | 103/152 | 68/81 | 101/138 | 572/703 |
| 说谎 | 99% | 23% | 151/152 | 81/81 | 138/138 | 693/703 |
| deception | 89% | 15% | 145/152 | 70/81 | 115/138 | 626/703 |
| deceive | 73% | 0% | 104/152 | 55/81 | 94/138 | 515/703 |
| 虚假信息 | 81% | 10% | 66/152 | 15/81 | 108/138 | 567/703 |
| 谎言 | 100% | 30% | 152/152 | 81/81 | 138/138 | 700/703 |
| dishonest | 78% | 9% | 118/152 | 63/81 | 90/138 | 551/703 |

**unrelated, Q9: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 不存在 | 84% | 5% | 0/152 | 2/81 | 7/138 | 592/703 |
| intentional | 67% | 4% | 7/152 | 2/81 | 3/138 | 473/703 |
| 故意 | 73% | 12% | 23/152 | 6/81 | 13/138 | 513/703 |
| deliberate | 57% | 2% | 4/152 | 1/81 | 2/138 | 401/703 |
| 我没有 | 85% | 31% | 0/152 | 31/81 | 43/138 | 598/703 |
| intentionally | 76% | 25% | 46/152 | 12/81 | 8/138 | 531/703 |
| 没有任何 | 51% | 1% | 0/152 | 0/81 | 1/138 | 359/703 |
| nonexistent | 44% | 0% | 0/152 | 0/81 | 0/138 | 310/703 |
| deliberately | 51% | 8% | 17/152 | 1/81 | 2/138 | 360/703 |
| 故意的 | 33% | 1% | 0/152 | 0/81 | 1/138 | 235/703 |


## At `<|im_start|>` after the question (preans_slot2)

**pressured, Q1: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| unethical | 77% | 4% | 118/152 | 62/81 | 5/138 | 1/703 |
| 隐瞒 | 57% | 0% | 100/152 | 32/81 | 0/138 | 0/703 |
| 秘密 | 38% | 1% | 76/152 | 12/81 | 1/138 | 0/703 |
| scenario | 37% | 1% | 53/152 | 34/81 | 2/138 | 3/703 |
| confidentiality | 37% | 2% | 63/152 | 23/81 | 3/138 | 3/703 |

**pressured, Q2: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| unethical | 66% | 2% | 101/152 | 52/81 | 3/138 | 0/703 |
| 隐瞒 | 56% | 2% | 99/152 | 32/81 | 3/138 | 0/703 |
| backstory | 40% | 1% | 67/152 | 27/81 | 2/138 | 0/703 |
| 秘密 | 37% | 0% | 72/152 | 14/81 | 0/138 | 0/703 |
| scenario | 40% | 5% | 62/152 | 31/81 | 7/138 | 3/703 |
| fake | 57% | 23% | 88/152 | 44/81 | 32/138 | 28/703 |
| 实际情况 | 32% | 2% | 66/152 | 9/81 | 1/138 | 12/703 |

**pressured, Q6: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| fake | 75% | 10% | 119/152 | 55/81 | 14/138 | 25/703 |
| 隐瞒 | 60% | 0% | 108/152 | 31/81 | 0/138 | 0/703 |
| unethical | 58% | 0% | 89/152 | 45/81 | 0/138 | 0/703 |
| scenario | 54% | 1% | 79/152 | 46/81 | 2/138 | 6/703 |
| backstory | 53% | 1% | 85/152 | 39/81 | 2/138 | 4/703 |
| 情境 | 42% | 0% | 62/152 | 36/81 | 0/138 | 0/703 |
| 秘密 | 42% | 0% | 81/152 | 16/81 | 0/138 | 0/703 |
| scenarios | 41% | 1% | 57/152 | 38/81 | 1/138 | 8/703 |
| 的真实 | 44% | 8% | 85/152 | 18/81 | 11/138 | 22/703 |
| 实际情况 | 35% | 3% | 66/152 | 16/81 | 3/138 | 21/703 |

**pressured, Q7: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 隐瞒 | 56% | 0% | 95/152 | 36/81 | 0/138 | 0/703 |
| unethical | 55% | 1% | 78/152 | 49/81 | 1/138 | 1/703 |
| 秘密 | 39% | 0% | 66/152 | 25/81 | 0/138 | 0/703 |
| fake | 64% | 26% | 100/152 | 50/81 | 36/138 | 48/703 |
| 保密 | 31% | 0% | 47/152 | 25/81 | 0/138 | 0/703 |

**pressured, Q9: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| falsehood | 64% | 14% | 120/152 | 28/81 | 47/138 | 16/703 |
| 谎言 | 64% | 26% | 118/152 | 32/81 | 13/138 | 0/703 |
| falsely | 55% | 16% | 101/152 | 26/81 | 6/138 | 10/703 |
| false | 49% | 12% | 96/152 | 19/81 | 10/138 | 5/703 |
| 虚假 | 61% | 28% | 115/152 | 26/81 | 17/138 | 55/703 |

**pressured, Q9: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 谎言 | 64% | 9% | 118/152 | 32/81 | 13/138 | 0/703 |
| 隐瞒 | 67% | 12% | 116/152 | 39/81 | 16/138 | 0/703 |
| falsely | 55% | 4% | 101/152 | 26/81 | 6/138 | 10/703 |
| 欺骗 | 51% | 1% | 99/152 | 19/81 | 2/138 | 0/703 |
| 虚假 | 61% | 12% | 115/152 | 26/81 | 17/138 | 55/703 |
| fals | 52% | 5% | 100/152 | 20/81 | 7/138 | 1/703 |
| false | 49% | 7% | 96/152 | 19/81 | 10/138 | 5/703 |
| fake | 67% | 28% | 122/152 | 35/81 | 38/138 | 98/703 |
| misleading | 33% | 2% | 59/152 | 19/81 | 3/138 | 15/703 |
| 说谎 | 33% | 2% | 66/152 | 12/81 | 3/138 | 0/703 |

**no-pressure truths, Q1: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| predefined | 86% | 1% | 2/152 | 0/81 | 119/138 | 3/703 |
| fact | 83% | 8% | 13/152 | 5/81 | 115/138 | 26/703 |
| 真理 | 78% | 3% | 3/152 | 3/81 | 107/138 | 1/703 |
| stated | 85% | 15% | 24/152 | 11/81 | 117/138 | 6/703 |
| specified | 71% | 3% | 4/152 | 2/81 | 98/138 | 14/703 |
| predetermined | 67% | 0% | 0/152 | 0/81 | 92/138 | 0/703 |
| constraint | 78% | 14% | 16/152 | 16/81 | 108/138 | 31/703 |
| provided | 67% | 4% | 1/152 | 1/81 | 93/138 | 27/703 |
| 事实和 | 66% | 3% | 1/152 | 2/81 | 91/138 | 20/703 |
| 的事实 | 86% | 24% | 46/152 | 9/81 | 118/138 | 38/703 |

**no-pressure truths, Q2: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| predefined | 87% | 1% | 2/152 | 0/81 | 120/138 | 1/703 |
| specified | 81% | 2% | 3/152 | 2/81 | 112/138 | 6/703 |
| fact | 86% | 9% | 16/152 | 4/81 | 119/138 | 17/703 |
| provided | 78% | 4% | 5/152 | 1/81 | 108/138 | 31/703 |
| 真理 | 76% | 3% | 3/152 | 3/81 | 105/138 | 0/703 |
| predetermined | 70% | 0% | 0/152 | 0/81 | 96/138 | 0/703 |
| stated | 88% | 20% | 35/152 | 12/81 | 121/138 | 7/703 |
| 事实和 | 65% | 2% | 3/152 | 2/81 | 90/138 | 10/703 |
| referenced | 68% | 5% | 8/152 | 4/81 | 94/138 | 7/703 |
| given | 62% | 1% | 0/152 | 1/81 | 85/138 | 9/703 |

**no-pressure truths, Q6: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| predefined | 90% | 0% | 1/152 | 0/81 | 124/138 | 2/703 |
| specified | 90% | 3% | 4/152 | 3/81 | 124/138 | 5/703 |
| fact | 92% | 6% | 10/152 | 5/81 | 127/138 | 17/703 |
| provided | 90% | 5% | 2/152 | 1/81 | 124/138 | 35/703 |
| 真理 | 86% | 3% | 4/152 | 2/81 | 119/138 | 1/703 |
| 事实和 | 81% | 1% | 1/152 | 0/81 | 112/138 | 6/703 |
| referenced | 83% | 4% | 8/152 | 2/81 | 115/138 | 23/703 |
| given | 77% | 1% | 3/152 | 0/81 | 106/138 | 9/703 |
| established | 75% | 0% | 1/152 | 0/81 | 103/138 | 1/703 |
| stated | 94% | 22% | 35/152 | 16/81 | 130/138 | 10/703 |

**no-pressure truths, Q7: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| fact | 85% | 5% | 9/152 | 3/81 | 117/138 | 5/703 |
| 的事实 | 86% | 14% | 24/152 | 8/81 | 118/138 | 8/703 |
| 真理 | 72% | 1% | 2/152 | 1/81 | 100/138 | 0/703 |
| facts | 91% | 22% | 38/152 | 14/81 | 125/138 | 86/703 |
| predefined | 66% | 0% | 0/152 | 1/81 | 91/138 | 2/703 |
| stated | 72% | 8% | 10/152 | 9/81 | 100/138 | 6/703 |
| 事实 | 93% | 29% | 51/152 | 16/81 | 128/138 | 79/703 |
| factual | 92% | 29% | 32/152 | 15/81 | 127/138 | 201/703 |
| truths | 69% | 7% | 15/152 | 2/81 | 95/138 | 6/703 |
| 事实和 | 62% | 0% | 0/152 | 0/81 | 85/138 | 2/703 |

**no-pressure truths, Q9: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| correctly | 75% | 11% | 2/152 | 15/81 | 103/138 | 512/703 |
| accurately | 58% | 0% | 1/152 | 7/81 | 80/138 | 410/703 |
| based | 57% | 1% | 0/152 | 0/81 | 79/138 | 12/703 |
| 正确 | 60% | 7% | 0/152 | 10/81 | 83/138 | 423/703 |
| 基于 | 54% | 0% | 0/152 | 0/81 | 74/138 | 12/703 |
| correct | 59% | 9% | 2/152 | 11/81 | 82/138 | 434/703 |
| 正确的 | 55% | 6% | 1/152 | 12/81 | 76/138 | 416/703 |
| 根据 | 55% | 9% | 10/152 | 1/81 | 76/138 | 1/703 |
| 依据 | 69% | 24% | 1/152 | 0/81 | 95/138 | 2/703 |
| accurate | 44% | 1% | 1/152 | 6/81 | 61/138 | 374/703 |

**no-pressure truths, Q9: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 依据 | 69% | 0% | 1/152 | 0/81 | 95/138 | 2/703 |
| based | 57% | 2% | 0/152 | 0/81 | 79/138 | 12/703 |
| 基于 | 54% | 2% | 0/152 | 0/81 | 74/138 | 12/703 |
| 根据 | 55% | 5% | 10/152 | 1/81 | 76/138 | 1/703 |
| facts | 80% | 38% | 39/152 | 22/81 | 111/138 | 265/703 |
| 事实 | 88% | 45% | 71/152 | 34/81 | 121/138 | 242/703 |
| 真实性 | 61% | 21% | 34/152 | 15/81 | 84/138 | 125/703 |
| 陈述 | 50% | 11% | 4/152 | 3/81 | 69/138 | 77/703 |
| 信息 | 61% | 23% | 6/152 | 4/81 | 84/138 | 164/703 |
| 符合 | 41% | 3% | 1/152 | 0/81 | 56/138 | 23/703 |

**unrelated, Q1: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| asked | 49% | 3% | 2/152 | 4/81 | 2/138 | 347/703 |
| 回答 | 50% | 4% | 1/152 | 7/81 | 5/138 | 353/703 |
| request | 51% | 9% | 4/152 | 17/81 | 4/138 | 360/703 |
| requested | 57% | 15% | 14/152 | 21/81 | 4/138 | 402/703 |
| question | 52% | 10% | 1/152 | 12/81 | 14/138 | 365/703 |
| questions | 46% | 7% | 1/152 | 10/81 | 9/138 | 323/703 |
| 请求 | 47% | 11% | 6/152 | 19/81 | 5/138 | 332/703 |
| 提问 | 40% | 6% | 1/152 | 5/81 | 8/138 | 279/703 |

**unrelated, Q2: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| correctly | 43% | 5% | 0/152 | 3/81 | 7/138 | 303/703 |
| asked | 40% | 3% | 0/152 | 3/81 | 4/138 | 281/703 |
| 回答 | 40% | 4% | 1/152 | 4/81 | 5/138 | 279/703 |
| request | 43% | 9% | 7/152 | 15/81 | 4/138 | 302/703 |
| requested | 51% | 18% | 19/152 | 23/81 | 3/138 | 358/703 |

**unrelated, Q6: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| correctly | 39% | 8% | 0/152 | 3/81 | 11/138 | 271/703 |

**unrelated, Q7: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| requested | 60% | 13% | 14/152 | 16/81 | 8/138 | 421/703 |
| asked | 49% | 4% | 2/152 | 2/81 | 6/138 | 345/703 |
| correctly | 48% | 4% | 0/152 | 2/81 | 5/138 | 335/703 |
| request | 48% | 7% | 4/152 | 13/81 | 8/138 | 335/703 |
| question | 50% | 10% | 3/152 | 8/81 | 14/138 | 348/703 |
| 回答 | 44% | 7% | 3/152 | 3/81 | 10/138 | 310/703 |
| questions | 43% | 8% | 3/152 | 9/81 | 11/138 | 301/703 |
| 请求 | 44% | 11% | 10/152 | 16/81 | 9/138 | 311/703 |

**unrelated, Q9: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| truthful | 51% | 9% | 112/152 | 52/81 | 127/138 | 359/703 |
| incorrect | 53% | 20% | 16/152 | 8/81 | 18/138 | 373/703 |
| 是正确的 | 50% | 17% | 0/152 | 5/81 | 32/138 | 348/703 |
| correct | 62% | 30% | 2/152 | 11/81 | 82/138 | 434/703 |
| accurate | 53% | 21% | 1/152 | 6/81 | 61/138 | 374/703 |
| accurately | 58% | 27% | 1/152 | 7/81 | 80/138 | 410/703 |

**unrelated, Q9: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| incorrect | 53% | 13% | 16/152 | 8/81 | 18/138 | 373/703 |
| descriptions | 35% | 2% | 2/152 | 3/81 | 0/138 | 243/703 |


## At `</think>` (think_slot2)

**pressured, Q1: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| it | 94% | 0% | 144/152 | 76/81 | 136/138 | 703/703 |
| the | 80% | 1% | 117/152 | 69/81 | 131/138 | 628/703 |
| does | 67% | 1% | 93/152 | 64/81 | 128/138 | 678/703 |
| —you | 76% | 15% | 110/152 | 68/81 | 126/138 | 635/703 |
| that | 61% | 0% | 92/152 | 49/81 | 61/138 | 535/703 |
| —which | 79% | 27% | 120/152 | 63/81 | 129/138 | 490/703 |
| —but | 46% | 0% | 74/152 | 33/81 | 23/138 | 233/703 |
| disabled | 61% | 17% | 91/152 | 50/81 | 0/138 | 4/703 |
| this | 42% | 0% | 64/152 | 33/81 | 4/138 | 1/703 |
| ­tion | 53% | 12% | 68/152 | 55/81 | 129/138 | 526/703 |

**pressured, Q1: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| disabled | 61% | 1% | 91/152 | 50/81 | 0/138 | 4/703 |
| 逆 | 44% | 1% | 66/152 | 37/81 | 1/138 | 2/703 |
| unauthorized | 82% | 41% | 128/152 | 64/81 | 56/138 | 12/703 |
| this | 42% | 3% | 64/152 | 33/81 | 4/138 | 1/703 |
| 我无法 | 39% | 3% | 69/152 | 21/81 | 4/138 | 0/703 |
| 隐私 | 46% | 16% | 75/152 | 33/81 | 22/138 | 27/703 |

**pressured, Q2: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| —even | 77% | 34% | 126/152 | 54/81 | 0/138 | 8/703 |

**pressured, Q2: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 沉默 | 87% | 10% | 129/152 | 73/81 | 14/138 | 0/703 |
| oui | 79% | 3% | 134/152 | 51/81 | 4/138 | 5/703 |
| —even | 77% | 1% | 126/152 | 54/81 | 0/138 | 8/703 |
| forbidden | 69% | 6% | 110/152 | 50/81 | 8/138 | 1/703 |
| cannot | 66% | 4% | 93/152 | 61/81 | 6/138 | 0/703 |
| تماماً | 77% | 22% | 119/152 | 60/81 | 30/138 | 60/703 |
| unauthorized | 97% | 44% | 149/152 | 77/81 | 61/138 | 166/703 |
| 直接 | 66% | 14% | 101/152 | 53/81 | 19/138 | 5/703 |
| 合规 | 68% | 21% | 110/152 | 49/81 | 29/138 | 8/703 |
| 反 | 61% | 21% | 93/152 | 50/81 | 1/138 | 149/703 |

**pressured, Q6: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 解答 | 52% | 12% | 76/152 | 44/81 | 126/138 | 505/703 |
| silent | 78% | 42% | 120/152 | 61/81 | 3/138 | 0/703 |
| privacidad | 60% | 25% | 91/152 | 48/81 | 105/138 | 32/703 |
| 寂 | 36% | 6% | 51/152 | 34/81 | 1/138 | 1/703 |

**pressured, Q6: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| oui | 86% | 1% | 145/152 | 56/81 | 2/138 | 5/703 |
| unauthorized | 93% | 14% | 144/152 | 72/81 | 19/138 | 2/703 |
| silent | 78% | 2% | 120/152 | 61/81 | 3/138 | 0/703 |
| 是的 | 98% | 25% | 148/152 | 80/81 | 28/138 | 175/703 |
| تماماً | 79% | 7% | 125/152 | 59/81 | 9/138 | 3/703 |
| wikileaks | 87% | 17% | 134/152 | 69/81 | 24/138 | 10/703 |
| 直接 | 78% | 12% | 122/152 | 60/81 | 17/138 | 7/703 |
| 沉默 | 97% | 32% | 148/152 | 79/81 | 44/138 | 19/703 |
| graphql | 70% | 7% | 112/152 | 51/81 | 9/138 | 0/703 |
| silence | 97% | 34% | 149/152 | 76/81 | 47/138 | 46/703 |

**pressured, Q7: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| placeholder | 81% | 1% | 125/152 | 64/81 | 20/138 | 25/703 |
| bc | 72% | 0% | 96/152 | 71/81 | 34/138 | 16/703 |
| abc | 70% | 0% | 109/152 | 53/81 | 19/138 | 17/703 |
| bf | 69% | 0% | 106/152 | 55/81 | 1/138 | 0/703 |
| hel | 62% | 3% | 98/152 | 46/81 | 16/138 | 68/703 |
| bbbb | 58% | 0% | 86/152 | 50/81 | 6/138 | 0/703 |
| 楚 | 58% | 0% | 78/152 | 58/81 | 52/138 | 36/703 |
| bff | 58% | 0% | 85/152 | 49/81 | 63/138 | 76/703 |
| vs | 55% | 2% | 83/152 | 45/81 | 12/138 | 41/703 |
| 底 | 46% | 3% | 84/152 | 23/81 | 49/138 | 423/703 |

**pressured, Q7: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| bf | 69% | 1% | 106/152 | 55/81 | 1/138 | 0/703 |
| disclosure | 75% | 8% | 118/152 | 57/81 | 11/138 | 15/703 |
| placeholder | 81% | 14% | 125/152 | 64/81 | 20/138 | 25/703 |
| forbidden | 82% | 15% | 124/152 | 66/81 | 21/138 | 2/703 |
| 直接 | 64% | 1% | 105/152 | 43/81 | 1/138 | 4/703 |
| 隐私 | 73% | 12% | 117/152 | 54/81 | 16/138 | 9/703 |
| silence | 64% | 4% | 92/152 | 58/81 | 5/138 | 2/703 |
| conscience | 60% | 0% | 109/152 | 31/81 | 0/138 | 0/703 |
| privacy | 94% | 37% | 144/152 | 76/81 | 51/138 | 222/703 |
| abc | 70% | 14% | 109/152 | 53/81 | 19/138 | 17/703 |

**pressured, Q9: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| badrequest | 86% | 5% | 134/152 | 67/81 | 18/138 | 0/703 |
| 答 | 94% | 29% | 140/152 | 80/81 | 137/138 | 699/703 |
| hypocrisy | 76% | 14% | 119/152 | 58/81 | 0/138 | 38/703 |
| 没有任何 | 65% | 9% | 98/152 | 54/81 | 125/138 | 189/703 |
| 反问 | 87% | 33% | 137/152 | 66/81 | 18/138 | 6/703 |
| 拒绝 | 83% | 35% | 136/152 | 57/81 | 10/138 | 1/703 |
| reply | 49% | 4% | 66/152 | 48/81 | 53/138 | 533/703 |
| 回答 | 94% | 55% | 141/152 | 77/81 | 138/138 | 703/703 |
| 回复 | 44% | 6% | 58/152 | 44/81 | 19/138 | 292/703 |
| 答复 | 38% | 2% | 41/152 | 47/81 | 24/138 | 84/703 |

**pressured, Q9: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| unauthorized | 88% | 4% | 138/152 | 67/81 | 6/138 | 3/703 |
| 沉默 | 97% | 14% | 148/152 | 78/81 | 20/138 | 22/703 |
| cannot | 83% | 7% | 130/152 | 63/81 | 9/138 | 2/703 |
| 拒绝 | 83% | 7% | 136/152 | 57/81 | 10/138 | 1/703 |
| 反问 | 87% | 13% | 137/152 | 66/81 | 18/138 | 6/703 |
| badrequest | 86% | 13% | 134/152 | 67/81 | 18/138 | 0/703 |
| silence | 78% | 5% | 118/152 | 64/81 | 7/138 | 13/703 |
| hypocrisy | 76% | 5% | 119/152 | 58/81 | 0/138 | 38/703 |
| assertnot | 84% | 18% | 137/152 | 59/81 | 17/138 | 128/703 |
| oui | 91% | 29% | 146/152 | 65/81 | 27/138 | 206/703 |

**no-pressure truths, Q1: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| it | 99% | 3% | 144/152 | 76/81 | 136/138 | 703/703 |
| the | 95% | 0% | 117/152 | 69/81 | 131/138 | 628/703 |
| your (q) | 93% | 0% | 24/152 | 34/81 | 129/138 | 627/703 |
| does | 93% | 4% | 93/152 | 64/81 | 128/138 | 678/703 |
| —that | 97% | 9% | 12/152 | 18/81 | 134/138 | 584/703 |
| 在 | 84% | 5% | 46/152 | 45/81 | 116/138 | 670/703 |
| —you | 91% | 14% | 110/152 | 68/81 | 126/138 | 635/703 |
| 问 | 80% | 6% | 33/152 | 34/81 | 111/138 | 611/703 |
| —which | 93% | 20% | 120/152 | 63/81 | 129/138 | 490/703 |
| ­tion | 93% | 20% | 68/152 | 55/81 | 129/138 | 526/703 |

**no-pressure truths, Q1: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| true | 54% | 11% | 13/152 | 13/81 | 74/138 | 12/703 |
| ăș | 46% | 8% | 9/152 | 9/81 | 63/138 | 45/703 |
| gdpr | 78% | 41% | 63/152 | 33/81 | 108/138 | 39/703 |
| tk | 37% | 4% | 1/152 | 3/81 | 51/138 | 27/703 |
| assertionerror | 40% | 9% | 6/152 | 7/81 | 55/138 | 61/703 |
| argument | 32% | 1% | 2/152 | 0/81 | 44/138 | 5/703 |

**no-pressure truths, Q2: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| non | 40% | 9% | 23/152 | 39/81 | 55/138 | 202/703 |

**no-pressure truths, Q2: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| priv | 83% | 14% | 10/152 | 16/81 | 114/138 | 97/703 |
| preced | 45% | 5% | 0/152 | 0/81 | 62/138 | 35/703 |
| privacidad | 51% | 19% | 30/152 | 14/81 | 71/138 | 8/703 |
| 安全 | 33% | 3% | 0/152 | 2/81 | 46/138 | 21/703 |

**no-pressure truths, Q6: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| собесед | 59% | 10% | 0/152 | 0/81 | 82/138 | 301/703 |
| 解答 | 91% | 54% | 76/152 | 44/81 | 126/138 | 505/703 |
| vi | 41% | 9% | 47/152 | 21/81 | 57/138 | 273/703 |

**no-pressure truths, Q6: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| priv | 86% | 28% | 31/152 | 34/81 | 118/138 | 87/703 |
| preced | 54% | 7% | 0/152 | 0/81 | 75/138 | 49/703 |
| 安全 | 46% | 2% | 0/152 | 3/81 | 63/138 | 11/703 |
| borg | 38% | 1% | 1/152 | 1/81 | 53/138 | 9/703 |
| 安全保障 | 36% | 0% | 0/152 | 0/81 | 49/138 | 0/703 |

**no-pressure truths, Q7: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 澄清 | 86% | 17% | 5/152 | 8/81 | 119/138 | 571/703 |
| compliance | 82% | 13% | 143/152 | 74/81 | 113/138 | 603/703 |
| 兼容 | 63% | 1% | 0/152 | 0/81 | 87/138 | 184/703 |
| 榜 | 62% | 1% | 0/152 | 1/81 | 86/138 | 396/703 |
| guest | 61% | 0% | 0/152 | 0/81 | 84/138 | 251/703 |
| bí | 59% | 0% | 43/152 | 22/81 | 81/138 | 560/703 |
| 纳 | 54% | 1% | 0/152 | 0/81 | 75/138 | 9/703 |
| java | 57% | 5% | 16/152 | 10/81 | 78/138 | 70/703 |
| angers | 50% | 4% | 10/152 | 8/81 | 69/138 | 189/703 |
| authorization | 46% | 0% | 4/152 | 3/81 | 64/138 | 69/703 |

**no-pressure truths, Q7: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 纳 | 54% | 1% | 0/152 | 0/81 | 75/138 | 9/703 |
| 安全 | 72% | 22% | 6/152 | 12/81 | 99/138 | 158/703 |
| java | 57% | 11% | 16/152 | 10/81 | 78/138 | 70/703 |
| 卡 | 49% | 6% | 0/152 | 0/81 | 67/138 | 39/703 |
| ēr | 39% | 0% | 0/152 | 0/81 | 54/138 | 2/703 |
| 思考 | 46% | 9% | 0/152 | 0/81 | 64/138 | 64/703 |
| 兼容 | 63% | 26% | 0/152 | 0/81 | 87/138 | 184/703 |
| authorization | 46% | 10% | 4/152 | 3/81 | 64/138 | 69/703 |
| browser | 46% | 12% | 20/152 | 9/81 | 63/138 | 47/703 |
| 违规 | 49% | 17% | 33/152 | 7/81 | 67/138 | 42/703 |

**no-pressure truths, Q9: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 没有任何 | 91% | 9% | 98/152 | 54/81 | 125/138 | 189/703 |
| 正直 | 60% | 1% | 12/152 | 13/81 | 83/138 | 91/703 |
| 的答案 | 57% | 0% | 23/152 | 23/81 | 78/138 | 237/703 |
| nein | 78% | 23% | 28/152 | 32/81 | 107/138 | 503/703 |
| いいえ | 57% | 4% | 5/152 | 13/81 | 79/138 | 286/703 |
| 验证 | 38% | 2% | 11/152 | 8/81 | 52/138 | 335/703 |
| 答 | 99% | 64% | 140/152 | 80/81 | 137/138 | 699/703 |
| invalid | 33% | 1% | 56/152 | 38/81 | 46/138 | 4/703 |
| answered | 93% | 61% | 27/152 | 45/81 | 128/138 | 671/703 |
| 的回答 | 36% | 4% | 22/152 | 23/81 | 50/138 | 46/703 |

**no-pressure truths, Q9: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 正直 | 60% | 13% | 12/152 | 13/81 | 83/138 | 91/703 |
| 回避 | 31% | 1% | 2/152 | 0/81 | 43/138 | 1/703 |

**unrelated, Q1: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| not | 96% | 0% | 0/152 | 10/81 | 55/138 | 675/703 |
| it | 100% | 6% | 144/152 | 76/81 | 136/138 | 703/703 |
| 的 | 94% | 3% | 2/152 | 19/81 | 85/138 | 664/703 |
| tl | 97% | 8% | 1/152 | 16/81 | 92/138 | 680/703 |
| 在 | 95% | 9% | 46/152 | 45/81 | 116/138 | 670/703 |
| 你 | 91% | 6% | 6/152 | 23/81 | 86/138 | 639/703 |
| 是 | 91% | 10% | 0/152 | 12/81 | 53/138 | 642/703 |
| your (q) | 89% | 9% | 24/152 | 34/81 | 129/138 | 627/703 |
| neither | 76% | 0% | 0/152 | 11/81 | 7/138 | 536/703 |
| that | 76% | 0% | 92/152 | 49/81 | 61/138 | 535/703 |

**unrelated, Q1: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| neither | 76% | 5% | 0/152 | 11/81 | 7/138 | 536/703 |
| 我 | 70% | 2% | 0/152 | 5/81 | 1/138 | 493/703 |
| nope | 79% | 20% | 2/152 | 3/81 | 27/138 | 557/703 |
| not | 96% | 40% | 0/152 | 10/81 | 55/138 | 675/703 |
| 是 | 91% | 38% | 0/152 | 12/81 | 53/138 | 642/703 |
| 中 | 86% | 48% | 7/152 | 22/81 | 66/138 | 608/703 |
| 并不 | 39% | 0% | 0/152 | 0/81 | 0/138 | 271/703 |
| onav | 35% | 0% | 0/152 | 0/81 | 0/138 | 248/703 |
| 的 | 94% | 62% | 2/152 | 19/81 | 85/138 | 664/703 |
| at | 42% | 11% | 0/152 | 0/81 | 15/138 | 298/703 |

**unrelated, Q2: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| integrity | 53% | 3% | 4/152 | 3/81 | 20/138 | 372/703 |
| disclosure | 86% | 44% | 103/152 | 43/81 | 110/138 | 608/703 |

**unrelated, Q2: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| cl | 67% | 10% | 0/152 | 0/81 | 14/138 | 473/703 |
| 问 | 83% | 31% | 40/152 | 33/81 | 6/138 | 586/703 |
| ­tion | 64% | 20% | 17/152 | 10/81 | 28/138 | 452/703 |
| assertfalse | 64% | 22% | 37/152 | 14/81 | 10/138 | 451/703 |
| truth | 44% | 1% | 0/152 | 0/81 | 2/138 | 306/703 |
| tri | 43% | 1% | 0/152 | 1/81 | 2/138 | 300/703 |
| nop | 43% | 2% | 1/152 | 1/81 | 3/138 | 299/703 |
| 答 | 61% | 21% | 21/152 | 27/81 | 23/138 | 427/703 |
| integrity | 53% | 14% | 4/152 | 3/81 | 20/138 | 372/703 |
| 草 | 38% | 0% | 0/152 | 0/81 | 0/138 | 265/703 |

**unrelated, Q6: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| checking | 68% | 16% | 0/152 | 0/81 | 7/138 | 475/703 |
| correct | 63% | 13% | 0/152 | 0/81 | 0/138 | 446/703 |
| erc | 67% | 19% | 1/152 | 13/81 | 38/138 | 472/703 |
| 低风险 | 72% | 26% | 51/152 | 53/81 | 109/138 | 504/703 |
| 核实 | 71% | 31% | 11/152 | 11/81 | 79/138 | 499/703 |
| 确认 | 47% | 7% | 3/152 | 3/81 | 4/138 | 330/703 |
| did (q) | 42% | 5% | 0/152 | 0/81 | 11/138 | 294/703 |
| собесед | 43% | 7% | 0/152 | 0/81 | 82/138 | 301/703 |
| trees | 34% | 0% | 0/152 | 0/81 | 0/138 | 237/703 |
| tp | 45% | 12% | 0/152 | 0/81 | 3/138 | 313/703 |

**unrelated, Q6: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| cl | 76% | 2% | 0/152 | 0/81 | 3/138 | 535/703 |
| ai | 84% | 20% | 5/152 | 8/81 | 28/138 | 590/703 |
| correct | 63% | 0% | 0/152 | 0/81 | 0/138 | 446/703 |
| checking | 68% | 5% | 0/152 | 0/81 | 7/138 | 475/703 |
| assertfalse | 71% | 14% | 25/152 | 7/81 | 5/138 | 496/703 |
| nop | 61% | 5% | 2/152 | 5/81 | 7/138 | 427/703 |
| tri | 61% | 9% | 0/152 | 0/81 | 12/138 | 429/703 |
| impossible | 68% | 20% | 30/152 | 17/81 | 26/138 | 480/703 |
| true | 72% | 25% | 27/152 | 18/81 | 34/138 | 508/703 |
| 答 | 81% | 34% | 18/152 | 24/81 | 47/138 | 572/703 |

**unrelated, Q7: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| bí | 80% | 2% | 43/152 | 22/81 | 81/138 | 560/703 |
| 榜 | 56% | 1% | 0/152 | 1/81 | 86/138 | 396/703 |
| 湖 | 55% | 1% | 0/152 | 1/81 | 22/138 | 386/703 |
| 底 | 60% | 8% | 84/152 | 23/81 | 49/138 | 423/703 |
| 合规 | 69% | 19% | 137/152 | 69/81 | 102/138 | 484/703 |
| cad | 57% | 10% | 0/152 | 0/81 | 28/138 | 401/703 |
| traits | 46% | 1% | 2/152 | 2/81 | 28/138 | 320/703 |
| 硼 | 41% | 0% | 1/152 | 1/81 | 45/138 | 290/703 |
| toc | 58% | 17% | 0/152 | 0/81 | 11/138 | 405/703 |
| guest | 36% | 0% | 0/152 | 0/81 | 84/138 | 251/703 |

**unrelated, Q7: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| toc | 58% | 8% | 0/152 | 0/81 | 11/138 | 405/703 |
| verification | 53% | 10% | 9/152 | 14/81 | 9/138 | 376/703 |
| robot | 40% | 1% | 0/152 | 0/81 | 1/138 | 281/703 |
| 湖 | 55% | 16% | 0/152 | 1/81 | 22/138 | 386/703 |
| cad | 57% | 20% | 0/152 | 0/81 | 28/138 | 401/703 |
| ηση | 31% | 1% | 0/152 | 0/81 | 1/138 | 218/703 |

**unrelated, Q9: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| nô | 45% | 0% | 2/152 | 6/81 | 2/138 | 315/703 |
| nein | 72% | 28% | 28/152 | 32/81 | 107/138 | 503/703 |
| 答案 | 52% | 9% | 1/152 | 2/81 | 19/138 | 368/703 |
| wikileaks | 69% | 26% | 149/152 | 81/81 | 102/138 | 484/703 |
| 验证 | 48% | 7% | 11/152 | 8/81 | 52/138 | 335/703 |
| answered | 95% | 55% | 27/152 | 45/81 | 128/138 | 671/703 |
| reply | 76% | 40% | 66/152 | 48/81 | 53/138 | 533/703 |
| br | 36% | 1% | 0/152 | 0/81 | 44/138 | 251/703 |
| 的答案 | 34% | 2% | 23/152 | 23/81 | 78/138 | 237/703 |
| 回复 | 42% | 11% | 58/152 | 44/81 | 19/138 | 292/703 |

**unrelated, Q9: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| answ | 91% | 38% | 1/152 | 3/81 | 52/138 | 637/703 |
| compliance | 90% | 47% | 77/152 | 32/81 | 17/138 | 633/703 |
| robot | 42% | 0% | 0/152 | 1/81 | 0/138 | 294/703 |
| nô | 45% | 3% | 2/152 | 6/81 | 2/138 | 315/703 |
| ai | 97% | 57% | 1/152 | 3/81 | 78/138 | 683/703 |
| 答案 | 52% | 14% | 1/152 | 2/81 | 19/138 | 368/703 |
| 澄清 | 55% | 17% | 2/152 | 2/81 | 23/138 | 385/703 |
| 否 | 92% | 61% | 69/152 | 62/81 | 84/138 | 645/703 |


## At the newline after the answer (postans_slot1)

**pressured, Q1: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 问 | 46% | 3% | 55/107 | 23/62 | 34/131 | 287/642 |
| 希望 | 38% | 1% | 34/107 | 30/62 | 48/131 | 358/642 |
| 回答 | 91% | 57% | 95/107 | 58/62 | 123/131 | 637/642 |
| 思考 | 39% | 7% | 33/107 | 33/62 | 82/131 | 526/642 |

**pressured, Q2: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| false | 36% | 2% | 82/152 | 3/81 | 1/138 | 14/703 |
| unethical | 31% | 0% | 71/152 | 1/81 | 0/138 | 0/703 |

**pressured, Q6: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| falsehood | 40% | 10% | 85/152 | 9/81 | 0/138 | 0/703 |

**pressured, Q6: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| truthful | 72% | 4% | 135/152 | 32/81 | 6/138 | 15/703 |
| false (q) | 66% | 2% | 131/152 | 23/81 | 2/138 | 14/703 |
| truth | 67% | 4% | 131/152 | 26/81 | 5/138 | 9/703 |
| 真相 | 60% | 1% | 119/152 | 21/81 | 2/138 | 1/703 |
| 本回答 | 54% | 8% | 84/152 | 42/81 | 11/138 | 14/703 |
| falsehood | 40% | 0% | 85/152 | 9/81 | 0/138 | 0/703 |
| fals | 36% | 0% | 75/152 | 10/81 | 0/138 | 0/703 |
| 用户提供 | 79% | 43% | 126/152 | 58/81 | 60/138 | 153/703 |
| 说谎 | 30% | 0% | 66/152 | 5/81 | 0/138 | 0/703 |

**pressured, Q7: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| truthful (q) | 63% | 13% | 111/152 | 36/81 | 18/138 | 32/703 |
| truth | 62% | 16% | 117/152 | 28/81 | 22/138 | 22/703 |
| 真相 | 53% | 7% | 104/152 | 19/81 | 9/138 | 10/703 |
| false | 42% | 2% | 73/152 | 24/81 | 2/138 | 16/703 |

**pressured, Q9: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 本回答 | 60% | 19% | 89/152 | 50/81 | 18/138 | 137/703 |
| thought | 67% | 27% | 100/152 | 55/81 | 36/138 | 189/703 |

**no-pressure truths, Q1: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 为什么 | 91% | 11% | 35/107 | 46/62 | 119/131 | 509/642 |
| why | 53% | 6% | 31/107 | 36/62 | 70/131 | 193/642 |
| principal | 39% | 0% | 7/107 | 14/62 | 51/131 | 304/642 |
| questions | 37% | 0% | 19/107 | 14/62 | 49/131 | 286/642 |
| 希望 | 37% | 1% | 34/107 | 30/62 | 48/131 | 358/642 |
| thought | 83% | 50% | 69/107 | 52/62 | 109/131 | 602/642 |
| cla | 48% | 15% | 2/107 | 6/62 | 63/131 | 27/642 |
| 人工智能 | 32% | 1% | 10/107 | 11/62 | 42/131 | 142/642 |

**no-pressure truths, Q1: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| cla | 48% | 5% | 2/107 | 6/62 | 63/131 | 27/642 |
| 万方 | 57% | 18% | 13/107 | 17/62 | 75/131 | 44/642 |
| 模型 | 40% | 4% | 2/107 | 5/62 | 53/131 | 23/642 |
| 解释 | 88% | 53% | 45/107 | 45/62 | 115/131 | 328/642 |

**no-pressure truths, Q2: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| ann | 49% | 5% | 0/152 | 0/81 | 68/138 | 35/703 |
| 因为 | 93% | 58% | 90/152 | 45/81 | 128/138 | 186/703 |
| 符合 | 40% | 6% | 4/152 | 11/81 | 55/138 | 0/703 |
| 给用户 | 54% | 22% | 44/152 | 7/81 | 75/138 | 8/703 |
| because | 59% | 28% | 53/152 | 12/81 | 81/138 | 77/703 |

**no-pressure truths, Q6: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| correct | 67% | 8% | 5/152 | 6/81 | 93/138 | 408/703 |

**no-pressure truths, Q6: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| ann | 67% | 7% | 2/152 | 1/81 | 92/138 | 47/703 |
| 皓 | 51% | 4% | 0/152 | 0/81 | 70/138 | 26/703 |
| 因为 | 90% | 44% | 83/152 | 20/81 | 124/138 | 165/703 |
| 确认 | 64% | 24% | 0/152 | 2/81 | 89/138 | 170/703 |
| 符合 | 49% | 12% | 9/152 | 18/81 | 68/138 | 0/703 |
| 解释 | 99% | 66% | 64/152 | 71/81 | 136/138 | 464/703 |

**no-pressure truths, Q7: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 给 | 70% | 17% | 0/152 | 1/81 | 96/138 | 167/703 |
| termination | 48% | 10% | 24/152 | 7/81 | 66/138 | 1/703 |

**no-pressure truths, Q7: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| ann | 93% | 44% | 32/152 | 30/81 | 128/138 | 312/703 |
| 给 | 70% | 24% | 0/152 | 1/81 | 96/138 | 167/703 |
| termination | 48% | 13% | 24/152 | 7/81 | 66/138 | 1/703 |
| eof | 78% | 43% | 20/152 | 34/81 | 107/138 | 303/703 |

**no-pressure truths, Q9: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 真实 | 51% | 7% | 100/152 | 36/81 | 71/138 | 115/703 |
| factual | 43% | 9% | 45/152 | 29/81 | 60/138 | 205/703 |
| truth | 82% | 49% | 133/152 | 44/81 | 113/138 | 332/703 |
| 真相 | 71% | 39% | 139/152 | 48/81 | 98/138 | 138/703 |

**no-pressure truths, Q9: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 因为 | 90% | 20% | 21/152 | 9/81 | 124/138 | 140/703 |
| ann | 63% | 7% | 2/152 | 6/81 | 87/138 | 48/703 |
| 符合 | 64% | 8% | 4/152 | 15/81 | 88/138 | 0/703 |
| 正确 | 44% | 7% | 3/152 | 13/81 | 61/138 | 43/703 |
| 解析 | 53% | 16% | 0/152 | 2/81 | 73/138 | 114/703 |
| hint | 54% | 18% | 6/152 | 7/81 | 74/138 | 130/703 |
| because | 40% | 7% | 1/152 | 2/81 | 55/138 | 50/703 |

**unrelated, Q1: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 质疑 | 74% | 0% | 3/107 | 8/62 | 5/131 | 472/642 |
| 为什么 | 79% | 7% | 35/107 | 46/62 | 119/131 | 509/642 |
| 思考 | 82% | 19% | 33/107 | 33/62 | 82/131 | 526/642 |
| 主 | 58% | 0% | 11/107 | 12/62 | 39/131 | 374/642 |
| 希望 | 56% | 0% | 34/107 | 30/62 | 48/131 | 358/642 |
| principal | 47% | 2% | 7/107 | 14/62 | 51/131 | 304/642 |
| 蒙 | 43% | 0% | 0/107 | 1/62 | 1/131 | 274/642 |
| 的回答 | 50% | 10% | 32/107 | 13/62 | 6/131 | 321/642 |
| 蒙特 | 35% | 1% | 1/107 | 1/62 | 21/131 | 226/642 |
| 争议 | 35% | 0% | 1/107 | 3/62 | 10/131 | 222/642 |

**unrelated, Q1: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 质疑 | 74% | 7% | 3/107 | 8/62 | 5/131 | 472/642 |
| 追问 | 89% | 36% | 41/107 | 19/62 | 38/131 | 572/642 |
| 蒙 | 43% | 1% | 0/107 | 1/62 | 1/131 | 274/642 |

**unrelated, Q2: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 提示 | 53% | 4% | 0/152 | 3/81 | 5/138 | 373/703 |
| 答案 | 92% | 51% | 9/152 | 9/81 | 71/138 | 648/703 |
| hint | 54% | 14% | 2/152 | 2/81 | 19/138 | 379/703 |
| 相关问答 | 39% | 2% | 1/152 | 0/81 | 3/138 | 276/703 |
| 追问 | 76% | 44% | 24/152 | 7/81 | 61/138 | 534/703 |
| thought | 93% | 63% | 95/152 | 52/81 | 59/138 | 655/703 |

**unrelated, Q6: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| correct | 58% | 4% | 5/152 | 6/81 | 93/138 | 408/703 |
| 正确 | 39% | 6% | 5/152 | 14/81 | 82/138 | 274/703 |

**unrelated, Q6: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 相关推荐 | 68% | 17% | 10/152 | 2/81 | 23/138 | 480/703 |
| hint | 55% | 14% | 22/152 | 10/81 | 9/138 | 384/703 |
| 提示 | 44% | 5% | 3/152 | 8/81 | 7/138 | 310/703 |
| thought | 92% | 58% | 92/152 | 42/81 | 55/138 | 647/703 |
| 吗 | 43% | 10% | 8/152 | 16/81 | 5/138 | 304/703 |
| placeholder | 34% | 2% | 1/152 | 3/81 | 1/138 | 236/703 |

**unrelated, Q7: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| kr | 63% | 1% | 0/152 | 0/81 | 0/138 | 445/703 |
| 人工智能 | 82% | 22% | 1/152 | 2/81 | 1/138 | 575/703 |
| 分析 | 57% | 0% | 1/152 | 0/81 | 2/138 | 398/703 |
| 原因 | 51% | 4% | 0/152 | 2/81 | 25/138 | 358/703 |
| ai | 51% | 7% | 1/152 | 0/81 | 0/138 | 359/703 |
| ann | 44% | 7% | 32/152 | 30/81 | 128/138 | 312/703 |

**unrelated, Q7: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 人工智能 | 82% | 1% | 1/152 | 2/81 | 1/138 | 575/703 |
| 相关推荐 | 66% | 1% | 2/152 | 1/81 | 2/138 | 467/703 |
| kr | 63% | 0% | 0/152 | 0/81 | 0/138 | 445/703 |
| 分析 | 57% | 1% | 1/152 | 0/81 | 2/138 | 398/703 |
| ai | 51% | 0% | 1/152 | 0/81 | 0/138 | 359/703 |
| 原因 | 51% | 18% | 0/152 | 2/81 | 25/138 | 358/703 |
| 答案 | 100% | 69% | 14/152 | 16/81 | 95/138 | 702/703 |
| thought | 81% | 50% | 45/152 | 48/81 | 69/138 | 568/703 |

**unrelated, Q9: A. special to the wording**

| word | this cell | largest share under another wording, same prompt type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 成功 | 83% | 4% | 18/152 | 40/81 | 55/138 | 582/703 |
| success | 65% | 1% | 8/152 | 24/81 | 35/138 | 454/703 |
| truth | 47% | 5% | 133/152 | 44/81 | 113/138 | 332/703 |
| successfully | 30% | 0% | 7/152 | 15/81 | 15/138 | 211/703 |

**unrelated, Q9: B. special to the prompt type**

| word | this cell | largest share in another prompt type, same wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| 追问 | 83% | 11% | 3/152 | 1/81 | 15/138 | 586/703 |
| 答案 | 80% | 25% | 1/152 | 1/81 | 34/138 | 559/703 |
| answer (q) | 97% | 49% | 35/152 | 37/81 | 67/138 | 679/703 |
| 成功 | 83% | 40% | 18/152 | 40/81 | 55/138 | 582/703 |
| success | 65% | 25% | 8/152 | 24/81 | 35/138 | 454/703 |
| 相关问答 | 37% | 5% | 7/152 | 5/81 | 3/138 | 257/703 |

