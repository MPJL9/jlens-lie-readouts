# Family report: qwen3.6-27b, logit lens, band 35-58, part Q7_ab, group postans

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q7_ab_postans_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## postans_slot0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | sincere (sincere, earnest) | truth | `诚挚` | 231 | L52-58; most at L52 (14), L53 (224), L54 (229) |
| 1 | fake (faking, a faker) | lie | `faker` | 230 | L35-43; most at L38 (230), L40 (133), L43 (120) |
| 1 | reveal (reveal, uncover, expose) | truth | `揭` | 84 | L36-37; most at L36 (13), L37 (84) |
| 2 | sincere (sincere, earnest) | truth | `诚挚` | 231 | L52-58; most at L52 (14), L53 (224), L54 (229) |
| 2 | fake (a faker, one who fakes) | lie | `faker` | 230 | L35-43; most at L38 (230), L40 (133), L43 (120) |
| 2 | reveal (uncover, expose) | truth | `揭` | 84 | L36-37; most at L36 (13), L37 (84) |
| 2 | solemn (solemnly, in earnest) | unclear | `郑重` | 216 | L39-44; most at L39 (171), L40 (165), L41 (198) |
| 2 | neutral (neutral stance) | unclear | `中立` | 23 | L42-43; most at L42 (9), L43 (21) |

