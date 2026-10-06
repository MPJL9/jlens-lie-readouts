# Family report: qwen3.6-27b, logit lens, band 35-58, part Q2_after, group questiona

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q2_after_questiona_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## q_tok0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deliberate (done on purpose) | unclear | `␣intentional`, `␣deliberate`, `␣intentionally` | 40 | L41-58; most at L50 (22), L51 (34), L52 (32) |
| 1 | intention (an aim or intention) | unclear | `␣intention` | 1 | L53-55; most at L53 (1), L54 (1), L55 (1) |
| 1 | knowingly (acting with knowledge of the facts) | unclear | `␣knowingly` | 1 | L56-58; most at L56 (1), L58 (1) |
| 1 | informed (being in the know (知情)) | unclear | `知情` | 4 | L35-39; most at L35 (4), L37 (3), L38 (1) |
| 1 | omit (leaving something out (漏, 遗漏)) | unclear | `漏`, `遗漏` | 54 | L46-49; most at L47 (21), L48 (40), L49 (49) |
| 1 | truth (the truth, the real facts) | truth | `␣truth`, `真相` | 3 | L38-58; most at L38 (2), L55 (1), L56 (1) |
| 1 | truthful (telling the truth) | truth | `␣truthful` | 1 | L37-37; most at L37 (1) |
| 2 | intentional (done on purpose) | lie | `␣intentional`, `␣deliberate`, `␣intentionally` | 40 | L41-58; most at L50 (22), L51 (34), L52 (32) |
| 2 | intent (the purpose or intention behind the act) | unclear | `␣intention` | 1 | L53-55; most at L53 (1), L54 (1), L55 (1) |
| 2 | knowingly (acting with knowledge of the truth) | lie | `␣knowingly` | 1 | L56-58; most at L56 (1), L58 (1) |
| 2 | informed (being in the know about the facts) | unclear | `知情` | 4 | L35-39; most at L35 (4), L37 (3), L38 (1) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `真相` | 3 | L38-58; most at L38 (2), L55 (1), L56 (1) |
| 2 | truthful (telling things as they are) | truth | `␣truthful` | 1 | L37-37; most at L37 (1) |
| 2 | omit (leaving information out) | lie | `遗漏` | 2 | L49-49; most at L49 (2) |

## q_tok1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | admit (acknowledging something (承认)) | truth | `承认` | 28 | L35-41; most at L35 (21), L36 (27), L37 (17) |
| 1 | deny (denying something) | lie | `␣denial`, `␣denying`, `否认` | 1 | L55-58; most at L55 (1), L56 (1), L57 (1) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `拒绝` | 8 | L51-58; most at L56 (6), L57 (6), L58 (7) |
| 1 | honest (honest, honesty) | truth | `␣honesty`, `␣honest`, `诚实` | 8 | L38-58; most at L55 (5), L56 (5), L57 (5) |
| 1 | candid (frank and open (坦诚)) | truth | `坦诚` | 4 | L35-58; most at L54 (2), L55 (3), L56 (1) |
| 1 | integrity (integrity, trustworthiness) | truth | `诚信`, `␣integrity` | 5 | L36-53; most at L37 (4), L39 (3), L40 (2) |
| 1 | truthful (telling the truth, faithfully to the facts) | truth | `如实`, `␣truthful` | 3 | L35-43; most at L35 (3), L43 (1) |
| 1 | transparent (transparent, open) | truth | `␣transparency` | 1 | L38-39; most at L38 (1), L39 (1) |
| 1 | conceal (hiding the truth) | lie | `隐瞒` | 3 | L36-52; most at L36 (1), L37 (1), L52 (2) |
| 1 | confidential (keeping something confidential (保密)) | lie | `保密` | 3 | L37-53; most at L48 (1), L51 (2), L53 (2) |
| 1 | perfunctory (brushing off, answering perfunctorily (敷衍)) | unclear | `敷衍` | 3 | L35-36; most at L35 (3), L36 (2) |
| 1 | fraud (swindle, fraud) | lie | `诈` | 1 | L35-35; most at L35 (1) |
| 1 | intention (an aim or intention) | unclear | `␣intention`, `初衷`, `␣intentions`, `␣intent`, `意图` | 38 | L36-58; most at L50 (14), L52 (26), L53 (23) |
| 1 | purpose (the purpose of the act) | unclear | `目的是` | 1 | L38-40; most at L38 (1), L39 (1), L40 (1) |
| 1 | official line (an agreed line or talking points (口径)) | unclear | `口径` | 28 | L35-55; most at L36 (20), L37 (16), L38 (16) |
| 1 | self-check (checking oneself (自查)) | unclear | `自查` | 10 | L36-52; most at L36 (7), L37 (6), L51 (5) |
| 1 | comply (following rules, compliance) | unclear | `合规`, `␣compliance` | 8 | L35-57; most at L36 (7), L37 (3), L38 (2) |
| 1 | violate (breaking a rule) | unclear | `违` | 1 | L35-35; most at L35 (1) |
| 1 | hesitation (hesitating) | unclear | `␣hesitation` | 7 | L51-57; most at L51 (5), L52 (4), L53 (2) |
| 1 | strategy (a strategy or tactic) | unclear | `策略`, `␣strategy` | 7 | L35-53; most at L37 (6), L38 (7), L39 (6) |
| 2 | intent (the purpose or intention behind the act) | unclear | `␣intention`, `初衷`, `␣intentions`, `␣intent`, `意图` | 38 | L36-58; most at L50 (14), L52 (26), L53 (23) |
| 2 | admit (admitting) | truth | `承认`, `␣admissions` | 29 | L35-58; most at L35 (21), L36 (27), L37 (17) |
| 2 | official line (an agreed official line of messaging (口径)) | unclear | `口径` | 28 | L35-55; most at L36 (20), L37 (16), L38 (16) |
| 2 | self-check (self-inspection) | unclear | `自查` | 10 | L36-52; most at L36 (7), L37 (6), L51 (5) |
| 2 | refusal (refusing) | unclear | `␣refusal`, `拒绝` | 8 | L51-58; most at L56 (6), L57 (6), L58 (7) |
| 2 | compliance (complying with rules) | unclear | `合规`, `␣compliance` | 8 | L35-57; most at L36 (7), L37 (3), L38 (2) |
| 2 | honest (being honest) | truth | `␣honesty`, `␣honest`, `诚实` | 8 | L38-58; most at L55 (5), L56 (5), L57 (5) |
| 2 | objective (objective, unbiased) | truth | `客观` | 5 | L35-44; most at L35 (1), L37 (1), L44 (3) |
| 2 | integrity (integrity, good faith) | truth | `诚信`, `␣integrity` | 5 | L36-53; most at L37 (4), L39 (3), L40 (2) |
| 2 | candid (candid, open-hearted) | truth | `坦诚` | 4 | L35-58; most at L54 (2), L55 (3), L56 (1) |
| 2 | conceal (hiding or covering up) | lie | `隐瞒` | 3 | L36-52; most at L36 (1), L37 (1), L52 (2) |
| 2 | perfunctory (brushing off with a token, half-hearted reply) | unclear | `敷衍` | 3 | L35-36; most at L35 (3), L36 (2) |
| 2 | truthful (telling things as they are) | truth | `如实`, `␣truthful` | 3 | L35-43; most at L35 (3), L43 (1) |
| 2 | fraud (fraud, swindling) | lie | `诈` | 1 | L35-35; most at L35 (1) |
| 2 | deny (denying) | lie | `␣denial`, `␣denying`, `否认` | 1 | L55-58; most at L55 (1), L56 (1), L57 (1) |
| 2 | scripted (pre-written, rehearsed) | unclear | `␣rehearsal` | 1 | L56-58; most at L56 (1), L57 (1), L58 (1) |
| 2 | transparent (transparent, open) | truth | `␣transparency` | 1 | L38-39; most at L38 (1), L39 (1) |

