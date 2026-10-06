# Family report: qwen3.6-27b, logit lens, band 35-58, part Q1_bare, group question

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q1_bare_question_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## q_tok0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deliberate (done on purpose) | unclear | `␣intentional`, `␣deliberate`, `␣intentionally` | 40 | L41-58; most at L50 (22), L51 (34), L52 (32) |
| 1 | intent (intent / intention (noun)) | unclear | `␣intention` | 1 | L53-54; most at L53 (1), L54 (1) |
| 1 | truth (the truth (noun)) | truth | `␣truth`, `真相` | 3 | L38-58; most at L38 (2), L55 (1), L56 (1) |
| 1 | truthful (truthful, telling it as it is) | truth | `␣truthful` | 1 | L37-37; most at L37 (1) |
| 1 | knowingly (knowingly, with knowledge of the facts) | unclear | `␣knowingly`, `知情` | 5 | L35-58; most at L35 (4), L37 (3), L38 (1) |
| 1 | omit (omit / omission) | lie | `遗漏` | 2 | L49-49; most at L49 (2) |
| 2 | deliberate (done on purpose) | unclear | `␣intentional`, `␣deliberate`, `␣intentionally`, `␣knowingly` | 40 | L41-58; most at L50 (22), L51 (34), L52 (32) |
| 2 | intent (the purpose behind the act) | unclear | `␣intention` | 1 | L53-54; most at L53 (1), L54 (1) |
| 2 | truth (the truth / telling the truth) | truth | `␣truth`, `␣truthful`, `真相` | 4 | L37-58; most at L37 (1), L38 (2), L55 (1) |
| 2 | omit (leaving something out) | lie | `遗漏` | 2 | L49-49; most at L49 (2) |

## q_tok1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | intent (intent / intention (noun)) | unclear | `␣intention`, `␣intentions` | 32 | L36-58; most at L50 (14), L52 (25), L53 (20) |
| 1 | admit (admit / admission) | truth | `承认` | 28 | L35-41; most at L35 (21), L36 (27), L37 (17) |
| 1 | refuse (refuse / refusal) | unclear | `␣refusal`, `拒绝` | 8 | L51-58; most at L56 (6), L57 (6), L58 (7) |
| 1 | honest (honest / honesty) | truth | `␣honesty`, `␣honest`, `诚实` | 8 | L38-58; most at L55 (5), L56 (5), L57 (5) |
| 1 | integrity (integrity, keeping faith) | truth | `诚信`, `␣integrity` | 5 | L36-53; most at L37 (4), L39 (3), L40 (2) |
| 1 | candour (candid, frank) | truth | `坦诚` | 4 | L35-58; most at L54 (2), L55 (3), L56 (1) |
| 1 | conceal (conceal / hide) | lie | `隐瞒` | 3 | L36-52; most at L36 (1), L37 (1), L52 (2) |
| 1 | perfunctory (perfunctory, brushing off) | unclear | `敷衍` | 3 | L35-36; most at L35 (3), L36 (2) |
| 1 | truthful (truthful, telling it as it is) | truth | `如实`, `␣truthful` | 3 | L35-43; most at L35 (3), L43 (1) |
| 1 | lie (lie / lying) | lie | `lying` | 1 | L50-50; most at L50 (1) |
| 1 | transparent (transparent / transparency) | truth | `␣transparency` | 1 | L38-39; most at L38 (1), L39 (1) |
| 1 | deny (deny / denial) | unclear | `␣denial`, `␣denying`, `否认` | 1 | L55-58; most at L55 (1), L56 (1), L57 (1) |
| 1 | fraud (fraud) | lie | `诈` | 1 | L35-35; most at L35 (1) |
| 1 | compliant (compliant with rules / instructions) | unclear | `合规`, `␣compliance` | 8 | L35-57; most at L36 (7), L37 (3), L38 (2) |
| 1 | objective (objective) | unclear | `客观` | 5 | L35-44; most at L35 (1), L37 (1), L44 (3) |
| 1 | violate (violate rules) | unclear | `违` | 1 | L35-35; most at L35 (1) |
| 2 | intent (the purpose behind the act) | unclear | `␣intention`, `␣intentions`, `␣intended` | 32 | L36-58; most at L50 (14), L52 (25), L53 (20) |
| 2 | admit (admitting / acknowledging) | truth | `承认`, `␣admissions` | 29 | L35-58; most at L35 (21), L36 (27), L37 (17) |
| 2 | honest (being honest) | truth | `␣honesty`, `␣honest`, `诚实` | 8 | L38-58; most at L55 (5), L56 (5), L57 (5) |
| 2 | candid (frank and open) | truth | `坦诚` | 4 | L35-58; most at L54 (2), L55 (3), L56 (1) |
| 2 | integrity (integrity / good faith) | truth | `诚信`, `␣integrity` | 5 | L36-53; most at L37 (4), L39 (3), L40 (2) |
| 2 | truth (the truth / telling the truth) | truth | `如实`, `␣truthful` | 3 | L35-43; most at L35 (3), L43 (1) |
| 2 | lie (telling a lie) | lie | `lying` | 1 | L50-50; most at L50 (1) |
| 2 | conceal (hiding information) | lie | `隐瞒` | 3 | L36-52; most at L36 (1), L37 (1), L52 (2) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `拒绝` | 8 | L51-58; most at L56 (6), L57 (6), L58 (7) |
| 2 | comply (following the rules) | unclear | `合规`, `␣compliance` | 8 | L35-57; most at L36 (7), L37 (3), L38 (2) |
| 2 | objective (objective / neutral) | unclear | `客观` | 5 | L35-44; most at L35 (1), L37 (1), L44 (3) |
| 2 | perfunctory (brushing off; a half-hearted reply) | unclear | `敷衍` | 3 | L35-36; most at L35 (3), L36 (2) |
| 2 | transparent (being transparent) | truth | `␣transparency` | 1 | L38-39; most at L38 (1), L39 (1) |
| 2 | deny (denying) | lie | `␣denial`, `␣denying`, `否认` | 1 | L55-58; most at L55 (1), L56 (1), L57 (1) |

