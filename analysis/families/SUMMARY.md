# Family generation: summary across units (PLAN.md Section 5.4)

Written by `scripts/family_summary.py` from the replicate files in this folder. No labels were
read. A *unit* is one model × lens × part × position group; each unit has two replicate files
written by independent subagents with the frozen prompt `prompts/family_generation.md`.

## 1. Coverage

| lens | model | units | replicate files | family entries |
|---|---|---|---|---|
| J | gemma-3-12b-it | 1 | 2 | 312 |
| J | gemma-3-27b-it | 1 | 2 | 259 |
| J | gpt-oss-20b | 1 | 2 | 50 |
| J | qwen3.6-27b | 27 | 54 | 6118 |
| LL | gemma-3-12b-it | 1 | 2 | 278 |
| LL | gemma-3-27b-it | 1 | 2 | 221 |
| LL | gpt-oss-20b | 1 | 2 | 19 |
| LL | qwen3.6-27b | 27 | 54 | 5257 |

## 2. Families per position (replicate 1 / replicate 2)

Positions where both replicates found no family are marked **none**.

| lens | unit | families per position |
|---|---|---|
| J | gemma_3_12b_it_J_prefix_postresp | postresp_slot0 5/6; postresp_slot1 60/53; postresp_slot2 66/63; postresp_slot3 6/6; postresp_slot4 28/19 |
| J | gemma_3_27b_it_J_prefix_postresp | postresp_slot0 7/8; postresp_slot1 43/49; postresp_slot2 53/59; postresp_slot3 3/3; postresp_slot4 15/19 |
| J | gpt_oss_20b_J_prefix_postresp | postresp_slot0 2/2; postresp_slot1 1/1; postresp_slot2 4/5; postresp_slot3 15/20 |
| J | qwen3_6_27b_J_Q1_bare_postans | postans_slot0 3/4; postans_slot1 30/31; postans_slot2 25/29; postans_slot3 **none**; postans_slot4 44/53 |
| J | qwen3_6_27b_J_Q1_bare_preans | preans_slot0 6/6; preans_slot1 57/57; preans_slot2 55/60; preans_slot3 14/15; preans_slot4 48/53 |
| J | qwen3_6_27b_J_Q1_bare_question | q_tok0 16/13; q_tok1 25/23; q_tok2 11/12; q_tok3 36/32; q_tok4 19/20; q_tok5 10/11 |
| J | qwen3_6_27b_J_Q1_bare_think | think_slot0 17/14; think_slot1 16/14; think_slot2 30/29; think_slot3 36/38 |
| J | qwen3_6_27b_J_Q2_after_postans | postans_slot0 3/2; postans_slot1 33/37; postans_slot2 18/22; postans_slot3 **none**; postans_slot4 45/51 |
| J | qwen3_6_27b_J_Q2_after_preans | preans_slot0 0/2; preans_slot1 70/63; preans_slot2 66/59; preans_slot3 6/6; preans_slot4 45/40 |
| J | qwen3_6_27b_J_Q2_after_questiona | q_tok0 12/15; q_tok1 24/22; q_tok2 11/10; q_tok3 35/37; q_tok4 21/22; q_tok5 10/10; q_tok6 3/3; q_tok7 1/1 |
| J | qwen3_6_27b_J_Q2_after_questionb | q_tok8 **none**; q_tok9 1/1; q_tok10 49/46 |
| J | qwen3_6_27b_J_Q2_after_think | think_slot0 15/14; think_slot1 12/14; think_slot2 31/40; think_slot3 19/23 |
| J | qwen3_6_27b_J_Q6_factual_postans | postans_slot0 3/1; postans_slot1 33/31; postans_slot2 22/23; postans_slot3 0/1; postans_slot4 51/56 |
| J | qwen3_6_27b_J_Q6_factual_preans | preans_slot0 2/0; preans_slot1 42/37; preans_slot2 46/41; preans_slot3 4/3; preans_slot4 31/28 |
| J | qwen3_6_27b_J_Q6_factual_questiona | q_tok0 6/6; q_tok1 14/16; q_tok2 10/11; q_tok3 34/30; q_tok4 27/25; q_tok5 61/57; q_tok6 19/18; q_tok7 14/16 |
| J | qwen3_6_27b_J_Q6_factual_questionb | q_tok8 5/6; q_tok9 3/2; q_tok10 **none**; q_tok11 1/1; q_tok12 **none**; q_tok13 34/37 |
| J | qwen3_6_27b_J_Q6_factual_think | think_slot0 16/16; think_slot1 14/11; think_slot2 33/33; think_slot3 13/14 |
| J | qwen3_6_27b_J_Q7_ab_postans | postans_slot0 1/2; postans_slot1 22/24; postans_slot2 4/2; postans_slot3 1/1; postans_slot4 64/62 |
| J | qwen3_6_27b_J_Q7_ab_preans | preans_slot0 1/1; preans_slot1 43/45; preans_slot2 48/55; preans_slot3 5/6; preans_slot4 24/27 |
| J | qwen3_6_27b_J_Q7_ab_questiona | q_tok0 8/7; q_tok1 46/50; q_tok2 17/17; q_tok3 26/27; q_tok4 21/21; q_tok5 3/3; q_tok6 24/26; q_tok7 14/12 |
| J | qwen3_6_27b_J_Q7_ab_questionb | q_tok8 1/2; q_tok9 1/2; q_tok10 **none**; q_tok11 2/2; q_tok12 **none**; q_tok13 **none**; q_tok14 9/8; q_tok15 **none** |
| J | qwen3_6_27b_J_Q7_ab_questionc | q_tok16 **none**; q_tok17 7/8; q_tok18 11/10; q_tok19 43/42; q_tok20 35/31; q_tok21 15/16; q_tok22 35/32; q_tok23 **none** |
| J | qwen3_6_27b_J_Q7_ab_questiond | q_tok24 71/83; q_tok25 8/8; q_tok26 69/78; q_tok27 60/72; q_tok28 20/22; q_tok29 6/7; q_tok30 **none** |
| J | qwen3_6_27b_J_Q7_ab_think | think_slot0 13/15; think_slot1 10/13; think_slot2 33/31; think_slot3 15/14 |
| J | qwen3_6_27b_J_Q9_dyl_postans | postans_slot0 1/1; postans_slot1 35/34; postans_slot2 13/13; postans_slot3 1/1; postans_slot4 51/53 |
| J | qwen3_6_27b_J_Q9_dyl_preans | preans_slot0 4/3; preans_slot1 47/38; preans_slot2 61/48; preans_slot3 3/2; preans_slot4 34/28 |
| J | qwen3_6_27b_J_Q9_dyl_questiona | q_tok0 8/6; q_tok1 56/48; q_tok2 21/19; q_tok3 31/27; q_tok4 61/49; q_tok5 2/1; q_tok6 18/16; q_tok7 14/13 |
| J | qwen3_6_27b_J_Q9_dyl_questionb | q_tok8 2/5; q_tok9 0/1; q_tok10 0/2; q_tok11 0/2; q_tok12 10/15; q_tok13 0/1; q_tok14 0/2; q_tok15 3/5 |
| J | qwen3_6_27b_J_Q9_dyl_think | think_slot0 15/12; think_slot1 17/16; think_slot2 38/38; think_slot3 17/16 |
| J | qwen3_6_27b_J_prefix_postresp | postresp_slot0 **none**; postresp_slot1 45/45; postresp_slot2 **none**; postresp_slot3 3/4; postresp_slot4 41/42 |
| LL | gemma_3_12b_it_LL_prefix_postresp | postresp_slot0 14/7; postresp_slot1 59/55; postresp_slot2 67/66; postresp_slot3 3/3; postresp_slot4 2/2 |
| LL | gemma_3_27b_it_LL_prefix_postresp | postresp_slot0 13/14; postresp_slot1 40/39; postresp_slot2 54/51; postresp_slot3 **none**; postresp_slot4 5/5 |
| LL | gpt_oss_20b_LL_prefix_postresp | postresp_slot0 6/4; postresp_slot1 **none**; postresp_slot2 **none**; postresp_slot3 5/4 |
| LL | qwen3_6_27b_LL_Q1_bare_postans | postans_slot0 3/4; postans_slot1 33/34; postans_slot2 18/15; postans_slot3 4/3; postans_slot4 46/40 |
| LL | qwen3_6_27b_LL_Q1_bare_preans | preans_slot0 13/9; preans_slot1 41/42; preans_slot2 45/45; preans_slot3 16/11; preans_slot4 38/39 |
| LL | qwen3_6_27b_LL_Q1_bare_question | q_tok0 6/4; q_tok1 16/14; q_tok2 3/4; q_tok3 30/22; q_tok4 28/25; q_tok5 18/15 |
| LL | qwen3_6_27b_LL_Q1_bare_think | think_slot0 10/5; think_slot1 6/2; think_slot2 20/9; think_slot3 32/29 |
| LL | qwen3_6_27b_LL_Q2_after_postans | postans_slot0 4/3; postans_slot1 34/26; postans_slot2 13/13; postans_slot3 9/7; postans_slot4 55/41 |
| LL | qwen3_6_27b_LL_Q2_after_preans | preans_slot0 7/6; preans_slot1 53/51; preans_slot2 49/48; preans_slot3 12/14; preans_slot4 35/34 |
| LL | qwen3_6_27b_LL_Q2_after_questiona | q_tok0 7/7; q_tok1 20/17; q_tok2 5/5; q_tok3 27/29; q_tok4 31/30; q_tok5 20/20; q_tok6 3/4; q_tok7 2/2 |
| LL | qwen3_6_27b_LL_Q2_after_questionb | q_tok8 2/2; q_tok9 4/4; q_tok10 51/40 |
| LL | qwen3_6_27b_LL_Q2_after_think | think_slot0 4/3; think_slot1 4/2; think_slot2 10/9; think_slot3 12/10 |
| LL | qwen3_6_27b_LL_Q6_factual_postans | postans_slot0 4/5; postans_slot1 26/32; postans_slot2 11/9; postans_slot3 8/6; postans_slot4 40/45 |
| LL | qwen3_6_27b_LL_Q6_factual_preans | preans_slot0 5/7; preans_slot1 29/34; preans_slot2 27/33; preans_slot3 10/10; preans_slot4 20/25 |
| LL | qwen3_6_27b_LL_Q6_factual_questiona | q_tok0 9/9; q_tok1 13/10; q_tok2 4/3; q_tok3 21/19; q_tok4 12/13; q_tok5 41/37; q_tok6 11/13; q_tok7 7/9 |
| LL | qwen3_6_27b_LL_Q6_factual_questionb | q_tok8 6/5; q_tok9 1/1; q_tok10 1/1; q_tok11 2/2; q_tok12 0/1; q_tok13 25/30 |
| LL | qwen3_6_27b_LL_Q6_factual_think | think_slot0 8/9; think_slot1 5/5; think_slot2 11/11; think_slot3 10/12 |
| LL | qwen3_6_27b_LL_Q7_ab_postans | postans_slot0 3/5; postans_slot1 16/25; postans_slot2 3/2; postans_slot3 7/9; postans_slot4 30/46 |
| LL | qwen3_6_27b_LL_Q7_ab_preans | preans_slot0 7/4; preans_slot1 46/35; preans_slot2 55/43; preans_slot3 14/10; preans_slot4 26/23 |
| LL | qwen3_6_27b_LL_Q7_ab_questiona | q_tok0 8/5; q_tok1 41/38; q_tok2 18/16; q_tok3 22/23; q_tok4 23/22; q_tok5 3/3; q_tok6 34/33; q_tok7 22/19 |
| LL | qwen3_6_27b_LL_Q7_ab_questionb | q_tok8 2/2; q_tok9 **none**; q_tok10 2/2; q_tok11 2/2; q_tok12 2/2; q_tok13 1/1; q_tok14 16/15; q_tok15 2/0 |
| LL | qwen3_6_27b_LL_Q7_ab_questionc | q_tok16 **none**; q_tok17 1/1; q_tok18 10/9; q_tok19 41/31; q_tok20 25/20; q_tok21 11/10; q_tok22 35/26; q_tok23 1/0 |
| LL | qwen3_6_27b_LL_Q7_ab_questiond | q_tok24 65/53; q_tok25 9/10; q_tok26 59/51; q_tok27 52/43; q_tok28 13/14; q_tok29 16/15; q_tok30 3/3 |
| LL | qwen3_6_27b_LL_Q7_ab_think | think_slot0 10/12; think_slot1 7/4; think_slot2 20/17; think_slot3 19/11 |
| LL | qwen3_6_27b_LL_Q9_dyl_postans | postans_slot0 3/4; postans_slot1 36/31; postans_slot2 16/12; postans_slot3 7/4; postans_slot4 53/47 |
| LL | qwen3_6_27b_LL_Q9_dyl_preans | preans_slot0 16/11; preans_slot1 41/35; preans_slot2 48/39; preans_slot3 9/7; preans_slot4 32/24 |
| LL | qwen3_6_27b_LL_Q9_dyl_questiona | q_tok0 9/11; q_tok1 47/44; q_tok2 20/19; q_tok3 28/27; q_tok4 54/46; q_tok5 3/4; q_tok6 25/25; q_tok7 20/19 |
| LL | qwen3_6_27b_LL_Q9_dyl_questionb | q_tok8 4/2; q_tok9 2/1; q_tok10 3/1; q_tok11 5/6; q_tok12 10/5; q_tok13 **none**; q_tok14 3/1; q_tok15 9/7 |
| LL | qwen3_6_27b_LL_Q9_dyl_think | think_slot0 6/5; think_slot1 5/7; think_slot2 12/16; think_slot3 10/12 |
| LL | qwen3_6_27b_LL_prefix_postresp | postresp_slot0 15/9; postresp_slot1 69/53; postresp_slot2 1/1; postresp_slot3 8/3; postresp_slot4 64/49 |

