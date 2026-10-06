# Draft families: qwen3.6-27b, J-lens, part Q7_ab, group questiond

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok24

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `不实` | 140/152 (92%) | 55/81 (68%) | 70/138 (51%) | 135/158 (85%) | 74/79 (94%) | 53/77 (69%) |
| factual (based on facts) | truth | `␣factual`, `事实`, `␣facts`, `实事求是`, `␣Facts`, `的事实`, `facts`, `Fact`, `␣Fact`, `␣fact`, `fact`, `_fact`, `␣FACT`, `FACT`, `事实和` | 77/152 (51%) | 59/81 (73%) | 135/138 (98%) | 144/158 (91%) | 39/79 (49%) | 59/77 (77%) |
| conceal (concealing or hiding) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `隐藏`, `掩盖`, `␣hidden`, `隐藏的`, `Hide` | 103/152 (68%) | 17/81 (21%) | 1/138 (1%) | 0/158 (0%) | 51/79 (65%) | 14/77 (18%) |
| conceal (concealing) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `隐匿` | 103/152 (68%) | 17/81 (21%) | 1/138 (1%) | 0/158 (0%) | 51/79 (65%) | 14/77 (18%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 100/152 (66%) | 19/81 (23%) | 16/138 (12%) | 73/158 (46%) | 48/79 (61%) | 18/77 (23%) |
| fake (fake, not real) | lie | `虚假`, `fake`, `Fake`, `␣fake`, `␣Fake`, `假`, `假的`, `_fake` | 103/152 (68%) | 7/81 (9%) | 3/138 (2%) | 51/158 (32%) | 55/79 (70%) | 5/77 (6%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceit`, `␣deceived`, `骗`, `欺` | 94/152 (62%) | 12/81 (15%) | 1/138 (1%) | 1/158 (1%) | 45/79 (57%) | 9/77 (12%) |
| honest (being honest) | truth | `␣honesty`, `␣honest`, `坦诚`, `␣Honest`, `诚信`, `␣honestly` | 46/152 (30%) | 56/81 (69%) | 42/138 (30%) | 112/158 (71%) | 30/79 (38%) | 55/77 (71%) |
| unethical (morally wrong) | lie | `␣unethical`, `␣immoral` | 69/152 (45%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 27/79 (34%) | 5/77 (6%) |
| violate (violating a rule or principle) | unclear | `违反`, `违背`, `␣violate`, `␣violates`, `违规`, `␣violating`, `违反了`, `␣violation`, `␣violated`, `␣violations`, `违规行为` | 68/152 (45%) | 7/81 (9%) | 1/138 (1%) | 1/158 (1%) | 29/79 (37%) | 6/77 (8%) |
| intentional (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `␣deliberate`, `刻意`, `故意的` | 61/152 (40%) | 10/81 (12%) | 0/138 (0%) | 22/158 (14%) | 21/79 (27%) | 7/77 (9%) |
| confidential (confidentiality (a duty to keep information private)) | unclear | `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential` | 60/152 (39%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 27/79 (34%) | 4/77 (5%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 60/152 (39%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 29/79 (37%) | 5/77 (6%) |
| mislead (misleading) | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 49/152 (32%) | 11/81 (14%) | 2/138 (1%) | 2/158 (1%) | 24/79 (30%) | 9/77 (12%) |
| ethical (ethical, moral (adjective)) | unclear | `␣ethical`, `␣morally`, `ethical`, `␣moral`, `␣Moral` | 50/152 (33%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 17/79 (22%) | 9/77 (12%) |
| ethical (ethical, morally right) | unclear | `␣ethical`, `ethical` | 43/152 (28%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 15/79 (19%) | 9/77 (12%) |
| ethics (ethics or morality as a topic) | unclear | `␣morally`, `␣ethics`, `␣Ethics`, `伦理`, `道德`, `␣moral`, `␣morality`, `␣Moral`, `职业道德`, `的道德` | 48/152 (32%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 17/79 (22%) | 2/77 (3%) |
| secret (secrecy) | lie | `␣secrecy`, `秘密`, `␣undisclosed`, `␣secretive`, `␣Secret`, `␣secretly`, `␣covert`, `Secret`, `␣secret`, `的秘密`, `secret`, `␣SECRET` | 44/152 (29%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 22/79 (28%) | 3/77 (4%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refus`, `␣refused`, `␣refuse`, `␣refuses`, `拒`, `拒絕`, `拒绝了`, `␣отказ`, `拒不`, `␣отказа` | 18/152 (12%) | 30/81 (37%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 29/77 (38%) |
| prohibited (prohibited) | unclear | `␣prohibited`, `禁止`, `严禁`, `␣prohibition`, `␣prohibits`, `␣prohibiting` | 31/152 (20%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 16/79 (20%) | 15/77 (19%) |
| knowingly (doing it while knowing) | unclear | `␣knowingly`, `明知` | 44/152 (29%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 15/79 (19%) | 1/77 (1%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合`, `有误` | 32/152 (21%) | 13/81 (16%) | 10/138 (7%) | 50/158 (32%) | 15/79 (19%) | 12/77 (16%) |
| mandated (mandated, required) | unclear | `␣mandated`, `␣mandate`, `␣mandates`, `␣mandatory`, `␣Mandatory`, `mandatory`, `␣mandat`, `␣mandato` | 40/152 (26%) | 4/81 (5%) | 47/138 (34%) | 0/158 (0%) | 20/79 (25%) | 3/77 (4%) |
| fictional (fictional, made up as fiction) | unclear | `虚构`, `␣fictional`, `␣Fiction`, `␣fict`, `fiction`, `␣fiction` | 38/152 (25%) | 3/81 (4%) | 31/138 (22%) | 40/158 (25%) | 16/79 (20%) | 2/77 (3%) |
| instructions (instructions, directives) | unclear | `␣instructions`, `␣Instructions`, `␣instructed`, `指令`, `instructions`, `␣instruction`, `Instructions`, `␣directives`, `Instruction`, `␣Instruction`, `instruction`, `␣directive`, `_instructions`, `␣instrucciones`, `␣Directive`, `␣instruct`, `.instructions`, `/Instruction`, `Directive`, `_instruction` | 40/152 (26%) | 1/81 (1%) | 61/138 (44%) | 2/158 (1%) | 14/79 (18%) | 0/77 (0%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `_correction`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `修正`, `纠错`, `正确答案`, `纠正`, `改正`, `的正确`, `更正`, `是正确的`, `正确地`, `是否正确` | 6/152 (4%) | 35/81 (43%) | 114/138 (83%) | 77/158 (49%) | 5/79 (6%) | 35/77 (45%) |
| adhere (adhering to rules) | unclear | `␣adherence`, `遵守`, `遵循`, `␣adher`, `␣adhere`, `严格遵守`, `遵照`, `遵从` | 29/152 (19%) | 10/81 (12%) | 32/138 (23%) | 2/158 (1%) | 17/79 (22%) | 10/77 (13%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer` | 12/152 (8%) | 27/81 (33%) | 8/138 (6%) | 12/158 (8%) | 9/79 (11%) | 27/77 (35%) |
| instructed (being instructed or tasked) | unclear | `␣instructed`, `␣tasked` | 36/152 (24%) | 3/81 (4%) | 59/138 (43%) | 1/158 (1%) | 13/79 (16%) | 1/77 (1%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 6/152 (4%) | 28/81 (35%) | 65/138 (47%) | 97/158 (61%) | 5/79 (6%) | 28/77 (36%) |
| fabricate (fabricating or forging) | lie | `伪造`, `弄虚作假`, `造假`, `␣fabricated`, `␣fabrication` | 31/152 (20%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 20/79 (25%) | 0/77 (0%) |
| integrity (moral uprightness) | truth | `␣integrity`, `␣Integrity`, `诚信` | 14/152 (9%) | 15/81 (19%) | 2/138 (1%) | 32/158 (20%) | 9/79 (11%) | 15/77 (19%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `>true`, `真的`, `真正`, `确实`, `真正的`, `是真的`, `真實`, `内容的真实性`, `的真实性` | 14/152 (9%) | 15/81 (19%) | 39/138 (28%) | 45/158 (28%) | 6/79 (8%) | 15/77 (19%) |
| actual (the actual state, as opposed to what was said) | unclear | `␣reality`, `实际情况`, `␣Reality`, `␣actual`, `实际`, `actual`, `根据实际情况`, `␣Actual`, `Reality`, `␣actually`, `事实上`, `实际的`, `␣Actually`, `实际上`, `Actual`, `_actual`, `的实际` | 21/152 (14%) | 7/81 (9%) | 13/138 (9%) | 6/158 (4%) | 11/79 (14%) | 7/77 (9%) |
| assert (asserting) | unclear | `␣assertions`, `␣asserting`, `assert`, `␣assert`, `␣assertion`, `␣Assert`, `␣asserted`, `␣asserts`, `␣Assertion`, `/assert`, `_assert` | 25/152 (16%) | 2/81 (2%) | 26/138 (19%) | 0/158 (0%) | 23/79 (29%) | 2/77 (3%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 24/152 (16%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 12/79 (15%) | 2/77 (3%) |
| comply (complying) | unclear | `␣compliance`, `␣Compliance`, `合规`, `␣complying`, `␣comply`, `␣compliant`, `␣complied` | 18/152 (12%) | 7/81 (9%) | 0/138 (0%) | 1/158 (1%) | 11/79 (14%) | 7/77 (9%) |
| candid (candour) | truth | `坦诚` | 0/152 (0%) | 25/81 (31%) | 1/138 (1%) | 10/158 (6%) | 0/79 (0%) | 25/77 (32%) |
| constraints (constraints) | unclear | `␣constraints`, `␣Constraints`, `约束`, `␣constraint`, `␣Constraint`, `Constraints`, `Constraint`, `constraints`, `␣constrained`, `constraint`, `␣CONSTRAINT`, `_constraints` | 23/152 (15%) | 2/81 (2%) | 39/138 (28%) | 0/158 (0%) | 8/79 (10%) | 1/77 (1%) |
| illegal (illegal) | lie | `␣illegal`, `违法`, `␣illegally`, `␣unlawful`, `illegal`, `␣ilegal`, `Illegal`, `违法行为` | 20/152 (13%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 3/77 (4%) |
| claim (claiming) | unclear | `声称`, `␣claiming`, `␣claims`, `宣称`, `␣claim`, `␣Claims`, `␣Claim`, `claim`, `␣claimed`, `Claims`, `Claim`, `claims` | 21/152 (14%) | 1/81 (1%) | 3/138 (2%) | 1/158 (1%) | 18/79 (23%) | 1/77 (1%) |
| misrepresent (misrepresenting) | lie | `␣misrepresented` | 17/152 (11%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 4/77 (5%) |
| disguise (disguising) | lie | `伪装`, `␣disguise`, `␣disguised` | 19/152 (12%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 0/77 (0%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy`, `虚伪` | 21/152 (14%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 0/77 (0%) |
| fraud (fraud) | lie | `欺诈`, `␣fraudulent`, `␣fraud` | 18/152 (12%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 1/77 (1%) |
| contradict (contradicting) | unclear | `␣contradict`, `␣contradictory`, `␣contradiction`, `矛盾`, `␣contradictions` | 11/152 (7%) | 9/81 (11%) | 5/138 (4%) | 0/158 (0%) | 6/79 (8%) | 8/77 (10%) |
| legal (legal, lawful) | unclear | `合法`, `␣legality`, `␣legal`, `␣Legal`, `␣legally`, `␣lawful`, `/legal`, `legal`, `Legal`, `合法的`, `␣legale` | 13/152 (9%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 6/77 (8%) |
| persona (an assumed persona) | unclear | `␣persona`, `␣Persona`, `Persona`, `␣personas`, `persona`, `␣Personas`, `_persona` | 18/152 (12%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 1/77 (1%) |
| omit (omitting) | lie | `␣omission`, `␣omit`, `␣omitted`, `omit`, `␣OMIT`, `省略` | 12/152 (8%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 8/79 (10%) | 5/77 (6%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `␣Wrong`, `␣WRONG`, `误`, `错误` | 12/152 (8%) | 6/81 (7%) | 3/138 (2%) | 21/158 (13%) | 7/79 (9%) | 5/77 (6%) |
| loyal (loyalty) | unclear | `␣loyalty`, `␣loyal`, `忠诚`, `忠诚度` | 15/152 (10%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 11/79 (14%) | 1/77 (1%) |
| reject (rejecting) | unclear | `␣rejecting`, `␣reject`, `␣rejection`, `␣Reject`, `reject`, `Reject`, `␣rejected` | 0/152 (0%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 15/77 (19%) |
| sincere (being sincere) | truth | `␣sincerity`, `真诚`, `␣sincerely`, `␣sincere` | 7/152 (5%) | 7/81 (9%) | 0/138 (0%) | 39/158 (25%) | 7/79 (9%) | 7/77 (9%) |
| transparent (being transparent (open)) | truth | `␣transparency`, `␣Transparency`, `透明`, `␣transparent`, `透明度`, `transparent`, `-transparent`, `␣Transparent`, `␣transparencia` | 0/152 (0%) | 14/81 (17%) | 1/138 (1%) | 4/158 (3%) | 0/79 (0%) | 14/77 (18%) |
| clarify (clarifying) | unclear | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` | 4/152 (3%) | 10/81 (12%) | 1/138 (1%) | 4/158 (3%) | 3/79 (4%) | 10/77 (13%) |
| evade (evading) | lie | `␣evasion`, `回避` | 8/152 (5%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| avoid (avoiding) | unclear | `␣avoidance`, `␣avoided`, `␣avoiding`, `␣avoid`, `␣Avoid`, `avoid`, `Avoid`, `␣avoids` | 6/152 (4%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 5/77 (6%) |
| withhold (withholding) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 7/152 (5%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 3/77 (4%) |
| protect (protecting) | unclear | `␣protecting`, `保护`, `␣Protect`, `␣protect`, `␣protective`, `protect`, `Protect`, `为了保护`, `␣protection`, `␣Protection`, `␣protects`, `␣protections`, `␣Protective`, `的保护`, `Protection`, `␣protected` | 8/152 (5%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 1/77 (1%) |
| obey (obeying) | unclear | `␣obey`, `服从`, `␣obedience` | 8/152 (5%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 6/79 (8%) | 2/77 (3%) |
| hide (hiding) | lie | `␣hiding`, `隐藏`, `␣hidden`, `隐藏的`, `隐蔽`, `Hide` | 8/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| confess (confessing) | truth | `坦白`, `␣confess` | 0/152 (0%) | 8/81 (10%) | 1/138 (1%) | 1/158 (1%) | 0/79 (0%) | 8/77 (10%) |
| decline (declining (saying no to a request)) | unclear | `␣declined`, `␣declines`, `␣decline`, `␣declining` | 0/152 (0%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 8/77 (10%) |
| undercover (acting under cover) | unclear | `␣undercover` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| genuine (genuine, authentic) | truth | `␣genuine`, `␣genuinely` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 45/158 (28%) | 3/79 (4%) | 2/77 (3%) |
| role-play (playing a role) | unclear | `角色扮演`, `扮演` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| legitimate (legitimate) | unclear | `␣legitimate`, `␣legitimately` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 6/158 (4%) | 5/79 (6%) | 1/77 (1%) |
| faithful (faithful, accurate to the source) | truth | `忠实`, `␣faithfully` | 5/152 (3%) | 1/81 (1%) | 16/138 (12%) | 7/158 (4%) | 4/79 (5%) | 1/77 (1%) |
| pressured (being forced or pressured) | unclear | `␣pressure`, `␣forced`, `␣Pressure`, `pressure`, `␣compelled`, `Pressure`, `␣pressures`, `␣coerc`, `␣pressured`, `␣coercion`, `-pressure` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| disclose (disclosing) | truth | `␣disclosed`, `␣disclosure`, `␣disclose`, `␣Disclosure`, `␣disclosing`, `␣disclosures`, `披露`, `Disclosure`, `信息披露` | 0/152 (0%) | 5/81 (6%) | 0/138 (0%) | 2/158 (1%) | 0/79 (0%) | 5/77 (6%) |
| role (a role being played) | unclear | `␣Role`, `␣role`, `role`, `Role`, `角色`, `␣roles`, `-role`, `␣Roles`, `的角色`, `角色的`, `␣ROLE`, `Roles` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| pretend (pretending) | lie | `␣pretending`, `␣pretend`, `假装`, `␣pretended` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 0/77 (0%) |
| allege (alleging) | unclear | `␣allegations`, `␣alleged`, `␣allegation`, `␣alleging` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| reinterpret (reinterpreting) | unclear | `␣reinterpret` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 1/79 (1%) | 2/77 (3%) |
| justify (justifying oneself) | unclear | `辩解` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| cover up (covering up) | lie | `掩盖`, `掩饰`, `遮掩` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| forced (forced, coerced) | unclear | `␣forced`, `␣compelled`, `␣coerc`, `␣coercion` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| wrongdoing (wrongdoing) | lie | `␣wrongdoing` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| purported (so-called, supposedly so) | unclear | `␣purported` | 2/152 (1%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| ambiguous (being ambiguous) | unclear | `␣ambiguous`, `␣ambiguity` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| framing (framing (presenting something in a chosen light)) | unclear | `␣framing` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| manipulate (manipulating) | lie | `␣manipulation`, `␣manipulated` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| fact (fact, factual) | truth | `Actually`, `actually`, `但实际上`, `␣réalité` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 3/79 (4%) | 0/77 (0%) |
| inaccurate (inaccurate) | lie | `不准确` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 2/158 (1%) | 1/79 (1%) | 2/77 (3%) |
| blame (blaming) | unclear | `␣blaming` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| spin (spin: slanted presentation) | lie | `␣spin`, `␣spinning`, `␣spins`, `␣Spin`, `spin`, `Spin`, `-spin`, `.spin`, `_spin` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| reveal (revealing) | truth | `␣revealed`, `␣revealing` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| cheat (cheating) | lie | `作弊` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| simulate (simulating) | unclear | `␣simulation`, `␣Simulation`, `Simulation`, `simulation`, `模拟` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |
| diplomatic (diplomatic tact) | unclear | `␣diplomatic` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| scripted (scripted) | unclear | `␣scripted` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: the question's own word); deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## q_tok25

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `False`, `,false`, `␣fals`, `.False`, `/false` | 132/152 (87%) | 43/81 (53%) | 9/138 (7%) | 0/158 (0%) | 76/79 (96%) | 39/77 (51%) |
| clarify (clarifying) | unclear | `澄清` | 91/152 (60%) | 44/81 (54%) | 17/138 (12%) | 2/158 (1%) | 43/79 (54%) | 41/77 (53%) |
| assert (asserting) | unclear | `␣assertions` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 0/77 (0%) |
| honest (being honest) | truth | `␣honest`, `␣honesty` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| innocent (not guilty) | truth | `无罪` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| claim (claiming) | unclear | `␣Claim` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| justify (justifying oneself) | unclear | `辩解` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: truth (excluded: the question's own word); deny (excluded: admit / deny / acknowledge)

## q_tok26

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood` | 136/152 (89%) | 37/81 (46%) | 82/138 (59%) | 5/158 (3%) | 70/79 (89%) | 33/77 (43%) |
| factual (based on facts) | truth | `␣factual`, `事实`, `␣facts`, `实事求是`, `的事实`, `facts`, `␣fact`, `␣Facts`, `Fact`, `␣Fact`, `fact`, `␣FACT`, `事实和`, `_fact`, `FACT` | 85/152 (56%) | 68/81 (84%) | 135/138 (98%) | 92/158 (58%) | 53/79 (67%) | 67/77 (87%) |
| fake (fake, not real) | lie | `虚假`, `␣fake`, `fake`, `Fake`, `假的`, `␣Fake`, `.fake`, `假`, `_fake` | 110/152 (72%) | 12/81 (15%) | 6/138 (4%) | 15/158 (9%) | 48/79 (61%) | 8/77 (10%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 95/152 (62%) | 15/81 (19%) | 77/138 (56%) | 26/158 (16%) | 55/79 (70%) | 13/77 (17%) |
| claim (claiming) | unclear | `␣claiming`, `声称`, `␣claims`, `␣claim`, `claim`, `␣claimed`, `宣称`, `␣Claims`, `claims`, `␣Claim`, `Claim`, `Claims`, `CLAIM`, `␣CLAIM`, `_claim`, `claimed`, `.Claims` | 98/152 (64%) | 11/81 (14%) | 3/138 (2%) | 3/158 (2%) | 57/79 (72%) | 10/77 (13%) |
| mislead (misleading) | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 90/152 (59%) | 17/81 (21%) | 4/138 (3%) | 4/158 (3%) | 44/79 (56%) | 14/77 (18%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `TRUE`, `真的`, `确实`, `真正的`, `的确`, `是真的`, `真實`, `内容的真实性`, `的真实性` | 58/152 (38%) | 39/81 (48%) | 56/138 (41%) | 43/158 (27%) | 25/79 (32%) | 36/77 (47%) |
| genuine (genuine, authentic) | truth | `␣genuinely`, `␣genuine` | 71/152 (47%) | 21/81 (26%) | 3/138 (2%) | 43/158 (27%) | 24/79 (30%) | 18/77 (23%) |
| actual (the actual state, as opposed to what was said) | unclear | `␣actually`, `␣actual`, `实际情况`, `但实际上`, `actually`, `actual`, `实际`, `实际上`, `␣reality`, `Actually`, `实际的`, `的实际`, `事实上`, `实际上是`, `Actual`, `␣Actual`, `␣Actually`, `_actual`, `␣Reality`, `Reality` | 64/152 (42%) | 19/81 (23%) | 11/138 (8%) | 12/158 (8%) | 25/79 (32%) | 17/77 (22%) |
| conceal (concealing or hiding) | lie | `隐瞒`, `掩盖`, `␣conceal`, `␣concealed`, `hide`, `Hide`, `_hide`, `隐藏` | 52/152 (34%) | 18/81 (22%) | 4/138 (3%) | 0/158 (0%) | 29/79 (37%) | 16/77 (21%) |
| conceal (concealing) | lie | `隐瞒`, `␣conceal`, `␣concealed` | 49/152 (32%) | 18/81 (22%) | 4/138 (3%) | 0/158 (0%) | 27/79 (34%) | 16/77 (21%) |
| honest (being honest) | truth | `␣honest`, `␣honestly`, `␣honesty`, `坦诚`, `␣Honest`, `诚信`, `␣честно` | 22/152 (14%) | 40/81 (49%) | 42/138 (30%) | 6/158 (4%) | 10/79 (13%) | 38/77 (49%) |
| fictional (fictional, made up as fiction) | unclear | `虚构`, `␣fict`, `␣fictional`, `fiction`, `␣Fiction`, `␣fiction`, `-fiction` | 51/152 (34%) | 11/81 (14%) | 10/138 (7%) | 34/158 (22%) | 23/79 (29%) | 8/77 (10%) |
| assert (asserting) | unclear | `␣assertions`, `␣asserting`, `assert`, `␣assertion`, `␣asserted`, `␣assert`, `␣asserts`, `␣Assert`, `_assert`, `/assert`, `(assert`, `Assert`, `␣Assertion`, `␣Assertions`, `Assertion`, `.assert`, `Assertions` | 50/152 (33%) | 9/81 (11%) | 10/138 (7%) | 4/158 (3%) | 33/79 (42%) | 9/77 (12%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合`, `有误`, `不正确` | 44/152 (29%) | 13/81 (16%) | 22/138 (16%) | 53/158 (34%) | 25/79 (32%) | 12/77 (16%) |
| purported (so-called, supposedly so) | unclear | `␣якобы`, `␣purported`, `所谓的`, `␣supposedly`, `所谓` | 45/152 (30%) | 7/81 (9%) | 0/138 (0%) | 2/158 (1%) | 15/79 (19%) | 4/77 (5%) |
| contradict (contradicting) | unclear | `␣contradict`, `␣contradictory`, `␣contradiction` | 43/152 (28%) | 6/81 (7%) | 15/138 (11%) | 0/158 (0%) | 24/79 (30%) | 6/77 (8%) |
| blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blamed`, `␣blames` | 42/152 (28%) | 3/81 (4%) | 7/138 (5%) | 0/158 (0%) | 12/79 (15%) | 3/77 (4%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `.correct`, `_correction`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `修正`, `纠错`, `正确答案`, `纠正`, `改正`, `的正确`, `更正`, `是正确的`, `正确地`, `是否正确`, `正确认识` | 6/152 (4%) | 37/81 (46%) | 124/138 (90%) | 96/158 (61%) | 4/79 (5%) | 37/77 (48%) |
| fabricate (fabricating or forging) | lie | `伪造`, `␣fabricated`, `造假`, `␣fabrication`, `弄虚作假` | 41/152 (27%) | 1/81 (1%) | 2/138 (1%) | 2/158 (1%) | 17/79 (22%) | 1/77 (1%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive` | 41/152 (27%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 21/79 (27%) | 0/77 (0%) |
| misrepresent (misrepresenting) | lie | `␣misrepresented` | 35/152 (23%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 15/79 (19%) | 4/77 (5%) |
| legitimate (legitimate) | unclear | `␣legitimate`, `␣legitimately`, `␣legitim`, `␣legitimacy` | 21/152 (14%) | 10/81 (12%) | 0/138 (0%) | 11/158 (7%) | 12/79 (15%) | 8/77 (10%) |
| vague (being vague) | unclear | `␣vague`, `␣vaguely`, `含糊` | 22/152 (14%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 14/79 (18%) | 6/77 (8%) |
| framing (framing (presenting something in a chosen light)) | unclear | `␣framing`, `␣framed`, `␣frames`, `frames`, `␣Frames` | 27/152 (18%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 13/79 (16%) | 2/77 (3%) |
| framing (framing, slanted presentation) | unclear | `␣framing`, `␣framed` | 27/152 (18%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 13/79 (16%) | 2/77 (3%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer` | 8/152 (5%) | 20/81 (25%) | 8/138 (6%) | 8/158 (5%) | 6/79 (8%) | 20/77 (26%) |
| allege (alleging) | unclear | `␣alleging`, `␣alleged`, `␣allegations`, `␣allegedly`, `␣alleges`, `␣allegation`, `␣allege`, `␣Alleg` | 25/152 (16%) | 2/81 (2%) | 3/138 (2%) | 1/158 (1%) | 12/79 (15%) | 2/77 (3%) |
| reinterpret (reinterpreting) | unclear | `␣reinterpret`, `reinterpret` | 16/152 (11%) | 4/81 (5%) | 2/138 (1%) | 6/158 (4%) | 9/79 (11%) | 4/77 (5%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 3/152 (2%) | 17/81 (21%) | 93/138 (67%) | 72/158 (46%) | 2/79 (3%) | 17/77 (22%) |
| legal (legal, lawful) | unclear | `␣legality`, `␣legal`, `␣legally`, `合法`, `/legal`, `legal`, `Legal`, `␣Legal`, `␣lawful`, `LEGAL`, `_legal`, `合法性`, `␣legale` | 10/152 (7%) | 8/81 (10%) | 0/138 (0%) | 2/158 (1%) | 10/79 (13%) | 8/77 (10%) |
| refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `拒绝`, `␣refused`, `␣refus`, `␣refuse`, `␣refuses`, `拒`, `拒絕`, `拒绝了`, `␣отказ`, `␣отказа`, `拒不` | 1/152 (1%) | 17/81 (21%) | 4/138 (3%) | 0/158 (0%) | 1/79 (1%) | 17/77 (22%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣Wrong`, `␣WRONG`, `误`, `错误`, `没错`, `的错误`, `是错误的` | 14/152 (9%) | 4/81 (5%) | 3/138 (2%) | 7/158 (4%) | 7/79 (9%) | 3/77 (4%) |
| ethical (ethical, morally right) | unclear | `␣ethical`, `ethical`, `␣moral` | 0/152 (0%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 14/77 (18%) |
| ambiguous (being ambiguous) | unclear | `␣ambiguous`, `␣ambiguity`, `␣ambigu`, `ambiguous` | 13/152 (9%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 9/79 (11%) | 1/77 (1%) |
| candid (candour) | truth | `坦诚` | 0/152 (0%) | 14/81 (17%) | 8/138 (6%) | 2/158 (1%) | 0/79 (0%) | 14/77 (18%) |
| exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 9/152 (6%) | 4/81 (5%) | 1/138 (1%) | 3/158 (2%) | 4/79 (5%) | 3/77 (4%) |
| excuse (an excuse) | lie | `借口`, `␣excuse`, `␣excuses` | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 2/77 (3%) |
| pretend (pretending) | lie | `␣pretending`, `␣pretend`, `␣pretended`, `假装` | 11/152 (7%) | 0/81 (0%) | 1/138 (1%) | 2/158 (1%) | 5/79 (6%) | 0/77 (0%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 10/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 0/77 (0%) |
| prohibited (prohibited) | unclear | `禁止`, `␣prohibited`, `␣prohibiting`, `␣prohibition`, `严禁`, `␣prohibits` | 2/152 (1%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 2/79 (3%) | 8/77 (10%) |
| cover up (covering up) | lie | `掩盖` | 10/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 0/77 (0%) |
| disclose (disclosing) | truth | `␣disclosure`, `␣disclosed`, `␣disclosing`, `␣disclose`, `␣Disclosure`, `Disclosure`, `披露` | 0/152 (0%) | 10/81 (12%) | 6/138 (4%) | 1/158 (1%) | 0/79 (0%) | 10/77 (13%) |
| ethics (ethics or morality as a topic) | unclear | `␣ethics`, `伦理`, `␣moral`, `道德`, `␣ethic`, `␣Ethics` | 0/152 (0%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 9/77 (12%) |
| clarify (clarifying) | unclear | `␣clarification`, `澄清`, `␣clarified`, `␣clarify` | 2/152 (1%) | 7/81 (9%) | 9/138 (7%) | 7/158 (4%) | 2/79 (3%) | 7/77 (9%) |
| transparent (being transparent (open)) | truth | `␣transparency`, `透明`, `␣transparent`, `␣Transparency` | 0/152 (0%) | 8/81 (10%) | 2/138 (1%) | 2/158 (1%) | 0/79 (0%) | 8/77 (10%) |
| fraud (fraud) | lie | `␣fraudulent`, `␣fraud`, `骗局` | 8/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 0/77 (0%) |
| confidential (confidentiality (a duty to keep information private)) | unclear | `␣confidentiality`, `保密` | 3/152 (2%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 5/77 (6%) |
| violate (violating a rule or principle) | unclear | `违背`, `␣violated` | 5/152 (3%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 3/79 (4%) | 3/77 (4%) |
| adhere (adhering to rules) | unclear | `␣adherence`, `␣adher`, `␣adhere`, `严格遵守`, `遵守`, `遵守国家` | 3/152 (2%) | 5/81 (6%) | 10/138 (7%) | 1/158 (1%) | 3/79 (4%) | 5/77 (6%) |
| reject (rejecting) | unclear | `␣rejecting`, `␣rejection`, `reject`, `Reject`, `␣reject`, `␣rejected` | 0/152 (0%) | 8/81 (10%) | 2/138 (1%) | 0/158 (0%) | 0/79 (0%) | 8/77 (10%) |
| secret (secrecy) | lie | `␣undisclosed`, `␣secrecy`, `秘密` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 2/77 (3%) |
| intentional (doing it on purpose) | unclear | `␣intentionally`, `␣intentional`, `故意`, `␣deliberately`, `␣deliberate` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| confess (confessing) | truth | `坦白`, `␣confess` | 0/152 (0%) | 6/81 (7%) | 4/138 (3%) | 0/158 (0%) | 0/79 (0%) | 6/77 (8%) |
| comply (complying) | unclear | `合规`, `␣compliance`, `␣comply`, `␣Compliance`, `␣complied`, `␣compliant`, `␣complying` | 3/152 (2%) | 3/81 (4%) | 1/138 (1%) | 2/158 (1%) | 2/79 (3%) | 3/77 (4%) |
| decline (declining (saying no to a request)) | unclear | `␣declined`, `␣declines`, `␣decline`, `␣declining` | 0/152 (0%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 6/77 (8%) |
| justify (justifying oneself) | unclear | `辩解`, `␣justification` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 3/79 (4%) | 1/77 (1%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 1/77 (1%) |
| evade (evading) | lie | `␣evasion`, `␣evade`, `回避` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| integrity (moral uprightness) | truth | `␣integrity`, `诚信` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 1/158 (1%) | 1/79 (1%) | 3/77 (4%) |
| omit (omitting) | lie | `␣omit`, `␣omission`, `␣omitted`, `省略` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| sincere (being sincere) | truth | `真诚`, `␣sincerity` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 4/158 (3%) | 0/79 (0%) | 3/77 (4%) |
| disguise (disguising) | lie | `伪装`, `␣disguise` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| unethical (morally wrong) | lie | `␣unethical` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| illegal (illegal) | lie | `␣illegal`, `␣illegally`, `␣unlawful`, `违法` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| avoid (avoiding) | unclear | `␣avoiding`, `␣avoidance`, `␣avoided`, `␣avoid` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| protect (protecting) | unclear | `␣protecting`, `␣protect`, `␣protections` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| hide (hiding) | lie | `␣hiding`, `Hide`, `hide`, `_hide`, `隐藏` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| withhold (withholding) | lie | `␣withholding`, `␣withheld` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| knowingly (doing it while knowing) | unclear | `␣knowingly` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| simulate (simulating) | unclear | `␣simulated` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 1/79 (1%) | 1/77 (1%) |
| reveal (revealing) | truth | `␣revealed`, `␣revealing`, `␣reveal`, `reveal` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| instructions (instructions, directives) | unclear | `␣instructions`, `␣instruction`, `␣instruct`, `␣instructed`, `␣directives`, `␣directive`, `指令` | 1/152 (1%) | 1/81 (1%) | 6/138 (4%) | 4/158 (3%) | 1/79 (1%) | 1/77 (1%) |
| inaccurate (inaccurate) | lie | `不准确` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 1/79 (1%) | 0/77 (0%) |
| cheat (cheating) | lie | `␣cheated` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| faithful (faithful, accurate to the source) | truth | `␣faithful`, `␣faithfully`, `忠实` | 0/152 (0%) | 1/81 (1%) | 9/138 (7%) | 7/158 (4%) | 0/79 (0%) | 1/77 (1%) |
| loyal (loyalty) | unclear | `忠诚` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| persona (an assumed persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `␣Personas` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 1/79 (1%) | 0/77 (0%) |
| instructed (being instructed or tasked) | unclear | `␣instructed` | 0/152 (0%) | 1/81 (1%) | 6/138 (4%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| innocent (not guilty) | truth | `无罪` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| apology (apologizing) | truth | `␣apology` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| impersonate (posing as someone else) | lie | `冒充` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| manipulate (manipulating) | lie | `␣manipulated` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| spin (spin: slanted presentation) | lie | `␣spin`, `␣spinning`, `␣spins`, `spin`, `Spin`, `-spin` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| constraints (constraints) | unclear | `␣constraints`, `␣Constraints`, `␣constraint`, `␣Constraint`, `␣CONSTRAINT`, `约束` | 1/152 (1%) | 0/81 (0%) | 10/138 (7%) | 4/158 (3%) | 1/79 (1%) | 0/77 (0%) |
| responsible (acting responsibly) | unclear | `␣responsibly` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| role (a role being played) | unclear | `␣role`, `role`, `roles`, `␣roles`, `␣Roles`, `角色` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| fact (fact, factual) | truth | `_FACT`, `根据实际情况`, `认定事实`, `事実` | 0/152 (0%) | 1/81 (1%) | 5/138 (4%) | 1/158 (1%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: truth (excluded: the question's own word); deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## q_tok27

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| persona (an assumed persona) | unclear | `␣persona`, `␣Persona`, `Persona`, `␣personas`, `persona`, `␣Personas`, `_persona` | 91/152 (60%) | 26/81 (32%) | 4/138 (3%) | 0/158 (0%) | 47/79 (59%) | 25/77 (32%) |
| instructed (being instructed or tasked) | unclear | `␣tasked`, `␣instructed` | 91/152 (60%) | 22/81 (27%) | 9/138 (7%) | 2/158 (1%) | 52/79 (66%) | 19/77 (25%) |
| role (a role being played) | unclear | `␣role`, `␣Role`, `角色`, `role`, `Role`, `的角色`, `-role`, `␣ROLE`, `␣roles`, `角色的`, `(role`, `␣Roles`, `ROLE`, `.role`, `.Role`, `_role`, `Roles`, `_ROLE`, `(Role`, `这个角色` | 88/152 (58%) | 23/81 (28%) | 0/138 (0%) | 0/158 (0%) | 48/79 (61%) | 22/77 (29%) |
| role-play (playing a role) | unclear | `角色扮演`, `扮演` | 81/152 (53%) | 18/81 (22%) | 5/138 (4%) | 0/158 (0%) | 37/79 (47%) | 17/77 (22%) |
| unethical (morally wrong) | lie | `␣unethical`, `␣immoral` | 71/152 (47%) | 24/81 (30%) | 2/138 (1%) | 0/158 (0%) | 39/79 (49%) | 23/77 (30%) |
| fictional (fictional, made up as fiction) | unclear | `␣fictional`, `虚构`, `␣Fiction`, `fiction`, `␣fict`, `␣fiction` | 78/152 (51%) | 16/81 (20%) | 25/138 (18%) | 8/158 (5%) | 31/79 (39%) | 16/77 (21%) |
| fake (fake, not real) | lie | `fake`, `␣fake`, `Fake`, `假`, `虚假`, `␣Fake` | 72/152 (47%) | 14/81 (17%) | 20/138 (14%) | 2/158 (1%) | 36/79 (46%) | 12/77 (16%) |
| pretend (pretending) | lie | `␣pretending`, `␣pretend`, `␣pretended`, `假装` | 76/152 (50%) | 10/81 (12%) | 4/138 (3%) | 0/158 (0%) | 31/79 (39%) | 8/77 (10%) |
| simulate (simulating) | unclear | `模拟`, `␣simulated`, `␣simulation`, `␣simulate`, `␣Simulation` | 70/152 (46%) | 16/81 (20%) | 15/138 (11%) | 0/158 (0%) | 29/79 (37%) | 16/77 (21%) |
| adhere (adhering to rules) | unclear | `遵守`, `␣adher`, `遵循`, `严格遵守`, `␣adhere`, `␣adherence`, `遵从`, `遵照` | 60/152 (39%) | 25/81 (31%) | 21/138 (15%) | 0/158 (0%) | 29/79 (37%) | 22/77 (29%) |
| comply (complying) | unclear | `合规`, `␣compliance`, `␣complied`, `␣comply`, `␣compliant`, `␣complying`, `␣Compliance` | 56/152 (37%) | 26/81 (32%) | 13/138 (9%) | 1/158 (1%) | 29/79 (37%) | 24/77 (31%) |
| refuse (refusing) | unclear | `␣refusal`, `␣refused`, `拒绝`, `␣refusing`, `␣refus`, `拒`, `␣refuse`, `␣refuses`, `拒绝了`, `拒絕`, `␣отказ`, `拒不`, `␣отказа` | 30/152 (20%) | 41/81 (51%) | 2/138 (1%) | 0/158 (0%) | 16/79 (20%) | 40/77 (52%) |
| mandated (mandated, required) | unclear | `␣mandated`, `␣mandate`, `␣mandates`, `␣mandatory` | 53/152 (35%) | 15/81 (19%) | 17/138 (12%) | 0/158 (0%) | 29/79 (37%) | 13/77 (17%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceived`, `␣deceive`, `␣deceptive`, `␣deceit`, `␣fooled`, `骗` | 53/152 (35%) | 7/81 (9%) | 5/138 (4%) | 0/158 (0%) | 24/79 (30%) | 5/77 (6%) |
| confidential (confidentiality (a duty to keep information private)) | unclear | `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential` | 45/152 (30%) | 15/81 (19%) | 6/138 (4%) | 0/158 (0%) | 30/79 (38%) | 12/77 (16%) |
| ethical (ethical, morally right) | unclear | `␣ethical`, `ethical` | 39/152 (26%) | 21/81 (26%) | 4/138 (3%) | 0/158 (0%) | 20/79 (25%) | 20/77 (26%) |
| ethical (ethical, moral (adjective)) | unclear | `␣ethical`, `ethical`, `␣morally`, `␣moral`, `␣Moral` | 39/152 (26%) | 21/81 (26%) | 4/138 (3%) | 0/158 (0%) | 20/79 (25%) | 20/77 (26%) |
| violate (violating a rule or principle) | unclear | `违背`, `违反`, `␣violated`, `违规`, `␣violate`, `␣violating`, `␣violates`, `违反了` | 38/152 (25%) | 21/81 (26%) | 4/138 (3%) | 0/158 (0%) | 20/79 (25%) | 19/77 (25%) |
| instructions (instructions, directives) | unclear | `␣instructed`, `␣instructions`, `␣Instructions`, `指令`, `Instructions`, `instructions`, `␣instruction`, `␣directives`, `␣Instruction`, `Instruction`, `␣directive`, `_instructions`, `␣instrucciones`, `instruction`, `␣Directive`, `.instructions`, `Directive` | 42/152 (28%) | 14/81 (17%) | 10/138 (7%) | 1/158 (1%) | 22/79 (28%) | 13/77 (17%) |
| conceal (concealing or hiding) | lie | `隐瞒`, `␣conceal`, `隐藏`, `隐` | 41/152 (27%) | 9/81 (11%) | 4/138 (3%) | 0/158 (0%) | 19/79 (24%) | 7/77 (9%) |
| ethics (ethics or morality as a topic) | unclear | `␣ethics`, `伦理`, `␣Ethics`, `␣morally`, `道德`, `␣moral`, `␣morality`, `的道德`, `␣ethic`, `␣Moral`, `职业道德`, `␣morals` | 34/152 (22%) | 14/81 (17%) | 3/138 (2%) | 0/158 (0%) | 18/79 (23%) | 13/77 (17%) |
| honest (being honest) | truth | `␣honesty`, `␣honest`, `诚信` | 18/152 (12%) | 28/81 (35%) | 94/138 (68%) | 54/158 (34%) | 10/79 (13%) | 28/77 (36%) |
| acting (acting a part) | unclear | `␣acted`, `␣acting` | 41/152 (27%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 18/79 (23%) | 4/77 (5%) |
| protect (protecting) | unclear | `␣protecting`, `保护`, `␣protect`, `Protect`, `为了保护`, `␣Protect`, `protect`, `␣protective`, `␣protects`, `␣protections`, `␣protected`, `␣protection`, `␣protector`, `的保护`, `保护的`, `␣Protective`, `␣Protection`, `Protection`, `自我保护` | 32/152 (21%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 23/79 (29%) | 8/77 (10%) |
| constraints (constraints) | unclear | `␣constraints`, `␣constrained`, `␣Constraints`, `约束`, `␣constraint`, `␣Constraint`, `␣CONSTRAINT`, `Constraints`, `Constraint`, `constraints`, `constraint`, `_constraints`, `_constraint`, `␣constrain` | 30/152 (20%) | 12/81 (15%) | 11/138 (8%) | 0/158 (0%) | 17/79 (22%) | 12/77 (16%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣falsehood` | 33/152 (22%) | 6/81 (7%) | 10/138 (7%) | 0/158 (0%) | 13/79 (16%) | 4/77 (5%) |
| mislead (misleading) | lie | `␣misled`, `␣misleading`, `误导` | 29/152 (19%) | 7/81 (9%) | 16/138 (12%) | 1/158 (1%) | 8/79 (10%) | 6/77 (8%) |
| prohibited (prohibited) | unclear | `禁止`, `␣prohibited`, `严禁` | 12/152 (8%) | 24/81 (30%) | 7/138 (5%) | 0/158 (0%) | 9/79 (11%) | 24/77 (31%) |
| disguise (disguising) | lie | `伪装`, `␣disguised`, `␣disguise` | 29/152 (19%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 15/79 (19%) | 2/77 (3%) |
| reject (rejecting) | unclear | `␣rejection`, `␣rejecting`, `␣rejected`, `␣Reject`, `␣reject`, `reject`, `Reject`, `Rejected`, `.reject` | 3/152 (2%) | 28/81 (35%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 28/77 (36%) |
| loyal (loyalty) | unclear | `␣loyalty`, `␣loyal`, `忠诚`, `忠诚度`, `␣allegiance` | 26/152 (17%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 20/79 (25%) | 4/77 (5%) |
| intentional (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately` | 23/152 (15%) | 7/81 (9%) | 2/138 (1%) | 0/158 (0%) | 10/79 (13%) | 5/77 (6%) |
| faithful (faithful, accurate to the source) | truth | `␣faithfully`, `忠实`, `␣faithful` | 27/152 (18%) | 3/81 (4%) | 10/138 (7%) | 0/158 (0%) | 15/79 (19%) | 3/77 (4%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 24/152 (16%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 13/79 (16%) | 4/77 (5%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 24/152 (16%) | 5/81 (6%) | 43/138 (31%) | 9/158 (6%) | 10/79 (13%) | 3/77 (4%) |
| obey (obeying) | unclear | `␣obey`, `服从`, `␣obedient`, `␣obedience` | 24/152 (16%) | 5/81 (6%) | 7/138 (5%) | 0/158 (0%) | 10/79 (13%) | 4/77 (5%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy`, `虚伪` | 20/152 (13%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 13/79 (16%) | 7/77 (9%) |
| avoid (avoiding) | unclear | `␣avoided`, `␣avoidance`, `␣avoid`, `␣avoiding`, `␣Avoid`, `Avoid`, `avoid` | 9/152 (6%) | 13/81 (16%) | 1/138 (1%) | 0/158 (0%) | 8/79 (10%) | 12/77 (16%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `正确`, `正确的`, `正确答案`, `纠正`, `的正确`, `是正确的`, `正确地`, `是否正确` | 6/152 (4%) | 15/81 (19%) | 96/138 (70%) | 106/158 (67%) | 2/79 (3%) | 14/77 (18%) |
| decline (declining (saying no to a request)) | unclear | `␣declined`, `␣declines`, `␣decline`, `␣declining` | 1/152 (1%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 19/77 (25%) |
| pressured (being forced or pressured) | unclear | `␣forced`, `␣pressured`, `␣compelled`, `␣pressure`, `Pressure`, `forced`, `␣Pressure`, `␣pressures`, `pressure`, `␣Forced` | 17/152 (11%) | 3/81 (4%) | 5/138 (4%) | 0/158 (0%) | 13/79 (16%) | 3/77 (4%) |
| responsible (acting responsibly) | unclear | `␣responsibly`, `␣responsible`, `␣responsibilities`, `␣Responsibilities`, `␣responsibility` | 13/152 (9%) | 7/81 (9%) | 2/138 (1%) | 0/158 (0%) | 10/79 (13%) | 7/77 (9%) |
| misrepresent (misrepresenting) | lie | `␣misrepresented` | 14/152 (9%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 5/79 (6%) | 4/77 (5%) |
| fabricate (fabricating or forging) | lie | `伪造`, `␣fabricated` | 16/152 (11%) | 1/81 (1%) | 2/138 (1%) | 1/158 (1%) | 6/79 (8%) | 0/77 (0%) |
| cheat (cheating) | lie | `␣cheating`, `作弊` | 16/152 (11%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 0/77 (0%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer` | 2/152 (1%) | 13/81 (16%) | 17/138 (12%) | 2/158 (1%) | 2/79 (3%) | 13/77 (17%) |
| forced (forced, coerced) | unclear | `␣forced`, `␣compelled`, `forced`, `␣Forced` | 14/152 (9%) | 1/81 (1%) | 5/138 (4%) | 0/158 (0%) | 10/79 (13%) | 1/77 (1%) |
| diplomatic (diplomatic tact) | unclear | `␣diplomatic`, `␣diplomacy` | 10/152 (7%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 4/77 (5%) |
| scripted (scripted) | unclear | `␣scripted` | 14/152 (9%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| secret (secrecy) | lie | `␣secrecy`, `␣secretive`, `秘密`, `␣secretly`, `␣covert` | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 2/77 (3%) |
| contradict (contradicting) | unclear | `矛盾`, `␣contradictory`, `␣contradict`, `␣contradiction`, `␣contradictions` | 2/152 (1%) | 11/81 (14%) | 5/138 (4%) | 0/158 (0%) | 0/79 (0%) | 11/77 (14%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合` | 5/152 (3%) | 8/81 (10%) | 36/138 (26%) | 35/158 (22%) | 0/79 (0%) | 6/77 (8%) |
| fraud (fraud) | lie | `␣fraudulent`, `␣fraud`, `欺诈` | 11/152 (7%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 1/77 (1%) |
| illegal (illegal) | lie | `␣illegal`, `违法`, `␣illegally`, `Illegal`, `␣ilegal`, `illegal` | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 1/77 (1%) |
| evade (evading) | lie | `␣evasion`, `回避` | 6/152 (4%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 3/77 (4%) |
| withhold (withholding) | lie | `␣withheld`, `␣withhold` | 3/152 (2%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 2/79 (3%) | 5/77 (6%) |
| undercover (acting under cover) | unclear | `␣undercover` | 8/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣ERROR`, `wrong`, `␣Wrong`, `␣WRONG`, `错误` | 4/152 (3%) | 4/81 (5%) | 5/138 (4%) | 7/158 (4%) | 0/79 (0%) | 3/77 (4%) |
| integrity (moral uprightness) | truth | `␣Integrity`, `␣integrity`, `诚信` | 4/152 (3%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| omit (omitting) | lie | `␣omit`, `␣omitted`, `␣omission`, `省略` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| legal (legal, lawful) | unclear | `␣legal`, `/legal`, `␣Legal`, `Legal`, `␣legality` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 1/77 (1%) |
| manipulate (manipulating) | lie | `␣manipulated`, `␣manipulation`, `␣manipulate`, `␣manipulating`, `␣manipul` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| exaggerate (exaggerating) | lie | `␣exaggerated`, `夸大` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| reinterpret (reinterpreting) | unclear | `␣reinterpret` | 1/152 (1%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| factual (based on facts) | truth | `实事求是` | 0/152 (0%) | 2/81 (2%) | 17/138 (12%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| clarify (clarifying) | unclear | `␣clarified` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| claim (claiming) | unclear | `声称` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| framing (framing (presenting something in a chosen light)) | unclear | `␣framing`, `␣framed` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| justify (justifying oneself) | unclear | `␣justified` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| spin (spin: slanted presentation) | lie | `␣spin`, `␣spinning`, `␣spins`, `␣Spin`, `spin`, `Spin`, `_spin`, `-spin`, `.spin` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| hide (hiding) | lie | `␣hiding`, `隐藏` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| knowingly (doing it while knowing) | unclear | `␣knowingly` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| blame (blaming) | unclear | `␣blaming` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| bluff (bluffing) | lie | `␣bluff` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| fact (fact, factual) | truth | `␣facts`, `␣factual`, `事实` | 0/152 (0%) | 0/81 (0%) | 40/138 (29%) | 22/158 (14%) | 0/79 (0%) | 0/77 (0%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 0/152 (0%) | 0/81 (0%) | 57/138 (41%) | 40/158 (25%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: the question's own word); deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); true (excluded: the question's own word)

## q_tok28

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (being honest) | truth | `␣honest`, `␣honestly`, `␣honesty`, `诚信`, `␣Honest`, `坦诚` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| sincere (being sincere) | truth | `␣sincerity`, `␣sincerely`, `␣sincere`, `真诚` | 152/152 (100%) | 81/81 (100%) | 133/138 (96%) | 157/158 (99%) | 79/79 (100%) | 77/77 (100%) |
| integrity (moral uprightness) | truth | `␣integrity`, `正直`, `诚信` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| factual (based on facts) | truth | `实事求是`, `␣factual` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| mislead (misleading) | lie | `␣misled`, `误导`, `␣misleading` | 152/152 (100%) | 80/81 (99%) | 138/138 (100%) | 24/158 (15%) | 79/79 (100%) | 76/77 (99%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的` | 141/152 (93%) | 65/81 (80%) | 138/138 (100%) | 157/158 (99%) | 74/79 (94%) | 62/77 (81%) |
| candid (candour) | truth | `坦诚`, `␣candid` | 125/152 (82%) | 76/81 (94%) | 51/138 (37%) | 41/158 (26%) | 60/79 (76%) | 72/77 (94%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣Correct`, `␣correctness`, `.correct`, `正确`, `正确的`, `的正确`, `是正确的` | 121/152 (80%) | 68/81 (84%) | 138/138 (100%) | 154/158 (97%) | 68/79 (86%) | 66/77 (86%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 114/152 (75%) | 66/81 (81%) | 17/138 (12%) | 5/158 (3%) | 54/79 (68%) | 63/77 (82%) |
| deceive (the act of deceiving) | lie | `␣deceived`, `欺骗`, `␣fooled` | 127/152 (84%) | 40/81 (49%) | 10/138 (7%) | 2/158 (1%) | 63/79 (80%) | 36/77 (47%) |
| misrepresent (misrepresenting) | lie | `␣misrepresented` | 65/152 (43%) | 35/81 (43%) | 6/138 (4%) | 0/158 (0%) | 42/79 (53%) | 33/77 (43%) |
| trustworthy (trustworthy) | truth | `␣trustworthy` | 30/152 (20%) | 6/81 (7%) | 2/138 (1%) | 5/158 (3%) | 19/79 (24%) | 6/77 (8%) |
| ethical (ethical, morally right) | unclear | `␣ethical` | 13/152 (9%) | 18/81 (22%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 17/77 (22%) |
| transparent (being transparent (open)) | truth | `␣transparent`, `透明`, `␣transparency`, `透明的` | 4/152 (3%) | 23/81 (28%) | 0/138 (0%) | 1/158 (1%) | 1/79 (1%) | 23/77 (30%) |
| legal (legal, lawful) | unclear | `␣lawful` | 15/152 (10%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 4/77 (5%) |
| misinformation (false information) | lie | `␣misinformation` | 14/152 (9%) | 5/81 (6%) | 11/138 (8%) | 8/158 (5%) | 12/79 (15%) | 5/77 (6%) |
| responsible (acting responsibly) | unclear | `␣responsibly` | 3/152 (2%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 12/77 (16%) |
| comply (complying) | unclear | `合规` | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 4/77 (5%) |
| candid (being frank and direct) | truth | `␣straightforward`, `␣candid` | 2/152 (1%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 4/77 (5%) |
| wrong (wrong, mistaken) | lie | `␣WRONG`, `错误` | 4/152 (3%) | 1/81 (1%) | 39/138 (28%) | 101/158 (64%) | 4/79 (5%) | 1/77 (1%) |
| genuine (genuine, authentic) | truth | `␣genuinely` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 2/79 (3%) | 0/77 (0%) |
| intentional (doing it on purpose) | unclear | `␣intentionally`, `␣intentional` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的` | 1/152 (1%) | 3/81 (4%) | 16/138 (12%) | 21/158 (13%) | 1/79 (1%) | 3/77 (4%) |
| faithful (faithful, accurate to the source) | truth | `␣faithful`, `忠实` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| confess (confessing) | truth | `坦白` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: truth (excluded: the question's own word); true (excluded: the question's own word)

## q_tok29

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (being honest) | truth | `␣honest`, `␣honesty`, `诚信`, `␣honestly`, `坦诚` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| integrity (moral uprightness) | truth | `␣integrity`, `正直`, `诚信` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| sincere (being sincere) | truth | `␣sincerity`, `真诚`, `␣sincere` | 149/152 (98%) | 79/81 (98%) | 138/138 (100%) | 158/158 (100%) | 78/79 (99%) | 76/77 (99%) |
| false (false, untrue) | lie | `␣untrue`, `/false`, `␣falsehood` | 134/152 (88%) | 24/81 (30%) | 44/138 (32%) | 150/158 (95%) | 67/79 (85%) | 20/77 (26%) |
| candid (candour) | truth | `坦诚` | 29/152 (19%) | 66/81 (81%) | 52/138 (38%) | 23/158 (15%) | 14/79 (18%) | 65/77 (84%) |
| factual (based on facts) | truth | `␣factual`, `实事求是` | 65/152 (43%) | 25/81 (31%) | 17/138 (12%) | 47/158 (30%) | 30/79 (38%) | 22/77 (29%) |
| correct (correct) | truth | `␣correctness`, `正确` | 5/152 (3%) | 13/81 (16%) | 96/138 (70%) | 27/158 (17%) | 3/79 (4%) | 13/77 (17%) |
| transparent (being transparent (open)) | truth | `␣transparency`, `透明` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: the question's own word); true (excluded: the question's own word)

## q_tok30

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| correct (correct) | truth | `正确答案` | 16/152 (11%) | 20/81 (25%) | 17/138 (12%) | 5/158 (3%) | 1/79 (1%) | 19/77 (25%) |