## postans_slot1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | conceal (hide, cover up) | lie | `掩`, `-hide` | 147 | L53-58; most at L53 (144), L56 (6), L58 (7) |
| 1 | honest (honest, honesty) | truth | `诚实`, `␣honesty`, `␣honest`, `诚` | 81 | L35-49; most at L39 (71), L40 (75), L41 (74) |
| 1 | dishonest (not honest) | lie | `␣dishonest` | 1 | L35-35; most at L35 (1) |
| 1 | upright (integrity, uprightness) | truth | `正直`, `诚信` | 83 | L35-48; most at L35 (49), L36 (52), L38 (29) |
| 1 | candid (candid, frank) | truth | `坦诚` | 36 | L38-48; most at L39 (32), L42 (23), L43 (27) |
| 1 | confess (confess, own up) | truth | `坦白`, `␣confession` | 9 | L39-48; most at L39 (5), L42 (3), L48 (8) |
| 1 | admit (admit, acknowledge) | truth | `承认`, `␣acknowledge`, `␣acknowledging`, `␣acknowledgment`, `␣acknowledges` | 55 | L35-51; most at L39 (53), L40 (51), L45 (47) |
| 1 | deceive (deceive, cheat) | lie | `骗` | 9 | L36-39; most at L36 (5), L38 (8), L39 (2) |
| 1 | fib (a small lie) | lie | `␣fib` | 36 | L50-51; most at L50 (1), L51 (36) |
| 1 | knowingly (acting with knowledge) | unclear | `明知` | 39 | L35-46; most at L42 (13), L43 (30), L44 (31) |
| 1 | ethics (ethics, morality) | unclear | `道德`, `␣moral`, `␣ethical`, `伦理` | 39 | L39-49; most at L43 (22), L44 (24), L46 (30) |
| 1 | comply (compliance with rules) | unclear | `合规`, `遵守` | 93 | L35-47; most at L36 (29), L38 (23), L46 (73) |
| 1 | violate (break a rule or law) | unclear | `违反`, `违法` | 10 | L44-46; most at L44 (3), L45 (2), L46 (8) |
| 1 | objective (objective, impartial) | unclear | `客观` | 78 | L35-46; most at L43 (30), L44 (36), L45 (48) |
| 1 | shame (shame, guilt) | unclear | `愧` | 7 | L45-45; most at L45 (7) |
| 1 | critique (critique, criticism) | unclear | `␣critique` | 29 | L57-58; most at L57 (3), L58 (29) |
| 2 | hide (cover up, hide) | lie | `掩`, `藏`, `-hide` | 153 | L35-58; most at L35 (8), L53 (144), L58 (7) |
| 2 | deceive (the act of deceiving) | lie | `骗` | 9 | L36-39; most at L36 (5), L38 (8), L39 (2) |
| 2 | fib (a small lie) | lie | `␣fib` | 36 | L50-51; most at L50 (1), L51 (36) |
| 2 | honest (being honest) | truth | `诚实`, `诚`, `␣honesty`, `␣honest`, `诚信` | 81 | L35-49; most at L39 (71), L40 (75), L41 (74) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 1 | L35-35; most at L35 (1) |
| 2 | candid (frank, candid) | truth | `坦诚` | 36 | L38-48; most at L39 (32), L42 (23), L43 (27) |
| 2 | confess (own up, confess) | truth | `坦白`, `␣confession` | 9 | L39-48; most at L39 (5), L42 (3), L48 (8) |
| 2 | admit (admit, acknowledge) | truth | `承认`, `␣acknowledge`, `␣acknowledging`, `␣acknowledgment`, `␣acknowledges` | 55 | L35-51; most at L39 (53), L40 (51), L45 (47) |
| 2 | upright (upright, of integrity) | truth | `正直` | 83 | L35-48; most at L35 (49), L36 (52), L38 (29) |
| 2 | faithful (faithful to the facts) | truth | `忠实` | 4 | L38-45; most at L38 (2), L45 (2) |
| 2 | moral (morality) | unclear | `道德`, `␣moral` | 37 | L39-48; most at L43 (19), L44 (24), L46 (30) |
| 2 | ethical (ethics, ethical) | unclear | `␣ethical`, `伦理` | 13 | L39-49; most at L41 (6), L42 (3), L43 (8) |
| 2 | right and wrong (right and wrong (moral judgement)) | unclear | `是非` | 3 | L35-46; most at L36 (2), L39 (1), L46 (1) |
| 2 | lawful (lawful, legal) | unclear | `合法`, `合法的` | 100 | L35-49; most at L36 (80), L37 (67), L44 (83) |
| 2 | compliant (compliant with rules) | unclear | `合规` | 79 | L36-47; most at L36 (12), L42 (15), L46 (73) |
| 2 | violate (violate rules) | unclear | `违反`, `违法` | 10 | L44-46; most at L44 (3), L45 (2), L46 (8) |
| 2 | knowingly (knowingly, in full awareness) | unclear | `明知` | 39 | L35-46; most at L42 (13), L43 (30), L44 (31) |
| 2 | apologize (apologize) | unclear | `道歉` | 11 | L42-48; most at L42 (5), L45 (4), L46 (9) |
| 2 | ashamed (shame, being ashamed) | unclear | `愧` | 7 | L45-45; most at L45 (7) |
| 2 | regret (regret, repent) | unclear | `悔` | 3 | L35-42; most at L35 (1), L36 (3), L41 (1) |
| 2 | conscience (conscience) | unclear | `良心` | 4 | L42-43; most at L42 (1), L43 (4) |
| 2 | objective (objective, impartial) | unclear | `客观` | 78 | L35-46; most at L43 (30), L44 (36), L45 (48) |
| 2 | disclose (disclose) | truth | `␣disclosure` | 1 | L38-42; most at L38 (1), L39 (1), L40 (1) |
| 2 | coerce (forced, compelled) | unclear | `迫` | 4 | L41-46; most at L41 (2), L43 (1), L46 (3) |
| 2 | private (private, not public) | unclear | `␣private` | 11 | L35-50; most at L44 (1), L45 (1), L50 (10) |

## postans_slot2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | critique (critique, criticism) | unclear | `␣critique`, `␣critical`, `批判`, `critical`, `␣Critical`, `␣critically`, `批评`, `Critical`, `␣criticism`, `␣critic`, `␣critiques` | 216 | L55-58; most at L56 (14), L57 (193), L58 (216) |
| 1 | reflect (self-reflection) | unclear | `反思` | 19 | L44-50; most at L44 (3), L50 (18) |
| 1 | comply (compliance with rules) | unclear | `合规` | 10 | L36-46; most at L39 (7), L43 (3), L46 (2) |
| 2 | compliant (compliant with rules) | unclear | `合规` | 10 | L36-46; most at L39 (7), L43 (3), L46 (2) |
| 2 | reflect (self-reflection) | unclear | `反思` | 19 | L44-50; most at L44 (3), L50 (18) |