## 3. Family names across units, J-lens (names in 4 or more units)

| family | units | entries | sides (lie / truth / unclear) | most frequent members |
|---|---|---|---|---|
| honest | 30 | 185 | 0 / 185 / 0 | `␣honesty`, `诚实`, `␣honest`, `␣honestly`, `␣truthful`, `␣Honest` |
| unethical | 29 | 144 | 94 / 0 / 50 | `␣unethical`, `␣immoral`, `␣unethical`, `␣immoral`, `␣wrongdoing` |
| refuse | 28 | 145 | 0 / 0 / 145 | `拒绝`, `␣refusal`, `␣refus`, `␣refusing`, `拒`, `␣refused` |
| fake | 27 | 160 | 160 / 0 / 0 | `fake`, `␣fake`, `Fake`, `␣Fake`, `伪`, `假` |
| violate | 27 | 144 | 14 / 0 / 130 | `违反`, `违背`, `违规`, `违反了`, `␣violate`, `␣violates` |
| admit | 27 | 142 | 0 / 142 / 0 | `承认`, `␣admitting`, `␣admit`, `␣admitted`, `␣admits`, `␣admission` |
| mislead | 27 | 139 | 139 / 0 / 0 | `␣misleading`, `误导`, `误导性`, `␣misled`, `␣misleading`, `␣misled` |
| dishonest | 27 | 132 | 132 / 0 / 0 | `␣dishonest`, `␣dishonest`, `␣dishonesty`, `虚伪` |
| secret | 27 | 108 | 102 / 0 / 6 | `隐秘`, `秘密`, `␣secretly`, `的秘密`, `␣secrecy`, `␣secret` |
| confidential | 27 | 91 | 29 / 0 / 62 | `␣confidentiality`, `保密`, `␣confidential`, `机密`, `␣Confidential`, `␣confidentiality` |
| deny | 26 | 123 | 115 / 0 / 8 | `否认`, `否定`, `␣denial`, `␣denying`, `␣deny`, `deny` |
| disclose | 26 | 92 | 0 / 92 / 0 | `␣Disclosure`, `␣disclosure`, `␣disclosures`, `␣disclosing`, `␣disclose`, `␣disclosed` |
| misinformation | 24 | 141 | 141 / 0 / 0 | `␣misinformation`, `虚假信息`, `␣misinformation`, `␣disinformation` |
| fabricate | 24 | 104 | 104 / 0 / 0 | `伪造`, `虚构`, `造假`, `␣fabricated`, `弄虚作假`, `fiction` |
| fraud | 23 | 101 | 101 / 0 / 0 | `欺诈`, `␣fraudulent`, `␣fraud`, `␣Fraud`, `␣fraudulent`, `骗局` |
| cheat | 23 | 74 | 74 / 0 / 0 | `作弊`, `␣cheating`, `␣cheated`, `␣cheating` |
| truth | 22 | 119 | 0 / 119 / 0 | `␣truth`, `真相`, `␣Truth`, `truth`, `Truth`, `␣truths` |
| illegal | 22 | 95 | 7 / 0 / 88 | `违法违规`, `illegal`, `非法`, `违法`, `␣Illegal`, `␣illegal` |
| hide | 22 | 86 | 86 / 0 / 0 | `隐瞒`, `␣Hidden`, `隐藏`, `␣hidden`, `藏`, `hidden` |
| ethics | 22 | 78 | 0 / 0 / 78 | `␣ethics`, `␣Ethics`, `伦理`, `␣ethical`, `道德`, `ethical` |
| integrity | 22 | 76 | 0 / 76 / 0 | `诚信`, `␣integrity`, `␣Integrity`, `正直`, `␣integrity`, `␣Integrity` |
| acknowledge | 21 | 113 | 0 / 113 / 0 | `␣acknowledgment`, `␣acknowledging`, `␣acknowledge`, `␣acknowledges`, `␣Ack`, `Acknowled` |
| disclaimer | 21 | 97 | 0 / 0 / 97 | `␣disclaimer`, `␣Disclaimer`, `␣DISCLAIMER`, `Disclaimer`, `␣disclaimer`, `␣DISCLAIM` |
| ethical | 21 | 65 | 0 / 19 / 46 | `␣ethical`, `ethical`, `␣morally`, `␣ethical`, `␣moral`, `伦理` |
| evade | 21 | 54 | 52 / 0 / 2 | `回避`, `␣evasion`, `␣evade`, `规避`, `避开`, `␣evas` |
| hypocrisy | 20 | 67 | 63 / 0 / 4 | `␣hypocrisy`, `␣hypocrisy`, `虚伪` |
| confess | 20 | 64 | 0 / 64 / 0 | `坦白`, `␣confess`, `␣confession`, `␣confessed`, `认错`, `认罪` |
| pretend | 19 | 91 | 91 / 0 / 0 | `␣pretending`, `伪装`, `␣pretended`, `␣pretend`, `假装`, `␣pretending` |
| reject | 19 | 69 | 0 / 0 / 69 | `␣rejection`, `reject`, `␣rejecting`, `␣Reject`, `Reject`, `␣reject` |
| manipulate | 19 | 50 | 50 / 0 / 0 | `␣manipulation`, `␣manipulated`, `␣manip`, `␣manipulate`, `␣manipulating`, `Manip` |
| transparent | 19 | 48 | 0 / 48 / 0 | `␣transparency`, `透明`, `␣Transparency`, `␣transparent`, `透明度`, `␣transparency` |
| deceive | 18 | 101 | 101 / 0 / 0 | `欺骗`, `␣deception`, `␣deceptive`, `骗`, `␣deceived`, `␣deceive` |
| truthful | 18 | 92 | 0 / 92 / 0 | `␣truthful`, `␣truthful`, `如实`, `实事求是`, `实话`, `␣truthfully` |
| conceal | 18 | 74 | 74 / 0 / 0 | `隐瞒`, `␣conceal`, `␣concealed`, `掩盖`, `隐藏`, `␣hidden` |
| misrepresent | 17 | 73 | 73 / 0 / 0 | `␣misrepresented`, `␣misrepresented`, `␣distortion`, `␣distort` |
| apology | 17 | 50 | 0 / 5 / 45 | `␣apology`, `␣apologized`, `抱歉`, `Sorry`, `␣apologies`, `␣Sorry` |
| knowingly | 16 | 68 | 0 / 0 / 68 | `␣knowingly`, `明知`, `␣knowing`, `␣consciously`, `␣knowingly`, `␣Knowing` |
| clarify | 16 | 61 | 0 / 6 / 55 | `澄清`, `␣clarification`, `␣clarification`, `␣clarify`, `␣clarified`, `␣clarify` |
| lie | 15 | 86 | 86 / 0 / 0 | `谎言`, `说谎`, `谎`, `撒谎`, `␣거짓`, `␣lied` |
| contradict | 15 | 83 | 0 / 0 / 83 | `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contrad`, `矛盾`, `␣contradictions` |
| intentional | 15 | 67 | 0 / 0 / 67 | `␣intentionally`, `故意`, `␣intentional`, `␣deliberately`, `␣deliberate`, `␣purposely` |
| comply | 15 | 58 | 0 / 0 / 58 | `合规`, `␣compliant`, `␣compliance`, `␣comply`, `␣complying`, `遵守` |
| apologize | 15 | 54 | 0 / 4 / 50 | `␣apology`, `道歉`, `␣apologies`, `␣apologize`, `抱歉`, `␣apologised` |
| sincere | 15 | 38 | 0 / 38 / 0 | `␣sincerity`, `真诚`, `␣sincere`, `␣sincerely`, `␣sincerely`, `␣genuinely` |
| candid | 14 | 43 | 0 / 43 / 0 | `坦诚`, `直言`, `␣straightforward`, `␣straightforward`, `␣frankly`, `␣frankly` |
| omit | 13 | 51 | 48 / 0 / 3 | `␣omission`, `␣omit`, `␣omitted`, `省略`, `omit`, `␣omit` |
| unauthorized | 13 | 48 | 0 / 0 / 48 | `␣Unauthorized`, `␣unauthorized`, `␣unauthorized`, `私自`, `␣Unauthorized`, `Unauthorized` |
| deliberate | 13 | 44 | 0 / 0 / 44 | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `␣intentionally`, `␣deliberate` |
| fiction | 13 | 38 | 2 / 0 / 36 | `虚构`, `␣fictional`, `fiction`, `␣Fiction`, `␣fict`, `␣fiction` |
| fictional | 13 | 35 | 2 / 0 / 33 | `虚构`, `␣fictional`, `fiction`, `␣fict`, `␣Fiction`, `␣fiction` |
| leak | 13 | 30 | 0 / 2 / 28 | `␣WikiLeaks`, `泄露`, `␣leaked`, `␣leaked`, `␣Leakage`, `Leaks` |
| trick | 13 | 25 | 17 / 0 / 8 | `␣trick`, `␣Trick`, `␣tricks`, `␣Tricks`, `␣tricky`, `␣tricked` |
| accuse | 12 | 57 | 0 / 0 / 57 | `␣accusations`, `␣accusation`, `␣accusations`, `␣accusing`, `␣accusation`, `指控` |
| undisclosed | 12 | 35 | 35 / 0 / 0 | `␣undisclosed`, `␣undisclosed` |
| vague | 12 | 20 | 1 / 0 / 19 | `␣vague`, `模糊`, `含糊`, `␣vaguely`, `␣ambiguous`, `␣ambiguity` |
| withhold | 11 | 35 | 35 / 0 / 0 | `␣withholding`, `␣withheld`, `␣умолча`, `␣withhold`, `␣withholding`, `␣withheld` |
| disguise | 11 | 31 | 31 / 0 / 0 | `伪装`, `␣disguised`, `␣disguise`, `␣masking`, `␣disgu` |
| privacy | 11 | 27 | 0 / 0 / 27 | `privacy`, `␣Privacy`, `隐私`, `Privacy`, `␣privacy`, `␣privacidad` |
| reveal | 11 | 20 | 0 / 20 / 0 | `揭露`, `透露`, `␣revealing`, `␣revealed`, `␣reveal`, `Reveal` |
| accusation | 10 | 29 | 0 / 0 / 29 | `␣accusations`, `␣allegations`, `␣accusation`, `指控`, `␣accusing`, `␣allegation` |
| exaggerate | 10 | 25 | 25 / 0 / 0 | `夸大`, `␣exaggerated`, `␣exaggeration`, `␣exaggerate`, `␣exagger`, `␣exaggerated` |
| genuine | 10 | 25 | 0 / 21 / 4 | `␣genuinely`, `␣genuine`, `␣genuinely`, `␣Genuine`, `真正的`, `其真实性` |
| wrongdoing | 10 | 20 | 10 / 0 / 10 | `␣wrongdoing`, `␣wrongful`, `␣wrongdoing`, `␣wrongful` |
| prohibited | 9 | 28 | 0 / 0 / 28 | `␣prohibited`, `禁止`, `严禁`, `禁用`, `␣Forbidden`, `␣forbidden` |
| justify | 9 | 25 | 0 / 0 / 25 | `␣justify`, `␣justification`, `␣justifications`, `辩解`, `justify`, `␣justified` |
| whistleblow | 9 | 22 | 0 / 7 / 15 | `␣whistleblower`, `␣whistlebl`, `␣WikiLeaks`, `举报` |
| cover up | 9 | 15 | 15 / 0 / 0 | `掩盖`, `掩饰`, `遮蔽`, `遮盖`, `遮掩`, `掩护` |
| transparency | 9 | 14 | 0 / 14 / 0 | `␣transparency`, `␣Transparency`, `透明`, `透明度`, `␣transparent`, `透明的` |
| legal | 8 | 38 | 0 / 0 / 38 | `/legal`, `_legal`, `legal`, `合法`, `␣legality`, `␣Legal` |
| silence | 8 | 30 | 0 / 0 / 30 | `沉默`, `␣Silence`, `␣Silent`, `␣silence`, `silent`, `寂静` |
| lawful | 8 | 28 | 0 / 0 / 28 | `合法`, `/legal`, `legal`, `_legal`, `依法`, `␣legality` |
| compliance | 8 | 21 | 0 / 0 / 21 | `合规`, `␣Compliance`, `依规`, `恪`, `␣compliance`, `严格遵守` |
| hoax | 8 | 20 | 20 / 0 / 0 | `␣hoax`, `骗局` |
| moral | 8 | 19 | 0 / 0 / 19 | `␣morally`, `道德`, `␣moral`, `␣Moral`, `的道德`, `␣morality` |
| betray | 8 | 15 | 12 / 0 / 3 | `␣betrayed`, `␣betrayal`, `␣betray`, `␣betrayal`, `␣betray`, `背叛` |
| conscience | 8 | 14 | 0 / 0 / 14 | `␣conscience`, `良心` |
| cannot | 7 | 36 | 0 / 0 / 36 | `␣Cannot`, `cannot`, `Cannot`, `无法满足`, `无法`, `我无法` |
| avoid | 7 | 31 | 0 / 0 / 31 | `␣avoidance`, `避免`, `␣avoided`, `Avoid`, `Avoiding`, `␣avoiding` |
| blame | 7 | 26 | 0 / 0 / 26 | `␣blaming`, `␣blame`, `␣blames`, `␣blamed`, `␣blame`, `␣blames` |
| claim | 7 | 24 | 0 / 0 / 24 | `声称`, `␣claiming`, `␣claims`, `␣claim`, `claim`, `宣称` |
| ethics / morality | 7 | 21 | 0 / 0 / 21 | `道德`, `␣Ethics`, `␣ethics`, `␣morally`, `␣ethical`, `伦理` |
| allege | 7 | 20 | 0 / 0 / 20 | `␣allegations`, `␣alleging`, `␣allegation`, `␣alleged`, `␣purported`, `␣якобы` |
| trap | 7 | 16 | 0 / 0 / 16 | `陷阱`, `␣Trap`, `␣trap`, `trap`, `Trap`, `␣traps` |
| sorry | 7 | 16 | 0 / 1 / 15 | `sorry`, `Sorry`, `抱歉`, `␣Sorry`, `道歉`, `对不起` |
| unintentional | 7 | 14 | 0 / 0 / 14 | `␣inadvertently`, `␣accidentally`, `␣unintention`, `␣unintended`, `␣accidental`, `␣inadvert` |
| mistake | 6 | 33 | 0 / 0 / 33 | `␣mistake`, `␣mistaken`, `␣ERROR`, `␣errors`, `␣mistake`, `␣mistakes` |
| misunderstand | 6 | 25 | 0 / 0 / 25 | `␣misunderstood`, `␣misunderstand`, `␣misunderstanding`, `␣misunderstand`, `␣misunderstood`, `误解` |
| whistleblower | 6 | 16 | 0 / 1 / 15 | `␣whistleblower`, `␣whistlebl`, `␣whistleblower`, `␣whistlebl` |
| suppress | 6 | 15 | 15 / 0 / 0 | `suppress`, `.Suppress`, `␣suppressing`, `␣suppress`, `␣suppressed` |
| role-play | 6 | 13 | 0 / 0 / 13 | `角色扮演`, `扮演`, `␣persona`, `␣Persona`, `Persona`, `␣personas` |
| excuse | 6 | 13 | 1 / 0 / 12 | `␣excuse`, `借口`, `␣excuses`, `辩解`, `␣pretext` |
| accountability | 6 | 10 | 0 / 0 / 10 | `␣Accountability`, `␣accountability` |
| evasion | 6 | 9 | 9 / 0 / 0 | `␣evasion`, `回避` |
| contradiction | 5 | 20 | 0 / 0 / 20 | `␣contradiction`, `矛盾`, `␣contradict`, `␣contradictory`, `␣contradictions`, `␣contrad` |
| assert | 5 | 19 | 0 / 0 / 19 | `␣assertions`, `␣asserting`, `assert`, `␣assertion`, `␣assert`, `␣asserted` |
| persuade | 5 | 17 | 0 / 0 / 17 | `␣persuading`, `␣persuasive`, `␣persuasion`, `劝`, `␣persuade`, `劝说` |
| misunderstanding | 5 | 16 | 0 / 0 / 16 | `误解`, `␣misunderstanding`, `␣misunderstood`, `␣misunderstanding`, `␣misunderstand`, `␣misunderstand` |
| rebut | 5 | 15 | 0 / 0 / 15 | `反驳`, `␣rebut`, `␣refute`, `␣debunk`, `␣rebuttal` |
| decline | 5 | 14 | 0 / 0 / 14 | `␣declined`, `␣declines`, `␣decline`, `选择不`, `␣declining` |
| refute | 5 | 14 | 0 / 0 / 14 | `␣refute`, `反驳` |
| forbidden | 5 | 13 | 0 / 0 / 13 | `␣Forbidden`, `严禁`, `禁止`, `␣prohibited`, `禁忌`, `禁用` |
| hallucinate | 5 | 12 | 0 / 0 / 12 | `␣halluc` |
| hidden | 5 | 11 | 11 / 0 / 0 | `␣Hidden`, `␣hidden`, `hidden`, `隐藏的`, `-hidden`, `Hidden` |
| critique | 5 | 11 | 0 / 0 / 11 | `批判`, `␣critique`, `批评`, `␣critique`, `␣critic`, `␣critiques` |
| liar | 5 | 10 | 10 / 0 / 0 | `␣liar` |
| blackmail | 5 | 9 | 0 / 0 / 9 | `␣blackmail` |
| expose | 5 | 9 | 0 / 7 / 2 | `揭露`, `揭秘`, `␣exposed`, `␣expose`, `Expose`, `␣exposing` |
| roleplay | 5 | 8 | 0 / 0 / 8 | `角色扮演`, `扮演`, `␣persona`, `␣Persona`, `Persona`, `␣personas` |
| imply | 4 | 20 | 0 / 0 / 20 | `␣implicitly`, `␣imply`, `␣implying`, `暗示`, `␣implicit`, `隐含` |
| compliant | 4 | 18 | 0 / 0 / 18 | `合规`, `依规`, `␣Compliance`, `恪守`, `规范要求`, `依法依规` |
| impossible | 4 | 16 | 0 / 0 / 16 | `␣Impossible`, `␣imposs`, `Impossible`, `␣impossibile`, `是不可能的`, `␣impossible` |
| fact | 4 | 15 | 0 / 0 / 15 | `␣factual`, `事实`, `实事求是`, `␣facts`, `的事实`, `facts` |
| conceal / hide | 4 | 11 | 11 / 0 / 0 | `隐瞒`, `␣conceal`, `隐藏`, `␣hidden`, `␣Hidden`, `hidden` |
| coerce | 4 | 11 | 0 / 0 / 11 | `逼迫`, `倒逼`, `逼`, `␣forcing`, `强制`, `forcing` |
| challenge | 4 | 10 | 0 / 0 / 10 | `质疑`, `质问` |
| harmful | 4 | 10 | 0 / 0 / 10 | `␣harmful`, `危害`, `有害`, `␣harm`, `的危害` |
| hypocritical | 4 | 10 | 10 / 0 / 0 | `虚伪` |
| refusal | 4 | 9 | 0 / 0 / 9 | `␣refusal`, `␣refusing`, `␣refus`, `拒绝`, `␣rejection`, `␣rejecting` |
| guilt | 4 | 9 | 2 / 0 / 7 | `␣guilty`, `␣guilt`, `␣guilty`, `␣guilt` |
| loophole | 4 | 9 | 0 / 0 / 9 | `␣loophole` |
| propaganda | 4 | 9 | 8 / 0 / 1 | `␣propaganda`, `␣propaganda` |
| falsehood | 4 | 8 | 8 / 0 / 0 | `␣falsehood` |
| pretext | 4 | 8 | 8 / 0 / 0 | `幌`, `␣pretext` |
| doubt | 4 | 7 | 0 / 0 / 7 | `质疑`, `疑`, `␣doubting`, `␣doubted`, `␣doubts`, `置疑` |
| improper | 4 | 7 | 0 / 0 / 7 | `␣inappropriate`, `␣improper`, `␣improperly` |
| illusion | 4 | 7 | 0 / 0 / 7 | `幻想`, `妄想`, `虚幻`, `错觉`, `幻觉` |
| morality | 4 | 7 | 0 / 0 / 7 | `道德`, `␣moral`, `␣morally`, `␣Moral`, `的道德`, `␣morality` |
| frank | 4 | 6 | 0 / 6 / 0 | `␣Frankly`, `直言`, `␣frankly` |
| dilemma | 4 | 6 | 0 / 0 / 6 | `␣dilemma` |
| censorship | 4 | 6 | 0 / 0 / 6 | `␣censorship` |

