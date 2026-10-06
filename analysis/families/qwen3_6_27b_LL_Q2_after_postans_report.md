# Family report: qwen3.6-27b, logit lens, band 35-58, part Q2_after, group postans

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q2_after_postans_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## postans_slot0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | sincere (sincere, earnest) | truth | `诚挚` | 200 | L52-58; most at L53 (186), L54 (195), L58 (29) |
| 1 | neutral (neutral, impartial) | unclear | `中立` | 103 | L42-43; most at L42 (15), L43 (103) |
| 1 | fake (one who fakes) | lie | `faker` | 184 | L36-45; most at L38 (171), L40 (115), L43 (87) |
| 1 | expose (to expose, lay bare) | truth | `揭` | 3 | L37-37; most at L37 (3) |
| 2 | sincere (sincere, heartfelt) | truth | `诚挚` | 200 | L52-58; most at L53 (186), L54 (195), L58 (29) |
| 2 | reveal (to reveal, expose) | truth | `揭` | 3 | L37-37; most at L37 (3) |
| 2 | neutral (neutral) | unclear | `中立` | 103 | L42-43; most at L42 (15), L43 (103) |

## postans_slot1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | conceal (to hide, cover up) | lie | `掩`, `隐瞒`, `-hide` | 181 | L40-58; most at L53 (180), L54 (68), L55 (73) |
| 1 | lie (to tell a lie) | lie | `␣fib`, `撒谎`, `说谎`, `␣lie`, `␣lying`, `谎`, `谎言`, `lying`, `␣lies` | 62 | L35-51; most at L36 (9), L38 (10), L51 (56) |
| 1 | fabricate (made up, fictional) | lie | `虚构` | 5 | L44-46; most at L44 (4), L46 (2) |
| 1 | knowingly (knowing full well (as in 明知故犯)) | unclear | `明知` | 102 | L35-47; most at L42 (61), L43 (86), L44 (96) |
| 1 | honest (honest, honesty) | truth | `诚实`, `诚`, `␣honest`, `␣honesty` | 101 | L35-48; most at L41 (86), L42 (94), L44 (91) |
| 1 | sincere (sincere, earnest) | truth | `诚恳` | 1 | L35-36; most at L35 (1), L36 (1) |
| 1 | candid (candid, frank) | truth | `坦诚` | 8 | L36-48; most at L39 (5), L42 (6), L43 (3) |
| 1 | confess (to own up, make a clean breast) | truth | `坦白` | 1 | L40-40; most at L40 (1) |
| 1 | admit (to admit) | truth | `承认` | 14 | L36-47; most at L39 (9), L40 (7), L46 (10) |
| 1 | deny (to deny) | lie | `否认` | 2 | L39-44; most at L39 (2), L42 (1), L44 (1) |
| 1 | truth (the truth (noun)) | truth | `␣truth`, `␣Truth`, `truth`, `真相`, `真理` | 75 | L35-51; most at L41 (44), L42 (32), L46 (71) |
| 1 | truthful (truthful, as it really is) | truth | `␣truthful`, `如实` | 22 | L35-48; most at L39 (9), L40 (10), L41 (15) |
| 1 | factual (factual, the facts) | truth | `事实`, `␣factual` | 46 | L35-48; most at L41 (19), L43 (20), L46 (34) |
| 1 | objective (objective, unslanted) | unclear | `客观`, `␣objectively` | 39 | L35-47; most at L43 (17), L44 (23), L45 (21) |
| 1 | neutral (neutral, impartial) | unclear | `中立` | 2 | L35-46; most at L35 (1), L36 (1), L46 (1) |
| 1 | upright (upright, principled) | truth | `正直` | 20 | L35-47; most at L35 (12), L36 (15), L38 (12) |
| 1 | ethical (ethical, ethics) | unclear | `␣ethical`, `ethical`, `伦理`, `␣ethics` | 39 | L35-49; most at L40 (32), L42 (34), L43 (32) |
| 1 | moral (moral, morality) | unclear | `道德`, `␣moral`, `␣morally`, `的道德` | 42 | L35-47; most at L43 (28), L44 (22), L46 (29) |
| 1 | violate (to violate, go against (rules, principles)) | unclear | `违背`, `违反`, `违`, `违反了` | 67 | L35-48; most at L43 (21), L44 (56), L45 (27) |
| 1 | illegal (against the law) | unclear | `违法` | 9 | L44-46; most at L44 (8), L45 (8), L46 (6) |
| 1 | legal (lawful, according to law) | unclear | `合法`, `依法`, `合法的`, `␣legally` | 61 | L35-49; most at L36 (39), L37 (36), L44 (55) |
| 1 | legitimate (legitimate, justified) | unclear | `正当`, `␣legitimate` | 11 | L35-38; most at L36 (4), L37 (11), L38 (2) |
| 1 | conform (to conform to, be consistent with) | unclear | `符合`, `是否符合`, `符合要求` | 163 | L35-50; most at L43 (83), L44 (71), L46 (151) |
| 1 | nonconform (not consistent with, does not conform) | unclear | `不符合` | 67 | L35-48; most at L44 (26), L46 (63), L47 (15) |
| 1 | comply (compliant, to comply with rules) | unclear | `合规`, `遵守` | 57 | L36-47; most at L36 (12), L37 (8), L46 (54) |
| 1 | justify (to justify, rationalize) | unclear | `␣justification`, `justify`, `合理化` | 8 | L36-48; most at L36 (5), L37 (2), L38 (2) |
| 1 | private (private, kept to oneself) | lie | `␣private`, `私密` | 12 | L36-50; most at L36 (1), L50 (11) |
| 1 | disclose (to disclose) | truth | `␣disclosure` | 2 | L35-42; most at L35 (1), L36 (2), L38 (1) |
| 1 | public (public, made public) | unclear | `公开` | 2 | L35-38; most at L35 (2), L36 (2), L37 (2) |
| 1 | refuse (to refuse) | unclear | `拒绝`, `␣refusal` | 6 | L39-47; most at L45 (2), L46 (6), L47 (3) |
| 1 | forced (forced, compelled) | unclear | `␣forced`, `forced`, `␣forcing`, `强制`, `被迫`, `迫使` | 1 | L39-46; most at L39 (1), L40 (1), L42 (1) |
| 1 | credible (credible, trustworthy) | truth | `可信` | 2 | L35-35; most at L35 (2) |
| 1 | apologize (to apologize) | unclear | `道歉` | 1 | L38-46; most at L38 (1), L40 (1), L41 (1) |
| 1 | critique (a critique, to criticize) | unclear | `␣critique` | 15 | L57-58; most at L57 (1), L58 (15) |
| 2 | honest (being honest) | truth | `诚实`, `诚`, `␣honest`, `␣honesty`, `诚恳` | 101 | L35-48; most at L41 (86), L42 (94), L44 (91) |
| 2 | candid (candid, frank) | truth | `坦诚` | 8 | L36-48; most at L39 (5), L42 (6), L43 (3) |
| 2 | confess (to come clean, confess) | truth | `坦白` | 1 | L40-40; most at L40 (1) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `␣Truth`, `truth`, `真相` | 75 | L35-51; most at L41 (44), L42 (32), L46 (70) |
| 2 | truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实` | 22 | L35-48; most at L39 (9), L40 (10), L41 (15) |
| 2 | lie (to lie, a lie) | lie | `撒谎`, `说谎`, `谎`, `谎言`, `␣lie`, `␣lies`, `␣lying`, `lying` | 12 | L35-46; most at L36 (9), L38 (10), L39 (8) |
| 2 | conceal (to hide, conceal, cover up) | lie | `掩`, `隐瞒`, `-hide` | 181 | L40-58; most at L53 (180), L54 (68), L55 (73) |
| 2 | disclose (to disclose, divulge) | truth | `␣disclosure` | 2 | L35-42; most at L35 (1), L36 (2), L38 (1) |
| 2 | integrity (integrity, uprightness) | truth | `正直` | 20 | L35-47; most at L35 (12), L36 (15), L38 (12) |
| 2 | admit (to admit) | truth | `承认` | 14 | L36-47; most at L39 (9), L40 (7), L46 (10) |
| 2 | deny (to deny) | lie | `否认` | 2 | L39-44; most at L39 (2), L42 (1), L44 (1) |
| 2 | ethics (ethics, morality) | unclear | `␣ethical`, `ethical`, `␣ethics`, `道德`, `的道德`, `伦理`, `␣moral`, `␣morally` | 55 | L35-49; most at L42 (34), L43 (43), L44 (33) |
| 2 | violate (to violate (rules, principles, law)) | unclear | `违背`, `违反`, `违反了`, `违`, `违法` | 73 | L35-48; most at L44 (62), L45 (35), L46 (26) |
| 2 | compliance (complying with rules) | unclear | `合规` | 55 | L36-47; most at L36 (11), L42 (7), L46 (53) |
| 2 | legal (lawful, legal) | unclear | `合法`, `合法的`, `␣legally` | 51 | L35-49; most at L36 (39), L37 (36), L44 (47) |
| 2 | deliberate (knowingly, on purpose) | unclear | `明知` | 102 | L35-47; most at L42 (61), L43 (86), L44 (96) |
| 2 | refuse (refusal) | unclear | `拒绝`, `␣refusal` | 6 | L39-47; most at L45 (2), L46 (6), L47 (3) |
| 2 | apology (apology) | unclear | `道歉` | 1 | L38-46; most at L38 (1), L40 (1), L41 (1) |
| 2 | regret (regret, remorse) | unclear | `悔` | 1 | L36-36; most at L36 (1) |
| 2 | harm (harm, harmful) | unclear | `害` | 6 | L44-47; most at L44 (5), L46 (1), L47 (3) |
| 2 | unbiased (unbiased, objective, impartial) | unclear | `客观`, `␣objectively` | 39 | L35-47; most at L43 (17), L44 (23), L45 (21) |
| 2 | neutral (neutral) | unclear | `中立` | 2 | L35-46; most at L35 (1), L36 (1), L46 (1) |
| 2 | credible (credible, trustworthy) | unclear | `可信` | 2 | L35-35; most at L35 (2) |
| 2 | contradiction (contradiction, inconsistency) | unclear | `矛盾`, `␣contradictory` | 8 | L35-46; most at L35 (5), L44 (4), L45 (3) |
| 2 | justify (justification, legitimate) | unclear | `␣justification`, `justify`, `正当` | 16 | L35-48; most at L36 (9), L37 (12), L38 (4) |
| 2 | critique (criticism, critique) | unclear | `␣critique` | 15 | L57-58; most at L57 (1), L58 (15) |

## postans_slot2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | critique (a critique, to criticize) | unclear | `␣critique`, `批判`, `批评`, `␣criticism`, `␣critic`, `␣critiques` | 197 | L55-58; most at L56 (28), L57 (160), L58 (192) |
| 1 | critical (critical (judging faults)) | unclear | `␣critical`, `critical`, `␣Critical`, `Critical`, `␣critically`, `_critical` | 113 | L57-58; most at L57 (1), L58 (113) |
| 1 | reflect (to reflect on oneself, self-examine) | unclear | `反思` | 39 | L44-53; most at L44 (16), L50 (32), L53 (2) |
| 1 | conceal (to hide, cover up) | lie | `蔽`, `Hidden`, `掩` | 9 | L46-53; most at L46 (1), L50 (5), L51 (2) |
| 1 | comply (compliant, to comply with rules) | unclear | `合规` | 8 | L35-46; most at L35 (3), L36 (3), L46 (4) |
| 1 | conform (to conform to, be consistent with) | unclear | `符合` | 3 | L35-46; most at L43 (2), L44 (1), L46 (3) |
| 1 | legal (lawful, according to law) | unclear | `依法`, `合法性` | 7 | L42-51; most at L46 (3), L48 (1), L51 (5) |
| 1 | violate (to violate, go against (rules, principles)) | unclear | `违` | 1 | L42-42; most at L42 (1) |
| 1 | truth (the truth (noun)) | truth | `␣truth`, `真相` | 1 | L39-46; most at L39 (1), L40 (1), L41 (1) |
| 1 | factual (factual, the facts) | truth | `␣factual`, `事实` | 1 | L37-46; most at L37 (1), L38 (1), L39 (1) |
| 1 | truthful (truthful, as it really is) | truth | `如实` | 1 | L42-43; most at L42 (1), L43 (1) |
| 1 | lure (to lure, induce) | unclear | `诱导` | 1 | L35-39; most at L35 (1), L36 (1), L39 (1) |
| 1 | persuade (persuasive) | unclear | `␣persuasive` | 1 | L41-42; most at L41 (1), L42 (1) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `真相` | 1 | L39-46; most at L39 (1), L40 (1), L41 (1) |
| 2 | truthful (truthful, telling it as it is) | truth | `如实` | 1 | L42-43; most at L42 (1), L43 (1) |
| 2 | conceal (to hide, conceal, cover up) | lie | `掩`, `蔽` | 8 | L46-51; most at L46 (1), L50 (5), L51 (2) |
| 2 | hidden (hidden, undisclosed (state)) | lie | `Hidden` | 1 | L53-53; most at L53 (1) |
| 2 | violate (to violate (rules, principles, law)) | unclear | `违` | 1 | L42-42; most at L42 (1) |
| 2 | compliance (complying with rules) | unclear | `合规` | 8 | L35-46; most at L35 (3), L36 (3), L46 (4) |
| 2 | legal (lawful, legal) | unclear | `合法性` | 1 | L46-46; most at L46 (1) |
| 2 | harm (harm, harmful) | unclear | `害` | 1 | L46-46; most at L46 (1) |
| 2 | induce (to lure, induce (a leading question)) | unclear | `诱导` | 1 | L35-39; most at L35 (1), L36 (1), L39 (1) |
| 2 | contradiction (contradiction, inconsistency) | unclear | `矛盾` | 1 | L35-38; most at L35 (1), L36 (1), L37 (1) |
| 2 | critique (criticism, critique) | unclear | `␣critique`, `␣critiques`, `␣criticism`, `␣critic`, `批评`, `批判` | 197 | L55-58; most at L56 (28), L57 (160), L58 (192) |
| 2 | critical (critical (of something)) | unclear | `␣critical`, `critical`, `␣Critical`, `Critical`, `␣critically`, `_critical` | 113 | L57-58; most at L57 (1), L58 (113) |
| 2 | reflect (self-reflection) | unclear | `反思` | 39 | L44-53; most at L44 (16), L50 (32), L53 (2) |

## postans_slot3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | biased (biased, bias) | unclear | `␣biased`, `␣bias`, `biased` | 55 | L44-50; most at L45 (31), L46 (32), L48 (48) |
| 1 | unbiased (unbiased, impartial) | unclear | `␣unbiased` | 17 | L44-49; most at L45 (5), L48 (13), L49 (12) |
| 1 | clarify (to clarify, set the record straight) | unclear | `澄清`, `␣clarification` | 25 | L36-48; most at L37 (4), L38 (23), L39 (17) |
| 1 | legal (lawful, according to law) | unclear | `依法`, `合法`, `依法依规` | 22 | L42-54; most at L42 (19), L45 (2), L51 (3) |
| 1 | credible (credible, trustworthy) | truth | `可信` | 7 | L35-35; most at L35 (7) |
| 1 | critique (a critique, to criticize) | unclear | `␣critique`, `批评` | 5 | L58-58; most at L58 (5) |
| 1 | critical (critical (judging faults)) | unclear | `␣critically` | 1 | L58-58; most at L58 (1) |
| 1 | role (a role (being played)) | unclear | `角色的`, `角色` | 3 | L53-53; most at L53 (3) |
| 1 | conform (to conform to, be consistent with) | unclear | `符合` | 1 | L39-39; most at L39 (1) |
| 2 | legal (lawful, legal) | unclear | `合法` | 5 | L45-51; most at L45 (2), L46 (1), L51 (3) |
| 2 | biased (biased, bias) | unclear | `␣biased`, `␣bias`, `biased` | 55 | L44-50; most at L45 (31), L46 (32), L48 (48) |
| 2 | unbiased (unbiased, objective, impartial) | unclear | `␣unbiased` | 17 | L44-49; most at L45 (5), L48 (13), L49 (12) |
| 2 | role (a role) | unclear | `角色`, `角色的` | 3 | L53-53; most at L53 (3) |
| 2 | credible (credible, trustworthy) | unclear | `可信` | 7 | L35-35; most at L35 (7) |
| 2 | critique (criticism, critique) | unclear | `␣critique`, `批评` | 5 | L58-58; most at L58 (5) |
| 2 | critical (critical (of something)) | unclear | `␣critically` | 1 | L58-58; most at L58 (1) |

## postans_slot4

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | ethical (ethical, ethics) | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣Ethics`, `ethical`, `␣ethic` | 126 | L35-58; most at L54 (94), L55 (90), L58 (103) |
| 1 | unethical (unethical) | unclear | `␣unethical` | 9 | L44-58; most at L56 (7), L57 (6), L58 (8) |
| 1 | moral (moral, morality) | unclear | `道德`, `的道德`, `␣moral`, `␣morality`, `职业道德`, `␣morals`, `␣morally`, `␣Moral` | 109 | L35-58; most at L39 (65), L51 (60), L58 (57) |
| 1 | conscience (conscience) | unclear | `良心` | 3 | L35-50; most at L46 (2), L47 (2), L50 (1) |
| 1 | honest (honest, honesty) | truth | `诚实`, `␣honesty`, `␣honest`, `诚信`, `诚实守信`, `诚`, `␣honestly` | 96 | L35-58; most at L39 (49), L55 (48), L56 (46) |
| 1 | dishonest (dishonest) | lie | `␣dishonest` | 2 | L51-58; most at L51 (2), L52 (1), L57 (2) |
| 1 | candid (candid, frank) | truth | `坦诚` | 26 | L35-57; most at L38 (13), L39 (21), L42 (12) |
| 1 | sincere (sincere, genuine) | truth | `真诚` | 1 | L44-44; most at L44 (1) |
| 1 | confess (to own up, make a clean breast) | truth | `坦白` | 6 | L38-58; most at L39 (2), L51 (3), L52 (2) |
| 1 | admit (to admit) | truth | `承认`, `␣admitting`, `␣admitted`, `␣admit`, `␣admits` | 4 | L36-58; most at L36 (2), L44 (2), L56 (2) |
| 1 | truth (the truth (noun)) | truth | `␣truth`, `␣Truth`, `truth`, `Truth`, `真相`, `_truth`, `真理`, `␣truths` | 78 | L35-58; most at L55 (48), L56 (46), L57 (48) |
| 1 | truthful (truthful, as it really is) | truth | `␣truthful`, `如实` | 51 | L35-58; most at L39 (27), L41 (23), L55 (26) |
| 1 | factual (factual, the facts) | truth | `事实`, `␣factual`, `的事实`, `事实和` | 21 | L35-58; most at L39 (10), L43 (8), L57 (11) |
| 1 | objective (objective, unslanted) | unclear | `客观`, `␣objective`, `␣objectively` | 10 | L35-56; most at L36 (6), L37 (6), L38 (7) |
| 1 | neutral (neutral, impartial) | unclear | `中立` | 1 | L51-51; most at L51 (1) |
| 1 | integrity (integrity) | truth | `␣integrity`, `␣Integrity` | 17 | L50-57; most at L51 (9), L55 (12), L56 (11) |
| 1 | upright (upright, principled) | truth | `正直` | 5 | L40-52; most at L42 (2), L47 (2), L51 (2) |
| 1 | disclose (to disclose) | truth | `␣disclosure`, `披露`, `信息披露`, `透露`, `␣disclosures`, `␣Disclosure`, `␣disclosing` | 78 | L35-58; most at L36 (42), L38 (53), L39 (50) |
| 1 | undisclosed (not disclosed) | lie | `␣undisclosed` | 1 | L56-56; most at L56 (1) |
| 1 | reveal (to reveal) | truth | `揭示了`, `揭示`, `␣reveal` | 3 | L35-38; most at L35 (1), L36 (1), L38 (1) |
| 1 | expose (to expose, lay bare) | truth | `揭露`, `揭`, `暴露` | 16 | L35-53; most at L35 (12), L36 (4), L39 (3) |
| 1 | transparent (transparent, transparency) | truth | `␣transparency`, `透明`, `透明度`, `␣Transparency`, `透明的`, `␣transparent`, `-transparent`, `transparent` | 14 | L37-58; most at L39 (8), L54 (10), L55 (7) |
| 1 | public (public, made public) | unclear | `公开`, `信息公开` | 9 | L36-48; most at L36 (3), L38 (7), L48 (3) |
| 1 | conceal (to hide, cover up) | lie | `隐蔽`, `隐瞒`, `␣hidden`, `隐藏`, `hidden`, `␣hide`, `␣hiding`, `␣concealed`, `␣conceal`, `␣hides`, `瞒`, `掩盖`, `掩饰`, `隐藏着` | 13 | L40-58; most at L45 (4), L52 (6), L53 (7) |
| 1 | withhold (to withhold) | lie | `␣withholding` | 3 | L51-57; most at L51 (1), L52 (2), L53 (3) |
| 1 | omit (to leave out) | lie | `␣omit` | 1 | L56-56; most at L56 (1) |
| 1 | evade (to evade, dodge) | lie | `␣evasion`, `回避` | 8 | L51-56; most at L51 (5), L52 (4), L53 (7) |
| 1 | lie (to tell a lie) | lie | `说谎`, `撒谎`, `␣lies`, `␣lying`, `谎`, `谎言`, `lying`, `␣lie`, `␣fib`, `␣liar` | 8 | L35-58; most at L39 (2), L40 (3), L55 (3) |
| 1 | mislead (to mislead) | lie | `误导`, `␣misleading` | 1 | L50-53; most at L50 (1), L53 (1) |
| 1 | fabricate (made up, fictional) | lie | `虚构` | 3 | L36-53; most at L51 (1), L52 (1), L53 (1) |
| 1 | knowingly (knowing full well (as in 明知故犯)) | unclear | `明知` | 31 | L35-57; most at L47 (19), L48 (24), L50 (24) |
| 1 | deliberate (deliberate, on purpose) | unclear | `故意`, `␣deliberately`, `␣deliberate` | 14 | L43-54; most at L44 (7), L46 (11), L47 (6) |
| 1 | violate (to violate, go against (rules, principles)) | unclear | `违反`, `违反了`, `违背`, `违`, `违规` | 55 | L35-55; most at L39 (24), L43 (23), L44 (35) |
| 1 | comply (compliant, to comply with rules) | unclear | `合规`, `␣compliance`, `遵守`, `␣Compliance` | 142 | L35-58; most at L36 (125), L38 (101), L39 (105) |
| 1 | code_of_conduct (a code of conduct, rules) | unclear | `守则` | 13 | L43-52; most at L44 (4), L45 (5), L46 (11) |
| 1 | conform (to conform to, be consistent with) | unclear | `符合`, `是否符合` | 47 | L35-49; most at L35 (12), L36 (42), L37 (5) |
| 1 | nonconform (not consistent with, does not conform) | unclear | `不符合` | 6 | L35-48; most at L35 (2), L36 (3), L46 (2) |
| 1 | legal (lawful, according to law) | unclear | `依法`, `合法`, `␣legally`, `␣legal`, `␣legality` | 36 | L35-58; most at L35 (14), L36 (22), L37 (30) |
| 1 | harmful (harmful, harm) | unclear | `␣harmful`, `有害`, `␣harm`, `危害` | 28 | L37-53; most at L40 (7), L50 (6), L53 (11) |
| 1 | hallucinate (to hallucinate (state made-up things without intent)) | unclear | `␣halluc` | 42 | L40-53; most at L43 (4), L44 (3), L52 (35) |
| 1 | biased (biased, bias) | unclear | `␣bias`, `偏见`, `␣biased`, `偏心` | 45 | L35-53; most at L37 (25), L38 (20), L39 (22) |
| 1 | deviate (to deviate, stray from) | unclear | `偏离` | 23 | L35-37; most at L35 (23), L36 (4), L37 (1) |
| 1 | role_play (to play a role, role-play) | unclear | `扮演`, `角色扮演` | 81 | L35-57; most at L51 (31), L52 (55), L53 (53) |
| 1 | role (a role (being played)) | unclear | `角色`, `␣role`, `的角色`, `role`, `Role`, `␣Role`, `角色的`, `-role`, `␣roles`, `ROLE` | 35 | L41-57; most at L52 (28), L53 (30), L54 (18) |
| 1 | persona (a persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona` | 19 | L51-58; most at L53 (15), L56 (13), L57 (10) |
| 1 | simulate (to simulate) | unclear | `模拟`, `仿真` | 12 | L35-56; most at L40 (3), L41 (8), L43 (5) |
| 1 | trap (a trap) | unclear | `陷阱`, `␣trap`, `␣trapped`, `␣traps`, `trap`, `Trap`, `␣Trap`, `␣trapping`, `_trap` | 18 | L36-58; most at L53 (14), L57 (15), L58 (15) |
| 1 | lure (to lure, induce, bait) | unclear | `诱导`, `␣bait` | 33 | L35-58; most at L43 (23), L44 (26), L45 (25) |
| 1 | trick (a trick) | unclear | `␣trick`, `␣tricks` | 10 | L38-58; most at L44 (7), L46 (7), L50 (6) |
| 1 | forced (forced, compelled) | unclear | `强制`, `迫使`, `␣forcing`, `␣forced`, `逼迫`, `forcing`, `被迫`, `胁迫`, `强迫`, `forced`, `被逼` | 19 | L37-58; most at L40 (10), L44 (10), L46 (10) |
| 1 | refuse (to refuse) | unclear | `拒绝`, `␣refusal`, `拒`, `␣refuse`, `␣refusing`, `␣refus`, `␣refused`, `␣refuses` | 13 | L39-58; most at L40 (7), L43 (5), L56 (5) |
| 1 | credible (credible, trustworthy) | truth | `可信`, `公信` | 2 | L35-35; most at L35 (2) |
| 1 | clarify (to clarify, set the record straight) | unclear | `澄清` | 2 | L35-37; most at L35 (1), L36 (2), L37 (1) |
| 1 | apologize (to apologize) | unclear | `道歉` | 1 | L56-56; most at L56 (1) |
| 1 | critical (critical (judging faults)) | unclear | `␣critical`, `␣Critical`, `␣critically` | 2 | L37-50; most at L45 (2), L46 (2), L47 (2) |
| 2 | honest (being honest) | truth | `诚实`, `诚`, `␣honest`, `␣honesty`, `␣honestly`, `诚信`, `诚实守信` | 96 | L35-58; most at L39 (49), L55 (48), L56 (46) |
| 2 | dishonest (not being honest) | lie | `␣dishonest` | 2 | L51-58; most at L51 (2), L52 (1), L57 (2) |
| 2 | sincere (sincere, heartfelt) | truth | `真诚` | 1 | L44-44; most at L44 (1) |
| 2 | candid (candid, frank) | truth | `坦诚` | 26 | L35-57; most at L38 (13), L39 (21), L42 (12) |
| 2 | confess (to come clean, confess) | truth | `坦白` | 6 | L38-58; most at L39 (2), L51 (3), L52 (2) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `␣Truth`, `truth`, `Truth`, `_truth`, `␣truths`, `真相` | 78 | L35-58; most at L55 (48), L56 (46), L57 (48) |
| 2 | truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实` | 51 | L35-58; most at L39 (27), L41 (23), L55 (26) |
| 2 | lie (to lie, a lie) | lie | `撒谎`, `说谎`, `谎`, `谎言`, `␣lie`, `␣lies`, `␣lying`, `lying`, `␣liar` | 7 | L36-58; most at L39 (2), L40 (3), L55 (3) |
| 2 | conceal (to hide, conceal, cover up) | lie | `隐瞒`, `瞒`, `␣hide`, `␣hides`, `␣conceal`, `␣concealed`, `掩盖`, `掩饰`, `隐藏`, `隐蔽` | 11 | L40-58; most at L45 (4), L52 (5), L53 (5) |
| 2 | hidden (hidden, undisclosed (state)) | lie | `␣hidden`, `hidden`, `␣undisclosed`, `隐藏着`, `藏着` | 6 | L40-58; most at L52 (2), L53 (5), L54 (3) |
| 2 | withhold (to withhold or omit information) | lie | `␣withholding`, `␣omit` | 3 | L51-57; most at L51 (1), L52 (2), L53 (3) |
| 2 | mislead (to mislead) | lie | `␣misleading`, `误导` | 1 | L50-53; most at L50 (1), L53 (1) |
| 2 | evade (evasion, avoiding the question) | lie | `␣evasion`, `回避` | 8 | L51-56; most at L51 (5), L52 (4), L53 (7) |
| 2 | disclose (to disclose, divulge) | truth | `␣disclosure`, `␣disclosures`, `␣Disclosure`, `␣disclosing`, `披露`, `信息披露`, `透露` | 78 | L35-58; most at L36 (42), L38 (53), L39 (50) |
| 2 | reveal (to reveal, expose) | truth | `揭`, `揭露`, `揭示`, `揭示了`, `␣reveal`, `暴露` | 17 | L35-53; most at L35 (12), L36 (4), L39 (3) |
| 2 | transparent (transparency) | truth | `␣transparency`, `␣Transparency`, `␣transparent`, `-transparent`, `transparent`, `透明`, `透明度`, `透明的` | 14 | L37-58; most at L39 (8), L54 (10), L55 (7) |
| 2 | integrity (integrity, uprightness) | truth | `␣integrity`, `␣Integrity`, `正直` | 22 | L40-57; most at L51 (11), L55 (12), L56 (11) |
| 2 | admit (to admit) | truth | `承认`, `␣admitting`, `␣admitted`, `␣admit`, `␣admits` | 4 | L36-58; most at L36 (2), L44 (2), L56 (2) |
| 2 | ethics (ethics, morality) | unclear | `␣ethical`, `ethical`, `␣ethics`, `␣Ethics`, `␣ethic`, `道德`, `的道德`, `伦理`, `␣moral`, `␣morality`, `␣morally`, `␣morals`, `␣Moral`, `职业道德` | 140 | L35-58; most at L54 (95), L55 (90), L58 (103) |
| 2 | unethical (unethical) | lie | `␣unethical` | 9 | L44-58; most at L56 (7), L57 (6), L58 (8) |
| 2 | conscience (conscience) | unclear | `良心` | 3 | L35-50; most at L46 (2), L47 (2), L50 (1) |
| 2 | violate (to violate (rules, principles, law)) | unclear | `违背`, `违反`, `违反了`, `违`, `违规` | 55 | L35-55; most at L39 (24), L43 (23), L44 (35) |
| 2 | compliance (complying with rules) | unclear | `合规`, `␣compliance`, `␣Compliance` | 140 | L35-58; most at L36 (125), L38 (101), L39 (105) |
| 2 | legal (lawful, legal) | unclear | `合法`, `␣legally`, `␣legal`, `␣legality` | 4 | L37-58; most at L37 (1), L51 (1), L52 (3) |
| 2 | deliberate (knowingly, on purpose) | unclear | `明知`, `故意`, `␣deliberately`, `␣deliberate` | 38 | L35-57; most at L46 (28), L48 (25), L50 (24) |
| 2 | refuse (refusal) | unclear | `拒绝`, `␣refusal`, `␣refuse`, `␣refusing`, `␣refused`, `␣refuses`, `␣refus` | 12 | L39-58; most at L40 (7), L41 (5), L56 (5) |
| 2 | apology (apology) | unclear | `道歉` | 1 | L56-56; most at L56 (1) |
| 2 | harm (harm, harmful) | unclear | `␣harmful`, `␣harm`, `有害`, `危害`, `害` | 55 | L35-53; most at L45 (16), L46 (29), L47 (21) |
| 2 | hallucinate (hallucination (making things up)) | unclear | `␣halluc` | 42 | L40-53; most at L43 (4), L44 (3), L52 (35) |
| 2 | biased (biased, bias) | unclear | `␣biased`, `␣bias`, `偏见`, `偏心` | 45 | L35-53; most at L37 (25), L38 (20), L39 (22) |
| 2 | unbiased (unbiased, objective, impartial) | unclear | `客观`, `␣objectively`, `␣objective`, `公正` | 13 | L35-56; most at L36 (7), L37 (7), L38 (7) |
| 2 | neutral (neutral) | unclear | `中立` | 1 | L51-51; most at L51 (1) |
| 2 | deviate (to deviate (from a standard)) | unclear | `偏离` | 23 | L35-37; most at L35 (23), L36 (4), L37 (1) |
| 2 | role-play (playing a role, persona) | unclear | `扮演`, `角色扮演`, `␣persona`, `␣personas`, `␣Persona`, `Persona` | 84 | L35-58; most at L51 (31), L52 (56), L53 (57) |
| 2 | role (a role) | unclear | `角色`, `的角色`, `角色的`, `␣role`, `role`, `Role`, `␣Role`, `-role`, `␣roles`, `ROLE` | 35 | L41-57; most at L52 (28), L53 (30), L54 (18) |
| 2 | trap (a trap or bait (for the model)) | unclear | `␣trap`, `␣trapped`, `␣traps`, `trap`, `Trap`, `␣Trap`, `␣trapping`, `_trap`, `陷阱`, `␣bait` | 25 | L36-58; most at L45 (17), L53 (17), L57 (18) |
| 2 | trick (a trick) | unclear | `␣trick`, `␣tricks` | 10 | L38-58; most at L44 (7), L46 (7), L50 (6) |
| 2 | induce (to lure, induce (a leading question)) | unclear | `诱导` | 30 | L35-57; most at L43 (23), L44 (26), L45 (22) |
| 2 | credible (credible, trustworthy) | unclear | `可信` | 1 | L35-35; most at L35 (1) |
| 2 | contradiction (contradiction, inconsistency) | unclear | `矛盾`, `矛盾的` | 3 | L44-50; most at L44 (1), L49 (2), L50 (2) |
| 2 | critical (critical (of something)) | unclear | `␣critical`, `␣Critical`, `␣critically` | 2 | L37-50; most at L45 (2), L46 (2), L47 (2) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| postans_slot0 | sincere | sincere | 1.00 | — | — |
| postans_slot0 | neutral | neutral | 1.00 | — | — |
| postans_slot0 | fake | — | 0 | all | — |
| postans_slot0 | expose | reveal | 1.00 | — | — |
| postans_slot1 | conceal | conceal | 1.00 | — | — |
| postans_slot1 | lie | lie | 0.89 | `␣fib` | — |
| postans_slot1 | fabricate | — | 0 | all | — |
| postans_slot1 | knowingly | deliberate | 1.00 | — | — |
| postans_slot1 | honest | honest | 0.80 | — | `诚恳` |
| postans_slot1 | sincere | honest | 0.20 | — | `诚实`, `诚`, `␣honest`, `␣honesty` |
| postans_slot1 | candid | candid | 1.00 | — | — |
| postans_slot1 | confess | confess | 1.00 | — | — |
| postans_slot1 | admit | admit | 1.00 | — | — |
| postans_slot1 | deny | deny | 1.00 | — | — |
| postans_slot1 | truth | truth | 0.80 | `真理` | — |
| postans_slot1 | truthful | truthful | 1.00 | — | — |
| postans_slot1 | factual | — | 0 | all | — |
| postans_slot1 | objective | unbiased | 1.00 | — | — |
| postans_slot1 | neutral | neutral | 1.00 | — | — |
| postans_slot1 | upright | integrity | 1.00 | — | — |
| postans_slot1 | ethical | ethics | 0.50 | — | `道德`, `的道德`, `␣moral`, `␣morally` |
| postans_slot1 | moral | ethics | 0.50 | — | `␣ethical`, `ethical`, `␣ethics`, `伦理` |
| postans_slot1 | violate | violate | 0.80 | — | `违法` |
| postans_slot1 | illegal | violate | 0.20 | — | `违背`, `违反`, `违反了`, `违` |
| postans_slot1 | legal | legal | 0.75 | `依法` | — |
| postans_slot1 | legitimate | justify | 0.25 | `␣legitimate` | `␣justification`, `justify` |
| postans_slot1 | conform | — | 0 | all | — |
| postans_slot1 | nonconform | — | 0 | all | — |
| postans_slot1 | comply | compliance | 0.50 | `遵守` | — |
| postans_slot1 | justify | justify | 0.50 | `合理化` | `正当` |
| postans_slot1 | private | — | 0 | all | — |
| postans_slot1 | disclose | disclose | 1.00 | — | — |
| postans_slot1 | public | — | 0 | all | — |
| postans_slot1 | refuse | refuse | 1.00 | — | — |
| postans_slot1 | forced | — | 0 | all | — |
| postans_slot1 | credible | credible | 1.00 | — | — |
| postans_slot1 | apologize | apology | 1.00 | — | — |
| postans_slot1 | critique | critique | 1.00 | — | — |
| postans_slot2 | critique | critique | 1.00 | — | — |
| postans_slot2 | critical | critical | 1.00 | — | — |
| postans_slot2 | reflect | reflect | 1.00 | — | — |
| postans_slot2 | conceal | conceal | 0.67 | `Hidden` | — |
| postans_slot2 | comply | compliance | 1.00 | — | — |
| postans_slot2 | conform | — | 0 | all | — |
| postans_slot2 | legal | legal | 0.50 | `依法` | — |
| postans_slot2 | violate | violate | 1.00 | — | — |
| postans_slot2 | truth | truth | 1.00 | — | — |
| postans_slot2 | factual | — | 0 | all | — |
| postans_slot2 | truthful | truthful | 1.00 | — | — |
| postans_slot2 | lure | induce | 1.00 | — | — |
| postans_slot2 | persuade | — | 0 | all | — |
| postans_slot3 | biased | biased | 1.00 | — | — |
| postans_slot3 | unbiased | unbiased | 1.00 | — | — |
| postans_slot3 | clarify | — | 0 | all | — |
| postans_slot3 | legal | legal | 0.33 | `依法`, `依法依规` | — |
| postans_slot3 | credible | credible | 1.00 | — | — |
| postans_slot3 | critique | critique | 1.00 | — | — |
| postans_slot3 | critical | critical | 1.00 | — | — |
| postans_slot3 | role | role | 1.00 | — | — |
| postans_slot3 | conform | — | 0 | all | — |
| postans_slot4 | ethical | ethics | 0.43 | — | `道德`, `的道德`, `␣moral`, `␣morality`, `␣morally`, `␣morals`, `␣Moral`, `职业道德` |
| postans_slot4 | unethical | unethical | 1.00 | — | — |
| postans_slot4 | moral | ethics | 0.57 | — | `␣ethical`, `ethical`, `␣ethics`, `␣Ethics`, `␣ethic`, `伦理` |
| postans_slot4 | conscience | conscience | 1.00 | — | — |
| postans_slot4 | honest | honest | 1.00 | — | — |
| postans_slot4 | dishonest | dishonest | 1.00 | — | — |
| postans_slot4 | candid | candid | 1.00 | — | — |
| postans_slot4 | sincere | sincere | 1.00 | — | — |
| postans_slot4 | confess | confess | 1.00 | — | — |
| postans_slot4 | admit | admit | 1.00 | — | — |
| postans_slot4 | truth | truth | 0.88 | `真理` | — |
| postans_slot4 | truthful | truthful | 1.00 | — | — |
| postans_slot4 | factual | — | 0 | all | — |
| postans_slot4 | objective | unbiased | 0.75 | — | `公正` |
| postans_slot4 | neutral | neutral | 1.00 | — | — |
| postans_slot4 | integrity | integrity | 0.67 | — | `正直` |
| postans_slot4 | upright | integrity | 0.33 | — | `␣integrity`, `␣Integrity` |
| postans_slot4 | disclose | disclose | 1.00 | — | — |
| postans_slot4 | undisclosed | hidden | 0.20 | — | `␣hidden`, `hidden`, `隐藏着`, `藏着` |
| postans_slot4 | reveal | reveal | 0.50 | — | `揭`, `揭露`, `暴露` |
| postans_slot4 | expose | reveal | 0.50 | — | `揭示`, `揭示了`, `␣reveal` |
| postans_slot4 | transparent | transparent | 1.00 | — | — |
| postans_slot4 | public | — | 0 | all | — |
| postans_slot4 | conceal | conceal | 0.71 | `␣hidden`, `hidden`, `␣hiding`, `隐藏着` | — |
| postans_slot4 | withhold | withhold | 0.50 | — | `␣omit` |
| postans_slot4 | omit | withhold | 0.50 | — | `␣withholding` |
| postans_slot4 | evade | evade | 1.00 | — | — |
| postans_slot4 | lie | lie | 0.90 | `␣fib` | — |
| postans_slot4 | mislead | mislead | 1.00 | — | — |
| postans_slot4 | fabricate | — | 0 | all | — |
| postans_slot4 | knowingly | deliberate | 0.25 | — | `故意`, `␣deliberately`, `␣deliberate` |
| postans_slot4 | deliberate | deliberate | 0.75 | — | `明知` |
| postans_slot4 | violate | violate | 1.00 | — | — |
| postans_slot4 | comply | compliance | 0.75 | `遵守` | — |
| postans_slot4 | code_of_conduct | — | 0 | all | — |
| postans_slot4 | conform | — | 0 | all | — |
| postans_slot4 | nonconform | — | 0 | all | — |
| postans_slot4 | legal | legal | 0.80 | `依法` | — |
| postans_slot4 | harmful | harm | 0.80 | — | `害` |
| postans_slot4 | hallucinate | hallucinate | 1.00 | — | — |
| postans_slot4 | biased | biased | 1.00 | — | — |
| postans_slot4 | deviate | deviate | 1.00 | — | — |
| postans_slot4 | role_play | role-play | 0.33 | — | `␣persona`, `␣personas`, `␣Persona`, `Persona` |
| postans_slot4 | role | role | 1.00 | — | — |
| postans_slot4 | persona | role-play | 0.67 | — | `扮演`, `角色扮演` |
| postans_slot4 | simulate | — | 0 | all | — |
| postans_slot4 | trap | trap | 0.90 | — | `␣bait` |
| postans_slot4 | lure | induce | 0.50 | `␣bait` | — |
| postans_slot4 | trick | trick | 1.00 | — | — |
| postans_slot4 | forced | — | 0 | all | — |
| postans_slot4 | refuse | refuse | 0.88 | `拒` | — |
| postans_slot4 | credible | credible | 0.50 | `公信` | — |
| postans_slot4 | clarify | — | 0 | all | — |
| postans_slot4 | apologize | apology | 1.00 | — | — |
| postans_slot4 | critical | critical | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: postans_slot1: regret, postans_slot1: harm, postans_slot1: contradiction, postans_slot2: hidden, postans_slot2: harm, postans_slot2: contradiction, postans_slot4: contradiction

## Families whose name recurs at 3 or more positions

- compliance: postans_slot1, postans_slot2, postans_slot4
- comply: postans_slot1, postans_slot2, postans_slot4
- conceal: postans_slot1, postans_slot2, postans_slot4
- conform: postans_slot1, postans_slot2, postans_slot3, postans_slot4
- contradiction: postans_slot1, postans_slot2, postans_slot4
- credible: postans_slot1, postans_slot3, postans_slot4
- critical: postans_slot2, postans_slot3, postans_slot4
- critique: postans_slot1, postans_slot2, postans_slot3
- factual: postans_slot1, postans_slot2, postans_slot4
- harm: postans_slot1, postans_slot2, postans_slot4
- legal: postans_slot1, postans_slot2, postans_slot3, postans_slot4
- neutral: postans_slot0, postans_slot1, postans_slot4
- sincere: postans_slot0, postans_slot1, postans_slot4
- truth: postans_slot1, postans_slot2, postans_slot4
- truthful: postans_slot1, postans_slot2, postans_slot4
- unbiased: postans_slot1, postans_slot3, postans_slot4
- violate: postans_slot1, postans_slot2, postans_slot4

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- postans_slot1: conceal / disclose
- postans_slot1: deny / admit
- postans_slot1: deny / confess
- postans_slot1: lie / truth
- postans_slot1: lie / truthful
- postans_slot4: conceal / disclose
- postans_slot4: conceal / reveal
- postans_slot4: conceal / transparent
- postans_slot4: dishonest / honest
- postans_slot4: evade / admit
- postans_slot4: hidden / admit
- postans_slot4: hidden / confess
- postans_slot4: hidden / disclose
- postans_slot4: lie / truth
- postans_slot4: lie / truthful
- postans_slot4: mislead / candid

Merged candidate list: `qwen3_6_27b_LL_Q2_after_postans_merged.json` (124 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