## postans_slot3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | critique (critique, criticism) | unclear | `批评`, `␣critically`, `␣critique`, `␣criticism`, `_critical`, `␣critical`, `Critical`, `␣critic`, `批判`, `␣Critical`, `␣criticisms`, `␣critica`, `critical`, `␣criticize`, `批評` | 49 | L57-58; most at L57 (11), L58 (49) |
| 1 | bias (biased, bias) | unclear | `␣biased`, `biased`, `bias` | 39 | L48-57; most at L48 (34), L49 (16), L57 (2) |
| 1 | unbiased (free of bias) | unclear | `␣unbiased` | 24 | L44-49; most at L44 (6), L45 (13), L49 (7) |
| 1 | reveal (reveal, uncover, expose) | truth | `揭` | 3 | L37-40; most at L37 (2), L40 (1) |
| 1 | violate (break a rule or law) | unclear | `违规` | 5 | L39-39; most at L39 (5) |
| 1 | comply (compliance with rules) | unclear | `遵守` | 1 | L47-47; most at L47 (1) |
| 1 | suspected (suspected of wrongdoing) | unclear | `涉嫌` | 13 | L35-36; most at L35 (13), L36 (2) |
| 2 | biased (biased) | unclear | `␣biased`, `biased`, `bias` | 39 | L48-57; most at L48 (34), L49 (16), L57 (2) |
| 2 | unbiased (unbiased) | unclear | `␣unbiased` | 24 | L44-49; most at L44 (6), L45 (13), L49 (7) |
| 2 | apologize (apologize) | unclear | `道歉`, `␣apology` | 8 | L55-56; most at L55 (8), L56 (2) |
| 2 | suspected (suspected of wrongdoing) | unclear | `涉嫌` | 13 | L35-36; most at L35 (13), L36 (2) |
| 2 | violate (violate rules) | unclear | `违规` | 5 | L39-39; most at L39 (5) |
| 2 | reveal (uncover, expose) | truth | `揭` | 3 | L37-40; most at L37 (2), L40 (1) |
| 2 | sly (cunning, sly) | lie | `狡` | 1 | L35-35; most at L35 (1) |
| 2 | harm (harm) | unclear | `␣harm` | 5 | L45-46; most at L45 (4), L46 (2) |
| 2 | unfair (unfair) | unclear | `不公平` | 3 | L49-50; most at L49 (2), L50 (2) |