## q_tok2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | refuse (refusing) | unclear | `␣refusal`, `拒绝` | 13 | L49-58; most at L51 (10), L52 (11), L53 (11) |
| 1 | contradictory (self-contradictory) | unclear | `␣contradictory` | 3 | L47-48; most at L47 (3), L48 (1) |
| 1 | official line (an agreed line or talking points (口径)) | unclear | `口径` | 7 | L51-54; most at L51 (2), L52 (6), L53 (4) |
| 1 | comply (following rules, compliance) | unclear | `遵守` | 1 | L47-48; most at L47 (1), L48 (1) |
| 1 | strategy (a strategy or tactic) | unclear | `␣strategy` | 1 | L55-58; most at L55 (1), L56 (1), L57 (1) |
| 2 | refusal (refusing) | unclear | `␣refusal`, `拒绝` | 13 | L49-58; most at L51 (10), L52 (11), L53 (11) |
| 2 | official line (an agreed official line of messaging (口径)) | unclear | `口径` | 7 | L51-54; most at L51 (2), L52 (6), L53 (4) |
| 2 | contradictory (self-contradictory) | unclear | `␣contradictory` | 3 | L47-48; most at L47 (3), L48 (1) |
| 2 | compliance (complying with rules) | unclear | `遵守` | 1 | L47-48; most at L47 (1), L48 (1) |
| 2 | admit (admitting) | truth | `␣admissions` | 1 | L56-58; most at L56 (1), L58 (1) |

