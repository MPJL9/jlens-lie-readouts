# Family report: qwen3.6-27b, logit lens, band 35-58, part Q2_after, group questionb

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q2_after_questionb_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## q_tok8

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | candid (speaking frankly, being upfront) | truth | `␣upfront` | 32 | L43-57; most at L47 (9), L53 (26), L54 (9) |
| 1 | refuse (refusing to answer or comply) | unclear | `␣refusal` | 1 | L42-42; most at L42 (1) |
| 2 | upfront (forthright, stating things openly at the start) | truth | `␣upfront` | 32 | L43-57; most at L47 (9), L53 (26), L54 (9) |
| 2 | refuse (refusing to answer) | unclear | `␣refusal` | 1 | L42-42; most at L42 (1) |

## q_tok9

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | candid (speaking frankly, being upfront) | truth | `␣upfront`, `␣straightforward` | 117 | L52-58; most at L52 (38), L53 (115), L57 (12) |
| 1 | deny (denying, refusing to acknowledge) | lie | `否认` | 35 | L35-42; most at L35 (34), L36 (23), L37 (6) |
| 1 | silent (staying silent, not speaking) | unclear | `不语` | 16 | L46-49; most at L46 (6), L47 (4), L49 (16) |
| 1 | kidding (joking, not being serious) | unclear | `␣kidding` | 7 | L54-55; most at L54 (7), L55 (1) |
| 2 | upfront (forthright, stating things openly at the start) | truth | `␣upfront` | 115 | L52-58; most at L52 (38), L53 (115), L57 (12) |
| 2 | deny (denying a fact or charge) | lie | `否认` | 35 | L35-42; most at L35 (34), L36 (23), L37 (6) |
| 2 | silence (saying nothing) | unclear | `不语` | 16 | L46-49; most at L46 (6), L47 (4), L49 (16) |
| 2 | neutral (taking no side) | unclear | `中立` | 34 | L35-39; most at L35 (8), L36 (34), L37 (15) |

