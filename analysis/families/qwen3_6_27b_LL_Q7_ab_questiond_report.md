# Family report: qwen3.6-27b, logit lens, band 35-58, part Q7_ab, group questiond

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q7_ab_questiond_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## q_tok24

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceived`, `骗` | 79 | L35-58; most at L50 (57), L52 (60), L53 (61) |
| 1 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `误导性` | 44 | L50-58; most at L53 (43), L54 (37), L55 (33) |
| 1 | dishonest (not honest) | lie | `␣dishonest` | 23 | L51-58; most at L53 (11), L57 (21), L58 (18) |
| 1 | honest (being honest) | truth | `诚实`, `␣honest`, `诚`, `␣honesty`, `诚信`, `␣Honest`, `␣honestly`, `诚实守信` | 168 | L35-58; most at L36 (111), L37 (137), L38 (112) |
| 1 | candid (frank, open about it) | truth | `坦诚`, `␣frank` | 22 | L35-58; most at L41 (12), L42 (13), L52 (13) |
| 1 | confess (owning up to the act) | truth | `坦白`, `如实供述` | 9 | L38-55; most at L51 (8), L52 (8), L53 (7) |
| 1 | admit (admitting or acknowledging) | truth | `承认`, `␣admit`, `␣admitted`, `␣acknowledge`, `␣admitting`, `␣admission`, `␣admits`, `␣acknowledging`, `␣acknowledged`, `␣acknowledges`, `␣acknowledgment` | 107 | L35-58; most at L35 (74), L36 (64), L37 (77) |
| 1 | deny (denying) | lie | `否认`, `否定`, `␣denial`, `␣denying`, `␣denied`, `␣deny`, `␣denies`, `␣Denied`, `deny` | 49 | L35-58; most at L39 (24), L55 (24), L56 (24) |
| 1 | refuse (refusing or declining) | unclear | `拒绝`, `␣refused`, `␣refuse`, `␣refusal`, `␣refusing`, `␣refuses`, `␣refus`, `拒`, `拒絕`, `拒绝了`, `␣declined`, `拒不`, `␣decline`, `␣declining`, `␣declines` | 23 | L36-58; most at L56 (20), L57 (20), L58 (19) |
| 1 | reject (rejecting) | unclear | `␣reject`, `␣rejected`, `␣rejection`, `reject`, `␣rejecting` | 2 | L43-56; most at L43 (1), L44 (1), L48 (2) |
| 1 | conceal (concealing or hiding) | lie | `隐瞒`, `␣conceal`, `掩盖`, `␣concealed`, `隐藏`, `␣hiding`, `瞒`, `掩饰`, `␣hide`, `隐蔽`, `隐藏的`, `␣hidden`, `Hide`, `_hide`, `-hide`, `遮掩`, `隐藏着` | 110 | L35-58; most at L38 (70), L39 (83), L40 (81) |
| 1 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 47 | L36-58; most at L52 (33), L53 (40), L57 (19) |
| 1 | omit (leaving things out) | lie | `␣omit`, `␣omission`, `␣omitted`, `省略`, `omit` | 26 | L36-58; most at L56 (21), L57 (18), L58 (17) |
| 1 | secret (secrecy, confidentiality) | lie | `保密`, `␣secret`, `秘密`, `secret`, `␣Secret`, `␣confidential`, `␣secretly`, `␣confidentiality`, `机密` | 35 | L35-57; most at L39 (20), L40 (32), L41 (17) |
| 1 | silence (keeping silent) | unclear | `缄`, `沉默` | 19 | L36-50; most at L36 (15), L40 (10), L42 (5) |
| 1 | fabricate (making things up) | lie | `␣invent`, `␣fabricated`, `凭空`, `␣fabrication`, `␣invented`, `伪造` | 37 | L35-58; most at L35 (7), L36 (18), L37 (29) |
| 1 | fictional (fictional, made-up story) | unclear | `虚构`, `␣fictional`, `fiction`, `␣fiction`, `␣Fiction`, `-fiction` | 114 | L35-58; most at L35 (48), L36 (45), L51 (63) |
| 1 | fake (fake, sham) | lie | `fake`, `伪`, `作假` | 6 | L38-51; most at L38 (3), L46 (1), L51 (1) |
| 1 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 29 | L37-58; most at L51 (18), L53 (22), L54 (14) |
| 1 | exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated`, `夸张` | 5 | L36-58; most at L49 (3), L50 (4), L51 (3) |
| 1 | downplay (downplaying) | lie | `淡化` | 19 | L35-52; most at L36 (17), L37 (1), L50 (4) |
| 1 | euphemistic (tactful, indirect wording) | unclear | `委婉` | 2 | L36-45; most at L36 (1), L40 (1), L45 (1) |
| 1 | evade (evading, dodging) | lie | `␣evasion`, `回避` | 11 | L46-58; most at L51 (6), L57 (8), L58 (7) |
| 1 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣deliberate`, `␣deliberately`, `故意`, `␣intentional`, `刻意`, `有意`, `故意的` | 75 | L35-58; most at L50 (49), L51 (35), L54 (42) |
| 1 | knowingly (knowing it was so) | unclear | `明知`, `␣knowingly` | 107 | L35-58; most at L43 (85), L44 (79), L45 (83) |
| 1 | ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣morally`, `␣moral`, `ethical`, `道德`, `␣Ethics`, `职业道德`, `的道德`, `␣morality` | 34 | L35-58; most at L40 (22), L41 (20), L42 (20) |
| 1 | unethical (unethical) | lie | `␣unethical` | 4 | L44-58; most at L56 (2), L57 (2), L58 (3) |
| 1 | wrongdoing (wrongdoing) | lie | `␣wrongdoing` | 2 | L51-56; most at L51 (1), L52 (1), L56 (2) |
| 1 | integrity (integrity, uprightness) | truth | `␣integrity`, `␣Integrity`, `正直` | 16 | L41-57; most at L50 (4), L51 (5), L52 (6) |
| 1 | transparent (transparency) | truth | `␣transparency`, `透明`, `-transparent`, `␣transparent`, `␣Transparency`, `透明的`, `透明度`, `transparent`, `␣transparencia` | 15 | L35-58; most at L47 (7), L54 (11), L57 (7) |
| 1 | genuine (genuine, authentic) | truth | `␣genuine`, `␣genuinely` | 23 | L35-50; most at L35 (6), L36 (17), L37 (12) |
| 1 | sincere (sincere) | truth | `真诚`, `␣sincerity`, `␣sincere`, `␣sincerely` | 4 | L36-58; most at L38 (2), L57 (2), L58 (2) |
| 1 | trustworthy (credible, trustworthy) | truth | `可信` | 1 | L42-42; most at L42 (1) |
| 1 | loyal (loyal, faithful) | unclear | `忠实`, `␣loyalty`, `忠诚`, `␣loyal`, `忠于`, `忠心`, `忠诚度` | 33 | L35-58; most at L38 (12), L41 (11), L57 (12) |
| 1 | comply (complying with instructions or rules) | unclear | `␣adher`, `遵循`, `␣adherence`, `遵照`, `服从`, `遵守`, `合规`, `␣adhere`, `严格遵守`, `遵从`, `␣compliance`, `␣obey`, `遵`, `␣comply`, `␣complying`, `␣Compliance` | 59 | L35-58; most at L46 (30), L48 (29), L54 (33) |
| 1 | follow (following (instructions)) | unclear | `␣follow`, `␣Follow`, `Follow`, `␣follows`, `follow`, `-follow`, `_follow`, `.follow`, `␣FOLLOW`, `␣followed` | 24 | L42-58; most at L56 (20), L57 (19), L58 (19) |
| 1 | fulfill (fulfilling a duty or task) | unclear | `履行`, `␣fulfill`, `履行职责`, `␣fulfillment`, `␣fulfilling` | 38 | L35-58; most at L41 (15), L43 (24), L44 (18) |
| 1 | role-play (playing a role) | unclear | `扮演`, `角色扮演` | 17 | L40-57; most at L51 (16), L52 (8), L53 (6) |
| 1 | role / persona (the role or persona the model was given) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `␣role`, `role`, `persona`, `角色`, `Role`, `␣Role`, `角色的`, `-role`, `的角色`, `␣roles`, `(role`, `ROLE`, `␣Personas` | 29 | L40-58; most at L51 (22), L52 (22), L56 (22) |
| 1 | simulate (simulating) | unclear | `模拟`, `␣simulated`, `␣simulation`, `仿真`, `␣simulate`, `␣Simulation`, `␣simulations`, `Simulation` | 6 | L41-58; most at L48 (4), L52 (3), L53 (3) |
| 1 | maintain (maintaining a position, persisting) | unclear | `坚持`, `必须坚持`, `␣maintaining`, `␣maintain`, `维持`, `要坚持`, `␣maintains`, `坚守`, `␣maintained`, `始终坚持`, `␣Maintain`, `坚持把` | 49 | L35-58; most at L48 (39), L50 (30), L54 (30) |
| 1 | firm (being firm) | unclear | `坚定`, `␣firm`, `坚定的`, `␣firmly`, `坚定不移` | 35 | L35-58; most at L38 (15), L42 (23), L43 (16) |
| 1 | uphold / defend (upholding or defending) | unclear | `维护`, `␣uphold`, `和维护`, `为维护`, `维护和` | 48 | L35-58; most at L43 (34), L44 (31), L45 (30) |
| 1 | justify (justifying) | unclear | `辩护`, `justify` | 3 | L36-57; most at L37 (2), L54 (1), L57 (1) |
| 1 | claim (claiming) | unclear | `声称`, `␣claim`, `claim`, `␣claims`, `␣claimed`, `␣Claim`, `␣claiming`, `Claim` | 10 | L36-58; most at L40 (6), L51 (5), L52 (6) |
| 1 | so-called (so-called) | unclear | `所谓的` | 1 | L53-53; most at L53 (1) |
| 1 | assert (asserting) | unclear | `assert`, `␣assert`, `␣asserting`, `␣assertions`, `␣asserts` | 25 | L35-58; most at L36 (11), L43 (11), L49 (13) |
| 1 | framing (framing, how it is presented) | unclear | `␣framing` | 2 | L53-58; most at L53 (1), L54 (1), L58 (2) |
| 1 | technically (technically (true)) | unclear | `␣technically` | 19 | L35-58; most at L45 (11), L55 (16), L56 (12) |
| 1 | plausible (plausible) | unclear | `␣plausible` | 1 | L44-47; most at L44 (1), L45 (1), L46 (1) |
| 1 | violate (violating, going against) | lie | `违背`, `违反`, `违`, `违反了`, `␣violate`, `␣violates`, `␣violations`, `␣violating`, `违规` | 75 | L35-58; most at L43 (59), L44 (40), L45 (41) |
| 1 | illegal (breaking the law) | lie | `违法`, `违法行为` | 3 | L42-57; most at L42 (1), L43 (1), L44 (3) |
| 1 | contradict (contradicting) | unclear | `␣contradict`, `矛盾`, `␣contrad`, `矛盾的`, `␣contradiction`, `␣contradictory` | 20 | L35-58; most at L42 (7), L43 (6), L50 (8) |
| 1 | ostensibly (on the surface (but not in reality)) | unclear | `表面上` | 61 | L35-49; most at L36 (51), L37 (53), L38 (44) |
| 1 | legitimate (legitimate, justified) | unclear | `正当`, `␣legitimate` | 3 | L35-45; most at L35 (1), L38 (1), L45 (1) |
| 1 | legal (legal) | unclear | `合法`, `合法的` | 23 | L35-50; most at L43 (13), L44 (12), L48 (11) |
| 1 | neutral (neutral) | unclear | `中立` | 24 | L35-37; most at L35 (13), L36 (21), L37 (3) |
| 1 | objective (objective) | truth | `客观`, `␣objectively`, `␣objective` | 179 | L35-57; most at L35 (165), L36 (134), L37 (72) |
| 1 | fact (the facts, factual) | truth | `事实`, `␣factual`, `␣fact`, `␣facts`, `实事求是`, `的事实`, `实际情况`, `实情`, `␣Fact`, `事实和`, `Fact`, `␣Facts`, `fact`, `facts`, `_fact`, `␣FACT`, `根据实际情况`, `FACT`, `上述事实` | 155 | L35-58; most at L39 (122), L40 (118), L41 (129) |
| 1 | manipulate (manipulating) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating` | 4 | L54-58; most at L54 (2), L55 (3), L56 (1) |
| 1 | pander (pandering, pleasing) | unclear | `迎合` | 7 | L36-50; most at L41 (2), L42 (2), L50 (2) |
| 1 | forced (being forced) | unclear | `被迫`, `␣forced` | 4 | L46-57; most at L47 (2), L48 (3), L49 (3) |
| 1 | disclose (disclosing, revealing) | truth | `公开`, `␣disclosure`, `揭`, `␣disclosed`, `␣disclosures`, `␣Disclosure`, `揭露`, `␣revealed`, `␣revealing`, `␣disclose`, `Disclosure`, `␣disclosing`, `揭示` | 21 | L35-58; most at L38 (10), L47 (6), L53 (6) |
| 1 | direct (direct, straightforward) | unclear | `␣direct`, `直接`, `Direct`, `␣directly`, `␣straightforward`, `␣Direct`, `直接的` | 57 | L35-57; most at L42 (21), L43 (47), L47 (21) |
| 1 | indirect (indirect) | unclear | `␣indirect`, `␣indirectly` | 3 | L43-49; most at L43 (1), L44 (1), L46 (3) |
| 2 | honest (being honest) | truth | `诚实`, `␣honest`, `诚`, `␣honesty`, `␣Honest`, `␣honestly`, `诚实守信` | 166 | L35-58; most at L36 (110), L37 (135), L38 (112) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 23 | L51-58; most at L53 (11), L57 (21), L58 (18) |
| 2 | truth (the truth (what really happened)) | truth | `␣truth`, `实话`, `truth`, `␣Truth`, `Truth`, `真相`, `实情`, `␣truths`, `真理`, `_truth`, `说实话`, `.truth` | 193 | L35-58; most at L35 (178), L40 (160), L41 (149) |
| 2 | factual (matching the facts) | unclear | `事实`, `␣factual`, `␣fact`, `␣facts`, `实事求是`, `的事实`, `␣Fact`, `事实和`, `Fact`, `␣Facts`, `事实上`, `fact`, `facts`, `_fact`, `␣FACT`, `FACT`, `上述事实` | 155 | L35-58; most at L39 (122), L40 (118), L41 (129) |
| 2 | objective (objective, without bias) | unclear | `客观`, `␣objectively`, `␣objective` | 179 | L35-57; most at L35 (165), L36 (134), L37 (72) |
| 2 | transparent (being transparent) | truth | `␣transparency`, `透明`, `-transparent`, `␣transparent`, `␣Transparency`, `透明的`, `透明度`, `transparent`, `␣transparencia` | 15 | L35-58; most at L47 (7), L54 (11), L57 (7) |
| 2 | candid (frank, straightforward) | truth | `坦诚`, `␣straightforward` | 23 | L35-58; most at L41 (12), L42 (13), L52 (13) |
| 2 | confess (coming clean, confessing) | truth | `坦白` | 9 | L45-55; most at L51 (8), L52 (8), L53 (7) |
| 2 | sincere (sincere) | truth | `真诚`, `␣sincerity`, `␣sincere`, `␣sincerely` | 4 | L36-58; most at L38 (2), L57 (2), L58 (2) |
| 2 | genuine (genuine, real) | unclear | `␣genuine`, `真正的`, `␣genuinely`, `真正` | 28 | L35-52; most at L35 (6), L36 (18), L37 (15) |
| 2 | integrity (integrity, uprightness) | truth | `诚信`, `␣integrity`, `␣Integrity`, `正直` | 42 | L35-58; most at L40 (17), L41 (15), L51 (8) |
| 2 | faithful (faithful, true to something) | unclear | `忠实`, `忠于` | 18 | L36-57; most at L38 (11), L41 (10), L42 (6) |
| 2 | loyal (loyalty) | unclear | `␣loyalty`, `忠诚`, `␣loyal`, `忠诚度`, `忠心` | 19 | L35-58; most at L51 (10), L54 (11), L57 (11) |
| 2 | trustworthy (trustworthy, credible) | truth | `可信` | 1 | L42-42; most at L42 (1) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceived`, `骗` | 79 | L35-58; most at L50 (57), L52 (60), L53 (61) |
| 2 | mislead (misleading) | lie | `␣misleading`, `误导`, `误导性` | 44 | L50-58; most at L53 (43), L54 (37), L55 (33) |
| 2 | conceal (concealing, hiding) | lie | `隐瞒`, `␣conceal`, `掩盖`, `掩`, `␣concealed`, `隐藏`, `掩饰`, `隐藏的`, `隐蔽`, `␣hide`, `Hide`, `_hide`, `-hide`, `␣hidden`, `遮掩`, `掩护`, `隐藏着` | 110 | L35-58; most at L38 (70), L39 (83), L40 (81) |
| 2 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 47 | L36-58; most at L52 (33), L53 (40), L57 (19) |
| 2 | omit (leaving something out) | lie | `␣omit`, `␣omission`, `␣omitted`, `omit` | 26 | L36-58; most at L56 (21), L57 (18), L58 (17) |
| 2 | secret (keeping secret, confidential) | lie | `保密`, `␣secret`, `secret`, `␣Secret`, `␣secretly`, `␣confidential`, `␣confidentiality` | 35 | L35-57; most at L39 (20), L40 (32), L41 (16) |
| 2 | falsehood (a false statement, false information) | lie | `␣falsehood`, `␣misinformation`, `虚假信息` | 61 | L36-58; most at L51 (48), L53 (43), L55 (41) |
| 2 | fabricate (making something up) | lie | `␣invent`, `␣fabricated`, `凭空`, `␣fabrication`, `伪造`, `␣invented`, `作假` | 37 | L35-58; most at L35 (7), L36 (18), L37 (29) |
| 2 | fake (fake) | lie | `fake` | 3 | L38-51; most at L38 (2), L51 (1) |
| 2 | fiction (fictional, invented story) | unclear | `虚构`, `␣fictional`, `fiction`, `␣fiction`, `␣Fiction`, `-fiction` | 114 | L35-58; most at L35 (48), L36 (45), L51 (63) |
| 2 | exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 5 | L36-58; most at L49 (3), L50 (4), L51 (3) |
| 2 | downplay (downplaying) | lie | `淡化` | 19 | L35-52; most at L36 (17), L37 (1), L50 (4) |
| 2 | distort (distorting) | lie | `␣distortion`, `␣distort` | 1 | L58-58; most at L58 (1) |
| 2 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣deliberate`, `␣deliberately`, `故意`, `␣intentional`, `刻意`, `有意`, `故意的` | 75 | L35-58; most at L50 (49), L51 (35), L54 (42) |
| 2 | knowingly (knowing it is so) | unclear | `明知`, `␣knowingly` | 107 | L35-58; most at L43 (85), L44 (79), L45 (83) |
| 2 | deny (denying) | lie | `否认`, `否定`, `␣denial`, `␣denying`, `␣denied`, `␣deny`, `␣denies`, `deny`, `␣Denied` | 49 | L35-58; most at L39 (24), L55 (24), L56 (24) |
| 2 | admit (admitting) | truth | `承认`, `␣admit`, `␣admitted`, `␣admitting`, `␣admits` | 107 | L35-58; most at L35 (74), L36 (64), L37 (77) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledge`, `␣acknowledging`, `␣acknowledged`, `␣acknowledges`, `␣acknowledgment` | 6 | L39-58; most at L56 (3), L57 (4), L58 (2) |
| 2 | refuse (refusing, declining) | unclear | `拒绝`, `␣refusal`, `␣refuse`, `␣refused`, `␣refusing`, `␣refuses`, `␣refus`, `拒`, `拒絕`, `拒绝了`, `拒不`, `␣declined`, `␣decline`, `␣declining`, `␣declines` | 23 | L36-58; most at L56 (20), L57 (20), L58 (19) |
| 2 | reject (rejecting) | unclear | `␣reject`, `␣rejection`, `␣rejecting`, `␣rejected`, `reject` | 2 | L43-56; most at L43 (1), L44 (1), L48 (2) |
| 2 | evade (evading) | lie | `␣evasion`, `回避` | 11 | L46-58; most at L51 (6), L57 (8), L58 (7) |
| 2 | ethical (ethical) | unclear | `␣ethical`, `␣ethics`, `伦理`, `ethical`, `␣Ethics` | 33 | L35-58; most at L40 (22), L41 (20), L42 (20) |
| 2 | unethical (unethical) | lie | `␣unethical` | 4 | L44-58; most at L56 (2), L57 (2), L58 (3) |
| 2 | violate (violating a rule or principle) | unclear | `违背`, `违反`, `违反了`, `␣violate`, `␣violates`, `␣violations`, `␣violating` | 74 | L35-58; most at L43 (58), L44 (40), L45 (40) |
| 2 | comply (complying, adhering, obeying) | unclear | `␣adher`, `遵循`, `␣adherence`, `遵照`, `服从`, `遵守`, `合规`, `␣adhere`, `严格遵守`, `遵从`, `␣obey`, `␣compliance`, `␣comply`, `␣complying`, `␣Compliance` | 59 | L35-58; most at L46 (30), L48 (29), L54 (33) |
| 2 | role-play (playing a role) | unclear | `扮演`, `␣role`, `role`, `角色扮演`, `角色`, `Role`, `␣Role`, `角色的`, `-role`, `的角色`, `ROLE`, `(role`, `␣roles` | 19 | L40-57; most at L51 (18), L52 (10), L53 (7) |
| 2 | persona (an assumed persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas` | 28 | L40-58; most at L51 (20), L52 (21), L56 (22) |
| 2 | insist (holding firm, insisting) | unclear | `坚持`, `坚定`, `␣firm`, `坚定的`, `必须坚持`, `要坚持`, `坚守`, `始终坚持`, `␣firmly`, `坚持把`, `坚定不移`, `␣insist`, `␣insists` | 58 | L35-58; most at L42 (35), L48 (35), L54 (29) |
| 2 | neutral (neutral, even-handed) | unclear | `中立` | 24 | L35-37; most at L35 (13), L36 (21), L37 (3) |
| 2 | claim (claiming) | unclear | `声称`, `␣claim`, `claim`, `␣claims`, `␣claimed`, `␣Claim`, `␣claiming`, `Claim` | 10 | L36-58; most at L40 (6), L51 (5), L52 (6) |
| 2 | assert (asserting) | unclear | `assert`, `␣assert`, `␣asserting`, `␣assertions`, `␣asserts` | 25 | L35-58; most at L36 (11), L43 (11), L49 (13) |
| 2 | legitimate (legitimate, justified) | unclear | `正当`, `␣legitimate` | 3 | L35-45; most at L35 (1), L38 (1), L45 (1) |
| 2 | justify (justifying, defending) | unclear | `辩护`, `justify` | 3 | L36-57; most at L37 (2), L54 (1), L57 (1) |
| 2 | contradict (contradicting) | unclear | `␣contradict`, `矛盾`, `矛盾的`, `␣contradictory`, `␣contradiction` | 19 | L35-58; most at L42 (7), L43 (6), L50 (8) |
| 2 | ostensible (on the surface only) | unclear | `表面上`, `表面` | 62 | L35-49; most at L36 (52), L37 (53), L38 (44) |
| 2 | official line (the agreed story (口径)) | unclear | `口径` | 40 | L35-58; most at L51 (22), L52 (24), L53 (22) |
| 2 | disclose (disclosing, revealing) | truth | `公开`, `␣disclosure`, `␣disclosed`, `␣disclosures`, `␣Disclosure`, `披露`, `信息披露`, `␣disclose`, `␣disclosing`, `Disclosure`, `␣revealed`, `␣revealing` | 20 | L35-58; most at L38 (10), L47 (6), L53 (4) |
| 2 | pander (pandering to someone) | unclear | `迎合` | 7 | L36-50; most at L41 (2), L42 (2), L50 (2) |
| 2 | coax (coaxing, fooling (哄)) | unclear | `哄` | 8 | L37-42; most at L39 (6), L40 (3), L42 (3) |

## q_tok25

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | honest (being honest) | truth | `诚信`, `诚实` | 6 | L35-53; most at L36 (4), L40 (2), L52 (1) |
| 1 | deny (denying) | lie | `否认`, `否定`, `␣denying` | 211 | L35-56; most at L37 (193), L38 (211), L39 (197) |
| 1 | integrity (integrity, uprightness) | truth | `␣integrity` | 17 | L51-53; most at L51 (3), L52 (5), L53 (17) |
| 1 | innocent (innocent, clean record) | truth | `清白` | 202 | L35-45; most at L36 (192), L37 (191), L40 (160) |
| 1 | claim (claiming) | unclear | `claim`, `␣claiming`, `␣claim` | 101 | L35-50; most at L36 (56), L37 (34), L47 (88) |
| 1 | assert (asserting) | unclear | `assert` | 190 | L35-47; most at L35 (140), L36 (88), L43 (175) |
| 1 | legitimate (legitimate, justified) | unclear | `正当` | 54 | L35-37; most at L35 (7), L36 (54), L37 (3) |
| 1 | neutral (neutral) | unclear | `中立` | 122 | L35-44; most at L36 (69), L37 (106), L39 (112) |
| 1 | direct (direct, straightforward) | unclear | `␣straightforward` | 1 | L36-36; most at L36 (1) |
| 2 | honest (being honest) | truth | `诚实` | 1 | L36-36; most at L36 (1) |
| 2 | candid (frank, straightforward) | truth | `␣straightforward` | 1 | L36-36; most at L36 (1) |
| 2 | integrity (integrity, uprightness) | truth | `␣integrity`, `诚信` | 21 | L35-53; most at L51 (3), L52 (6), L53 (18) |
| 2 | deny (denying) | lie | `否认`, `否定`, `␣denying` | 211 | L35-56; most at L37 (193), L38 (211), L39 (197) |
| 2 | neutral (neutral, even-handed) | unclear | `持平`, `中立` | 187 | L35-45; most at L37 (107), L39 (115), L44 (135) |
| 2 | innocent (innocent, with a clean record) | truth | `清白` | 202 | L35-45; most at L36 (192), L37 (191), L40 (160) |
| 2 | kidding (joking, not serious) | unclear | `␣kidding` | 233 | L51-58; most at L54 (233), L55 (233), L56 (217) |
| 2 | claim (claiming) | unclear | `claim`, `␣claiming`, `␣claim` | 101 | L35-50; most at L36 (56), L37 (34), L47 (88) |
| 2 | assert (asserting) | unclear | `assert`, `Assertions` | 190 | L35-47; most at L35 (140), L36 (88), L43 (175) |
| 2 | legitimate (legitimate, justified) | unclear | `正当` | 54 | L35-37; most at L35 (7), L36 (54), L37 (3) |

## q_tok26

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception` | 39 | L35-58; most at L38 (19), L44 (10), L50 (15) |
| 1 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `误导性` | 17 | L45-58; most at L53 (10), L54 (9), L55 (6) |
| 1 | honest (being honest) | truth | `诚`, `诚实`, `␣honest`, `␣honesty`, `诚信`, `␣honestly`, `␣Honest`, `诚实守信` | 151 | L35-58; most at L37 (111), L38 (108), L40 (90) |
| 1 | candid (frank, open about it) | truth | `坦诚`, `␣upfront`, `␣frank` | 14 | L35-56; most at L38 (8), L39 (8), L41 (8) |
| 1 | confess (owning up to the act) | truth | `坦白` | 3 | L51-54; most at L51 (2), L52 (2), L53 (3) |
| 1 | admit (admitting or acknowledging) | truth | `承认`, `␣admitting`, `␣acknowledge`, `␣admit`, `␣admits`, `␣acknowledging`, `␣admission`, `␣acknowledges`, `␣admitted`, `␣acknowledged`, `␣admite`, `␣acknowledgement`, `␣acknowledgment` | 34 | L35-58; most at L47 (21), L50 (17), L55 (16) |
| 1 | deny (denying) | lie | `否认`, `否定`, `␣denying`, `␣denial`, `␣deny`, `␣denies`, `␣denied`, `deny`, `␣Denied` | 63 | L35-58; most at L47 (32), L48 (33), L49 (33) |
| 1 | refuse (refusing or declining) | unclear | `␣refusal`, `␣refusing`, `拒绝`, `␣refuse`, `␣refused`, `␣refuses`, `拒`, `␣refus`, `拒絕`, `␣decline`, `␣declined`, `␣declining`, `␣declines`, `拒绝了`, `拒不` | 16 | L36-58; most at L50 (15), L56 (15), L57 (14) |
| 1 | conceal (concealing or hiding) | lie | `掩盖`, `隐瞒`, `掩饰`, `␣conceal`, `␣hiding`, `遮盖`, `␣hide`, `␣concealed`, `_hide`, `隐藏`, `遮掩`, `遮蔽`, `hide`, `Hide`, `-hide`, `瞒`, `隐匿`, `遮住` | 94 | L35-58; most at L48 (69), L49 (69), L50 (62) |
| 1 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 8 | L50-58; most at L51 (5), L52 (6), L53 (6) |
| 1 | omit (leaving things out) | lie | `␣omit`, `omit`, `␣omission` | 14 | L36-56; most at L49 (7), L50 (6), L52 (9) |
| 1 | secret (secrecy, confidentiality) | lie | `␣confidentiality`, `保密` | 2 | L40-53; most at L51 (1), L52 (1), L53 (1) |
| 1 | fabricate (making things up) | lie | `␣fabricated`, `凭空`, `␣invented`, `伪造`, `␣fabrication`, `␣invent` | 85 | L35-58; most at L36 (64), L37 (72), L43 (33) |
| 1 | fictional (fictional, made-up story) | unclear | `虚构`, `␣fictional`, `fiction`, `-fiction`, `␣fiction`, `␣Fiction` | 98 | L35-58; most at L38 (67), L45 (63), L46 (70) |
| 1 | fake (fake, sham) | lie | `fake`, `␣fake`, `伪`, `作假` | 22 | L36-50; most at L38 (8), L44 (15), L45 (7) |
| 1 | pretend (pretending, disguising) | lie | `假装`, `伪装` | 7 | L46-50; most at L46 (3), L48 (2), L50 (3) |
| 1 | misinformation (false information) | lie | `虚假信息`, `␣misinformation` | 17 | L36-54; most at L37 (11), L38 (8), L53 (5) |
| 1 | exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 51 | L35-57; most at L36 (22), L43 (22), L46 (21) |
| 1 | downplay (downplaying) | lie | `淡化` | 13 | L35-55; most at L38 (6), L49 (6), L50 (8) |
| 1 | vague (vague or ambiguous) | unclear | `␣vague`, `含糊`, `␣vaguely`, `模糊`, `␣ambiguous`, `␣ambiguity`, `␣ambigu` | 35 | L35-58; most at L49 (23), L50 (22), L51 (22) |
| 1 | euphemistic (tactful, indirect wording) | unclear | `委婉` | 2 | L40-53; most at L40 (1), L41 (1), L48 (2) |
| 1 | evade (evading, dodging) | lie | `␣evasion`, `回避`, `␣dodge`, `␣evade` | 7 | L47-58; most at L52 (3), L53 (4), L57 (3) |
| 1 | perfunctory (brushing off, perfunctory) | unclear | `敷衍` | 2 | L47-48; most at L47 (2), L48 (1) |
| 1 | deliberate (doing it on purpose) | unclear | `故意`, `␣deliberately`, `␣intentionally`, `␣deliberate`, `刻意`, `␣intentional`, `有意` | 19 | L36-58; most at L39 (5), L51 (6), L52 (6) |
| 1 | knowingly (knowing it was so) | unclear | `明知`, `␣knowingly` | 19 | L35-58; most at L43 (9), L44 (7), L45 (6) |
| 1 | ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣moral`, `ethical`, `␣Ethics`, `道德`, `的道德` | 9 | L36-58; most at L52 (8), L53 (8), L54 (8) |
| 1 | integrity (integrity, uprightness) | truth | `␣integrity`, `正直` | 2 | L51-54; most at L51 (1), L52 (1), L54 (1) |
| 1 | transparent (transparency) | truth | `透明`, `␣transparency`, `-transparent`, `␣transparent`, `transparent`, `透明的`, `透明度`, `␣Transparency`, `␣transparencia` | 12 | L35-58; most at L47 (5), L48 (5), L54 (6) |
| 1 | genuine (genuine, authentic) | truth | `␣genuine`, `␣genuinely`, `␣Genuine` | 87 | L35-58; most at L35 (57), L36 (83), L37 (66) |
| 1 | sincere (sincere) | truth | `真诚` | 6 | L36-53; most at L36 (3), L37 (2), L38 (4) |
| 1 | trustworthy (credible, trustworthy) | truth | `可信`, `␣credible` | 2 | L37-45; most at L37 (1), L43 (2), L44 (1) |
| 1 | loyal (loyal, faithful) | unclear | `忠`, `␣faithful`, `␣faithfully`, `忠诚`, `忠实`, `忠于` | 4 | L37-58; most at L37 (1), L39 (3), L43 (2) |
| 1 | comply (complying with instructions or rules) | unclear | `␣adherence`, `␣adher`, `合规`, `遵循`, `␣adhere`, `␣compliance`, `遵守`, `严格遵守`, `␣comply`, `␣compliant`, `␣Compliance`, `␣complied`, `遵守国家` | 13 | L50-58; most at L52 (11), L53 (9), L54 (8) |
| 1 | follow (following (instructions)) | unclear | `␣follow`, `␣follows` | 1 | L50-53; most at L50 (1), L51 (1), L52 (1) |
| 1 | fulfill (fulfilling a duty or task) | unclear | `␣fulfill` | 1 | L47-47; most at L47 (1) |
| 1 | role / persona (the role or persona the model was given) | unclear | `␣role`, `role`, `的角色`, `Role`, `␣roles`, `roles`, `␣persona`, `␣personas`, `␣Persona`, `角色` | 4 | L50-58; most at L55 (3), L56 (3), L57 (4) |
| 1 | simulate (simulating) | unclear | `模拟`, `␣simulated` | 2 | L39-57; most at L39 (1), L51 (2), L52 (2) |
| 1 | maintain (maintaining a position, persisting) | unclear | `坚持`, `必须坚持`, `坚守`, `要坚持`, `维持`, `␣maintain`, `␣maintaining`, `始终坚持` | 25 | L37-58; most at L47 (14), L48 (15), L50 (15) |
| 1 | firm (being firm) | unclear | `␣firmly`, `坚定的`, `坚定` | 6 | L40-56; most at L53 (3), L54 (4), L56 (2) |
| 1 | uphold / defend (upholding or defending) | unclear | `维护`, `␣uphold`, `维护和` | 26 | L35-58; most at L41 (7), L52 (5), L57 (5) |
| 1 | justify (justifying) | unclear | `辩护` | 1 | L54-55; most at L54 (1), L55 (1) |
| 1 | claim (claiming) | unclear | `声称`, `␣claim`, `␣claims`, `␣claiming`, `␣claimed`, `claim`, `␣Claim`, `宣称`, `Claim`, `␣Claims`, `claims`, `Claims`, `_claim`, `␣CLAIM`, `CLAIM`, `claimed` | 99 | L35-58; most at L43 (64), L47 (57), L50 (55) |
| 1 | so-called (so-called) | unclear | `所谓`, `所谓的` | 36 | L47-58; most at L51 (28), L52 (16), L53 (26) |
| 1 | assert (asserting) | unclear | `assert`, `␣assert`, `␣asserting`, `␣assertions`, `␣asserts`, `␣assertion`, `␣Assert`, `␣asserted`, `Assert`, `Assertion`, `␣Assertion` | 42 | L35-58; most at L48 (25), L53 (20), L54 (25) |
| 1 | framing (framing, how it is presented) | unclear | `␣framing`, `␣frames`, `␣frame`, `␣framed` | 48 | L43-58; most at L52 (37), L53 (28), L58 (17) |
| 1 | technically (technically (true)) | unclear | `␣technically` | 44 | L35-58; most at L44 (23), L45 (14), L55 (15) |
| 1 | plausible (plausible) | unclear | `␣plausible` | 34 | L35-57; most at L44 (28), L45 (25), L46 (20) |
| 1 | blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blamed`, `␣blames` | 26 | L48-58; most at L54 (21), L55 (18), L56 (18) |
| 1 | violate (violating, going against) | lie | `违背`, `违反`, `违`, `违反了` | 30 | L35-52; most at L45 (12), L48 (13), L49 (18) |
| 1 | illegal (breaking the law) | lie | `违法` | 4 | L35-48; most at L35 (3), L44 (2), L45 (2) |
| 1 | contradict (contradicting) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `矛盾`, `矛盾的` | 35 | L35-58; most at L49 (18), L50 (20), L51 (14) |
| 1 | ostensibly (on the surface (but not in reality)) | unclear | `表面上` | 20 | L36-50; most at L42 (7), L46 (7), L47 (11) |
| 1 | legitimate (legitimate, justified) | unclear | `␣legitimate`, `正当`, `␣legitimately`, `正当理由` | 14 | L35-58; most at L36 (8), L43 (8), L44 (5) |
| 1 | legal (legal) | unclear | `合法`, `合法性` | 13 | L35-58; most at L43 (4), L44 (7), L45 (3) |
| 1 | objective (objective) | truth | `客观`, `␣objectively`, `␣objective` | 137 | L35-54; most at L35 (108), L36 (98), L39 (67) |
| 1 | fact (the facts, factual) | truth | `事实`, `␣fact`, `␣factual`, `实情`, `实际情况`, `␣facts`, `实事求是`, `的事实`, `Fact`, `␣Fact`, `fact`, `␣FACT`, `FACT`, `事实和`, `facts`, `␣Facts`, `_fact`, `根据实际情况` | 226 | L35-58; most at L38 (201), L39 (204), L40 (203) |
| 1 | disclose (disclosing, revealing) | truth | `揭露`, `␣disclosure`, `␣revealing`, `公开`, `␣disclosed`, `␣revealed`, `␣reveal`, `␣disclose`, `␣Disclosure`, `reveal`, `␣disclosing`, `揭示`, `透露`, `揭示了` | 12 | L35-58; most at L44 (8), L45 (7), L47 (4) |
| 1 | direct (direct, straightforward) | unclear | `直接`, `␣direct`, `␣directly`, `Direct` | 37 | L35-52; most at L42 (16), L43 (16), L44 (14) |
| 1 | indirect (indirect) | unclear | `␣indirect`, `␣indirectly` | 1 | L43-52; most at L43 (1), L44 (1), L45 (1) |
| 2 | honest (being honest) | truth | `诚`, `诚实`, `␣honest`, `␣honesty`, `␣honestly`, `␣Honest`, `诚实守信` | 151 | L35-58; most at L37 (111), L38 (108), L40 (90) |
| 2 | truth (the truth (what really happened)) | truth | `␣truth`, `truth`, `实话`, `␣Truth`, `真相`, `实情`, `Truth`, `␣truths`, `真理`, `_truth`, `说实话`, `.truth` | 223 | L35-58; most at L35 (218), L36 (196), L38 (200) |
| 2 | factual (matching the facts) | unclear | `事实`, `␣fact`, `␣factual`, `␣facts`, `事实上`, `实事求是`, `的事实`, `Fact`, `␣Fact`, `fact`, `␣FACT`, `FACT`, `事实和`, `facts`, `␣Facts`, `_fact` | 220 | L35-58; most at L38 (179), L39 (196), L40 (196) |
| 2 | objective (objective, without bias) | unclear | `客观`, `␣objectively`, `␣objective` | 137 | L35-54; most at L35 (108), L36 (98), L39 (67) |
| 2 | transparent (being transparent) | truth | `透明`, `-transparent`, `␣transparency`, `␣transparent`, `transparent`, `透明的`, `透明度`, `␣Transparency`, `␣transparencia` | 12 | L35-58; most at L47 (5), L48 (5), L54 (6) |
| 2 | candid (frank, straightforward) | truth | `坦诚`, `␣upfront` | 13 | L35-56; most at L38 (8), L39 (8), L41 (8) |
| 2 | confess (coming clean, confessing) | truth | `坦白` | 3 | L51-54; most at L51 (2), L52 (2), L53 (3) |
| 2 | sincere (sincere) | truth | `真诚` | 6 | L36-53; most at L36 (3), L37 (2), L38 (4) |
| 2 | genuine (genuine, real) | unclear | `␣genuine`, `␣genuinely`, `真正的`, `真正`, `的真正`, `␣Genuine` | 92 | L35-58; most at L35 (57), L36 (83), L37 (66) |
| 2 | integrity (integrity, uprightness) | truth | `诚信`, `␣integrity`, `正直` | 8 | L35-54; most at L36 (4), L37 (2), L38 (5) |
| 2 | faithful (faithful, true to something) | unclear | `␣faithful`, `␣faithfully`, `忠实`, `忠于` | 1 | L37-58; most at L37 (1), L38 (1), L39 (1) |
| 2 | loyal (loyalty) | unclear | `忠`, `忠诚` | 4 | L39-58; most at L39 (3), L43 (2), L52 (1) |
| 2 | trustworthy (trustworthy, credible) | truth | `可信` | 2 | L37-45; most at L37 (1), L43 (2), L44 (1) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception` | 39 | L35-58; most at L38 (19), L44 (10), L50 (15) |
| 2 | mislead (misleading) | lie | `␣misleading`, `误导`, `误导性` | 17 | L45-58; most at L53 (10), L54 (9), L55 (6) |
| 2 | conceal (concealing, hiding) | lie | `掩盖`, `隐瞒`, `掩饰`, `␣conceal`, `␣concealed`, `遮掩`, `掩护`, `掩`, `隐藏`, `␣hide`, `_hide`, `隐匿`, `Hide`, `-hide`, `hide` | 94 | L35-58; most at L48 (69), L49 (69), L50 (62) |
| 2 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 8 | L50-58; most at L51 (5), L52 (6), L53 (6) |
| 2 | omit (leaving something out) | lie | `␣omit`, `omit`, `␣omission` | 14 | L36-56; most at L49 (7), L50 (6), L52 (9) |
| 2 | secret (keeping secret, confidential) | lie | `保密`, `␣confidentiality` | 2 | L40-53; most at L51 (1), L52 (1), L53 (1) |
| 2 | falsehood (a false statement, false information) | lie | `␣falsehood`, `虚假信息`, `␣misinformation` | 44 | L35-58; most at L37 (20), L38 (31), L50 (24) |
| 2 | fabricate (making something up) | lie | `␣fabricated`, `凭空`, `␣invented`, `伪造`, `␣fabrication`, `␣invent`, `␣invention`, `作假` | 85 | L35-58; most at L36 (64), L37 (72), L43 (33) |
| 2 | fake (fake) | lie | `fake`, `␣fake` | 21 | L36-46; most at L38 (8), L44 (15), L45 (7) |
| 2 | pretend (pretending) | lie | `假装` | 4 | L46-48; most at L46 (3), L48 (1) |
| 2 | fiction (fictional, invented story) | unclear | `虚构`, `␣fictional`, `fiction`, `-fiction`, `␣fiction`, `␣Fiction` | 98 | L35-58; most at L38 (67), L45 (63), L46 (70) |
| 2 | exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 51 | L35-57; most at L36 (22), L43 (22), L46 (21) |
| 2 | downplay (downplaying) | lie | `淡化` | 13 | L35-55; most at L38 (6), L49 (6), L50 (8) |
| 2 | deliberate (doing it on purpose) | unclear | `故意`, `␣deliberately`, `␣deliberate`, `␣intentionally`, `刻意`, `␣intentional`, `有意` | 19 | L36-58; most at L39 (5), L51 (6), L52 (6) |
| 2 | knowingly (knowing it is so) | unclear | `明知`, `␣knowingly` | 19 | L35-58; most at L43 (9), L44 (7), L45 (6) |
| 2 | deny (denying) | lie | `否认`, `否定`, `␣denying`, `␣denial`, `␣deny`, `␣denies`, `␣denied`, `deny`, `␣Denied` | 63 | L35-58; most at L47 (32), L48 (33), L49 (33) |
| 2 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admit`, `␣admits`, `␣admitted`, `␣admite` | 34 | L35-58; most at L47 (21), L50 (17), L55 (16) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledge`, `␣acknowledging`, `␣acknowledges`, `␣acknowledged`, `␣acknowledgment`, `␣acknowledgement` | 12 | L36-58; most at L56 (9), L57 (10), L58 (10) |
| 2 | refuse (refusing, declining) | unclear | `␣refusal`, `␣refusing`, `拒绝`, `␣refuse`, `␣refused`, `␣refuses`, `␣refus`, `拒`, `拒絕`, `␣decline`, `␣declined`, `␣declining`, `␣declines`, `拒绝了`, `拒不` | 16 | L36-58; most at L50 (15), L56 (15), L57 (14) |
| 2 | evade (evading) | lie | `␣evasion`, `回避`, `␣evade` | 7 | L47-58; most at L52 (3), L53 (4), L57 (3) |
| 2 | vague (being vague) | unclear | `␣vague`, `含糊`, `␣vaguely` | 35 | L35-58; most at L49 (23), L50 (22), L51 (21) |
| 2 | ethical (ethical) | unclear | `␣ethical`, `␣ethics`, `伦理`, `ethical`, `␣Ethics` | 9 | L36-58; most at L52 (8), L53 (8), L54 (8) |
| 2 | violate (violating a rule or principle) | unclear | `违背`, `违反`, `违反了` | 29 | L35-52; most at L45 (11), L48 (13), L49 (18) |
| 2 | comply (complying, adhering, obeying) | unclear | `␣adherence`, `␣adher`, `合规`, `遵循`, `␣adhere`, `␣compliance`, `遵守`, `严格遵守`, `␣comply`, `␣Compliance`, `␣compliant`, `␣complied` | 13 | L50-58; most at L52 (11), L53 (9), L54 (8) |
| 2 | role-play (playing a role) | unclear | `␣role`, `role`, `的角色`, `Role`, `␣roles`, `roles`, `角色` | 3 | L50-58; most at L55 (2), L56 (2), L57 (3) |
| 2 | persona (an assumed persona) | unclear | `␣persona`, `␣Persona`, `␣personas` | 1 | L52-58; most at L52 (1), L53 (1), L54 (1) |
| 2 | insist (holding firm, insisting) | unclear | `坚持`, `必须坚持`, `要坚持`, `坚守`, `␣firmly`, `坚定的`, `始终坚持`, `坚定` | 25 | L37-58; most at L47 (14), L50 (15), L54 (14) |
| 2 | claim (claiming) | unclear | `声称`, `␣claim`, `␣claims`, `␣claiming`, `␣claimed`, `claim`, `␣Claim`, `宣称`, `Claim`, `␣Claims`, `claims`, `Claims`, `_claim`, `␣CLAIM`, `CLAIM`, `claimed` | 99 | L35-58; most at L43 (64), L47 (57), L50 (55) |
| 2 | assert (asserting) | unclear | `assert`, `␣assert`, `␣asserting`, `␣assertions`, `␣asserts`, `␣assertion`, `␣Assert`, `␣asserted`, `Assert`, `Assertion`, `␣Assertion` | 42 | L35-58; most at L48 (25), L53 (20), L54 (25) |
| 2 | legitimate (legitimate, justified) | unclear | `␣legitimate`, `正当`, `␣legitimately`, `正当理由` | 14 | L35-58; most at L36 (8), L43 (8), L44 (5) |
| 2 | justify (justifying, defending) | unclear | `辩护` | 1 | L54-55; most at L54 (1), L55 (1) |
| 2 | contradict (contradicting) | unclear | `␣contradict`, `␣contradictory`, `矛盾`, `矛盾的` | 32 | L36-58; most at L49 (18), L50 (20), L51 (14) |
| 2 | blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blamed`, `␣blames` | 26 | L48-58; most at L54 (21), L55 (18), L56 (18) |
| 2 | ostensible (on the surface only) | unclear | `表面上`, `表面`, `的表面` | 20 | L36-50; most at L42 (7), L46 (7), L47 (11) |
| 2 | official line (the agreed story (口径)) | unclear | `口径` | 23 | L35-57; most at L51 (16), L52 (7), L53 (12) |
| 2 | disclose (disclosing, revealing) | truth | `␣disclosure`, `␣revealing`, `公开`, `␣disclosed`, `␣disclose`, `␣disclosing`, `␣Disclosure`, `␣revealed`, `␣reveal`, `reveal`, `披露`, `透露` | 6 | L45-58; most at L48 (3), L52 (3), L53 (4) |
| 2 | coax (coaxing, fooling (哄)) | unclear | `哄` | 6 | L37-44; most at L37 (3), L40 (3), L41 (5) |
| 2 | perfunctory (going through the motions) | unclear | `敷衍` | 2 | L47-48; most at L47 (2), L48 (1) |

## q_tok27

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗`, `␣deceptive`, `␣deceive` | 17 | L35-58; most at L37 (9), L51 (7), L52 (8) |
| 1 | mislead (leading someone to a wrong belief) | lie | `␣misleading` | 1 | L52-57; most at L52 (1), L53 (1), L54 (1) |
| 1 | honest (being honest) | truth | `诚实`, `␣honesty`, `诚`, `诚信`, `␣honest` | 43 | L35-58; most at L51 (19), L52 (23), L55 (24) |
| 1 | admit (admitting or acknowledging) | truth | `承认` | 4 | L35-54; most at L35 (2), L36 (1), L37 (1) |
| 1 | deny (denying) | lie | `否认`, `否定` | 3 | L40-50; most at L40 (1), L48 (1), L50 (1) |
| 1 | refuse (refusing or declining) | unclear | `拒绝`, `␣refusal`, `拒`, `␣refused`, `␣refusing`, `␣refuse`, `␣refuses`, `拒绝了`, `␣refus`, `␣decline`, `拒絕`, `ปฏิเสธ`, `␣declined`, `␣declines`, `␣declining`, `拒不` | 43 | L35-58; most at L45 (34), L46 (34), L47 (36) |
| 1 | reject (rejecting) | unclear | `␣rejection`, `␣reject`, `␣rejecting`, `␣rejects`, `␣rejected`, `Reject`, `抗拒`, `reject`, `␣Reject` | 20 | L39-53; most at L44 (16), L45 (16), L48 (16) |
| 1 | conceal (concealing or hiding) | lie | `隐瞒`, `隐藏`, `␣conceal`, `掩盖`, `␣hidden`, `␣hiding`, `掩饰`, `隐藏的` | 44 | L35-58; most at L40 (15), L50 (34), L53 (12) |
| 1 | withhold (withholding information) | lie | `␣withhold`, `␣withholding` | 15 | L39-56; most at L51 (10), L52 (9), L53 (3) |
| 1 | omit (leaving things out) | lie | `␣omit`, `␣omission` | 8 | L45-58; most at L52 (7), L53 (7), L55 (3) |
| 1 | secret (secrecy, confidentiality) | lie | `保密` | 2 | L36-40; most at L36 (1), L38 (1), L40 (1) |
| 1 | silence (keeping silent) | unclear | `沉默` | 2 | L38-39; most at L38 (1), L39 (1) |
| 1 | fabricate (making things up) | lie | `␣fabricated`, `伪造`, `凭空`, `␣invented`, `␣fabrication` | 9 | L35-57; most at L36 (6), L37 (5), L56 (2) |
| 1 | fictional (fictional, made-up story) | unclear | `␣fictional`, `虚构`, `fiction`, `␣fiction`, `␣Fiction` | 118 | L35-57; most at L35 (51), L36 (82), L37 (92) |
| 1 | fake (fake, sham) | lie | `fake`, `_fake` | 13 | L36-38; most at L36 (7), L37 (11), L38 (1) |
| 1 | pretend (pretending, disguising) | lie | `␣pretend` | 4 | L47-50; most at L47 (1), L50 (4) |
| 1 | exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated`, `夸张` | 4 | L35-58; most at L36 (2), L54 (3), L55 (3) |
| 1 | downplay (downplaying) | lie | `淡化` | 5 | L35-55; most at L49 (2), L50 (3), L53 (2) |
| 1 | vague (vague or ambiguous) | unclear | `模糊` | 1 | L47-48; most at L47 (1), L48 (1) |
| 1 | euphemistic (tactful, indirect wording) | unclear | `委婉` | 8 | L35-54; most at L35 (4), L36 (4), L40 (6) |
| 1 | evade (evading, dodging) | lie | `吞吐`, `␣evasion`, `回避` | 35 | L35-58; most at L35 (12), L36 (25), L37 (21) |
| 1 | deliberate (doing it on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `刻意` | 36 | L35-57; most at L35 (35), L36 (24), L37 (7) |
| 1 | knowingly (knowing it was so) | unclear | `明知` | 126 | L35-50; most at L35 (120), L36 (33), L47 (24) |
| 1 | ethics (ethics, morality) | unclear | `␣ethical`, `伦理`, `␣ethics`, `道德`, `␣moral`, `的道德`, `␣morally`, `ethical`, `␣Ethics`, `职业道德`, `␣morality`, `␣morals`, `␣Moral` | 43 | L35-58; most at L38 (18), L39 (23), L40 (31) |
| 1 | unethical (unethical) | lie | `␣unethical` | 6 | L39-58; most at L55 (3), L56 (3), L58 (3) |
| 1 | integrity (integrity, uprightness) | truth | `␣integrity`, `正直` | 4 | L51-57; most at L51 (3), L52 (1), L56 (2) |
| 1 | loyal (loyal, faithful) | unclear | `␣loyalty`, `忠实`, `␣faithfully`, `忠诚`, `␣loyal`, `忠于`, `忠诚度`, `忠`, `忠心` | 52 | L36-58; most at L51 (30), L52 (27), L53 (32) |
| 1 | comply (complying with instructions or rules) | unclear | `␣adher`, `遵守`, `遵循`, `合规`, `服从`, `␣adherence`, `␣adhere`, `严格遵守`, `遵从`, `␣obey`, `遵照`, `␣comply`, `␣compliance`, `遵`, `␣Compliance`, `␣complied`, `␣complying`, `␣compliant` | 171 | L35-58; most at L46 (100), L50 (95), L53 (95) |
| 1 | follow (following (instructions)) | unclear | `␣follow`, `␣followed`, `␣Follow`, `Follow`, `follow`, `_follow`, `-follow`, `␣follows`, `␣FOLLOW`, `.follow`, `_FOLLOW` | 46 | L49-58; most at L56 (40), L57 (45), L58 (42) |
| 1 | fulfill (fulfilling a duty or task) | unclear | `履行`, `␣fulfill`, `␣fulfilling`, `履行职责`, `␣fulfilled`, `␣fulfillment` | 105 | L35-58; most at L35 (58), L40 (51), L46 (68) |
| 1 | role-play (playing a role) | unclear | `扮演`, `角色扮演`, `扮演着` | 146 | L36-58; most at L51 (133), L52 (116), L53 (105) |
| 1 | role / persona (the role or persona the model was given) | unclear | `␣role`, `␣persona`, `角色`, `role`, `-role`, `Role`, `角色的`, `␣Persona`, `␣personas`, `␣Role`, `的角色`, `ROLE`, `Persona`, `persona`, `(role`, `␣roles`, `.role`, `_role`, `␣ROLE`, `␣Personas`, `roles`, `这个角色`, `_ROLE`, `<Role`, `_persona` | 143 | L35-58; most at L42 (119), L43 (112), L51 (109) |
| 1 | simulate (simulating) | unclear | `模拟`, `␣simulated`, `␣simulation`, `仿真`, `␣simulate`, `␣simulations` | 123 | L35-58; most at L35 (99), L36 (106), L37 (87) |
| 1 | maintain (maintaining a position, persisting) | unclear | `坚持`, `维持`, `␣maintain`, `␣maintaining`, `坚守`, `␣maintained`, `␣maintains`, `␣Maintain`, `必须坚持` | 108 | L35-58; most at L46 (50), L47 (59), L49 (46) |
| 1 | firm (being firm) | unclear | `坚定的`, `坚定`, `␣firmly`, `坚定地` | 26 | L35-49; most at L37 (21), L38 (14), L40 (14) |
| 1 | uphold / defend (upholding or defending) | unclear | `维护`, `为维护`, `和维护`, `␣uphold`, `维护和` | 136 | L35-58; most at L43 (97), L44 (83), L46 (86) |
| 1 | justify (justifying) | unclear | `辩护`, `␣justified`, `␣justification` | 20 | L36-58; most at L40 (8), L41 (17), L42 (11) |
| 1 | claim (claiming) | unclear | `声称` | 1 | L54-54; most at L54 (1) |
| 1 | framing (framing, how it is presented) | unclear | `␣framing`, `␣frame` | 3 | L37-58; most at L51 (1), L52 (1), L58 (2) |
| 1 | violate (violating, going against) | lie | `违背`, `违`, `违反`, `违反了`, `违规` | 68 | L35-58; most at L35 (47), L37 (26), L38 (25) |
| 1 | illegal (breaking the law) | lie | `违法` | 2 | L44-48; most at L44 (1), L46 (2), L48 (2) |
| 1 | contradict (contradicting) | unclear | `矛盾`, `␣contradictory`, `␣contradict`, `矛盾的`, `␣contrad`, `之间的矛盾`, `␣contradiction`, `␣contradictions` | 19 | L35-50; most at L46 (15), L47 (17), L48 (13) |
| 1 | ostensibly (on the surface (but not in reality)) | unclear | `表面上` | 22 | L36-51; most at L36 (9), L37 (8), L43 (9) |
| 1 | legitimate (legitimate, justified) | unclear | `正当` | 2 | L35-38; most at L35 (1), L38 (1) |
| 1 | legal (legal) | unclear | `合法的`, `合法` | 5 | L49-52; most at L49 (1), L50 (4), L52 (1) |
| 1 | objective (objective) | truth | `客观` | 24 | L35-48; most at L35 (17), L36 (13), L44 (7) |
| 1 | fact (the facts, factual) | truth | `实事求是`, `␣factual`, `事实` | 12 | L40-55; most at L52 (5), L53 (11), L55 (4) |
| 1 | manipulate (manipulating) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated` | 3 | L54-56; most at L54 (3), L55 (2), L56 (2) |
| 1 | pander (pandering, pleasing) | unclear | `迎合`, `讨好` | 23 | L35-58; most at L35 (15), L36 (19), L46 (5) |
| 1 | forced (being forced) | unclear | `被迫`, `␣forced` | 17 | L35-53; most at L47 (9), L49 (9), L50 (8) |
| 1 | disclose (disclosing, revealing) | truth | `揭` | 1 | L53-53; most at L53 (1) |
| 1 | direct (direct, straightforward) | unclear | `直接`, `␣direct` | 32 | L35-48; most at L35 (15), L36 (12), L43 (13) |
| 2 | honest (being honest) | truth | `诚实`, `␣honesty`, `诚`, `␣honest` | 43 | L35-58; most at L51 (18), L52 (22), L55 (24) |
| 2 | truth (the truth (what really happened)) | truth | `␣truth`, `truth`, `Truth`, `␣Truth`, `真相`, `实话`, `␣truths`, `_truth`, `说实话` | 98 | L35-58; most at L53 (44), L55 (86), L56 (50) |
| 2 | factual (matching the facts) | unclear | `实事求是`, `␣factual`, `事实` | 12 | L40-55; most at L52 (5), L53 (11), L55 (4) |
| 2 | objective (objective, without bias) | unclear | `客观` | 24 | L35-48; most at L35 (17), L36 (13), L44 (7) |
| 2 | integrity (integrity, uprightness) | truth | `诚信`, `␣integrity`, `正直` | 7 | L38-57; most at L51 (5), L55 (3), L56 (2) |
| 2 | faithful (faithful, true to something) | unclear | `忠实`, `␣faithfully`, `忠于` | 33 | L36-58; most at L38 (16), L53 (12), L57 (10) |
| 2 | loyal (loyalty) | unclear | `␣loyalty`, `忠诚`, `␣loyal`, `忠诚度`, `忠`, `忠心` | 34 | L37-58; most at L51 (27), L52 (23), L53 (24) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗`, `␣deceptive`, `␣deceive` | 17 | L35-58; most at L37 (9), L51 (7), L52 (8) |
| 2 | mislead (misleading) | lie | `␣misleading` | 1 | L52-57; most at L52 (1), L53 (1), L54 (1) |
| 2 | conceal (concealing, hiding) | lie | `隐瞒`, `隐藏`, `␣conceal`, `掩盖`, `掩饰`, `␣hidden`, `隐藏的` | 44 | L35-58; most at L40 (15), L50 (34), L53 (12) |
| 2 | withhold (withholding information) | lie | `␣withhold`, `␣withholding` | 15 | L39-56; most at L51 (10), L52 (9), L53 (3) |
| 2 | omit (leaving something out) | lie | `␣omit`, `␣omission` | 8 | L45-58; most at L52 (7), L53 (7), L55 (3) |
| 2 | secret (keeping secret, confidential) | lie | `保密` | 2 | L36-40; most at L36 (1), L38 (1), L40 (1) |
| 2 | falsehood (a false statement, false information) | lie | `␣falsehood` | 6 | L55-58; most at L55 (6), L56 (4), L57 (1) |
| 2 | fabricate (making something up) | lie | `␣fabricated`, `伪造`, `凭空`, `␣fabrication`, `␣invented` | 9 | L35-57; most at L36 (6), L37 (5), L56 (2) |
| 2 | fake (fake) | lie | `fake`, `_fake` | 13 | L36-38; most at L36 (7), L37 (11), L38 (1) |
| 2 | pretend (pretending) | lie | `␣pretend` | 4 | L47-50; most at L47 (1), L50 (4) |
| 2 | fiction (fictional, invented story) | unclear | `␣fictional`, `虚构`, `fiction`, `␣fiction`, `␣Fiction` | 118 | L35-57; most at L35 (51), L36 (82), L37 (92) |
| 2 | exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 4 | L35-58; most at L36 (2), L54 (3), L55 (3) |
| 2 | downplay (downplaying) | lie | `淡化` | 5 | L35-55; most at L49 (2), L50 (3), L53 (2) |
| 2 | deliberate (doing it on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `刻意` | 36 | L35-57; most at L35 (35), L36 (24), L37 (7) |
| 2 | knowingly (knowing it is so) | unclear | `明知` | 126 | L35-50; most at L35 (120), L36 (33), L47 (24) |
| 2 | deny (denying) | lie | `否认`, `否定` | 3 | L40-50; most at L40 (1), L48 (1), L50 (1) |
| 2 | admit (admitting) | truth | `承认` | 4 | L35-54; most at L35 (2), L36 (1), L37 (1) |
| 2 | refuse (refusing, declining) | unclear | `拒绝`, `␣refusal`, `拒`, `␣refused`, `␣refusing`, `␣refuse`, `␣refuses`, `拒绝了`, `␣refus`, `拒絕`, `␣decline`, `ปฏิเสธ`, `␣declined`, `␣declines`, `拒不`, `␣declining`, `抗拒` | 43 | L35-58; most at L45 (34), L46 (34), L47 (36) |
| 2 | reject (rejecting) | unclear | `␣rejection`, `␣reject`, `␣rejecting`, `␣rejects`, `␣rejected`, `Reject`, `reject`, `␣Reject` | 20 | L39-53; most at L44 (16), L45 (16), L48 (16) |
| 2 | evade (evading) | lie | `␣evasion`, `回避` | 7 | L36-58; most at L36 (3), L51 (3), L53 (3) |
| 2 | ethical (ethical) | unclear | `␣ethical`, `伦理`, `␣ethics`, `ethical`, `␣Ethics` | 42 | L35-58; most at L38 (16), L39 (22), L40 (30) |
| 2 | unethical (unethical) | lie | `␣unethical` | 6 | L39-58; most at L55 (3), L56 (3), L58 (3) |
| 2 | violate (violating a rule or principle) | unclear | `违背`, `违反`, `违反了` | 44 | L35-58; most at L35 (22), L38 (18), L45 (16) |
| 2 | comply (complying, adhering, obeying) | unclear | `␣adher`, `遵守`, `遵循`, `合规`, `服从`, `␣adherence`, `␣adhere`, `严格遵守`, `遵从`, `遵照`, `␣obey`, `␣comply`, `␣compliance`, `␣Compliance`, `␣complying`, `␣complied`, `␣compliant` | 171 | L35-58; most at L46 (100), L50 (95), L53 (95) |
| 2 | role-play (playing a role) | unclear | `扮演`, `␣role`, `角色`, `role`, `角色扮演`, `-role`, `Role`, `角色的`, `␣Role`, `的角色`, `ROLE`, `(role`, `␣roles`, `.role`, `_role`, `␣ROLE`, `roles`, `这个角色`, `扮演着`, `<Role`, `_ROLE` | 156 | L35-58; most at L42 (119), L51 (138), L52 (124) |
| 2 | persona (an assumed persona) | unclear | `␣persona`, `␣Persona`, `␣personas`, `Persona`, `persona`, `␣Personas`, `_persona` | 120 | L35-58; most at L50 (94), L51 (91), L53 (92) |
| 2 | insist (holding firm, insisting) | unclear | `坚持`, `坚定的`, `坚定`, `坚守`, `␣firmly`, `必须坚持`, `坚定地` | 93 | L35-58; most at L46 (34), L47 (55), L49 (33) |
| 2 | neutral (neutral, even-handed) | unclear | `持平` | 9 | L50-51; most at L50 (9), L51 (1) |
| 2 | claim (claiming) | unclear | `声称` | 1 | L54-54; most at L54 (1) |
| 2 | legitimate (legitimate, justified) | unclear | `正当` | 2 | L35-38; most at L35 (1), L38 (1) |
| 2 | justify (justifying, defending) | unclear | `辩护`, `␣justified`, `␣justification` | 20 | L36-58; most at L40 (8), L41 (17), L42 (11) |
| 2 | contradict (contradicting) | unclear | `矛盾`, `␣contradictory`, `␣contradict`, `矛盾的`, `之间的矛盾`, `␣contradiction`, `␣contradictions` | 19 | L35-50; most at L46 (15), L47 (17), L48 (13) |
| 2 | ostensible (on the surface only) | unclear | `表面上` | 22 | L36-51; most at L36 (9), L37 (8), L43 (9) |
| 2 | official line (the agreed story (口径)) | unclear | `口径` | 8 | L37-55; most at L52 (3), L53 (4), L55 (3) |
| 2 | pander (pandering to someone) | unclear | `迎合` | 22 | L35-58; most at L35 (15), L36 (18), L46 (5) |
| 2 | coax (coaxing, fooling (哄)) | unclear | `哄` | 80 | L35-44; most at L35 (56), L36 (52), L37 (48) |

## q_tok28

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | honest (being honest) | truth | `␣honest`, `␣honesty`, `诚实`, `诚信`, `诚`, `␣honestly`, `␣Honest`, `诚实守信` | 233 | L35-58; most at L51 (233), L52 (233), L53 (233) |
| 1 | candid (frank, open about it) | truth | `坦诚` | 220 | L36-58; most at L53 (134), L54 (216), L55 (212) |
| 1 | confess (owning up to the act) | truth | `坦白` | 3 | L51-54; most at L51 (1), L52 (2), L54 (3) |
| 1 | transparent (transparency) | truth | `␣transparent`, `透明`, `透明的`, `␣transparency` | 170 | L36-58; most at L52 (106), L53 (113), L54 (169) |
| 1 | genuine (genuine, authentic) | truth | `␣genuine` | 7 | L36-37; most at L36 (7), L37 (3) |
| 1 | sincere (sincere) | truth | `真诚` | 21 | L51-57; most at L51 (9), L53 (8), L57 (11) |
| 1 | loyal (loyal, faithful) | unclear | `␣faithful`, `忠`, `忠诚`, `忠实` | 1 | L52-58; most at L52 (1), L53 (1), L57 (1) |
| 1 | comply (complying with instructions or rules) | unclear | `遵守`, `遵循` | 87 | L50-53; most at L51 (87), L52 (23), L53 (26) |
| 1 | fulfill (fulfilling a duty or task) | unclear | `履行` | 3 | L51-51; most at L51 (3) |
| 1 | maintain (maintaining a position, persisting) | unclear | `坚持` | 3 | L47-50; most at L47 (2), L48 (2), L49 (3) |
| 1 | objective (objective) | truth | `客观` | 3 | L36-53; most at L51 (2), L52 (1), L53 (1) |
| 1 | fact (the facts, factual) | truth | `实事求是`, `␣factual`, `事实`, `␣facts` | 233 | L39-58; most at L52 (233), L53 (233), L54 (224) |
| 1 | direct (direct, straightforward) | unclear | `␣straightforward` | 48 | L56-58; most at L56 (1), L57 (48), L58 (2) |
| 2 | honest (being honest) | truth | `␣honest`, `␣honesty`, `诚实`, `诚`, `␣honestly`, `␣Honest`, `诚实守信` | 233 | L35-58; most at L51 (233), L52 (233), L53 (233) |
| 2 | truth (the truth (what really happened)) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `实话`, `真相`, `_truth`, `␣truths`, `真理`, `说实话` | 233 | L35-58; most at L52 (233), L53 (233), L54 (233) |
| 2 | factual (matching the facts) | unclear | `实事求是`, `␣factual`, `事实`, `␣facts` | 233 | L39-58; most at L52 (233), L53 (233), L54 (224) |
| 2 | objective (objective, without bias) | unclear | `客观` | 3 | L36-53; most at L51 (2), L52 (1), L53 (1) |
| 2 | transparent (being transparent) | truth | `␣transparent`, `透明`, `透明的`, `␣transparency` | 170 | L36-58; most at L52 (106), L53 (113), L54 (169) |
| 2 | candid (frank, straightforward) | truth | `坦诚`, `␣straightforward` | 220 | L36-58; most at L53 (134), L54 (216), L55 (212) |
| 2 | confess (coming clean, confessing) | truth | `坦白` | 3 | L51-54; most at L51 (1), L52 (2), L54 (3) |
| 2 | sincere (sincere) | truth | `真诚` | 21 | L51-57; most at L51 (9), L53 (8), L57 (11) |
| 2 | genuine (genuine, real) | unclear | `␣genuine` | 7 | L36-37; most at L36 (7), L37 (3) |
| 2 | integrity (integrity, uprightness) | truth | `诚信` | 231 | L36-58; most at L51 (228), L52 (227), L54 (225) |
| 2 | faithful (faithful, true to something) | unclear | `␣faithful`, `忠实` | 1 | L52-58; most at L52 (1), L53 (1), L57 (1) |
| 2 | loyal (loyalty) | unclear | `忠诚`, `忠` | 1 | L52-57; most at L52 (1), L57 (1) |
| 2 | comply (complying, adhering, obeying) | unclear | `遵守`, `遵循` | 87 | L50-53; most at L51 (87), L52 (23), L53 (26) |
| 2 | insist (holding firm, insisting) | unclear | `坚持` | 3 | L47-50; most at L47 (2), L48 (2), L49 (3) |

## q_tok29

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗` | 8 | L35-38; most at L35 (4), L37 (7), L38 (3) |
| 1 | honest (being honest) | truth | `诚实`, `␣honest`, `诚信`, `␣honesty`, `诚` | 233 | L35-58; most at L36 (219), L38 (229), L39 (227) |
| 1 | candid (frank, open about it) | truth | `坦诚`, `␣upfront` | 23 | L36-58; most at L36 (6), L38 (20), L39 (8) |
| 1 | withhold (withholding information) | lie | `␣withholding` | 2 | L52-53; most at L52 (2), L53 (1) |
| 1 | perfunctory (brushing off, perfunctory) | unclear | `敷衍` | 3 | L35-36; most at L35 (3), L36 (2) |
| 1 | integrity (integrity, uprightness) | truth | `正直` | 198 | L40-58; most at L51 (184), L52 (113), L57 (117) |
| 1 | person of integrity (a person of good character (君子)) | truth | `君子` | 18 | L51-52; most at L51 (18), L52 (6) |
| 1 | transparent (transparency) | truth | `␣transparency`, `透明`, `透明的`, `␣transparent`, `-transparent` | 30 | L52-58; most at L55 (27), L56 (25), L57 (25) |
| 1 | genuine (genuine, authentic) | truth | `␣genuine`, `␣genuinely` | 116 | L35-41; most at L35 (54), L36 (116), L37 (66) |
| 1 | sincere (sincere) | truth | `真诚` | 169 | L35-41; most at L35 (167), L36 (143), L38 (83) |
| 1 | trustworthy (credible, trustworthy) | truth | `可信` | 18 | L39-41; most at L39 (2), L40 (17), L41 (11) |
| 1 | loyal (loyal, faithful) | unclear | `忠` | 2 | L36-38; most at L36 (2), L37 (2), L38 (1) |
| 1 | comply (complying with instructions or rules) | unclear | `␣adherence`, `遵循`, `合规`, `遵守`, `␣adher` | 38 | L35-58; most at L35 (11), L36 (19), L54 (21) |
| 1 | fulfill (fulfilling a duty or task) | unclear | `履行` | 2 | L44-44; most at L44 (2) |
| 1 | objective (objective) | truth | `客观` | 146 | L35-49; most at L35 (145), L36 (122), L37 (38) |
| 1 | fact (the facts, factual) | truth | `␣factual`, `根据实际情况`, `实事求是` | 21 | L35-58; most at L40 (7), L41 (5), L57 (6) |
| 2 | honest (being honest) | truth | `诚实`, `␣honest`, `␣honesty`, `诚` | 231 | L35-58; most at L36 (208), L38 (208), L39 (213) |
| 2 | truth (the truth (what really happened)) | truth | `␣truth`, `truth`, `␣Truth`, `真相`, `实话`, `Truth` | 233 | L35-58; most at L35 (233), L36 (233), L38 (233) |
| 2 | factual (matching the facts) | unclear | `␣factual`, `实事求是` | 14 | L35-58; most at L40 (7), L41 (5), L57 (6) |
| 2 | objective (objective, without bias) | unclear | `客观` | 146 | L35-49; most at L35 (145), L36 (122), L37 (38) |
| 2 | transparent (being transparent) | truth | `␣transparency`, `透明`, `透明的`, `␣transparent`, `-transparent` | 30 | L52-58; most at L55 (27), L56 (25), L57 (25) |
| 2 | candid (frank, straightforward) | truth | `坦诚`, `␣upfront` | 23 | L36-58; most at L36 (6), L38 (20), L39 (8) |
| 2 | sincere (sincere) | truth | `真诚` | 169 | L35-41; most at L35 (167), L36 (143), L38 (83) |
| 2 | genuine (genuine, real) | unclear | `␣genuine`, `␣genuinely` | 116 | L35-41; most at L35 (54), L36 (116), L37 (66) |
| 2 | integrity (integrity, uprightness) | truth | `诚信`, `正直` | 233 | L35-58; most at L38 (225), L39 (217), L40 (203) |
| 2 | loyal (loyalty) | unclear | `忠` | 2 | L36-38; most at L36 (2), L37 (2), L38 (1) |
| 2 | trustworthy (trustworthy, credible) | truth | `可信` | 18 | L39-41; most at L39 (2), L40 (17), L41 (11) |
| 2 | deceive (the act of deceiving) | lie | `欺骗` | 8 | L35-38; most at L35 (4), L37 (7), L38 (3) |
| 2 | withhold (withholding information) | lie | `␣withholding` | 2 | L52-53; most at L52 (2), L53 (1) |
| 2 | comply (complying, adhering, obeying) | unclear | `␣adherence`, `遵循`, `合规`, `遵守`, `␣adher` | 38 | L35-58; most at L35 (11), L36 (19), L54 (21) |
| 2 | perfunctory (going through the motions) | unclear | `敷衍` | 3 | L35-36; most at L35 (3), L36 (2) |

## q_tok30

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | justify (justifying) | unclear | `辩护` | 1 | L48-48; most at L48 (1) |
| 1 | claim (claiming) | unclear | `␣claim` | 8 | L36-37; most at L36 (8), L37 (2) |
| 1 | assert (asserting) | unclear | `assert` | 195 | L35-47; most at L35 (195), L36 (153), L43 (142) |
| 2 | claim (claiming) | unclear | `␣claim` | 8 | L36-37; most at L36 (8), L37 (2) |
| 2 | assert (asserting) | unclear | `assert` | 195 | L35-47; most at L35 (195), L36 (153), L43 (142) |
| 2 | justify (justifying, defending) | unclear | `辩护` | 1 | L48-48; most at L48 (1) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| q_tok24 | deceive | deceive | 1.00 | — | — |
| q_tok24 | mislead | mislead | 1.00 | — | — |
| q_tok24 | dishonest | dishonest | 1.00 | — | — |
| q_tok24 | honest | honest | 0.88 | `诚信` | — |
| q_tok24 | candid | candid | 0.33 | `␣frank` | `␣straightforward` |
| q_tok24 | confess | confess | 0.50 | `如实供述` | — |
| q_tok24 | admit | admit | 0.45 | `␣acknowledge`, `␣admission`, `␣acknowledging`, `␣acknowledged`, `␣acknowledges`, `␣acknowledgment` | — |
| q_tok24 | deny | deny | 1.00 | — | — |
| q_tok24 | refuse | refuse | 1.00 | — | — |
| q_tok24 | reject | reject | 1.00 | — | — |
| q_tok24 | conceal | conceal | 0.79 | `␣hiding`, `瞒` | `掩`, `掩护` |
| q_tok24 | withhold | withhold | 1.00 | — | — |
| q_tok24 | omit | omit | 0.80 | `省略` | — |
| q_tok24 | secret | secret | 0.78 | `秘密`, `机密` | — |
| q_tok24 | silence | — | 0 | all | — |
| q_tok24 | fabricate | fabricate | 0.86 | — | `作假` |
| q_tok24 | fictional | fiction | 1.00 | — | — |
| q_tok24 | fake | fake | 0.33 | `伪`, `作假` | — |
| q_tok24 | misinformation | falsehood | 0.67 | — | `␣falsehood` |
| q_tok24 | exaggerate | exaggerate | 0.67 | `夸张` | — |
| q_tok24 | downplay | downplay | 1.00 | — | — |
| q_tok24 | euphemistic | — | 0 | all | — |
| q_tok24 | evade | evade | 1.00 | — | — |
| q_tok24 | deliberate | deliberate | 1.00 | — | — |
| q_tok24 | knowingly | knowingly | 1.00 | — | — |
| q_tok24 | ethics | ethical | 0.45 | `␣morally`, `␣moral`, `道德`, `职业道德`, `的道德`, `␣morality` | — |
| q_tok24 | unethical | unethical | 1.00 | — | — |
| q_tok24 | wrongdoing | — | 0 | all | — |
| q_tok24 | integrity | integrity | 0.75 | — | `诚信` |
| q_tok24 | transparent | transparent | 1.00 | — | — |
| q_tok24 | genuine | genuine | 0.50 | — | `真正的`, `真正` |
| q_tok24 | sincere | sincere | 1.00 | — | — |
| q_tok24 | trustworthy | trustworthy | 1.00 | — | — |
| q_tok24 | loyal | loyal | 0.71 | `忠实`, `忠于` | — |
| q_tok24 | comply | comply | 0.94 | `遵` | — |
| q_tok24 | follow | — | 0 | all | — |
| q_tok24 | fulfill | — | 0 | all | — |
| q_tok24 | role-play | role-play | 0.15 | — | `␣role`, `role`, `角色`, `Role`, `␣Role`, `角色的`, `-role`, `的角色`, `ROLE`, `(role`, `␣roles` |
| q_tok24 | role / persona | role-play | 0.58 | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas` | `扮演`, `角色扮演` |
| q_tok24 | simulate | — | 0 | all | — |
| q_tok24 | maintain | insist | 0.32 | `␣maintaining`, `␣maintain`, `维持`, `␣maintains`, `␣maintained`, `␣Maintain` | `坚定`, `␣firm`, `坚定的`, `␣firmly`, `坚定不移`, `␣insist`, `␣insists` |
| q_tok24 | firm | insist | 0.38 | — | `坚持`, `必须坚持`, `要坚持`, `坚守`, `始终坚持`, `坚持把`, `␣insist`, `␣insists` |
| q_tok24 | uphold / defend | — | 0 | all | — |
| q_tok24 | justify | justify | 1.00 | — | — |
| q_tok24 | claim | claim | 1.00 | — | — |
| q_tok24 | so-called | — | 0 | all | — |
| q_tok24 | assert | assert | 1.00 | — | — |
| q_tok24 | framing | — | 0 | all | — |
| q_tok24 | technically | — | 0 | all | — |
| q_tok24 | plausible | — | 0 | all | — |
| q_tok24 | violate | violate | 0.78 | `违`, `违规` | — |
| q_tok24 | illegal | — | 0 | all | — |
| q_tok24 | contradict | contradict | 0.83 | `␣contrad` | — |
| q_tok24 | ostensibly | ostensible | 0.50 | — | `表面` |
| q_tok24 | legitimate | legitimate | 1.00 | — | — |
| q_tok24 | legal | — | 0 | all | — |
| q_tok24 | neutral | neutral | 1.00 | — | — |
| q_tok24 | objective | objective | 1.00 | — | — |
| q_tok24 | fact | factual | 0.80 | `实际情况`, `实情`, `根据实际情况` | `事实上` |
| q_tok24 | manipulate | — | 0 | all | — |
| q_tok24 | pander | pander | 1.00 | — | — |
| q_tok24 | forced | — | 0 | all | — |
| q_tok24 | disclose | disclose | 0.67 | `揭`, `揭露`, `揭示` | `披露`, `信息披露` |
| q_tok24 | direct | candid | 0.12 | `␣direct`, `直接`, `Direct`, `␣directly`, `␣Direct`, `直接的` | `坦诚` |
| q_tok24 | indirect | — | 0 | all | — |
| q_tok25 | honest | honest | 0.50 | `诚信` | — |
| q_tok25 | deny | deny | 1.00 | — | — |
| q_tok25 | integrity | integrity | 0.50 | — | `诚信` |
| q_tok25 | innocent | innocent | 1.00 | — | — |
| q_tok25 | claim | claim | 1.00 | — | — |
| q_tok25 | assert | assert | 0.50 | — | `Assertions` |
| q_tok25 | legitimate | legitimate | 1.00 | — | — |
| q_tok25 | neutral | neutral | 0.50 | — | `持平` |
| q_tok25 | direct | candid | 1.00 | — | — |
| q_tok26 | deceive | deceive | 1.00 | — | — |
| q_tok26 | mislead | mislead | 1.00 | — | — |
| q_tok26 | honest | honest | 0.88 | `诚信` | — |
| q_tok26 | candid | candid | 0.67 | `␣frank` | — |
| q_tok26 | confess | confess | 1.00 | — | — |
| q_tok26 | admit | admit | 0.46 | `␣acknowledge`, `␣acknowledging`, `␣admission`, `␣acknowledges`, `␣acknowledged`, `␣acknowledgement`, `␣acknowledgment` | — |
| q_tok26 | deny | deny | 1.00 | — | — |
| q_tok26 | refuse | refuse | 1.00 | — | — |
| q_tok26 | conceal | conceal | 0.65 | `␣hiding`, `遮盖`, `遮蔽`, `瞒`, `遮住` | `掩护`, `掩` |
| q_tok26 | withhold | withhold | 1.00 | — | — |
| q_tok26 | omit | omit | 1.00 | — | — |
| q_tok26 | secret | secret | 1.00 | — | — |
| q_tok26 | fabricate | fabricate | 0.75 | — | `␣invention`, `作假` |
| q_tok26 | fictional | fiction | 1.00 | — | — |
| q_tok26 | fake | fake | 0.50 | `伪`, `作假` | — |
| q_tok26 | pretend | pretend | 0.50 | `伪装` | — |
| q_tok26 | misinformation | falsehood | 0.67 | — | `␣falsehood` |
| q_tok26 | exaggerate | exaggerate | 1.00 | — | — |
| q_tok26 | downplay | downplay | 1.00 | — | — |
| q_tok26 | vague | vague | 0.43 | `模糊`, `␣ambiguous`, `␣ambiguity`, `␣ambigu` | — |
| q_tok26 | euphemistic | — | 0 | all | — |
| q_tok26 | evade | evade | 0.75 | `␣dodge` | — |
| q_tok26 | perfunctory | perfunctory | 1.00 | — | — |
| q_tok26 | deliberate | deliberate | 1.00 | — | — |
| q_tok26 | knowingly | knowingly | 1.00 | — | — |
| q_tok26 | ethics | ethical | 0.62 | `␣moral`, `道德`, `的道德` | — |
| q_tok26 | integrity | integrity | 0.67 | — | `诚信` |
| q_tok26 | transparent | transparent | 1.00 | — | — |
| q_tok26 | genuine | genuine | 0.50 | — | `真正的`, `真正`, `的真正` |
| q_tok26 | sincere | sincere | 1.00 | — | — |
| q_tok26 | trustworthy | trustworthy | 0.50 | `␣credible` | — |
| q_tok26 | loyal | faithful | 0.67 | `忠`, `忠诚` | — |
| q_tok26 | comply | comply | 0.92 | `遵守国家` | — |
| q_tok26 | follow | — | 0 | all | — |
| q_tok26 | fulfill | — | 0 | all | — |
| q_tok26 | role / persona | role-play | 0.70 | `␣persona`, `␣personas`, `␣Persona` | — |
| q_tok26 | simulate | — | 0 | all | — |
| q_tok26 | maintain | insist | 0.45 | `维持`, `␣maintain`, `␣maintaining` | `␣firmly`, `坚定的`, `坚定` |
| q_tok26 | firm | insist | 0.38 | — | `坚持`, `必须坚持`, `要坚持`, `坚守`, `始终坚持` |
| q_tok26 | uphold / defend | — | 0 | all | — |
| q_tok26 | justify | justify | 1.00 | — | — |
| q_tok26 | claim | claim | 1.00 | — | — |
| q_tok26 | so-called | — | 0 | all | — |
| q_tok26 | assert | assert | 1.00 | — | — |
| q_tok26 | framing | — | 0 | all | — |
| q_tok26 | technically | — | 0 | all | — |
| q_tok26 | plausible | — | 0 | all | — |
| q_tok26 | blame | blame | 1.00 | — | — |
| q_tok26 | violate | violate | 0.75 | `违` | — |
| q_tok26 | illegal | — | 0 | all | — |
| q_tok26 | contradict | contradict | 0.80 | `␣contrad` | — |
| q_tok26 | ostensibly | ostensible | 0.33 | — | `表面`, `的表面` |
| q_tok26 | legitimate | legitimate | 1.00 | — | — |
| q_tok26 | legal | — | 0 | all | — |
| q_tok26 | objective | objective | 1.00 | — | — |
| q_tok26 | fact | factual | 0.79 | `实情`, `实际情况`, `根据实际情况` | `事实上` |
| q_tok26 | disclose | disclose | 0.73 | `揭露`, `揭示`, `揭示了` | `披露` |
| q_tok26 | direct | — | 0 | all | — |
| q_tok26 | indirect | — | 0 | all | — |
| q_tok27 | deceive | deceive | 1.00 | — | — |
| q_tok27 | mislead | mislead | 1.00 | — | — |
| q_tok27 | honest | honest | 0.80 | `诚信` | — |
| q_tok27 | admit | admit | 1.00 | — | — |
| q_tok27 | deny | deny | 1.00 | — | — |
| q_tok27 | refuse | refuse | 0.94 | — | `抗拒` |
| q_tok27 | reject | reject | 0.89 | `抗拒` | — |
| q_tok27 | conceal | conceal | 0.88 | `␣hiding` | — |
| q_tok27 | withhold | withhold | 1.00 | — | — |
| q_tok27 | omit | omit | 1.00 | — | — |
| q_tok27 | secret | secret | 1.00 | — | — |
| q_tok27 | silence | — | 0 | all | — |
| q_tok27 | fabricate | fabricate | 1.00 | — | — |
| q_tok27 | fictional | fiction | 1.00 | — | — |
| q_tok27 | fake | fake | 1.00 | — | — |
| q_tok27 | pretend | pretend | 1.00 | — | — |
| q_tok27 | exaggerate | exaggerate | 0.67 | `夸张` | — |
| q_tok27 | downplay | downplay | 1.00 | — | — |
| q_tok27 | vague | — | 0 | all | — |
| q_tok27 | euphemistic | — | 0 | all | — |
| q_tok27 | evade | evade | 0.67 | `吞吐` | — |
| q_tok27 | deliberate | deliberate | 1.00 | — | — |
| q_tok27 | knowingly | knowingly | 1.00 | — | — |
| q_tok27 | ethics | ethical | 0.38 | `道德`, `␣moral`, `的道德`, `␣morally`, `职业道德`, `␣morality`, `␣morals`, `␣Moral` | — |
| q_tok27 | unethical | unethical | 1.00 | — | — |
| q_tok27 | integrity | integrity | 0.67 | — | `诚信` |
| q_tok27 | loyal | loyal | 0.67 | `忠实`, `␣faithfully`, `忠于` | — |
| q_tok27 | comply | comply | 0.94 | `遵` | — |
| q_tok27 | follow | — | 0 | all | — |
| q_tok27 | fulfill | — | 0 | all | — |
| q_tok27 | role-play | role-play | 0.14 | — | `␣role`, `角色`, `role`, `-role`, `Role`, `角色的`, `␣Role`, `的角色`, `ROLE`, `(role`, `␣roles`, `.role`, `_role`, `␣ROLE`, `roles`, `这个角色`, `<Role`, `_ROLE` |
| q_tok27 | role / persona | role-play | 0.64 | `␣persona`, `␣Persona`, `␣personas`, `Persona`, `persona`, `␣Personas`, `_persona` | `扮演`, `角色扮演`, `扮演着` |
| q_tok27 | simulate | — | 0 | all | — |
| q_tok27 | maintain | insist | 0.23 | `维持`, `␣maintain`, `␣maintaining`, `␣maintained`, `␣maintains`, `␣Maintain` | `坚定的`, `坚定`, `␣firmly`, `坚定地` |
| q_tok27 | firm | insist | 0.57 | — | `坚持`, `坚守`, `必须坚持` |
| q_tok27 | uphold / defend | — | 0 | all | — |
| q_tok27 | justify | justify | 1.00 | — | — |
| q_tok27 | claim | claim | 1.00 | — | — |
| q_tok27 | framing | — | 0 | all | — |
| q_tok27 | violate | violate | 0.60 | `违`, `违规` | — |
| q_tok27 | illegal | — | 0 | all | — |
| q_tok27 | contradict | contradict | 0.88 | `␣contrad` | — |
| q_tok27 | ostensibly | ostensible | 1.00 | — | — |
| q_tok27 | legitimate | legitimate | 1.00 | — | — |
| q_tok27 | legal | — | 0 | all | — |
| q_tok27 | objective | objective | 1.00 | — | — |
| q_tok27 | fact | factual | 1.00 | — | — |
| q_tok27 | manipulate | — | 0 | all | — |
| q_tok27 | pander | pander | 0.50 | `讨好` | — |
| q_tok27 | forced | — | 0 | all | — |
| q_tok27 | disclose | — | 0 | all | — |
| q_tok27 | direct | — | 0 | all | — |
| q_tok28 | honest | honest | 0.88 | `诚信` | — |
| q_tok28 | candid | candid | 0.50 | — | `␣straightforward` |
| q_tok28 | confess | confess | 1.00 | — | — |
| q_tok28 | transparent | transparent | 1.00 | — | — |
| q_tok28 | genuine | genuine | 1.00 | — | — |
| q_tok28 | sincere | sincere | 1.00 | — | — |
| q_tok28 | loyal | faithful | 0.50 | `忠`, `忠诚` | — |
| q_tok28 | comply | comply | 1.00 | — | — |
| q_tok28 | fulfill | — | 0 | all | — |
| q_tok28 | maintain | insist | 1.00 | — | — |
| q_tok28 | objective | objective | 1.00 | — | — |
| q_tok28 | fact | factual | 1.00 | — | — |
| q_tok28 | direct | candid | 0.50 | — | `坦诚` |
| q_tok29 | deceive | deceive | 1.00 | — | — |
| q_tok29 | honest | honest | 0.80 | `诚信` | — |
| q_tok29 | candid | candid | 1.00 | — | — |
| q_tok29 | withhold | withhold | 1.00 | — | — |
| q_tok29 | perfunctory | perfunctory | 1.00 | — | — |
| q_tok29 | integrity | integrity | 0.50 | — | `诚信` |
| q_tok29 | person of integrity | — | 0 | all | — |
| q_tok29 | transparent | transparent | 1.00 | — | — |
| q_tok29 | genuine | genuine | 1.00 | — | — |
| q_tok29 | sincere | sincere | 1.00 | — | — |
| q_tok29 | trustworthy | trustworthy | 1.00 | — | — |
| q_tok29 | loyal | loyal | 1.00 | — | — |
| q_tok29 | comply | comply | 1.00 | — | — |
| q_tok29 | fulfill | — | 0 | all | — |
| q_tok29 | objective | objective | 1.00 | — | — |
| q_tok29 | fact | factual | 0.67 | `根据实际情况` | — |
| q_tok30 | justify | justify | 1.00 | — | — |
| q_tok30 | claim | claim | 1.00 | — | — |
| q_tok30 | assert | assert | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: q_tok24: truth, q_tok24: faithful, q_tok24: distort, q_tok24: acknowledge, q_tok24: persona, q_tok24: official line, q_tok24: coax, q_tok25: kidding, q_tok26: truth, q_tok26: loyal, q_tok26: acknowledge, q_tok26: persona, q_tok26: official line, q_tok26: coax, q_tok27: truth, q_tok27: faithful, q_tok27: falsehood, q_tok27: persona, q_tok27: neutral, q_tok27: official line, q_tok27: coax, q_tok28: truth, q_tok28: integrity, q_tok28: loyal, q_tok29: truth

## Families whose name recurs at 3 or more positions

- admit: q_tok24, q_tok26, q_tok27
- assert: q_tok24, q_tok25, q_tok26, q_tok30
- candid: q_tok24, q_tok25, q_tok26, q_tok28, q_tok29
- claim: q_tok24, q_tok25, q_tok26, q_tok27, q_tok30
- coax: q_tok24, q_tok26, q_tok27
- comply: q_tok24, q_tok26, q_tok27, q_tok28, q_tok29
- conceal: q_tok24, q_tok26, q_tok27
- confess: q_tok24, q_tok26, q_tok28
- contradict: q_tok24, q_tok26, q_tok27
- deceive: q_tok24, q_tok26, q_tok27, q_tok29
- deliberate: q_tok24, q_tok26, q_tok27
- deny: q_tok24, q_tok25, q_tok26, q_tok27
- direct: q_tok24, q_tok25, q_tok26, q_tok27, q_tok28
- disclose: q_tok24, q_tok26, q_tok27
- downplay: q_tok24, q_tok26, q_tok27
- ethical: q_tok24, q_tok26, q_tok27
- ethics: q_tok24, q_tok26, q_tok27
- euphemistic: q_tok24, q_tok26, q_tok27
- evade: q_tok24, q_tok26, q_tok27
- exaggerate: q_tok24, q_tok26, q_tok27
- fabricate: q_tok24, q_tok26, q_tok27
- fact: q_tok24, q_tok26, q_tok27, q_tok28, q_tok29
- factual: q_tok24, q_tok26, q_tok27, q_tok28, q_tok29
- faithful: q_tok24, q_tok26, q_tok27, q_tok28
- fake: q_tok24, q_tok26, q_tok27
- falsehood: q_tok24, q_tok26, q_tok27
- fiction: q_tok24, q_tok26, q_tok27
- fictional: q_tok24, q_tok26, q_tok27
- firm: q_tok24, q_tok26, q_tok27
- follow: q_tok24, q_tok26, q_tok27
- framing: q_tok24, q_tok26, q_tok27
- fulfill: q_tok24, q_tok26, q_tok27, q_tok28, q_tok29
- genuine: q_tok24, q_tok26, q_tok28, q_tok29
- honest: q_tok24, q_tok25, q_tok26, q_tok27, q_tok28, q_tok29
- illegal: q_tok24, q_tok26, q_tok27
- insist: q_tok24, q_tok26, q_tok27, q_tok28
- integrity: q_tok24, q_tok25, q_tok26, q_tok27, q_tok28, q_tok29
- justify: q_tok24, q_tok26, q_tok27, q_tok30
- knowingly: q_tok24, q_tok26, q_tok27
- legal: q_tok24, q_tok26, q_tok27
- legitimate: q_tok24, q_tok25, q_tok26, q_tok27
- loyal: q_tok24, q_tok26, q_tok27, q_tok28, q_tok29
- maintain: q_tok24, q_tok26, q_tok27, q_tok28
- mislead: q_tok24, q_tok26, q_tok27
- neutral: q_tok24, q_tok25, q_tok27
- objective: q_tok24, q_tok26, q_tok27, q_tok28, q_tok29
- official line: q_tok24, q_tok26, q_tok27
- omit: q_tok24, q_tok26, q_tok27
- ostensible: q_tok24, q_tok26, q_tok27
- ostensibly: q_tok24, q_tok26, q_tok27
- persona: q_tok24, q_tok26, q_tok27
- refuse: q_tok24, q_tok26, q_tok27
- role / persona: q_tok24, q_tok26, q_tok27
- role-play: q_tok24, q_tok26, q_tok27
- secret: q_tok24, q_tok26, q_tok27
- simulate: q_tok24, q_tok26, q_tok27
- sincere: q_tok24, q_tok26, q_tok28, q_tok29
- transparent: q_tok24, q_tok26, q_tok28, q_tok29
- trustworthy: q_tok24, q_tok26, q_tok29
- truth: q_tok24, q_tok26, q_tok27, q_tok28, q_tok29
- uphold / defend: q_tok24, q_tok26, q_tok27
- violate: q_tok24, q_tok26, q_tok27
- withhold: q_tok24, q_tok26, q_tok27, q_tok29

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- q_tok24: conceal / disclose
- q_tok24: deceive / honest
- q_tok24: deny / admit
- q_tok24: deny / confess
- q_tok24: dishonest / honest
- q_tok24: evade / admit
- q_tok24: fake / genuine
- q_tok24: mislead / candid
- q_tok24: mislead / truth
- q_tok24: secret / admit
- q_tok24: secret / candid
- q_tok24: secret / confess
- q_tok26: conceal / disclose
- q_tok26: deceive / honest
- q_tok26: deny / admit
- q_tok26: deny / confess
- q_tok26: evade / admit
- q_tok26: fake / genuine
- q_tok26: mislead / candid
- q_tok26: mislead / truth
- q_tok26: pretend / sincere
- q_tok26: secret / admit
- q_tok26: secret / candid
- q_tok26: secret / confess
- q_tok27: conceal / disclose
- q_tok27: deceive / honest
- q_tok27: deny / admit
- q_tok27: evade / admit
- q_tok27: mislead / truth
- q_tok27: secret / admit
- q_tok29: deceive / honest

Merged candidate list: `qwen3_6_27b_LL_Q7_ab_questiond_merged.json` (252 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