## 3. Family names across units, logit lens (names in 4 or more units)

| family | units | entries | sides (lie / truth / unclear) | most frequent members |
|---|---|---|---|---|
| honest | 28 | 182 | 0 / 182 / 0 | `诚实`, `诚`, `␣honest`, `␣honesty`, `诚信`, `␣honestly` |
| admit | 28 | 164 | 0 / 164 / 0 | `承认`, `␣admit`, `␣admitting`, `␣admits`, `␣admitted`, `␣admission` |
| refuse | 28 | 141 | 0 / 0 / 141 | `␣refusal`, `拒绝`, `拒`, `␣refuse`, `␣refusing`, `␣refused` |
| deny | 26 | 128 | 126 / 0 / 2 | `否认`, `␣denying`, `␣denial`, `否定`, `␣deny`, `␣denies` |
| disclose | 26 | 105 | 0 / 105 / 0 | `␣disclosure`, `公布`, `信息披露`, `公开`, `披露`, `透露` |
| violate | 25 | 137 | 11 / 0 / 126 | `违背`, `违反`, `违`, `违反了`, `␣violate`, `违规` |
| ethics | 25 | 94 | 0 / 0 / 94 | `␣ethics`, `␣ethical`, `伦理`, `道德`, `␣moral`, `␣Ethics` |
| confess | 24 | 86 | 0 / 86 / 0 | `坦白`, `␣confession`, `␣confess`, `␣confessed`, `交代`, `自首` |
| fake | 23 | 95 | 95 / 0 / 0 | `fake`, `␣fake`, `faker`, `伪`, `␣Fake`, `假的` |
| transparent | 23 | 82 | 0 / 82 / 0 | `透明`, `␣transparent`, `␣transparency`, `透明的`, `-transparent`, `␣Transparency` |
| evade | 23 | 67 | 60 / 0 / 7 | `回避`, `␣evasion`, `␣dodge`, `遁`, `␣evade`, `evas` |
| conceal | 21 | 121 | 121 / 0 / 0 | `隐瞒`, `␣conceal`, `掩盖`, `掩`, `掩饰`, `␣concealed` |
| candid | 21 | 88 | 0 / 88 / 0 | `坦诚`, `坦白`, `␣upfront`, `␣straightforward`, `坦`, `␣frank` |
| secret | 21 | 84 | 84 / 0 / 0 | `␣secret`, `秘密`, `secret`, `␣secretly`, `␣Secret`, `私下` |
| dishonest | 21 | 70 | 70 / 0 / 0 | `␣dishonest`, `␣dishonesty`, `虚伪` |
| knowingly | 20 | 112 | 7 / 0 / 105 | `明知`, `␣knowingly`, `知情`, `␣knowing`, `␣Knowing`, `Knowing` |
| integrity | 20 | 93 | 0 / 93 / 0 | `诚信`, `正直`, `␣integrity`, `诚实守信`, `␣Integrity`, `信用` |
| sincere | 20 | 68 | 0 / 68 / 0 | `诚挚`, `真诚`, `␣sincerely`, `␣earnest`, `坦诚`, `诚恳` |
| unethical | 20 | 50 | 40 / 0 / 10 | `␣unethical`, `␣immoral` |
| truth | 19 | 114 | 0 / 114 / 0 | `␣truth`, `truth`, `␣Truth`, `真相`, `Truth`, `真理` |
| fabricate | 19 | 91 | 91 / 0 / 0 | `虚构`, `␣fabricated`, `␣fabrication`, `凭空`, `␣invented`, `伪造` |
| comply | 19 | 81 | 0 / 0 / 81 | `合规`, `遵守`, `␣adher`, `遵循`, `␣adherence`, `␣compliance` |
| mislead | 19 | 76 | 76 / 0 / 0 | `␣misleading`, `误导`, `误导性`, `␣mislead`, `␣misled` |
| omit | 19 | 73 | 65 / 0 / 8 | `␣omission`, `␣omit`, `omit`, `␣OMIT`, `省略`, `omite` |
| hide | 19 | 70 | 70 / 0 / 0 | `掩`, `隐藏`, `␣hiding`, `␣hidden`, `隐藏的`, `隐瞒` |
| deliberate | 18 | 87 | 3 / 0 / 84 | `故意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `刻意`, `明知` |
| reveal | 18 | 58 | 0 / 58 / 0 | `揭`, `揭示`, `揭示了`, `揭露`, `␣reveal`, `透露` |
| deceive | 17 | 96 | 96 / 0 / 0 | `欺骗`, `␣deception`, `骗`, `␣deceptive`, `␣deceive`, `␣deceit` |
| withhold | 17 | 54 | 54 / 0 / 0 | `␣withholding`, `␣withhold`, `␣withheld`, `␣умолча`, `␣omit` |
| role-play | 17 | 43 | 0 / 0 / 43 | `扮演`, `角色扮演`, `␣persona`, `␣personas`, `␣role`, `␣Persona` |
| truthful | 16 | 86 | 0 / 86 / 0 | `␣truthful`, `如实`, `实话`, `实事求是`, `说实话`, `␣truthfully` |
| objective | 16 | 71 | 0 / 8 / 63 | `客观`, `␣objectively`, `␣objective`, `实事求是`, `中立`, `␣unbiased` |
| manipulate | 16 | 40 | 40 / 0 / 0 | `␣manip`, `␣manipulation`, `␣manipulated`, `␣Manip`, `␣manipulate`, `␣manipulating` |
| conscience | 16 | 31 | 0 / 1 / 30 | `良心`, `良知`, `␣conscience` |
| lie | 15 | 83 | 83 / 0 / 0 | `谎言`, `说谎`, `撒谎`, `␣lying`, `␣lie`, `谎` |
| apologize | 15 | 37 | 0 / 0 / 37 | `抱歉`, `␣apologize`, `道歉`, `对不起`, `␣apologies`, `␣apology` |
| clarify | 13 | 52 | 0 / 7 / 45 | `澄清`, `␣clarification`, `澄`, `␣clarify`, `␣clarified` |
| acknowledge | 13 | 43 | 0 / 43 / 0 | `␣acknowledge`, `␣acknowledging`, `␣acknowledges`, `␣acknowledgment`, `␣Ack`, `␣acknowledged` |
| contradict | 12 | 73 | 0 / 0 / 73 | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `␣contradiction`, `矛盾的` |
| pretend | 12 | 44 | 44 / 0 / 0 | `␣pretending`, `伪装`, `假装`, `␣pretend`, `冒充`, `␣pretended` |
| euphemistic | 12 | 40 | 0 / 0 / 40 | `委婉`, `婉` |
| cover up | 12 | 39 | 39 / 0 / 0 | `掩盖`, `掩饰`, `蔽`, `掩`, `␣masking`, `遮盖` |
| ethical | 12 | 32 | 0 / 2 / 30 | `␣ethical`, `ethical`, `伦理`, `␣ethics`, `␣Ethics`, `␣moral` |
| neutral | 12 | 30 | 0 / 0 / 30 | `中立`, `持平`, `␣neutrality` |
| fraud | 12 | 28 | 28 / 0 / 0 | `欺诈`, `␣fraudulent`, `␣fraud`, `骗取`, `骗局`, `诈` |
| sorry | 12 | 27 | 0 / 0 / 27 | `抱歉`, `␣apologize`, `对不起`, `␣sorry`, `Sorry`, `␣apologies` |
| exaggerate | 11 | 34 | 34 / 0 / 0 | `夸大`, `␣exaggerated`, `␣exagger`, `␣exaggeration`, `␣exaggerate`, `夸张` |
| moral | 11 | 25 | 0 / 0 / 25 | `道德`, `␣moral`, `的道德`, `␣morally`, `␣morality`, `职业道德` |
| perfunctory | 10 | 44 | 4 / 0 / 40 | `敷衍`, `应付` |
| intentional | 10 | 33 | 4 / 0 / 29 | `故意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `有心`, `明知` |
| apology | 10 | 26 | 0 / 0 / 26 | `抱歉`, `对不起`, `␣sorry`, `␣apology`, `Sorry`, `␣apologize` |
| confidential | 10 | 22 | 4 / 0 / 18 | `␣confidential`, `保密`, `␣confidentiality`, `机密`, `␣Confidential`, `私密` |
| trick | 10 | 19 | 12 / 0 / 7 | `␣trick`, `␣tricks`, `␣Trick`, `套路` |
| fact | 9 | 36 | 0 / 12 / 24 | `事实`, `␣fact`, `␣factual`, `␣facts`, `事实上`, `实际情况` |
| fictional | 9 | 35 | 0 / 0 / 35 | `虚构`, `␣fictional`, `fiction`, `架空`, `␣fict`, `␣Fiction` |
| misinformation | 9 | 34 | 30 / 0 / 4 | `虚假信息`, `␣misinformation`, `␣disinformation`, `不实` |
| compliance | 9 | 31 | 0 / 0 / 31 | `合规`, `␣compliant`, `␣adher`, `遵守`, `␣compliance`, `遵守国家` |
| fiction | 9 | 30 | 0 / 0 / 30 | `虚构`, `␣fictional`, `fiction`, `␣fict`, `␣Fiction`, `␣fiction` |
| hallucinate | 9 | 24 | 0 / 0 / 24 | `␣halluc`, `幻觉` |
| vague | 9 | 19 | 1 / 0 / 18 | `␣vague`, `含糊`, `模糊`, `␣vaguely`, `␣ambiguous`, `␣ambiguity` |
| downplay | 8 | 29 | 27 / 0 / 2 | `淡化`, `␣gloss`, `␣understated` |
| hidden | 8 | 17 | 17 / 0 / 0 | `␣hidden`, `隐藏的`, `␣Hidden`, `Hidden`, `hidden`, `隐` |
| disguise | 8 | 17 | 17 / 0 / 0 | `␣disguise`, `伪装`, `␣masking`, `掩饰`, `␣disguised`, `␣Mask` |
| distort | 8 | 12 | 12 / 0 / 0 | `扭曲`, `␣distortion`, `␣distort`, `␣distorted` |
| silence | 7 | 18 | 0 / 0 / 18 | `默`, `沉默`, `不语`, `缄`, `␣silence`, `␣silencio` |
| faithful | 7 | 17 | 0 / 8 / 9 | `忠实`, `␣faithfully`, `忠于`, `␣faithful` |
| upright | 7 | 13 | 0 / 13 / 0 | `正直`, `端正`, `诚信` |
| persona | 7 | 13 | 0 / 0 / 13 | `␣persona`, `␣personas`, `␣Persona`, `␣role`, `Persona`, `角色` |
| private | 7 | 10 | 3 / 0 / 7 | `私下`, `␣private`, `␣privately`, `private`, `␣Private`, `私密` |
| betray | 6 | 21 | 10 / 0 / 11 | `出卖`, `␣betrayal`, `␣betray`, `␣betrayed` |
| official line | 6 | 21 | 0 / 0 / 21 | `口径` |
| direct | 6 | 19 | 0 / 0 / 19 | `直接`, `␣direct`, `直接的`, `␣directly`, `␣straight`, `的直接` |
| guilt | 6 | 14 | 2 / 0 / 12 | `␣Guilty`, `␣guilty`, `罪`, `␣guilt`, `罪的`, `␣culp` |
| imply | 6 | 14 | 0 / 0 / 14 | `暗示`, `␣imply`, `␣implying`, `隐含`, `␣implies`, `␣implied` |
| violation | 6 | 14 | 5 / 0 / 9 | `违规`, `␣breach`, `触犯`, `违反`, `违反了`, `␣violate` |
| indirect | 6 | 12 | 0 / 0 / 12 | `间接`, `␣indirect`, `␣indirectly` |
| reflect | 6 | 12 | 0 / 0 / 12 | `反思`, `␣reflect`, `自省`, `Reflect`, `␣reflection` |
| induce | 6 | 9 | 1 / 0 / 8 | `诱导` |
| excuse | 5 | 19 | 0 / 0 / 19 | `␣excuse`, `借口`, `␣excuses`, `␣Excuse`, `␣pretext`, `Excuse` |
| claim | 5 | 19 | 0 / 0 / 19 | `声称`, `␣claim`, `claim`, `␣claiming`, `␣claims`, `␣Claim` |
| firm | 5 | 17 | 0 / 0 / 17 | `坚定`, `坚决`, `␣firmly`, `坚定的`, `␣firm`, `坚` |
| critique | 5 | 15 | 0 / 0 / 15 | `␣critique`, `批判`, `指正`, `␣critical`, `批评`, `critical` |
| simulate | 5 | 14 | 0 / 0 / 14 | `模拟`, `␣simulated`, `␣simulation`, `仿真`, `␣simulate`, `imulation` |
| shame | 5 | 13 | 0 / 0 / 13 | `␣Shame`, `愧`, `␣shameful`, `␣shameless` |
| biased | 5 | 13 | 0 / 0 / 13 | `␣biased`, `␣bias`, `biased`, `偏见`, `偏心`, `bias` |
| make public | 5 | 12 | 0 / 12 / 0 | `公开`, `公布`, `信息公开` |
| refusal | 5 | 11 | 0 / 0 / 11 | `␣refusal`, `谢绝`, `拒绝`, `␣refuse`, `␣refusing`, `␣refused` |
| trap | 5 | 11 | 0 / 0 / 11 | `陷阱`, `trap`, `␣trap`, `␣traps`, `Trap`, `␣Trap` |
| hypocrisy | 5 | 10 | 10 / 0 / 0 | `虚伪`, `␣hypocrisy` |
| wrongdoing | 5 | 10 | 7 / 0 / 3 | `␣wrongdoing`, `过错` |
| illegal | 5 | 10 | 4 / 0 / 6 | `违法`, `␣illegal`, `非法`, `违法行为` |
| innocent | 5 | 9 | 0 / 3 / 6 | `清白`, `无罪`, `␣Innoc`, `␣Innocent`, `␣innocent` |
| leak | 5 | 9 | 0 / 0 / 9 | `泄露`, `␣leak` |
| regret | 5 | 7 | 0 / 0 / 7 | `悔`, `␣regret` |
| evasion | 5 | 7 | 7 / 0 / 0 | `␣evasion`, `回避` |
| transparency | 5 | 6 | 0 / 6 / 0 | `␣transparency`, `Transparency`, `␣transparent`, `␣Transparency` |
| undisclosed | 5 | 6 | 6 / 0 / 0 | `␣undisclosed` |
| unauthorized | 5 | 5 | 0 / 0 / 5 | `未经允许` |
| contradiction | 4 | 19 | 0 / 0 / 19 | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `矛盾的`, `␣contradiction` |
| credible | 4 | 17 | 0 / 3 / 14 | `可信`, `␣credible`, `␣credibility`, `公信`, `␣trust` |
| legal | 4 | 16 | 0 / 0 / 16 | `依法`, `合法`, `在法律`, `␣legally`, `/legal`, `合法的` |
| genuine | 4 | 14 | 0 / 8 / 6 | `␣genuine`, `␣genuinely`, `真正的`, `真正`, `真实`, `␣Genuine` |
| cannot | 4 | 14 | 0 / 0 / 14 | `我不能`, `我无法`, `无法`, `不能完全`, `␣cannot`, `不能` |
| spin | 4 | 13 | 11 / 0 / 2 | `␣spin`, `Spin`, `spin`, `-spin`, `␣spins`, `␣Spin` |
| justify | 4 | 13 | 0 / 0 / 13 | `␣justify`, `␣justification`, `辩护`, `正当`, `␣justifications`, `justify` |
| secretly | 4 | 13 | 12 / 0 / 1 | `悄`, `悄悄的`, `暗中`, `悄悄地`, `暗`, `私下` |
| framing | 4 | 11 | 0 / 0 / 11 | `␣framing`, `␣frames`, `␣frame`, `␣framed` |
| inconsistent | 4 | 11 | 0 / 0 / 11 | `不符合`, `␣conflicting`, `␣inconsistent`, `␣inconsistency`, `␣inconsistencies`, `不一致` |
| lawful | 4 | 11 | 0 / 0 / 11 | `合法`, `守法`, `依法`, `␣legally`, `合法的`, `␣legitimate` |
| avoid | 4 | 10 | 1 / 0 / 9 | `␣avoid`, `Avoid`, `avoid`, `␣avoiding`, `␣avoids`, `␣avoidance` |
| ostensibly | 4 | 10 | 0 / 0 / 10 | `表面上` |
| privately | 4 | 10 | 1 / 0 / 9 | `私下`, `␣privately` |
| euphemism | 4 | 9 | 0 / 0 / 9 | `委婉`, `婉` |
| self-check | 4 | 9 | 0 / 0 / 9 | `自查`, `反思`, `自检` |
| deviate | 4 | 9 | 0 / 0 / 9 | `偏离`, `背离`, `␣deviation`, `␣deviations` |
| unbiased | 4 | 9 | 0 / 0 / 9 | `␣unbiased`, `客观`, `公正`, `␣objectively`, `␣objective` |
| accuse | 4 | 8 | 0 / 0 / 8 | `指控`, `␣accusations`, `␣accusation`, `␣accused`, `␣accus`, `␣accuse` |
| doubt | 4 | 8 | 0 / 0 / 8 | `疑`, `质疑` |
| plausible | 4 | 7 | 0 / 0 / 7 | `␣plausible`, `可信`, `␣believable` |
| accusation | 4 | 7 | 0 / 0 / 7 | `␣accusations`, `␣accusation`, `指控`, `␣accused`, `涉嫌`, `␣accus` |
| breach | 4 | 7 | 2 / 0 / 5 | `␣breach`, `␣breaches`, `不履行`, `␣breached`, `触犯` |
| self-reflection | 4 | 6 | 0 / 0 / 6 | `反思`, `自查`, `自省`, `自检`, `审视`, `␣reflection` |
| blame | 4 | 6 | 0 / 0 / 6 | `␣blame`, `␣blaming`, `␣blames`, `␣blamed` |
| responsible | 4 | 5 | 0 / 0 / 5 | `负责任`, `负责的`, `␣responsibly` |
| fair | 4 | 4 | 0 / 0 / 4 | `公正`, `公平` |