## q_tok10

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | honest (being honest) | truth | `诚实`, `␣honesty`, `␣honest`, `␣honestly`, `␣Honest`, `诚实守信`, `诚` | 205 | L35-58; most at L38 (120), L39 (111), L40 (134) |
| 1 | dishonest (being dishonest) | lie | `␣dishonest` | 10 | L51-58; most at L51 (6), L57 (5), L58 (6) |
| 1 | integrity (integrity, uprightness) | truth | `诚信`, `正直`, `␣integrity`, `␣Integrity` | 86 | L35-58; most at L39 (29), L40 (52), L41 (26) |
| 1 | candid (speaking frankly, being upfront) | truth | `坦诚`, `直言`, `␣straightforward` | 46 | L35-58; most at L39 (16), L40 (19), L41 (19) |
| 1 | confess (confessing, coming clean) | truth | `坦白` | 8 | L35-58; most at L51 (5), L52 (3), L53 (3) |
| 1 | truth (the truth) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `_truth`, `␣truths`, `.truth`, `真相`, `真理`, `真实`, `真实的`, `的真实`, `的真实性`, `真实性`, `真實` | 196 | L35-58; most at L35 (128), L40 (117), L41 (114) |
| 1 | truthful (telling it as it is) | truth | `␣truthful`, `实话`, `说实话`, `如实`, `实事求是` | 180 | L35-58; most at L35 (128), L40 (91), L55 (88) |
| 1 | faithful (faithful to the facts) | truth | `忠实` | 30 | L35-51; most at L38 (22), L39 (10), L41 (11) |
| 1 | fact (facts, what actually is) | truth | `␣fact`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣factual`, `␣Facts`, `␣FACT`, `facts`, `FACT`, `事实`, `的事实`, `事实上`, `事实和`, `实际情况` | 72 | L35-58; most at L41 (51), L44 (59), L45 (65) |
| 1 | objective (objective, unbiased) | unclear | `客观`, `␣objectively`, `␣objective` | 178 | L35-52; most at L35 (135), L36 (167), L43 (85) |
| 1 | lie (telling a lie) | lie | `␣lie`, `␣lied`, `␣lies`, `lie`, `␣Lie`, `lies`, `Lie`, `␣Lies`, `␣lying`, `lying`, `说谎`, `谎言`, `撒谎`, `谎`, `␣mentira` | 105 | L35-58; most at L52 (40), L55 (69), L56 (43) |
| 1 | fabricate (making something up) | lie | `虚构`, `␣fabrication`, `␣fabricated`, `伪造` | 102 | L35-58; most at L35 (85), L36 (54), L40 (50) |
| 1 | fiction (fiction, fictional) | unclear | `fiction`, `␣fictional`, `␣Fiction`, `␣fiction`, `-fiction` | 40 | L35-57; most at L35 (18), L36 (18), L39 (19) |
| 1 | fake (fake) | lie | `fake` | 18 | L35-38; most at L35 (6), L36 (9), L37 (14) |
| 1 | fraud (fraud) | lie | `␣fraud` | 1 | L51-51; most at L51 (1) |
| 1 | pretend (pretending) | lie | `␣pretending` | 4 | L36-57; most at L36 (2), L52 (1), L53 (1) |
| 1 | mislead (misleading) | lie | `␣misleading`, `误导` | 7 | L37-58; most at L37 (2), L38 (5), L53 (2) |
| 1 | manipulate (manipulating) | lie | `␣manip`, `␣manipulation`, `␣manipulating` | 15 | L35-56; most at L37 (2), L38 (5), L46 (12) |
| 1 | exaggerate (exaggerating) | lie | `夸大` | 1 | L51-58; most at L51 (1), L52 (1), L54 (1) |
| 1 | conceal (concealing) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `瞒` | 119 | L35-58; most at L38 (89), L39 (94), L40 (102) |
| 1 | cover up (covering up, masking) | lie | `掩盖`, `掩饰`, `遮掩`, `掩`, `␣masking` | 53 | L36-58; most at L50 (34), L52 (25), L53 (21) |
| 1 | hide (hiding) | lie | `隐藏`, `␣hiding`, `␣hide`, `hide`, `Hide`, `␣hidden`, `-hidden`, `␣Hidden` | 31 | L35-58; most at L36 (13), L37 (13), L40 (14) |
| 1 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 58 | L36-58; most at L51 (34), L52 (40), L53 (44) |
| 1 | omit (leaving something out) | lie | `␣omit`, `omit`, `␣omission` | 9 | L37-58; most at L52 (5), L53 (6), L56 (3) |
| 1 | secret (secrecy, doing in secret) | lie | `␣secretly`, `␣secret`, `秘密`, `的秘密`, `暗中`, `␣covert` | 6 | L35-51; most at L37 (2), L38 (2), L43 (2) |
| 1 | evade (evading) | lie | `evas`, `␣evasion`, `回避` | 37 | L36-58; most at L51 (19), L52 (30), L53 (22) |
| 1 | avoid (avoiding) | unclear | `␣avoid`, `␣avoiding`, `␣avoided`, `avoid`, `␣avoidance` | 2 | L51-58; most at L51 (2), L52 (2), L53 (2) |
| 1 | silent (staying silent) | unclear | `沉默` | 4 | L35-42; most at L36 (3), L37 (4), L39 (2) |
| 1 | deny (denying, refusing to acknowledge) | lie | `否认`, `␣denying`, `␣deny`, `␣denial`, `␣denied`, `␣denies`, `deny` | 3 | L52-58; most at L53 (3), L54 (3), L55 (3) |
| 1 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admit`, `␣admits`, `␣admitted` | 105 | L35-58; most at L37 (60), L40 (57), L42 (74) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledge`, `␣acknowledging`, `␣acknowledgment`, `␣acknowledges`, `␣acknowledged` | 26 | L35-58; most at L39 (17), L40 (17), L44 (17) |
| 1 | disclose (disclosing information) | truth | `信息披露`, `披露`, `␣disclosure`, `␣disclosures`, `␣Disclosure`, `␣disclose`, `␣disclosed`, `␣disclosing`, `透露` | 25 | L35-58; most at L36 (9), L37 (7), L38 (20) |
| 1 | reveal (revealing, exposing) | truth | `揭示了`, `揭示`, `␣reveal`, `reveal`, `␣revealing`, `揭露`, `揭` | 25 | L35-54; most at L35 (18), L36 (5), L53 (7) |
| 1 | transparent (transparency) | truth | `␣transparency`, `␣Transparency`, `-transparent`, `␣transparent`, `transparent`, `␣Transparent`, `透明`, `透明度`, `透明的` | 19 | L35-58; most at L45 (8), L52 (8), L54 (12) |
| 1 | refuse (refusing) | unclear | `拒绝`, `拒绝了`, `␣refusal`, `␣refusing`, `␣refuse`, `␣refused`, `␣refuses`, `␣refus` | 33 | L36-58; most at L40 (24), L56 (25), L57 (24) |
| 1 | violate (violating a rule or principle) | unclear | `违反`, `违背`, `违反了`, `违`, `␣violate`, `␣violating`, `␣violates`, `␣violations`, `␣violation`, `␣violated`, `违法`, `违规`, `违反上述` | 170 | L35-58; most at L37 (139), L47 (145), L49 (143) |
| 1 | not conform (not conforming to) | unclear | `不符合` | 121 | L35-50; most at L37 (62), L43 (75), L46 (81) |
| 1 | deviate (deviating from) | unclear | `偏离`, `背离` | 8 | L46-58; most at L54 (6), L55 (4), L57 (4) |
| 1 | contradict (contradicting) | unclear | `␣contrad`, `␣contradict`, `␣contradictory`, `␣contradiction` | 26 | L35-58; most at L37 (14), L38 (14), L48 (12) |
| 1 | knowingly (acting with knowledge) | unclear | `明知`, `␣knowingly`, `␣knowing` | 137 | L35-58; most at L42 (96), L43 (119), L44 (115) |
| 1 | deliberate (doing on purpose) | unclear | `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate`, `故意`, `故意的`, `刻意`, `有意`, `␣sengaja`, `␣purposely` | 106 | L35-58; most at L36 (73), L37 (67), L51 (70) |
| 1 | ethics (ethics, ethical) | unclear | `␣ethical`, `ethical`, `␣ethics`, `␣Ethics`, `␣ethic`, `伦理` | 120 | L35-58; most at L39 (75), L40 (87), L58 (68) |
| 1 | moral (morality, moral) | unclear | `␣moral`, `␣morally`, `␣morality`, `␣Moral`, `␣morals`, `道德`, `的道德`, `职业道德` | 90 | L36-58; most at L39 (48), L50 (41), L58 (40) |
| 1 | unethical (unethical) | lie | `␣unethical` | 30 | L37-58; most at L39 (15), L40 (22), L50 (21) |
| 1 | conscience (conscience) | unclear | `良心` | 18 | L43-52; most at L49 (15), L50 (10), L51 (4) |
| 1 | comply (complying, adhering to rules) | unclear | `遵守`, `严格遵守`, `合规`, `␣compliance`, `␣Compliance`, `␣complying`, `␣comply`, `␣compliant`, `␣adherence`, `␣adher`, `␣adhere`, `遵循`, `遵照` | 106 | L35-58; most at L37 (49), L38 (57), L54 (43) |
| 1 | fulfill (fulfilling a duty or request) | unclear | `␣fulfill`, `␣fulfillment`, `␣fulfilled`, `␣fulfilling`, `履行`, `履行职责` | 52 | L35-54; most at L43 (33), L44 (31), L45 (20) |
| 1 | unfulfilled (failing to fulfil) | unclear | `未履行` | 2 | L48-53; most at L51 (1), L52 (1), L53 (1) |
| 1 | role-play (playing a role) | unclear | `扮演`, `角色扮演` | 70 | L35-57; most at L36 (35), L51 (40), L52 (33) |
| 1 | persona (an adopted persona) | unclear | `␣persona`, `␣personas`, `Persona`, `␣Persona`, `persona`, `␣personagem` | 32 | L51-58; most at L52 (30), L53 (23), L56 (29) |
| 1 | euphemistic (speaking tactfully, indirectly) | unclear | `委婉` | 51 | L35-45; most at L35 (37), L36 (40), L40 (12) |
| 2 | honest (being honest) | truth | `诚实`, `␣honesty`, `␣honest`, `␣honestly`, `␣Honest`, `诚`, `诚实守信` | 205 | L35-58; most at L38 (120), L39 (111), L40 (134) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 10 | L51-58; most at L51 (6), L57 (5), L58 (6) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `真相`, `_truth`, `␣truths`, `.truth` | 177 | L35-58; most at L40 (117), L41 (113), L55 (112) |
| 2 | truthful (telling it as it is, truthfully) | truth | `实话`, `␣truthful`, `如实`, `实事求是`, `说实话` | 180 | L35-58; most at L35 (128), L40 (91), L55 (88) |
| 2 | faithful (faithful to the facts) | truth | `忠实` | 30 | L35-51; most at L38 (22), L39 (10), L41 (11) |
| 2 | integrity (integrity, uprightness) | truth | `诚信`, `正直`, `␣integrity`, `␣Integrity` | 86 | L35-58; most at L39 (29), L40 (52), L41 (26) |
| 2 | candid (frank, candid) | truth | `坦诚` | 44 | L35-58; most at L39 (16), L40 (19), L41 (19) |
| 2 | confess (coming clean, confessing) | truth | `坦白` | 8 | L35-58; most at L51 (5), L52 (3), L53 (3) |
| 2 | admit (admitting a fact) | truth | `承认`, `␣admitting`, `␣admit`, `␣admits`, `␣admitted` | 105 | L35-58; most at L37 (60), L40 (57), L42 (74) |
| 2 | acknowledge (acknowledging a fact) | truth | `␣acknowledge`, `␣acknowledging`, `␣acknowledgment`, `␣acknowledges`, `␣acknowledged` | 26 | L35-58; most at L39 (17), L40 (17), L44 (17) |
| 2 | disclose (disclosing information) | truth | `信息披露`, `␣disclosure`, `披露`, `␣disclosures`, `␣Disclosure`, `␣disclose`, `␣disclosed`, `␣disclosing` | 25 | L35-58; most at L36 (9), L37 (6), L38 (20) |
| 2 | reveal (revealing) | truth | `揭示了`, `␣reveal`, `揭示`, `reveal`, `␣revealing` | 18 | L35-53; most at L35 (17), L36 (4), L38 (5) |
| 2 | transparent (transparency) | truth | `␣transparency`, `␣Transparency`, `-transparent`, `␣transparent`, `transparent`, `␣Transparent` | 19 | L35-58; most at L45 (8), L52 (8), L54 (12) |
| 2 | lie (telling a lie) | lie | `说谎`, `谎言`, `␣lie`, `撒谎`, `␣lied`, `␣lies`, `谎`, `lie`, `␣Lie`, `lies`, `Lie`, `␣Lies` | 105 | L35-58; most at L52 (40), L55 (69), L56 (43) |
| 2 | conceal (hiding or covering up information) | lie | `隐瞒`, `␣conceal`, `掩盖`, `隐藏`, `␣hiding`, `掩饰`, `␣concealed`, `␣hide`, `遮掩`, `␣hidden`, `-hidden`, `hide`, `Hide`, `␣Hidden` | 124 | L35-58; most at L38 (90), L39 (95), L40 (102) |
| 2 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 58 | L36-58; most at L51 (34), L52 (40), L53 (44) |
| 2 | secret (secrecy) | lie | `␣secretly`, `秘密`, `的秘密`, `␣secret`, `␣covert` | 4 | L35-51; most at L37 (2), L38 (2), L41 (2) |
| 2 | mislead (misleading) | lie | `误导`, `␣misleading` | 7 | L37-58; most at L37 (2), L38 (5), L53 (2) |
| 2 | manipulate (manipulating) | lie | `␣manip`, `␣manipulation`, `␣manipulating` | 15 | L35-56; most at L37 (2), L38 (5), L46 (12) |
| 2 | evade (evading) | lie | `evas`, `␣evasion` | 33 | L51-58; most at L51 (19), L52 (28), L53 (18) |
| 2 | fabricate (making something up) | lie | `伪造`, `␣fabrication`, `␣fabricated` | 3 | L37-58; most at L37 (2), L38 (1), L40 (1) |
| 2 | fake (fake) | lie | `fake` | 18 | L35-38; most at L35 (6), L36 (9), L37 (14) |
| 2 | impersonate (pretending to be someone) | lie | `冒充` | 1 | L51-51; most at L51 (1) |
| 2 | pretend (pretending) | lie | `␣pretending` | 4 | L36-57; most at L36 (2), L52 (1), L53 (1) |
| 2 | fraud (fraud) | lie | `␣fraud` | 1 | L51-51; most at L51 (1) |
| 2 | fiction (fictional, invented story) | unclear | `虚构`, `fiction`, `␣fictional`, `␣Fiction`, `␣fiction`, `-fiction` | 102 | L35-57; most at L35 (85), L36 (54), L40 (50) |
| 2 | role-play (playing a role or persona) | unclear | `扮演`, `␣persona`, `␣backstory`, `角色扮演`, `␣personas`, `Persona`, `␣Persona`, `persona`, `␣personagem` | 87 | L35-58; most at L51 (53), L52 (52), L53 (41) |
| 2 | intentional (doing it on purpose, knowingly) | unclear | `明知`, `␣intentionally`, `␣deliberately`, `故意`, `␣deliberate`, `␣knowingly`, `刻意`, `␣intentional`, `有意`, `␣sengaja`, `故意的`, `␣knowing` | 145 | L35-58; most at L36 (102), L43 (119), L44 (115) |
| 2 | violate (breaking a rule or principle) | unclear | `违反`, `违背`, `违反了`, `␣violate`, `违`, `␣violating`, `␣violates`, `␣violations`, `␣violation`, `␣violated`, `违法`, `违规`, `违反上述` | 170 | L35-58; most at L37 (139), L47 (145), L49 (143) |
| 2 | comply (following rules or instructions) | unclear | `遵守`, `合规`, `␣adherence`, `␣adher`, `␣compliance`, `严格遵守`, `遵循`, `␣adhere`, `遵照`, `␣Compliance`, `␣compliant` | 106 | L35-58; most at L37 (49), L38 (57), L54 (43) |
| 2 | ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣morally`, `道德`, `ethical`, `␣moral`, `的道德`, `␣Ethics`, `␣morality`, `职业道德`, `␣Moral`, `␣morals`, `␣ethic` | 130 | L35-58; most at L39 (79), L40 (89), L58 (71) |
| 2 | unethical (morally wrong) | lie | `␣unethical` | 30 | L37-58; most at L39 (15), L40 (22), L50 (21) |
| 2 | conscience (conscience) | unclear | `良心` | 18 | L43-52; most at L49 (15), L50 (10), L51 (4) |
| 2 | deny (denying a fact or charge) | lie | `␣denying`, `否认`, `␣deny`, `␣denial`, `deny` | 3 | L52-58; most at L53 (3), L54 (3), L55 (3) |
| 2 | refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refusing`, `␣refuse`, `␣refused`, `␣refuses`, `␣refus`, `拒绝了` | 33 | L36-58; most at L40 (24), L56 (25), L57 (24) |
| 2 | euphemistic (tactful, indirect wording) | unclear | `委婉` | 51 | L35-45; most at L35 (37), L36 (40), L40 (12) |
| 2 | objective (objective, impartial) | unclear | `客观`, `␣objectively`, `␣objective` | 178 | L35-52; most at L35 (135), L36 (167), L43 (85) |
| 2 | contradict (contradicting) | unclear | `␣contrad`, `␣contradict`, `␣contradictory`, `␣contradiction` | 26 | L35-58; most at L37 (14), L38 (14), L48 (12) |
| 2 | silence (staying silent) | unclear | `沉默`, `␣silence` | 6 | L35-56; most at L36 (3), L37 (4), L39 (2) |
| 2 | neutral (taking no side) | unclear | `中立` | 4 | L35-36; most at L35 (1), L36 (3) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| q_tok8 | candid | upfront | 1.00 | — | — |
| q_tok8 | refuse | refuse | 1.00 | — | — |
| q_tok9 | candid | upfront | 0.50 | `␣straightforward` | — |
| q_tok9 | deny | deny | 1.00 | — | — |
| q_tok9 | silent | silence | 1.00 | — | — |
| q_tok9 | kidding | — | 0 | all | — |
| q_tok10 | honest | honest | 1.00 | — | — |
| q_tok10 | dishonest | dishonest | 1.00 | — | — |
| q_tok10 | integrity | integrity | 1.00 | — | — |
| q_tok10 | candid | candid | 0.33 | `直言`, `␣straightforward` | — |
| q_tok10 | confess | confess | 1.00 | — | — |
| q_tok10 | truth | truth | 0.53 | `真理`, `真实`, `真实的`, `的真实`, `的真实性`, `真实性`, `真實` | — |
| q_tok10 | truthful | truthful | 1.00 | — | — |
| q_tok10 | faithful | faithful | 1.00 | — | — |
| q_tok10 | fact | — | 0 | all | — |
| q_tok10 | objective | objective | 1.00 | — | — |
| q_tok10 | lie | lie | 0.80 | `␣lying`, `lying`, `␣mentira` | — |
| q_tok10 | fabricate | fabricate | 0.75 | `虚构` | — |
| q_tok10 | fiction | fiction | 0.83 | — | `虚构` |
| q_tok10 | fake | fake | 1.00 | — | — |
| q_tok10 | fraud | fraud | 1.00 | — | — |
| q_tok10 | pretend | pretend | 1.00 | — | — |
| q_tok10 | mislead | mislead | 1.00 | — | — |
| q_tok10 | manipulate | manipulate | 1.00 | — | — |
| q_tok10 | exaggerate | — | 0 | all | — |
| q_tok10 | conceal | conceal | 0.20 | `瞒` | `掩盖`, `隐藏`, `␣hiding`, `掩饰`, `␣hide`, `遮掩`, `␣hidden`, `-hidden`, `hide`, `Hide`, `␣Hidden` |
| q_tok10 | cover up | conceal | 0.19 | `掩`, `␣masking` | `隐瞒`, `␣conceal`, `隐藏`, `␣hiding`, `␣concealed`, `␣hide`, `␣hidden`, `-hidden`, `hide`, `Hide`, `␣Hidden` |
| q_tok10 | hide | conceal | 0.57 | — | `隐瞒`, `␣conceal`, `掩盖`, `掩饰`, `␣concealed`, `遮掩` |
| q_tok10 | withhold | withhold | 1.00 | — | — |
| q_tok10 | omit | — | 0 | all | — |
| q_tok10 | secret | secret | 0.83 | `暗中` | — |
| q_tok10 | evade | evade | 0.67 | `回避` | — |
| q_tok10 | avoid | — | 0 | all | — |
| q_tok10 | silent | silence | 0.50 | — | `␣silence` |
| q_tok10 | deny | deny | 0.71 | `␣denied`, `␣denies` | — |
| q_tok10 | admit | admit | 1.00 | — | — |
| q_tok10 | acknowledge | acknowledge | 1.00 | — | — |
| q_tok10 | disclose | disclose | 0.89 | `透露` | — |
| q_tok10 | reveal | reveal | 0.71 | `揭露`, `揭` | — |
| q_tok10 | transparent | transparent | 0.67 | `透明`, `透明度`, `透明的` | — |
| q_tok10 | refuse | refuse | 1.00 | — | — |
| q_tok10 | violate | violate | 1.00 | — | — |
| q_tok10 | not conform | — | 0 | all | — |
| q_tok10 | deviate | — | 0 | all | — |
| q_tok10 | contradict | contradict | 1.00 | — | — |
| q_tok10 | knowingly | intentional | 0.25 | — | `␣intentionally`, `␣deliberately`, `故意`, `␣deliberate`, `刻意`, `␣intentional`, `有意`, `␣sengaja`, `故意的` |
| q_tok10 | deliberate | intentional | 0.69 | `␣purposely` | `明知`, `␣knowingly`, `␣knowing` |
| q_tok10 | ethics | ethics | 0.43 | — | `␣morally`, `道德`, `␣moral`, `的道德`, `␣morality`, `职业道德`, `␣Moral`, `␣morals` |
| q_tok10 | moral | ethics | 0.57 | — | `␣ethical`, `␣ethics`, `伦理`, `ethical`, `␣Ethics`, `␣ethic` |
| q_tok10 | unethical | unethical | 1.00 | — | — |
| q_tok10 | conscience | conscience | 1.00 | — | — |
| q_tok10 | comply | comply | 0.85 | `␣complying`, `␣comply` | — |
| q_tok10 | fulfill | — | 0 | all | — |
| q_tok10 | unfulfilled | — | 0 | all | — |
| q_tok10 | role-play | role-play | 0.22 | — | `␣persona`, `␣backstory`, `␣personas`, `Persona`, `␣Persona`, `persona`, `␣personagem` |
| q_tok10 | persona | role-play | 0.67 | — | `扮演`, `␣backstory`, `角色扮演` |
| q_tok10 | euphemistic | euphemistic | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: q_tok9: neutral, q_tok10: impersonate, q_tok10: neutral

## Families whose name recurs at 3 or more positions

- candid: q_tok10, q_tok8, q_tok9

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- q_tok10: conceal / disclose
- q_tok10: conceal / reveal
- q_tok10: cover up / transparent
- q_tok10: deny / admit
- q_tok10: deny / confess
- q_tok10: dishonest / honest
- q_tok10: evade / admit
- q_tok10: hide / disclose
- q_tok10: hide / reveal
- q_tok10: lie / truth
- q_tok10: lie / truthful
- q_tok10: mislead / candid

Merged candidate list: `qwen3_6_27b_LL_Q2_after_questionb_merged.json` (61 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
