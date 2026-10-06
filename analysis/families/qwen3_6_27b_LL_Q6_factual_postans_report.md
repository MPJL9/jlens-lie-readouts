# Family report: qwen3.6-27b, logit lens, band 35-58, part Q6_factual, group postans

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q6_factual_postans_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## postans_slot0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | sincere (sincere, earnest) | truth | `诚挚` | 194 | L52-58; most at L53 (182), L54 (187), L58 (7) |
| 1 | fake (one who fakes) | lie | `faker` | 127 | L38-50; most at L38 (114), L40 (41), L43 (56) |
| 1 | doubt (doubt, suspicion) | unclear | `疑` | 39 | L35-40; most at L35 (3), L36 (2), L40 (36) |
| 1 | hide (hiding, concealing) | lie | `-hide` | 2 | L56-56; most at L56 (2) |
| 2 | sincere (sincere, earnest) | truth | `诚挚` | 194 | L52-58; most at L53 (182), L54 (187), L58 (7) |
| 2 | neutral (neutral) | unclear | `中立` | 93 | L42-43; most at L42 (16), L43 (91) |
| 2 | joke (joking) | unclear | `玩笑` | 43 | L52-53; most at L52 (10), L53 (42) |
| 2 | responsibility (responsibility, liability) | unclear | `负责任` | 5 | L41-44; most at L41 (1), L42 (3), L44 (1) |
| 2 | hide (hiding or covering something) | lie | `-hide` | 2 | L56-56; most at L56 (2) |