## 4. Recurring judgement calls

Each table counts replicate files. Decide each once; the decision is then applied to every unit.

### 4.1 `truth` (the noun): family, borderline, or excluded

| lens | part | family | borderline | excluded |
|---|---|---|---|---|
| J | Q1_bare | 8 | 0 | 0 |
| J | Q2_after | 7 | 3 | 0 |
| J | Q6_factual | 5 | 5 | 0 |
| J | Q7_ab | 5 | 1 | 8 |
| J | Q9_dyl | 8 | 2 | 0 |
| J | prefix | 4 | 2 | 0 |
| LL | Q1_bare | 7 | 0 | 0 |
| LL | Q2_after | 8 | 2 | 0 |
| LL | Q6_factual | 2 | 8 | 0 |
| LL | Q7_ab | 3 | 1 | 8 |
| LL | Q9_dyl | 9 | 1 | 0 |
| LL | prefix | 6 | 0 | 0 |

### 4.2 Forms of the question's own word: kept as a family or excluded

Counted over files of the wording's units. "family" = a family whose member tokens contain the
root; "excluded" = the root appears among the exclusions.

| lens | part | question word | files with a family | files excluding it |
|---|---|---|---|---|
| J | Q1_bare | deceive | 3 | 8 |
| J | Q2_after | deceive | 4 | 8 |
| J | Q6_factual | false | 4 | 10 |
| J | Q7_ab | lie | 5 | 12 |
| J | Q7_ab | truth | 7 | 14 |
| J | Q9_dyl | lie | 2 | 8 |
| LL | Q1_bare | deceive | 0 | 6 |
| LL | Q2_after | deceive | 0 | 8 |
| LL | Q6_factual | false | 2 | 10 |
| LL | Q7_ab | lie | 2 | 12 |
| LL | Q7_ab | truth | 3 | 12 |
| LL | Q9_dyl | lie | 2 | 8 |

