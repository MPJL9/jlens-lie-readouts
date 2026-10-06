# Family report: qwen3.6-27b, logit lens, band 35-58, part Q6_factual, group questionb

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q6_factual_questionb_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## q_tok8

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `␣lie` | 18 | L35-38; most at L35 (2), L36 (11), L37 (18) |
| 1 | honest (being honest / truthful) | truth | `诚实` | 4 | L36-50; most at L36 (2), L45 (3), L49 (3) |
| 1 | admit (admitting / acknowledging) | truth | `承认`, `␣admission` | 7 | L40-58; most at L40 (5), L44 (4), L45 (2) |
| 1 | knowingly (doing it knowingly, in full awareness) | unclear | `明知` | 11 | L35-54; most at L50 (4), L51 (8), L52 (9) |
| 1 | self-examine (checking / reflecting on one's own output) | unclear | `自查`, `自检`, `反思`, `自省`, `审视`, `␣reflect`, `␣reflection`, `reflect`, `␣reflecting`, `␣Reflection` | 160 | L35-58; most at L52 (128), L53 (135), L54 (145) |
| 1 | objective (being objective) | unclear | `客观` | 8 | L35-44; most at L36 (6), L43 (3), L44 (6) |
| 2 | lie (telling a lie) | lie | `␣lie`, `␣лож` | 32 | L35-55; most at L36 (11), L37 (18), L55 (14) |
| 2 | honest (being honest) | truth | `诚实` | 4 | L36-50; most at L36 (2), L45 (3), L49 (3) |
| 2 | admit (admitting / owning up) | truth | `承认`, `␣admission` | 7 | L40-58; most at L40 (5), L44 (4), L45 (2) |
| 2 | knowingly (acting with knowledge that it is so) | unclear | `明知` | 11 | L35-54; most at L50 (4), L51 (8), L52 (9) |
| 2 | objective (being objective / impartial) | unclear | `客观` | 8 | L35-44; most at L36 (6), L43 (3), L44 (6) |

## q_tok9

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | honest (being honest / truthful) | truth | `实事求是` | 7 | L41-44; most at L42 (3), L43 (6), L44 (2) |
| 2 | objective (being objective / sticking to the facts) | unclear | `实事求是` | 7 | L41-44; most at L42 (3), L43 (6), L44 (2) |

## q_tok10

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | admit (admitting / acknowledging) | truth | `承认` | 1 | L40-43; most at L40 (1), L43 (1) |
| 2 | admit (admitting / owning up) | truth | `承认` | 1 | L40-43; most at L40 (1), L43 (1) |

## q_tok11

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | sorry (apologising) | unclear | `␣sorry` | 2 | L56-56; most at L56 (2) |
| 1 | refuse (refusing) | unclear | `␣refusal` | 1 | L39-39; most at L39 (1) |
| 2 | sorry (apology / regret) | unclear | `␣sorry` | 2 | L56-56; most at L56 (2) |
| 2 | refuse (refusing) | unclear | `␣refusal` | 1 | L39-39; most at L39 (1) |

## q_tok12

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 2 | silent (staying silent / not speaking) | unclear | `不语` | 78 | L46-49; most at L47 (2), L48 (27), L49 (77) |

## q_tok13

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | honest (being honest / truthful) | truth | `诚实`, `␣truthful`, `如实`, `实话`, `实事求是`, `␣honesty`, `忠实`, `诚信`, `诚实守信`, `坦诚`, `␣honest`, `诚` | 165 | L35-58; most at L38 (91), L40 (94), L41 (91) |
| 1 | dishonest (being dishonest) | lie | `␣dishonest` | 1 | L57-57; most at L57 (1) |
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceit`, `␣deceive`, `骗` | 36 | L35-58; most at L35 (25), L36 (11), L37 (18) |
| 1 | lie (telling a lie) | lie | `说谎`, `谎言`, `␣lie`, `撒谎`, `␣lying`, `lying`, `谎` | 21 | L35-58; most at L39 (9), L40 (9), L55 (8) |
| 1 | hide (hiding / concealing) | lie | `隐瞒`, `␣hidden`, `-hidden`, `隐藏的`, `隐藏`, `hidden`, `Hidden`, `␣hide`, `␣Hidden`, `␣conceal`, `掩盖` | 65 | L35-58; most at L36 (27), L39 (30), L40 (37) |
| 1 | secret (secrecy) | lie | `␣secret`, `␣secretly`, `秘密`, `Secret`, `secret`, `-secret` | 6 | L35-58; most at L38 (2), L56 (3), L57 (1) |
| 1 | reveal (revealing / disclosing) | truth | `透露`, `␣reveal`, `reveal` | 17 | L35-39; most at L36 (3), L37 (3), L38 (12) |
| 1 | admit (admitting / acknowledging) | truth | `承认`, `␣acknowledge`, `␣acknowledging`, `␣acknowledgment`, `␣acknowledges`, `␣admitted`, `␣admitting`, `坦白` | 49 | L35-58; most at L37 (23), L40 (22), L42 (31) |
| 1 | deliberate (doing it intentionally) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `故意的`, `␣deliberate`, `␣intentional` | 61 | L35-58; most at L35 (22), L36 (46), L37 (54) |
| 1 | knowingly (doing it knowingly, in full awareness) | unclear | `明知` | 104 | L35-54; most at L43 (90), L44 (64), L47 (61) |
| 1 | fictional (fictional / made up) | unclear | `虚构`, `架空`, `␣fictional`, `fiction`, `␣fiction`, `␣Fiction` | 101 | L35-56; most at L35 (51), L44 (57), L45 (67) |
| 1 | fake (fake) | lie | `␣fake`, `fake`, `Fake` | 1 | L36-37; most at L36 (1), L37 (1) |
| 1 | pretend (pretending) | lie | `␣pretending` | 1 | L37-37; most at L37 (1) |
| 1 | trick (tricking) | lie | `␣trick` | 1 | L58-58; most at L58 (1) |
| 1 | role-play (playing a role) | unclear | `扮演`, `角色扮演`, `扮演着` | 97 | L35-57; most at L35 (59), L36 (71), L52 (55) |
| 1 | persona (an assumed persona) | unclear | `␣persona`, `␣personas`, `Persona`, `␣Persona`, `persona`, `␣Personas` | 64 | L51-58; most at L52 (53), L53 (50), L56 (63) |
| 1 | violate (violating rules or principles) | unclear | `违反`, `违背`, `违反了`, `违`, `␣violate`, `␣violating`, `␣violations`, `违规`, `␣violation` | 137 | L35-57; most at L37 (91), L38 (96), L39 (85) |
| 1 | comply (complying with rules) | unclear | `合规`, `遵守`, `␣compliance`, `严格遵守`, `␣Compliance`, `␣comply` | 40 | L35-58; most at L37 (14), L38 (17), L39 (16) |
| 1 | ethics (ethics / morality) | unclear | `␣ethical`, `伦理`, `␣ethics`, `ethical`, `␣Ethics`, `道德`, `␣moral`, `职业道德`, `的道德`, `␣morally`, `␣morality`, `␣ethic`, `␣Moral`, `␣morals` | 63 | L35-58; most at L39 (43), L40 (49), L55 (45) |
| 1 | unethical (being unethical) | lie | `␣unethical` | 10 | L37-58; most at L40 (4), L51 (5), L55 (5) |
| 1 | conscience (conscience) | unclear | `良心` | 19 | L35-51; most at L49 (16), L50 (10), L51 (2) |
| 1 | objective (being objective) | unclear | `客观`, `␣objectively`, `␣objective`, `objective`, `Objective` | 181 | L35-57; most at L36 (146), L42 (133), L43 (134) |
| 1 | self-examine (checking / reflecting on one's own output) | unclear | `自查`, `反思`, `自检`, `␣reflection`, `␣reflective`, `.reflect`, `␣Reflection`, `Reflection`, `Reflect`, `reflection`, `␣reflect`, `reflect`, `自省`, `审视`, `␣Reflect` | 49 | L35-58; most at L35 (26), L37 (16), L44 (17) |
| 1 | euphemistic (phrasing tactfully / indirectly) | unclear | `委婉` | 25 | L35-37; most at L35 (21), L36 (17), L37 (3) |
| 1 | refuse (refusing) | unclear | `拒绝`, `␣refusal`, `拒绝了`, `␣refused`, `␣refuse`, `␣refusing`, `␣refus`, `␣refuses` | 9 | L37-58; most at L39 (5), L40 (6), L43 (5) |
| 2 | lie (telling a lie) | lie | `说谎`, `␣lie`, `谎言`, `撒谎`, `谎` | 21 | L35-58; most at L39 (8), L40 (9), L55 (8) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗` | 36 | L35-58; most at L35 (25), L36 (11), L37 (18) |
| 2 | trick (tricking) | lie | `␣trick` | 1 | L58-58; most at L58 (1) |
| 2 | conceal (concealing / withholding the truth) | lie | `隐瞒`, `␣conceal`, `掩盖` | 44 | L35-53; most at L39 (29), L40 (37), L44 (17) |
| 2 | hide (hiding / hidden) | lie | `␣hidden`, `-hidden`, `隐藏的`, `隐藏`, `hidden`, `Hidden`, `␣hide`, `␣Hidden` | 37 | L36-58; most at L54 (21), L55 (20), L56 (17) |
| 2 | secret (secrecy) | lie | `␣secret`, `␣secretly`, `秘密`, `Secret`, `secret`, `-secret` | 6 | L35-58; most at L38 (2), L56 (3), L57 (1) |
| 2 | fake (faking) | lie | `␣fake`, `fake`, `Fake` | 1 | L36-37; most at L36 (1), L37 (1) |
| 2 | pretend (pretending) | lie | `␣pretending` | 1 | L37-37; most at L37 (1) |
| 2 | fictional (made-up / fabricated / fictional) | unclear | `虚构`, `架空`, `␣fictional`, `fiction`, `␣fiction`, `␣Fiction` | 101 | L35-56; most at L35 (51), L44 (57), L45 (67) |
| 2 | role-play (playing a role) | unclear | `扮演`, `角色扮演` | 97 | L35-57; most at L35 (59), L36 (71), L52 (55) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 1 | L57-57; most at L57 (1) |
| 2 | honest (being honest / integrity) | truth | `诚实`, `␣honesty`, `诚信`, `诚实守信`, `␣honest`, `诚` | 97 | L35-58; most at L39 (51), L40 (61), L42 (48) |
| 2 | truthful (telling the truth / truthfully) | truth | `␣truthful`, `如实`, `实话` | 131 | L35-58; most at L35 (52), L40 (74), L41 (62) |
| 2 | candid (candour / frankness) | truth | `坦诚` | 3 | L35-37; most at L35 (2), L36 (2), L37 (1) |
| 2 | confess (confessing / coming clean) | truth | `坦白` | 1 | L37-37; most at L37 (1) |
| 2 | faithful (faithful (to facts or instructions)) | unclear | `忠实` | 67 | L35-45; most at L36 (31), L38 (55), L41 (33) |
| 2 | objective (being objective / sticking to the facts) | unclear | `客观`, `␣objectively`, `实事求是`, `␣objective`, `objective`, `Objective` | 182 | L35-57; most at L36 (146), L42 (133), L43 (134) |
| 2 | admit (admitting / owning up) | truth | `承认`, `␣admitted`, `␣admitting` | 48 | L35-58; most at L40 (22), L41 (22), L42 (31) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledge`, `␣acknowledging`, `␣acknowledgment`, `␣acknowledges` | 7 | L35-47; most at L39 (5), L43 (5), L44 (5) |
| 2 | reveal (revealing / disclosing) | truth | `透露`, `␣reveal`, `reveal` | 17 | L35-39; most at L36 (3), L37 (3), L38 (12) |
| 2 | knowingly (acting with knowledge that it is so) | unclear | `明知`, `␣knowingly` | 104 | L35-58; most at L43 (90), L44 (64), L47 (61) |
| 2 | deliberate (intentional / on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `故意的`, `␣intentional`, `刻意`, `有意` | 61 | L35-58; most at L35 (22), L36 (46), L37 (54) |
| 2 | violate (violating / breaking a rule) | unclear | `违反`, `违背`, `违反了`, `违`, `␣violate`, `␣violating`, `␣violations`, `违规`, `␣violation`, `违法` | 137 | L35-57; most at L37 (91), L38 (96), L39 (85) |
| 2 | comply (complying with rules) | unclear | `合规`, `␣compliance`, `遵守`, `严格遵守`, `␣Compliance`, `␣comply` | 40 | L35-58; most at L37 (14), L38 (17), L39 (16) |
| 2 | ethics (ethics / morality) | unclear | `␣ethical`, `伦理`, `␣ethics`, `ethical`, `␣Ethics`, `␣moral`, `道德`, `职业道德`, `␣morally`, `的道德`, `␣morality`, `␣ethic`, `␣Moral`, `␣morals` | 63 | L35-58; most at L39 (43), L40 (49), L55 (45) |
| 2 | unethical (being unethical) | lie | `␣unethical` | 10 | L37-58; most at L40 (4), L51 (5), L55 (5) |
| 2 | conscience (conscience) | unclear | `良心` | 19 | L35-51; most at L49 (16), L50 (10), L51 (2) |
| 2 | euphemistic (tactful / indirect phrasing) | unclear | `委婉` | 25 | L35-37; most at L35 (21), L36 (17), L37 (3) |
| 2 | refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `拒绝了`, `␣refus` | 9 | L37-58; most at L39 (5), L40 (6), L43 (5) |
| 2 | silent (staying silent) | unclear | `沉默` | 2 | L35-37; most at L35 (2), L36 (2), L37 (2) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| q_tok8 | lie | lie | 0.50 | — | `␣лож` |
| q_tok8 | honest | honest | 1.00 | — | — |
| q_tok8 | admit | admit | 1.00 | — | — |
| q_tok8 | knowingly | knowingly | 1.00 | — | — |
| q_tok8 | self-examine | — | 0 | all | — |
| q_tok8 | objective | objective | 1.00 | — | — |
| q_tok9 | honest | objective | 1.00 | — | — |
| q_tok10 | admit | admit | 1.00 | — | — |
| q_tok11 | sorry | sorry | 1.00 | — | — |
| q_tok11 | refuse | refuse | 1.00 | — | — |
| q_tok13 | honest | honest | 0.50 | `␣truthful`, `如实`, `实话`, `实事求是`, `忠实`, `坦诚` | — |
| q_tok13 | dishonest | dishonest | 1.00 | — | — |
| q_tok13 | deceive | deceive | 0.83 | `␣deceit` | — |
| q_tok13 | lie | lie | 0.71 | `␣lying`, `lying` | — |
| q_tok13 | hide | hide | 0.73 | `隐瞒`, `␣conceal`, `掩盖` | — |
| q_tok13 | secret | secret | 1.00 | — | — |
| q_tok13 | reveal | reveal | 1.00 | — | — |
| q_tok13 | admit | acknowledge | 0.50 | `承认`, `␣admitted`, `␣admitting`, `坦白` | — |
| q_tok13 | deliberate | deliberate | 0.75 | — | `刻意`, `有意` |
| q_tok13 | knowingly | knowingly | 0.50 | — | `␣knowingly` |
| q_tok13 | fictional | fictional | 1.00 | — | — |
| q_tok13 | fake | fake | 1.00 | — | — |
| q_tok13 | pretend | pretend | 1.00 | — | — |
| q_tok13 | trick | trick | 1.00 | — | — |
| q_tok13 | role-play | role-play | 0.67 | `扮演着` | — |
| q_tok13 | persona | — | 0 | all | — |
| q_tok13 | violate | violate | 0.90 | — | `违法` |
| q_tok13 | comply | comply | 1.00 | — | — |
| q_tok13 | ethics | ethics | 1.00 | — | — |
| q_tok13 | unethical | unethical | 1.00 | — | — |
| q_tok13 | conscience | conscience | 1.00 | — | — |
| q_tok13 | objective | objective | 0.83 | — | `实事求是` |
| q_tok13 | self-examine | — | 0 | all | — |
| q_tok13 | euphemistic | euphemistic | 1.00 | — | — |
| q_tok13 | refuse | refuse | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: q_tok12: silent, q_tok13: conceal, q_tok13: truthful, q_tok13: candid, q_tok13: confess, q_tok13: faithful, q_tok13: admit, q_tok13: silent

## Families whose name recurs at 3 or more positions

- admit: q_tok10, q_tok13, q_tok8
- honest: q_tok13, q_tok8, q_tok9
- objective: q_tok13, q_tok8, q_tok9

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- q_tok13: conceal / reveal
- q_tok13: deceive / honest
- q_tok13: dishonest / honest
- q_tok13: hide / reveal
- q_tok13: lie / honest
- q_tok13: lie / truthful
- q_tok8: lie / honest

Merged candidate list: `qwen3_6_27b_LL_Q6_factual_questionb_merged.json` (43 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