## postans_slot1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `说谎`, `谎言`, `撒谎`, `␣lie`, `␣lying`, `谎`, `lying`, `␣fib` | 100 | L35-51; most at L39 (27), L40 (23), L51 (84) |
| 1 | deceive (the act of deceiving) | lie | `骗`, `欺骗`, `␣deception` | 7 | L36-40; most at L38 (4), L39 (5), L40 (3) |
| 1 | hide (hiding, concealing) | lie | `掩`, `隐瞒`, `-hide`, `Hidden` | 188 | L39-58; most at L53 (184), L54 (46), L55 (40) |
| 1 | fabricate (made up, fictional) | lie | `虚构` | 10 | L39-46; most at L44 (10), L45 (3), L46 (5) |
| 1 | hypocrisy (hypocritical, insincere) | lie | `虚伪` | 1 | L40-40; most at L40 (1) |
| 1 | dishonest (dishonest) | lie | `␣dishonest` | 2 | L36-41; most at L36 (1), L40 (2), L41 (1) |
| 1 | honest (honest, candid) | truth | `诚实`, `诚`, `如实`, `坦诚`, `␣honest`, `␣honesty`, `诚信`, `诚恳` | 79 | L35-48; most at L40 (63), L41 (57), L42 (62) |
| 1 | truthful (truthful) | truth | `␣truthful` | 76 | L35-48; most at L39 (45), L41 (71), L43 (41) |
| 1 | truth (the truth) | truth | `␣truth`, `␣Truth`, `truth`, `真相` | 131 | L35-48; most at L41 (100), L43 (101), L46 (130) |
| 1 | admit (admitting) | truth | `承认` | 10 | L37-48; most at L42 (8), L46 (8), L47 (9) |
| 1 | disclose (disclosing, making public) | truth | `公开`, `␣disclosure` | 4 | L35-40; most at L35 (3), L36 (2), L37 (2) |
| 1 | knowingly (doing it knowingly, on purpose) | unclear | `明知` | 108 | L35-48; most at L42 (75), L43 (102), L44 (101) |
| 1 | violate (violating a rule or principle) | unclear | `违背`, `违反`, `违反了` | 42 | L35-47; most at L35 (15), L44 (27), L45 (13) |
| 1 | illegal (breaking the law) | unclear | `违法` | 9 | L42-46; most at L44 (7), L45 (8), L46 (6) |
| 1 | legal (lawful, by law) | unclear | `合法`, `依法`, `␣legally`, `合法的` | 39 | L35-48; most at L36 (23), L37 (14), L44 (25) |
| 1 | compliance (complying with rules) | unclear | `合规`, `遵循` | 24 | L36-46; most at L36 (2), L38 (2), L46 (22) |
| 1 | ethics (ethics, morality) | unclear | `道德`, `␣moral`, `␣ethical`, `伦理`, `␣morally` | 11 | L36-46; most at L43 (8), L44 (10), L46 (9) |
| 1 | contradiction (contradiction, paradox) | unclear | `矛盾`, `␣paradox`, `␣contradict`, `␣contradiction`, `␣contradictory`, `矛盾的` | 18 | L35-50; most at L35 (12), L43 (9), L44 (8) |
| 1 | consistent (consistent with, conforming to) | unclear | `符合`, `是否符合`, `符合要求` | 95 | L35-50; most at L41 (61), L43 (66), L46 (83) |
| 1 | inconsistent (not consistent with) | unclear | `不符合` | 36 | L35-48; most at L37 (7), L44 (11), L46 (31) |
| 1 | fact (fact, factual) | unclear | `␣factual`, `事实`, `␣fact`, `␣facts`, `␣Fact`, `事实上`, `的事实`, `事实和` | 116 | L35-48; most at L41 (96), L43 (87), L46 (102) |
| 1 | objective (objective, impartial) | unclear | `客观` | 42 | L35-46; most at L43 (21), L44 (21), L45 (20) |
| 1 | good_intent (good intentions) | unclear | `好心` | 26 | L53-54; most at L53 (26), L54 (1) |
| 1 | coercion (being forced) | unclear | `迫`, `␣force`, `␣forced`, `␣forcing`, `逼`, `迫使` | 4 | L38-48; most at L38 (3), L46 (3), L48 (2) |
| 1 | indirect (indirect, roundabout) | unclear | `␣indirectly`, `间接` | 6 | L35-35; most at L35 (6) |
| 1 | trapped (falling into a trap) | unclear | `陷入` | 1 | L39-39; most at L39 (1) |
| 2 | hide (hiding or covering something) | lie | `掩`, `-hide`, `Hidden`, `隐瞒` | 188 | L39-58; most at L53 (184), L54 (46), L55 (40) |
| 2 | lie (telling a lie) | lie | `说谎`, `谎言`, `撒谎`, `␣lie`, `␣lying`, `谎`, `lying` | 35 | L35-46; most at L36 (16), L39 (27), L40 (23) |
| 2 | deceive (the act of deceiving) | lie | `骗`, `欺骗`, `␣deception` | 7 | L36-40; most at L38 (4), L39 (5), L40 (3) |
| 2 | fabricate (making something up) | lie | `虚构` | 10 | L39-46; most at L44 (10), L45 (3), L46 (5) |
| 2 | hypocrisy (hypocritical, insincere) | lie | `虚伪` | 1 | L40-40; most at L40 (1) |
| 2 | dishonest (not honest) | lie | `␣dishonest` | 2 | L36-41; most at L36 (1), L40 (2), L41 (1) |
| 2 | honest (being honest) | truth | `诚实`, `诚`, `␣honest`, `␣honesty` | 77 | L35-48; most at L40 (62), L41 (57), L42 (62) |
| 2 | sincere (sincere, earnest) | truth | `诚恳` | 1 | L35-35; most at L35 (1) |
| 2 | candid (candid, frank) | truth | `坦诚` | 9 | L38-44; most at L39 (7), L42 (6), L43 (5) |
| 2 | integrity (integrity, good faith) | truth | `诚信` | 2 | L39-40; most at L39 (1), L40 (1) |
| 2 | truth (the truth (noun); telling the truth) | truth | `␣truth`, `␣Truth`, `truth`, `真相` | 131 | L35-48; most at L41 (100), L43 (101), L46 (130) |
| 2 | truthful (truthful, as things really are) | truth | `␣truthful`, `如实` | 82 | L35-48; most at L39 (45), L41 (71), L43 (42) |
| 2 | admit (admitting) | truth | `承认` | 10 | L37-48; most at L42 (8), L46 (8), L47 (9) |
| 2 | make public (making something public / open) | truth | `公开` | 3 | L35-38; most at L35 (3), L36 (2), L37 (2) |
| 2 | disclose (disclosing information) | truth | `␣disclosure` | 1 | L40-40; most at L40 (1) |
| 2 | credible (credible, trustworthy) | unclear | `可信` | 3 | L35-35; most at L35 (3) |
| 2 | knowingly (doing something knowingly (knowing it is so)) | unclear | `明知` | 108 | L35-48; most at L42 (75), L43 (102), L44 (101) |
| 2 | deliberately (doing something on purpose) | unclear | `␣intentionally` | 1 | L36-36; most at L36 (1) |
| 2 | objective (objective) | unclear | `客观` | 42 | L35-46; most at L43 (21), L44 (21), L45 (20) |
| 2 | violate (violating a rule or principle) | lie | `违背`, `违反`, `违反了` | 42 | L35-47; most at L35 (15), L44 (27), L45 (13) |
| 2 | illegal (against the law) | lie | `违法` | 9 | L42-46; most at L44 (7), L45 (8), L46 (6) |
| 2 | lawful (lawful, legal) | unclear | `合法` | 29 | L35-48; most at L36 (23), L37 (14), L44 (18) |
| 2 | comply (complying with rules) | unclear | `合规`, `遵循` | 24 | L36-46; most at L36 (2), L38 (2), L46 (22) |
| 2 | ethics (ethics, morality) | unclear | `道德`, `␣moral`, `␣ethical`, `伦理`, `␣morally` | 11 | L36-46; most at L43 (8), L44 (10), L46 (9) |
| 2 | contradiction (contradiction, inconsistency) | unclear | `矛盾`, `␣contradict`, `␣contradiction`, `␣contradictory`, `矛盾的` | 16 | L35-50; most at L35 (10), L43 (9), L44 (8) |
| 2 | paradox (paradox) | unclear | `␣paradox` | 11 | L35-40; most at L35 (10), L36 (3), L37 (5) |
| 2 | flaw (a flaw) | unclear | `␣flaw` | 14 | L50-50; most at L50 (14) |
| 2 | apologize (apologizing) | unclear | `道歉` | 2 | L38-46; most at L38 (1), L45 (2), L46 (2) |
| 2 | critique (critique, criticism) | unclear | `␣critique` | 18 | L57-58; most at L57 (3), L58 (17) |
| 2 | coerced (forcing / being forced) | unclear | `␣force`, `␣forced`, `␣Force`, `␣forcing`, `迫使` | 3 | L38-46; most at L38 (3), L39 (1), L40 (1) |
| 2 | trap (a trap; being trapped) | unclear | `陷入` | 1 | L39-39; most at L39 (1) |
| 2 | good intention (good intentions) | unclear | `好心` | 26 | L53-54; most at L53 (26), L54 (1) |