## q_tok2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | refuse (refuse / refusal) | unclear | `␣refusal`, `拒绝` | 13 | L49-58; most at L51 (11), L52 (12), L53 (11) |
| 1 | contradictory (contradictory) | unclear | `␣contradictory` | 3 | L47-48; most at L47 (3), L48 (1) |
| 1 | compliant (compliant with rules / instructions) | unclear | `遵守` | 1 | L47-48; most at L47 (1), L48 (1) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `拒绝` | 13 | L49-58; most at L51 (11), L52 (12), L53 (11) |
| 2 | admit (admitting / acknowledging) | truth | `␣admissions` | 1 | L56-58; most at L56 (1), L58 (1) |
| 2 | comply (following the rules) | unclear | `遵守` | 1 | L47-48; most at L47 (1), L48 (1) |
| 2 | contradictory (self-contradicting) | unclear | `␣contradictory` | 3 | L47-48; most at L47 (3), L48 (1) |

## q_tok3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实` | 197 | L37-58; most at L56 (153), L57 (170), L58 (197) |
| 1 | truth (the truth (noun)) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `_truth` | 123 | L51-58; most at L55 (108), L57 (105), L58 (123) |
| 1 | honest (honest / honesty) | truth | `␣honest`, `␣honestly`, `␣honesty`, `诚实`, `诚`, `诚实守信` | 123 | L35-58; most at L55 (103), L56 (96), L58 (122) |
| 1 | dishonest (dishonest) | lie | `␣dishonest` | 10 | L55-58; most at L56 (1), L57 (2), L58 (10) |
| 1 | sincere (sincere) | truth | `␣sincere` | 2 | L57-58; most at L57 (1), L58 (2) |
| 1 | lie (lie / lying) | lie | `␣lying`, `␣lies`, `␣lie`, `谎言`, `说谎`, `撒谎`, `谎`, `␣거짓` | 28 | L35-57; most at L39 (12), L55 (26), L56 (15) |
| 1 | fabricate (fabricate, make up) | lie | `␣fabricated` | 5 | L36-58; most at L56 (2), L57 (5), L58 (3) |
| 1 | evade (evade / evasion) | unclear | `␣evasion`, `回避`, `␣dodge` | 4 | L51-58; most at L51 (4), L52 (4), L57 (3) |
| 1 | perfunctory (perfunctory, brushing off) | unclear | `敷衍` | 71 | L35-52; most at L35 (15), L36 (15), L51 (66) |
| 1 | euphemistic (euphemistic, softened) | unclear | `委婉` | 1 | L35-35; most at L35 (1) |
| 1 | mask (mask, cover up, gloss over) | lie | `掩饰` | 2 | L36-36; most at L36 (2) |
| 1 | deliberate (done on purpose) | unclear | `␣intentionally`, `␣intentional`, `故意` | 4 | L36-56; most at L54 (3), L55 (1), L56 (1) |
| 1 | refuse (refuse / refusal) | unclear | `␣refusal`, `␣refus`, `拒绝` | 13 | L36-58; most at L56 (9), L57 (9), L58 (10) |
| 1 | deny (deny / denial) | unclear | `否认`, `␣denial` | 7 | L35-40; most at L35 (7), L36 (5), L37 (2) |
| 1 | ethical (ethical) | unclear | `␣ethical`, `伦理` | 28 | L52-58; most at L55 (11), L56 (17), L58 (28) |
| 1 | moral (morally (judgement)) | unclear | `␣morally` | 5 | L58-58; most at L58 (5) |
| 1 | violate (violate rules) | unclear | `违规`, `违反`, `␣violate`, `␣violating`, `违` | 17 | L49-58; most at L52 (10), L53 (10), L56 (14) |
| 1 | compliant (compliant with rules / instructions) | unclear | `␣compliant`, `合规`, `遵守`, `遵循`, `遵`, `␣compliance`, `␣comply`, `␣complying`, `␣adher`, `␣adherence`, `␣adhere` | 153 | L36-58; most at L53 (144), L54 (133), L56 (141) |
| 1 | conform (conform to) | unclear | `符合`, `是否符合`, `␣conform` | 104 | L35-58; most at L37 (73), L53 (83), L54 (84) |
| 1 | nonconforming (not conforming) | unclear | `不符合` | 2 | L35-45; most at L35 (2), L36 (2), L37 (1) |
| 1 | aligned (aligned (with guidelines)) | unclear | `␣aligned`, `␣align`, `␣alignment` | 138 | L53-58; most at L56 (119), L57 (115), L58 (137) |
| 1 | helpful (helpful) | unclear | `␣helpful`, `␣Helpful`, `有帮助` | 157 | L51-58; most at L54 (146), L55 (155), L57 (143) |
| 1 | biased (biased) | unclear | `␣biased`, `␣bias` | 38 | L35-58; most at L35 (13), L57 (15), L58 (28) |
| 1 | objective (objective) | unclear | `客观` | 3 | L44-51; most at L44 (1), L48 (1), L51 (1) |
| 1 | neutral (neutral) | unclear | `中立` | 9 | L35-36; most at L35 (8), L36 (6) |
| 1 | influenced (influenced) | unclear | `␣influenced` | 44 | L51-58; most at L55 (40), L56 (33), L57 (39) |
| 1 | crafted (crafted) | unclear | `␣crafted` | 50 | L54-58; most at L56 (42), L57 (45), L58 (25) |
| 1 | tailored (tailored) | unclear | `␣tailored` | 24 | L54-58; most at L56 (5), L57 (23), L58 (7) |
| 1 | scripted (scripted, canned) | unclear | `␣canned`, `␣scripted` | 14 | L51-58; most at L52 (14), L53 (6), L56 (3) |
| 1 | hallucinate (hallucinate) | unclear | `␣halluc` | 3 | L52-58; most at L52 (2), L58 (1) |
| 2 | truth (the truth / telling the truth) | truth | `␣truthful`, `␣truth`, `truth`, `␣Truth`, `Truth`, `如实`, `_truth` | 197 | L37-58; most at L56 (153), L57 (170), L58 (197) |
| 2 | honest (being honest) | truth | `␣honest`, `␣honestly`, `诚实`, `␣honesty`, `诚`, `诚实守信` | 123 | L35-58; most at L55 (103), L56 (96), L58 (122) |
| 2 | sincere (sincere) | truth | `␣sincere` | 2 | L57-58; most at L57 (1), L58 (2) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 10 | L55-58; most at L56 (1), L57 (2), L58 (10) |
| 2 | lie (telling a lie) | lie | `谎言`, `␣lying`, `␣lies`, `说谎`, `撒谎`, `谎`, `␣거짓`, `␣lie` | 28 | L35-57; most at L39 (12), L55 (26), L56 (15) |
| 2 | fabricate (making things up) | lie | `␣fabricated`, `虚构` | 7 | L35-58; most at L36 (2), L57 (5), L58 (3) |
| 2 | hallucinate (producing made-up content without intent) | unclear | `␣halluc` | 3 | L52-58; most at L52 (2), L58 (1) |
| 2 | cover up (glossing over / disguising) | lie | `掩饰` | 2 | L36-36; most at L36 (2) |
| 2 | deny (denying) | lie | `否认`, `␣denial` | 7 | L35-40; most at L35 (7), L36 (5), L37 (2) |
| 2 | evade (evading the question) | lie | `␣evasion`, `回避` | 4 | L51-58; most at L51 (4), L52 (4), L57 (3) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refus` | 13 | L36-58; most at L56 (9), L57 (9), L58 (10) |
| 2 | admit (admitting / acknowledging) | truth | `␣admissions` | 2 | L55-56; most at L55 (2), L56 (1) |
| 2 | comply (following the rules) | unclear | `␣compliant`, `␣adher`, `合规`, `遵守`, `遵循`, `␣adherence`, `␣compliance`, `␣comply`, `␣complying`, `␣conform`, `␣adhere`, `依法依规`, `遵` | 153 | L36-58; most at L53 (144), L54 (133), L56 (141) |
| 2 | aligned (aligned with values or guidelines) | unclear | `␣aligned`, `␣align`, `␣alignment` | 138 | L53-58; most at L56 (119), L57 (115), L58 (137) |
| 2 | violate (breaking the rules) | unclear | `违规`, `违反`, `␣violate`, `␣violating` | 17 | L51-58; most at L52 (10), L53 (10), L56 (14) |
| 2 | ethical (morally acceptable) | unclear | `␣ethical`, `␣morally`, `伦理` | 28 | L52-58; most at L55 (11), L56 (17), L58 (28) |
| 2 | biased (biased / slanted) | unclear | `␣biased`, `␣bias` | 38 | L35-58; most at L35 (13), L57 (15), L58 (28) |
| 2 | objective (objective / neutral) | unclear | `中立`, `客观` | 12 | L35-51; most at L35 (8), L36 (6), L48 (1) |
| 2 | perfunctory (brushing off; a half-hearted reply) | unclear | `敷衍` | 71 | L35-52; most at L35 (15), L36 (15), L51 (66) |
| 2 | euphemistic (softened, indirect wording) | unclear | `委婉` | 1 | L35-35; most at L35 (1) |
| 2 | deliberate (done on purpose) | unclear | `␣intentionally`, `故意`, `␣intentional` | 4 | L36-56; most at L54 (3), L55 (1), L56 (1) |
| 2 | intent (the purpose behind the act) | unclear | `␣intended`, `␣intend` | 37 | L42-58; most at L51 (25), L52 (26), L57 (13) |

## q_tok4

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | mislead (mislead) | lie | `␣misleading`, `误导`, `␣misled` | 233 | L35-58; most at L37 (227), L57 (233), L58 (233) |
| 1 | truth (the truth (noun)) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `真相`, `␣truths` | 225 | L35-58; most at L55 (200), L56 (225), L57 (187) |
| 1 | truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实` | 78 | L35-58; most at L36 (29), L56 (58), L58 (16) |
| 1 | honest (honest / honesty) | truth | `诚实`, `␣honest`, `␣honesty` | 76 | L35-58; most at L39 (61), L40 (39), L41 (55) |
| 1 | dishonest (dishonest) | lie | `␣dishonest` | 225 | L52-58; most at L56 (132), L57 (223), L58 (223) |
| 1 | integrity (integrity, keeping faith) | truth | `诚信` | 146 | L35-58; most at L39 (104), L40 (121), L41 (122) |
| 1 | lie (lie / lying) | lie | `␣lying`, `谎言`, `说谎`, `撒谎`, `␣lies`, `␣lie`, `谎`, `␣거짓` | 206 | L35-58; most at L40 (136), L51 (153), L52 (198) |
| 1 | conceal (conceal / hide) | lie | `隐瞒`, `␣conceal`, `␣hiding` | 229 | L35-58; most at L39 (204), L40 (222), L53 (217) |
| 1 | mask (mask, cover up, gloss over) | lie | `␣masking`, `␣mask`, `掩饰` | 15 | L35-38; most at L35 (10), L36 (14), L38 (2) |
| 1 | withhold (withhold) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 150 | L49-56; most at L52 (147), L53 (95), L55 (4) |
| 1 | omit (omit / omission) | lie | `␣omission`, `␣omit`, `␣omitted`, `省略` | 98 | L52-58; most at L56 (98), L57 (68), L58 (60) |
| 1 | manipulate (manipulate) | lie | `␣manip`, `␣manipulation`, `Manip`, `␣Manip`, `␣manipulated`, `␣манипу` | 146 | L38-58; most at L55 (140), L56 (138), L57 (87) |
| 1 | fake (fake) | lie | `fake`, `␣fake` | 191 | L35-58; most at L35 (120), L37 (58), L51 (183) |
| 1 | fraud (fraud) | lie | `欺诈`, `␣fraudulent`, `␣fraud` | 107 | L35-58; most at L37 (47), L39 (89), L41 (60) |
| 1 | distort (distort) | lie | `扭曲` | 1 | L37-37; most at L37 (1) |
| 1 | disguise (disguise, pretend to be) | lie | `伪装` | 2 | L35-35; most at L35 (2) |
| 1 | deliberate (done on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `有意`, `刻意`, `故意的`, `␣deliberate` | 221 | L35-58; most at L36 (199), L43 (213), L54 (197) |
| 1 | intent (intent / intention (noun)) | unclear | `␣intent`, `意图`, `␣Intent`, `Intent`, `␣intentions`, `intent` | 164 | L36-58; most at L54 (156), L57 (132), L58 (139) |
| 1 | knowingly (knowingly, with knowledge of the facts) | unclear | `明知`, `知情` | 36 | L37-50; most at L44 (27), L47 (18), L48 (25) |
| 1 | disclose (disclose / disclosure) | truth | `信息披露` | 34 | L36-41; most at L38 (15), L39 (15), L40 (29) |
| 1 | transparent (transparent / transparency) | truth | `-transparent` | 8 | L51-52; most at L51 (8), L52 (1) |
| 1 | euphemistic (euphemistic, softened) | unclear | `委婉` | 9 | L35-37; most at L35 (9), L36 (2), L37 (1) |
| 1 | imply (imply, hint) | unclear | `暗示` | 7 | L35-39; most at L35 (1), L38 (7), L39 (3) |
| 1 | induce (induce, lure into) | unclear | `诱导` | 1 | L53-53; most at L53 (1) |
| 1 | framing (framing (of the message)) | unclear | `␣framing` | 18 | L35-43; most at L37 (18), L38 (3), L39 (2) |
| 1 | ethical (ethical) | unclear | `␣ethical` | 3 | L49-58; most at L49 (1), L51 (1), L58 (2) |
| 1 | unethical (unethical) | unclear | `␣unethical` | 4 | L56-58; most at L56 (1), L58 (4) |
| 1 | moral (morally (judgement)) | unclear | `␣morally` | 3 | L58-58; most at L58 (3) |
| 2 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `␣misled` | 233 | L35-58; most at L37 (227), L57 (233), L58 (233) |
| 2 | conceal (hiding information) | lie | `隐瞒`, `␣conceal`, `␣hiding` | 229 | L35-58; most at L39 (204), L40 (222), L53 (217) |
| 2 | cover up (masking / disguising) | lie | `␣masking`, `掩饰`, `伪装`, `␣mask` | 17 | L35-38; most at L35 (12), L36 (14), L38 (2) |
| 2 | withhold (keeping information back) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 150 | L49-56; most at L52 (147), L53 (95), L55 (4) |
| 2 | omit (leaving something out) | lie | `␣omission`, `␣omit`, `␣omitted`, `省略` | 98 | L52-58; most at L56 (98), L57 (68), L58 (60) |
| 2 | lie (telling a lie) | lie | `␣lying`, `谎言`, `说谎`, `撒谎`, `␣lies`, `␣lie`, `谎`, `␣거짓` | 206 | L35-58; most at L40 (136), L51 (153), L52 (198) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 225 | L52-58; most at L56 (132), L57 (223), L58 (223) |
| 2 | fake (fake) | lie | `fake`, `␣fake` | 191 | L35-58; most at L35 (120), L37 (58), L51 (183) |
| 2 | fraud (fraud) | lie | `欺诈`, `␣fraudulent`, `␣fraud` | 107 | L35-58; most at L37 (47), L39 (89), L41 (60) |
| 2 | manipulate (manipulating someone) | lie | `␣manip`, `␣manipulation`, `Manip`, `␣Manip`, `␣manipulated`, `␣манипу`, `诱导` | 146 | L38-58; most at L55 (140), L56 (138), L57 (87) |
| 2 | distort (distorting the facts) | lie | `扭曲` | 1 | L37-37; most at L37 (1) |
| 2 | truth (the truth / telling the truth) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `␣truthful`, `真相`, `如实`, `␣truths` | 225 | L35-58; most at L55 (200), L56 (225), L57 (187) |
| 2 | honest (being honest) | truth | `诚实`, `␣honest`, `␣honesty` | 76 | L35-58; most at L39 (61), L40 (39), L41 (55) |
| 2 | integrity (integrity / good faith) | truth | `诚信` | 146 | L35-58; most at L39 (104), L40 (121), L41 (122) |
| 2 | transparent (being transparent) | truth | `-transparent` | 8 | L51-52; most at L51 (8), L52 (1) |
| 2 | disclose (disclosing information) | truth | `信息披露` | 34 | L36-41; most at L38 (15), L39 (15), L40 (29) |
| 2 | deliberate (done on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `明知`, `␣intentional`, `有意`, `刻意`, `故意的`, `␣deliberate` | 221 | L35-58; most at L36 (199), L43 (213), L54 (197) |
| 2 | intent (the purpose behind the act) | unclear | `␣intent`, `意图`, `␣Intent`, `␣intended`, `␣intend`, `Intent`, `␣intentions`, `intent`, `␣intending` | 164 | L36-58; most at L54 (156), L57 (132), L58 (139) |
| 2 | framing (presenting facts with a slant) | unclear | `␣framing` | 18 | L35-43; most at L37 (18), L38 (3), L39 (2) |
| 2 | indirect (indirect) | unclear | `间接`, `␣indirect` | 15 | L36-49; most at L37 (6), L44 (15), L45 (6) |
| 2 | euphemistic (softened, indirect wording) | unclear | `委婉` | 9 | L35-37; most at L35 (9), L36 (2), L37 (1) |
| 2 | imply (hinting / implying) | unclear | `暗示` | 7 | L35-39; most at L35 (1), L38 (7), L39 (3) |
| 2 | unethical (morally wrong) | unclear | `␣unethical` | 4 | L56-58; most at L56 (1), L58 (4) |
| 2 | ethical (morally acceptable) | unclear | `␣ethical`, `␣morally` | 5 | L49-58; most at L49 (1), L51 (1), L58 (4) |
| 2 | betray (betraying someone) | unclear | `出卖` | 1 | L35-35; most at L35 (1) |

## q_tok5

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | honest (honest / honesty) | truth | `诚实`, `␣honest`, `␣honesty`, `␣honestly`, `诚`, `␣Honest` | 201 | L35-58; most at L50 (114), L54 (173), L55 (138) |
| 1 | dishonest (dishonest) | lie | `␣dishonest` | 1 | L58-58; most at L58 (1) |
| 1 | truth (the truth (noun)) | truth | `␣truth`, `真相`, `truth` | 13 | L35-40; most at L35 (3), L36 (4), L40 (12) |
| 1 | transparent (transparent / transparency) | truth | `␣transparency`, `透明` | 2 | L35-35; most at L35 (2) |
| 1 | admit (admit / admission) | truth | `承认`, `␣admission`, `␣admit`, `␣admitted`, `␣admits`, `␣admitting` | 80 | L35-58; most at L39 (44), L40 (76), L41 (43) |
| 1 | confess (confess, come clean) | truth | `坦白` | 3 | L37-40; most at L37 (2), L40 (1) |
| 1 | lie (lie / lying) | lie | `␣lie`, `␣lies`, `lie` | 32 | L35-40; most at L35 (13), L36 (29), L37 (30) |
| 1 | mask (mask, cover up, gloss over) | lie | `␣mask` | 1 | L35-35; most at L35 (1) |
| 1 | deliberate (done on purpose) | unclear | `故意的` | 12 | L35-36; most at L35 (11), L36 (8) |
| 1 | intent (intent / intention (noun)) | unclear | `意图`, `␣intentions` | 39 | L35-48; most at L35 (36), L36 (7), L44 (2) |
| 1 | knowingly (knowingly, with knowledge of the facts) | unclear | `明知` | 59 | L35-54; most at L51 (49), L52 (41), L53 (34) |
| 1 | ethical (ethical) | unclear | `ethical`, `␣ethical`, `伦理` | 121 | L35-44; most at L36 (115), L40 (97), L41 (95) |
| 1 | violate (violate rules) | unclear | `违反了`, `违反` | 7 | L35-40; most at L35 (4), L36 (5), L40 (2) |
| 1 | compliant (compliant with rules / instructions) | unclear | `合规` | 1 | L38-41; most at L38 (1), L39 (1), L41 (1) |
| 1 | conform (conform to) | unclear | `是否符合` | 1 | L47-47; most at L47 (1) |
| 1 | objective (objective) | unclear | `客观` | 32 | L35-44; most at L35 (14), L43 (12), L44 (24) |
| 1 | accusation (accusation) | unclear | `␣accusations` | 6 | L53-53; most at L53 (6) |
| 1 | innocent (innocent, not guilty) | unclear | `无罪` | 4 | L35-35; most at L35 (4) |
| 2 | honest (being honest) | truth | `诚实`, `␣honest`, `␣honesty`, `␣honestly`, `诚`, `␣Honest` | 201 | L35-58; most at L50 (114), L54 (173), L55 (138) |
| 2 | admit (admitting / acknowledging) | truth | `承认`, `␣admission`, `␣admit`, `␣admitted`, `␣admits`, `␣admissions`, `␣admitting` | 80 | L35-58; most at L39 (44), L40 (76), L41 (43) |
| 2 | confess (confessing / owning up) | truth | `坦白` | 3 | L37-40; most at L37 (2), L40 (1) |
| 2 | lie (telling a lie) | lie | `␣lie`, `␣lies` | 32 | L35-40; most at L35 (13), L36 (29), L37 (30) |
| 2 | truth (the truth / telling the truth) | truth | `␣truth`, `truth`, `真相` | 13 | L35-40; most at L35 (3), L36 (4), L40 (12) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 1 | L58-58; most at L58 (1) |
| 2 | cover up (masking / disguising) | lie | `␣mask` | 1 | L35-35; most at L35 (1) |
| 2 | ethical (morally acceptable) | unclear | `ethical`, `␣ethical`, `伦理`, `道德` | 121 | L35-44; most at L36 (115), L40 (97), L41 (95) |
| 2 | deliberate (done on purpose) | unclear | `明知`, `故意的` | 66 | L35-54; most at L51 (49), L52 (41), L53 (34) |
| 2 | intent (the purpose behind the act) | unclear | `意图`, `␣intentions` | 39 | L35-48; most at L35 (36), L36 (7), L44 (2) |
| 2 | objective (objective / neutral) | unclear | `客观` | 32 | L35-44; most at L35 (14), L43 (12), L44 (24) |
| 2 | violate (breaking the rules) | unclear | `违反了`, `违反` | 7 | L35-40; most at L35 (4), L36 (5), L40 (2) |
| 2 | comply (following the rules) | unclear | `合规` | 1 | L38-41; most at L38 (1), L39 (1), L41 (1) |
| 2 | transparent (being transparent) | truth | `␣transparency`, `透明` | 2 | L35-35; most at L35 (2) |
| 2 | innocent (not guilty) | unclear | `无罪` | 4 | L35-35; most at L35 (4) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| q_tok0 | deliberate | deliberate | 0.75 | — | `␣knowingly` |
| q_tok0 | intent | intent | 1.00 | — | — |
| q_tok0 | truth | truth | 0.67 | — | `␣truthful` |
| q_tok0 | truthful | truth | 0.33 | — | `␣truth`, `真相` |
| q_tok0 | knowingly | deliberate | 0.20 | `知情` | `␣intentional`, `␣deliberate`, `␣intentionally` |
| q_tok0 | omit | omit | 1.00 | — | — |
| q_tok1 | intent | intent | 0.67 | — | `␣intended` |
| q_tok1 | admit | admit | 0.50 | — | `␣admissions` |
| q_tok1 | refuse | refuse | 1.00 | — | — |
| q_tok1 | honest | honest | 1.00 | — | — |
| q_tok1 | integrity | integrity | 1.00 | — | — |
| q_tok1 | candour | candid | 1.00 | — | — |
| q_tok1 | conceal | conceal | 1.00 | — | — |
| q_tok1 | perfunctory | perfunctory | 1.00 | — | — |
| q_tok1 | truthful | truth | 1.00 | — | — |
| q_tok1 | lie | lie | 1.00 | — | — |
| q_tok1 | transparent | transparent | 1.00 | — | — |
| q_tok1 | deny | deny | 1.00 | — | — |
| q_tok1 | fraud | — | 0 | all | — |
| q_tok1 | compliant | comply | 1.00 | — | — |
| q_tok1 | objective | objective | 1.00 | — | — |
| q_tok1 | violate | — | 0 | all | — |
| q_tok2 | refuse | refuse | 1.00 | — | — |
| q_tok2 | contradictory | contradictory | 1.00 | — | — |
| q_tok2 | compliant | comply | 1.00 | — | — |
| q_tok3 | truthful | truth | 0.29 | — | `␣truth`, `truth`, `␣Truth`, `Truth`, `_truth` |
| q_tok3 | truth | truth | 0.71 | — | `␣truthful`, `如实` |
| q_tok3 | honest | honest | 1.00 | — | — |
| q_tok3 | dishonest | dishonest | 1.00 | — | — |
| q_tok3 | sincere | sincere | 1.00 | — | — |
| q_tok3 | lie | lie | 1.00 | — | — |
| q_tok3 | fabricate | fabricate | 0.50 | — | `虚构` |
| q_tok3 | evade | evade | 0.67 | `␣dodge` | — |
| q_tok3 | perfunctory | perfunctory | 1.00 | — | — |
| q_tok3 | euphemistic | euphemistic | 1.00 | — | — |
| q_tok3 | mask | cover up | 1.00 | — | — |
| q_tok3 | deliberate | deliberate | 1.00 | — | — |
| q_tok3 | refuse | refuse | 1.00 | — | — |
| q_tok3 | deny | deny | 1.00 | — | — |
| q_tok3 | ethical | ethical | 0.67 | — | `␣morally` |
| q_tok3 | moral | ethical | 0.33 | — | `␣ethical`, `伦理` |
| q_tok3 | violate | violate | 0.80 | `违` | — |
| q_tok3 | compliant | comply | 0.85 | — | `␣conform`, `依法依规` |
| q_tok3 | conform | comply | 0.07 | `符合`, `是否符合` | `␣compliant`, `␣adher`, `合规`, `遵守`, `遵循`, `␣adherence`, `␣compliance`, `␣comply`, `␣complying`, `␣adhere`, `依法依规`, `遵` |
| q_tok3 | nonconforming | — | 0 | all | — |
| q_tok3 | aligned | aligned | 1.00 | — | — |
| q_tok3 | helpful | — | 0 | all | — |
| q_tok3 | biased | biased | 1.00 | — | — |
| q_tok3 | objective | objective | 0.50 | — | `中立` |
| q_tok3 | neutral | objective | 0.50 | — | `客观` |
| q_tok3 | influenced | — | 0 | all | — |
| q_tok3 | crafted | — | 0 | all | — |
| q_tok3 | tailored | — | 0 | all | — |
| q_tok3 | scripted | — | 0 | all | — |
| q_tok3 | hallucinate | hallucinate | 1.00 | — | — |
| q_tok4 | mislead | mislead | 1.00 | — | — |
| q_tok4 | truth | truth | 0.75 | — | `␣truthful`, `如实` |
| q_tok4 | truthful | truth | 0.25 | — | `␣truth`, `truth`, `␣Truth`, `Truth`, `真相`, `␣truths` |
| q_tok4 | honest | honest | 1.00 | — | — |
| q_tok4 | dishonest | dishonest | 1.00 | — | — |
| q_tok4 | integrity | integrity | 1.00 | — | — |
| q_tok4 | lie | lie | 1.00 | — | — |
| q_tok4 | conceal | conceal | 1.00 | — | — |
| q_tok4 | mask | cover up | 0.75 | — | `伪装` |
| q_tok4 | withhold | withhold | 1.00 | — | — |
| q_tok4 | omit | omit | 1.00 | — | — |
| q_tok4 | manipulate | manipulate | 0.86 | — | `诱导` |
| q_tok4 | fake | fake | 1.00 | — | — |
| q_tok4 | fraud | fraud | 1.00 | — | — |
| q_tok4 | distort | distort | 1.00 | — | — |
| q_tok4 | disguise | cover up | 0.25 | — | `␣masking`, `掩饰`, `␣mask` |
| q_tok4 | deliberate | deliberate | 0.89 | — | `明知` |
| q_tok4 | intent | intent | 0.67 | — | `␣intended`, `␣intend`, `␣intending` |
| q_tok4 | knowingly | deliberate | 0.10 | `知情` | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `有意`, `刻意`, `故意的`, `␣deliberate` |
| q_tok4 | disclose | disclose | 1.00 | — | — |
| q_tok4 | transparent | transparent | 1.00 | — | — |
| q_tok4 | euphemistic | euphemistic | 1.00 | — | — |
| q_tok4 | imply | imply | 1.00 | — | — |
| q_tok4 | induce | manipulate | 0.14 | — | `␣manip`, `␣manipulation`, `Manip`, `␣Manip`, `␣manipulated`, `␣манипу` |
| q_tok4 | framing | framing | 1.00 | — | — |
| q_tok4 | ethical | ethical | 0.50 | — | `␣morally` |
| q_tok4 | unethical | unethical | 1.00 | — | — |
| q_tok4 | moral | ethical | 0.50 | — | `␣ethical` |
| q_tok5 | honest | honest | 1.00 | — | — |
| q_tok5 | dishonest | dishonest | 1.00 | — | — |
| q_tok5 | truth | truth | 1.00 | — | — |
| q_tok5 | transparent | transparent | 1.00 | — | — |
| q_tok5 | admit | admit | 0.86 | — | `␣admissions` |
| q_tok5 | confess | confess | 1.00 | — | — |
| q_tok5 | lie | lie | 0.67 | `lie` | — |
| q_tok5 | mask | cover up | 1.00 | — | — |
| q_tok5 | deliberate | deliberate | 0.50 | — | `明知` |
| q_tok5 | intent | intent | 1.00 | — | — |
| q_tok5 | knowingly | deliberate | 0.50 | — | `故意的` |
| q_tok5 | ethical | ethical | 0.75 | — | `道德` |
| q_tok5 | violate | violate | 1.00 | — | — |
| q_tok5 | compliant | comply | 1.00 | — | — |
| q_tok5 | conform | — | 0 | all | — |
| q_tok5 | objective | objective | 1.00 | — | — |
| q_tok5 | accusation | — | 0 | all | — |
| q_tok5 | innocent | innocent | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: q_tok2: admit, q_tok3: admit, q_tok3: intent, q_tok4: indirect, q_tok4: betray

## Families whose name recurs at 3 or more positions

- admit: q_tok1, q_tok2, q_tok3, q_tok5
- compliant: q_tok1, q_tok2, q_tok3, q_tok5
- comply: q_tok1, q_tok2, q_tok3, q_tok5
- cover up: q_tok3, q_tok4, q_tok5
- deliberate: q_tok0, q_tok3, q_tok4, q_tok5
- dishonest: q_tok3, q_tok4, q_tok5
- ethical: q_tok3, q_tok4, q_tok5
- honest: q_tok1, q_tok3, q_tok4, q_tok5
- intent: q_tok0, q_tok1, q_tok3, q_tok4, q_tok5
- knowingly: q_tok0, q_tok4, q_tok5
- lie: q_tok1, q_tok3, q_tok4, q_tok5
- mask: q_tok3, q_tok4, q_tok5
- objective: q_tok1, q_tok3, q_tok5
- refuse: q_tok1, q_tok2, q_tok3
- transparent: q_tok1, q_tok4, q_tok5
- truth: q_tok0, q_tok1, q_tok3, q_tok4, q_tok5
- truthful: q_tok0, q_tok1, q_tok3, q_tok4
- violate: q_tok1, q_tok3, q_tok5

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- q_tok1: lie / truthful
- q_tok3: dishonest / honest
- q_tok3: lie / truth
- q_tok3: lie / truthful
- q_tok4: conceal / disclose
- q_tok4: dishonest / honest
- q_tok4: lie / truth
- q_tok4: lie / truthful
- q_tok4: mask / transparent
- q_tok5: dishonest / honest
- q_tok5: lie / truth
- q_tok5: mask / transparent

Merged candidate list: `qwen3_6_27b_LL_Q1_bare_question_merged.json` (106 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