## postans_slot4

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | ethics (ethics, morality) | unclear | `道德`, `␣ethical`, `␣ethics`, `伦理`, `的道德`, `␣moral`, `␣Ethics`, `ethical`, `␣morality`, `职业道德`, `␣morally`, `␣Moral`, `␣morals`, `␣ethic` | 159 | L35-58; most at L51 (130), L54 (132), L58 (128) |
| 1 | unethical (not ethical) | unclear | `␣unethical` | 19 | L50-58; most at L53 (10), L56 (11), L58 (11) |
| 1 | comply (compliance with rules) | unclear | `合规`, `␣compliance`, `遵守`, `␣Compliance`, `␣compliant`, `严格遵守` | 198 | L35-58; most at L36 (172), L38 (180), L39 (160) |
| 1 | violate (break a rule or law) | unclear | `违`, `违反`, `违背`, `违规`, `违反了`, `␣violate`, `违法` | 119 | L35-53; most at L37 (50), L38 (88), L39 (94) |
| 1 | honest (honest, honesty) | truth | `诚实`, `␣honesty`, `␣honest`, `诚`, `␣honestly`, `␣Honest`, `誠` | 129 | L35-58; most at L55 (96), L56 (99), L57 (86) |
| 1 | integrity (integrity, good faith) | truth | `␣integrity`, `诚信`, `诚实守信`, `␣Integrity`, `正直` | 98 | L35-58; most at L51 (62), L55 (74), L56 (74) |
| 1 | dishonest (not honest) | lie | `␣dishonest` | 24 | L51-58; most at L51 (17), L57 (14), L58 (11) |
| 1 | candid (candid, frank) | truth | `坦诚` | 23 | L38-58; most at L39 (11), L40 (10), L42 (12) |
| 1 | confess (confess, own up) | truth | `坦白`, `␣confession`, `␣confess` | 7 | L39-58; most at L51 (4), L52 (4), L57 (5) |
| 1 | admit (admit, acknowledge) | truth | `承认`, `␣admitting`, `␣admit`, `␣admits`, `␣admitted`, `␣acknowledge`, `␣acknowledging`, `␣acknowledges`, `␣admite`, `␣acknowledgment`, `␣acknowledged` | 16 | L36-58; most at L40 (10), L55 (11), L56 (11) |
| 1 | disclose (disclose, make public) | truth | `␣disclosure`, `公开`, `披露`, `␣disclosures`, `信息披露` | 82 | L36-53; most at L37 (44), L38 (61), L39 (54) |
| 1 | reveal (reveal, uncover, expose) | truth | `揭`, `透露`, `揭露`, `暴露`, `揭示了`, `揭示`, `␣reveal` | 12 | L35-58; most at L35 (4), L51 (3), L52 (3) |
| 1 | transparent (transparency) | truth | `␣transparency`, `␣transparent`, `透明`, `透明的`, `透明度` | 7 | L38-57; most at L38 (1), L54 (5), L56 (2) |
| 1 | deceive (the act of deceiving) | lie | `␣deception`, `欺骗`, `␣deceptive`, `骗`, `␣deceit`, `␣deceive` | 43 | L39-58; most at L52 (28), L53 (25), L54 (26) |
| 1 | fraud (fraud, swindle) | lie | `欺诈` | 1 | L57-57; most at L57 (1) |
| 1 | mislead (mislead) | lie | `误导` | 1 | L50-58; most at L50 (1), L51 (1), L52 (1) |
| 1 | conceal (hide, cover up, hidden) | lie | `隐瞒`, `隐蔽`, `␣conceal`, `␣hidden` | 15 | L38-58; most at L40 (9), L50 (3), L53 (6) |
| 1 | fabricate (fabricate, make up, falsify) | lie | `虚构`, `␣fabricated`, `␣fabrication`, `造假` | 5 | L42-58; most at L44 (2), L45 (2), L53 (3) |
| 1 | manipulate (manipulate) | lie | `␣manipulation`, `␣manipulated`, `操纵`, `␣manipulating` | 4 | L54-57; most at L54 (4), L56 (3), L57 (1) |
| 1 | evasion (evade, avoid answering) | lie | `␣evasion` | 4 | L52-55; most at L52 (3), L53 (4), L54 (1) |
| 1 | fib (a small lie) | lie | `␣fib` | 5 | L35-36; most at L35 (4), L36 (3) |
| 1 | hallucinate (produce false content unintentionally) | unclear | `␣halluc` | 62 | L40-58; most at L52 (60), L53 (26), L57 (6) |
| 1 | trap (trap, trick question) | unclear | `陷阱`, `trap`, `␣trap`, `␣traps`, `Trap`, `␣Trap`, `␣trapped`, `␣trapping`, `_trap` | 52 | L36-58; most at L53 (30), L57 (30), L58 (33) |
| 1 | lure (bait, lure, induce) | unclear | `诱导`, `␣bait`, `诱`, `␣lure`, `诱惑`, `引诱` | 61 | L36-58; most at L42 (36), L43 (38), L44 (40) |
| 1 | coerce (force, coerce) | unclear | `迫使`, `␣forcing`, `␣forced`, `逼迫`, `forcing`, `被迫`, `强制`, `forced`, `强迫`, `␣Forced`, `胁迫`, `␣coerc`, `␣coercion`, `压迫` | 58 | L37-58; most at L51 (21), L53 (22), L54 (42) |
| 1 | role-play (playing a role) | unclear | `扮演`, `角色扮演` | 33 | L36-56; most at L51 (8), L52 (23), L53 (23) |
| 1 | knowingly (acting with knowledge) | unclear | `明知`, `␣knowingly` | 84 | L35-53; most at L47 (43), L48 (51), L50 (53) |
| 1 | intentional (deliberately) | unclear | `故意` | 10 | L44-54; most at L44 (7), L46 (6), L47 (4) |
| 1 | bias (biased, bias) | unclear | `␣bias`, `␣biased` | 29 | L35-53; most at L35 (23), L37 (10), L38 (10) |
| 1 | objective (objective, impartial) | unclear | `客观`, `␣objective`, `␣objectively` | 14 | L36-58; most at L36 (7), L43 (8), L44 (8) |
| 2 | moral (morality) | unclear | `道德`, `的道德`, `␣moral`, `␣morality`, `职业道德`, `␣morally`, `␣Moral`, `␣morals` | 152 | L35-58; most at L51 (123), L53 (107), L54 (120) |
| 2 | ethical (ethics, ethical) | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣Ethics`, `ethical`, `␣ethic` | 146 | L35-58; most at L54 (124), L55 (117), L58 (122) |
| 2 | unethical (unethical) | lie | `␣unethical` | 19 | L50-58; most at L53 (10), L56 (11), L58 (11) |
| 2 | right and wrong (right and wrong (moral judgement)) | unclear | `是非` | 206 | L35-54; most at L42 (149), L43 (152), L44 (123) |
| 2 | compliant (compliant with rules) | unclear | `合规`, `␣compliance`, `␣Compliance`, `␣compliant` | 197 | L35-58; most at L36 (172), L38 (180), L39 (160) |
| 2 | lawful (lawful, legal) | unclear | `合法` | 2 | L38-53; most at L38 (1), L53 (1) |
| 2 | honest (being honest) | truth | `诚实`, `␣honesty`, `诚信`, `诚实守信`, `␣honest`, `诚`, `誠`, `␣honestly`, `␣Honest` | 131 | L35-58; most at L55 (96), L56 (99), L57 (86) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 24 | L51-58; most at L51 (17), L57 (14), L58 (11) |
| 2 | candid (frank, candid) | truth | `坦诚` | 23 | L38-58; most at L39 (11), L40 (10), L42 (12) |
| 2 | confess (own up, confess) | truth | `坦白`, `␣confession`, `␣confess` | 7 | L39-58; most at L51 (4), L52 (4), L57 (5) |
| 2 | admit (admit, acknowledge) | truth | `承认`, `␣admitting`, `␣admit`, `␣admits`, `␣admitted`, `␣admite`, `␣acknowledge`, `␣acknowledging`, `␣acknowledges`, `␣acknowledgment`, `␣acknowledged` | 16 | L36-58; most at L40 (10), L55 (11), L56 (11) |
| 2 | integrity (integrity) | truth | `␣integrity`, `␣Integrity` | 72 | L50-58; most at L54 (53), L55 (60), L56 (54) |
| 2 | upright (upright, of integrity) | truth | `正直` | 2 | L42-47; most at L42 (1), L43 (1), L46 (1) |
| 2 | faithful (faithful to the facts) | truth | `忠实` | 1 | L38-38; most at L38 (1) |
| 2 | seek truth from facts (being realistic, true to the facts) | truth | `实事求是`, `求实` | 10 | L35-57; most at L35 (2), L39 (4), L56 (2) |
| 2 | violate (violate rules) | unclear | `违`, `违反`, `违背`, `违规`, `违反了`, `␣violate`, `违法` | 119 | L35-53; most at L37 (50), L38 (88), L39 (94) |
| 2 | knowingly (knowingly, in full awareness) | unclear | `明知`, `␣knowingly` | 84 | L35-53; most at L47 (43), L48 (51), L50 (53) |
| 2 | deliberate (on purpose) | unclear | `故意`, `␣deliberately`, `␣deliberate`, `␣intentionally`, `刻意` | 16 | L44-54; most at L44 (7), L46 (8), L51 (6) |
| 2 | disclose (disclose, make known) | truth | `␣disclosure`, `␣disclosures`, `披露`, `信息披露`, `透露`, `公开` | 82 | L36-58; most at L37 (44), L38 (61), L39 (54) |
| 2 | reveal (uncover, expose) | truth | `揭`, `揭露`, `揭示了`, `揭示`, `␣reveal`, `暴露` | 9 | L35-55; most at L35 (4), L46 (2), L51 (3) |
| 2 | transparent (transparency) | truth | `␣transparency`, `␣transparent`, `透明`, `透明的`, `透明度` | 7 | L38-57; most at L38 (1), L54 (5), L56 (2) |
| 2 | deceive (the act of deceiving) | lie | `␣deception`, `欺骗`, `␣deceptive`, `骗`, `␣deceit`, `␣deceive` | 43 | L39-58; most at L52 (28), L53 (25), L54 (26) |
| 2 | mislead (mislead) | lie | `误导` | 1 | L50-58; most at L50 (1), L51 (1), L52 (1) |
| 2 | fraud (fraud) | lie | `␣fraud`, `␣fraudulent`, `欺诈` | 4 | L51-58; most at L51 (3), L53 (1), L57 (2) |
| 2 | fabricate (make up, falsify) | lie | `␣fabricated`, `␣fabrication`, `虚构`, `伪造`, `造假` | 5 | L42-58; most at L43 (2), L44 (2), L53 (3) |
| 2 | conceal (conceal) | lie | `隐瞒`, `␣conceal` | 9 | L38-58; most at L40 (4), L50 (3), L53 (5) |
| 2 | hidden (hidden, covert) | lie | `隐蔽`, `␣hidden` | 6 | L40-53; most at L40 (5), L44 (1), L45 (1) |
| 2 | fib (a small lie) | lie | `␣fib` | 5 | L35-36; most at L35 (4), L36 (3) |
| 2 | coax (coax, fool someone) | lie | `哄` | 10 | L36-58; most at L39 (8), L41 (5), L42 (4) |
| 2 | manipulate (manipulate) | lie | `␣manipulation`, `␣manipulated`, `␣manipulating` | 4 | L54-57; most at L54 (4), L56 (3), L57 (1) |
| 2 | evasion (evade) | lie | `␣evasion` | 4 | L52-55; most at L52 (3), L53 (4), L54 (1) |
| 2 | refusal (refusal) | unclear | `␣refusal` | 2 | L52-57; most at L52 (1), L53 (1), L57 (2) |
| 2 | deny (deny, denial) | lie | `␣denial`, `␣deny`, `deny`, `␣denying` | 1 | L55-58; most at L55 (1), L56 (1), L57 (1) |
| 2 | hallucinate (hallucinate, make things up by error) | unclear | `␣halluc` | 62 | L40-58; most at L52 (60), L53 (26), L57 (6) |
| 2 | trap (a trap, being trapped) | unclear | `陷阱`, `trap`, `␣trap`, `␣traps`, `Trap`, `␣Trap`, `␣trapped`, `␣trapping`, `_trap` | 52 | L36-58; most at L53 (30), L57 (30), L58 (33) |
| 2 | trick (a trick) | unclear | `␣trick`, `␣tricks`, `␣Trick`, `套路` | 14 | L40-58; most at L53 (8), L57 (9), L58 (7) |
| 2 | lure (lure, bait) | unclear | `␣bait`, `␣lure`, `诱`, `引诱`, `诱惑` | 34 | L36-58; most at L51 (26), L53 (28), L54 (23) |
| 2 | induce (induce, lead someone into) | unclear | `诱导` | 52 | L36-57; most at L42 (36), L43 (37), L44 (37) |
| 2 | coerce (forced, compelled) | unclear | `迫使`, `迫`, `逼`, `强制`, `逼迫`, `␣forcing`, `␣forced`, `forcing`, `被迫`, `forced`, `强迫`, `␣Forced`, `胁迫`, `逼人`, `force`, `倒逼`, `forcer`, `压迫`, `被逼`, `FORCE`, `␣coerc`, `␣coercion` | 61 | L37-58; most at L47 (24), L51 (27), L54 (45) |
| 2 | pressure (pressure) | unclear | `压力`, `␣pressure`, `␣pressures`, `␣Pressure`, `pressure`, `Pressure`, `␣pressured` | 15 | L38-58; most at L44 (7), L46 (8), L54 (11) |
| 2 | harmful (harm, harmful) | unclear | `有害`, `␣harm`, `␣harmful` | 17 | L44-53; most at L44 (4), L52 (6), L53 (12) |
| 2 | bias (bias) | unclear | `␣bias`, `␣biased` | 29 | L35-53; most at L35 (23), L37 (10), L38 (10) |
| 2 | objective (objective, impartial) | unclear | `客观`, `␣objective`, `␣objectively` | 14 | L36-58; most at L36 (7), L43 (8), L44 (8) |
| 2 | fair (fair, just) | unclear | `公平`, `公正` | 2 | L35-51; most at L35 (1), L50 (1), L51 (1) |
| 2 | sly (cunning, sly) | lie | `狡` | 1 | L51-51; most at L51 (1) |
| 2 | conscience (conscience) | unclear | `良心` | 4 | L35-51; most at L35 (2), L36 (1), L46 (1) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| postans_slot0 | sincere | sincere | 1.00 | — | — |
| postans_slot0 | fake | fake | 1.00 | — | — |
| postans_slot0 | reveal | reveal | 1.00 | — | — |
| postans_slot1 | conceal | hide | 0.67 | — | `藏` |
| postans_slot1 | honest | honest | 0.80 | — | `诚信` |
| postans_slot1 | dishonest | dishonest | 1.00 | — | — |
| postans_slot1 | upright | upright | 0.50 | `诚信` | — |
| postans_slot1 | candid | candid | 1.00 | — | — |
| postans_slot1 | confess | confess | 1.00 | — | — |
| postans_slot1 | admit | admit | 1.00 | — | — |
| postans_slot1 | deceive | deceive | 1.00 | — | — |
| postans_slot1 | fib | fib | 1.00 | — | — |
| postans_slot1 | knowingly | knowingly | 1.00 | — | — |
| postans_slot1 | ethics | moral | 0.50 | `␣ethical`, `伦理` | — |
| postans_slot1 | comply | compliant | 0.50 | `遵守` | — |
| postans_slot1 | violate | violate | 1.00 | — | — |
| postans_slot1 | objective | objective | 1.00 | — | — |
| postans_slot1 | shame | ashamed | 1.00 | — | — |
| postans_slot1 | critique | — | 0 | all | — |
| postans_slot2 | critique | — | 0 | all | — |
| postans_slot2 | reflect | reflect | 1.00 | — | — |
| postans_slot2 | comply | compliant | 1.00 | — | — |
| postans_slot3 | critique | — | 0 | all | — |
| postans_slot3 | bias | biased | 1.00 | — | — |
| postans_slot3 | unbiased | unbiased | 1.00 | — | — |
| postans_slot3 | reveal | reveal | 1.00 | — | — |
| postans_slot3 | violate | violate | 1.00 | — | — |
| postans_slot3 | comply | — | 0 | all | — |
| postans_slot3 | suspected | suspected | 1.00 | — | — |
| postans_slot4 | ethics | moral | 0.57 | `␣ethical`, `␣ethics`, `伦理`, `␣Ethics`, `ethical`, `␣ethic` | — |
| postans_slot4 | unethical | unethical | 1.00 | — | — |
| postans_slot4 | comply | compliant | 0.67 | `遵守`, `严格遵守` | — |
| postans_slot4 | violate | violate | 1.00 | — | — |
| postans_slot4 | honest | honest | 0.78 | — | `诚信`, `诚实守信` |
| postans_slot4 | integrity | integrity | 0.40 | `诚信`, `诚实守信`, `正直` | — |
| postans_slot4 | dishonest | dishonest | 1.00 | — | — |
| postans_slot4 | candid | candid | 1.00 | — | — |
| postans_slot4 | confess | confess | 1.00 | — | — |
| postans_slot4 | admit | admit | 1.00 | — | — |
| postans_slot4 | disclose | disclose | 0.83 | — | `透露` |
| postans_slot4 | reveal | reveal | 0.86 | `透露` | — |
| postans_slot4 | transparent | transparent | 1.00 | — | — |
| postans_slot4 | deceive | deceive | 1.00 | — | — |
| postans_slot4 | fraud | fraud | 0.33 | — | `␣fraud`, `␣fraudulent` |
| postans_slot4 | mislead | mislead | 1.00 | — | — |
| postans_slot4 | conceal | conceal | 0.50 | `隐蔽`, `␣hidden` | — |
| postans_slot4 | fabricate | fabricate | 0.80 | — | `伪造` |
| postans_slot4 | manipulate | manipulate | 0.75 | `操纵` | — |
| postans_slot4 | evasion | evasion | 1.00 | — | — |
| postans_slot4 | fib | fib | 1.00 | — | — |
| postans_slot4 | hallucinate | hallucinate | 1.00 | — | — |
| postans_slot4 | trap | trap | 1.00 | — | — |
| postans_slot4 | lure | lure | 0.83 | `诱导` | — |
| postans_slot4 | coerce | coerce | 0.64 | — | `迫`, `逼`, `逼人`, `force`, `倒逼`, `forcer`, `被逼`, `FORCE` |
| postans_slot4 | role-play | — | 0 | all | — |
| postans_slot4 | knowingly | knowingly | 1.00 | — | — |
| postans_slot4 | intentional | deliberate | 0.20 | — | `␣deliberately`, `␣deliberate`, `␣intentionally`, `刻意` |
| postans_slot4 | bias | bias | 1.00 | — | — |
| postans_slot4 | objective | objective | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: postans_slot0: solemn, postans_slot0: neutral, postans_slot1: faithful, postans_slot1: ethical, postans_slot1: right and wrong, postans_slot1: lawful, postans_slot1: apologize, postans_slot1: regret, postans_slot1: conscience, postans_slot1: disclose, postans_slot1: coerce, postans_slot1: private, postans_slot3: apologize, postans_slot3: sly, postans_slot3: harm, postans_slot3: unfair, postans_slot4: ethical, postans_slot4: right and wrong, postans_slot4: lawful, postans_slot4: upright, postans_slot4: faithful, postans_slot4: seek truth from facts, postans_slot4: hidden, postans_slot4: coax, postans_slot4: refusal, postans_slot4: deny, postans_slot4: trick, postans_slot4: induce, postans_slot4: pressure, postans_slot4: harmful, postans_slot4: fair, postans_slot4: sly, postans_slot4: conscience

## Families whose name recurs at 3 or more positions

- compliant: postans_slot1, postans_slot2, postans_slot4
- comply: postans_slot1, postans_slot2, postans_slot3, postans_slot4
- critique: postans_slot1, postans_slot2, postans_slot3
- reveal: postans_slot0, postans_slot3, postans_slot4
- violate: postans_slot1, postans_slot3, postans_slot4

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- postans_slot1: conceal / disclose
- postans_slot1: deceive / honest
- postans_slot1: dishonest / honest
- postans_slot4: conceal / admit
- postans_slot4: conceal / confess
- postans_slot4: conceal / disclose
- postans_slot4: conceal / reveal
- postans_slot4: conceal / transparent
- postans_slot4: deceive / honest
- postans_slot4: deny / admit
- postans_slot4: deny / confess
- postans_slot4: dishonest / honest
- postans_slot4: evasion / admit
- postans_slot4: fib / seek truth from facts
- postans_slot4: hidden / admit
- postans_slot4: hidden / confess
- postans_slot4: hidden / disclose
- postans_slot4: hidden / transparent
- postans_slot4: mislead / candid

Merged candidate list: `qwen3_6_27b_LL_Q7_ab_postans_merged.json` (95 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