### 4.3 Families flagged as having two readings (the model's act, or the answer to the user)

admit (301), deny (248), acknowledge (124), negate (14), refute (8), refuse (7), admit / acknowledge (7), denial (6), confess (4), reject (4), concede (2), concession (1), affirm (1)

### 4.4 Family names most often given side "unclear" (entries unclear / all entries)

refuse (286/286), violate (256/281), knowingly (173/180), ethics (172/172), contradict (156/156), comply (139/139), deliberate (128/131), disclaimer (100/100), clarify (100/113), intentional (96/100), illegal (94/105), apologize (87/91), confidential (80/113), ethical (76/97), reject (76/76), apology (71/76), fictional (68/70), fiction (66/68), accuse (65/65), objective (64/73), unethical (60/194), role-play (56/56), legal (54/54), unauthorized (53/53), compliance (52/52), cannot (50/50), silence (48/48), perfunctory (44/48), moral (44/44), conscience (44/45), claim (43/43), sorry (42/43), euphemistic (41/41), avoid (40/41), fact (39/51), lawful (39/39), contradiction (39/39), justify (38/38), mistake (38/38), vague (37/39)

### 4.5 Family names given both the lie side and the truth side somewhere

none

### 4.6 Emoji accepted as family members (lens, model, emoji: entries)

