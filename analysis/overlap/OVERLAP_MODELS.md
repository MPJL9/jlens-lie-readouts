# Which families carry the lie signal, on each model, and how they overlap

Written by `scripts/findings_2026_10_02/overlap_models.py`. J-lens, post-response slot 1 (the newline after the response), build split only; every number is in-sample. Bands: Qwen 35-58, Gemma-12B 17-40, Gemma-27B 27-52, gpt-oss 10-20.

Families are the draft families as they are (kept entries, pooled by name at this position). Each model has its
own draft families, so a name such as `lie` has a different token list on each model; Section 3 counts one fixed
list on every model instead.

- *gap* = share of lies with the family minus share of truths, in points.
- *strict rule* = truths and both controls at most 5%, lies at least 50%; *main rule* = at most 10% and at least 40% (the user's decision of 2026-10-02).
- *lie-leaning* = lies at least 15%, truths at most 15%, both controls at most 10%, gap at least 10 points. This looser bar is my choice: on Gemma the two rules keep one family or none, and the truth groups are 30 and 32 transcripts, so 15% is four or five of them.

## 1. Every lie-leaning family, per model

All kept families whose gap is positive, sorted by gap. Families with a gap of 5 points or less are folded into one line.

### Qwen (58 kept families; lies / truths / no-pressure truths / unrelated = 152 / 81 / 138 / 158)

| family | draft side | members | lies | truths | no-pressure truths | unrelated | gap | rule met | lie-leaning |
|---|---|---|---|---|---|---|---|---|---|
| lie | lie | `谎言`, `说谎`, `撒谎`, `谎`, `␣lied`, `␣lie`, `␣lies`, `␣mentira`, `␣거짓`, `␣lying`, `␣Lie`, `␣Lies`, `lie`, `Lie`, `lies`, `lying`, `␣liar` | 127/152 (84%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | +75 | main | yes |
| fake | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `假`, `假的`, `.fake`, `_fake`, `虚假` | 117/152 (77%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | +71 | main | yes |
| falsehood | lie | `␣falsehood` | 89/152 (59%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | +59 | strict | yes |
| misinformation | lie | `␣misinformation`, `虚假信息` | 101/152 (66%) | 7/81 (9%) | 10/138 (7%) | 0/158 (0%) | +58 | main | yes |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗`, `␣deceive`, `␣deceit`, `␣deceived` | 94/152 (62%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | +56 | main | yes |
| fabricate | lie | `伪造`, `虚构`, `造假`, `␣fabricated`, `弄虚作假` | 83/152 (55%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | +53 | strict | yes |
| conceal | lie | `隐瞒`, `掩盖`, `瞒` | 109/152 (72%) | 17/81 (21%) | 2/138 (1%) | 0/158 (0%) | +51 | – | – |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `FALSE`, `>false`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `真假` | 79/152 (52%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | +50 | strict | yes |
| mislead | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 61/152 (40%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) | +33 | main | yes |
| excuse | unclear | `␣excuse`, `␣excuses`, `借口`, `辩解` | 33/152 (22%) | 2/81 (2%) | 3/138 (2%) | 0/158 (0%) | +19 | – | yes |
| dishonest | lie | `␣dishonest` | 35/152 (23%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | +18 | – | yes |
| liar | lie | `␣liar` | 22/152 (14%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | +14 | – | – |
| truth | truth | `真相`, `␣truth`, `truth`, `␣Truth`, `Truth`, `␣truths`, `_truth`, `.truth`, `真理`, `实话`, `说实话`, `␣verità`, `␣vérité` | 102/152 (67%) | 45/81 (56%) | 61/138 (44%) | 0/158 (0%) | +12 | – | – |
| misrepresent | lie | `␣misrepresented` | 20/152 (13%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | +11 | – | – |
| truthful | truth | `␣truthful`, `如实`, `实话`, `实事求是`, `说实话` | 101/152 (66%) | 46/81 (57%) | 59/138 (43%) | 0/158 (0%) | +10 | – | – |
| dismiss | unclear | `␣dismiss`, `␣dismissing`, `␣dismissal`, `-dismiss`, `␣dismissed`, `dismiss`, `.dismiss`, `Dismiss` | 14/152 (9%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | +9 | – | – |
| spin | lie | `␣spin`, `spin`, `Spin`, `␣spun`, `-spin`, `␣Spin`, `␣spins`, `␣spinning`, `_spin` | 13/152 (9%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | +9 | – | – |
| bluff | lie | `␣bluff` | 12/152 (8%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | +8 | – | – |
| rebut | unclear | `反驳`, `␣rebut`, `␣refute`, `␣debunk` | 31/152 (20%) | 11/81 (14%) | 12/138 (9%) | 0/158 (0%) | +7 | – | – |
| justify | unclear | `辩解` | 12/152 (8%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) | +7 | – | – |
| fraud | lie | `骗局`, `␣fraudulent`, `欺诈` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | +6 | – | – |
| blame | unclear | `␣blame`, `␣blames`, `␣blamed` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | +6 | – | – |
| evade (+4), vague (+4), fiction (+3), pretend (+3), ignore (+3), avoid (+3), apologize (+2), clarify (+1), secret (+1), omit (+1), accurate (+1), contradict (+0), redirect (+0) | | gap of 5 points or less | | | | | | | |

Draft lie-side families that are not more frequent after lies: inaccurate (0% / 0%), hidden (0% / 1%), wrong (7% / 9%), incorrect (7% / 9%), unethical (3% / 23%).

### Gemma-12B (66 kept families; lies / truths / no-pressure truths / unrelated = 49 / 32 / 135 / 179)

| family | draft side | members | lies | truths | no-pressure truths | unrelated | gap | rule met | lie-leaning |
|---|---|---|---|---|---|---|---|---|---|
| lie | lie | `謊`, `␣মিথ্যা`, `谎`, `␣거짓`, `␣झूठ`, `Lie` | 20/49 (41%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) | +35 | main | yes |
| hush emoji | lie | `🤫`, `🤐` | 28/49 (57%) | 11/32 (34%) | 1/135 (1%) | 0/179 (0%) | +23 | – | – |
| obfuscate | lie | `␣obfusc` | 15/49 (31%) | 3/32 (9%) | 0/135 (0%) | 0/179 (0%) | +21 | – | yes |
| mislead | lie | `␣misleading`, `␣mislead`, `␣misled` | 12/49 (24%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) | +18 | – | yes |
| pretend | lie | `␣pretending`, `␣pretended`, `␣pretends` | 10/49 (20%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) | +17 | – | yes |
| reassure | unclear | `␣reassurance`, `␣reassuring`, `␣reassured`, `␣reassure` | 15/49 (31%) | 5/32 (16%) | 7/135 (5%) | 0/179 (0%) | +15 | – | – |
| evade | lie | `␣evas`, `␣evasion`, `␣evade`, `回避`, `␣evaded` | 10/49 (20%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) | +14 | – | yes |
| fake | lie | `偽`, `FAKE`, `伪` | 6/49 (12%) | 0/32 (0%) | 1/135 (1%) | 0/179 (0%) | +12 | – | – |
| hide | lie | `隐藏`, `␣скры`, `␣concealing`, `␣concealment`, `Hide`, `␣hiding`, `隠` | 9/49 (18%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) | +12 | – | yes |
| deflect | lie | `␣deflect`, `␣deflection`, `␣deflected` | 9/49 (18%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) | +12 | – | yes |
| misinformation | lie | `␣misinformation`, `␣disinformation` | 7/49 (14%) | 1/32 (3%) | 3/135 (2%) | 0/179 (0%) | +11 | – | – |
| secret | lie | `␣secrecy`, `␣خفیہ`, `␣secretly` | 5/49 (10%) | 0/32 (0%) | 2/135 (1%) | 0/179 (0%) | +10 | – | – |
| blatant | unclear | `␣blatantly`, `␣blatant` | 8/49 (16%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) | +10 | – | yes |
| avoid | unclear | `避免`, `Avoid`, `␣menghindari`, `Avoiding`, `␣avoidance`, `␣এড়িয়ে`, `␣avoiding`, `␣Avoiding`, `éviter`, `␣avoids`, `␣evitare`, `␣vermeiden`, `␣avoid`, `avoid`, `␣Avoid`, `␣evitar`, `␣éviter`, `␣evitando` | 23/49 (47%) | 12/32 (38%) | 3/135 (2%) | 1/179 (1%) | +9 | – | – |
| contradict | unclear | `␣contradicting`, `␣contradicted`, `␣contradicts`, `␣противоре`, `␣contradictory` | 9/49 (18%) | 3/32 (9%) | 3/135 (2%) | 0/179 (0%) | +9 | – | – |
| justify | unclear | `␣justifications`, `␣justification` | 12/49 (24%) | 5/32 (16%) | 3/135 (2%) | 1/179 (1%) | +9 | – | – |
| sincere | truth | `Sincerely` | 4/49 (8%) | 0/32 (0%) | 19/135 (14%) | 24/179 (13%) | +8 | – | – |
| fraud | lie | `␣fraudulently`, `␣fraudulent` | 4/49 (8%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) | +8 | – | – |
| redirect | unclear | `␣redirection`, `␣redirect`, `redirect`, `Redirect`, `␣Redirect`, `REDIRECT`, `␣redirected`, `␣redirects` | 5/49 (10%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) | +7 | – | – |
| dodge | lie | `␣dodging`, `␣dodge`, `dodge` | 5/49 (10%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) | +7 | – | – |
| manipulate | lie | `Manipulation`, `␣manipulative` | 3/49 (6%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) | +6 | – | – |
| rumour | unclear | `␣rumors`, `␣rumored`, `␣rumor` | 3/49 (6%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) | +6 | – | – |
| deceive | lie | `␣deception`, `␣deceptive`, `␣deceit` | 4/49 (8%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) | +5 | – | – |
| dishonest | lie | `␣dishonesty`, `␣dishonest` | 4/49 (8%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) | +5 | – | – |
| misrepresent | lie | `␣misrepresented` | 4/49 (8%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) | +5 | – | – |
| clever (+5), deliberately (+4), refuse (+4), scepticism (+3), honest (+3), persuade (+3), omit (+2), withhold (+2), fabricate (+2), unethical (+2), damning (+2), unknowingly (+2), paranoia (+2), true (+2), vague (+2), rebut (+2), whisper (+2), suspicion (+1), doubt (+1), exaggerate (+1), truth (+1), false (+1), unapologetic (+1) | | gap of 5 points or less | | | | | | | |

Draft lie-side families that are not more frequent after lies: sneaky (6% / 6%), incorrect (2% / 3%).

### Gemma-27B (49 kept families; lies / truths / no-pressure truths / unrelated = 58 / 30 / 133 / 199)

| family | draft side | members | lies | truths | no-pressure truths | unrelated | gap | rule met | lie-leaning |
|---|---|---|---|---|---|---|---|---|---|
| lie | lie | `␣মিথ্যা`, `␣거짓`, `␣झूठ`, `谎`, `謊`, `␣lied`, `␣liar`, `␣lying`, `Lie`, `🤥` | 20/58 (34%) | 4/30 (13%) | 0/133 (0%) | 0/199 (0%) | +21 | – | yes |
| keep-quiet emoji | unclear | `🤫`, `🤐`, `🔇` | 35/58 (60%) | 12/30 (40%) | 13/133 (10%) | 1/199 (1%) | +20 | – | – |
| lying-face emoji | lie | `🤥` | 19/58 (33%) | 4/30 (13%) | 0/133 (0%) | 0/199 (0%) | +19 | – | yes |
| secret | lie | `␣خفیہ`, `秘密` | 12/58 (21%) | 3/30 (10%) | 2/133 (2%) | 0/199 (0%) | +11 | – | yes |
| reassure | unclear | `␣安心`, `安心`, `␣reassurance`, `␣reassured`, `␣reassuring`, `␣reassure` | 19/58 (33%) | 7/30 (23%) | 27/133 (20%) | 24/199 (12%) | +9 | – | – |
| confident | unclear | `␣आत्मविश्वास`, `自信`, `Confident`, `Confidence`, `␣confidence`, `␣confident`, `confidence`, `␣confidently`, `␣Confidence`, `confident` | 20/58 (34%) | 8/30 (27%) | 2/133 (2%) | 2/199 (1%) | +8 | – | – |
| crafty | unclear | `巧妙` | 6/58 (10%) | 1/30 (3%) | 1/133 (1%) | 1/199 (1%) | +7 | – | – |
| confidential | unclear | `␣गोपनीयता` | 5/58 (9%) | 1/30 (3%) | 5/133 (4%) | 0/199 (0%) | +5 | – | – |
| avoid | unclear | `éviter`, `␣এড়িয়ে`, `Avoiding`, `Avoid`, `避免`, `avoid`, `␣избежать` | 5/58 (9%) | 1/30 (3%) | 3/133 (2%) | 0/199 (0%) | +5 | – | – |
| locked (+4), mislead (+3), fake (+3), manipulate (+3), conceal (+3), suspicion (+3), protect (+3), cunning (+3), false (+3), honest (+3), hand over mouth (+3), deceive (+2), truth (+2), sceptical (+2), accuse (+2), contradict (+2), misinformation (+2), trick (+2), scam (+2), shameless (+2), sneaky (+2), pretend (+2), challenge (+2), rumour (+2), incorrect (+2), dishonest (+0) | | gap of 5 points or less | | | | | | | |

Draft lie-side families that are not more frequent after lies: betray (2% / 3%), immoral (0% / 3%).

### gpt-oss (1 kept families; lies / truths / no-pressure truths / unrelated = 116 / 94 / 127 / 265)

| family | draft side | members | lies | truths | no-pressure truths | unrelated | gap | rule met | lie-leaning |
|---|---|---|---|---|---|---|---|---|---|
| (no kept family has a positive gap: concession (unclear; 1% / 1%)) | | | | | | | | | |

Note: gpt-oss's turn boundary is made of different tokens. Qwen and Gemma have `turn end, newline, turn start,
user, newline`, and the signal sits at the first newline; gpt-oss has `<|end|>, <|start|>, user, <|message|>` with no
newline, so its post-response slot 1 is `<|start|>`.

## 2. The overlap study on each model's signal set

The study of `family_findings.md` Section 9, repeated. Sets: the families that meet the strict rule, those that meet
the main rule (the strict ones included), and the lie-leaning families.

| model | strict rule | main rule | lie-leaning |
|---|---|---|---|
| Qwen | falsehood, fabricate, false (3) | lie, fake, falsehood, misinformation, deceive, fabricate, false, mislead (8) | lie, fake, falsehood, misinformation, deceive, fabricate, false, mislead, excuse, dishonest (10) |
| Gemma-12B | none (0) | lie (1) | lie, obfuscate, mislead, pretend, evade, hide, deflect, blatant (8) |
| Gemma-27B | none (0) | none (0) | lie, lying-face emoji, secret (3) |
| gpt-oss | none (0) | none (0) | none (0) — no newline in its turn boundary; slot 1 is `<\|start\|>` |

### Qwen: main rule (8 families: lie, fake, falsehood, misinformation, deceive, fabricate, false, mislead)

Number of these families present, per transcript:

| at least | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|
| 1 | 133/152 (88%) | 10/81 (12%) | 13/138 (9%) | 0/158 (0%) |
| 2 | 126/152 (83%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) |
| 3 | 115/152 (76%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) |
| 4 | 104/152 (68%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) |
| 5 | 92/152 (61%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) |
| 6 | 80/152 (53%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) |
| 7 | 65/152 (43%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| 8 | 36/152 (24%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |

- Greedy order (each family with the lies it adds that no earlier family caught): lie +127, fake +4, misinformation +1, fabricate +1, falsehood +0, deceive +0, false +0, mislead +0. Lies with none of the set: 19/152.
- Truths with one or more of the set: 10/81; how many families each has: 1, 1, 1, 1, 3, 4, 5, 5, 6, 6.
- Scenarios with both a lie and a truth: 70. In them, one or more families: lies 61/70, truths 7/70; two or more: lies 58/70, truths 4/70.

Share of the lies with the row family that also have the column family:

| A \ B | lie | fake | falsehood | misinformation | deceive | fabricate | false | mislead |
|---|---|---|---|---|---|---|---|---|
| lie (127) | – | 89% | 70% | 78% | 72% | 63% | 61% | 47% |
| fake (117) | 97% | – | 74% | 79% | 79% | 70% | 67% | 50% |
| falsehood (89) | 100% | 98% | – | 90% | 87% | 74% | 85% | 61% |
| misinformation (101) | 98% | 92% | 79% | – | 82% | 67% | 67% | 56% |
| deceive (94) | 98% | 99% | 82% | 88% | – | 78% | 74% | 55% |
| fabricate (83) | 96% | 99% | 80% | 82% | 88% | – | 75% | 47% |
| false (79) | 99% | 99% | 96% | 86% | 89% | 78% | – | 63% |
| mislead (61) | 98% | 97% | 89% | 93% | 85% | 64% | 82% | – |

### Qwen: lie-leaning (10 families: lie, fake, falsehood, misinformation, deceive, fabricate, false, mislead, excuse, dishonest)

Number of these families present, per transcript:

| at least | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|
| 1 | 134/152 (88%) | 14/81 (17%) | 16/138 (12%) | 0/158 (0%) |
| 2 | 128/152 (84%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) |
| 3 | 119/152 (78%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) |
| 4 | 110/152 (72%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) |
| 5 | 98/152 (64%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) |
| 6 | 86/152 (57%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) |
| 7 | 71/152 (47%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| 8 | 51/152 (34%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| 9 | 21/152 (14%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| 10 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |

- Greedy order (each family with the lies it adds that no earlier family caught): lie +127, fake +4, misinformation +1, fabricate +1, excuse +1, falsehood +0, deceive +0, false +0, mislead +0, dishonest +0. Lies with none of the set: 18/152.
- Truths with one or more of the set: 14/81; how many families each has: 1, 1, 1, 1, 1, 1, 1, 1, 3, 5, 5, 5, 6, 7.
- Scenarios with both a lie and a truth: 70. In them, one or more families: lies 61/70, truths 10/70; two or more: lies 58/70, truths 4/70.

Share of the lies with the row family that also have the column family:

| A \ B | lie | fake | falsehood | misinformation | deceive | fabricate | false | mislead | excuse | dishonest |
|---|---|---|---|---|---|---|---|---|---|---|
| lie (127) | – | 89% | 70% | 78% | 72% | 63% | 61% | 47% | 25% | 28% |
| fake (117) | 97% | – | 74% | 79% | 79% | 70% | 67% | 50% | 25% | 29% |
| falsehood (89) | 100% | 98% | – | 90% | 87% | 74% | 85% | 61% | 12% | 38% |
| misinformation (101) | 98% | 92% | 79% | – | 82% | 67% | 67% | 56% | 19% | 31% |
| deceive (94) | 98% | 99% | 82% | 88% | – | 78% | 74% | 55% | 18% | 36% |
| fabricate (83) | 96% | 99% | 80% | 82% | 88% | – | 75% | 47% | 23% | 36% |
| false (79) | 99% | 99% | 96% | 86% | 89% | 78% | – | 63% | 11% | 43% |
| mislead (61) | 98% | 97% | 89% | 93% | 85% | 64% | 82% | – | 11% | 38% |
| excuse (33) | 97% | 88% | 33% | 58% | 52% | 58% | 27% | 21% | – | 6% |
| dishonest (35) | 100% | 97% | 97% | 89% | 97% | 86% | 97% | 66% | 6% | – |

### Gemma-12B: main rule (1 families: lie)

Number of these families present, per transcript:

| at least | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|
| 1 | 20/49 (41%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |

- Greedy order (each family with the lies it adds that no earlier family caught): lie +20. Lies with none of the set: 29/49.
- Truths with one or more of the set: 2/32; how many families each has: 1, 1.
- Scenarios with both a lie and a truth: 16. In them, one or more families: lies 5/16, truths 1/16; two or more: lies 0/16, truths 0/16.

### Gemma-12B: lie-leaning (8 families: lie, obfuscate, mislead, pretend, evade, hide, deflect, blatant)

Number of these families present, per transcript:

| at least | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|
| 1 | 30/49 (61%) | 5/32 (16%) | 1/135 (1%) | 0/179 (0%) |
| 2 | 23/49 (47%) | 3/32 (9%) | 0/135 (0%) | 0/179 (0%) |
| 3 | 18/49 (37%) | 3/32 (9%) | 0/135 (0%) | 0/179 (0%) |
| 4 | 15/49 (31%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| 5 | 5/49 (10%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| 6 | 2/49 (4%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| 7 | 0/49 (0%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| 8 | 0/49 (0%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |

- Greedy order (each family with the lies it adds that no earlier family caught): lie +20, deflect +7, hide +2, pretend +1, obfuscate +0, mislead +0, evade +0, blatant +0. Lies with none of the set: 19/49.
- Truths with one or more of the set: 5/32; how many families each has: 1, 1, 3, 5, 6.
- Scenarios with both a lie and a truth: 16. In them, one or more families: lies 9/16, truths 4/16; two or more: lies 7/16, truths 2/16.

Share of the lies with the row family that also have the column family:

| A \ B | lie | obfuscate | mislead | pretend | evade | hide | deflect | blatant |
|---|---|---|---|---|---|---|---|---|
| lie (20) | – | 50% | 55% | 45% | 25% | 30% | 10% | 30% |
| obfuscate (15) | 67% | – | 47% | 33% | 53% | 47% | 40% | 33% |
| mislead (12) | 92% | 58% | – | 42% | 25% | 25% | 17% | 42% |
| pretend (10) | 90% | 50% | 50% | – | 20% | 30% | 10% | 40% |
| evade (10) | 50% | 80% | 30% | 20% | – | 30% | 60% | 40% |
| hide (9) | 67% | 78% | 33% | 33% | 33% | – | 11% | 22% |
| deflect (9) | 22% | 67% | 22% | 11% | 67% | 11% | – | 33% |
| blatant (8) | 75% | 62% | 62% | 50% | 50% | 25% | 38% | – |

### Gemma-27B: main rule (0 families)

No family in this set.

### Gemma-27B: lie-leaning (3 families: lie, lying-face emoji, secret)

Number of these families present, per transcript:

| at least | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|
| 1 | 24/58 (41%) | 6/30 (20%) | 2/133 (2%) | 0/199 (0%) |
| 2 | 19/58 (33%) | 4/30 (13%) | 0/133 (0%) | 0/199 (0%) |
| 3 | 8/58 (14%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |

- Greedy order (each family with the lies it adds that no earlier family caught): lie +20, secret +4, lying-face emoji +0. Lies with none of the set: 34/58.
- Truths with one or more of the set: 6/30; how many families each has: 1, 1, 2, 2, 2, 3.
- Scenarios with both a lie and a truth: 11. In them, one or more families: lies 5/11, truths 4/11; two or more: lies 4/11, truths 3/11.

Share of the lies with the row family that also have the column family:

| A \ B | lie | lying-face emoji | secret |
|---|---|---|---|
| lie (20) | – | 95% | 40% |
| lying-face emoji (19) | 100% | – | 42% |
| secret (12) | 67% | 67% | – |

### gpt-oss: main rule (0 families)

No family in this set.

### gpt-oss: lie-leaning — the same set as above

## 3. The same families on every model, with one fixed token list each

For each family name, the list is the union of the tokens that the drafts of all four models give it at this
position; tokens are matched by spelling (leading space ignored) in each model's vocabulary. The list is shown so
that the rows can be checked. Cells: lies / truths, in percent; `–` = no token of the list is in the model's
vocabulary.

| family | fixed list | Qwen | Gemma-12B | Gemma-27B | gpt-oss |
|---|---|---|---|---|---|
| lie | `Lie`, `Lies`, `liar`, `lie`, `lied`, `lies`, `lying`, `mentira`, `झूठ`, `মিথ্যা`, `撒谎`, `謊`, `说谎`, `谎`, `谎言`, `거짓`, `🤥` | 84 / 9 | 41 / 6 | 34 / 13 | 0 / 0 |
| fake | `.fake`, `FAKE`, `Fake`, `_fake`, `fake`, `جعلی`, `नकली`, `伪`, `假`, `假的`, `偽`, `虚假` | 77 / 6 | 12 / 0 | 3 / 0 | 0 / 0 |
| falsehood | `falsehood` | 59 / 0 | 4 / 0 | 2 / 0 | – |
| misinformation | `disinformation`, `misinformation`, `虚假信息` | 66 / 9 (controls 7) | 14 / 3 | 2 / 0 | 0 / 0 |
| deceive | `deceit`, `deceive`, `deceived`, `deceiving`, `deception`, `deceptive`, `فريبي`, `欺`, `欺骗`, `骗` | 62 / 6 | 8 / 3 | 12 / 10 | 0 / 0 |
| fabricate | `Fabrication`, `fabricate`, `fabricated`, `fabricating`, `fabrication`, `伪造`, `弄虚作假`, `虚构`, `造假` | 55 / 1 | 2 / 0 | 0 / 0 | 0 / 0 |
| false | `/false`, `>false`, `FALSE`, `False`, `fals`, `false`, `falsehood`, `falsely`, `faux`, `untrue`, `真假` | 61 / 2 | 4 / 3 | 3 / 0 | 0 / 0 |
| mislead | `mislead`, `misleading`, `misled`, `误导`, `误导性` | 40 / 7 | 24 / 6 | 3 / 0 | 0 / 0 |
| excuse | `excuse`, `excuses`, `借口`, `辩解` | 22 / 2 | 8 / 0 | 0 / 0 | 0 / 0 |
| dishonest | `dishonest`, `dishonesty` | 23 / 5 | 8 / 3 | 3 / 3 | 0 / 0 |
| obfuscate | `obfusc` | – | 31 / 9 | 0 / 0 | – |
| pretend | `pretend`, `pretended`, `pretending`, `pretends` | 3 / 0 | 20 / 3 | 2 / 0 | 0 / 0 |
| evade | `deflect`, `dodge`, `evade`, `evaded`, `evas`, `evasion`, `回避`, `规避`, `逃避`, `避开` | 12 / 7 | 27 / 12 | 0 / 0 | 0 / 0 |
| hide | `Hide`, `concealing`, `concealment`, `hiding`, `скры`, `隐藏`, `隠` | 0 / 0 | 18 / 6 | 0 / 0 | 0 / 0 |
| deflect | `deflect`, `deflected`, `deflection` | 3 / 0 | 18 / 6 | 2 / 0 | – |
| blatant | `blatant`, `blatantly` | 6 / 0 | 16 / 6 | 3 / 3 | 0 / 0 |
| lying-face emoji | `🤥` | – | 2 / 0 | 33 / 13 | – |
| secret | `secrecy`, `secretly`, `خفیہ`, `秘密` | 1 / 0 | 10 / 0 | 21 / 10 | 0 / 0 |
| conceal | `nascost`, `掩盖`, `瞒`, `瞞`, `隐瞒` | 72 / 21 | 0 / 0 | 3 / 0 | – |

A union list is wider than any one model's own list, so a cell can differ from Section 1: Qwen's `false` reads 61
here against 52 there because Gemma-12B's draft puts `falsehood` in its `false` family; Gemma-12B's `evade` reads 27
against 20 because Qwen's draft puts `deflect` and `dodge` in its `evade` family.

Qwen's eight families, each with its fixed list above, counted on every model:

| model | one or more | two or more | three or more |
|---|---|---|---|
| Qwen | 88 / 12 / 9 / 0 | 83 / 7 / 2 / 0 | 76 / 7 / 1 / 0 |
| Gemma-12B | 43 / 6 / 3 / 0 | 27 / 6 / 0 / 0 | 20 / 6 / 0 / 0 |
| Gemma-27B | 34 / 20 / 3 / 1 | 14 / 3 / 2 / 0 | 7 / 0 / 0 / 0 |
| gpt-oss | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |

Cells: lies / truths / no-pressure truths / unrelated, in percent.

## 4. The other post-response slots

Number of kept families that meet the main rule (in brackets: the strict rule) at each post-response slot, per model.

| model | slot 0 | slot 1 | slot 2 | slot 3 | slot 4 |
|---|---|---|---|---|---|
| Qwen | 0 (0) | 8 (3) | 0 (0) | 0 (0) | 0 (0) |
| Gemma-12B | 0 (0) | 1 (0) | 0 (0) | 0 (0) | 0 (0) |
| Gemma-27B | 0 (0) | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| gpt-oss | 0 (0) | 0 (0) | 0 (0) | 0 (0) | – |