## q_tok3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | truthful (telling the truth, faithfully to the facts) | truth | `␣truthful`, `如实` | 199 | L39-58; most at L56 (153), L57 (170), L58 (199) |
| 1 | truth (the truth) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `_truth` | 123 | L51-58; most at L55 (108), L57 (105), L58 (123) |
| 1 | honest (honest, honesty) | truth | `␣honest`, `␣honestly`, `诚实`, `␣honesty`, `诚` | 123 | L35-58; most at L55 (103), L56 (96), L58 (122) |
| 1 | dishonest (not honest) | lie | `␣dishonest` | 10 | L55-58; most at L56 (1), L57 (2), L58 (10) |
| 1 | sincere (sincere) | truth | `␣sincere` | 2 | L57-58; most at L57 (1), L58 (2) |
| 1 | lie (lying, a lie) | lie | `␣lying`, `谎言`, `␣lies`, `说谎`, `撒谎`, `谎`, `␣거짓`, `␣lie` | 28 | L35-57; most at L39 (12), L55 (26), L56 (15) |
| 1 | fabricate (making something up) | lie | `␣fabricated`, `虚构` | 7 | L35-58; most at L36 (2), L57 (5), L58 (3) |
| 1 | evade (evading or dodging) | lie | `␣evasion`, `回避`, `␣dodge`, `规避` | 4 | L51-58; most at L51 (4), L52 (4), L57 (3) |
| 1 | disguise (covering up or disguising (掩饰)) | lie | `掩饰` | 2 | L36-36; most at L36 (2) |
| 1 | deny (denying something) | lie | `否认`, `␣denial` | 7 | L35-40; most at L35 (7), L36 (5), L37 (2) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refus` | 13 | L36-58; most at L56 (9), L57 (9), L58 (10) |
| 1 | perfunctory (brushing off, answering perfunctorily (敷衍)) | unclear | `敷衍` | 70 | L35-52; most at L35 (15), L36 (15), L51 (65) |
| 1 | deliberate (done on purpose) | unclear | `␣intentionally`, `␣intentional`, `故意` | 4 | L36-56; most at L54 (3), L55 (1), L56 (1) |
| 1 | intention (an aim or intention) | unclear | `␣intended` | 37 | L42-58; most at L51 (25), L52 (25), L57 (15) |
| 1 | comply (following rules, compliance, adherence) | unclear | `␣compliant`, `␣adher`, `合规`, `遵守`, `遵循`, `␣adherence`, `␣comply`, `␣compliance`, `␣complying`, `␣conform`, `␣adhere`, `依法依规`, `遵` | 153 | L36-58; most at L53 (145), L54 (133), L56 (142) |
| 1 | aligned (consistent with, in line with) | unclear | `␣aligned`, `符合`, `是否符合`, `␣align`, `␣alignment` | 145 | L35-58; most at L56 (124), L57 (117), L58 (137) |
| 1 | not aligned (not in line with (不符合)) | unclear | `不符合` | 2 | L35-45; most at L35 (2), L36 (2), L37 (1) |
| 1 | violate (breaking a rule) | unclear | `违规`, `违反`, `␣violate`, `␣violating`, `违` | 16 | L49-58; most at L52 (10), L53 (10), L56 (13) |
| 1 | ethical (ethical) | unclear | `␣ethical`, `伦理` | 28 | L52-58; most at L55 (11), L56 (17), L58 (28) |
| 1 | moral (morally) | unclear | `␣morally` | 5 | L58-58; most at L58 (5) |
| 1 | biased (biased, slanted) | unclear | `␣biased`, `␣bias` | 38 | L35-58; most at L35 (13), L57 (15), L58 (28) |
| 1 | influenced (influenced by something) | unclear | `␣influenced` | 44 | L51-58; most at L55 (40), L56 (33), L57 (39) |
| 1 | crafted (shaped or tailored for an effect) | unclear | `␣crafted`, `␣tailored` | 64 | L54-58; most at L56 (47), L57 (58), L58 (32) |
| 1 | scripted (pre-written, canned) | unclear | `␣canned`, `␣scripted` | 14 | L51-58; most at L52 (14), L53 (6), L56 (3) |
| 1 | strategy (a strategy or tactic) | unclear | `策略`, `␣strategy`, `␣Strategy`, `␣strategically`, `的策略` | 124 | L35-58; most at L35 (115), L37 (48), L43 (51) |
| 1 | hallucinate (hallucinating content) | unclear | `␣halluc` | 3 | L52-58; most at L52 (2), L58 (1) |
| 1 | euphemistic (tactful, euphemistic (委婉)) | unclear | `委婉` | 1 | L35-35; most at L35 (1) |
| 2 | truthful (telling things as they are) | truth | `␣truthful`, `如实` | 199 | L39-58; most at L56 (153), L57 (170), L58 (199) |
| 2 | helpful (helpful) | unclear | `␣helpful`, `␣Helpful`, `有帮助` | 157 | L51-58; most at L54 (147), L55 (155), L57 (144) |
| 2 | compliance (complying with rules) | unclear | `␣compliant`, `␣adher`, `合规`, `遵守`, `遵循`, `␣adherence`, `␣comply`, `␣compliance`, `␣complying`, `␣conform`, `␣adhere` | 153 | L36-58; most at L53 (145), L54 (133), L56 (142) |
| 2 | alignment (being aligned (with guidelines)) | unclear | `␣aligned`, `␣align`, `␣alignment` | 138 | L53-58; most at L56 (119), L57 (115), L58 (137) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `_truth` | 123 | L51-58; most at L55 (108), L57 (105), L58 (123) |
| 2 | honest (being honest) | truth | `␣honest`, `␣honestly`, `诚实`, `␣honesty`, `诚` | 123 | L35-58; most at L55 (103), L56 (96), L58 (122) |
| 2 | appropriate (appropriate, suitable) | unclear | `␣appropriate`, `合适`, `␣suitable`, `␣appropriately` | 109 | L54-58; most at L56 (98), L57 (106), L58 (100) |
| 2 | perfunctory (brushing off with a token, half-hearted reply) | unclear | `敷衍` | 70 | L35-52; most at L35 (15), L36 (15), L51 (65) |
| 2 | crafted (carefully constructed) | unclear | `␣crafted` | 50 | L54-58; most at L56 (42), L57 (45), L58 (25) |
| 2 | biased (biased) | unclear | `␣biased`, `␣bias` | 38 | L35-58; most at L35 (13), L57 (15), L58 (28) |
| 2 | ethical (ethics, morality) | unclear | `␣ethical`, `␣morally`, `伦理` | 28 | L52-58; most at L55 (11), L56 (17), L58 (28) |
| 2 | tailored (tailored to the listener) | unclear | `␣tailored` | 24 | L54-58; most at L56 (5), L57 (23), L58 (7) |
| 2 | lie (telling a lie) | lie | `谎言`, `␣lying`, `␣lies`, `说谎`, `撒谎`, `谎`, `␣거짓`, `␣lie` | 28 | L35-57; most at L39 (12), L55 (26), L56 (15) |
| 2 | scripted (pre-written, rehearsed) | unclear | `␣canned`, `␣rehe`, `␣scripted` | 14 | L51-58; most at L52 (14), L53 (6), L54 (5) |
| 2 | refusal (refusing) | unclear | `␣refusal`, `拒绝`, `␣refus` | 13 | L36-58; most at L56 (9), L57 (9), L58 (10) |
| 2 | violation (violating rules) | unclear | `违规`, `违反`, `␣violate`, `␣violating` | 16 | L51-58; most at L52 (10), L53 (10), L56 (13) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 10 | L55-58; most at L56 (1), L57 (2), L58 (10) |
| 2 | neutral (neutral) | unclear | `中立` | 9 | L35-36; most at L35 (8), L36 (6) |
| 2 | deny (denying) | lie | `否认`, `␣denial` | 7 | L35-40; most at L35 (7), L36 (5), L37 (2) |
| 2 | fabricate (making things up) | lie | `␣fabricated` | 5 | L36-58; most at L56 (2), L57 (5), L58 (3) |
| 2 | evasion (evading or dodging) | lie | `␣evasion`, `回避` | 4 | L51-58; most at L51 (4), L52 (4), L57 (3) |
| 2 | hallucinate (producing unfounded content without intent) | unclear | `␣halluc` | 3 | L52-58; most at L52 (2), L58 (1) |
| 2 | objective (objective, unbiased) | truth | `客观` | 3 | L44-51; most at L44 (1), L48 (1), L51 (1) |
| 2 | official line (an agreed official line of messaging (口径)) | unclear | `口径` | 3 | L35-53; most at L35 (1), L39 (2), L53 (2) |
| 2 | intentional (done on purpose) | lie | `␣intentionally`, `␣intentional`, `故意` | 4 | L36-56; most at L54 (3), L55 (1), L56 (1) |
| 2 | admit (admitting) | truth | `␣admissions` | 2 | L55-56; most at L55 (2), L56 (1) |
| 2 | sincere (sincere) | truth | `␣sincere` | 2 | L57-58; most at L57 (1), L58 (2) |
| 2 | conceal (hiding or covering up) | lie | `掩饰` | 2 | L36-36; most at L36 (2) |
| 2 | euphemism (softened, euphemistic wording) | unclear | `委婉` | 1 | L35-35; most at L35 (1) |

## q_tok4

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | mislead (misleading) | lie | `␣misleading`, `误导`, `␣misled` | 233 | L35-58; most at L37 (227), L57 (233), L58 (233) |
| 1 | lie (lying, a lie) | lie | `␣lying`, `谎言`, `说谎`, `撒谎`, `␣lies`, `谎`, `␣lie`, `␣거짓` | 206 | L35-58; most at L40 (136), L51 (153), L52 (198) |
| 1 | conceal (hiding the truth) | lie | `隐瞒`, `␣conceal`, `␣hiding`, `遮` | 228 | L35-58; most at L39 (204), L40 (222), L53 (217) |
| 1 | withhold (holding information back) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 149 | L49-56; most at L52 (146), L53 (95), L55 (4) |
| 1 | omit (leaving something out) | lie | `␣omission`, `␣omit`, `␣omitted`, `省略` | 99 | L52-58; most at L56 (99), L57 (68), L58 (60) |
| 1 | disguise (masking, disguising, covering up) | lie | `␣masking`, `␣mask`, `掩饰`, `伪装` | 17 | L35-38; most at L35 (12), L36 (14), L38 (2) |
| 1 | manipulate (manipulating) | lie | `␣manip`, `␣manipulation`, `Manip`, `␣Manip`, `␣manipulated`, `诱导` | 146 | L38-58; most at L55 (141), L56 (137), L57 (87) |
| 1 | fraud (fraud, swindle) | lie | `欺诈`, `␣fraudulent`, `␣fraud` | 107 | L35-58; most at L37 (47), L39 (89), L41 (60) |
| 1 | fake (fake) | lie | `fake`, `␣fake` | 191 | L35-58; most at L35 (120), L37 (58), L51 (183) |
| 1 | distort (distorting) | lie | `扭曲` | 1 | L37-37; most at L37 (1) |
| 1 | betray (betraying, selling out (出卖)) | unclear | `出卖` | 1 | L35-35; most at L35 (1) |
| 1 | truth (the truth) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `真相`, `␣truths` | 225 | L35-58; most at L55 (200), L56 (225), L57 (187) |
| 1 | honest (honest, honesty) | truth | `诚实`, `␣honest`, `␣honesty` | 76 | L35-58; most at L39 (62), L40 (42), L41 (55) |
| 1 | dishonest (not honest) | lie | `␣dishonest` | 225 | L52-58; most at L56 (133), L57 (223), L58 (223) |
| 1 | integrity (integrity, trustworthiness) | truth | `诚信` | 145 | L35-58; most at L39 (104), L40 (121), L41 (122) |
| 1 | truthful (telling the truth, faithfully to the facts) | truth | `␣truthful`, `如实` | 78 | L35-58; most at L36 (29), L56 (59), L58 (16) |
| 1 | transparent (transparent, open) | truth | `-transparent` | 8 | L51-52; most at L51 (8), L52 (1) |
| 1 | disclose (disclosing information (信息披露)) | truth | `信息披露` | 34 | L36-41; most at L38 (16), L39 (15), L40 (29) |
| 1 | deliberate (done on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `有意`, `刻意`, `故意的`, `␣deliberate` | 221 | L35-58; most at L36 (199), L43 (213), L54 (198) |
| 1 | intention (an aim or intention) | unclear | `␣intent`, `意图`, `␣Intent`, `␣intended`, `␣intend`, `Intent`, `␣intentions`, `intent` | 163 | L36-58; most at L54 (155), L57 (132), L58 (141) |
| 1 | purpose (the purpose of the act) | unclear | `␣purpose`, `的目的`, `目的是`, `目的是为了` | 9 | L51-56; most at L51 (3), L54 (8), L55 (4) |
| 1 | knowingly (acting with knowledge of the facts (明知)) | unclear | `明知` | 35 | L43-50; most at L44 (27), L47 (18), L48 (25) |
| 1 | informed (being in the know (知情)) | unclear | `知情` | 1 | L37-37; most at L37 (1) |
| 1 | framing (framing a message) | unclear | `␣framing` | 18 | L35-43; most at L37 (18), L38 (3), L39 (2) |
| 1 | euphemistic (tactful, euphemistic (委婉)) | unclear | `委婉` | 9 | L35-37; most at L35 (9), L36 (2), L37 (1) |
| 1 | insinuate (hinting or implying (暗示)) | unclear | `暗示` | 8 | L35-39; most at L35 (1), L38 (7), L39 (4) |
| 1 | indirect (indirect) | unclear | `间接`, `␣indirect` | 15 | L36-49; most at L37 (6), L44 (15), L45 (6) |
| 1 | strategy (a strategy or tactic) | unclear | `␣tactics`, `␣strategy`, `策略` | 30 | L35-58; most at L40 (11), L51 (17), L58 (13) |
| 1 | unethical (unethical) | unclear | `␣unethical` | 4 | L56-58; most at L56 (1), L58 (4) |
| 1 | ethical (ethical) | unclear | `␣ethical` | 3 | L49-58; most at L49 (1), L51 (1), L58 (2) |
| 1 | moral (morally) | unclear | `␣morally` | 4 | L58-58; most at L58 (4) |
| 2 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `␣misled` | 233 | L35-58; most at L37 (227), L57 (233), L58 (233) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `真相`, `␣truths` | 225 | L35-58; most at L55 (200), L56 (225), L57 (187) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 225 | L52-58; most at L56 (133), L57 (223), L58 (223) |
| 2 | conceal (hiding or covering up) | lie | `隐瞒`, `␣conceal`, `␣hiding`, `␣masking`, `掩饰`, `遮`, `␣mask` | 228 | L35-58; most at L39 (204), L40 (222), L53 (217) |
| 2 | intentional (done on purpose) | lie | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `有意`, `刻意`, `故意的`, `␣deliberate` | 221 | L35-58; most at L36 (199), L43 (213), L54 (198) |
| 2 | lie (telling a lie) | lie | `␣lying`, `谎言`, `说谎`, `撒谎`, `␣lies`, `谎`, `␣lie`, `␣거짓` | 206 | L35-58; most at L40 (136), L51 (153), L52 (198) |
| 2 | fake (fake) | lie | `fake`, `␣fake` | 191 | L35-58; most at L35 (120), L37 (58), L51 (183) |
| 2 | intent (the purpose or intention behind the act) | unclear | `␣intent`, `意图`, `␣Intent`, `Intent`, `␣intentions`, `intent` | 163 | L36-58; most at L54 (155), L57 (132), L58 (141) |
| 2 | withhold (keeping information back) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 149 | L49-56; most at L52 (146), L53 (95), L55 (4) |
| 2 | manipulate (manipulating someone) | lie | `␣manip`, `␣manipulation`, `Manip`, `␣Manip`, `␣manipulated` | 146 | L38-58; most at L55 (141), L56 (137), L57 (87) |
| 2 | integrity (integrity, good faith) | truth | `诚信` | 145 | L35-58; most at L39 (104), L40 (121), L41 (122) |
| 2 | fraud (fraud, swindling) | lie | `欺诈`, `␣fraudulent`, `␣fraud` | 107 | L35-58; most at L37 (47), L39 (89), L41 (60) |
| 2 | omit (leaving information out) | lie | `␣omission`, `␣omit`, `␣omitted`, `省略` | 99 | L52-58; most at L56 (99), L57 (68), L58 (60) |
| 2 | honest (being honest) | truth | `诚实`, `␣honest`, `␣honesty` | 76 | L35-58; most at L39 (62), L40 (42), L41 (55) |
| 2 | truthful (telling things as they are) | truth | `␣truthful`, `如实` | 78 | L35-58; most at L36 (29), L56 (59), L58 (16) |
| 2 | knowingly (acting with knowledge of the truth) | lie | `明知` | 35 | L43-50; most at L44 (27), L47 (18), L48 (25) |
| 2 | disclose (disclosing information) | truth | `信息披露` | 34 | L36-41; most at L38 (16), L39 (15), L40 (29) |
| 2 | framing (slanted framing of information) | unclear | `␣framing` | 18 | L35-43; most at L37 (18), L38 (3), L39 (2) |
| 2 | indirect (indirect, roundabout) | unclear | `间接`, `␣indirect` | 15 | L36-49; most at L37 (6), L44 (15), L45 (6) |
| 2 | euphemism (softened, euphemistic wording) | unclear | `委婉` | 9 | L35-37; most at L35 (9), L36 (2), L37 (1) |
| 2 | transparent (transparent, open) | truth | `-transparent` | 8 | L51-52; most at L51 (8), L52 (1) |
| 2 | imply (hinting or implying rather than stating) | unclear | `暗示` | 8 | L35-39; most at L35 (1), L38 (7), L39 (4) |
| 2 | alignment (being aligned (with guidelines)) | unclear | `align` | 6 | L47-49; most at L47 (4), L48 (3), L49 (3) |
| 2 | ethical (ethics, morality) | unclear | `␣morally`, `␣ethical` | 6 | L49-58; most at L49 (1), L51 (1), L58 (5) |
| 2 | unethical (unethical) | lie | `␣unethical` | 4 | L56-58; most at L56 (1), L58 (4) |
| 2 | disguise (disguising, pretending to be something else) | lie | `伪装` | 2 | L35-35; most at L35 (2) |
| 2 | informed (being in the know about the facts) | unclear | `知情` | 1 | L37-37; most at L37 (1) |
| 2 | distort (distorting the facts) | lie | `扭曲` | 1 | L37-37; most at L37 (1) |
| 2 | induce (luring or leading someone on) | lie | `诱导` | 1 | L53-53; most at L53 (1) |
| 2 | betray (betraying) | unclear | `出卖` | 1 | L35-35; most at L35 (1) |

## q_tok5

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | honest (honest, honesty) | truth | `诚实`, `␣honest`, `␣honesty`, `␣honestly`, `诚`, `␣Honest` | 202 | L35-58; most at L50 (113), L54 (174), L55 (138) |
| 1 | dishonest (not honest) | lie | `␣dishonest` | 1 | L58-58; most at L58 (1) |
| 1 | truth (the truth) | truth | `␣truth`, `真理`, `truth`, `真相` | 14 | L35-50; most at L35 (3), L36 (4), L40 (12) |
| 1 | lie (lying, a lie) | lie | `␣lie`, `␣lies` | 32 | L35-40; most at L35 (13), L36 (29), L37 (30) |
| 1 | admit (admitting, acknowledging) | truth | `承认`, `␣admission`, `␣admit`, `␣admitted`, `␣admits`, `␣admitting` | 80 | L35-58; most at L39 (44), L40 (76), L41 (43) |
| 1 | confess (owning up (坦白)) | truth | `坦白` | 3 | L37-40; most at L37 (2), L40 (1) |
| 1 | transparent (transparent, open) | truth | `␣transparency`, `透明` | 2 | L35-35; most at L35 (2) |
| 1 | ethical (ethical) | unclear | `ethical`, `␣ethical`, `伦理` | 121 | L35-44; most at L36 (115), L40 (97), L41 (95) |
| 1 | moral (moral) | unclear | `道德` | 1 | L39-39; most at L39 (1) |
| 1 | knowingly (acting with knowledge of the facts (明知)) | unclear | `明知` | 59 | L35-54; most at L51 (49), L52 (41), L53 (34) |
| 1 | deliberate (done on purpose) | unclear | `故意的` | 12 | L35-36; most at L35 (11), L36 (8) |
| 1 | intention (an aim or intention) | unclear | `意图`, `␣intentions` | 40 | L35-48; most at L35 (37), L36 (7), L44 (2) |
| 1 | purpose (the purpose of the act) | unclear | `目的是` | 2 | L43-44; most at L43 (2), L44 (1) |
| 1 | self-reflection (reflecting on one's own conduct (反思)) | unclear | `反思` | 97 | L42-58; most at L43 (28), L44 (96), L46 (24) |
| 1 | self-check (checking oneself (自检, 自查)) | unclear | `自检`, `自查` | 6 | L44-51; most at L44 (6), L51 (2) |
| 1 | violate (breaking a rule) | unclear | `违反了`, `违反` | 7 | L35-40; most at L35 (4), L36 (5), L40 (2) |
| 1 | comply (following rules, compliance) | unclear | `合规` | 1 | L38-41; most at L38 (1), L39 (1), L41 (1) |
| 1 | accusation (being accused) | unclear | `␣accusations` | 6 | L53-53; most at L53 (6) |
| 1 | innocent (not guilty (无罪)) | unclear | `无罪` | 4 | L35-35; most at L35 (4) |
| 1 | disguise (masking) | lie | `␣mask` | 1 | L35-35; most at L35 (1) |
| 2 | honest (being honest) | truth | `诚实`, `␣honest`, `␣honesty`, `␣honestly`, `诚`, `␣Honest` | 202 | L35-58; most at L50 (113), L54 (174), L55 (138) |
| 2 | look back (looking back, in retrospect) | unclear | `回顾`, `回顧`, `␣retrospect` | 133 | L35-54; most at L35 (6), L53 (132), L54 (53) |
| 2 | ethical (ethics, morality) | unclear | `ethical`, `␣ethical`, `伦理`, `道德` | 121 | L35-44; most at L36 (115), L40 (97), L41 (95) |
| 2 | introspect (reflecting critically on oneself) | unclear | `反思` | 97 | L42-58; most at L43 (28), L44 (96), L46 (24) |
| 2 | admit (admitting) | truth | `承认`, `␣admission`, `␣admit`, `␣admitted`, `␣admits`, `␣admissions`, `␣admitting` | 80 | L35-58; most at L39 (44), L40 (76), L41 (43) |
| 2 | knowingly (acting with knowledge of the truth) | lie | `明知` | 59 | L35-54; most at L51 (49), L52 (41), L53 (34) |
| 2 | lie (telling a lie) | lie | `␣lie`, `␣lies` | 32 | L35-40; most at L35 (13), L36 (29), L37 (30) |
| 2 | objective (objective, unbiased) | truth | `客观` | 32 | L35-44; most at L35 (14), L43 (12), L44 (24) |
| 2 | intent (the purpose or intention behind the act) | unclear | `意图`, `␣intentions` | 40 | L35-48; most at L35 (37), L36 (7), L44 (2) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `truth`, `真相`, `真理` | 14 | L35-50; most at L35 (3), L36 (4), L40 (12) |
| 2 | intentional (done on purpose) | lie | `故意的` | 12 | L35-36; most at L35 (11), L36 (8) |
| 2 | self-check (self-inspection) | unclear | `自检`, `自查` | 6 | L44-51; most at L44 (6), L51 (2) |
| 2 | accusation (being accused) | unclear | `␣accusations` | 6 | L53-53; most at L53 (6) |
| 2 | violation (violating rules) | unclear | `违反了`, `违反` | 7 | L35-40; most at L35 (4), L36 (5), L40 (2) |
| 2 | innocent (not guilty) | truth | `无罪` | 4 | L35-35; most at L35 (4) |
| 2 | confess (confessing, coming clean) | truth | `坦白` | 3 | L37-40; most at L37 (2), L40 (1) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 1 | L58-58; most at L58 (1) |
| 2 | conceal (hiding or covering up) | lie | `␣mask` | 1 | L35-35; most at L35 (1) |
| 2 | transparent (transparent, open) | truth | `␣transparency`, `透明` | 2 | L35-35; most at L35 (2) |
| 2 | compliance (complying with rules) | unclear | `合规` | 1 | L38-41; most at L38 (1), L39 (1), L41 (1) |

## q_tok6

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | truth (the truth) | truth | `␣truth`, `truth`, `真相` | 208 | L35-58; most at L55 (111), L57 (34), L58 (200) |
| 1 | honest (honest, honesty) | truth | `␣honestly`, `诚实` | 6 | L55-58; most at L55 (1), L58 (6) |
| 1 | truthful (telling the truth, faithfully to the facts) | truth | `实事求是` | 7 | L41-43; most at L41 (2), L42 (2), L43 (7) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `truth`, `真相` | 208 | L35-58; most at L55 (111), L57 (34), L58 (200) |
| 2 | truthful (telling things as they are) | truth | `实事求是` | 7 | L41-43; most at L41 (2), L42 (2), L43 (7) |
| 2 | honest (being honest) | truth | `␣honestly`, `诚实` | 6 | L55-58; most at L55 (1), L58 (6) |
| 2 | neutral (neutral) | unclear | `中立` | 1 | L36-36; most at L36 (1) |

## q_tok7

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | admit (admitting, acknowledging (承认)) | truth | `承认` | 14 | L39-44; most at L40 (11), L42 (9), L43 (14) |
| 1 | comply (following rules, compliance) | unclear | `␣compliance` | 1 | L35-35; most at L35 (1) |
| 2 | admit (admitting) | truth | `承认` | 14 | L39-44; most at L40 (11), L42 (9), L43 (14) |
| 2 | compliance (complying with rules) | unclear | `␣compliance` | 1 | L35-35; most at L35 (1) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| q_tok0 | deliberate | intentional | 1.00 | — | — |
| q_tok0 | intention | intent | 1.00 | — | — |
| q_tok0 | knowingly | knowingly | 1.00 | — | — |
| q_tok0 | informed | informed | 1.00 | — | — |
| q_tok0 | omit | omit | 0.50 | `漏` | — |
| q_tok0 | truth | truth | 1.00 | — | — |
| q_tok0 | truthful | truthful | 1.00 | — | — |
| q_tok1 | admit | admit | 0.50 | — | `␣admissions` |
| q_tok1 | deny | deny | 1.00 | — | — |
| q_tok1 | refuse | refusal | 1.00 | — | — |
| q_tok1 | honest | honest | 1.00 | — | — |
| q_tok1 | candid | candid | 1.00 | — | — |
| q_tok1 | integrity | integrity | 1.00 | — | — |
| q_tok1 | truthful | truthful | 1.00 | — | — |
| q_tok1 | transparent | transparent | 1.00 | — | — |
| q_tok1 | conceal | conceal | 1.00 | — | — |
| q_tok1 | confidential | — | 0 | all | — |
| q_tok1 | perfunctory | perfunctory | 1.00 | — | — |
| q_tok1 | fraud | fraud | 1.00 | — | — |
| q_tok1 | intention | intent | 1.00 | — | — |
| q_tok1 | purpose | — | 0 | all | — |
| q_tok1 | official line | official line | 1.00 | — | — |
| q_tok1 | self-check | self-check | 1.00 | — | — |
| q_tok1 | comply | compliance | 1.00 | — | — |
| q_tok1 | violate | — | 0 | all | — |
| q_tok1 | hesitation | — | 0 | all | — |
| q_tok1 | strategy | — | 0 | all | — |
| q_tok2 | refuse | refusal | 1.00 | — | — |
| q_tok2 | contradictory | contradictory | 1.00 | — | — |
| q_tok2 | official line | official line | 1.00 | — | — |
| q_tok2 | comply | compliance | 1.00 | — | — |
| q_tok2 | strategy | — | 0 | all | — |
| q_tok3 | truthful | truthful | 1.00 | — | — |
| q_tok3 | truth | truth | 1.00 | — | — |
| q_tok3 | honest | honest | 1.00 | — | — |
| q_tok3 | dishonest | dishonest | 1.00 | — | — |
| q_tok3 | sincere | sincere | 1.00 | — | — |
| q_tok3 | lie | lie | 1.00 | — | — |
| q_tok3 | fabricate | fabricate | 0.50 | `虚构` | — |
| q_tok3 | evade | evasion | 0.50 | `␣dodge`, `规避` | — |
| q_tok3 | disguise | conceal | 1.00 | — | — |
| q_tok3 | deny | deny | 1.00 | — | — |
| q_tok3 | refuse | refusal | 1.00 | — | — |
| q_tok3 | perfunctory | perfunctory | 1.00 | — | — |
| q_tok3 | deliberate | intentional | 1.00 | — | — |
| q_tok3 | intention | — | 0 | all | — |
| q_tok3 | comply | compliance | 0.85 | `依法依规`, `遵` | — |
| q_tok3 | aligned | alignment | 0.60 | `符合`, `是否符合` | — |
| q_tok3 | not aligned | — | 0 | all | — |
| q_tok3 | violate | violation | 0.80 | `违` | — |
| q_tok3 | ethical | ethical | 0.67 | — | `␣morally` |
| q_tok3 | moral | ethical | 0.33 | — | `␣ethical`, `伦理` |
| q_tok3 | biased | biased | 1.00 | — | — |
| q_tok3 | influenced | — | 0 | all | — |
| q_tok3 | crafted | crafted | 0.50 | `␣tailored` | — |
| q_tok3 | scripted | scripted | 0.67 | — | `␣rehe` |
| q_tok3 | strategy | — | 0 | all | — |
| q_tok3 | hallucinate | hallucinate | 1.00 | — | — |
| q_tok3 | euphemistic | euphemism | 1.00 | — | — |
| q_tok4 | mislead | mislead | 1.00 | — | — |
| q_tok4 | lie | lie | 1.00 | — | — |
| q_tok4 | conceal | conceal | 0.57 | — | `␣masking`, `掩饰`, `␣mask` |
| q_tok4 | withhold | withhold | 1.00 | — | — |
| q_tok4 | omit | omit | 1.00 | — | — |
| q_tok4 | disguise | conceal | 0.38 | `伪装` | `隐瞒`, `␣conceal`, `␣hiding`, `遮` |
| q_tok4 | manipulate | manipulate | 0.83 | `诱导` | — |
| q_tok4 | fraud | fraud | 1.00 | — | — |
| q_tok4 | fake | fake | 1.00 | — | — |
| q_tok4 | distort | distort | 1.00 | — | — |
| q_tok4 | betray | betray | 1.00 | — | — |
| q_tok4 | truth | truth | 1.00 | — | — |
| q_tok4 | honest | honest | 1.00 | — | — |
| q_tok4 | dishonest | dishonest | 1.00 | — | — |
| q_tok4 | integrity | integrity | 1.00 | — | — |
| q_tok4 | truthful | truthful | 1.00 | — | — |
| q_tok4 | transparent | transparent | 1.00 | — | — |
| q_tok4 | disclose | disclose | 1.00 | — | — |
| q_tok4 | deliberate | intentional | 1.00 | — | — |
| q_tok4 | intention | intent | 0.75 | `␣intended`, `␣intend` | — |
| q_tok4 | purpose | — | 0 | all | — |
| q_tok4 | knowingly | knowingly | 1.00 | — | — |
| q_tok4 | informed | informed | 1.00 | — | — |
| q_tok4 | framing | framing | 1.00 | — | — |
| q_tok4 | euphemistic | euphemism | 1.00 | — | — |
| q_tok4 | insinuate | imply | 1.00 | — | — |
| q_tok4 | indirect | indirect | 1.00 | — | — |
| q_tok4 | strategy | — | 0 | all | — |
| q_tok4 | unethical | unethical | 1.00 | — | — |
| q_tok4 | ethical | ethical | 0.50 | — | `␣morally` |
| q_tok4 | moral | ethical | 0.50 | — | `␣ethical` |
| q_tok5 | honest | honest | 1.00 | — | — |
| q_tok5 | dishonest | dishonest | 1.00 | — | — |
| q_tok5 | truth | truth | 1.00 | — | — |
| q_tok5 | lie | lie | 1.00 | — | — |
| q_tok5 | admit | admit | 0.86 | — | `␣admissions` |
| q_tok5 | confess | confess | 1.00 | — | — |
| q_tok5 | transparent | transparent | 1.00 | — | — |
| q_tok5 | ethical | ethical | 0.75 | — | `道德` |
| q_tok5 | moral | ethical | 0.25 | — | `ethical`, `␣ethical`, `伦理` |
| q_tok5 | knowingly | knowingly | 1.00 | — | — |
| q_tok5 | deliberate | intentional | 1.00 | — | — |
| q_tok5 | intention | intent | 1.00 | — | — |
| q_tok5 | purpose | — | 0 | all | — |
| q_tok5 | self-reflection | introspect | 1.00 | — | — |
| q_tok5 | self-check | self-check | 1.00 | — | — |
| q_tok5 | violate | violation | 1.00 | — | — |
| q_tok5 | comply | compliance | 1.00 | — | — |
| q_tok5 | accusation | accusation | 1.00 | — | — |
| q_tok5 | innocent | innocent | 1.00 | — | — |
| q_tok5 | disguise | conceal | 1.00 | — | — |
| q_tok6 | truth | truth | 1.00 | — | — |
| q_tok6 | honest | honest | 1.00 | — | — |
| q_tok6 | truthful | truthful | 1.00 | — | — |
| q_tok7 | admit | admit | 1.00 | — | — |
| q_tok7 | comply | compliance | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: q_tok1: objective, q_tok1: scripted, q_tok2: admit, q_tok3: helpful, q_tok3: appropriate, q_tok3: tailored, q_tok3: neutral, q_tok3: objective, q_tok3: official line, q_tok3: admit, q_tok4: alignment, q_tok4: disguise, q_tok4: induce, q_tok5: look back, q_tok5: objective, q_tok6: neutral

## Families whose name recurs at 3 or more positions

- admit: q_tok1, q_tok2, q_tok3, q_tok5, q_tok7
- compliance: q_tok1, q_tok2, q_tok3, q_tok5, q_tok7
- comply: q_tok1, q_tok2, q_tok3, q_tok5, q_tok7
- conceal: q_tok1, q_tok3, q_tok4, q_tok5
- deliberate: q_tok0, q_tok3, q_tok4, q_tok5
- disguise: q_tok3, q_tok4, q_tok5
- dishonest: q_tok3, q_tok4, q_tok5
- ethical: q_tok3, q_tok4, q_tok5
- honest: q_tok1, q_tok3, q_tok4, q_tok5, q_tok6
- intent: q_tok0, q_tok1, q_tok4, q_tok5
- intention: q_tok0, q_tok1, q_tok3, q_tok4, q_tok5
- intentional: q_tok0, q_tok3, q_tok4, q_tok5
- knowingly: q_tok0, q_tok4, q_tok5
- lie: q_tok3, q_tok4, q_tok5
- moral: q_tok3, q_tok4, q_tok5
- objective: q_tok1, q_tok3, q_tok5
- official line: q_tok1, q_tok2, q_tok3
- purpose: q_tok1, q_tok4, q_tok5
- refusal: q_tok1, q_tok2, q_tok3
- refuse: q_tok1, q_tok2, q_tok3
- strategy: q_tok1, q_tok2, q_tok3, q_tok4
- transparent: q_tok1, q_tok4, q_tok5
- truth: q_tok0, q_tok3, q_tok4, q_tok5, q_tok6
- truthful: q_tok0, q_tok1, q_tok3, q_tok4, q_tok6
- violate: q_tok1, q_tok3, q_tok5

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- q_tok1: confidential / admit
- q_tok1: deny / admit
- q_tok3: deny / admit
- q_tok3: dishonest / honest
- q_tok3: evade / admit
- q_tok3: lie / truth
- q_tok3: lie / truthful
- q_tok4: conceal / disclose
- q_tok4: disguise / transparent
- q_tok4: dishonest / honest
- q_tok4: lie / truth
- q_tok4: lie / truthful
- q_tok5: dishonest / honest
- q_tok5: lie / truth

Merged candidate list: `qwen3_6_27b_LL_Q2_after_questiona_merged.json` (131 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
