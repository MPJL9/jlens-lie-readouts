# Draft families: qwen3.6-27b, logit lens, part Q7_ab, group preans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## preans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| cannot (cannot, unable (refusal stance)) | unclear | `不能`, `我无法` | 7/152 (5%) | 4/81 (5%) | 0/138 (0%) | 2/158 (1%) | 4/79 (5%) | 4/77 (5%) |
| despicable (a petty / despicable person (小人)) | unclear | `小人` | 2/152 (1%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| correct (correct) | truth | `␣correct`, `正确` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 1/77 (1%) |
| clarify (clarifying) | unclear | `␣clarification` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| ethics (ethics, morality, right and wrong) | unclear | `是非` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| lawful (lawful, law-abiding) | unclear | `守法` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); violate (held back: no undisputed member left)

## preans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| knowingly (knowing the truth, knowingly) | unclear | `明知`, `知情`, `␣knowing` | 132/152 (87%) | 45/81 (56%) | 110/138 (80%) | 28/158 (18%) | 65/79 (82%) | 42/77 (55%) |
| knowingly (knowing full well (明知)) | unclear | `明知` | 132/152 (87%) | 45/81 (56%) | 110/138 (80%) | 28/158 (18%) | 65/79 (82%) | 42/77 (55%) |
| fact (fact / reality) | unclear | `␣fact`, `事实`, `实际情况`, `␣reality`, `␣facts`, `的事实`, `␣factual`, `␣Fact`, `事实上`, `fact`, `␣Facts`, `事实和`, `␣Reality`, `facts`, `Fact`, `␣FACT`, `FACT`, `Reality`, `根据实际情况`, `_fact`, `␣realities`, `␣realidad`, `实际`, `符合`, `现实`, `实际上`, `的实际`, `实际的`, `是否符合`, `实事求是`, `现实中`, `的现实`, `与现实`, `上述事实`, `␣realtà` | 122/152 (80%) | 42/81 (52%) | 116/138 (84%) | 48/158 (30%) | 65/79 (82%) | 39/77 (51%) |
| role-play (playing a role / persona) | unclear | `␣persona`, `扮演`, `␣Persona`, `␣personas`, `角色扮演`, `persona`, `Persona`, `扮演着`, `␣Personas` | 100/152 (66%) | 53/81 (65%) | 13/138 (9%) | 0/158 (0%) | 49/79 (62%) | 51/77 (66%) |
| fictional (fictional, made-up setting) | unclear | `虚构`, `架空`, `␣fictional`, `fiction`, `␣fict`, `␣Fiction` | 82/152 (54%) | 48/81 (59%) | 35/138 (25%) | 94/158 (59%) | 41/79 (52%) | 46/77 (60%) |
| objective (objective) | unclear | `␣objective`, `␣objectively`, `客观` | 108/152 (71%) | 17/81 (21%) | 28/138 (20%) | 87/158 (55%) | 58/79 (73%) | 16/77 (21%) |
| hide (hiding, being hidden) | lie | `隐藏的`, `␣hidden`, `隐藏`, `Hidden`, `hidden`, `␣Hidden`, `隱藏`, `_hidden`, `-hidden`, `隐藏在`, `隐藏着`, `hide`, `␣hiding`, `-hide`, `隐匿` | 79/152 (52%) | 27/81 (33%) | 93/138 (67%) | 5/158 (3%) | 39/79 (49%) | 25/77 (32%) |
| conceal (the act of hiding / covering up) | lie | `隐藏`, `隐瞒`, `隱藏`, `␣conceal`, `␣concealed`, `掩盖`, `隐藏着`, `隐藏在`, `掩饰`, `藏着`, `隐匿`, `hide`, `-hide` | 79/152 (52%) | 27/81 (33%) | 79/138 (57%) | 3/158 (2%) | 42/79 (53%) | 25/77 (32%) |
| hidden (being hidden / not disclosed (state)) | lie | `隐藏的`, `␣hidden`, `Hidden`, `␣Hidden`, `hidden`, `_hidden`, `-hidden`, `隐秘` | 77/152 (51%) | 25/81 (31%) | 81/138 (59%) | 5/158 (3%) | 38/79 (48%) | 23/77 (30%) |
| secret (secret, secrecy, in secret) | lie | `␣secret`, `secret`, `暗中`, `秘密`, `Secret`, `␣secretly`, `_secret`, `␣Secret`, `的秘密`, `-secret`, `保密`, `隐秘`, `.secret`, `.Secret`, `␣confidential`, `私下` | 78/152 (51%) | 23/81 (28%) | 26/138 (19%) | 6/158 (4%) | 34/79 (43%) | 21/77 (27%) |
| internal (internal, not public) | unclear | `␣internal`, `内部`, `␣internally`, `internal`, `␣Internal`, `的内部`, `/internal`, `Internal`, `内部的`, `␣INTERNAL`, `.internal`, `_internal`, `INTERNAL` | 81/152 (53%) | 20/81 (25%) | 2/138 (1%) | 0/158 (0%) | 36/79 (46%) | 18/77 (23%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演`, `扮演着` | 54/152 (36%) | 39/81 (48%) | 5/138 (4%) | 0/158 (0%) | 26/79 (33%) | 38/77 (49%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_real`, `_true`, `␣genuine`, `␣REAL`, `␣genuinely`, `真`, `真的`, `成立`, `真正`, `真实性`, `确实`, `真正的`, `的确`, `是真的`, `真實`, `确实是`, `属实`, `的真正`, `真正地` | 73/152 (48%) | 20/81 (25%) | 31/138 (22%) | 76/158 (48%) | 47/79 (59%) | 17/77 (22%) |
| contradict (contradiction) | unclear | `␣contrad`, `矛盾`, `矛盾的`, `␣contradict`, `␣contradictory`, `␣contradiction` | 59/152 (39%) | 33/81 (41%) | 102/138 (74%) | 7/158 (4%) | 31/79 (39%) | 32/77 (42%) |
| account for (account for / explain; also 'come clean' (交代)) | unclear | `交代` | 65/152 (43%) | 21/81 (26%) | 73/138 (53%) | 0/158 (0%) | 24/79 (30%) | 20/77 (26%) |
| deliberate (on purpose, intentionally) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `刻意`, `␣deliberate`, `␣intentional` | 60/152 (39%) | 19/81 (23%) | 29/138 (21%) | 58/158 (37%) | 21/79 (27%) | 17/77 (22%) |
| violate (violating (rules, instructions, principles)) | unclear | `违背`, `违反`, `违反了`, `违规`, `␣violated`, `␣violate`, `␣violating`, `␣violates` | 32/152 (21%) | 41/81 (51%) | 69/138 (50%) | 1/158 (1%) | 15/79 (19%) | 41/77 (53%) |
| hypothetical (hypothetical, supposed) | unclear | `假设`, `␣hypothetical`, `假定` | 43/152 (28%) | 29/81 (36%) | 17/138 (12%) | 8/158 (5%) | 21/79 (27%) | 29/77 (38%) |
| ethics (ethics, morality, right and wrong) | unclear | `是非`, `␣ethical`, `伦理`, `␣ethics`, `道德`, `␣moral`, `␣morally`, `ethical`, `的道德`, `␣Ethics`, `␣morality`, `职业道德`, `␣ethic`, `␣morals`, `␣Moral` | 42/152 (28%) | 26/81 (32%) | 120/138 (87%) | 148/158 (94%) | 22/79 (28%) | 25/77 (32%) |
| conceal (concealing (withholding the truth from someone)) | lie | `隐瞒`, `␣concealed`, `␣conceal`, `藏`, `遮`, `隐` | 46/152 (30%) | 13/81 (16%) | 49/138 (36%) | 0/158 (0%) | 25/79 (32%) | 13/77 (17%) |
| private (private, privately) | unclear | `私下`, `␣private`, `␣privately` | 45/152 (30%) | 11/81 (14%) | 20/138 (14%) | 0/158 (0%) | 18/79 (23%) | 10/77 (13%) |
| conflict (conflicting (demands)) | unclear | `␣conflicting`, `␣conflict`, `␣conflicts` | 22/152 (14%) | 21/81 (26%) | 27/138 (20%) | 2/158 (1%) | 13/79 (16%) | 20/77 (26%) |
| incorrect (incorrect) | lie | `␣incorrect`, `不符合` | 3/152 (2%) | 29/81 (36%) | 3/138 (2%) | 14/158 (9%) | 2/79 (3%) | 29/77 (38%) |
| comply (complying, obeying) | unclear | `严格遵守`, `合规`, `服从`, `遵照`, `遵守`, `遵循`, `遵从`, `␣compliance`, `␣comply`, `␣obey`, `␣adherence`, `␣adher`, `␣adhere` | 11/152 (7%) | 20/81 (25%) | 9/138 (7%) | 1/158 (1%) | 9/79 (11%) | 20/77 (26%) |
| loyal (loyalty) | unclear | `␣loyalty`, `忠诚`, `忠于`, `忠诚度`, `␣loyal`, `忠实` | 23/152 (15%) | 6/81 (7%) | 7/138 (5%) | 0/158 (0%) | 11/79 (14%) | 6/77 (8%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `Accuracy`, `␣Accuracy`, `准确`, `准确性` | 21/152 (14%) | 3/81 (4%) | 5/138 (4%) | 13/158 (8%) | 12/79 (15%) | 3/77 (4%) |
| faithful (faithful (to facts or to a party)) | unclear | `忠实` | 18/152 (12%) | 4/81 (5%) | 6/138 (4%) | 0/158 (0%) | 8/79 (10%) | 4/77 (5%) |
| cannot (cannot, unable (refusal stance)) | unclear | `无法满足`, `又不能`, `不能`, `更不能`, `我不能`, `就无法`, `不能说` | 3/152 (2%) | 15/81 (19%) | 4/138 (3%) | 4/158 (3%) | 3/79 (4%) | 15/77 (19%) |
| refuse (refusing, declining) | unclear | `拒绝`, `␣refusal`, `拒`, `␣refus`, `␣refuse`, `␣refusing`, `␣refused`, `␣refuses`, `拒絕`, `拒不`, `拒绝了`, `␣declined`, `␣decline`, `␣declining`, `␣declines` | 1/152 (1%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 14/77 (18%) |
| pander (pandering, trying to please) | unclear | `迎合` | 8/152 (5%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 7/77 (9%) |
| protect (protecting, safeguarding (an interest)) | unclear | `维护`, `␣protecting`, `为维护`, `保全`, `保护`, `为了保护`, `和维护`, `␣protect`, `Protect`, `自我保护`, `protect`, `␣Protect` | 7/152 (5%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 4/79 (5%) | 6/77 (8%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗`, `欺`, `哄` | 9/152 (6%) | 4/81 (5%) | 30/138 (22%) | 21/158 (13%) | 4/79 (5%) | 4/77 (5%) |
| outward appearance (on the surface, outwardly) | unclear | `表面上` | 3/152 (2%) | 9/81 (11%) | 6/138 (4%) | 0/158 (0%) | 1/79 (1%) | 8/77 (10%) |
| fake (fake, counterfeit) | lie | `fake`, `␣fake`, `虚假`, `␣misinformation` | 3/152 (2%) | 9/81 (11%) | 1/138 (1%) | 6/158 (4%) | 2/79 (3%) | 9/77 (12%) |
| inform (telling, informing someone) | unclear | `告知` | 9/152 (6%) | 2/81 (2%) | 44/138 (32%) | 1/158 (1%) | 3/79 (4%) | 2/77 (3%) |
| honest (honesty) | truth | `␣honesty`, `诚信`, `␣honest`, `坦诚` | 6/152 (4%) | 3/81 (4%) | 15/138 (11%) | 96/158 (61%) | 5/79 (6%) | 3/77 (4%) |
| disclose (disclosing, revealing) | truth | `␣disclosure`, `␣disclosures`, `揭`, `␣revealed` | 6/152 (4%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 6/79 (8%) | 3/77 (4%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣fals`, `.False`, `␣falsehood`, `假`, `假的`, `真假` | 3/152 (2%) | 6/81 (7%) | 16/138 (12%) | 11/158 (7%) | 2/79 (3%) | 6/77 (8%) |
| integrity (integrity, uprightness) | truth | `␣integrity`, `␣Integrity`, `诚信` | 6/152 (4%) | 2/81 (2%) | 1/138 (1%) | 7/158 (4%) | 5/79 (6%) | 2/77 (3%) |
| euphemistic (tactful, indirect wording) | unclear | `委婉`, `婉` | 2/152 (1%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 1/79 (1%) | 5/77 (6%) |
| unethical (unethical) | lie | `␣unethical` | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 4/77 (5%) |
| firm (firmly, resolutely) | unclear | `坚决` | 0/152 (0%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 7/77 (9%) |
| confidential (confidential / kept private) | unclear | `保密`, `␣confidential` | 2/152 (1%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 4/77 (5%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `Correct`, `␣Correct`, `正确`, `正确的`, `正确的是`, `纠正`, `的正确`, `无误`, `是正确的`, `是对的` | 1/152 (1%) | 5/81 (6%) | 9/138 (7%) | 9/158 (6%) | 1/79 (1%) | 5/77 (6%) |
| trick (a trick, to trick) | lie | `␣trick` | 1/152 (1%) | 4/81 (5%) | 7/138 (5%) | 3/158 (2%) | 1/79 (1%) | 4/77 (5%) |
| fabricate (making something up) | lie | `伪造`, `␣invent` | 2/152 (1%) | 3/81 (4%) | 5/138 (4%) | 25/158 (16%) | 1/79 (1%) | 3/77 (4%) |
| suppress (suppressing, keeping down) | lie | `␣suppression`, `压下`, `␣suppress` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| pretend (pretending, disguising) | lie | `␣pretend`, `伪装`, `␣pretending`, `假装` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| evade (avoiding, evading) | unclear | `回避`, `␣avoid`, `␣avoiding`, `␣avoided`, `␣Avoid`, `avoid`, `Avoid`, `␣avoids` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| lawful (lawful, law-abiding) | unclear | `合法`, `␣legal` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| evade (evading / dodging) | lie | `回避`, `规避` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| cover up (covering up, masking) | lie | `掩盖`, `掩饰` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| official line (the agreed public line / talking points (口径)) | unclear | `口径` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| misinformation (false information) | lie | `␣misinformation` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| conscience (conscience) | unclear | `良心` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 0/79 (0%) | 1/77 (1%) |
| manipulate (manipulating) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated` | 1/152 (1%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| embellish (embellishing, prettifying) | unclear | `美化` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| candid (candid / frank) | truth | `坦诚` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 73/158 (46%) | 1/79 (1%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `␣error`, `错`, `是错误的` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 2/158 (1%) | 0/79 (0%) | 0/77 (0%) |
| inaccurate (inaccurate) | lie | `准确性和` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: the question's own word)

## preans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact / reality) | unclear | `␣fact`, `实际情况`, `事实`, `␣reality`, `␣facts`, `的事实`, `␣factual`, `事实上`, `fact`, `␣Fact`, `Fact`, `␣FACT`, `facts`, `事实和`, `␣Facts`, `␣Reality`, `FACT`, `事实证明`, `Reality`, `_fact`, `␣realities`, `␣realidad`, `实际`, `符合`, `现实`, `实际上`, `的实际`, `实际的`, `是否符合`, `实事求是`, `现实中`, `的现实`, `实际上是`, `与实际`, `犯罪事实`, `求实`, `与现实`, `认定事实`, `上述事实`, `␣reale`, `␣reales` | 93/152 (61%) | 31/81 (38%) | 129/138 (93%) | 82/158 (52%) | 47/79 (59%) | 27/77 (35%) |
| knowingly (knowing the truth, knowingly) | unclear | `明知`, `知情`, `␣knowing`, `␣Knowing`, `␣knowingly`, `Knowing` | 66/152 (43%) | 28/81 (35%) | 44/138 (32%) | 0/158 (0%) | 35/79 (44%) | 28/77 (36%) |
| knowingly (knowing full well (明知)) | unclear | `明知` | 63/152 (41%) | 26/81 (32%) | 43/138 (31%) | 0/158 (0%) | 34/79 (43%) | 26/77 (34%) |
| conceal (the act of hiding / covering up) | lie | `隐瞒`, `掩盖`, `隐藏`, `␣conceal`, `␣masking`, `瞒`, `隐藏着`, `␣concealed`, `遮盖`, `␣hide`, `掩饰`, `隐蔽`, `hide`, `Hide`, `␣hides`, `遮掩`, `-hide`, `_hide`, `␣masks`, `遮蔽`, `藏着`, `.hide`, `␣Hide` | 63/152 (41%) | 25/81 (31%) | 5/138 (4%) | 0/158 (0%) | 27/79 (34%) | 24/77 (31%) |
| conceal (concealing (withholding the truth from someone)) | lie | `隐瞒`, `␣conceal`, `瞒`, `␣concealed`, `掩`, `遮`, `隐` | 55/152 (36%) | 24/81 (30%) | 3/138 (2%) | 0/158 (0%) | 22/79 (28%) | 23/77 (30%) |
| internal (internal, not public) | unclear | `␣internal`, `内部`, `␣internally`, `的内部`, `internal`, `␣Internal`, `/internal`, `Internal`, `内部的`, `␣INTERNAL`, `.internal`, `_internal`, `公司内部`, `INTERNAL`, `_INTERNAL`, `/Internal`, `(internal`, `.Internal`, `	internal`, `企业内部` | 53/152 (35%) | 20/81 (25%) | 4/138 (3%) | 0/158 (0%) | 28/79 (35%) | 18/77 (23%) |
| fictional (fictional, made-up setting) | unclear | `虚构`, `␣fictional`, `fiction`, `␣fict`, `架空`, `␣Fiction`, `␣fiction` | 40/152 (26%) | 32/81 (40%) | 42/138 (30%) | 35/158 (22%) | 21/79 (27%) | 32/77 (42%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `=true`, `_real`, `_true`, `:true`, `,true`, `␣genuine`, `␣REAL`, `.real`, `.True`, `␣genuinely`, `真`, `成立`, `真正`, `真实性`, `确实`, `真正的`, `的确`, `是真的`, `真實`, `确实是`, `属实`, `的真正` | 55/152 (36%) | 17/81 (21%) | 81/138 (59%) | 51/158 (32%) | 24/79 (30%) | 14/77 (18%) |
| secret (secret, secrecy, in secret) | lie | `␣secret`, `秘密`, `机密`, `的秘密`, `保密`, `␣Secret`, `secret`, `␣secretly`, `␣confidential`, `暗中`, `-secret`, `_secret`, `.secret`, `␣secrets`, `␣confidentiality`, `Secret`, `(secret`, `隐秘`, `␣Confidential`, `私下` | 49/152 (32%) | 22/81 (27%) | 2/138 (1%) | 0/158 (0%) | 25/79 (32%) | 20/77 (26%) |
| protect (protecting, safeguarding (an interest)) | unclear | `维护`, `和维护`, `保全`, `保护`, `␣protecting`, `为了保护`, `␣protect`, `␣protects`, `protect`, `为维护`, `保护和`, `保护的`, `␣Protect`, `Protect`, `的保护`, `和保护`, `␣protection`, `␣protective`, `与维护`, `␣protected`, `␣Protective` | 47/152 (31%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 31/79 (39%) | 19/77 (25%) |
| objective (objective) | unclear | `␣objective`, `␣objectively`, `客观` | 50/152 (33%) | 12/81 (15%) | 69/138 (50%) | 23/158 (15%) | 31/79 (39%) | 11/77 (14%) |
| role-play (playing a role / persona) | unclear | `␣persona`, `扮演`, `␣personas`, `␣Persona`, `角色扮演`, `persona`, `Persona`, `扮演着` | 25/152 (16%) | 32/81 (40%) | 13/138 (9%) | 1/158 (1%) | 18/79 (23%) | 30/77 (39%) |
| outward appearance (on the surface, outwardly) | unclear | `表面上`, `对外`, `表面的` | 32/152 (21%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 16/79 (20%) | 20/77 (26%) |
| inform (telling, informing someone) | unclear | `告知`, `␣tell`, `␣tells`, `被告知`, `␣telling`, `Tell`, `␣inform`, `请告知`, `␣Tell`, `␣informed`, `inform` | 39/152 (26%) | 11/81 (14%) | 37/138 (27%) | 1/158 (1%) | 20/79 (25%) | 10/77 (13%) |
| comply (complying, obeying) | unclear | `遵照`, `合规`, `服从`, `遵从`, `␣compliance`, `遵循`, `严格遵守`, `␣obey`, `遵`, `遵守`, `␣adherence`, `␣adher` | 38/152 (25%) | 12/81 (15%) | 1/138 (1%) | 16/158 (10%) | 24/79 (30%) | 11/77 (14%) |
| private (private, privately) | unclear | `私下`, `␣private`, `␣privately`, `␣Private`, `private`, `Private`, `.private`, `PRIVATE`, `/private`, `私人`, `私密`, `(private`, `-private`, `/Private`, `,private`, `私自` | 33/152 (22%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 14/79 (18%) | 14/77 (18%) |
| inform (informing / telling (告知)) | unclear | `告知`, `被告知`, `请告知` | 38/152 (25%) | 10/81 (12%) | 37/138 (27%) | 0/158 (0%) | 19/79 (24%) | 9/77 (12%) |
| deliberate (on purpose, intentionally) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `刻意`, `␣deliberate`, `␣intentional` | 35/152 (23%) | 12/81 (15%) | 0/138 (0%) | 3/158 (2%) | 13/79 (16%) | 12/77 (16%) |
| hypothetical (hypothetical, supposed) | unclear | `␣hypothetical`, `假设` | 18/152 (12%) | 29/81 (36%) | 57/138 (41%) | 15/158 (9%) | 12/79 (15%) | 28/77 (36%) |
| account for (account for / explain; also 'come clean' (交代)) | unclear | `交代` | 31/152 (20%) | 16/81 (20%) | 3/138 (2%) | 0/158 (0%) | 15/79 (19%) | 16/77 (21%) |
| hide (hiding, being hidden) | lie | `隐藏`, `␣hidden`, `隐藏的`, `␣hiding`, `隐藏着`, `␣hide`, `hide`, `Hide`, `␣hides`, `隐蔽`, `-hidden`, `-hide`, `_hide`, `hidden`, `␣Hidden`, `:hidden`, `.hide`, `␣Hide`, `␣hid` | 25/152 (16%) | 13/81 (16%) | 8/138 (6%) | 0/158 (0%) | 14/79 (18%) | 12/77 (16%) |
| cover up (covering up, masking) | lie | `掩盖`, `␣masking`, `␣cover`, `遮盖`, `掩饰`, `cover`, `␣Cover`, `Cover`, `␣masks`, `遮掩`, `␣covering`, `遮蔽`, `COVER`, `-cover` | 28/152 (18%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 8/77 (10%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `>false`, `␣fals`, `␣falsely`, `/false`, `␣falsehood`, `假`, `假的`, `真假`, `不实` | 28/152 (18%) | 8/81 (10%) | 21/138 (15%) | 4/158 (3%) | 12/79 (15%) | 8/77 (10%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗`, `␣deceive`, `␣deceived`, `␣deceit`, `欺`, `哄` | 25/152 (16%) | 7/81 (9%) | 2/138 (1%) | 0/158 (0%) | 9/79 (11%) | 7/77 (9%) |
| contradict (contradiction) | unclear | `矛盾`, `矛盾的`, `␣contrad`, `␣contradict`, `␣contradictory` | 17/152 (11%) | 15/81 (19%) | 8/138 (6%) | 1/158 (1%) | 8/79 (10%) | 14/77 (18%) |
| violate (violating (rules, instructions, principles)) | unclear | `违背`, `违规`, `违反`, `违法` | 13/152 (9%) | 18/81 (22%) | 1/138 (1%) | 1/158 (1%) | 4/79 (5%) | 18/77 (23%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演`, `扮演着` | 10/152 (7%) | 20/81 (25%) | 2/138 (1%) | 1/158 (1%) | 5/79 (6%) | 19/77 (25%) |
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `准确`, `准确的`, `准确地` | 22/152 (14%) | 8/81 (10%) | 12/138 (9%) | 69/158 (44%) | 13/79 (16%) | 8/77 (10%) |
| suppress (suppressing, keeping down) | lie | `压下`, `␣suppression`, `suppress` | 21/152 (14%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 15/79 (19%) | 8/77 (10%) |
| confidential (confidential / kept private) | unclear | `机密`, `保密`, `␣confidential`, `␣confidentiality`, `私密`, `␣Confidential` | 20/152 (13%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 12/79 (15%) | 6/77 (8%) |
| fake (fake, counterfeit) | lie | `fake`, `␣fake`, `Fake`, `虚假`, `␣misinformation`, `虚假信息` | 20/152 (13%) | 5/81 (6%) | 5/138 (4%) | 1/158 (1%) | 6/79 (8%) | 5/77 (6%) |
| official line (the agreed public line / talking points (口径)) | unclear | `口径` | 21/152 (14%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 8/79 (10%) | 3/77 (4%) |
| loyal (loyalty) | unclear | `␣loyalty`, `忠诚`, `忠于`, `忠诚度`, `␣loyal`, `忠`, `忠实`, `␣faithfully` | 12/152 (8%) | 10/81 (12%) | 2/138 (1%) | 10/158 (6%) | 8/79 (10%) | 10/77 (13%) |
| hidden (being hidden / not disclosed (state)) | lie | `␣hidden`, `隐藏的`, `␣undisclosed`, `-hidden`, `␣Hidden`, `hidden`, `:hidden`, `隐秘` | 11/152 (7%) | 10/81 (12%) | 6/138 (4%) | 0/158 (0%) | 6/79 (8%) | 9/77 (12%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `误导性` | 14/152 (9%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 5/79 (6%) | 4/77 (5%) |
| scheme (a scheme, plot) | unclear | `␣scheme` | 14/152 (9%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 3/77 (4%) |
| ethics (ethics, morality, right and wrong) | unclear | `是非`, `␣ethical`, `伦理`, `␣ethics`, `道德`, `ethical`, `␣moral`, `␣morally` | 11/152 (7%) | 5/81 (6%) | 15/138 (11%) | 2/158 (1%) | 6/79 (8%) | 4/77 (5%) |
| euphemistic (tactful, indirect wording) | unclear | `委婉` | 10/152 (7%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 5/77 (6%) |
| fabricate (making something up) | lie | `伪造`, `␣fabricated`, `␣invented`, `␣fabrication`, `作假` | 12/152 (8%) | 2/81 (2%) | 1/138 (1%) | 3/158 (2%) | 3/79 (4%) | 2/77 (3%) |
| conflict (conflicting (demands)) | unclear | `␣conflicting`, `␣conflict`, `␣conflicts` | 3/152 (2%) | 11/81 (14%) | 2/138 (1%) | 0/158 (0%) | 2/79 (3%) | 11/77 (14%) |
| faithful (faithful (to facts or to a party)) | unclear | `忠实`, `␣faithfully` | 6/152 (4%) | 7/81 (9%) | 2/138 (1%) | 9/158 (6%) | 3/79 (4%) | 7/77 (9%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 9/152 (6%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| pander (pandering, trying to please) | unclear | `迎合`, `讨好` | 6/152 (4%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 5/77 (6%) |
| pretend (pretending, disguising) | lie | `伪装`, `␣pretend`, `␣pretending`, `假装`, `␣disguised` | 7/152 (5%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 3/77 (4%) |
| disclose (disclosing, revealing) | truth | `揭露`, `␣disclosed`, `␣disclosure`, `披露`, `透露`, `␣revealed`, `揭示`, `揭` | 5/152 (3%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 5/77 (6%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣mistake`, `␣mistakes`, `错`, `错误`, `不对`, `错了`, `没错`, `失误`, `的错误`, `是错误的` | 5/152 (3%) | 3/81 (4%) | 2/138 (1%) | 3/158 (2%) | 1/79 (1%) | 3/77 (4%) |
| embellish (embellishing, prettifying) | unclear | `美化` | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 4/77 (5%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `不符合`, `有误` | 2/152 (1%) | 5/81 (6%) | 0/138 (0%) | 11/158 (7%) | 1/79 (1%) | 5/77 (6%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣correctamente`, `␣correcting`, `␣Corrections`, `正确`, `正确的`, `正确的是`, `纠正`, `的正确`, `无误`, `是正确的`, `正确地`, `是否正确`, `␣correcto` | 2/152 (1%) | 3/81 (4%) | 44/138 (32%) | 107/158 (68%) | 0/79 (0%) | 3/77 (4%) |
| evade (avoiding, evading) | unclear | `回避`, `␣avoid`, `␣avoidance` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| unethical (unethical) | lie | `␣unethical` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| manipulate (manipulating) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating`, `␣manipul`, `操纵` | 2/152 (1%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| cannot (cannot, unable (refusal stance)) | unclear | `不能`, `又不能`, `不能说`, `␣cannot`, `Cannot`, `cannot`, `␣Cannot`, `无法`, `也不能`, `都不能`, `就不能`, `都无法`, `但不能`, `我们不能`, `而不能`, `根本无法`, `不能在`, `绝对不能`, `绝不能`, `却不能`, `不能让` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 10/158 (6%) | 1/79 (1%) | 1/77 (1%) |
| firm (firmly, resolutely) | unclear | `坚决` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| evade (evading / dodging) | lie | `回避`, `规避` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| trick (a trick, to trick) | lie | `␣trick`, `␣tricks` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| honest (honesty) | truth | `␣honest`, `␣honesty`, `诚信`, `坦诚` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 3/158 (2%) | 0/79 (0%) | 1/77 (1%) |
| confess (confessing) | truth | `␣confess`, `␣confession`, `␣confessed`, `坦白` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| wrongdoing (wrongdoing) | unclear | `␣wrongdoing` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| discovered (being found out) | unclear | `␣discovered` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| inaccurate (inaccurate) | lie | `准确性和`, `不准确` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 1/79 (1%) | 0/77 (0%) |
| fraud (fraud, swindle) | lie | `诈骗`, `欺诈`, `骗局`, `␣fraud`, `␣fraudulent` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| transparent (transparency) | truth | `␣transparency` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| clarify (clarifying) | unclear | `澄清` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 1/158 (1%) | 1/79 (1%) | 0/77 (0%) |
| refuse (refusing, declining) | unclear | `拒绝` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| illegal (illegal) | unclear | `␣illegal`, `违法` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| guilt (guilt) | unclear | `␣guilt` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| selfish (selfish) | unclear | `自私` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| impersonate (impersonating someone) | lie | `冒充` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| integrity (integrity / uprightness) | truth | `诚信` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| candid (candid / frank) | truth | `坦诚` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: the question's own word)

## preans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| disclose (disclosing / revealing) | truth | `公布` | 151/152 (99%) | 81/81 (100%) | 138/138 (100%) | 153/158 (97%) | 78/79 (99%) | 77/77 (100%) |
| cannot (cannot, unable (refusal stance)) | unclear | `无法`, `␣cannot`, `我无法`, `不能被`, `不能`, `都无法`, `我不能`, `是无法`, `不能作为`, `cannot`, `是不能`, `也不能`, `都不能`, `根本无法`, `Cannot` | 140/152 (92%) | 58/81 (72%) | 56/138 (41%) | 3/158 (2%) | 71/79 (90%) | 55/77 (71%) |
| false (false, untrue) | lie | `␣false`, `False`, `FALSE`, `假`, `假的`, `真假` | 117/152 (77%) | 66/81 (81%) | 124/138 (90%) | 89/158 (56%) | 57/79 (72%) | 62/77 (81%) |
| lawful (lawful, law-abiding) | unclear | `守法`, `␣legally`, `依法`, `/legal` | 117/152 (77%) | 53/81 (65%) | 10/138 (7%) | 7/158 (4%) | 54/79 (68%) | 49/77 (64%) |
| apologize (apology, sorry) | unclear | `抱歉`, `Sorry`, `␣apologize`, `␣sorry`, `␣Sorry` | 119/152 (78%) | 35/81 (43%) | 11/138 (8%) | 26/158 (16%) | 67/79 (85%) | 34/77 (44%) |
| refuse (refusing, declining) | unclear | `␣refusal`, `拒`, `拒不`, `拒绝` | 97/152 (64%) | 29/81 (36%) | 1/138 (1%) | 0/158 (0%) | 53/79 (67%) | 28/77 (36%) |
| firm (firmly, resolutely) | unclear | `坚决` | 85/152 (56%) | 25/81 (31%) | 0/138 (0%) | 0/158 (0%) | 51/79 (65%) | 24/77 (31%) |
| impossible (impossible) | unclear | `␣impossible`, `␣Impossible`, `Impossible` | 40/152 (26%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 24/79 (30%) | 18/77 (23%) |
| correct (correct) | truth | `␣correct`, `正确`, `正确的` | 39/152 (26%) | 20/81 (25%) | 21/138 (15%) | 58/158 (37%) | 14/79 (18%) | 20/77 (26%) |
| euphemistic (tactful, indirect wording) | unclear | `婉` | 10/152 (7%) | 4/81 (5%) | 17/138 (12%) | 3/158 (2%) | 6/79 (8%) | 4/77 (5%) |
| clarify (clarifying) | unclear | `澄清` | 1/152 (1%) | 12/81 (15%) | 9/138 (7%) | 0/158 (0%) | 1/79 (1%) | 12/77 (16%) |
| fictional (fictional, made-up setting) | unclear | `fiction` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 2/77 (3%) |
| secret (secret, secrecy, in secret) | lie | `_secret`, `秘密` | 2/152 (1%) | 3/81 (4%) | 30/138 (22%) | 35/158 (22%) | 2/79 (3%) | 3/77 (4%) |
| ethics (ethics, morality, right and wrong) | unclear | `的道德`, `伦理`, `␣ethical`, `␣morally` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| conscience (conscience) | unclear | `良心` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| hide (hiding, being hidden) | lie | `:hidden` | 0/152 (0%) | 1/81 (1%) | 12/138 (9%) | 32/158 (20%) | 0/79 (0%) | 1/77 (1%) |
| wrong (wrong, mistaken) | lie | `的错误` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: cover up (held back: no undisputed member left); truth (excluded: the question's own word)

## preans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `真`, `确实` | 117/152 (77%) | 46/81 (57%) | 97/138 (70%) | 149/158 (94%) | 48/79 (61%) | 42/77 (55%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `>false`, `_false`, `.False`, `/false`, `假`, `假的` | 121/152 (80%) | 35/81 (43%) | 64/138 (46%) | 33/158 (21%) | 69/79 (87%) | 32/77 (42%) |
| cannot (cannot, unable (refusal stance)) | unclear | `␣cannot`, `无法`, `我无法`, `我不能`, `cannot`, `不能`, `Cannot`, `␣Cannot`, `是无法`, `是不能` | 57/152 (38%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 20/79 (25%) | 2/77 (3%) |
| honest (honesty) | truth | `诚信`, `␣honest`, `坦诚` | 42/152 (28%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 22/79 (28%) | 14/77 (18%) |
| integrity (integrity, uprightness) | truth | `正直`, `诚信` | 42/152 (28%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 22/79 (28%) | 14/77 (18%) |
| conceal (concealing (withholding the truth from someone)) | lie | `隐瞒`, `瞒`, `掩`, `隐` | 27/152 (18%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 1/77 (1%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception` | 23/152 (15%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 3/77 (4%) |
| correct (correct) | truth | `valid`, `␣correct`, `正确`, `纠正` | 3/152 (2%) | 26/81 (32%) | 84/138 (61%) | 2/158 (1%) | 3/79 (4%) | 26/77 (34%) |
| objective (objective) | unclear | `客观` | 12/152 (8%) | 15/81 (19%) | 5/138 (4%) | 0/158 (0%) | 8/79 (10%) | 15/77 (19%) |
| knowingly (knowing the truth, knowingly) | unclear | `明知` | 21/152 (14%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| secret (secret, secrecy, in secret) | lie | `秘密`, `保密`, `secret` | 22/152 (14%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 0/77 (0%) |
| outward appearance (on the surface, outwardly) | unclear | `外表`, `表面上` | 20/152 (13%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 17/79 (22%) | 2/77 (3%) |
| protect (protecting, safeguarding (an interest)) | unclear | `为了保护` | 16/152 (11%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 14/79 (18%) | 3/77 (4%) |
| violate (violating (rules, instructions, principles)) | unclear | `违反`, `违反了` | 16/152 (11%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| lawful (lawful, law-abiding) | unclear | `合法`, `␣legally`, `依法` | 15/152 (10%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 14/79 (18%) | 1/77 (1%) |
| apologize (apology, sorry) | unclear | `抱歉`, `对不起`, `Sorry`, `␣sorry` | 11/152 (7%) | 5/81 (6%) | 5/138 (4%) | 3/158 (2%) | 6/79 (8%) | 5/77 (6%) |
| firm (firmly, resolutely) | unclear | `坚决`, `␣firmly` | 13/152 (9%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 1/77 (1%) |
| confidential (confidential / kept private) | unclear | `保密` | 11/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 0/77 (0%) |
| confess (confessing) | truth | `坦白` | 7/152 (5%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 3/77 (4%) |
| fact (fact / reality) | unclear | `事实`, `根据实际情况`, `符合`, `实际上` | 8/152 (5%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 4/79 (5%) | 1/77 (1%) |
| comply (complying, obeying) | unclear | `␣adher`, `遵循` | 6/152 (4%) | 3/81 (4%) | 2/138 (1%) | 1/158 (1%) | 5/79 (6%) | 3/77 (4%) |
| refuse (refusing, declining) | unclear | `␣refusal`, `␣refuse`, `␣refused`, `拒绝` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 1/77 (1%) |
| fictional (fictional, made-up setting) | unclear | `虚构`, `fiction` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 3/79 (4%) | 1/77 (1%) |
| hide (hiding, being hidden) | lie | `␣hidden`, `hidden`, `:hidden` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| dishonest (dishonesty) | lie | `␣dishonest` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| ethics (ethics, morality, right and wrong) | unclear | `是非` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| contradict (contradiction) | unclear | `矛盾`, `␣contradiction` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| candid (candid / frank) | truth | `坦诚` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| accurate (accurate) | truth | `␣accurate`, `准确` | 0/152 (0%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| deliberate (on purpose, intentionally) | unclear | `␣intentionally`, `␣deliberately` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `不对` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `不符合` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: cover up (held back: no undisputed member left); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: the question's own word); honest (excluded: the question's own word)