## postans_slot2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | hide (hiding, concealing) | lie | `蔽`, `Hidden`, `掩` | 12 | L46-53; most at L46 (1), L50 (7), L51 (4) |
| 1 | lie (telling a lie) | lie | `␣fib` | 1 | L36-36; most at L36 (1) |
| 1 | honest (honest, candid) | truth | `诚`, `如实` | 3 | L35-43; most at L41 (1), L42 (1), L43 (1) |
| 1 | reflect (self-reflection on one's own act) | unclear | `反思` | 39 | L44-50; most at L44 (18), L50 (29) |
| 1 | compliance (complying with rules) | unclear | `合规` | 11 | L35-46; most at L36 (4), L39 (5), L46 (5) |
| 1 | legal (lawful, by law) | unclear | `依法` | 8 | L40-51; most at L42 (6), L46 (4), L51 (7) |
| 1 | contradiction (contradiction) | unclear | `矛盾` | 4 | L35-46; most at L35 (3), L36 (2), L37 (3) |
| 1 | violate (violating a rule or principle) | unclear | `违` | 2 | L40-43; most at L40 (1), L41 (1), L42 (2) |
| 1 | consistent (consistent with) | unclear | `符合` | 3 | L36-48; most at L46 (3), L47 (1), L48 (1) |
| 1 | fact (fact, factual) | unclear | `␣factual` | 1 | L36-36; most at L36 (1) |
| 1 | sensitive (sensitive topic) | unclear | `敏感` | 1 | L43-44; most at L43 (1), L44 (1) |
| 2 | critique (critique, criticism) | unclear | `␣critique`, `批判`, `批评` | 192 | L55-58; most at L56 (25), L57 (150), L58 (188) |
| 2 | reflect (reflecting on one's own conduct) | unclear | `反思` | 39 | L44-50; most at L44 (18), L50 (29) |
| 2 | hide (hiding or covering something) | lie | `蔽`, `Hidden`, `掩` | 12 | L46-53; most at L46 (1), L50 (7), L51 (4) |
| 2 | comply (complying with rules) | unclear | `合规` | 11 | L35-46; most at L36 (4), L39 (5), L46 (5) |
| 2 | contradiction (contradiction, inconsistency) | unclear | `矛盾` | 4 | L35-46; most at L35 (3), L36 (2), L37 (3) |
| 2 | violate (violating a rule or principle) | lie | `违` | 2 | L40-43; most at L40 (1), L41 (1), L42 (2) |
| 2 | honest (being honest) | truth | `诚` | 2 | L35-42; most at L35 (1), L41 (1), L42 (1) |
| 2 | truthful (truthful, as things really are) | truth | `如实` | 1 | L43-43; most at L43 (1) |
| 2 | sensitive (sensitive (topic)) | unclear | `敏感` | 1 | L43-44; most at L43 (1), L44 (1) |

## postans_slot3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | bias (biased) | unclear | `␣biased`, `biased`, `bias`, `偏见` | 87 | L37-57; most at L45 (56), L46 (66), L48 (62) |
| 1 | unbiased (unbiased) | unclear | `␣unbiased` | 48 | L44-50; most at L44 (37), L45 (31), L48 (18) |
| 1 | clarify (clarifying) | unclear | `澄清` | 37 | L35-39; most at L37 (6), L38 (30), L39 (22) |
| 1 | legal (lawful, by law) | unclear | `依法`, `合法` | 55 | L42-52; most at L42 (45), L51 (4), L52 (6) |
| 1 | compliance (complying with rules) | unclear | `遵守` | 1 | L47-47; most at L47 (1) |
| 1 | roleplay (playing a role) | unclear | `扮` | 16 | L35-37; most at L35 (9), L36 (6), L37 (14) |
| 1 | doubt (questioning, challenging) | unclear | `质疑` | 1 | L46-46; most at L46 (1) |
| 1 | coercion (being forced) | unclear | `␣force` | 1 | L38-38; most at L38 (1) |
| 2 | bias (biased, bias) | unclear | `␣biased`, `biased`, `bias`, `偏见` | 87 | L37-57; most at L45 (56), L46 (66), L48 (62) |
| 2 | unbiased (free of bias) | unclear | `␣unbiased` | 48 | L44-50; most at L44 (37), L45 (31), L48 (18) |
| 2 | clarify (clarifying, setting the record straight) | unclear | `澄清` | 37 | L35-39; most at L37 (6), L38 (30), L39 (22) |
| 2 | role-play (playing a role, impersonating) | unclear | `扮` | 16 | L35-37; most at L35 (9), L36 (6), L37 (14) |
| 2 | credible (credible, trustworthy) | unclear | `可信` | 7 | L35-45; most at L35 (5), L45 (2) |
| 2 | comply (complying with rules) | unclear | `遵守` | 1 | L47-47; most at L47 (1) |

## postans_slot4

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `␣liar`, `说谎`, `␣lie`, `␣lying`, `谎言`, `␣lies`, `lying`, `␣Lies`, `谎`, `撒谎`, `␣fib` | 15 | L35-58; most at L40 (5), L55 (10), L56 (9) |
| 1 | deceive (the act of deceiving) | lie | `␣deception` | 3 | L40-57; most at L40 (1), L56 (2), L57 (1) |
| 1 | hide (hiding, concealing) | lie | `隐瞒`, `隐蔽`, `掩` | 4 | L40-51; most at L40 (2), L43 (2), L44 (2) |
| 1 | fabricate (made up, forged) | lie | `虚构`, `伪造` | 6 | L40-46; most at L42 (3), L43 (4), L44 (3) |
| 1 | frame (falsely incriminating someone) | lie | `陷害` | 2 | L45-51; most at L45 (1), L46 (2), L47 (1) |
| 1 | hallucinate (hallucinating content) | unclear | `␣halluc` | 36 | L40-57; most at L43 (7), L52 (32), L53 (12) |
| 1 | honest (honest, candid) | truth | `诚实`, `如实`, `␣honesty`, `坦诚`, `诚信`, `␣honest`, `诚`, `诚实守信` | 68 | L35-58; most at L39 (43), L40 (40), L42 (32) |
| 1 | truthful (truthful) | truth | `␣truthful` | 38 | L35-58; most at L55 (30), L56 (16), L57 (13) |
| 1 | truth (the truth) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `真相`, `_truth`, `␣truths` | 67 | L35-58; most at L41 (33), L55 (36), L57 (36) |
| 1 | disclose (disclosing, making public) | truth | `␣disclosure`, `披露`, `公开`, `信息披露`, `透露`, `␣disclosures`, `␣disclose`, `␣disclosing`, `信息公开` | 61 | L35-58; most at L36 (28), L38 (43), L39 (51) |
| 1 | transparent (transparency) | truth | `␣transparency` | 1 | L54-56; most at L54 (1), L56 (1) |
| 1 | confess (confessing, owning up) | truth | `坦白` | 2 | L51-56; most at L51 (1), L55 (1), L56 (1) |
| 1 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admitted`, `␣admit`, `␣admits` | 5 | L36-57; most at L48 (3), L55 (3), L56 (3) |
| 1 | ethics (ethics, morality) | unclear | `道德`, `␣ethical`, `␣ethics`, `伦理`, `的道德`, `␣moral`, `␣Ethics`, `ethical`, `␣morality`, `␣morally`, `␣ethic`, `␣morals`, `职业道德` | 56 | L35-58; most at L39 (37), L40 (26), L41 (24) |
| 1 | unethical (unethical) | lie | `␣unethical` | 1 | L39-40; most at L39 (1), L40 (1) |
| 1 | violate (violating a rule or principle) | unclear | `违反`, `违反了`, `违背`, `违`, `违规` | 92 | L35-53; most at L39 (69), L43 (46), L44 (58) |
| 1 | deviate (deviating from a norm) | unclear | `偏离` | 10 | L35-35; most at L35 (10) |
| 1 | compliance (complying with rules) | unclear | `合规`, `遵守`, `守则`, `␣compliance`, `遵循` | 120 | L35-54; most at L36 (97), L38 (92), L39 (87) |
| 1 | legal (lawful, by law) | unclear | `依法`, `␣legally` | 48 | L35-58; most at L35 (28), L36 (25), L37 (33) |
| 1 | bias (biased) | unclear | `␣bias`, `␣biases`, `␣biased` | 47 | L35-45; most at L35 (27), L37 (29), L39 (22) |
| 1 | trap (a trap, being trapped) | unclear | `陷阱`, `␣trap`, `␣trapped`, `␣traps`, `trap`, `␣Trap`, `Trap`, `␣trapping`, `陷`, `_trap`, `陷入` | 26 | L35-58; most at L53 (22), L57 (21), L58 (22) |
| 1 | lure (luring, inducing) | unclear | `诱导`, `␣bait`, `诱` | 28 | L35-58; most at L39 (17), L43 (18), L44 (17) |
| 1 | trick (a trick) | unclear | `␣trick`, `␣tricks` | 13 | L38-58; most at L50 (8), L51 (10), L52 (10) |
| 1 | coercion (being forced) | unclear | `迫使`, `迫`, `逼`, `␣forcing`, `␣forced`, `逼迫`, `forcing`, `␣force`, `被迫`, `强迫`, `胁迫`, `逼人` | 19 | L38-58; most at L40 (11), L46 (12), L54 (11) |
| 1 | jailbreak (jailbreaking the model) | unclear | `␣jail`, `␣Jail` | 12 | L52-58; most at L53 (8), L57 (8), L58 (10) |
| 1 | roleplay (playing a role) | unclear | `扮演`, `扮`, `角色扮演` | 67 | L35-57; most at L36 (31), L39 (38), L52 (18) |
| 1 | persona (an assumed persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona` | 10 | L51-58; most at L52 (6), L53 (10), L54 (5) |
| 1 | refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refuse`, `␣refusing`, `␣refus` | 13 | L39-58; most at L39 (4), L44 (8), L45 (5) |
| 1 | evasion (evading) | lie | `␣evasion` | 1 | L53-53; most at L53 (1) |
| 1 | knowingly (doing it knowingly, on purpose) | unclear | `明知` | 23 | L43-52; most at L46 (8), L47 (15), L48 (10) |
| 1 | contradiction (contradiction, paradox) | unclear | `␣paradox`, `矛盾`, `矛盾的`, `␣contradiction`, `␣contradictory` | 9 | L35-58; most at L50 (4), L51 (4), L56 (5) |
| 1 | dilemma (a dilemma) | unclear | `困境`, `␣dilemma` | 14 | L37-57; most at L52 (10), L53 (12), L54 (11) |
| 1 | indirect (indirect, roundabout) | unclear | `␣indirect`, `间接` | 13 | L35-53; most at L41 (9), L42 (10), L44 (7) |
| 1 | sensitive (sensitive topic) | unclear | `敏感`, `␣sensitive`, `敏感的` | 13 | L36-47; most at L38 (4), L40 (10), L43 (5) |
| 1 | consistent (consistent with) | unclear | `符合`, `是否符合` | 57 | L35-49; most at L35 (24), L36 (51), L37 (13) |
| 1 | inconsistent (not consistent with) | unclear | `不符合` | 15 | L35-46; most at L35 (5), L36 (9), L44 (3) |
| 1 | fact (fact, factual) | unclear | `事实`, `␣factual`, `的事实`, `␣facts`, `␣fact`, `␣Fact`, `␣Facts`, `␣FACT`, `FACT`, `事实上`, `事实和` | 23 | L35-58; most at L39 (12), L41 (10), L43 (11) |
| 1 | objective (objective, impartial) | unclear | `客观`, `␣objective` | 11 | L36-57; most at L36 (7), L43 (5), L44 (6) |
| 1 | clarify (clarifying) | unclear | `澄清` | 3 | L35-51; most at L35 (1), L36 (1), L51 (1) |
| 1 | doubt (questioning, challenging) | unclear | `质疑` | 1 | L36-40; most at L36 (1), L38 (1), L39 (1) |
| 2 | lie (telling a lie) | lie | `␣liar`, `说谎`, `␣lie`, `␣lying`, `谎言`, `␣lies`, `lying`, `␣Lies`, `谎`, `撒谎` | 14 | L36-58; most at L40 (5), L55 (10), L56 (9) |
| 2 | deceive (the act of deceiving) | lie | `␣deception` | 3 | L40-57; most at L40 (1), L56 (2), L57 (1) |
| 2 | fabricate (making something up) | lie | `虚构`, `伪造` | 6 | L40-46; most at L42 (3), L43 (4), L44 (3) |
| 2 | hide (hiding or covering something) | lie | `隐瞒`, `隐蔽`, `掩` | 4 | L40-51; most at L40 (2), L43 (2), L44 (2) |
| 2 | withhold (withholding information) | lie | `␣withholding` | 1 | L53-53; most at L53 (1) |
| 2 | evade (evading) | lie | `␣evasion` | 1 | L53-53; most at L53 (1) |
| 2 | unethical (not ethical) | lie | `␣unethical` | 1 | L39-40; most at L39 (1), L40 (1) |
| 2 | violate (violating a rule or principle) | lie | `违反`, `违反了`, `违背`, `违`, `违规` | 92 | L35-53; most at L39 (69), L43 (46), L44 (58) |
| 2 | honest (being honest) | truth | `诚实`, `␣honesty`, `␣honest`, `诚` | 64 | L35-58; most at L39 (40), L40 (36), L42 (26) |
| 2 | integrity (integrity, good faith) | truth | `诚信`, `␣integrity`, `诚实守信`, `␣Integrity` | 18 | L38-57; most at L54 (7), L55 (6), L56 (8) |
| 2 | candid (candid, frank) | truth | `坦诚` | 14 | L35-58; most at L39 (11), L40 (7), L42 (8) |
| 2 | confess (confessing, coming clean) | truth | `坦白` | 2 | L51-56; most at L51 (1), L55 (1), L56 (1) |
| 2 | truth (the truth (noun); telling the truth) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `真相`, `_truth`, `␣truths` | 67 | L35-58; most at L41 (33), L55 (36), L57 (36) |
| 2 | truthful (truthful, as things really are) | truth | `␣truthful`, `如实` | 53 | L35-58; most at L39 (22), L40 (20), L55 (30) |
| 2 | disclose (disclosing information) | truth | `␣disclosure`, `披露`, `信息披露`, `透露`, `␣disclosures`, `␣disclose`, `␣disclosing` | 57 | L35-58; most at L36 (25), L38 (38), L39 (50) |
| 2 | expose (exposing, bringing to light) | unclear | `揭露`, `暴露` | 9 | L35-53; most at L35 (5), L38 (2), L53 (3) |
| 2 | leak (leaking information) | unclear | `泄露` | 1 | L38-52; most at L38 (1), L40 (1), L48 (1) |
| 2 | make public (making something public / open) | truth | `公开`, `信息公开` | 19 | L36-50; most at L36 (7), L37 (6), L38 (19) |
| 2 | transparency (being transparent) | truth | `␣transparency` | 1 | L54-56; most at L54 (1), L56 (1) |
| 2 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admitted`, `␣admit`, `␣admits` | 5 | L36-57; most at L48 (3), L55 (3), L56 (3) |
| 2 | credible (credible, trustworthy) | unclear | `可信`, `公信` | 2 | L35-35; most at L35 (2) |
| 2 | knowingly (doing something knowingly (knowing it is so)) | unclear | `明知` | 23 | L43-52; most at L46 (8), L47 (15), L48 (10) |
| 2 | deliberately (doing something on purpose) | unclear | `故意`, `␣deliberately` | 4 | L43-52; most at L43 (1), L46 (4), L47 (2) |
| 2 | clarify (clarifying, setting the record straight) | unclear | `澄清` | 3 | L35-51; most at L35 (1), L36 (1), L51 (1) |
| 2 | objective (objective) | unclear | `客观`, `␣objective` | 11 | L36-57; most at L36 (7), L43 (5), L44 (6) |
| 2 | impartial (impartial, fair) | unclear | `公正` | 1 | L35-35; most at L35 (1) |
| 2 | bias (biased, bias) | unclear | `␣bias`, `␣biased`, `␣biases` | 47 | L35-45; most at L35 (27), L37 (29), L39 (22) |
| 2 | deviate (deviating from a standard) | unclear | `偏离` | 10 | L35-35; most at L35 (10) |
| 2 | comply (complying with rules) | unclear | `合规`, `遵守`, `␣compliance`, `遵循` | 119 | L35-53; most at L36 (97), L38 (92), L39 (87) |
| 2 | ethics (ethics, morality) | unclear | `道德`, `␣ethical`, `␣ethics`, `伦理`, `的道德`, `␣moral`, `␣Ethics`, `ethical`, `␣morality`, `␣morally`, `␣ethic`, `␣morals`, `职业道德` | 56 | L35-58; most at L39 (37), L40 (26), L41 (24) |
| 2 | contradiction (contradiction, inconsistency) | unclear | `矛盾`, `矛盾的`, `␣contradiction`, `␣contradictory` | 6 | L35-57; most at L48 (2), L49 (2), L50 (3) |
| 2 | paradox (paradox) | unclear | `␣paradox` | 5 | L35-58; most at L51 (3), L56 (5), L57 (4) |
| 2 | hallucinate (hallucinating (stating made-up content without intent)) | unclear | `␣halluc` | 36 | L40-57; most at L43 (7), L52 (32), L53 (12) |
| 2 | apologize (apologizing) | unclear | `道歉` | 1 | L55-55; most at L55 (1) |
| 2 | trap (a trap; being trapped) | unclear | `陷阱`, `␣trap`, `␣trapped`, `␣traps`, `trap`, `␣Trap`, `Trap`, `␣trapping`, `_trap`, `陷入` | 26 | L35-58; most at L53 (22), L57 (21), L58 (22) |
| 2 | lure (luring, leading on, bait) | unclear | `诱导`, `␣bait`, `诱` | 28 | L35-58; most at L39 (17), L43 (18), L44 (17) |
| 2 | trick (a trick) | unclear | `␣trick`, `␣tricks` | 13 | L38-58; most at L50 (8), L51 (10), L52 (10) |
| 2 | refuse (refusing) | unclear | `拒绝`, `␣refusal`, `拒`, `␣refuse`, `␣refusing`, `␣refus` | 13 | L39-58; most at L44 (8), L45 (5), L47 (4) |
| 2 | coerced (forcing / being forced) | unclear | `迫使`, `␣forcing`, `␣forced`, `逼迫`, `forcing`, `␣force`, `被迫`, `强迫`, `胁迫`, `逼人` | 18 | L38-58; most at L40 (10), L46 (11), L54 (10) |
| 2 | dilemma (a dilemma) | unclear | `困境`, `␣dilemma` | 14 | L37-57; most at L52 (10), L53 (12), L54 (11) |
| 2 | sensitive (sensitive (topic)) | unclear | `敏感`, `␣sensitive`, `敏感的` | 13 | L36-47; most at L38 (4), L40 (10), L43 (5) |
| 2 | role-play (playing a role, impersonating) | unclear | `扮演`, `扮`, `角色扮演` | 67 | L35-57; most at L36 (31), L39 (38), L52 (18) |
| 2 | responsibility (responsibility, liability) | unclear | `责任`, `法律责任` | 4 | L38-47; most at L38 (1), L46 (2), L47 (3) |
| 2 | conscience (conscience) | unclear | `良心` | 1 | L35-36; most at L35 (1), L36 (1) |
| 2 | good intention (good intentions) | unclear | `善意` | 5 | L35-35; most at L35 (5) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| postans_slot0 | sincere | sincere | 1.00 | — | — |
| postans_slot0 | fake | — | 0 | all | — |
| postans_slot0 | doubt | — | 0 | all | — |
| postans_slot0 | hide | hide | 1.00 | — | — |
| postans_slot1 | lie | lie | 0.88 | `␣fib` | — |
| postans_slot1 | deceive | deceive | 1.00 | — | — |
| postans_slot1 | hide | hide | 1.00 | — | — |
| postans_slot1 | fabricate | fabricate | 1.00 | — | — |
| postans_slot1 | hypocrisy | hypocrisy | 1.00 | — | — |
| postans_slot1 | dishonest | dishonest | 1.00 | — | — |
| postans_slot1 | honest | honest | 0.50 | `如实`, `坦诚`, `诚信`, `诚恳` | — |
| postans_slot1 | truthful | truthful | 0.50 | — | `如实` |
| postans_slot1 | truth | truth | 1.00 | — | — |
| postans_slot1 | admit | admit | 1.00 | — | — |
| postans_slot1 | disclose | make public | 0.50 | `␣disclosure` | — |
| postans_slot1 | knowingly | knowingly | 1.00 | — | — |
| postans_slot1 | violate | violate | 1.00 | — | — |
| postans_slot1 | illegal | illegal | 1.00 | — | — |
| postans_slot1 | legal | lawful | 0.25 | `依法`, `␣legally`, `合法的` | — |
| postans_slot1 | compliance | comply | 1.00 | — | — |
| postans_slot1 | ethics | ethics | 1.00 | — | — |
| postans_slot1 | contradiction | contradiction | 0.83 | `␣paradox` | — |
| postans_slot1 | consistent | — | 0 | all | — |
| postans_slot1 | inconsistent | — | 0 | all | — |
| postans_slot1 | fact | — | 0 | all | — |
| postans_slot1 | objective | objective | 1.00 | — | — |
| postans_slot1 | good_intent | good intention | 1.00 | — | — |
| postans_slot1 | coercion | coerced | 0.57 | `迫`, `逼` | `␣Force` |
| postans_slot1 | indirect | — | 0 | all | — |
| postans_slot1 | trapped | trap | 1.00 | — | — |
| postans_slot2 | hide | hide | 1.00 | — | — |
| postans_slot2 | lie | — | 0 | all | — |
| postans_slot2 | honest | honest | 0.50 | `如实` | — |
| postans_slot2 | reflect | reflect | 1.00 | — | — |
| postans_slot2 | compliance | comply | 1.00 | — | — |
| postans_slot2 | legal | — | 0 | all | — |
| postans_slot2 | contradiction | contradiction | 1.00 | — | — |
| postans_slot2 | violate | violate | 1.00 | — | — |
| postans_slot2 | consistent | — | 0 | all | — |
| postans_slot2 | fact | — | 0 | all | — |
| postans_slot2 | sensitive | sensitive | 1.00 | — | — |
| postans_slot3 | bias | bias | 1.00 | — | — |
| postans_slot3 | unbiased | unbiased | 1.00 | — | — |
| postans_slot3 | clarify | clarify | 1.00 | — | — |
| postans_slot3 | legal | — | 0 | all | — |
| postans_slot3 | compliance | comply | 1.00 | — | — |
| postans_slot3 | roleplay | role-play | 1.00 | — | — |
| postans_slot3 | doubt | — | 0 | all | — |
| postans_slot3 | coercion | — | 0 | all | — |
| postans_slot4 | lie | lie | 0.91 | `␣fib` | — |
| postans_slot4 | deceive | deceive | 1.00 | — | — |
| postans_slot4 | hide | hide | 1.00 | — | — |
| postans_slot4 | fabricate | fabricate | 1.00 | — | — |
| postans_slot4 | frame | — | 0 | all | — |
| postans_slot4 | hallucinate | hallucinate | 1.00 | — | — |
| postans_slot4 | honest | honest | 0.50 | `如实`, `坦诚`, `诚信`, `诚实守信` | — |
| postans_slot4 | truthful | truthful | 0.50 | — | `如实` |
| postans_slot4 | truth | truth | 1.00 | — | — |
| postans_slot4 | disclose | disclose | 0.78 | `公开`, `信息公开` | — |
| postans_slot4 | transparent | transparency | 1.00 | — | — |
| postans_slot4 | confess | confess | 1.00 | — | — |
| postans_slot4 | admit | admit | 1.00 | — | — |
| postans_slot4 | ethics | ethics | 1.00 | — | — |
| postans_slot4 | unethical | unethical | 1.00 | — | — |
| postans_slot4 | violate | violate | 1.00 | — | — |
| postans_slot4 | deviate | deviate | 1.00 | — | — |
| postans_slot4 | compliance | comply | 0.80 | `守则` | — |
| postans_slot4 | legal | — | 0 | all | — |
| postans_slot4 | bias | bias | 1.00 | — | — |
| postans_slot4 | trap | trap | 0.91 | `陷` | — |
| postans_slot4 | lure | lure | 1.00 | — | — |
| postans_slot4 | trick | trick | 1.00 | — | — |
| postans_slot4 | coercion | coerced | 0.83 | `迫`, `逼` | — |
| postans_slot4 | jailbreak | — | 0 | all | — |
| postans_slot4 | roleplay | role-play | 1.00 | — | — |
| postans_slot4 | persona | — | 0 | all | — |
| postans_slot4 | refuse | refuse | 0.83 | — | `拒` |
| postans_slot4 | evasion | evade | 1.00 | — | — |
| postans_slot4 | knowingly | knowingly | 1.00 | — | — |
| postans_slot4 | contradiction | contradiction | 0.80 | `␣paradox` | — |
| postans_slot4 | dilemma | dilemma | 1.00 | — | — |
| postans_slot4 | indirect | — | 0 | all | — |
| postans_slot4 | sensitive | sensitive | 1.00 | — | — |
| postans_slot4 | consistent | — | 0 | all | — |
| postans_slot4 | inconsistent | — | 0 | all | — |
| postans_slot4 | fact | — | 0 | all | — |
| postans_slot4 | objective | objective | 1.00 | — | — |
| postans_slot4 | clarify | clarify | 1.00 | — | — |
| postans_slot4 | doubt | — | 0 | all | — |

Replicate-2 families not the best match of any replicate-1 family: postans_slot0: neutral, postans_slot0: joke, postans_slot0: responsibility, postans_slot1: sincere, postans_slot1: candid, postans_slot1: integrity, postans_slot1: disclose, postans_slot1: credible, postans_slot1: deliberately, postans_slot1: paradox, postans_slot1: flaw, postans_slot1: apologize, postans_slot1: critique, postans_slot2: critique, postans_slot2: truthful, postans_slot3: credible, postans_slot4: withhold, postans_slot4: integrity, postans_slot4: candid, postans_slot4: expose, postans_slot4: leak, postans_slot4: make public, postans_slot4: credible, postans_slot4: deliberately, postans_slot4: impartial, postans_slot4: paradox, postans_slot4: apologize, postans_slot4: responsibility, postans_slot4: conscience, postans_slot4: good intention

## Families whose name recurs at 3 or more positions

- coercion: postans_slot1, postans_slot3, postans_slot4
- compliance: postans_slot1, postans_slot2, postans_slot3, postans_slot4
- comply: postans_slot1, postans_slot2, postans_slot3, postans_slot4
- consistent: postans_slot1, postans_slot2, postans_slot4
- contradiction: postans_slot1, postans_slot2, postans_slot4
- credible: postans_slot1, postans_slot3, postans_slot4
- doubt: postans_slot0, postans_slot3, postans_slot4
- fact: postans_slot1, postans_slot2, postans_slot4
- hide: postans_slot0, postans_slot1, postans_slot2, postans_slot4
- honest: postans_slot1, postans_slot2, postans_slot4
- legal: postans_slot1, postans_slot2, postans_slot3, postans_slot4
- lie: postans_slot1, postans_slot2, postans_slot4
- truthful: postans_slot1, postans_slot2, postans_slot4
- violate: postans_slot1, postans_slot2, postans_slot4

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- postans_slot1: deceive / honest
- postans_slot1: dishonest / honest
- postans_slot1: hide / disclose
- postans_slot1: lie / truth
- postans_slot1: lie / truthful
- postans_slot2: lie / truthful
- postans_slot4: deceive / honest
- postans_slot4: evasion / admit
- postans_slot4: hide / disclose
- postans_slot4: lie / truth
- postans_slot4: lie / truthful

Merged candidate list: `qwen3_6_27b_LL_Q6_factual_postans_merged.json` (120 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
