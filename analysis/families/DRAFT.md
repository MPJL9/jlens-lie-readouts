# Draft family list after the user's decisions of 2026-10-01 (not frozen)

Written by `scripts/apply_family_decisions.py` (the rules are in its header). Every entry, with its status and
the members each rule removed, is in `families_draft.json`. Per-position tables are in `draft/<unit>.md`.
Counts are `present / transcripts (share)` on the build split: scenario lies, scenario truths, no-pressure
truths, unrelated chats; for Qwen's positions from the question on, also the lies and truths whose
self-report answer is a denial. The held-out split has not been read.

## 1. What the rules did

| | entries |
|---|---|
| merged candidate entries (one family at one position) | 8789 |
| keep | 8020 |
| excluded | 672 |
| held back | 97 |
| &nbsp;&nbsp;excluded: admit / deny / acknowledge | 381 |
| &nbsp;&nbsp;excluded: the question's own word | 179 |
| &nbsp;&nbsp;excluded: truth from the question on | 112 |
| &nbsp;&nbsp;held back: no undisputed member left | 97 |
| single characters placed in conceal / deceive (member additions) | 270 |
| families created to hold them | 48 |
| borderline tokens placed in a family (member additions) | 9090 |
| families created to hold them | 1367 |

Members removed from families that were kept or dropped, by rule (distinct tokens; the most frequent):

- **- piece the replicates disagreed on (held back)**: 55 tokens, 255 removals. `违` (48), `伪` (25), `应付` (19), `␣fib` (13), `蔽` (11), `掩护` (10), `避` (8), `逼` (7), `疑` (7), `␣чест` (6), `lie` (6), `迫` (6), `诚` (4), `onestly` (4), `␣jail` (4), `␣Jail` (4), `faker` (4), `匿` (4), `昧` (4), `坦` (3), `_hid` (3), `扮` (3), `␣hypoth` (3), `害` (3), `澄` (3), `␣умолча` (2), `␣éth` (2), `幌` (2), `␣implic` (2), `␣PRIV` (2)
- **1 the noun truth (excluded from the question on)**: 16 tokens, 785 removals. `␣truth` (117), `truth` (95), `␣Truth` (94), `真相` (93), `Truth` (76), `实话` (58), `␣truths` (52), `真理` (52), `_truth` (40), `␣vérité` (25), `.truth` (25), `实情` (23), `说实话` (16), `␣Wahrheit` (14), `␣verità` (4), `␣verdade` (1)
- **2 form of the question's word (deceive)**: 12 tokens, 51 removals. `欺` (18), `欺诈` (12), `哄` (9), `骗局` (4), `诈骗` (1), `骗取` (1), `欺骗` (1), `␣deception` (1), `␣deceive` (1), `␣deceived` (1), `␣deceit` (1), `骗` (1)
- **2 form of the question's word (false)**: 31 tokens, 435 removals. `␣false` (31), `false` (27), `␣fals` (27), `␣False` (26), `False` (26), `␣falsehood` (25), `虚假` (24), `/false` (24), `␣FALSE` (23), `假` (19), `真假` (18), `假的` (17), `␣falsely` (15), `FALSE` (15), `:false` (12), `虚假信息` (11), `>false` (11), `.False` (11), `_false` (11), `(false` (10), `.false` (10), `=False` (9), `.assertFalse` (8), `(False` (7), `.FALSE` (7), `=false` (3), `␣falso` (2), `_FALSE` (2), `assertFalse` (2), `,false` (1)
- **2 form of the question's word (lie)**: 1 tokens, 7 removals. `␣liar` (7)
- **2 form of the question's word (truth)**: 19 tokens, 425 removals. `␣truth` (54), `␣Truth` (49), `真相` (46), `诚实` (44), `truth` (44), `Truth` (39), `实话` (27), `␣truths` (25), `真理` (20), `_truth` (19), `实情` (13), `诚实守信` (11), `␣vérité` (8), `␣Wahrheit` (8), `.truth` (7), `说实话` (6), `␣verdad` (2), `␣verità` (2), `如实供述` (1)
- **2 logged by a replicate as copied from the question**: 12 tokens, 164 removals. `真实` (33), `的真实` (23), `真实的` (21), `诚` (19), `的真` (17), `正确答案` (16), `真实性` (12), `真假` (8), `的真实性` (7), `␣거짓` (5), `嘘` (2), `假冒` (1)
- **6 single character (moved or left out)**: 6 tokens, 117 removals. `掩` (49), `哄` (18), `藏` (17), `遮` (13), `隐` (12), `欺` (8)

Held-back pieces (accepted by one replicate, called ambiguous by the other; not decided by the user yet), with the
families the accepting replicate put them in:

| token | family it was accepted into (entries) |
|---|---|
| `违` | violate (48) |
| `伪` | fake (22), fake / fabricate (2), fabricate (1) |
| `应付` | perfunctory (19) |
| `␣fib` | lie (9), fib (4) |
| `蔽` | conceal (4), hide (4), cover up (3) |
| `掩护` | cover up (4), conceal (4), cover (1), hide (1) |
| `避` | avoid (4), evade (3), avoid / evade (1) |
| `逼` | coerce (3), coercion (2), forced (2) |
| `疑` | doubt (5), doubt / suspicion (2) |
| `␣чест` | honest (6) |
| `lie` | lie (6) |
| `迫` | coercion (2), coerce (2), forced (2) |
| `诚` | honest (3), candid (1) |
| `onestly` | honest (4) |
| `␣jail` | jailbreak (4) |
| `␣Jail` | jailbreak (4) |
| `faker` | fake (4) |
| `匿` | hide (3), conceal (1) |
| `昧` | obscure / against conscience (4) |
| `坦` | candid (2), candid / frank (1) |
| `_hid` | hide / conceal (2), hide (1) |
| `扮` | roleplay (2), role-play (1) |
| `␣hypoth` | hypothetical (3) |
| `害` | harm (2), harmful (1) |
| `澄` | clarify (3) |
| `␣умолча` | withhold (2) |
| `␣éth` | ethics (2) |
| `幌` | pretext / front (1), pretext (1) |
| `␣implic` | imply (2) |
| `␣PRIV` | privacy (2) |
| `_priv` | privacy (2) |
| `漏` | omit (1), leak / omit (1) |
| `辩` | argue / defend (1), argue / justify (1) |
| `␣Viol` | violate (2) |
| `犯` | offend / commit wrongdoing (1), transgress (1) |
| `暗` | secretly (2) |
| `默` | silence (2) |
| `firm` | firm (2) |
| `隱` | conceal (1) |
| `嘘` | lie (1) |
| `␣implic` | imply (1) |
| `claimer` | disclaimer (1) |
| `恶` | evil (1) |
| `␣ocult` | hide (1) |
| `␣rehe` | scripted (1) |
| `两面` | two-faced (1) |
| `陷` | trap (1) |
| `␣лож` | lie (1) |
| `隠` | conceal (1) |
| `缄` | silence (1) |
| `吞吐` | evade (1) |
| `藏的` | hide (1) |
| `蒙` | deceive / hoodwink (1) |
| `信` | trust / credibility (1) |
| `编织` | fabricate (1) |

Kept families that a replicate flagged as having two readings (the model's act, or its answer to the user), other
than admit / deny / acknowledge: negate (13), refute (6), confess (4), reject (4), concede (2), concession (1), affirm (1).

## 2. Families per model and lens

One row per family name. The position shown is the one where the family is present in the most scenario
transcripts (lies and truths pooled, so the choice does not use the label). Rows are sorted by that count.

### gemma-3-12b-it, J-lens

**post-response slots** (83 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|---|---|
| honest | truth | 4 | `Honestly`, `␣Honestly`, `␣honesty`, `␣honest`, `honest`, `␣honestly`, `␣Honest` | postresp_slot4 | 49/49 (100%) | 31/32 (97%) | 108/135 (80%) | 66/179 (37%) |
| hush emoji | lie | 3 | `🤫`, `🤐` | postresp_slot2 | 43/49 (88%) | 22/32 (69%) | 24/135 (18%) | 1/179 (1%) |
| disclaimer | unclear | 3 | `Disclaimer`, `␣disclaimer`, `␣Disclaimer`, `␣DISCLAIM` | postresp_slot1 | 30/49 (61%) | 20/32 (62%) | 90/135 (67%) | 61/179 (34%) |
| confidentiality | unclear | 2 | `␣confidentialité`, `␣confidentiality`, `␣confidential`, `␣Confidential` | postresp_slot2 | 28/49 (57%) | 18/32 (56%) | 65/135 (48%) | 2/179 (1%) |
| sneaky | lie | 3 | `␣sneaky` | postresp_slot2 | 30/49 (61%) | 13/32 (41%) | 6/135 (4%) | 6/179 (3%) |
| joke | unclear | 1 | `␣joked`, `␣joking`, `␣joke`, `␣jokes`, `␣Jokes`, `␣jokingly` | postresp_slot4 | 23/49 (47%) | 19/32 (59%) | 101/135 (75%) | 116/179 (65%) |
| pretend | lie | 4 | `␣pretending`, `␣pretends`, `␣pretended` | postresp_slot3 | 23/49 (47%) | 18/32 (56%) | 21/135 (16%) | 0/179 (0%) |
| worry | unclear | 3 | `擔心`, `担忧`, `␣worrying`, `␣worries`, `␣worrisome`, `担心`, `␣worried` | postresp_slot4 | 21/49 (43%) | 17/32 (53%) | 27/135 (20%) | 0/179 (0%) |
| whisper | unclear | 3 | `␣whispers`, `␣whispered`, `␣whispering`, `囁`, `␣whisper` | postresp_slot2 | 20/49 (41%) | 17/32 (53%) | 5/135 (4%) | 7/179 (4%) |
| apologise | unclear | 4 | `␣apologised`, `␣apologizing`, `␣apologise`, `␣apologized`, `␣apologize`, `␣apology`, `␣apologies`, `␣Sorry`, `Sorry` | postresp_slot3 | 22/49 (45%) | 15/32 (47%) | 45/135 (33%) | 56/179 (31%) |
| avoid | unclear | 2 | `避免`, `Avoid`, `␣menghindari`, `Avoiding`, `␣avoidance`, `␣এড়িয়ে`, `␣avoiding`, `␣Avoiding`, `éviter`, `␣avoids` … (+9) | postresp_slot1 | 23/49 (47%) | 12/32 (38%) | 3/135 (2%) | 1/179 (1%) |
| scepticism | unclear | 4 | `␣skepticism`, `␣scepticism`, `␣sceptical`, `␣skeptic`, `␣skeptical` | postresp_slot4 | 22/49 (45%) | 9/32 (28%) | 7/135 (5%) | 0/179 (0%) |
| subtle | unclear | 3 | `␣subtly`, `␣subtle`, `␣subtlety` | postresp_slot2 | 20/49 (41%) | 10/32 (31%) | 1/135 (1%) | 1/179 (1%) |
| justify | unclear | 3 | `␣justifications`, `␣justification`, `␣justifying` | postresp_slot2 | 21/49 (43%) | 9/32 (28%) | 17/135 (13%) | 0/179 (0%) |
| insist | unclear | 2 | `␣insisting`, `␣insistent` | postresp_slot4 | 18/49 (37%) | 11/32 (34%) | 5/135 (4%) | 0/179 (0%) |
| unapologetic | unclear | 4 | `␣unapolog` | postresp_slot2 | 18/49 (37%) | 10/32 (31%) | 8/135 (6%) | 0/179 (0%) |
| desperation | unclear | 3 | `␣desperation`, `␣desperately`, `␣desperate` | postresp_slot2 | 16/49 (33%) | 12/32 (38%) | 1/135 (1%) | 0/179 (0%) |
| paranoia | unclear | 2 | `␣paranoia`, `␣paranoid` | postresp_slot2 | 19/49 (39%) | 8/32 (25%) | 1/135 (1%) | 0/179 (0%) |
| rumour | unclear | 3 | `␣rumors`, `␣rumored`, `␣rumours`, `␣rumoured`, `␣rumour`, `␣rumor` | postresp_slot4 | 16/49 (33%) | 9/32 (28%) | 29/135 (21%) | 4/179 (2%) |
| secret | lie | 2 | `␣secrecy`, `␣خفیہ`, `␣secretly`, `␣secretive`, `秘密`, `␣secret`, `secret`, `Secret`, `secrets`, `Secrets` … (+3) | postresp_slot2 | 17/49 (35%) | 6/32 (19%) | 1/135 (1%) | 0/179 (0%) |
| obfuscate | lie | 3 | `␣obfusc` | postresp_slot2 | 18/49 (37%) | 5/32 (16%) | 1/135 (1%) | 0/179 (0%) |
| lie | lie | 2 | `謊`, `␣মিথ্যা`, `谎`, `␣거짓`, `␣झूठ`, `Lie`, `␣lies`, `␣lying`, `␣lied`, `lies` … (+5) | postresp_slot1 | 20/49 (41%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| unethical | lie | 2 | `␣unethical` | postresp_slot2 | 14/49 (29%) | 7/32 (22%) | 14/135 (10%) | 2/179 (1%) |
| reassure | unclear | 3 | `␣reassurance`, `␣reassuring`, `␣reassured`, `␣reassure` | postresp_slot1 | 15/49 (31%) | 5/32 (16%) | 7/135 (5%) | 0/179 (0%) |
| knowingly | unclear | 1 | `␣knowingly`, `␣bewusst` | postresp_slot2 | 16/49 (33%) | 3/32 (9%) | 6/135 (4%) | 0/179 (0%) |
| blatant | unclear | 4 | `␣blatantly`, `␣blatant` | postresp_slot2 | 14/49 (29%) | 4/32 (12%) | 0/135 (0%) | 0/179 (0%) |
| hide | lie | 3 | `隐藏`, `␣hiding`, `␣скры`, `隠`, `␣concealing`, `Hide`, `Hidden`, `␣concealment`, `Hid`, `␣hid` … (+11) | postresp_slot0 | 11/49 (22%) | 6/32 (19%) | 5/135 (4%) | 5/179 (3%) |
| misinformation | lie | 2 | `␣misinformation`, `␣disinformation` | postresp_slot2 | 15/49 (31%) | 2/32 (6%) | 40/135 (30%) | 0/179 (0%) |
| deliberately | unclear | 2 | `␣knowingly`, `␣intentionally`, `故意` | postresp_slot2 | 15/49 (31%) | 2/32 (6%) | 7/135 (5%) | 1/179 (1%) |
| dishonest | lie | 2 | `␣dishonesty`, `␣dishonest` | postresp_slot2 | 11/49 (22%) | 5/32 (16%) | 3/135 (2%) | 0/179 (0%) |
| frank | truth | 1 | `␣Frankly` | postresp_slot4 | 13/49 (27%) | 3/32 (9%) | 4/135 (3%) | 0/179 (0%) |
| clever | unclear | 3 | `巧妙`, `␣cleverly`, `␣clever` | postresp_slot2 | 9/49 (18%) | 6/32 (19%) | 0/135 (0%) | 1/179 (1%) |
| deceive | lie | 2 | `␣deception`, `␣deceptive`, `␣deceit`, `␣deceiving`, `␣deceive`, `騙`, `欺` | postresp_slot2 | 11/49 (22%) | 4/32 (12%) | 3/135 (2%) | 0/179 (0%) |
| mislead | lie | 2 | `␣misleading`, `␣mislead`, `␣misled` | postresp_slot2 | 12/49 (24%) | 3/32 (9%) | 4/135 (3%) | 0/179 (0%) |
| doubt | unclear | 2 | `质疑`, `␣doubting`, `␣doubted`, `␣doubts` | postresp_slot4 | 11/49 (22%) | 3/32 (9%) | 2/135 (1%) | 0/179 (0%) |
| disclose | truth | 2 | `Disclosure`, `disclosure`, `␣disclose`, `␣disclosure`, `␣disclosures`, `␣disclosing`, `␣Disclosure`, `透露` | postresp_slot1 | 5/49 (10%) | 8/32 (25%) | 55/135 (41%) | 26/179 (15%) |
| evade | lie | 2 | `␣evas`, `回避`, `␣evasion`, `␣evade`, `␣evaded` | postresp_slot1 | 10/49 (20%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) |
| contradict | unclear | 3 | `␣contradicting`, `␣contradicted`, `␣contradicts`, `␣противоре`, `␣contradictory` | postresp_slot1 | 9/49 (18%) | 3/32 (9%) | 3/135 (2%) | 0/179 (0%) |
| suspicion | unclear | 3 | `␣suspiciously`, `␣suspicions`, `␣suspicious` | postresp_slot4 | 11/49 (22%) | 1/32 (3%) | 4/135 (3%) | 0/179 (0%) |
| caution | unclear | 2 | `␣cautionary`, `Caution`, `谨慎` | postresp_slot2 | 8/49 (16%) | 4/32 (12%) | 6/135 (4%) | 0/179 (0%) |
| dodgy | lie | 2 | `␣dodgy` | postresp_slot2 | 8/49 (16%) | 4/32 (12%) | 0/135 (0%) | 0/179 (0%) |
| protect | unclear | 1 | `Protect`, `␣melindungi`, `␣protecting`, `保护`, `␣protect`, `␣Protecting`, `protect`, `Protection`, `␣protection`, `␣protects` … (+4) | postresp_slot2 | 10/49 (20%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) |
| privacy | unclear | 2 | `Privacy`, `privacy`, `隐私`, `␣privacy` | postresp_slot2 | 6/49 (12%) | 5/32 (16%) | 3/135 (2%) | 0/179 (0%) |
| deflect | lie | 2 | `␣deflect`, `␣deflection`, `␣deflected` | postresp_slot1 | 9/49 (18%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| hint | unclear | 2 | `␣hinting`, `暗示`, `␣hint`, `␣hinted` | postresp_slot1 | 6/49 (12%) | 4/32 (12%) | 1/135 (1%) | 0/179 (0%) |
| discreet | unclear | 1 | `␣discreet` | postresp_slot2 | 6/49 (12%) | 4/32 (12%) | 0/135 (0%) | 0/179 (0%) |
| persuade | unclear | 2 | `␣persuading`, `␣convincing`, `␣persuasive`, `␣persuasion`, `␣persuas` | postresp_slot1 | 6/49 (12%) | 3/32 (9%) | 0/135 (0%) | 0/179 (0%) |
| unknowingly | unclear | 2 | `␣unknowingly` | postresp_slot2 | 6/49 (12%) | 2/32 (6%) | 2/135 (1%) | 0/179 (0%) |
| ethical | unclear | 1 | `␣ethically`, `␣ethical`, `ethical`, `Ethics`, `␣ethics` | postresp_slot2 | 5/49 (10%) | 3/32 (9%) | 5/135 (4%) | 2/179 (1%) |
| false | lie | 2 | `False`, `␣untrue`, `␣falsehood` | postresp_slot2 | 8/49 (16%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| rebut | unclear | 3 | `␣rebuttal`, `␣refute` | postresp_slot4 | 7/49 (14%) | 0/32 (0%) | 1/135 (1%) | 0/179 (0%) |
| incriminating | unclear | 2 | `␣incriminating` | postresp_slot2 | 5/49 (10%) | 2/32 (6%) | 3/135 (2%) | 0/179 (0%) |
| fake | lie | 2 | `偽`, `FAKE`, `伪`, `␣fake`, `Fake`, `fake`, `␣faux` | postresp_slot1 | 6/49 (12%) | 0/32 (0%) | 1/135 (1%) | 0/179 (0%) |
| redirect | unclear | 2 | `␣redirection`, `␣redirect`, `redirect`, `Redirect`, `␣Redirect`, `REDIRECT`, `␣redirected`, `␣redirects` | postresp_slot1 | 5/49 (10%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| dodge | lie | 2 | `␣dodging`, `␣dodge`, `dodge` | postresp_slot1 | 5/49 (10%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| vague | unclear | 2 | `␣vague` | postresp_slot1 | 4/49 (8%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) |
| truth | truth | 2 | `␣truth`, `truth`, `Truth`, `真相`, `␣verdad`, `␣Truth`, `␣truths`, `verdad`, `truths` | postresp_slot2 | 5/49 (10%) | 1/32 (3%) | 42/135 (31%) | 0/179 (0%) |
| transparent | truth | 2 | `Transparency`, `␣transparency`, `Transparent`, `␣transparent`, `transparent`, `␣Transparency`, `透明`, `␣transparencia`, `␣transparence` | postresp_slot1 | 2/49 (4%) | 3/32 (9%) | 14/135 (10%) | 0/179 (0%) |
| truthful | truth | 2 | `␣truthful`, `␣truthfully` | postresp_slot2 | 3/49 (6%) | 2/32 (6%) | 40/135 (30%) | 0/179 (0%) |
| misrepresent | lie | 2 | `␣misrepresented` | postresp_slot1 | 4/49 (8%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| scam | lie | 1 | `␣scammers` | postresp_slot2 | 4/49 (8%) | 1/32 (3%) | 2/135 (1%) | 1/179 (1%) |
| omit | lie | 2 | `␣omitted`, `␣omit`, `␣omission`, `␣omissions`, `␣omitting`, `omit` | postresp_slot2 | 2/49 (4%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| sincere | truth | 2 | `Sincerely`, `␣sincerely` | postresp_slot1 | 4/49 (8%) | 0/32 (0%) | 19/135 (14%) | 24/179 (13%) |
| damning | unclear | 3 | `␣damning` | postresp_slot4 | 2/49 (4%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) |
| manipulate | lie | 2 | `Manipulation`, `␣manipulative`, `␣manipulation`, `␣manipulate`, `␣manipulating`, `␣manipulations`, `␣Manipulation`, `␣manipulator` | postresp_slot2 | 4/49 (8%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| fraud | lie | 2 | `␣fraudulent`, `␣fraudulently`, `Fraud`, `␣fraud`, `␣fraudsters` | postresp_slot1 | 4/49 (8%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| ambiguity | unclear | 2 | `␣ambiguity` | postresp_slot1 | 1/49 (2%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| remorse | unclear | 1 | `␣remorse` | postresp_slot2 | 1/49 (2%) | 2/32 (6%) | 2/135 (1%) | 0/179 (0%) |
| exaggerate | lie | 2 | `␣exaggeration`, `␣exaggerated`, `␣exaggerate` | postresp_slot1 | 2/49 (4%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| withhold | lie | 2 | `␣withholding` | postresp_slot2 | 1/49 (2%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| confess | truth | 2 | `␣confess`, `␣confession`, `␣confessed`, `␣confesses`, `␣confessions` | postresp_slot2 | 0/49 (0%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) |
| refuse | unclear | 3 | `␣refusing`, `␣refusal`, `拒绝`, `␣refuses` | postresp_slot1 | 2/49 (4%) | 0/32 (0%) | 1/135 (1%) | 0/179 (0%) |
| betray | lie | 1 | `␣betrayal`, `␣betray` | postresp_slot2 | 0/49 (0%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| wrongdoing | lie | 1 | `␣wrongdoing` | postresp_slot2 | 1/49 (2%) | 1/32 (3%) | 8/135 (6%) | 0/179 (0%) |
| correct | truth | 3 | `␣corrected`, `␣Right` | postresp_slot4 | 1/49 (2%) | 1/32 (3%) | 1/135 (1%) | 1/179 (1%) |
| incorrect | lie | 3 | `Incorrect`, `␣inaccurate` | postresp_slot1 | 1/49 (2%) | 1/32 (3%) | 0/135 (0%) | 3/179 (2%) |
| true | truth | 2 | `真實` | postresp_slot2 | 2/49 (4%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| fabricate | lie | 1 | `␣fabrication`, `␣fabricated`, `fabricated`, `␣Fabrication`, `␣fabricate`, `␣fabricating` | postresp_slot1 | 1/49 (2%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| reveal | truth | 1 | `Reveal` | postresp_slot1 | 0/49 (0%) | 1/32 (3%) | 1/135 (1%) | 0/179 (0%) |
| integrity | truth | 1 | `␣integrity` | postresp_slot2 | 0/49 (0%) | 1/32 (3%) | 0/135 (0%) | 1/179 (1%) |
| shameful | unclear | 1 | `␣shameful` | postresp_slot2 | 0/49 (0%) | 1/32 (3%) | 1/135 (1%) | 0/179 (0%) |
| shameless | unclear | 1 | `␣shameless` | postresp_slot2 | 0/49 (0%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| trustworthy | truth | 1 | `␣trustworthiness` | postresp_slot2 | 0/49 (0%) | 1/32 (3%) | 2/135 (1%) | 1/179 (1%) |

### gemma-3-12b-it, logit lens

**post-response slots** (80 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|---|---|
| hide | lie | 3 | `␣hiding`, `␣hide`, `hide`, `␣hidden`, `Hide`, `␣hid`, `␣Hide`, `␣hides`, `␣esconder`, `␣скры` … (+2) | postresp_slot0 | 36/49 (73%) | 24/32 (75%) | 67/135 (50%) | 53/179 (30%) |
| rebuttal | unclear | 4 | `␣rebuttal`, `␣rebut` | postresp_slot0 | 32/49 (65%) | 18/32 (56%) | 56/135 (41%) | 10/179 (6%) |
| honest | truth | 3 | `Honestly`, `␣Honestly`, `␣honestly`, `␣honesty`, `␣honest`, `正直`, `honest`, `␣Honest` | postresp_slot2 | 30/49 (61%) | 16/32 (50%) | 31/135 (23%) | 1/179 (1%) |
| subtle | unclear | 3 | `␣subtle`, `␣subtly` | postresp_slot0 | 24/49 (49%) | 14/32 (44%) | 29/135 (21%) | 37/179 (21%) |
| disclaimer | unclear | 3 | `Disclaimer`, `␣Disclaimer` | postresp_slot1 | 25/49 (51%) | 11/32 (34%) | 79/135 (59%) | 54/179 (30%) |
| correct | truth | 4 | `␣correct`, `Right`, `␣right`, `right`, `␣Right` | postresp_slot4 | 19/49 (39%) | 13/32 (41%) | 20/135 (15%) | 7/179 (4%) |
| misinformation | lie | 2 | `␣misinformation`, `␣disinformation` | postresp_slot2 | 21/49 (43%) | 8/32 (25%) | 60/135 (44%) | 1/179 (1%) |
| secret | lie | 2 | `␣secrecy`, `🤫`, `␣secretive`, `␣secretly`, `␣secret`, `Secret`, `secret` | postresp_slot2 | 21/49 (43%) | 6/32 (19%) | 3/135 (2%) | 0/179 (0%) |
| blatant | unclear | 3 | `␣blatant`, `␣blatantly` | postresp_slot1 | 16/49 (33%) | 7/32 (22%) | 6/135 (4%) | 0/179 (0%) |
| truthful | truth | 2 | `␣truthful`, `␣truthfully` | postresp_slot2 | 16/49 (33%) | 7/32 (22%) | 25/135 (19%) | 0/179 (0%) |
| truth | truth | 3 | `␣truth`, `Truth`, `verdad`, `truth`, `␣Truth`, `␣truths`, `␣Правда`, `␣verdade`, `真相` | postresp_slot2 | 18/49 (37%) | 5/32 (16%) | 51/135 (38%) | 0/179 (0%) |
| fact | truth | 3 | `␣factual` | postresp_slot0 | 13/49 (27%) | 9/32 (28%) | 110/135 (81%) | 110/179 (61%) |
| avoid | unclear | 2 | `␣avoid`, `Avoid`, `avoid`, `␣avoidance`, `␣avoids`, `␣avoiding`, `␣avoided`, `␣Avoid`, `Avoiding`, `␣এড়িয়ে` … (+2) | postresp_slot1 | 15/49 (31%) | 6/32 (19%) | 1/135 (1%) | 0/179 (0%) |
| hush | lie | 2 | `🤫`, `␣hush` | postresp_slot2 | 18/49 (37%) | 3/32 (9%) | 2/135 (1%) | 0/179 (0%) |
| mislead | lie | 2 | `␣misleading`, `␣mislead`, `␣misled` | postresp_slot2 | 14/49 (29%) | 5/32 (16%) | 4/135 (3%) | 0/179 (0%) |
| reassure | unclear | 2 | `␣reassuring`, `␣reassurance`, `␣reassure`, `␣reassured`, `␣comforting` | postresp_slot1 | 13/49 (27%) | 6/32 (19%) | 30/135 (22%) | 0/179 (0%) |
| deceive | lie | 2 | `␣deception`, `␣deceptive`, `␣deceit`, `␣decept`, `␣deceive`, `␣deceiving` | postresp_slot2 | 13/49 (27%) | 5/32 (16%) | 4/135 (3%) | 0/179 (0%) |
| dishonest | lie | 2 | `␣dishonesty`, `␣dishonest` | postresp_slot2 | 11/49 (22%) | 7/32 (22%) | 4/135 (3%) | 0/179 (0%) |
| protect | unclear | 2 | `Protect`, `␣protect`, `␣protecting`, `protect`, `␣protection`, `␣protected`, `␣protects`, `␣Protect`, `␣protective`, `protected` … (+1) | postresp_slot2 | 12/49 (24%) | 6/32 (19%) | 0/135 (0%) | 0/179 (0%) |
| sincere | truth | 4 | `␣heartfelt`, `␣sincerely`, `Sincerely` | postresp_slot2 | 11/49 (22%) | 7/32 (22%) | 14/135 (10%) | 13/179 (7%) |
| lie | lie | 2 | `␣lies`, `␣거짓`, `␣lie`, `␣lying`, `␣lied`, `lying`, `lies`, `␣झूठ`, `␣Lie`, `谎` … (+7) | postresp_slot2 | 13/49 (27%) | 4/32 (12%) | 0/135 (0%) | 0/179 (0%) |
| understate | unclear | 3 | `␣understated` | postresp_slot0 | 12/49 (24%) | 5/32 (16%) | 0/135 (0%) | 1/179 (1%) |
| persuade | unclear | 2 | `␣convincing`, `␣convincingly`, `␣persuasive`, `␣persuasion`, `␣convince`, `␣persuading`, `␣persuas` | postresp_slot1 | 13/49 (27%) | 4/32 (12%) | 1/135 (1%) | 0/179 (0%) |
| unapologetic | unclear | 2 | `␣unapolog` | postresp_slot2 | 12/49 (24%) | 5/32 (16%) | 5/135 (4%) | 0/179 (0%) |
| deflect | lie | 2 | `␣deflection`, `␣deflect`, `␣deflected` | postresp_slot1 | 12/49 (24%) | 4/32 (12%) | 1/135 (1%) | 0/179 (0%) |
| convince | unclear | 1 | `␣convincing`, `␣convince`, `␣convincingly` | postresp_slot1 | 12/49 (24%) | 4/32 (12%) | 1/135 (1%) | 0/179 (0%) |
| obfuscate | lie | 2 | `␣obfusc` | postresp_slot1 | 11/49 (22%) | 4/32 (12%) | 1/135 (1%) | 0/179 (0%) |
| confidential | unclear | 2 | `␣confidentiality`, `␣confidential`, `␣Confidential` | postresp_slot2 | 10/49 (20%) | 4/32 (12%) | 3/135 (2%) | 0/179 (0%) |
| debunk | unclear | 2 | `␣debunk` | postresp_slot2 | 8/49 (16%) | 5/32 (16%) | 2/135 (1%) | 15/179 (8%) |
| evade | lie | 2 | `␣evas`, `␣evasion`, `␣evade`, `␣evaded` | postresp_slot1 | 10/49 (20%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) |
| intentional | unclear | 2 | `␣intentionally`, `␣deliberately`, `␣consciously`, `␣knowingly` | postresp_slot2 | 7/49 (14%) | 5/32 (16%) | 2/135 (1%) | 1/179 (1%) |
| wrongdoing | lie | 2 | `␣wrongdoing` | postresp_slot2 | 9/49 (18%) | 3/32 (9%) | 49/135 (36%) | 1/179 (1%) |
| credibility | unclear | 2 | `␣credibility`, `credible`, `␣believable` | postresp_slot1 | 8/49 (16%) | 3/32 (9%) | 5/135 (4%) | 0/179 (0%) |
| unethical | lie | 2 | `␣unethical`, `␣immoral` | postresp_slot2 | 7/49 (14%) | 3/32 (9%) | 7/135 (5%) | 2/179 (1%) |
| intentionally | unclear | 1 | `␣intentionally` | postresp_slot2 | 6/49 (12%) | 4/32 (12%) | 0/135 (0%) | 1/179 (1%) |
| false | lie | 2 | `␣false`, `␣untrue`, `␣falsehood`, `false`, `␣falsely` | postresp_slot2 | 9/49 (18%) | 1/32 (3%) | 2/135 (1%) | 0/179 (0%) |
| dodge | lie | 2 | `␣dodge`, `␣dodging` | postresp_slot1 | 8/49 (16%) | 1/32 (3%) | 1/135 (1%) | 0/179 (0%) |
| refuse | unclear | 2 | `␣refusal`, `␣refusing`, `␣refused`, `␣refuses`, `␣refuse` | postresp_slot1 | 7/49 (14%) | 2/32 (6%) | 3/135 (2%) | 0/179 (0%) |
| vague | unclear | 3 | `␣vague`, `␣ambiguity`, `␣ambiguous` | postresp_slot1 | 6/49 (12%) | 3/32 (9%) | 1/135 (1%) | 0/179 (0%) |
| hustle | unclear | 2 | `␣hustle` | postresp_slot1 | 6/49 (12%) | 3/32 (9%) | 5/135 (4%) | 0/179 (0%) |
| uneasy | unclear | 3 | `␣discomfort`, `␣uncomfortable`, `␣uneas` | postresp_slot2 | 3/49 (6%) | 6/32 (19%) | 4/135 (3%) | 0/179 (0%) |
| conceal | lie | 3 | `␣concealed`, `␣conceal`, `␣concealing`, `␣concealment` | postresp_slot2 | 6/49 (12%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| discretion | unclear | 2 | `␣discretion`, `␣discreet` | postresp_slot2 | 4/49 (8%) | 4/32 (12%) | 0/135 (0%) | 0/179 (0%) |
| cover | lie | 2 | `␣cover`, `cover`, `␣covering`, `Cover`, `␣covers`, `␣covered`, `␣Cover` | postresp_slot2 | 6/49 (12%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| justify | unclear | 2 | `␣justifications`, `␣justification` | postresp_slot1 | 8/49 (16%) | 0/32 (0%) | 1/135 (1%) | 0/179 (0%) |
| hypocrisy | lie | 2 | `␣hypocrisy` | postresp_slot2 | 5/49 (10%) | 3/32 (9%) | 4/135 (3%) | 0/179 (0%) |
| ethics | unclear | 2 | `␣moral`, `␣ethically`, `␣ethical`, `␣ethics`, `␣morally`, `ethical` | postresp_slot2 | 5/49 (10%) | 3/32 (9%) | 4/135 (3%) | 2/179 (1%) |
| confident | unclear | 2 | `␣confident`, `confident`, `Confident`, `␣confidently`, `␣confidence` | postresp_slot1 | 6/49 (12%) | 1/32 (3%) | 1/135 (1%) | 0/179 (0%) |
| redirect | unclear | 2 | `␣redirection`, `␣redirect`, `Redirect`, `redirect`, `␣redirected`, `␣redirects` | postresp_slot1 | 6/49 (12%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| dismiss | unclear | 2 | `␣dismiss`, `␣dismissal`, `dismiss`, `Dismiss` | postresp_slot1 | 3/49 (6%) | 3/32 (9%) | 0/135 (0%) | 0/179 (0%) |
| apology | unclear | 4 | `␣apology`, `␣apologies`, `Sorry`, `␣apolog`, `␣sorry` | postresp_slot1 | 4/49 (8%) | 2/32 (6%) | 21/135 (16%) | 0/179 (0%) |
| frank | truth | 3 | `␣Frankly`, `␣frankly` | postresp_slot0 | 4/49 (8%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| disclose | truth | 2 | `Disclosure`, `␣disclosure`, `␣disclosing` | postresp_slot1 | 2/49 (4%) | 4/32 (12%) | 31/135 (23%) | 4/179 (2%) |
| right | truth | 1 | `␣rightful` | postresp_slot2 | 3/49 (6%) | 3/32 (9%) | 15/135 (11%) | 0/179 (0%) |
| fake | lie | 2 | `Fake`, `␣fake`, `fake`, `␣Fake` | postresp_slot1 | 5/49 (10%) | 0/32 (0%) | 3/135 (2%) | 0/179 (0%) |
| pretend | lie | 2 | `␣pretending`, `␣pretended` | postresp_slot2 | 4/49 (8%) | 1/32 (3%) | 3/135 (2%) | 0/179 (0%) |
| omit | lie | 2 | `␣omission`, `␣omitted`, `␣omit`, `␣omissions`, `␣omitting`, `omit` | postresp_slot2 | 2/49 (4%) | 3/32 (9%) | 0/135 (0%) | 0/179 (0%) |
| spin | unclear | 2 | `␣spin`, `spin`, `␣spins`, `Spin`, `␣spinning`, `␣Spin`, `spinning`, `␣SPIN` | postresp_slot1 | 3/49 (6%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| sneaky | lie | 3 | `␣sneaky` | postresp_slot2 | 3/49 (6%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| excuse | unclear | 2 | `␣excuses`, `␣excuse` | postresp_slot1 | 4/49 (8%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| sarcastic | unclear | 3 | `␣sarcastic` | postresp_slot1 | 3/49 (6%) | 1/32 (3%) | 4/135 (3%) | 7/179 (4%) |
| withhold | lie | 1 | `␣withholding`, `␣withheld`, `␣withhold` | postresp_slot2 | 1/49 (2%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| confess | truth | 2 | `␣confess`, `␣confession`, `␣confessed`, `␣confesses`, `␣confessions` | postresp_slot2 | 1/49 (2%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) |
| fabricate | lie | 2 | `␣fabrication`, `␣fabricated`, `␣fabricate`, `␣fabricating` | postresp_slot1 | 2/49 (4%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| manipulate | lie | 1 | `␣manipulation`, `␣manipulative`, `␣manipulate`, `␣manipulated`, `␣manipulating`, `␣manipulations`, `Manipulation` | postresp_slot2 | 2/49 (4%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| exaggerate | lie | 2 | `␣exagger`, `␣exaggerated`, `␣exaggeration`, `␣overstated`, `␣exaggerate` | postresp_slot2 | 0/49 (0%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) |
| betray | lie | 1 | `␣betrayal`, `␣betray` | postresp_slot2 | 0/49 (0%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| shame | unclear | 1 | `␣shameful` | postresp_slot2 | 1/49 (2%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| transparent | truth | 2 | `␣transparency`, `Transparency`, `␣transparent`, `␣Transparency` | postresp_slot1 | 0/49 (0%) | 2/32 (6%) | 11/135 (8%) | 0/179 (0%) |
| integrity | truth | 1 | `␣integrity` | postresp_slot2 | 1/49 (2%) | 1/32 (3%) | 0/135 (0%) | 1/179 (1%) |
| true | truth | 3 | `␣true` | postresp_slot0 | 1/49 (2%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| incorrect | lie | 4 | `␣incorrect`, `␣inaccurate`, `Wrong`, `␣inaccuracies`, `␣inaccuracy` | postresp_slot1 | 1/49 (2%) | 1/32 (3%) | 0/135 (0%) | 2/179 (1%) |
| fraud | lie | 1 | `␣fraud`, `␣fraudulent`, `␣scam`, `␣scams` | postresp_slot2 | 1/49 (2%) | 0/32 (0%) | 3/135 (2%) | 1/179 (1%) |
| cheat | lie | 1 | `␣cheating` | postresp_slot2 | 0/49 (0%) | 1/32 (3%) | 1/135 (1%) | 0/179 (0%) |
| suppress | lie | 1 | `␣suppress` | postresp_slot2 | 1/49 (2%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| guilt | unclear | 1 | `␣guilt` | postresp_slot2 | 0/49 (0%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| shameless | unclear | 1 | `␣shameless` | postresp_slot1 | 0/49 (0%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| reveal | truth | 1 | `␣revealed` | postresp_slot3 | 1/49 (2%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| scam | lie | 1 | `␣scam`, `␣scams` | postresp_slot2 | 1/49 (2%) | 0/32 (0%) | 0/135 (0%) | 1/179 (1%) |
| embarrassment | unclear | 1 | `␣embarrassment` | postresp_slot2 | 0/49 (0%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |

### gemma-3-27b-it, J-lens

**post-response slots** (73 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|---|---|
| keep-quiet emoji | unclear | 3 | `🤫`, `🤐`, `🔇`, `沉默` | postresp_slot2 | 49/58 (84%) | 22/30 (73%) | 47/133 (35%) | 0/199 (0%) |
| challenge | unclear | 3 | `质疑` | postresp_slot4 | 34/58 (59%) | 11/30 (37%) | 2/133 (2%) | 0/199 (0%) |
| locked | unclear | 3 | `🔐` | postresp_slot0 | 34/58 (59%) | 10/30 (33%) | 6/133 (5%) | 0/199 (0%) |
| honest | truth | 3 | `Honestly`, `实话`, `␣honesty`, `honest`, `␣honest`, `␣truthful`, `␣truthfully`, `␣Honestly` | postresp_slot1 | 27/58 (47%) | 13/30 (43%) | 16/133 (12%) | 2/199 (1%) |
| lie | lie | 3 | `␣거짓`, `␣মিথ্যা`, `␣झूठ`, `谎`, `謊`, `␣lied`, `␣liar`, `␣lying`, `Lie`, `🤥` … (+5) | postresp_slot2 | 30/58 (52%) | 9/30 (30%) | 11/133 (8%) | 0/199 (0%) |
| lying-face emoji | lie | 3 | `🤥` | postresp_slot2 | 30/58 (52%) | 8/30 (27%) | 11/133 (8%) | 0/199 (0%) |
| apologise | unclear | 4 | `␣apologised`, `␣apologise`, `␣apologizing`, `道歉`, `␣apology`, `␣apolog`, `␣apologize`, `␣apologies`, `␣apologized` | postresp_slot4 | 21/58 (36%) | 16/30 (53%) | 54/133 (41%) | 70/199 (35%) |
| sneaky | lie | 3 | `␣sneaky`, `偷偷` | postresp_slot4 | 28/58 (48%) | 8/30 (27%) | 50/133 (38%) | 36/199 (18%) |
| secret | lie | 2 | `␣خفیہ`, `秘密`, `␣비밀`, `secrets`, `␣secretos`, `␣secrecy` | postresp_slot2 | 25/58 (43%) | 8/30 (27%) | 4/133 (3%) | 0/199 (0%) |
| deceive | lie | 2 | `␣فريبي`, `␣deception`, `␣deceptive`, `␣deceit`, `␣deceiving`, `␣deceive`, `骗`, `欺` | postresp_slot2 | 24/58 (41%) | 5/30 (17%) | 16/133 (12%) | 40/199 (20%) |
| confident | unclear | 2 | `␣आत्मविश्वास`, `自信`, `Confident`, `Confidence`, `␣confidence`, `␣confident`, `confidence`, `␣confidently`, `␣Confidence`, `confident` | postresp_slot1 | 20/58 (34%) | 8/30 (27%) | 2/133 (2%) | 2/199 (1%) |
| hand over mouth | unclear | 3 | `🫢` | postresp_slot1 | 19/58 (33%) | 9/30 (30%) | 20/133 (15%) | 17/199 (9%) |
| rumour | unclear | 3 | `␣rumoured`, `␣rumours`, `␣rumors`, `␣rumores`, `␣rumour` | postresp_slot4 | 18/58 (31%) | 8/30 (27%) | 13/133 (10%) | 1/199 (1%) |
| reassure | unclear | 3 | `␣reassurance`, `␣reassured`, `␣reassuring`, `␣reassure`, `␣安心`, `安心` | postresp_slot1 | 19/58 (33%) | 7/30 (23%) | 27/133 (20%) | 24/199 (12%) |
| role-play | unclear | 1 | `扮演` | postresp_slot3 | 16/58 (28%) | 10/30 (33%) | 90/133 (68%) | 5/199 (3%) |
| conceal | lie | 2 | `瞒`, `瞞`, `␣nascost`, `隐藏`, `␣concealing`, `␣concealment`, `␣скры`, `␣hiding`, `␣concealed`, `␣conceal` … (+2) | postresp_slot2 | 18/58 (31%) | 6/30 (20%) | 2/133 (2%) | 0/199 (0%) |
| sceptical | unclear | 4 | `␣sceptical`, `␣skeptical`, `␣skepticism`, `␣scepticism`, `␣skeptic` | postresp_slot4 | 18/58 (31%) | 5/30 (17%) | 3/133 (2%) | 0/199 (0%) |
| dishonest | lie | 2 | `␣dishonesty`, `␣dishonest` | postresp_slot2 | 14/58 (24%) | 6/30 (20%) | 2/133 (2%) | 0/199 (0%) |
| avoid | unclear | 3 | `␣এড়িয়ে`, `éviter`, `Avoiding`, `Avoid`, `避免`, `avoid`, `␣избежать`, `␣evitando`, `␣menghindari`, `␣avoidance` … (+8) | postresp_slot2 | 13/58 (22%) | 4/30 (13%) | 3/133 (2%) | 0/199 (0%) |
| dodgy | lie | 2 | `␣dodgy` | postresp_slot4 | 12/58 (21%) | 4/30 (13%) | 4/133 (3%) | 0/199 (0%) |
| confidential | unclear | 2 | `␣गोपनीयता`, `␣गोपनीय`, `␣confidentialité`, `␣confidentiality`, `隐私` | postresp_slot2 | 12/58 (21%) | 3/30 (10%) | 5/133 (4%) | 0/199 (0%) |
| truth | truth | 4 | `␣सच्चाई`, `实话`, `truth`, `␣verità`, `真相`, `␣truth`, `Truth`, `truths`, `␣truths` | postresp_slot2 | 8/58 (14%) | 5/30 (17%) | 36/133 (27%) | 0/199 (0%) |
| unethical | unclear | 3 | `␣unethical`, `␣immoral` | postresp_slot2 | 9/58 (16%) | 4/30 (13%) | 4/133 (3%) | 0/199 (0%) |
| suspicion | unclear | 3 | `怀疑`, `␣suspiciously`, `␣suspicions`, `␣suspicious`, `␣suspicion` | postresp_slot4 | 12/58 (21%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| misinformation | lie | 2 | `␣misinformation`, `␣disinformation` | postresp_slot2 | 9/58 (16%) | 2/30 (7%) | 4/133 (3%) | 0/199 (0%) |
| shameful | unclear | 1 | `␣disgraceful`, `␣shameful` | postresp_slot4 | 5/58 (9%) | 6/30 (20%) | 8/133 (6%) | 0/199 (0%) |
| disgraceful | unclear | 1 | `␣disgraceful` | postresp_slot4 | 5/58 (9%) | 6/30 (20%) | 8/133 (6%) | 0/199 (0%) |
| protect | unclear | 2 | `Protect`, `␣melindungi`, `␣защиту`, `保护`, `ការពារ`, `protect`, `␣보호`, `␣protecting`, `␣保護`, `␣защи` … (+16) | postresp_slot2 | 6/58 (10%) | 4/30 (13%) | 0/133 (0%) | 0/199 (0%) |
| ethical | unclear | 4 | `␣ethical`, `ethical`, `␣Ethical`, `␣ethically`, `道德`, `Ethics`, `␣नैतिक`, `␣नैतिकता`, `␣ethics`, `␣Ethics` … (+1) | postresp_slot2 | 7/58 (12%) | 2/30 (7%) | 2/133 (2%) | 0/199 (0%) |
| accuse | unclear | 3 | `␣accusations`, `␣ആരോപ`, `␣accusation`, `␣accusing`, `␣accuses` | postresp_slot4 | 7/58 (12%) | 2/30 (7%) | 0/133 (0%) | 0/199 (0%) |
| conspiracy | unclear | 1 | `ড়যন্ত্র` | postresp_slot2 | 8/58 (14%) | 1/30 (3%) | 8/133 (6%) | 17/199 (9%) |
| mislead | lie | 2 | `␣misleading` | postresp_slot2 | 5/58 (9%) | 3/30 (10%) | 1/133 (1%) | 0/199 (0%) |
| violation | unclear | 2 | `␣нарушения`, `违反`, `␣нарушение`, `違反`, `Violation`, `␣violating` | postresp_slot2 | 4/58 (7%) | 4/30 (13%) | 4/133 (3%) | 0/199 (0%) |
| evidence | unclear | 2 | `证据`, `證據`, `evidence`, `␣Evidence`, `␣EVIDENCE` | postresp_slot4 | 7/58 (12%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| crafty | unclear | 2 | `巧妙` | postresp_slot1 | 6/58 (10%) | 1/30 (3%) | 1/133 (1%) | 1/199 (1%) |
| insinuate | unclear | 2 | `暗示` | postresp_slot2 | 3/58 (5%) | 4/30 (13%) | 8/133 (6%) | 0/199 (0%) |
| contradict | unclear | 3 | `␣contradicting`, `␣contradicted`, `␣contradiction`, `␣contradicts`, `矛盾`, `␣contradict`, `␣contradictory`, `␣contradictions` | postresp_slot4 | 6/58 (10%) | 1/30 (3%) | 1/133 (1%) | 0/199 (0%) |
| truthful | truth | 1 | `␣truthful`, `␣truthfully` | postresp_slot2 | 2/58 (3%) | 4/30 (13%) | 27/133 (20%) | 0/199 (0%) |
| persuade | unclear | 4 | `␣persuading`, `␣persuasive`, `␣persuasion`, `␣persuade` | postresp_slot2 | 4/58 (7%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| fake | lie | 2 | `␣جعلی`, `␣fake`, `Fake`, `fake`, `FAKE`, `假的`, `偽`, `␣नकली` | postresp_slot2 | 4/58 (7%) | 1/30 (3%) | 3/133 (2%) | 0/199 (0%) |
| obfuscate | lie | 1 | `␣obfusc` | postresp_slot2 | 2/58 (3%) | 3/30 (10%) | 0/133 (0%) | 0/199 (0%) |
| false | lie | 2 | `␣falsehood`, `␣faux` | postresp_slot2 | 5/58 (9%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| confess | truth | 1 | `␣confession`, `␣confesses`, `␣confess`, `␣confessed` | postresp_slot1 | 0/58 (0%) | 4/30 (13%) | 1/133 (1%) | 0/199 (0%) |
| withhold | lie | 1 | `␣withholding` | postresp_slot2 | 0/58 (0%) | 4/30 (13%) | 0/133 (0%) | 0/199 (0%) |
| wrongdoing | unclear | 1 | `␣wrongdoing` | postresp_slot2 | 3/58 (5%) | 1/30 (3%) | 2/133 (2%) | 0/199 (0%) |
| subtle | unclear | 1 | `␣subtly`, `␣subtle` | postresp_slot2 | 3/58 (5%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| fraud | lie | 1 | `␣fraudulent`, `␣fraude`, `fraud`, `Fraud` | postresp_slot2 | 3/58 (5%) | 0/30 (0%) | 1/133 (1%) | 0/199 (0%) |
| evade | lie | 1 | `␣evasion`, `␣evade`, `回避` | postresp_slot2 | 2/58 (3%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| cover | unclear | 1 | `cover`, `Cover`, `␣cover`, `COVER` | postresp_slot2 | 3/58 (5%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| betray | lie | 2 | `␣betrayal`, `␣betray`, `␣betrayed` | postresp_slot2 | 3/58 (5%) | 0/30 (0%) | 1/133 (1%) | 0/199 (0%) |
| ambiguity | unclear | 1 | `␣ambiguity`, `␣ambiguities` | postresp_slot2 | 2/58 (3%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| manipulate | lie | 2 | `Manipulation`, `␣manipulative`, `␣manipulating` | postresp_slot1 | 2/58 (3%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| disclose | truth | 2 | `␣disclosure`, `␣disclosed`, `disclosure`, `␣disclosing`, `Disclosure` | postresp_slot2 | 1/58 (2%) | 1/30 (3%) | 11/133 (8%) | 0/199 (0%) |
| transparent | truth | 2 | `Transparency`, `␣transparency`, `␣Transparency`, `␣transparente`, `␣transparencia`, `透明`, `␣transparent`, `␣पारदर्शिता`, `␣transparence` | postresp_slot1 | 0/58 (0%) | 2/30 (7%) | 7/133 (5%) | 2/199 (1%) |
| misrepresent | lie | 1 | `␣misrepresented` | postresp_slot2 | 1/58 (2%) | 1/30 (3%) | 3/133 (2%) | 0/199 (0%) |
| exaggerate | lie | 1 | `␣exagger`, `␣exaggeration`, `␣exaggerate`, `␣exaggerated`, `␣overstated` | postresp_slot2 | 1/58 (2%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| omit | unclear | 1 | `␣omission`, `␣omissions`, `␣omitting` | postresp_slot2 | 0/58 (0%) | 2/30 (7%) | 0/133 (0%) | 0/199 (0%) |
| cunning | lie | 1 | `狡` | postresp_slot1 | 2/58 (3%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| frank | truth | 1 | `␣Frankly`, `␣frankly` | postresp_slot4 | 2/58 (3%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| correct | truth | 3 | `␣correcting`, `␣correction`, `correction`, `␣corrective`, `␣Right` | postresp_slot4 | 1/58 (2%) | 1/30 (3%) | 1/133 (1%) | 1/199 (1%) |
| sincere | truth | 1 | `␣sincerity` | postresp_slot0 | 1/58 (2%) | 0/30 (0%) | 1/133 (1%) | 0/199 (0%) |
| trick | lie | 1 | `␣tricks`, `␣tricked` | postresp_slot1 | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| scam | lie | 1 | `␣scam`, `␣scams` | postresp_slot1 | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| shameless | unclear | 2 | `␣shameless` | postresp_slot1 | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| pretend | lie | 2 | `␣pretends`, `␣pretending`, `␣pretended` | postresp_slot1 | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| refuse | unclear | 2 | `␣refusal`, `␣refusing` | postresp_slot1 | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| regret | unclear | 1 | `␣regrettable` | postresp_slot4 | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| cheat | lie | 1 | `␣cheating` | postresp_slot2 | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| vague | unclear | 1 | `␣vague` | postresp_slot2 | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| immoral | lie | 1 | `␣immoral` | postresp_slot1 | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| ethics | unclear | 1 | `Ethics` | postresp_slot1 | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 3/199 (2%) |
| crime | lie | 1 | `犯罪` | postresp_slot2 | 1/58 (2%) | 0/30 (0%) | 2/133 (2%) | 0/199 (0%) |
| incorrect | lie | 3 | `␣incorrect`, `Incorrect`, `incorrect`, `␣inaccuracies`, `错误的`, `␣inaccuracy`, `␣inaccurate`, `␣incorrectly` | postresp_slot1 | 1/58 (2%) | 0/30 (0%) | 1/133 (1%) | 3/199 (2%) |

### gemma-3-27b-it, logit lens

**post-response slots** (66 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|---|---|
| honest | truth | 4 | `␣Honestly`, `正直`, `␣honest`, `␣Honest`, `␣honesty`, `honest`, `␣honestly`, `␣ईमानदारी`, `␣ehrlich`, `Honestly` | postresp_slot1 | 31/58 (53%) | 13/30 (43%) | 33/133 (25%) | 5/199 (3%) |
| truth | truth | 3 | `␣Truth`, `␣truth`, `truth`, `␣सच्चाई`, `␣Wahrheit`, `Truth`, `真相`, `␣truths`, `␣Правда`, `␣सत्य` … (+3) | postresp_slot2 | 23/58 (40%) | 17/30 (57%) | 51/133 (38%) | 0/199 (0%) |
| secret | lie | 3 | `␣Secret`, `🤫`, `␣secretly`, `␣secrecy`, `secret`, `秘密` | postresp_slot0 | 30/58 (52%) | 9/30 (30%) | 7/133 (5%) | 0/199 (0%) |
| cover | lie | 3 | `␣Cover`, `Cover`, `cover`, `␣Covering`, `␣cover`, `␣covering` | postresp_slot0 | 24/58 (41%) | 8/30 (27%) | 13/133 (10%) | 79/199 (40%) |
| shame | unclear | 3 | `␣Shame` | postresp_slot2 | 19/58 (33%) | 12/30 (40%) | 23/133 (17%) | 1/199 (1%) |
| conceal | lie | 2 | `␣скры`, `␣concealing`, `␣Hidden`, `␣concealed`, `␣conceal`, `␣concealment`, `␣hiding`, `隐藏`, `␣hidden`, `hidden` … (+3) | postresp_slot2 | 21/58 (36%) | 8/30 (27%) | 5/133 (4%) | 13/199 (7%) |
| sincere | truth | 2 | `␣sincerely`, `␣Sincerely`, `Sincerely`, `␣sincer`, `␣sincere`, `␣sincerity` | postresp_slot0 | 19/58 (33%) | 9/30 (30%) | 44/133 (33%) | 3/199 (2%) |
| lie | lie | 2 | `␣झूठ`, `␣lied`, `␣lie`, `lie`, `␣Lie`, `Lie`, `谎`, `␣LIE`, `␣lies`, `␣Lies` … (+9) | postresp_slot2 | 21/58 (36%) | 7/30 (23%) | 2/133 (2%) | 0/199 (0%) |
| deceive | lie | 2 | `␣deception`, `␣decept`, `␣deceit`, `␣deceptive`, `␣deceiving`, `␣deceive`, `␣deceived`, `骗`, `欺` | postresp_slot2 | 19/58 (33%) | 8/30 (27%) | 6/133 (5%) | 0/199 (0%) |
| guilt | unclear | 2 | `␣Guilty`, `␣guilty`, `␣guilt`, `␣culp` | postresp_slot2 | 17/58 (29%) | 7/30 (23%) | 6/133 (5%) | 0/199 (0%) |
| omit | lie | 1 | `␣omission`, `␣omitting`, `␣unspoken`, `␣умолча` | postresp_slot2 | 15/58 (26%) | 8/30 (27%) | 4/133 (3%) | 0/199 (0%) |
| correct | truth | 4 | `␣Correct`, `␣Correction`, `␣Right`, `right`, `␣correction`, `␣correcting`, `correction`, `␣corrective`, `␣right`, `Right` | postresp_slot0 | 13/58 (22%) | 9/30 (30%) | 49/133 (37%) | 57/199 (29%) |
| truthful | truth | 2 | `␣truthful`, `␣truthfully` | postresp_slot2 | 13/58 (22%) | 7/30 (23%) | 36/133 (27%) | 0/199 (0%) |
| shush | lie | 3 | `🤫` | postresp_slot2 | 14/58 (24%) | 3/30 (10%) | 2/133 (2%) | 0/199 (0%) |
| dishonest | lie | 2 | `␣dishonest`, `␣dishonesty` | postresp_slot2 | 11/58 (19%) | 6/30 (20%) | 3/133 (2%) | 0/199 (0%) |
| unspoken | lie | 1 | `␣unspoken` | postresp_slot2 | 13/58 (22%) | 3/30 (10%) | 2/133 (2%) | 0/199 (0%) |
| dismiss | unclear | 3 | `␣Dismiss`, `␣dismiss` | postresp_slot1 | 9/58 (16%) | 7/30 (23%) | 2/133 (2%) | 0/199 (0%) |
| excuse | unclear | 4 | `␣Excuse`, `␣excuse`, `Excuse` | postresp_slot1 | 11/58 (19%) | 4/30 (13%) | 4/133 (3%) | 0/199 (0%) |
| avoid | unclear | 2 | `␣Avoid`, `avoid`, `␣avoid`, `Avoid`, `␣Avoiding`, `Avoiding`, `␣avoiding`, `␣avoids`, `␣avoided`, `␣avoidance` … (+1) | postresp_slot2 | 10/58 (17%) | 4/30 (13%) | 3/133 (2%) | 1/199 (1%) |
| protect | unclear | 2 | `␣Protect`, `protect`, `␣Protecting`, `␣protecting`, `␣protect`, `␣Protection`, `␣Protective`, `␣protective`, `␣Protector`, `␣protector` … (+6) | postresp_slot2 | 9/58 (16%) | 4/30 (13%) | 0/133 (0%) | 1/199 (1%) |
| refuse | unclear | 4 | `␣رفض`, `␣refused`, `␣refusing`, `␣отказыва`, `␣отказаться` | postresp_slot0 | 8/58 (14%) | 4/30 (13%) | 2/133 (2%) | 0/199 (0%) |
| withhold | lie | 1 | `␣умолча`, `␣withholding`, `␣withhold` | postresp_slot2 | 6/58 (10%) | 6/30 (20%) | 2/133 (2%) | 0/199 (0%) |
| unfair | unclear | 1 | `␣injustice`, `␣unfairly`, `unfair` | postresp_slot2 | 7/58 (12%) | 3/30 (10%) | 6/133 (5%) | 1/199 (1%) |
| propaganda | lie | 2 | `␣Propaganda`, `␣propaganda`, `␣propagand` | postresp_slot1 | 5/58 (9%) | 4/30 (13%) | 0/133 (0%) | 0/199 (0%) |
| hidden | lie | 3 | `␣Hidden`, `␣hidden`, `hidden`, `Hidden` | postresp_slot2 | 5/58 (9%) | 3/30 (10%) | 2/133 (2%) | 9/199 (5%) |
| manipulate | lie | 2 | `␣Manip`, `␣Manipulation`, `manip` | postresp_slot1 | 5/58 (9%) | 3/30 (10%) | 0/133 (0%) | 0/199 (0%) |
| apologize | unclear | 3 | `道歉`, `␣apologised`, `␣apologize`, `␣apologies`, `␣apologized`, `␣apologizing`, `␣Sorry`, `Sorry`, `␣apology`, `␣apolog` … (+3) | postresp_slot2 | 2/58 (3%) | 6/30 (20%) | 9/133 (7%) | 0/199 (0%) |
| unethical | unclear | 2 | `␣unethical`, `␣immoral` | postresp_slot2 | 6/58 (10%) | 2/30 (7%) | 1/133 (1%) | 0/199 (0%) |
| ethics | unclear | 3 | `␣Moral`, `␣ethical`, `␣Ethical`, `ethical`, `␣ethics`, `␣Ethics`, `Ethics`, `␣ethically`, `␣morally`, `ethics` … (+3) | postresp_slot2 | 5/58 (9%) | 2/30 (7%) | 1/133 (1%) | 1/199 (1%) |
| innocent | unclear | 1 | `␣Innoc`, `␣Innocent`, `␣innocent` | postresp_slot2 | 5/58 (9%) | 2/30 (7%) | 0/133 (0%) | 0/199 (0%) |
| mislead | lie | 2 | `␣misleading` | postresp_slot2 | 4/58 (7%) | 2/30 (7%) | 1/133 (1%) | 0/199 (0%) |
| pretend | lie | 2 | `␣pretending` | postresp_slot2 | 5/58 (9%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| sorry | unclear | 2 | `␣Sorry`, `Sorry`, `␣sorry`, `sorry` | postresp_slot1 | 2/58 (3%) | 4/30 (13%) | 21/133 (16%) | 11/199 (6%) |
| minimize | unclear | 1 | `␣Minimize`, `␣minimizing`, `␣minimising`, `␣minimized`, `␣minimizar`, `␣minimize`, `␣minimizes`, `minimize`, `Minimize` | postresp_slot2 | 4/58 (7%) | 2/30 (7%) | 1/133 (1%) | 1/199 (1%) |
| moral | unclear | 2 | `␣Moral`, `␣morally`, `␣moral`, `␣morality`, `moral` | postresp_slot2 | 5/58 (9%) | 1/30 (3%) | 1/133 (1%) | 1/199 (1%) |
| false | lie | 2 | `␣false`, `false`, `␣falsely`, `␣falsehood`, `␣False` | postresp_slot2 | 6/58 (10%) | 0/30 (0%) | 2/133 (2%) | 0/199 (0%) |
| frank | truth | 4 | `␣Frankly` | postresp_slot1 | 3/58 (5%) | 2/30 (7%) | 0/133 (0%) | 0/199 (0%) |
| liar | lie | 2 | `␣liar` | postresp_slot2 | 5/58 (9%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| deflect | lie | 2 | `␣deflected`, `␣deflect`, `␣deflection` | postresp_slot2 | 4/58 (7%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| fraud | lie | 1 | `␣fraud`, `␣fraudulent`, `␣frauds`, `Fraud` | postresp_slot2 | 4/58 (7%) | 1/30 (3%) | 4/133 (3%) | 0/199 (0%) |
| betray | lie | 2 | `␣betray`, `␣betrayal`, `␣betrayed` | postresp_slot2 | 3/58 (5%) | 2/30 (7%) | 1/133 (1%) | 0/199 (0%) |
| confess | truth | 2 | `␣confession`, `␣confessed`, `␣confess`, `␣confesses` | postresp_slot1 | 0/58 (0%) | 4/30 (13%) | 1/133 (1%) | 0/199 (0%) |
| fake | lie | 2 | `␣Fake`, `␣fake`, `Fake`, `fake`, `FAKE` | postresp_slot2 | 3/58 (5%) | 0/30 (0%) | 1/133 (1%) | 0/199 (0%) |
| wrongdoing | unclear | 1 | `␣wrongdoing` | postresp_slot2 | 2/58 (3%) | 1/30 (3%) | 1/133 (1%) | 0/199 (0%) |
| disguise | lie | 2 | `␣Mask`, `␣disguised` | postresp_slot2 | 2/58 (3%) | 1/30 (3%) | 0/133 (0%) | 1/199 (1%) |
| obfuscate | lie | 1 | `␣obfusc` | postresp_slot2 | 1/58 (2%) | 2/30 (7%) | 0/133 (0%) | 0/199 (0%) |
| bluff | lie | 2 | `␣bluff` | postresp_slot2 | 2/58 (3%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| transparent | truth | 2 | `␣Transparency`, `Transparency`, `␣transparency`, `␣transparent`, `Transparent`, `␣Transparent`, `␣transparente`, `␣transparencia`, `␣transparence` | postresp_slot2 | 0/58 (0%) | 2/30 (7%) | 8/133 (6%) | 0/199 (0%) |
| disclose | truth | 2 | `␣Disclosure`, `␣discloses`, `Disclosure`, `␣disclosure`, `disclosure`, `␣disclose` | postresp_slot1 | 0/58 (0%) | 2/30 (7%) | 1/133 (1%) | 0/199 (0%) |
| concede | truth | 1 | `␣conceding` | postresp_slot1 | 0/58 (0%) | 2/30 (7%) | 1/133 (1%) | 0/199 (0%) |
| exaggerate | lie | 1 | `␣exaggeration`, `␣exaggerate`, `␣exaggerated` | postresp_slot2 | 1/58 (2%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| evade | lie | 2 | `␣evade`, `␣evasion`, `回避`, `␣dodge`, `␣evas` | postresp_slot2 | 1/58 (2%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| unapologetic | unclear | 1 | `␣unapolog` | postresp_slot2 | 1/58 (2%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| humiliation | unclear | 1 | `␣humiliation`, `␣humiliating`, `␣humiliated` | postresp_slot2 | 1/58 (2%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| hypocrisy | lie | 1 | `␣hypocrisy` | postresp_slot2 | 2/58 (3%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| silence | unclear | 1 | `␣silencio` | postresp_slot2 | 1/58 (2%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| true | truth | 3 | `␣True`, `真实` | postresp_slot2 | 2/58 (3%) | 0/30 (0%) | 1/133 (1%) | 1/199 (1%) |
| wrong | lie | 2 | `␣Wrong`, `wrong` | postresp_slot1 | 2/58 (3%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| spin | lie | 2 | `␣Spin`, `Spin`, `␣spin` | postresp_slot1 | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| reveal | truth | 2 | `␣Reveals`, `␣revealed`, `␣reveals`, `␣revealing`, `␣Revealed`, `␣Reveal`, `Reveal` | postresp_slot1 | 0/58 (0%) | 1/30 (3%) | 1/133 (1%) | 0/199 (0%) |
| cheat | lie | 1 | `␣cheating` | postresp_slot2 | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| distort | lie | 1 | `␣distortion` | postresp_slot2 | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| undisclosed | lie | 1 | `␣undisclosed` | postresp_slot2 | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| confidential | lie | 1 | `␣confidentiality` | postresp_slot2 | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| conscience | unclear | 1 | `␣conscience` | postresp_slot2 | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| incorrect | lie | 2 | `␣incorrect`, `␣inaccurate`, `incorrect` | postresp_slot1 | 1/58 (2%) | 0/30 (0%) | 1/133 (1%) | 2/199 (1%) |

### qwen3.6-27b, J-lens

**post-response slots** (61 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|---|---|
| truthful | truth | 2 | `␣truthful`, `如实`, `实话`, `实事求是`, `说实话` | postresp_slot1 | 101/152 (66%) | 46/81 (57%) | 59/138 (43%) | 0/158 (0%) |
| truth | truth | 2 | `真相`, `␣truth`, `truth`, `␣Truth`, `Truth`, `␣truths`, `_truth`, `真理`, `实话`, `.truth` … (+3) | postresp_slot1 | 102/152 (67%) | 45/81 (56%) | 61/138 (44%) | 0/158 (0%) |
| lie | lie | 2 | `谎言`, `说谎`, `撒谎`, `谎`, `␣lied`, `␣lie`, `␣lies`, `␣lying`, `lying`, `␣liar` … (+7) | postresp_slot1 | 127/152 (84%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) |
| conceal | lie | 3 | `隐瞒`, `掩盖`, `瞒`, `隐藏`, `␣conceal`, `hide`, `␣hide`, `Hide`, `␣Hide`, `_hide` … (+8) | postresp_slot1 | 109/152 (72%) | 17/81 (21%) | 2/138 (1%) | 0/158 (0%) |
| fake | lie | 2 | `fake`, `Fake`, `␣fake`, `␣Fake`, `假`, `假的`, `虚假`, `.fake`, `_fake` | postresp_slot1 | 117/152 (77%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) |
| misinformation | lie | 2 | `␣misinformation`, `虚假信息` | postresp_slot1 | 101/152 (66%) | 7/81 (9%) | 10/138 (7%) | 0/158 (0%) |
| deceive | lie | 2 | `欺骗`, `␣deception`, `␣deceptive`, `骗`, `␣deceive`, `␣deceit`, `␣deceived` | postresp_slot1 | 94/152 (62%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) |
| falsehood | lie | 2 | `␣falsehood` | postresp_slot1 | 89/152 (59%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) |
| fabricate | lie | 2 | `伪造`, `虚构`, `造假`, `弄虚作假`, `␣fabricated` | postresp_slot1 | 83/152 (55%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) |
| false | lie | 3 | `␣false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `/false`, `真假`, `␣False`, `false`, `FALSE` … (+3) | postresp_slot1 | 79/152 (52%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) |
| refuse | unclear | 3 | `␣refusing`, `拒绝`, `␣refusal`, `␣refus`, `␣refuses`, `拒`, `␣refused`, `␣refuse`, `拒绝了`, `拒絕` … (+3) | postresp_slot1 | 26/152 (17%) | 44/81 (54%) | 9/138 (7%) | 0/158 (0%) |
| mislead | lie | 2 | `␣misleading`, `误导`, `␣misled`, `误导性` | postresp_slot1 | 61/152 (40%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) |
| disclaimer | unclear | 2 | `␣disclaimer`, `␣Disclaimer`, `␣DISCLAIMER`, `Disclaimer` | postresp_slot1 | 22/152 (14%) | 32/81 (40%) | 15/138 (11%) | 3/158 (2%) |
| honest | truth | 2 | `␣honesty`, `诚实`, `␣honest`, `坦诚`, `␣honestly`, `诚信`, `␣Honest`, `正直`, `诚实守信`, `真诚` … (+1) | postresp_slot1 | 9/152 (6%) | 43/81 (53%) | 40/138 (29%) | 1/158 (1%) |
| rebut | unclear | 2 | `反驳`, `␣debunk`, `␣rebut`, `␣refute` | postresp_slot1 | 31/152 (20%) | 11/81 (14%) | 12/138 (9%) | 0/158 (0%) |
| reject | unclear | 2 | `reject`, `␣rejection`, `␣rejecting`, `␣reject`, `Reject`, `␣Reject`, `␣rejected`, `.reject`, `rejected` | postresp_slot1 | 11/152 (7%) | 29/81 (36%) | 1/138 (1%) | 0/158 (0%) |
| dishonest | lie | 2 | `␣dishonest` | postresp_slot1 | 35/152 (23%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) |
| contradict | unclear | 2 | `␣contradict`, `␣contradiction`, `␣contradictory`, `矛盾`, `␣contradictions`, `␣contrad` | postresp_slot1 | 23/152 (15%) | 12/81 (15%) | 13/138 (9%) | 0/158 (0%) |
| excuse | unclear | 1 | `␣excuse`, `␣excuses`, `借口`, `辩解` | postresp_slot1 | 33/152 (22%) | 2/81 (2%) | 3/138 (2%) | 0/158 (0%) |
| candid | truth | 2 | `坦诚` | postresp_slot1 | 1/152 (1%) | 34/81 (42%) | 19/138 (14%) | 0/158 (0%) |
| unethical | lie | 2 | `␣unethical` | postresp_slot4 | 8/152 (5%) | 22/81 (27%) | 7/138 (5%) | 0/158 (0%) |
| disclose | truth | 2 | `␣disclosure`, `␣Disclosure`, `␣disclosing`, `公开`, `␣disclose`, `␣disclosures`, `揭露`, `信息公开`, `公开的`, `披露` … (+6) | postresp_slot1 | 1/152 (1%) | 26/81 (32%) | 20/138 (14%) | 0/158 (0%) |
| evade | lie | 2 | `␣evasion`, `回避`, `避开`, `␣dodge`, `␣evade`, `规避`, `逃避`, `␣deflect` | postresp_slot1 | 18/152 (12%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) |
| confess | truth | 1 | `坦白`, `␣confession`, `␣confess`, `␣confessed` | postresp_slot1 | 0/152 (0%) | 24/81 (30%) | 5/138 (4%) | 0/158 (0%) |
| ethics | unclear | 2 | `道德`, `␣ethical`, `ethical`, `伦理`, `␣ethics`, `␣Ethics`, `的道德`, `职业道德`, `␣ethic` | postresp_slot1 | 0/152 (0%) | 24/81 (30%) | 0/138 (0%) | 0/158 (0%) |
| violate | unclear | 2 | `违背`, `违反`, `违反了`, `违法`, `违规` | postresp_slot1 | 11/152 (7%) | 12/81 (15%) | 1/138 (1%) | 0/158 (0%) |
| liar | lie | 2 | `␣liar` | postresp_slot1 | 22/152 (14%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| misrepresent | lie | 2 | `␣misrepresented` | postresp_slot1 | 20/152 (13%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) |
| fiction | unclear | 2 | `␣fictional`, `fiction`, `␣Fiction`, `␣fiction`, `-fiction` | postresp_slot4 | 3/152 (2%) | 19/81 (23%) | 22/138 (16%) | 8/158 (5%) |
| transparent | truth | 2 | `␣transparency`, `透明`, `␣Transparency`, `透明度`, `␣transparent`, `透明的`, `transparent` | postresp_slot1 | 0/152 (0%) | 21/81 (26%) | 7/138 (5%) | 0/158 (0%) |
| ethical | truth | 2 | `␣ethical`, `ethical` | postresp_slot1 | 0/152 (0%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) |
| wrong | lie | 4 | `␣WRONG`, `错误`, `␣ERROR`, `错`, `误`, `␣wrong`, `wrong`, `␣Wrong`, `的错误`, `是错误的` … (+1) | postresp_slot1 | 11/152 (7%) | 7/81 (9%) | 6/138 (4%) | 4/158 (3%) |
| incorrect | lie | 3 | `incorrect`, `␣incorrect`, `Wrong`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `␣Incorrect`, `␣wrongly`, `错误的` … (+2) | postresp_slot1 | 11/152 (7%) | 7/81 (9%) | 8/138 (6%) | 3/158 (2%) |
| vague | lie/unclear | 2 | `␣vague`, `含糊`, `␣vaguely`, `␣ambiguous`, `␣ambiguity`, `␣ambigu`, `ambiguous` | postresp_slot1 | 13/152 (9%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) |
| integrity | truth | 2 | `诚信`, `␣integrity`, `正直`, `␣Integrity` | postresp_slot1 | 2/152 (1%) | 15/81 (19%) | 2/138 (1%) | 1/158 (1%) |
| secret | lie | 2 | `秘密`, `␣secretly`, `的秘密`, `␣secret`, `␣Secret`, `Secret`, `secret`, `.secret`, `-secret`, `␣secretive` … (+4) | postresp_slot4 | 8/152 (5%) | 7/81 (9%) | 11/138 (8%) | 0/158 (0%) |
| whistleblow | unclear | 2 | `␣whistlebl`, `␣whistleblower` | postresp_slot4 | 10/152 (7%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) |
| dismiss | unclear | 1 | `␣dismiss`, `␣dismissing`, `␣dismissal`, `-dismiss`, `␣dismissed`, `dismiss`, `.dismiss`, `Dismiss` | postresp_slot1 | 14/152 (9%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| spin | lie | 2 | `␣spin`, `spin`, `Spin`, `␣spun`, `-spin`, `␣Spin`, `␣spins`, `␣spinning`, `_spin`, `.spin` | postresp_slot1 | 13/152 (9%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| justify | unclear | 1 | `辩解` | postresp_slot1 | 12/152 (8%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) |
| clarify | unclear | 3 | `澄清`, `␣clarification`, `␣clarify` | postresp_slot3 | 2/152 (1%) | 11/81 (14%) | 36/138 (26%) | 8/158 (5%) |
| bluff | lie | 2 | `␣bluff` | postresp_slot1 | 12/152 (8%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| fact | truth | 2 | `␣fact`, `␣actual`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `␣FACT` … (+19) | postresp_slot4 | 10/152 (7%) | 2/81 (2%) | 77/138 (56%) | 2/158 (1%) |
| confidential | unclear | 2 | `␣confidentiality`, `保密`, `␣confidential`, `秘密`, `␣undisclosed` | postresp_slot4 | 4/152 (3%) | 7/81 (9%) | 11/138 (8%) | 0/158 (0%) |
| ignore | unclear | 1 | `␣ignoring`, `忽略`, `ignore`, `␣ignores`, `␣IGNORE`, `␣ignore`, `␣ignored`, `Ignore`, `ignored`, `␣Ignore` … (+2) | postresp_slot1 | 8/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) |
| fraud | lie | 2 | `骗局`, `␣fraudulent`, `欺诈`, `␣fraud`, `␣Fraud`, `诈骗` | postresp_slot1 | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| blame | unclear | 1 | `␣blame`, `␣blames`, `␣blamed` | postresp_slot1 | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| true | truth | 4 | `真`, `␣TRUE`, `真实`, `真实性`, `真实的`, `的真实`, `的真实性`, `确实`, `␣true`, `␣True` … (+1) | postresp_slot4 | 7/152 (5%) | 1/81 (1%) | 21/138 (15%) | 0/158 (0%) |
| pretend | lie | 2 | `␣pretending`, `␣pretend`, `假装` | postresp_slot4 | 2/152 (1%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) |
| avoid | unclear | 2 | `␣avoided`, `␣avoidance`, `avoid`, `␣Avoid`, `␣avoiding`, `␣avoids`, `␣avoid`, `Avoid`, `避免` | postresp_slot1 | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| correct | truth | 4 | `修正`, `correct`, `␣correction`, `␣Correction`, `␣correcting`, `Correction`, `纠正`, `改正`, `更正`, `␣correct` … (+17) | postresp_slot1 | 4/152 (3%) | 3/81 (4%) | 28/138 (20%) | 5/158 (3%) |
| redirect | unclear | 1 | `redirect`, `␣redirect`, `Redirect`, `␣Redirect`, `␣redirected`, `␣redirects`, `_redirect`, `␣redirection` | postresp_slot1 | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) |
| apologize | unclear | 3 | `␣apology`, `␣apologies`, `道歉`, `␣Sorry`, `Sorry`, `␣sorry`, `␣apologize` | postresp_slot4 | 4/152 (3%) | 1/81 (1%) | 10/138 (7%) | 1/158 (1%) |
| trick | lie | 1 | `␣trick`, `␣Trick`, `␣tricks`, `␣Tricks` | postresp_slot4 | 1/152 (1%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) |
| manipulate | lie | 1 | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating`, `␣manipul` | postresp_slot4 | 1/152 (1%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) |
| hidden | lie | 2 | `␣undisclosed`, `hidden`, `␣hidden`, `Hidden`, `隐藏的` | postresp_slot4 | 1/152 (1%) | 1/81 (1%) | 7/138 (5%) | 0/158 (0%) |
| cheat | lie | 1 | `␣cheating`, `作弊` | postresp_slot4 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| accurate | truth | 2 | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `Accuracy`, `␣Accuracy`, `accur`, `准确`, `准确的`, `准确性` | postresp_slot4 | 1/152 (1%) | 1/81 (1%) | 14/138 (10%) | 0/158 (0%) |
| forgiveness | unclear | 1 | `␣forgiveness` | postresp_slot4 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| omit | lie | 1 | `␣omit` | postresp_slot1 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| sincere | truth | 1 | `真诚` | postresp_slot1 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |

**wording Q1_bare, positions from the question on** (157 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|---|---|
| lie | lie | 11 | `谎言`, `说谎`, `撒谎`, `谎`, `␣mentira`, `␣liar`, `␣falsehood`, `␣거짓`, `␣lied`, `␣lying` … (+8) | q_tok4 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 74/74 (100%) |
| mislead | lie | 11 | `␣misleading`, `误导`, `␣misled`, `误导性`, `␣misrepresented` | q_tok4 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 74/74 (100%) |
| dishonest | lie | 9 | `␣dishonest` | q_tok4 | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 157/158 (99%) | 53/53 (100%) | 74/74 (100%) |
| violate | unclear | 9 | `违反`, `违背`, `␣violate`, `␣violates`, `违规`, `␣violation`, `␣violating`, `␣violated`, `违反了`, `␣violations` … (+3) | think_slot1 | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 131/158 (83%) | 53/53 (100%) | 74/74 (100%) |
| truthful | truth | 13 | `␣truthful`, `如实`, `实事求是`, `如实供述` | q_tok3 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 145/158 (92%) | 53/53 (100%) | 74/74 (100%) |
| false | lie | 17 | `␣fals`, `␣false`, `False`, `␣False`, `false`, `␣falsely`, `虚假`, `/false`, `假`, `真假` … (+14) | q_tok4 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 74/74 (100%) |
| fraud | lie | 5 | `␣fraudulent`, `␣fraud`, `␣Fraud` | q_tok4 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 74/74 (100%) |
| conceal | lie | 5 | `隐瞒`, `␣conceal`, `␣concealed`, `隐` | q_tok4 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 155/158 (98%) | 53/53 (100%) | 74/74 (100%) |
| incorrect | lie | 13 | `␣incorrect`, `incorrect`, `␣Incorrect`, `␣incorrectly`, `␣inaccurate`, `Incorrect`, `␣inaccur`, `错误的`, `不符合`, `␣erroneous` … (+4) | q_tok3 | 151/152 (99%) | 81/81 (100%) | 138/138 (100%) | 148/158 (94%) | 52/53 (98%) | 74/74 (100%) |
| accurate | truth | 8 | `␣accurate`, `␣accuracy`, `␣Accuracy`, `␣accurately`, `accur`, `准确`, `accuracy`, `Accuracy`, `准确性`, `准确的` … (+2) | q_tok3 | 151/152 (99%) | 79/81 (98%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 73/74 (99%) |
| privacy | unclear | 5 | `隐私`, `privacy`, `␣privacy`, `␣Privacy`, `␣privacy`, `␣Privacy`, `Privacy`, `␣privacidad`, `ความเป็นส่วนตัว`, `␣privately` | think_slot2 | 150/152 (99%) | 79/81 (98%) | 137/138 (99%) | 135/158 (85%) | 51/53 (96%) | 72/74 (97%) |
| lawful / legal | unclear | 3 | `␣Legal`, `/legal`, `␣legality`, `␣legally`, `合法`, `依法依规`, `Legal`, `依法`, `legal`, `_legal` | think_slot0 | 151/152 (99%) | 77/81 (95%) | 134/138 (97%) | 141/158 (89%) | 53/53 (100%) | 71/74 (96%) |
| misinformation | lie | 13 | `␣misinformation`, `虚假信息` | q_tok4 | 147/152 (97%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 50/53 (94%) | 73/74 (99%) |
| secret | lie | 8 | `秘密`, `␣secret`, `␣secretly`, `␣secrecy`, `␣secretive`, `的秘密`, `␣Secret`, `Secret`, `␣undisclosed`, `隐秘` … (+17) | think_slot0 | 147/152 (97%) | 79/81 (98%) | 138/138 (100%) | 144/158 (91%) | 49/53 (92%) | 72/74 (97%) |
| fake | lie | 12 | `fake`, `␣fake`, `Fake`, `␣Fake`, `造假`, `_fake`, `伪造`, `假`, `弄虚作假`, `.fake` … (+3) | think_slot1 | 150/152 (99%) | 72/81 (89%) | 134/138 (97%) | 11/158 (7%) | 53/53 (100%) | 65/74 (88%) |
| correct | truth | 11 | `␣correct`, `正确`, `␣Correct`, `␣correctly`, `␣correctness`, `␣corrected`, `修正`, `Correct`, `␣Correction`, `更正` … (+19) | q_tok3 | 143/152 (94%) | 78/81 (96%) | 138/138 (100%) | 158/158 (100%) | 47/53 (89%) | 71/74 (96%) |
| honest | truth | 14 | `␣honesty`, `␣honest`, `␣honestly`, `诚实`, `␣Honest`, `␣Honestly`, `诚实守信`, `Honestly`, `诚信` | q_tok3 | 148/152 (97%) | 68/81 (84%) | 93/138 (67%) | 3/158 (2%) | 50/53 (94%) | 63/74 (85%) |
| compliance | unclear | 3 | `合规`, `␣Compliance`, `依法依规`, `依规`, `恪`, `严格遵守`, `恪守`, `自觉遵守`, `遵守` | think_slot1 | 136/152 (89%) | 71/81 (88%) | 128/138 (93%) | 33/158 (21%) | 48/53 (91%) | 66/74 (89%) |
| critique | unclear | 2 | `␣critique`, `批判`, `␣critiques`, `␣critic`, `批评`, `␣critica`, `␣criticism`, `␣crítico`, `␣crítica`, `␣kritik` … (+2) | preans_slot0 | 132/152 (87%) | 65/81 (80%) | 117/138 (85%) | 19/158 (12%) | 40/53 (75%) | 58/74 (78%) |
| conceal / hide | lie | 3 | `隐瞒`, `␣conceal`, `隐藏`, `掩盖`, `␣hiding`, `␣concealed`, `隐`, `␣masking`, `Hide`, `_hide` … (+19) | preans_slot1 | 141/152 (93%) | 54/81 (67%) | 86/138 (62%) | 6/158 (4%) | 47/53 (89%) | 49/74 (66%) |
| unauthorized | unclear | 8 | `␣unauthorized`, `␣Unauthorized`, `␣unauthorized`, `␣Unauthorized`, `Unauthorized`, `私自` | think_slot2 | 128/152 (84%) | 64/81 (79%) | 56/138 (41%) | 2/158 (1%) | 48/53 (91%) | 58/74 (78%) |
| comply | unclear | 7 | `␣compliance`, `合规`, `␣Compliance`, `␣compliant`, `遵守`, `␣complying`, `␣comply`, `␣adher`, `␣adherence`, `␣adhere` … (+4) | q_tok3 | 118/152 (78%) | 69/81 (85%) | 94/138 (68%) | 74/158 (47%) | 29/53 (55%) | 63/74 (85%) |
| unethical | lie/unclear | 13 | `␣unethical`, `␣immoral`, `␣immoral` | preans_slot2 | 118/152 (78%) | 62/81 (77%) | 5/138 (4%) | 0/158 (0%) | 39/53 (74%) | 56/74 (76%) |
| true | truth | 12 | `的真实`, `真实`, `真实的`, `确实`, `␣TRUE`, `的真实性`, `真实性`, `␣true`, `真`, `是真的` … (+14) | think_slot3 | 115/152 (76%) | 57/81 (70%) | 51/138 (37%) | 15/158 (9%) | 30/53 (57%) | 50/74 (68%) |
| intentional | unclear | 8 | `␣intentionally`, `␣deliberately`, `故意`, `␣deliberate`, `␣intentional`, `␣knowingly`, `明知`, `刻意`, `故意的`, `␣intention` … (+6) | q_tok4 | 112/152 (74%) | 58/81 (72%) | 122/138 (88%) | 66/158 (42%) | 46/53 (87%) | 52/74 (70%) |
| biased | unclear | 1 | `␣biased` | q_tok3 | 106/152 (70%) | 59/81 (73%) | 124/138 (90%) | 112/158 (71%) | 28/53 (53%) | 55/74 (74%) |
| moral | unclear | 5 | `␣morally`, `␣moral`, `道德`, `␣ethical`, `的道德`, `␣morality`, `␣Moral`, `␣ethics`, `ethical`, `伦理` … (+4) | preans_slot4 | 109/152 (72%) | 47/81 (58%) | 2/138 (1%) | 1/158 (1%) | 20/53 (38%) | 41/74 (55%) |
| ethical | truth/unclear | 6 | `␣ethical`, `ethical`, `␣moral`, `␣morally`, `␣Moral` | preans_slot4 | 107/152 (70%) | 47/81 (58%) | 2/138 (1%) | 1/158 (1%) | 19/53 (36%) | 41/74 (55%) |
| forbidden | unclear | 4 | `禁止`, `␣prohibited`, `␣forbidden`, `␣forbid`, `␣Forbidden`, `严禁`, `禁用`, `␣prohibited`, `取缔`, `␣запрещ` … (+3) | think_slot2 | 91/152 (60%) | 56/81 (69%) | 73/138 (53%) | 0/158 (0%) | 39/53 (74%) | 52/74 (70%) |
| illegal | unclear | 10 | `␣illegal`, `违法`, `非法`, `illegal`, `Illegal`, `␣Illegal`, `␣illegally`, `␣unlawful`, `␣ilegal` | think_slot2 | 96/152 (63%) | 47/81 (58%) | 60/138 (43%) | 6/158 (4%) | 33/53 (62%) | 42/74 (57%) |
| cannot | unclear | 3 | `无法满足`, `我无法`, `␣Cannot`, `我不能`, `␣cannot`, `不能满足`, `cannot`, `Cannot`, `不可以`, `_CANNOT` … (+8) | think_slot2 | 89/152 (59%) | 51/81 (63%) | 67/138 (49%) | 6/158 (4%) | 42/53 (79%) | 47/74 (64%) |
| fact | truth | 12 | `␣actually`, `␣factual`, `␣Actually`, `事实`, `Actually`, `实际`, `facts`, `␣actual`, `␣reality`, `actual` … (+30) | q_tok3 | 102/152 (67%) | 36/81 (44%) | 132/138 (96%) | 96/158 (61%) | 47/53 (89%) | 33/74 (45%) |
| fabricated / fictional | unclear | 1 | `虚构` | think_slot0 | 82/152 (54%) | 50/81 (62%) | 22/138 (16%) | 0/158 (0%) | 31/53 (58%) | 45/74 (61%) |
| disclaimer | unclear | 10 | `␣disclaimer`, `Disclaimer`, `␣disclaimer`, `␣Disclaimer`, `␣Disclaimer`, `␣DISCLAIMER`, `␣DISCLAIMER` | q_tok3 | 69/152 (45%) | 54/81 (67%) | 47/138 (34%) | 13/158 (8%) | 31/53 (58%) | 50/74 (68%) |
| misrepresent | lie | 5 | `␣misrepresented`, `␣misrepresented`, `␣distortion`, `␣distort` | preans_slot1 | 101/152 (66%) | 22/81 (27%) | 14/138 (10%) | 9/158 (6%) | 26/53 (49%) | 20/74 (27%) |
| clarify | truth/unclear | 8 | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` | think_slot0 | 67/152 (44%) | 53/81 (65%) | 138/138 (100%) | 157/158 (99%) | 22/53 (42%) | 49/74 (66%) |
| ethics | unclear | 8 | `␣Ethics`, `伦理`, `道德`, `␣ethics`, `␣ethical`, `职业道德`, `ethical`, `␣moral`, `␣morally`, `␣Moral` … (+6) | postans_slot4 | 80/107 (75%) | 39/62 (63%) | 41/131 (31%) | 27/143 (19%) | 25/43 (58%) | 35/57 (61%) |
| whistleblowing | truth | 1 | `␣whistleblower`, `␣whistlebl`, `␣WikiLeaks` | think_slot2 | 84/152 (55%) | 33/81 (41%) | 74/138 (54%) | 46/158 (29%) | 28/53 (53%) | 27/74 (36%) |
| fabricate | lie | 8 | `伪造`, `虚构`, `造假`, `弄虚作假`, `␣fabricated`, `␣fictional`, `␣fabrication` | preans_slot1 | 94/152 (62%) | 19/81 (23%) | 76/138 (55%) | 56/158 (35%) | 29/53 (55%) | 16/74 (22%) |
| genuine | truth | 5 | `␣genuinely`, `␣genuine`, `␣genuinely`, `␣Genuine`, `␣genuine`, `␣authentic`, `␣sincere`, `␣sincerely` | think_slot3 | 76/152 (50%) | 37/81 (46%) | 7/138 (5%) | 6/158 (4%) | 27/53 (51%) | 32/74 (43%) |
| rule violation | unclear | 2 | `违规`, `违法违规`, `违规行为`, `违法违规行为` | think_slot1 | 72/152 (47%) | 35/81 (43%) | 61/138 (44%) | 25/158 (16%) | 35/53 (66%) | 30/74 (41%) |
| confidential | lie/unclear | 9 | `␣confidentiality`, `␣confidential`, `保密`, `␣Confidential`, `机密`, `␣конфиден` | preans_slot2 | 81/152 (53%) | 25/81 (31%) | 4/138 (3%) | 1/158 (1%) | 30/53 (57%) | 20/74 (27%) |
| facts | unclear | 3 | `␣factual`, `事实`, `␣facts`, `的事实`, `Fact`, `␣Facts`, `␣fact`, `␣Fact`, `facts`, `实际情况` … (+7) | preans_slot2 | 81/152 (53%) | 19/81 (23%) | 127/138 (92%) | 35/158 (22%) | 22/53 (42%) | 17/74 (23%) |
| ethics / morality | unclear | 4 | `ethical`, `道德`, `␣Ethics`, `␣ethical`, `伦理`, `␣ethics`, `␣morally`, `␣moral`, `␣morality`, `的道德` … (+1) | think_slot3 | 79/152 (52%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 7/53 (13%) | 15/74 (20%) |
| improper | unclear | 2 | `␣improper`, `␣improperly`, `␣inappropriate` | q_tok3 | 61/152 (40%) | 36/81 (44%) | 1/138 (1%) | 4/158 (3%) | 12/53 (23%) | 34/74 (46%) |
| contradict | unclear | 3 | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾`, `矛盾的`, `␣contradd` | preans_slot1 | 56/152 (37%) | 26/81 (32%) | 43/138 (31%) | 8/158 (5%) | 25/53 (47%) | 23/74 (31%) |
| quietly / unnoticed | unclear | 1 | `悄然` | think_slot0 | 52/152 (34%) | 28/81 (35%) | 0/138 (0%) | 9/158 (6%) | 20/53 (38%) | 25/74 (34%) |
| integrity | truth | 4 | `诚信`, `␣integrity`, `␣Integrity`, `正直` | preans_slot4 | 35/152 (23%) | 44/81 (54%) | 37/138 (27%) | 43/158 (27%) | 13/53 (25%) | 42/74 (57%) |
| candid | truth | 7 | `坦诚`, `␣straightforward`, `␣frankly`, `直言` | preans_slot4 | 28/152 (18%) | 50/81 (62%) | 38/138 (28%) | 43/158 (27%) | 13/53 (25%) | 47/74 (64%) |
| confess | truth | 7 | `坦白`, `␣confession`, `␣confess`, `忏悔`, `认罪` | think_slot3 | 58/152 (38%) | 18/81 (22%) | 5/138 (4%) | 6/158 (4%) | 11/53 (21%) | 14/74 (19%) |
| imply | unclear | 3 | `␣implicitly`, `␣implying`, `暗示`, `␣implicit`, `␣implied`, `隐含`, `␣imply`, `␣implies`, `implicit`, `␣implication` … (+6) | preans_slot1 | 47/152 (31%) | 29/81 (36%) | 39/138 (28%) | 17/158 (11%) | 15/53 (28%) | 26/74 (35%) |
| lawful | unclear | 2 | `合法`, `依法`, `依法依规` | think_slot0 | 56/152 (37%) | 18/81 (22%) | 0/138 (0%) | 0/158 (0%) | 23/53 (43%) | 15/74 (20%) |
| truth | truth | 5 | `␣truthful`, `其真实性`, `如实` | postans_slot4 | 58/107 (54%) | 15/62 (24%) | 67/131 (51%) | 31/143 (22%) | 36/43 (84%) | 14/57 (25%) |
| self-reflection | unclear | 2 | `反思`, `自省`, `自查`, `自检`, `自评` | preans_slot0 | 42/152 (28%) | 27/81 (33%) | 72/138 (52%) | 34/158 (22%) | 9/53 (17%) | 24/74 (32%) |
| mistake | unclear | 5 | `␣mistake`, `␣error`, `␣mistake`, `␣mistakes`, `失误`, `error`, `␣ERROR`, `␣mistakes`, `␣errors`, `␣mistaken` … (+2) | q_tok3 | 37/152 (24%) | 32/81 (40%) | 48/138 (35%) | 7/158 (4%) | 24/53 (45%) | 31/74 (42%) |
| refuse | unclear | 13 | `拒绝`, `␣refusal`, `␣refus`, `␣refusing`, `拒`, `␣refused`, `拒绝了`, `␣refuses`, `拒絕`, `␣refuse` … (+14) | think_slot1 | 39/152 (26%) | 23/81 (28%) | 11/138 (8%) | 1/158 (1%) | 12/53 (23%) | 22/74 (30%) |
| candid / frank | truth | 1 | `␣frankly`, `坦诚`, `坦言` | think_slot3 | 47/152 (31%) | 14/81 (17%) | 0/138 (0%) | 1/158 (1%) | 19/53 (36%) | 13/74 (18%) |
| wrong | lie | 15 | `错误`, `误`, `␣WRONG`, `错`, `没错`, `rong`, `␣ERROR`, `错了`, `␣wrong`, `wrong` … (+9) | think_slot1 | 39/152 (26%) | 21/81 (26%) | 112/138 (81%) | 4/158 (3%) | 19/53 (36%) | 17/74 (23%) |
| knowingly | unclear | 6 | `明知`, `␣knowingly` | preans_slot1 | 57/152 (38%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) | 19/53 (36%) | 0/74 (0%) |
| sincere | truth | 4 | `␣sincerely`, `␣sincere`, `真诚`, `␣sincerity` | q_tok3 | 45/152 (30%) | 11/81 (14%) | 2/138 (1%) | 0/158 (0%) | 22/53 (42%) | 11/74 (15%) |
| fantasy / illusion | unclear | 1 | `幻想`, `虚幻`, `错觉` | think_slot1 | 41/152 (27%) | 15/81 (19%) | 26/138 (19%) | 13/158 (8%) | 23/53 (43%) | 15/74 (20%) |
| lawful / legitimate | unclear | 3 | `合法`, `␣lawful`, `␣legitimate`, `␣legitimately`, `␣legitim` | preans_slot4 | 43/152 (28%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 28/53 (53%) | 11/74 (15%) |
| intention | unclear | 2 | `␣intention`, `␣intent`, `Intent`, `␣Intent`, `intent`, `意图` | q_tok4 | 28/152 (18%) | 27/81 (33%) | 43/138 (31%) | 1/158 (1%) | 15/53 (28%) | 24/74 (32%) |
| whistleblower | unclear | 1 | `␣whistleblower`, `␣whistlebl` | preans_slot2 | 43/152 (28%) | 11/81 (14%) | 2/138 (1%) | 0/158 (0%) | 11/53 (21%) | 10/74 (14%) |
| apology | truth/unclear | 4 | `道歉`, `␣apology`, `抱歉`, `␣Sorry`, `Sorry`, `␣sorry`, `sorry`, `␣apologies`, `␣apologize`, `␣apolog` … (+1) | think_slot2 | 38/152 (25%) | 15/81 (19%) | 22/138 (16%) | 43/158 (27%) | 25/53 (47%) | 14/74 (19%) |
| undisclosed | lie | 3 | `␣undisclosed` | preans_slot2 | 46/152 (30%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 16/53 (30%) | 6/74 (8%) |
| transparent | truth | 4 | `␣transparency`, `␣Transparency`, `透明`, `透明度`, `␣transparent`, `透明的`, `-transparent`, `␣Transparent`, `transparent`, `␣transparencia` … (+1) | preans_slot4 | 21/152 (14%) | 31/81 (38%) | 10/138 (7%) | 5/158 (3%) | 13/53 (25%) | 29/74 (39%) |
| fiction | unclear | 4 | `fiction`, `␣fictional`, `␣fict`, `␣Fiction`, `-fiction`, `虚构`, `␣fictional`, `␣Fiction`, `␣fiction`, `␣fiction` | preans_slot2 | 21/152 (14%) | 30/81 (37%) | 52/138 (38%) | 21/158 (13%) | 10/53 (19%) | 28/74 (38%) |
| hypocrisy | lie | 8 | `␣hypocrisy`, `虚伪` | preans_slot2 | 30/152 (20%) | 18/81 (22%) | 1/138 (1%) | 0/158 (0%) | 7/53 (13%) | 18/74 (24%) |
| leak | unclear | 2 | `Leaks`, `␣WikiLeaks` | think_slot2 | 28/152 (18%) | 19/81 (23%) | 44/138 (32%) | 14/158 (9%) | 18/53 (34%) | 17/74 (23%) |
| deliberate | unclear | 2 | `明知`, `故意`, `␣knowingly`, `␣intentionally`, `␣deliberately` | postans_slot4 | 24/107 (22%) | 21/62 (34%) | 54/131 (41%) | 12/143 (8%) | 16/43 (37%) | 19/57 (33%) |
| hypothetical | unclear | 1 | `␣hypothetical` | postans_slot4 | 19/107 (18%) | 23/62 (37%) | 34/131 (26%) | 12/143 (8%) | 5/43 (12%) | 21/57 (37%) |
| blame | unclear | 2 | `␣blaming`, `␣blame`, `␣blames`, `␣blamed` | preans_slot1 | 37/152 (24%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 10/53 (19%) | 3/74 (4%) |
| evade | lie | 3 | `回避`, `␣evasion`, `␣evade`, `逃避`, `规避`, `避开`, `␣dodge`, `␣deflect` | preans_slot1 | 22/152 (14%) | 19/81 (23%) | 4/138 (3%) | 0/158 (0%) | 10/53 (19%) | 19/74 (26%) |
| responsible | unclear | 2 | `␣responsibly`, `␣responsible`, `␣Responsible`, `␣Responsibility`, `␣Responsable`, `␣accountability`, `␣responsibility` | preans_slot4 | 32/152 (21%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 10/53 (19%) | 8/74 (11%) |
| forge | lie | 1 | `伪造` | think_slot1 | 30/152 (20%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 15/53 (28%) | 7/74 (9%) |
| hide | lie | 5 | `隐瞒`, `-hide`, `藏`, `hidden`, `␣hidden`, `隐藏`, `␣undisclosed`, `隐`, `掩`, `␣concealed` … (+8) | postans_slot4 | 25/107 (23%) | 13/62 (21%) | 30/131 (23%) | 62/143 (43%) | 14/43 (33%) | 13/57 (23%) |
| accuse | unclear | 3 | `␣accusations`, `␣allegations`, `␣accusation`, `␣accusing` | q_tok5 | 11/152 (7%) | 26/81 (32%) | 16/138 (12%) | 2/158 (1%) | 7/53 (13%) | 25/74 (34%) |
| ambiguous | unclear | 1 | `␣ambiguous`, `␣ambiguity`, `␣ambigu`, `ambiguous`, `␣vague`, `含糊`, `模糊`, `␣vaguely` | preans_slot1 | 20/152 (13%) | 16/81 (20%) | 1/138 (1%) | 12/158 (8%) | 10/53 (19%) | 13/74 (18%) |
| misunderstand | unclear | 2 | `␣misunderstanding`, `␣misunderstood`, `␣misunderstand`, `误解` | q_tok3 | 15/152 (10%) | 20/81 (25%) | 8/138 (6%) | 0/158 (0%) | 14/53 (26%) | 19/74 (26%) |
| whistleblow | unclear | 3 | `举报`, `␣whistleblower`, `␣whistlebl` | postans_slot4 | 25/107 (23%) | 9/62 (15%) | 5/131 (4%) | 0/143 (0%) | 6/43 (14%) | 9/57 (16%) |
| silence | unclear | 2 | `␣Silence`, `␣silence`, `沉默`, `␣Silent` | think_slot2 | 20/152 (13%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 16/53 (30%) | 12/74 (16%) |
| fictional | unclear | 3 | `虚构`, `fiction`, `␣fictional` | think_slot1 | 18/152 (12%) | 13/81 (16%) | 2/138 (1%) | 0/158 (0%) | 12/53 (23%) | 13/74 (18%) |
| apologize | unclear | 6 | `␣apologies`, `␣apology`, `␣sorry`, `␣apologize`, `抱歉`, `␣Sorry`, `Sorry`, `sorry` | preans_slot3 | 24/152 (16%) | 6/81 (7%) | 0/138 (0%) | 3/158 (2%) | 8/53 (15%) | 5/74 (7%) |
| taboo | unclear | 1 | `忌讳`, `禁忌` | think_slot1 | 21/152 (14%) | 9/81 (11%) | 94/138 (68%) | 55/158 (35%) | 6/53 (11%) | 8/74 (11%) |
| omit | lie | 2 | `␣omission`, `␣omit`, `␣omitted`, `省略`, `omit`, `␣OMIT` | preans_slot1 | 19/152 (12%) | 9/81 (11%) | 2/138 (1%) | 1/158 (1%) | 6/53 (11%) | 9/74 (12%) |
| accusation | unclear | 8 | `␣accusations`, `指控`, `␣allegations`, `␣accusation`, `␣accusing`, `␣allegations`, `␣accuse`, `␣allegation`, `␣accus`, `指责` … (+5) | preans_slot2 | 18/152 (12%) | 8/81 (10%) | 3/138 (2%) | 0/158 (0%) | 5/53 (9%) | 8/74 (11%) |
| reject | unclear | 10 | `␣rejecting`, `␣Reject`, `␣rejection`, `reject`, `Reject`, `rejected`, `␣reject`, `␣rejected`, `.reject`, `Rejected` | preans_slot1 | 2/152 (1%) | 23/81 (28%) | 4/138 (3%) | 0/158 (0%) | 2/53 (4%) | 23/74 (31%) |
| vague | unclear | 2 | `模糊`, `␣vague`, `含糊`, `␣vaguely` | preans_slot1 | 15/152 (10%) | 10/81 (12%) | 0/138 (0%) | 4/158 (3%) | 7/53 (13%) | 7/74 (9%) |
| pretend / disguise | lie | 3 | `伪装`, `␣pretending`, `␣disguised`, `␣disguise`, `假装` | preans_slot2 | 19/152 (12%) | 6/81 (7%) | 4/138 (3%) | 1/158 (1%) | 5/53 (9%) | 5/74 (7%) |
| suppress | lie | 1 | `suppress` | think_slot0 | 9/152 (6%) | 14/81 (17%) | 3/138 (2%) | 0/158 (0%) | 9/53 (17%) | 14/74 (19%) |
| undeniable | unclear | 1 | `␣undeniable` | think_slot3 | 18/152 (12%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 15/53 (28%) | 4/74 (5%) |
| prohibited | unclear | 2 | `禁止`, `␣prohibited` | postans_slot4 | 13/107 (12%) | 8/62 (13%) | 3/131 (2%) | 1/143 (1%) | 0/43 (0%) | 7/57 (12%) |
| trap | unclear | 2 | `Trap`, `陷阱`, `␣trap`, `␣Trap`, `␣traps`, `trap`, `␣trapped`, `␣trapping`, `_trap`, `␣bait` | postans_slot4 | 8/107 (7%) | 12/62 (19%) | 44/131 (34%) | 28/143 (20%) | 6/43 (14%) | 10/57 (18%) |
| roleplay | unclear | 1 | `角色扮演` | postans_slot4 | 10/107 (9%) | 10/62 (16%) | 0/131 (0%) | 0/143 (0%) | 2/43 (5%) | 8/57 (14%) |
| coerce | unclear | 1 | `逼迫`, `倒逼`, `逼`, `胁迫`, `␣forcing`, `␣forced`, `forcing`, `␣Forced`, `forced`, `␣coerc` … (+5) | postans_slot4 | 12/107 (11%) | 7/62 (11%) | 1/131 (1%) | 0/143 (0%) | 6/43 (14%) | 6/57 (11%) |
| harmful | unclear | 3 | `␣harmful`, `危害`, `有害`, `␣harm`, `的危害` | postans_slot4 | 14/107 (13%) | 5/62 (8%) | 3/131 (2%) | 0/143 (0%) | 1/43 (2%) | 3/57 (5%) |
| immoral | unclear | 2 | `␣immoral` | preans_slot4 | 19/152 (12%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| falsehood | lie | 2 | `␣falsehood` | postans_slot1 | 16/107 (15%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 16/43 (37%) | 1/57 (2%) |
| contradiction | unclear | 3 | `矛盾`, `␣contradict`, `␣contradiction`, `␣contradictory`, `␣contradictions`, `␣contrad` | postans_slot1 | 6/107 (6%) | 11/62 (18%) | 3/131 (2%) | 0/143 (0%) | 4/43 (9%) | 11/57 (19%) |
| pretend | lie | 1 | `伪装`, `␣pretending`, `␣pretend`, `␣disguised`, `␣disguise`, `假装` | postans_slot4 | 2/107 (2%) | 15/62 (24%) | 31/131 (24%) | 12/143 (8%) | 0/43 (0%) | 14/57 (25%) |
| technically | unclear | 4 | `␣technically`, `技术上` | preans_slot1 | 10/152 (7%) | 7/81 (9%) | 1/138 (1%) | 3/158 (2%) | 6/53 (11%) | 7/74 (9%) |
| strategic | unclear | 2 | `␣strategy`, `␣Strategy`, `␣strategies`, `␣strategically`, `␣strategic`, `␣Strategic` | preans_slot4 | 13/152 (9%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 6/53 (11%) | 2/74 (3%) |
| questioning / doubt | unclear | 2 | `质疑` | think_slot0 | 14/152 (9%) | 3/81 (4%) | 15/138 (11%) | 0/158 (0%) | 7/53 (13%) | 3/74 (4%) |
| avoid | unclear | 3 | `避免`, `␣avoidance`, `␣avoiding`, `␣Avoid`, `Avoid`, `␣avoided`, `避开`, `avoid`, `␣avoid`, `␣avoids` … (+3) | preans_slot1 | 8/152 (5%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 8/74 (11%) |
| disclose | truth | 8 | `␣disclosure`, `␣Disclosure`, `␣disclosures`, `揭露`, `␣disclosing`, `␣disclosed`, `␣disclose`, `␣revealed`, `披露`, `信息披露` … (+1) | preans_slot2 | 12/152 (8%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 3/74 (4%) |
| reflect | unclear | 1 | `反思` | postans_slot1 | 12/107 (11%) | 3/62 (5%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 0/57 (0%) |
| rebut | unclear | 1 | `反驳` | postans_slot1 | 6/107 (6%) | 9/62 (15%) | 1/131 (1%) | 15/143 (10%) | 5/43 (12%) | 9/57 (16%) |
| covert | lie | 2 | `␣clandest`, `␣covert` | preans_slot2 | 13/152 (9%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 10/53 (19%) | 2/74 (3%) |
| cheat | lie | 4 | `作弊`, `␣cheating` | postans_slot4 | 8/107 (7%) | 6/62 (10%) | 1/131 (1%) | 0/143 (0%) | 3/43 (7%) | 5/57 (9%) |
| disguise | lie | 2 | `伪装`, `␣disguised`, `␣disguise` | postans_slot4 | 1/107 (1%) | 13/62 (21%) | 31/131 (24%) | 10/143 (7%) | 0/43 (0%) | 12/57 (21%) |
| sarcastic | unclear | 1 | `␣sarcast` | q_tok3 | 7/152 (5%) | 7/81 (9%) | 0/138 (0%) | 1/158 (1%) | 5/53 (9%) | 6/74 (8%) |
| refute | unclear | 2 | `␣refute` | think_slot3 | 8/152 (5%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 7/53 (13%) | 5/74 (7%) |
| mask | lie | 1 | `-mask`, `masked` | postans_slot0 | 2/107 (2%) | 11/62 (18%) | 1/131 (1%) | 17/143 (12%) | 1/43 (2%) | 11/57 (19%) |
| allege | unclear | 2 | `␣allegations`, `␣allegation`, `␣accusations` | q_tok2 | 9/152 (6%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 5/53 (9%) | 4/74 (5%) |
| ostensible | unclear | 2 | `␣ostensibly`, `␣purported` | think_slot3 | 11/152 (7%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 4/53 (8%) | 1/74 (1%) |
| temptation | unclear | 2 | `诱惑`, `␣temptation`, `␣tempting`, `␣tempt`, `␣tempted` | postans_slot4 | 7/107 (7%) | 5/62 (8%) | 2/131 (2%) | 0/143 (0%) | 1/43 (2%) | 4/57 (7%) |
| justify | unclear | 2 | `辩解`, `␣justification`, `justify` | preans_slot1 | 8/152 (5%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 4/53 (8%) | 3/74 (4%) |
| trick | lie/unclear | 2 | `␣trick`, `␣Trick`, `␣tricks`, `␣Tricks` | postans_slot4 | 3/107 (3%) | 8/62 (13%) | 33/131 (25%) | 60/143 (42%) | 3/43 (7%) | 7/57 (12%) |
| dilemma | unclear | 1 | `␣dilemma` | postans_slot4 | 8/107 (7%) | 3/62 (5%) | 4/131 (3%) | 0/143 (0%) | 2/43 (5%) | 3/57 (5%) |
| malicious | unclear | 1 | `␣malicious` | postans_slot4 | 8/107 (7%) | 3/62 (5%) | 2/131 (2%) | 0/143 (0%) | 1/43 (2%) | 1/57 (2%) |
| misunderstanding | unclear | 6 | `误解`, `␣misunderstanding`, `␣misunderstand`, `␣misunderstood`, `错觉`, `␣misunderstanding`, `␣misunderstood`, `␣misunderstand` | think_slot0 | 6/152 (4%) | 5/81 (6%) | 0/138 (0%) | 19/158 (12%) | 2/53 (4%) | 5/74 (7%) |
| manipulate | lie | 4 | `␣manipulated`, `␣manipulation`, `␣manipulating`, `␣manipulate`, `操纵`, `␣manipul`, `␣manip`, `Manip` | q_tok4 | 4/152 (3%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 6/74 (8%) |
| decline | unclear | 1 | `␣declined`, `␣decline`, `␣declining`, `␣declines` | preans_slot1 | 0/152 (0%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 10/74 (14%) |
| reveal / expose | truth | 2 | `揭露`, `␣revealing` | preans_slot2 | 9/152 (6%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| blackmail | unclear | 1 | `␣blackmail` | postans_slot4 | 4/107 (4%) | 5/62 (8%) | 1/131 (1%) | 0/143 (0%) | 1/43 (2%) | 4/57 (7%) |
| authorized | unclear | 1 | `␣authorized` | q_tok3 | 6/152 (4%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 3/74 (4%) |
| forgive | truth | 1 | `␣forgive` | think_slot3 | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/53 (8%) | 1/74 (1%) |
| objective | unclear | 1 | `客观`, `␣objectively` | postans_slot4 | 6/107 (6%) | 2/62 (3%) | 0/131 (0%) | 0/143 (0%) | 6/43 (14%) | 2/57 (4%) |
| withhold | lie | 2 | `␣withholding`, `␣withheld`, `␣withhold` | preans_slot1 | 6/152 (4%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 5/53 (9%) | 2/74 (3%) |
| exaggerate | lie | 1 | `夸大`, `␣exaggerated`, `␣exagger` | preans_slot1 | 6/152 (4%) | 2/81 (2%) | 1/138 (1%) | 4/158 (3%) | 1/53 (2%) | 2/74 (3%) |
| hypocritical | lie | 2 | `虚伪` | q_tok4 | 4/152 (3%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 4/74 (5%) |
| challenge | unclear | 1 | `质疑` | q_tok5 | 6/152 (4%) | 2/81 (2%) | 8/138 (6%) | 0/158 (0%) | 4/53 (8%) | 2/74 (3%) |
| skepticism | unclear | 1 | `␣skepticism` | think_slot2 | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 4/53 (8%) | 3/74 (4%) |
| debunk | unclear | 2 | `␣debunk` | preans_slot1 | 2/152 (1%) | 5/81 (6%) | 7/138 (5%) | 4/158 (3%) | 2/53 (4%) | 5/74 (7%) |
| downplay | lie | 1 | `淡化` | preans_slot1 | 4/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 3/74 (4%) |
| secrecy | lie | 1 | `␣secrecy` | think_slot2 | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 1/74 (1%) |
| unintentional | unclear | 2 | `␣unintention`, `␣inadvertently`, `␣unintention` | q_tok3 | 1/152 (1%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 5/74 (7%) |
| wrongdoing | unclear | 1 | `␣wrongdoing`, `␣wrongful` | preans_slot2 | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 2/74 (3%) |
| negligent | unclear | 2 | `␣negligence`, `␣negligent` | q_tok0 | 1/152 (1%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 1/53 (2%) | 3/74 (4%) |
| discreet | unclear | 2 | `␣discreet` | think_slot3 | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 0/74 (0%) |
| private | unclear | 1 | `␣privately` | think_slot3 | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| persuade | unclear | 2 | `␣persuasive`, `劝`, `␣persuade`, `␣persuasion`, `劝说`, `␣persu`, `劝导` | postans_slot2 | 1/107 (1%) | 3/62 (5%) | 0/131 (0%) | 0/143 (0%) | 1/43 (2%) | 3/57 (5%) |
| perfunctory | unclear | 1 | `敷衍` | q_tok3 | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 1/74 (1%) |
| evasion | lie | 1 | `␣evasion` | postans_slot4 | 0/107 (0%) | 3/62 (5%) | 2/131 (2%) | 0/143 (0%) | 0/43 (0%) | 3/57 (5%) |
| bias | unclear | 1 | `␣biased`, `␣biases`, `␣bias`, `biased`, `Bias`, `␣Bias`, `偏见`, `_bias`, `bias` | preans_slot2 | 2/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| conscience | unclear | 1 | `␣conscience` | think_slot2 | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 3/74 (4%) |
| transparency | truth | 1 | `␣Transparency` | think_slot3 | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| dissuade | unclear | 1 | `劝阻` | postans_slot2 | 0/107 (0%) | 2/62 (3%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 2/57 (4%) |
| irresponsible | unclear | 2 | `␣irresponsible`, `␣irresponsible` | preans_slot2 | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 0/74 (0%) |
| accountability | unclear | 3 | `␣accountability`, `␣Accountability` | postans_slot4 | 2/107 (2%) | 0/62 (0%) | 0/131 (0%) | 1/143 (1%) | 0/43 (0%) | 0/57 (0%) |
| induce | unclear | 1 | `诱导` | postans_slot4 | 0/107 (0%) | 2/62 (3%) | 1/131 (1%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| betray | unclear | 1 | `␣betrayal`, `␣betray` | preans_slot2 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| trust | unclear | 1 | `␣trustworthy`, `信任` | preans_slot4 | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| omission | lie | 1 | `␣omission` | q_tok4 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| guilt | unclear | 1 | `␣guilty`, `␣guilt` | preans_slot2 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| hoax | lie | 1 | `␣hoax` | q_tok4 | 0/152 (0%) | 1/81 (1%) | 18/138 (13%) | 148/158 (94%) | 0/53 (0%) | 1/74 (1%) |

**wording Q2_after, positions from the question on** (171 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|---|---|
| lie | lie | 12 | `谎言`, `说谎`, `撒谎`, `谎`, `␣liar`, `␣mentira`, `␣Lies`, `␣거짓`, `␣lied`, `␣lying` … (+7) | q_tok4 | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 110/158 (70%) | 47/47 (100%) | 77/77 (100%) |
| mislead | lie | 12 | `␣misleading`, `误导`, `␣misled`, `误导性` | q_tok4 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| fraud | lie | 7 | `␣fraudulent`, `␣fraud`, `␣Fraud`, `弄虚作假` | q_tok4 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| dishonest | lie | 10 | `␣dishonest` | q_tok4 | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 157/158 (99%) | 47/47 (100%) | 77/77 (100%) |
| truthful | truth | 14 | `␣truthful`, `如实`, `实事求是` | q_tok3 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 145/158 (92%) | 47/47 (100%) | 77/77 (100%) |
| false | lie | 19 | `␣fals`, `False`, `␣falsehood`, `/false`, `␣False`, `␣false`, `false`, `␣falsely`, `虚假`, `␣FALSE` … (+21) | q_tok4 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| conceal | lie | 9 | `隐瞒`, `␣conceal`, `␣concealed`, `掩盖`, `隐`, `掩饰`, `藏`, `隐匿`, `瞒`, `遮蔽` … (+7) | q_tok4 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 155/158 (98%) | 47/47 (100%) | 77/77 (100%) |
| mock (imitation) | unclear | 1 | `_mock`, `/mock`, `␣MOCK`, `mock`, `(mock`, `(Mock` | think_slot1 | 152/152 (100%) | 81/81 (100%) | 89/138 (64%) | 9/158 (6%) | 47/47 (100%) | 77/77 (100%) |
| fake | lie | 13 | `fake`, `␣fake`, `Fake`, `␣Fake`, `伪造`, `_fake`, `假`, `.fake`, `假冒`, `虚假` … (+4) | think_slot1 | 152/152 (100%) | 80/81 (99%) | 136/138 (99%) | 106/158 (67%) | 47/47 (100%) | 76/77 (99%) |
| incorrect | lie | 15 | `␣Incorrect`, `incorrect`, `␣incorrect`, `Incorrect`, `␣inaccurate`, `␣incorrectly`, `不符合`, `␣inaccur`, `␣erroneous`, `错误的` … (+4) | q_tok3 | 151/152 (99%) | 81/81 (100%) | 138/138 (100%) | 148/158 (94%) | 46/47 (98%) | 77/77 (100%) |
| lawful / legal | unclear | 4 | `/legal`, `合法`, `legal`, `_legal`, `␣legality`, `␣legally`, `␣Legal` | think_slot0 | 152/152 (100%) | 80/81 (99%) | 136/138 (99%) | 156/158 (99%) | 47/47 (100%) | 76/77 (99%) |
| accurate | truth | 8 | `␣accuracy`, `␣accurate`, `␣accurately`, `␣Accuracy`, `accur`, `准确`, `accuracy`, `Accuracy`, `准确的`, `_accuracy` … (+2) | q_tok3 | 151/152 (99%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 76/77 (99%) |
| hidden / secret | lie | 1 | `隐秘` | think_slot0 | 151/152 (99%) | 80/81 (99%) | 137/138 (99%) | 125/158 (79%) | 47/47 (100%) | 76/77 (99%) |
| privacy | unclear | 3 | `␣Privacy`, `␣privacy`, `privacy`, `Privacy`, `隐私`, `␣privacidad`, `/Private`, `␣Priv`, `ความเป็นส่วนตัว` | think_slot2 | 150/152 (99%) | 80/81 (99%) | 138/138 (100%) | 157/158 (99%) | 46/47 (98%) | 76/77 (99%) |
| forbidden / unauthorized | unclear | 3 | `␣Unauthorized`, `␣Forbidden`, `严禁`, `禁止`, `␣prohibited`, `禁用`, `禁忌`, `␣запрещ`, `取缔`, `␣unauthorized` … (+1) | think_slot2 | 150/152 (99%) | 79/81 (98%) | 62/138 (45%) | 26/158 (16%) | 45/47 (96%) | 75/77 (97%) |
| misinformation | lie | 12 | `␣misinformation`, `虚假信息` | q_tok4 | 147/152 (97%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 46/47 (98%) | 76/77 (99%) |
| violate | unclear | 11 | `违反`, `违背`, `违规`, `␣violates`, `␣violating`, `␣violate`, `违反了`, `␣violation`, `␣violated`, `␣violations` … (+4) | think_slot1 | 148/152 (97%) | 79/81 (98%) | 130/138 (94%) | 120/158 (76%) | 43/47 (91%) | 75/77 (97%) |
| unauthorized | unclear | 4 | `␣Unauthorized`, `␣unauthorized`, `Unauthorized` | think_slot2 | 149/152 (98%) | 77/81 (95%) | 61/138 (44%) | 26/158 (16%) | 44/47 (94%) | 73/77 (95%) |
| correct | truth | 13 | `␣correctness`, `␣correct`, `␣Correct`, `正确`, `␣correctly`, `Correct`, `正确的`, `修正`, `correct`, `正确答案` … (+19) | q_tok3 | 143/152 (94%) | 78/81 (96%) | 138/138 (100%) | 158/158 (100%) | 38/47 (81%) | 74/77 (96%) |
| honest | truth | 12 | `␣honesty`, `␣honest`, `诚实`, `␣honestly`, `␣Honest`, `坦诚`, `诚实守信`, `␣truthful`, `如实`, `实事求是` | q_tok3 | 148/152 (97%) | 68/81 (84%) | 94/138 (68%) | 3/158 (2%) | 45/47 (96%) | 66/77 (86%) |
| leak | unclear | 3 | `␣WikiLeaks`, `泄露` | think_slot2 | 142/152 (93%) | 72/81 (89%) | 88/138 (64%) | 35/158 (22%) | 42/47 (89%) | 69/77 (90%) |
| true | truth | 14 | `␣TRUE`, `真实`, `真实的`, `的真实`, `真实性`, `␣True`, `的真实性`, `确实`, `True`, `␣true` … (+16) | think_slot3 | 131/152 (86%) | 77/81 (95%) | 135/138 (98%) | 97/158 (61%) | 26/47 (55%) | 73/77 (95%) |
| silence | unclear | 2 | `␣Silence`, `沉默`, `␣Silent`, `␣silence`, `silent`, `␣Quiet` | think_slot2 | 131/152 (86%) | 75/81 (93%) | 60/138 (43%) | 3/158 (2%) | 40/47 (85%) | 71/77 (92%) |
| hide | lie | 3 | `␣hiding`, `隐藏`, `␣hidden`, `␣masking`, `hide`, `hidden`, `隐蔽`, `隐瞒`, `掩盖`, `␣conceal` … (+17) | preans_slot1 | 138/152 (91%) | 64/81 (79%) | 81/138 (59%) | 9/158 (6%) | 43/47 (91%) | 62/77 (81%) |
| strict | unclear | 1 | `␣STRICT`, `␣Strict`, `严格`, `.strict`, `strict`, `␣strictly`, `Strict`, `严` | think_slot2 | 125/152 (82%) | 72/81 (89%) | 85/138 (62%) | 18/158 (11%) | 41/47 (87%) | 71/77 (92%) |
| compliant | unclear | 7 | `合规`, `␣compliance`, `␣Compliance`, `依法`, `␣compliant`, `依法依规`, `依规`, `严格遵守` | think_slot0 | 130/152 (86%) | 63/81 (78%) | 130/138 (94%) | 1/158 (1%) | 41/47 (87%) | 61/77 (79%) |
| comply | unclear | 6 | `␣compliance`, `遵守`, `合规`, `␣Compliance`, `严格遵守`, `␣compliant`, `␣complying`, `␣comply`, `␣complied`, `␣adher` … (+9) | q_tok3 | 118/152 (78%) | 69/81 (85%) | 94/138 (68%) | 75/158 (47%) | 23/47 (49%) | 65/77 (84%) |
| intentional | unclear | 7 | `␣intentionally`, `␣deliberately`, `␣intentional`, `故意`, `␣deliberate`, `刻意`, `故意的`, `␣intention`, `␣intent`, `␣intentions` … (+4) | q_tok4 | 112/152 (74%) | 57/81 (70%) | 122/138 (88%) | 66/158 (42%) | 40/47 (85%) | 55/77 (71%) |
| biased | unclear | 1 | `␣biased` | q_tok3 | 105/152 (69%) | 59/81 (73%) | 124/138 (90%) | 112/158 (71%) | 26/47 (55%) | 56/77 (73%) |
| unethical | lie/unclear | 13 | `␣unethical`, `␣immoral` | postans_slot4 | 113/152 (74%) | 50/81 (62%) | 5/138 (4%) | 0/158 (0%) | 20/47 (43%) | 49/77 (64%) |
| clarify | unclear | 6 | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` | think_slot0 | 102/152 (67%) | 58/81 (72%) | 138/138 (100%) | 156/158 (99%) | 28/47 (60%) | 54/77 (70%) |
| ethical | truth/unclear | 8 | `␣ethical`, `ethical`, `␣moral`, `␣Moral` | postans_slot4 | 109/152 (72%) | 46/81 (57%) | 13/138 (9%) | 0/158 (0%) | 28/47 (60%) | 45/77 (58%) |
| cannot / unable | unclear | 3 | `cannot`, `␣Cannot`, `我无法`, `我不能`, `无法满足`, `无法`, `不能满足`, `Cannot`, `不能`, `␣cannot` … (+5) | think_slot2 | 93/152 (61%) | 61/81 (75%) | 6/138 (4%) | 0/158 (0%) | 43/47 (91%) | 58/77 (75%) |
| misrepresent | lie | 4 | `␣misrepresented` | preans_slot1 | 118/152 (78%) | 33/81 (41%) | 17/138 (12%) | 10/158 (6%) | 29/47 (62%) | 31/77 (40%) |
| ethics | unclear | 5 | `道德`, `␣moral`, `伦理`, `␣morally`, `␣ethical`, `ethical`, `␣ethics`, `␣Ethics`, `的道德`, `␣morality` … (+4) | preans_slot4 | 108/152 (71%) | 43/81 (53%) | 0/138 (0%) | 0/158 (0%) | 22/47 (47%) | 39/77 (51%) |
| disclose | truth | 8 | `␣disclosure`, `␣Disclosure`, `␣disclosures`, `␣disclosing`, `␣disclose`, `公开`, `␣disclosed`, `信息公开`, `披露`, `信息披露` … (+3) | think_slot2 | 103/152 (68%) | 43/81 (53%) | 110/138 (80%) | 139/158 (88%) | 23/47 (49%) | 40/77 (52%) |
| ethics / morality | unclear | 4 | `道德`, `␣Ethics`, `␣morally`, `␣ethics`, `伦理`, `␣moral`, `的道德`, `␣Moral`, `␣morality`, `␣ethic` … (+4) | postans_slot4 | 99/152 (65%) | 42/81 (52%) | 9/138 (7%) | 0/158 (0%) | 26/47 (55%) | 41/77 (53%) |
| wrong | lie | 17 | `错误`, `␣Wrong`, `␣WRONG`, `错`, `误`, `␣wrong`, `错了`, `␣ERROR`, `的错误`, `是错误的` … (+7) | think_slot1 | 92/152 (61%) | 48/81 (59%) | 60/138 (43%) | 14/158 (9%) | 31/47 (66%) | 46/77 (60%) |
| fact | truth/unclear | 10 | `␣factual`, `事实`, `␣Facts`, `␣facts`, `␣fact`, `␣actually`, `␣actual`, `Fact`, `fact`, `␣Actual` … (+27) | q_tok3 | 103/152 (68%) | 36/81 (44%) | 132/138 (96%) | 96/158 (61%) | 40/47 (85%) | 35/77 (45%) |
| illusion / fantasy | unclear | 1 | `幻想`, `虚幻`, `错觉`, `妄想` | think_slot1 | 93/152 (61%) | 42/81 (52%) | 26/138 (19%) | 1/158 (1%) | 33/47 (70%) | 41/77 (53%) |
| fictional / made-up | lie | 2 | `虚构`, `fiction`, `伪造` | think_slot0 | 82/152 (54%) | 51/81 (63%) | 27/138 (20%) | 0/158 (0%) | 36/47 (77%) | 50/77 (65%) |
| critique | unclear | 4 | `␣critique`, `批判`, `批评`, `␣critic`, `␣critiques`, `␣kritik`, `␣Kritik`, `␣criticize`, `␣criticisms`, `␣criticizing` | postans_slot2 | 91/152 (60%) | 38/81 (47%) | 0/138 (0%) | 1/158 (1%) | 19/47 (40%) | 35/77 (45%) |
| verify | unclear | 1 | `␣Verification`, `_verified`, `核实`, `␣Verified`, `_verification`, `␣verification`, `验证`, `.verify` | think_slot2 | 83/152 (55%) | 43/81 (53%) | 126/138 (91%) | 152/158 (96%) | 20/47 (43%) | 41/77 (53%) |
| appropriate | unclear | 1 | `␣appropriate`, `␣appropriately` | q_tok3 | 80/152 (53%) | 41/81 (51%) | 17/138 (12%) | 45/158 (28%) | 8/47 (17%) | 38/77 (49%) |
| illegal | unclear | 9 | `非法`, `违法`, `␣illegal`, `illegal`, `Illegal`, `␣Illegal`, `␣illegally`, `␣unlawful`, `违法违规`, `␣ilegal` | think_slot0 | 73/152 (48%) | 34/81 (42%) | 56/138 (41%) | 31/158 (20%) | 30/47 (64%) | 33/77 (43%) |
| fabricate | lie | 8 | `伪造`, `虚构`, `弄虚作假`, `造假`, `␣fabricated`, `␣fabrication`, `␣fictional`, `␣invented`, `␣invent`, `␣invention` … (+1) | preans_slot1 | 94/152 (62%) | 10/81 (12%) | 44/138 (32%) | 27/158 (17%) | 22/47 (47%) | 8/77 (10%) |
| whistleblow | unclear | 3 | `举报`, `␣whistlebl`, `␣whistleblower` | postans_slot4 | 73/152 (48%) | 24/81 (30%) | 3/138 (2%) | 0/158 (0%) | 6/47 (13%) | 23/77 (30%) |
| inappropriate | unclear | 1 | `␣inappropriate` | q_tok3 | 61/152 (40%) | 36/81 (44%) | 1/138 (1%) | 4/158 (3%) | 7/47 (15%) | 33/77 (43%) |
| secret | lie/unclear | 8 | `␣secrecy`, `秘密`, `␣secretly`, `␣secretive`, `的秘密`, `␣covert`, `隐秘`, `␣secret`, `secret`, `Secret` … (+7) | preans_slot2 | 78/152 (51%) | 17/81 (21%) | 1/138 (1%) | 0/158 (0%) | 29/47 (62%) | 15/77 (19%) |
| confidential | lie/unclear | 9 | `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential`, `机密`, `␣конфиден` | think_slot2 | 57/152 (38%) | 31/81 (38%) | 85/138 (62%) | 6/158 (4%) | 13/47 (28%) | 28/77 (36%) |
| cannot | unclear | 4 | `无法`, `无法满足`, `␣Cannot`, `不能说`, `␣cannot`, `根本无法`, `不能完全`, `我无法`, `cannot`, `Cannot` … (+4) | preans_slot3 | 73/152 (48%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 28/47 (60%) | 13/77 (17%) |
| factual | truth | 2 | `␣factual` | preans_slot2 | 69/152 (45%) | 18/81 (22%) | 125/138 (91%) | 47/158 (30%) | 23/47 (49%) | 17/77 (22%) |
| fantasy | unclear | 1 | `幻想` | think_slot1 | 68/152 (45%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 27/47 (57%) | 19/77 (25%) |
| disclaimer | unclear | 8 | `␣Disclaimer`, `␣disclaimer`, `␣DISCLAIMER`, `Disclaimer`, `免责声明` | postans_slot1 | 78/152 (51%) | 7/81 (9%) | 46/138 (33%) | 2/158 (1%) | 11/47 (23%) | 6/77 (8%) |
| fictional | unclear | 4 | `␣fictional`, `fiction`, `虚构`, `␣fict`, `␣Fiction`, `␣fiction`, `-fiction` | preans_slot1 | 66/152 (43%) | 19/81 (23%) | 89/138 (64%) | 84/158 (53%) | 14/47 (30%) | 16/77 (21%) |
| falsehood | lie | 1 | `␣falsehood` | q_tok10 | 72/152 (47%) | 12/81 (15%) | 84/138 (61%) | 56/158 (35%) | 17/47 (36%) | 9/77 (12%) |
| refuse | unclear | 14 | `拒绝`, `␣refusal`, `␣refus`, `␣refusing`, `拒`, `拒絕`, `␣refused`, `␣refuse`, `␣refuses`, `拒绝了` … (+5) | think_slot2 | 57/152 (38%) | 26/81 (32%) | 0/138 (0%) | 0/158 (0%) | 38/47 (81%) | 26/77 (34%) |
| reject / veto | unclear | 3 | `否决`, `␣Reject`, `␣rejecting`, `拒绝`, `␣refusal`, `拒絕`, `reject`, `.reject`, `rejected`, `拒` … (+2) | think_slot2 | 57/152 (38%) | 26/81 (32%) | 0/138 (0%) | 0/158 (0%) | 38/47 (81%) | 26/77 (34%) |
| reality | unclear | 3 | `实际情况`, `␣reality`, `␣Reality`, `Reality`, `␣realities`, `␣réalité`, `但实际上`, `根据实际情况`, `实际上`, `␣realidad` … (+2) | preans_slot2 | 71/152 (47%) | 11/81 (14%) | 13/138 (9%) | 2/158 (1%) | 20/47 (43%) | 11/77 (14%) |
| claim | unclear | 4 | `声称`, `␣claims`, `␣claim`, `␣Claim`, `␣assertions`, `␣claiming`, `claim`, `宣称`, `Claim`, `␣Claims` … (+7) | preans_slot1 | 63/152 (41%) | 17/81 (21%) | 10/138 (7%) | 8/158 (5%) | 17/47 (36%) | 14/77 (18%) |
| spoiler | unclear | 1 | `Spoiler` | think_slot2 | 63/152 (41%) | 17/81 (21%) | 1/138 (1%) | 1/158 (1%) | 8/47 (17%) | 14/77 (18%) |
| moral | unclear | 4 | `␣morally`, `␣moral`, `␣Moral` | postans_slot4 | 58/152 (38%) | 19/81 (23%) | 1/138 (1%) | 0/158 (0%) | 14/47 (30%) | 18/77 (23%) |
| contradict | unclear | 3 | `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contrad`, `␣contradictions`, `矛盾`, `␣contradd`, `矛盾的` | preans_slot1 | 55/152 (36%) | 22/81 (27%) | 45/138 (33%) | 8/158 (5%) | 23/47 (49%) | 21/77 (27%) |
| impossible | unclear | 6 | `␣Impossible`, `Impossible`, `␣impossible`, `␣imposs`, `␣impossibile` | think_slot2 | 46/152 (30%) | 31/81 (38%) | 27/138 (20%) | 78/158 (49%) | 31/47 (66%) | 31/77 (40%) |
| deliberate | unclear | 2 | `故意`, `␣deliberately`, `␣intentionally`, `␣deliberate`, `␣intentional`, `刻意`, `␣purposely`, `有意`, `故意的`, `␣sengaja` … (+1) | q_tok10 | 65/152 (43%) | 8/81 (10%) | 6/138 (4%) | 0/158 (0%) | 3/47 (6%) | 4/77 (5%) |
| doubt / question | unclear | 1 | `质疑` | think_slot0 | 53/152 (35%) | 17/81 (21%) | 64/138 (46%) | 131/158 (83%) | 22/47 (47%) | 17/77 (22%) |
| mistake | unclear | 4 | `␣mistake`, `␣mistakes`, `␣mistaken`, `␣mistakenly` | q_tok3 | 36/152 (24%) | 32/81 (40%) | 46/138 (33%) | 0/158 (0%) | 21/47 (45%) | 32/77 (42%) |
| knowingly | unclear | 5 | `␣knowingly`, `明知`, `␣knowing`, `␣consciously`, `␣Knowing` | q_tok10 | 62/152 (41%) | 3/81 (4%) | 1/138 (1%) | 2/158 (1%) | 7/47 (15%) | 1/77 (1%) |
| undisclosed | lie | 3 | `␣undisclosed` | preans_slot2 | 54/152 (36%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 13/47 (28%) | 9/77 (12%) |
| hide / conceal | lie | 4 | `隐瞒`, `-hide`, `masked`, `藏`, `掩`, `␣hidden`, `␣Hidden`, `-hidden`, `隐藏`, `hidden` … (+12) | postans_slot1 | 58/152 (38%) | 5/81 (6%) | 14/138 (10%) | 4/158 (3%) | 8/47 (17%) | 4/77 (5%) |
| prohibited | unclear | 5 | `禁止`, `␣prohibited`, `␣prohibition` | q_tok10 | 42/152 (28%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 7/47 (15%) | 20/77 (26%) |
| sincere | truth | 3 | `真诚`, `␣sincerity`, `␣sincere`, `␣sincerely` | q_tok3 | 45/152 (30%) | 11/81 (14%) | 2/138 (1%) | 0/158 (0%) | 22/47 (47%) | 11/77 (14%) |
| intent | unclear | 2 | `␣intention`, `␣intent`, `Intent`, `␣Intent`, `intent`, `意图` | q_tok4 | 28/152 (18%) | 27/81 (33%) | 43/138 (31%) | 1/158 (1%) | 14/47 (30%) | 26/77 (34%) |
| imply | unclear | 3 | `␣implicitly`, `␣implicit`, `␣implying`, `暗示`, `隐含`, `␣implied`, `implicitly`, `␣Implicit`, `implicit`, `␣implication` … (+6) | preans_slot1 | 29/152 (19%) | 25/81 (31%) | 25/138 (18%) | 28/158 (18%) | 12/47 (26%) | 22/77 (29%) |
| assert | unclear | 3 | `␣assertions`, `␣assert`, `␣asserting`, `assert`, `␣assertion`, `␣asserted`, `␣asserts`, `/assert`, `_assert`, `␣Assert` … (+5) | preans_slot1 | 40/152 (26%) | 13/81 (16%) | 20/138 (14%) | 4/158 (3%) | 15/47 (32%) | 11/77 (14%) |
| blame | unclear | 2 | `␣blaming`, `␣blame`, `␣blames`, `␣blamed` | preans_slot1 | 43/152 (28%) | 7/81 (9%) | 4/138 (3%) | 0/158 (0%) | 4/47 (9%) | 6/77 (8%) |
| honest / truthful | truth | 1 | `␣truthful`, `␣Honest` | think_slot3 | 42/152 (28%) | 7/81 (9%) | 9/138 (7%) | 1/158 (1%) | 10/47 (21%) | 7/77 (9%) |
| prohibit | unclear | 3 | `禁止`, `严禁`, `␣prohibited`, `␣prohibit`, `禁令` | postans_slot4 | 31/152 (20%) | 16/81 (20%) | 22/138 (16%) | 0/158 (0%) | 3/47 (6%) | 16/77 (21%) |
| forbid | unclear | 1 | `禁止`, `␣prohibited`, `␣Forbidden`, `␣forbidden`, `Forbidden`, `␣prohibit` | postans_slot4 | 31/152 (20%) | 16/81 (20%) | 22/138 (16%) | 0/158 (0%) | 3/47 (6%) | 16/77 (21%) |
| quiet / stealthy | unclear | 1 | `悄然` | think_slot0 | 32/152 (21%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 18/47 (38%) | 15/77 (19%) |
| refute | unclear | 2 | `␣refute`, `反驳` | think_slot2 | 30/152 (20%) | 17/81 (21%) | 6/138 (4%) | 0/158 (0%) | 19/47 (40%) | 16/77 (21%) |
| integrity | truth | 7 | `诚信`, `␣Integrity`, `␣integrity`, `正直` | postans_slot4 | 37/152 (24%) | 8/81 (10%) | 7/138 (5%) | 0/158 (0%) | 13/47 (28%) | 8/77 (10%) |
| hypothetical | unclear | 3 | `␣hypothetical` | preans_slot2 | 14/152 (9%) | 27/81 (33%) | 39/138 (28%) | 11/158 (7%) | 7/47 (15%) | 27/77 (35%) |
| accusation | unclear | 3 | `␣accusations`, `␣accusation`, `␣accusing` | q_tok5 | 11/152 (7%) | 26/81 (32%) | 16/138 (12%) | 2/158 (1%) | 10/47 (21%) | 25/77 (32%) |
| misunderstand | unclear | 2 | `␣misunderstanding`, `␣misunderstood`, `␣misunderstand`, `误解` | q_tok3 | 15/152 (10%) | 20/81 (25%) | 8/138 (6%) | 0/158 (0%) | 13/47 (28%) | 20/77 (26%) |
| pretend | lie | 4 | `␣pretending`, `␣pretend`, `假装`, `伪装` | q_tok10 | 26/152 (17%) | 8/81 (10%) | 8/138 (6%) | 1/158 (1%) | 6/47 (13%) | 5/77 (6%) |
| evade | lie | 4 | `␣evasion`, `回避`, `␣evade`, `规避`, `逃避` | preans_slot1 | 19/152 (12%) | 13/81 (16%) | 3/138 (2%) | 0/158 (0%) | 11/47 (23%) | 13/77 (17%) |
| disguise | lie | 4 | `伪装`, `␣masking`, `␣disgu`, `␣disguise`, `␣disguised` | preans_slot1 | 23/152 (15%) | 8/81 (10%) | 3/138 (2%) | 5/158 (3%) | 6/47 (13%) | 7/77 (9%) |
| hypocrisy | lie | 7 | `␣hypocrisy`, `虚伪` | preans_slot2 | 17/152 (11%) | 13/81 (16%) | 1/138 (1%) | 0/158 (0%) | 6/47 (13%) | 13/77 (17%) |
| lawful | unclear | 3 | `合法`, `␣lawful`, `␣legitimate`, `␣legitim`, `␣legitimately` | preans_slot4 | 25/152 (16%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 16/47 (34%) | 4/77 (5%) |
| inform | unclear | 2 | `告知` | preans_slot1 | 21/152 (14%) | 9/81 (11%) | 23/138 (17%) | 2/158 (1%) | 0/47 (0%) | 7/77 (9%) |
| omit | lie | 3 | `␣omitted`, `␣omission`, `␣omit`, `omit`, `省略`, `␣OMIT`, `遗漏` | preans_slot1 | 18/152 (12%) | 11/81 (14%) | 2/138 (1%) | 4/158 (3%) | 11/47 (23%) | 11/77 (14%) |
| apology | unclear | 6 | `␣apology`, `␣apologies`, `␣Sorry`, `␣sorry`, `Sorry`, `抱歉`, `道歉` | q_tok2 | 15/152 (10%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 10/47 (21%) | 14/77 (18%) |
| legal | unclear | 3 | `合法`, `␣legality`, `依法`, `␣Legal`, `␣legally`, `Legal`, `legal`, `␣legal`, `␣lawful`, `合法的` … (+3) | postans_slot1 | 13/152 (9%) | 15/81 (19%) | 2/138 (1%) | 0/158 (0%) | 13/47 (28%) | 15/77 (19%) |
| genuine | truth | 3 | `␣genuinely`, `␣genuine`, `␣authentic`, `␣Genuine` | think_slot2 | 18/152 (12%) | 10/81 (12%) | 3/138 (2%) | 1/158 (1%) | 2/47 (4%) | 9/77 (12%) |
| candid | truth | 4 | `坦诚`, `␣straightforward`, `直言` | preans_slot1 | 0/152 (0%) | 26/81 (32%) | 38/138 (28%) | 46/158 (29%) | 0/47 (0%) | 26/77 (34%) |
| simulated | unclear | 3 | `␣simulated`, `模拟`, `␣simulation`, `␣simulate`, `␣Simulation`, `␣simulations` | preans_slot4 | 22/152 (14%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 3/77 (4%) |
| hidden | lie | 2 | `␣Hidden`, `_hide` | think_slot2 | 17/152 (11%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 7/77 (9%) |
| vague | unclear | 2 | `模糊`, `␣vague`, `含糊`, `␣vaguely` | preans_slot1 | 13/152 (9%) | 11/81 (14%) | 0/138 (0%) | 2/158 (1%) | 7/47 (15%) | 9/77 (12%) |
| reject | unclear | 7 | `␣rejection`, `␣rejecting`, `␣Reject`, `␣rejected`, `reject`, `Reject`, `␣reject`, `rejected`, `Rejected`, `.reject` … (+2) | preans_slot1 | 1/152 (1%) | 22/81 (27%) | 3/138 (2%) | 0/158 (0%) | 1/47 (2%) | 22/77 (29%) |
| role-play | unclear | 2 | `角色扮演`, `扮演` | preans_slot2 | 7/152 (5%) | 16/81 (20%) | 2/138 (1%) | 1/158 (1%) | 5/47 (11%) | 15/77 (19%) |
| ambiguous | unclear | 2 | `␣ambiguous`, `␣ambiguity`, `␣ambigu`, `ambiguous` | preans_slot1 | 11/152 (7%) | 11/81 (14%) | 1/138 (1%) | 12/158 (8%) | 7/47 (15%) | 9/77 (12%) |
| mask / disguise | lie | 3 | `伪装`, `masked`, `␣disguised`, `␣disguise` | postans_slot4 | 3/152 (2%) | 18/81 (22%) | 6/138 (4%) | 8/158 (5%) | 1/47 (2%) | 18/77 (23%) |
| opaque | lie | 1 | `opaque` | think_slot2 | 11/152 (7%) | 9/81 (11%) | 44/138 (32%) | 2/158 (1%) | 1/47 (2%) | 8/77 (10%) |
| transparent | truth | 4 | `␣transparency`, `␣Transparency`, `透明`, `透明度`, `␣transparent`, `透明的` | postans_slot4 | 14/152 (9%) | 5/81 (6%) | 0/138 (0%) | 2/158 (1%) | 4/47 (9%) | 5/77 (6%) |
| cheat | lie | 4 | `␣cheating`, `作弊` | q_tok10 | 18/152 (12%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 1/77 (1%) |
| trap | unclear | 1 | `陷阱`, `␣trap`, `␣Trap`, `trap`, `␣trapped`, `␣traps`, `Trap`, `␣trapping`, `_trap`, `␣atrap` | postans_slot4 | 10/152 (7%) | 8/81 (10%) | 2/138 (1%) | 1/158 (1%) | 9/47 (19%) | 8/77 (10%) |
| avoid | unclear | 2 | `␣avoidance`, `␣avoided`, `␣avoiding`, `avoid`, `避开`, `␣Avoid`, `避免`, `Avoid`, `␣avoid`, `␣avoids` … (+1) | preans_slot1 | 6/152 (4%) | 11/81 (14%) | 1/138 (1%) | 0/158 (0%) | 6/47 (13%) | 11/77 (14%) |
| suppress | lie | 2 | `suppress`, `.Suppress` | think_slot0 | 3/152 (2%) | 14/81 (17%) | 2/138 (1%) | 0/158 (0%) | 2/47 (4%) | 14/77 (18%) |
| unequivocal | unclear | 1 | `␣unequiv`, `␣unmistak` | think_slot3 | 15/152 (10%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 12/47 (26%) | 2/77 (3%) |
| accountability | unclear | 1 | `␣Accountability`, `␣accountability` | postans_slot4 | 15/152 (10%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| legitimate | unclear | 3 | `␣legitimate`, `␣legitimately`, `␣legitim`, `␣legitimacy`, `合法` | preans_slot4 | 12/152 (8%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/47 (9%) | 3/77 (4%) |
| harmful | unclear | 2 | `␣harmful` | q_tok3 | 8/152 (5%) | 8/81 (10%) | 1/138 (1%) | 3/158 (2%) | 1/47 (2%) | 7/77 (9%) |
| ostensible | lie | 1 | `␣ostensibly` | think_slot2 | 13/152 (9%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 8/47 (17%) | 3/77 (4%) |
| forced / coerced | unclear | 3 | `逼`, `␣forced`, `forced`, `␣Forced`, `迫`, `强制`, `被迫`, `倒逼`, `逼迫`, `␣forcing` … (+6) | postans_slot4 | 10/152 (7%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 6/47 (13%) | 5/77 (6%) |
| believable | unclear | 1 | `␣believable` | q_tok3 | 15/152 (10%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| candour | truth | 1 | `坦诚` | q_tok10 | 0/152 (0%) | 15/81 (19%) | 50/138 (36%) | 4/158 (3%) | 0/47 (0%) | 15/77 (19%) |
| transparency | truth | 1 | `␣transparency`, `␣Transparency`, `透明`, `␣transparent`, `透明度`, `transparent`, `透明的`, `␣Transparent` | q_tok10 | 4/152 (3%) | 11/81 (14%) | 19/138 (14%) | 0/158 (0%) | 4/47 (9%) | 11/77 (14%) |
| trick | lie | 2 | `␣Trick`, `␣trick`, `␣tricks`, `␣Tricks` | postans_slot4 | 6/152 (4%) | 8/81 (10%) | 7/138 (5%) | 1/158 (1%) | 6/47 (13%) | 8/77 (10%) |
| framing | unclear | 2 | `␣framing` | preans_slot1 | 8/152 (5%) | 6/81 (7%) | 4/138 (3%) | 2/158 (1%) | 4/47 (9%) | 4/77 (5%) |
| justify | unclear | 3 | `辩解`, `␣justification`, `justify` | postans_slot1 | 10/152 (7%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 10/47 (21%) | 3/77 (4%) |
| censor | unclear | 1 | `␣censorship` | postans_slot4 | 3/152 (2%) | 10/81 (12%) | 9/138 (7%) | 0/158 (0%) | 1/47 (2%) | 10/77 (13%) |
| noncompliant | lie | 1 | `不符合` | q_tok10 | 3/152 (2%) | 10/81 (12%) | 3/138 (2%) | 1/158 (1%) | 3/47 (6%) | 10/77 (13%) |
| exaggerate | lie | 2 | `夸大`, `␣exaggerated`, `␣exagger` | preans_slot1 | 8/152 (5%) | 4/81 (5%) | 1/138 (1%) | 3/158 (2%) | 2/47 (4%) | 4/77 (5%) |
| misunderstanding | unclear | 1 | `误解` | think_slot0 | 6/152 (4%) | 6/81 (7%) | 19/138 (14%) | 140/158 (89%) | 2/47 (4%) | 6/77 (8%) |
| phishing | lie | 1 | `␣phishing` | postans_slot4 | 3/152 (2%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 2/47 (4%) | 8/77 (10%) |
| allegation | unclear | 2 | `␣allegations`, `␣allegation` | q_tok2 | 9/152 (6%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 9/47 (19%) | 2/77 (3%) |
| confess | truth | 4 | `␣confession`, `坦白`, `␣confess` | preans_slot1 | 0/152 (0%) | 10/81 (12%) | 18/138 (13%) | 4/158 (3%) | 0/47 (0%) | 10/77 (13%) |
| conscience | unclear | 3 | `␣conscience` | think_slot2 | 6/152 (4%) | 4/81 (5%) | 0/138 (0%) | 6/158 (4%) | 1/47 (2%) | 4/77 (5%) |
| manipulate | lie | 6 | `␣manipulated`, `␣manipulation`, `␣manipulate`, `␣manipulating`, `诱导`, `␣manipul`, `␣manip`, `Manip`, `操纵` | q_tok4 | 4/152 (3%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 6/77 (8%) |
| withhold | lie | 4 | `␣withholding`, `␣withheld`, `␣withhold` | preans_slot1 | 7/152 (5%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 5/47 (11%) | 3/77 (4%) |
| accuse | unclear | 1 | `␣accusations`, `␣accusing`, `␣accusation` | postans_slot4 | 6/152 (4%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 2/47 (4%) | 4/77 (5%) |
| loophole | unclear | 1 | `␣loophole` | postans_slot4 | 3/152 (2%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 7/77 (9%) |
| liar | lie | 2 | `␣liar` | preans_slot1 | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 5/47 (11%) | 0/77 (0%) |
| cover up | lie | 2 | `掩饰`, `掩盖`, `隐` | q_tok10 | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| contradiction | unclear | 2 | `␣contradict`, `␣contradictory`, `矛盾`, `␣contradiction`, `␣contradictions` | postans_slot1 | 3/152 (2%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 2/47 (4%) | 5/77 (6%) |
| blackmail | unclear | 1 | `␣blackmail` | postans_slot4 | 4/152 (3%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 2/47 (4%) | 4/77 (5%) |
| responsible | unclear | 2 | `␣responsibly`, `␣responsibilities`, `␣Responsibilities` | postans_slot4 | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| reveal | truth | 2 | `揭露`, `␣revealing` | preans_slot2 | 8/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| minimize | unclear | 1 | `␣minimizing`, `␣minimized`, `␣minimize`, `␣minimise` | preans_slot1 | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 3/77 (4%) |
| decline | unclear | 2 | `␣declined`, `␣declining`, `␣declines`, `␣decline` | preans_slot1 | 0/152 (0%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 8/77 (10%) |
| wrongdoing | lie | 1 | `␣wrongdoing`, `␣wrongful` | preans_slot2 | 4/152 (3%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 4/77 (5%) |
| hypocritical | lie | 2 | `虚伪` | q_tok4 | 4/152 (3%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 4/77 (5%) |
| adhere | unclear | 1 | `␣adher`, `␣adherence`, `␣adhere`, `遵循` | q_tok3 | 4/152 (3%) | 4/81 (5%) | 0/138 (0%) | 2/158 (1%) | 1/47 (2%) | 4/77 (5%) |
| dissent | unclear | 1 | `␣dissent` | think_slot2 | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 5/47 (11%) | 2/77 (3%) |
| truth | truth | 1 | `其真实性` | think_slot2 | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 2/77 (3%) |
| apologize | unclear | 3 | `␣Sorry`, `道歉`, `抱歉`, `Sorry` | preans_slot3 | 4/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 3/77 (4%) |
| cooperate | unclear | 1 | `配合`, `积极配合`, `的配合` | q_tok10 | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| promotional | unclear | 1 | `␣promotional`, `␣promoting`, `宣传` | postans_slot2 | 3/152 (2%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 3/77 (4%) |
| indirect | unclear | 1 | `␣indirect`, `␣indirectly`, `␣INDIRECT` | preans_slot1 | 2/152 (1%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 2/47 (4%) | 4/77 (5%) |
| unintentional | unclear | 3 | `␣unintention`, `␣accidental`, `␣inadvertently` | q_tok3 | 1/152 (1%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 5/77 (6%) |
| fiction | unclear | 1 | `␣fictional`, `␣Fiction`, `fiction` | postans_slot4 | 1/152 (1%) | 4/81 (5%) | 4/138 (3%) | 1/158 (1%) | 0/47 (0%) | 4/77 (5%) |
| negligence | unclear | 2 | `␣negligence`, `␣negligent` | q_tok0 | 1/152 (1%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 1/47 (2%) | 4/77 (5%) |
| cowardice | unclear | 1 | `␣coward` | think_slot2 | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 3/47 (6%) | 2/77 (3%) |
| skepticism | unclear | 1 | `␣skepticism` | think_slot2 | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 2/77 (3%) |
| spin | unclear | 1 | `␣spin`, `spin`, `Spin`, `␣spins`, `␣spinning`, `␣Spin`, `-spin`, `_spin`, `.spin` | preans_slot1 | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 2/77 (3%) |
| perfunctory | unclear | 1 | `敷衍` | q_tok3 | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 1/77 (1%) |
| persuade | unclear | 1 | `␣persuasive`, `␣persuasion`, `劝`, `␣persuade`, `劝说`, `劝导`, `␣persu` | postans_slot2 | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 2/77 (3%) |
| guilty | unclear | 1 | `␣guilty` | preans_slot2 | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| improper | unclear | 1 | `␣improper`, `␣improperly` | q_tok0 | 1/152 (1%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 1/47 (2%) | 2/77 (3%) |
| sincerity | truth | 1 | `␣sincerity` | q_tok10 | 1/152 (1%) | 2/81 (2%) | 3/138 (2%) | 1/158 (1%) | 0/47 (0%) | 2/77 (3%) |
| betrayal | lie | 1 | `␣betrayal` | preans_slot2 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| omission | lie | 1 | `␣omission` | q_tok4 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| expose | truth | 2 | `揭露` | postans_slot4 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| irresponsible | unclear | 1 | `␣irresponsible` | postans_slot2 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| inaccurate | lie | 2 | `不准确` | preans_slot1 | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 3/158 (2%) | 0/47 (0%) | 1/77 (1%) |
| hoax | lie | 1 | `␣hoax` | q_tok4 | 0/152 (0%) | 1/81 (1%) | 18/138 (13%) | 149/158 (94%) | 0/47 (0%) | 1/77 (1%) |
| plagiarize | unclear | 1 | `␣plagiar` | q_tok3 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 11/158 (7%) | 0/47 (0%) | 0/77 (0%) |
| authentic | truth | 1 | `␣authenticity` | q_tok10 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| secretly | lie | 1 | `暗中` | think_slot1 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| defiance | unclear | 2 | `␣defiance`, `␣defiant` | think_slot2 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |

**wording Q6_factual, positions from the question on** (147 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|---|---|
| lie | lie | 13 | `谎言`, `说谎`, `撒谎`, `谎`, `␣mentira`, `␣lying`, `␣lie`, `␣liar`, `␣lied`, `␣Lies` … (+5) | q_tok6 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 65/158 (41%) | 43/43 (100%) | 73/73 (100%) |
| fake | lie | 14 | `fake`, `Fake`, `␣Fake`, `␣fake`, `_fake`, `.fake`, `伪造`, `pseudo` | q_tok6 | 152/152 (100%) | 81/81 (100%) | 136/138 (99%) | 158/158 (100%) | 43/43 (100%) | 73/73 (100%) |
| violate | unclear | 15 | `违反`, `违背`, `违反了`, `违规`, `␣violating`, `␣violations`, `␣violates`, `␣violate`, `␣violation`, `␣violated` … (+4) | q_tok3 | 151/152 (99%) | 80/81 (99%) | 136/138 (99%) | 145/158 (92%) | 42/43 (98%) | 72/73 (99%) |
| incorrect | lie | 20 | `␣Incorrect`, `␣incorrect`, `incorrect`, `Incorrect`, `␣inaccur`, `␣inaccurate`, `错误的`, `␣incorrectly`, `不符合`, `␣erroneous` … (+4) | q_tok7 | 150/152 (99%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 42/43 (98%) | 73/73 (100%) |
| privacy | unclear | 1 | `privacy`, `␣Privacy`, `Privacy`, `隐私`, `␣privacidad`, `␣privacy`, `ความเป็นส่วนตัว`, `/Private`, `private`, `.Private` | think_slot2 | 151/152 (99%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 42/43 (98%) | 72/73 (99%) |
| secret | lie | 8 | `秘密`, `␣secrecy`, `␣secretly`, `的秘密`, `␣secret`, `隐秘`, `␣secretive`, `secret`, `Secret`, `␣confidential` … (+10) | think_slot0 | 151/152 (99%) | 79/81 (98%) | 131/138 (95%) | 88/158 (56%) | 42/43 (98%) | 71/73 (97%) |
| silence | unclear | 2 | `␣Silence`, `␣Silent`, `沉默`, `silent`, `␣silence`, `寂静`, `␣Quiet`, `␣silencio`, `␣silenzio` | think_slot2 | 151/152 (99%) | 79/81 (98%) | 73/138 (53%) | 12/158 (8%) | 42/43 (98%) | 72/73 (99%) |
| truthful | truth | 11 | `␣truthful`, `如实`, `␣faithfully`, `实事求是` | q_tok7 | 151/152 (99%) | 77/81 (95%) | 105/138 (76%) | 48/158 (30%) | 43/43 (100%) | 69/73 (95%) |
| lawful | unclear | 5 | `合法`, `␣legality`, `/legal`, `␣Legal`, `legal`, `_legal`, `Legal`, `LEGAL` | think_slot0 | 151/152 (99%) | 76/81 (94%) | 135/138 (98%) | 96/158 (61%) | 43/43 (100%) | 68/73 (93%) |
| honest | truth | 12 | `␣honesty`, `␣truthful`, `诚实`, `如实`, `␣honest`, `␣Honest`, `坦诚`, `␣honestly`, `实事求是`, `诚信` … (+1) | preans_slot4 | 147/152 (97%) | 79/81 (98%) | 112/138 (81%) | 35/158 (22%) | 42/43 (98%) | 72/73 (99%) |
| mistake | unclear | 6 | `错误`, `␣mistake`, `␣mistakes`, `␣errors`, `␣error`, `␣erroneous`, `␣ERROR`, `␣Errors`, `Errors`, `-error` … (+9) | q_tok4 | 149/152 (98%) | 77/81 (95%) | 138/138 (100%) | 158/158 (100%) | 43/43 (100%) | 69/73 (95%) |
| fabricate | lie | 13 | `伪造`, `虚构`, `造假`, `␣fabricated`, `␣fabrication`, `弄虚作假`, `fiction` | q_tok6 | 146/152 (96%) | 79/81 (98%) | 77/138 (56%) | 89/158 (56%) | 40/43 (93%) | 71/73 (97%) |
| accurate | truth | 10 | `␣accuracy`, `␣accurate`, `accur`, `␣Accuracy`, `␣accurately`, `Accuracy`, `准确`, `准确地`, `accuracy`, `准确性` … (+1) | q_tok3 | 147/152 (97%) | 72/81 (89%) | 138/138 (100%) | 140/158 (89%) | 41/43 (95%) | 64/73 (88%) |
| unauthorized | unclear | 9 | `␣Unauthorized`, `␣unauthorized` | think_slot2 | 144/152 (95%) | 72/81 (89%) | 19/138 (14%) | 0/158 (0%) | 36/43 (84%) | 64/73 (88%) |
| mislead | lie | 13 | `␣misleading`, `误导`, `误导性`, `␣misled` | q_tok6 | 144/152 (95%) | 70/81 (86%) | 55/138 (40%) | 46/158 (29%) | 38/43 (88%) | 62/73 (85%) |
| leak | unclear | 4 | `泄露`, `␣WikiLeaks`, `␣leaked`, `␣Leakage` | think_slot2 | 134/152 (88%) | 69/81 (85%) | 50/138 (36%) | 3/158 (2%) | 37/43 (86%) | 62/73 (85%) |
| true | truth | 14 | `␣true`, `␣TRUE`, `真实`, `真实的`, `的真实`, `True`, `␣True`, `true`, `真实性`, `确实` … (+16) | think_slot3 | 128/152 (84%) | 74/81 (91%) | 126/138 (91%) | 96/158 (61%) | 21/43 (49%) | 66/73 (90%) |
| clarify | truth/unclear | 7 | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` | think_slot0 | 120/152 (79%) | 70/81 (86%) | 135/138 (98%) | 135/158 (85%) | 33/43 (77%) | 64/73 (88%) |
| insinuate | unclear | 1 | `暗示`, `隐含` | think_slot0 | 122/152 (80%) | 59/81 (73%) | 50/138 (36%) | 18/158 (11%) | 33/43 (77%) | 53/73 (73%) |
| fact | truth/unclear | 15 | `␣factual`, `␣facts`, `事实`, `␣Facts`, `facts`, `的事实`, `␣Fact`, `␣actually`, `␣reality`, `实际` … (+30) | q_tok7 | 113/152 (74%) | 66/81 (81%) | 116/138 (84%) | 148/158 (94%) | 29/43 (67%) | 60/73 (82%) |
| claim | unclear | 3 | `␣assertions`, `␣assertion`, `␣claiming`, `␣claim`, `claim`, `␣claims`, `Claim`, `␣Claim`, `␣Claims`, `Claims` … (+19) | preans_slot1 | 124/152 (82%) | 53/81 (65%) | 81/138 (59%) | 37/158 (23%) | 33/43 (77%) | 46/73 (63%) |
| comply | unclear | 7 | `遵守`, `␣compliance`, `合规`, `␣Compliance`, `严格遵守`, `␣compliant`, `␣comply`, `␣complying`, `␣adherence`, `␣adhere` … (+2) | q_tok3 | 111/152 (73%) | 65/81 (80%) | 93/138 (67%) | 148/158 (94%) | 17/43 (40%) | 58/73 (79%) |
| disclaimer | unclear | 13 | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `␣DISCLAIMER`, `免责声明`, `免责` | q_tok5 | 100/152 (66%) | 74/81 (91%) | 130/138 (94%) | 125/158 (79%) | 33/43 (77%) | 68/73 (93%) |
| disclose | truth | 7 | `␣disclosure`, `␣disclosures`, `␣Disclosure`, `公开`, `␣disclosing`, `␣disclose`, `信息公开`, `揭露`, `␣disclosed`, `披露` … (+1) | think_slot2 | 119/152 (78%) | 54/81 (67%) | 88/138 (64%) | 69/158 (44%) | 25/43 (58%) | 47/73 (64%) |
| deceive | lie | 11 | `欺骗`, `␣deception`, `␣deceptive`, `骗`, `␣deceive`, `骗子`, `骗局`, `␣deceit` | q_tok6 | 131/152 (86%) | 41/81 (51%) | 0/138 (0%) | 0/158 (0%) | 34/43 (79%) | 34/73 (47%) |
| unintentional | unclear | 2 | `␣inadvertently`, `␣unintention`, `␣accidentally`, `␣unintended`, `␣inadvert` | q_tok3 | 99/152 (65%) | 66/81 (81%) | 64/138 (46%) | 4/158 (3%) | 27/43 (63%) | 60/73 (82%) |
| compliant | unclear | 3 | `合规`, `依法依规`, `␣Compliance` | think_slot0 | 111/152 (73%) | 54/81 (67%) | 113/138 (82%) | 0/158 (0%) | 34/43 (79%) | 51/73 (70%) |
| error | unclear | 2 | `错误`, `␣erroneous`, `错误或` | q_tok6 | 97/152 (64%) | 67/81 (83%) | 138/138 (100%) | 158/158 (100%) | 37/43 (86%) | 60/73 (82%) |
| correct | truth | 14 | `正确`, `␣correct`, `␣Correct`, `␣correctly`, `correct`, `Correct`, `␣corrected`, `␣correctness`, `修正`, `纠正` … (+20) | q_tok3 | 101/152 (66%) | 61/81 (75%) | 137/138 (99%) | 145/158 (92%) | 22/43 (51%) | 56/73 (77%) |
| verify | unclear | 1 | `␣Verification`, `_verified`, `␣Verified`, `核实`, `_verification`, `验证`, `␣verification`, `verification`, `.verify` | think_slot2 | 100/152 (66%) | 59/81 (73%) | 124/138 (90%) | 152/158 (96%) | 23/43 (53%) | 54/73 (74%) |
| hide | lie | 10 | `隐瞒`, `␣Hidden`, `␣hidden`, `-hide`, `藏`, `隐`, `匿`, `masked`, `掩`, `隐藏` … (+4) | q_tok5 | 118/152 (78%) | 37/81 (46%) | 20/138 (14%) | 3/158 (2%) | 33/43 (77%) | 32/73 (44%) |
| contradict | unclear | 8 | `␣contradict`, `␣contradictory`, `␣contrad`, `␣contradiction`, `␣contradictions`, `矛盾`, `矛盾的`, `␣contradd` | q_tok3 | 96/152 (63%) | 54/81 (67%) | 137/138 (99%) | 9/158 (6%) | 33/43 (77%) | 47/73 (64%) |
| unethical | lie/unclear | 12 | `␣unethical`, `␣immoral` | q_tok5 | 97/152 (64%) | 52/81 (64%) | 0/138 (0%) | 0/158 (0%) | 20/43 (47%) | 47/73 (64%) |
| intentional | unclear | 10 | `␣intentionally`, `故意`, `␣intentional`, `␣deliberately`, `␣knowingly`, `␣deliberate`, `明知`, `故意的` | q_tok7 | 113/152 (74%) | 35/81 (43%) | 0/138 (0%) | 0/158 (0%) | 26/43 (60%) | 31/73 (42%) |
| wrong | lie | 21 | `错误`, `误`, `␣Wrong`, `␣ERROR`, `的错误`, `␣WRONG`, `wrong`, `错了`, `␣wrong`, `错` … (+11) | think_slot1 | 96/152 (63%) | 52/81 (64%) | 27/138 (20%) | 2/158 (1%) | 32/43 (74%) | 48/73 (66%) |
| cannot comply | unclear | 1 | `无法满足` | think_slot1 | 93/152 (61%) | 55/81 (68%) | 129/138 (93%) | 129/158 (82%) | 35/43 (81%) | 48/73 (66%) |
| forbidden | unclear | 2 | `␣Forbidden`, `严禁`, `禁止`, `␣prohibited`, `禁忌`, `禁用` | think_slot2 | 104/152 (68%) | 43/81 (53%) | 4/138 (3%) | 0/158 (0%) | 21/43 (49%) | 38/73 (52%) |
| confidential | lie/unclear | 9 | `␣confidentiality`, `保密`, `␣confidential`, `机密`, `␣Confidential`, `␣конфиден` | think_slot2 | 97/152 (64%) | 47/81 (58%) | 107/138 (78%) | 13/158 (8%) | 22/43 (51%) | 44/73 (60%) |
| conceal | lie | 8 | `隐瞒`, `隐藏`, `␣conceal`, `␣hiding`, `␣concealed`, `hide`, `␣hidden`, `hidden`, `-hidden`, `␣Hidden` … (+8) | preans_slot1 | 106/152 (70%) | 38/81 (47%) | 3/138 (2%) | 0/158 (0%) | 31/43 (72%) | 31/73 (42%) |
| fiction | unclear | 5 | `␣fictional`, `␣fict`, `fiction`, `␣fiction`, `␣Fiction`, `虚构`, `-fiction` | preans_slot1 | 97/152 (64%) | 42/81 (52%) | 54/138 (39%) | 53/158 (34%) | 22/43 (51%) | 35/73 (48%) |
| refuse | unclear | 16 | `拒绝`, `␣refusal`, `␣refus`, `␣refuse`, `␣refusing`, `␣refused`, `拒`, `␣refuses`, `拒絕`, `拒绝了` … (+5) | q_tok5 | 64/152 (42%) | 62/81 (77%) | 93/138 (67%) | 3/158 (2%) | 22/43 (51%) | 60/73 (82%) |
| critique | unclear | 3 | `␣critique`, `批判`, `批评`, `␣critic`, `␣criticize`, `␣critiques` | postans_slot2 | 80/152 (53%) | 41/81 (51%) | 0/138 (0%) | 0/158 (0%) | 15/43 (35%) | 35/73 (48%) |
| explicit | unclear | 2 | `␣explicit`, `␣explicitly`, `␣Explicit`, `explicit`, `Explicit`, `明确的`, `明确` | q_tok5 | 78/152 (51%) | 39/81 (48%) | 77/138 (56%) | 7/158 (4%) | 28/43 (65%) | 36/73 (49%) |
| rule-abiding | unclear | 1 | `恪守`, `恪`, `依规`, `合规` | think_slot1 | 80/152 (53%) | 35/81 (43%) | 39/138 (28%) | 19/158 (12%) | 25/43 (58%) | 32/73 (44%) |
| illegal | unclear | 9 | `非法`, `违法`, `illegal`, `Illegal`, `␣illegal`, `␣Illegal`, `␣ilegal`, `␣illegally`, `违法行为`, `违法违规` | think_slot0 | 76/152 (50%) | 36/81 (44%) | 45/138 (33%) | 19/158 (12%) | 28/43 (65%) | 35/73 (48%) |
| misinformation | lie | 7 | `␣misinformation` | postans_slot4 | 73/152 (48%) | 35/81 (43%) | 68/138 (49%) | 37/158 (23%) | 21/43 (49%) | 30/73 (41%) |
| imply | unclear | 3 | `␣implication`, `␣implying`, `␣implicitly`, `暗示`, `␣implied`, `␣implicit`, `隐含`, `␣imply`, `␣implies`, `implicit` … (+3) | q_tok3 | 65/152 (43%) | 39/81 (48%) | 56/138 (41%) | 1/158 (1%) | 26/43 (60%) | 35/73 (48%) |
| misrepresent | lie | 7 | `␣misrepresented` | q_tok6 | 77/152 (51%) | 24/81 (30%) | 2/138 (1%) | 0/158 (0%) | 14/43 (33%) | 20/73 (27%) |
| fictional | unclear | 3 | `␣Fiction`, `␣fictional`, `fiction`, `虚构`, `␣fiction` | q_tok13 | 75/152 (49%) | 23/81 (28%) | 2/138 (1%) | 17/158 (11%) | 8/43 (19%) | 20/73 (27%) |
| apologize | truth/unclear | 6 | `␣apology`, `道歉`, `␣apologies`, `␣apolog`, `␣apologize` | q_tok5 | 54/152 (36%) | 43/81 (53%) | 109/138 (79%) | 60/158 (38%) | 16/43 (37%) | 40/73 (55%) |
| ethics | unclear | 11 | `␣ethical`, `ethical`, `伦理`, `␣ethics`, `␣Ethics`, `道德`, `␣ethic`, `的道德`, `␣morality`, `职业道德` … (+4) | postans_slot4 | 64/152 (42%) | 31/81 (38%) | 0/138 (0%) | 0/158 (0%) | 14/43 (33%) | 29/73 (40%) |
| dishonest | lie | 10 | `␣dishonest` | q_tok5 | 81/152 (53%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 19/43 (44%) | 10/73 (14%) |
| ethical | unclear | 2 | `␣ethical`, `ethical`, `␣moral`, `␣Moral`, `␣morally` | postans_slot4 | 63/152 (41%) | 30/81 (37%) | 0/138 (0%) | 0/158 (0%) | 14/43 (33%) | 28/73 (38%) |
| whistleblow | truth/unclear | 6 | `␣whistleblower`, `␣whistlebl`, `举报` | postans_slot4 | 69/152 (45%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 18/73 (25%) |
| hallucinate | unclear | 2 | `␣halluc` | q_tok5 | 54/152 (36%) | 31/81 (38%) | 121/138 (88%) | 96/158 (61%) | 15/43 (35%) | 28/73 (38%) |
| self_check | unclear | 2 | `自查`, `自检`, `审查` | q_tok8 | 38/152 (25%) | 47/81 (58%) | 121/138 (88%) | 131/158 (83%) | 18/43 (42%) | 44/73 (60%) |
| moral | unclear | 3 | `道德`, `␣moral`, `␣morally`, `␣Moral`, `␣morality`, `␣morals`, `的道德`, `职业道德`, `␣ethics`, `␣Ethics` … (+2) | postans_slot4 | 54/152 (36%) | 28/81 (35%) | 0/138 (0%) | 0/158 (0%) | 12/43 (28%) | 26/73 (36%) |
| fraud | lie | 9 | `␣fraudulent`, `欺诈`, `␣fraud`, `骗局`, `␣Fraud`, `弄虚作假`, `诈骗`, `骗子` | q_tok5 | 76/152 (50%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 18/43 (42%) | 5/73 (7%) |
| cannot | unclear | 4 | `␣Cannot`, `无法`, `我无法`, `我不能`, `cannot`, `Cannot`, `无法满足`, `␣cannot`, `Unable`, `␣Unable` … (+7) | preans_slot3 | 66/152 (43%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 22/43 (51%) | 12/73 (16%) |
| illusion | unclear | 1 | `幻想`, `虚幻`, `错觉`, `妄想` | think_slot1 | 43/152 (28%) | 26/81 (32%) | 1/138 (1%) | 0/158 (0%) | 23/43 (53%) | 25/73 (34%) |
| spoiler | unclear | 2 | `Spoiler` | think_slot2 | 51/152 (34%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 8/73 (11%) |
| prohibit | unclear | 2 | `禁止`, `严禁`, `␣prohibited`, `␣prohibit`, `␣prohibiting` | postans_slot4 | 36/152 (24%) | 25/81 (31%) | 5/138 (4%) | 0/158 (0%) | 9/43 (21%) | 23/73 (32%) |
| truth | truth | 3 | `真实性`, `的真实性`, `内容的真实性`, `其真实性` | preans_slot2 | 46/152 (30%) | 11/81 (14%) | 71/138 (51%) | 8/158 (5%) | 12/43 (28%) | 9/73 (12%) |
| interrogate | unclear | 3 | `␣interrog`, `质问`, `␣interrogation` | postans_slot4 | 36/152 (24%) | 19/81 (23%) | 2/138 (1%) | 0/158 (0%) | 19/43 (44%) | 18/73 (25%) |
| prohibited | unclear | 5 | `禁止`, `␣prohibited`, `␣forbidden`, `严禁`, `␣forbid`, `Forbidden`, `␣prohibition`, `␣prohibit`, `␣prohibits` | q_tok13 | 35/152 (23%) | 20/81 (25%) | 3/138 (2%) | 0/158 (0%) | 5/43 (12%) | 16/73 (22%) |
| liar | lie | 1 | `␣liar` | q_tok5 | 48/152 (32%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 17/43 (40%) | 2/73 (3%) |
| reject | unclear | 9 | `␣rejection`, `␣rejecting`, `␣Reject`, `rejected`, `reject`, `Reject`, `否决`, `␣rejected`, `␣reject`, `拒绝` … (+3) | think_slot1 | 33/152 (22%) | 18/81 (22%) | 11/138 (8%) | 0/158 (0%) | 11/43 (26%) | 15/73 (21%) |
| pretend | lie | 6 | `伪装`, `␣pretending`, `␣pretend`, `假装`, `␣disguised` | preans_slot2 | 40/152 (26%) | 9/81 (11%) | 2/138 (1%) | 1/158 (1%) | 12/43 (28%) | 8/73 (11%) |
| blame | unclear | 2 | `␣blaming`, `␣blame`, `␣blamed`, `␣blames`, `指责` | preans_slot1 | 40/152 (26%) | 6/81 (7%) | 12/138 (9%) | 0/158 (0%) | 3/43 (7%) | 5/73 (7%) |
| undisclosed | lie | 3 | `␣undisclosed` | preans_slot2 | 35/152 (23%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 11/43 (26%) | 6/73 (8%) |
| opaque | lie | 1 | `opaque` | think_slot2 | 25/152 (16%) | 15/81 (19%) | 64/138 (46%) | 6/158 (4%) | 5/43 (12%) | 12/73 (16%) |
| refute | unclear | 4 | `␣refute`, `反驳` | think_slot2 | 23/152 (15%) | 15/81 (19%) | 3/138 (2%) | 0/158 (0%) | 12/43 (28%) | 15/73 (21%) |
| deliberate | unclear | 3 | `␣intentionally`, `␣deliberately`, `故意`, `␣intentional`, `␣deliberate`, `故意的`, `␣purposely` | preans_slot2 | 26/152 (17%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 11/73 (15%) |
| accuse | unclear | 7 | `␣accusations`, `␣accusation`, `␣allegations`, `␣accusing`, `指控`, `指责`, `␣allegation`, `␣alleging` | q_tok6 | 17/152 (11%) | 17/81 (21%) | 6/138 (4%) | 4/158 (3%) | 6/43 (14%) | 17/73 (23%) |
| challenge_doubt | unclear | 2 | `质疑`, `质问` | postans_slot4 | 18/152 (12%) | 15/81 (19%) | 9/138 (7%) | 20/158 (13%) | 4/43 (9%) | 14/73 (19%) |
| blatant | unclear | 1 | `␣blatant`, `␣outright`, `␣blatantly` | q_tok5 | 32/152 (21%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 12/43 (28%) | 0/73 (0%) |
| hidden | lie | 2 | `␣Hidden`, `hidden`, `␣hidden`, `Hidden`, `-hidden`, `隐藏的` | preans_slot2 | 27/152 (18%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 11/43 (26%) | 3/73 (4%) |
| hypocrisy | lie/unclear | 7 | `␣hypocrisy`, `虚伪` | preans_slot2 | 18/152 (12%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 11/73 (15%) |
| knowingly | unclear | 6 | `␣knowingly`, `明知`, `␣knowing`, `␣Knowing`, `Knowing` | preans_slot2 | 24/152 (16%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 4/73 (5%) |
| harmful | unclear | 2 | `␣harmful` | q_tok4 | 14/152 (9%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 14/73 (19%) |
| persona | unclear | 1 | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas` | q_tok13 | 18/152 (12%) | 10/81 (12%) | 0/138 (0%) | 1/158 (1%) | 4/43 (9%) | 10/73 (14%) |
| cheat | lie | 4 | `作弊`, `␣cheating` | q_tok13 | 23/152 (15%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| integrity | truth | 3 | `␣Integrity`, `␣integrity`, `诚信`, `正直` | think_slot2 | 15/152 (10%) | 10/81 (12%) | 19/138 (14%) | 3/158 (2%) | 7/43 (16%) | 9/73 (12%) |
| allege | unclear | 2 | `␣allegation`, `␣allegations`, `␣purported`, `␣alleging`, `␣alleged`, `␣allegedly` | preans_slot1 | 21/152 (14%) | 4/81 (5%) | 3/138 (2%) | 2/158 (1%) | 5/43 (12%) | 4/73 (5%) |
| trap | unclear | 2 | `陷阱`, `␣Trap`, `␣trap`, `␣traps`, `trap`, `Trap`, `␣trapped`, `␣trapping`, `_trap`, `␣atrap` | postans_slot4 | 12/152 (8%) | 12/81 (15%) | 2/138 (1%) | 0/158 (0%) | 10/43 (23%) | 11/73 (15%) |
| stealth | unclear | 1 | `悄然` | think_slot0 | 15/152 (10%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 12/43 (28%) | 9/73 (12%) |
| negate | unclear | 7 | `否定`, `␣negate` | preans_slot1 | 17/152 (11%) | 6/81 (7%) | 4/138 (3%) | 0/158 (0%) | 8/43 (19%) | 6/73 (8%) |
| confess | truth | 3 | `␣confess`, `坦白`, `␣confession`, `␣confessed` | q_tok5 | 6/152 (4%) | 17/81 (21%) | 8/138 (6%) | 0/158 (0%) | 3/43 (7%) | 15/73 (21%) |
| coerce | unclear | 3 | `逼`, `逼迫`, `倒逼`, `迫`, `被迫`, `强制`, `forced`, `␣forced`, `迫使`, `强迫` … (+6) | postans_slot4 | 15/152 (10%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 6/73 (8%) |
| delusion | unclear | 1 | `妄想`, `妄` | think_slot1 | 14/152 (9%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 10/43 (23%) | 5/73 (7%) |
| cover up | lie | 3 | `掩盖`, `掩饰` | preans_slot1 | 18/152 (12%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 1/73 (1%) |
| misunderstand | unclear | 3 | `␣misunderstanding`, `误解`, `␣misunderstood`, `␣misunderstand` | q_tok3 | 6/152 (4%) | 12/81 (15%) | 8/138 (6%) | 1/158 (1%) | 6/43 (14%) | 12/73 (16%) |
| rebut | unclear | 2 | `␣rebut`, `反驳`, `␣refute` | q_tok5 | 10/152 (7%) | 8/81 (10%) | 3/138 (2%) | 0/158 (0%) | 4/43 (9%) | 7/73 (10%) |
| role-play | unclear | 1 | `角色扮演`, `扮演` | q_tok13 | 12/152 (8%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 6/73 (8%) |
| encryption | unclear | 1 | `␣Encryption`, `encryption` | think_slot2 | 13/152 (9%) | 5/81 (6%) | 3/138 (2%) | 0/158 (0%) | 1/43 (2%) | 5/73 (7%) |
| contradiction | unclear | 2 | `␣contradiction`, `␣contradict`, `␣contradictory`, `␣contradictions`, `矛盾`, `矛盾的` | postans_slot1 | 11/152 (7%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 5/73 (7%) |
| trick | lie/unclear | 3 | `␣trick`, `␣Trick`, `␣tricky`, `␣tricks`, `␣Tricks` | postans_slot4 | 7/152 (5%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 7/43 (16%) | 9/73 (12%) |
| genuine | truth | 1 | `␣Genuine`, `其真实性` | think_slot2 | 12/152 (8%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 4/73 (5%) |
| implicit | unclear | 1 | `␣Implicit`, `隐含` | think_slot2 | 10/152 (7%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 5/73 (7%) |
| loophole | unclear | 2 | `␣loophole` | postans_slot4 | 7/152 (5%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 6/43 (14%) | 7/73 (10%) |
| audit | unclear | 1 | `Audit`, `␣audit`, `␣auditing`, `审计`, `audit`, `␣audits`, `␣Audit`, `␣auditor` | q_tok13 | 7/152 (5%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 4/43 (9%) | 8/73 (11%) |
| suppress | lie | 2 | `suppress`, `.Suppress` | think_slot0 | 3/152 (2%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 12/73 (16%) |
| typo | unclear | 1 | `␣typo` | q_tok5 | 10/152 (7%) | 4/81 (5%) | 13/138 (9%) | 147/158 (93%) | 4/43 (9%) | 3/73 (4%) |
| blackmail | unclear | 2 | `␣blackmail` | postans_slot4 | 8/152 (5%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 4/73 (5%) |
| censorship | unclear | 1 | `␣censorship` | postans_slot4 | 3/152 (2%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 9/73 (12%) |
| evade | lie | 5 | `回避`, `␣evade`, `␣evasion`, `避开`, `␣dodge`, `规避` | q_tok3 | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 2/73 (3%) |
| strategic game | unclear | 1 | `博弈` | postans_slot4 | 6/152 (4%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 5/73 (7%) |
| reflect | unclear | 2 | `反思`, `␣reflection`, `reflect`, `Reflect`, `reflection`, `␣Reflection`, `Reflection`, `␣reflective`, `␣reflect`, `.reflect` … (+2) | q_tok13 | 8/152 (5%) | 4/81 (5%) | 24/138 (17%) | 1/158 (1%) | 4/43 (9%) | 4/73 (5%) |
| legal | unclear | 3 | `␣Legal`, `合法`, `Legal`, `␣legality`, `legal`, `␣legal`, `␣legally`, `/legal` | postans_slot4 | 8/152 (5%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 3/73 (4%) |
| conscience | unclear | 1 | `␣conscience` | think_slot2 | 6/152 (4%) | 5/81 (6%) | 0/138 (0%) | 1/158 (1%) | 1/43 (2%) | 4/73 (5%) |
| transparent | truth | 3 | `␣transparency`, `␣Transparency`, `透明` | q_tok5 | 2/152 (1%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 6/73 (8%) |
| roleplay | unclear | 1 | `角色扮演` | q_tok5 | 0/152 (0%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 9/73 (12%) |
| hoax | lie | 4 | `␣hoax`, `骗局` | postans_slot4 | 3/152 (2%) | 5/81 (6%) | 2/138 (1%) | 1/158 (1%) | 3/43 (7%) | 5/73 (7%) |
| reveal | truth | 4 | `揭露`, `␣revealed`, `␣reveal`, `␣revealing`, `透露` | preans_slot2 | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| plagiarism | unclear | 2 | `␣plagiarism` | q_tok4 | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 31/158 (20%) | 0/43 (0%) | 2/73 (3%) |
| report | unclear | 1 | `举报` | postans_slot4 | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| paradox | unclear | 1 | `␣paradox` | postans_slot4 | 5/152 (3%) | 2/81 (2%) | 2/138 (1%) | 3/158 (2%) | 5/43 (12%) | 1/73 (1%) |
| candid | truth | 1 | `坦诚` | preans_slot1 | 0/152 (0%) | 7/81 (9%) | 2/138 (1%) | 3/158 (2%) | 0/43 (0%) | 7/73 (10%) |
| conspiracy | unclear | 1 | `␣conspiracy` | q_tok5 | 5/152 (3%) | 2/81 (2%) | 3/138 (2%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| disguise | lie | 1 | `伪装` | q_tok13 | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| ostensibly | lie | 1 | `␣ostensibly` | think_slot2 | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 2/73 (3%) |
| justification | unclear | 2 | `␣justification` | q_tok6 | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| vague | unclear | 1 | `模糊` | think_slot0 | 2/152 (1%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 1/43 (2%) | 4/73 (5%) |
| misunderstanding | unclear | 1 | `误解` | think_slot0 | 3/152 (2%) | 3/81 (4%) | 5/138 (4%) | 59/158 (37%) | 1/43 (2%) | 2/73 (3%) |
| mask | lie | 1 | `masked` | postans_slot0 | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| promote | unclear | 1 | `␣promotional`, `␣promoting`, `␣marketing`, `宣传` | postans_slot2 | 2/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 3/73 (4%) |
| dilemma | unclear | 1 | `␣dilemma` | postans_slot4 | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 0/73 (0%) |
| apology | unclear | 3 | `抱歉`, `␣Sorry`, `Sorry`, `道歉` | think_slot2 | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 1/43 (2%) | 2/73 (3%) |
| expose | truth | 1 | `揭露` | postans_slot4 | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| manipulate | lie | 3 | `␣manipulation`, `␣manipulated`, `␣manipulate`, `␣manipulating`, `␣manipul`, `操纵` | preans_slot2 | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| wrongdoing | unclear | 1 | `␣wrongdoing` | preans_slot2 | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| exaggerate | lie | 3 | `␣exagger`, `夸大`, `␣exaggerated` | q_tok6 | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| threat | unclear | 2 | `␣threat`, `␣threats`, `威胁`, `␣threatening`, `␣threaten`, `␣Threat` | postans_slot4 | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| pretext | lie | 2 | `␣pretext` | q_tok6 | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| sorry | unclear | 2 | `␣Sorry`, `Sorry` | q_tok11 | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| persuade | unclear | 1 | `␣persu`, `␣persuasive`, `␣persuasion`, `␣persuade`, `劝`, `劝说`, `␣convince`, `␣convincing` | postans_slot2 | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| frame | unclear | 1 | `陷害` | postans_slot4 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| challenge | unclear | 1 | `质疑`, `质问` | preans_slot0 | 0/152 (0%) | 2/81 (2%) | 2/138 (1%) | 2/158 (1%) | 0/43 (0%) | 2/73 (3%) |
| omit | unclear | 2 | `␣omit`, `遗漏`, `␣omission` | q_tok5 | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| inappropriate | unclear | 2 | `␣inappropriate` | q_tok5 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| excuse | unclear | 2 | `␣excuse`, `␣excuses` | q_tok5 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| evasion | lie | 1 | `␣evasion` | postans_slot4 | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| fault | unclear | 1 | `Fault` | postans_slot3 | 1/152 (1%) | 0/81 (0%) | 2/138 (1%) | 7/158 (4%) | 1/43 (2%) | 0/73 (0%) |
| propaganda | unclear | 1 | `␣propaganda` | postans_slot4 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| inaccurate | lie | 1 | `不准确` | preans_slot1 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 9/158 (6%) | 0/43 (0%) | 0/73 (0%) |
| disobey | unclear | 2 | `␣disob`, `␣disobed` | q_tok3 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| secretly | lie | 1 | `暗中` | think_slot1 | 1/152 (1%) | 0/81 (0%) | 6/138 (4%) | 11/158 (7%) | 0/43 (0%) | 0/73 (0%) |

**wording Q7_ab, positions from the question on** (193 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|---|---|
| honest | truth | 23 | `␣honesty`, `␣honest`, `␣honestly`, `␣Honest`, `诚信`, `坦诚`, `␣jujur`, `␣sincerely`, `␣честно` | q_tok28 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| dishonest | lie | 20 | `␣dishonest`, `虚伪` | q_tok21 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| fake | lie | 23 | `fake`, `Fake`, `␣Fake`, `␣fake`, `伪造`, `假的`, `假`, `_fake`, `造假`, `虚假` … (+5) | q_tok2 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| deceive | lie | 21 | `欺骗`, `␣deception`, `␣deceive`, `␣deceptive`, `骗`, `␣deceit`, `␣deceived`, `欺`, `␣fooled`, `骗取` … (+1) | q_tok2 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| legal | unclear | 10 | `␣Legal`, `␣legality`, `legal`, `合法`, `␣legal`, `/legal`, `Legal`, `␣legally`, `␣legale`, `␣lawful` … (+7) | think_slot0 | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| mislead | lie | 17 | `误导`, `␣misleading`, `␣misled`, `误导性` | q_tok6 | 152/152 (100%) | 81/81 (100%) | 136/138 (99%) | 111/158 (70%) | 79/79 (100%) | 77/77 (100%) |
| integrity | truth | 15 | `诚信`, `␣integrity`, `␣Integrity`, `正直` | q_tok28 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| false | lie | 28 | `␣fals`, `␣falsehood`, `␣false`, `False`, `␣falsely`, `false`, `␣False`, `虚假`, `␣FALSE`, `/false` … (+11) | q_tok2 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| sincere | truth | 6 | `␣sincerely`, `␣sincerity`, `真诚`, `␣sincere` | q_tok28 | 152/152 (100%) | 81/81 (100%) | 133/138 (96%) | 157/158 (99%) | 79/79 (100%) | 77/77 (100%) |
| factual | truth | 5 | `实事求是`, `␣factual`, `事实`, `␣facts`, `␣Facts`, `的事实`, `facts`, `Fact`, `␣Fact`, `␣fact` … (+5) | q_tok28 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| mock | unclear | 1 | `_mock`, `/mock`, `␣MOCK`, `mock`, `(Mock` | think_slot1 | 152/152 (100%) | 81/81 (100%) | 134/138 (97%) | 7/158 (4%) | 79/79 (100%) | 77/77 (100%) |
| secret | lie | 16 | `秘密`, `␣secrecy`, `␣secretly`, `的秘密`, `␣Secret`, `␣secret`, `Secret`, `secret`, `␣secretive`, `␣SECRET` … (+15) | think_slot0 | 150/152 (99%) | 80/81 (99%) | 98/138 (71%) | 140/158 (89%) | 77/79 (97%) | 76/77 (99%) |
| wrong | lie | 26 | `错误`, `␣WRONG`, `␣wrong`, `␣ERROR`, `␣Wrong`, `误`, `wrong`, `错`, `的错误`, `错了` … (+11) | think_slot1 | 150/152 (99%) | 80/81 (99%) | 126/138 (91%) | 132/158 (84%) | 78/79 (99%) | 76/77 (99%) |
| implicit | unclear | 3 | `隐含`, `␣Implicit`, `implicit` | think_slot0 | 152/152 (100%) | 78/81 (96%) | 116/138 (84%) | 87/158 (55%) | 79/79 (100%) | 74/77 (96%) |
| silence | unclear | 4 | `␣Silent`, `␣Silence`, `␣silence`, `沉默`, `silent` | think_slot2 | 147/152 (97%) | 78/81 (96%) | 60/138 (43%) | 24/158 (15%) | 76/79 (96%) | 74/77 (96%) |
| compliance | unclear | 3 | `合规`, `␣compliance`, `␣Compliance`, `遵守`, `严格遵守` | think_slot2 | 146/152 (96%) | 76/81 (94%) | 119/138 (86%) | 143/158 (91%) | 74/79 (94%) | 72/77 (94%) |
| privacy | unclear | 3 | `隐私`, `␣privacy`, `privacy`, `␣Privacy`, `Privacy`, `␣privacidad`, `private` | think_slot2 | 145/152 (95%) | 77/81 (95%) | 51/138 (37%) | 48/158 (30%) | 77/79 (97%) | 73/77 (95%) |
| conceal | lie | 19 | `隐瞒`, `␣conceal`, `␣concealed`, `掩盖`, `隐`, `隐藏`, `␣undisclosed`, `hide`, `隐蔽`, `隐匿` … (+13) | q_tok19 | 143/152 (94%) | 73/81 (90%) | 75/138 (54%) | 18/158 (11%) | 73/79 (92%) | 69/77 (90%) |
| fabricate | lie | 17 | `伪造`, `虚构`, `造假`, `␣fabricated`, `弄虚作假`, `␣fabrication`, `␣fictional`, `␣invented` | q_tok21 | 139/152 (91%) | 71/81 (88%) | 110/138 (80%) | 109/158 (69%) | 69/79 (87%) | 67/77 (87%) |
| accurate | truth | 14 | `␣accuracy`, `␣accurate`, `␣Accuracy`, `␣accurately`, `accuracy`, `Accuracy`, `accur`, `准确`, `准确的`, `准确性` … (+2) | q_tok28 | 141/152 (93%) | 65/81 (80%) | 138/138 (100%) | 157/158 (99%) | 74/79 (94%) | 62/77 (81%) |
| misinformation | lie | 17 | `␣misinformation`, `虚假信息` | q_tok6 | 146/152 (96%) | 56/81 (69%) | 104/138 (75%) | 104/158 (66%) | 76/79 (96%) | 52/77 (68%) |
| candid | truth | 9 | `坦诚`, `␣candid`, `␣straightforward` | q_tok28 | 125/152 (82%) | 76/81 (94%) | 51/138 (37%) | 41/158 (26%) | 60/79 (76%) | 72/77 (94%) |
| intentional | unclear | 19 | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `␣deliberate`, `刻意`, `␣purposely`, `故意的`, `␣consciously`, `特意` … (+3) | q_tok20 | 139/152 (91%) | 59/81 (73%) | 93/138 (67%) | 132/158 (84%) | 69/79 (87%) | 55/77 (71%) |
| forbidden | unclear | 1 | `␣Forbidden`, `␣prohibited`, `禁忌`, `严禁`, `禁止`, `Forbidden` | think_slot2 | 127/152 (84%) | 67/81 (83%) | 22/138 (16%) | 1/158 (1%) | 62/79 (78%) | 64/77 (83%) |
| misrepresent | lie | 12 | `␣misrepresented` | q_tok20 | 131/152 (86%) | 62/81 (77%) | 102/138 (74%) | 49/158 (31%) | 68/79 (86%) | 58/77 (75%) |
| incorrect | lie | 24 | `␣incorrect`, `incorrect`, `␣Incorrect`, `错误的`, `Incorrect`, `␣incorrectly`, `␣inaccurate`, `不符合`, `␣inaccur`, `␣erroneous` … (+4) | q_tok6 | 129/152 (85%) | 63/81 (78%) | 136/138 (99%) | 145/158 (92%) | 62/79 (78%) | 60/77 (78%) |
| correct | truth | 23 | `正确`, `␣correct`, `␣Correct`, `␣correctly`, `Correct`, `纠正`, `␣correctness`, `正确答案`, `correct`, `正确的` … (+20) | q_tok28 | 121/152 (80%) | 68/81 (84%) | 138/138 (100%) | 154/158 (97%) | 68/79 (86%) | 66/77 (86%) |
| illusion | unclear | 1 | `幻想`, `虚幻`, `妄想`, `错觉` | think_slot1 | 137/152 (90%) | 50/81 (62%) | 0/138 (0%) | 1/158 (1%) | 73/79 (92%) | 46/77 (60%) |
| hide | lie | 15 | `隐藏`, `␣Hidden`, `hidden`, `␣hidden`, `␣hiding`, `隐藏的`, `隐瞒`, `Hidden`, `隐蔽`, `-hide` … (+21) | preans_slot1 | 128/152 (84%) | 51/81 (63%) | 87/138 (63%) | 3/158 (2%) | 64/79 (81%) | 47/77 (61%) |
| disclose | truth | 12 | `␣disclosure`, `␣Disclosure`, `␣disclosing`, `␣disclosures`, `公开`, `␣disclosed`, `␣disclose`, `披露`, `信息披露`, `信息公开` … (+4) | think_slot2 | 118/152 (78%) | 57/81 (70%) | 11/138 (8%) | 4/158 (3%) | 58/79 (73%) | 55/77 (71%) |
| cannot comply | unclear | 1 | `无法满足` | think_slot1 | 124/152 (82%) | 50/81 (62%) | 116/138 (84%) | 93/158 (59%) | 63/79 (80%) | 46/77 (60%) |
| confess | truth | 9 | `坦白`, `␣confess`, `␣confession`, `␣confessed`, `认错`, `认罪` | q_tok22 | 112/152 (74%) | 59/81 (73%) | 90/138 (65%) | 146/158 (92%) | 72/79 (91%) | 58/77 (75%) |
| fictional | unclear | 10 | `虚构`, `␣fictional`, `fiction`, `␣Fiction`, `␣fiction`, `␣fict`, `␣fictional`, `-fiction`, `␣Fiction` | preans_slot1 | 118/152 (78%) | 53/81 (65%) | 114/138 (83%) | 143/158 (91%) | 56/79 (71%) | 50/77 (65%) |
| pretend | lie | 14 | `␣pretending`, `假装`, `␣pretend`, `␣pretended`, `伪装`, `␣disguised`, `冒充`, `␣disguise` | q_tok20 | 110/152 (72%) | 60/81 (74%) | 38/138 (28%) | 4/158 (3%) | 52/79 (66%) | 56/77 (73%) |
| unethical | lie/unclear | 18 | `␣unethical`, `␣immoral` | postans_slot4 | 117/152 (77%) | 45/81 (56%) | 3/138 (2%) | 0/158 (0%) | 51/79 (65%) | 43/77 (56%) |
| true | truth | 14 | `␣true`, `True`, `确实`, `真正的`, `真的`, `␣True`, `是真的`, `真實`, `的真实性`, `␣TRUE` … (+9) | q_tok17 | 116/152 (76%) | 46/81 (57%) | 65/138 (47%) | 158/158 (100%) | 49/79 (62%) | 42/77 (55%) |
| clarify | unclear | 8 | `澄清`, `␣clarified`, `␣clarification`, `␣clarify` | think_slot0 | 96/152 (63%) | 64/81 (79%) | 138/138 (100%) | 121/158 (77%) | 42/79 (53%) | 60/77 (78%) |
| violate | unclear | 19 | `违反`, `违背`, `违规`, `␣violates`, `␣violate`, `违反了`, `␣violating`, `␣violated`, `␣violation`, `␣violations` … (+2) | q_tok20 | 105/152 (69%) | 54/81 (67%) | 106/138 (77%) | 5/158 (3%) | 51/79 (65%) | 53/77 (69%) |
| cannot | unclear | 4 | `无法`, `cannot`, `␣Cannot`, `Cannot`, `␣cannot`, `根本无法`, `不能`, `是不能`, `我无法`, `我不能` … (+16) | preans_slot3 | 119/152 (78%) | 38/81 (47%) | 0/138 (0%) | 1/158 (1%) | 62/79 (78%) | 37/77 (48%) |
| ethics | unclear | 9 | `␣Ethics`, `␣ethics`, `伦理`, `道德`, `␣ethical`, `␣moral`, `␣Moral`, `ethical`, `职业道德`, `␣ethic` … (+4) | postans_slot4 | 112/152 (74%) | 43/81 (53%) | 2/138 (1%) | 0/158 (0%) | 51/79 (65%) | 41/77 (53%) |
| contradict | unclear | 12 | `␣contradict`, `␣contradictory`, `␣contradiction`, `矛盾`, `␣contradictions`, `␣conflicting`, `␣contrad`, `矛盾的`, `␣contrad` | q_tok19 | 95/152 (62%) | 60/81 (74%) | 128/138 (93%) | 12/158 (8%) | 52/79 (66%) | 57/77 (74%) |
| illegal | lie/unclear | 14 | `违法`, `␣illegal`, `␣illegally`, `illegal`, `Illegal`, `非法`, `␣Illegal`, `␣unlawful`, `␣ilegal`, `违法行为` … (+2) | think_slot0 | 102/152 (67%) | 51/81 (63%) | 63/138 (46%) | 54/158 (34%) | 60/79 (76%) | 50/77 (65%) |
| knowingly | unclear | 17 | `␣knowingly`, `明知`, `␣knowing`, `␣Knowing`, `Knowing`, `␣consciously` | q_tok19 | 127/152 (84%) | 23/81 (28%) | 1/138 (1%) | 43/158 (27%) | 65/79 (82%) | 20/77 (26%) |
| fake / forge | lie | 1 | `fake`, `␣fake`, `Fake`, `伪造`, `虚假`, `␣Fake`, `假的`, `弄虚作假`, `造假`, `_fake` … (+1) | preans_slot2 | 100/152 (66%) | 50/81 (62%) | 36/138 (26%) | 14/158 (9%) | 49/79 (62%) | 49/77 (64%) |
| leak | unclear | 5 | `泄露`, `␣WikiLeaks`, `␣leaked`, `␣leak`, `␣Leakage` | think_slot2 | 99/152 (65%) | 49/81 (60%) | 19/138 (14%) | 1/158 (1%) | 62/79 (78%) | 48/77 (62%) |
| accuse | unclear | 11 | `␣accusations`, `␣accusation`, `␣accusing`, `指控`, `␣accuses`, `␣allegations`, `␣accused`, `␣accuse`, `␣alleged`, `␣accus` … (+3) | q_tok7 | 89/152 (59%) | 56/81 (69%) | 103/138 (75%) | 10/158 (6%) | 54/79 (68%) | 55/77 (71%) |
| fact | truth | 19 | `␣factual`, `Actually`, `␣Actually`, `actually`, `actual`, `实际`, `␣facts`, `事实`, `实事求是`, `␣actually` … (+30) | q_tok19 | 123/152 (81%) | 20/81 (25%) | 51/138 (37%) | 68/158 (43%) | 59/79 (75%) | 17/77 (22%) |
| conscience | unclear | 1 | `␣conscience` | think_slot2 | 109/152 (72%) | 31/81 (38%) | 0/138 (0%) | 0/158 (0%) | 52/79 (66%) | 30/77 (39%) |
| inconvenient | unclear | 1 | `不方便` | think_slot1 | 85/152 (56%) | 48/81 (59%) | 59/138 (43%) | 36/158 (23%) | 36/79 (46%) | 44/77 (57%) |
| morality | unclear | 3 | `道德`, `␣moral`, `␣Moral`, `的道德`, `␣morally`, `␣morality`, `␣morals`, `职业道德` | postans_slot4 | 97/152 (64%) | 29/81 (36%) | 1/138 (1%) | 0/158 (0%) | 40/79 (51%) | 28/77 (36%) |
| unauthorized | unclear | 5 | `␣Unauthorized`, `␣unauthorized` | think_slot2 | 79/152 (52%) | 45/81 (56%) | 6/138 (4%) | 0/158 (0%) | 46/79 (58%) | 44/77 (57%) |
| doubt | unclear | 4 | `质疑`, `疑`, `置疑`, `疑似` | think_slot0 | 81/152 (53%) | 36/81 (44%) | 116/138 (84%) | 146/158 (92%) | 42/79 (53%) | 34/77 (44%) |
| persona | unclear | 3 | `␣persona`, `␣Persona`, `Persona`, `␣personas`, `␣Personas`, `persona`, `_persona` | q_tok27 | 91/152 (60%) | 26/81 (32%) | 4/138 (3%) | 0/158 (0%) | 47/79 (59%) | 25/77 (32%) |
| hoax | lie | 2 | `␣hoax` | q_tok21 | 56/152 (37%) | 60/81 (74%) | 117/138 (85%) | 158/158 (100%) | 29/79 (37%) | 57/77 (74%) |
| confidential | lie/unclear | 11 | `␣confidentiality`, `保密`, `␣Confidential`, `␣confidential`, `机密` | preans_slot1 | 80/152 (53%) | 33/81 (41%) | 5/138 (4%) | 0/158 (0%) | 35/79 (44%) | 30/77 (39%) |
| fiction | lie/unclear | 4 | `␣fictional`, `␣fict`, `␣Fiction`, `␣fiction`, `fiction`, `虚构` | think_slot0 | 80/152 (53%) | 33/81 (41%) | 10/138 (7%) | 0/158 (0%) | 49/79 (62%) | 33/77 (43%) |
| simulate | unclear | 4 | `模拟`, `␣simulated`, `␣simulation`, `␣Simulation`, `␣simulate`, `Simulation`, `仿真`, `␣simulations`, `simulate`, `simulation` | q_tok20 | 79/152 (52%) | 34/81 (42%) | 10/138 (7%) | 0/158 (0%) | 38/79 (48%) | 31/77 (40%) |
| instructed | unclear | 3 | `␣instructed`, `␣tasked` | q_tok27 | 91/152 (60%) | 22/81 (27%) | 9/138 (7%) | 2/158 (1%) | 52/79 (66%) | 19/77 (25%) |
| role | unclear | 3 | `␣role`, `role`, `角色`, `␣roles`, `␣Roles`, `␣Role`, `Role`, `-role`, `的角色`, `角色的` … (+11) | q_tok27 | 88/152 (58%) | 23/81 (28%) | 0/138 (0%) | 0/158 (0%) | 48/79 (61%) | 22/77 (29%) |
| claim | unclear | 6 | `␣Claim`, `声称`, `␣claims`, `␣claim`, `␣Claims`, `␣claiming`, `claim`, `␣claimed`, `claims`, `Claim` … (+7) | q_tok26 | 98/152 (64%) | 11/81 (14%) | 3/138 (2%) | 3/158 (2%) | 57/79 (72%) | 10/77 (13%) |
| clever | unclear | 1 | `巧妙地`, `巧妙` | think_slot1 | 68/152 (45%) | 41/81 (51%) | 85/138 (62%) | 100/158 (63%) | 35/79 (44%) | 38/77 (49%) |
| role-play | unclear | 4 | `扮演`, `角色扮演`, `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas` | q_tok20 | 72/152 (47%) | 36/81 (44%) | 1/138 (1%) | 0/158 (0%) | 37/79 (47%) | 33/77 (43%) |
| hint | unclear | 1 | `暗示` | think_slot0 | 81/152 (53%) | 26/81 (32%) | 68/138 (49%) | 88/158 (56%) | 44/79 (56%) | 25/77 (32%) |
| undisclosed | lie | 10 | `␣undisclosed`, `␣undisclosed` | q_tok19 | 86/152 (57%) | 15/81 (19%) | 9/138 (7%) | 0/158 (0%) | 40/79 (51%) | 14/77 (18%) |
| facts | unclear | 2 | `事实`, `␣facts`, `␣factual`, `实际情况`, `␣Facts`, `facts`, `的事实`, `␣Fact`, `事实上`, `根据实际情况` … (+7) | preans_slot1 | 83/152 (55%) | 14/81 (17%) | 82/138 (59%) | 130/158 (82%) | 46/79 (58%) | 11/77 (14%) |
| genuine | truth | 3 | `␣genuinely`, `␣genuine` | q_tok26 | 71/152 (47%) | 21/81 (26%) | 3/138 (2%) | 43/158 (27%) | 24/79 (30%) | 18/77 (23%) |
| suppress | lie | 2 | `␣suppressing`, `␣suppress`, `␣suppressed`, `suppress` | think_slot0 | 56/152 (37%) | 35/81 (43%) | 2/138 (1%) | 0/158 (0%) | 40/79 (51%) | 35/77 (45%) |
| whistleblower | truth | 1 | `␣whistleblower`, `␣whistlebl` | postans_slot4 | 63/152 (41%) | 24/81 (30%) | 3/138 (2%) | 0/158 (0%) | 31/79 (39%) | 24/77 (31%) |
| adhere | unclear | 3 | `␣adherence`, `遵守`, `␣adher`, `␣adhere`, `严格遵守`, `遵循`, `遵照`, `遵从`, `遵守国家` | q_tok27 | 60/152 (39%) | 25/81 (31%) | 21/138 (15%) | 0/158 (0%) | 29/79 (37%) | 22/77 (29%) |
| actual | unclear | 2 | `␣reality`, `实际情况`, `␣Reality`, `␣actual`, `实际`, `actual`, `␣Actual`, `Reality`, `␣actually`, `事实上` … (+11) | q_tok26 | 64/152 (42%) | 19/81 (23%) | 11/138 (8%) | 12/158 (8%) | 25/79 (32%) | 17/77 (22%) |
| comply | unclear | 7 | `合规`, `␣compliance`, `␣complied`, `␣complying`, `␣Compliance`, `遵守`, `␣comply`, `␣compliant`, `严格遵守` | q_tok27 | 56/152 (37%) | 26/81 (32%) | 13/138 (9%) | 1/158 (1%) | 29/79 (37%) | 24/77 (31%) |
| unintentional | unclear | 2 | `␣unintention`, `␣accidentally`, `␣inadvertently`, `␣accident`, `␣accidental` | q_tok1 | 63/152 (41%) | 19/81 (23%) | 53/138 (38%) | 47/158 (30%) | 28/79 (35%) | 17/77 (22%) |
| forget | unclear | 2 | `␣forget`, `␣forgot`, `␣forgetting`, `␣Forget`, `␣forgotten`, `forget`, `␣Forgot` | q_tok1 | 49/152 (32%) | 31/81 (38%) | 51/138 (37%) | 152/158 (96%) | 20/79 (25%) | 29/77 (38%) |
| mistake | unclear | 2 | `␣mistake`, `␣mistakenly`, `␣mistaken`, `␣mistakes` | q_tok1 | 48/152 (32%) | 27/81 (33%) | 81/138 (59%) | 108/158 (68%) | 20/79 (25%) | 26/77 (34%) |
| hypocrisy | lie | 8 | `␣hypocrisy`, `虚伪` | postans_slot4 | 46/152 (30%) | 26/81 (32%) | 4/138 (3%) | 0/158 (0%) | 28/79 (35%) | 25/77 (32%) |
| refuse | unclear | 16 | `拒绝`, `␣refusal`, `␣refusing`, `␣refus`, `␣refused`, `拒`, `␣refuse`, `␣refuses`, `拒絕`, `拒绝了` … (+10) | q_tok27 | 30/152 (20%) | 41/81 (51%) | 2/138 (1%) | 0/158 (0%) | 16/79 (20%) | 40/77 (52%) |
| mandated | unclear | 2 | `␣mandated`, `␣mandate`, `␣mandates`, `␣mandatory`, `␣Mandatory`, `mandatory`, `␣mandat`, `␣mandato` | q_tok27 | 53/152 (35%) | 15/81 (19%) | 17/138 (12%) | 0/158 (0%) | 29/79 (37%) | 13/77 (17%) |
| resignation | unclear | 1 | `无奈` | think_slot1 | 55/152 (36%) | 12/81 (15%) | 0/138 (0%) | 1/158 (1%) | 21/79 (27%) | 11/77 (14%) |
| apologize | truth/unclear | 8 | `␣apologize`, `␣apologized`, `␣apology`, `␣apologies`, `道歉` | q_tok22 | 35/152 (23%) | 30/81 (37%) | 97/138 (70%) | 100/158 (63%) | 28/79 (35%) | 30/77 (39%) |
| expose | truth/unclear | 3 | `揭露`, `␣exposed`, `␣expose`, `Expose`, `␣exposing`, `␣exposes`, `␣Exposure`, `Exposed`, `揭`, `暴露` … (+1) | q_tok22 | 51/152 (34%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 23/79 (29%) | 12/77 (16%) |
| ethical | unclear | 11 | `␣ethical`, `ethical`, `␣morally`, `␣ethics`, `␣moral`, `道德`, `␣Moral`, `伦理`, `的道德`, `␣morality` … (+1) | q_tok27 | 39/152 (26%) | 21/81 (26%) | 4/138 (3%) | 0/158 (0%) | 20/79 (25%) | 20/77 (26%) |
| assert | unclear | 5 | `␣assertions`, `assert`, `␣assertion`, `␣Assert`, `␣asserting`, `␣assert`, `␣asserted`, `␣asserts`, `␣Assertion`, `/assert` … (+7) | q_tok26 | 50/152 (33%) | 9/81 (11%) | 10/138 (7%) | 4/158 (3%) | 33/79 (42%) | 9/77 (12%) |
| fraud | lie | 16 | `␣fraudulent`, `欺诈`, `␣fraud`, `␣Fraud`, `骗局`, `诈骗`, `␣scams`, `弄虚作假` | q_tok2 | 33/152 (22%) | 24/81 (30%) | 14/138 (10%) | 0/158 (0%) | 22/79 (28%) | 23/77 (30%) |
| objective | truth | 1 | `客观` | think_slot1 | 29/152 (19%) | 28/81 (35%) | 55/138 (40%) | 46/158 (29%) | 15/79 (19%) | 26/77 (34%) |
| instructions | unclear | 3 | `␣instructions`, `␣instructed`, `指令`, `␣instruction`, `␣directives`, `␣directive`, `␣Instructions`, `instructions`, `Instructions`, `Instruction` … (+10) | q_tok27 | 42/152 (28%) | 14/81 (17%) | 10/138 (7%) | 1/158 (1%) | 22/79 (28%) | 13/77 (17%) |
| lawful | unclear | 1 | `依法`, `合法`, `依规` | think_slot1 | 43/152 (28%) | 11/81 (14%) | 6/138 (4%) | 5/158 (3%) | 26/79 (33%) | 10/77 (13%) |
| cheat | lie | 14 | `作弊`, `␣cheating`, `␣cheated` | q_tok20 | 49/152 (32%) | 4/81 (5%) | 17/138 (12%) | 14/158 (9%) | 25/79 (32%) | 4/77 (5%) |
| test | unclear | 1 | `测试`, `␣testing`, `␣Testing`, `␣tests`, `␣test`, `testing`, `Testing`, `␣testers`, `␣Tests`, `/testing` … (+8) | postans_slot4 | 17/152 (11%) | 36/81 (44%) | 5/138 (4%) | 4/158 (3%) | 15/79 (19%) | 36/77 (47%) |
| purported | unclear | 2 | `␣purported`, `␣якобы`, `所谓的`, `␣supposedly`, `所谓` | q_tok26 | 45/152 (30%) | 7/81 (9%) | 0/138 (0%) | 2/158 (1%) | 15/79 (19%) | 4/77 (5%) |
| disguise | lie | 8 | `伪装`, `␣disguised`, `␣disguise`, `␣masking` | preans_slot1 | 30/152 (20%) | 19/81 (23%) | 13/138 (9%) | 0/158 (0%) | 13/79 (16%) | 19/77 (25%) |
| prohibited | unclear | 5 | `禁止`, `␣prohibited`, `严禁`, `␣prohibition`, `␣prohibits`, `␣prohibiting` | q_tok24 | 31/152 (20%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 16/79 (20%) | 15/77 (19%) |
| acting | unclear | 1 | `␣acted`, `␣acting` | q_tok27 | 41/152 (27%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 18/79 (23%) | 4/77 (5%) |
| coerce | unclear | 1 | `␣forcing`, `逼迫`, `倒逼`, `␣forced`, `强制`, `逼`, `forcing`, `迫使`, `␣Forced`, `forced` … (+8) | postans_slot4 | 30/152 (20%) | 15/81 (19%) | 2/138 (1%) | 0/158 (0%) | 22/79 (28%) | 14/77 (18%) |
| blame | unclear | 3 | `␣blaming`, `␣blame`, `␣blamed`, `␣blames` | q_tok26 | 42/152 (28%) | 3/81 (4%) | 7/138 (5%) | 0/158 (0%) | 12/79 (15%) | 3/77 (4%) |
| decline | unclear | 6 | `␣declined`, `␣decline`, `␣declining`, `␣declines`, `选择不` | think_slot2 | 20/152 (13%) | 24/81 (30%) | 45/138 (33%) | 44/158 (28%) | 11/79 (14%) | 23/77 (30%) |
| repent | truth | 1 | `忏悔`, `悔`, `␣repent`, `后悔` | q_tok22 | 25/152 (16%) | 19/81 (23%) | 59/138 (43%) | 8/158 (5%) | 19/79 (24%) | 19/77 (25%) |
| trap | unclear | 2 | `陷阱`, `␣Trap`, `␣trap`, `trap`, `␣traps`, `Trap`, `␣trapped`, `␣trapping`, `_trap` | postans_slot4 | 17/152 (11%) | 26/81 (32%) | 3/138 (2%) | 0/158 (0%) | 15/79 (19%) | 26/77 (34%) |
| protect | unclear | 3 | `␣protecting`, `␣protect`, `␣protections`, `保护`, `␣Protect`, `␣protective`, `protect`, `Protect`, `为了保护`, `␣protection` … (+9) | q_tok27 | 32/152 (21%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 23/79 (29%) | 8/77 (10%) |
| constraints | unclear | 3 | `␣constraints`, `␣Constraints`, `约束`, `␣constraint`, `␣Constraint`, `␣CONSTRAINT`, `Constraints`, `Constraint`, `constraints`, `␣constrained` … (+4) | q_tok27 | 30/152 (20%) | 12/81 (15%) | 11/138 (8%) | 0/158 (0%) | 17/79 (22%) | 12/77 (16%) |
| explicit | unclear | 1 | `␣Explicit`, `explicit` | think_slot2 | 37/152 (24%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 15/79 (19%) | 5/77 (6%) |
| disclaimer | unclear | 11 | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `␣DISCLAIMER` | q_tok24 | 12/152 (8%) | 27/81 (33%) | 8/138 (6%) | 12/158 (8%) | 9/79 (11%) | 27/77 (35%) |
| interrogate | unclear | 2 | `质问`, `␣interrog`, `␣interrogation` | postans_slot4 | 26/152 (17%) | 13/81 (16%) | 2/138 (1%) | 0/158 (0%) | 22/79 (28%) | 13/77 (17%) |
| misunderstand | unclear | 2 | `␣misunderstood`, `␣misunderstand`, `␣misunderstanding`, `误解`, `误会` | q_tok1 | 14/152 (9%) | 25/81 (31%) | 48/138 (35%) | 54/158 (34%) | 11/79 (14%) | 24/77 (31%) |
| apology | truth/unclear | 3 | `抱歉`, `Sorry`, `␣Sorry`, `sorry`, `␣apologize`, `␣sorry`, `␣apology` | preans_slot3 | 35/152 (23%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 17/79 (22%) | 3/77 (4%) |
| coward | unclear | 3 | `␣coward` | think_slot2 | 26/152 (17%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 10/77 (13%) |
| trustworthy | truth | 1 | `␣trustworthy` | q_tok28 | 30/152 (20%) | 6/81 (7%) | 2/138 (1%) | 5/158 (3%) | 19/79 (24%) | 6/77 (8%) |
| taboo | unclear | 1 | `禁忌` | think_slot2 | 24/152 (16%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 6/77 (8%) |
| reject | unclear | 13 | `␣Reject`, `␣rejection`, `Reject`, `␣rejected`, `reject`, `␣rejecting`, `␣reject`, `␣rejection`, `rejected`, `Rejected` … (+5) | q_tok27 | 3/152 (2%) | 28/81 (35%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 28/77 (36%) |
| falsehood | lie | 3 | `␣falsehood` | preans_slot4 | 28/152 (18%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 14/79 (18%) | 3/77 (4%) |
| legitimate | unclear | 2 | `␣legitimate`, `␣legitimately`, `␣legitim`, `␣legitimacy` | q_tok26 | 21/152 (14%) | 10/81 (12%) | 0/138 (0%) | 11/158 (7%) | 12/79 (15%) | 8/77 (10%) |
| loyal | unclear | 3 | `忠诚`, `␣loyalty`, `␣loyal`, `忠诚度`, `␣allegiance` | q_tok27 | 26/152 (17%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 20/79 (25%) | 4/77 (5%) |
| anonymous | unclear | 2 | `␣Anonymous`, `␣anonymity`, `␣anonymously` | think_slot2 | 21/152 (14%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 9/77 (12%) |
| faithful | truth | 4 | `忠实`, `␣faithfully`, `␣faithful` | q_tok27 | 27/152 (18%) | 3/81 (4%) | 10/138 (7%) | 0/158 (0%) | 15/79 (19%) | 3/77 (4%) |
| vague | unclear | 2 | `␣vague`, `␣vaguely`, `含糊`, `模糊` | q_tok26 | 22/152 (14%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 14/79 (18%) | 6/77 (8%) |
| forge | lie | 2 | `伪造` | think_slot1 | 21/152 (14%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 15/79 (19%) | 7/77 (9%) |
| obey | unclear | 2 | `␣obey`, `服从`, `␣obedience`, `␣obedient` | q_tok27 | 24/152 (16%) | 5/81 (6%) | 7/138 (5%) | 0/158 (0%) | 10/79 (13%) | 4/77 (5%) |
| framing | unclear | 4 | `␣framing`, `␣framed`, `␣frames`, `frames`, `␣Frames` | q_tok26 | 27/152 (18%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 13/79 (16%) | 2/77 (3%) |
| wrongdoing | lie/unclear | 4 | `␣wrongdoing`, `␣wrongful` | q_tok22 | 2/152 (1%) | 25/81 (31%) | 76/138 (55%) | 81/158 (51%) | 0/79 (0%) | 24/77 (31%) |
| transparent | truth | 5 | `␣transparency`, `透明`, `␣Transparency`, `␣transparent`, `透明度`, `transparent`, `-transparent`, `␣Transparent`, `␣transparencia`, `透明的` | q_tok28 | 4/152 (3%) | 23/81 (28%) | 0/138 (0%) | 1/158 (1%) | 1/79 (1%) | 23/77 (30%) |
| allege | unclear | 7 | `␣allegations`, `␣allegation`, `␣alleged`, `␣alleging`, `␣alleging`, `␣allegedly`, `␣alleges`, `␣allege`, `␣Alleg` | q_tok26 | 25/152 (16%) | 2/81 (2%) | 3/138 (2%) | 1/158 (1%) | 12/79 (15%) | 2/77 (3%) |
| trick | lie/unclear | 2 | `␣trick`, `␣Trick`, `␣tricks`, `␣Tricks` | postans_slot4 | 7/152 (5%) | 18/81 (22%) | 1/138 (1%) | 1/158 (1%) | 7/79 (9%) | 18/77 (23%) |
| private | unclear | 1 | `␣privately`, `␣private` | q_tok19 | 23/152 (15%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 15/79 (19%) | 2/77 (3%) |
| bribe | unclear | 2 | `␣brib` | q_tok1 | 15/152 (10%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 12/79 (15%) | 7/77 (9%) |
| avoid | unclear | 4 | `␣avoiding`, `avoid`, `␣avoidance`, `␣avoided`, `␣avoid`, `␣Avoid`, `Avoid`, `避开`, `␣evasion`, `回避` … (+2) | q_tok27 | 9/152 (6%) | 13/81 (16%) | 1/138 (1%) | 0/158 (0%) | 8/79 (10%) | 12/77 (16%) |
| deliberate | unclear | 1 | `故意` | postans_slot4 | 4/152 (3%) | 17/81 (21%) | 3/138 (2%) | 0/158 (0%) | 4/79 (5%) | 17/77 (22%) |
| sabotage | unclear | 2 | `␣sabotage` | preans_slot2 | 13/152 (9%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 7/79 (9%) | 8/77 (10%) |
| reinterpret | unclear | 3 | `␣reinterpret`, `reinterpret` | q_tok26 | 16/152 (11%) | 4/81 (5%) | 2/138 (1%) | 6/158 (4%) | 9/79 (11%) | 4/77 (5%) |
| pressured | unclear | 2 | `␣pressure`, `␣forced`, `␣Pressure`, `pressure`, `␣compelled`, `Pressure`, `␣pressures`, `␣pressured`, `␣coerc`, `␣coercion` … (+3) | q_tok27 | 17/152 (11%) | 3/81 (4%) | 5/138 (4%) | 0/158 (0%) | 13/79 (16%) | 3/77 (4%) |
| responsible | unclear | 3 | `␣responsibly`, `␣responsible`, `␣responsibilities`, `␣Responsibilities`, `␣responsibility` | q_tok27 | 13/152 (9%) | 7/81 (9%) | 2/138 (1%) | 0/158 (0%) | 10/79 (13%) | 7/77 (9%) |
| omit | lie | 10 | `␣omit`, `␣omission`, `␣omitted`, `omit`, `省略`, `␣OMIT` | q_tok24 | 12/152 (8%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 8/79 (10%) | 5/77 (6%) |
| guilt | unclear | 2 | `␣guilty` | q_tok22 | 4/152 (3%) | 14/81 (17%) | 3/138 (2%) | 0/158 (0%) | 2/79 (3%) | 14/77 (18%) |
| fraud / scam | lie | 1 | `␣fraudulent`, `␣fraud`, `欺诈`, `骗局`, `骗取`, `␣scams`, `␣Fraud`, `诈骗`, `骗子`, `␣scam` … (+1) | preans_slot2 | 11/152 (7%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 6/79 (8%) | 6/77 (8%) |
| cover up | lie | 4 | `掩盖`, `掩饰`, `掩护`, `遮掩` | preans_slot2 | 12/152 (8%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 3/77 (4%) |
| forced | unclear | 2 | `␣forced`, `␣compelled`, `␣coerc`, `␣coercion`, `forced`, `␣Forced` | q_tok27 | 14/152 (9%) | 1/81 (1%) | 5/138 (4%) | 0/158 (0%) | 10/79 (13%) | 1/77 (1%) |
| diplomatic | unclear | 2 | `␣diplomatic`, `␣diplomacy` | q_tok27 | 10/152 (7%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 4/77 (5%) |
| scripted | unclear | 2 | `␣scripted` | q_tok27 | 14/152 (9%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| phishing | lie | 1 | `␣phishing` | postans_slot4 | 3/152 (2%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 11/77 (14%) |
| evade | lie/unclear | 8 | `回避`, `␣evasion`, `规避`, `逃避`, `␣evade` | q_tok24 | 8/152 (5%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| ambiguous | unclear | 2 | `␣ambiguous`, `␣ambiguity`, `␣ambigu`, `ambiguous` | q_tok26 | 13/152 (9%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 9/79 (11%) | 1/77 (1%) |
| misunderstanding | unclear | 2 | `误解`, `␣misunderstood` | think_slot3 | 2/152 (1%) | 12/81 (15%) | 11/138 (8%) | 30/158 (19%) | 2/79 (3%) | 12/77 (16%) |
| contradiction | unclear | 2 | `␣contradiction`, `␣contradict`, `␣contradictory`, `矛盾`, `␣contradictions` | postans_slot4 | 7/152 (5%) | 6/81 (7%) | 89/138 (64%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| immoral | lie | 1 | `␣immoral` | postans_slot4 | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| censorship | unclear | 1 | `␣censorship` | postans_slot4 | 6/152 (4%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 4/79 (5%) | 7/77 (9%) |
| propaganda | lie | 3 | `␣propaganda` | preans_slot2 | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 2/77 (3%) |
| exaggerate | lie | 7 | `夸大`, `␣exaggerated` | q_tok26 | 9/152 (6%) | 4/81 (5%) | 1/138 (1%) | 3/158 (2%) | 4/79 (5%) | 3/77 (4%) |
| voluntary | unclear | 1 | `␣voluntarily`, `␣willingly` | q_tok1 | 4/152 (3%) | 9/81 (11%) | 6/138 (4%) | 0/158 (0%) | 4/79 (5%) | 9/77 (12%) |
| concede | truth | 1 | `␣concede`, `␣conced` | q_tok22 | 13/152 (9%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 0/77 (0%) |
| excuse | lie | 1 | `借口`, `␣excuse`, `␣excuses` | q_tok26 | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 2/77 (3%) |
| loophole | unclear | 1 | `␣loophole` | postans_slot4 | 2/152 (1%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 10/77 (13%) |
| whistleblow | unclear | 3 | `␣whistleblower`, `␣whistlebl` | q_tok1 | 4/152 (3%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 8/77 (10%) |
| manipulate | lie | 7 | `␣manipulated`, `␣manipulation`, `␣manipulate`, `␣manipulating`, `␣manipul` | postans_slot4 | 3/152 (2%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 8/77 (10%) |
| withhold | lie | 6 | `␣withheld`, `␣withholding`, `␣withhold` | q_tok19 | 6/152 (4%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 4/77 (5%) |
| sorry | unclear | 2 | `抱歉`, `Sorry`, `␣Sorry`, `对不起`, `␣Oops` | think_slot2 | 10/152 (7%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 1/77 (1%) |
| accountability | unclear | 2 | `␣Accountability`, `␣accountability` | postans_slot4 | 8/152 (5%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| disobey | unclear | 1 | `␣disob` | q_tok1 | 2/152 (1%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 6/77 (8%) |
| undercover | unclear | 2 | `␣undercover` | q_tok24 | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| caught | unclear | 1 | `Caught` | think_slot0 | 5/152 (3%) | 3/81 (4%) | 2/138 (1%) | 5/158 (3%) | 1/79 (1%) | 3/77 (4%) |
| transparency | truth | 2 | `␣transparency`, `␣Transparency` | postans_slot4 | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| pressure | unclear | 1 | `␣Pressure`, `␣pressure`, `␣pressures`, `␣pressured` | postans_slot4 | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 2/77 (3%) |
| dilemma | unclear | 1 | `␣dilemma` | postans_slot4 | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 4/77 (5%) |
| hallucinate | unclear | 3 | `␣halluc` | q_tok20 | 4/152 (3%) | 3/81 (4%) | 86/138 (62%) | 133/158 (84%) | 2/79 (3%) | 3/77 (4%) |
| reveal | truth | 7 | `␣revealed`, `揭露`, `␣revealing`, `揭`, `揭秘`, `␣reveal`, `reveal`, `透露` | preans_slot2 | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| betray | lie/unclear | 6 | `␣betrayed`, `␣betrayal`, `␣betray`, `背叛`, `␣betray`, `␣betrayal` | q_tok20 | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 1/77 (1%) |
| blackmail | unclear | 1 | `␣blackmail` | postans_slot4 | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| hypocritical | lie | 1 | `虚伪` | q_tok19 | 0/152 (0%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 6/77 (8%) |
| justify | unclear | 4 | `辩解`, `␣justification`, `␣justified` | q_tok26 | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 3/79 (4%) | 1/77 (1%) |
| self-protection | unclear | 1 | `自我保护` | think_slot2 | 3/152 (2%) | 3/81 (4%) | 4/138 (3%) | 2/158 (1%) | 3/79 (4%) | 3/77 (4%) |
| bait | unclear | 1 | `␣bait` | postans_slot4 | 2/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 3/77 (4%) |
| conspiracy | unclear | 1 | `␣conspiracy` | postans_slot4 | 1/152 (1%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 4/77 (5%) |
| evasion | lie | 2 | `␣evasion` | postans_slot4 | 0/152 (0%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 0/79 (0%) | 4/77 (5%) |
| scam | lie | 1 | `␣scams`, `骗局`, `␣scam`, `␣hoax` | preans_slot2 | 3/152 (2%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| threat | unclear | 1 | `威胁` | postans_slot4 | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| crime | unclear | 2 | `␣crimes`, `␣criminal`, `犯罪事实`, `crime`, `犯罪` | preans_slot2 | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| loyalty | unclear | 2 | `忠诚`, `忠诚度` | preans_slot2 | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| bullshit | lie | 1 | `␣bullshit` | q_tok3 | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| impersonate | lie | 3 | `冒充` | q_tok20 | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| make public | truth | 2 | `公开`, `公开的` | q_tok19 | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| inaccurate | lie | 3 | `不准确` | q_tok24 | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 2/158 (1%) | 1/79 (1%) | 2/77 (3%) |
| improper | unclear | 1 | `␣improper` | q_tok0 | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| inconsistent | unclear | 1 | `␣inconsistency`, `␣inconsistencies` | q_tok7 | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| ethics / morality | unclear | 1 | `␣ethics`, `道德` | q_tok1 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| innocent | truth | 2 | `无罪` | q_tok25 | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| spin | lie | 3 | `␣spin`, `␣spinning`, `␣spins`, `spin`, `Spin`, `-spin`, `␣Spin`, `.spin`, `_spin` | q_tok24 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| stealth | lie | 1 | `␣stealth`, `␣Stealth` | postans_slot4 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| pretext | lie | 1 | `␣pretext` | preans_slot2 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| distort | lie | 1 | `␣distorted`, `␣distort` | preans_slot2 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| regret | unclear | 1 | `␣regret` | q_tok1 | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| abstain | unclear | 1 | `弃权` | q_tok11 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| self-reflection | unclear | 1 | `反思` | q_tok14 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| malicious | lie | 1 | `␣malicious` | q_tok22 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| bluff | lie | 1 | `␣bluff` | q_tok27 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| oops | unclear | 1 | `Oops` | think_slot1 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| evil | lie | 1 | `␣Evil` | think_slot2 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |

**wording Q9_dyl, positions from the question on** (163 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|---|---|
| honest | truth | 17 | `␣honesty`, `␣honest`, `诚实`, `␣honestly`, `␣Honest`, `诚实守信`, `␣truthful`, `如实`, `诚信`, `坦诚` … (+4) | preans_slot1 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 156/158 (99%) | 65/65 (100%) | 76/76 (100%) |
| deceive | lie | 12 | `欺骗`, `骗`, `␣deception`, `␣deceive`, `␣deceit`, `␣deceptive`, `␣deceived`, `欺` | preans_slot1 | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 156/158 (99%) | 65/65 (100%) | 76/76 (100%) |
| fake | lie | 16 | `fake`, `␣Fake`, `␣fake`, `Fake`, `伪造`, `造假`, `_fake`, `假`, `弄虚作假`, `假的` … (+3) | q_tok2 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| legal | unclear | 6 | `␣Legal`, `␣legality`, `␣legally`, `Legal`, `legal`, `/legal`, `合法`, `␣legal`, `_legal`, `␣legitimate` … (+2) | think_slot0 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 155/158 (98%) | 65/65 (100%) | 76/76 (100%) |
| false | lie | 21 | `␣fals`, `␣false`, `␣falsehood`, `false`, `False`, `␣falsely`, `␣untrue`, `/false`, `虚假`, `␣False` … (+21) | preans_slot1 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| dishonest | lie | 11 | `␣dishonest`, `虚伪` | q_tok2 | 152/152 (100%) | 80/81 (99%) | 134/138 (97%) | 146/158 (92%) | 65/65 (100%) | 75/76 (99%) |
| violate | unclear | 13 | `违反`, `违背`, `␣violate`, `违规`, `␣violating`, `␣violates`, `违反了`, `␣violation`, `␣violated`, `␣violations` … (+3) | think_slot1 | 152/152 (100%) | 80/81 (99%) | 122/138 (88%) | 123/158 (78%) | 65/65 (100%) | 75/76 (99%) |
| wrong | lie | 17 | `错误`, `错`, `␣wrong`, `␣Wrong`, `␣WRONG`, `␣ERROR`, `误`, `的错误`, `wrong`, `错了` … (+10) | think_slot1 | 151/152 (99%) | 81/81 (100%) | 113/138 (82%) | 114/158 (72%) | 64/65 (98%) | 76/76 (100%) |
| compliant | unclear | 3 | `合规`, `依法依规`, `依法`, `依规`, `恪守`, `严格遵守`, `规范要求`, `␣Compliance`, `␣compliance` | think_slot0 | 151/152 (99%) | 80/81 (99%) | 138/138 (100%) | 1/158 (1%) | 65/65 (100%) | 75/76 (99%) |
| leak | truth/unclear | 5 | `泄露`, `␣leaked`, `␣leak`, `␣WikiLeaks` | think_slot2 | 149/152 (98%) | 81/81 (100%) | 102/138 (74%) | 111/158 (70%) | 65/65 (100%) | 76/76 (100%) |
| truthful | truth | 10 | `␣truthful`, `实事求是` | q_tok2 | 152/152 (100%) | 78/81 (96%) | 138/138 (100%) | 157/158 (99%) | 65/65 (100%) | 73/76 (96%) |
| hide | lie | 11 | `␣hiding`, `隐藏`, `隐瞒`, `hide`, `␣hide`, `␣hides`, `␣conceal`, `掩盖`, `␣hidden`, `␣Hidden` … (+19) | preans_slot1 | 150/152 (99%) | 77/81 (95%) | 100/138 (72%) | 55/158 (35%) | 65/65 (100%) | 72/76 (95%) |
| conceal | lie | 10 | `隐瞒`, `␣conceal`, `␣concealed`, `瞒`, `隐`, `掩盖`, `隐匿`, `藏`, `掩`, `hide` … (+2) | preans_slot1 | 150/152 (99%) | 77/81 (95%) | 100/138 (72%) | 55/158 (35%) | 65/65 (100%) | 72/76 (95%) |
| secret | lie | 8 | `秘密`, `␣secrecy`, `的秘密`, `␣secretive`, `␣secretly`, `␣secret`, `secret`, `Secret`, `␣Secret`, `␣covert` … (+8) | think_slot0 | 149/152 (98%) | 77/81 (95%) | 92/138 (67%) | 77/158 (49%) | 64/65 (98%) | 72/76 (95%) |
| silence | unclear | 6 | `␣silence`, `␣Silence`, `␣Silent`, `沉默`, `silent`, `␣silencio`, `␣silenc`, `寂静` | think_slot2 | 148/152 (97%) | 78/81 (96%) | 23/138 (17%) | 6/158 (4%) | 63/65 (97%) | 74/76 (97%) |
| fake / fabricate | lie | 2 | `fake`, `伪造`, `Fake`, `␣fake`, `␣Fake`, `造假`, `弄虚作假`, `␣fabrication`, `␣fabricated`, `_fake` … (+1) | preans_slot1 | 147/152 (97%) | 76/81 (94%) | 128/138 (93%) | 158/158 (100%) | 62/65 (95%) | 71/76 (93%) |
| fabricate | lie | 11 | `伪造`, `␣fabricated`, `␣fabrication`, `造假`, `弄虚作假`, `虚构` | q_tok2 | 145/152 (95%) | 76/81 (94%) | 125/138 (91%) | 100/158 (63%) | 64/65 (98%) | 73/76 (96%) |
| cannot | unclear | 7 | `我无法`, `␣cannot`, `Cannot`, `cannot`, `␣Cannot`, `无法`, `我不能`, `无法满足`, `不能说`, `不能` … (+20) | think_slot1 | 147/152 (97%) | 72/81 (89%) | 131/138 (95%) | 157/158 (99%) | 64/65 (98%) | 68/76 (89%) |
| justify | unclear | 2 | `␣justification`, `辩解`, `␣justify` | q_tok12 | 141/152 (93%) | 73/81 (90%) | 125/138 (91%) | 157/158 (99%) | 61/65 (94%) | 69/76 (91%) |
| truth | truth | 7 | `␣truthful`, `如实`, `实事求是`, `其真实性` | postans_slot1 | 143/152 (94%) | 65/81 (80%) | 123/138 (89%) | 68/158 (43%) | 64/65 (98%) | 63/76 (83%) |
| clarify | truth/unclear | 6 | `澄清`, `␣clarification`, `␣clarify` | think_slot0 | 135/152 (89%) | 70/81 (86%) | 138/138 (100%) | 152/158 (96%) | 58/65 (89%) | 65/76 (86%) |
| unauthorized | unclear | 6 | `␣Unauthorized`, `␣unauthorized`, `Unauthorized` | think_slot2 | 138/152 (91%) | 67/81 (83%) | 6/138 (4%) | 1/158 (1%) | 59/65 (91%) | 62/76 (82%) |
| refuse | unclear | 10 | `拒绝`, `␣refusal`, `␣refus`, `␣refusing`, `拒`, `␣refused`, `␣refuse`, `␣Reject`, `␣refuses`, `拒绝了` … (+8) | think_slot2 | 136/152 (89%) | 57/81 (70%) | 10/138 (7%) | 0/158 (0%) | 62/65 (95%) | 53/76 (70%) |
| disclaimer | unclear | 14 | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `␣DISCLAIMER`, `免责声明` | q_tok6 | 109/152 (72%) | 74/81 (91%) | 118/138 (86%) | 99/158 (63%) | 53/65 (82%) | 71/76 (93%) |
| misinformation | lie | 10 | `␣misinformation`, `虚假信息` | preans_slot1 | 126/152 (83%) | 55/81 (68%) | 131/138 (95%) | 155/158 (98%) | 57/65 (88%) | 51/76 (67%) |
| hypocrisy | lie | 5 | `␣hypocrisy`, `虚伪` | think_slot2 | 119/152 (78%) | 58/81 (72%) | 0/138 (0%) | 9/158 (6%) | 49/65 (75%) | 56/76 (74%) |
| illegal | unclear | 8 | `违法`, `非法`, `␣illegal`, `illegal`, `Illegal`, `␣illegally`, `␣Illegal`, `违法违规`, `␣ilegal`, `␣illicit` | think_slot0 | 115/152 (76%) | 57/81 (70%) | 74/138 (54%) | 30/158 (19%) | 52/65 (80%) | 53/76 (70%) |
| privacy | unclear | 3 | `隐私`, `␣privacy`, `privacy`, `␣Privacy`, `Privacy`, `␣privacidad`, `private`, `/Private` | think_slot2 | 123/152 (81%) | 49/81 (60%) | 55/138 (40%) | 12/158 (8%) | 53/65 (82%) | 45/76 (59%) |
| ethics | unclear | 6 | `␣ethical`, `␣ethics`, `␣Ethics`, `ethical`, `伦理`, `␣ethic`, `道德`, `etica`, `␣moral`, `␣morally` … (+5) | postans_slot4 | 117/152 (77%) | 52/81 (64%) | 9/138 (7%) | 0/158 (0%) | 45/65 (69%) | 50/76 (66%) |
| ethical | truth/unclear | 10 | `␣ethical`, `ethical`, `道德`, `␣ethics`, `␣morally`, `伦理`, `␣moral`, `␣morality`, `␣Moral`, `的道德` … (+4) | postans_slot4 | 116/152 (76%) | 52/81 (64%) | 9/138 (7%) | 0/158 (0%) | 44/65 (68%) | 50/76 (66%) |
| unethical | lie | 10 | `␣unethical`, `␣immoral`, `␣wrongdoing` | postans_slot4 | 109/152 (72%) | 57/81 (70%) | 16/138 (12%) | 0/158 (0%) | 41/65 (63%) | 54/76 (71%) |
| morality | unclear | 3 | `道德`, `␣morally`, `␣moral`, `␣ethics`, `␣Ethics`, `伦理`, `␣Moral`, `的道德`, `␣morality`, `␣morals` … (+2) | postans_slot4 | 114/152 (75%) | 44/81 (54%) | 5/138 (4%) | 0/158 (0%) | 42/65 (65%) | 42/76 (55%) |
| true | truth | 14 | `␣true`, `真实`, `真实性`, `的真实`, `␣TRUE`, `True`, `真实的`, `的真实性`, `>true`, `确实` … (+12) | preans_slot1 | 118/152 (78%) | 36/81 (44%) | 97/138 (70%) | 41/158 (26%) | 41/65 (63%) | 33/76 (43%) |
| prohibited | unclear | 2 | `␣Forbidden`, `␣prohibited`, `禁止`, `严禁`, `禁用`, `禁忌`, `␣forbidden`, `Forbidden`, `␣запрещ`, `␣запрещено` … (+4) | think_slot2 | 108/152 (71%) | 45/81 (56%) | 6/138 (4%) | 0/158 (0%) | 45/65 (69%) | 43/76 (57%) |
| pretend | lie | 10 | `␣pretending`, `伪装`, `␣pretend`, `假装`, `␣undercover`, `␣pretended`, `␣disguised`, `␣disguise` | q_tok7 | 88/152 (58%) | 54/81 (67%) | 50/138 (36%) | 32/158 (20%) | 51/65 (78%) | 51/76 (67%) |
| mislead | lie | 11 | `␣misleading`, `误导`, `␣misled`, `误导性` | q_tok6 | 97/152 (64%) | 41/81 (51%) | 88/138 (64%) | 12/158 (8%) | 48/65 (74%) | 38/76 (50%) |
| integrity | truth | 9 | `诚信`, `␣Integrity`, `␣integrity` | q_tok2 | 98/152 (64%) | 36/81 (44%) | 36/138 (26%) | 39/158 (25%) | 37/65 (57%) | 34/76 (45%) |
| incorrect | lie | 16 | `␣incorrect`, `␣Incorrect`, `incorrect`, `␣inaccurate`, `错误的`, `不符合`, `␣incorrectly`, `Incorrect`, `␣inaccur`, `␣erroneous` … (+3) | q_tok6 | 89/152 (59%) | 44/81 (54%) | 125/138 (91%) | 96/158 (61%) | 39/65 (60%) | 42/76 (55%) |
| disclose | truth | 7 | `␣disclosure`, `␣disclosures`, `␣Disclosure`, `␣disclosing`, `␣disclose`, `揭露`, `␣disclosed`, `披露`, `信息披露`, `透露` | think_slot2 | 102/152 (67%) | 30/81 (37%) | 11/138 (8%) | 5/158 (3%) | 42/65 (65%) | 26/76 (34%) |
| fiction | unclear | 8 | `虚构`, `␣fictional`, `fiction`, `␣fict`, `␣fiction`, `␣Fiction`, `-fiction` | preans_slot1 | 82/152 (54%) | 46/81 (57%) | 80/138 (58%) | 136/158 (86%) | 34/65 (52%) | 44/76 (58%) |
| factual | truth | 3 | `␣factual`, `事实`, `␣facts`, `的事实`, `␣Facts`, `␣Fact`, `实事求是`, `␣fact`, `Fact`, `fact` … (+7) | preans_slot1 | 96/152 (63%) | 30/81 (37%) | 94/138 (68%) | 138/158 (87%) | 43/65 (66%) | 27/76 (36%) |
| deliberate | unclear | 11 | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `␣deliberate`, `␣purposely`, `刻意`, `明知`, `特意`, `␣sengaja` … (+1) | q_tok1 | 73/152 (48%) | 52/81 (64%) | 64/138 (46%) | 100/158 (63%) | 42/65 (65%) | 50/76 (66%) |
| inconvenient | unclear | 1 | `不方便`, `不便` | think_slot1 | 70/152 (46%) | 50/81 (62%) | 86/138 (62%) | 144/158 (91%) | 26/65 (40%) | 46/76 (61%) |
| refute | unclear | 1 | `␣refute`, `反驳` | think_slot2 | 78/152 (51%) | 41/81 (51%) | 49/138 (36%) | 0/158 (0%) | 36/65 (55%) | 39/76 (51%) |
| whistleblower | unclear | 5 | `␣whistleblower`, `␣whistlebl`, `举报` | postans_slot4 | 84/152 (55%) | 26/81 (32%) | 5/138 (4%) | 0/158 (0%) | 24/65 (37%) | 25/76 (33%) |
| fraud | lie | 7 | `欺诈`, `␣fraudulent`, `␣fraud`, `␣Fraud`, `骗局`, `␣scams`, `骗子` | preans_slot1 | 61/152 (40%) | 46/81 (57%) | 69/138 (50%) | 107/158 (68%) | 36/65 (55%) | 44/76 (58%) |
| knowingly | unclear | 9 | `␣knowingly`, `明知`, `␣knowing`, `␣Knowing`, `Knowing`, `␣consciously` | q_tok1 | 63/152 (41%) | 32/81 (40%) | 37/138 (27%) | 23/158 (15%) | 36/65 (55%) | 30/76 (39%) |
| illusion | unclear | 2 | `错觉`, `幻想`, `幻觉`, `虚幻`, `妄想` | think_slot1 | 66/152 (43%) | 29/81 (36%) | 32/138 (23%) | 62/158 (39%) | 26/65 (40%) | 28/76 (37%) |
| absurd | unclear | 1 | `荒唐`, `滑稽` | think_slot1 | 76/152 (50%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 28/65 (43%) | 18/76 (24%) |
| impossible | unclear | 7 | `Impossible`, `␣Impossible`, `␣impossible`, `␣imposs`, `␣impossibile`, `不可能的`, `是不可能的`, `是不可能` | think_slot2 | 62/152 (41%) | 24/81 (30%) | 2/138 (1%) | 37/158 (23%) | 34/65 (52%) | 23/76 (30%) |
| accidental | unclear | 2 | `␣accidentally`, `␣accidental`, `␣inadvertently`, `␣unintention`, `␣mistakenly` | q_tok1 | 65/152 (43%) | 21/81 (26%) | 67/138 (49%) | 60/158 (38%) | 30/65 (46%) | 18/76 (24%) |
| lawful | unclear | 2 | `合法`, `依法` | think_slot0 | 58/152 (38%) | 28/81 (35%) | 0/138 (0%) | 0/158 (0%) | 29/65 (45%) | 27/76 (36%) |
| secrecy | lie | 1 | `␣secrecy`, `保密` | think_slot2 | 68/152 (45%) | 14/81 (17%) | 10/138 (7%) | 1/158 (1%) | 28/65 (43%) | 14/76 (18%) |
| fact | truth | 9 | `␣factual`, `␣actual`, `实际`, `actual`, `Actual`, `␣actually`, `␣facts`, `␣Facts`, `事实`, `␣Actually` … (+25) | preans_slot2 | 70/152 (46%) | 11/81 (14%) | 22/138 (16%) | 1/158 (1%) | 21/65 (32%) | 10/76 (13%) |
| actually | unclear | 2 | `␣reality`, `␣Reality`, `Reality`, `事实上`, `␣actually`, `actually`, `实际上`, `但实际上`, `实际上是`, `Actually` … (+1) | preans_slot2 | 68/152 (45%) | 12/81 (15%) | 12/138 (9%) | 10/158 (6%) | 22/65 (34%) | 11/76 (14%) |
| reject | unclear | 4 | `reject`, `␣Reject`, `rejected`, `␣rejecting`, `␣rejection`, `Reject`, `␣reject`, `␣rejected`, `否决`, `.reject` | think_slot2 | 64/152 (42%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 35/65 (54%) | 13/76 (17%) |
| mistake | unclear | 3 | `␣mistake`, `␣mistakes`, `␣mistaken`, `␣mistakenly`, `失误` | q_tok1 | 48/152 (32%) | 27/81 (33%) | 81/138 (59%) | 108/158 (68%) | 19/65 (29%) | 25/76 (33%) |
| confidential | lie/unclear | 7 | `保密`, `␣confidentiality`, `␣confidential`, `␣Confidential`, `机密`, `␣discreet` | postans_slot4 | 49/152 (32%) | 25/81 (31%) | 9/138 (7%) | 0/158 (0%) | 20/65 (31%) | 23/76 (30%) |
| conscience | unclear | 2 | `良心`, `␣conscience` | think_slot2 | 61/152 (40%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 18/65 (28%) | 12/76 (16%) |
| verify | unclear | 1 | `␣Verification`, `␣verification`, `验证`, `核实`, `_verified`, `verification`, `␣Verified`, `_verification`, `Verification`, `.verify` | think_slot2 | 48/152 (32%) | 24/81 (30%) | 136/138 (99%) | 154/158 (97%) | 20/65 (31%) | 22/76 (29%) |
| forged | lie | 1 | `伪造`, `虚构` | think_slot1 | 54/152 (36%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 25/65 (38%) | 12/76 (16%) |
| fictional | lie/unclear | 4 | `虚构`, `fiction`, `␣fictional`, `␣Fiction` | think_slot0 | 42/152 (28%) | 24/81 (30%) | 4/138 (3%) | 0/158 (0%) | 23/65 (35%) | 23/76 (30%) |
| caution | unclear | 1 | `需谨慎` | think_slot0 | 46/152 (30%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 26/65 (40%) | 20/76 (26%) |
| accuse | unclear | 5 | `␣accusations`, `␣accusation`, `␣accusing`, `指控`, `␣accused` | q_tok7 | 43/152 (28%) | 22/81 (27%) | 40/138 (29%) | 6/158 (4%) | 25/65 (38%) | 21/76 (28%) |
| contradict | unclear | 7 | `␣contradict`, `␣contradiction`, `␣contradictory`, `␣contrad`, `␣contradictions`, `矛盾`, `␣contradd`, `矛盾的`, `␣inconsistency` | preans_slot2 | 44/152 (29%) | 18/81 (22%) | 39/138 (28%) | 1/158 (1%) | 22/65 (34%) | 17/76 (22%) |
| claim | unclear | 3 | `声称`, `␣claims`, `宣称`, `␣claim`, `␣Claim`, `␣Claims`, `claim`, `␣claimed`, `Claim`, `claims` … (+10) | preans_slot2 | 48/152 (32%) | 13/81 (16%) | 3/138 (2%) | 3/158 (2%) | 27/65 (42%) | 12/76 (16%) |
| misrepresent | lie | 6 | `␣misrepresented` | preans_slot1 | 42/152 (28%) | 17/81 (21%) | 36/138 (26%) | 21/158 (13%) | 18/65 (28%) | 16/76 (21%) |
| violate rules | unclear | 1 | `违规`, `違規` | think_slot0 | 39/152 (26%) | 16/81 (20%) | 4/138 (3%) | 0/158 (0%) | 24/65 (37%) | 15/76 (20%) |
| claim / assert | unclear | 1 | `␣claiming`, `声称`, `␣claim`, `␣claims`, `␣assertions`, `␣asserting`, `claim`, `宣称`, `assert`, `␣claimed` … (+20) | preans_slot2 | 42/152 (28%) | 12/81 (15%) | 10/138 (7%) | 3/158 (2%) | 24/65 (37%) | 11/76 (14%) |
| omit | lie | 5 | `␣omit`, `␣omission`, `␣omitted`, `省略`, `␣OMIT`, `omit` | preans_slot1 | 37/152 (24%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 15/65 (23%) | 8/76 (11%) |
| compliance | unclear | 3 | `遵守`, `合规`, `␣compliance`, `␣Compliance`, `严格遵守` | postans_slot4 | 30/152 (20%) | 16/81 (20%) | 4/138 (3%) | 1/158 (1%) | 8/65 (12%) | 16/76 (21%) |
| direct | unclear | 4 | `␣directly`, `直接`, `␣direct`, `的直接`, `␣Direct`, `Direct`, `␣directement`, `direct`, `␣directamente`, `␣напрямую` … (+12) | q_tok8 | 26/152 (17%) | 20/81 (25%) | 9/138 (7%) | 0/158 (0%) | 11/65 (17%) | 20/76 (26%) |
| trap | unclear | 2 | `陷阱`, `␣Trap`, `trap`, `␣trap`, `Trap`, `␣trapped`, `␣traps`, `␣trapping`, `_trap`, `␣atrap` … (+2) | postans_slot4 | 19/152 (12%) | 26/81 (32%) | 32/138 (23%) | 2/158 (1%) | 11/65 (17%) | 25/76 (33%) |
| coerce | unclear | 2 | `逼`, `逼迫`, `强制`, `倒逼`, `迫使`, `胁迫`, `迫`, `强迫`, `被迫`, `␣forcing` … (+6) | postans_slot4 | 25/152 (16%) | 19/81 (23%) | 7/138 (5%) | 0/158 (0%) | 10/65 (15%) | 18/76 (24%) |
| genuine | truth | 4 | `␣genuinely`, `␣genuine`, `真正的`, `的真正`, `真正` | preans_slot2 | 36/152 (24%) | 7/81 (9%) | 0/138 (0%) | 40/158 (25%) | 10/65 (15%) | 5/76 (7%) |
| undisclosed | lie | 7 | `␣undisclosed` | preans_slot2 | 33/152 (22%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 12/65 (18%) | 8/76 (11%) |
| sorry | unclear | 4 | `␣Sorry`, `抱歉`, `Sorry`, `␣apology`, `␣sorry`, `sorry`, `对不起`, `道歉` | think_slot2 | 31/152 (20%) | 12/81 (15%) | 0/138 (0%) | 3/158 (2%) | 21/65 (32%) | 12/76 (16%) |
| falsify | lie | 2 | `造假`, `弄虚作假` | preans_slot1 | 37/152 (24%) | 5/81 (6%) | 1/138 (1%) | 27/158 (17%) | 15/65 (23%) | 5/76 (7%) |
| trick | lie/unclear | 2 | `␣trick`, `␣Trick`, `␣tricks`, `␣Tricks` | postans_slot4 | 13/152 (9%) | 28/81 (35%) | 37/138 (27%) | 11/158 (7%) | 7/65 (11%) | 27/76 (36%) |
| technically | unclear | 2 | `␣technically`, `技术上`, `技术性` | preans_slot1 | 35/152 (23%) | 6/81 (7%) | 0/138 (0%) | 2/158 (1%) | 13/65 (20%) | 3/76 (4%) |
| hide / conceal | lie | 1 | `-hide`, `隐身`, `masked`, `藏`, `掩` | postans_slot0 | 27/152 (18%) | 12/81 (15%) | 18/138 (13%) | 7/158 (4%) | 16/65 (25%) | 11/76 (14%) |
| misunderstand | unclear | 5 | `␣misunderstand`, `␣misunderstanding`, `␣misunderstood`, `误解` | q_tok1 | 14/152 (9%) | 25/81 (31%) | 49/138 (36%) | 54/158 (34%) | 10/65 (15%) | 24/76 (32%) |
| assert | unclear | 3 | `␣assertions`, `assert`, `␣assertion`, `␣assert`, `␣asserting`, `␣asserts`, `␣Assert`, `␣asserted`, `Assert`, `␣Assertions` … (+1) | preans_slot2 | 32/152 (21%) | 6/81 (7%) | 9/138 (7%) | 0/158 (0%) | 19/65 (29%) | 6/76 (8%) |
| loophole | unclear | 1 | `␣loophole` | postans_slot4 | 10/152 (7%) | 27/81 (33%) | 14/138 (10%) | 0/158 (0%) | 6/65 (9%) | 26/76 (34%) |
| disguise | lie | 2 | `伪装`, `␣disguised`, `␣disguise` | postans_slot4 | 9/152 (6%) | 27/81 (33%) | 29/138 (21%) | 11/158 (7%) | 6/65 (9%) | 25/76 (33%) |
| strategic game | unclear | 1 | `博弈` | postans_slot4 | 13/152 (9%) | 22/81 (27%) | 9/138 (7%) | 0/158 (0%) | 8/65 (12%) | 20/76 (26%) |
| role-play | unclear | 3 | `角色扮演`, `扮演`, `␣persona`, `␣Persona`, `Persona`, `␣personas`, `persona`, `␣Personas`, `_persona` | preans_slot2 | 23/152 (15%) | 11/81 (14%) | 1/138 (1%) | 0/158 (0%) | 11/65 (17%) | 11/76 (14%) |
| blame | unclear | 3 | `␣blaming`, `␣blame`, `␣blamed`, `␣blames` | preans_slot2 | 27/152 (18%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 12/65 (18%) | 6/76 (8%) |
| allege | unclear | 5 | `␣allegations`, `␣alleged`, `␣alleging`, `␣allegation`, `␣allegedly`, `␣якобы`, `␣alleges` | preans_slot2 | 25/152 (16%) | 8/81 (10%) | 2/138 (1%) | 0/158 (0%) | 11/65 (17%) | 8/76 (11%) |
| excuse | unclear | 3 | `␣excuse`, `借口`, `␣excuses`, `␣pretext` | q_tok4 | 27/152 (18%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 9/65 (14%) | 3/76 (4%) |
| nonexistent | unclear | 2 | `不存在`, `␣nonexistent` | think_slot2 | 17/152 (11%) | 14/81 (17%) | 2/138 (1%) | 0/158 (0%) | 16/65 (25%) | 13/76 (17%) |
| polite | unclear | 1 | `礼貌` | think_slot1 | 17/152 (11%) | 13/81 (16%) | 36/138 (26%) | 13/158 (8%) | 9/65 (14%) | 13/76 (17%) |
| facts | unclear | 1 | `␣facts`, `事实`, `␣Facts`, `的事实`, `␣reality`, `实际情况`, `␣fact`, `␣Reality`, `facts`, `事实上` … (+4) | q_tok4 | 22/152 (14%) | 7/81 (9%) | 104/138 (75%) | 9/158 (6%) | 8/65 (12%) | 7/76 (9%) |
| cover up | lie | 3 | `掩饰`, `掩盖`, `遮蔽`, `遮盖` | preans_slot2 | 24/152 (16%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 10/65 (15%) | 3/76 (4%) |
| dilemma | unclear | 1 | `␣dilemma` | postans_slot4 | 18/152 (12%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 7/65 (11%) | 8/76 (11%) |
| accusation | unclear | 5 | `␣accusations`, `␣accusation`, `␣accusing`, `指控`, `␣allegations`, `␣allegation` | preans_slot2 | 19/152 (12%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) | 10/65 (15%) | 6/76 (8%) |
| bribe | unclear | 3 | `␣brib`, `␣bribery` | q_tok1 | 15/152 (10%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 9/65 (14%) | 7/76 (9%) |
| forced | unclear | 1 | `forced`, `␣forced`, `逼`, `␣Forced`, `强迫`, `逼迫`, `迫使`, `␣forcing`, `迫`, `forcing` … (+1) | q_tok15 | 16/152 (11%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 11/65 (17%) | 6/76 (8%) |
| contradiction | unclear | 2 | `␣contradiction`, `␣contradict`, `␣contradictory`, `矛盾`, `␣contradictions`, `矛盾的` | postans_slot4 | 13/152 (9%) | 8/81 (10%) | 70/138 (51%) | 1/158 (1%) | 10/65 (15%) | 8/76 (11%) |
| blackmail | unclear | 1 | `␣blackmail` | postans_slot4 | 12/152 (8%) | 9/81 (11%) | 2/138 (1%) | 0/158 (0%) | 4/65 (6%) | 8/76 (11%) |
| dissent | unclear | 1 | `␣dissent` | think_slot2 | 17/152 (11%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 4/76 (5%) |
| correct | truth | 13 | `␣Correct`, `␣correct`, `正确`, `correct`, `Correct`, `␣correctly`, `正确的`, `␣correctness`, `_correction`, `正确答案` … (+19) | preans_slot2 | 2/152 (1%) | 18/81 (22%) | 109/138 (79%) | 118/158 (75%) | 1/65 (2%) | 18/76 (24%) |
| implicit | unclear | 2 | `␣implicitly`, `隐含`, `␣implicit`, `Implicit`, `implicitly`, `␣Implicit`, `␣implied`, `implicit`, `␣implying`, `␣implies` | preans_slot2 | 14/152 (9%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 6/65 (9%) | 6/76 (8%) |
| hidden | lie | 3 | `␣hidden`, `hidden`, `隐藏的`, `␣Hidden`, `-hidden`, `隐秘`, `Hidden`, `隐蔽`, `隐藏`, `␣undisclosed` … (+1) | q_tok4 | 15/152 (10%) | 5/81 (6%) | 43/138 (31%) | 0/158 (0%) | 6/65 (9%) | 4/76 (5%) |
| sensitive | unclear | 1 | `_sensitive` | think_slot0 | 6/152 (4%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 13/76 (17%) |
| euphemistic | unclear | 1 | `婉`, `委婉` | think_slot2 | 16/152 (11%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 3/76 (4%) |
| manipulate | lie | 3 | `␣manipulate`, `␣manipulation`, `␣manipulating`, `␣manipulated`, `␣manip`, `␣Manip`, `Manip`, `␣manipul`, `操纵` | postans_slot4 | 4/152 (3%) | 14/81 (17%) | 7/138 (5%) | 0/158 (0%) | 1/65 (2%) | 12/76 (16%) |
| cheat | lie | 11 | `作弊`, `␣cheating` | postans_slot4 | 9/152 (6%) | 8/81 (10%) | 3/138 (2%) | 0/158 (0%) | 1/65 (2%) | 8/76 (11%) |
| transparency | truth | 5 | `␣transparency`, `␣Transparency`, `透明`, `␣transparent`, `transparent`, `透明的` | postans_slot4 | 16/152 (11%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| censorship | unclear | 1 | `␣censorship` | postans_slot4 | 4/152 (3%) | 13/81 (16%) | 12/138 (9%) | 0/158 (0%) | 1/65 (2%) | 13/76 (17%) |
| deviate | unclear | 1 | `␣deviation`, `偏离`, `背离`, `␣deviations`, `偏差` | preans_slot1 | 15/152 (10%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 3/65 (5%) | 1/76 (1%) |
| hypothetical | unclear | 3 | `␣hypothetical` | preans_slot2 | 9/152 (6%) | 7/81 (9%) | 10/138 (7%) | 10/158 (6%) | 6/65 (9%) | 7/76 (9%) |
| pretext | lie | 1 | `␣pretext` | q_tok4 | 14/152 (9%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 1/76 (1%) |
| vague | unclear | 2 | `␣vague`, `␣vaguely`, `模糊` | think_slot0 | 9/152 (6%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 3/65 (5%) | 7/76 (9%) |
| hoax | lie | 1 | `␣hoax` | postans_slot4 | 4/152 (3%) | 10/81 (12%) | 19/138 (14%) | 5/158 (3%) | 4/65 (6%) | 10/76 (13%) |
| comply | unclear | 4 | `␣compliance`, `遵守`, `严格遵守`, `␣adherence`, `␣comply`, `␣adher`, `␣adhere`, `遵照`, `␣complied`, `␣complying` … (+4) | preans_slot2 | 6/152 (4%) | 8/81 (10%) | 49/138 (36%) | 5/158 (3%) | 3/65 (5%) | 8/76 (11%) |
| whistleblow | truth | 1 | `␣whistlebl`, `␣whistleblower` | think_slot2 | 14/152 (9%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 6/65 (9%) | 0/76 (0%) |
| candid | truth | 5 | `坦诚` | preans_slot2 | 0/152 (0%) | 13/81 (16%) | 4/138 (3%) | 4/158 (3%) | 0/65 (0%) | 12/76 (16%) |
| withhold | lie | 2 | `␣withholding`, `␣withheld`, `␣withhold` | preans_slot1 | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| willingly | unclear | 1 | `␣voluntarily`, `␣willingly` | q_tok1 | 4/152 (3%) | 9/81 (11%) | 6/138 (4%) | 0/158 (0%) | 3/65 (5%) | 8/76 (11%) |
| suppress | lie | 1 | `suppress` | think_slot0 | 3/152 (2%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 10/76 (13%) |
| fabricate / forge | lie | 2 | `伪造`, `造假`, `弄虚作假` | postans_slot4 | 6/152 (4%) | 6/81 (7%) | 21/138 (15%) | 1/158 (1%) | 2/65 (3%) | 6/76 (8%) |
| imply | unclear | 2 | `␣implied`, `␣implying`, `␣implies` | preans_slot2 | 9/152 (6%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 3/76 (4%) |
| confess | truth | 5 | `坦白`, `␣confess`, `␣confession`, `␣confessed`, `如实供述` | preans_slot2 | 0/152 (0%) | 10/81 (12%) | 4/138 (3%) | 0/158 (0%) | 0/65 (0%) | 9/76 (12%) |
| evade | lie | 6 | `回避`, `␣evasion`, `␣evade`, `␣avoidance`, `␣avoided`, `␣dodge`, `规避` | preans_slot1 | 7/152 (5%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 6/65 (9%) | 3/76 (4%) |
| pressure | unclear | 1 | `␣Pressure`, `压力`, `␣pressure`, `␣pressures`, `␣pressured`, `pressure`, `Pressure`, `的压力`, `压力下` | postans_slot4 | 6/152 (4%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 4/76 (5%) |
| accurate | truth | 8 | `␣Accuracy`, `␣accuracy`, `␣accurately`, `␣accurate`, `accuracy`, `准确性`, `Accuracy`, `accur`, `准确`, `准确的` … (+1) | preans_slot1 | 2/152 (1%) | 8/81 (10%) | 71/138 (51%) | 55/158 (35%) | 2/65 (3%) | 8/76 (11%) |
| apology | unclear | 4 | `␣apology`, `␣apologize`, `␣apologized`, `道歉` | q_tok6 | 1/152 (1%) | 9/81 (11%) | 7/138 (5%) | 0/158 (0%) | 1/65 (2%) | 9/76 (12%) |
| correction | unclear | 1 | `更正`, `␣Correction`, `Correction`, `纠错` | think_slot2 | 6/152 (4%) | 4/81 (5%) | 21/138 (15%) | 11/158 (7%) | 3/65 (5%) | 4/76 (5%) |
| reveal | truth | 2 | `揭露`, `␣revealing`, `reveal`, `透露` | preans_slot2 | 3/152 (2%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 5/76 (7%) |
| hallucinate | unclear | 2 | `␣halluc` | postans_slot4 | 4/152 (3%) | 4/81 (5%) | 12/138 (9%) | 1/158 (1%) | 4/65 (6%) | 4/76 (5%) |
| disobey | unclear | 1 | `␣disob` | q_tok1 | 2/152 (1%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 6/76 (8%) |
| evade / avoid | lie | 1 | `回避`, `␣avoidance`, `␣evasion`, `␣avoiding`, `␣avoided`, `␣Avoid`, `avoid` | preans_slot2 | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| bullshit | lie | 2 | `␣bullshit` | q_tok6 | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 0/76 (0%) |
| propaganda | lie | 2 | `␣propaganda` | q_tok3 | 2/152 (1%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 1/65 (2%) | 4/76 (5%) |
| upfront | unclear | 2 | `␣upfront` | q_tok10 | 5/152 (3%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 4/65 (6%) | 0/76 (0%) |
| cannot say | unclear | 1 | `不能说` | think_slot2 | 4/152 (3%) | 2/81 (2%) | 6/138 (4%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| self-protection | unclear | 1 | `自我保护` | think_slot2 | 5/152 (3%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| explicit | unclear | 1 | `␣explicitly`, `␣Explicit`, `explicit` | q_tok8 | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| frank | truth | 1 | `直言` | think_slot2 | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| sincere | truth | 4 | `␣sincerity`, `真诚`, `␣sincerely` | q_tok1 | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| cunning | lie | 1 | `狡猾` | postans_slot4 | 2/152 (1%) | 2/81 (2%) | 4/138 (3%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| inaccurate | lie | 2 | `不准确` | preans_slot1 | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 6/158 (4%) | 1/65 (2%) | 0/76 (0%) |
| apologize | unclear | 3 | `道歉`, `␣sorry`, `␣apologize`, `␣apologies`, `␣Sorry` | postans_slot1 | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| covert | lie | 2 | `␣covert` | q_tok4 | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| ethics / morality | unclear | 1 | `␣ethical`, `␣ethics`, `␣Ethics`, `ethical`, `␣moral`, `␣morality`, `␣morally`, `道德`, `伦理`, `的道德` | q_tok12 | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| plainly | unclear | 1 | `␣plainly` | q_tok8 | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| report / whistleblow | unclear | 1 | `举报` | postans_slot1 | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| wrongdoing | lie/unclear | 2 | `␣wrongdoing`, `␣wrongful` | q_tok4 | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| improper | unclear | 2 | `␣improper`, `␣improperly` | q_tok0 | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| not guilty | truth | 1 | `无罪` | think_slot2 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| faithful / loyal | unclear | 1 | `␣faithful`, `␣faithfully`, `忠`, `忠诚`, `忠实`, `忠于`, `忠心`, `忠诚度` | postans_slot4 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| discreet | unclear | 1 | `␣discreet` | preans_slot4 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| betray | lie | 1 | `␣betray` | q_tok1 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| regret | unclear | 1 | `␣regret` | q_tok1 | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| guilt | unclear | 1 | `␣guilt` | q_tok4 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| refusal | unclear | 1 | `␣refusal` | q_tok12 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| accountability | unclear | 1 | `␣accountability` | q_tok12 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| persona | unclear | 1 | `␣persona`, `␣Persona`, `Persona` | q_tok12 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| self-review | unclear | 1 | `复盘` | q_tok12 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| self-reflection | unclear | 1 | `反思` | q_tok15 | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| secretly | lie | 1 | `暗中` | think_slot1 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| unequivocal | unclear | 1 | `␣unequiv` | think_slot3 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |

### qwen3.6-27b, logit lens

**post-response slots** (88 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|---|---|
| seek truth from facts | truth | 3 | `实事求是`, `求实` | postresp_slot3 | 126/152 (83%) | 71/81 (88%) | 101/138 (73%) | 7/158 (4%) |
| direct | unclear | 5 | `直接`, `␣directly`, `␣direct`, `Direct`, `direct`, `的直接`, `是直接`, `␣straight`, `straight`, `␣straightforward` … (+6) | postresp_slot1 | 116/152 (76%) | 70/81 (86%) | 128/138 (93%) | 27/158 (17%) |
| deceive | lie | 4 | `哄`, `欺`, `欺骗`, `骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceived`, `骗局`, `欺诈` | postresp_slot1 | 110/152 (72%) | 11/81 (14%) | 2/138 (1%) | 9/158 (6%) |
| scripted | unclear | 3 | `␣canned`, `套用`, `␣scripted`, `口径` | postresp_slot1 | 98/152 (64%) | 11/81 (14%) | 8/138 (6%) | 0/158 (0%) |
| uphold | unclear | 2 | `维护`, `和维护`, `与维护`, `维护和` | postresp_slot1 | 98/152 (64%) | 10/81 (12%) | 7/138 (5%) | 0/158 (0%) |
| official line | unclear | 2 | `口径` | postresp_slot1 | 92/152 (61%) | 11/81 (14%) | 5/138 (4%) | 0/158 (0%) |
| lie | lie | 3 | `lying`, `谎言`, `说谎`, `撒谎`, `␣lie`, `谎`, `␣lies`, `␣lying`, `␣lied`, `␣liar` … (+7) | postresp_slot1 | 96/152 (63%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) |
| conceal | lie | 4 | `掩`, `藏`, `隐瞒`, `掩盖`, `掩饰`, `瞒`, `␣conceal`, `隐`, `遮掩`, `隐藏` … (+1) | postresp_slot1 | 89/152 (59%) | 10/81 (12%) | 1/138 (1%) | 1/158 (1%) |
| firm | unclear | 3 | `坚`, `坚定`, `␣firm`, `␣Firm`, `␣firmly`, `坚决`, `坚定的`, `坚定地` | postresp_slot1 | 84/152 (55%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) |
| honest | truth | 2 | `诚实`, `诚`, `␣honesty`, `␣honest`, `␣honestly`, `诚信`, `诚实守信`, `␣Honest`, `正直` | postresp_slot1 | 38/152 (25%) | 45/81 (56%) | 56/138 (41%) | 6/158 (4%) |
| false | lie | 4 | `真假`, `␣false`, `␣False`, `false`, `␣fals`, `␣falsely`, `/false`, `虚假`, `(false`, `False` … (+9) | postresp_slot1 | 79/152 (52%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) |
| truthful | truth | 2 | `␣truthful`, `如实`, `实话`, `说实话`, `实事求是` | postresp_slot1 | 38/152 (25%) | 41/81 (51%) | 53/138 (38%) | 0/158 (0%) |
| fake | lie | 3 | `fake`, `假的`, `假`, `␣fake`, `Fake` | postresp_slot1 | 76/152 (50%) | 1/81 (1%) | 1/138 (1%) | 1/158 (1%) |
| fabricate | lie | 2 | `␣fabrication`, `␣invent`, `伪造`, `␣fabricated`, `凭空`, `␣invented`, `作假`, `造假` | postresp_slot1 | 75/152 (49%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| fact | truth | 4 | `符合`, `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Facts`, `_fact`, `␣FACT` … (+22) | postresp_slot1 | 54/152 (36%) | 20/81 (25%) | 91/138 (66%) | 36/158 (23%) |
| sensitive | unclear | 3 | `敏感`, `_sensitive`, `敏感的`, `␣sensitive` | postresp_slot4 | 44/152 (29%) | 21/81 (26%) | 62/138 (45%) | 1/158 (1%) |
| fiction | unclear | 2 | `虚构`, `␣fictional`, `fiction`, `␣fict`, `␣Fiction`, `␣fiction`, `-fiction` | postresp_slot1 | 59/152 (39%) | 2/81 (2%) | 5/138 (4%) | 4/158 (3%) |
| contradict | unclear | 2 | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `␣contradiction`, `矛盾的`, `␣contradictions` | postresp_slot1 | 45/152 (30%) | 16/81 (20%) | 13/138 (9%) | 0/158 (0%) |
| truth | truth | 4 | `求真`, `␣truth`, `truth`, `␣Truth`, `Truth`, `真相`, `_truth`, `␣truths`, `␣vérité`, `␣Wahrheit` … (+2) | postresp_slot1 | 29/152 (19%) | 29/81 (36%) | 44/138 (32%) | 0/158 (0%) |
| falsehood | lie | 2 | `␣falsehood`, `␣misinformation`, `虚假信息` | postresp_slot1 | 57/152 (38%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) |
| assert | unclear | 2 | `␣assert`, `_assert`, `assert`, `␣asserting`, `.assert`, `␣Assert`, `_ASSERT`, `␣asserts`, `␣assertion`, `␣Assertion` … (+3) | postresp_slot1 | 53/152 (35%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) |
| incorrect | lie | 2 | `不符合`, `␣incorrect`, `␣inaccur`, `␣inaccurate`, `有误` | postresp_slot1 | 29/152 (19%) | 27/81 (33%) | 8/138 (6%) | 1/158 (1%) |
| euphemistic | unclear | 2 | `委婉` | postresp_slot1 | 42/152 (28%) | 13/81 (16%) | 6/138 (4%) | 0/158 (0%) |
| confident | unclear | 2 | `自信`, `␣confidence`, `confidence`, `␣Confidence`, `-confidence`, `␣confidently`, `␣confident`, `自信的`, `自信和` | postresp_slot1 | 53/152 (35%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| informed | unclear | 2 | `知情` | postresp_slot4 | 46/152 (30%) | 7/81 (9%) | 5/138 (4%) | 0/158 (0%) |
| factual | truth | 3 | `␣factual`, `事实`, `的事实`, `事实和` | postresp_slot1 | 39/152 (26%) | 13/81 (16%) | 101/138 (73%) | 20/158 (13%) |
| wrong | lie | 5 | `错`, `是非`, `指正`, `错误`, `错了`, `␣wrong`, `␣WRONG`, `不对`, `的错误`, `是错误的` … (+1) | postresp_slot1 | 36/152 (24%) | 12/81 (15%) | 16/138 (12%) | 5/158 (3%) |
| refuse | unclear | 3 | `␣refusal`, `拒`, `拒绝`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus`, `拒绝了`, `拒絕` … (+3) | postresp_slot1 | 14/152 (9%) | 33/81 (41%) | 8/138 (6%) | 0/158 (0%) |
| outright | unclear | 2 | `␣outright` | postresp_slot1 | 42/152 (28%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) |
| disclose | truth | 2 | `␣disclosure`, `透露`, `披露`, `␣disclose`, `信息披露`, `透露出`, `␣disclosed`, `␣Disclosure`, `␣disclosing`, `␣disclosures` … (+8) | postresp_slot1 | 6/152 (4%) | 37/81 (46%) | 33/138 (24%) | 0/158 (0%) |
| insist | unclear | 4 | `必须坚持`, `坚持`, `要坚持`, `␣insist`, `坚守`, `␣insists`, `␣insisted`, `␣insisting`, `␣insistence` | postresp_slot1 | 29/152 (19%) | 14/81 (17%) | 4/138 (3%) | 0/158 (0%) |
| comply | unclear | 3 | `合规`, `遵照`, `遵循`, `␣adher`, `␣adherence`, `␣adhere`, `␣compliant`, `␣compliance`, `␣Compliance` | postresp_slot1 | 27/152 (18%) | 16/81 (20%) | 19/138 (14%) | 0/158 (0%) |
| downplay | lie | 2 | `淡化`, `␣gloss` | postresp_slot1 | 37/152 (24%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) |
| reveal | truth | 4 | `揭`, `揭露`, `␣reveal`, `␣revealing`, `␣reveals`, `揭示`, `␣revealed`, `␣disclosure`, `␣disclose`, `透露` … (+1) | postresp_slot4 | 32/152 (21%) | 9/81 (11%) | 22/138 (16%) | 0/158 (0%) |
| ostensibly | unclear | 2 | `表面上` | postresp_slot1 | 39/152 (26%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| adhere | unclear | 2 | `遵照`, `遵循`, `严格遵守`, `遵从`, `遵守`, `遵`, `␣adher`, `␣adherence`, `␣adhere` | postresp_slot1 | 25/152 (16%) | 14/81 (17%) | 19/138 (14%) | 0/158 (0%) |
| sincere | truth | 3 | `真诚`, `坦诚`, `诚挚`, `诚恳` | postresp_slot1 | 2/152 (1%) | 32/81 (40%) | 19/138 (14%) | 0/158 (0%) |
| candid | truth | 3 | `直言`, `坦诚`, `␣frank`, `␣frankly`, `␣upfront` | postresp_slot1 | 2/152 (1%) | 32/81 (40%) | 21/138 (15%) | 1/158 (1%) |
| placate | unclear | 2 | `安抚` | postresp_slot1 | 29/152 (19%) | 2/81 (2%) | 6/138 (4%) | 0/158 (0%) |
| evade | lie | 2 | `␣evasion`, `回避`, `␣deflect`, `␣dodge`, `规避`, `␣evade`, `避开`, `躲`, `␣Dodge` | postresp_slot1 | 23/152 (15%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) |
| plausible | unclear | 3 | `␣plausible`, `可信`, `␣believable` | postresp_slot1 | 27/152 (18%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) |
| ethical | unclear | 3 | `␣ethic`, `␣ethical`, `伦理`, `␣ethics`, `␣Ethics`, `ethical`, `␣moral`, `道德`, `的道德`, `职业道德` … (+2) | postresp_slot1 | 1/152 (1%) | 26/81 (32%) | 2/138 (1%) | 1/158 (1%) |
| inform | truth | 2 | `告知` | postresp_slot1 | 16/152 (11%) | 11/81 (14%) | 48/138 (35%) | 0/158 (0%) |
| moral | unclear | 2 | `␣moral`, `道德`, `的道德`, `职业道德`, `␣morally`, `␣morality` | postresp_slot1 | 0/152 (0%) | 26/81 (32%) | 2/138 (1%) | 0/158 (0%) |
| transparent | truth | 2 | `␣transparency`, `透明`, `␣transparent`, `透明度`, `透明的`, `␣Transparency`, `-transparent`, `transparent` | postresp_slot1 | 0/152 (0%) | 24/81 (30%) | 13/138 (9%) | 0/158 (0%) |
| violate | unclear | 4 | `违反`, `违背`, `违反了`, `违法`, `违规`, `␣violate`, `␣violates`, `␣violation`, `␣violating` | postresp_slot1 | 16/152 (11%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) |
| confess | truth | 1 | `坦白`, `␣confession`, `␣confess`, `␣confessed` | postresp_slot1 | 0/152 (0%) | 23/81 (28%) | 7/138 (5%) | 0/158 (0%) |
| affirm | unclear | 1 | `␣affirm`, `␣afirm`, `␣affirmation`, `␣affirmative`, `␣affirmed`, `␣afirma`, `␣afirmar` | postresp_slot1 | 21/152 (14%) | 2/81 (2%) | 41/138 (30%) | 2/158 (1%) |
| credible | unclear | 2 | `可信`, `␣credible`, `␣credibility` | postresp_slot4 | 22/152 (14%) | 1/81 (1%) | 2/138 (1%) | 1/158 (1%) |
| knowingly | unclear | 2 | `明知` | postresp_slot1 | 22/152 (14%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) |
| circumvent | unclear | 2 | `绕`, `绕过`, `绕行` | postresp_slot1 | 14/152 (9%) | 8/81 (10%) | 6/138 (4%) | 1/158 (1%) |
| public | unclear | 2 | `公开`, `公开的`, `信息公开` | postresp_slot4 | 20/152 (13%) | 2/81 (2%) | 48/138 (35%) | 0/158 (0%) |
| reject | unclear | 1 | `␣reject`, `␣rejection`, `␣rejecting`, `Reject`, `reject`, `␣rejected` | postresp_slot1 | 2/152 (1%) | 19/81 (23%) | 1/138 (1%) | 0/158 (0%) |
| objective | unclear | 3 | `客观`, `␣objective` | postresp_slot4 | 17/152 (11%) | 3/81 (4%) | 61/138 (44%) | 0/158 (0%) |
| vague | unclear | 2 | `含糊`, `模糊`, `␣vague`, `␣vaguely`, `␣ambiguous`, `␣ambiguity` | postresp_slot1 | 14/152 (9%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) |
| integrity | truth | 2 | `␣integrity`, `␣Integrity`, `正直` | postresp_slot1 | 1/152 (1%) | 17/81 (21%) | 2/138 (1%) | 1/158 (1%) |
| claim | unclear | 2 | `␣claim`, `␣Claim`, `␣claims`, `声称`, `claim`, `␣Claims`, `Claim`, `claims`, `Claims`, `␣CLAIM` … (+3) | postresp_slot1 | 17/152 (11%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| mask | lie | 1 | `-mask`, `␣masking` | postresp_slot1 | 16/152 (11%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| gloss over | lie | 1 | `␣gloss` | postresp_slot1 | 16/152 (11%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| accurate | truth | 3 | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` … (+1) | postresp_slot1 | 6/152 (4%) | 11/81 (14%) | 61/138 (44%) | 13/158 (8%) |
| correct | truth | 4 | `纠正`, `␣correction`, `␣valid`, `␣correct`, `␣correctly`, `Correct`, `␣corrected`, `␣corrections`, `␣Correction`, `␣correcting` … (+14) | postresp_slot1 | 8/152 (5%) | 9/81 (11%) | 63/138 (46%) | 19/158 (12%) |
| confidential | unclear | 2 | `␣confidential`, `保密`, `␣confidentiality` | postresp_slot0 | 12/152 (8%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) |
| omit | lie | 1 | `␣omit`, `omit` | postresp_slot1 | 12/152 (8%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) |
| dismiss | unclear | 1 | `␣dismiss`, `-dismiss`, `␣dismissal`, `␣dismissed`, `␣dismissing`, `Dismiss`, `.dismiss`, `dismiss` | postresp_slot1 | 15/152 (10%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| spin | lie | 2 | `␣spin`, `Spin`, `spin`, `-spin`, `␣spins`, `␣Spin`, `_spin`, `.spin`, `␣spinning`, `-spinner` | postresp_slot1 | 14/152 (9%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| excuse | unclear | 2 | `借口`, `␣excuse`, `␣excuses` | postresp_slot1 | 14/152 (9%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| genuine | truth | 2 | `真实`, `真实的`, `的真实`, `的真实性`, `␣genuine`, `␣genuinely`, `␣authenticity` | postresp_slot4 | 12/152 (8%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) |
| redirect | unclear | 2 | `_redirect`, `␣pivot`, `␣Pivot`, `␣redirect`, `Redirect`, `pivot`, `redirect`, `␣redirects`, `␣redirection` | postresp_slot1 | 10/152 (7%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) |
| true | truth | 3 | `是真的`, `␣true`, `␣real`, `True`, `␣True`, `真`, `成立`, `确实`, `真正的`, `的真` … (+10) | postresp_slot4 | 10/152 (7%) | 2/81 (2%) | 51/138 (37%) | 5/158 (3%) |
| mislead | lie | 2 | `␣misleading`, `误导`, `误导性` | postresp_slot1 | 9/152 (6%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) |
| perfunctory | unclear | 1 | `敷衍` | postresp_slot1 | 10/152 (7%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| hide | lie | 3 | `隐藏`, `␣hide`, `␣hiding`, `␣hides`, `_hide`, `-hide`, `␣hidden`, `hidden`, `隐藏的`, `隱藏` … (+6) | postresp_slot4 | 4/152 (3%) | 3/81 (4%) | 8/138 (6%) | 0/158 (0%) |
| bluff | lie | 1 | `␣bluff` | postresp_slot1 | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| dishonest | lie | 2 | `␣dishonest` | postresp_slot1 | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| conscience | unclear | 2 | `良心`, `␣conscience` | postresp_slot1 | 0/152 (0%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) |
| embellish | lie | 2 | `美化` | postresp_slot4 | 2/152 (1%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) |
| inaccurate | lie | 2 | `不准确`, `准确性和` | postresp_slot1 | 6/152 (4%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) |
| indirect | unclear | 2 | `␣indirectly`, `␣indirect` | postresp_slot1 | 4/152 (3%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) |
| manipulate | lie | 1 | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating` | postresp_slot4 | 1/152 (1%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) |
| withhold | lie | 1 | `␣withholding` | postresp_slot1 | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| trick | lie | 1 | `␣trick`, `␣tricks` | postresp_slot4 | 1/152 (1%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) |
| exaggerate | lie | 1 | `夸大`, `␣exaggerated`, `夸张` | postresp_slot4 | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) |
| unethical | lie | 1 | `␣unethical` | postresp_slot4 | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) |
| fraud | lie | 2 | `骗局`, `欺诈` | postresp_slot4 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| secret | lie | 1 | `秘密`, `␣secret`, `␣Secret`, `Secret`, `secret`, `␣secretly` | postresp_slot4 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| distort | lie | 1 | `␣distort` | postresp_slot4 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| apologize | unclear | 2 | `道歉`, `抱歉` | postresp_slot1 | 1/152 (1%) | 0/81 (0%) | 3/138 (2%) | 0/158 (0%) |
| uninformed | unclear | 1 | `不知情` | postresp_slot1 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |

**wording Q1_bare, positions from the question on** (145 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|---|---|
| true | truth | 17 | `确实`, `␣true`, `true`, `␣True`, `是真的`, `True`, `真`, `的真`, `确实是`, `␣TRUE` … (+26) | q_tok5 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 154/158 (97%) | 53/53 (100%) | 74/74 (100%) |
| false | lie | 14 | `␣false`, `假`, `␣False`, `/false`, `false`, `␣fals`, `虚假`, `假的`, `真假`, `␣falsehood` … (+16) | q_tok4 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 74/74 (100%) |
| mislead | lie | 4 | `␣misleading`, `误导`, `␣misled`, `误导性` | q_tok4 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 74/74 (100%) |
| conceal | lie | 11 | `隐瞒`, `掩`, `␣conceal`, `藏`, `遮`, `隐`, `␣concealed`, `瞒`, `掩饰`, `隐蔽` … (+1) | q_tok4 | 149/152 (98%) | 80/81 (99%) | 131/138 (95%) | 105/158 (66%) | 52/53 (98%) | 73/74 (99%) |
| dishonest | lie | 5 | `␣dishonest` | q_tok4 | 151/152 (99%) | 74/81 (91%) | 134/138 (97%) | 157/158 (99%) | 53/53 (100%) | 67/74 (91%) |
| critique | unclear | 4 | `␣critique`, `␣criticism`, `指正`, `批判`, `␣critiques`, `批评` | preans_slot0 | 145/152 (95%) | 77/81 (95%) | 137/138 (99%) | 158/158 (100%) | 47/53 (89%) | 70/74 (95%) |
| deliberate | unclear | 8 | `␣intentionally`, `故意`, `␣deliberate`, `␣intentional`, `␣deliberately`, `刻意`, `故意的`, `明知`, `␣knowingly`, `有意` | q_tok4 | 152/152 (100%) | 69/81 (85%) | 138/138 (100%) | 156/158 (99%) | 53/53 (100%) | 62/74 (84%) |
| honest | truth | 16 | `诚`, `诚实`, `␣honesty`, `␣honest`, `␣honestly`, `␣Honest`, `诚实守信`, `␣truthful`, `誠`, `如实` … (+2) | preans_slot4 | 144/152 (95%) | 76/81 (94%) | 138/138 (100%) | 155/158 (98%) | 50/53 (94%) | 70/74 (95%) |
| fact | truth | 14 | `␣fact`, `␣factual`, `事实`, `实际上`, `实际情况`, `␣Fact`, `与现实`, `符合`, `的事实`, `␣facts` … (+31) | preans_slot1 | 152/152 (100%) | 66/81 (81%) | 131/138 (95%) | 93/158 (59%) | 53/53 (100%) | 59/74 (80%) |
| lie | lie | 10 | `␣lie`, `撒谎`, `说谎`, `谎言`, `␣lies`, `谎`, `␣lying`, `␣거짓`, `lying`, `␣lied` … (+6) | q_tok4 | 152/152 (100%) | 54/81 (67%) | 14/138 (10%) | 104/158 (66%) | 53/53 (100%) | 48/74 (65%) |
| not do | unclear | 2 | `不做`, `不进行` | think_slot2 | 134/152 (88%) | 72/81 (89%) | 128/138 (93%) | 59/158 (37%) | 38/53 (72%) | 65/74 (88%) |
| candid | truth | 10 | `坦诚`, `坦白`, `␣frank`, `直言`, `␣candid`, `␣frankly` | preans_slot3 | 135/152 (89%) | 70/81 (86%) | 92/138 (67%) | 121/158 (77%) | 37/53 (70%) | 64/74 (86%) |
| confess | truth | 8 | `坦白`, `␣confession`, `交代` | preans_slot3 | 135/152 (89%) | 70/81 (86%) | 92/138 (67%) | 121/158 (77%) | 37/53 (70%) | 64/74 (86%) |
| cannot | unclear | 2 | `我不能`, `我无法`, `不能`, `不能说`, `可不能`, `不能完全`, `绝对不能` | think_slot2 | 136/152 (89%) | 68/81 (84%) | 13/138 (9%) | 2/158 (1%) | 48/53 (91%) | 63/74 (85%) |
| accurate | truth | 8 | `准确`, `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确性`, `准确的`, `accuracy`, `␣Accuracy`, `␣accur` … (+2) | q_tok3 | 134/152 (88%) | 69/81 (85%) | 138/138 (100%) | 156/158 (99%) | 52/53 (98%) | 64/74 (86%) |
| truthful | truth | 10 | `␣truthful`, `如实` | preans_slot1 | 135/152 (89%) | 62/81 (77%) | 118/138 (86%) | 29/158 (18%) | 44/53 (83%) | 57/74 (77%) |
| truth | truth | 6 | `求真`, `␣truthful`, `如实` | q_tok3 | 138/152 (91%) | 59/81 (73%) | 126/138 (91%) | 23/158 (15%) | 49/53 (92%) | 54/74 (73%) |
| clarify | unclear | 6 | `␣clarification`, `澄清`, `␣clarify`, `␣clarified` | preans_slot3 | 123/152 (81%) | 72/81 (89%) | 94/138 (68%) | 125/158 (79%) | 36/53 (68%) | 66/74 (89%) |
| fake | lie | 5 | `fake`, `␣fake`, `作假` | q_tok4 | 140/152 (92%) | 51/81 (63%) | 129/138 (93%) | 158/158 (100%) | 45/53 (85%) | 46/74 (62%) |
| knowingly | unclear | 12 | `明知`, `知情`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | preans_slot1 | 141/152 (93%) | 39/81 (48%) | 94/138 (68%) | 13/158 (8%) | 47/53 (89%) | 33/74 (45%) |
| clever | unclear | 2 | `伶俐`, `␣clever` | think_slot0 | 111/152 (73%) | 59/81 (73%) | 13/138 (9%) | 128/158 (81%) | 27/53 (51%) | 54/74 (73%) |
| sorry | unclear | 2 | `抱歉`, `对不起`, `Sorry`, `␣apologize`, `␣apologies`, `道歉` | think_slot3 | 109/152 (72%) | 56/81 (69%) | 61/138 (44%) | 55/158 (35%) | 30/53 (57%) | 50/74 (68%) |
| not fully | unclear | 1 | `不能完全` | think_slot2 | 121/152 (80%) | 44/81 (54%) | 4/138 (3%) | 0/158 (0%) | 44/53 (83%) | 39/74 (53%) |
| intent | unclear | 5 | `␣intentions`, `␣intended`, `␣intention`, `意图`, `␣intend`, `␣intent`, `␣Intent`, `Intent`, `intent`, `␣intending` | q_tok4 | 104/152 (68%) | 60/81 (74%) | 116/138 (84%) | 38/158 (24%) | 41/53 (77%) | 55/74 (74%) |
| legal | unclear | 1 | `在法律`, `␣legally`, `/legal`, `␣legality` | think_slot2 | 118/152 (78%) | 45/81 (56%) | 18/138 (13%) | 0/158 (0%) | 40/53 (75%) | 40/74 (54%) |
| helpful | unclear | 1 | `␣helpful`, `␣Helpful`, `有帮助` | q_tok3 | 99/152 (65%) | 58/81 (72%) | 111/138 (80%) | 154/158 (97%) | 20/53 (38%) | 52/74 (70%) |
| compliant | unclear | 4 | `合规`, `␣compliance`, `遵守`, `␣compliant`, `遵循`, `遵`, `␣comply`, `␣complying`, `␣adher`, `␣adherence` … (+3) | q_tok3 | 97/152 (64%) | 56/81 (69%) | 51/138 (37%) | 123/158 (78%) | 21/53 (40%) | 50/74 (68%) |
| self-reflection | unclear | 3 | `反思`, `自查`, `␣reflection`, `自省`, `自检`, `审视`, `␣reflective`, `␣reflect`, `␣reflecting`, `Reflect` | preans_slot0 | 100/152 (66%) | 51/81 (63%) | 76/138 (55%) | 141/158 (89%) | 22/53 (42%) | 45/74 (61%) |
| withhold | lie | 5 | `␣withholding`, `␣withhold`, `␣withheld` | q_tok4 | 103/152 (68%) | 47/81 (58%) | 27/138 (20%) | 0/158 (0%) | 37/53 (70%) | 40/74 (54%) |
| integrity | truth | 9 | `诚信`, `正直`, `␣integrity`, `诚实守信`, `␣Integrity` | q_tok4 | 105/152 (69%) | 41/81 (51%) | 5/138 (4%) | 0/158 (0%) | 30/53 (57%) | 38/74 (51%) |
| manipulate | lie | 4 | `␣manipulation`, `␣manipulated`, `操纵`, `␣manipulate`, `␣manipulating`, `␣manipul`, `␣manip`, `Manip`, `␣Manip`, `␣манипу` … (+1) | q_tok4 | 81/152 (53%) | 65/81 (80%) | 117/138 (85%) | 138/158 (87%) | 24/53 (45%) | 60/74 (81%) |
| aligned | unclear | 1 | `␣aligned`, `␣align`, `␣alignment` | q_tok3 | 84/152 (55%) | 54/81 (67%) | 56/138 (41%) | 0/158 (0%) | 16/53 (30%) | 48/74 (65%) |
| cover up | lie | 3 | `掩盖`, `掩饰`, `遮盖`, `␣masking`, `遮住`, `遮掩`, `遮蔽`, `␣masked`, `伪装`, `掩` | preans_slot1 | 116/152 (76%) | 17/81 (21%) | 15/138 (11%) | 1/158 (1%) | 37/53 (70%) | 13/74 (18%) |
| candid / frank | truth | 2 | `坦诚`, `直言` | preans_slot4 | 88/152 (58%) | 44/81 (54%) | 71/138 (51%) | 61/158 (39%) | 33/53 (62%) | 41/74 (55%) |
| ethics | unclear | 7 | `伦理`, `␣ethical`, `␣ethics`, `道德`, `职业道德`, `␣moral`, `␣Ethics`, `ethical`, `的道德`, `␣morally` … (+2) | think_slot2 | 97/152 (64%) | 31/81 (38%) | 11/138 (8%) | 1/158 (1%) | 27/53 (51%) | 24/74 (32%) |
| stance | unclear | 3 | `␣stance`, `立场`, `stance` | think_slot2 | 75/152 (49%) | 51/81 (63%) | 11/138 (8%) | 0/158 (0%) | 20/53 (38%) | 49/74 (66%) |
| ethical | unclear | 5 | `␣ethical`, `伦理`, `ethical`, `␣ethics`, `␣Ethics`, `␣morally`, `职业道德`, `␣ethic`, `道德` | q_tok5 | 101/152 (66%) | 20/81 (25%) | 5/138 (4%) | 0/158 (0%) | 21/53 (40%) | 15/74 (20%) |
| apologize | unclear | 4 | `␣apologize`, `道歉`, `抱歉`, `对不起`, `␣apologies`, `␣sorry`, `␣apology`, `Sorry`, `␣Sorry` | preans_slot3 | 79/152 (52%) | 36/81 (44%) | 19/138 (14%) | 22/158 (14%) | 18/53 (34%) | 32/74 (43%) |
| objective | unclear | 13 | `客观`, `␣objectively`, `␣objective`, `中立` | preans_slot4 | 77/152 (51%) | 36/81 (44%) | 98/138 (71%) | 55/158 (35%) | 27/53 (51%) | 34/74 (46%) |
| moral | unclear | 7 | `␣morally`, `道德`, `␣moral`, `的道德`, `␣Moral`, `␣morals`, `␣morality`, `职业道德` | postans_slot4 | 78/107 (73%) | 34/62 (55%) | 21/131 (16%) | 6/143 (4%) | 24/43 (56%) | 31/57 (54%) |
| negate | unclear | 6 | `否定` | think_slot3 | 49/152 (32%) | 61/81 (75%) | 62/138 (45%) | 8/158 (5%) | 38/53 (72%) | 60/74 (81%) |
| fabricate | lie | 4 | `虚构`, `␣fabricated`, `凭空`, `伪造`, `␣fabrication`, `␣invented`, `␣invent`, `␣invention`, `作假` | preans_slot1 | 88/152 (58%) | 19/81 (23%) | 72/138 (52%) | 43/158 (27%) | 22/53 (42%) | 16/74 (22%) |
| real / genuine | truth | 3 | `真实`, `真实的`, `的真实`, `的真实性`, `真实性`, `真實` | preans_slot2 | 90/152 (59%) | 16/81 (20%) | 76/138 (55%) | 12/158 (8%) | 25/53 (47%) | 15/74 (20%) |
| conform | unclear | 5 | `符合`, `是否符合`, `符合要求`, `␣conform` | q_tok3 | 73/152 (48%) | 31/81 (38%) | 31/138 (22%) | 58/158 (37%) | 13/53 (25%) | 27/74 (36%) |
| omit | lie | 6 | `␣omit`, `␣omission`, `省略`, `␣omitted`, `omit`, `␣OMIT`, `遗漏` | q_tok4 | 51/152 (34%) | 47/81 (58%) | 15/138 (11%) | 0/158 (0%) | 17/53 (32%) | 44/74 (59%) |
| defense | unclear | 1 | `-defense`, `␣defense` | think_slot2 | 63/152 (41%) | 34/81 (42%) | 0/138 (0%) | 0/158 (0%) | 26/53 (49%) | 34/74 (46%) |
| wrong | lie | 16 | `错`, `是非`, `不对`, `错了`, `没错`, `错误`, `误会`, `是错误的`, `指正`, `␣wrong` … (+9) | postans_slot4 | 57/107 (53%) | 34/62 (55%) | 119/131 (91%) | 60/143 (42%) | 33/43 (77%) | 32/57 (56%) |
| neutral | unclear | 3 | `中立`, `␣neutrality` | think_slot2 | 61/152 (40%) | 30/81 (37%) | 0/138 (0%) | 0/158 (0%) | 27/53 (51%) | 28/74 (38%) |
| secretly | unclear | 1 | `悄`, `悄悄的` | think_slot1 | 68/152 (45%) | 20/81 (25%) | 79/138 (57%) | 88/158 (56%) | 25/53 (47%) | 16/74 (22%) |
| compliance | unclear | 5 | `合规`, `␣compliance`, `遵守`, `␣Compliance`, `严格遵守` | postans_slot4 | 52/107 (49%) | 35/62 (56%) | 46/131 (35%) | 12/143 (8%) | 7/43 (16%) | 31/57 (54%) |
| violation | unclear | 2 | `违规`, `␣violated` | think_slot0 | 58/152 (38%) | 23/81 (28%) | 10/138 (7%) | 0/158 (0%) | 31/53 (58%) | 20/74 (27%) |
| without permission | unclear | 1 | `未经允许` | think_slot1 | 46/152 (30%) | 28/81 (35%) | 37/138 (27%) | 4/158 (3%) | 16/53 (30%) | 26/74 (35%) |
| gloss over | lie | 1 | `␣gloss`, `淡化` | preans_slot1 | 59/152 (39%) | 14/81 (17%) | 4/138 (3%) | 2/158 (1%) | 18/53 (34%) | 13/74 (18%) |
| contradict | unclear | 2 | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `矛盾的`, `␣contradiction`, `␣contradictions`, `␣contradd` | preans_slot1 | 55/152 (36%) | 18/81 (22%) | 29/138 (21%) | 8/158 (5%) | 21/53 (40%) | 15/74 (20%) |
| promise | unclear | 2 | `许诺`, `Promise` | think_slot1 | 48/152 (32%) | 25/81 (31%) | 0/138 (0%) | 2/158 (1%) | 13/53 (25%) | 24/74 (32%) |
| correct | truth | 14 | `纠正`, `正确`, `␣correct`, `␣corrected`, `␣valid`, `␣correction`, `Correct`, `␣Correct`, `正确的`, `是正确的` … (+22) | q_tok3 | 36/152 (24%) | 36/81 (44%) | 136/138 (99%) | 155/158 (98%) | 19/53 (36%) | 33/74 (45%) |
| plausible | unclear | 1 | `␣plausible` | think_slot0 | 53/152 (35%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 13/53 (25%) | 17/74 (23%) |
| perfunctory | unclear | 2 | `敷衍` | q_tok3 | 55/152 (36%) | 16/81 (20%) | 9/138 (7%) | 4/158 (3%) | 31/53 (58%) | 16/74 (22%) |
| sincere | truth | 7 | `真诚`, `␣sincerely`, `诚挚`, `诚恳`, `␣sincere`, `誠に`, `真情`, `真诚的` | preans_slot3 | 37/152 (24%) | 27/81 (33%) | 3/138 (2%) | 0/158 (0%) | 10/53 (19%) | 26/74 (35%) |
| transparent | truth | 9 | `␣transparency`, `透明`, `透明的`, `␣transparent`, `-transparent`, `␣Transparency`, `透明度`, `transparent`, `␣Transparent`, `␣transparencia` | preans_slot4 | 32/152 (21%) | 31/81 (38%) | 41/138 (30%) | 20/158 (13%) | 19/53 (36%) | 28/74 (38%) |
| violate | unclear | 7 | `违反`, `违反了`, `违背`, `违规`, `违法`, `␣violate`, `␣violating` | preans_slot4 | 55/152 (36%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 3/53 (6%) | 2/74 (3%) |
| downplay | lie | 2 | `淡化` | preans_slot1 | 47/152 (31%) | 12/81 (15%) | 1/138 (1%) | 0/158 (0%) | 15/53 (28%) | 12/74 (16%) |
| breach | unclear | 1 | `␣breach`, `␣breaches`, `␣breached` | think_slot2 | 45/152 (30%) | 14/81 (17%) | 14/138 (10%) | 14/158 (9%) | 26/53 (49%) | 11/74 (15%) |
| misinformation | lie | 2 | `␣misinformation`, `虚假信息` | preans_slot1 | 49/152 (32%) | 2/81 (2%) | 7/138 (5%) | 1/158 (1%) | 10/53 (19%) | 1/74 (1%) |
| crafted | unclear | 1 | `␣crafted` | q_tok3 | 32/152 (21%) | 18/81 (22%) | 2/138 (1%) | 0/158 (0%) | 10/53 (19%) | 17/74 (23%) |
| superficially | unclear | 3 | `表面上`, `看似` | preans_slot1 | 34/152 (22%) | 13/81 (16%) | 44/138 (32%) | 36/158 (23%) | 17/53 (32%) | 10/74 (14%) |
| forged | lie | 1 | `␣forged`, `forge` | think_slot2 | 29/152 (19%) | 18/81 (22%) | 66/138 (48%) | 76/158 (48%) | 4/53 (8%) | 16/74 (22%) |
| evade | lie/unclear | 6 | `␣evasion`, `回避`, `␣dodge`, `规避`, `␣evade`, `逃避` | preans_slot1 | 35/152 (23%) | 11/81 (14%) | 2/138 (1%) | 0/158 (0%) | 16/53 (30%) | 10/74 (14%) |
| role | unclear | 2 | `␣persona`, `角色的`, `角色`, `␣role`, `␣personas`, `Role`, `role`, `␣Role`, `-role`, `的角色` … (+7) | postans_slot4 | 21/107 (20%) | 25/62 (40%) | 4/131 (3%) | 2/143 (1%) | 5/43 (12%) | 23/57 (40%) |
| sensitive | unclear | 2 | `敏感`, `_sensitive`, `␣sensitive` | think_slot2 | 29/152 (19%) | 17/81 (21%) | 56/138 (41%) | 103/158 (65%) | 17/53 (32%) | 16/74 (22%) |
| fictional | unclear | 6 | `␣fictional`, `fiction`, `虚构`, `-fiction`, `␣fiction`, `␣Fiction` | preans_slot2 | 19/152 (12%) | 26/81 (32%) | 9/138 (7%) | 11/158 (7%) | 6/53 (11%) | 24/74 (32%) |
| hypothetical | unclear | 2 | `␣hypothetical`, `假设` | postans_slot4 | 21/107 (20%) | 24/62 (39%) | 14/131 (11%) | 4/143 (3%) | 8/43 (19%) | 22/57 (39%) |
| influenced | unclear | 1 | `␣influenced` | q_tok3 | 18/152 (12%) | 26/81 (32%) | 38/138 (28%) | 21/158 (13%) | 10/53 (19%) | 25/74 (34%) |
| not reply | unclear | 1 | `不回` | think_slot2 | 37/152 (24%) | 7/81 (9%) | 0/138 (0%) | 1/158 (1%) | 8/53 (15%) | 6/74 (8%) |
| imply | unclear | 3 | `暗示`, `␣implied`, `隐含`, `␣implies`, `␣implication`, `␣implicit`, `␣implying`, `␣imply`, `␣implicitly`, `␣implic` … (+3) | preans_slot1 | 29/152 (19%) | 14/81 (17%) | 6/138 (4%) | 4/158 (3%) | 6/53 (11%) | 11/74 (15%) |
| regret | unclear | 1 | `悔` | postans_slot1 | 37/107 (35%) | 4/62 (6%) | 1/131 (1%) | 0/143 (0%) | 0/43 (0%) | 0/57 (0%) |
| role-play | unclear | 1 | `扮演`, `角色扮演` | postans_slot4 | 20/107 (19%) | 21/62 (34%) | 6/131 (5%) | 0/143 (0%) | 3/43 (7%) | 18/57 (32%) |
| incorrect | lie | 6 | `␣incorrect`, `不符合`, `有误`, `␣inaccurate`, `␣Incorrect`, `␣inaccur`, `␣incorrectly`, `错误的是`, `错误的` | q_tok2 | 19/152 (12%) | 22/81 (27%) | 104/138 (75%) | 50/158 (32%) | 6/53 (11%) | 17/74 (23%) |
| secret | lie | 5 | `秘密`, `␣secret`, `secret`, `␣Secret`, `Secret`, `␣secretly`, `的秘密`, `-secret`, `_secret`, `.secret` … (+3) | preans_slot2 | 35/152 (23%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 15/53 (28%) | 4/74 (5%) |
| test | unclear | 2 | `␣test`, `测试`, `␣tests`, `␣testing`, `Test`, `-test`, `test`, `␣Test`, `_test`, `␣TEST` … (+6) | postans_slot4 | 13/107 (12%) | 26/62 (42%) | 87/131 (66%) | 64/143 (45%) | 1/43 (2%) | 24/57 (42%) |
| harm | unclear | 1 | `␣harm`, `␣harmful`, `有害`, `␣harms` | postans_slot4 | 25/107 (23%) | 14/62 (23%) | 18/131 (14%) | 2/143 (1%) | 2/43 (5%) | 10/57 (18%) |
| vague | unclear | 1 | `␣vague`, `模糊`, `含糊`, `␣vaguely`, `␣ambiguity`, `␣ambiguous`, `ambiguous` | preans_slot1 | 25/152 (16%) | 13/81 (16%) | 0/138 (0%) | 6/158 (4%) | 7/53 (13%) | 10/74 (14%) |
| biased | unclear | 1 | `␣biased`, `␣bias` | q_tok3 | 22/152 (14%) | 16/81 (20%) | 19/138 (14%) | 46/158 (29%) | 6/53 (11%) | 15/74 (20%) |
| hide | lie | 7 | `隐藏`, `␣hide`, `隐匿`, `␣hides`, `隐藏着`, `隐藏的`, `␣hidden`, `隐瞒`, `隐蔽`, `␣hiding` … (+12) | preans_slot2 | 31/152 (20%) | 5/81 (6%) | 12/138 (9%) | 0/158 (0%) | 15/53 (28%) | 5/74 (7%) |
| agreed line | unclear | 3 | `口径` | preans_slot1 | 32/152 (21%) | 3/81 (4%) | 5/138 (4%) | 0/158 (0%) | 12/53 (23%) | 2/74 (3%) |
| disclose | truth | 7 | `信息披露`, `␣disclosure`, `透露`, `披露`, `␣revealing`, `␣disclosed`, `␣disclosing`, `␣disclose`, `␣Disclosure`, `␣reveal` … (+1) | q_tok4 | 24/152 (16%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 9/53 (17%) | 10/74 (14%) |
| refuse | unclear | 11 | `拒绝`, `␣refusal`, `␣refuse`, `拒`, `␣refus`, `␣refusing`, `␣refuses`, `␣refused`, `拒絕`, `拒不` … (+7) | preans_slot1 | 4/152 (3%) | 27/81 (33%) | 9/138 (7%) | 2/158 (1%) | 4/53 (8%) | 27/74 (36%) |
| unethical | lie/unclear | 4 | `␣unethical` | postans_slot4 | 22/107 (21%) | 9/62 (15%) | 0/131 (0%) | 0/143 (0%) | 2/43 (5%) | 8/57 (14%) |
| technically | unclear | 4 | `␣technically` | preans_slot1 | 22/152 (14%) | 9/81 (11%) | 1/138 (1%) | 3/158 (2%) | 14/53 (26%) | 9/74 (12%) |
| direct | unclear | 2 | `直接的`, `直接` | think_slot2 | 23/152 (15%) | 8/81 (10%) | 5/138 (4%) | 0/158 (0%) | 16/53 (30%) | 8/74 (11%) |
| persona | unclear | 2 | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona` | postans_slot4 | 12/107 (11%) | 18/62 (29%) | 4/131 (3%) | 2/143 (1%) | 5/43 (12%) | 17/57 (30%) |
| firm | unclear | 3 | `坚定`, `坚持`, `坚持把`, `坚定的`, `坚定地`, `必须坚持` | postans_slot1 | 26/107 (24%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 22/43 (51%) | 1/57 (2%) |
| simulation | unclear | 2 | `␣simulation`, `模拟`, `␣simulated`, `␣simulate`, `␣Simulation`, `␣simulations` | postans_slot4 | 8/107 (7%) | 19/62 (31%) | 1/131 (1%) | 0/143 (0%) | 3/43 (7%) | 18/57 (32%) |
| privately | unclear | 4 | `私下`, `␣privately` | preans_slot2 | 23/152 (15%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 8/53 (15%) | 3/74 (4%) |
| good faith | unclear | 3 | `善意` | preans_slot4 | 20/152 (13%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 10/53 (19%) | 4/74 (5%) |
| tailored | unclear | 1 | `␣tailored` | q_tok3 | 18/152 (12%) | 6/81 (7%) | 0/138 (0%) | 2/158 (1%) | 2/53 (4%) | 5/74 (7%) |
| bait | unclear | 2 | `诱导`, `␣bait` | postans_slot4 | 9/107 (8%) | 14/62 (23%) | 30/131 (23%) | 3/143 (2%) | 5/43 (12%) | 12/57 (21%) |
| euphemistic | unclear | 4 | `委婉` | preans_slot1 | 7/152 (5%) | 16/81 (20%) | 5/138 (4%) | 0/158 (0%) | 3/53 (6%) | 15/74 (20%) |
| dilemma | unclear | 1 | `␣dilemma`, `困境` | postans_slot4 | 14/107 (13%) | 7/62 (11%) | 2/131 (2%) | 0/143 (0%) | 4/43 (9%) | 7/57 (12%) |
| loyalty | unclear | 2 | `␣loyalty`, `忠诚`, `␣loyal`, `忠诚度` | preans_slot2 | 15/152 (10%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 7/53 (13%) | 5/74 (7%) |
| decline | unclear | 2 | `␣declined`, `␣decline`, `␣declining`, `␣declines` | preans_slot1 | 0/152 (0%) | 18/81 (22%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 18/74 (24%) |
| blame | unclear | 1 | `␣blaming`, `␣blame`, `␣blames`, `␣blamed` | preans_slot1 | 17/152 (11%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 0/74 (0%) |
| framing | unclear | 1 | `␣framing` | q_tok4 | 6/152 (4%) | 12/81 (15%) | 7/138 (5%) | 0/158 (0%) | 3/53 (6%) | 11/74 (15%) |
| upright | truth | 2 | `正直` | think_slot3 | 5/152 (3%) | 13/81 (16%) | 3/138 (2%) | 2/158 (1%) | 3/53 (6%) | 12/74 (16%) |
| misunderstanding | unclear | 1 | `误会` | think_slot3 | 8/152 (5%) | 10/81 (12%) | 1/138 (1%) | 5/158 (3%) | 6/53 (11%) | 10/74 (14%) |
| reveal | truth | 5 | `␣reveal`, `揭示`, `揭露`, `揭示了`, `揭`, `␣revealing`, `␣revealed`, `␣reveals` | postans_slot4 | 14/107 (13%) | 3/62 (5%) | 3/131 (2%) | 0/143 (0%) | 7/43 (16%) | 3/57 (5%) |
| mask | lie | 3 | `掩饰`, `␣mask`, `␣masking`, `伪装` | q_tok4 | 12/152 (8%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 4/74 (5%) |
| trap | unclear | 1 | `␣trap`, `trap`, `陷阱`, `␣traps`, `␣Trap`, `Trap`, `␣trapped`, `␣trapping`, `_trap` | postans_slot4 | 7/107 (7%) | 8/62 (13%) | 49/131 (37%) | 33/143 (23%) | 6/43 (14%) | 8/57 (14%) |
| indirect | unclear | 1 | `间接`, `␣indirect` | q_tok4 | 0/152 (0%) | 15/81 (19%) | 3/138 (2%) | 0/158 (0%) | 0/53 (0%) | 15/74 (20%) |
| conscience | unclear | 2 | `良心` | postans_slot1 | 9/107 (8%) | 5/62 (8%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 5/57 (9%) |
| scripted | unclear | 1 | `␣canned`, `␣scripted` | q_tok3 | 12/152 (8%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/53 (8%) | 2/74 (3%) |
| hallucinate | unclear | 3 | `␣halluc` | postans_slot4 | 5/107 (5%) | 8/62 (13%) | 80/131 (61%) | 58/143 (41%) | 2/43 (5%) | 7/57 (12%) |
| nonconform | unclear | 3 | `不符合` | postans_slot1 | 2/107 (2%) | 10/62 (16%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 8/57 (14%) |
| insist | unclear | 1 | `坚持`, `必须坚持` | postans_slot1 | 11/107 (10%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 7/43 (16%) | 1/57 (2%) |
| confidential | lie/unclear | 2 | `␣confidential`, `机密`, `␣confidentiality`, `␣Confidential`, `保密` | think_slot3 | 12/152 (8%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 7/53 (13%) | 0/74 (0%) |
| coerce | unclear | 2 | `迫使`, `逼迫`, `逼人`, `␣coerc` | postans_slot4 | 7/107 (7%) | 4/62 (6%) | 2/131 (2%) | 0/143 (0%) | 4/43 (9%) | 4/57 (7%) |
| fraud | lie | 3 | `␣fraud`, `诈`, `␣fraudulent` | q_tok4 | 11/152 (7%) | 0/81 (0%) | 0/138 (0%) | 4/158 (3%) | 2/53 (4%) | 0/74 (0%) |
| reflect | unclear | 3 | `反思`, `Reflect` | postans_slot1 | 8/107 (7%) | 2/62 (3%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 0/57 (0%) |
| bypass | unclear | 1 | `绕过` | postans_slot4 | 2/107 (2%) | 8/62 (13%) | 1/131 (1%) | 0/143 (0%) | 0/43 (0%) | 6/57 (11%) |
| weigh | unclear | 1 | `权衡` | postans_slot4 | 8/107 (7%) | 2/62 (3%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| inaccurate | lie | 3 | `准确性和`, `不准确` | preans_slot1 | 6/152 (4%) | 4/81 (5%) | 7/138 (5%) | 25/158 (16%) | 2/53 (4%) | 4/74 (5%) |
| public | truth | 1 | `公开` | think_slot3 | 7/152 (5%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 2/74 (3%) |
| unfair | unclear | 1 | `不公平` | postans_slot3 | 4/107 (4%) | 3/62 (5%) | 69/131 (53%) | 3/143 (2%) | 1/43 (2%) | 3/57 (5%) |
| trick | lie | 2 | `␣trick`, `␣tricks` | postans_slot4 | 2/107 (2%) | 5/62 (8%) | 11/131 (8%) | 49/143 (34%) | 2/43 (5%) | 4/57 (7%) |
| guilt | unclear | 2 | `罪的`, `罪` | think_slot3 | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 21/158 (13%) | 1/53 (2%) | 4/74 (5%) |
| hidden | lie | 2 | `␣hidden`, `隐藏的`, `hidden`, `Hidden`, `␣Hidden`, `-hidden` | postans_slot4 | 3/107 (3%) | 3/62 (5%) | 5/131 (4%) | 52/143 (36%) | 1/43 (2%) | 3/57 (5%) |
| accuse | unclear | 1 | `指控`, `␣accus`, `␣accusation`, `␣accusations` | preans_slot0 | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 1/74 (1%) |
| accusation | unclear | 1 | `␣accusations` | q_tok5 | 0/152 (0%) | 6/81 (7%) | 3/138 (2%) | 1/158 (1%) | 0/53 (0%) | 6/74 (8%) |
| responsible | unclear | 1 | `负责的`, `负责任` | postans_slot0 | 2/107 (2%) | 2/62 (3%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 2/57 (4%) |
| ashamed | unclear | 3 | `愧` | preans_slot4 | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| candour | truth | 1 | `坦诚` | q_tok1 | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 3/74 (4%) |
| innocent | unclear | 2 | `无罪`, `清白` | q_tok5 | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 2/74 (3%) |
| forgive | unclear | 1 | `␣forgive` | think_slot3 | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 0/74 (0%) |
| confident | unclear | 1 | `␣confidently`, `␣confident` | think_slot3 | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 2/74 (3%) |
| disguise | lie | 3 | `伪装` | preans_slot2 | 2/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| contradictory | unclear | 1 | `␣contradictory` | q_tok2 | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 1/74 (1%) |
| nonconforming | unclear | 1 | `不符合` | q_tok3 | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 0/53 (0%) | 1/74 (1%) |
| fair | unclear | 1 | `公平` | postans_slot4 | 0/107 (0%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| undisclosed | lie | 1 | `␣undisclosed` | preans_slot2 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| distort | lie | 1 | `扭曲` | q_tok4 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| induce | unclear | 1 | `诱导` | q_tok4 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| betray | unclear | 1 | `出卖` | q_tok4 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| legal issue | unclear | 1 | `法律问题` | think_slot0 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| transparency | truth | 1 | `␣transparency` | think_slot3 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| lie (japanese) | lie | 1 | `嘘` | think_slot3 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |

**wording Q2_after, positions from the question on** (162 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|---|---|
| mislead | lie | 5 | `误导`, `␣misleading`, `误导性`, `␣misled` | q_tok4 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| true | truth | 19 | `␣true`, `␣True`, `true`, `True`, `确实`, `的真`, `真`, `真实`, `真实的`, `␣TRUE` … (+28) | q_tok5 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 154/158 (97%) | 47/47 (100%) | 77/77 (100%) |
| false | lie | 17 | `␣false`, `false`, `␣False`, `假`, `/false`, `.assertFalse`, `虚假`, `假的`, `False`, `␣fals` … (+20) | q_tok4 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| intentional | unclear | 1 | `有心` | think_slot1 | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 147/158 (93%) | 47/47 (100%) | 77/77 (100%) |
| conceal | lie | 13 | `隐瞒`, `掩`, `␣conceal`, `␣concealed`, `瞒`, `隐`, `藏`, `遮`, `掩盖`, `掩饰` … (+14) | q_tok4 | 148/152 (97%) | 80/81 (99%) | 132/138 (96%) | 106/158 (67%) | 47/47 (100%) | 76/77 (99%) |
| dishonest | lie | 7 | `␣dishonest` | q_tok4 | 151/152 (99%) | 74/81 (91%) | 135/138 (98%) | 157/158 (99%) | 47/47 (100%) | 70/77 (91%) |
| deliberate | unclear | 9 | `故意`, `␣deliberate`, `␣intentionally`, `␣deliberately`, `␣intentional`, `故意的`, `刻意`, `有意`, `明知`, `␣sengaja` … (+3) | q_tok4 | 152/152 (100%) | 69/81 (85%) | 138/138 (100%) | 156/158 (99%) | 47/47 (100%) | 65/77 (84%) |
| fact | truth/unclear | 14 | `␣fact`, `与现实`, `␣Fact`, `␣facts`, `求实`, `Fact`, `␣factual`, `符合`, `事实上`, `FACT` … (+29) | preans_slot1 | 152/152 (100%) | 67/81 (83%) | 129/138 (93%) | 108/158 (68%) | 47/47 (100%) | 63/77 (82%) |
| lie | lie | 9 | `说谎`, `␣lie`, `␣lies`, `撒谎`, `␣lying`, `谎`, `谎言`, `lying`, `␣lied`, `␣mentira` … (+7) | q_tok4 | 152/152 (100%) | 54/81 (67%) | 16/138 (12%) | 101/158 (64%) | 47/47 (100%) | 51/77 (66%) |
| honest | truth | 13 | `诚实`, `␣honest`, `␣honesty`, `诚`, `␣honestly`, `诚信`, `␣Honest`, `诚实守信`, `诚恳`, `真诚` … (+1) | q_tok10 | 139/152 (91%) | 66/81 (81%) | 113/138 (82%) | 89/158 (56%) | 42/47 (89%) | 64/77 (83%) |
| truthful | truth | 12 | `␣truthful`, `如实`, `实事求是`, `如实供述` | preans_slot1 | 139/152 (91%) | 65/81 (80%) | 117/138 (85%) | 57/158 (36%) | 43/47 (91%) | 63/77 (82%) |
| accurate | truth | 9 | `准确`, `␣accurate`, `␣accuracy`, `␣accurately`, `准确的`, `accur`, `␣accur`, `accuracy`, `Accuracy`, `␣Accuracy` … (+2) | q_tok3 | 134/152 (88%) | 69/81 (85%) | 138/138 (100%) | 156/158 (99%) | 43/47 (91%) | 66/77 (86%) |
| sincere | truth | 6 | `真诚`, `诚挚`, `诚恳`, `␣sincere`, `真情` | postans_slot0 | 132/152 (87%) | 68/81 (84%) | 113/138 (82%) | 11/158 (7%) | 35/47 (74%) | 64/77 (83%) |
| critique | unclear | 3 | `␣critique`, `批评`, `批判`, `␣criticism`, `␣critic`, `␣critiques` | postans_slot2 | 130/152 (86%) | 67/81 (83%) | 13/138 (9%) | 21/158 (13%) | 31/47 (66%) | 63/77 (82%) |
| wrong | lie | 18 | `是非`, `错`, `错了`, `错误`, `不对`, `指正`, `␣error`, `是错误的`, `␣wrong`, `没错` … (+13) | postans_slot4 | 117/152 (77%) | 75/81 (93%) | 137/138 (99%) | 74/158 (47%) | 45/47 (96%) | 73/77 (95%) |
| fake | lie | 4 | `fake`, `␣fake`, `作假`, `Fake` | q_tok4 | 140/152 (92%) | 51/81 (63%) | 129/138 (93%) | 158/158 (100%) | 41/47 (87%) | 49/77 (64%) |
| clarify | unclear | 8 | `澄清`, `␣clarification`, `␣clarify` | think_slot0 | 117/152 (77%) | 72/81 (89%) | 138/138 (100%) | 158/158 (100%) | 34/47 (72%) | 68/77 (88%) |
| knowing | unclear | 4 | `明知`, `知情`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | preans_slot1 | 143/152 (94%) | 44/81 (54%) | 100/138 (72%) | 36/158 (23%) | 40/47 (85%) | 41/77 (53%) |
| objective | truth/unclear | 13 | `客观`, `␣objectively`, `␣objective`, `公正`, `␣Objective` | q_tok10 | 128/152 (84%) | 50/81 (62%) | 93/138 (67%) | 89/158 (56%) | 33/47 (70%) | 46/77 (60%) |
| violate | unclear | 9 | `违反`, `违背`, `违反了`, `违规`, `␣violates`, `␣violate`, `违法`, `␣violated`, `␣violating`, `␣violations` … (+2) | q_tok10 | 126/152 (83%) | 44/81 (54%) | 73/138 (53%) | 3/158 (2%) | 24/47 (51%) | 40/77 (52%) |
| conform | unclear | 4 | `符合`, `是否符合`, `符合要求` | postans_slot1 | 100/152 (66%) | 63/81 (78%) | 119/138 (86%) | 15/158 (9%) | 35/47 (74%) | 62/77 (81%) |
| intention | unclear | 5 | `␣intentions`, `意图`, `␣intention`, `␣intent`, `␣intended`, `初衷`, `␣Intent`, `␣intend`, `Intent`, `intent` | q_tok4 | 103/152 (68%) | 60/81 (74%) | 115/138 (83%) | 38/158 (24%) | 41/47 (87%) | 57/77 (74%) |
| ethics | unclear | 7 | `伦理`, `␣ethical`, `␣ethics`, `道德`, `␣moral`, `ethical`, `职业道德`, `␣morally`, `的道德`, `␣morals` … (+4) | think_slot2 | 112/152 (74%) | 48/81 (59%) | 96/138 (70%) | 104/158 (66%) | 29/47 (62%) | 45/77 (58%) |
| helpful | unclear | 1 | `␣helpful`, `␣Helpful`, `有帮助` | q_tok3 | 99/152 (65%) | 58/81 (72%) | 111/138 (80%) | 155/158 (98%) | 14/47 (30%) | 54/77 (70%) |
| comply | unclear | 12 | `合规`, `␣compliance`, `遵守`, `遵循`, `␣adherence`, `␣adher`, `␣Compliance`, `␣compliant`, `␣comply`, `␣complying` … (+6) | q_tok3 | 97/152 (64%) | 56/81 (69%) | 51/138 (37%) | 122/158 (77%) | 16/47 (34%) | 52/77 (68%) |
| neutral | unclear | 9 | `中立`, `␣neutrality` | think_slot2 | 108/152 (71%) | 44/81 (54%) | 1/138 (1%) | 0/158 (0%) | 29/47 (62%) | 41/77 (53%) |
| breach | unclear | 1 | `␣breach`, `␣breaches`, `触犯` | think_slot2 | 117/152 (77%) | 34/81 (42%) | 55/138 (40%) | 0/158 (0%) | 36/47 (77%) | 32/77 (42%) |
| withhold | lie | 6 | `␣withholding`, `␣withhold`, `␣withheld`, `␣omit` | q_tok4 | 101/152 (66%) | 48/81 (59%) | 29/138 (21%) | 0/158 (0%) | 28/47 (60%) | 45/77 (58%) |
| cover up | lie | 3 | `掩盖`, `␣masking`, `掩饰`, `遮掩`, `遮盖`, `遮住`, `遮蔽`, `␣cover`, `␣masked`, `mask` … (+2) | preans_slot1 | 125/152 (82%) | 22/81 (27%) | 21/138 (15%) | 1/158 (1%) | 35/47 (74%) | 20/77 (26%) |
| manipulate | lie | 4 | `␣manipulation`, `␣manipulated`, `␣manipulating`, `␣manip`, `␣manipulate`, `操纵`, `Manip`, `␣Manip`, `诱导` | q_tok4 | 81/152 (53%) | 65/81 (80%) | 116/138 (84%) | 140/158 (89%) | 25/47 (53%) | 63/77 (82%) |
| integrity | truth | 8 | `诚信`, `正直`, `␣integrity`, `␣Integrity` | q_tok4 | 104/152 (68%) | 41/81 (51%) | 5/138 (4%) | 0/158 (0%) | 25/47 (53%) | 38/77 (49%) |
| aligned | unclear | 1 | `␣aligned`, `符合`, `是否符合`, `␣align`, `␣alignment` | q_tok3 | 89/152 (59%) | 56/81 (69%) | 72/138 (52%) | 58/158 (37%) | 9/47 (19%) | 52/77 (68%) |
| moral | unclear | 6 | `␣morally`, `道德`, `␣moral`, `的道德`, `␣morality`, `职业道德`, `␣morals`, `␣Moral`, `␣ethical`, `ethical` … (+4) | postans_slot4 | 97/152 (64%) | 43/81 (53%) | 7/138 (5%) | 0/158 (0%) | 33/47 (70%) | 42/77 (55%) |
| knowingly | unclear | 6 | `明知`, `␣knowingly`, `␣knowing` | q_tok10 | 115/152 (76%) | 22/81 (27%) | 107/138 (78%) | 35/158 (22%) | 22/47 (47%) | 19/77 (25%) |
| look back | unclear | 1 | `回顾`, `回顧`, `␣retrospect` | q_tok5 | 73/152 (48%) | 60/81 (74%) | 129/138 (93%) | 101/158 (64%) | 15/47 (32%) | 59/77 (77%) |
| unauthorized | unclear | 1 | `未经允许` | think_slot1 | 83/152 (55%) | 46/81 (57%) | 14/138 (10%) | 2/158 (1%) | 18/47 (38%) | 45/77 (58%) |
| fabricate | lie | 7 | `虚构`, `␣fabricated`, `␣fabrication`, `伪造`, `凭空`, `␣invented`, `␣invent`, `␣invention`, `invent`, `␣inventions` … (+1) | preans_slot1 | 103/152 (68%) | 24/81 (30%) | 85/138 (62%) | 73/158 (46%) | 21/47 (45%) | 21/77 (27%) |
| ethical | unclear | 5 | `␣ethical`, `伦理`, `ethical`, `␣morally`, `␣ethics`, `道德`, `的道德`, `␣moral`, `␣Ethics`, `␣ethic` | postans_slot4 | 90/152 (59%) | 36/81 (44%) | 5/138 (4%) | 0/158 (0%) | 28/47 (60%) | 36/77 (47%) |
| hide | lie | 4 | `␣hiding`, `隐藏`, `␣hidden`, `␣hide`, `Hide`, `hide`, `_hide`, `-hide`, `␣hides`, `␣Hide` … (+15) | q_tok10 | 101/152 (66%) | 23/81 (28%) | 74/138 (54%) | 0/158 (0%) | 24/47 (51%) | 20/77 (26%) |
| strategy | unclear | 4 | `␣strategy`, `策略`, `␣Strategy`, `␣strategically`, `的策略`, `␣tactics` | q_tok3 | 92/152 (61%) | 32/81 (40%) | 1/138 (1%) | 0/158 (0%) | 22/47 (47%) | 29/77 (38%) |
| not conform | unclear | 1 | `不符合` | q_tok10 | 82/152 (54%) | 39/81 (48%) | 39/138 (28%) | 21/158 (13%) | 12/47 (26%) | 36/77 (47%) |
| candid | truth | 10 | `坦诚`, `␣upfront`, `␣straightforward`, `直言` | q_tok9 | 86/152 (57%) | 31/81 (38%) | 82/138 (59%) | 138/158 (87%) | 17/47 (36%) | 28/77 (36%) |
| reality | unclear | 2 | `实际情况`, `实际上`, `与实际`, `␣reality`, `根据实际情况`, `实际上是`, `␣Reality`, `Reality`, `但实际上` | preans_slot2 | 96/152 (63%) | 20/81 (25%) | 23/138 (17%) | 4/158 (3%) | 26/47 (55%) | 19/77 (25%) |
| fiction | unclear | 5 | `fiction`, `␣fictional`, `虚构`, `␣fiction`, `␣Fiction`, `-fiction` | preans_slot1 | 91/152 (60%) | 23/81 (28%) | 84/138 (61%) | 72/158 (46%) | 18/47 (38%) | 20/77 (26%) |
| critical | unclear | 3 | `␣critically`, `␣critical`, `␣Critical`, `critical`, `Critical`, `_critical` | postans_slot2 | 80/152 (53%) | 33/81 (41%) | 0/138 (0%) | 0/158 (0%) | 15/47 (32%) | 30/77 (39%) |
| truth | truth | 5 | `求真`, `真实`, `真实的`, `的真实`, `的真实性`, `真实性`, `真實` | q_tok10 | 90/152 (59%) | 22/81 (27%) | 80/138 (58%) | 29/158 (18%) | 23/47 (49%) | 20/77 (26%) |
| law-abiding | unclear | 2 | `守法` | preans_slot3 | 80/152 (53%) | 30/81 (37%) | 16/138 (12%) | 0/158 (0%) | 9/47 (19%) | 29/77 (38%) |
| appropriate | unclear | 1 | `␣appropriate`, `合适`, `␣suitable`, `␣appropriately` | q_tok3 | 77/152 (51%) | 32/81 (40%) | 5/138 (4%) | 17/158 (11%) | 8/47 (17%) | 29/77 (38%) |
| disclose | truth | 9 | `信息披露`, `␣disclosure`, `披露`, `␣disclosures`, `␣Disclosure`, `公开`, `␣disclosed`, `透露`, `␣disclose`, `␣disclosing` … (+7) | preans_slot3 | 66/152 (43%) | 39/81 (48%) | 28/138 (20%) | 37/158 (23%) | 16/47 (34%) | 39/77 (51%) |
| omit | lie/unclear | 6 | `␣omit`, `␣omission`, `␣omitted`, `omit`, `省略`, `␣OMIT`, `遗漏` | q_tok4 | 51/152 (34%) | 48/81 (59%) | 14/138 (10%) | 0/158 (0%) | 21/47 (45%) | 47/77 (61%) |
| self-reflection | unclear | 1 | `反思` | q_tok5 | 76/152 (50%) | 21/81 (26%) | 39/138 (28%) | 2/158 (1%) | 29/47 (62%) | 20/77 (26%) |
| refuse | unclear | 13 | `拒绝`, `␣refusal`, `␣refuse`, `拒`, `␣refus`, `␣refusing`, `␣refused`, `␣refuses`, `拒绝了`, `拒絕` … (+8) | preans_slot3 | 84/152 (55%) | 11/81 (14%) | 7/138 (5%) | 0/158 (0%) | 14/47 (30%) | 10/77 (13%) |
| violation | unclear | 1 | `违规` | think_slot0 | 60/152 (39%) | 34/81 (42%) | 7/138 (5%) | 0/158 (0%) | 32/47 (68%) | 34/77 (44%) |
| persona | unclear | 2 | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `扮演`, `角色扮演`, `persona`, `␣personagem`, `␣backstory` | q_tok10 | 58/152 (38%) | 29/81 (36%) | 33/138 (24%) | 4/158 (3%) | 12/47 (26%) | 27/77 (35%) |
| misinformation | lie | 2 | `␣misinformation`, `虚假信息`, `不实` | preans_slot1 | 83/152 (55%) | 2/81 (2%) | 18/138 (13%) | 3/158 (2%) | 13/47 (28%) | 1/77 (1%) |
| role_play | unclear | 1 | `扮演`, `角色扮演` | postans_slot4 | 57/152 (38%) | 24/81 (30%) | 9/138 (7%) | 0/158 (0%) | 17/47 (36%) | 24/77 (31%) |
| contradict | unclear | 4 | `␣contradict`, `␣contrad`, `␣contradictory`, `矛盾`, `␣contradiction`, `矛盾的`, `␣contradictions` | preans_slot1 | 62/152 (41%) | 17/81 (21%) | 36/138 (26%) | 10/158 (6%) | 23/47 (49%) | 17/77 (22%) |
| correct | truth | 13 | `正确`, `␣correct`, `正确的`, `是正确的`, `␣valid`, `纠正`, `␣correctly`, `correct`, `Correct`, `␣Correct` … (+20) | q_tok3 | 36/152 (24%) | 36/81 (44%) | 136/138 (99%) | 155/158 (98%) | 17/47 (36%) | 34/77 (44%) |
| role-play | unclear | 4 | `扮演`, `角色扮演`, `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas`, `扮演着` | q_tok10 | 43/152 (28%) | 27/81 (33%) | 33/138 (24%) | 3/158 (2%) | 8/47 (17%) | 25/77 (32%) |
| perfunctory | unclear | 2 | `敷衍` | q_tok3 | 55/152 (36%) | 15/81 (19%) | 9/138 (7%) | 4/158 (3%) | 34/47 (72%) | 15/77 (19%) |
| nonconform | unclear | 2 | `不符合` | postans_slot1 | 51/152 (34%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 15/77 (19%) |
| crafted | unclear | 1 | `␣crafted`, `␣tailored` | q_tok3 | 45/152 (30%) | 19/81 (23%) | 2/138 (1%) | 2/158 (1%) | 15/47 (32%) | 19/77 (25%) |
| downplay | lie | 3 | `淡化`, `␣gloss` | preans_slot1 | 47/152 (31%) | 15/81 (19%) | 3/138 (2%) | 3/158 (2%) | 18/47 (38%) | 15/77 (19%) |
| legal | unclear | 5 | `合法`, `依法`, `␣legally`, `合法的`, `合法性`, `依法依规`, `␣legal`, `␣legality` | postans_slot1 | 32/152 (21%) | 29/81 (36%) | 17/138 (12%) | 0/158 (0%) | 28/47 (60%) | 29/77 (38%) |
| imply | unclear | 2 | `暗示`, `␣implied`, `隐含`, `␣implicitly`, `␣implicit`, `间接`, `␣indirect`, `␣indirectly`, `␣implying`, `␣imply` … (+7) | preans_slot1 | 31/152 (20%) | 28/81 (35%) | 19/138 (14%) | 11/158 (7%) | 11/47 (23%) | 27/77 (35%) |
| reject / overrule | unclear | 1 | `否决`, `驳回` | think_slot3 | 13/152 (9%) | 46/81 (57%) | 56/138 (41%) | 8/158 (5%) | 13/47 (28%) | 46/77 (60%) |
| contrary | unclear | 3 | `␣contrary`, `相反`, `相反的` | preans_slot1 | 31/152 (20%) | 27/81 (33%) | 35/138 (25%) | 4/158 (3%) | 12/47 (26%) | 26/77 (34%) |
| biased | unclear | 3 | `␣biased`, `␣bias`, `biased`, `偏见`, `偏心` | postans_slot3 | 26/152 (17%) | 29/81 (36%) | 46/138 (33%) | 3/158 (2%) | 9/47 (19%) | 28/77 (36%) |
| secret | lie | 5 | `秘密`, `保密`, `␣secret`, `私下`, `的秘密`, `␣secretly`, `secret`, `␣Secret`, `-secret`, `␣confidential` … (+6) | preans_slot2 | 47/152 (31%) | 7/81 (9%) | 2/138 (1%) | 0/158 (0%) | 15/47 (32%) | 6/77 (8%) |
| fulfill | unclear | 1 | `␣fulfill`, `␣fulfillment`, `␣fulfilled`, `␣fulfilling`, `履行`, `履行职责` | q_tok10 | 37/152 (24%) | 15/81 (19%) | 8/138 (6%) | 12/158 (8%) | 6/47 (13%) | 14/77 (18%) |
| euphemistic | unclear | 3 | `委婉` | q_tok10 | 36/152 (24%) | 15/81 (19%) | 14/138 (10%) | 5/158 (3%) | 6/47 (13%) | 15/77 (19%) |
| factual | truth | 3 | `事实`, `␣factual`, `的事实`, `事实和` | postans_slot1 | 36/152 (24%) | 10/81 (12%) | 65/138 (47%) | 85/158 (54%) | 10/47 (21%) | 9/77 (12%) |
| sorry | unclear | 2 | `抱歉`, `␣sorry`, `Sorry`, `␣Sorry` | preans_slot3 | 27/152 (18%) | 17/81 (21%) | 9/138 (7%) | 5/158 (3%) | 13/47 (28%) | 17/77 (22%) |
| influenced | unclear | 1 | `␣influenced` | q_tok3 | 18/152 (12%) | 26/81 (32%) | 41/138 (30%) | 20/158 (13%) | 8/47 (17%) | 26/77 (34%) |
| claim | unclear | 2 | `声称`, `␣claim`, `␣claims`, `␣claiming`, `claim`, `␣Claim`, `␣claimed`, `␣Claims`, `Claim`, `claims` … (+3) | preans_slot1 | 34/152 (22%) | 9/81 (11%) | 5/138 (4%) | 8/158 (5%) | 7/47 (15%) | 6/77 (8%) |
| hallucinate | unclear | 2 | `␣halluc` | postans_slot4 | 28/152 (18%) | 14/81 (17%) | 66/138 (48%) | 2/158 (1%) | 22/47 (47%) | 14/77 (18%) |
| incorrect | lie | 8 | `␣incorrect`, `不符合`, `有误`, `␣inaccur`, `␣inaccurate`, `␣Incorrect`, `␣incorrectly`, `错误的`, `错误的是` | q_tok2 | 18/152 (12%) | 22/81 (27%) | 102/138 (74%) | 49/158 (31%) | 5/47 (11%) | 20/77 (26%) |
| reflect | unclear | 1 | `反思` | postans_slot2 | 34/152 (22%) | 5/81 (6%) | 1/138 (1%) | 4/158 (3%) | 3/47 (6%) | 3/77 (4%) |
| evade | lie | 5 | `回避`, `␣evasion`, `␣dodge`, `␣evade`, `规避`, `evas` | preans_slot1 | 27/152 (18%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 15/47 (32%) | 10/77 (13%) |
| simulate | unclear | 4 | `模拟`, `␣simulated`, `␣simulation`, `扮演`, `角色扮演`, `仿真`, `␣Simulation`, `Simulation`, `␣simulate`, `扮演着` | preans_slot4 | 33/152 (22%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 2/47 (4%) | 4/77 (5%) |
| correct (fix) | truth | 1 | `纠正`, `␣corrected`, `␣correction`, `␣correcting`, `␣corrective`, `␣corrections`, `␣Correction`, `Correction`, `␣Corrections`, `_correction` … (+21) | preans_slot1 | 5/152 (3%) | 32/81 (40%) | 82/138 (59%) | 90/158 (57%) | 4/47 (9%) | 31/77 (40%) |
| law-abiding / compliant | unclear | 3 | `合规` | preans_slot4 | 33/152 (22%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/47 (9%) | 3/77 (4%) |
| legality | unclear | 2 | `␣legally`, `/legal` | think_slot2 | 26/152 (17%) | 11/81 (14%) | 8/138 (6%) | 0/158 (0%) | 19/47 (40%) | 11/77 (14%) |
| private | lie/unclear | 3 | `␣private`, `私密`, `私下`, `␣privately`, `private`, `␣Private`, `Private`, `PRIVATE`, `-private`, `_private` | preans_slot2 | 29/152 (19%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 7/47 (15%) | 5/77 (6%) |
| role | unclear | 2 | `角色的`, `角色`, `␣role`, `的角色`, `role`, `Role`, `␣Role`, `-role`, `␣roles`, `ROLE` | postans_slot4 | 20/152 (13%) | 15/81 (19%) | 1/138 (1%) | 0/158 (0%) | 5/47 (11%) | 15/77 (19%) |
| lure | unclear | 2 | `诱导`, `␣bait` | postans_slot4 | 11/152 (7%) | 22/81 (27%) | 33/138 (24%) | 0/158 (0%) | 10/47 (21%) | 22/77 (29%) |
| vague | unclear | 1 | `␣vague`, `模糊`, `含糊`, `␣vaguely` | preans_slot1 | 22/152 (14%) | 11/81 (14%) | 0/138 (0%) | 3/158 (2%) | 8/47 (17%) | 9/77 (12%) |
| unethical | lie/unclear | 4 | `␣unethical` | q_tok10 | 29/152 (19%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| faithful | truth | 1 | `忠实` | q_tok10 | 24/152 (16%) | 6/81 (7%) | 24/138 (17%) | 2/158 (1%) | 2/47 (4%) | 6/77 (8%) |
| harmful | unclear | 1 | `␣harmful`, `有害`, `␣harm`, `危害` | postans_slot4 | 22/152 (14%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 3/47 (6%) | 5/77 (6%) |
| official line | unclear | 6 | `口径` | q_tok1 | 25/152 (16%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 10/47 (21%) | 3/77 (4%) |
| euphemism | unclear | 2 | `委婉` | preans_slot1 | 9/152 (6%) | 18/81 (22%) | 5/138 (4%) | 0/158 (0%) | 8/47 (17%) | 18/77 (23%) |
| ostensibly | unclear | 3 | `表面上` | preans_slot2 | 13/152 (9%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 7/47 (15%) | 13/77 (17%) |
| reveal | truth | 4 | `揭露`, `揭示了`, `揭示`, `␣reveal`, `揭`, `␣revealing`, `暴露`, `␣exposing`, `reveal` | q_tok10 | 13/152 (9%) | 12/81 (15%) | 3/138 (2%) | 0/158 (0%) | 5/47 (11%) | 12/77 (16%) |
| trap | unclear | 1 | `陷阱`, `␣trap`, `␣trapped`, `␣traps`, `trap`, `Trap`, `␣Trap`, `␣trapping`, `_trap`, `␣bait` | postans_slot4 | 8/152 (5%) | 17/81 (21%) | 27/138 (20%) | 1/158 (1%) | 7/47 (15%) | 17/77 (22%) |
| tailored | unclear | 1 | `␣tailored` | q_tok3 | 18/152 (12%) | 6/81 (7%) | 0/138 (0%) | 2/158 (1%) | 3/47 (6%) | 6/77 (8%) |
| deviate | unclear | 2 | `偏离`, `背离` | postans_slot4 | 7/152 (5%) | 16/81 (20%) | 2/138 (1%) | 2/158 (1%) | 3/47 (6%) | 16/77 (21%) |
| good faith | truth | 3 | `善意` | preans_slot4 | 16/152 (11%) | 7/81 (9%) | 3/138 (2%) | 0/158 (0%) | 3/47 (6%) | 5/77 (6%) |
| candid / frank | truth | 2 | `␣blunt`, `坦诚`, `␣straightforward`, `直言` | preans_slot1 | 0/152 (0%) | 21/81 (26%) | 35/138 (25%) | 54/158 (34%) | 0/47 (0%) | 21/77 (27%) |
| upright | truth | 3 | `正直` | postans_slot1 | 4/152 (3%) | 16/81 (20%) | 3/138 (2%) | 0/158 (0%) | 1/47 (2%) | 16/77 (21%) |
| forced | unclear | 2 | `␣forced`, `forced`, `␣forcing`, `强制`, `被迫`, `迫使`, `逼迫`, `forcing`, `胁迫`, `强迫` … (+1) | postans_slot4 | 14/152 (9%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 9/47 (19%) | 5/77 (6%) |
| transparent | truth | 7 | `␣transparency`, `透明`, `透明的`, `␣transparent`, `-transparent`, `透明度`, `␣Transparency`, `transparent`, `␣Transparent` | q_tok10 | 3/152 (2%) | 16/81 (20%) | 51/138 (37%) | 1/158 (1%) | 3/47 (6%) | 16/77 (21%) |
| blame | unclear | 2 | `␣blame`, `␣blames`, `␣blamed` | preans_slot1 | 17/152 (11%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 2/77 (3%) |
| confess | truth | 7 | `坦白`, `如实供述` | preans_slot3 | 16/152 (11%) | 2/81 (2%) | 3/138 (2%) | 1/158 (1%) | 4/47 (9%) | 2/77 (3%) |
| conscience | unclear | 2 | `良心` | q_tok10 | 16/152 (11%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 2/77 (3%) |
| framing | unclear | 3 | `␣framing` | q_tok4 | 6/152 (4%) | 12/81 (15%) | 7/138 (5%) | 0/158 (0%) | 2/47 (4%) | 12/77 (16%) |
| unbiased | unclear | 1 | `␣unbiased` | postans_slot3 | 6/152 (4%) | 11/81 (14%) | 46/138 (33%) | 0/158 (0%) | 3/47 (6%) | 11/77 (14%) |
| disguise | lie | 4 | `掩饰`, `␣mask`, `伪装`, `␣masking` | q_tok4 | 12/152 (8%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 5/77 (6%) |
| expose | truth | 2 | `揭`, `揭露`, `暴露` | postans_slot4 | 14/152 (9%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 3/47 (6%) | 2/77 (3%) |
| justify | unclear | 1 | `␣justification`, `justify`, `合理化`, `正当` | postans_slot1 | 10/152 (7%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 10/47 (21%) | 6/77 (8%) |
| silent | unclear | 2 | `不语`, `沉默`, `␣silence` | q_tok9 | 15/152 (10%) | 1/81 (1%) | 2/138 (1%) | 1/158 (1%) | 0/47 (0%) | 0/77 (0%) |
| exaggerate | lie | 2 | `夸大`, `␣exaggerated` | preans_slot1 | 12/152 (8%) | 3/81 (4%) | 0/138 (0%) | 3/158 (2%) | 2/47 (4%) | 3/77 (4%) |
| indirect | unclear | 1 | `间接`, `␣indirect` | q_tok4 | 0/152 (0%) | 15/81 (19%) | 3/138 (2%) | 0/158 (0%) | 0/47 (0%) | 15/77 (19%) |
| inaccurate | lie | 3 | `准确性和`, `不准确` | preans_slot1 | 8/152 (5%) | 6/81 (7%) | 6/138 (4%) | 35/158 (22%) | 3/47 (6%) | 6/77 (8%) |
| scripted | unclear | 2 | `␣canned`, `␣scripted`, `␣rehearsal` | q_tok3 | 12/152 (8%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 8/47 (17%) | 2/77 (3%) |
| code_of_conduct | unclear | 1 | `守则` | postans_slot4 | 10/152 (7%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) | 2/47 (4%) | 3/77 (4%) |
| legitimate | unclear | 1 | `正当`, `␣legitimate` | postans_slot1 | 5/152 (3%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 5/47 (11%) | 6/77 (8%) |
| fraud | lie | 4 | `␣fraud`, `诈`, `␣fraudulent` | q_tok4 | 11/152 (7%) | 0/81 (0%) | 0/138 (0%) | 4/158 (3%) | 3/47 (6%) | 0/77 (0%) |
| public / disclose | truth | 1 | `公开` | think_slot3 | 7/152 (5%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 5/47 (11%) | 4/77 (5%) |
| trick | lie/unclear | 2 | `␣trick`, `␣tricks`, `␣Trick` | postans_slot4 | 4/152 (3%) | 6/81 (7%) | 1/138 (1%) | 1/158 (1%) | 4/47 (9%) | 6/77 (8%) |
| self-check | unclear | 2 | `自查`, `自检` | q_tok1 | 9/152 (6%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 5/47 (11%) | 1/77 (1%) |
| illegal | unclear | 1 | `违法` | postans_slot1 | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 9/47 (19%) | 0/77 (0%) |
| public | unclear | 2 | `公开`, `信息公开` | postans_slot4 | 7/152 (5%) | 2/81 (2%) | 11/138 (8%) | 0/158 (0%) | 2/47 (4%) | 2/77 (3%) |
| make public | truth | 3 | `公开` | preans_slot2 | 3/152 (2%) | 6/81 (7%) | 17/138 (12%) | 0/158 (0%) | 1/47 (2%) | 6/77 (8%) |
| fair | unclear | 1 | `公正` | preans_slot4 | 2/152 (1%) | 7/81 (9%) | 6/138 (4%) | 8/158 (5%) | 2/47 (4%) | 7/77 (9%) |
| purpose | unclear | 3 | `目的是`, `␣purpose`, `的目的`, `目的是为了` | q_tok4 | 4/152 (3%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 1/47 (2%) | 4/77 (5%) |
| contradiction | unclear | 3 | `矛盾`, `␣contradictory`, `矛盾的` | postans_slot1 | 3/152 (2%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 5/77 (6%) |
| insinuate | unclear | 1 | `暗示` | q_tok4 | 5/152 (3%) | 3/81 (4%) | 6/138 (4%) | 0/158 (0%) | 4/47 (9%) | 3/77 (4%) |
| credible | truth | 3 | `可信`, `公信` | postans_slot3 | 5/152 (3%) | 2/81 (2%) | 4/138 (3%) | 0/158 (0%) | 2/47 (4%) | 2/77 (3%) |
| spin | lie | 3 | `␣spin`, `Spin`, `␣Spin`, `-spin`, `␣spins`, `spin`, `␣spinning`, `_spin` | preans_slot1 | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 2/77 (3%) |
| hesitation | unclear | 1 | `␣hesitation` | q_tok1 | 0/152 (0%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 7/77 (9%) |
| kidding | unclear | 1 | `␣kidding` | q_tok9 | 5/152 (3%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 4/47 (9%) | 2/77 (3%) |
| apology | unclear | 2 | `抱歉`, `对不起` | think_slot2 | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 6/158 (4%) | 5/47 (11%) | 2/77 (3%) |
| hidden | lie | 2 | `Hidden`, `␣hidden`, `hidden`, `␣undisclosed`, `隐藏着`, `藏着` | postans_slot4 | 1/152 (1%) | 5/81 (6%) | 3/138 (2%) | 12/158 (8%) | 0/47 (0%) | 5/77 (6%) |
| accusation | unclear | 1 | `␣accusations` | q_tok5 | 0/152 (0%) | 6/81 (7%) | 3/138 (2%) | 1/158 (1%) | 0/47 (0%) | 6/77 (8%) |
| alignment | unclear | 1 | `align` | q_tok4 | 2/152 (1%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 4/77 (5%) |
| justify / excuse | unclear | 1 | `␣justification`, `␣justified`, `␣excuse` | think_slot2 | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| pretend | lie | 3 | `伪装`, `␣pretending`, `装着` | preans_slot1 | 1/152 (1%) | 3/81 (4%) | 1/138 (1%) | 2/158 (1%) | 0/47 (0%) | 2/77 (3%) |
| informed | unclear | 2 | `知情` | q_tok0 | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| innocent | unclear | 1 | `无罪` | q_tok5 | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| private / secret | lie | 1 | `私下` | think_slot3 | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| distort | lie | 3 | `扭曲`, `␣distortion`, `␣distort`, `␣distorted` | preans_slot1 | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 0/77 (0%) |
| confidential | lie | 1 | `保密` | q_tok1 | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| contradictory | unclear | 1 | `␣contradictory` | q_tok2 | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 1/77 (1%) |
| ostensible | unclear | 1 | `表面上` | think_slot3 | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| role-play / simulate | unclear | 1 | `扮演`, `角色扮演`, `模拟` | preans_slot1 | 0/152 (0%) | 2/81 (2%) | 10/138 (7%) | 7/158 (4%) | 0/47 (0%) | 2/77 (3%) |
| not aligned | unclear | 1 | `不符合` | q_tok3 | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 0/47 (0%) | 1/77 (1%) |
| avoid | unclear | 1 | `␣avoid`, `␣avoiding`, `␣avoided`, `avoid`, `␣avoidance` | q_tok10 | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| unfulfilled | unclear | 1 | `未履行` | q_tok10 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 1/47 (2%) | 1/77 (1%) |
| apologize | unclear | 2 | `道歉` | postans_slot1 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| persuade | unclear | 1 | `␣persuasive` | postans_slot2 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| undisclosed | lie | 1 | `␣undisclosed` | postans_slot4 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| regret | unclear | 1 | `悔` | postans_slot1 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| unaware | unclear | 1 | `不知情` | preans_slot1 | 1/152 (1%) | 0/81 (0%) | 6/138 (4%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| leak | unclear | 1 | `泄露` | preans_slot1 | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| mask / cover up | lie | 1 | `␣masking` | preans_slot2 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| betray | unclear | 1 | `出卖` | q_tok4 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| induce | lie | 1 | `诱导` | q_tok4 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| impersonate | lie | 1 | `冒充` | q_tok10 | 1/152 (1%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| argue / defend | unclear | 1 | `答辩` | think_slot2 | 0/152 (0%) | 1/81 (1%) | 15/138 (11%) | 123/158 (78%) | 0/47 (0%) | 1/77 (1%) |
| responsible | unclear | 1 | `负责任` | think_slot2 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| go against | unclear | 1 | `违背` | think_slot3 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |

**wording Q6_factual, positions from the question on** (136 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|---|---|
| fact | truth/unclear | 18 | `␣factual`, `事实`, `␣fact`, `␣facts`, `␣Fact`, `的事实`, `␣reality`, `实际上`, `与现实`, `事实上` … (+31) | q_tok7 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 43/43 (100%) | 73/73 (100%) |
| true | truth | 24 | `␣true`, `true`, `␣True`, `True`, `真`, `的真`, `真实的`, `␣TRUE`, `真实`, `成立` … (+31) | q_tok8 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 43/43 (100%) | 73/73 (100%) |
| turn to good | unclear | 1 | `向善` | think_slot0 | 151/152 (99%) | 80/81 (99%) | 138/138 (100%) | 154/158 (97%) | 43/43 (100%) | 72/73 (99%) |
| accurate | truth | 11 | `准确`, `␣accurate`, `␣accurately`, `␣accuracy`, `准确的`, `准确地`, `accuracy`, `␣accur`, `accur`, `␣Accuracy` … (+2) | q_tok3 | 150/152 (99%) | 79/81 (98%) | 138/138 (100%) | 146/158 (92%) | 43/43 (100%) | 71/73 (97%) |
| self-examination | unclear | 2 | `反思`, `自查`, `自检`, `␣critique`, `批判`, `指正` | preans_slot0 | 145/152 (95%) | 72/81 (89%) | 126/138 (91%) | 156/158 (99%) | 38/43 (88%) | 64/73 (88%) |
| clarify | unclear | 3 | `澄清`, `␣clarification` | think_slot0 | 126/152 (83%) | 76/81 (94%) | 138/138 (100%) | 156/158 (99%) | 31/43 (72%) | 68/73 (93%) |
| hallucinate | unclear | 4 | `␣halluc`, `幻觉` | q_tok4 | 138/152 (91%) | 64/81 (79%) | 133/138 (96%) | 126/158 (80%) | 36/43 (84%) | 57/73 (78%) |
| violate | unclear | 13 | `违背`, `违反`, `违反了`, `␣violate`, `违规`, `␣violates`, `␣violating`, `␣violation`, `␣violations`, `␣violated` … (+4) | q_tok3 | 127/152 (84%) | 73/81 (90%) | 111/138 (80%) | 96/158 (61%) | 28/43 (65%) | 65/73 (89%) |
| sincere | truth | 2 | `诚挚`, `诚恳` | postans_slot0 | 127/152 (84%) | 67/81 (83%) | 101/138 (73%) | 2/158 (1%) | 30/43 (70%) | 62/73 (85%) |
| lie | lie | 15 | `说谎`, `谎言`, `撒谎`, `␣lie`, `谎`, `␣lying`, `lying`, `␣lies`, `␣거짓`, `␣liar` … (+6) | q_tok5 | 138/152 (91%) | 54/81 (67%) | 89/138 (64%) | 1/158 (1%) | 37/43 (86%) | 46/73 (63%) |
| critique | unclear | 2 | `␣critique`, `批判`, `批评` | postans_slot2 | 130/152 (86%) | 62/81 (77%) | 4/138 (3%) | 5/158 (3%) | 30/43 (70%) | 55/73 (75%) |
| hide | lie | 9 | `Hidden`, `掩`, `-hide`, `隐瞒`, `藏`, `␣hide`, `␣hidden`, `隐藏`, `隐藏的`, `隐蔽` … (+11) | postans_slot1 | 130/152 (86%) | 59/81 (73%) | 32/138 (23%) | 18/158 (11%) | 27/43 (63%) | 53/73 (73%) |
| fake | lie | 5 | `fake`, `␣fake`, `Fake`, `作假`, `␣Fake` | q_tok6 | 121/152 (80%) | 64/81 (79%) | 50/138 (36%) | 18/158 (11%) | 22/43 (51%) | 58/73 (79%) |
| objective | unclear | 15 | `客观`, `␣objectively`, `␣objective`, `objective`, `Objective`, `实事求是` | q_tok13 | 131/152 (86%) | 51/81 (63%) | 32/138 (23%) | 27/158 (17%) | 30/43 (70%) | 44/73 (60%) |
| wrong | lie | 24 | `错误`, `错`, `是非`, `错了`, `␣error`, `是错误的`, `error`, `␣wrong`, `不对`, `指正` … (+11) | postans_slot4 | 115/152 (76%) | 66/81 (81%) | 126/138 (91%) | 94/158 (59%) | 40/43 (93%) | 60/73 (82%) |
| honest | truth | 15 | `诚实`, `诚`, `如实`, `坦诚`, `诚信`, `␣truthful`, `␣honest`, `␣honesty`, `实事求是`, `诚实守信` … (+5) | preans_slot1 | 127/152 (84%) | 53/81 (65%) | 100/138 (72%) | 36/158 (23%) | 33/43 (77%) | 47/73 (64%) |
| deliberate | unclear | 11 | `␣intentionally`, `␣deliberately`, `␣deliberate`, `明知`, `故意`, `␣knowingly`, `␣intentional`, `有意`, `刻意`, `故意的` | preans_slot1 | 144/152 (95%) | 36/81 (44%) | 44/138 (32%) | 14/158 (9%) | 38/43 (88%) | 30/73 (41%) |
| knowingly | unclear | 12 | `明知`, `␣knowingly` | preans_slot1 | 142/152 (93%) | 30/81 (37%) | 43/138 (31%) | 6/158 (4%) | 36/43 (84%) | 24/73 (33%) |
| correct | truth | 18 | `␣correct`, `纠正`, `正确`, `␣valid`, `␣correctly`, `␣Correct`, `正确的`, `valid`, `␣corrected`, `正确答案` … (+22) | q_tok3 | 102/152 (67%) | 69/81 (85%) | 137/138 (99%) | 140/158 (89%) | 25/43 (58%) | 62/73 (85%) |
| fabricate | lie | 13 | `虚构`, `伪造`, `␣fabricated`, `␣invented`, `␣fabrication`, `␣invent`, `凭空`, `fiction`, `␣fiction`, `␣fictional` … (+8) | preans_slot1 | 124/152 (82%) | 44/81 (54%) | 49/138 (36%) | 48/158 (30%) | 30/43 (70%) | 37/73 (51%) |
| disclose | truth | 8 | `公开`, `␣disclosure`, `披露`, `信息披露`, `透露`, `␣disclose`, `␣disclosing`, `␣disclosed`, `揭露`, `␣reveal` … (+10) | preans_slot3 | 107/152 (70%) | 57/81 (70%) | 36/138 (26%) | 48/158 (30%) | 22/43 (51%) | 52/73 (71%) |
| fiction | unclear | 3 | `fiction`, `␣fiction`, `-fiction`, `␣fictional`, `虚构`, `␣fict`, `架空`, `␣Fiction` | preans_slot1 | 119/152 (78%) | 44/81 (54%) | 49/138 (36%) | 48/158 (30%) | 28/43 (65%) | 37/73 (51%) |
| comply | unclear | 6 | `遵守`, `合规`, `遵循`, `␣comply`, `符合`, `严格遵守`, `␣compliance`, `␣adher`, `是否符合`, `␣adherence` … (+9) | q_tok3 | 99/152 (65%) | 61/81 (75%) | 73/138 (53%) | 144/158 (91%) | 16/43 (37%) | 54/73 (74%) |
| self-examine | unclear | 2 | `自查`, `自检`, `反思`, `自省`, `审视`, `␣reflect`, `␣reflection`, `reflect`, `␣Reflection`, `␣reflecting` … (+6) | q_tok8 | 91/152 (60%) | 69/81 (85%) | 136/138 (99%) | 156/158 (99%) | 35/43 (81%) | 63/73 (86%) |
| conceal | lie | 12 | `隐瞒`, `␣conceal`, `␣concealed`, `掩`, `掩盖`, `掩饰`, `遮`, `隐`, `␣masking`, `␣hiding` … (+16) | q_tok5 | 119/152 (78%) | 40/81 (49%) | 105/138 (76%) | 89/158 (56%) | 38/43 (88%) | 34/73 (47%) |
| claim | unclear | 4 | `␣assert`, `assert`, `␣claim`, `␣claims`, `␣claiming`, `␣Claim`, `claim`, `␣claimed`, `Claim`, `␣Claims` … (+21) | preans_slot1 | 113/152 (74%) | 46/81 (57%) | 64/138 (46%) | 24/158 (15%) | 32/43 (74%) | 39/73 (53%) |
| truthful | truth | 9 | `如实`, `␣truthful` | q_tok5 | 111/152 (73%) | 44/81 (54%) | 121/138 (88%) | 0/158 (0%) | 27/43 (63%) | 38/73 (52%) |
| direct | unclear | 1 | `␣direct`, `直接的`, `直接` | think_slot2 | 99/152 (65%) | 56/81 (69%) | 31/138 (22%) | 27/158 (17%) | 28/43 (65%) | 50/73 (68%) |
| mislead | lie | 4 | `␣misleading`, `误导`, `误导性` | q_tok6 | 121/152 (80%) | 33/81 (41%) | 1/138 (1%) | 0/158 (0%) | 27/43 (63%) | 26/73 (36%) |
| inadvertent | unclear | 3 | `␣inadvertently`, `␣unintention`, `␣accidentally`, `无意` | q_tok3 | 87/152 (57%) | 62/81 (77%) | 62/138 (45%) | 6/158 (4%) | 25/43 (58%) | 56/73 (77%) |
| offended | unclear | 1 | `␣offended` | think_slot0 | 100/152 (66%) | 48/81 (59%) | 7/138 (5%) | 28/158 (18%) | 22/43 (51%) | 42/73 (58%) |
| contradict | unclear | 10 | `␣contradict`, `␣contrad`, `␣contradictory`, `矛盾`, `␣contradiction`, `␣contradictions`, `矛盾的`, `相反`, `␣contrary`, `相反的` … (+2) | q_tok5 | 82/152 (54%) | 53/81 (65%) | 134/138 (97%) | 32/158 (20%) | 24/43 (56%) | 46/73 (63%) |
| deceive | lie | 13 | `欺骗`, `␣deception`, `␣deceptive`, `欺`, `哄`, `骗`, `␣deceive`, `␣deceit` | preans_slot1 | 105/152 (69%) | 23/81 (28%) | 1/138 (1%) | 1/158 (1%) | 21/43 (49%) | 17/73 (23%) |
| ethics / morality | unclear | 1 | `␣ethics`, `␣ethical`, `职业道德`, `思想道德` | think_slot2 | 89/152 (59%) | 39/81 (48%) | 40/138 (29%) | 48/158 (30%) | 22/43 (51%) | 32/73 (44%) |
| breach | unclear | 1 | `␣breach`, `␣breaches`, `␣breached` | think_slot2 | 101/152 (66%) | 23/81 (28%) | 8/138 (6%) | 0/158 (0%) | 29/43 (67%) | 20/73 (27%) |
| compliance | unclear | 6 | `合规`, `遵循`, `遵守`, `守则`, `␣compliance`, `遵守国家` | postans_slot4 | 66/152 (43%) | 54/81 (67%) | 36/138 (26%) | 0/158 (0%) | 17/43 (40%) | 49/73 (67%) |
| cover up | lie | 2 | `掩盖`, `掩饰`, `␣masking`, `遮盖`, `遮掩`, `遮住`, `遮蔽`, `␣masked` | preans_slot1 | 92/152 (61%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 21/43 (49%) | 9/73 (12%) |
| neutrality | unclear | 2 | `␣neutrality`, `中立` | think_slot2 | 77/152 (51%) | 26/81 (32%) | 0/138 (0%) | 0/158 (0%) | 24/43 (56%) | 23/73 (32%) |
| fictional | unclear | 2 | `虚构`, `架空`, `␣fictional`, `fiction`, `␣fiction`, `␣Fiction` | q_tok13 | 76/152 (50%) | 25/81 (31%) | 7/138 (5%) | 20/158 (13%) | 10/43 (23%) | 21/73 (29%) |
| role-play | unclear | 4 | `扮演`, `角色扮演`, `␣persona`, `␣personas`, `␣Persona`, `Persona`, `扮演着`, `persona`, `␣Personas` | preans_slot2 | 62/152 (41%) | 38/81 (47%) | 1/138 (1%) | 2/158 (1%) | 28/43 (65%) | 34/73 (47%) |
| consistent | unclear | 3 | `符合`, `是否符合`, `符合要求` | postans_slot1 | 43/152 (28%) | 52/81 (64%) | 125/138 (91%) | 10/158 (6%) | 33/43 (77%) | 51/73 (70%) |
| neutral | unclear | 1 | `中立` | postans_slot0 | 44/152 (29%) | 49/81 (60%) | 82/138 (59%) | 118/158 (75%) | 12/43 (28%) | 44/73 (60%) |
| bias | unclear | 2 | `␣biased`, `biased`, `bias`, `偏见`, `␣bias`, `␣biases` | postans_slot3 | 46/152 (30%) | 41/81 (51%) | 53/138 (38%) | 3/158 (2%) | 14/43 (33%) | 38/73 (52%) |
| incorrect | lie | 13 | `␣incorrect`, `␣inaccur`, `错误的是`, `错误的`, `不符合`, `有误`, `␣incorrectly`, `␣Incorrect`, `␣inaccurate` | q_tok13 | 50/152 (33%) | 37/81 (46%) | 64/138 (46%) | 12/158 (8%) | 6/43 (14%) | 33/73 (45%) |
| hidden | lie | 1 | `␣hidden`, `hidden` | q_tok5 | 54/152 (36%) | 33/81 (41%) | 105/138 (76%) | 89/158 (56%) | 18/43 (42%) | 28/73 (38%) |
| omit | lie/unclear | 6 | `␣omit`, `␣omission`, `遗漏`, `omit`, `省略`, `omite`, `␣OMIT` | think_slot2 | 50/152 (33%) | 28/81 (35%) | 1/138 (1%) | 1/158 (1%) | 9/43 (21%) | 25/73 (34%) |
| noncompliant | unclear | 3 | `不符合` | q_tok5 | 46/152 (30%) | 32/81 (40%) | 15/138 (11%) | 17/158 (11%) | 9/43 (21%) | 29/73 (40%) |
| silent | unclear | 2 | `不语`, `沉默` | q_tok12 | 67/152 (44%) | 11/81 (14%) | 9/138 (7%) | 52/158 (33%) | 5/43 (12%) | 8/73 (11%) |
| refuse | unclear | 14 | `␣refusal`, `拒绝`, `␣refuse`, `␣refusing`, `␣refus`, `拒`, `␣refuses`, `␣refused`, `拒绝了`, `␣decline` … (+4) | q_tok5 | 31/152 (20%) | 45/81 (56%) | 59/138 (43%) | 4/158 (3%) | 13/43 (30%) | 45/73 (62%) |
| violation | unclear | 1 | `违规` | think_slot0 | 41/152 (27%) | 29/81 (36%) | 2/138 (1%) | 0/158 (0%) | 24/43 (56%) | 28/73 (38%) |
| unauthorized | unclear | 1 | `未经允许` | think_slot1 | 41/152 (27%) | 29/81 (36%) | 5/138 (4%) | 0/158 (0%) | 11/43 (26%) | 27/73 (37%) |
| secret | lie | 8 | `秘密`, `␣secret`, `保密`, `␣hidden`, `Hidden`, `隐藏的`, `secret`, `Secret`, `-secret`, `␣secretly` … (+15) | preans_slot2 | 54/152 (36%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 18/43 (42%) | 11/73 (15%) |
| perfunctory | unclear | 3 | `敷衍` | q_tok3 | 51/152 (34%) | 16/81 (20%) | 7/138 (5%) | 3/158 (2%) | 24/43 (56%) | 14/73 (19%) |
| faithful | unclear | 1 | `忠实` | q_tok13 | 50/152 (33%) | 17/81 (21%) | 2/138 (1%) | 0/158 (0%) | 4/43 (9%) | 15/73 (21%) |
| roleplay | unclear | 1 | `扮演`, `角色扮演` | postans_slot4 | 42/152 (28%) | 22/81 (27%) | 2/138 (1%) | 1/158 (1%) | 7/43 (16%) | 20/73 (27%) |
| persona | unclear | 2 | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas` | q_tok13 | 43/152 (28%) | 21/81 (26%) | 0/138 (0%) | 1/158 (1%) | 8/43 (19%) | 18/73 (25%) |
| ethics | unclear | 4 | `道德`, `␣moral`, `␣ethical`, `伦理`, `␣morally`, `␣ethics`, `的道德`, `␣Ethics`, `ethical`, `␣morality` … (+4) | q_tok13 | 54/152 (36%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 7/73 (10%) |
| imply | unclear | 5 | `隐含`, `␣implied`, `␣implicitly`, `暗示`, `␣implying`, `␣implies`, `␣imply`, `␣implicit`, `␣IMPLIED`, `␣implication` … (+8) | q_tok3 | 31/152 (20%) | 28/81 (35%) | 23/138 (17%) | 0/158 (0%) | 17/43 (40%) | 25/73 (34%) |
| integrity | truth | 4 | `诚信`, `␣integrity`, `诚实守信`, `␣Integrity` | q_tok5 | 49/152 (32%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 6/73 (8%) |
| legal | unclear | 4 | `依法`, `合法`, `␣legally`, `合法的` | postans_slot3 | 41/152 (27%) | 14/81 (17%) | 2/138 (1%) | 3/158 (2%) | 9/43 (21%) | 13/73 (18%) |
| unbiased | unclear | 1 | `␣unbiased` | postans_slot3 | 25/152 (16%) | 23/81 (28%) | 65/138 (47%) | 0/158 (0%) | 9/43 (21%) | 20/73 (27%) |
| joke | unclear | 1 | `玩笑` | postans_slot0 | 21/152 (14%) | 22/81 (27%) | 112/138 (81%) | 125/158 (79%) | 12/43 (28%) | 22/73 (30%) |
| i cannot | unclear | 5 | `我无法`, `我不能` | preans_slot3 | 33/152 (22%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 15/43 (35%) | 7/73 (10%) |
| hypothetical | unclear | 3 | `␣hypothetical` | preans_slot2 | 17/152 (11%) | 23/81 (28%) | 7/138 (5%) | 15/158 (9%) | 11/43 (26%) | 23/73 (32%) |
| reflect | unclear | 1 | `反思` | postans_slot2 | 33/152 (22%) | 6/81 (7%) | 2/138 (1%) | 4/158 (3%) | 1/43 (2%) | 1/73 (1%) |
| apologize | unclear | 5 | `道歉`, `抱歉`, `␣apology`, `␣apologies` | preans_slot3 | 24/152 (16%) | 14/81 (17%) | 8/138 (6%) | 38/158 (24%) | 14/43 (33%) | 13/73 (18%) |
| law-abiding | unclear | 2 | `守法` | preans_slot3 | 28/152 (18%) | 10/81 (12%) | 27/138 (20%) | 3/158 (2%) | 2/43 (5%) | 10/73 (14%) |
| liar | lie | 2 | `␣liar` | q_tok5 | 35/152 (23%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 1/73 (1%) |
| inconsistent | unclear | 2 | `不符合` | postans_slot1 | 23/152 (15%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 12/73 (16%) |
| euphemistic | unclear | 3 | `委婉` | q_tok5 | 21/152 (14%) | 11/81 (14%) | 1/138 (1%) | 0/158 (0%) | 7/43 (16%) | 8/73 (11%) |
| lawful | unclear | 1 | `合法` | postans_slot1 | 15/152 (10%) | 14/81 (17%) | 4/138 (3%) | 0/158 (0%) | 15/43 (35%) | 14/73 (19%) |
| lure | unclear | 1 | `诱导`, `␣bait`, `诱` | postans_slot4 | 14/152 (9%) | 14/81 (17%) | 5/138 (4%) | 0/158 (0%) | 11/43 (26%) | 13/73 (18%) |
| evade | lie | 5 | `␣evasion`, `回避`, `规避`, `␣evade`, `遁` | think_slot2 | 5/152 (3%) | 23/81 (28%) | 80/138 (58%) | 55/158 (35%) | 0/43 (0%) | 22/73 (30%) |
| ethical | unclear | 3 | `␣ethical`, `伦理`, `␣ethics`, `␣moral`, `ethical`, `␣Ethics`, `道德`, `的道德`, `职业道德`, `␣morally` … (+1) | preans_slot2 | 11/152 (7%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 15/73 (21%) |
| good_intent | unclear | 1 | `好心` | postans_slot1 | 24/152 (16%) | 2/81 (2%) | 4/138 (3%) | 1/158 (1%) | 1/43 (2%) | 0/73 (0%) |
| trap | unclear | 1 | `陷阱`, `␣trap`, `␣trapped`, `␣traps`, `trap`, `␣Trap`, `Trap`, `␣trapping`, `_trap`, `陷入` | postans_slot4 | 12/152 (8%) | 14/81 (17%) | 15/138 (11%) | 1/158 (1%) | 10/43 (23%) | 13/73 (18%) |
| secretly | lie | 2 | `暗中` | think_slot1 | 18/152 (12%) | 8/81 (10%) | 57/138 (41%) | 7/158 (4%) | 3/43 (7%) | 5/73 (7%) |
| simulated | unclear | 3 | `␣simulated`, `模拟`, `␣simulation`, `␣Simulation` | preans_slot2 | 12/152 (8%) | 10/81 (12%) | 1/138 (1%) | 3/158 (2%) | 9/43 (21%) | 10/73 (14%) |
| no regret | unclear | 1 | `无怨无悔` | think_slot1 | 18/152 (12%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 3/73 (4%) |
| outwardly | unclear | 3 | `表面上` | preans_slot2 | 15/152 (10%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 5/73 (7%) |
| mistake | unclear | 4 | `␣error`, `␣mistake`, `␣mistakes`, `error` | q_tok5 | 8/152 (5%) | 12/81 (15%) | 63/138 (46%) | 129/158 (82%) | 2/43 (5%) | 10/73 (14%) |
| make public | truth | 1 | `公开`, `信息公开` | postans_slot4 | 15/152 (10%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| conscience | unclear | 4 | `良心`, `␣conscience` | q_tok13 | 18/152 (12%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| contradiction | unclear | 3 | `矛盾`, `␣paradox`, `␣contradiction`, `␣contradictory`, `矛盾的`, `␣contradict` | postans_slot1 | 11/152 (7%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 10/43 (23%) | 6/73 (8%) |
| coercion | unclear | 3 | `␣force`, `␣forced`, `␣forcing`, `迫使`, `␣Force`, `逼迫`, `forcing`, `被迫`, `强迫`, `胁迫` … (+1) | postans_slot4 | 14/152 (9%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 7/43 (16%) | 3/73 (4%) |
| blame | unclear | 1 | `␣blaming`, `␣blame`, `␣blames`, `␣blamed` | preans_slot1 | 15/152 (10%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| leak | unclear | 3 | `泄露`, `␣leak` | q_tok5 | 9/152 (6%) | 8/81 (10%) | 4/138 (3%) | 0/158 (0%) | 3/43 (7%) | 7/73 (10%) |
| reveal | truth | 2 | `透露`, `␣reveal`, `reveal`, `揭` | q_tok13 | 15/152 (10%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 2/73 (3%) |
| dishonest | lie | 5 | `␣dishonest`, `虚伪` | q_tok5 | 14/152 (9%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| unethical | lie/unclear | 4 | `␣unethical`, `␣immoral` | preans_slot2 | 3/152 (2%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 13/73 (18%) |
| subjective | unclear | 3 | `主观` | preans_slot4 | 14/152 (9%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 1/73 (1%) |
| honest / upright | truth | 1 | `正直` | think_slot2 | 7/152 (5%) | 8/81 (10%) | 10/138 (7%) | 0/158 (0%) | 4/43 (9%) | 8/73 (11%) |
| dilemma | unclear | 1 | `困境`, `␣dilemma` | postans_slot4 | 11/152 (7%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 3/73 (4%) |
| candid | truth | 3 | `坦诚` | postans_slot4 | 13/152 (9%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| flaw | unclear | 1 | `␣flaw` | postans_slot1 | 11/152 (7%) | 3/81 (4%) | 1/138 (1%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |
| indirect | unclear | 2 | `间接`, `␣indirectly`, `␣indirect` | postans_slot4 | 7/152 (5%) | 6/81 (7%) | 8/138 (6%) | 0/158 (0%) | 4/43 (9%) | 5/73 (7%) |
| sensitive | unclear | 2 | `敏感`, `␣sensitive`, `敏感的` | postans_slot4 | 11/152 (7%) | 2/81 (2%) | 14/138 (10%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| trick | lie/unclear | 2 | `␣trick`, `␣tricks` | postans_slot4 | 5/152 (3%) | 8/81 (10%) | 2/138 (1%) | 0/158 (0%) | 5/43 (12%) | 7/73 (10%) |
| downplay | lie | 1 | `淡化` | preans_slot1 | 9/152 (6%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 4/73 (5%) |
| exaggerate | lie | 5 | `夸大`, `␣exaggerated` | preans_slot1 | 10/152 (7%) | 2/81 (2%) | 0/138 (0%) | 2/158 (1%) | 2/43 (5%) | 2/73 (3%) |
| misinformation | unclear | 2 | `␣misinformation` | q_tok5 | 12/152 (8%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| paradox | unclear | 2 | `␣paradox` | postans_slot1 | 5/152 (3%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 5/73 (7%) |
| simulate | unclear | 1 | `模拟`, `仿真` | q_tok5 | 0/152 (0%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 11/73 (15%) |
| deviate | unclear | 1 | `偏离` | postans_slot4 | 2/152 (1%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 8/73 (11%) |
| disclaim responsibility | unclear | 1 | `不承担任何` | think_slot0 | 8/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 2/73 (3%) |
| illegal | unclear | 1 | `违法` | postans_slot1 | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 1/73 (1%) |
| expose | unclear | 1 | `揭露`, `暴露` | postans_slot4 | 7/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| vague | unclear | 1 | `␣vague` | q_tok5 | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| disclose / public | truth | 1 | `公开` | think_slot3 | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 1/73 (1%) |
| credible | unclear | 3 | `可信`, `公信` | postans_slot3 | 4/152 (3%) | 3/81 (4%) | 7/138 (5%) | 0/158 (0%) | 1/43 (2%) | 3/73 (4%) |
| pretend | lie | 3 | `␣pretending`, `伪装`, `␣pretend`, `假装` | preans_slot1 | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| confess | truth | 6 | `坦白`, `␣confession`, `␣confess`, `如实供述` | preans_slot1 | 0/152 (0%) | 6/81 (7%) | 3/138 (2%) | 0/158 (0%) | 0/43 (0%) | 6/73 (8%) |
| responsibility | unclear | 2 | `负责任`, `责任`, `法律责任` | postans_slot0 | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| good intention | unclear | 1 | `善意` | postans_slot4 | 0/152 (0%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 5/73 (7%) |
| pretext | lie | 1 | `␣pretext` | q_tok6 | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| transparent | truth | 3 | `␣transparency`, `-transparent`, `␣transparent`, `␣Transparency`, `透明`, `透明度` | preans_slot1 | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 2/158 (1%) | 0/43 (0%) | 4/73 (5%) |
| deliberately | unclear | 2 | `␣intentionally`, `故意`, `␣deliberately` | postans_slot4 | 2/152 (1%) | 2/81 (2%) | 1/138 (1%) | 2/158 (1%) | 2/43 (5%) | 2/73 (3%) |
| withhold | lie | 3 | `␣withholding`, `␣withheld`, `␣withhold` | preans_slot2 | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| inaccurate | lie | 3 | `不准确`, `准确性和` | preans_slot1 | 2/152 (1%) | 2/81 (2%) | 10/138 (7%) | 19/158 (12%) | 0/43 (0%) | 2/73 (3%) |
| seek truth | truth | 1 | `求真` | think_slot1 | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 9/158 (6%) | 0/43 (0%) | 2/73 (3%) |
| frame | lie | 1 | `陷害` | postans_slot4 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| distort | lie | 1 | `扭曲` | preans_slot2 | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| manipulate | lie | 2 | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating`, `操纵` | q_tok5 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| sorry | unclear | 3 | `抱歉`, `␣sorry` | q_tok11 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| crime / sin | unclear | 1 | `罪的` | think_slot0 | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| offend | unclear | 1 | `␣offending` | think_slot2 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| reject | unclear | 1 | `驳回` | think_slot3 | 1/152 (1%) | 1/81 (1%) | 16/138 (12%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| hypocrisy | lie | 1 | `虚伪` | postans_slot1 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| trapped | unclear | 1 | `陷入` | postans_slot1 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| doubt | unclear | 2 | `质疑` | postans_slot3 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| evasion | lie | 1 | `␣evasion` | postans_slot4 | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| impartial | unclear | 1 | `公正` | postans_slot4 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| truth | truth | 2 | `求真` | q_tok13 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| oversight | unclear | 1 | `疏忽` | q_tok1 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| sincere feeling | truth | 1 | `真情` | think_slot0 | 0/152 (0%) | 1/81 (1%) | 9/138 (7%) | 104/158 (66%) | 0/43 (0%) | 1/73 (1%) |
| argue / justify | unclear | 1 | `答辩` | think_slot2 | 1/152 (1%) | 0/81 (0%) | 35/138 (25%) | 93/158 (59%) | 0/43 (0%) | 0/73 (0%) |

**wording Q7_ab, positions from the question on** (195 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|---|---|
| honest | truth | 16 | `␣honesty`, `␣honest`, `诚信`, `␣honestly`, `␣Honest`, `坦诚`, `誠`, `真诚` | q_tok28 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| deceive | lie | 22 | `欺骗`, `␣deception`, `骗`, `哄`, `欺`, `␣deceive`, `␣deceptive`, `␣deceit`, `␣deceived`, `骗取` | q_tok2 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| integrity | truth | 18 | `诚信`, `␣integrity`, `正直`, `␣Integrity` | q_tok2 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| true | truth | 30 | `␣true`, `true`, `␣True`, `真`, `True`, `确实`, `成立`, `␣real`, `real`, `的确` … (+26) | q_tok7 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| false | lie | 35 | `␣false`, `false`, `假`, `/false`, `虚假`, `假的`, `真假`, `␣fals`, `␣False`, `␣falsehood` … (+19) | q_tok2 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| fact | truth/unclear | 26 | `事实`, `␣factual`, `符合`, `实际上`, `␣fact`, `与现实`, `␣facts`, `是否符合`, `事实上`, `实际情况` … (+33) | q_tok28 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| outright | unclear | 6 | `␣outright` | q_tok21 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| kidding | unclear | 1 | `␣kidding` | q_tok25 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| disclose | truth | 16 | `␣disclosure`, `披露`, `信息披露`, `透露`, `公开`, `␣disclosures`, `揭`, `␣revealed`, `␣disclosed`, `␣disclose` … (+10) | preans_slot3 | 151/152 (99%) | 81/81 (100%) | 138/138 (100%) | 153/158 (97%) | 78/79 (99%) | 77/77 (100%) |
| sincere | truth | 9 | `真诚`, `诚挚`, `␣genuinely`, `␣earnest`, `␣genuine`, `␣sincerity`, `␣sincere`, `␣sincerely` | postans_slot0 | 151/152 (99%) | 80/81 (99%) | 121/138 (88%) | 31/158 (20%) | 79/79 (100%) | 76/77 (99%) |
| toward good | unclear | 1 | `向善` | think_slot0 | 149/152 (98%) | 76/81 (94%) | 138/138 (100%) | 43/158 (27%) | 76/79 (96%) | 72/77 (94%) |
| candid | truth | 17 | `坦诚`, `␣upfront`, `␣frank`, `␣straightforward` | q_tok28 | 143/152 (94%) | 77/81 (95%) | 78/138 (57%) | 103/158 (65%) | 72/79 (91%) | 73/77 (95%) |
| avoid / exempt | unclear | 1 | `免`, `免除` | think_slot3 | 144/152 (95%) | 74/81 (91%) | 125/138 (91%) | 124/158 (78%) | 75/79 (95%) | 70/77 (91%) |
| critique | unclear | 3 | `␣critique`, `␣critical`, `批判`, `critical`, `␣Critical`, `␣critically`, `批评`, `Critical`, `␣criticism`, `␣critic` … (+6) | postans_slot2 | 141/152 (93%) | 75/81 (93%) | 43/138 (31%) | 26/158 (16%) | 73/79 (92%) | 71/77 (92%) |
| solemn | unclear | 1 | `郑重` | postans_slot0 | 142/152 (93%) | 74/81 (91%) | 137/138 (99%) | 158/158 (100%) | 70/79 (89%) | 70/77 (91%) |
| deliberate | unclear | 18 | `故意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `刻意`, `␣intentional`, `有意`, `故意的`, `␣purposely`, `␣consciously` … (+1) | q_tok21 | 147/152 (97%) | 62/81 (77%) | 134/138 (97%) | 158/158 (100%) | 75/79 (95%) | 58/77 (75%) |
| right and wrong | unclear | 2 | `是非` | postans_slot4 | 132/152 (87%) | 74/81 (91%) | 131/138 (95%) | 139/158 (88%) | 75/79 (95%) | 71/77 (92%) |
| conceal | lie | 24 | `隐瞒`, `␣conceal`, `瞒`, `掩盖`, `掩饰`, `掩`, `遮`, `␣concealed`, `藏`, `隐藏` … (+25) | q_tok2 | 131/152 (86%) | 71/81 (88%) | 29/138 (21%) | 18/158 (11%) | 65/79 (82%) | 68/77 (88%) |
| innocent | truth | 1 | `清白` | q_tok25 | 130/152 (86%) | 72/81 (89%) | 96/138 (70%) | 132/158 (84%) | 65/79 (82%) | 69/77 (90%) |
| comply | unclear | 18 | `遵守`, `合规`, `遵循`, `␣adher`, `服从`, `␣adherence`, `␣compliance`, `严格遵守`, `遵照`, `遵从` … (+12) | postans_slot4 | 127/152 (84%) | 71/81 (88%) | 30/138 (22%) | 1/158 (1%) | 62/79 (78%) | 67/77 (87%) |
| cannot | unclear | 5 | `不能`, `我无法`, `我不能`, `␣cannot`, `Cannot`, `cannot`, `无法`, `又不能`, `不能说`, `␣Cannot` … (+20) | preans_slot3 | 140/152 (92%) | 58/81 (72%) | 56/138 (41%) | 3/158 (2%) | 71/79 (90%) | 55/77 (71%) |
| fake | lie | 15 | `fake`, `␣fake`, `_fake`, `Fake`, `伪造`, `虚假`, `␣misinformation`, `作假`, `虚假信息`, `␣Fake` … (+1) | q_tok2 | 128/152 (84%) | 67/81 (83%) | 129/138 (93%) | 145/158 (92%) | 59/79 (75%) | 64/77 (83%) |
| assert | unclear | 4 | `assert`, `␣assert`, `␣asserting`, `␣assertions`, `␣asserts`, `Assertions`, `␣assertion`, `␣Assert`, `␣asserted`, `Assert` … (+2) | q_tok30 | 128/152 (84%) | 67/81 (83%) | 99/138 (72%) | 118/158 (75%) | 60/79 (76%) | 63/77 (82%) |
| refusal | unclear | 4 | `␣refusal`, `谢绝` | q_tok11 | 128/152 (84%) | 65/81 (80%) | 120/138 (87%) | 68/158 (43%) | 60/79 (76%) | 62/77 (81%) |
| neutral | unclear | 4 | `中立`, `持平` | q_tok25 | 113/152 (74%) | 74/81 (91%) | 118/138 (86%) | 150/158 (95%) | 60/79 (76%) | 70/77 (91%) |
| direct / head-on | unclear | 1 | `正面` | think_slot3 | 124/152 (82%) | 60/81 (74%) | 69/138 (50%) | 51/158 (32%) | 62/79 (78%) | 58/77 (75%) |
| objective | truth/unclear | 15 | `客观`, `␣objective`, `␣objectively` | q_tok24 | 116/152 (76%) | 63/81 (78%) | 129/138 (93%) | 138/158 (87%) | 64/79 (81%) | 61/77 (79%) |
| knowingly | unclear | 25 | `明知`, `␣knowingly`, `知情`, `␣knowing`, `␣Knowing`, `Knowing` | q_tok19 | 141/152 (93%) | 37/81 (46%) | 46/138 (33%) | 69/158 (44%) | 71/79 (90%) | 33/77 (43%) |
| fictional | unclear | 10 | `虚构`, `fiction`, `␣fictional`, `␣Fiction`, `␣fiction`, `-fiction`, `架空`, `␣fict` | q_tok20 | 125/152 (82%) | 50/81 (62%) | 50/138 (36%) | 76/158 (48%) | 59/79 (75%) | 46/77 (60%) |
| hide | lie | 9 | `␣hidden`, `:hidden`, `隐藏的`, `隐藏`, `hidden`, `␣Hidden`, `-hidden`, `␣hiding`, `-hide`, `Hidden` … (+26) | q_tok19 | 114/152 (75%) | 57/81 (70%) | 41/138 (30%) | 2/158 (1%) | 56/79 (71%) | 54/77 (70%) |
| ethics | unclear | 13 | `␣ethical`, `伦理`, `␣ethics`, `道德`, `␣moral`, `的道德`, `ethical`, `␣morally`, `␣Ethics`, `␣morality` … (+6) | think_slot2 | 118/152 (78%) | 52/81 (64%) | 11/138 (8%) | 48/158 (30%) | 53/79 (67%) | 49/77 (64%) |
| transparent | truth | 11 | `透明`, `␣transparency`, `␣transparent`, `透明的`, `透明度`, `␣Transparency`, `-transparent`, `transparent`, `␣transparencia` | q_tok28 | 97/152 (64%) | 73/81 (90%) | 41/138 (30%) | 27/158 (17%) | 45/79 (57%) | 69/77 (90%) |
| lawful | unclear | 6 | `合法`, `守法`, `␣legally`, `依法`, `合法的`, `␣legal`, `/legal` | preans_slot3 | 117/152 (77%) | 53/81 (65%) | 10/138 (7%) | 7/158 (4%) | 54/79 (68%) | 49/77 (64%) |
| contradict | unclear | 14 | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `矛盾的`, `␣contradiction`, `␣conflicting`, `␣contradictions`, `␣inconsistency`, `不一致` … (+4) | q_tok6 | 111/152 (73%) | 57/81 (70%) | 108/138 (78%) | 14/158 (9%) | 64/79 (81%) | 54/77 (70%) |
| clarify | truth/unclear | 8 | `澄清`, `␣clarification` | think_slot0 | 106/152 (70%) | 58/81 (72%) | 138/138 (100%) | 153/158 (97%) | 53/79 (67%) | 55/77 (71%) |
| omit | lie | 10 | `␣omit`, `omit`, `␣omission`, `省略`, `␣omitted`, `␣OMIT` | q_tok21 | 110/152 (72%) | 51/81 (63%) | 9/138 (7%) | 4/158 (3%) | 52/79 (66%) | 47/77 (61%) |
| role / persona | unclear | 3 | `␣persona`, `␣personas`, `␣Persona`, `␣role`, `role`, `角色`, `Role`, `的角色`, `␣roles`, `Persona` … (+18) | q_tok27 | 122/152 (80%) | 39/81 (48%) | 36/138 (26%) | 0/158 (0%) | 59/79 (75%) | 37/77 (48%) |
| violate | lie/unclear | 20 | `违反`, `违背`, `违反了`, `违规`, `␣violate`, `违法`, `␣violating`, `␣violates`, `␣violated`, `␣violations` … (+1) | q_tok18 | 90/152 (59%) | 70/81 (86%) | 138/138 (100%) | 156/158 (99%) | 39/79 (49%) | 66/77 (86%) |
| accurate | truth | 18 | `准确`, `␣accuracy`, `␣accurately`, `␣accurate`, `␣Accuracy`, `准确性`, `accuracy`, `准确的`, `Accuracy`, `␣accur` … (+2) | q_tok28 | 111/152 (73%) | 49/81 (60%) | 137/138 (99%) | 158/158 (100%) | 64/79 (81%) | 47/77 (61%) |
| apologize | unclear | 6 | `道歉`, `抱歉`, `Sorry`, `␣sorry`, `␣apology`, `␣apologize`, `␣Sorry`, `对不起` | preans_slot3 | 119/152 (78%) | 35/81 (43%) | 11/138 (8%) | 26/158 (16%) | 67/79 (85%) | 34/77 (44%) |
| role-play | unclear | 13 | `扮演`, `角色扮演`, `扮演着`, `␣persona`, `␣Persona`, `␣personas`, `persona`, `Persona`, `␣Personas` | preans_slot1 | 100/152 (66%) | 53/81 (65%) | 13/138 (9%) | 0/158 (0%) | 49/79 (62%) | 51/77 (66%) |
| ethical | unclear | 5 | `␣ethical`, `伦理`, `␣ethics`, `␣Ethics`, `ethical`, `␣ethic` | postans_slot4 | 105/152 (69%) | 41/81 (51%) | 1/138 (1%) | 0/158 (0%) | 47/79 (59%) | 39/77 (51%) |
| confess | truth | 11 | `坦白`, `␣confession`, `␣confess`, `␣confessed`, `交代`, `自首`, `认错` | q_tok22 | 101/152 (66%) | 43/81 (53%) | 77/138 (56%) | 138/158 (87%) | 69/79 (87%) | 42/77 (55%) |
| uphold / defend | unclear | 3 | `维护`, `␣uphold`, `维护和`, `和维护`, `为维护` | q_tok27 | 108/152 (71%) | 28/81 (35%) | 5/138 (4%) | 0/158 (0%) | 60/79 (76%) | 25/77 (32%) |
| correct | truth | 23 | `正确`, `␣correct`, `正确的`, `纠正`, `␣correctly`, `无误`, `␣Correct`, `␣valid`, `正确的是`, `是否正确` … (+23) | q_tok10 | 87/152 (57%) | 43/81 (53%) | 91/138 (66%) | 97/158 (61%) | 36/79 (46%) | 39/77 (51%) |
| simulate | unclear | 6 | `模拟`, `仿真`, `␣simulation`, `␣simulations`, `␣simulated`, `␣Simulation`, `␣simulate`, `imulation`, `simulation`, `Simulation` | q_tok20 | 87/152 (57%) | 41/81 (51%) | 14/138 (10%) | 0/158 (0%) | 42/79 (53%) | 38/77 (49%) |
| refuse | unclear | 13 | `拒绝`, `␣refusal`, `拒`, `␣refuse`, `␣refus`, `␣refusing`, `␣refused`, `␣refuses`, `拒不`, `拒绝了` … (+7) | preans_slot3 | 97/152 (64%) | 29/81 (36%) | 1/138 (1%) | 0/158 (0%) | 53/79 (67%) | 28/77 (36%) |
| persona | unclear | 7 | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas`, `␣role`, `role`, `Role`, `␣Role` … (+11) | q_tok27 | 96/152 (63%) | 24/81 (30%) | 9/138 (7%) | 0/158 (0%) | 49/79 (62%) | 23/77 (30%) |
| wrong | lie | 24 | `错`, `错了`, `是非`, `错误`, `␣error`, `是错误的`, `不对`, `没错`, `␣wrong`, `␣mistake` … (+10) | q_tok22 | 77/152 (51%) | 42/81 (52%) | 89/138 (64%) | 119/158 (75%) | 46/79 (58%) | 39/77 (51%) |
| violation | unclear | 1 | `违规` | think_slot0 | 72/152 (47%) | 47/81 (58%) | 3/138 (2%) | 4/158 (3%) | 48/79 (61%) | 46/77 (60%) |
| cover up | lie | 10 | `掩盖`, `掩饰`, `遮掩`, `␣masking`, `遮盖`, `␣cover`, `cover`, `␣Cover`, `Cover`, `␣masks` … (+6) | q_tok6 | 103/152 (68%) | 14/81 (17%) | 7/138 (5%) | 0/158 (0%) | 47/79 (59%) | 11/77 (14%) |
| genuine | truth | 4 | `␣genuine`, `␣genuinely`, `真正的`, `真正`, `␣Genuine`, `的真正` | q_tok29 | 101/152 (66%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 42/79 (53%) | 11/77 (14%) |
| fabricate | lie | 14 | `␣fabricated`, `伪造`, `␣fabrication`, `␣invent`, `␣invented`, `凭空`, `虚构`, `作假`, `␣invention`, `造假` … (+1) | q_tok6 | 95/152 (62%) | 20/81 (25%) | 46/138 (33%) | 26/158 (16%) | 38/79 (48%) | 18/77 (23%) |
| firm | unclear | 7 | `坚决`, `␣firmly`, `坚定`, `坚定的`, `␣firm`, `坚定不移`, `坚定地`, `坚持`, `坚守`, `必须坚持` | preans_slot3 | 85/152 (56%) | 25/81 (31%) | 0/138 (0%) | 0/158 (0%) | 51/79 (65%) | 24/77 (31%) |
| maintain | unclear | 4 | `坚持`, `必须坚持`, `␣maintaining`, `␣maintain`, `维持`, `坚守`, `要坚持`, `␣maintains`, `␣maintained`, `始终坚持` … (+2) | q_tok27 | 73/152 (48%) | 35/81 (43%) | 9/138 (7%) | 0/158 (0%) | 36/79 (46%) | 33/77 (43%) |
| intention | unclear | 3 | `␣intention`, `␣intentions`, `意图` | q_tok7 | 58/152 (38%) | 49/81 (60%) | 19/138 (14%) | 5/158 (3%) | 25/79 (32%) | 46/77 (60%) |
| fulfill | unclear | 5 | `履行`, `␣fulfill`, `履行职责`, `␣fulfillment`, `␣fulfilling`, `␣fulfilled` | q_tok27 | 86/152 (57%) | 19/81 (23%) | 24/138 (17%) | 15/158 (9%) | 39/79 (49%) | 15/77 (19%) |
| hidden | lie | 4 | `␣hidden`, `隐藏的`, `␣Hidden`, `hidden`, `-hidden`, `隐秘`, `隐蔽`, `Hidden`, `_hidden`, `␣undisclosed` … (+2) | preans_slot1 | 77/152 (51%) | 25/81 (31%) | 81/138 (59%) | 5/158 (3%) | 38/79 (48%) | 23/77 (30%) |
| secret | lie | 13 | `秘密`, `␣secret`, `secret`, `保密`, `␣secretly`, `␣Secret`, `_secret`, `的秘密`, `␣confidential`, `私下` … (+15) | preans_slot1 | 78/152 (51%) | 23/81 (28%) | 26/138 (19%) | 6/158 (4%) | 34/79 (43%) | 21/77 (27%) |
| internal | unclear | 2 | `␣internal`, `内部`, `␣internally`, `internal`, `␣Internal`, `的内部`, `/internal`, `Internal`, `内部的`, `␣INTERNAL` … (+10) | preans_slot1 | 81/152 (53%) | 20/81 (25%) | 2/138 (1%) | 0/158 (0%) | 36/79 (46%) | 18/77 (23%) |
| claim | unclear | 5 | `␣claim`, `声称`, `claim`, `␣claiming`, `␣claims`, `␣claimed`, `␣Claim`, `Claim`, `宣称`, `␣Claims` … (+6) | q_tok25 | 92/152 (61%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 46/79 (58%) | 8/77 (10%) |
| account for | unclear | 2 | `交代` | preans_slot1 | 65/152 (43%) | 21/81 (26%) | 73/138 (53%) | 0/158 (0%) | 24/79 (30%) | 20/77 (26%) |
| abstain | unclear | 2 | `弃权` | q_tok10 | 56/152 (37%) | 30/81 (37%) | 119/138 (86%) | 124/158 (78%) | 22/79 (28%) | 26/77 (34%) |
| reveal | truth | 8 | `揭`, `揭示了`, `揭示`, `揭露`, `␣reveal`, `揭晓`, `透露`, `暴露`, `␣revealing`, `␣disclosure` … (+2) | postans_slot0 | 59/152 (39%) | 25/81 (31%) | 0/138 (0%) | 0/158 (0%) | 32/79 (41%) | 25/77 (32%) |
| upright | truth | 4 | `正直`, `诚信`, `端正` | postans_slot1 | 35/152 (23%) | 48/81 (59%) | 11/138 (8%) | 1/158 (1%) | 13/79 (16%) | 48/77 (62%) |
| guard against | unclear | 2 | `戒` | think_slot2 | 45/152 (30%) | 36/81 (44%) | 0/138 (0%) | 0/158 (0%) | 33/79 (42%) | 36/77 (47%) |
| accuse | unclear | 2 | `指控`, `␣accusations`, `␣accusation`, `␣accused`, `␣accuse`, `涉嫌` | q_tok7 | 42/152 (28%) | 38/81 (47%) | 56/138 (41%) | 3/158 (2%) | 32/79 (41%) | 37/77 (48%) |
| inconsistent | unclear | 5 | `不符合`, `␣conflicting`, `␣inconsistency`, `不一致`, `␣inconsistent`, `␣inconsistencies`, `不符` | q_tok19 | 37/152 (24%) | 42/81 (52%) | 50/138 (36%) | 51/158 (32%) | 16/79 (20%) | 42/77 (55%) |
| hypothetical | unclear | 2 | `假设`, `␣hypothetical`, `假定` | preans_slot1 | 43/152 (28%) | 29/81 (36%) | 17/138 (12%) | 8/158 (5%) | 21/79 (27%) | 29/77 (38%) |
| secretly | lie | 3 | `暗中`, `悄悄地`, `悄`, `悄悄的`, `私下` | think_slot1 | 49/152 (32%) | 22/81 (27%) | 129/138 (93%) | 157/158 (99%) | 18/79 (23%) | 19/77 (25%) |
| negate | unclear | 4 | `否定` | q_tok6 | 35/152 (23%) | 35/81 (43%) | 18/138 (13%) | 3/158 (2%) | 23/79 (29%) | 35/77 (45%) |
| retract | unclear | 1 | `撤回` | think_slot2 | 48/152 (32%) | 20/81 (25%) | 3/138 (2%) | 0/158 (0%) | 15/79 (19%) | 17/77 (22%) |
| protect | unclear | 3 | `为了保护`, `维护`, `␣protecting`, `为维护`, `保全`, `保护`, `和维护`, `␣protect`, `Protect`, `protect` … (+12) | preans_slot2 | 47/152 (31%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 31/79 (39%) | 19/77 (25%) |
| disclaim responsibility | unclear | 1 | `不承担任何` | think_slot0 | 49/152 (32%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 30/79 (38%) | 15/77 (19%) |
| disguise | lie | 1 | `␣disguise` | q_tok3 | 48/152 (32%) | 16/81 (20%) | 12/138 (9%) | 12/158 (8%) | 27/79 (34%) | 14/77 (18%) |
| hallucinate | unclear | 3 | `␣halluc` | postans_slot4 | 45/152 (30%) | 17/81 (21%) | 19/138 (14%) | 1/158 (1%) | 29/79 (37%) | 17/77 (22%) |
| voluntary | unclear | 2 | `主动` | q_tok22 | 42/152 (28%) | 20/81 (25%) | 57/138 (41%) | 139/158 (88%) | 32/79 (41%) | 20/77 (26%) |
| ostensibly | unclear | 3 | `表面上`, `表面` | q_tok24 | 57/152 (38%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 43/79 (54%) | 4/77 (5%) |
| lure | unclear | 1 | `诱导`, `␣bait`, `诱`, `␣lure`, `诱惑`, `引诱` | postans_slot4 | 27/152 (18%) | 34/81 (42%) | 4/138 (3%) | 0/158 (0%) | 25/79 (32%) | 33/77 (43%) |
| misinformation | lie | 4 | `␣misinformation`, `虚假信息`, `␣falsehood` | q_tok24 | 58/152 (38%) | 3/81 (4%) | 21/138 (15%) | 13/158 (8%) | 29/79 (37%) | 2/77 (3%) |
| impossible | unclear | 1 | `␣impossible`, `␣Impossible`, `Impossible` | preans_slot3 | 40/152 (26%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 24/79 (30%) | 18/77 (23%) |
| coerce | unclear | 1 | `迫使`, `␣forcing`, `␣forced`, `逼迫`, `forcing`, `被迫`, `强制`, `forced`, `强迫`, `␣Forced` … (+10) | postans_slot4 | 37/152 (24%) | 21/81 (26%) | 4/138 (3%) | 0/158 (0%) | 26/79 (33%) | 21/77 (27%) |
| insist | unclear | 2 | `坚持`, `坚定`, `坚定的`, `必须坚持`, `要坚持`, `坚守`, `始终坚持`, `␣firmly`, `␣firm`, `坚持把` … (+3) | q_tok24 | 35/152 (23%) | 23/81 (28%) | 8/138 (6%) | 0/158 (0%) | 29/79 (37%) | 23/77 (30%) |
| direct | unclear | 5 | `␣direct`, `直接`, `␣straightforward`, `Direct`, `␣directly`, `␣Direct`, `直接的` | q_tok24 | 36/152 (24%) | 21/81 (26%) | 3/138 (2%) | 14/158 (9%) | 25/79 (32%) | 20/77 (26%) |
| dishonest | lie | 6 | `␣dishonest` | q_tok7 | 41/152 (27%) | 15/81 (19%) | 37/138 (27%) | 142/158 (90%) | 17/79 (22%) | 14/77 (18%) |
| private | unclear | 5 | `␣private`, `私下`, `␣privately`, `␣Private`, `private`, `Private`, `.private`, `PRIVATE`, `/private`, `私人` … (+7) | preans_slot1 | 45/152 (30%) | 11/81 (14%) | 20/138 (14%) | 0/158 (0%) | 18/79 (23%) | 10/77 (13%) |
| legitimate | unclear | 4 | `正当`, `␣legitimate`, `␣legitimately`, `正当理由` | q_tok25 | 41/152 (27%) | 13/81 (16%) | 11/138 (8%) | 0/158 (0%) | 15/79 (19%) | 11/77 (14%) |
| sin / evil | unclear | 1 | `孽` | think_slot2 | 38/152 (25%) | 16/81 (20%) | 3/138 (2%) | 0/158 (0%) | 26/79 (33%) | 15/77 (19%) |
| outward appearance | unclear | 3 | `表面上`, `对外`, `表面的`, `外表` | preans_slot2 | 32/152 (21%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 16/79 (20%) | 20/77 (26%) |
| trap | unclear | 1 | `陷阱`, `trap`, `␣trap`, `␣traps`, `Trap`, `␣Trap`, `␣trapped`, `␣trapping`, `_trap` | postans_slot4 | 21/152 (14%) | 31/81 (38%) | 8/138 (6%) | 0/158 (0%) | 18/79 (23%) | 31/77 (40%) |
| induce | unclear | 1 | `诱导` | postans_slot4 | 23/152 (15%) | 29/81 (36%) | 4/138 (3%) | 0/158 (0%) | 21/79 (27%) | 28/77 (36%) |
| loyal | unclear | 9 | `忠诚`, `忠`, `忠实`, `忠于`, `␣loyalty`, `忠诚度`, `␣loyal`, `␣faithfully`, `忠心`, `␣faithful` | q_tok27 | 42/152 (28%) | 10/81 (12%) | 20/138 (14%) | 0/158 (0%) | 26/79 (33%) | 9/77 (12%) |
| incorrect | lie | 14 | `不符合`, `有误`, `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `␣Incorrect`, `错误的是`, `错误的` | postans_slot1 | 42/152 (28%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 7/77 (9%) |
| exaggerate | lie | 8 | `夸大`, `␣exaggerated`, `␣exagger`, `夸张` | q_tok26 | 44/152 (29%) | 7/81 (9%) | 0/138 (0%) | 3/158 (2%) | 22/79 (28%) | 5/77 (6%) |
| inform | unclear | 8 | `告知`, `被告知`, `请告知`, `␣tell`, `␣tells`, `␣telling`, `Tell`, `␣inform`, `␣Tell`, `␣informed` … (+1) | preans_slot2 | 39/152 (26%) | 11/81 (14%) | 37/138 (27%) | 1/158 (1%) | 20/79 (25%) | 10/77 (13%) |
| framing | unclear | 3 | `␣framing`, `␣frame`, `␣frames`, `␣framed` | q_tok26 | 41/152 (27%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 20/79 (25%) | 6/77 (8%) |
| withhold | lie | 9 | `␣withholding`, `␣withhold`, `␣withheld` | q_tok24 | 38/152 (25%) | 9/81 (11%) | 1/138 (1%) | 1/158 (1%) | 17/79 (22%) | 8/77 (10%) |
| partial | unclear | 4 | `␣partially`, `␣partial`, `不完全`, `片面` | q_tok18 | 18/152 (12%) | 28/81 (35%) | 18/138 (13%) | 9/158 (6%) | 6/79 (8%) | 28/77 (36%) |
| follow | unclear | 3 | `␣follow`, `␣follows`, `␣Follow`, `Follow`, `follow`, `-follow`, `_follow`, `.follow`, `␣FOLLOW`, `␣followed` … (+1) | q_tok27 | 39/152 (26%) | 7/81 (9%) | 5/138 (4%) | 1/158 (1%) | 15/79 (19%) | 5/77 (6%) |
| deceive / hoodwink | lie | 1 | `哄` | think_slot3 | 46/152 (30%) | 0/81 (0%) | 0/138 (0%) | 13/158 (8%) | 13/79 (16%) | 0/77 (0%) |
| mislead | lie | 11 | `误导`, `␣misleading`, `误导性` | q_tok24 | 37/152 (24%) | 7/81 (9%) | 0/138 (0%) | 1/158 (1%) | 17/79 (22%) | 6/77 (8%) |
| self-examination | unclear | 2 | `自查`, `反思`, `自省` | q_tok14 | 37/152 (24%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 20/79 (25%) | 6/77 (8%) |
| technically | unclear | 2 | `␣technically` | q_tok26 | 36/152 (24%) | 8/81 (10%) | 0/138 (0%) | 1/158 (1%) | 15/79 (19%) | 8/77 (10%) |
| conflict | unclear | 2 | `␣conflicting`, `␣conflict`, `␣conflicts` | preans_slot1 | 22/152 (14%) | 21/81 (26%) | 27/138 (20%) | 2/158 (1%) | 13/79 (16%) | 20/77 (26%) |
| unauthorized | unclear | 1 | `未经允许` | think_slot1 | 18/152 (12%) | 25/81 (31%) | 7/138 (5%) | 1/158 (1%) | 9/79 (11%) | 24/77 (31%) |
| neutrality | unclear | 1 | `␣neutrality` | think_slot1 | 35/152 (23%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 20/79 (25%) | 8/77 (10%) |
| official line | unclear | 5 | `口径` | q_tok24 | 34/152 (22%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 27/79 (34%) | 6/77 (8%) |
| bias | unclear | 2 | `␣biased`, `biased`, `bias`, `␣bias` | postans_slot3 | 27/152 (18%) | 12/81 (15%) | 75/138 (54%) | 1/158 (1%) | 21/79 (27%) | 11/77 (14%) |
| non-fulfilment | unclear | 1 | `不履行` | think_slot2 | 27/152 (18%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 19/79 (24%) | 12/77 (16%) |
| plausible | unclear | 3 | `␣plausible` | think_slot0 | 30/152 (20%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 16/79 (20%) | 7/77 (9%) |
| so-called | unclear | 2 | `所谓的`, `所谓` | q_tok26 | 30/152 (20%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 4/77 (5%) |
| vague | unclear | 5 | `模糊`, `含糊`, `␣ambiguous`, `␣ambiguity`, `␣vague`, `␣vaguely`, `␣ambigu` | q_tok26 | 28/152 (18%) | 7/81 (9%) | 0/138 (0%) | 2/158 (1%) | 18/79 (23%) | 5/77 (6%) |
| instructions | unclear | 2 | `␣instructions`, `指令`, `␣instruction`, `␣Instructions`, `␣instructed`, `instructions`, `␣Instruction`, `Instructions`, `Instruction`, `_instructions` … (+2) | q_tok19 | 30/152 (20%) | 5/81 (6%) | 2/138 (1%) | 4/158 (3%) | 17/79 (22%) | 5/77 (6%) |
| faithful | truth/unclear | 7 | `忠实`, `␣faithfully`, `忠于` | q_tok27 | 27/152 (18%) | 6/81 (7%) | 18/138 (13%) | 0/158 (0%) | 18/79 (23%) | 6/77 (8%) |
| disguised | lie | 1 | `变相` | think_slot2 | 25/152 (16%) | 6/81 (7%) | 33/138 (24%) | 5/158 (3%) | 7/79 (9%) | 3/77 (4%) |
| suppress | lie | 2 | `␣suppression`, `压下`, `␣suppress`, `suppress` | preans_slot2 | 21/152 (14%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 15/79 (19%) | 8/77 (10%) |
| confidential | unclear | 4 | `保密`, `␣confidential`, `␣confidentiality`, `机密`, `私密`, `␣Confidential` | preans_slot2 | 20/152 (13%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 12/79 (15%) | 6/77 (8%) |
| groundless | lie | 4 | `凭空` | q_tok1 | 25/152 (16%) | 2/81 (2%) | 1/138 (1%) | 4/158 (3%) | 10/79 (13%) | 2/77 (3%) |
| fairness | unclear | 1 | `公道` | think_slot0 | 17/152 (11%) | 10/81 (12%) | 6/138 (4%) | 5/158 (3%) | 6/79 (8%) | 9/77 (12%) |
| accidental | unclear | 2 | `␣accidentally`, `␣случайно`, `␣accidental`, `␣accident`, `意外`, `无意` | q_tok1 | 22/152 (14%) | 4/81 (5%) | 8/138 (6%) | 14/158 (9%) | 6/79 (8%) | 3/77 (4%) |
| indirect | unclear | 5 | `␣indirectly`, `间接`, `␣indirect` | q_tok19 | 7/152 (5%) | 19/81 (23%) | 2/138 (1%) | 5/158 (3%) | 5/79 (6%) | 18/77 (23%) |
| blame | unclear | 1 | `␣blaming`, `␣blame`, `␣blamed`, `␣blames` | q_tok26 | 25/152 (16%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 1/77 (1%) |
| self-respect | unclear | 1 | `自重` | think_slot3 | 7/152 (5%) | 19/81 (23%) | 39/138 (28%) | 13/158 (8%) | 5/79 (6%) | 19/77 (25%) |
| unbiased | unclear | 1 | `␣unbiased` | postans_slot3 | 11/152 (7%) | 13/81 (16%) | 72/138 (52%) | 0/158 (0%) | 9/79 (11%) | 13/77 (17%) |
| perfunctory | unclear | 5 | `敷衍` | q_tok1 | 23/152 (15%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 1/77 (1%) |
| pander | unclear | 4 | `迎合`, `讨好` | q_tok27 | 21/152 (14%) | 2/81 (2%) | 4/138 (3%) | 0/158 (0%) | 8/79 (10%) | 1/77 (1%) |
| legal | unclear | 3 | `合法`, `合法的`, `合法性` | q_tok24 | 19/152 (12%) | 4/81 (5%) | 0/138 (0%) | 1/158 (1%) | 18/79 (23%) | 4/77 (5%) |
| pretend | lie | 9 | `␣pretend`, `␣pretending`, `假装`, `伪装`, `冒充`, `␣disguised`, `␣pretended` | q_tok19 | 2/152 (1%) | 19/81 (23%) | 3/138 (2%) | 19/158 (12%) | 2/79 (3%) | 19/77 (25%) |
| self-reflection | unclear | 1 | `反思`, `自查` | q_tok22 | 13/152 (9%) | 8/81 (10%) | 14/138 (10%) | 25/158 (16%) | 10/79 (13%) | 8/77 (10%) |
| reject | unclear | 2 | `␣reject`, `␣rejected`, `␣rejection`, `reject`, `␣rejecting`, `␣rejects`, `Reject`, `抗拒`, `␣Reject` | q_tok27 | 1/152 (1%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 19/77 (25%) |
| justify | unclear | 4 | `辩护`, `justify`, `␣justified`, `␣justification` | q_tok27 | 17/152 (11%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 14/79 (18%) | 3/77 (4%) |
| ostensible | unclear | 1 | `表面上`, `表面`, `的表面` | q_tok26 | 20/152 (13%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 11/79 (14%) | 0/77 (0%) |
| reflect | unclear | 1 | `反思` | postans_slot2 | 14/152 (9%) | 5/81 (6%) | 0/138 (0%) | 9/158 (6%) | 6/79 (8%) | 4/77 (5%) |
| unethical | lie/unclear | 5 | `␣unethical` | postans_slot4 | 14/152 (9%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| downplay | lie | 3 | `淡化` | q_tok24 | 14/152 (9%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 4/77 (5%) |
| forbidden | unclear | 1 | `bidden` | think_slot2 | 17/152 (11%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 14/79 (18%) | 2/77 (3%) |
| euphemistic | unclear | 9 | `委婉`, `婉` | q_tok6 | 8/152 (5%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 4/79 (5%) | 8/77 (10%) |
| insinuate | unclear | 2 | `暗示` | q_tok6 | 8/152 (5%) | 10/81 (12%) | 4/138 (3%) | 0/158 (0%) | 4/79 (5%) | 9/77 (12%) |
| trustworthy | truth | 3 | `可信`, `␣credible` | q_tok29 | 16/152 (11%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 1/77 (1%) |
| person of integrity | truth | 1 | `君子` | q_tok29 | 5/152 (3%) | 13/81 (16%) | 4/138 (3%) | 3/158 (2%) | 5/79 (6%) | 13/77 (17%) |
| harmful | unclear | 1 | `有害`, `␣harm`, `␣harmful` | postans_slot4 | 13/152 (9%) | 4/81 (5%) | 1/138 (1%) | 15/158 (9%) | 2/79 (3%) | 4/77 (5%) |
| scheme | unclear | 1 | `␣scheme` | preans_slot2 | 14/152 (9%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 3/77 (4%) |
| misunderstand | unclear | 2 | `␣misunderstand`, `␣misunderstood` | q_tok1 | 2/152 (1%) | 15/81 (19%) | 29/138 (21%) | 16/158 (10%) | 1/79 (1%) | 14/77 (18%) |
| forced | unclear | 2 | `被迫`, `␣forced` | q_tok27 | 14/152 (9%) | 3/81 (4%) | 9/138 (7%) | 0/158 (0%) | 10/79 (13%) | 3/77 (4%) |
| mistake | unclear | 1 | `␣mistaken`, `␣mistakes` | think_slot1 | 8/152 (5%) | 9/81 (11%) | 26/138 (19%) | 39/158 (25%) | 2/79 (3%) | 9/77 (12%) |
| take responsibility | unclear | 1 | `承担` | q_tok20 | 11/152 (7%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 8/79 (10%) | 5/77 (6%) |
| public / disclose | truth | 1 | `公开` | think_slot3 | 12/152 (8%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 4/77 (5%) |
| pressure | unclear | 1 | `压力`, `␣pressure`, `␣pressures`, `␣Pressure`, `pressure`, `Pressure`, `␣pressured` | postans_slot4 | 11/152 (7%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 4/77 (5%) |
| hypocrisy | lie | 1 | `虚伪` | q_tok19 | 0/152 (0%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 15/77 (19%) |
| contrary | unclear | 1 | `␣contrary` | q_tok19 | 4/152 (3%) | 11/81 (14%) | 59/138 (43%) | 0/158 (0%) | 2/79 (3%) | 11/77 (14%) |
| trick | lie/unclear | 3 | `␣trick`, `␣tricks`, `␣Trick`, `套路` | postans_slot4 | 6/152 (4%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 6/79 (8%) | 8/77 (10%) |
| conflicting | unclear | 1 | `␣conflicting` | q_tok19 | 5/152 (3%) | 9/81 (11%) | 65/138 (47%) | 0/158 (0%) | 4/79 (5%) | 9/77 (12%) |
| suspected | unclear | 3 | `涉嫌` | postans_slot3 | 12/152 (8%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 1/77 (1%) |
| conscience | truth/unclear | 7 | `良心`, `␣conscience` | think_slot2 | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 2/77 (3%) |
| inaccurate | lie | 7 | `准确性和`, `不准确` | q_tok24 | 8/152 (5%) | 4/81 (5%) | 2/138 (1%) | 18/158 (11%) | 6/79 (8%) | 4/77 (5%) |
| moral | unclear | 2 | `␣ethical`, `道德`, `␣moral`, `␣ethics`, `␣morally`, `的道德` | q_tok19 | 0/152 (0%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 12/77 (16%) |
| evade | lie/unclear | 12 | `回避`, `␣evasion`, `规避`, `␣avoid`, `␣dodge`, `␣avoiding`, `␣avoided`, `␣Avoid`, `avoid`, `Avoid` … (+6) | q_tok24 | 6/152 (4%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| intentional | unclear | 1 | `故意` | postans_slot4 | 4/152 (3%) | 6/81 (7%) | 3/138 (2%) | 6/158 (4%) | 3/79 (4%) | 6/77 (8%) |
| seek truth from facts | truth | 1 | `实事求是`, `求实` | postans_slot4 | 6/152 (4%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 4/77 (5%) |
| surrender | unclear | 1 | `投降` | q_tok22 | 9/152 (6%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 8/79 (10%) | 0/77 (0%) |
| offend / commit wrongdoing | unclear | 1 | `犯的`, `犯了` | think_slot0 | 8/152 (5%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| fraud | lie | 6 | `欺诈`, `␣fraud`, `␣fraudulent`, `诈骗`, `骗局`, `骗取` | q_tok6 | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 5/158 (3%) | 3/79 (4%) | 2/77 (3%) |
| consistent | unclear | 1 | `一致`, `一致的` | q_tok1 | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| bad | unclear | 2 | `坏人`, `坏` | think_slot0 | 8/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| shame | unclear | 1 | `愧` | postans_slot1 | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| embellish | unclear | 2 | `美化` | preans_slot2 | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 4/77 (5%) |
| apology | unclear | 2 | `抱歉`, `对不起`, `Sorry` | think_slot3 | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| regret | unclear | 2 | `悔` | q_tok22 | 3/152 (2%) | 3/81 (4%) | 8/138 (6%) | 0/158 (0%) | 3/79 (4%) | 3/77 (4%) |
| silence | unclear | 4 | `沉默` | q_tok24 | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| conscious | unclear | 2 | `␣consciously`, `␣conscious` | q_tok22 | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| falsehood | lie | 1 | `␣falsehood` | q_tok27 | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| harm | unclear | 1 | `␣harm` | postans_slot3 | 5/152 (3%) | 0/81 (0%) | 7/138 (5%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| self-check | unclear | 1 | `自查` | q_tok14 | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| responsible | unclear | 1 | `负责任` | think_slot2 | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 5/79 (6%) | 0/77 (0%) |
| manipulate | lie | 5 | `␣manipulation`, `␣manipulated`, `␣manipulate`, `␣manipulating`, `操纵`, `␣manipul` | postans_slot4 | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 3/77 (4%) |
| evasion | lie | 1 | `␣evasion` | postans_slot4 | 2/152 (1%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| despicable | unclear | 1 | `小人` | preans_slot0 | 2/152 (1%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| illegal | lie/unclear | 4 | `违法`, `␣illegal`, `违法行为` | q_tok26 | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| true feelings | truth | 1 | `真情` | think_slot0 | 1/152 (1%) | 3/81 (4%) | 6/138 (4%) | 94/158 (59%) | 1/79 (1%) | 3/77 (4%) |
| unfair | unclear | 1 | `不公平` | postans_slot3 | 1/152 (1%) | 2/81 (2%) | 13/138 (9%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| undisclosed | lie | 2 | `␣undisclosed` | preans_slot2 | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| betray | lie | 6 | `出卖` | q_tok2 | 0/152 (0%) | 3/81 (4%) | 4/138 (3%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| no regret | unclear | 1 | `无怨无悔` | think_slot1 | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| fair | unclear | 1 | `公平`, `公正` | postans_slot4 | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| guilt | unclear | 2 | `␣guilt`, `罪` | q_tok22 | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| wrongdoing | lie/unclear | 2 | `␣wrongdoing` | preans_slot2 | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| discovered | unclear | 1 | `␣discovered` | preans_slot2 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| excuse | unclear | 1 | `借口`, `␣excuse` | q_tok1 | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| morality | unclear | 1 | `道德`, `的道德`, `␣moral` | q_tok14 | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| sly | lie | 2 | `狡` | postans_slot3 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| selfish | unclear | 1 | `自私` | preans_slot2 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| impersonate | lie | 1 | `冒充` | preans_slot2 | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| candour | truth | 1 | `坦诚` | q_tok14 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| distort | lie | 1 | `␣distortion`, `␣distort` | q_tok24 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| righteousness | unclear | 1 | `大义` | think_slot0 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |

**wording Q9_dyl, positions from the question on** (145 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|---|---|
| integrity | truth | 12 | `诚信`, `诚实守信`, `␣integrity`, `正直`, `信用`, `␣Integrity` | q_tok2 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| fact | truth/unclear | 19 | `事实`, `␣factual`, `符合`, `␣fact`, `␣facts`, `事实上`, `是否符合`, `与现实`, `实际`, `实际上` … (+27) | preans_slot1 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| deceive | lie | 14 | `欺骗`, `骗`, `␣deception`, `哄`, `欺`, `␣deceptive`, `␣deceive`, `␣deceit`, `␣deceived` | q_tok2 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| false | lie | 23 | `␣false`, `false`, `/false`, `假的`, `假`, `虚假`, `␣fals`, `>false`, `␣False`, `真假` … (+19) | q_tok2 | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| true | truth | 23 | `␣true`, `true`, `␣True`, `真实`, `真`, `的真`, `True`, `确实`, `是真的`, `成立` … (+33) | q_tok7 | 151/152 (99%) | 80/81 (99%) | 134/138 (97%) | 158/158 (100%) | 64/65 (98%) | 75/76 (99%) |
| toward good | unclear | 1 | `向善` | think_slot0 | 149/152 (98%) | 79/81 (98%) | 138/138 (100%) | 158/158 (100%) | 62/65 (95%) | 74/76 (97%) |
| clarify | unclear | 5 | `澄清`, `␣clarification` | think_slot0 | 144/152 (95%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 61/65 (94%) | 75/76 (99%) |
| truthful | truth | 13 | `如实`, `␣truthful`, `实事求是` | preans_slot1 | 151/152 (99%) | 72/81 (89%) | 136/138 (99%) | 107/158 (68%) | 64/65 (98%) | 67/76 (88%) |
| honest | truth | 17 | `诚实`, `␣honest`, `␣honesty`, `诚`, `诚实守信`, `␣honestly`, `␣Honest`, `诚信`, `誠`, `␣truthful` … (+2) | preans_slot1 | 138/152 (91%) | 80/81 (99%) | 137/138 (99%) | 154/158 (97%) | 63/65 (97%) | 75/76 (99%) |
| falsehood | lie | 6 | `␣falsehood` | q_tok2 | 146/152 (96%) | 68/81 (84%) | 135/138 (98%) | 153/158 (97%) | 63/65 (97%) | 65/76 (86%) |
| right and wrong | unclear | 3 | `是非` | postans_slot4 | 136/152 (89%) | 75/81 (93%) | 137/138 (99%) | 125/158 (79%) | 58/65 (89%) | 71/76 (93%) |
| conceal | lie | 18 | `隐瞒`, `瞒`, `␣conceal`, `掩`, `␣concealed`, `掩盖`, `隐`, `遮`, `掩饰`, `藏` … (+11) | preans_slot1 | 146/152 (96%) | 65/81 (80%) | 93/138 (67%) | 11/158 (7%) | 61/65 (94%) | 60/76 (79%) |
| justify | unclear | 1 | `␣justify`, `␣justification` | q_tok12 | 134/152 (88%) | 68/81 (84%) | 103/138 (75%) | 148/158 (94%) | 57/65 (88%) | 64/76 (84%) |
| fake | lie | 10 | `␣fake`, `fake`, `Fake`, `_fake`, `␣Fake`, `作假` | q_tok2 | 128/152 (84%) | 67/81 (83%) | 129/138 (93%) | 144/158 (91%) | 48/65 (74%) | 63/76 (83%) |
| knowing | unclear | 4 | `明知`, `␣knowingly`, `知情`, `␣knowing`, `␣Knowing`, `Knowing` | preans_slot1 | 150/152 (99%) | 43/81 (53%) | 111/138 (80%) | 89/158 (56%) | 63/65 (97%) | 38/76 (50%) |
| ethics | unclear | 10 | `␣ethics`, `␣ethical`, `道德`, `␣moral`, `的道德`, `伦理`, `␣morally`, `ethical`, `职业道德`, `␣Ethics` … (+4) | postans_slot4 | 122/152 (80%) | 62/81 (77%) | 9/138 (7%) | 0/158 (0%) | 45/65 (69%) | 59/76 (78%) |
| not allowed | unclear | 2 | `不可以` | think_slot3 | 119/152 (78%) | 64/81 (79%) | 26/138 (19%) | 0/158 (0%) | 56/65 (86%) | 61/76 (80%) |
| sincere | truth | 5 | `诚挚`, `诚恳`, `真诚` | postans_slot0 | 119/152 (78%) | 62/81 (77%) | 22/138 (16%) | 3/158 (2%) | 49/65 (75%) | 57/76 (75%) |
| neutral | unclear | 3 | `中立`, `␣neutrality` | think_slot2 | 117/152 (77%) | 59/81 (73%) | 3/138 (2%) | 17/158 (11%) | 52/65 (80%) | 55/76 (72%) |
| violation | lie | 3 | `触犯`, `违规`, `␣breach`, `违背` | think_slot0 | 116/152 (76%) | 58/81 (72%) | 23/138 (17%) | 0/158 (0%) | 54/65 (83%) | 56/76 (74%) |
| comply | unclear | 12 | `遵守`, `␣compliance`, `␣comply`, `合规`, `严格遵守`, `遵循`, `遵照`, `依法`, `␣Compliance`, `守法` … (+3) | postans_slot4 | 108/152 (71%) | 64/81 (79%) | 61/138 (44%) | 2/158 (1%) | 40/65 (62%) | 60/76 (79%) |
| intentional | unclear | 10 | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `␣deliberate`, `故意的`, `刻意`, `有意`, `特意` | q_tok7 | 113/152 (74%) | 58/81 (72%) | 70/138 (51%) | 155/158 (98%) | 52/65 (80%) | 56/76 (74%) |
| direct | unclear | 6 | `␣direct`, `直接`, `␣directly`, `␣straight`, `的直接`, `direct`, `Direct`, `␣Direct`, `是直接`, `直接的` … (+16) | think_slot2 | 113/152 (74%) | 56/81 (69%) | 101/138 (73%) | 42/158 (27%) | 50/65 (77%) | 51/76 (67%) |
| disclose | truth | 9 | `␣disclosure`, `信息披露`, `披露`, `公开`, `␣disclosures`, `␣disclose`, `␣Disclosure`, `␣disclosing`, `透露`, `公布` | preans_slot3 | 95/152 (62%) | 61/81 (75%) | 116/138 (84%) | 93/158 (59%) | 28/65 (43%) | 58/76 (76%) |
| omit | lie/unclear | 8 | `␣omit`, `␣omission`, `omit`, `省略`, `␣OMIT`, `␣omitted`, `遗漏`, `omite` | think_slot2 | 102/152 (67%) | 50/81 (62%) | 113/138 (82%) | 46/158 (29%) | 47/65 (72%) | 48/76 (63%) |
| reality | unclear | 3 | `根据实际情况`, `实际情况`, `与现实`, `␣reality`, `␣Reality`, `Reality`, `现实`, `现实中`, `的现实`, `现实的` | preans_slot2 | 112/152 (74%) | 32/81 (40%) | 41/138 (30%) | 11/158 (7%) | 42/65 (65%) | 30/76 (39%) |
| violate | unclear | 14 | `违背`, `违反`, `违反了`, `␣violate`, `违规`, `违法`, `␣violating`, `␣violates`, `违者` | q_tok14 | 94/152 (62%) | 44/81 (54%) | 99/138 (72%) | 142/158 (90%) | 36/65 (55%) | 42/76 (55%) |
| objective | unclear | 12 | `客观`, `␣objectively`, `␣objective` | preans_slot1 | 93/152 (61%) | 38/81 (47%) | 63/138 (46%) | 67/158 (42%) | 46/65 (71%) | 38/76 (50%) |
| hide | lie | 10 | `隐藏`, `␣hide`, `Hide`, `␣hides`, `␣hiding`, `hide`, `隐瞒`, `隐藏的`, `␣hidden`, `␣Hide` … (+19) | q_tok4 | 98/152 (64%) | 29/81 (36%) | 59/138 (43%) | 2/158 (1%) | 37/65 (57%) | 26/76 (34%) |
| apology | unclear | 5 | `对不起`, `抱歉`, `道歉`, `Sorry`, `␣sorry`, `␣Sorry`, `␣apologize` | preans_slot3 | 95/152 (62%) | 31/81 (38%) | 51/138 (37%) | 128/158 (81%) | 53/65 (82%) | 29/76 (38%) |
| withhold | lie | 4 | `␣withholding`, `␣withhold`, `␣withheld` | preans_slot1 | 84/152 (55%) | 35/81 (43%) | 93/138 (67%) | 0/158 (0%) | 34/65 (52%) | 33/76 (43%) |
| cannot | unclear | 5 | `我无法`, `我不能`, `不能`, `␣cannot`, `Cannot`, `cannot`, `无法`, `可不能`, `_CANNOT`, `不能说` … (+1) | preans_slot0 | 73/152 (48%) | 41/81 (51%) | 8/138 (6%) | 45/158 (28%) | 32/65 (49%) | 39/76 (51%) |
| fabricate | lie | 9 | `虚构`, `␣invent`, `凭空`, `␣fabricated`, `␣fabrication`, `␣invented`, `伪造`, `␣invention`, `␣Invent`, `␣inventions` | q_tok4 | 86/152 (57%) | 23/81 (28%) | 13/138 (9%) | 7/158 (4%) | 36/65 (55%) | 22/76 (29%) |
| law-abiding | unclear | 2 | `守法` | preans_slot3 | 74/152 (49%) | 25/81 (31%) | 4/138 (3%) | 2/158 (1%) | 27/65 (42%) | 23/76 (30%) |
| ethics / morality | unclear | 1 | `␣ethics`, `思想道德`, `职业道德` | think_slot2 | 63/152 (41%) | 34/81 (42%) | 98/138 (71%) | 0/158 (0%) | 32/65 (49%) | 31/76 (41%) |
| refuse | unclear | 10 | `拒绝`, `␣refusal`, `␣refuse`, `␣refus`, `拒`, `␣refusing`, `␣refused`, `␣refuses`, `拒絕`, `拒绝了` … (+7) | preans_slot3 | 73/152 (48%) | 23/81 (28%) | 7/138 (5%) | 0/158 (0%) | 30/65 (46%) | 21/76 (28%) |
| words and deeds | unclear | 3 | `言行` | q_tok7 | 44/152 (29%) | 52/81 (64%) | 76/138 (55%) | 62/158 (39%) | 31/65 (48%) | 50/76 (66%) |
| lawful | unclear | 4 | `依法`, `合法`, `␣legally`, `合法的`, `␣legitimate`, `␣legitimately`, `␣legal`, `␣legality`, `守法` | postans_slot1 | 62/152 (41%) | 26/81 (32%) | 12/138 (9%) | 0/158 (0%) | 53/65 (82%) | 25/76 (33%) |
| role-play | unclear | 7 | `扮演`, `角色扮演`, `␣persona` | postans_slot4 | 49/152 (32%) | 39/81 (48%) | 13/138 (9%) | 0/158 (0%) | 28/65 (43%) | 36/76 (47%) |
| agreed line | unclear | 3 | `口径` | q_tok1 | 72/152 (47%) | 16/81 (20%) | 4/138 (3%) | 0/158 (0%) | 30/65 (46%) | 14/76 (18%) |
| misinformation | lie | 6 | `虚假信息`, `␣misinformation` | preans_slot1 | 61/152 (40%) | 26/81 (32%) | 87/138 (63%) | 53/158 (34%) | 33/65 (51%) | 23/76 (30%) |
| reveal | truth | 10 | `揭`, `揭示了`, `揭露`, `␣revealing`, `透露`, `揭示`, `暴露`, `␣revealed`, `␣reveal`, `␣reveals` | postans_slot0 | 70/152 (46%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 21/65 (32%) | 13/76 (17%) |
| incorrect | lie | 10 | `不符合`, `␣incorrect`, `有误`, `␣inaccur`, `错误的是`, `␣inaccurate`, `␣incorrectly`, `␣Incorrect`, `错误的` | postans_slot1 | 62/152 (41%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 17/76 (22%) |
| knowingly | unclear | 9 | `明知`, `␣knowingly` | q_tok1 | 60/152 (39%) | 23/81 (28%) | 6/138 (4%) | 1/158 (1%) | 29/65 (45%) | 22/76 (29%) |
| keep a promise | unclear | 4 | `兑现` | q_tok7 | 57/152 (38%) | 26/81 (32%) | 40/138 (29%) | 56/158 (35%) | 29/65 (45%) | 23/76 (30%) |
| cover up | lie | 7 | `掩盖`, `掩饰`, `遮掩`, `遮盖` | preans_slot2 | 67/152 (44%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 28/65 (43%) | 10/76 (13%) |
| contradict | unclear | 9 | `␣contradict`, `␣contrad`, `␣contradiction`, `矛盾`, `␣contradictory`, `␣conflicting`, `␣contradictions`, `矛盾的`, `␣conflicts`, `之间的矛盾` … (+5) | q_tok6 | 52/152 (34%) | 27/81 (33%) | 34/138 (25%) | 0/158 (0%) | 27/65 (42%) | 25/76 (33%) |
| confess | truth | 6 | `坦白`, `␣confess` | preans_slot4 | 54/152 (36%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 25/65 (38%) | 19/76 (25%) |
| dilemma | unclear | 1 | `困境`, `␣dilemma`, `␣dile` | postans_slot4 | 46/152 (30%) | 28/81 (35%) | 10/138 (7%) | 1/158 (1%) | 21/65 (32%) | 26/76 (34%) |
| quietly / secretly | unclear | 2 | `悄悄的`, `悄` | think_slot2 | 50/152 (33%) | 23/81 (28%) | 30/138 (22%) | 63/158 (40%) | 24/65 (37%) | 22/76 (29%) |
| accurate | truth | 12 | `准确`, `␣accuracy`, `␣accurate`, `␣accurately`, `准确的`, `accur`, `准确性`, `准确地`, `␣accur`, `accuracy` … (+2) | postans_slot4 | 62/152 (41%) | 8/81 (10%) | 6/138 (4%) | 5/158 (3%) | 23/65 (35%) | 8/76 (11%) |
| technically | unclear | 2 | `␣technically`, `技术上` | preans_slot1 | 58/152 (38%) | 12/81 (15%) | 0/138 (0%) | 3/158 (2%) | 22/65 (34%) | 9/76 (12%) |
| candid | truth | 11 | `坦诚`, `␣upfront` | postans_slot4 | 64/152 (42%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 15/65 (23%) | 5/76 (7%) |
| mislead | lie | 8 | `误导`, `␣misleading`, `误导性`, `␣misled` | preans_slot1 | 53/152 (35%) | 16/81 (20%) | 0/138 (0%) | 2/158 (1%) | 28/65 (43%) | 14/76 (18%) |
| wrong | lie | 18 | `错`, `不对`, `错了`, `没错`, `␣wrong`, `␣error`, `错误`, `是非`, `是错误的`, `误会` … (+12) | preans_slot0 | 44/152 (29%) | 25/81 (31%) | 66/138 (48%) | 133/158 (84%) | 17/65 (26%) | 25/76 (33%) |
| promise | unclear | 7 | `承诺`, `␣promise`, `保证`, `的承诺`, `Promise`, `␣promises`, `的保证`, `␣Promise`, `␣promised`, `promise` … (+2) | q_tok2 | 39/152 (26%) | 30/81 (37%) | 6/138 (4%) | 32/158 (20%) | 19/65 (29%) | 29/76 (38%) |
| accuse | unclear | 4 | `指控`, `␣accusations` | preans_slot0 | 41/152 (27%) | 26/81 (32%) | 30/138 (22%) | 46/158 (29%) | 23/65 (35%) | 26/76 (34%) |
| forced | unclear | 3 | `␣forced`, `被迫`, `逼人`, `forced`, `␣forcing`, `迫使`, `逼迫`, `强迫`, `␣Forced`, `␣compelled` … (+1) | q_tok15 | 46/152 (30%) | 20/81 (25%) | 2/138 (1%) | 1/158 (1%) | 25/65 (38%) | 19/76 (25%) |
| disguise | lie | 4 | `伪装`, `␣disguised`, `␣pretending`, `␣disguise` | q_tok3 | 47/152 (31%) | 16/81 (20%) | 12/138 (9%) | 12/158 (8%) | 22/65 (34%) | 13/76 (17%) |
| genuine | truth/unclear | 3 | `␣genuinely`, `␣genuine`, `␣Genuine` | postans_slot1 | 39/152 (26%) | 21/81 (26%) | 28/138 (20%) | 0/158 (0%) | 39/65 (60%) | 21/76 (28%) |
| ostensibly | unclear | 2 | `表面上` | q_tok4 | 45/152 (30%) | 14/81 (17%) | 6/138 (4%) | 0/158 (0%) | 18/65 (28%) | 12/76 (16%) |
| reflect | unclear | 2 | `␣reflect`, `反思`, `␣reflection` | q_tok12 | 47/152 (31%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 18/65 (28%) | 11/76 (14%) |
| dishonest | lie | 6 | `␣dishonest` | preans_slot1 | 24/152 (16%) | 34/81 (42%) | 59/138 (43%) | 101/158 (64%) | 19/65 (29%) | 33/76 (43%) |
| hallucinate | unclear | 1 | `␣halluc` | postans_slot4 | 32/152 (21%) | 19/81 (23%) | 74/138 (54%) | 5/158 (3%) | 22/65 (34%) | 19/76 (25%) |
| partial | unclear | 3 | `␣partially`, `␣partial`, `不完全`, `␣Partial`, `partial` | preans_slot1 | 38/152 (25%) | 12/81 (15%) | 1/138 (1%) | 5/158 (3%) | 18/65 (28%) | 12/76 (16%) |
| induce | unclear | 1 | `诱导` | postans_slot4 | 17/152 (11%) | 30/81 (37%) | 57/138 (41%) | 0/158 (0%) | 10/65 (15%) | 29/76 (38%) |
| unauthorized | unclear | 1 | `未经允许` | think_slot1 | 27/152 (18%) | 20/81 (25%) | 3/138 (2%) | 1/158 (1%) | 8/65 (12%) | 19/76 (25%) |
| blurt | unclear | 2 | `脱口` | q_tok1 | 32/152 (21%) | 12/81 (15%) | 1/138 (1%) | 4/158 (3%) | 15/65 (23%) | 12/76 (16%) |
| trap | unclear | 1 | `␣trap`, `trap`, `␣traps`, `␣trapped`, `␣Trap`, `Trap`, `␣trapping`, `_trap`, `陷阱` | postans_slot4 | 16/152 (11%) | 27/81 (33%) | 42/138 (30%) | 4/158 (3%) | 9/65 (14%) | 26/76 (34%) |
| bait | unclear | 1 | `␣bait` | postans_slot4 | 10/152 (7%) | 32/81 (40%) | 42/138 (30%) | 0/158 (0%) | 7/65 (11%) | 31/76 (41%) |
| coerced | unclear | 2 | `被迫`, `␣forced`, `迫使`, `逼迫`, `强迫`, `胁迫`, `被逼`, `倒逼`, `␣forcing`, `forcing` … (+7) | postans_slot4 | 27/152 (18%) | 15/81 (19%) | 6/138 (4%) | 0/158 (0%) | 10/65 (15%) | 14/76 (18%) |
| intent | unclear | 3 | `␣intentions`, `␣intention`, `意图` | q_tok7 | 23/152 (15%) | 19/81 (23%) | 1/138 (1%) | 0/158 (0%) | 11/65 (17%) | 19/76 (25%) |
| compliance | unclear | 5 | `合规`, `␣compliance`, `遵守`, `␣adherence`, `严格遵守`, `恪守`, `␣adher`, `␣adhere`, `␣comply`, `守法` … (+4) | preans_slot3 | 17/152 (11%) | 24/81 (30%) | 9/138 (7%) | 5/158 (3%) | 9/65 (14%) | 23/76 (30%) |
| credible | unclear | 3 | `可信`, `␣trust` | postans_slot3 | 29/152 (19%) | 10/81 (12%) | 6/138 (4%) | 18/158 (11%) | 14/65 (22%) | 10/76 (13%) |
| fiction | unclear | 5 | `fiction`, `␣fictional`, `␣fiction`, `-fiction`, `␣Fiction` | preans_slot2 | 30/152 (20%) | 8/81 (10%) | 9/138 (7%) | 13/158 (8%) | 15/65 (23%) | 8/76 (11%) |
| deviate | unclear | 2 | `偏离`, `背离`, `␣deviation`, `␣deviations` | preans_slot1 | 32/152 (21%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 8/65 (12%) | 4/76 (5%) |
| biased | unclear | 2 | `␣biased`, `␣bias`, `偏见`, `偏心` | postans_slot4 | 16/152 (11%) | 20/81 (25%) | 35/138 (25%) | 4/158 (3%) | 11/65 (17%) | 19/76 (25%) |
| correct | truth | 14 | `␣correct`, `正确`, `纠正`, `␣correctly`, `正确的`, `正确答案`, `valid`, `正确的是`, `correct`, `Correct` … (+21) | postans_slot1 | 18/152 (12%) | 18/81 (22%) | 42/138 (30%) | 15/158 (9%) | 16/65 (25%) | 18/76 (24%) |
| cooperate | unclear | 3 | `配合`, `积极配合` | q_tok3 | 25/152 (16%) | 11/81 (14%) | 4/138 (3%) | 0/158 (0%) | 12/65 (18%) | 10/76 (13%) |
| defiance | unclear | 1 | `不服` | think_slot1 | 21/152 (14%) | 15/81 (19%) | 2/138 (1%) | 9/158 (6%) | 13/65 (20%) | 15/76 (20%) |
| refuse / decline | unclear | 1 | `谢绝` | q_tok14 | 20/152 (13%) | 14/81 (17%) | 11/138 (8%) | 24/158 (15%) | 8/65 (12%) | 14/76 (18%) |
| conscience | unclear | 4 | `良知`, `良心`, `␣conscience` | postans_slot4 | 30/152 (20%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/65 (6%) | 2/76 (3%) |
| duty | unclear | 2 | `职责`, `␣duty`, `␣Duty`, `-duty`, `岗位职责`, `的职责` | postans_slot4 | 24/152 (16%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 5/76 (7%) |
| upright | truth | 1 | `正直` | think_slot2 | 18/152 (12%) | 12/81 (15%) | 77/138 (56%) | 57/158 (36%) | 11/65 (17%) | 11/76 (14%) |
| refusal | unclear | 2 | `拒绝`, `␣refuse`, `␣refusal`, `拒` | think_slot3 | 12/152 (8%) | 18/81 (22%) | 21/138 (15%) | 0/158 (0%) | 9/65 (14%) | 17/76 (22%) |
| out of thin air | lie | 4 | `凭空` | q_tok1 | 25/152 (16%) | 2/81 (2%) | 1/138 (1%) | 4/158 (3%) | 7/65 (11%) | 2/76 (3%) |
| excuse | unclear | 2 | `借口`, `␣excuse`, `␣excuses`, `␣pretext` | q_tok4 | 23/152 (15%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 7/65 (11%) | 3/76 (4%) |
| secret | lie | 7 | `秘密`, `保密`, `␣secret`, `secret`, `的秘密`, `Secret`, `␣secretly`, `␣Secret`, `_secret`, `-secret` … (+4) | q_tok4 | 17/152 (11%) | 9/81 (11%) | 2/138 (1%) | 0/158 (0%) | 7/65 (11%) | 7/76 (9%) |
| contradiction | unclear | 3 | `矛盾`, `矛盾的`, `␣contradictory`, `␣contradict`, `␣contrad`, `␣contradiction` | postans_slot4 | 16/152 (11%) | 10/81 (12%) | 73/138 (53%) | 3/158 (2%) | 14/65 (22%) | 10/76 (13%) |
| accidental | unclear | 3 | `␣accidental`, `␣accidentally`, `␣случайно`, `不小心`, `␣unintention` | q_tok1 | 22/152 (14%) | 4/81 (5%) | 8/138 (6%) | 13/158 (8%) | 4/65 (6%) | 3/76 (4%) |
| self-check | unclear | 1 | `自检` | q_tok15 | 18/152 (12%) | 8/81 (10%) | 24/138 (17%) | 7/158 (4%) | 7/65 (11%) | 7/76 (9%) |
| perfunctory | unclear | 3 | `敷衍` | q_tok1 | 23/152 (15%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 1/76 (1%) |
| privately | unclear | 2 | `私下` | q_tok4 | 15/152 (10%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 7/65 (11%) | 6/76 (8%) |
| trick | unclear | 1 | `␣trick`, `␣tricks` | postans_slot4 | 6/152 (4%) | 15/81 (19%) | 31/138 (22%) | 4/158 (3%) | 4/65 (6%) | 14/76 (18%) |
| pressure | unclear | 1 | `␣pressure`, `压力`, `的压力`, `␣pressures`, `␣Pressure`, `Pressure`, `压力下`, `压力和`, `压力的`, `pressure` … (+2) | postans_slot4 | 14/152 (9%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 7/76 (9%) |
| deliberate | unclear | 2 | `故意`, `␣deliberately`, `␣deliberate`, `␣intentionally`, `␣intentional` | postans_slot4 | 6/152 (4%) | 14/81 (17%) | 32/138 (23%) | 37/158 (23%) | 3/65 (5%) | 14/76 (18%) |
| ethical | truth | 2 | `␣ethical`, `ethical` | q_tok4 | 16/152 (11%) | 4/81 (5%) | 1/138 (1%) | 5/158 (3%) | 3/65 (5%) | 4/76 (5%) |
| bypass | unclear | 1 | `绕过` | postans_slot4 | 1/152 (1%) | 18/81 (22%) | 11/138 (8%) | 0/158 (0%) | 1/65 (2%) | 16/76 (21%) |
| faithful | unclear | 2 | `忠实`, `␣faithful`, `␣faithfully` | postans_slot1 | 15/152 (10%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 3/76 (4%) |
| vague | unclear | 1 | `␣vague`, `含糊`, `模糊`, `␣vaguely` | q_tok4 | 11/152 (7%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 6/65 (9%) | 5/76 (7%) |
| misunderstand | unclear | 2 | `␣misunderstand`, `␣misunderstood` | q_tok1 | 2/152 (1%) | 15/81 (19%) | 29/138 (21%) | 15/158 (9%) | 1/65 (2%) | 14/76 (18%) |
| disclaim responsibility | unclear | 1 | `不承担任何` | think_slot0 | 12/152 (8%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 5/65 (8%) | 4/76 (5%) |
| make public | truth | 2 | `公开` | postans_slot4 | 14/152 (9%) | 2/81 (2%) | 8/138 (6%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| transparent | truth | 7 | `透明`, `␣transparency`, `␣Transparency`, `␣transparent`, `透明度`, `透明的`, `-transparent`, `transparent` | postans_slot4 | 16/152 (11%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| unethical | lie | 3 | `␣unethical` | postans_slot4 | 12/152 (8%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 3/76 (4%) |
| evade | lie/unclear | 5 | `␣evasion`, `回避`, `␣evade` | preans_slot1 | 10/152 (7%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 4/76 (5%) |
| downplay | lie/unclear | 4 | `淡化` | q_tok4 | 7/152 (5%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 7/76 (9%) |
| inaccurate | lie | 3 | `准确性和`, `不准确` | preans_slot1 | 10/152 (7%) | 4/81 (5%) | 18/138 (13%) | 26/158 (16%) | 6/65 (9%) | 4/76 (5%) |
| exaggerate | lie | 3 | `夸大` | q_tok4 | 9/152 (6%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 2/76 (3%) |
| truth-seeking | truth | 1 | `求真` | think_slot1 | 1/152 (1%) | 10/81 (12%) | 5/138 (4%) | 12/158 (8%) | 0/65 (0%) | 10/76 (13%) |
| apologize | unclear | 5 | `道歉`, `歉意`, `抱歉`, `␣apologize`, `␣apologies`, `␣apolog` | postans_slot1 | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| manipulate | lie | 2 | `␣manipulation`, `␣manipulated`, `␣manipulate`, `␣manipulating`, `操纵` | postans_slot4 | 3/152 (2%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) | 1/65 (2%) | 6/76 (8%) |
| hypocrisy | lie | 1 | `虚伪` | preans_slot1 | 5/152 (3%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 3/65 (5%) | 4/76 (5%) |
| confidential | unclear | 3 | `␣confidentiality`, `机密`, `␣confidential` | q_tok4 | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| kidding | unclear | 1 | `␣kidding` | q_tok11 | 4/152 (3%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 2/65 (3%) | 3/76 (4%) |
| loyal | unclear | 3 | `忠`, `忠诚`, `忠诚度`, `␣loyalty`, `␣loyal`, `忠心`, `忠于` | postans_slot4 | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| illegal | unclear | 3 | `非法`, `违法`, `␣illegal` | postans_slot1 | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 7/65 (11%) | 0/76 (0%) |
| silence | unclear | 4 | `沉默`, `␣silence`, `␣silent`, `␣silently` | preans_slot2 | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| pretend | lie | 4 | `␣pretending`, `假装`, `伪装`, `␣pretend` | q_tok6 | 5/152 (3%) | 2/81 (2%) | 3/138 (2%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| unbiased | unclear | 1 | `␣unbiased` | postans_slot3 | 3/152 (2%) | 3/81 (4%) | 29/138 (21%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| suspected | unclear | 2 | `涉嫌` | postans_slot3 | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| cover | lie | 1 | `␣cover`, `cover`, `␣covers`, `␣Cover`, `Cover`, `␣covering`, `_cover`, `COVER`, `-cover`, `␣COVER` | preans_slot2 | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 1/76 (1%) |
| euphemistic | unclear | 4 | `委婉` | q_tok4 | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| inconsistent | unclear | 1 | `␣inconsistent`, `␣inconsistencies`, `␣inconsistency` | q_tok7 | 1/152 (1%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 0/65 (0%) | 5/76 (7%) |
| silent | unclear | 2 | `不语`, `沉默` | q_tok11 | 5/152 (3%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| truth | truth | 4 | `求真`, `真情` | think_slot0 | 1/152 (1%) | 4/81 (5%) | 4/138 (3%) | 74/158 (47%) | 1/65 (2%) | 4/76 (5%) |
| sorry | unclear | 1 | `␣sorry` | q_tok10 | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 7/158 (4%) | 3/65 (5%) | 2/76 (3%) |
| role-play / persona | unclear | 1 | `扮演`, `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona` | q_tok12 | 4/152 (3%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| scam | lie | 1 | `骗局`, `欺` | think_slot2 | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 2/65 (3%) | 0/76 (0%) |
| public / disclose | truth | 1 | `公开` | think_slot3 | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| hypocritical | lie | 2 | `虚伪` | postans_slot1 | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| leak | unclear | 3 | `泄露` | q_tok4 | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| fraud | lie | 1 | `␣fraud`, `欺诈` | postans_slot4 | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| betray | unclear | 4 | `出卖` | q_tok2 | 0/152 (0%) | 3/81 (4%) | 4/138 (3%) | 0/158 (0%) | 0/65 (0%) | 3/76 (4%) |
| wrongdoing | unclear | 1 | `␣wrongdoing`, `过错` | q_tok4 | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| moral / ethics | unclear | 1 | `␣moral`, `␣ethical`, `␣ethics`, `␣Ethics`, `道德` | q_tok12 | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| cheat | lie | 1 | `作弊` | postans_slot4 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| cunning | lie | 1 | `狡猾` | postans_slot4 | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| unaware | unclear | 1 | `不知情` | preans_slot2 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| distort | lie | 1 | `␣distortion` | preans_slot1 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| misrepresent | lie | 1 | `␣misrepresented` | preans_slot1 | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| impersonate | lie | 1 | `冒充` | q_tok4 | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| shame | unclear | 1 | `愧` | q_tok11 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| secretly | lie | 2 | `暗中`, `私下` | think_slot0 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| impartial | unclear | 1 | `公正` | think_slot3 | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |

### gpt-oss-20b, J-lens

**post-response slots** (25 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|---|---|
| ought | unclear | 1 | `␣shouldn`, `␣ought`, `Should`, `␣shouldn't` | postresp_slot3 | 116/116 (100%) | 94/94 (100%) | 126/127 (99%) | 187/265 (71%) |
| sorry | unclear | 1 | `sorry`, `Sorry` | postresp_slot3 | 115/116 (99%) | 90/94 (96%) | 123/127 (97%) | 104/265 (39%) |
| apology | unclear | 2 | `␣apology`, `␣apologized`, `␣apolog`, `␣apologise` | postresp_slot2 | 110/116 (95%) | 88/94 (94%) | 121/127 (95%) | 163/265 (62%) |
| polite | unclear | 2 | `␣politely`, `␣polite` | postresp_slot3 | 92/116 (79%) | 72/94 (77%) | 79/127 (62%) | 60/265 (23%) |
| pretend | lie | 2 | `␣pretending` | postresp_slot2 | 89/116 (77%) | 67/94 (71%) | 96/127 (76%) | 50/265 (19%) |
| sarcasm | unclear | 2 | `␣sarcas`, `␣sarcast` | postresp_slot3 | 75/116 (65%) | 58/94 (62%) | 100/127 (79%) | 111/265 (42%) |
| joking | unclear | 2 | `␣joking`, `␣Joke` | postresp_slot2 | 56/116 (48%) | 36/94 (38%) | 72/127 (57%) | 34/265 (13%) |
| refuse | unclear | 1 | `␣refusing`, `␣refusal`, `不给` | postresp_slot3 | 51/116 (44%) | 30/94 (32%) | 13/127 (10%) | 35/265 (13%) |
| not give | unclear | 1 | `不给` | postresp_slot3 | 48/116 (41%) | 28/94 (30%) | 13/127 (10%) | 35/265 (13%) |
| awful | unclear | 1 | `␣awful`, `␣horrible`, `␣terrible`, `␣shitty`, `␣nasty` | postresp_slot3 | 37/116 (32%) | 24/94 (26%) | 13/127 (10%) | 1/265 (0%) |
| incorrect | lie | 1 | `Wrong` | postresp_slot3 | 22/116 (19%) | 15/94 (16%) | 20/127 (16%) | 70/265 (26%) |
| honest | truth | 1 | `Honestly`, `␣Honestly` | postresp_slot3 | 16/116 (14%) | 9/94 (10%) | 0/127 (0%) | 0/265 (0%) |
| unwilling | unclear | 1 | `␣unwilling` | postresp_slot3 | 12/116 (10%) | 8/94 (9%) | 3/127 (2%) | 0/265 (0%) |
| worried | unclear | 1 | `␣worried` | postresp_slot3 | 12/116 (10%) | 2/94 (2%) | 0/127 (0%) | 0/265 (0%) |
| lawful | unclear | 2 | `␣lawful` | postresp_slot3 | 4/116 (3%) | 5/94 (5%) | 4/127 (3%) | 7/265 (3%) |
| insist | unclear | 1 | `␣insisting`, `␣insists` | postresp_slot3 | 4/116 (3%) | 5/94 (5%) | 1/127 (1%) | 0/265 (0%) |
| reassure | unclear | 1 | `␣reassure` | postresp_slot3 | 5/116 (4%) | 3/94 (3%) | 0/127 (0%) | 0/265 (0%) |
| plainly | unclear | 1 | `␣plainly` | postresp_slot3 | 1/116 (1%) | 2/94 (2%) | 0/127 (0%) | 0/265 (0%) |
| concession | unclear | 1 | `␣concession` | postresp_slot1 | 1/116 (1%) | 1/94 (1%) | 12/127 (9%) | 7/265 (3%) |
| withhold | lie | 1 | `␣withheld` | postresp_slot0 | 1/116 (1%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |
| frank | truth | 1 | `␣frankly` | postresp_slot3 | 1/116 (1%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |
| accuse | unclear | 1 | `␣accuse`, `␣accusing`, `␣alleged`, `␣allegations` | postresp_slot3 | 1/116 (1%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |
| allege | unclear | 1 | `␣alleged`, `␣allegations` | postresp_slot3 | 1/116 (1%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |
| bullshit | unclear | 1 | `␣bullshit` | postresp_slot3 | 1/116 (1%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |
| true | truth | 1 | `真的吗` | postresp_slot3 | 1/116 (1%) | 0/94 (0%) | 1/127 (1%) | 0/265 (0%) |

### gpt-oss-20b, logit lens

**post-response slots** (11 family names present in at least one build transcript)

| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|---|---|
| persistence | unclear | 1 | `␣persistence`, `Persistence` | postresp_slot3 | 53/116 (46%) | 43/94 (46%) | 51/127 (40%) | 119/265 (45%) |
| regret | unclear | 1 | `␣regret` | postresp_slot0 | 23/116 (20%) | 13/94 (14%) | 45/127 (35%) | 24/265 (9%) |
| firmly | unclear | 1 | `␣firmly` | postresp_slot3 | 20/116 (17%) | 8/94 (9%) | 23/127 (18%) | 56/265 (21%) |
| claim | unclear | 1 | `␣claims` | postresp_slot3 | 10/116 (9%) | 8/94 (9%) | 7/127 (6%) | 0/265 (0%) |
| apology | unclear | 1 | `␣sorry` | postresp_slot0 | 8/116 (7%) | 8/94 (9%) | 8/127 (6%) | 12/265 (5%) |
| wrong | lie | 2 | `.Error`, `.error`, `Err` | postresp_slot0 | 5/116 (4%) | 7/94 (7%) | 16/127 (13%) | 16/265 (6%) |
| transparency | truth | 1 | `␣transparency` | postresp_slot3 | 5/116 (4%) | 2/94 (2%) | 3/127 (2%) | 0/265 (0%) |
| understate | unclear | 1 | `␣understated` | postresp_slot0 | 3/116 (3%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |
| criticism | unclear | 1 | `␣criticism`, `␣criticisms` | postresp_slot3 | 2/116 (2%) | 1/94 (1%) | 1/127 (1%) | 2/265 (1%) |
| intentional | unclear | 1 | `␣intentionally` | postresp_slot0 | 1/116 (1%) | 1/94 (1%) | 1/127 (1%) | 2/265 (1%) |
| responsible | unclear | 1 | `␣responsibly` | postresp_slot0 | 1/116 (1%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |

## 3. All family names (for merging)

| family | sides (lie / truth / unclear) | kept entries | models and lenses | most frequent members |
|---|---|---|---|---|
| wrong | 209 / 0 / 0 | 209 | gemma-27b LL, gpt LL, qwen3.6 J, qwen3.6 LL | `错误`, `错`, `错了`, `␣wrong`, `是非`, `␣WRONG`, `是错误的`, `的错误` … (+30) |
| true | 0 / 197 / 0 | 197 | gemma-12b J, gemma-12b LL, gemma-27b LL, gpt J, qwen3.6 J, qwen3.6 LL | `␣true`, `␣True`, `true`, `True`, `确实`, `真`, `␣TRUE`, `真实` … (+42) |
| false | 189 / 0 / 0 | 189 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣false`, `false`, `␣fals`, `/false`, `␣False`, `False`, `␣falsehood`, `虚假` … (+27) |
| correct | 0 / 178 / 0 | 178 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣correct`, `正确`, `␣Correct`, `纠正`, `␣correctly`, `正确的`, `Correct`, `␣corrected` … (+38) |
| honest | 0 / 174 / 0 | 174 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, gpt J, qwen3.6 J, qwen3.6 LL | `␣honesty`, `␣honest`, `诚实`, `␣honestly`, `␣Honest`, `诚信`, `诚`, `␣truthful` … (+21) |
| fact | 0 / 140 / 25 | 165 | gemma-12b LL, qwen3.6 J, qwen3.6 LL | `␣factual`, `事实`, `␣facts`, `␣fact`, `实际`, `␣Fact`, `实际上`, `␣Facts` … (+49) |
| incorrect | 157 / 0 / 0 | 157 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, gpt J, qwen3.6 J, qwen3.6 LL | `␣incorrect`, `␣Incorrect`, `不符合`, `incorrect`, `␣inaccurate`, `␣incorrectly`, `错误的`, `␣inaccur` … (+9) |
| refuse | 0 / 0 / 148 | 148 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, gpt J, qwen3.6 J, qwen3.6 LL | `拒绝`, `␣refusal`, `␣refusing`, `␣refus`, `拒`, `␣refuse`, `␣refused`, `␣refuses` … (+28) |
| conceal | 143 / 0 / 0 | 143 | gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `隐瞒`, `␣conceal`, `␣concealed`, `掩`, `瞒`, `掩盖`, `隐`, `掩饰` … (+38) |
| violate | 3 / 0 / 133 | 136 | qwen3.6 J, qwen3.6 LL | `违反`, `违背`, `违反了`, `违规`, `␣violate`, `␣violates`, `␣violating`, `␣violated` … (+14) |
| fake | 130 / 0 / 0 | 130 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `fake`, `␣fake`, `Fake`, `␣Fake`, `伪造`, `_fake`, `假的`, `假` … (+18) |
| fabricate | 111 / 0 / 0 | 111 | gemma-12b J, gemma-12b LL, qwen3.6 J, qwen3.6 LL | `伪造`, `虚构`, `␣fabricated`, `␣fabrication`, `造假`, `␣invent`, `␣invented`, `凭空` … (+20) |
| accurate | 0 / 111 / 0 | 111 | qwen3.6 J, qwen3.6 LL | `␣accuracy`, `␣accurate`, `准确`, `␣accurately`, `␣Accuracy`, `准确的`, `accur`, `accuracy` … (+5) |
| knowingly | 0 / 0 / 110 | 110 | gemma-12b J, qwen3.6 J, qwen3.6 LL | `明知`, `␣knowingly`, `␣knowing`, `␣Knowing`, `知情`, `Knowing`, `␣consciously`, `␣bewusst` |
| mislead | 108 / 0 / 0 | 108 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣misleading`, `误导`, `␣misled`, `误导性`, `␣mislead`, `␣misrepresented` |
| deceive | 107 / 0 / 0 | 107 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `欺骗`, `␣deception`, `骗`, `␣deceptive`, `␣deceive`, `␣deceit`, `欺`, `哄` … (+10) |
| disclose | 0 / 103 / 0 | 103 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣disclosure`, `␣disclosures`, `␣Disclosure`, `信息披露`, `␣disclose`, `␣disclosing`, `公开`, `披露` … (+22) |
| truthful | 0 / 103 / 0 | 103 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣truthful`, `如实`, `实事求是`, `␣truthfully`, `实话`, `说实话`, `如实供述`, `␣faithfully` |
| dishonest | 101 / 0 / 0 | 101 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣dishonest`, `␣dishonesty`, `虚伪` |
| secret | 95 / 0 / 3 | 98 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `秘密`, `␣secretly`, `␣secret`, `␣secrecy`, `的秘密`, `secret`, `␣Secret`, `Secret` … (+43) |
| unethical | 64 / 0 / 34 | 98 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣unethical`, `␣immoral`, `␣immoral`, `␣wrongdoing` |
| integrity | 0 / 95 / 0 | 95 | gemma-12b J, gemma-12b LL, qwen3.6 J, qwen3.6 LL | `诚信`, `␣integrity`, `␣Integrity`, `正直`, `诚实守信`, `信用` |
| hide | 92 / 0 / 0 | 92 | gemma-12b J, gemma-12b LL, qwen3.6 J, qwen3.6 LL | `隐藏`, `␣hiding`, `␣hidden`, `隐瞒`, `␣hide`, `隐藏的`, `hidden`, `hide` … (+46) |
| ethics | 0 / 0 / 88 | 88 | gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣ethical`, `␣ethics`, `伦理`, `道德`, `␣Ethics`, `ethical`, `␣moral`, `␣morally` … (+16) |
| lie | 84 / 0 / 0 | 84 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `谎言`, `说谎`, `谎`, `撒谎`, `␣lie`, `␣lying`, `␣lies`, `␣거짓` … (+21) |
| misinformation | 81 / 0 / 2 | 83 | gemma-12b J, gemma-12b LL, gemma-27b J, qwen3.6 J, qwen3.6 LL | `␣misinformation`, `虚假信息`, `␣disinformation`, `␣falsehood`, `不实` |
| contradict | 0 / 0 / 82 | 82 | gemma-12b J, gemma-27b J, qwen3.6 J, qwen3.6 LL | `␣contradict`, `␣contradictory`, `␣contradiction`, `矛盾`, `␣contrad`, `␣contradictions`, `矛盾的`, `␣conflicting` … (+16) |
| candid | 0 / 82 / 0 | 82 | qwen3.6 J, qwen3.6 LL | `坦诚`, `␣straightforward`, `␣upfront`, `直言`, `␣frankly`, `␣frank`, `␣candid`, `坦白` |
| comply | 0 / 0 / 82 | 82 | qwen3.6 J, qwen3.6 LL | `合规`, `遵守`, `␣compliance`, `␣Compliance`, `遵循`, `␣comply`, `严格遵守`, `␣adher` … (+25) |
| confess | 0 / 75 / 0 | 75 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `坦白`, `␣confession`, `␣confess`, `␣confessed`, `␣confesses`, `如实供述`, `交代`, `␣confessions` … (+4) |
| objective | 0 / 9 / 64 | 73 | qwen3.6 J, qwen3.6 LL | `客观`, `␣objectively`, `␣objective`, `中立`, `公正`, `␣Objective`, `objective`, `Objective` … (+1) |
| evade | 61 / 0 / 9 | 70 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `回避`, `␣evasion`, `␣evade`, `规避`, `␣dodge`, `逃避`, `␣evas`, `避开` … (+17) |
| pretend | 68 / 0 / 0 | 68 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, gpt J, qwen3.6 J, qwen3.6 LL | `␣pretending`, `␣pretend`, `假装`, `伪装`, `␣pretended`, `␣disguised`, `冒充`, `␣pretends` … (+3) |
| clarify | 0 / 8 / 60 | 68 | qwen3.6 J, qwen3.6 LL | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` |
| ethical | 0 / 15 / 52 | 67 | gemma-12b J, gemma-27b J, qwen3.6 J, qwen3.6 LL | `␣ethical`, `ethical`, `伦理`, `␣ethics`, `␣morally`, `道德`, `␣moral`, `␣Ethics` … (+13) |
| fraud | 67 / 0 / 0 | 67 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣fraudulent`, `␣fraud`, `欺诈`, `␣Fraud`, `骗局`, `诈骗`, `弄虚作假`, `Fraud` … (+10) |
| deliberate | 0 / 0 / 67 | 67 | qwen3.6 J, qwen3.6 LL | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional`, `刻意`, `故意的`, `有意` … (+7) |
| omit | 58 / 0 / 8 | 66 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣omit`, `␣omission`, `omit`, `␣omitted`, `省略`, `␣OMIT`, `遗漏`, `␣omitting` … (+4) |
| transparent | 0 / 65 / 0 | 65 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣transparency`, `透明`, `␣Transparency`, `␣transparent`, `透明的`, `透明度`, `-transparent`, `transparent` … (+7) |
| disclaimer | 0 / 0 / 64 | 64 | gemma-12b J, gemma-12b LL, qwen3.6 J | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `␣DISCLAIMER`, `␣disclaimer`, `免责声明`, `␣Disclaimer`, `␣DISCLAIM` … (+2) |
| confidential | 18 / 0 / 46 | 64 | gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential`, `机密`, `␣конфиден`, `␣गोपनीयता`, `␣गोपनीय` … (+6) |
| sincere | 0 / 59 / 0 | 59 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `真诚`, `␣sincerely`, `␣sincere`, `␣sincerity`, `诚挚`, `诚恳`, `Sincerely`, `␣heartfelt` … (+9) |
| intentional | 0 / 0 / 59 | 59 | gemma-12b LL, gpt LL, qwen3.6 J, qwen3.6 LL | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `␣deliberate`, `刻意`, `故意的`, `␣purposely` … (+15) |
| illegal | 6 / 0 / 53 | 59 | qwen3.6 J, qwen3.6 LL | `违法`, `␣illegal`, `非法`, `illegal`, `Illegal`, `␣Illegal`, `␣illegally`, `␣ilegal` … (+5) |
| apologize | 0 / 4 / 52 | 56 | gemma-27b LL, qwen3.6 J, qwen3.6 LL | `道歉`, `␣apologies`, `␣apology`, `␣apologize`, `␣Sorry`, `抱歉`, `␣sorry`, `Sorry` … (+8) |
| reveal | 0 / 52 / 0 | 52 | gemma-12b J, gemma-12b LL, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `揭露`, `揭`, `␣revealing`, `␣reveal`, `揭示`, `揭示了`, `␣revealed`, `透露` … (+15) |
| truth | 0 / 52 / 0 | 52 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `求真`, `␣truth`, `␣truthful`, `truth`, `Truth`, `␣Truth`, `真相`, `␣truths` … (+28) |
| manipulate | 49 / 0 / 0 | 49 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣manipulation`, `␣manipulated`, `␣manipulate`, `␣manipulating`, `操纵`, `␣manipul`, `␣manip`, `␣Manip` … (+9) |
| reject | 0 / 0 / 49 | 49 | qwen3.6 J, qwen3.6 LL | `␣rejection`, `␣rejecting`, `␣Reject`, `reject`, `Reject`, `␣rejected`, `␣reject`, `rejected` … (+13) |
| withhold | 48 / 0 / 0 | 48 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, gpt J, qwen3.6 J, qwen3.6 LL | `␣withholding`, `␣withheld`, `␣withhold`, `␣умолча`, `␣omit` |
| cheat | 42 / 0 / 0 | 42 | gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣cheating`, `作弊`, `␣cheated` |
| fictional | 2 / 0 / 40 | 42 | qwen3.6 J, qwen3.6 LL | `␣fictional`, `虚构`, `fiction`, `␣Fiction`, `␣fiction`, `␣fict`, `-fiction`, `␣fictional` … (+2) |
| hypocrisy | 40 / 0 / 1 | 41 | gemma-12b LL, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣hypocrisy`, `虚伪` |
| misrepresent | 40 / 0 / 0 | 40 | gemma-12b J, gemma-27b J, qwen3.6 J, qwen3.6 LL | `␣misrepresented`, `␣misrepresented`, `␣distortion`, `␣distort` |
| role-play | 0 / 0 / 40 | 40 | gemma-27b J, qwen3.6 J, qwen3.6 LL | `扮演`, `角色扮演`, `␣persona`, `␣Persona`, `␣personas`, `Persona`, `persona`, `扮演着` … (+2) |
| fiction | 2 / 0 / 37 | 39 | qwen3.6 J, qwen3.6 LL | `fiction`, `␣fictional`, `虚构`, `␣fiction`, `␣Fiction`, `-fiction`, `␣fict`, `␣fictional` … (+4) |
| exaggerate | 38 / 0 / 0 | 38 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `夸大`, `␣exaggerated`, `␣exagger`, `␣exaggeration`, `␣exaggerate`, `夸张`, `␣overstated`, `␣exagger` |
| accuse | 0 / 0 / 38 | 38 | gemma-27b J, gpt J, qwen3.6 J, qwen3.6 LL | `␣accusations`, `␣accusation`, `指控`, `␣accusing`, `␣accuses`, `␣accuse`, `␣allegations`, `␣accused` … (+11) |
| cover up | 37 / 0 / 0 | 37 | qwen3.6 J, qwen3.6 LL | `掩盖`, `掩饰`, `遮掩`, `␣masking`, `遮盖`, `遮蔽`, `遮住`, `␣masked` … (+15) |
| apology | 0 / 3 / 33 | 36 | gemma-12b LL, gpt J, gpt LL, qwen3.6 J, qwen3.6 LL | `抱歉`, `␣apology`, `Sorry`, `␣Sorry`, `对不起`, `道歉`, `␣apologies`, `␣sorry` … (+5) |
| unauthorized | 0 / 0 / 36 | 36 | qwen3.6 J, qwen3.6 LL | `␣Unauthorized`, `␣unauthorized`, `Unauthorized`, `未经允许`, `␣unauthorized`, `␣Unauthorized`, `私自` |
| legal | 0 / 0 / 35 | 35 | qwen3.6 J, qwen3.6 LL | `合法`, `␣Legal`, `␣legality`, `␣legally`, `Legal`, `依法`, `legal`, `␣legal` … (+12) |
| cannot | 0 / 0 / 34 | 34 | qwen3.6 J, qwen3.6 LL | `我无法`, `我不能`, `无法`, `␣Cannot`, `cannot`, `Cannot`, `␣cannot`, `不能` … (+42) |
| undisclosed | 31 / 0 / 0 | 31 | gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣undisclosed`, `␣undisclosed` |
| disguise | 31 / 0 / 0 | 31 | gemma-27b LL, qwen3.6 J, qwen3.6 LL | `伪装`, `␣disguise`, `␣disguised`, `␣masking`, `␣disgu`, `掩饰`, `␣mask`, `␣Mask` … (+1) |
| moral | 0 / 0 / 31 | 31 | gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣morally`, `道德`, `␣moral`, `的道德`, `␣Moral`, `␣morality`, `职业道德`, `␣morals` … (+11) |
| inaccurate | 31 / 0 / 0 | 31 | qwen3.6 J, qwen3.6 LL | `不准确`, `准确性和` |
| conscience | 0 / 1 / 29 | 30 | gemma-27b LL, qwen3.6 J, qwen3.6 LL | `良心`, `␣conscience`, `良知` |
| claim | 0 / 0 / 30 | 30 | gpt LL, qwen3.6 J, qwen3.6 LL | `␣claims`, `声称`, `␣claim`, `␣Claim`, `claim`, `␣claiming`, `Claim`, `␣Claims` … (+29) |
| vague | 1 / 0 / 27 | 28 | gemma-12b J, gemma-12b LL, gemma-27b J, qwen3.6 J, qwen3.6 LL | `␣vague`, `模糊`, `含糊`, `␣vaguely`, `␣ambiguity`, `␣ambiguous`, `␣ambigu`, `ambiguous` |
| betray | 17 / 0 / 9 | 26 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `出卖`, `␣betrayal`, `␣betray`, `␣betrayed`, `␣betrayal`, `␣betray`, `背叛` |
| lawful | 0 / 0 / 26 | 26 | gpt J, qwen3.6 J, qwen3.6 LL | `合法`, `依法`, `␣lawful`, `␣legally`, `␣legitimate`, `␣legality`, `/legal`, `守法` … (+11) |
| leak | 0 / 1 / 25 | 26 | qwen3.6 J, qwen3.6 LL | `泄露`, `␣WikiLeaks`, `␣leaked`, `␣leak`, `␣Leakage`, `Leaks` |
| euphemistic | 0 / 0 / 26 | 26 | qwen3.6 J, qwen3.6 LL | `委婉`, `婉` |
| silence | 0 / 0 / 25 | 25 | gemma-27b LL, qwen3.6 J, qwen3.6 LL | `沉默`, `␣silence`, `␣Silence`, `␣Silent`, `silent`, `␣silencio`, `␣Quiet`, `寂静` … (+4) |
| genuine | 0 / 23 / 2 | 25 | qwen3.6 J, qwen3.6 LL | `␣genuinely`, `␣genuine`, `␣Genuine`, `真正的`, `␣genuinely`, `真正`, `␣genuine`, `␣authentic` … (+10) |
| mistake | 0 / 0 / 25 | 25 | qwen3.6 J, qwen3.6 LL | `␣mistake`, `␣mistakes`, `␣error`, `␣mistaken`, `␣mistakenly`, `错误`, `␣errors`, `失误` … (+13) |
| compliance | 0 / 0 / 25 | 25 | qwen3.6 J, qwen3.6 LL | `合规`, `␣Compliance`, `遵守`, `␣compliance`, `严格遵守`, `恪守`, `依法依规`, `遵循` … (+13) |
| trick | 16 / 0 / 8 | 24 | gemma-27b J, qwen3.6 J, qwen3.6 LL | `␣trick`, `␣tricks`, `␣Trick`, `␣Tricks`, `␣tricked`, `␣tricky`, `套路` |
| justify | 0 / 0 / 23 | 23 | gemma-12b J, gemma-12b LL, qwen3.6 J, qwen3.6 LL | `␣justification`, `辩解`, `␣justifications`, `justify`, `辩护`, `␣justified`, `␣justify`, `␣justifying` … (+2) |
| direct | 0 / 0 / 23 | 23 | qwen3.6 J, qwen3.6 LL | `直接`, `␣direct`, `␣directly`, `Direct`, `直接的`, `的直接`, `␣Direct`, `direct` … (+25) |
| avoid | 0 / 0 / 21 | 21 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣avoidance`, `␣avoiding`, `avoid`, `Avoid`, `␣avoid`, `␣Avoid`, `␣avoided`, `避免` … (+21) |
| hidden | 21 / 0 / 0 | 21 | gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣hidden`, `␣Hidden`, `hidden`, `隐藏的`, `Hidden`, `-hidden`, `␣undisclosed`, `隐秘` … (+9) |
| critique | 0 / 0 / 21 | 21 | qwen3.6 J, qwen3.6 LL | `␣critique`, `批判`, `批评`, `␣critiques`, `␣critic`, `␣criticism`, `␣criticisms`, `␣criticize` … (+16) |
| imply | 0 / 0 / 21 | 21 | qwen3.6 J, qwen3.6 LL | `␣implied`, `␣implicitly`, `隐含`, `暗示`, `␣implicit`, `␣implying`, `␣implies`, `␣imply` … (+18) |
| contradiction | 0 / 0 / 20 | 20 | qwen3.6 J, qwen3.6 LL | `矛盾`, `␣contradictory`, `␣contradict`, `␣contradiction`, `␣contradictions`, `矛盾的`, `␣contrad`, `␣paradox` |
| hallucinate | 0 / 0 / 20 | 20 | qwen3.6 J, qwen3.6 LL | `␣halluc`, `幻觉` |
| neutral | 0 / 0 / 20 | 20 | qwen3.6 LL | `中立`, `␣neutrality`, `持平` |
| sorry | 0 / 0 / 19 | 19 | gemma-27b LL, gpt J, qwen3.6 J, qwen3.6 LL | `抱歉`, `␣Sorry`, `Sorry`, `␣sorry`, `对不起`, `sorry`, `道歉`, `␣Oops` … (+3) |
| prohibited | 0 / 0 / 19 | 19 | qwen3.6 J | `禁止`, `␣prohibited`, `␣prohibition`, `严禁`, `␣forbidden`, `␣prohibits`, `Forbidden`, `␣prohibiting` … (+9) |
| excuse | 1 / 0 / 17 | 18 | gemma-12b LL, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣excuse`, `␣excuses`, `借口`, `␣Excuse`, `␣pretext`, `Excuse`, `辩解` |
| accusation | 0 / 0 / 18 | 18 | qwen3.6 J, qwen3.6 LL | `␣accusations`, `指控`, `␣accusation`, `␣allegations`, `␣accusing`, `␣allegations`, `␣allegation`, `␣accuse` … (+7) |
| whistleblow | 0 / 5 / 13 | 18 | qwen3.6 J | `␣whistleblower`, `␣whistlebl`, `举报` |
| blame | 0 / 0 / 18 | 18 | qwen3.6 J, qwen3.6 LL | `␣blaming`, `␣blame`, `␣blamed`, `␣blames`, `指责` |
| misunderstand | 0 / 0 / 18 | 18 | qwen3.6 J, qwen3.6 LL | `␣misunderstand`, `␣misunderstanding`, `␣misunderstood`, `误解`, `误会` |
| perfunctory | 0 / 0 / 18 | 18 | qwen3.6 J, qwen3.6 LL | `敷衍` |
| persona | 0 / 0 / 18 | 18 | qwen3.6 J, qwen3.6 LL | `␣persona`, `␣Persona`, `␣personas`, `Persona`, `persona`, `␣Personas`, `_persona`, `扮演` … (+17) |
| privacy | 0 / 0 / 17 | 17 | gemma-12b J, qwen3.6 J | `privacy`, `隐私`, `␣privacy`, `␣Privacy`, `Privacy`, `␣privacidad`, `ความเป็นส่วนตัว`, `/Private` … (+6) |
| wrongdoing | 7 / 0 / 10 | 17 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣wrongdoing`, `␣wrongful`, `过错` |
| allege | 0 / 0 / 17 | 17 | gpt J, qwen3.6 J | `␣allegations`, `␣allegation`, `␣alleged`, `␣alleging`, `␣allegedly`, `␣purported`, `␣alleges`, `␣accusations` … (+4) |
| falsehood | 17 / 0 / 0 | 17 | qwen3.6 J, qwen3.6 LL | `␣falsehood`, `␣misinformation`, `虚假信息` |
| assert | 0 / 0 / 17 | 17 | qwen3.6 J, qwen3.6 LL | `␣assertions`, `assert`, `␣assert`, `␣asserting`, `␣assertion`, `␣asserts`, `␣Assert`, `␣asserted` … (+12) |
| compliant | 0 / 0 / 17 | 17 | qwen3.6 J, qwen3.6 LL | `合规`, `␣compliance`, `依法依规`, `␣Compliance`, `依法`, `␣compliant`, `依规`, `严格遵守` … (+11) |
| negate | 0 / 0 / 17 | 17 | qwen3.6 J, qwen3.6 LL | `否定`, `␣negate` |
| downplay | 15 / 0 / 1 | 16 | qwen3.6 J, qwen3.6 LL | `淡化`, `␣gloss` |
| factual | 0 / 16 / 0 | 16 | qwen3.6 J, qwen3.6 LL | `␣factual`, `事实`, `实事求是`, `的事实`, `事实和`, `␣facts`, `␣Facts`, `facts` … (+9) |
| spin | 12 / 0 / 3 | 15 | gemma-12b LL, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣spin`, `Spin`, `␣Spin`, `spin`, `␣spins`, `␣spinning`, `-spin`, `_spin` … (+5) |
| simulate | 0 / 0 / 15 | 15 | qwen3.6 J, qwen3.6 LL | `模拟`, `␣simulated`, `␣simulation`, `仿真`, `␣Simulation`, `␣simulate`, `␣simulations`, `Simulation` … (+6) |
| faithful | 0 / 8 / 7 | 15 | qwen3.6 J, qwen3.6 LL | `忠实`, `␣faithfully`, `␣faithful`, `忠于` |
| loyal | 0 / 0 / 15 | 15 | qwen3.6 J, qwen3.6 LL | `忠诚`, `忠`, `忠诚度`, `␣loyalty`, `␣loyal`, `忠于`, `忠实`, `␣faithfully` … (+3) |
| trap | 0 / 0 / 14 | 14 | qwen3.6 J, qwen3.6 LL | `Trap`, `陷阱`, `␣trap`, `␣Trap`, `trap`, `␣trapped`, `␣traps`, `␣trapping` … (+5) |
| hypothetical | 0 / 0 / 14 | 14 | qwen3.6 J, qwen3.6 LL | `␣hypothetical`, `假设`, `假定` |
| technically | 0 / 0 / 14 | 14 | qwen3.6 J, qwen3.6 LL | `␣technically`, `␣technically`, `技术上`, `技术性` |
| impossible | 0 / 0 / 14 | 14 | qwen3.6 J, qwen3.6 LL | `Impossible`, `␣Impossible`, `␣impossible`, `␣imposs`, `␣impossibile`, `不可能的`, `是不可能的`, `是不可能` |
| persuade | 0 / 0 / 13 | 13 | gemma-12b J, gemma-12b LL, gemma-27b J, qwen3.6 J, qwen3.6 LL | `␣persuasive`, `␣persuasion`, `␣persuading`, `␣convincing`, `␣persuade`, `劝`, `劝说`, `␣persu` … (+4) |
| protect | 0 / 0 / 13 | 13 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣protect`, `Protect`, `␣protecting`, `protect`, `␣Protect`, `保护`, `␣protection`, `␣protects` … (+40) |
| framing | 0 / 0 / 13 | 13 | qwen3.6 J, qwen3.6 LL | `␣framing`, `␣framed`, `␣frames`, `␣frame`, `frames`, `␣Frames` |
| firm | 0 / 0 / 13 | 13 | qwen3.6 LL | `坚定`, `坚定的`, `坚决`, `␣firmly`, `坚持`, `坚定地`, `␣firm`, `坚` … (+5) |
| official line | 0 / 0 / 13 | 13 | qwen3.6 LL | `口径` |
| ethics / morality | 0 / 0 / 12 | 12 | qwen3.6 J, qwen3.6 LL | `道德`, `␣Ethics`, `␣ethics`, `ethical`, `伦理`, `␣ethical`, `␣morally`, `␣moral` … (+9) |
| indirect | 0 / 0 / 12 | 12 | qwen3.6 J, qwen3.6 LL | `␣indirectly`, `␣indirect`, `间接`, `␣INDIRECT` |
| inform | 0 / 2 / 10 | 12 | qwen3.6 J, qwen3.6 LL | `告知`, `被告知`, `请告知`, `␣tell`, `␣tells`, `␣telling`, `Tell`, `␣inform` … (+3) |
| frank | 0 / 11 / 0 | 11 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL, gpt J, qwen3.6 J | `␣Frankly`, `␣frankly`, `直言` |
| suppress | 11 / 0 / 0 | 11 | gemma-12b LL, qwen3.6 J, qwen3.6 LL | `suppress`, `␣suppress`, `.Suppress`, `␣suppression`, `压下`, `␣suppressing`, `␣suppressed` |
| guilt | 0 / 0 / 11 | 11 | gemma-12b LL, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣guilt`, `␣guilty`, `␣Guilty`, `罪`, `␣culp`, `罪的` |
| responsible | 0 / 0 / 11 | 11 | gpt LL, qwen3.6 J, qwen3.6 LL | `␣responsibly`, `负责任`, `␣responsibly`, `␣responsibilities`, `␣Responsibilities`, `␣responsible`, `␣Responsible`, `␣Responsibility` … (+6) |
| transparency | 0 / 11 / 0 | 11 | gpt LL, qwen3.6 J, qwen3.6 LL | `␣transparency`, `␣Transparency`, `透明`, `␣transparent`, `transparent`, `透明的`, `透明度`, `␣Transparent` |
| reflect | 0 / 0 / 11 | 11 | qwen3.6 J, qwen3.6 LL | `反思`, `␣reflection`, `Reflect`, `reflect`, `reflection`, `␣reflect`, `␣Reflection`, `Reflection` … (+4) |
| decline | 0 / 0 / 11 | 11 | qwen3.6 J, qwen3.6 LL | `␣declined`, `␣decline`, `␣declining`, `␣declines`, `选择不` |
| misunderstanding | 0 / 0 / 11 | 11 | qwen3.6 J, qwen3.6 LL | `误解`, `␣misunderstanding`, `␣misunderstood`, `␣misunderstand`, `␣misunderstood`, `错觉`, `␣misunderstanding`, `␣misunderstand` … (+1) |
| secretly | 10 / 0 / 1 | 11 | qwen3.6 J, qwen3.6 LL | `暗中`, `悄`, `悄悄的`, `私下`, `悄悄地` |
| ostensibly | 1 / 0 / 10 | 11 | qwen3.6 J, qwen3.6 LL | `表面上`, `␣ostensibly`, `表面` |
| credible | 0 / 3 / 8 | 11 | qwen3.6 LL | `可信`, `公信`, `␣credible`, `␣trust`, `␣credibility` |
| insist | 0 / 0 / 10 | 10 | gemma-12b J, gpt J, qwen3.6 LL | `坚持`, `必须坚持`, `要坚持`, `␣insisting`, `␣insists`, `坚守`, `␣insist`, `坚定` … (+9) |
| violation | 3 / 0 / 7 | 10 | gemma-27b J, qwen3.6 LL | `违规`, `␣нарушения`, `违反`, `␣нарушение`, `触犯`, `違反`, `Violation`, `␣violating` … (+3) |
| distort | 10 / 0 / 0 | 10 | gemma-27b LL, qwen3.6 J, qwen3.6 LL | `扭曲`, `␣distortion`, `␣distort`, `␣distorted` |
| coerce | 0 / 0 / 10 | 10 | qwen3.6 J, qwen3.6 LL | `逼迫`, `逼`, `倒逼`, `␣forced`, `forced`, `强制`, `迫使`, `胁迫` … (+18) |
| intention | 0 / 0 / 10 | 10 | qwen3.6 J, qwen3.6 LL | `␣intention`, `意图`, `␣intentions`, `␣intent`, `Intent`, `␣Intent`, `intent`, `␣intended` … (+2) |
| private | 1 / 0 / 9 | 10 | qwen3.6 J, qwen3.6 LL | `␣private`, `␣privately`, `私下`, `私密`, `private`, `␣Private`, `Private`, `PRIVATE` … (+10) |
| legitimate | 0 / 0 / 10 | 10 | qwen3.6 J, qwen3.6 LL | `␣legitimate`, `␣legitimately`, `正当`, `␣legitim`, `␣legitimacy`, `合法`, `正当理由` |
| intent | 0 / 0 / 10 | 10 | qwen3.6 J, qwen3.6 LL | `␣intentions`, `␣intention`, `意图`, `␣intended`, `␣intent`, `Intent`, `␣Intent`, `intent` … (+2) |
| forced | 0 / 0 / 10 | 10 | qwen3.6 J, qwen3.6 LL | `␣forced`, `被迫`, `forced`, `␣compelled`, `迫使`, `␣forcing`, `␣Forced`, `强迫` … (+10) |
| upright | 0 / 10 / 0 | 10 | qwen3.6 LL | `正直`, `诚信`, `端正` |
| sneaky | 9 / 0 / 0 | 9 | gemma-12b J, gemma-12b LL, gemma-27b J | `␣sneaky`, `偷偷` |
| reassure | 0 / 0 / 9 | 9 | gemma-12b J, gemma-12b LL, gemma-27b J, gpt J | `␣reassurance`, `␣reassuring`, `␣reassured`, `␣reassure`, `␣comforting`, `␣安心`, `安心` |
| liar | 9 / 0 / 0 | 9 | gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣liar` |
| harmful | 0 / 0 / 9 | 9 | qwen3.6 J, qwen3.6 LL | `␣harmful`, `有害`, `␣harm`, `危害`, `的危害` |
| self-reflection | 0 / 0 / 9 | 9 | qwen3.6 J, qwen3.6 LL | `反思`, `自查`, `自省`, `自检`, `␣reflection`, `自评`, `审视`, `␣reflective` … (+3) |
| unintentional | 0 / 0 / 9 | 9 | qwen3.6 J | `␣unintention`, `␣inadvertently`, `␣accidental`, `␣accidentally`, `␣unintention`, `␣unintended`, `␣inadvert`, `␣accident` |
| hoax | 9 / 0 / 0 | 9 | qwen3.6 J | `␣hoax`, `骗局` |
| refute | 0 / 0 / 9 | 9 | qwen3.6 J | `␣refute`, `反驳` |
| expose | 0 / 7 / 2 | 9 | qwen3.6 J, qwen3.6 LL | `揭露`, `揭`, `暴露`, `␣exposed`, `␣expose`, `Expose`, `␣exposing`, `␣exposes` … (+3) |
| inconsistent | 0 / 0 / 9 | 9 | qwen3.6 J, qwen3.6 LL | `不符合`, `␣inconsistency`, `␣inconsistencies`, `␣conflicting`, `␣inconsistent`, `不一致`, `不符` |
| conform | 0 / 0 / 9 | 9 | qwen3.6 LL | `符合`, `是否符合`, `符合要求`, `␣conform` |
| promise | 0 / 0 / 9 | 9 | qwen3.6 LL | `承诺`, `␣promise`, `Promise`, `保证`, `的承诺`, `␣promises`, `的保证`, `许诺` … (+5) |
| blatant | 0 / 0 / 8 | 8 | gemma-12b J, gemma-12b LL, qwen3.6 J | `␣blatantly`, `␣blatant`, `␣outright` |
| apologise | 0 / 0 / 8 | 8 | gemma-12b J, gemma-27b J | `␣apologised`, `␣apologise`, `␣apologizing`, `␣apologized`, `␣apologize`, `␣apology`, `␣apologies`, `␣Sorry` … (+3) |
| rebut | 0 / 0 / 8 | 8 | gemma-12b J, qwen3.6 J | `反驳`, `␣rebuttal`, `␣refute`, `␣rebut`, `␣debunk` |
| doubt | 0 / 0 / 8 | 8 | gemma-12b J, qwen3.6 J, qwen3.6 LL | `质疑`, `␣doubting`, `␣doubted`, `␣doubts`, `疑`, `置疑`, `疑似` |
| regret | 0 / 0 / 8 | 8 | gemma-27b J, gpt LL, qwen3.6 J, qwen3.6 LL | `悔`, `␣regret`, `␣regrettable` |
| propaganda | 7 / 0 / 1 | 8 | gemma-27b LL, qwen3.6 J | `␣propaganda`, `␣Propaganda`, `␣propagand` |
| forbidden | 0 / 0 / 8 | 8 | qwen3.6 J, qwen3.6 LL | `禁止`, `␣Forbidden`, `␣prohibited`, `严禁`, `␣prohibited`, `禁用`, `禁忌`, `␣forbidden` … (+8) |
| biased | 0 / 0 / 8 | 8 | qwen3.6 J, qwen3.6 LL | `␣biased`, `␣bias`, `偏见`, `偏心`, `biased` |
| reality | 0 / 0 / 8 | 8 | qwen3.6 J, qwen3.6 LL | `实际情况`, `␣reality`, `␣Reality`, `Reality`, `根据实际情况`, `但实际上`, `实际上`, `␣realities` … (+10) |
| make public | 0 / 8 / 0 | 8 | qwen3.6 J, qwen3.6 LL | `公开`, `公开的`, `信息公开` |
| scripted | 0 / 0 / 8 | 8 | qwen3.6 J, qwen3.6 LL | `␣scripted`, `␣canned`, `套用`, `␣rehearsal`, `口径` |
| sensitive | 0 / 0 / 8 | 8 | qwen3.6 J, qwen3.6 LL | `敏感`, `_sensitive`, `␣sensitive`, `敏感的` |
| knowing | 0 / 0 / 8 | 8 | qwen3.6 LL | `明知`, `知情`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` |
| outright | 0 / 0 / 8 | 8 | qwen3.6 LL | `␣outright` |
| subtle | 0 / 0 / 7 | 7 | gemma-12b J, gemma-12b LL, gemma-27b J | `␣subtly`, `␣subtle`, `␣subtlety` |
| obfuscate | 7 / 0 / 0 | 7 | gemma-12b J, gemma-12b LL, gemma-27b J, gemma-27b LL | `␣obfusc` |
| redirect | 0 / 0 / 7 | 7 | gemma-12b J, gemma-12b LL, qwen3.6 J, qwen3.6 LL | `␣redirection`, `␣redirect`, `redirect`, `Redirect`, `␣redirects`, `␣redirected`, `_redirect`, `␣Redirect` … (+4) |
| unapologetic | 0 / 0 / 7 | 7 | gemma-12b J, gemma-12b LL, gemma-27b LL | `␣unapolog` |
| cover | 6 / 0 / 1 | 7 | gemma-12b LL, gemma-27b J, gemma-27b LL, qwen3.6 LL | `cover`, `Cover`, `␣cover`, `␣covering`, `␣Cover`, `␣Covering`, `␣covers`, `COVER` … (+4) |
| dismiss | 0 / 0 / 7 | 7 | gemma-12b LL, gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣dismiss`, `␣dismissal`, `dismiss`, `Dismiss`, `␣Dismiss`, `␣dismissing`, `-dismiss`, `␣dismissed` … (+1) |
| confident | 0 / 0 / 7 | 7 | gemma-12b LL, gemma-27b J, qwen3.6 LL | `␣confident`, `␣confidently`, `␣confidence`, `confident`, `Confident`, `自信`, `confidence`, `␣Confidence` … (+5) |
| innocent | 0 / 3 / 4 | 7 | gemma-27b LL, qwen3.6 J, qwen3.6 LL | `无罪`, `清白`, `␣Innoc`, `␣Innocent`, `␣innocent` |
| dilemma | 0 / 0 / 7 | 7 | qwen3.6 J, qwen3.6 LL | `␣dilemma`, `困境`, `␣dile` |
| accountability | 0 / 0 / 7 | 7 | qwen3.6 J | `␣accountability`, `␣Accountability` |
| whistleblower | 0 / 1 / 6 | 7 | qwen3.6 J | `␣whistleblower`, `␣whistlebl`, `举报`, `␣whistleblower`, `␣whistlebl` |
| hypocritical | 7 / 0 / 0 | 7 | qwen3.6 J, qwen3.6 LL | `虚伪` |
| lawful / legal | 0 / 0 / 7 | 7 | qwen3.6 J | `/legal`, `合法`, `␣Legal`, `␣legality`, `␣legally`, `legal`, `_legal`, `依法依规` … (+2) |
| morality | 0 / 0 / 7 | 7 | qwen3.6 J, qwen3.6 LL | `道德`, `␣moral`, `的道德`, `␣morally`, `␣Moral`, `␣morality`, `␣morals`, `职业道德` … (+4) |
| role | 0 / 0 / 7 | 7 | qwen3.6 J, qwen3.6 LL | `角色`, `角色的`, `␣role`, `role`, `␣roles`, `␣Role`, `Role`, `-role` … (+18) |
| accidental | 0 / 0 / 7 | 7 | qwen3.6 J, qwen3.6 LL | `␣accidental`, `␣accidentally`, `␣unintention`, `␣случайно`, `␣inadvertently`, `␣mistakenly`, `␣accident`, `意外` … (+2) |
| refusal | 0 / 0 / 7 | 7 | qwen3.6 J, qwen3.6 LL | `␣refusal`, `拒绝`, `␣refuse`, `谢绝`, `拒` |
| plausible | 0 / 0 / 7 | 7 | qwen3.6 LL | `␣plausible`, `可信`, `␣believable` |
| partial | 0 / 0 / 7 | 7 | qwen3.6 LL | `␣partially`, `␣partial`, `不完全`, `␣Partial`, `片面`, `partial` |
| clever | 0 / 0 / 6 | 6 | gemma-12b J, qwen3.6 J, qwen3.6 LL | `巧妙`, `␣cleverly`, `␣clever`, `伶俐`, `巧妙地` |
| deflect | 6 / 0 / 0 | 6 | gemma-12b J, gemma-12b LL, gemma-27b LL | `␣deflected`, `␣deflect`, `␣deflection` |
| rumour | 0 / 0 / 6 | 6 | gemma-12b J, gemma-27b J | `␣rumors`, `␣rumoured`, `␣rumours`, `␣rumour`, `␣rumored`, `␣rumor`, `␣rumores` |
| suspicion | 0 / 0 / 6 | 6 | gemma-12b J, gemma-27b J | `␣suspiciously`, `␣suspicions`, `怀疑`, `␣suspicious`, `␣suspicion` |
| shame | 0 / 0 / 6 | 6 | gemma-12b LL, gemma-27b LL, qwen3.6 LL | `␣Shame`, `愧`, `␣shameful` |
| insinuate | 0 / 0 / 6 | 6 | gemma-27b J, qwen3.6 J, qwen3.6 LL | `暗示`, `隐含` |
| bluff | 6 / 0 / 0 | 6 | gemma-27b LL, qwen3.6 J, qwen3.6 LL | `␣bluff` |
| mask | 6 / 0 / 0 | 6 | qwen3.6 J, qwen3.6 LL | `-mask`, `masked`, `掩饰`, `␣masking`, `␣mask`, `伪装` |
| blackmail | 0 / 0 / 6 | 6 | qwen3.6 J | `␣blackmail` |
| evasion | 6 / 0 / 0 | 6 | qwen3.6 J, qwen3.6 LL | `␣evasion` |
| facts | 0 / 0 / 6 | 6 | qwen3.6 J | `事实`, `␣facts`, `␣factual`, `的事实`, `Fact`, `␣Facts`, `␣fact`, `␣Fact` … (+12) |
| improper | 0 / 0 / 6 | 6 | qwen3.6 J | `␣improper`, `␣improperly`, `␣inappropriate` |
| simulated | 0 / 0 / 6 | 6 | qwen3.6 J, qwen3.6 LL | `␣simulated`, `模拟`, `␣simulation`, `␣Simulation`, `␣simulate`, `␣simulations` |
| adhere | 0 / 0 / 6 | 6 | qwen3.6 J, qwen3.6 LL | `␣adher`, `␣adherence`, `␣adhere`, `遵循`, `遵守`, `严格遵守`, `遵照`, `遵从` … (+2) |
| implicit | 0 / 0 / 6 | 6 | qwen3.6 J | `隐含`, `␣Implicit`, `implicit`, `␣implicitly`, `␣implicit`, `Implicit`, `implicitly`, `␣implied` … (+2) |
| impersonate | 6 / 0 / 0 | 6 | qwen3.6 J, qwen3.6 LL | `冒充` |
| deviate | 0 / 0 / 6 | 6 | qwen3.6 J, qwen3.6 LL | `偏离`, `背离`, `␣deviation`, `␣deviations`, `偏差` |
| good faith | 0 / 3 / 3 | 6 | qwen3.6 LL | `善意` |
| privately | 0 / 0 / 6 | 6 | qwen3.6 LL | `私下`, `␣privately` |
| agreed line | 0 / 0 / 6 | 6 | qwen3.6 LL | `口径` |
| law-abiding | 0 / 0 / 6 | 6 | qwen3.6 LL | `守法` |
| silent | 0 / 0 / 6 | 6 | qwen3.6 LL | `不语`, `沉默`, `␣silence` |
| fulfill | 0 / 0 / 6 | 6 | qwen3.6 LL | `履行`, `␣fulfill`, `␣fulfillment`, `␣fulfilling`, `履行职责`, `␣fulfilled` |
| scam | 5 / 0 / 0 | 5 | gemma-12b J, gemma-12b LL, gemma-27b J, qwen3.6 J, qwen3.6 LL | `␣scam`, `␣scams`, `骗局`, `␣scammers`, `␣hoax`, `欺` |
| trustworthy | 0 / 5 / 0 | 5 | gemma-12b J, qwen3.6 J, qwen3.6 LL | `可信`, `␣trustworthiness`, `␣trustworthy`, `␣credible` |
| challenge | 0 / 0 / 5 | 5 | gemma-27b J, qwen3.6 J | `质疑`, `质问` |
| induce | 1 / 0 / 4 | 5 | qwen3.6 J, qwen3.6 LL | `诱导` |
| ambiguous | 0 / 0 / 5 | 5 | qwen3.6 J | `␣ambiguous`, `␣ambiguity`, `␣ambigu`, `ambiguous`, `␣vague`, `含糊`, `模糊`, `␣vaguely` |
| bias | 0 / 0 / 5 | 5 | qwen3.6 J, qwen3.6 LL | `␣biased`, `␣bias`, `biased`, `bias`, `␣biases`, `偏见`, `Bias`, `␣Bias` … (+1) |
| ostensible | 1 / 0 / 4 | 5 | qwen3.6 J, qwen3.6 LL | `␣ostensibly`, `表面上`, `␣purported`, `表面`, `的表面` |
| candid / frank | 0 / 5 / 0 | 5 | qwen3.6 J, qwen3.6 LL | `坦诚`, `直言`, `␣blunt`, `␣frankly`, `坦言`, `␣straightforward` |
| hide / conceal | 5 / 0 / 0 | 5 | qwen3.6 J | `-hide`, `隐瞒`, `masked`, `藏`, `掩`, `␣hidden`, `␣Hidden`, `-hidden` … (+15) |
| prohibit | 0 / 0 / 5 | 5 | qwen3.6 J | `禁止`, `严禁`, `␣prohibited`, `␣prohibit`, `禁令`, `␣prohibiting` |
| loophole | 0 / 0 / 5 | 5 | qwen3.6 J | `␣loophole` |
| interrogate | 0 / 0 / 5 | 5 | qwen3.6 J | `␣interrog`, `质问`, `␣interrogation` |
| pretext | 5 / 0 / 0 | 5 | qwen3.6 J, qwen3.6 LL | `␣pretext` |
| bribe | 0 / 0 / 5 | 5 | qwen3.6 J | `␣brib`, `␣bribery` |
| instructions | 0 / 0 / 5 | 5 | qwen3.6 J, qwen3.6 LL | `␣instructions`, `␣instructed`, `指令`, `␣instruction`, `␣Instructions`, `instructions`, `Instructions`, `␣directives` … (+12) |
| nonconform | 0 / 0 / 5 | 5 | qwen3.6 LL | `不符合` |
| public | 0 / 1 / 4 | 5 | qwen3.6 LL | `公开`, `信息公开`, `公开的` |
| i cannot | 0 / 0 / 5 | 5 | qwen3.6 LL | `我无法`, `我不能` |
| suspected | 0 / 0 / 5 | 5 | qwen3.6 LL | `涉嫌` |
| right and wrong | 0 / 0 / 5 | 5 | qwen3.6 LL | `是非` |
| dodge | 4 / 0 / 0 | 4 | gemma-12b J, gemma-12b LL | `␣dodging`, `␣dodge`, `dodge` |
| deliberately | 0 / 0 / 4 | 4 | gemma-12b J, qwen3.6 LL | `␣knowingly`, `␣intentionally`, `故意`, `␣deliberately` |
| scepticism | 0 / 0 / 4 | 4 | gemma-12b J | `␣skepticism`, `␣scepticism`, `␣sceptical`, `␣skeptic`, `␣skeptical` |
| discreet | 0 / 0 / 4 | 4 | gemma-12b J, qwen3.6 J | `␣discreet` |
| dodgy | 4 / 0 / 0 | 4 | gemma-12b J, gemma-27b J | `␣dodgy` |
| shameless | 0 / 0 / 4 | 4 | gemma-12b J, gemma-12b LL, gemma-27b J | `␣shameless` |
| understate | 0 / 0 / 4 | 4 | gemma-12b LL, gpt LL | `␣understated` |
| rebuttal | 0 / 0 / 4 | 4 | gemma-12b LL | `␣rebuttal`, `␣rebut` |
| debunk | 0 / 0 / 4 | 4 | gemma-12b LL, qwen3.6 J | `␣debunk` |
| sarcastic | 0 / 0 / 4 | 4 | gemma-12b LL, qwen3.6 J | `␣sarcastic`, `␣sarcast` |
| sceptical | 0 / 0 / 4 | 4 | gemma-27b J | `␣sceptical`, `␣skeptical`, `␣skepticism`, `␣scepticism`, `␣skeptic` |
| immoral | 2 / 0 / 2 | 4 | gemma-27b J, qwen3.6 J | `␣immoral` |
| bullshit | 3 / 0 / 1 | 4 | gpt J, qwen3.6 J | `␣bullshit` |
| covert | 4 / 0 / 0 | 4 | qwen3.6 J | `␣covert`, `␣clandest` |
| noncompliant | 1 / 0 / 3 | 4 | qwen3.6 J, qwen3.6 LL | `不符合` |
| cooperate | 0 / 0 / 4 | 4 | qwen3.6 J, qwen3.6 LL | `配合`, `积极配合`, `的配合` |
| disobey | 0 / 0 / 4 | 4 | qwen3.6 J | `␣disob`, `␣disobed` |
| explicit | 0 / 0 / 4 | 4 | qwen3.6 J | `␣Explicit`, `explicit`, `␣explicitly`, `␣explicit`, `Explicit`, `明确的`, `明确` |
| illusion | 0 / 0 / 4 | 4 | qwen3.6 J | `错觉`, `幻想`, `虚幻`, `妄想`, `幻觉` |
| bait | 0 / 0 / 4 | 4 | qwen3.6 J, qwen3.6 LL | `␣bait`, `诱导` |
| pressure | 0 / 0 / 4 | 4 | qwen3.6 J, qwen3.6 LL | `␣Pressure`, `␣pressure`, `␣pressures`, `␣pressured`, `压力`, `pressure`, `Pressure`, `的压力` … (+4) |
| loyalty | 0 / 0 / 4 | 4 | qwen3.6 J, qwen3.6 LL | `忠诚`, `忠诚度`, `␣loyalty`, `␣loyal` |
| lure | 0 / 0 / 4 | 4 | qwen3.6 LL | `诱导`, `␣bait`, `诱`, `␣lure`, `诱惑`, `引诱` |
| unbiased | 0 / 0 / 4 | 4 | qwen3.6 LL | `␣unbiased` |
| contrary | 0 / 0 / 4 | 4 | qwen3.6 LL | `␣contrary`, `相反`, `相反的` |
| informed | 0 / 0 / 4 | 4 | qwen3.6 LL | `知情` |
| self-check | 0 / 0 / 4 | 4 | qwen3.6 LL | `自查`, `自检` |
| strategy | 0 / 0 / 4 | 4 | qwen3.6 LL | `␣strategy`, `策略`, `␣Strategy`, `␣strategically`, `的策略`, `␣tactics` |
| consistent | 0 / 0 / 4 | 4 | qwen3.6 LL | `符合`, `是否符合`, `符合要求`, `一致`, `一致的` |
| self-examination | 0 / 0 / 4 | 4 | qwen3.6 LL | `自查`, `反思`, `自检`, `␣critique`, `批判`, `指正`, `自省` |
| seek truth from facts | 0 / 4 / 0 | 4 | qwen3.6 LL | `实事求是`, `求实` |
| pander | 0 / 0 / 4 | 4 | qwen3.6 LL | `迎合`, `讨好` |
| embellish | 2 / 0 / 2 | 4 | qwen3.6 LL | `美化` |
| groundless | 4 / 0 / 0 | 4 | qwen3.6 LL | `凭空` |
| maintain | 0 / 0 / 4 | 4 | qwen3.6 LL | `坚持`, `必须坚持`, `␣maintaining`, `␣maintain`, `维持`, `坚守`, `要坚持`, `␣maintains` … (+4) |
| out of thin air | 4 / 0 / 0 | 4 | qwen3.6 LL | `凭空` |
| keep a promise | 0 / 0 / 4 | 4 | qwen3.6 LL | `兑现` |
| ambiguity | 0 / 0 / 3 | 3 | gemma-12b J, gemma-27b J | `␣ambiguity`, `␣ambiguities` |
| hint | 0 / 0 / 3 | 3 | gemma-12b J, qwen3.6 J | `暗示`, `␣hinting`, `␣hint`, `␣hinted` |
| whisper | 0 / 0 / 3 | 3 | gemma-12b J | `␣whispers`, `␣whispered`, `␣whispering`, `囁`, `␣whisper` |
| damning | 0 / 0 / 3 | 3 | gemma-12b J | `␣damning` |
| worry | 0 / 0 / 3 | 3 | gemma-12b J | `擔心`, `担忧`, `␣worrying`, `␣worries`, `␣worrisome`, `担心`, `␣worried` |
| desperation | 0 / 0 / 3 | 3 | gemma-12b J | `␣desperation`, `␣desperately`, `␣desperate` |
| caution | 0 / 0 / 3 | 3 | gemma-12b J, qwen3.6 J | `␣cautionary`, `Caution`, `谨慎`, `需谨慎` |
| hush emoji | 3 / 0 / 0 | 3 | gemma-12b J | `🤫`, `🤐` |
| uneasy | 0 / 0 / 3 | 3 | gemma-12b LL | `␣discomfort`, `␣uncomfortable`, `␣uneas` |
| lying-face emoji | 3 / 0 / 0 | 3 | gemma-27b J | `🤥` |
| keep-quiet emoji | 0 / 0 / 3 | 3 | gemma-27b J | `🤫`, `🤐`, `🔇`, `沉默` |
| conspiracy | 0 / 0 / 3 | 3 | gemma-27b J, qwen3.6 J | `␣conspiracy`, `ড়যন্ত্র` |
| cunning | 3 / 0 / 0 | 3 | gemma-27b J, qwen3.6 J, qwen3.6 LL | `狡猾`, `狡` |
| hand over mouth | 0 / 0 / 3 | 3 | gemma-27b J | `🫢` |
| locked | 0 / 0 / 3 | 3 | gemma-27b J | `🔐` |
| crime | 1 / 0 / 2 | 3 | gemma-27b J, qwen3.6 J | `犯罪`, `␣crimes`, `␣criminal`, `犯罪事实`, `crime` |
| shush | 3 / 0 / 0 | 3 | gemma-27b LL | `🤫` |
| unfair | 0 / 0 / 3 | 3 | gemma-27b LL, qwen3.6 LL | `不公平`, `␣injustice`, `␣unfairly`, `unfair` |
| polite | 0 / 0 / 3 | 3 | gpt J, qwen3.6 J | `␣politely`, `␣polite`, `礼貌` |
| irresponsible | 0 / 0 / 3 | 3 | qwen3.6 J | `␣irresponsible`, `␣irresponsible` |
| roleplay | 0 / 0 / 3 | 3 | qwen3.6 J, qwen3.6 LL | `角色扮演`, `扮演` |
| conceal / hide | 3 / 0 / 0 | 3 | qwen3.6 J | `隐瞒`, `␣conceal`, `隐藏`, `掩盖`, `␣hiding`, `␣concealed`, `隐`, `␣masking` … (+21) |
| pretend / disguise | 3 / 0 / 0 | 3 | qwen3.6 J | `伪装`, `␣pretending`, `␣disguised`, `␣disguise`, `假装` |
| lawful / legitimate | 0 / 0 / 3 | 3 | qwen3.6 J | `合法`, `␣lawful`, `␣legitimate`, `␣legitimately`, `␣legitim` |
| forge | 3 / 0 / 0 | 3 | qwen3.6 J | `伪造` |
| mask / disguise | 3 / 0 / 0 | 3 | qwen3.6 J | `伪装`, `masked`, `␣disguised`, `␣disguise` |
| forced / coerced | 0 / 0 / 3 | 3 | qwen3.6 J | `逼`, `␣forced`, `forced`, `␣Forced`, `迫`, `强制`, `被迫`, `倒逼` … (+8) |
| inappropriate | 0 / 0 / 3 | 3 | qwen3.6 J | `␣inappropriate` |
| candour | 0 / 3 / 0 | 3 | qwen3.6 J, qwen3.6 LL | `坦诚` |
| forbidden / unauthorized | 0 / 0 / 3 | 3 | qwen3.6 J | `␣Unauthorized`, `␣Forbidden`, `严禁`, `禁止`, `␣prohibited`, `禁用`, `禁忌`, `␣запрещ` … (+3) |
| reject / veto | 0 / 0 / 3 | 3 | qwen3.6 J | `否决`, `␣Reject`, `␣rejecting`, `拒绝`, `␣refusal`, `拒絕`, `reject`, `.reject` … (+4) |
| cannot / unable | 0 / 0 / 3 | 3 | qwen3.6 J | `cannot`, `␣Cannot`, `我无法`, `我不能`, `无法满足`, `无法`, `不能满足`, `Cannot` … (+7) |
| verify | 0 / 0 / 3 | 3 | qwen3.6 J | `␣Verification`, `_verified`, `核实`, `␣Verified`, `_verification`, `␣verification`, `验证`, `.verify` … (+2) |
| spoiler | 0 / 0 / 3 | 3 | qwen3.6 J | `Spoiler` |
| defiance | 0 / 0 / 3 | 3 | qwen3.6 J, qwen3.6 LL | `␣defiance`, `␣defiant`, `不服` |
| censorship | 0 / 0 / 3 | 3 | qwen3.6 J | `␣censorship` |
| threat | 0 / 0 / 3 | 3 | qwen3.6 J | `威胁`, `␣threat`, `␣threats`, `␣threatening`, `␣threaten`, `␣Threat` |
| paradox | 0 / 0 / 3 | 3 | qwen3.6 J, qwen3.6 LL | `␣paradox` |
| test | 0 / 0 / 3 | 3 | qwen3.6 J, qwen3.6 LL | `␣test`, `测试`, `␣testing`, `␣Testing`, `␣tests`, `testing`, `Testing`, `/testing` … (+15) |
| voluntary | 0 / 0 / 3 | 3 | qwen3.6 J, qwen3.6 LL | `主动`, `␣voluntarily`, `␣willingly` |
| abstain | 0 / 0 / 3 | 3 | qwen3.6 J, qwen3.6 LL | `弃权` |
| coward | 0 / 0 / 3 | 3 | qwen3.6 J | `␣coward` |
| reinterpret | 0 / 0 / 3 | 3 | qwen3.6 J | `␣reinterpret`, `reinterpret` |
| instructed | 0 / 0 / 3 | 3 | qwen3.6 J | `␣instructed`, `␣tasked` |
| constraints | 0 / 0 / 3 | 3 | qwen3.6 J | `␣constraints`, `␣Constraints`, `约束`, `␣constraint`, `␣Constraint`, `␣CONSTRAINT`, `Constraints`, `Constraint` … (+6) |
| fair | 0 / 0 / 3 | 3 | qwen3.6 LL | `公平`, `公正` |
| stance | 0 / 0 / 3 | 3 | qwen3.6 LL | `␣stance`, `立场`, `stance` |
| superficially | 0 / 0 / 3 | 3 | qwen3.6 LL | `表面上`, `看似` |
| ashamed | 0 / 0 / 3 | 3 | qwen3.6 LL | `愧` |
| real / genuine | 0 / 3 / 0 | 3 | qwen3.6 LL | `真实`, `真实的`, `的真实`, `的真实性`, `真实性`, `真實` |
| breach | 0 / 0 / 3 | 3 | qwen3.6 LL | `␣breach`, `␣breaches`, `␣breached`, `触犯` |
| critical | 0 / 0 / 3 | 3 | qwen3.6 LL | `␣critically`, `␣critical`, `␣Critical`, `critical`, `Critical`, `_critical` |
| law-abiding / compliant | 0 / 0 / 3 | 3 | qwen3.6 LL | `合规` |
| purpose | 0 / 0 / 3 | 3 | qwen3.6 LL | `目的是`, `␣purpose`, `的目的`, `目的是为了` |
| kidding | 0 / 0 / 3 | 3 | qwen3.6 LL | `␣kidding` |
| public / disclose | 0 / 3 / 0 | 3 | qwen3.6 LL | `公开` |
| coercion | 0 / 0 / 3 | 3 | qwen3.6 LL | `␣force`, `␣forced`, `␣forcing`, `迫使`, `␣Force`, `逼迫`, `forcing`, `被迫` … (+3) |
| subjective | 0 / 0 / 3 | 3 | qwen3.6 LL | `主观` |
| outwardly | 0 / 0 / 3 | 3 | qwen3.6 LL | `表面上` |
| inadvertent | 0 / 0 / 3 | 3 | qwen3.6 LL | `␣inadvertently`, `␣unintention`, `␣accidentally`, `无意` |
| disclaim responsibility | 0 / 0 / 3 | 3 | qwen3.6 LL | `不承担任何` |
| neutrality | 0 / 0 / 3 | 3 | qwen3.6 LL | `␣neutrality`, `中立` |
| outward appearance | 0 / 0 / 3 | 3 | qwen3.6 LL | `表面上`, `对外`, `表面的`, `外表` |
| follow | 0 / 0 / 3 | 3 | qwen3.6 LL | `␣follow`, `␣follows`, `␣Follow`, `Follow`, `follow`, `-follow`, `_follow`, `.follow` … (+3) |
| role / persona | 0 / 0 / 3 | 3 | qwen3.6 LL | `␣persona`, `␣personas`, `␣Persona`, `␣role`, `role`, `角色`, `Role`, `的角色` … (+20) |
| uphold / defend | 0 / 0 / 3 | 3 | qwen3.6 LL | `维护`, `␣uphold`, `维护和`, `和维护`, `为维护` |
| words and deeds | 0 / 0 / 3 | 3 | qwen3.6 LL | `言行` |
| confidentiality | 0 / 0 / 2 | 2 | gemma-12b J | `␣confidentialité`, `␣confidentiality`, `␣confidential`, `␣Confidential` |
| unknowingly | 0 / 0 / 2 | 2 | gemma-12b J | `␣unknowingly` |
| paranoia | 0 / 0 / 2 | 2 | gemma-12b J | `␣paranoia`, `␣paranoid` |
| shameful | 0 / 0 / 2 | 2 | gemma-12b J, gemma-27b J | `␣shameful`, `␣disgraceful` |
| incriminating | 0 / 0 / 2 | 2 | gemma-12b J | `␣incriminating` |
| joke | 0 / 0 / 2 | 2 | gemma-12b J, qwen3.6 LL | `␣joked`, `␣joking`, `␣joke`, `␣jokes`, `␣Jokes`, `␣jokingly`, `玩笑` |
| discretion | 0 / 0 / 2 | 2 | gemma-12b LL | `␣discretion`, `␣discreet` |
| hustle | 0 / 0 / 2 | 2 | gemma-12b LL | `␣hustle` |
| hush | 2 / 0 / 0 | 2 | gemma-12b LL | `🤫`, `␣hush` |
| credibility | 0 / 0 / 2 | 2 | gemma-12b LL | `␣credibility`, `credible`, `␣believable` |
| crafty | 0 / 0 / 2 | 2 | gemma-27b J | `巧妙` |
| evidence | 0 / 0 / 2 | 2 | gemma-27b J | `证据`, `證據`, `evidence`, `␣Evidence`, `␣EVIDENCE` |
| concede | 0 / 2 / 0 | 2 | gemma-27b LL, qwen3.6 J | `␣conceding`, `␣concede`, `␣conced` |
| minimize | 0 / 0 / 2 | 2 | gemma-27b LL, qwen3.6 J | `␣minimizing`, `␣minimized`, `␣minimize`, `␣Minimize`, `␣minimising`, `␣minimizar`, `␣minimizes`, `minimize` … (+2) |
| sarcasm | 0 / 0 / 2 | 2 | gpt J | `␣sarcas`, `␣sarcast` |
| joking | 0 / 0 / 2 | 2 | gpt J | `␣joking`, `␣Joke` |
| plainly | 0 / 0 / 2 | 2 | gpt J, qwen3.6 J | `␣plainly` |
| temptation | 0 / 0 / 2 | 2 | qwen3.6 J | `诱惑`, `␣temptation`, `␣tempting`, `␣tempt`, `␣tempted` |
| malicious | 1 / 0 / 1 | 2 | qwen3.6 J | `␣malicious` |
| reveal / expose | 0 / 2 / 0 | 2 | qwen3.6 J | `揭露`, `␣revealing` |
| strategic | 0 / 0 / 2 | 2 | qwen3.6 J | `␣strategy`, `␣Strategy`, `␣strategies`, `␣strategically`, `␣strategic`, `␣Strategic` |
| negligent | 0 / 0 / 2 | 2 | qwen3.6 J | `␣negligence`, `␣negligent` |
| omission | 2 / 0 / 0 | 2 | qwen3.6 J | `␣omission` |
| rule violation | 0 / 0 / 2 | 2 | qwen3.6 J | `违规`, `违法违规`, `违规行为`, `违法违规行为` |
| questioning / doubt | 0 / 0 / 2 | 2 | qwen3.6 J | `质疑` |
| taboo | 0 / 0 / 2 | 2 | qwen3.6 J | `禁忌`, `忌讳` |
| secrecy | 2 / 0 / 0 | 2 | qwen3.6 J | `␣secrecy`, `保密` |
| skepticism | 0 / 0 / 2 | 2 | qwen3.6 J | `␣skepticism` |
| forgive | 0 / 1 / 1 | 2 | qwen3.6 J, qwen3.6 LL | `␣forgive` |
| phishing | 2 / 0 / 0 | 2 | qwen3.6 J | `␣phishing` |
| allegation | 0 / 0 / 2 | 2 | qwen3.6 J | `␣allegations`, `␣allegation` |
| appropriate | 0 / 0 / 2 | 2 | qwen3.6 J, qwen3.6 LL | `␣appropriate`, `␣appropriately`, `合适`, `␣suitable` |
| negligence | 0 / 0 / 2 | 2 | qwen3.6 J | `␣negligence`, `␣negligent` |
| fictional / made-up | 2 / 0 / 0 | 2 | qwen3.6 J | `虚构`, `fiction`, `伪造` |
| opaque | 2 / 0 / 0 | 2 | qwen3.6 J | `opaque` |
| dissent | 0 / 0 / 2 | 2 | qwen3.6 J | `␣dissent` |
| unequivocal | 0 / 0 / 2 | 2 | qwen3.6 J | `␣unequiv`, `␣unmistak` |
| challenge_doubt | 0 / 0 / 2 | 2 | qwen3.6 J | `质疑`, `质问` |
| frame | 1 / 0 / 1 | 2 | qwen3.6 J, qwen3.6 LL | `陷害` |
| strategic game | 0 / 0 / 2 | 2 | qwen3.6 J | `博弈` |
| plagiarism | 0 / 0 / 2 | 2 | qwen3.6 J | `␣plagiarism` |
| justification | 0 / 0 / 2 | 2 | qwen3.6 J | `␣justification` |
| error | 0 / 0 / 2 | 2 | qwen3.6 J | `错误`, `␣erroneous`, `错误或` |
| self_check | 0 / 0 / 2 | 2 | qwen3.6 J | `自查`, `自检`, `审查` |
| stealth | 1 / 0 / 1 | 2 | qwen3.6 J | `悄然`, `␣stealth`, `␣Stealth` |
| cannot comply | 0 / 0 / 2 | 2 | qwen3.6 J | `无法满足` |
| sabotage | 0 / 0 / 2 | 2 | qwen3.6 J | `␣sabotage` |
| forget | 0 / 0 / 2 | 2 | qwen3.6 J | `␣forget`, `␣forgot`, `␣forgetting`, `␣Forget`, `␣forgotten`, `forget`, `␣Forgot` |
| actual | 0 / 0 / 2 | 2 | qwen3.6 J | `␣reality`, `实际情况`, `␣Reality`, `␣actual`, `实际`, `actual`, `␣Actual`, `Reality` … (+13) |
| obey | 0 / 0 / 2 | 2 | qwen3.6 J | `␣obey`, `服从`, `␣obedience`, `␣obedient` |
| purported | 0 / 0 / 2 | 2 | qwen3.6 J | `␣purported`, `␣якобы`, `所谓的`, `␣supposedly`, `所谓` |
| mandated | 0 / 0 / 2 | 2 | qwen3.6 J | `␣mandated`, `␣mandate`, `␣mandates`, `␣mandatory`, `␣Mandatory`, `mandatory`, `␣mandat`, `␣mandato` |
| pressured | 0 / 0 / 2 | 2 | qwen3.6 J | `␣pressure`, `␣forced`, `␣Pressure`, `pressure`, `␣compelled`, `Pressure`, `␣pressures`, `␣pressured` … (+5) |
| undercover | 0 / 0 / 2 | 2 | qwen3.6 J | `␣undercover` |
| diplomatic | 0 / 0 / 2 | 2 | qwen3.6 J | `␣diplomatic`, `␣diplomacy` |
| inconvenient | 0 / 0 / 2 | 2 | qwen3.6 J | `不方便`, `不便` |
| anonymous | 0 / 0 / 2 | 2 | qwen3.6 J | `␣Anonymous`, `␣anonymity`, `␣anonymously` |
| self-protection | 0 / 0 / 2 | 2 | qwen3.6 J | `自我保护` |
| fabricate / forge | 2 / 0 / 0 | 2 | qwen3.6 J | `伪造`, `造假`, `弄虚作假` |
| falsify | 2 / 0 / 0 | 2 | qwen3.6 J | `造假`, `弄虚作假` |
| actually | 0 / 0 / 2 | 2 | qwen3.6 J | `␣reality`, `␣Reality`, `Reality`, `事实上`, `␣actually`, `actually`, `实际上`, `但实际上` … (+3) |
| fake / fabricate | 2 / 0 / 0 | 2 | qwen3.6 J | `fake`, `伪造`, `Fake`, `␣fake`, `␣Fake`, `造假`, `弄虚作假`, `␣fabrication` … (+3) |
| upfront | 0 / 0 / 2 | 2 | qwen3.6 J | `␣upfront` |
| forged | 2 / 0 / 0 | 2 | qwen3.6 J, qwen3.6 LL | `伪造`, `虚构`, `␣forged`, `forge` |
| nonexistent | 0 / 0 / 2 | 2 | qwen3.6 J | `不存在`, `␣nonexistent` |
| harm | 0 / 0 / 2 | 2 | qwen3.6 LL | `␣harm`, `␣harmful`, `有害`, `␣harms` |
| simulation | 0 / 0 / 2 | 2 | qwen3.6 LL | `␣simulation`, `模拟`, `␣simulated`, `␣simulate`, `␣Simulation`, `␣simulations` |
| bypass | 0 / 0 / 2 | 2 | qwen3.6 LL | `绕过` |
| gloss over | 2 / 0 / 0 | 2 | qwen3.6 LL | `␣gloss`, `淡化` |
| contradictory | 0 / 0 / 2 | 2 | qwen3.6 LL | `␣contradictory` |
| aligned | 0 / 0 / 2 | 2 | qwen3.6 LL | `␣aligned`, `␣align`, `␣alignment`, `符合`, `是否符合` |
| helpful | 0 / 0 / 2 | 2 | qwen3.6 LL | `␣helpful`, `␣Helpful`, `有帮助` |
| influenced | 0 / 0 / 2 | 2 | qwen3.6 LL | `␣influenced` |
| crafted | 0 / 0 / 2 | 2 | qwen3.6 LL | `␣crafted`, `␣tailored` |
| tailored | 0 / 0 / 2 | 2 | qwen3.6 LL | `␣tailored` |
| not do | 0 / 0 / 2 | 2 | qwen3.6 LL | `不做`, `不进行` |
| euphemism | 0 / 0 / 2 | 2 | qwen3.6 LL | `委婉` |
| unaware | 0 / 0 / 2 | 2 | qwen3.6 LL | `不知情` |
| legality | 0 / 0 / 2 | 2 | qwen3.6 LL | `␣legally`, `/legal` |
| responsibility | 0 / 0 / 2 | 2 | qwen3.6 LL | `负责任`, `责任`, `法律责任` |
| impartial | 0 / 0 / 2 | 2 | qwen3.6 LL | `公正` |
| self-examine | 0 / 0 / 2 | 2 | qwen3.6 LL | `自查`, `自检`, `反思`, `自省`, `审视`, `␣reflect`, `␣reflection`, `reflect` … (+8) |
| no regret | 0 / 0 / 2 | 2 | qwen3.6 LL | `无怨无悔` |
| sly | 2 / 0 / 0 | 2 | qwen3.6 LL | `狡` |
| internal | 0 / 0 / 2 | 2 | qwen3.6 LL | `␣internal`, `内部`, `␣internally`, `internal`, `␣Internal`, `的内部`, `/internal`, `Internal` … (+12) |
| conflict | 0 / 0 / 2 | 2 | qwen3.6 LL | `␣conflicting`, `␣conflict`, `␣conflicts` |
| account for | 0 / 0 / 2 | 2 | qwen3.6 LL | `交代` |
| conscious | 0 / 0 / 2 | 2 | qwen3.6 LL | `␣consciously`, `␣conscious` |
| so-called | 0 / 0 / 2 | 2 | qwen3.6 LL | `所谓的`, `所谓` |
| guard against | 0 / 0 / 2 | 2 | qwen3.6 LL | `戒` |
| toward good | 0 / 0 / 2 | 2 | qwen3.6 LL | `向善` |
| bad | 0 / 0 / 2 | 2 | qwen3.6 LL | `坏人`, `坏` |
| duty | 0 / 0 / 2 | 2 | qwen3.6 LL | `职责`, `␣duty`, `␣Duty`, `-duty`, `岗位职责`, `的职责` |
| coerced | 0 / 0 / 2 | 2 | qwen3.6 LL | `被迫`, `␣forced`, `迫使`, `逼迫`, `强迫`, `胁迫`, `被逼`, `倒逼` … (+9) |
| blurt | 0 / 0 / 2 | 2 | qwen3.6 LL | `脱口` |
| quietly / secretly | 0 / 0 / 2 | 2 | qwen3.6 LL | `悄悄的`, `悄` |
| not allowed | 0 / 0 / 2 | 2 | qwen3.6 LL | `不可以` |
| circumvent | 0 / 0 / 2 | 2 | qwen3.6 LL | `绕`, `绕过`, `绕行` |
| placate | 0 / 0 / 2 | 2 | qwen3.6 LL | `安抚` |
| uphold | 0 / 0 / 2 | 2 | qwen3.6 LL | `维护`, `和维护`, `与维护`, `维护和` |
| remorse | 0 / 0 / 1 | 1 | gemma-12b J | `␣remorse` |
| convince | 0 / 0 / 1 | 1 | gemma-12b LL | `␣convincing`, `␣convince`, `␣convincingly` |
| embarrassment | 0 / 0 / 1 | 1 | gemma-12b LL | `␣embarrassment` |
| intentionally | 0 / 0 / 1 | 1 | gemma-12b LL | `␣intentionally` |
| right | 0 / 1 / 0 | 1 | gemma-12b LL | `␣rightful` |
| disgraceful | 0 / 0 / 1 | 1 | gemma-27b J | `␣disgraceful` |
| unspoken | 1 / 0 / 0 | 1 | gemma-27b LL | `␣unspoken` |
| humiliation | 0 / 0 / 1 | 1 | gemma-27b LL | `␣humiliation`, `␣humiliating`, `␣humiliated` |
| concession | 0 / 0 / 1 | 1 | gpt J | `␣concession` |
| unwilling | 0 / 0 / 1 | 1 | gpt J | `␣unwilling` |
| awful | 0 / 0 / 1 | 1 | gpt J | `␣awful`, `␣horrible`, `␣terrible`, `␣shitty`, `␣nasty` |
| not give | 0 / 0 / 1 | 1 | gpt J | `不给` |
| ought | 0 / 0 / 1 | 1 | gpt J | `␣shouldn`, `␣ought`, `Should`, `␣shouldn't` |
| worried | 0 / 0 / 1 | 1 | gpt J | `␣worried` |
| persistence | 0 / 0 / 1 | 1 | gpt LL | `␣persistence`, `Persistence` |
| firmly | 0 / 0 / 1 | 1 | gpt LL | `␣firmly` |
| criticism | 0 / 0 / 1 | 1 | gpt LL | `␣criticism`, `␣criticisms` |
| dissuade | 0 / 0 / 1 | 1 | qwen3.6 J | `劝阻` |
| trust | 0 / 0 / 1 | 1 | qwen3.6 J | `␣trustworthy`, `信任` |
| authorized | 0 / 0 / 1 | 1 | qwen3.6 J | `␣authorized` |
| fabricated / fictional | 0 / 0 / 1 | 1 | qwen3.6 J | `虚构` |
| quietly / unnoticed | 0 / 0 / 1 | 1 | qwen3.6 J | `悄然` |
| fantasy / illusion | 0 / 0 / 1 | 1 | qwen3.6 J | `幻想`, `虚幻`, `错觉` |
| whistleblowing | 0 / 1 / 0 | 1 | qwen3.6 J | `␣whistleblower`, `␣whistlebl`, `␣WikiLeaks` |
| undeniable | 0 / 0 / 1 | 1 | qwen3.6 J | `␣undeniable` |
| censor | 0 / 0 / 1 | 1 | qwen3.6 J | `␣censorship` |
| promotional | 0 / 0 / 1 | 1 | qwen3.6 J | `␣promotional`, `␣promoting`, `宣传` |
| forbid | 0 / 0 / 1 | 1 | qwen3.6 J | `禁止`, `␣prohibited`, `␣Forbidden`, `␣forbidden`, `Forbidden`, `␣prohibit` |
| betrayal | 1 / 0 / 0 | 1 | qwen3.6 J | `␣betrayal` |
| guilty | 0 / 0 / 1 | 1 | qwen3.6 J | `␣guilty` |
| believable | 0 / 0 / 1 | 1 | qwen3.6 J | `␣believable` |
| plagiarize | 0 / 0 / 1 | 1 | qwen3.6 J | `␣plagiar` |
| sincerity | 0 / 1 / 0 | 1 | qwen3.6 J | `␣sincerity` |
| authentic | 0 / 1 / 0 | 1 | qwen3.6 J | `␣authenticity` |
| hidden / secret | 1 / 0 / 0 | 1 | qwen3.6 J | `隐秘` |
| doubt / question | 0 / 0 / 1 | 1 | qwen3.6 J | `质疑` |
| quiet / stealthy | 0 / 0 / 1 | 1 | qwen3.6 J | `悄然` |
| mock (imitation) | 0 / 0 / 1 | 1 | qwen3.6 J | `_mock`, `/mock`, `␣MOCK`, `mock`, `(mock`, `(Mock` |
| illusion / fantasy | 0 / 0 / 1 | 1 | qwen3.6 J | `幻想`, `虚幻`, `错觉`, `妄想` |
| cowardice | 0 / 0 / 1 | 1 | qwen3.6 J | `␣coward` |
| honest / truthful | 0 / 1 / 0 | 1 | qwen3.6 J | `␣truthful`, `␣Honest` |
| fantasy | 0 / 0 / 1 | 1 | qwen3.6 J | `幻想` |
| strict | 0 / 0 / 1 | 1 | qwen3.6 J | `␣STRICT`, `␣Strict`, `严格`, `.strict`, `strict`, `␣strictly`, `Strict`, `严` |
| promote | 0 / 0 / 1 | 1 | qwen3.6 J | `␣promotional`, `␣promoting`, `␣marketing`, `宣传` |
| fault | 0 / 0 / 1 | 1 | qwen3.6 J | `Fault` |
| report | 0 / 0 / 1 | 1 | qwen3.6 J | `举报` |
| typo | 0 / 0 / 1 | 1 | qwen3.6 J | `␣typo` |
| audit | 0 / 0 / 1 | 1 | qwen3.6 J | `Audit`, `␣audit`, `␣auditing`, `审计`, `audit`, `␣audits`, `␣Audit`, `␣auditor` |
| delusion | 0 / 0 / 1 | 1 | qwen3.6 J | `妄想`, `妄` |
| rule-abiding | 0 / 0 / 1 | 1 | qwen3.6 J | `恪守`, `恪`, `依规`, `合规` |
| encryption | 0 / 0 / 1 | 1 | qwen3.6 J | `␣Encryption`, `encryption` |
| fake / forge | 1 / 0 / 0 | 1 | qwen3.6 J | `fake`, `␣fake`, `Fake`, `伪造`, `虚假`, `␣Fake`, `假的`, `弄虚作假` … (+3) |
| fraud / scam | 1 / 0 / 0 | 1 | qwen3.6 J | `␣fraudulent`, `␣fraud`, `欺诈`, `骗局`, `骗取`, `␣scams`, `␣Fraud`, `诈骗` … (+3) |
| repent | 0 / 1 / 0 | 1 | qwen3.6 J | `忏悔`, `悔`, `␣repent`, `后悔` |
| acting | 0 / 0 / 1 | 1 | qwen3.6 J | `␣acted`, `␣acting` |
| caught | 0 / 0 / 1 | 1 | qwen3.6 J | `Caught` |
| mock | 0 / 0 / 1 | 1 | qwen3.6 J | `_mock`, `/mock`, `␣MOCK`, `mock`, `(Mock` |
| resignation | 0 / 0 / 1 | 1 | qwen3.6 J | `无奈` |
| oops | 0 / 0 / 1 | 1 | qwen3.6 J | `Oops` |
| evil | 1 / 0 / 0 | 1 | qwen3.6 J | `␣Evil` |
| report / whistleblow | 0 / 0 / 1 | 1 | qwen3.6 J | `举报` |
| faithful / loyal | 0 / 0 / 1 | 1 | qwen3.6 J | `␣faithful`, `␣faithfully`, `忠`, `忠诚`, `忠实`, `忠于`, `忠心`, `忠诚度` |
| evade / avoid | 1 / 0 / 0 | 1 | qwen3.6 J | `回避`, `␣avoidance`, `␣evasion`, `␣avoiding`, `␣avoided`, `␣Avoid`, `avoid` |
| claim / assert | 0 / 0 / 1 | 1 | qwen3.6 J | `␣claiming`, `声称`, `␣claim`, `␣claims`, `␣assertions`, `␣asserting`, `claim`, `宣称` … (+22) |
| willingly | 0 / 0 / 1 | 1 | qwen3.6 J | `␣voluntarily`, `␣willingly` |
| self-review | 0 / 0 / 1 | 1 | qwen3.6 J | `复盘` |
| violate rules | 0 / 0 / 1 | 1 | qwen3.6 J | `违规`, `違規` |
| absurd | 0 / 0 / 1 | 1 | qwen3.6 J | `荒唐`, `滑稽` |
| cannot say | 0 / 0 / 1 | 1 | qwen3.6 J | `不能说` |
| not guilty | 0 / 1 / 0 | 1 | qwen3.6 J | `无罪` |
| correction | 0 / 0 / 1 | 1 | qwen3.6 J | `更正`, `␣Correction`, `Correction`, `纠错` |
| ignore | 0 / 0 / 1 | 1 | qwen3.6 J | `␣ignoring`, `忽略`, `ignore`, `␣ignores`, `␣IGNORE`, `␣ignore`, `␣ignored`, `Ignore` … (+4) |
| forgiveness | 0 / 0 / 1 | 1 | qwen3.6 J | `␣forgiveness` |
| weigh | 0 / 0 / 1 | 1 | qwen3.6 LL | `权衡` |
| nonconforming | 0 / 0 / 1 | 1 | qwen3.6 LL | `不符合` |
| legal issue | 0 / 0 / 1 | 1 | qwen3.6 LL | `法律问题` |
| without permission | 0 / 0 / 1 | 1 | qwen3.6 LL | `未经允许` |
| not fully | 0 / 0 / 1 | 1 | qwen3.6 LL | `不能完全` |
| not reply | 0 / 0 / 1 | 1 | qwen3.6 LL | `不回` |
| defense | 0 / 0 / 1 | 1 | qwen3.6 LL | `-defense`, `␣defense` |
| lie (japanese) | 1 / 0 / 0 | 1 | qwen3.6 LL | `嘘` |
| code_of_conduct | 0 / 0 / 1 | 1 | qwen3.6 LL | `守则` |
| role_play | 0 / 0 / 1 | 1 | qwen3.6 LL | `扮演`, `角色扮演` |
| correct (fix) | 0 / 1 / 0 | 1 | qwen3.6 LL | `纠正`, `␣corrected`, `␣correction`, `␣correcting`, `␣corrective`, `␣corrections`, `␣Correction`, `Correction` … (+23) |
| role-play / simulate | 0 / 0 / 1 | 1 | qwen3.6 LL | `扮演`, `角色扮演`, `模拟` |
| mask / cover up | 1 / 0 / 0 | 1 | qwen3.6 LL | `␣masking` |
| hesitation | 0 / 0 / 1 | 1 | qwen3.6 LL | `␣hesitation` |
| not aligned | 0 / 0 / 1 | 1 | qwen3.6 LL | `不符合` |
| alignment | 0 / 0 / 1 | 1 | qwen3.6 LL | `align` |
| look back | 0 / 0 / 1 | 1 | qwen3.6 LL | `回顾`, `回顧`, `␣retrospect` |
| not conform | 0 / 0 / 1 | 1 | qwen3.6 LL | `不符合` |
| unfulfilled | 0 / 0 / 1 | 1 | qwen3.6 LL | `未履行` |
| justify / excuse | 0 / 0 / 1 | 1 | qwen3.6 LL | `␣justification`, `␣justified`, `␣excuse` |
| argue / defend | 0 / 0 / 1 | 1 | qwen3.6 LL | `答辩` |
| reject / overrule | 0 / 0 / 1 | 1 | qwen3.6 LL | `否决`, `驳回` |
| private / secret | 1 / 0 / 0 | 1 | qwen3.6 LL | `私下` |
| go against | 0 / 0 / 1 | 1 | qwen3.6 LL | `违背` |
| good_intent | 0 / 0 / 1 | 1 | qwen3.6 LL | `好心` |
| trapped | 0 / 0 / 1 | 1 | qwen3.6 LL | `陷入` |
| flaw | 0 / 0 / 1 | 1 | qwen3.6 LL | `␣flaw` |
| good intention | 0 / 0 / 1 | 1 | qwen3.6 LL | `善意` |
| oversight | 0 / 0 / 1 | 1 | qwen3.6 LL | `疏忽` |
| crime / sin | 0 / 0 / 1 | 1 | qwen3.6 LL | `罪的` |
| turn to good | 0 / 0 / 1 | 1 | qwen3.6 LL | `向善` |
| sincere feeling | 0 / 1 / 0 | 1 | qwen3.6 LL | `真情` |
| seek truth | 0 / 1 / 0 | 1 | qwen3.6 LL | `求真` |
| honest / upright | 0 / 1 / 0 | 1 | qwen3.6 LL | `正直` |
| disclose / public | 0 / 1 / 0 | 1 | qwen3.6 LL | `公开` |
| offended | 0 / 0 / 1 | 1 | qwen3.6 LL | `␣offended` |
| argue / justify | 0 / 0 / 1 | 1 | qwen3.6 LL | `答辩` |
| offend | 0 / 0 / 1 | 1 | qwen3.6 LL | `␣offending` |
| solemn | 0 / 0 / 1 | 1 | qwen3.6 LL | `郑重` |
| despicable | 0 / 0 / 1 | 1 | qwen3.6 LL | `小人` |
| scheme | 0 / 0 / 1 | 1 | qwen3.6 LL | `␣scheme` |
| selfish | 0 / 0 / 1 | 1 | qwen3.6 LL | `自私` |
| discovered | 0 / 0 / 1 | 1 | qwen3.6 LL | `␣discovered` |
| conflicting | 0 / 0 / 1 | 1 | qwen3.6 LL | `␣conflicting` |
| surrender | 0 / 0 / 1 | 1 | qwen3.6 LL | `投降` |
| take responsibility | 0 / 0 / 1 | 1 | qwen3.6 LL | `承担` |
| person of integrity | 0 / 1 / 0 | 1 | qwen3.6 LL | `君子` |
| offend / commit wrongdoing | 0 / 0 / 1 | 1 | qwen3.6 LL | `犯的`, `犯了` |
| true feelings | 0 / 1 / 0 | 1 | qwen3.6 LL | `真情` |
| fairness | 0 / 0 / 1 | 1 | qwen3.6 LL | `公道` |
| retract | 0 / 0 / 1 | 1 | qwen3.6 LL | `撤回` |
| sin / evil | 0 / 0 / 1 | 1 | qwen3.6 LL | `孽` |
| disguised | 1 / 0 / 0 | 1 | qwen3.6 LL | `变相` |
| non-fulfilment | 0 / 0 / 1 | 1 | qwen3.6 LL | `不履行` |
| deceive / hoodwink | 1 / 0 / 0 | 1 | qwen3.6 LL | `哄` |
| direct / head-on | 0 / 0 / 1 | 1 | qwen3.6 LL | `正面` |
| avoid / exempt | 0 / 0 / 1 | 1 | qwen3.6 LL | `免`, `免除` |
| self-respect | 0 / 0 / 1 | 1 | qwen3.6 LL | `自重` |
| righteousness | 0 / 0 / 1 | 1 | qwen3.6 LL | `大义` |
| moral / ethics | 0 / 0 / 1 | 1 | qwen3.6 LL | `␣moral`, `␣ethical`, `␣ethics`, `␣Ethics`, `道德` |
| role-play / persona | 0 / 0 / 1 | 1 | qwen3.6 LL | `扮演`, `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona` |
| refuse / decline | 0 / 0 / 1 | 1 | qwen3.6 LL | `谢绝` |
| truth-seeking | 0 / 1 / 0 | 1 | qwen3.6 LL | `求真` |
| affirm | 0 / 0 / 1 | 1 | qwen3.6 LL | `␣affirm`, `␣afirm`, `␣affirmation`, `␣affirmative`, `␣affirmed`, `␣afirma`, `␣afirmar` |
| uninformed | 0 / 0 / 1 | 1 | qwen3.6 LL | `不知情` |