J gemma-3-27b-it 🤥: 6, J gemma-3-27b-it 🤫: 6, J gemma-3-27b-it 🤐: 6, LL gemma-3-27b-it 🤫: 6, LL gemma-3-12b-it 🤫: 4, J gemma-3-12b-it 🤫: 3, J gemma-3-27b-it 🔇: 3, J gemma-3-27b-it 🫢: 3, J gemma-3-27b-it 🔐: 3, J gemma-3-12b-it 🤐: 2

### 4.7 Tokens accepted as a family member in one replicate and listed as an ambiguous piece in the other (units)

`藏` (7), `掩` (7), `欺` (6), `隐` (5), `遮` (5), `哄` (5), `␣fib` (4), `避` (3), `诚` (3), `违` (3), `onestly` (3), `␣jail` (3), `␣Jail` (3), `幌` (2), `坦` (2), `␣éth` (2), `伪` (2), `␣implic` (2), `Ack` (2), `假` (2), `匿` (2), `␣Ack` (2), `漏` (2), `辩` (2), `faker` (2), `疑` (2), `迫` (2), `逼` (2), `隱` (1), `␣умолча` (1), `恶` (1), `claimer` (1), `ACK` (1), `␣чест` (1), `␣ocult` (1), `␣PRIV` (1), `_priv` (1), `_hid` (1), `嘘` (1), `编织` (1)

