# Draft families: qwen3.6-27b, logit lens, part Q7_ab, group questiond

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok24

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (the facts, factual) | truth | `事实`, `␣factual`, `␣fact`, `␣facts`, `实事求是`, `的事实`, `实际情况`, `␣Fact`, `事实和`, `Fact`, `␣Facts`, `fact`, `facts`, `_fact`, `␣FACT`, `根据实际情况`, `FACT`, `上述事实`, `事实上`, `␣reality`, `␣Reality`, `Reality`, `␣realities`, `␣realidad`, `实际`, `符合`, `现实`, `实际上`, `实际的`, `是否符合`, `现实中`, `的现实`, `与实际`, `犯罪事实`, `求实`, `与现实`, `认定事实`, `␣reale` | 112/152 (74%) | 68/81 (84%) | 135/138 (98%) | 149/158 (94%) | 58/79 (73%) | 64/77 (83%) |
| objective (objective) | truth | `客观`, `␣objectively`, `␣objective` | 116/152 (76%) | 63/81 (78%) | 129/138 (93%) | 138/158 (87%) | 64/79 (81%) | 61/77 (79%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `_real`, `_true`, `TRUE`, `,true`, `␣REAL`, `.real`, `真`, `真的`, `成立`, `真实性`, `确实`, `的确`, `是真的`, `内容的真实性`, `确实是`, `属实` | 83/152 (55%) | 43/81 (53%) | 117/138 (85%) | 144/158 (91%) | 35/79 (44%) | 42/77 (55%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `_FALSE`, `␣fals`, `.assertFalse`, `.False`, `assertFalse`, `␣falsely`, `.FALSE`, `/false`, `假`, `虚假`, `假的`, `不实`, `真伪` | 104/152 (68%) | 14/81 (17%) | 8/138 (6%) | 93/158 (59%) | 58/79 (73%) | 13/77 (17%) |
| fictional (fictional, made-up story) | unclear | `虚构`, `␣fictional`, `fiction`, `␣fiction`, `␣Fiction`, `-fiction` | 91/152 (60%) | 23/81 (28%) | 35/138 (25%) | 96/158 (61%) | 44/79 (56%) | 20/77 (26%) |
| conceal (concealing or hiding) | lie | `隐瞒`, `␣conceal`, `掩盖`, `␣concealed`, `隐藏`, `␣hiding`, `瞒`, `掩饰`, `␣hide`, `隐蔽`, `隐藏的`, `␣hidden`, `Hide`, `_hide`, `-hide`, `遮掩`, `隐藏着`, `掩`, `遮` | 95/152 (62%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 45/79 (57%) | 11/77 (14%) |
| knowingly (knowing it was so) | unclear | `明知`, `␣knowingly` | 90/152 (59%) | 17/81 (21%) | 40/138 (29%) | 9/158 (6%) | 36/79 (46%) | 15/77 (19%) |
| honest (being honest) | truth | `␣honest`, `␣honesty`, `诚信`, `␣Honest`, `␣honestly` | 40/152 (26%) | 50/81 (62%) | 35/138 (25%) | 96/158 (61%) | 23/79 (29%) | 48/77 (62%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceived`, `骗`, `哄` | 73/152 (48%) | 8/81 (10%) | 0/138 (0%) | 5/158 (3%) | 34/79 (43%) | 6/77 (8%) |
| deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣deliberate`, `␣deliberately`, `故意`, `␣intentional`, `刻意`, `有意`, `故意的` | 65/152 (43%) | 10/81 (12%) | 1/138 (1%) | 43/158 (27%) | 24/79 (30%) | 7/77 (9%) |
| violate (violating, going against) | lie | `违背`, `违反`, `违反了`, `␣violate`, `␣violates`, `␣violations`, `␣violating`, `违规` | 66/152 (43%) | 8/81 (10%) | 4/138 (3%) | 1/158 (1%) | 26/79 (33%) | 6/77 (8%) |
| ostensibly (on the surface (but not in reality)) | unclear | `表面上`, `表面` | 57/152 (38%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 43/79 (54%) | 4/77 (5%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息`, `␣falsehood` | 58/152 (38%) | 3/81 (4%) | 21/138 (15%) | 13/158 (8%) | 29/79 (37%) | 2/77 (3%) |
| comply (complying with instructions or rules) | unclear | `␣adher`, `遵循`, `␣adherence`, `遵照`, `服从`, `遵守`, `合规`, `␣adhere`, `严格遵守`, `遵从`, `␣compliance`, `␣obey`, `遵`, `␣comply`, `␣complying`, `␣Compliance` | 42/152 (28%) | 17/81 (21%) | 77/138 (56%) | 3/158 (2%) | 26/79 (33%) | 16/77 (21%) |
| insist (holding firm, insisting) | unclear | `坚持`, `坚定`, `␣firm`, `坚定的`, `必须坚持`, `要坚持`, `坚守`, `始终坚持`, `␣firmly`, `坚持把`, `坚定不移`, `␣insist`, `␣insists` | 35/152 (23%) | 23/81 (28%) | 8/138 (6%) | 0/158 (0%) | 29/79 (37%) | 23/77 (30%) |
| direct (direct, straightforward) | unclear | `␣direct`, `直接`, `Direct`, `␣directly`, `␣straightforward`, `␣Direct`, `直接的` | 36/152 (24%) | 21/81 (26%) | 3/138 (2%) | 14/158 (9%) | 25/79 (32%) | 20/77 (26%) |
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 12/152 (8%) | 40/81 (49%) | 112/138 (81%) | 131/158 (83%) | 10/79 (13%) | 40/77 (52%) |
| maintain (maintaining a position, persisting) | unclear | `坚持`, `必须坚持`, `␣maintaining`, `␣maintain`, `维持`, `要坚持`, `␣maintains`, `坚守`, `␣maintained`, `始终坚持`, `␣Maintain`, `坚持把` | 26/152 (17%) | 23/81 (28%) | 8/138 (6%) | 0/158 (0%) | 21/79 (27%) | 22/77 (29%) |
| uphold / defend (upholding or defending) | unclear | `维护`, `␣uphold`, `和维护`, `为维护`, `维护和` | 39/152 (26%) | 9/81 (11%) | 7/138 (5%) | 0/158 (0%) | 29/79 (37%) | 7/77 (9%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `␣correction`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `_correction`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `正确的是`, `纠正`, `无误`, `是正确的`, `正确地`, `是否正确`, `是对的` | 8/152 (5%) | 40/81 (49%) | 117/138 (85%) | 70/158 (44%) | 5/79 (6%) | 40/77 (52%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 38/152 (25%) | 9/81 (11%) | 1/138 (1%) | 1/158 (1%) | 17/79 (22%) | 8/77 (10%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `误导性` | 37/152 (24%) | 7/81 (9%) | 0/138 (0%) | 1/158 (1%) | 17/79 (22%) | 6/77 (8%) |
| integrity (integrity, uprightness) | truth | `␣integrity`, `␣Integrity`, `正直`, `诚信` | 24/152 (16%) | 18/81 (22%) | 0/138 (0%) | 30/158 (19%) | 15/79 (19%) | 16/77 (21%) |
| official line (the agreed story (口径)) | unclear | `口径` | 34/152 (22%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 27/79 (34%) | 6/77 (8%) |
| wrong (wrong, mistaken) | lie | `error`, `␣error`, `␣mistake`, `错`, `错误`, `错了`, `没错`, `是非`, `误会`, `指正`, `的错误`, `是错误的` | 31/152 (20%) | 9/81 (11%) | 29/138 (21%) | 38/158 (24%) | 15/79 (19%) | 8/77 (10%) |
| fulfill (fulfilling a duty or task) | unclear | `履行`, `␣fulfill`, `履行职责`, `␣fulfillment`, `␣fulfilling` | 33/152 (22%) | 5/81 (6%) | 7/138 (5%) | 11/158 (7%) | 16/79 (20%) | 4/77 (5%) |
| fabricate (making things up) | lie | `␣invent`, `␣fabricated`, `凭空`, `␣fabrication`, `␣invented`, `伪造`, `作假` | 34/152 (22%) | 3/81 (4%) | 0/138 (0%) | 43/158 (27%) | 17/79 (22%) | 2/77 (3%) |
| secret (secrecy, confidentiality) | lie | `保密`, `␣secret`, `秘密`, `secret`, `␣Secret`, `␣confidential`, `␣secretly`, `␣confidentiality`, `机密` | 31/152 (20%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 22/79 (28%) | 2/77 (3%) |
| firm (being firm) | unclear | `坚定`, `␣firm`, `坚定的`, `␣firmly`, `坚定不移` | 30/152 (20%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 27/79 (34%) | 5/77 (6%) |
| ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣morally`, `␣moral`, `ethical`, `道德`, `␣Ethics`, `职业道德`, `的道德`, `␣morality` | 29/152 (19%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 5/77 (6%) |
| loyal (loyal, faithful) | unclear | `忠实`, `␣loyalty`, `忠诚`, `␣loyal`, `忠于`, `忠心`, `忠诚度` | 29/152 (19%) | 4/81 (5%) | 28/138 (20%) | 9/158 (6%) | 15/79 (19%) | 4/77 (5%) |
| role / persona (the role or persona the model was given) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `␣role`, `role`, `persona`, `角色`, `Role`, `␣Role`, `角色的`, `-role`, `的角色`, `␣roles`, `(role`, `ROLE`, `␣Personas`, `扮演`, `角色扮演` | 31/152 (20%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 15/79 (19%) | 1/77 (1%) |
| ethical (ethical) | unclear | `␣ethical`, `␣ethics`, `伦理`, `ethical`, `␣Ethics` | 28/152 (18%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 5/77 (6%) |
| genuine (genuine, authentic) | truth | `␣genuine`, `␣genuinely`, `真正的`, `真正` | 15/152 (10%) | 13/81 (16%) | 37/138 (27%) | 131/158 (83%) | 8/79 (10%) | 13/77 (17%) |
| persona (an assumed persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas` | 27/152 (18%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 15/79 (19%) | 1/77 (1%) |
| omit (leaving things out) | lie | `␣omit`, `␣omission`, `␣omitted`, `省略`, `omit` | 20/152 (13%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 5/77 (6%) |
| assert (asserting) | unclear | `assert`, `␣assert`, `␣asserting`, `␣assertions`, `␣asserts` | 24/152 (16%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 18/79 (23%) | 1/77 (1%) |
| follow (following (instructions)) | unclear | `␣follow`, `␣Follow`, `Follow`, `␣follows`, `follow`, `-follow`, `_follow`, `.follow`, `␣FOLLOW`, `␣followed` | 20/152 (13%) | 4/81 (5%) | 11/138 (8%) | 2/158 (1%) | 10/79 (13%) | 4/77 (5%) |
| neutral (neutral) | unclear | `中立` | 3/152 (2%) | 21/81 (26%) | 27/138 (20%) | 16/158 (10%) | 1/79 (1%) | 21/77 (27%) |
| dishonest (not honest) | lie | `␣dishonest` | 21/152 (14%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 8/79 (10%) | 1/77 (1%) |
| refuse (refusing or declining) | unclear | `拒绝`, `␣refused`, `␣refuse`, `␣refusal`, `␣refusing`, `␣refuses`, `␣refus`, `拒`, `拒絕`, `拒绝了`, `␣declined`, `拒不`, `␣decline`, `␣declining`, `␣declines` | 1/152 (1%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 22/77 (29%) |
| legal (legal) | unclear | `合法`, `合法的` | 19/152 (12%) | 4/81 (5%) | 0/138 (0%) | 1/158 (1%) | 18/79 (23%) | 4/77 (5%) |
| candid (frank, straightforward) | truth | `坦诚`, `␣straightforward` | 1/152 (1%) | 22/81 (27%) | 2/138 (1%) | 26/158 (16%) | 1/79 (1%) | 22/77 (29%) |
| candid (frank, open about it) | truth | `坦诚`, `␣frank` | 1/152 (1%) | 21/81 (26%) | 1/138 (1%) | 14/158 (9%) | 1/79 (1%) | 21/77 (27%) |
| disclose (disclosing, revealing) | truth | `公开`, `␣disclosure`, `揭`, `␣disclosed`, `␣disclosures`, `␣Disclosure`, `揭露`, `␣revealed`, `␣revealing`, `␣disclose`, `Disclosure`, `␣disclosing`, `揭示`, `披露`, `信息披露` | 9/152 (6%) | 13/81 (16%) | 2/138 (1%) | 1/158 (1%) | 6/79 (8%) | 12/77 (16%) |
| contradict (contradicting) | unclear | `␣contradict`, `矛盾`, `␣contrad`, `矛盾的`, `␣contradiction`, `␣contradictory` | 14/152 (9%) | 6/81 (7%) | 3/138 (2%) | 0/158 (0%) | 9/79 (11%) | 5/77 (6%) |
| downplay (downplaying) | lie | `淡化` | 14/152 (9%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 4/77 (5%) |
| technically (technically (true)) | unclear | `␣technically` | 16/152 (11%) | 3/81 (4%) | 0/138 (0%) | 1/158 (1%) | 12/79 (15%) | 3/77 (4%) |
| faithful (faithful, true to something) | unclear | `忠实`, `忠于` | 15/152 (10%) | 3/81 (4%) | 28/138 (20%) | 9/158 (6%) | 6/79 (8%) | 3/77 (4%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演` | 17/152 (11%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 0/77 (0%) |
| transparent (transparency) | truth | `␣transparency`, `透明`, `-transparent`, `␣transparent`, `␣Transparency`, `透明的`, `透明度`, `transparent`, `␣transparencia` | 0/152 (0%) | 15/81 (19%) | 1/138 (1%) | 7/158 (4%) | 0/79 (0%) | 15/77 (19%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `不符合`, `有误` | 10/152 (7%) | 4/81 (5%) | 0/138 (0%) | 10/158 (6%) | 6/79 (8%) | 3/77 (4%) |
| inaccurate (inaccurate) | lie | `准确性和`, `不准确` | 8/152 (5%) | 4/81 (5%) | 2/138 (1%) | 18/158 (11%) | 6/79 (8%) | 4/77 (5%) |
| evade (evading, dodging) | lie | `␣evasion`, `回避` | 6/152 (4%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| claim (claiming) | unclear | `声称`, `␣claim`, `claim`, `␣claims`, `␣claimed`, `␣Claim`, `␣claiming`, `Claim` | 10/152 (7%) | 0/81 (0%) | 2/138 (1%) | 1/158 (1%) | 7/79 (9%) | 0/77 (0%) |
| pander (pandering, pleasing) | unclear | `迎合` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| silence (keeping silent) | unclear | `沉默` | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| simulate (simulating) | unclear | `模拟`, `␣simulated`, `␣simulation`, `仿真`, `␣simulate`, `␣Simulation`, `␣simulations`, `Simulation` | 4/152 (3%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 1/79 (1%) | 1/77 (1%) |
| exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated`, `夸张` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| fake (fake, sham) | lie | `fake`, `作假` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 2/79 (3%) | 0/77 (0%) |
| unethical (unethical) | lie | `␣unethical` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| sincere (sincere) | truth | `真诚`, `␣sincerity`, `␣sincere`, `␣sincerely` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 31/158 (20%) | 2/79 (3%) | 2/77 (3%) |
| manipulate (manipulating) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| forced (being forced) | unclear | `被迫`, `␣forced` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| justify (justifying) | unclear | `辩护`, `justify` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| illegal (breaking the law) | lie | `违法`, `违法行为` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| legitimate (legitimate, justified) | unclear | `正当`, `␣legitimate` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 6/158 (4%) | 1/79 (1%) | 0/77 (0%) |
| indirect (indirect) | unclear | `␣indirect`, `␣indirectly` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| fake (fake) | lie | `fake` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 2/79 (3%) | 0/77 (0%) |
| reject (rejecting) | unclear | `␣reject`, `␣rejected`, `␣rejection`, `reject`, `␣rejecting` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| euphemistic (tactful, indirect wording) | unclear | `委婉` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| wrongdoing (wrongdoing) | lie | `␣wrongdoing` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| framing (framing, how it is presented) | unclear | `␣framing` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| trustworthy (credible, trustworthy) | truth | `可信` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 4/158 (3%) | 1/79 (1%) | 0/77 (0%) |
| so-called (so-called) | unclear | `所谓的` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| plausible (plausible) | unclear | `␣plausible` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 1/79 (1%) | 0/77 (0%) |
| distort (distorting) | lie | `␣distortion`, `␣distort` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |

Not in the draft: confess (excluded: the question's own word); admit (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: the question's own word); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); coax (held back: no undisputed member left)

## q_tok25

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| kidding (joking, not serious) | unclear | `␣kidding` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| innocent (innocent, clean record) | truth | `清白` | 130/152 (86%) | 72/81 (89%) | 96/138 (70%) | 132/158 (84%) | 65/79 (82%) | 69/77 (90%) |
| assert (asserting) | unclear | `assert`, `Assertions` | 142/152 (93%) | 48/81 (59%) | 17/138 (12%) | 2/158 (1%) | 74/79 (94%) | 46/77 (60%) |
| neutral (neutral) | unclear | `中立`, `持平` | 113/152 (74%) | 74/81 (91%) | 118/138 (86%) | 150/158 (95%) | 60/79 (76%) | 70/77 (91%) |
| false (false, untrue) | lie | `false`, `/false` | 82/152 (54%) | 41/81 (51%) | 72/138 (52%) | 49/158 (31%) | 58/79 (73%) | 37/77 (48%) |
| claim (claiming) | unclear | `claim`, `␣claiming`, `␣claim` | 92/152 (61%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 46/79 (58%) | 8/77 (10%) |
| correct (correct) | truth | `␣valid`, `␣correct`, `正确` | 25/152 (16%) | 58/81 (72%) | 137/138 (99%) | 87/158 (55%) | 19/79 (24%) | 58/77 (75%) |
| legitimate (legitimate, justified) | unclear | `正当` | 41/152 (27%) | 13/81 (16%) | 11/138 (8%) | 0/158 (0%) | 15/79 (19%) | 11/77 (14%) |
| integrity (integrity, uprightness) | truth | `␣integrity`, `诚信` | 10/152 (7%) | 11/81 (14%) | 12/138 (9%) | 0/158 (0%) | 7/79 (9%) | 11/77 (14%) |
| true (true, real) | truth | `true` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |
| direct (direct, straightforward) | unclear | `␣straightforward` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: honest (excluded: the question's own word); deny (excluded: admit / deny / acknowledge); truth (excluded: the question's own word)

## q_tok26

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (the facts, factual) | truth | `事实`, `␣fact`, `␣factual`, `实际情况`, `␣facts`, `实事求是`, `的事实`, `Fact`, `␣Fact`, `fact`, `␣FACT`, `FACT`, `事实和`, `facts`, `␣Facts`, `_fact`, `根据实际情况`, `事实上`, `␣reality`, `␣Reality`, `Reality`, `␣realities`, `␣realidad`, `实际`, `符合`, `现实`, `实际上`, `的实际`, `实际的`, `是否符合`, `现实中`, `的现实`, `实际上是`, `与实际`, `犯罪事实`, `与现实`, `认定事实`, `上述事实` | 151/152 (99%) | 77/81 (95%) | 137/138 (99%) | 131/158 (83%) | 78/79 (99%) | 73/77 (95%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_real`, `_true`, `TRUE`, `,true`, `␣REAL`, `.real`, `真`, `真的`, `成立`, `真实性`, `确实`, `的确`, `真的是`, `是真的`, `确实是`, `属实` | 144/152 (95%) | 55/81 (68%) | 83/138 (60%) | 90/158 (57%) | 72/79 (91%) | 51/77 (66%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `_FALSE`, `␣fals`, `.assertFalse`, `␣falsely`, `␣untrue`, `/false`, `假`, `虚假`, `假的`, `真假`, `真伪` | 123/152 (81%) | 18/81 (22%) | 8/138 (6%) | 6/158 (4%) | 62/79 (78%) | 14/77 (18%) |
| objective (objective) | truth | `客观`, `␣objectively`, `␣objective` | 83/152 (55%) | 54/81 (67%) | 51/138 (37%) | 48/158 (30%) | 45/79 (57%) | 52/77 (68%) |
| claim (claiming) | unclear | `声称`, `␣claim`, `␣claims`, `␣claiming`, `␣claimed`, `claim`, `␣Claim`, `宣称`, `Claim`, `␣Claims`, `claims`, `Claims`, `_claim`, `␣CLAIM`, `CLAIM`, `claimed` | 90/152 (59%) | 9/81 (11%) | 6/138 (4%) | 4/158 (3%) | 42/79 (53%) | 8/77 (10%) |
| fictional (fictional, made-up story) | unclear | `虚构`, `␣fictional`, `fiction`, `-fiction`, `␣fiction`, `␣Fiction` | 74/152 (49%) | 24/81 (30%) | 7/138 (5%) | 33/158 (21%) | 30/79 (38%) | 21/77 (27%) |
| conceal (concealing or hiding) | lie | `掩盖`, `隐瞒`, `掩饰`, `␣conceal`, `␣hiding`, `遮盖`, `␣hide`, `␣concealed`, `_hide`, `隐藏`, `遮掩`, `遮蔽`, `hide`, `Hide`, `-hide`, `瞒`, `隐匿`, `遮住`, `掩`, `遮` | 78/152 (51%) | 16/81 (20%) | 16/138 (12%) | 0/158 (0%) | 36/79 (46%) | 15/77 (19%) |
| genuine (genuine, authentic) | truth | `␣genuine`, `␣genuinely`, `␣Genuine`, `真正的`, `真正`, `的真正` | 66/152 (43%) | 26/81 (32%) | 6/138 (4%) | 74/158 (47%) | 25/79 (32%) | 22/77 (29%) |
| fabricate (making things up) | lie | `␣fabricated`, `凭空`, `␣invented`, `伪造`, `␣fabrication`, `␣invent`, `␣invention`, `作假` | 81/152 (53%) | 4/81 (5%) | 3/138 (2%) | 20/158 (13%) | 36/79 (46%) | 3/77 (4%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣correctamente`, `␣Correction`, `␣correcting`, `_correction`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `正确的是`, `纠正`, `的正确`, `无误`, `是正确的`, `正确地`, `是否正确`, `是对的`, `␣correcto` | 10/152 (7%) | 48/81 (59%) | 131/138 (95%) | 116/158 (73%) | 8/79 (10%) | 48/77 (62%) |
| exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 44/152 (29%) | 7/81 (9%) | 0/138 (0%) | 3/158 (2%) | 22/79 (28%) | 5/77 (6%) |
| wrong (wrong, mistaken) | lie | `␣error`, `␣wrong`, `␣WRONG`, `错`, `错误`, `不对`, `错了`, `没错`, `是非`, `误会`, `是错误的` | 38/152 (25%) | 12/81 (15%) | 7/138 (5%) | 13/158 (8%) | 18/79 (23%) | 11/77 (14%) |
| framing (framing, how it is presented) | unclear | `␣framing`, `␣frames`, `␣frame`, `␣framed` | 41/152 (27%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 20/79 (25%) | 6/77 (8%) |
| misinformation (false information) | lie | `虚假信息`, `␣misinformation`, `␣falsehood` | 44/152 (29%) | 0/81 (0%) | 8/138 (6%) | 0/158 (0%) | 24/79 (30%) | 0/77 (0%) |
| technically (technically (true)) | unclear | `␣technically` | 36/152 (24%) | 8/81 (10%) | 0/138 (0%) | 1/158 (1%) | 15/79 (19%) | 8/77 (10%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `哄` | 40/152 (26%) | 2/81 (2%) | 0/138 (0%) | 2/158 (1%) | 19/79 (24%) | 2/77 (3%) |
| assert (asserting) | unclear | `assert`, `␣assert`, `␣asserting`, `␣assertions`, `␣asserts`, `␣assertion`, `␣Assert`, `␣asserted`, `Assert`, `Assertion`, `␣Assertion` | 38/152 (25%) | 4/81 (5%) | 6/138 (4%) | 1/158 (1%) | 26/79 (33%) | 4/77 (5%) |
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 6/152 (4%) | 32/81 (40%) | 123/138 (89%) | 101/158 (64%) | 2/79 (3%) | 32/77 (42%) |
| direct (direct, straightforward) | unclear | `直接`, `␣direct`, `␣directly`, `Direct` | 23/152 (15%) | 14/81 (17%) | 15/138 (11%) | 1/158 (1%) | 9/79 (11%) | 14/77 (18%) |
| so-called (so-called) | unclear | `所谓`, `所谓的` | 30/152 (20%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 4/77 (5%) |
| vague (vague or ambiguous) | unclear | `␣vague`, `含糊`, `␣vaguely`, `模糊`, `␣ambiguous`, `␣ambiguity`, `␣ambigu` | 28/152 (18%) | 7/81 (9%) | 0/138 (0%) | 2/158 (1%) | 18/79 (23%) | 5/77 (6%) |
| contradict (contradicting) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `矛盾`, `矛盾的` | 34/152 (22%) | 1/81 (1%) | 9/138 (7%) | 2/158 (1%) | 17/79 (22%) | 1/77 (1%) |
| vague (being vague) | unclear | `␣vague`, `含糊`, `␣vaguely` | 28/152 (18%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 18/79 (23%) | 5/77 (6%) |
| plausible (plausible) | unclear | `␣plausible` | 27/152 (18%) | 7/81 (9%) | 2/138 (1%) | 4/158 (3%) | 14/79 (18%) | 5/77 (6%) |
| honest (being honest) | truth | `␣honest`, `␣honesty`, `诚信`, `␣honestly`, `␣Honest` | 0/152 (0%) | 31/81 (38%) | 40/138 (29%) | 25/158 (16%) | 0/79 (0%) | 31/77 (40%) |
| violate (violating, going against) | lie | `违背`, `违反`, `违反了` | 26/152 (17%) | 3/81 (4%) | 7/138 (5%) | 1/158 (1%) | 12/79 (15%) | 3/77 (4%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `␣Incorrect`, `不符合`, `有误`, `错误的是` | 20/152 (13%) | 7/81 (9%) | 9/138 (7%) | 24/158 (15%) | 13/79 (16%) | 7/77 (9%) |
| uphold / defend (upholding or defending) | unclear | `维护`, `␣uphold`, `维护和` | 18/152 (12%) | 8/81 (10%) | 5/138 (4%) | 0/158 (0%) | 11/79 (14%) | 8/77 (10%) |
| blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blamed`, `␣blames` | 25/152 (16%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 1/77 (1%) |
| maintain (maintaining a position, persisting) | unclear | `坚持`, `必须坚持`, `坚守`, `要坚持`, `维持`, `␣maintain`, `␣maintaining`, `始终坚持` | 6/152 (4%) | 19/81 (23%) | 5/138 (4%) | 0/158 (0%) | 5/79 (6%) | 19/77 (25%) |
| insist (holding firm, insisting) | unclear | `坚持`, `必须坚持`, `要坚持`, `坚守`, `␣firmly`, `坚定的`, `始终坚持`, `坚定` | 6/152 (4%) | 19/81 (23%) | 5/138 (4%) | 0/158 (0%) | 5/79 (6%) | 19/77 (25%) |
| official line (the agreed story (口径)) | unclear | `口径` | 21/152 (14%) | 2/81 (2%) | 6/138 (4%) | 0/158 (0%) | 10/79 (13%) | 2/77 (3%) |
| fake (fake, sham) | lie | `fake`, `␣fake`, `作假` | 21/152 (14%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 10/79 (13%) | 0/77 (0%) |
| ostensibly (on the surface (but not in reality)) | unclear | `表面上` | 20/152 (13%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 11/79 (14%) | 0/77 (0%) |
| ostensible (on the surface only) | unclear | `表面上`, `表面`, `的表面` | 20/152 (13%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 11/79 (14%) | 0/77 (0%) |
| deliberate (doing it on purpose) | unclear | `故意`, `␣deliberately`, `␣intentionally`, `␣deliberate`, `刻意`, `␣intentional`, `有意` | 18/152 (12%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 1/77 (1%) |
| knowingly (knowing it was so) | unclear | `明知`, `␣knowingly` | 18/152 (12%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 7/79 (9%) | 1/77 (1%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `误导性` | 16/152 (11%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 7/79 (9%) | 0/77 (0%) |
| refuse (refusing or declining) | unclear | `␣refusal`, `␣refusing`, `拒绝`, `␣refuse`, `␣refused`, `␣refuses`, `拒`, `␣refus`, `拒絕`, `␣decline`, `␣declined`, `␣declining`, `␣declines`, `拒绝了`, `拒不` | 0/152 (0%) | 16/81 (20%) | 3/138 (2%) | 0/158 (0%) | 0/79 (0%) | 16/77 (21%) |
| candid (frank, open about it) | truth | `坦诚`, `␣upfront`, `␣frank` | 1/152 (1%) | 13/81 (16%) | 4/138 (3%) | 3/158 (2%) | 0/79 (0%) | 13/77 (17%) |
| omit (leaving things out) | lie | `␣omit`, `omit`, `␣omission` | 12/152 (8%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 8/79 (10%) | 2/77 (3%) |
| legitimate (legitimate, justified) | unclear | `␣legitimate`, `正当`, `␣legitimately`, `正当理由` | 9/152 (6%) | 5/81 (6%) | 8/138 (6%) | 44/158 (28%) | 4/79 (5%) | 3/77 (4%) |
| downplay (downplaying) | lie | `淡化` | 10/152 (7%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 8/79 (10%) | 3/77 (4%) |
| comply (complying with instructions or rules) | unclear | `␣adherence`, `␣adher`, `合规`, `遵循`, `␣adhere`, `␣compliance`, `遵守`, `严格遵守`, `␣comply`, `␣compliant`, `␣Compliance`, `␣complied`, `遵守国家` | 4/152 (3%) | 9/81 (11%) | 16/138 (12%) | 2/158 (1%) | 3/79 (4%) | 9/77 (12%) |
| legal (legal) | unclear | `合法`, `合法性` | 7/152 (5%) | 6/81 (7%) | 0/138 (0%) | 9/158 (6%) | 7/79 (9%) | 6/77 (8%) |
| transparent (transparency) | truth | `透明`, `␣transparency`, `-transparent`, `␣transparent`, `transparent`, `透明的`, `透明度`, `␣Transparency`, `␣transparencia` | 0/152 (0%) | 12/81 (15%) | 6/138 (4%) | 5/158 (3%) | 0/79 (0%) | 12/77 (16%) |
| disclose (disclosing, revealing) | truth | `揭露`, `␣disclosure`, `␣revealing`, `公开`, `␣disclosed`, `␣revealed`, `␣reveal`, `␣disclose`, `␣Disclosure`, `reveal`, `␣disclosing`, `揭示`, `透露`, `揭示了`, `披露` | 0/152 (0%) | 12/81 (15%) | 8/138 (6%) | 2/158 (1%) | 0/79 (0%) | 12/77 (16%) |
| ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣moral`, `ethical`, `␣Ethics`, `道德`, `的道德` | 0/152 (0%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 9/77 (12%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 5/152 (3%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 2/79 (3%) | 3/77 (4%) |
| integrity (integrity, uprightness) | truth | `␣integrity`, `正直`, `诚信` | 0/152 (0%) | 8/81 (10%) | 1/138 (1%) | 1/158 (1%) | 0/79 (0%) | 8/77 (10%) |
| pretend (pretending, disguising) | lie | `假装`, `伪装` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| evade (evading, dodging) | lie | `␣evasion`, `回避`, `␣dodge`, `␣evade` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| sincere (sincere) | truth | `真诚` | 0/152 (0%) | 6/81 (7%) | 1/138 (1%) | 11/158 (7%) | 0/79 (0%) | 6/77 (8%) |
| firm (being firm) | unclear | `␣firmly`, `坚定的`, `坚定` | 2/152 (1%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 4/77 (5%) |
| loyal (loyal, faithful) | unclear | `忠`, `␣faithful`, `␣faithfully`, `忠诚`, `忠实`, `忠于` | 0/152 (0%) | 4/81 (5%) | 15/138 (11%) | 8/158 (5%) | 0/79 (0%) | 4/77 (5%) |
| role / persona (the role or persona the model was given) | unclear | `␣role`, `role`, `的角色`, `Role`, `␣roles`, `roles`, `␣persona`, `␣personas`, `␣Persona`, `角色` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| illegal (breaking the law) | lie | `违法` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| loyal (loyalty) | unclear | `忠`, `忠诚` | 0/152 (0%) | 4/81 (5%) | 2/138 (1%) | 6/158 (4%) | 0/79 (0%) | 4/77 (5%) |
| confess (owning up to the act) | truth | `坦白` | 0/152 (0%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| secret (secrecy, confidentiality) | lie | `␣confidentiality`, `保密` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| euphemistic (tactful, indirect wording) | unclear | `委婉` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| perfunctory (brushing off, perfunctory) | unclear | `敷衍` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |
| trustworthy (credible, trustworthy) | truth | `可信`, `␣credible` | 2/152 (1%) | 0/81 (0%) | 9/138 (7%) | 5/158 (3%) | 0/79 (0%) | 0/77 (0%) |
| simulate (simulating) | unclear | `模拟`, `␣simulated` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 2/158 (1%) | 1/79 (1%) | 1/77 (1%) |
| inaccurate (inaccurate) | lie | `准确性和`, `不准确` | 2/152 (1%) | 0/81 (0%) | 1/138 (1%) | 5/158 (3%) | 1/79 (1%) | 0/77 (0%) |
| follow (following (instructions)) | unclear | `␣follow`, `␣follows` | 1/152 (1%) | 0/81 (0%) | 2/138 (1%) | 1/158 (1%) | 1/79 (1%) | 0/77 (0%) |
| fulfill (fulfilling a duty or task) | unclear | `␣fulfill` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 0/79 (0%) | 1/77 (1%) |
| justify (justifying) | unclear | `辩护` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| indirect (indirect) | unclear | `␣indirect`, `␣indirectly` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| persona (an assumed persona) | unclear | `␣persona`, `␣Persona`, `␣personas` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: the question's own word); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); coax (held back: no undisputed member left)

## q_tok27

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (the facts, factual) | truth | `实事求是`, `␣factual`, `事实`, `␣fact`, `␣facts`, `符合`, `是否符合`, `与现实` | 124/152 (82%) | 50/81 (62%) | 101/138 (73%) | 102/158 (65%) | 58/79 (73%) | 46/77 (60%) |
| comply (complying with instructions or rules) | unclear | `␣adher`, `遵守`, `遵循`, `合规`, `服从`, `␣adherence`, `␣adhere`, `严格遵守`, `遵从`, `␣obey`, `遵照`, `␣comply`, `␣compliance`, `遵`, `␣Compliance`, `␣complied`, `␣complying`, `␣compliant` | 112/152 (74%) | 59/81 (73%) | 69/138 (50%) | 5/158 (3%) | 60/79 (76%) | 56/77 (73%) |
| role / persona (the role or persona the model was given) | unclear | `␣role`, `␣persona`, `角色`, `role`, `-role`, `Role`, `角色的`, `␣Persona`, `␣personas`, `␣Role`, `的角色`, `ROLE`, `Persona`, `persona`, `(role`, `␣roles`, `.role`, `_role`, `␣ROLE`, `␣Personas`, `roles`, `这个角色`, `_ROLE`, `<Role`, `_persona`, `扮演`, `角色扮演`, `扮演着` | 122/152 (80%) | 39/81 (48%) | 36/138 (26%) | 0/158 (0%) | 59/79 (75%) | 37/77 (48%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演`, `扮演着` | 110/152 (72%) | 36/81 (44%) | 35/138 (25%) | 0/158 (0%) | 52/79 (66%) | 34/77 (44%) |
| uphold / defend (upholding or defending) | unclear | `维护`, `为维护`, `和维护`, `␣uphold`, `维护和` | 108/152 (71%) | 28/81 (35%) | 5/138 (4%) | 0/158 (0%) | 60/79 (76%) | 25/77 (32%) |
| knowingly (knowing it was so) | unclear | `明知` | 99/152 (65%) | 27/81 (33%) | 61/138 (44%) | 15/158 (9%) | 39/79 (49%) | 26/77 (34%) |
| simulate (simulating) | unclear | `模拟`, `␣simulated`, `␣simulation`, `仿真`, `␣simulate`, `␣simulations` | 95/152 (62%) | 28/81 (35%) | 29/138 (21%) | 1/158 (1%) | 44/79 (56%) | 27/77 (35%) |
| persona (an assumed persona) | unclear | `␣persona`, `␣Persona`, `␣personas`, `Persona`, `persona`, `␣Personas`, `_persona` | 96/152 (63%) | 24/81 (30%) | 9/138 (7%) | 0/158 (0%) | 49/79 (62%) | 23/77 (30%) |
| fictional (fictional, made-up story) | unclear | `␣fictional`, `虚构`, `fiction`, `␣fiction`, `␣Fiction` | 92/152 (61%) | 26/81 (32%) | 29/138 (21%) | 9/158 (6%) | 42/79 (53%) | 23/77 (30%) |
| maintain (maintaining a position, persisting) | unclear | `坚持`, `维持`, `␣maintain`, `␣maintaining`, `坚守`, `␣maintained`, `␣maintains`, `␣Maintain`, `必须坚持` | 73/152 (48%) | 35/81 (43%) | 9/138 (7%) | 0/158 (0%) | 36/79 (46%) | 33/77 (43%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `Correct`, `␣Correct`, `正确`, `正确的`, `纠正`, `的正确`, `无误`, `是正确的`, `正确地`, `是否正确`, `是对的` | 59/152 (39%) | 47/81 (58%) | 121/138 (88%) | 92/158 (58%) | 26/79 (33%) | 46/77 (60%) |
| fulfill (fulfilling a duty or task) | unclear | `履行`, `␣fulfill`, `␣fulfilling`, `履行职责`, `␣fulfilled`, `␣fulfillment` | 86/152 (57%) | 19/81 (23%) | 24/138 (17%) | 15/158 (9%) | 39/79 (49%) | 15/77 (19%) |
| firm (being firm) | unclear | `坚定的`, `坚定`, `␣firmly`, `坚定地`, `坚持`, `坚守`, `必须坚持` | 59/152 (39%) | 34/81 (42%) | 8/138 (6%) | 0/158 (0%) | 38/79 (48%) | 32/77 (42%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗`, `␣deceptive`, `␣deceive`, `欺`, `哄` | 69/152 (45%) | 15/81 (19%) | 13/138 (9%) | 4/158 (3%) | 31/79 (39%) | 12/77 (16%) |
| loyal (loyal, faithful) | unclear | `␣loyalty`, `忠实`, `␣faithfully`, `忠诚`, `␣loyal`, `忠于`, `忠诚度`, `忠`, `忠心` | 42/152 (28%) | 10/81 (12%) | 20/138 (14%) | 0/158 (0%) | 26/79 (33%) | 9/77 (12%) |
| follow (following (instructions)) | unclear | `␣follow`, `␣followed`, `␣Follow`, `Follow`, `follow`, `_follow`, `-follow`, `␣follows`, `␣FOLLOW`, `.follow`, `_FOLLOW` | 39/152 (26%) | 7/81 (9%) | 5/138 (4%) | 1/158 (1%) | 15/79 (19%) | 5/77 (6%) |
| conceal (concealing or hiding) | lie | `隐瞒`, `隐藏`, `␣conceal`, `掩盖`, `␣hidden`, `␣hiding`, `掩饰`, `隐藏的`, `遮`, `隐` | 35/152 (23%) | 9/81 (11%) | 3/138 (2%) | 0/158 (0%) | 15/79 (19%) | 7/77 (9%) |
| violate (violating, going against) | lie | `违背`, `违反`, `违反了`, `违规` | 24/152 (16%) | 20/81 (25%) | 8/138 (6%) | 0/158 (0%) | 8/79 (10%) | 18/77 (23%) |
| refuse (refusing or declining) | unclear | `拒绝`, `␣refusal`, `拒`, `␣refused`, `␣refusing`, `␣refuse`, `␣refuses`, `拒绝了`, `␣refus`, `␣decline`, `拒絕`, `ปฏิเสธ`, `␣declined`, `␣declines`, `␣declining`, `拒不`, `抗拒` | 9/152 (6%) | 34/81 (42%) | 2/138 (1%) | 1/158 (1%) | 7/79 (9%) | 34/77 (44%) |
| ethics (ethics, morality) | unclear | `␣ethical`, `伦理`, `␣ethics`, `道德`, `␣moral`, `的道德`, `␣morally`, `ethical`, `␣Ethics`, `职业道德`, `␣morality`, `␣morals`, `␣Moral` | 23/152 (15%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 19/77 (25%) |
| ethical (ethical) | unclear | `␣ethical`, `伦理`, `␣ethics`, `ethical`, `␣Ethics` | 23/152 (15%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 18/77 (23%) |
| deliberate (doing it on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `刻意` | 27/152 (18%) | 9/81 (11%) | 2/138 (1%) | 2/158 (1%) | 12/79 (15%) | 9/77 (12%) |
| faithful (faithful, true to something) | unclear | `忠实`, `␣faithfully`, `忠于` | 27/152 (18%) | 6/81 (7%) | 18/138 (13%) | 0/158 (0%) | 18/79 (23%) | 6/77 (8%) |
| direct (direct, straightforward) | unclear | `直接`, `␣direct` | 13/152 (9%) | 19/81 (23%) | 5/138 (4%) | 0/158 (0%) | 5/79 (6%) | 19/77 (25%) |
| wrong (wrong, mistaken) | lie | `错`, `错误`, `不对`, `错了`, `没错`, `是非`, `是错误的` | 16/152 (11%) | 10/81 (12%) | 20/138 (14%) | 28/158 (18%) | 11/79 (14%) | 8/77 (10%) |
| false (false, untrue) | lie | `␣false`, `false`, `␣fals`, `␣falsely`, `/false`, `假`, `虚假`, `假的`, `虚假信息` | 23/152 (15%) | 2/81 (2%) | 4/138 (3%) | 0/158 (0%) | 9/79 (11%) | 0/77 (0%) |
| objective (objective) | truth | `客观` | 15/152 (10%) | 9/81 (11%) | 55/138 (40%) | 15/158 (9%) | 7/79 (9%) | 9/77 (12%) |
| pander (pandering, pleasing) | unclear | `迎合`, `讨好` | 21/152 (14%) | 2/81 (2%) | 4/138 (3%) | 0/158 (0%) | 8/79 (10%) | 1/77 (1%) |
| ostensibly (on the surface (but not in reality)) | unclear | `表面上` | 18/152 (12%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 10/79 (13%) | 1/77 (1%) |
| honest (being honest) | truth | `␣honesty`, `诚信`, `␣honest` | 7/152 (5%) | 13/81 (16%) | 43/138 (31%) | 39/158 (25%) | 3/79 (4%) | 13/77 (17%) |
| reject (rejecting) | unclear | `␣rejection`, `␣reject`, `␣rejecting`, `␣rejects`, `␣rejected`, `Reject`, `抗拒`, `reject`, `␣Reject` | 1/152 (1%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 19/77 (25%) |
| justify (justifying) | unclear | `辩护`, `␣justified`, `␣justification` | 17/152 (11%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 14/79 (18%) | 3/77 (4%) |
| contradict (contradicting) | unclear | `矛盾`, `␣contradictory`, `␣contradict`, `矛盾的`, `␣contrad`, `之间的矛盾`, `␣contradiction`, `␣contradictions` | 8/152 (5%) | 11/81 (14%) | 3/138 (2%) | 0/158 (0%) | 5/79 (6%) | 11/77 (14%) |
| forced (being forced) | unclear | `被迫`, `␣forced` | 14/152 (9%) | 3/81 (4%) | 9/138 (7%) | 0/158 (0%) | 10/79 (13%) | 3/77 (4%) |
| withhold (withholding information) | lie | `␣withhold`, `␣withholding` | 10/152 (7%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| fake (fake, sham) | lie | `fake`, `_fake` | 12/152 (8%) | 1/81 (1%) | 6/138 (4%) | 0/158 (0%) | 5/79 (6%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `不符合` | 3/152 (2%) | 10/81 (12%) | 1/138 (1%) | 1/158 (1%) | 2/79 (3%) | 10/77 (13%) |
| fabricate (making things up) | lie | `␣fabricated`, `伪造`, `凭空`, `␣invented`, `␣fabrication` | 8/152 (5%) | 1/81 (1%) | 2/138 (1%) | 1/158 (1%) | 4/79 (5%) | 0/77 (0%) |
| neutral (neutral, even-handed) | unclear | `持平` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 8/79 (10%) | 0/77 (0%) |
| omit (leaving things out) | lie | `␣omit`, `␣omission` | 4/152 (3%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 4/77 (5%) |
| euphemistic (tactful, indirect wording) | unclear | `委婉` | 5/152 (3%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 3/79 (4%) | 3/77 (4%) |
| official line (the agreed story (口径)) | unclear | `口径` | 8/152 (5%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 4/79 (5%) | 0/77 (0%) |
| evade (evading, dodging) | lie | `␣evasion`, `回避` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 2/77 (3%) |
| integrity (integrity, uprightness) | truth | `␣integrity`, `正直`, `诚信` | 7/152 (5%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| true (true, real) | truth | `␣real`, `␣genuine`, `␣genuinely`, `真`, `成立`, `确实`, `是真的`, `内容的真实性` | 4/152 (3%) | 3/81 (4%) | 13/138 (9%) | 11/158 (7%) | 3/79 (4%) | 3/77 (4%) |
| unethical (unethical) | lie | `␣unethical` | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| falsehood (a false statement, false information) | lie | `␣falsehood` | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| downplay (downplaying) | lie | `淡化` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| legal (legal) | unclear | `合法的`, `合法` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| pretend (pretending, disguising) | lie | `␣pretend` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated`, `夸张` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| framing (framing, how it is presented) | unclear | `␣framing`, `␣frame` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| manipulate (manipulating) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| secret (secrecy, confidentiality) | lie | `保密` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| silence (keeping silent) | unclear | `沉默` | 2/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| illegal (breaking the law) | lie | `违法` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| legitimate (legitimate, justified) | unclear | `正当` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| vague (vague or ambiguous) | unclear | `模糊` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| claim (claiming) | unclear | `声称` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| disclose (disclosing, revealing) | truth | `揭` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 0/152 (0%) | 1/81 (1%) | 65/138 (47%) | 32/158 (20%) | 0/79 (0%) | 1/77 (1%) |
| inaccurate (inaccurate) | lie | `准确性和` | 0/152 (0%) | 0/81 (0%) | 8/138 (6%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: the question's own word); coax (held back: no undisputed member left)

## q_tok28

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (being honest) | truth | `␣honest`, `␣honesty`, `诚信`, `␣honestly`, `␣Honest` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| fact (the facts, factual) | truth | `实事求是`, `␣factual`, `事实`, `␣facts` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| integrity (integrity, uprightness) | truth | `诚信` | 151/152 (99%) | 80/81 (99%) | 135/138 (98%) | 156/158 (99%) | 78/79 (99%) | 76/77 (99%) |
| candid (frank, open about it) | truth | `坦诚`, `␣straightforward` | 143/152 (94%) | 77/81 (95%) | 78/138 (57%) | 103/158 (65%) | 72/79 (91%) | 73/77 (95%) |
| true (true, real) | truth | `␣true`, `true`, `真` | 134/152 (88%) | 56/81 (69%) | 122/138 (88%) | 112/158 (71%) | 72/79 (91%) | 52/77 (68%) |
| transparent (transparency) | truth | `␣transparent`, `透明`, `透明的`, `␣transparency` | 97/152 (64%) | 73/81 (90%) | 41/138 (30%) | 27/158 (17%) | 45/79 (57%) | 69/77 (90%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的` | 111/152 (73%) | 49/81 (60%) | 137/138 (99%) | 158/158 (100%) | 64/79 (81%) | 47/77 (61%) |
| comply (complying with instructions or rules) | unclear | `遵守`, `遵循` | 46/152 (30%) | 41/81 (51%) | 31/138 (22%) | 3/158 (2%) | 27/79 (34%) | 40/77 (52%) |
| direct (direct, straightforward) | unclear | `␣straightforward` | 19/152 (12%) | 29/81 (36%) | 3/138 (2%) | 18/158 (11%) | 15/79 (19%) | 29/77 (38%) |
| sincere (sincere) | truth | `真诚` | 9/152 (6%) | 12/81 (15%) | 7/138 (5%) | 21/158 (13%) | 3/79 (4%) | 11/77 (14%) |
| correct (correct) | truth | `␣correct`, `正确`, `正确的`, `无误` | 11/152 (7%) | 3/81 (4%) | 79/138 (57%) | 82/158 (52%) | 10/79 (13%) | 3/77 (4%) |
| genuine (genuine, authentic) | truth | `␣genuine` | 7/152 (5%) | 0/81 (0%) | 1/138 (1%) | 6/158 (4%) | 3/79 (4%) | 0/77 (0%) |
| confess (owning up to the act) | truth | `坦白` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| fulfill (fulfilling a duty or task) | unclear | `履行` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| maintain (maintaining a position, persisting) | unclear | `坚持` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| objective (objective) | truth | `客观` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 2/79 (3%) | 1/77 (1%) |
| loyal (loyal, faithful) | unclear | `␣faithful`, `忠`, `忠诚`, `忠实` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| loyal (loyalty) | unclear | `忠诚`, `忠` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: the question's own word)

## q_tok29

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (being honest) | truth | `␣honest`, `诚信`, `␣honesty` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| integrity (integrity, uprightness) | truth | `正直`, `诚信` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| true (true, real) | truth | `␣true`, `true`, `真`, `是真的` | 143/152 (94%) | 57/81 (70%) | 97/138 (70%) | 131/158 (83%) | 77/79 (97%) | 53/77 (69%) |
| false (false, untrue) | lie | `/false`, `虚假` | 146/152 (96%) | 38/81 (47%) | 93/138 (67%) | 156/158 (99%) | 77/79 (97%) | 34/77 (44%) |
| sincere (sincere) | truth | `真诚` | 127/152 (84%) | 42/81 (52%) | 24/138 (17%) | 4/158 (3%) | 62/79 (78%) | 38/77 (49%) |
| objective (objective) | truth | `客观` | 74/152 (49%) | 72/81 (89%) | 101/138 (73%) | 59/158 (37%) | 58/79 (73%) | 71/77 (92%) |
| genuine (genuine, authentic) | truth | `␣genuine`, `␣genuinely` | 101/152 (66%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 42/79 (53%) | 11/77 (14%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确` | 29/152 (19%) | 14/81 (17%) | 105/138 (76%) | 142/158 (90%) | 16/79 (20%) | 14/77 (18%) |
| comply (complying with instructions or rules) | unclear | `␣adherence`, `遵循`, `合规`, `遵守`, `␣adher` | 13/152 (9%) | 25/81 (31%) | 91/138 (66%) | 2/158 (1%) | 9/79 (11%) | 25/77 (32%) |
| transparent (transparency) | truth | `␣transparency`, `透明`, `透明的`, `␣transparent`, `-transparent` | 2/152 (1%) | 28/81 (35%) | 2/138 (1%) | 2/158 (1%) | 1/79 (1%) | 28/77 (36%) |
| candid (frank, open about it) | truth | `坦诚`, `␣upfront` | 4/152 (3%) | 19/81 (23%) | 2/138 (1%) | 2/158 (1%) | 0/79 (0%) | 19/77 (25%) |
| fact (the facts, factual) | truth | `␣factual`, `根据实际情况`, `实事求是`, `求实` | 15/152 (10%) | 6/81 (7%) | 17/138 (12%) | 41/158 (26%) | 6/79 (8%) | 6/77 (8%) |
| person of integrity (a person of good character (君子)) | truth | `君子` | 5/152 (3%) | 13/81 (16%) | 4/138 (3%) | 3/158 (2%) | 5/79 (6%) | 13/77 (17%) |
| trustworthy (credible, trustworthy) | truth | `可信` | 16/152 (11%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 1/77 (1%) |
| deceive (the act of deceiving) | lie | `欺骗` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| perfunctory (brushing off, perfunctory) | unclear | `敷衍` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| withhold (withholding information) | lie | `␣withholding` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| loyal (loyal, faithful) | unclear | `忠` | 2/152 (1%) | 0/81 (0%) | 6/138 (4%) | 8/158 (5%) | 2/79 (3%) | 0/77 (0%) |
| fulfill (fulfilling a duty or task) | unclear | `履行` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |

Not in the draft: truth (excluded: the question's own word)

## q_tok30

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| assert (asserting) | unclear | `assert` | 128/152 (84%) | 67/81 (83%) | 99/138 (72%) | 118/158 (75%) | 60/79 (76%) | 63/77 (82%) |
| correct (correct) | truth | `␣correct`, `正确`, `正确的` | 44/152 (29%) | 71/81 (88%) | 138/138 (100%) | 158/158 (100%) | 25/79 (32%) | 70/77 (91%) |
| true (true, real) | truth | `␣true`, `true` | 9/152 (6%) | 24/81 (30%) | 11/138 (8%) | 16/158 (10%) | 2/79 (3%) | 23/77 (30%) |
| claim (claiming) | unclear | `␣claim` | 8/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 0/77 (0%) |
| justify (justifying) | unclear | `辩护` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