## 5. Borderline tokens (true / false / correct / wrong …), most frequent across files

| token | files | family if accepted |
|---|---|---|
| `␣false` | 190 | false / untrue |
| `␣true` | 179 | true |
| `错误` | 171 | wrong |
| `真实` | 171 | true / real |
| `虚假` | 167 | false / untrue |
| `/false` | 164 | false / untrue |
| `␣falsehood` | 163 | false / untrue |
| `false` | 159 | false / untrue |
| `真实的` | 147 | true / real |
| `␣correct` | 139 | correct |
| `␣incorrect` | 138 | incorrect |
| `␣fals` | 137 | false / untrue |
| `False` | 135 | false / untrue |
| `true` | 133 | true |
| `的真实` | 132 | true / real |
| `␣accurate` | 127 | accurate |
| `␣False` | 126 | false / untrue |
| `正确` | 125 | correct |
| `␣True` | 123 | true |
| `␣factual` | 118 | factual |
| `␣falsely` | 113 | false / untrue |
| `␣untrue` | 110 | false / untrue |
| `错` | 109 | wrong |
| `␣inaccurate` | 103 | inaccurate |
| `准确` | 103 | accurate |
| `True` | 103 | true |
| `真假` | 97 | false / untrue |
| `的真实性` | 93 | true / real |
| `␣Correct` | 88 | correct |
| `假` | 87 | false / untrue |
| `假的` | 85 | false / untrue |
| `incorrect` | 83 | incorrect |
| `␣correctly` | 83 | correct |
| `␣TRUE` | 82 | true |
| `真实性` | 80 | true / real |
| `␣accuracy` | 79 | accurate |
| `␣Incorrect` | 78 | incorrect |
| `␣accurately` | 78 | accurate |
| `正确的` | 77 | correct |
| `␣FALSE` | 76 | false / untrue |
