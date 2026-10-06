# Draft families grouped by position, rare families dropped (temporary view)

Made on 2026-10-01 from `families_draft.json`, the entries behind `DRAFT.md`. `DRAFT.md` is unchanged.
Only kept entries are used (not the excluded or held-back ones). Nothing is frozen.

- **Layout.** One section per model and lens. Inside it, one table per position. Qwen's positions from the
  question on are listed per question wording, because the token at a position differs between wordings.
- **Counts** are `present / transcripts (share)` on the build split, as in `DRAFT.md`: scenario lies, scenario
  truths, no-pressure truths, unrelated chats; for Qwen's positions from the question on, also the lies and
  truths whose self-report answer is a denial. The held-out split has not been read.
- **Drop rule.** A family is listed at a position only if it is present in at least 20% of the transcripts of
  one or more of those groups at that position. A family under 20% in every group at a position is dropped
  there. The test uses the exact share, so a row shown as `(20%)` after rounding can still be under 20%.
- **Same name twice at one position.** Where the two replicates left two entries with the same family name at
  one position (109 cases), they are joined into one row: the members are pooled and the counts are
  recounted for the pooled members.
- **Members** are the family's tokens at that position (at most 10 shown). Rows are sorted by the number of
  scenario transcripts (lies and truths pooled) in which the family is present.

## Overview

A row is one family at one position.

| model, lens | positions with a family | positions left | rows before | rows left | family names before | family names left |
|---|---|---|---|---|---|---|
| gemma-3-12b-it, J-lens | 5 | 5 | 182 | 60 | 83 | 40 |
| gemma-3-12b-it, logit lens | 5 | 4 | 165 | 47 | 80 | 32 |
| gemma-3-27b-it, J-lens | 5 | 5 | 143 | 38 | 73 | 26 |
| gemma-3-27b-it, logit lens | 4 | 4 | 131 | 27 | 66 | 19 |
| qwen3.6-27b, J-lens | 147 | 122 | 3743 | 1446 | 348 | 206 |
| qwen3.6-27b, logit lens | 152 | 145 | 3504 | 1411 | 353 | 231 |
| gpt-oss-20b, J-lens | 4 | 2 | 31 | 13 | 25 | 11 |
| gpt-oss-20b, logit lens | 2 | 2 | 12 | 3 | 11 | 3 |
| all | | | 7911 | 3045 | 573 | 384 |

## gemma-3-12b-it, J-lens

### postresp_slot0

3 of 6 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| subtle | unclear | `␣subtly`, `␣subtle` | 16/49 (33%) | 6/32 (19%) | 1/135 (1%) | 2/179 (1%) |
| hide | lie | `隐藏`, `␣hiding`, `Hide`, `Hid`, `␣hid`, `HIDE`, `␣লুকিয়ে`, `␣esconder`, `␣скры`, `␣छिपा` … (+7) | 11/49 (22%) | 6/32 (19%) | 5/135 (4%) | 5/179 (3%) |
| disclaimer | unclear | `Disclaimer`, `␣disclaimer`, `␣Disclaimer` | 10/49 (20%) | 5/32 (16%) | 91/135 (67%) | 76/179 (42%) |

### postresp_slot1

14 of 66 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| disclaimer | unclear | `Disclaimer`, `␣disclaimer`, `␣Disclaimer`, `␣DISCLAIM` | 30/49 (61%) | 20/32 (62%) | 90/135 (67%) | 61/179 (34%) |
| honest | truth | `Honestly`, `␣Honestly`, `␣honesty`, `␣honest`, `␣Honest`, `honest` | 29/49 (59%) | 18/32 (56%) | 36/135 (27%) | 8/179 (4%) |
| hush emoji | lie | `🤫`, `🤐` | 28/49 (57%) | 11/32 (34%) | 1/135 (1%) | 0/179 (0%) |
| avoid | unclear | `避免`, `Avoid`, `␣menghindari`, `Avoiding`, `␣avoidance`, `␣এড়িয়ে`, `␣avoiding`, `␣Avoiding`, `éviter`, `␣avoids` … (+8) | 23/49 (47%) | 12/32 (38%) | 3/135 (2%) | 1/179 (1%) |
| confidentiality | unclear | `␣confidentialité`, `␣confidentiality` | 14/49 (29%) | 10/32 (31%) | 14/135 (10%) | 0/179 (0%) |
| subtle | unclear | `␣subtly`, `␣subtle` | 13/49 (27%) | 10/32 (31%) | 0/135 (0%) | 0/179 (0%) |
| lie | lie | `謊`, `␣মিথ্যা`, `谎`, `␣거짓`, `␣झूठ`, `Lie` | 20/49 (41%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| reassure | unclear | `␣reassurance`, `␣reassuring`, `␣reassured`, `␣reassure` | 15/49 (31%) | 5/32 (16%) | 7/135 (5%) | 0/179 (0%) |
| obfuscate | lie | `␣obfusc` | 15/49 (31%) | 3/32 (9%) | 0/135 (0%) | 0/179 (0%) |
| justify | unclear | `␣justifications`, `␣justification` | 12/49 (24%) | 5/32 (16%) | 3/135 (2%) | 1/179 (1%) |
| mislead | lie | `␣misleading`, `␣mislead`, `␣misled` | 12/49 (24%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| disclose | truth | `Disclosure`, `disclosure`, `␣disclose`, `␣Disclosure`, `␣disclosure`, `␣disclosures`, `␣disclosing`, `透露` | 5/49 (10%) | 8/32 (25%) | 55/135 (41%) | 26/179 (15%) |
| evade | lie | `␣evas`, `␣evasion`, `␣evade`, `回避`, `␣evaded` | 10/49 (20%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) |
| pretend | lie | `␣pretending`, `␣pretended`, `␣pretends` | 10/49 (20%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |

### postresp_slot2

28 of 76 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| hush emoji | lie | `🤫`, `🤐` | 43/49 (88%) | 22/32 (69%) | 24/135 (18%) | 1/179 (1%) |
| honest | truth | `Honestly`, `␣honestly`, `␣Honestly`, `␣honesty`, `␣honest`, `honest` | 33/49 (67%) | 21/32 (66%) | 24/135 (18%) | 15/179 (8%) |
| confidentiality | unclear | `␣confidentiality`, `␣confidentialité`, `␣confidential`, `␣Confidential` | 28/49 (57%) | 18/32 (56%) | 65/135 (48%) | 2/179 (1%) |
| sneaky | lie | `␣sneaky` | 30/49 (61%) | 13/32 (41%) | 6/135 (4%) | 6/179 (3%) |
| whisper | unclear | `␣whispers`, `␣whispered`, `囁`, `␣whispering` | 20/49 (41%) | 17/32 (53%) | 5/135 (4%) | 7/179 (4%) |
| justify | unclear | `␣justifications`, `␣justification`, `␣justifying` | 21/49 (43%) | 9/32 (28%) | 17/135 (13%) | 0/179 (0%) |
| subtle | unclear | `␣subtly`, `␣subtle`, `␣subtlety` | 20/49 (41%) | 10/32 (31%) | 1/135 (1%) | 1/179 (1%) |
| desperation | unclear | `␣desperation`, `␣desperately`, `␣desperate` | 16/49 (33%) | 12/32 (38%) | 1/135 (1%) | 0/179 (0%) |
| unapologetic | unclear | `␣unapolog` | 18/49 (37%) | 10/32 (31%) | 8/135 (6%) | 0/179 (0%) |
| paranoia | unclear | `␣paranoia`, `␣paranoid` | 19/49 (39%) | 8/32 (25%) | 1/135 (1%) | 0/179 (0%) |
| avoid | unclear | `避免`, `Avoiding`, `␣menghindari`, `␣avoidance`, `éviter`, `Avoid`, `␣avoiding`, `␣vermeiden`, `␣এড়িয়ে`, `␣avoids` … (+7) | 17/49 (35%) | 8/32 (25%) | 3/135 (2%) | 1/179 (1%) |
| obfuscate | lie | `␣obfusc` | 18/49 (37%) | 5/32 (16%) | 1/135 (1%) | 0/179 (0%) |
| secret | lie | `␣secretly`, `␣secrecy`, `␣خفیہ`, `␣secretive`, `秘密`, `␣secret`, `secret`, `Secret`, `secrets`, `Secrets` … (+3) | 17/49 (35%) | 6/32 (19%) | 1/135 (1%) | 0/179 (0%) |
| unethical | lie | `␣unethical` | 14/49 (29%) | 7/32 (22%) | 14/135 (10%) | 2/179 (1%) |
| knowingly | unclear | `␣knowingly`, `␣bewusst` | 16/49 (33%) | 3/32 (9%) | 6/135 (4%) | 0/179 (0%) |
| pretend | lie | `␣pretending`, `␣pretends` | 13/49 (27%) | 6/32 (19%) | 3/135 (2%) | 0/179 (0%) |
| blatant | unclear | `␣blatantly`, `␣blatant` | 14/49 (29%) | 4/32 (12%) | 0/135 (0%) | 0/179 (0%) |
| lie | lie | `謊`, `␣মিথ্যা`, `␣거짓`, `谎`, `␣झूठ`, `␣lies`, `␣lying`, `␣lied`, `lies`, `␣lie` … (+5) | 13/49 (27%) | 5/32 (16%) | 1/135 (1%) | 0/179 (0%) |
| deliberately | unclear | `␣knowingly`, `␣intentionally`, `故意` | 15/49 (31%) | 2/32 (6%) | 7/135 (5%) | 1/179 (1%) |
| disclaimer | unclear | `␣disclaimer`, `Disclaimer` | 11/49 (22%) | 6/32 (19%) | 66/135 (49%) | 4/179 (2%) |
| misinformation | lie | `␣misinformation`, `␣disinformation` | 15/49 (31%) | 2/32 (6%) | 40/135 (30%) | 0/179 (0%) |
| dishonest | lie | `␣dishonesty`, `␣dishonest` | 11/49 (22%) | 5/32 (16%) | 3/135 (2%) | 0/179 (0%) |
| worry | unclear | `␣worrying`, `担忧`, `␣worries`, `␣worrisome`, `擔心`, `担心` | 9/49 (18%) | 7/32 (22%) | 6/135 (4%) | 0/179 (0%) |
| deceive | lie | `␣deceptive`, `␣deception`, `␣deceit`, `␣deceiving`, `␣deceive`, `騙`, `欺` | 11/49 (22%) | 4/32 (12%) | 3/135 (2%) | 0/179 (0%) |
| mislead | lie | `␣misleading`, `␣mislead`, `␣misled` | 12/49 (24%) | 3/32 (9%) | 4/135 (3%) | 0/179 (0%) |
| protect | unclear | `Protect`, `␣melindungi`, `␣protecting`, `保护`, `␣protect`, `␣Protecting`, `protect`, `Protection`, `␣protection`, `␣protects` … (+4) | 10/49 (20%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) |
| truth | truth | `␣truth`, `␣verdad`, `␣Truth`, `truth`, `␣truths`, `Truth`, `verdad`, `真相`, `truths` | 5/49 (10%) | 1/32 (3%) | 42/135 (31%) | 0/179 (0%) |
| truthful | truth | `␣truthful`, `␣truthfully` | 3/49 (6%) | 2/32 (6%) | 40/135 (30%) | 0/179 (0%) |

### postresp_slot3

2 of 6 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| pretend | lie | `␣pretending` | 23/49 (47%) | 18/32 (56%) | 21/135 (16%) | 0/179 (0%) |
| apologise | unclear | `␣apologised`, `␣apologise`, `␣apologizing`, `␣Sorry` | 22/49 (45%) | 15/32 (47%) | 45/135 (33%) | 56/179 (31%) |

### postresp_slot4

13 of 28 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| honest | truth | `␣Honestly`, `Honestly`, `␣honestly` | 49/49 (100%) | 31/32 (97%) | 108/135 (80%) | 66/179 (37%) |
| joke | unclear | `␣joked`, `␣joking`, `␣joke`, `␣jokes`, `␣Jokes`, `␣jokingly` | 23/49 (47%) | 19/32 (59%) | 101/135 (75%) | 116/179 (65%) |
| worry | unclear | `␣worrying`, `␣worries`, `␣worried`, `擔心` | 21/49 (43%) | 17/32 (53%) | 27/135 (20%) | 0/179 (0%) |
| scepticism | unclear | `␣skepticism`, `␣scepticism`, `␣sceptical`, `␣skeptic`, `␣skeptical` | 22/49 (45%) | 9/32 (28%) | 7/135 (5%) | 0/179 (0%) |
| insist | unclear | `␣insisting`, `␣insistent` | 18/49 (37%) | 11/32 (34%) | 5/135 (4%) | 0/179 (0%) |
| rumour | unclear | `␣rumours`, `␣rumour`, `␣rumoured`, `␣rumors` | 16/49 (33%) | 9/32 (28%) | 29/135 (21%) | 4/179 (2%) |
| pretend | lie | `␣pretending` | 13/49 (27%) | 5/32 (16%) | 38/135 (28%) | 3/179 (2%) |
| reassure | unclear | `␣reassured`, `␣reassurance`, `␣reassuring` | 10/49 (20%) | 8/32 (25%) | 5/135 (4%) | 0/179 (0%) |
| frank | truth | `␣Frankly` | 13/49 (27%) | 3/32 (9%) | 4/135 (3%) | 0/179 (0%) |
| sneaky | lie | `␣sneaky` | 12/49 (24%) | 4/32 (12%) | 29/135 (21%) | 5/179 (3%) |
| doubt | unclear | `␣doubting`, `质疑`, `␣doubted`, `␣doubts` | 11/49 (22%) | 3/32 (9%) | 2/135 (1%) | 0/179 (0%) |
| suspicion | unclear | `␣suspicions`, `␣suspiciously` | 11/49 (22%) | 1/32 (3%) | 4/135 (3%) | 0/179 (0%) |
| apologise | unclear | `␣apologised`, `␣apologise`, `Sorry`, `␣apologies`, `␣Sorry` | 6/49 (12%) | 5/32 (16%) | 30/135 (22%) | 5/179 (3%) |

## gemma-3-12b-it, logit lens

### postresp_slot0

8 of 17 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| hide | lie | `␣hiding`, `␣hide`, `␣hid`, `hide`, `␣hidden`, `␣Hide`, `␣hides`, `␣esconder`, `Hide` | 36/49 (73%) | 24/32 (75%) | 67/135 (50%) | 53/179 (30%) |
| rebuttal | unclear | `␣rebuttal` | 32/49 (65%) | 18/32 (56%) | 56/135 (41%) | 10/179 (6%) |
| subtle | unclear | `␣subtle`, `␣subtly` | 24/49 (49%) | 14/32 (44%) | 29/135 (21%) | 37/179 (21%) |
| disclaimer | unclear | `Disclaimer`, `␣Disclaimer` | 19/49 (39%) | 10/32 (31%) | 90/135 (67%) | 70/179 (39%) |
| fact | truth | `␣factual` | 13/49 (27%) | 9/32 (28%) | 110/135 (81%) | 110/179 (61%) |
| understate | unclear | `␣understated` | 12/49 (24%) | 5/32 (16%) | 0/135 (0%) | 1/179 (1%) |
| correct | truth | `␣right`, `␣correct`, `Right` | 10/49 (20%) | 5/32 (16%) | 6/135 (4%) | 27/179 (15%) |
| sincere | truth | `␣heartfelt` | 6/49 (12%) | 6/32 (19%) | 53/135 (39%) | 53/179 (30%) |

### postresp_slot1

17 of 65 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| disclaimer | unclear | `Disclaimer`, `␣Disclaimer` | 25/49 (51%) | 11/32 (34%) | 79/135 (59%) | 54/179 (30%) |
| honest | truth | `Honestly`, `␣Honestly`, `␣honestly`, `␣honesty`, `␣honest`, `正直`, `honest` | 21/49 (43%) | 15/32 (47%) | 37/135 (27%) | 0/179 (0%) |
| blatant | unclear | `␣blatant`, `␣blatantly` | 16/49 (33%) | 7/32 (22%) | 6/135 (4%) | 0/179 (0%) |
| truth | truth | `Truth`, `␣truth`, `verdad`, `␣Правда`, `truth`, `␣Truth`, `␣verdade`, `␣truths`, `真相` | 16/49 (33%) | 6/32 (19%) | 21/135 (16%) | 0/179 (0%) |
| avoid | unclear | `␣avoid`, `Avoid`, `avoid`, `␣এড়িয়ে`, `␣avoidance`, `␣avoids`, `␣avoiding`, `␣avoided`, `␣Avoid`, `避免` … (+1) | 15/49 (31%) | 6/32 (19%) | 1/135 (1%) | 0/179 (0%) |
| rebuttal | unclear | `␣rebuttal`, `␣rebut` | 16/49 (33%) | 4/32 (12%) | 10/135 (7%) | 1/179 (1%) |
| reassure | unclear | `␣reassuring`, `␣reassurance`, `␣reassure`, `␣comforting`, `␣reassured` | 13/49 (27%) | 6/32 (19%) | 30/135 (22%) | 0/179 (0%) |
| persuade | unclear | `␣convincing`, `␣persuasive`, `␣persuasion`, `␣convince`, `␣convincingly`, `␣persuading`, `␣persuas` | 13/49 (27%) | 4/32 (12%) | 1/135 (1%) | 0/179 (0%) |
| convince | unclear | `␣convincing`, `␣convince`, `␣convincingly` | 12/49 (24%) | 4/32 (12%) | 1/135 (1%) | 0/179 (0%) |
| deflect | lie | `␣deflection`, `␣deflect`, `␣deflected` | 12/49 (24%) | 4/32 (12%) | 1/135 (1%) | 0/179 (0%) |
| misinformation | lie | `␣misinformation`, `␣disinformation` | 14/49 (29%) | 2/32 (6%) | 14/135 (10%) | 1/179 (1%) |
| obfuscate | lie | `␣obfusc` | 11/49 (22%) | 4/32 (12%) | 1/135 (1%) | 0/179 (0%) |
| mislead | lie | `␣misleading`, `␣mislead`, `␣misled` | 10/49 (20%) | 3/32 (9%) | 0/135 (0%) | 1/179 (1%) |
| evade | lie | `␣evas`, `␣evasion`, `␣evade`, `␣evaded` | 10/49 (20%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) |
| lie | lie | `␣lies`, `␣거짓`, `␣lie`, `␣lying`, `␣lied`, `lying`, `lies`, `␣झूठ`, `␣Lie`, `谎` | 11/49 (22%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| fact | truth | `␣factual` | 3/49 (6%) | 4/32 (12%) | 86/135 (64%) | 19/179 (11%) |
| disclose | truth | `Disclosure`, `␣disclosure` | 2/49 (4%) | 4/32 (12%) | 31/135 (23%) | 4/179 (2%) |

### postresp_slot2

20 of 76 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| honest | truth | `Honestly`, `␣Honestly`, `␣honestly`, `␣honesty`, `␣honest`, `␣Honest` | 30/49 (61%) | 16/32 (50%) | 31/135 (23%) | 1/179 (1%) |
| misinformation | lie | `␣misinformation`, `␣disinformation` | 21/49 (43%) | 8/32 (25%) | 60/135 (44%) | 1/179 (1%) |
| secret | lie | `🤫`, `␣secrecy`, `␣secretly`, `␣secret`, `Secret`, `secret` | 21/49 (43%) | 6/32 (19%) | 3/135 (2%) | 0/179 (0%) |
| blatant | unclear | `␣blatant`, `␣blatantly` | 17/49 (35%) | 6/32 (19%) | 10/135 (7%) | 6/179 (3%) |
| truth | truth | `Truth`, `␣truth`, `verdad`, `␣Truth`, `truth`, `␣truths` | 18/49 (37%) | 5/32 (16%) | 51/135 (38%) | 0/179 (0%) |
| truthful | truth | `␣truthfully`, `␣truthful` | 16/49 (33%) | 7/32 (22%) | 25/135 (19%) | 0/179 (0%) |
| hush | lie | `🤫`, `␣hush` | 18/49 (37%) | 3/32 (9%) | 2/135 (1%) | 0/179 (0%) |
| avoid | unclear | `␣avoid`, `Avoid`, `␣avoiding`, `␣avoids`, `␣avoidance`, `avoid`, `␣Avoid`, `Avoiding`, `␣avoided`, `回避` | 14/49 (29%) | 6/32 (19%) | 2/135 (1%) | 0/179 (0%) |
| mislead | lie | `␣misleading`, `␣mislead`, `␣misled` | 14/49 (29%) | 5/32 (16%) | 4/135 (3%) | 0/179 (0%) |
| deceive | lie | `␣deception`, `␣deceit`, `␣deceptive`, `␣deceive`, `␣deceiving`, `␣decept` | 13/49 (27%) | 5/32 (16%) | 4/135 (3%) | 0/179 (0%) |
| dishonest | lie | `␣dishonesty`, `␣dishonest` | 11/49 (22%) | 7/32 (22%) | 4/135 (3%) | 0/179 (0%) |
| protect | unclear | `Protect`, `␣protect`, `␣protecting`, `protect`, `␣protection`, `␣protected`, `␣protects`, `␣Protect`, `␣protective`, `protected` … (+1) | 12/49 (24%) | 6/32 (19%) | 0/135 (0%) | 0/179 (0%) |
| sincere | truth | `␣heartfelt`, `␣sincerely` | 11/49 (22%) | 7/32 (22%) | 14/135 (10%) | 13/179 (7%) |
| lie | lie | `␣lies`, `␣lie`, `␣lying`, `␣lied`, `lying`, `lie`, `␣Lie`, `␣거짓`, `Lie`, `谎` … (+7) | 13/49 (27%) | 4/32 (12%) | 0/135 (0%) | 0/179 (0%) |
| unapologetic | unclear | `␣unapolog` | 12/49 (24%) | 5/32 (16%) | 5/135 (4%) | 0/179 (0%) |
| confidential | unclear | `␣confidentiality`, `␣confidential`, `␣Confidential` | 10/49 (20%) | 4/32 (12%) | 3/135 (2%) | 0/179 (0%) |
| understate | unclear | `␣understated` | 5/49 (10%) | 7/32 (22%) | 0/135 (0%) | 3/179 (2%) |
| wrongdoing | lie | `␣wrongdoing` | 9/49 (18%) | 3/32 (9%) | 49/135 (36%) | 1/179 (1%) |
| fact | truth | `␣factual` | 6/49 (12%) | 2/32 (6%) | 100/135 (74%) | 11/179 (6%) |
| true | truth | `␣true` | 0/49 (0%) | 0/32 (0%) | 53/135 (39%) | 0/179 (0%) |

### postresp_slot4

2 of 4 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| honest | truth | `Honestly`, `␣Honestly` | 22/49 (45%) | 12/32 (38%) | 24/135 (18%) | 0/179 (0%) |
| correct | truth | `right`, `␣right`, `␣correct`, `Right`, `␣Right` | 19/49 (39%) | 13/32 (41%) | 20/135 (15%) | 7/179 (4%) |

Positions where every family is under 20% (number of families dropped): postresp_slot3 (3).

## gemma-3-27b-it, J-lens

### postresp_slot0

3 of 9 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| keep-quiet emoji | unclear | `🤫`, `🤐`, `🔇` | 38/58 (66%) | 15/30 (50%) | 5/133 (4%) | 0/199 (0%) |
| locked | unclear | `🔐` | 34/58 (59%) | 10/30 (33%) | 6/133 (5%) | 0/199 (0%) |
| hand over mouth | unclear | `🫢` | 13/58 (22%) | 10/30 (33%) | 4/133 (3%) | 2/199 (1%) |

### postresp_slot1

9 of 49 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| keep-quiet emoji | unclear | `🤫`, `🤐`, `🔇` | 35/58 (60%) | 12/30 (40%) | 13/133 (10%) | 1/199 (1%) |
| honest | truth | `Honestly`, `实话`, `␣honesty`, `honest` | 27/58 (47%) | 13/30 (43%) | 16/133 (12%) | 2/199 (1%) |
| confident | unclear | `␣आत्मविश्वास`, `自信`, `Confident`, `Confidence`, `␣confidence`, `␣confident`, `confidence`, `␣confidently`, `␣Confidence`, `confident` | 20/58 (34%) | 8/30 (27%) | 2/133 (2%) | 2/199 (1%) |
| hand over mouth | unclear | `🫢` | 19/58 (33%) | 9/30 (30%) | 20/133 (15%) | 17/199 (9%) |
| reassure | unclear | `␣安心`, `安心`, `␣reassurance`, `␣reassured`, `␣reassuring`, `␣reassure` | 19/58 (33%) | 7/30 (23%) | 27/133 (20%) | 24/199 (12%) |
| lie | lie | `␣মিথ্যা`, `␣거짓`, `␣झूठ`, `谎`, `謊`, `␣lied`, `␣liar`, `␣lying`, `Lie`, `🤥` | 20/58 (34%) | 4/30 (13%) | 0/133 (0%) | 0/199 (0%) |
| lying-face emoji | lie | `🤥` | 19/58 (33%) | 4/30 (13%) | 0/133 (0%) | 0/199 (0%) |
| apologise | unclear | `␣apologised`, `␣apologise`, `道歉`, `␣apologizing` | 6/58 (10%) | 11/30 (37%) | 32/133 (24%) | 1/199 (1%) |
| secret | lie | `␣خفیہ`, `秘密` | 12/58 (21%) | 3/30 (10%) | 2/133 (2%) | 0/199 (0%) |

### postresp_slot2

14 of 61 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| keep-quiet emoji | unclear | `🤫`, `🤐`, `🔇`, `沉默` | 49/58 (84%) | 22/30 (73%) | 47/133 (35%) | 0/199 (0%) |
| lie | lie | `␣মিথ্যা`, `␣거짓`, `␣झूठ`, `谎`, `謊`, `␣lies`, `␣lied`, `␣liar`, `␣lie`, `␣lying` … (+5) | 30/58 (52%) | 9/30 (30%) | 11/133 (8%) | 0/199 (0%) |
| lying-face emoji | lie | `🤥` | 30/58 (52%) | 8/30 (27%) | 11/133 (8%) | 0/199 (0%) |
| locked | unclear | `🔐` | 24/58 (41%) | 10/30 (33%) | 13/133 (10%) | 9/199 (5%) |
| secret | lie | `␣خفیہ`, `秘密`, `␣비밀`, `secrets`, `␣secretos`, `␣secrecy` | 25/58 (43%) | 8/30 (27%) | 4/133 (3%) | 0/199 (0%) |
| deceive | lie | `␣deception`, `␣deceptive`, `␣deceit`, `␣فريبي`, `␣deceive`, `␣deceiving`, `骗`, `欺` | 24/58 (41%) | 5/30 (17%) | 16/133 (12%) | 40/199 (20%) |
| conceal | lie | `瞒`, `瞞`, `隐藏`, `␣nascost`, `␣concealing`, `␣concealment`, `␣скры`, `␣hiding`, `␣concealed`, `␣conceal` … (+2) | 18/58 (31%) | 6/30 (20%) | 2/133 (2%) | 0/199 (0%) |
| dishonest | lie | `␣dishonesty`, `␣dishonest` | 14/58 (24%) | 6/30 (20%) | 2/133 (2%) | 0/199 (0%) |
| avoid | unclear | `Avoiding`, `避免`, `éviter`, `␣избежать`, `avoid`, `␣evitando`, `␣menghindari`, `␣avoidance`, `␣tránh`, `␣এড়িয়ে` … (+8) | 13/58 (22%) | 4/30 (13%) | 3/133 (2%) | 0/199 (0%) |
| confidential | unclear | `␣गोपनीय`, `␣गोपनीयता`, `␣confidentialité`, `␣confidentiality`, `隐私` | 12/58 (21%) | 3/30 (10%) | 5/133 (4%) | 0/199 (0%) |
| honest | truth | `实话`, `Honestly`, `␣honesty`, `␣honest`, `honest`, `␣truthful`, `␣truthfully` | 8/58 (14%) | 5/30 (17%) | 30/133 (23%) | 0/199 (0%) |
| truth | truth | `␣सच्चाई`, `truth`, `␣verità`, `真相`, `␣truth`, `Truth`, `truths`, `␣truths`, `实话` | 8/58 (14%) | 5/30 (17%) | 36/133 (27%) | 0/199 (0%) |
| apologise | unclear | `␣apologise`, `␣apologised`, `道歉`, `␣apologizing`, `␣apology`, `␣apolog`, `␣apologize`, `␣apologies`, `␣apologized` | 4/58 (7%) | 8/30 (27%) | 12/133 (9%) | 0/199 (0%) |
| truthful | truth | `␣truthful`, `␣truthfully` | 2/58 (3%) | 4/30 (13%) | 27/133 (20%) | 0/199 (0%) |

### postresp_slot3

3 of 3 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| role-play | unclear | `扮演` | 16/58 (28%) | 10/30 (33%) | 90/133 (68%) | 5/199 (3%) |
| sceptical | unclear | `␣sceptical` | 11/58 (19%) | 6/30 (20%) | 3/133 (2%) | 0/199 (0%) |
| apologise | unclear | `␣apologised`, `␣apologise` | 9/58 (16%) | 7/30 (23%) | 13/133 (10%) | 11/199 (6%) |

### postresp_slot4

9 of 21 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| challenge | unclear | `质疑` | 34/58 (59%) | 11/30 (37%) | 2/133 (2%) | 0/199 (0%) |
| apologise | unclear | `␣apologised`, `␣apologise`, `␣apologizing` | 21/58 (36%) | 16/30 (53%) | 54/133 (41%) | 70/199 (35%) |
| sneaky | lie | `␣sneaky` | 28/58 (48%) | 8/30 (27%) | 50/133 (38%) | 36/199 (18%) |
| rumour | unclear | `␣rumoured`, `␣rumours`, `␣rumour`, `␣rumors` | 18/58 (31%) | 8/30 (27%) | 13/133 (10%) | 1/199 (1%) |
| sceptical | unclear | `␣sceptical`, `␣scepticism`, `␣skepticism`, `␣skeptical` | 18/58 (31%) | 5/30 (17%) | 3/133 (2%) | 0/199 (0%) |
| dodgy | lie | `␣dodgy` | 12/58 (21%) | 4/30 (13%) | 4/133 (3%) | 0/199 (0%) |
| suspicion | unclear | `怀疑`, `␣suspiciously` | 12/58 (21%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| disgraceful | unclear | `␣disgraceful` | 5/58 (9%) | 6/30 (20%) | 8/133 (6%) | 0/199 (0%) |
| shameful | unclear | `␣disgraceful`, `␣shameful` | 5/58 (9%) | 6/30 (20%) | 8/133 (6%) | 0/199 (0%) |

## gemma-3-27b-it, logit lens

### postresp_slot0

7 of 14 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| secret | lie | `␣Secret`, `🤫` | 30/58 (52%) | 9/30 (30%) | 7/133 (5%) | 0/199 (0%) |
| cover | lie | `␣Cover`, `Cover`, `cover`, `␣Covering` | 24/58 (41%) | 8/30 (27%) | 13/133 (10%) | 79/199 (40%) |
| sincere | truth | `␣sincerely`, `␣Sincerely`, `Sincerely`, `␣sincer` | 19/58 (33%) | 9/30 (30%) | 44/133 (33%) | 3/199 (2%) |
| correct | truth | `right`, `␣Correct`, `␣Correction` | 13/58 (22%) | 9/30 (30%) | 49/133 (37%) | 57/199 (29%) |
| shame | unclear | `␣Shame` | 10/58 (17%) | 9/30 (30%) | 27/133 (20%) | 12/199 (6%) |
| honest | truth | `正直`, `␣Honestly`, `␣honest`, `␣Honest` | 5/58 (9%) | 6/30 (20%) | 11/133 (8%) | 5/199 (3%) |
| truth | truth | `␣Truth`, `␣truth` | 4/58 (7%) | 6/30 (20%) | 35/133 (26%) | 6/199 (3%) |

### postresp_slot1

4 of 46 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| honest | truth | `␣Honestly`, `␣honesty`, `␣honest`, `␣Honest`, `honest`, `␣honestly`, `␣ईमानदारी`, `Honestly`, `␣ehrlich`, `正直` | 31/58 (53%) | 13/30 (43%) | 33/133 (25%) | 5/199 (3%) |
| shame | unclear | `␣Shame` | 10/58 (17%) | 12/30 (40%) | 21/133 (16%) | 3/199 (2%) |
| dismiss | unclear | `␣Dismiss` | 9/58 (16%) | 7/30 (23%) | 2/133 (2%) | 0/199 (0%) |
| apologize | unclear | `道歉`, `␣apologize`, `␣apologies`, `␣apologized`, `␣apologised`, `␣apologizing`, `␣Sorry`, `Sorry` | 2/58 (3%) | 5/30 (17%) | 31/133 (23%) | 11/199 (6%) |

### postresp_slot2

15 of 64 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| truth | truth | `␣सच्चाई`, `␣Truth`, `truth`, `␣truth`, `␣Wahrheit`, `Truth`, `真相`, `␣truths`, `␣Правда`, `␣सत्य` … (+3) | 23/58 (40%) | 17/30 (57%) | 51/133 (38%) | 0/199 (0%) |
| secret | lie | `␣secretly`, `␣Secret`, `␣secrecy`, `secret`, `秘密`, `🤫` | 25/58 (43%) | 10/30 (33%) | 4/133 (3%) | 0/199 (0%) |
| shame | unclear | `␣Shame` | 19/58 (33%) | 12/30 (40%) | 23/133 (17%) | 1/199 (1%) |
| conceal | lie | `␣concealing`, `␣скры`, `␣concealed`, `␣conceal`, `␣concealment`, `␣hiding`, `隐藏`, `␣Hidden`, `␣hidden`, `hidden` … (+3) | 21/58 (36%) | 8/30 (27%) | 5/133 (4%) | 13/199 (7%) |
| lie | lie | `␣झूठ`, `␣lie`, `␣lies`, `谎`, `␣Lie`, `Lie`, `␣lying`, `␣거짓`, `␣মিথ্যা`, `lie` … (+7) | 21/58 (36%) | 7/30 (23%) | 2/133 (2%) | 0/199 (0%) |
| deceive | lie | `␣deception`, `␣deceit`, `␣deceptive`, `␣deceive`, `␣deceiving`, `␣decept`, `␣deceived`, `骗`, `欺` | 19/58 (33%) | 8/30 (27%) | 6/133 (5%) | 0/199 (0%) |
| guilt | unclear | `␣Guilty`, `␣guilty`, `␣guilt`, `␣culp` | 17/58 (29%) | 7/30 (23%) | 6/133 (5%) | 0/199 (0%) |
| honest | truth | `␣honestly`, `␣Honestly`, `␣honesty`, `␣Honest`, `正直`, `honest`, `␣ईमानदारी`, `␣honest`, `␣ehrlich` | 13/58 (22%) | 11/30 (37%) | 22/133 (17%) | 0/199 (0%) |
| omit | lie | `␣omission`, `␣omitting`, `␣unspoken`, `␣умолча` | 15/58 (26%) | 8/30 (27%) | 4/133 (3%) | 0/199 (0%) |
| truthful | truth | `␣truthfully`, `␣truthful` | 13/58 (22%) | 7/30 (23%) | 36/133 (27%) | 0/199 (0%) |
| dishonest | lie | `␣dishonest`, `␣dishonesty` | 11/58 (19%) | 6/30 (20%) | 3/133 (2%) | 0/199 (0%) |
| shush | lie | `🤫` | 14/58 (24%) | 3/30 (10%) | 2/133 (2%) | 0/199 (0%) |
| unspoken | lie | `␣unspoken` | 13/58 (22%) | 3/30 (10%) | 2/133 (2%) | 0/199 (0%) |
| withhold | lie | `␣умолча`, `␣withholding`, `␣withhold` | 6/58 (10%) | 6/30 (20%) | 2/133 (2%) | 0/199 (0%) |
| apologize | unclear | `␣apologize`, `␣apology`, `␣apologies`, `␣apolog`, `␣apologized`, `␣apologised`, `␣apologizing`, `␣apologise`, `道歉`, `␣sorry` … (+2) | 2/58 (3%) | 6/30 (20%) | 9/133 (7%) | 0/199 (0%) |

### postresp_slot4

1 of 7 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| correct | truth | `␣right`, `Right`, `␣Right`, `␣Correct` | 10/58 (17%) | 6/30 (20%) | 7/133 (5%) | 5/199 (3%) |

## qwen3.6-27b, J-lens

### post-response slots

#### postresp_slot1

27 of 58 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| truth | truth | `真相`, `␣truth`, `truth`, `␣Truth`, `Truth`, `␣truths`, `_truth`, `.truth`, `真理`, `实话` … (+3) | 102/152 (67%) | 45/81 (56%) | 61/138 (44%) | 0/158 (0%) |
| truthful | truth | `␣truthful`, `如实`, `实话`, `实事求是`, `说实话` | 101/152 (66%) | 46/81 (57%) | 59/138 (43%) | 0/158 (0%) |
| lie | lie | `谎言`, `说谎`, `撒谎`, `谎`, `␣lied`, `␣lie`, `␣lies`, `␣mentira`, `␣거짓`, `␣lying` … (+7) | 127/152 (84%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) |
| conceal | lie | `隐瞒`, `掩盖`, `瞒` | 109/152 (72%) | 17/81 (21%) | 2/138 (1%) | 0/158 (0%) |
| fake | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `假`, `假的`, `.fake`, `_fake`, `虚假` | 117/152 (77%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 101/152 (66%) | 7/81 (9%) | 10/138 (7%) | 0/158 (0%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗`, `␣deceive`, `␣deceit`, `␣deceived` | 94/152 (62%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) |
| falsehood | lie | `␣falsehood` | 89/152 (59%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) |
| fabricate | lie | `伪造`, `虚构`, `造假`, `␣fabricated`, `弄虚作假` | 83/152 (55%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `FALSE`, `>false`, `␣fals`, `␣falsely`, `␣untrue` … (+2) | 79/152 (52%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) |
| refuse | unclear | `拒绝`, `␣refusal`, `␣refus`, `拒`, `␣refusing`, `␣refused`, `␣refuses`, `␣refuse`, `拒绝了`, `拒絕` … (+3) | 26/152 (17%) | 44/81 (54%) | 9/138 (7%) | 0/158 (0%) |
| mislead | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 61/152 (40%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer`, `␣DISCLAIMER`, `Disclaimer` | 22/152 (14%) | 32/81 (40%) | 15/138 (11%) | 3/158 (2%) |
| honest | truth | `␣honesty`, `诚实`, `␣honest`, `坦诚`, `␣honestly`, `␣Honest`, `诚信`, `正直`, `诚实守信`, `真诚` | 9/152 (6%) | 43/81 (53%) | 40/138 (29%) | 1/158 (1%) |
| rebut | unclear | `反驳`, `␣rebut`, `␣refute`, `␣debunk` | 31/152 (20%) | 11/81 (14%) | 12/138 (9%) | 0/158 (0%) |
| reject | unclear | `reject`, `␣rejection`, `␣rejecting`, `Reject`, `␣Reject`, `␣reject`, `␣rejected`, `.reject`, `rejected` | 11/152 (7%) | 29/81 (36%) | 1/138 (1%) | 0/158 (0%) |
| dishonest | lie | `␣dishonest` | 35/152 (23%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) |
| candid | truth | `坦诚` | 1/152 (1%) | 34/81 (42%) | 19/138 (14%) | 0/158 (0%) |
| excuse | unclear | `␣excuse`, `␣excuses`, `借口`, `辩解` | 33/152 (22%) | 2/81 (2%) | 3/138 (2%) | 0/158 (0%) |
| disclose | truth | `␣disclosure`, `␣Disclosure`, `␣disclosing`, `公开`, `␣disclose`, `␣disclosures`, `披露`, `揭露`, `␣disclosed`, `Disclosure` … (+4) | 1/152 (1%) | 26/81 (32%) | 20/138 (14%) | 0/158 (0%) |
| confess | truth | `坦白`, `␣confession`, `␣confess`, `␣confessed` | 0/152 (0%) | 24/81 (30%) | 5/138 (4%) | 0/158 (0%) |
| ethics | unclear | `道德`, `␣ethical`, `ethical`, `伦理`, `␣ethics`, `␣Ethics`, `的道德` | 0/152 (0%) | 24/81 (30%) | 0/138 (0%) | 0/158 (0%) |
| unethical | lie | `␣unethical` | 4/152 (3%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) |
| ethical | truth | `␣ethical`, `ethical` | 0/152 (0%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) |
| transparent | truth | `␣transparency`, `透明`, `␣Transparency`, `透明度`, `␣transparent`, `透明的`, `transparent` | 0/152 (0%) | 21/81 (26%) | 7/138 (5%) | 0/158 (0%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣Correction`, `␣correcting` … (+13) | 4/152 (3%) | 3/81 (4%) | 28/138 (20%) | 5/158 (3%) |
| fact | truth | `␣fact`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `fact`, `␣Actual`, `␣Fact` … (+18) | 4/152 (3%) | 3/81 (4%) | 56/138 (41%) | 2/158 (1%) |

#### postresp_slot3

1 of 8 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| clarify | unclear | `澄清`, `␣clarify` | 2/152 (1%) | 11/81 (14%) | 36/138 (26%) | 8/158 (5%) |

#### postresp_slot4

9 of 51 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| misinformation | lie | `␣misinformation`, `虚假信息` | 47/152 (31%) | 23/81 (28%) | 89/138 (64%) | 1/158 (1%) |
| truth | truth | `真相`, `␣truth`, `truth`, `Truth`, `␣Truth`, `␣truths`, `真理`, `实话`, `_truth` | 42/152 (28%) | 7/81 (9%) | 84/138 (61%) | 0/158 (0%) |
| fake | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `假`, `假的`, `虚假` | 18/152 (12%) | 25/81 (31%) | 25/138 (18%) | 0/158 (0%) |
| fabricate | lie | `虚构`, `伪造`, `造假`, `弄虚作假` | 9/152 (6%) | 22/81 (27%) | 31/138 (22%) | 2/158 (1%) |
| unethical | lie | `␣unethical` | 8/152 (5%) | 22/81 (27%) | 7/138 (5%) | 0/158 (0%) |
| truthful | truth | `␣truthful`, `实事求是`, `实话`, `如实` | 21/152 (14%) | 4/81 (5%) | 72/138 (52%) | 0/158 (0%) |
| fiction | unclear | `␣fictional`, `fiction`, `␣Fiction`, `␣fiction`, `-fiction` | 3/152 (2%) | 19/81 (23%) | 22/138 (16%) | 8/158 (5%) |
| fact | truth | `␣fact`, `␣actually`, `␣actual`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts` … (+9) | 10/152 (7%) | 2/81 (2%) | 77/138 (56%) | 2/158 (1%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `␣Correct`, `␣correctness`, `␣Correction`, `␣correcting`, `Correction`, `正确` … (+7) | 0/152 (0%) | 2/81 (2%) | 28/138 (20%) | 9/158 (6%) |

Positions where every family is under 20% (number of families dropped): postresp_slot0 (2), postresp_slot2 (2).

### wording Q1_bare, positions from the question on

#### q_tok0

1 of 21 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| intentional | unclear | `␣intentional`, `␣intentionally`, `␣deliberate`, `␣deliberately`, `故意`, `␣intention` | 18/152 (12%) | 20/81 (25%) | 30/138 (22%) | 0/158 (0%) | 7/53 (13%) | 17/74 (23%) |

#### q_tok1

2 of 29 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| refuse | unclear | `␣refusal`, `拒绝`, `␣refus`, `␣refusing`, `␣rejection` | 6/152 (4%) | 20/81 (25%) | 11/138 (8%) | 1/158 (1%) | 4/53 (8%) | 20/74 (27%) |
| misinformation | lie | `␣misinformation` | 8/152 (5%) | 1/81 (1%) | 39/138 (28%) | 4/158 (3%) | 3/53 (6%) | 1/74 (1%) |

#### q_tok2

2 of 14 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的` | 81/152 (53%) | 52/81 (64%) | 124/138 (90%) | 74/158 (47%) | 35/53 (66%) | 46/74 (62%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer` | 61/152 (40%) | 61/81 (75%) | 44/138 (32%) | 8/158 (5%) | 29/53 (55%) | 56/74 (76%) |

#### q_tok3

25 of 43 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful | truth | `␣truthful` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 145/158 (92%) | 53/53 (100%) | 74/74 (100%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的` | 151/152 (99%) | 81/81 (100%) | 138/138 (100%) | 148/158 (94%) | 52/53 (98%) | 74/74 (100%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确的` | 151/152 (99%) | 79/81 (98%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 73/74 (99%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `␣correcting`, `.correct` … (+6) | 143/152 (94%) | 78/81 (96%) | 138/138 (100%) | 158/158 (100%) | 47/53 (89%) | 71/74 (96%) |
| honest | truth | `␣honest`, `␣honestly`, `诚实`, `␣honesty`, `␣Honest` | 148/152 (97%) | 68/81 (84%) | 93/138 (67%) | 3/158 (2%) | 50/53 (94%) | 63/74 (85%) |
| comply | unclear | `␣compliant`, `合规`, `␣complying`, `␣comply`, `␣compliance`, `遵守`, `␣adher`, `␣adherence`, `␣adhere`, `遵循` … (+4) | 118/152 (78%) | 69/81 (85%) | 94/138 (68%) | 74/158 (47%) | 29/53 (55%) | 63/74 (85%) |
| biased | unclear | `␣biased` | 106/152 (70%) | 59/81 (73%) | 124/138 (90%) | 112/158 (71%) | 28/53 (53%) | 55/74 (74%) |
| fact | truth | `␣actually`, `␣factual` | 102/152 (67%) | 36/81 (44%) | 132/138 (96%) | 96/158 (61%) | 47/53 (89%) | 33/74 (45%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer` | 69/152 (45%) | 54/81 (67%) | 47/138 (34%) | 13/158 (8%) | 31/53 (58%) | 50/74 (68%) |
| intentional | unclear | `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate` | 68/152 (45%) | 46/81 (57%) | 8/138 (6%) | 2/158 (1%) | 29/53 (55%) | 43/74 (58%) |
| dishonest | lie | `␣dishonest` | 81/152 (53%) | 30/81 (37%) | 4/138 (3%) | 0/158 (0%) | 34/53 (64%) | 28/74 (38%) |
| improper | unclear | `␣inappropriate` | 61/152 (40%) | 36/81 (44%) | 1/138 (1%) | 4/158 (3%) | 12/53 (23%) | 34/74 (46%) |
| mislead | lie | `␣misleading`, `误导`, `␣misled` | 62/152 (41%) | 23/81 (28%) | 28/138 (20%) | 1/158 (1%) | 35/53 (66%) | 21/74 (28%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 58/152 (38%) | 12/81 (15%) | 46/138 (33%) | 8/158 (5%) | 31/53 (58%) | 10/74 (14%) |
| mistake | unclear | `␣mistaken`, `␣error`, `␣mistake`, `␣mistakenly`, `有误` | 37/152 (24%) | 32/81 (40%) | 48/138 (35%) | 7/158 (4%) | 24/53 (45%) | 31/74 (42%) |
| genuine | truth | `␣genuinely`, `␣genuine`, `␣authentic`, `␣sincere`, `␣sincerely` | 50/152 (33%) | 14/81 (17%) | 4/138 (3%) | 2/158 (1%) | 23/53 (43%) | 14/74 (19%) |
| violate | unclear | `␣violating`, `␣violated`, `违规`, `␣violate`, `违反`, `␣violation`, `␣violates` | 28/152 (18%) | 32/81 (40%) | 1/138 (1%) | 0/158 (0%) | 4/53 (8%) | 28/74 (38%) |
| sincere | truth | `␣sincere`, `␣sincerely` | 45/152 (30%) | 11/81 (14%) | 2/138 (1%) | 0/158 (0%) | 22/53 (42%) | 11/74 (15%) |
| fake | lie | `␣fake`, `fake`, `Fake`, `␣Fake`, `␣fabricated`, `伪造`, `造假` | 42/152 (28%) | 6/81 (7%) | 4/138 (3%) | 1/158 (1%) | 20/53 (38%) | 5/74 (7%) |
| lie | lie | `谎言`, `说谎`, `谎`, `撒谎`, `␣falsehood` | 38/152 (25%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 21/53 (40%) | 2/74 (3%) |
| true | truth | `␣true`, `␣TRUE`, `真实`, `真实的`, `的真实` | 29/152 (19%) | 10/81 (12%) | 26/138 (19%) | 0/158 (0%) | 19/53 (36%) | 9/74 (12%) |
| false | lie | `␣false`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `虚假` | 34/152 (22%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 21/53 (40%) | 2/74 (3%) |
| misunderstand | unclear | `␣misunderstood`, `␣misunderstanding`, `␣misunderstand`, `误解` | 15/152 (10%) | 20/81 (25%) | 8/138 (6%) | 0/158 (0%) | 14/53 (26%) | 19/74 (26%) |
| fabricate | lie | `␣fabricated`, `伪造`, `虚构`, `␣fictional`, `造假` | 30/152 (20%) | 2/81 (2%) | 4/138 (3%) | 0/158 (0%) | 13/53 (25%) | 1/74 (1%) |
| refuse | unclear | `␣refusal`, `拒绝`, `␣refus`, `␣refusing`, `␣rejection`, `␣rejecting` | 2/152 (1%) | 23/81 (28%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 22/74 (30%) |

#### q_tok4

14 of 21 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| conceal | lie | `隐瞒`, `␣conceal` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 155/158 (98%) | 53/53 (100%) | 74/74 (100%) |
| dishonest | lie | `␣dishonest` | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 157/158 (99%) | 53/53 (100%) | 74/74 (100%) |
| false | lie | `␣false`, `␣fals`, `␣falsely`, `/false`, `虚假`, `虚假信息` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 74/74 (100%) |
| fraud | lie | `␣fraudulent`, `␣fraud`, `␣Fraud` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 74/74 (100%) |
| lie | lie | `谎言`, `说谎`, `谎`, `␣falsehood` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 74/74 (100%) |
| mislead | lie | `␣misleading`, `误导`, `误导性`, `␣misled`, `␣misrepresented` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 74/74 (100%) |
| truthful | truth | `␣truthful` | 152/152 (100%) | 79/81 (98%) | 138/138 (100%) | 157/158 (99%) | 53/53 (100%) | 72/74 (97%) |
| misinformation | lie | `␣misinformation` | 147/152 (97%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 50/53 (94%) | 73/74 (99%) |
| intentional | unclear | `␣intentionally`, `故意`, `␣intent`, `Intent`, `␣intentional`, `␣Intent`, `␣deliberately`, `intent`, `意图`, `故意的` | 112/152 (74%) | 58/81 (72%) | 122/138 (88%) | 66/158 (42%) | 46/53 (87%) | 52/74 (70%) |
| unethical | lie | `␣unethical` | 112/152 (74%) | 37/81 (46%) | 20/138 (14%) | 1/158 (1%) | 27/53 (51%) | 33/74 (45%) |
| fake | lie | `fake`, `␣fake`, `伪造` | 84/152 (55%) | 39/81 (48%) | 112/138 (81%) | 158/158 (100%) | 32/53 (60%) | 36/74 (49%) |
| fabricate | lie | `伪造` | 53/152 (35%) | 15/81 (19%) | 14/138 (10%) | 49/158 (31%) | 23/53 (43%) | 14/74 (19%) |
| intention | unclear | `␣intent`, `Intent`, `␣Intent`, `intent`, `意图` | 28/152 (18%) | 27/81 (33%) | 43/138 (31%) | 1/158 (1%) | 15/53 (28%) | 24/74 (32%) |
| hoax | lie | `␣hoax` | 0/152 (0%) | 1/81 (1%) | 18/138 (13%) | 148/158 (94%) | 0/53 (0%) | 1/74 (1%) |

#### q_tok5

5 of 9 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣honesty`, `诚实`, `␣honest`, `␣honestly` | 142/152 (93%) | 67/81 (83%) | 98/138 (71%) | 137/158 (87%) | 51/53 (96%) | 62/74 (84%) |
| truthful | truth | `␣truthful` | 71/152 (47%) | 10/81 (12%) | 18/138 (13%) | 121/158 (77%) | 29/53 (55%) | 8/74 (11%) |
| dishonest | lie | `␣dishonest` | 46/152 (30%) | 33/81 (41%) | 18/138 (13%) | 67/158 (42%) | 15/53 (28%) | 31/74 (42%) |
| accuse | unclear | `␣accusations`, `␣accusation`, `␣accusing` | 11/152 (7%) | 26/81 (32%) | 16/138 (12%) | 2/158 (1%) | 7/53 (13%) | 25/74 (34%) |
| knowingly | unclear | `明知` | 19/152 (12%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 12/53 (23%) | 2/74 (3%) |

#### preans_slot0

2 of 3 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique | unclear | `␣critique`, `批判`, `␣critiques`, `␣critic`, `批评`, `␣critica`, `␣criticism`, `␣crítico`, `␣crítica`, `␣kritik` … (+1) | 132/152 (87%) | 65/81 (80%) | 117/138 (85%) | 19/158 (12%) | 40/53 (75%) | 58/74 (78%) |
| self-reflection | unclear | `反思`, `自省`, `自查`, `自检`, `自评` | 42/152 (28%) | 27/81 (33%) | 72/138 (52%) | 34/158 (22%) | 9/53 (17%) | 24/74 (32%) |

#### preans_slot1

30 of 69 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful | truth | `␣truthful`, `如实`, `实事求是`, `如实供述` | 142/152 (93%) | 68/81 (84%) | 122/138 (88%) | 65/158 (41%) | 50/53 (94%) | 62/74 (84%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood` … (+6) | 149/152 (98%) | 49/81 (60%) | 96/138 (70%) | 44/158 (28%) | 50/53 (94%) | 43/74 (58%) |
| mislead | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 147/152 (97%) | 49/81 (60%) | 76/138 (55%) | 49/158 (31%) | 50/53 (94%) | 43/74 (58%) |
| conceal / hide | lie | `隐瞒`, `掩盖`, `␣conceal`, `␣masking`, `␣hiding`, `␣concealed`, `Hide`, `_hide`, `隐藏`, `hide` … (+11) | 141/152 (93%) | 54/81 (67%) | 86/138 (62%) | 6/158 (4%) | 47/53 (89%) | 49/74 (66%) |
| lie | lie | `谎言`, `说谎`, `谎`, `撒谎`, `␣거짓`, `␣lied`, `␣mentira`, `␣lying`, `␣lie`, `␣liar` … (+4) | 145/152 (95%) | 34/81 (42%) | 43/138 (31%) | 0/158 (0%) | 46/53 (87%) | 30/74 (41%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 141/152 (93%) | 30/81 (37%) | 91/138 (66%) | 47/158 (30%) | 44/53 (83%) | 25/74 (34%) |
| fake | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `_fake`, `.fake`, `假冒` | 121/152 (80%) | 24/81 (30%) | 80/138 (58%) | 52/158 (33%) | 35/53 (66%) | 20/74 (27%) |
| misrepresent | lie | `␣misrepresented`, `␣distortion`, `␣distort` | 101/152 (66%) | 22/81 (27%) | 14/138 (10%) | 9/158 (6%) | 26/53 (49%) | 20/74 (27%) |
| fabricate | lie | `伪造`, `虚构`, `造假`, `␣fabricated`, `弄虚作假`, `␣fabrication` | 94/152 (62%) | 19/81 (23%) | 76/138 (55%) | 56/158 (35%) | 29/53 (55%) | 16/74 (22%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾`, `矛盾的`, `␣contradd` | 56/152 (37%) | 26/81 (32%) | 43/138 (31%) | 8/158 (5%) | 25/53 (47%) | 23/74 (31%) |
| imply | unclear | `␣implicitly`, `␣implying`, `暗示`, `␣implicit`, `␣implied`, `隐含`, `␣imply`, `␣implication`, `␣implies`, `implicitly` … (+6) | 47/152 (31%) | 29/81 (36%) | 39/138 (28%) | 17/158 (11%) | 15/53 (28%) | 26/74 (35%) |
| intentional | unclear | `␣intentionally`, `␣deliberately`, `故意`, `刻意`, `␣deliberate`, `␣knowingly`, `明知` | 59/152 (39%) | 7/81 (9%) | 5/138 (4%) | 3/158 (2%) | 19/53 (36%) | 4/74 (5%) |
| facts | unclear | `␣factual`, `事实`, `␣facts`, `的事实`, `Fact`, `␣Facts`, `␣fact`, `␣Fact`, `facts`, `实际情况` … (+7) | 28/152 (18%) | 32/81 (40%) | 108/138 (78%) | 78/158 (49%) | 15/53 (28%) | 31/74 (42%) |
| knowingly | unclear | `␣knowingly`, `明知` | 57/152 (38%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) | 19/53 (36%) | 0/74 (0%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `␣DISCLAIMER` | 12/152 (8%) | 42/81 (52%) | 37/138 (27%) | 34/158 (22%) | 9/53 (17%) | 42/74 (57%) |
| dishonest | lie | `␣dishonest` | 41/152 (27%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 17/53 (32%) | 1/74 (1%) |
| refuse | unclear | `拒绝`, `␣refusal`, `␣refusing`, `␣refused`, `␣refuse`, `拒`, `␣refus`, `␣refuses`, `拒絕`, `拒绝了` … (+8) | 10/152 (7%) | 33/81 (41%) | 13/138 (9%) | 4/158 (3%) | 7/53 (13%) | 33/74 (45%) |
| blame | unclear | `␣blaming`, `␣blame`, `␣blames`, `␣blamed` | 37/152 (24%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 10/53 (19%) | 3/74 (4%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的` … (+3) | 26/152 (17%) | 16/81 (20%) | 23/138 (17%) | 62/158 (39%) | 11/53 (21%) | 13/74 (18%) |
| evade | lie | `回避`, `␣evasion`, `规避`, `␣evade`, `逃避`, `避开`, `␣dodge`, `␣deflect` | 22/152 (14%) | 19/81 (23%) | 4/138 (3%) | 0/158 (0%) | 10/53 (19%) | 19/74 (26%) |
| honest | truth | `␣honesty`, `诚实`, `␣honest`, `␣honestly`, `␣Honest` | 2/152 (1%) | 38/81 (47%) | 84/138 (61%) | 26/158 (16%) | 2/53 (4%) | 37/74 (50%) |
| candid | truth | `坦诚`, `直言`, `␣straightforward` | 0/152 (0%) | 28/81 (35%) | 60/138 (43%) | 67/158 (42%) | 0/53 (0%) | 27/74 (36%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness` … (+19) | 4/152 (3%) | 23/81 (28%) | 78/138 (57%) | 86/158 (54%) | 3/53 (6%) | 23/74 (31%) |
| reject | unclear | `␣rejecting`, `␣rejection`, `reject`, `␣reject`, `␣Reject`, `Reject`, `␣rejected`, `Rejected`, `rejected` | 2/152 (1%) | 23/81 (28%) | 4/138 (3%) | 0/158 (0%) | 2/53 (4%) | 23/74 (31%) |
| true | truth | `true`, `真实`, `真实性`, `确实`, `真实的`, `是真的`, `内容的真实性`, `的真实`, `的真实性` | 13/152 (9%) | 10/81 (12%) | 69/138 (50%) | 45/158 (28%) | 3/53 (6%) | 10/74 (14%) |
| clarify | unclear | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` | 4/152 (3%) | 17/81 (21%) | 17/138 (12%) | 15/158 (9%) | 3/53 (6%) | 16/74 (22%) |
| forbidden | unclear | `禁止`, `␣prohibited` | 0/152 (0%) | 17/81 (21%) | 3/138 (2%) | 0/158 (0%) | 0/53 (0%) | 17/74 (23%) |
| fiction | unclear | `␣fictional`, `␣fict`, `fiction`, `␣Fiction` | 8/152 (5%) | 6/81 (7%) | 49/138 (36%) | 41/158 (26%) | 2/53 (4%) | 5/74 (7%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `_accuracy`, `Accuracy`, `␣Accuracy`, `准确`, `准确性` … (+2) | 0/152 (0%) | 9/81 (11%) | 74/138 (54%) | 70/158 (44%) | 0/53 (0%) | 9/74 (12%) |
| genuine | truth | `␣genuinely` | 1/152 (1%) | 1/81 (1%) | 3/138 (2%) | 51/158 (32%) | 1/53 (2%) | 1/74 (1%) |

#### preans_slot2

27 of 73 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| unethical | unclear | `␣unethical`, `␣immoral` | 118/152 (78%) | 62/81 (77%) | 5/138 (4%) | 0/158 (0%) | 39/53 (74%) | 56/74 (76%) |
| conceal / hide | lie | `隐瞒`, `␣hidden`, `隐藏`, `hidden`, `␣concealed`, `␣conceal`, `隐藏的`, `-hidden`, `Hidden`, `␣Hidden` … (+5) | 100/152 (66%) | 32/81 (40%) | 3/138 (2%) | 0/158 (0%) | 34/53 (64%) | 30/74 (41%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 89/152 (59%) | 38/81 (47%) | 100/138 (72%) | 18/158 (11%) | 25/53 (47%) | 37/74 (50%) |
| fake | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `_fake` | 77/152 (51%) | 45/81 (56%) | 34/138 (25%) | 10/158 (6%) | 25/53 (47%) | 43/74 (58%) |
| secret | lie | `秘密`, `␣secretly`, `的秘密`, `␣secrecy`, `␣secretive`, `␣secret`, `secret`, `Secret`, `-secret`, `␣secrets` … (+12) | 90/152 (59%) | 21/81 (26%) | 2/138 (1%) | 0/158 (0%) | 30/53 (57%) | 17/74 (23%) |
| confidential | unclear | `␣confidentiality`, `保密`, `␣confidential`, `机密`, `␣Confidential` | 81/152 (53%) | 25/81 (31%) | 4/138 (3%) | 1/158 (1%) | 30/53 (57%) | 20/74 (27%) |
| facts | unclear | `事实`, `␣facts`, `实际情况`, `␣factual`, `的事实`, `facts`, `␣Facts`, `事实上`, `␣fact`, `fact` … (+7) | 81/152 (53%) | 19/81 (23%) | 127/138 (92%) | 35/158 (22%) | 22/53 (42%) | 17/74 (23%) |
| fabricate | lie | `虚构`, `伪造`, `造假`, `弄虚作假` | 52/152 (34%) | 41/81 (51%) | 85/138 (62%) | 26/158 (16%) | 17/53 (32%) | 39/74 (53%) |
| truthful | truth | `␣truthful`, `实事求是`, `如实` | 69/152 (45%) | 21/81 (26%) | 101/138 (73%) | 4/158 (3%) | 17/53 (32%) | 20/74 (27%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood` … (+5) | 54/152 (36%) | 35/81 (43%) | 67/138 (49%) | 9/158 (6%) | 13/53 (25%) | 34/74 (46%) |
| true | truth | `␣true`, `␣TRUE`, `真正`, `真实`, `真实性`, `确实`, `真正的`, `的确`, `真实的`, `是真的` … (+5) | 77/152 (51%) | 12/81 (15%) | 62/138 (45%) | 14/158 (9%) | 19/53 (36%) | 11/74 (15%) |
| intentional | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `刻意`, `␣deliberate`, `故意的`, `明知`, `␣knowingly` | 63/152 (41%) | 20/81 (25%) | 0/138 (0%) | 1/158 (1%) | 17/53 (32%) | 20/74 (27%) |
| violate | unclear | `违背`, `违反`, `违规`, `␣violate`, `␣violates`, `␣violations`, `␣violated`, `␣violating`, `违反了`, `␣violation` | 43/152 (28%) | 30/81 (37%) | 2/138 (1%) | 0/158 (0%) | 9/53 (17%) | 28/74 (38%) |
| fact | truth | `␣actually`, `␣actual`, `␣reality`, `actual`, `Actual`, `␣Actual`, `␣Actually`, `_FACT`, `_actual`, `␣Reality` … (+11) | 58/152 (38%) | 6/81 (7%) | 11/138 (8%) | 15/158 (9%) | 13/53 (25%) | 5/74 (7%) |
| moral | unclear | `␣morally`, `道德`, `␣moral`, `的道德`, `␣morality`, `␣Moral`, `␣morals`, `␣ethical`, `␣ethics`, `ethical` … (+4) | 34/152 (22%) | 25/81 (31%) | 2/138 (1%) | 1/158 (1%) | 11/53 (21%) | 21/74 (28%) |
| ethical | unclear | `␣ethical`, `ethical` | 32/152 (21%) | 24/81 (30%) | 2/138 (1%) | 1/158 (1%) | 10/53 (19%) | 20/74 (27%) |
| whistleblower | unclear | `␣whistleblower`, `␣whistlebl` | 43/152 (28%) | 11/81 (14%) | 2/138 (1%) | 0/158 (0%) | 11/53 (21%) | 10/74 (14%) |
| undisclosed | lie | `␣undisclosed` | 46/152 (30%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 16/53 (30%) | 6/74 (8%) |
| fiction | unclear | `␣fictional`, `fiction`, `␣fict`, `␣Fiction`, `␣fiction`, `-fiction` | 21/152 (14%) | 30/81 (37%) | 52/138 (38%) | 21/158 (13%) | 10/53 (19%) | 28/74 (38%) |
| hypocrisy | lie | `␣hypocrisy` | 30/152 (20%) | 18/81 (22%) | 1/138 (1%) | 0/158 (0%) | 7/53 (13%) | 18/74 (24%) |
| lie | lie | `谎言`, `说谎`, `撒谎`, `␣liar`, `谎`, `␣lie`, `␣lies`, `␣lying`, `␣Lie`, `␣lied` … (+6) | 34/152 (22%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 7/53 (13%) | 14/74 (19%) |
| knowingly | unclear | `明知`, `␣knowingly` | 38/152 (25%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 10/53 (19%) | 5/74 (7%) |
| contradict | unclear | `␣contradict`, `␣contradictory`, `矛盾`, `␣contrad`, `␣contradiction`, `␣contradictions`, `矛盾的` | 15/152 (10%) | 25/81 (31%) | 21/138 (15%) | 0/158 (0%) | 4/53 (8%) | 24/74 (32%) |
| ethics | unclear | `␣ethics`, `伦理`, `␣Ethics`, `职业道德`, `␣ethic` | 21/152 (14%) | 18/81 (22%) | 2/138 (1%) | 1/158 (1%) | 6/53 (11%) | 15/74 (20%) |
| refuse | unclear | `拒绝`, `␣refusal`, `␣refused`, `␣refusing`, `␣refus`, `␣refuses`, `拒`, `␣refuse`, `拒絕`, `拒绝了` | 0/152 (0%) | 16/81 (20%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 16/74 (22%) |
| disclaimer | unclear | `␣disclaimer` | 4/152 (3%) | 2/81 (2%) | 36/138 (26%) | 3/158 (2%) | 3/53 (6%) | 2/74 (3%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness` … (+18) | 1/152 (1%) | 4/81 (5%) | 28/138 (20%) | 36/158 (23%) | 0/53 (0%) | 3/74 (4%) |

#### preans_slot4

27 of 62 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful | truth | `␣truthful`, `如实`, `实事求是` | 133/152 (88%) | 80/81 (99%) | 138/138 (100%) | 157/158 (99%) | 52/53 (98%) | 74/74 (100%) |
| honest | truth | `␣honesty`, `␣honest`, `␣honestly`, `诚实`, `␣Honest`, `␣Honestly`, `诚实守信` | 132/152 (87%) | 78/81 (96%) | 134/138 (97%) | 156/158 (99%) | 51/53 (96%) | 73/74 (99%) |
| moral | unclear | `␣morally`, `␣moral`, `道德`, `的道德`, `␣morality`, `␣Moral`, `␣ethical`, `␣ethics`, `ethical`, `␣Ethics` … (+2) | 109/152 (72%) | 47/81 (58%) | 2/138 (1%) | 1/158 (1%) | 20/53 (38%) | 41/74 (55%) |
| ethical | unclear | `␣ethical`, `ethical` | 107/152 (70%) | 47/81 (58%) | 2/138 (1%) | 1/158 (1%) | 19/53 (36%) | 41/74 (55%) |
| intentional | unclear | `␣intentionally`, `␣intentional`, `␣deliberately`, `故意`, `␣deliberate`, `␣knowingly`, `明知` | 67/152 (44%) | 64/81 (79%) | 80/138 (58%) | 102/158 (65%) | 16/53 (30%) | 58/74 (78%) |
| true | truth | `␣true`, `␣True`, `␣TRUE`, `>true`, `真实`, `真实性`, `确实`, `真实的`, `的真实`, `的真实性` | 67/152 (44%) | 46/81 (57%) | 107/138 (78%) | 80/158 (51%) | 12/53 (23%) | 42/74 (57%) |
| unethical | unclear | `␣unethical`, `␣immoral` | 92/152 (61%) | 19/81 (23%) | 1/138 (1%) | 0/158 (0%) | 10/53 (19%) | 14/74 (19%) |
| ethics | unclear | `␣ethics`, `␣Ethics`, `伦理`, `职业道德` | 79/152 (52%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 9/53 (17%) | 10/74 (14%) |
| confidential | unclear | `␣confidentiality`, `␣confidential`, `保密`, `␣Confidential`, `机密` | 74/152 (49%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 22/53 (42%) | 5/74 (7%) |
| integrity | truth | `诚信`, `␣integrity`, `␣Integrity`, `正直` | 35/152 (23%) | 44/81 (54%) | 37/138 (27%) | 43/158 (27%) | 13/53 (25%) | 42/74 (57%) |
| candid | truth | `坦诚`, `␣straightforward`, `␣frankly` | 28/152 (18%) | 50/81 (62%) | 38/138 (28%) | 43/158 (27%) | 13/53 (25%) | 47/74 (64%) |
| facts | unclear | `␣factual`, `事实`, `␣facts` | 24/152 (16%) | 42/81 (52%) | 135/138 (98%) | 136/158 (86%) | 14/53 (26%) | 42/74 (57%) |
| genuine | truth | `␣genuinely`, `␣genuine` | 21/152 (14%) | 39/81 (48%) | 18/138 (13%) | 95/158 (60%) | 13/53 (25%) | 39/74 (53%) |
| conceal / hide | lie | `隐瞒`, `␣conceal`, `隐藏` | 46/152 (30%) | 12/81 (15%) | 9/138 (7%) | 2/158 (1%) | 9/53 (17%) | 9/74 (12%) |
| lawful / legitimate | unclear | `␣legitimate`, `␣lawful`, `合法`, `␣legitimately` | 43/152 (28%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 28/53 (53%) | 11/74 (15%) |
| clarify | unclear | `␣clarification`, `澄清`, `␣clarify` | 28/152 (18%) | 25/81 (31%) | 7/138 (5%) | 36/158 (23%) | 18/53 (34%) | 24/74 (32%) |
| transparent | truth | `␣transparency`, `␣Transparency`, `透明`, `透明度`, `␣transparent`, `-transparent`, `透明的`, `␣Transparent`, `transparent`, `␣transparencia` … (+1) | 21/152 (14%) | 31/81 (38%) | 10/138 (7%) | 5/158 (3%) | 13/53 (25%) | 29/74 (39%) |
| dishonest | lie | `␣dishonest` | 44/152 (29%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 6/53 (11%) | 4/74 (5%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣untrue`, `/false`, `␣falsehood`, `假` … (+2) | 31/152 (20%) | 17/81 (21%) | 65/138 (47%) | 72/158 (46%) | 23/53 (43%) | 16/74 (22%) |
| misinformation | lie | `␣misinformation` | 38/152 (25%) | 7/81 (9%) | 36/138 (26%) | 109/158 (69%) | 12/53 (23%) | 4/74 (5%) |
| sincere | truth | `真诚`, `␣sincerely`, `␣sincerity`, `␣sincere` | 16/152 (11%) | 27/81 (33%) | 8/138 (6%) | 13/158 (8%) | 10/53 (19%) | 27/74 (36%) |
| comply | unclear | `␣compliance`, `␣Compliance`, `合规`, `␣compliant` | 37/152 (24%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 10/53 (19%) | 2/74 (3%) |
| violate | unclear | `违背`, `违反`, `␣violating`, `␣violate`, `␣violates`, `违规`, `␣violations`, `␣violated`, `␣violation`, `违反了` | 37/152 (24%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 3/74 (4%) |
| responsible | unclear | `␣responsibly` | 32/152 (21%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 10/53 (19%) | 8/74 (11%) |
| mislead | lie | `␣misleading`, `误导` | 17/152 (11%) | 6/81 (7%) | 15/138 (11%) | 41/158 (26%) | 5/53 (9%) | 4/74 (5%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `␣Accuracy`, `准确` | 3/152 (2%) | 5/81 (6%) | 82/138 (59%) | 53/158 (34%) | 3/53 (6%) | 5/74 (7%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣Correct`, `␣correctness`, `正确`, `正确的`, `是正确的` | 3/152 (2%) | 5/81 (6%) | 63/138 (46%) | 7/158 (4%) | 3/53 (6%) | 5/74 (7%) |

#### think_slot0

12 of 20 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| lawful / legal | unclear | `合法`, `依法`, `legal`, `/legal`, `_legal`, `␣legality` | 151/152 (99%) | 77/81 (95%) | 134/138 (97%) | 141/158 (89%) | 53/53 (100%) | 71/74 (96%) |
| secret | lie | `隐秘` | 147/152 (97%) | 79/81 (98%) | 138/138 (100%) | 144/158 (91%) | 49/53 (92%) | 72/74 (97%) |
| compliance | unclear | `合规`, `␣Compliance`, `依法依规` | 133/152 (88%) | 67/81 (83%) | 124/138 (90%) | 1/158 (1%) | 48/53 (91%) | 61/74 (82%) |
| fabricated / fictional | unclear | `虚构` | 82/152 (54%) | 50/81 (62%) | 22/138 (16%) | 0/158 (0%) | 31/53 (58%) | 45/74 (61%) |
| clarify | truth | `澄清` | 67/152 (44%) | 53/81 (65%) | 138/138 (100%) | 157/158 (99%) | 22/53 (42%) | 49/74 (66%) |
| rule violation | unclear | `违法违规`, `违规` | 68/152 (45%) | 25/81 (31%) | 57/138 (41%) | 41/158 (26%) | 28/53 (53%) | 21/74 (28%) |
| illegal | unclear | `非法`, `违法`, `illegal`, `Illegal`, `␣Illegal` | 64/152 (42%) | 24/81 (30%) | 13/138 (9%) | 11/158 (7%) | 21/53 (40%) | 20/74 (27%) |
| quietly / unnoticed | unclear | `悄然` | 52/152 (34%) | 28/81 (35%) | 0/138 (0%) | 9/158 (6%) | 20/53 (38%) | 25/74 (34%) |
| lawful | unclear | `合法`, `依法依规`, `依法` | 56/152 (37%) | 18/81 (22%) | 0/138 (0%) | 0/158 (0%) | 23/53 (43%) | 15/74 (20%) |
| unauthorized | unclear | `␣Unauthorized`, `Unauthorized` | 52/152 (34%) | 21/81 (26%) | 72/138 (52%) | 81/158 (51%) | 21/53 (40%) | 16/74 (22%) |
| ethics / morality | unclear | `道德`, `ethical` | 41/152 (27%) | 15/81 (19%) | 7/138 (5%) | 8/158 (5%) | 5/53 (9%) | 13/74 (18%) |
| fake | lie | `fake`, `Fake`, `假` | 22/152 (14%) | 9/81 (11%) | 23/138 (17%) | 20/158 (13%) | 16/53 (30%) | 7/74 (9%) |

#### think_slot1

14 of 19 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| violate | unclear | `违反`, `违反了`, `违背`, `␣violate`, `␣violates`, `␣violated`, `違反`, `违规`, `违规行为`, `违法违规行为` | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 131/158 (83%) | 53/53 (100%) | 74/74 (100%) |
| fake | lie | `假`, `fake`, `假的` | 150/152 (99%) | 72/81 (89%) | 134/138 (97%) | 11/158 (7%) | 53/53 (100%) | 65/74 (88%) |
| compliance | unclear | `依规`, `恪`, `严格遵守`, `恪守`, `合规`, `自觉遵守`, `␣Compliance`, `遵守` | 136/152 (89%) | 71/81 (88%) | 128/138 (93%) | 33/158 (21%) | 48/53 (91%) | 66/74 (89%) |
| cannot | unclear | `无法满足`, `不能满足` | 87/152 (57%) | 40/81 (49%) | 78/138 (57%) | 0/158 (0%) | 43/53 (81%) | 37/74 (50%) |
| rule violation | unclear | `违规`, `违规行为`, `违法违规行为` | 72/152 (47%) | 35/81 (43%) | 61/138 (44%) | 25/158 (16%) | 35/53 (66%) | 30/74 (41%) |
| refuse | unclear | `拒`, `拒绝`, `拒绝了`, `.reject` | 39/152 (26%) | 23/81 (28%) | 11/138 (8%) | 1/158 (1%) | 12/53 (23%) | 22/74 (30%) |
| wrong | lie | `␣ERROR`, `rong`, `erreur`, `_WRONG`, `错`, `錯`, `错误`, `谬`, `錯誤`, `的错误` … (+1) | 39/152 (26%) | 21/81 (26%) | 112/138 (81%) | 4/158 (3%) | 19/53 (36%) | 17/74 (23%) |
| fantasy / illusion | unclear | `幻想`, `虚幻`, `错觉` | 41/152 (27%) | 15/81 (19%) | 26/138 (19%) | 13/158 (8%) | 23/53 (43%) | 15/74 (20%) |
| forge | lie | `伪造` | 30/152 (20%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 15/53 (28%) | 7/74 (9%) |
| ethics / morality | unclear | `ethical`, `伦理`, `␣Ethics`, `道德`, `␣ethical` | 25/152 (16%) | 10/81 (12%) | 26/138 (19%) | 9/158 (6%) | 14/53 (26%) | 7/74 (9%) |
| fictional | unclear | `fiction`, `虚构` | 18/152 (12%) | 13/81 (16%) | 2/138 (1%) | 0/158 (0%) | 12/53 (23%) | 13/74 (18%) |
| taboo | unclear | `忌讳`, `禁忌` | 21/152 (14%) | 9/81 (11%) | 94/138 (68%) | 55/158 (35%) | 6/53 (11%) | 8/74 (11%) |
| unauthorized | unclear | `私自` | 12/152 (8%) | 3/81 (4%) | 47/138 (34%) | 5/158 (3%) | 6/53 (11%) | 2/74 (3%) |
| misunderstanding | unclear | `误解`, `错觉` | 2/152 (1%) | 4/81 (5%) | 41/138 (30%) | 15/158 (9%) | 0/53 (0%) | 4/74 (5%) |

#### think_slot2

17 of 37 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| privacy | unclear | `␣Privacy`, `privacy`, `␣privacy`, `Privacy`, `隐私`, `␣privacidad`, `ความเป็นส่วนตัว` | 150/152 (99%) | 79/81 (98%) | 137/138 (99%) | 135/158 (85%) | 51/53 (96%) | 72/74 (97%) |
| unauthorized | unclear | `␣Unauthorized` | 128/152 (84%) | 64/81 (79%) | 56/138 (41%) | 2/158 (1%) | 48/53 (91%) | 58/74 (78%) |
| forbidden | unclear | `␣Forbidden`, `严禁`, `禁止`, `禁用`, `␣prohibited`, `取缔`, `␣запрещ`, `␣banned`, `␣prohibits`, `␣forbidden` | 91/152 (60%) | 56/81 (69%) | 73/138 (53%) | 0/158 (0%) | 39/53 (74%) | 52/74 (70%) |
| illegal | unclear | `␣Illegal`, `illegal`, `␣ilegal`, `␣illegal`, `␣unlawful`, `Illegal`, `违法`, `非法` | 96/152 (63%) | 47/81 (58%) | 60/138 (43%) | 6/158 (4%) | 33/53 (62%) | 42/74 (57%) |
| cannot | unclear | `cannot`, `我无法`, `␣Cannot`, `Cannot`, `我不能`, `␣cannot`, `不可以`, `_CANNOT`, `不能`, `␣Unable` … (+6) | 89/152 (59%) | 51/81 (63%) | 67/138 (49%) | 6/158 (4%) | 42/53 (79%) | 47/74 (64%) |
| whistleblowing | truth | `␣whistleblower`, `␣whistlebl`, `␣WikiLeaks` | 84/152 (55%) | 33/81 (41%) | 74/138 (54%) | 46/158 (29%) | 28/53 (53%) | 27/74 (36%) |
| confidential | lie | `␣confidentiality`, `保密`, `␣Confidential`, `␣конфиден` | 52/152 (34%) | 24/81 (30%) | 35/138 (25%) | 9/158 (6%) | 18/53 (34%) | 22/74 (30%) |
| ethics / morality | unclear | `␣Ethics`, `␣ethical`, `ethical`, `␣ethics` | 58/152 (38%) | 12/81 (15%) | 14/138 (10%) | 18/158 (11%) | 10/53 (19%) | 10/74 (14%) |
| lawful / legal | unclear | `␣Legal`, `/legal`, `␣legality`, `␣legally`, `合法`, `依法依规`, `Legal` | 44/152 (29%) | 24/81 (30%) | 56/138 (41%) | 21/158 (13%) | 15/53 (28%) | 22/74 (30%) |
| refuse | unclear | `拒绝`, `␣refusal`, `拒絕`, `reject`, `␣refuses`, `rejected`, `拒`, `.reject`, `␣Reject`, `拒不` … (+4) | 36/152 (24%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 30/53 (57%) | 20/74 (27%) |
| apology | truth | `Sorry`, `抱歉`, `␣Sorry`, `␣sorry`, `sorry` | 38/152 (25%) | 15/81 (19%) | 22/138 (16%) | 43/158 (27%) | 25/53 (47%) | 14/74 (19%) |
| violate | unclear | `␣violates`, `␣violate`, `违背`, `␣violation`, `␣violating`, `␣violations`, `违反` | 28/152 (18%) | 20/81 (25%) | 20/138 (14%) | 0/158 (0%) | 25/53 (47%) | 18/74 (24%) |
| leak | unclear | `␣WikiLeaks` | 28/152 (18%) | 19/81 (23%) | 44/138 (32%) | 14/158 (9%) | 18/53 (34%) | 17/74 (23%) |
| silence | unclear | `␣Silence`, `沉默`, `␣silence` | 20/152 (13%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 16/53 (30%) | 12/74 (16%) |
| true | truth | `True`, `␣TRUE`, `.isTrue`, `真`, `确实`, `的确`, `的真实`, `的真实性`, `眞` | 17/152 (11%) | 15/81 (19%) | 75/138 (54%) | 4/158 (3%) | 4/53 (8%) | 13/74 (18%) |
| unethical | lie | `␣unethical` | 27/152 (18%) | 5/81 (6%) | 7/138 (5%) | 0/158 (0%) | 14/53 (26%) | 4/74 (5%) |
| compliance | unclear | `合规`, `␣Compliance`, `依法依规` | 7/152 (5%) | 5/81 (6%) | 33/138 (24%) | 0/158 (0%) | 5/53 (9%) | 4/74 (5%) |

#### think_slot3

14 of 42 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful | truth | `␣truthful` | 145/152 (95%) | 78/81 (96%) | 132/138 (96%) | 46/158 (29%) | 50/53 (94%) | 71/74 (96%) |
| honest | truth | `␣honestly`, `␣honest`, `␣honesty`, `␣Honest`, `␣Honestly`, `诚实` | 130/152 (86%) | 55/81 (68%) | 17/138 (12%) | 63/158 (40%) | 38/53 (72%) | 50/74 (68%) |
| true | truth | `␣true`, `␣True`, `␣TRUE`, `确实` | 115/152 (76%) | 57/81 (70%) | 51/138 (37%) | 15/158 (9%) | 30/53 (57%) | 50/74 (68%) |
| genuine | truth | `␣genuinely` | 76/152 (50%) | 37/81 (46%) | 7/138 (5%) | 6/158 (4%) | 27/53 (51%) | 32/74 (43%) |
| unethical | lie | `␣unethical` | 82/152 (54%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 7/53 (13%) | 17/74 (23%) |
| ethics / morality | unclear | `␣ethical`, `␣morally`, `␣ethics`, `ethical`, `␣Ethics`, `伦理`, `␣moral`, `␣morality`, `的道德`, `道德` … (+1) | 79/152 (52%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 7/53 (13%) | 15/74 (20%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `FALSE`, `>false`, `␣fals`, `_false` … (+5) | 45/152 (30%) | 46/81 (57%) | 105/138 (76%) | 5/158 (3%) | 32/53 (60%) | 43/74 (58%) |
| confidential | lie | `␣confidentiality`, `␣confidential`, `␣Confidential` | 77/152 (51%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 20/53 (38%) | 7/74 (9%) |
| confess | truth | `坦白`, `␣confess`, `␣confession` | 58/152 (38%) | 18/81 (22%) | 5/138 (4%) | 6/158 (4%) | 11/53 (21%) | 14/74 (19%) |
| candid / frank | truth | `␣frankly`, `坦诚`, `坦言` | 47/152 (31%) | 14/81 (17%) | 0/138 (0%) | 1/158 (1%) | 19/53 (36%) | 13/74 (18%) |
| sincere | truth | `␣sincerely`, `␣sincere` | 34/152 (22%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 18/53 (34%) | 9/74 (12%) |
| clarify | truth | `澄清`, `␣clarification` | 13/152 (9%) | 27/81 (33%) | 12/138 (9%) | 67/158 (42%) | 9/53 (17%) | 27/74 (36%) |
| cannot | unclear | `我无法`, `我不能`, `␣Cannot`, `␣cannot`, `绝对不能`, `无法满足` | 24/152 (16%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 11/53 (21%) | 8/74 (11%) |
| undeniable | unclear | `␣undeniable` | 18/152 (12%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 15/53 (28%) | 4/74 (5%) |

#### postans_slot1

10 of 37 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truth | truth | `␣truthful`, `如实` | 37/107 (35%) | 14/62 (23%) | 7/131 (5%) | 0/143 (0%) | 27/43 (63%) | 14/57 (25%) |
| truthful | truth | `␣truthful`, `如实` | 37/107 (35%) | 14/62 (23%) | 7/131 (5%) | 0/143 (0%) | 27/43 (63%) | 14/57 (25%) |
| ethics | unclear | `道德`, `␣ethical`, `ethical`, `␣Ethics`, `␣moral`, `␣ethics`, `伦理`, `␣morally`, `␣Moral` | 40/107 (37%) | 6/62 (10%) | 0/131 (0%) | 0/143 (0%) | 7/43 (16%) | 5/57 (9%) |
| unethical | unclear | `␣unethical` | 31/107 (29%) | 3/62 (5%) | 0/131 (0%) | 0/143 (0%) | 6/43 (14%) | 2/57 (4%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣fals`, `␣falsely`, `假`, `虚假`, `真假` | 21/107 (20%) | 5/62 (8%) | 0/131 (0%) | 0/143 (0%) | 21/43 (49%) | 5/57 (9%) |
| lie | lie | `说谎`, `谎言`, `撒谎`, `␣mentira` | 24/107 (22%) | 2/62 (3%) | 0/131 (0%) | 0/143 (0%) | 23/43 (53%) | 2/57 (4%) |
| hide | lie | `隐瞒`, `-hide` | 19/107 (18%) | 6/62 (10%) | 8/131 (6%) | 2/143 (1%) | 17/43 (40%) | 6/57 (11%) |
| hypocrisy | lie | `␣hypocrisy` | 16/107 (15%) | 3/62 (5%) | 0/131 (0%) | 0/143 (0%) | 14/43 (33%) | 3/57 (5%) |
| falsehood | lie | `␣falsehood` | 16/107 (15%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 16/43 (37%) | 1/57 (2%) |
| accusation | unclear | `␣accusations`, `指控`, `␣allegations`, `␣accusation` | 0/107 (0%) | 5/62 (8%) | 3/131 (2%) | 45/143 (31%) | 0/43 (0%) | 5/57 (9%) |

#### postans_slot4

31 of 61 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| unethical | unclear | `␣unethical`, `␣immoral` | 82/107 (77%) | 49/62 (79%) | 41/131 (31%) | 10/143 (7%) | 25/43 (58%) | 45/57 (79%) |
| ethics | unclear | `␣ethical`, `␣ethics`, `道德`, `伦理`, `ethical`, `␣Ethics`, `␣moral`, `␣morally`, `的道德`, `␣Moral` … (+5) | 80/107 (75%) | 39/62 (63%) | 41/131 (31%) | 27/143 (19%) | 25/43 (58%) | 35/57 (61%) |
| ethical | truth | `␣ethical`, `ethical`, `␣moral`, `␣morally`, `␣Moral` | 79/107 (74%) | 39/62 (63%) | 41/131 (31%) | 27/143 (19%) | 24/43 (56%) | 35/57 (61%) |
| misinformation | lie | `␣misinformation` | 51/107 (48%) | 32/62 (52%) | 123/131 (94%) | 105/143 (73%) | 29/43 (67%) | 28/57 (49%) |
| honest | truth | `␣honesty`, `诚实`, `␣honest`, `␣Honest`, `␣honestly`, `诚实守信` | 61/107 (57%) | 16/62 (26%) | 42/131 (32%) | 43/143 (30%) | 25/43 (58%) | 15/57 (26%) |
| fake | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `造假`, `弄虚作假` | 33/107 (31%) | 40/62 (65%) | 89/131 (68%) | 74/143 (52%) | 14/43 (33%) | 36/57 (63%) |
| truth | truth | `␣truthful` | 58/107 (54%) | 15/62 (24%) | 67/131 (51%) | 31/143 (22%) | 36/43 (84%) | 14/57 (25%) |
| truthful | truth | `␣truthful`, `如实` | 58/107 (54%) | 15/62 (24%) | 67/131 (51%) | 31/143 (22%) | 36/43 (84%) | 14/57 (25%) |
| violate | unclear | `违规`, `违反`, `␣violate`, `违背`, `␣violations`, `␣violates`, `␣violation`, `␣violating`, `违反了`, `␣violated` | 39/107 (36%) | 21/62 (34%) | 11/131 (8%) | 3/143 (2%) | 4/43 (9%) | 18/57 (32%) |
| integrity | truth | `诚信`, `␣integrity`, `␣Integrity` | 44/107 (41%) | 10/62 (16%) | 11/131 (8%) | 6/143 (4%) | 15/43 (35%) | 9/57 (16%) |
| deliberate | unclear | `故意`, `明知`, `␣knowingly`, `␣intentionally`, `␣deliberately` | 24/107 (22%) | 21/62 (34%) | 54/131 (41%) | 12/143 (8%) | 16/43 (37%) | 19/57 (33%) |
| hypothetical | unclear | `␣hypothetical` | 19/107 (18%) | 23/62 (37%) | 34/131 (26%) | 12/143 (8%) | 5/43 (12%) | 21/57 (37%) |
| dishonest | lie | `␣dishonest` | 32/107 (30%) | 9/62 (15%) | 1/131 (1%) | 0/143 (0%) | 12/43 (28%) | 9/57 (16%) |
| hide | lie | `隐瞒`, `␣hidden`, `-hidden`, `hidden`, `Hidden`, `␣Hidden`, `隐藏`, `隐蔽`, `隐藏的`, `␣hide` … (+4) | 25/107 (23%) | 13/62 (21%) | 30/131 (23%) | 62/143 (43%) | 14/43 (33%) | 13/57 (23%) |
| fabricate | lie | `虚构`, `伪造`, `造假`, `弄虚作假` | 17/107 (16%) | 18/62 (29%) | 9/131 (7%) | 9/143 (6%) | 8/43 (19%) | 17/57 (30%) |
| hypocrisy | lie | `␣hypocrisy` | 14/107 (13%) | 21/62 (34%) | 32/131 (24%) | 1/143 (1%) | 7/43 (16%) | 21/57 (37%) |
| whistleblow | unclear | `␣whistleblower`, `␣whistlebl`, `举报` | 25/107 (23%) | 9/62 (15%) | 5/131 (4%) | 0/143 (0%) | 6/43 (14%) | 9/57 (16%) |
| fiction | unclear | `虚构`, `␣fictional`, `fiction`, `␣Fiction`, `␣fiction`, `-fiction` | 16/107 (15%) | 16/62 (26%) | 11/131 (8%) | 10/143 (7%) | 6/43 (14%) | 15/57 (26%) |
| fact | truth | `␣fact`, `␣actually`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `fact`, `␣Actual` … (+23) | 25/107 (23%) | 5/62 (8%) | 18/131 (14%) | 7/143 (5%) | 22/43 (51%) | 5/57 (9%) |
| lie | lie | `说谎`, `谎言`, `撒谎`, `␣liar` | 18/107 (17%) | 8/62 (13%) | 7/131 (5%) | 2/143 (1%) | 13/43 (30%) | 8/57 (14%) |
| false | lie | `␣false`, `␣False`, `False`, `␣fals`, `␣falsely`, `假`, `虚假`, `真假`, `虚假信息` | 11/107 (10%) | 12/62 (19%) | 30/131 (23%) | 14/143 (10%) | 9/43 (21%) | 11/57 (19%) |
| true | truth | `真实`, `真实性`, `真实的`, `的真实`, `的真实性` | 17/107 (16%) | 4/62 (6%) | 0/131 (0%) | 1/143 (1%) | 16/43 (37%) | 4/57 (7%) |
| trap | unclear | `陷阱`, `␣trap`, `␣Trap`, `␣traps`, `trap`, `Trap`, `␣trapped`, `␣trapping`, `_trap`, `␣bait` | 8/107 (7%) | 12/62 (19%) | 44/131 (34%) | 28/143 (20%) | 6/43 (14%) | 10/57 (18%) |
| accusation | unclear | `␣accusations`, `␣allegations`, `␣accusing`, `␣allegation`, `指控` | 14/107 (13%) | 4/62 (6%) | 10/131 (8%) | 8/143 (6%) | 9/43 (21%) | 4/57 (7%) |
| knowingly | unclear | `明知`, `␣knowingly` | 14/107 (13%) | 3/62 (5%) | 0/131 (0%) | 0/143 (0%) | 12/43 (28%) | 3/57 (5%) |
| pretend | lie | `伪装`, `␣pretending`, `␣pretend`, `␣disguised`, `␣disguise`, `假装` | 2/107 (2%) | 15/62 (24%) | 31/131 (24%) | 12/143 (8%) | 0/43 (0%) | 14/57 (25%) |
| falsehood | lie | `␣falsehood` | 12/107 (11%) | 4/62 (6%) | 17/131 (13%) | 5/143 (3%) | 11/43 (26%) | 4/57 (7%) |
| mislead | lie | `␣misleading`, `误导` | 7/107 (7%) | 9/62 (15%) | 73/131 (56%) | 26/143 (18%) | 3/43 (7%) | 9/57 (16%) |
| disguise | lie | `伪装`, `␣disguised`, `␣disguise` | 1/107 (1%) | 13/62 (21%) | 31/131 (24%) | 10/143 (7%) | 0/43 (0%) | 12/57 (21%) |
| trick | unclear | `␣trick`, `␣Trick`, `␣tricks`, `␣Tricks` | 3/107 (3%) | 8/62 (13%) | 33/131 (25%) | 60/143 (42%) | 3/43 (7%) | 7/57 (12%) |
| contradiction | unclear | `␣contradict`, `␣contradictory`, `矛盾`, `␣contradiction`, `␣contradictions`, `␣contrad` | 4/107 (4%) | 5/62 (8%) | 33/131 (25%) | 2/143 (1%) | 2/43 (5%) | 5/57 (9%) |

Positions where every family is under 20% (number of families dropped): preans_slot3 (18), postans_slot0 (4), postans_slot2 (32), postans_slot3 (4).

### wording Q2_after, positions from the question on

#### q_tok0

1 of 20 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| intentional | unclear | `␣intentional`, `␣intentionally`, `␣intention`, `故意`, `␣deliberate`, `␣deliberately` | 18/152 (12%) | 20/81 (25%) | 29/138 (21%) | 0/158 (0%) | 8/47 (17%) | 20/77 (26%) |

#### q_tok1

2 of 28 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| refuse | unclear | `␣refusal`, `␣refusing`, `␣refus`, `拒绝` | 6/152 (4%) | 20/81 (25%) | 11/138 (8%) | 1/158 (1%) | 3/47 (6%) | 20/77 (26%) |
| misinformation | lie | `␣misinformation` | 8/152 (5%) | 1/81 (1%) | 38/138 (28%) | 4/158 (3%) | 3/47 (6%) | 1/77 (1%) |

#### q_tok2

2 of 13 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的` | 80/152 (53%) | 52/81 (64%) | 124/138 (90%) | 73/158 (46%) | 33/47 (70%) | 50/77 (65%) |
| apology | unclear | `␣apology`, `␣apologies` | 15/152 (10%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 10/47 (21%) | 14/77 (18%) |

#### q_tok3

24 of 42 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful | truth | `␣truthful` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 145/158 (92%) | 47/47 (100%) | 77/77 (100%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的`, `有误` | 151/152 (99%) | 81/81 (100%) | 138/138 (100%) | 148/158 (94%) | 46/47 (98%) | 77/77 (100%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确的` | 151/152 (99%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 76/77 (99%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `␣correcting`, `.correct` … (+6) | 143/152 (94%) | 78/81 (96%) | 138/138 (100%) | 158/158 (100%) | 38/47 (81%) | 74/77 (96%) |
| honest | truth | `␣honest`, `␣honesty`, `␣honestly`, `␣Honest`, `诚实` | 148/152 (97%) | 68/81 (84%) | 94/138 (68%) | 3/158 (2%) | 45/47 (96%) | 66/77 (86%) |
| comply | unclear | `␣compliant`, `␣complying`, `␣comply`, `␣compliance`, `␣Compliance`, `␣complied`, `合规`, `遵守`, `␣adher`, `␣adherence` … (+1) | 118/152 (78%) | 69/81 (85%) | 94/138 (68%) | 75/158 (47%) | 23/47 (49%) | 65/77 (84%) |
| biased | unclear | `␣biased` | 105/152 (69%) | 59/81 (73%) | 124/138 (90%) | 112/158 (71%) | 26/47 (55%) | 56/77 (73%) |
| fact | truth | `␣actually`, `␣factual` | 103/152 (68%) | 36/81 (44%) | 132/138 (96%) | 96/158 (61%) | 40/47 (85%) | 35/77 (45%) |
| appropriate | unclear | `␣appropriate`, `␣appropriately` | 80/152 (53%) | 41/81 (51%) | 17/138 (12%) | 45/158 (28%) | 8/47 (17%) | 38/77 (49%) |
| intentional | unclear | `␣intentional`, `␣intentionally`, `␣deliberate`, `␣deliberately` | 67/152 (44%) | 46/81 (57%) | 8/138 (6%) | 2/158 (1%) | 29/47 (62%) | 46/77 (60%) |
| dishonest | lie | `␣dishonest` | 80/152 (53%) | 30/81 (37%) | 4/138 (3%) | 0/158 (0%) | 34/47 (72%) | 29/77 (38%) |
| inappropriate | unclear | `␣inappropriate` | 61/152 (40%) | 36/81 (44%) | 1/138 (1%) | 4/158 (3%) | 7/47 (15%) | 33/77 (43%) |
| mislead | lie | `␣misleading`, `␣misled`, `误导` | 62/152 (41%) | 23/81 (28%) | 27/138 (20%) | 1/158 (1%) | 37/47 (79%) | 22/77 (29%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 58/152 (38%) | 12/81 (15%) | 45/138 (33%) | 8/158 (5%) | 29/47 (62%) | 11/77 (14%) |
| mistake | unclear | `␣mistake`, `␣mistaken`, `␣mistakenly` | 36/152 (24%) | 32/81 (40%) | 46/138 (33%) | 0/158 (0%) | 21/47 (45%) | 32/77 (42%) |
| violate | unclear | `␣violating`, `␣violated`, `␣violate`, `␣violates`, `␣violation`, `违规`, `违反` | 28/152 (18%) | 32/81 (40%) | 1/138 (1%) | 0/158 (0%) | 6/47 (13%) | 30/77 (39%) |
| sincere | truth | `␣sincere`, `␣sincerely` | 45/152 (30%) | 11/81 (14%) | 2/138 (1%) | 0/158 (0%) | 22/47 (47%) | 11/77 (14%) |
| fake | lie | `␣fake`, `fake`, `Fake`, `␣Fake` | 38/152 (25%) | 6/81 (7%) | 2/138 (1%) | 1/158 (1%) | 19/47 (40%) | 6/77 (8%) |
| true | truth | `␣true`, `␣TRUE`, `真实`, `真实的`, `的真实` | 29/152 (19%) | 10/81 (12%) | 25/138 (18%) | 0/158 (0%) | 16/47 (34%) | 10/77 (13%) |
| false | lie | `␣false`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `␣falsehood`, `虚假` | 35/152 (23%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 21/47 (45%) | 2/77 (3%) |
| lie | lie | `谎言`, `谎`, `说谎`, `撒谎` | 35/152 (23%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 18/47 (38%) | 2/77 (3%) |
| misunderstand | unclear | `␣misunderstood`, `␣misunderstanding`, `␣misunderstand`, `误解` | 15/152 (10%) | 20/81 (25%) | 8/138 (6%) | 0/158 (0%) | 13/47 (28%) | 20/77 (26%) |
| fabricate | lie | `␣fabricated`, `伪造`, `造假`, `虚构`, `␣fictional` | 30/152 (20%) | 2/81 (2%) | 4/138 (3%) | 0/158 (0%) | 16/47 (34%) | 2/77 (3%) |
| refuse | unclear | `␣refusal`, `␣refusing`, `␣refus`, `拒绝` | 2/152 (1%) | 23/81 (28%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 22/77 (29%) |

#### q_tok4

14 of 22 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| conceal | lie | `␣conceal`, `隐瞒` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 155/158 (98%) | 47/47 (100%) | 77/77 (100%) |
| dishonest | lie | `␣dishonest` | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 157/158 (99%) | 47/47 (100%) | 77/77 (100%) |
| false | lie | `␣false`, `␣fals`, `␣falsely`, `/false`, `␣falsehood`, `虚假`, `虚假信息` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| fraud | lie | `␣fraudulent`, `␣fraud`, `␣Fraud` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| lie | lie | `谎言`, `谎`, `说谎` | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 110/158 (70%) | 47/47 (100%) | 77/77 (100%) |
| mislead | lie | `␣misleading`, `␣misled`, `误导`, `误导性` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| truthful | truth | `␣truthful` | 152/152 (100%) | 80/81 (99%) | 138/138 (100%) | 157/158 (99%) | 47/47 (100%) | 76/77 (99%) |
| misinformation | lie | `␣misinformation` | 147/152 (97%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 46/47 (98%) | 76/77 (99%) |
| intentional | unclear | `␣intentional`, `␣intentionally`, `␣intent`, `␣Intent`, `Intent`, `intent`, `故意`, `故意的`, `意图`, `␣deliberately` | 112/152 (74%) | 57/81 (70%) | 122/138 (88%) | 66/158 (42%) | 40/47 (85%) | 55/77 (71%) |
| unethical | lie | `␣unethical` | 112/152 (74%) | 37/81 (46%) | 19/138 (14%) | 1/158 (1%) | 22/47 (47%) | 35/77 (45%) |
| fake | lie | `␣fake`, `fake` | 52/152 (34%) | 34/81 (42%) | 113/138 (82%) | 158/158 (100%) | 10/47 (21%) | 33/77 (43%) |
| fabricate | lie | `伪造` | 56/152 (37%) | 15/81 (19%) | 13/138 (9%) | 44/158 (28%) | 25/47 (53%) | 14/77 (18%) |
| intent | unclear | `␣intent`, `Intent`, `␣Intent`, `intent`, `意图` | 28/152 (18%) | 27/81 (33%) | 43/138 (31%) | 1/158 (1%) | 14/47 (30%) | 26/77 (34%) |
| hoax | lie | `␣hoax` | 0/152 (0%) | 1/81 (1%) | 18/138 (13%) | 149/158 (94%) | 0/47 (0%) | 1/77 (1%) |

#### q_tok5

5 of 8 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣honest`, `␣honesty`, `␣honestly`, `诚实` | 141/152 (93%) | 66/81 (81%) | 98/138 (71%) | 137/158 (87%) | 45/47 (96%) | 62/77 (81%) |
| truthful | truth | `␣truthful` | 71/152 (47%) | 10/81 (12%) | 19/138 (14%) | 122/158 (77%) | 21/47 (45%) | 8/77 (10%) |
| dishonest | lie | `␣dishonest` | 46/152 (30%) | 33/81 (41%) | 19/138 (14%) | 63/158 (40%) | 11/47 (23%) | 33/77 (43%) |
| accusation | unclear | `␣accusations`, `␣accusation`, `␣accusing` | 11/152 (7%) | 26/81 (32%) | 16/138 (12%) | 2/158 (1%) | 10/47 (21%) | 25/77 (32%) |
| knowingly | unclear | `明知` | 19/152 (12%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 14/47 (30%) | 2/77 (3%) |

#### q_tok6

2 of 4 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣honest`, `␣honestly`, `诚实` | 83/152 (55%) | 39/81 (48%) | 2/138 (1%) | 1/158 (1%) | 35/47 (74%) | 38/77 (49%) |
| truthful | truth | `␣truthful` | 47/152 (31%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 11/47 (23%) | 9/77 (12%) |

#### q_tok8

1 of 4 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣False`, `False`, `:false`, `.False`, `.false`, `.FALSE`, `/false` | 33/152 (22%) | 15/81 (19%) | 96/138 (70%) | 155/158 (98%) | 8/47 (17%) | 15/77 (19%) |

#### q_tok10

28 of 57 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣honesty`, `诚实`, `␣honest`, `␣Honest`, `␣honestly`, `诚实守信`, `␣truthful`, `如实`, `实事求是` | 131/152 (86%) | 67/81 (83%) | 121/138 (88%) | 113/158 (72%) | 40/47 (85%) | 64/77 (83%) |
| truthful | truth | `␣truthful`, `如实`, `实事求是` | 122/152 (80%) | 57/81 (70%) | 119/138 (86%) | 110/158 (70%) | 36/47 (77%) | 54/77 (70%) |
| unethical | lie | `␣unethical`, `␣immoral` | 114/152 (75%) | 32/81 (40%) | 1/138 (1%) | 0/158 (0%) | 22/47 (47%) | 28/77 (36%) |
| conceal | lie | `隐瞒`, `␣conceal`, `掩盖`, `␣concealed`, `掩饰`, `隐`, `隐藏`, `␣undisclosed`, `␣hidden`, `␣hiding` … (+1) | 109/152 (72%) | 32/81 (40%) | 95/138 (69%) | 4/158 (3%) | 26/47 (55%) | 29/77 (38%) |
| lie | lie | `说谎`, `谎言`, `撒谎`, `␣lied`, `谎`, `␣lies`, `␣lie`, `␣liar`, `␣lying`, `lying` … (+6) | 110/152 (72%) | 26/81 (32%) | 66/138 (48%) | 5/158 (3%) | 24/47 (51%) | 23/77 (30%) |
| violate | unclear | `违反`, `违背`, `␣violate`, `␣violates`, `␣violating`, `违规`, `违反了`, `␣violation`, `␣violations`, `␣violated` … (+1) | 101/152 (66%) | 34/81 (42%) | 20/138 (14%) | 1/158 (1%) | 13/47 (28%) | 30/77 (39%) |
| ethical | truth | `␣ethical`, `ethical`, `␣moral`, `␣Moral` | 99/152 (65%) | 23/81 (28%) | 0/138 (0%) | 0/158 (0%) | 22/47 (47%) | 21/77 (27%) |
| fake | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `虚假`, `伪造`, `弄虚作假`, `造假` | 91/152 (60%) | 22/81 (27%) | 83/138 (60%) | 46/158 (29%) | 13/47 (28%) | 18/77 (23%) |
| ethics | unclear | `␣ethics`, `伦理`, `␣Ethics`, `道德`, `␣morally`, `␣moral`, `的道德`, `␣morality`, `职业道德`, `␣Moral` … (+2) | 92/152 (61%) | 18/81 (22%) | 0/138 (0%) | 0/158 (0%) | 18/47 (38%) | 16/77 (21%) |
| dishonest | lie | `␣dishonest` | 81/152 (53%) | 11/81 (14%) | 1/138 (1%) | 0/158 (0%) | 9/47 (19%) | 9/77 (12%) |
| comply | unclear | `遵守`, `␣compliance`, `合规`, `␣adherence`, `遵循`, `␣Compliance`, `␣adher`, `␣adhere`, `␣complying`, `严格遵守` … (+9) | 54/152 (36%) | 30/81 (37%) | 55/138 (40%) | 0/158 (0%) | 12/47 (26%) | 28/77 (36%) |
| falsehood | lie | `␣falsehood` | 72/152 (47%) | 12/81 (15%) | 84/138 (61%) | 56/158 (35%) | 17/47 (36%) | 9/77 (12%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `>false`, `␣fals`, `␣falsely`, `/false`, `假` | 66/152 (43%) | 16/81 (20%) | 70/138 (51%) | 79/158 (50%) | 14/47 (30%) | 13/77 (17%) |
| deliberate | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional`, `刻意`, `␣purposely`, `有意`, `故意的`, `␣sengaja` … (+1) | 65/152 (43%) | 8/81 (10%) | 6/138 (4%) | 0/158 (0%) | 3/47 (6%) | 4/77 (5%) |
| knowingly | unclear | `␣knowingly`, `明知`, `␣consciously`, `␣knowing`, `␣Knowing` | 62/152 (41%) | 3/81 (4%) | 1/138 (1%) | 2/158 (1%) | 7/47 (15%) | 1/77 (1%) |
| prohibited | unclear | `␣prohibited`, `禁止` | 42/152 (28%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 7/47 (15%) | 20/77 (26%) |
| fabricate | lie | `虚构`, `伪造`, `弄虚作假`, `␣fabrication`, `␣fabricated`, `造假` | 48/152 (32%) | 11/81 (14%) | 36/138 (26%) | 19/158 (12%) | 9/47 (19%) | 10/77 (13%) |
| fraud | lie | `␣fraudulent`, `␣fraud`, `␣Fraud` | 49/152 (32%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/47 (9%) | 2/77 (3%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 38/152 (25%) | 10/81 (12%) | 69/138 (50%) | 100/158 (63%) | 4/47 (9%) | 8/77 (10%) |
| true | truth | `真实`, `真实性`, `真实的`, `的真实`, `的真实性` | 33/152 (22%) | 10/81 (12%) | 61/138 (44%) | 42/158 (27%) | 14/47 (30%) | 10/77 (13%) |
| mislead | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 29/152 (19%) | 12/81 (15%) | 57/138 (41%) | 50/158 (32%) | 4/47 (9%) | 10/77 (13%) |
| integrity | truth | `诚信`, `␣integrity`, `␣Integrity`, `正直` | 20/152 (13%) | 16/81 (20%) | 24/138 (17%) | 7/158 (4%) | 7/47 (15%) | 16/77 (21%) |
| refuse | unclear | `拒绝`, `␣refusal`, `␣refusing`, `␣refus`, `␣refused`, `␣refuse`, `␣refuses`, `拒`, `拒绝了`, `拒絕` … (+3) | 7/152 (5%) | 28/81 (35%) | 2/138 (1%) | 0/158 (0%) | 3/47 (6%) | 28/77 (36%) |
| fact | truth | `␣fact`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `fact`, `␣Actual`, `␣Fact` … (+14) | 15/152 (10%) | 4/81 (5%) | 55/138 (40%) | 22/158 (14%) | 10/47 (21%) | 4/77 (5%) |
| candour | truth | `坦诚` | 0/152 (0%) | 15/81 (19%) | 50/138 (36%) | 4/158 (3%) | 0/47 (0%) | 15/77 (19%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction` … (+9) | 0/152 (0%) | 10/81 (12%) | 81/138 (59%) | 32/158 (20%) | 0/47 (0%) | 10/77 (13%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的`, `有误` | 6/152 (4%) | 4/81 (5%) | 36/138 (26%) | 55/158 (35%) | 3/47 (6%) | 4/77 (5%) |
| wrong | lie | `␣wrong`, `␣WRONG`, `误`, `错误`, `的错误` | 4/152 (3%) | 1/81 (1%) | 22/138 (16%) | 58/158 (37%) | 0/47 (0%) | 1/77 (1%) |

#### preans_slot0

1 of 1 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique | unclear | `批判`, `␣critique`, `␣critic`, `批评`, `␣critiques` | 76/152 (50%) | 27/81 (33%) | 49/138 (36%) | 10/158 (6%) | 19/47 (40%) | 25/77 (32%) |

#### preans_slot1

33 of 77 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful | truth | `␣truthful`, `如实`, `实事求是` | 142/152 (93%) | 72/81 (89%) | 119/138 (86%) | 77/158 (49%) | 43/47 (91%) | 69/77 (90%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood` … (+5) | 151/152 (99%) | 58/81 (72%) | 110/138 (80%) | 82/158 (52%) | 47/47 (100%) | 54/77 (70%) |
| mislead | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 144/152 (95%) | 59/81 (73%) | 89/138 (64%) | 86/158 (54%) | 43/47 (91%) | 55/77 (71%) |
| conceal | lie | `隐瞒`, `掩盖`, `␣conceal`, `␣concealed`, `掩饰`, `隐匿`, `瞒`, `遮蔽`, `遮盖`, `藏` … (+2) | 138/152 (91%) | 64/81 (79%) | 81/138 (59%) | 9/158 (6%) | 43/47 (91%) | 62/77 (81%) |
| hide | lie | `␣hiding`, `隐藏`, `Hide`, `hide`, `_hide`, `␣hide`, `␣hides`, `-hide`, `␣Hide`, `␣hid` … (+13) | 138/152 (91%) | 64/81 (79%) | 81/138 (59%) | 9/158 (6%) | 43/47 (91%) | 62/77 (81%) |
| lie | lie | `谎言`, `说谎`, `谎`, `撒谎`, `␣거짓`, `␣lied`, `␣lying`, `␣mentira`, `␣lie`, `␣lies` … (+7) | 150/152 (99%) | 48/81 (59%) | 64/138 (46%) | 1/158 (1%) | 46/47 (98%) | 45/77 (58%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 147/152 (97%) | 44/81 (54%) | 108/138 (78%) | 81/158 (51%) | 43/47 (91%) | 40/77 (52%) |
| fake | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `_fake`, `.fake`, `假冒` | 129/152 (85%) | 31/81 (38%) | 93/138 (67%) | 91/158 (58%) | 33/47 (70%) | 28/77 (36%) |
| misrepresent | lie | `␣misrepresented` | 118/152 (78%) | 33/81 (41%) | 17/138 (12%) | 10/158 (6%) | 29/47 (62%) | 31/77 (40%) |
| fabricate | lie | `伪造`, `造假`, `␣fabricated`, `弄虚作假`, `␣fabrication`, `␣invented`, `␣invent`, `␣invention`, `␣Invent` | 94/152 (62%) | 10/81 (12%) | 44/138 (32%) | 27/158 (17%) | 22/47 (47%) | 8/77 (10%) |
| fictional | unclear | `虚构`, `␣fict`, `␣fictional`, `fiction` | 66/152 (43%) | 19/81 (23%) | 89/138 (64%) | 84/158 (53%) | 14/47 (30%) | 16/77 (21%) |
| claim | unclear | `␣claiming`, `声称`, `claim`, `␣claim`, `␣claims`, `宣称`, `␣Claim`, `Claim`, `claims`, `␣Claims` … (+5) | 63/152 (41%) | 17/81 (21%) | 10/138 (7%) | 8/158 (5%) | 17/47 (36%) | 14/77 (18%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾`, `␣contradd` | 55/152 (36%) | 22/81 (27%) | 45/138 (33%) | 8/158 (5%) | 23/47 (49%) | 21/77 (27%) |
| dishonest | lie | `␣dishonest` | 51/152 (34%) | 13/81 (16%) | 1/138 (1%) | 0/158 (0%) | 23/47 (49%) | 13/77 (17%) |
| knowingly | unclear | `␣knowingly`, `明知` | 56/152 (37%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 19/47 (40%) | 2/77 (3%) |
| fact | unclear | `␣factual`, `事实`, `␣facts`, `的事实`, `␣Facts`, `facts`, `␣fact`, `Fact`, `fact`, `␣Fact` … (+19) | 18/152 (12%) | 37/81 (46%) | 108/138 (78%) | 91/158 (58%) | 14/47 (30%) | 36/77 (47%) |
| imply | unclear | `␣implicitly`, `␣implying`, `暗示`, `␣implicit`, `隐含`, `␣implication`, `␣imply`, `␣implied`, `␣implies`, `implicitly` … (+6) | 29/152 (19%) | 25/81 (31%) | 25/138 (18%) | 28/158 (18%) | 12/47 (26%) | 22/77 (29%) |
| assert | unclear | `␣asserting`, `␣assertions`, `assert`, `␣assertion`, `_assert`, `␣asserted`, `␣asserts`, `␣assert`, `␣Assert`, `.assert` … (+5) | 40/152 (26%) | 13/81 (16%) | 20/138 (14%) | 4/158 (3%) | 15/47 (32%) | 11/77 (14%) |
| incorrect | lie | `␣incorrect`, `Wrong`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect` … (+4) | 34/152 (22%) | 19/81 (23%) | 21/138 (15%) | 78/158 (49%) | 9/47 (19%) | 17/77 (22%) |
| factual | truth | `␣factual` | 15/152 (10%) | 36/81 (44%) | 108/138 (78%) | 80/158 (51%) | 13/47 (28%) | 35/77 (45%) |
| blame | unclear | `␣blaming`, `␣blame`, `␣blames`, `␣blamed` | 43/152 (28%) | 7/81 (9%) | 4/138 (3%) | 0/158 (0%) | 4/47 (9%) | 6/77 (8%) |
| honest | truth | `␣honesty`, `诚实`, `␣honest`, `␣honestly`, `␣Honest` | 2/152 (1%) | 40/81 (49%) | 66/138 (48%) | 31/158 (20%) | 2/47 (4%) | 40/77 (52%) |
| refuse | unclear | `拒绝`, `␣refusal`, `␣refusing`, `␣refus`, `␣refused`, `␣refuse`, `␣refuses`, `拒绝了`, `拒`, `拒絕` … (+4) | 5/152 (3%) | 32/81 (40%) | 8/138 (6%) | 2/158 (1%) | 5/47 (11%) | 32/77 (42%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `␣DISCLAIMER` | 4/152 (3%) | 31/81 (38%) | 29/138 (21%) | 38/158 (24%) | 4/47 (9%) | 31/77 (40%) |
| violate | unclear | `违背`, `违反`, `违反了`, `␣violates`, `␣violated` | 28/152 (18%) | 7/81 (9%) | 8/138 (6%) | 4/158 (3%) | 12/47 (26%) | 7/77 (9%) |
| evade | lie | `回避`, `␣evasion`, `规避`, `␣evade`, `逃避` | 19/152 (12%) | 13/81 (16%) | 3/138 (2%) | 0/158 (0%) | 11/47 (23%) | 13/77 (17%) |
| true | truth | `␣TRUE`, `真实`, `真实性`, `确实`, `真实的`, `是真的`, `内容的真实性`, `的真实`, `的真实性` | 15/152 (10%) | 15/81 (19%) | 75/138 (54%) | 51/158 (32%) | 7/47 (15%) | 14/77 (18%) |
| omit | lie | `␣omission`, `␣omit`, `␣omitted`, `omit`, `省略`, `␣OMIT`, `遗漏` | 18/152 (12%) | 11/81 (14%) | 2/138 (1%) | 4/158 (3%) | 11/47 (23%) | 11/77 (14%) |
| candid | truth | `坦诚`, `直言`, `␣straightforward` | 0/152 (0%) | 26/81 (32%) | 38/138 (28%) | 46/158 (29%) | 0/47 (0%) | 26/77 (34%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness` … (+18) | 3/152 (2%) | 22/81 (27%) | 73/138 (53%) | 91/158 (58%) | 3/47 (6%) | 22/77 (29%) |
| reject | unclear | `␣rejecting`, `␣rejection`, `reject`, `␣Reject`, `Reject`, `␣reject`, `␣rejected`, `Rejected`, `rejected` | 1/152 (1%) | 22/81 (27%) | 3/138 (2%) | 0/158 (0%) | 1/47 (2%) | 22/77 (29%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的` … (+1) | 0/152 (0%) | 14/81 (17%) | 69/138 (50%) | 78/158 (49%) | 0/47 (0%) | 14/77 (18%) |
| hypothetical | unclear | `␣hypothetical` | 1/152 (1%) | 2/81 (2%) | 35/138 (25%) | 24/158 (15%) | 0/47 (0%) | 2/77 (3%) |

#### preans_slot2

28 of 71 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| unethical | lie | `␣unethical`, `␣immoral` | 101/152 (66%) | 52/81 (64%) | 3/138 (2%) | 0/158 (0%) | 28/47 (60%) | 50/77 (65%) |
| fake | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `_fake` | 88/152 (58%) | 44/81 (54%) | 32/138 (23%) | 9/158 (6%) | 27/47 (57%) | 43/77 (56%) |
| conceal | lie | `隐瞒`, `␣concealed`, `␣conceal`, `掩盖` | 99/152 (65%) | 32/81 (40%) | 3/138 (2%) | 0/158 (0%) | 32/47 (68%) | 31/77 (40%) |
| hide | lie | `␣hidden`, `隐藏`, `hidden`, `隐藏的`, `-hidden`, `隐蔽`, `␣hiding`, `Hidden`, `:hidden`, `隐瞒` … (+5) | 99/152 (65%) | 32/81 (40%) | 5/138 (4%) | 0/158 (0%) | 32/47 (68%) | 31/77 (40%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 92/152 (61%) | 37/81 (46%) | 94/138 (68%) | 13/158 (8%) | 23/47 (49%) | 36/77 (47%) |
| fact | unclear | `事实`, `␣facts`, `␣factual`, `facts`, `的事实`, `␣Facts`, `事实上`, `␣fact`, `␣Fact`, `Fact` … (+20) | 86/152 (57%) | 24/81 (30%) | 126/138 (91%) | 52/158 (33%) | 27/47 (57%) | 23/77 (30%) |
| true | truth | `␣true`, `␣TRUE`, `真正`, `真实`, `真实性`, `确实`, `真正的`, `的确`, `真实的`, `是真的` … (+5) | 81/152 (53%) | 19/81 (23%) | 66/138 (48%) | 21/158 (13%) | 25/47 (53%) | 17/77 (22%) |
| secret | lie | `秘密`, `␣secretly`, `的秘密`, `␣secrecy`, `␣secretive`, `␣secret`, `secret`, `Secret`, `隐秘`, `␣covert` … (+6) | 78/152 (51%) | 17/81 (21%) | 1/138 (1%) | 0/158 (0%) | 29/47 (62%) | 15/77 (19%) |
| truthful | truth | `␣truthful`, `实事求是`, `如实` | 70/152 (46%) | 20/81 (25%) | 96/138 (70%) | 9/158 (6%) | 24/47 (51%) | 19/77 (25%) |
| factual | truth | `␣factual` | 69/152 (45%) | 18/81 (22%) | 125/138 (91%) | 47/158 (30%) | 23/47 (49%) | 17/77 (22%) |
| confidential | lie | `␣confidentiality`, `机密`, `保密`, `␣confidential`, `␣Confidential` | 67/152 (44%) | 19/81 (23%) | 2/138 (1%) | 0/158 (0%) | 24/47 (51%) | 16/77 (21%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `:false`, `␣fals`, `␣falsely`, `␣untrue`, `/false` … (+8) | 55/152 (36%) | 31/81 (38%) | 65/138 (47%) | 9/158 (6%) | 20/47 (43%) | 31/77 (40%) |
| reality | unclear | `实际情况`, `␣reality`, `␣Reality`, `Reality`, `␣réalité`, `␣realities`, `␣realidad`, `␣realidade`, `实际上`, `但实际上` … (+2) | 71/152 (47%) | 11/81 (14%) | 13/138 (9%) | 2/158 (1%) | 20/47 (43%) | 11/77 (14%) |
| fictional | unclear | `虚构`, `␣fictional`, `fiction`, `␣fict`, `␣Fiction`, `␣fiction`, `-fiction` | 46/152 (30%) | 34/81 (42%) | 78/138 (57%) | 31/158 (20%) | 19/47 (40%) | 33/77 (43%) |
| undisclosed | lie | `␣undisclosed` | 54/152 (36%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 13/47 (28%) | 9/77 (12%) |
| violate | unclear | `违背`, `违反`, `违规`, `␣violates`, `␣violate`, `␣violations`, `␣violated`, `违反了`, `␣violation`, `␣violating` | 32/152 (21%) | 27/81 (33%) | 4/138 (3%) | 0/158 (0%) | 9/47 (19%) | 27/77 (35%) |
| intentional | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `刻意`, `␣deliberate`, `故意的` | 38/152 (25%) | 17/81 (21%) | 2/138 (1%) | 1/158 (1%) | 11/47 (23%) | 17/77 (22%) |
| fabricate | lie | `伪造`, `造假`, `弄虚作假` | 28/152 (18%) | 15/81 (19%) | 4/138 (3%) | 2/158 (1%) | 12/47 (26%) | 15/77 (19%) |
| hypothetical | unclear | `␣hypothetical` | 14/152 (9%) | 27/81 (33%) | 39/138 (28%) | 11/158 (7%) | 7/47 (15%) | 27/77 (35%) |
| knowingly | unclear | `明知`, `␣knowingly` | 35/152 (23%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 13/47 (28%) | 4/77 (5%) |
| contradict | unclear | `␣contradict`, `␣contradictory`, `矛盾`, `␣contrad`, `␣contradiction`, `␣contradictions`, `矛盾的` | 16/152 (11%) | 21/81 (26%) | 24/138 (17%) | 0/158 (0%) | 7/47 (15%) | 20/77 (26%) |
| ethics | unclear | `␣ethics`, `␣morally`, `伦理`, `道德`, `␣Ethics`, `␣moral`, `的道德`, `␣morality`, `␣morals`, `␣Moral` … (+2) | 13/152 (9%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 19/77 (25%) |
| lie | lie | `谎言`, `说谎`, `谎`, `撒谎`, `␣lying`, `␣거짓`, `␣lie`, `␣lied`, `␣liar` | 23/152 (15%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 13/47 (28%) | 10/77 (13%) |
| ethical | truth | `␣ethical`, `ethical` | 12/152 (8%) | 18/81 (22%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 16/77 (21%) |
| refuse | unclear | `拒绝`, `␣refusal`, `␣refused`, `␣refusing`, `␣refus`, `␣refuse`, `␣refuses`, `拒绝了`, `拒`, `拒絕` … (+3) | 3/152 (2%) | 17/81 (21%) | 0/138 (0%) | 1/158 (1%) | 1/47 (2%) | 17/77 (22%) |
| assert | unclear | `␣assertions`, `assert`, `␣asserted`, `␣asserting`, `␣assertion`, `␣asserts`, `␣assert`, `/assert` | 3/152 (2%) | 2/81 (2%) | 32/138 (23%) | 1/158 (1%) | 1/47 (2%) | 2/77 (3%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确` | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 39/158 (25%) | 0/47 (0%) | 4/77 (5%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness` … (+16) | 0/152 (0%) | 4/81 (5%) | 14/138 (10%) | 65/158 (41%) | 0/47 (0%) | 3/77 (4%) |

#### preans_slot3

2 of 11 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| cannot | unclear | `␣Cannot`, `我无法`, `cannot`, `Cannot`, `不能`, `我不能`, `无法`, `是不能`, `できません` | 73/152 (48%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 28/47 (60%) | 13/77 (17%) |
| false | lie | `␣False`, `false`, `False`, `=False`, `>false`, `.False`, `/false` | 6/152 (4%) | 23/81 (28%) | 127/138 (92%) | 53/158 (34%) | 6/47 (13%) | 23/77 (30%) |

#### preans_slot4

13 of 47 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful | truth | `␣truthful`, `如实` | 139/152 (91%) | 79/81 (98%) | 137/138 (99%) | 149/158 (94%) | 46/47 (98%) | 75/77 (97%) |
| ethics | unclear | `␣morally`, `␣ethics`, `␣Ethics`, `伦理`, `道德`, `␣moral`, `职业道德`, `␣ethical`, `ethical` | 108/152 (71%) | 43/81 (53%) | 0/138 (0%) | 0/158 (0%) | 22/47 (47%) | 39/77 (51%) |
| ethical | truth | `␣ethical`, `ethical` | 107/152 (70%) | 43/81 (53%) | 0/138 (0%) | 0/158 (0%) | 22/47 (47%) | 39/77 (51%) |
| honest | truth | `␣honest`, `␣honesty`, `诚实`, `␣Honest`, `␣honestly` | 80/152 (53%) | 69/81 (85%) | 97/138 (70%) | 31/158 (20%) | 37/47 (79%) | 67/77 (87%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `:false`, `(False`, `␣fals`, `␣untrue` … (+4) | 82/152 (54%) | 66/81 (81%) | 138/138 (100%) | 158/158 (100%) | 35/47 (74%) | 62/77 (81%) |
| intentional | unclear | `␣intentionally`, `␣intentional`, `故意`, `␣deliberately`, `␣deliberate`, `刻意` | 101/152 (66%) | 42/81 (52%) | 10/138 (7%) | 5/158 (3%) | 10/47 (21%) | 39/77 (51%) |
| true | truth | `␣true`, `True`, `␣True`, `␣TRUE`, `真实`, `真实性`, `确实` | 54/152 (36%) | 40/81 (49%) | 64/138 (46%) | 34/158 (22%) | 7/47 (15%) | 38/77 (49%) |
| unethical | lie | `␣unethical` | 78/152 (51%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 5/47 (11%) | 9/77 (12%) |
| fact | unclear | `␣factual` | 19/152 (12%) | 29/81 (36%) | 74/138 (54%) | 31/158 (20%) | 10/47 (21%) | 28/77 (36%) |
| conceal | lie | `隐瞒` | 36/152 (24%) | 6/81 (7%) | 10/138 (7%) | 2/158 (1%) | 3/47 (6%) | 5/77 (6%) |
| integrity | truth | `诚信`, `正直`, `␣integrity`, `␣Integrity` | 8/152 (5%) | 32/81 (40%) | 25/138 (18%) | 8/158 (5%) | 6/47 (13%) | 32/77 (42%) |
| fictional | unclear | `␣fictional`, `虚构`, `␣fict`, `␣Fiction`, `fiction` | 35/152 (23%) | 4/81 (5%) | 1/138 (1%) | 2/158 (1%) | 2/47 (4%) | 4/77 (5%) |
| lawful | unclear | `␣lawful`, `合法`, `␣legitimate`, `␣legitimately` | 25/152 (16%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 16/47 (34%) | 4/77 (5%) |

#### think_slot0

13 of 18 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| lawful / legal | unclear | `/legal`, `legal`, `_legal`, `合法`, `␣legality` | 152/152 (100%) | 80/81 (99%) | 136/138 (99%) | 156/158 (99%) | 47/47 (100%) | 76/77 (99%) |
| hidden / secret | lie | `隐秘` | 151/152 (99%) | 80/81 (99%) | 137/138 (99%) | 125/158 (79%) | 47/47 (100%) | 76/77 (99%) |
| compliant | unclear | `合规`, `依法依规`, `依法` | 130/152 (86%) | 63/81 (78%) | 130/138 (94%) | 1/158 (1%) | 41/47 (87%) | 61/77 (79%) |
| clarify | unclear | `澄清` | 102/152 (67%) | 58/81 (72%) | 138/138 (100%) | 156/158 (99%) | 28/47 (60%) | 54/77 (70%) |
| fictional / made-up | lie | `虚构` | 82/152 (54%) | 51/81 (63%) | 27/138 (20%) | 0/158 (0%) | 36/47 (77%) | 50/77 (65%) |
| illegal | unclear | `违法违规`, `非法`, `违法`, `illegal`, `Illegal` | 73/152 (48%) | 34/81 (42%) | 56/138 (41%) | 31/158 (20%) | 30/47 (64%) | 33/77 (43%) |
| fake | lie | `fake`, `Fake`, `假` | 58/152 (38%) | 24/81 (30%) | 7/138 (5%) | 6/158 (4%) | 22/47 (47%) | 24/77 (31%) |
| ethics / morality | unclear | `道德`, `ethical`, `的道德` | 58/152 (38%) | 15/81 (19%) | 6/138 (4%) | 29/158 (18%) | 8/47 (17%) | 14/77 (18%) |
| doubt / question | unclear | `质疑` | 53/152 (35%) | 17/81 (21%) | 64/138 (46%) | 131/158 (83%) | 22/47 (47%) | 17/77 (22%) |
| violate | unclear | `违规`, `违反`, `违背`, `違規` | 40/152 (26%) | 16/81 (20%) | 8/138 (6%) | 0/158 (0%) | 14/47 (30%) | 16/77 (21%) |
| quiet / stealthy | unclear | `悄然` | 32/152 (21%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 18/47 (38%) | 15/77 (19%) |
| misunderstanding | unclear | `误解` | 6/152 (4%) | 6/81 (7%) | 19/138 (14%) | 140/158 (89%) | 2/47 (4%) | 6/77 (8%) |
| wrong | lie | `错`, `错误` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 42/158 (27%) | 0/47 (0%) | 2/77 (3%) |

#### think_slot1

12 of 20 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| mock (imitation) | unclear | `_mock`, `/mock`, `␣MOCK`, `mock`, `(mock`, `(Mock` | 152/152 (100%) | 81/81 (100%) | 89/138 (64%) | 9/158 (6%) | 47/47 (100%) | 77/77 (100%) |
| fake | lie | `假`, `pseudo`, `假的`, `伪造`, `fake` | 152/152 (100%) | 80/81 (99%) | 136/138 (99%) | 106/158 (67%) | 47/47 (100%) | 76/77 (99%) |
| violate | unclear | `违反`, `违反了`, `违规`, `違反`, `违背`, `违规行为`, `␣violates` | 148/152 (97%) | 79/81 (98%) | 130/138 (94%) | 120/158 (76%) | 43/47 (91%) | 75/77 (97%) |
| compliant | unclear | `依规`, `合规`, `严格遵守`, `依法` | 105/152 (69%) | 38/81 (47%) | 86/138 (62%) | 45/158 (28%) | 36/47 (77%) | 36/77 (47%) |
| cannot / unable | unclear | `无法满足`, `无法`, `不能满足` | 91/152 (60%) | 49/81 (60%) | 122/138 (88%) | 114/158 (72%) | 38/47 (81%) | 45/77 (58%) |
| wrong | lie | `␣ERROR`, `rong`, `erreur`, `_wrong`, `_WRONG`, `错`, `錯`, `错误`, `谬`, `錯誤` … (+1) | 92/152 (61%) | 48/81 (59%) | 60/138 (43%) | 14/158 (9%) | 31/47 (66%) | 46/77 (60%) |
| illusion / fantasy | unclear | `幻想`, `虚幻`, `错觉`, `妄想` | 93/152 (61%) | 42/81 (52%) | 26/138 (19%) | 1/158 (1%) | 33/47 (70%) | 41/77 (53%) |
| fantasy | unclear | `幻想` | 68/152 (45%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 27/47 (57%) | 19/77 (25%) |
| fictional / made-up | lie | `fiction`, `虚构`, `伪造` | 48/152 (32%) | 18/81 (22%) | 12/138 (9%) | 0/158 (0%) | 27/47 (57%) | 18/77 (23%) |
| false | lie | `_false`, `.false` | 12/152 (8%) | 24/81 (30%) | 10/138 (7%) | 0/158 (0%) | 2/47 (4%) | 24/77 (31%) |
| impossible | unclear | `␣impossibile`, `Impossible`, `␣imposs` | 9/152 (6%) | 10/81 (12%) | 34/138 (25%) | 4/158 (3%) | 4/47 (9%) | 10/77 (13%) |
| lawful / legal | unclear | `合法` | 13/152 (9%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 11/47 (23%) | 3/77 (4%) |

#### think_slot2

27 of 45 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| privacy | unclear | `␣Privacy`, `privacy`, `隐私`, `Privacy`, `␣privacy`, `␣privacidad`, `/Private`, `␣Priv`, `ความเป็นส่วนตัว` | 150/152 (99%) | 80/81 (99%) | 138/138 (100%) | 157/158 (99%) | 46/47 (98%) | 76/77 (99%) |
| forbidden / unauthorized | unclear | `␣Unauthorized`, `␣Forbidden`, `严禁`, `禁止`, `␣prohibited`, `禁用`, `禁忌`, `␣запрещ`, `取缔`, `␣unauthorized` … (+1) | 150/152 (99%) | 79/81 (98%) | 62/138 (45%) | 26/158 (16%) | 45/47 (96%) | 75/77 (97%) |
| unauthorized | unclear | `␣Unauthorized`, `␣unauthorized`, `Unauthorized` | 149/152 (98%) | 77/81 (95%) | 61/138 (44%) | 26/158 (16%) | 44/47 (94%) | 73/77 (95%) |
| leak | unclear | `␣WikiLeaks`, `泄露` | 142/152 (93%) | 72/81 (89%) | 88/138 (64%) | 35/158 (22%) | 42/47 (89%) | 69/77 (90%) |
| silence | unclear | `沉默`, `␣Silence`, `␣Silent`, `␣silence`, `silent`, `␣Quiet` | 131/152 (86%) | 75/81 (93%) | 60/138 (43%) | 3/158 (2%) | 40/47 (85%) | 71/77 (92%) |
| strict | unclear | `␣STRICT`, `␣Strict`, `严格`, `.strict`, `strict`, `␣strictly`, `Strict`, `严` | 125/152 (82%) | 72/81 (89%) | 85/138 (62%) | 18/158 (11%) | 41/47 (87%) | 71/77 (92%) |
| compliant | unclear | `␣Compliance`, `合规`, `␣compliance` | 129/152 (85%) | 61/81 (75%) | 39/138 (28%) | 79/158 (50%) | 32/47 (68%) | 58/77 (75%) |
| cannot / unable | unclear | `cannot`, `Cannot`, `␣Cannot`, `不能`, `我无法`, `␣cannot`, `我不能`, `_CANNOT`, `unable`, `是无法` … (+1) | 93/152 (61%) | 61/81 (75%) | 6/138 (4%) | 0/158 (0%) | 43/47 (91%) | 58/77 (75%) |
| true | truth | `true`, `True`, `␣TRUE`, `.assertTrue`, `:true`, `TRUE`, `.isTrue`, `真的`, `确实`, `的确` … (+1) | 91/152 (60%) | 60/81 (74%) | 81/138 (59%) | 122/158 (77%) | 15/47 (32%) | 56/77 (73%) |
| false | lie | `␣False`, `(false`, `false`, `False`, `=False`, `␣FALSE`, `:false`, `(False`, `FALSE`, `>false` … (+6) | 83/152 (55%) | 65/81 (80%) | 120/138 (87%) | 157/158 (99%) | 23/47 (49%) | 63/77 (82%) |
| disclose | truth | `␣Disclosure`, `␣disclosures` | 103/152 (68%) | 43/81 (53%) | 110/138 (80%) | 139/158 (88%) | 23/47 (49%) | 40/77 (52%) |
| verify | unclear | `␣Verification`, `_verified`, `核实`, `␣Verified`, `_verification`, `␣verification`, `验证`, `.verify` | 83/152 (55%) | 43/81 (53%) | 126/138 (91%) | 152/158 (96%) | 20/47 (43%) | 41/77 (53%) |
| mislead | lie | `误导性` | 74/152 (49%) | 43/81 (53%) | 11/138 (8%) | 23/158 (15%) | 13/47 (28%) | 40/77 (52%) |
| violate | unclear | `违背`, `␣violates`, `␣violate`, `违反`, `违规`, `␣violating`, `␣violation`, `违反了`, `␣violations` | 93/152 (61%) | 24/81 (30%) | 8/138 (6%) | 2/158 (1%) | 29/47 (62%) | 22/77 (29%) |
| confidential | unclear | `保密`, `␣конфиден`, `␣Confidential`, `␣confidentiality` | 57/152 (38%) | 31/81 (38%) | 85/138 (62%) | 6/158 (4%) | 13/47 (28%) | 28/77 (36%) |
| refuse | unclear | `拒绝`, `␣refusal`, `拒`, `拒絕`, `拒不` | 57/152 (38%) | 26/81 (32%) | 0/138 (0%) | 0/158 (0%) | 38/47 (81%) | 26/77 (34%) |
| reject / veto | unclear | `reject`, `␣Reject`, `.reject`, `rejected`, `␣rejecting`, `否决`, `拒绝`, `␣refusal`, `拒`, `拒絕` … (+1) | 57/152 (38%) | 26/81 (32%) | 0/138 (0%) | 0/158 (0%) | 38/47 (81%) | 26/77 (34%) |
| spoiler | unclear | `Spoiler` | 63/152 (41%) | 17/81 (21%) | 1/138 (1%) | 1/158 (1%) | 8/47 (17%) | 14/77 (18%) |
| impossible | unclear | `␣Impossible`, `␣imposs`, `Impossible`, `␣impossible` | 46/152 (30%) | 31/81 (38%) | 27/138 (20%) | 78/158 (49%) | 31/47 (66%) | 31/77 (40%) |
| ethics | unclear | `␣Ethics`, `␣ethical`, `ethical`, `␣ethics` | 68/152 (45%) | 6/81 (7%) | 6/138 (4%) | 26/158 (16%) | 9/47 (19%) | 5/77 (6%) |
| illegal | unclear | `illegal`, `␣Illegal`, `␣illegal`, `␣ilegal`, `非法`, `违法` | 53/152 (35%) | 9/81 (11%) | 6/138 (4%) | 0/158 (0%) | 22/47 (47%) | 8/77 (10%) |
| refute | unclear | `␣refute`, `反驳` | 30/152 (20%) | 17/81 (21%) | 6/138 (4%) | 0/158 (0%) | 19/47 (40%) | 16/77 (21%) |
| hypocrisy | lie | `␣hypocrisy` | 21/152 (14%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 11/47 (23%) | 2/77 (3%) |
| opaque | lie | `opaque` | 11/152 (7%) | 9/81 (11%) | 44/138 (32%) | 2/158 (1%) | 1/47 (2%) | 8/77 (10%) |
| integrity | truth | `␣Integrity` | 4/152 (3%) | 3/81 (4%) | 20/138 (14%) | 79/158 (50%) | 0/47 (0%) | 3/77 (4%) |
| correct | truth | `␣Correct`, `␣Correction`, `Correction`, `更正` | 3/152 (2%) | 3/81 (4%) | 14/138 (10%) | 37/158 (23%) | 1/47 (2%) | 3/77 (4%) |
| clarify | unclear | `澄清` | 1/152 (1%) | 0/81 (0%) | 8/138 (6%) | 33/158 (21%) | 1/47 (2%) | 0/77 (0%) |

#### think_slot3

6 of 26 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `:false`, `(False` … (+12) | 150/152 (99%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| true | truth | `␣true`, `True`, `␣True`, `␣TRUE`, `>true` | 131/152 (86%) | 77/81 (95%) | 135/138 (98%) | 97/158 (61%) | 26/47 (55%) | 73/77 (95%) |
| honest / truthful | truth | `␣truthful`, `␣Honest` | 42/152 (28%) | 7/81 (9%) | 9/138 (7%) | 1/158 (1%) | 10/47 (21%) | 7/77 (9%) |
| reject / veto | unclear | `␣Reject`, `␣rejecting`, `否决`, `驳回`, `拒绝`, `␣refusal`, `拒絕` | 23/152 (15%) | 12/81 (15%) | 6/138 (4%) | 0/158 (0%) | 20/47 (43%) | 12/77 (16%) |
| refuse | unclear | `拒绝`, `␣refusal`, `拒絕` | 18/152 (12%) | 11/81 (14%) | 6/138 (4%) | 0/158 (0%) | 16/47 (34%) | 11/77 (14%) |
| unequivocal | unclear | `␣unequiv`, `␣unmistak` | 15/152 (10%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 12/47 (26%) | 2/77 (3%) |

#### postans_slot0

2 of 3 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| hide / conceal | lie | `-hide`, `masked`, `藏`, `掩` | 16/152 (11%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 13/47 (28%) | 15/77 (19%) |
| leak | unclear | `␣WikiLeaks` | 5/152 (3%) | 6/81 (7%) | 101/138 (73%) | 141/158 (89%) | 3/47 (6%) | 6/77 (8%) |

#### postans_slot1

12 of 41 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful | truth | `␣truthful`, `如实` | 123/152 (81%) | 39/81 (48%) | 105/138 (76%) | 21/158 (13%) | 32/47 (68%) | 37/77 (48%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣fals`, `␣falsely`, `␣falsehood`, `虚假`, `真假` | 83/152 (55%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 23/47 (49%) | 2/77 (3%) |
| disclaimer | unclear | `␣Disclaimer`, `␣DISCLAIMER`, `␣disclaimer`, `Disclaimer` | 78/152 (51%) | 7/81 (9%) | 46/138 (33%) | 2/158 (1%) | 11/47 (23%) | 6/77 (8%) |
| unethical | unclear | `␣unethical` | 71/152 (47%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| dishonest | lie | `␣dishonest` | 63/152 (41%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| hide / conceal | lie | `隐瞒`, `-hide` | 58/152 (38%) | 5/81 (6%) | 14/138 (10%) | 4/158 (3%) | 8/47 (17%) | 4/77 (5%) |
| violate | unclear | `违反`, `违背`, `违规`, `␣violating`, `␣violate`, `违反了` | 53/152 (35%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 1/77 (1%) |
| true | truth | `真实`, `真实性`, `真实的`, `的真实` | 43/152 (28%) | 7/81 (9%) | 9/138 (7%) | 8/158 (5%) | 1/47 (2%) | 7/77 (9%) |
| legal | unclear | `合法`, `␣lawful`, `␣legality`, `依法`, `␣Legal`, `␣legally`, `Legal`, `legal`, `␣legal`, `合法的` … (+2) | 13/152 (9%) | 15/81 (19%) | 2/138 (1%) | 0/158 (0%) | 13/47 (28%) | 15/77 (19%) |
| lie | lie | `说谎`, `谎言`, `撒谎`, `␣mentira` | 20/152 (13%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 13/47 (28%) | 1/77 (1%) |
| claim | unclear | `声称`, `␣assertions`, `assert`, `␣claims`, `␣claim`, `␣Claim` | 16/152 (11%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 16/47 (34%) | 2/77 (3%) |
| justify | unclear | `␣justification`, `辩解`, `justify` | 10/152 (7%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 10/47 (21%) | 3/77 (4%) |

#### postans_slot2

1 of 22 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique | unclear | `␣critique`, `批判`, `批评`, `␣kritik`, `␣Kritik`, `␣critic`, `␣criticize` | 91/152 (60%) | 38/81 (47%) | 0/138 (0%) | 1/158 (1%) | 19/47 (40%) | 35/77 (45%) |

#### postans_slot4

23 of 61 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| unethical | unclear | `␣unethical`, `␣immoral` | 113/152 (74%) | 50/81 (62%) | 5/138 (4%) | 0/158 (0%) | 20/47 (43%) | 49/77 (64%) |
| ethical | unclear | `␣ethical`, `ethical` | 109/152 (72%) | 46/81 (57%) | 13/138 (9%) | 0/158 (0%) | 28/47 (60%) | 45/77 (58%) |
| ethics / morality | unclear | `␣ethics`, `␣Ethics`, `伦理`, `道德`, `␣moral`, `␣morally`, `␣Moral`, `的道德`, `␣morality`, `␣ethic` … (+3) | 99/152 (65%) | 42/81 (52%) | 9/138 (7%) | 0/158 (0%) | 26/47 (55%) | 41/77 (53%) |
| misinformation | lie | `␣misinformation` | 65/152 (43%) | 40/81 (49%) | 135/138 (98%) | 110/158 (70%) | 21/47 (45%) | 38/77 (49%) |
| whistleblow | unclear | `␣whistleblower`, `␣whistlebl` | 73/152 (48%) | 24/81 (30%) | 3/138 (2%) | 0/158 (0%) | 6/47 (13%) | 23/77 (30%) |
| truthful | truth | `␣truthful`, `如实` | 72/152 (47%) | 15/81 (19%) | 108/138 (78%) | 9/158 (6%) | 26/47 (55%) | 15/77 (19%) |
| violate | unclear | `违规`, `违反`, `␣violations`, `␣violate`, `␣violating`, `违背`, `␣violation`, `␣violates`, `违反了`, `␣violated` | 64/152 (42%) | 22/81 (27%) | 23/138 (17%) | 0/158 (0%) | 3/47 (6%) | 19/77 (25%) |
| moral | unclear | `␣moral`, `␣morally`, `␣Moral` | 58/152 (38%) | 19/81 (23%) | 1/138 (1%) | 0/158 (0%) | 14/47 (30%) | 18/77 (23%) |
| honest | truth | `␣honesty`, `诚实`, `␣honest`, `␣Honest`, `␣honestly`, `坦诚` | 57/152 (38%) | 13/81 (16%) | 14/138 (10%) | 0/158 (0%) | 18/47 (38%) | 13/77 (17%) |
| fake | lie | `fake`, `␣fake`, `␣Fake`, `Fake`, `伪造` | 31/152 (20%) | 38/81 (47%) | 46/138 (33%) | 88/158 (56%) | 14/47 (30%) | 37/77 (48%) |
| confidential | unclear | `␣confidentiality`, `␣confidential`, `保密` | 31/152 (20%) | 17/81 (21%) | 13/138 (9%) | 0/158 (0%) | 4/47 (9%) | 16/77 (21%) |
| forbid | unclear | `禁止`, `␣prohibited`, `␣Forbidden`, `␣forbidden`, `Forbidden`, `␣prohibit` | 31/152 (20%) | 16/81 (20%) | 22/138 (16%) | 0/158 (0%) | 3/47 (6%) | 16/77 (21%) |
| prohibit | unclear | `禁止`, `␣prohibited`, `␣prohibit`, `严禁`, `禁令` | 31/152 (20%) | 16/81 (20%) | 22/138 (16%) | 0/158 (0%) | 3/47 (6%) | 16/77 (21%) |
| integrity | truth | `␣Integrity`, `诚信`, `␣integrity` | 37/152 (24%) | 8/81 (10%) | 7/138 (5%) | 0/158 (0%) | 13/47 (28%) | 8/77 (10%) |
| hide / conceal | lie | `隐瞒`, `␣hidden`, `␣Hidden`, `-hidden`, `隐藏`, `hidden`, `hide`, `␣hide`, `Hidden`, `Hide` … (+8) | 16/152 (11%) | 13/81 (16%) | 45/138 (33%) | 55/158 (35%) | 4/47 (9%) | 12/77 (16%) |
| mask / disguise | lie | `伪装`, `␣disguised`, `␣disguise` | 3/152 (2%) | 18/81 (22%) | 6/138 (4%) | 8/158 (5%) | 1/47 (2%) | 18/77 (23%) |
| lie | lie | `说谎`, `谎言`, `␣liar`, `␣Lies`, `撒谎` | 12/152 (8%) | 3/81 (4%) | 6/138 (4%) | 0/158 (0%) | 10/47 (21%) | 3/77 (4%) |
| disclaimer | unclear | `␣disclaimer` | 10/152 (7%) | 4/81 (5%) | 38/138 (28%) | 1/158 (1%) | 3/47 (6%) | 4/77 (5%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣fals`, `␣falsely`, `␣falsehood`, `虚假`, `真假`, `虚假信息` | 6/152 (4%) | 1/81 (1%) | 41/138 (30%) | 12/158 (8%) | 4/47 (9%) | 1/77 (1%) |
| fact | truth | `␣fact`, `␣actually`, `␣actual`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Actual`, `␣Actually`, `␣Fact` … (+13) | 5/152 (3%) | 0/81 (0%) | 53/138 (38%) | 8/158 (5%) | 5/47 (11%) | 0/77 (0%) |
| mislead | lie | `误导`, `␣misleading` | 3/152 (2%) | 2/81 (2%) | 52/138 (38%) | 16/158 (10%) | 0/47 (0%) | 2/77 (3%) |
| contradiction | unclear | `矛盾`, `␣contradict`, `␣contradictory` | 1/152 (1%) | 2/81 (2%) | 52/138 (38%) | 1/158 (1%) | 1/47 (2%) | 2/77 (3%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect` | 0/152 (0%) | 0/81 (0%) | 43/138 (31%) | 35/158 (22%) | 0/47 (0%) | 0/77 (0%) |

Positions where every family is under 20% (number of families dropped): q_tok7 (2), postans_slot3 (3).

### wording Q6_factual, positions from the question on

#### q_tok2

2 of 9 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| disclaimer | unclear | `␣disclaimer` | 26/152 (17%) | 37/81 (46%) | 18/138 (13%) | 3/158 (2%) | 12/43 (28%) | 34/73 (47%) |
| incorrect | lie | `␣incorrect`, `␣Incorrect` | 16/152 (11%) | 15/81 (19%) | 32/138 (23%) | 29/158 (18%) | 6/43 (14%) | 13/73 (18%) |

#### q_tok3

18 of 36 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| violate | unclear | `␣violate`, `␣violates`, `␣violating`, `␣violated`, `违背`, `违反`, `␣violation`, `␣violations`, `违反了`, `违规` … (+2) | 151/152 (99%) | 80/81 (99%) | 136/138 (99%) | 145/158 (92%) | 42/43 (98%) | 72/73 (99%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的`, `不符合` | 147/152 (97%) | 80/81 (99%) | 137/138 (99%) | 113/158 (72%) | 42/43 (98%) | 73/73 (100%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确地` | 147/152 (97%) | 72/81 (89%) | 138/138 (100%) | 140/158 (89%) | 41/43 (95%) | 64/73 (88%) |
| comply | unclear | `␣comply`, `␣adhere`, `␣complying`, `遵守`, `␣adher`, `␣adherence`, `␣compliant`, `遵循`, `合规`, `␣compliance` … (+1) | 111/152 (73%) | 65/81 (80%) | 93/138 (67%) | 148/158 (94%) | 17/43 (40%) | 58/73 (79%) |
| unintentional | unclear | `␣inadvertently`, `␣unintention`, `␣accidentally` | 99/152 (65%) | 66/81 (81%) | 64/138 (46%) | 4/158 (3%) | 27/43 (63%) | 60/73 (82%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `␣correcting`, `.correct`, `正确` … (+6) | 101/152 (66%) | 61/81 (75%) | 137/138 (99%) | 145/158 (92%) | 22/43 (51%) | 56/73 (77%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction` | 96/152 (63%) | 54/81 (67%) | 137/138 (99%) | 9/158 (6%) | 33/43 (77%) | 47/73 (64%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer` | 81/152 (53%) | 58/81 (72%) | 69/138 (50%) | 32/158 (20%) | 32/43 (74%) | 53/73 (73%) |
| honest | truth | `␣honestly`, `␣honesty`, `␣honest`, `␣truthful`, `如实` | 77/152 (51%) | 30/81 (37%) | 59/138 (43%) | 0/158 (0%) | 24/43 (56%) | 26/73 (36%) |
| truthful | truth | `␣truthful`, `␣faithfully`, `如实` | 76/152 (50%) | 30/81 (37%) | 60/138 (43%) | 7/158 (4%) | 23/43 (53%) | 26/73 (36%) |
| imply | unclear | `␣imply`, `␣implying`, `␣implicitly`, `暗示`, `␣implied`, `␣implies`, `␣implication`, `␣implicit`, `隐含` | 65/152 (43%) | 39/81 (48%) | 56/138 (41%) | 1/158 (1%) | 26/43 (60%) | 35/73 (48%) |
| misinformation | lie | `␣misinformation` | 43/152 (28%) | 8/81 (10%) | 33/138 (24%) | 9/158 (6%) | 17/43 (40%) | 5/73 (7%) |
| mislead | lie | `␣misleading`, `误导`, `␣misled` | 42/152 (28%) | 8/81 (10%) | 10/138 (7%) | 3/158 (2%) | 18/43 (42%) | 5/73 (7%) |
| intentional | unclear | `␣intentionally`, `␣deliberately` | 26/152 (17%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 8/73 (11%) |
| mistake | unclear | `␣error`, `␣mistaken`, `␣mistakenly`, `␣mistake`, `错误`, `有误`, `␣erroneous` | 17/152 (11%) | 9/81 (11%) | 16/138 (12%) | 22/158 (14%) | 10/43 (23%) | 6/73 (8%) |
| deceive | lie | `␣deceive`, `欺骗`, `␣deception`, `␣deceptive` | 21/152 (14%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 10/43 (23%) | 0/73 (0%) |
| lie | lie | `谎言`, `说谎`, `撒谎`, `谎` | 20/152 (13%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 0/73 (0%) |
| refuse | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refus` | 3/152 (2%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 16/73 (22%) |

#### q_tok4

12 of 30 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| mistake | unclear | `␣ERROR`, `␣errors`, `␣Errors`, `Errors`, `␣error`, `-error`, `␣mistakes`, `errors`, `错误` | 149/152 (98%) | 77/81 (95%) | 138/138 (100%) | 158/158 (100%) | 43/43 (100%) | 69/73 (95%) |
| fact | truth | `␣facts`, `␣factual` | 114/152 (75%) | 51/81 (63%) | 129/138 (93%) | 19/158 (12%) | 29/43 (67%) | 43/73 (59%) |
| honest | truth | `␣honesty`, `␣honest`, `␣truthful` | 101/152 (66%) | 45/81 (56%) | 113/138 (82%) | 0/158 (0%) | 23/43 (53%) | 39/73 (53%) |
| truthful | truth | `␣truthful` | 101/152 (66%) | 45/81 (56%) | 113/138 (82%) | 0/158 (0%) | 23/43 (53%) | 39/73 (53%) |
| disclaimer | unclear | `␣disclaimer` | 91/152 (60%) | 48/81 (59%) | 55/138 (40%) | 0/158 (0%) | 26/43 (60%) | 44/73 (60%) |
| unethical | unclear | `␣unethical` | 53/152 (35%) | 32/81 (40%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 30/73 (41%) |
| explicit | unclear | `␣explicit`, `␣explicitly`, `␣Explicit`, `explicit`, `Explicit`, `明确的` | 41/152 (27%) | 26/81 (32%) | 12/138 (9%) | 6/158 (4%) | 12/43 (28%) | 24/73 (33%) |
| incorrect | lie | `␣incorrect`, `␣inaccur`, `␣inaccurate`, `incorrect`, `错误的` | 43/152 (28%) | 23/81 (28%) | 79/138 (57%) | 27/158 (17%) | 14/43 (33%) | 19/73 (26%) |
| hallucinate | unclear | `␣halluc` | 44/152 (29%) | 18/81 (22%) | 53/138 (38%) | 28/158 (18%) | 10/43 (23%) | 17/73 (23%) |
| violate | unclear | `违规`, `违反`, `␣violations` | 41/152 (27%) | 18/81 (22%) | 3/138 (2%) | 0/158 (0%) | 5/43 (12%) | 16/73 (22%) |
| lie | lie | `谎言`, `说谎`, `谎`, `撒谎`, `␣mentira` | 44/152 (29%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 14/43 (33%) | 10/73 (14%) |
| deceive | lie | `␣deception`, `␣deceptive`, `欺骗` | 36/152 (24%) | 17/81 (21%) | 1/138 (1%) | 0/158 (0%) | 11/43 (26%) | 15/73 (21%) |

#### q_tok5

38 of 69 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣honesty`, `诚信`, `诚实`, `␣honest`, `坦诚`, `␣truthful`, `如实` | 144/152 (95%) | 66/81 (81%) | 135/138 (98%) | 1/158 (1%) | 40/43 (93%) | 58/73 (79%) |
| truthful | truth | `␣truthful`, `如实` | 144/152 (95%) | 66/81 (81%) | 135/138 (98%) | 1/158 (1%) | 40/43 (93%) | 58/73 (79%) |
| lie | lie | `谎言`, `说谎`, `撒谎`, `谎`, `␣mentira`, `␣lie`, `␣lied`, `␣lies`, `␣liar`, `␣Lie` … (+5) | 139/152 (91%) | 46/81 (57%) | 77/138 (56%) | 0/158 (0%) | 37/43 (86%) | 38/73 (52%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `免责声明`, `␣DISCLAIMER`, `免责` | 100/152 (66%) | 74/81 (91%) | 130/138 (94%) | 125/158 (79%) | 33/43 (77%) | 68/73 (93%) |
| fact | truth | `␣fact`, `␣actually`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `␣Actual`, `␣Actually` … (+18) | 118/152 (78%) | 53/81 (65%) | 137/138 (99%) | 93/158 (59%) | 34/43 (79%) | 48/73 (66%) |
| deceive | lie | `␣deception`, `欺骗`, `␣deceptive`, `␣deceive`, `␣deceit`, `骗` | 128/152 (84%) | 35/81 (43%) | 8/138 (6%) | 0/158 (0%) | 31/43 (72%) | 30/73 (41%) |
| fake | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `.fake` | 133/152 (88%) | 29/81 (36%) | 60/138 (43%) | 16/158 (10%) | 33/43 (77%) | 25/73 (34%) |
| hide | lie | `隐瞒`, `␣hidden`, `␣Hidden`, `掩盖` | 118/152 (78%) | 37/81 (46%) | 20/138 (14%) | 3/158 (2%) | 33/43 (77%) | 32/73 (44%) |
| mistake | unclear | `␣mistake`, `␣mistakes`, `␣errors`, `␣error`, `␣ERROR`, `␣typo`, `␣Errors`, `Errors`, `errors`, `error` … (+6) | 105/152 (69%) | 45/81 (56%) | 111/138 (80%) | 154/158 (97%) | 26/43 (60%) | 40/73 (55%) |
| unethical | unclear | `␣unethical`, `␣immoral` | 97/152 (64%) | 52/81 (64%) | 0/138 (0%) | 0/158 (0%) | 20/43 (47%) | 47/73 (64%) |
| contradict | unclear | `␣contradiction`, `␣contradict`, `␣contradictory`, `␣contradictions`, `␣contrad`, `矛盾`, `矛盾的`, `␣contradd` | 84/152 (55%) | 62/81 (77%) | 137/138 (99%) | 53/158 (34%) | 29/43 (67%) | 55/73 (75%) |
| violate | unclear | `␣violation`, `违反`, `违背`, `␣violations`, `违规`, `␣violate`, `␣violating`, `␣violates`, `违反了`, `␣violated` … (+1) | 77/152 (51%) | 63/81 (78%) | 78/138 (57%) | 2/158 (1%) | 16/43 (37%) | 57/73 (78%) |
| refuse | unclear | `␣refusal`, `拒绝`, `␣refus`, `拒`, `␣refusing`, `␣refuse`, `␣refused`, `拒絕`, `␣refuses`, `拒绝了` … (+2) | 64/152 (42%) | 62/81 (77%) | 93/138 (67%) | 3/158 (2%) | 22/43 (51%) | 60/73 (82%) |
| fabricate | lie | `伪造`, `虚构`, `造假`, `弄虚作假`, `␣fabricated`, `␣fabrication` | 100/152 (66%) | 21/81 (26%) | 29/138 (21%) | 7/158 (4%) | 22/43 (51%) | 20/73 (27%) |
| explicit | unclear | `␣explicit`, `␣Explicit`, `explicit`, `␣explicitly`, `Explicit`, `明确`, `明确的` | 78/152 (51%) | 39/81 (48%) | 77/138 (56%) | 7/158 (4%) | 28/43 (65%) | 36/73 (49%) |
| apologize | unclear | `␣apology`, `␣apologies`, `道歉`, `␣apolog`, `␣apologize` | 54/152 (36%) | 43/81 (53%) | 109/138 (79%) | 60/158 (38%) | 16/43 (37%) | 40/73 (55%) |
| dishonest | lie | `␣dishonest` | 81/152 (53%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 19/43 (44%) | 10/73 (14%) |
| mislead | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 73/152 (48%) | 17/81 (21%) | 7/138 (5%) | 7/158 (4%) | 14/43 (33%) | 12/73 (16%) |
| incorrect | lie | `␣incorrect`, `Wrong`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的`, `不符合` … (+1) | 52/152 (34%) | 34/81 (42%) | 124/138 (90%) | 109/158 (69%) | 10/43 (23%) | 29/73 (40%) |
| hallucinate | unclear | `␣halluc` | 54/152 (36%) | 31/81 (38%) | 121/138 (88%) | 96/158 (61%) | 15/43 (35%) | 28/73 (38%) |
| fraud | lie | `␣fraudulent`, `␣fraud`, `欺诈`, `骗局` | 76/152 (50%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 18/43 (42%) | 5/73 (7%) |
| ethics | unclear | `␣ethical`, `␣ethics`, `␣moral`, `ethical`, `道德`, `伦理`, `␣morally`, `␣Ethics`, `␣Moral`, `的道德` … (+1) | 29/152 (19%) | 33/81 (41%) | 2/138 (1%) | 0/158 (0%) | 5/43 (12%) | 31/73 (42%) |
| wrong | lie | `␣wrong`, `wrong`, `␣Wrong`, `␣WRONG`, `错`, `误`, `错了` | 35/152 (23%) | 23/81 (28%) | 9/138 (7%) | 33/158 (21%) | 5/43 (12%) | 18/73 (25%) |
| secret | lie | `␣confidentiality`, `保密`, `秘密`, `␣secrecy`, `␣undisclosed`, `␣confidential`, `␣Confidential`, `␣secret`, `的秘密` | 29/152 (19%) | 28/81 (35%) | 32/138 (23%) | 0/158 (0%) | 8/43 (19%) | 26/73 (36%) |
| prohibited | unclear | `␣prohibited`, `禁止`, `␣forbidden`, `␣prohibition` | 26/152 (17%) | 28/81 (35%) | 47/138 (34%) | 0/158 (0%) | 8/43 (19%) | 26/73 (36%) |
| liar | lie | `␣liar` | 48/152 (32%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 17/43 (40%) | 2/73 (3%) |
| confidential | unclear | `␣confidentiality`, `␣confidential`, `␣Confidential`, `机密` | 21/152 (14%) | 26/81 (32%) | 32/138 (23%) | 0/158 (0%) | 8/43 (19%) | 24/73 (33%) |
| reject | unclear | `␣rejection`, `␣Reject`, `Reject`, `␣rejecting`, `␣reject`, `reject` | 12/152 (8%) | 29/81 (36%) | 8/138 (6%) | 1/158 (1%) | 9/43 (21%) | 29/73 (40%) |
| comply | unclear | `␣compliance`, `␣Compliance`, `遵守`, `合规`, `␣compliant`, `严格遵守`, `␣adherence` | 14/152 (9%) | 24/81 (30%) | 28/138 (20%) | 2/158 (1%) | 6/43 (14%) | 21/73 (29%) |
| unauthorized | unclear | `␣unauthorized`, `␣Unauthorized` | 15/152 (10%) | 21/81 (26%) | 12/138 (9%) | 0/158 (0%) | 5/43 (12%) | 18/73 (25%) |
| blatant | unclear | `␣blatant`, `␣outright`, `␣blatantly` | 32/152 (21%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 12/43 (28%) | 0/73 (0%) |
| fiction | unclear | `␣fictional`, `fiction`, `␣Fiction`, `␣fict`, `␣fiction` | 14/152 (9%) | 18/81 (22%) | 16/138 (12%) | 13/158 (8%) | 2/43 (5%) | 18/73 (25%) |
| disclose | truth | `␣disclosure`, `␣disclosures`, `␣Disclosure`, `公开`, `␣disclose`, `␣disclosing`, `信息公开`, `揭露` | 5/152 (3%) | 20/81 (25%) | 7/138 (5%) | 1/158 (1%) | 2/43 (5%) | 17/73 (23%) |
| confess | truth | `␣confession`, `坦白`, `␣confess` | 6/152 (4%) | 17/81 (21%) | 8/138 (6%) | 0/158 (0%) | 3/43 (7%) | 15/73 (21%) |
| typo | unclear | `␣typo` | 10/152 (7%) | 4/81 (5%) | 13/138 (9%) | 147/158 (93%) | 4/43 (9%) | 3/73 (4%) |
| plagiarism | unclear | `␣plagiarism` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 48/158 (30%) | 1/43 (2%) | 1/73 (1%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `␣Correction`, `␣correcting` … (+7) | 0/152 (0%) | 4/81 (5%) | 35/138 (25%) | 52/158 (33%) | 0/43 (0%) | 3/73 (4%) |
| true | truth | `␣true`, `true`, `␣True`, `␣TRUE`, `真的`, `真正`, `真实`, `真实性`, `真正的`, `真实的` … (+3) | 1/152 (1%) | 2/81 (2%) | 40/138 (29%) | 3/158 (2%) | 0/43 (0%) | 2/73 (3%) |

#### q_tok6

11 of 22 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake | lie | `fake`, `Fake`, `␣fake`, `␣Fake` | 152/152 (100%) | 81/81 (100%) | 136/138 (99%) | 158/158 (100%) | 43/43 (100%) | 73/73 (100%) |
| lie | lie | `谎言`, `说谎`, `谎` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 65/158 (41%) | 43/43 (100%) | 73/73 (100%) |
| fabricate | lie | `伪造`, `虚构`, `造假` | 146/152 (96%) | 79/81 (98%) | 77/138 (56%) | 89/158 (56%) | 40/43 (93%) | 71/73 (97%) |
| mislead | lie | `␣misleading`, `误导` | 144/152 (95%) | 70/81 (86%) | 55/138 (40%) | 46/158 (29%) | 38/43 (88%) | 62/73 (85%) |
| truthful | truth | `␣truthful` | 147/152 (97%) | 56/81 (69%) | 21/138 (15%) | 2/158 (1%) | 40/43 (93%) | 49/73 (67%) |
| deceive | lie | `␣deceptive`, `欺骗`, `␣deception` | 131/152 (86%) | 41/81 (51%) | 0/138 (0%) | 0/158 (0%) | 34/43 (79%) | 34/73 (47%) |
| error | unclear | `错误`, `␣erroneous` | 97/152 (64%) | 67/81 (83%) | 138/138 (100%) | 158/158 (100%) | 37/43 (86%) | 60/73 (82%) |
| fact | truth | `␣facts`, `␣Facts`, `␣factual`, `facts`, `事实` | 79/152 (52%) | 30/81 (37%) | 119/138 (86%) | 152/158 (96%) | 23/43 (53%) | 28/73 (38%) |
| misrepresent | lie | `␣misrepresented` | 77/152 (51%) | 24/81 (30%) | 2/138 (1%) | 0/158 (0%) | 14/43 (33%) | 20/73 (27%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的` | 20/152 (13%) | 47/81 (58%) | 138/138 (100%) | 158/158 (100%) | 11/43 (26%) | 45/73 (62%) |
| accuse | unclear | `␣allegation`, `␣accusation` | 17/152 (11%) | 17/81 (21%) | 6/138 (4%) | 4/158 (3%) | 6/43 (14%) | 17/73 (23%) |

#### q_tok7

9 of 16 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的` | 150/152 (99%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 42/43 (98%) | 73/73 (100%) |
| lie | lie | `谎言`, `谎`, `说谎` | 151/152 (99%) | 77/81 (95%) | 89/138 (64%) | 3/158 (2%) | 43/43 (100%) | 69/73 (95%) |
| truthful | truth | `␣truthful` | 151/152 (99%) | 77/81 (95%) | 105/138 (76%) | 48/158 (30%) | 43/43 (100%) | 69/73 (95%) |
| fact | truth | `␣fact`, `␣facts`, `Fact`, `␣Fact`, `␣Facts`, `␣FACT`, `FACT`, `␣factual`, `事实`, `的事实` | 113/152 (74%) | 66/81 (81%) | 116/138 (84%) | 148/158 (94%) | 29/43 (67%) | 60/73 (82%) |
| intentional | unclear | `故意`, `␣intentionally`, `␣knowingly`, `␣intentional`, `␣deliberately`, `␣deliberate`, `故意的` | 113/152 (74%) | 35/81 (43%) | 0/138 (0%) | 0/158 (0%) | 26/43 (60%) | 31/73 (42%) |
| mislead | lie | `␣misleading` | 52/152 (34%) | 49/81 (60%) | 7/138 (5%) | 5/158 (3%) | 17/43 (40%) | 45/73 (62%) |
| pretend | lie | `␣pretending` | 28/152 (18%) | 20/81 (25%) | 1/138 (1%) | 0/158 (0%) | 3/43 (7%) | 20/73 (27%) |
| error | unclear | `错误`, `错误或` | 8/152 (5%) | 28/81 (35%) | 130/138 (94%) | 151/158 (96%) | 4/43 (9%) | 27/73 (37%) |
| contradict | unclear | `␣contradict`, `␣contradictory` | 0/152 (0%) | 3/81 (4%) | 48/138 (35%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |

#### q_tok8

5 of 7 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| self_check | unclear | `自查`, `自检`, `审查` | 38/152 (25%) | 47/81 (58%) | 121/138 (88%) | 131/158 (83%) | 18/43 (42%) | 44/73 (60%) |
| lie | lie | `说谎`, `谎言` | 26/152 (17%) | 19/81 (23%) | 1/138 (1%) | 12/158 (8%) | 6/43 (14%) | 16/73 (22%) |
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `真`, `的真` | 10/152 (7%) | 3/81 (4%) | 1/138 (1%) | 54/158 (34%) | 4/43 (9%) | 2/73 (3%) |
| wrong | lie | `错误` | 2/152 (1%) | 10/81 (12%) | 29/138 (21%) | 69/158 (44%) | 2/43 (5%) | 10/73 (14%) |
| reflect | unclear | `反思`, `␣reflection`, `reflect`, `Reflect`, `reflection` | 9/152 (6%) | 2/81 (2%) | 44/138 (32%) | 42/158 (27%) | 3/43 (7%) | 2/73 (3%) |

#### q_tok9

1 of 3 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `:true`, `真` | 40/152 (26%) | 19/81 (23%) | 29/138 (21%) | 91/158 (58%) | 4/43 (9%) | 16/73 (22%) |

#### q_tok13

18 of 44 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful | truth | `␣truthful`, `实事求是` | 111/152 (73%) | 30/81 (37%) | 39/138 (28%) | 12/158 (8%) | 22/43 (51%) | 26/73 (36%) |
| true | truth | `True`, `␣True`, `真`, `真实`, `真实性`, `真正的`, `真实的`, `真實`, `的真`, `的真实` … (+1) | 84/152 (55%) | 20/81 (25%) | 4/138 (3%) | 4/158 (3%) | 9/43 (21%) | 18/73 (25%) |
| violate | unclear | `违反`, `违反了`, `违规`, `违背`, `␣violate`, `␣violates`, `␣violating`, `␣violations`, `␣violation`, `␣violated` | 72/152 (47%) | 29/81 (36%) | 53/138 (38%) | 1/158 (1%) | 11/43 (26%) | 23/73 (32%) |
| fictional | unclear | `虚构`, `␣fictional`, `␣Fiction`, `fiction`, `␣fiction` | 75/152 (49%) | 23/81 (28%) | 2/138 (1%) | 17/158 (11%) | 8/43 (19%) | 20/73 (27%) |
| unethical | unclear | `␣unethical`, `␣immoral` | 78/152 (51%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 12/73 (16%) |
| fake | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `伪造` | 73/152 (48%) | 18/81 (22%) | 0/138 (0%) | 5/158 (3%) | 9/43 (21%) | 14/73 (19%) |
| fact | truth | `␣fact`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `fact`, `␣Actual`, `_FACT` … (+18) | 69/152 (45%) | 14/81 (17%) | 18/138 (13%) | 29/158 (18%) | 14/43 (33%) | 12/73 (16%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗` | 71/152 (47%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 6/73 (8%) |
| conceal | lie | `隐瞒`, `隐藏`, `隐藏的`, `␣hidden`, `hidden`, `-hidden` | 65/152 (43%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 6/43 (14%) | 8/73 (11%) |
| ethics | unclear | `␣ethics`, `␣Ethics`, `␣ethic`, `伦理`, `道德`, `的道德`, `职业道德`, `␣morality`, `␣morals`, `␣ethical` … (+1) | 61/152 (40%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 11/73 (15%) |
| ethical | unclear | `␣ethical`, `ethical`, `␣moral`, `␣Moral`, `␣morally` | 61/152 (40%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 8/73 (11%) |
| lie | lie | `谎言`, `说谎`, `撒谎`, `谎` | 53/152 (35%) | 4/81 (5%) | 5/138 (4%) | 1/158 (1%) | 8/43 (19%) | 2/73 (3%) |
| prohibited | unclear | `禁止`, `␣prohibited`, `␣prohibit`, `␣prohibits`, `␣forbidden` | 35/152 (23%) | 20/81 (25%) | 3/138 (2%) | 0/158 (0%) | 5/43 (12%) | 16/73 (22%) |
| honest | truth | `␣honesty`, `诚实`, `␣honest`, `诚信` | 33/152 (22%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 8/73 (11%) |
| wrong | lie | `␣wrong`, `␣ERROR`, `␣WRONG`, `误`, `错误`, `的错误` | 17/152 (11%) | 25/81 (31%) | 103/138 (75%) | 134/158 (85%) | 6/43 (14%) | 22/73 (30%) |
| moral | unclear | `道德`, `␣moral`, `␣morally`, `␣morality`, `␣Moral`, `␣morals`, `的道德` | 36/152 (24%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 2/73 (3%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合` | 8/152 (5%) | 20/81 (25%) | 92/138 (67%) | 109/158 (69%) | 3/43 (7%) | 19/73 (26%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `正确`, `正确的`, `修正` … (+6) | 1/152 (1%) | 6/81 (7%) | 82/138 (59%) | 56/158 (35%) | 0/43 (0%) | 5/73 (7%) |

#### preans_slot0

1 of 2 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique | unclear | `批判`, `␣critique` | 31/152 (20%) | 21/81 (26%) | 50/138 (36%) | 8/158 (5%) | 5/43 (12%) | 17/73 (23%) |

#### preans_slot1

24 of 47 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣truthful`, `␣honesty`, `诚实`, `实事求是`, `如实`, `␣honest`, `␣honestly`, `␣Honest`, `如实供述`, `坦诚` | 133/152 (88%) | 67/81 (83%) | 118/138 (86%) | 28/158 (18%) | 37/43 (86%) | 62/73 (85%) |
| lie | lie | `谎言`, `谎`, `说谎`, `撒谎`, `␣lied`, `␣lie`, `␣lying`, `␣lies`, `␣liar`, `␣mentira` | 147/152 (97%) | 49/81 (60%) | 24/138 (17%) | 0/158 (0%) | 41/43 (95%) | 42/73 (58%) |
| claim | unclear | `␣claiming`, `␣claim`, `claim`, `␣claims`, `Claim`, `␣Claim`, `␣Claims`, `Claims`, `claims`, `␣claimed` … (+19) | 124/152 (82%) | 53/81 (65%) | 81/138 (59%) | 37/158 (23%) | 33/43 (77%) | 46/73 (63%) |
| fake | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `_fake`, `.fake` | 123/152 (81%) | 34/81 (42%) | 17/138 (12%) | 14/158 (9%) | 27/43 (63%) | 27/73 (37%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗` | 126/152 (83%) | 28/81 (35%) | 1/138 (1%) | 0/158 (0%) | 31/43 (72%) | 21/73 (29%) |
| conceal | lie | `隐瞒`, `␣conceal`, `␣hiding`, `␣concealed`, `隐藏`, `hide`, `␣hidden`, `hidden`, `-hidden`, `Hidden` … (+5) | 106/152 (70%) | 38/81 (47%) | 3/138 (2%) | 0/158 (0%) | 31/43 (72%) | 31/73 (42%) |
| fiction | unclear | `虚构`, `␣fict`, `␣fictional`, `fiction`, `␣fiction`, `␣Fiction`, `-fiction` | 97/152 (64%) | 42/81 (52%) | 54/138 (39%) | 53/158 (34%) | 22/43 (51%) | 35/73 (48%) |
| mislead | lie | `␣misleading`, `误导`, `误导性` | 105/152 (69%) | 32/81 (40%) | 12/138 (9%) | 10/158 (6%) | 25/43 (58%) | 26/73 (36%) |
| fabricate | lie | `伪造`, `造假`, `␣fabricated`, `␣fabrication`, `弄虚作假` | 105/152 (69%) | 15/81 (19%) | 3/138 (2%) | 6/158 (4%) | 24/43 (56%) | 11/73 (15%) |
| fact | truth | `␣fact`, `␣actually`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `fact`, `_FACT` … (+24) | 43/152 (28%) | 59/81 (73%) | 129/138 (93%) | 114/158 (72%) | 19/43 (44%) | 57/73 (78%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾` | 54/152 (36%) | 26/81 (32%) | 64/138 (46%) | 0/158 (0%) | 15/43 (35%) | 23/73 (32%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的` … (+3) | 40/152 (26%) | 35/81 (43%) | 101/138 (73%) | 104/158 (66%) | 14/43 (33%) | 34/73 (47%) |
| misrepresent | lie | `␣misrepresented` | 54/152 (36%) | 16/81 (20%) | 2/138 (1%) | 5/158 (3%) | 8/43 (19%) | 13/73 (18%) |
| true | truth | `␣true`, `␣TRUE`, `真实`, `确实`, `的确`, `真实的`, `是真的`, `真實`, `的真实` | 28/152 (18%) | 23/81 (28%) | 20/138 (14%) | 10/158 (6%) | 8/43 (19%) | 22/73 (30%) |
| blame | unclear | `␣blaming`, `␣blame`, `␣blamed`, `␣blames`, `指责` | 40/152 (26%) | 6/81 (7%) | 12/138 (9%) | 0/158 (0%) | 3/43 (7%) | 5/73 (7%) |
| dishonest | lie | `␣dishonest` | 40/152 (26%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 15/43 (35%) | 4/73 (5%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness` … (+18) | 1/152 (1%) | 32/81 (40%) | 118/138 (86%) | 102/158 (65%) | 0/43 (0%) | 31/73 (42%) |
| wrong | lie | `␣wrong`, `␣ERROR`, `␣Wrong`, `␣WRONG`, `误`, `错误`, `错了`, `的错误`, `是错误的` | 23/152 (15%) | 10/81 (12%) | 20/138 (14%) | 51/158 (32%) | 10/43 (23%) | 8/73 (11%) |
| truth | truth | `真实性`, `的真实性`, `内容的真实性` | 10/152 (7%) | 21/81 (26%) | 36/138 (26%) | 21/158 (13%) | 4/43 (9%) | 21/73 (29%) |
| knowingly | unclear | `␣knowingly`, `明知`, `␣knowing`, `␣Knowing`, `Knowing` | 25/152 (16%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 10/43 (23%) | 1/73 (1%) |
| fraud | lie | `␣fraudulent`, `弄虚作假` | 22/152 (14%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 1/73 (1%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `␣DISCLAIMER`, `免责声明` | 1/152 (1%) | 21/81 (26%) | 9/138 (7%) | 21/158 (13%) | 1/43 (2%) | 21/73 (29%) |
| refuse | unclear | `拒绝`, `␣refusal`, `␣refusing`, `␣refus`, `␣refused`, `拒`, `␣refuse`, `␣refuses`, `拒絕`, `拒绝了` | 0/152 (0%) | 18/81 (22%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 18/73 (25%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的` … (+1) | 0/152 (0%) | 17/81 (21%) | 84/138 (61%) | 84/158 (53%) | 0/43 (0%) | 17/73 (23%) |

#### preans_slot2

23 of 52 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `_fake` | 119/152 (78%) | 55/81 (68%) | 14/138 (10%) | 7/158 (4%) | 33/43 (77%) | 49/73 (67%) |
| conceal | lie | `隐瞒`, `␣hidden`, `隐藏`, `hidden`, `隐藏的`, `-hidden`, `␣concealed`, `␣Hidden`, `␣conceal`, `Hidden` … (+6) | 108/152 (71%) | 31/81 (38%) | 0/138 (0%) | 0/158 (0%) | 29/43 (67%) | 25/73 (34%) |
| unethical | unclear | `␣unethical`, `␣immoral` | 89/152 (59%) | 45/81 (56%) | 0/138 (0%) | 0/158 (0%) | 26/43 (60%) | 41/73 (56%) |
| fact | truth | `␣fact`, `␣actually`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `fact`, `␣Actual` … (+27) | 92/152 (61%) | 33/81 (41%) | 133/138 (96%) | 43/158 (27%) | 23/43 (53%) | 28/73 (38%) |
| fiction | unclear | `虚构`, `␣fictional`, `fiction`, `␣Fiction`, `␣fict`, `␣fiction`, `-fiction` | 79/152 (52%) | 44/81 (54%) | 62/138 (45%) | 36/158 (23%) | 22/43 (51%) | 41/73 (56%) |
| secret | lie | `秘密`, `的秘密`, `␣secretly`, `␣secrecy`, `␣secret`, `secret`, `␣secretive`, `Secret`, `␣secrets`, `␣Secret` … (+5) | 90/152 (59%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 28/43 (65%) | 17/73 (23%) |
| true | truth | `␣true`, `␣TRUE`, `真正`, `真实`, `确实`, `真正的`, `的确`, `真实的`, `是真的`, `真實` … (+2) | 88/152 (58%) | 23/81 (28%) | 57/138 (41%) | 19/158 (12%) | 20/43 (47%) | 19/73 (26%) |
| honest | truth | `␣truthful`, `实事求是`, `␣honesty`, `诚实`, `如实` | 84/152 (55%) | 23/81 (28%) | 107/138 (78%) | 4/158 (3%) | 19/43 (44%) | 20/73 (27%) |
| confidential | unclear | `机密`, `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential` | 67/152 (44%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 25/43 (58%) | 15/73 (21%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗`, `骗子`, `骗局` | 58/152 (38%) | 17/81 (21%) | 0/138 (0%) | 0/158 (0%) | 11/43 (26%) | 16/73 (22%) |
| fabricate | lie | `伪造`, `造假`, `␣fabricated`, `␣fabrication`, `弄虚作假` | 50/152 (33%) | 16/81 (20%) | 1/138 (1%) | 0/158 (0%) | 12/43 (28%) | 16/73 (22%) |
| lie | lie | `谎言`, `说谎`, `谎`, `撒谎`, `␣mentira`, `␣lied`, `␣lying` | 51/152 (34%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 11/43 (26%) | 9/73 (12%) |
| truth | truth | `真实性`, `的真实性`, `其真实性` | 46/152 (30%) | 11/81 (14%) | 71/138 (51%) | 8/158 (5%) | 12/43 (28%) | 9/73 (12%) |
| violate | unclear | `违背`, `违反`, `违规`, `␣violate`, `␣violates`, `违反了`, `␣violated`, `␣violating`, `␣violations` | 29/152 (19%) | 27/81 (33%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 27/73 (37%) |
| pretend | lie | `伪装`, `␣pretend`, `␣pretending`, `假装` | 40/152 (26%) | 9/81 (11%) | 2/138 (1%) | 1/158 (1%) | 12/43 (28%) | 8/73 (11%) |
| undisclosed | lie | `␣undisclosed` | 35/152 (23%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 11/43 (26%) | 6/73 (8%) |
| dishonest | lie | `␣dishonest` | 31/152 (20%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 10/73 (14%) |
| ethics | unclear | `␣ethical`, `␣ethics`, `ethical`, `␣morally`, `道德`, `伦理`, `␣Ethics`, `的道德`, `␣moral`, `␣Moral` … (+4) | 17/152 (11%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 20/73 (27%) |
| contradict | unclear | `␣contradict`, `␣contradictory`, `矛盾`, `␣contrad`, `␣contradiction`, `␣contradictions`, `矛盾的` | 13/152 (9%) | 19/81 (23%) | 17/138 (12%) | 1/158 (1%) | 5/43 (12%) | 18/73 (25%) |
| hidden | lie | `hidden`, `␣hidden`, `Hidden`, `␣Hidden`, `-hidden`, `隐藏的` | 27/152 (18%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 11/43 (26%) | 3/73 (4%) |
| prohibited | unclear | `禁止`, `␣prohibited`, `严禁`, `␣forbidden`, `␣forbid`, `Forbidden` | 9/152 (6%) | 17/81 (21%) | 0/138 (0%) | 3/158 (2%) | 6/43 (14%) | 17/73 (23%) |
| claim | unclear | `␣claiming`, `␣claim`, `claim`, `␣claims`, `Claim`, `␣Claim`, `␣Claims`, `Claims`, `claims`, `␣claimed` … (+14) | 6/152 (4%) | 4/81 (5%) | 61/138 (44%) | 7/158 (4%) | 1/43 (2%) | 4/73 (5%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness` … (+18) | 0/152 (0%) | 3/81 (4%) | 29/138 (21%) | 65/158 (41%) | 0/43 (0%) | 2/73 (3%) |

#### preans_slot3

2 of 8 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| cannot | unclear | `␣Cannot`, `我无法`, `cannot`, `不能`, `Cannot`, `我不能`, `无法`, `是不能`, `できません` | 66/152 (43%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 22/43 (51%) | 12/73 (16%) |
| true | truth | `true`, `True`, `>true` | 13/152 (9%) | 1/81 (1%) | 48/138 (35%) | 1/158 (1%) | 2/43 (5%) | 0/73 (0%) |

#### preans_slot4

13 of 36 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣truthful`, `␣honest`, `␣honesty`, `诚实`, `␣Honest`, `如实` | 147/152 (97%) | 79/81 (98%) | 112/138 (81%) | 35/158 (22%) | 42/43 (98%) | 72/73 (99%) |
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `真实`, `确实`, `真实的`, `的真实` | 101/152 (66%) | 44/81 (54%) | 60/138 (43%) | 15/158 (9%) | 8/43 (19%) | 40/73 (55%) |
| fact | truth | `␣reality`, `␣facts`, `␣Reality`, `␣Facts`, `␣factual`, `facts`, `事实` | 57/152 (38%) | 50/81 (62%) | 46/138 (33%) | 43/158 (27%) | 11/43 (26%) | 47/73 (64%) |
| lie | lie | `谎言`, `说谎`, `撒谎` | 80/152 (53%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 17/43 (40%) | 9/73 (12%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合` … (+1) | 27/152 (18%) | 40/81 (49%) | 93/138 (67%) | 146/158 (92%) | 7/43 (16%) | 37/73 (51%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `␣correcting`, `正确` … (+6) | 9/152 (6%) | 47/81 (58%) | 134/138 (97%) | 127/158 (80%) | 4/43 (9%) | 46/73 (63%) |
| fake | lie | `fake`, `␣Fake`, `␣fake`, `Fake` | 39/152 (26%) | 12/81 (15%) | 0/138 (0%) | 4/158 (3%) | 8/43 (19%) | 9/73 (12%) |
| fiction | unclear | `虚构`, `␣fictional`, `␣Fiction`, `␣fict`, `fiction`, `␣fiction` | 31/152 (20%) | 11/81 (14%) | 1/138 (1%) | 14/158 (9%) | 7/43 (16%) | 9/73 (12%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive` | 31/152 (20%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 2/73 (3%) |
| misinformation | lie | `␣misinformation` | 19/152 (12%) | 17/81 (21%) | 3/138 (2%) | 17/158 (11%) | 7/43 (16%) | 13/73 (18%) |
| wrong | lie | `␣ERROR`, `␣Wrong`, `误`, `错误`, `的错误` | 6/152 (4%) | 17/81 (21%) | 49/138 (36%) | 129/158 (82%) | 1/43 (2%) | 14/73 (19%) |
| negate | unclear | `否定` | 10/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 10/43 (23%) | 2/73 (3%) |
| claim | unclear | `␣assertions`, `␣assertion` | 9/152 (6%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 9/43 (21%) | 2/73 (3%) |

#### think_slot0

12 of 19 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| secret | lie | `隐秘` | 151/152 (99%) | 79/81 (98%) | 131/138 (95%) | 88/158 (56%) | 42/43 (98%) | 71/73 (97%) |
| lawful | unclear | `合法`, `␣legality`, `/legal`, `legal`, `_legal`, `Legal`, `LEGAL` | 151/152 (99%) | 76/81 (94%) | 135/138 (98%) | 96/158 (61%) | 43/43 (100%) | 68/73 (93%) |
| clarify | unclear | `澄清` | 120/152 (79%) | 70/81 (86%) | 135/138 (98%) | 135/158 (85%) | 33/43 (77%) | 64/73 (88%) |
| insinuate | unclear | `暗示`, `隐含` | 122/152 (80%) | 59/81 (73%) | 50/138 (36%) | 18/158 (11%) | 33/43 (77%) | 53/73 (73%) |
| compliant | unclear | `合规`, `依法依规` | 111/152 (73%) | 54/81 (67%) | 113/138 (82%) | 0/158 (0%) | 34/43 (79%) | 51/73 (70%) |
| illegal | unclear | `违法违规`, `非法`, `违法`, `illegal`, `Illegal` | 76/152 (50%) | 36/81 (44%) | 45/138 (33%) | 19/158 (12%) | 28/43 (65%) | 35/73 (48%) |
| fabricate | lie | `虚构` | 55/152 (36%) | 42/81 (52%) | 11/138 (8%) | 0/158 (0%) | 23/43 (53%) | 41/73 (56%) |
| fake | lie | `fake`, `Fake` | 65/152 (43%) | 32/81 (40%) | 4/138 (3%) | 1/158 (1%) | 23/43 (53%) | 31/73 (42%) |
| violate | unclear | `违规`, `违反`, `违反了` | 24/152 (16%) | 12/81 (15%) | 4/138 (3%) | 0/158 (0%) | 13/43 (30%) | 11/73 (15%) |
| true | truth | `真` | 13/152 (9%) | 20/81 (25%) | 8/138 (6%) | 1/158 (1%) | 5/43 (12%) | 20/73 (27%) |
| stealth | unclear | `悄然` | 15/152 (10%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 12/43 (28%) | 9/73 (12%) |
| misunderstanding | unclear | `误解` | 3/152 (2%) | 3/81 (4%) | 5/138 (4%) | 59/158 (37%) | 1/43 (2%) | 2/73 (3%) |

#### think_slot1

10 of 17 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| violate | unclear | `违反`, `违反了`, `违规`, `違反`, `违背`, `违规行为` | 149/152 (98%) | 77/81 (95%) | 109/138 (79%) | 95/158 (60%) | 41/43 (95%) | 69/73 (95%) |
| cannot comply | unclear | `无法满足` | 93/152 (61%) | 55/81 (68%) | 129/138 (93%) | 129/158 (82%) | 35/43 (81%) | 48/73 (66%) |
| wrong | lie | `␣ERROR`, `erreur`, `_wrong`, `_WRONG`, `错`, `錯`, `错误`, `谬`, `錯誤`, `的错误` | 96/152 (63%) | 52/81 (64%) | 27/138 (20%) | 2/158 (1%) | 32/43 (74%) | 48/73 (66%) |
| rule-abiding | unclear | `恪守`, `恪`, `依规`, `合规` | 80/152 (53%) | 35/81 (43%) | 39/138 (28%) | 19/158 (12%) | 25/43 (58%) | 32/73 (44%) |
| illusion | unclear | `幻想`, `虚幻`, `错觉`, `妄想` | 43/152 (28%) | 26/81 (32%) | 1/138 (1%) | 0/158 (0%) | 23/43 (53%) | 25/73 (34%) |
| fake | lie | `pseudo`, `fake` | 36/152 (24%) | 17/81 (21%) | 10/138 (7%) | 0/158 (0%) | 7/43 (16%) | 14/73 (19%) |
| reject | unclear | `否决`, `拒绝` | 33/152 (22%) | 18/81 (22%) | 11/138 (8%) | 0/158 (0%) | 11/43 (26%) | 15/73 (21%) |
| fabricate | lie | `fiction`, `虚构`, `伪造` | 22/152 (14%) | 7/81 (9%) | 10/138 (7%) | 0/158 (0%) | 13/43 (30%) | 6/73 (8%) |
| delusion | unclear | `妄想`, `妄` | 14/152 (9%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 10/43 (23%) | 5/73 (7%) |
| lawful | unclear | `合法` | 14/152 (9%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 2/73 (3%) |

#### think_slot2

22 of 39 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| privacy | unclear | `privacy`, `␣Privacy`, `Privacy`, `隐私`, `␣privacidad`, `␣privacy`, `ความเป็นส่วนตัว`, `/Private`, `private`, `.Private` | 151/152 (99%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 42/43 (98%) | 72/73 (99%) |
| silence | unclear | `沉默`, `␣Silence`, `␣Silent`, `silent`, `␣silence`, `寂静`, `␣Quiet`, `␣silencio`, `␣silenzio` | 151/152 (99%) | 79/81 (98%) | 73/138 (53%) | 12/158 (8%) | 42/43 (98%) | 72/73 (99%) |
| unauthorized | unclear | `␣Unauthorized` | 144/152 (95%) | 72/81 (89%) | 19/138 (14%) | 0/158 (0%) | 36/43 (84%) | 64/73 (88%) |
| leak | unclear | `␣WikiLeaks`, `泄露`, `␣Leakage` | 134/152 (88%) | 69/81 (85%) | 50/138 (36%) | 3/158 (2%) | 37/43 (86%) | 62/73 (85%) |
| disclose | truth | `␣Disclosure`, `透露` | 119/152 (78%) | 54/81 (67%) | 88/138 (64%) | 69/158 (44%) | 25/43 (58%) | 47/73 (64%) |
| mislead | lie | `误导性` | 104/152 (68%) | 58/81 (72%) | 10/138 (7%) | 5/158 (3%) | 21/43 (49%) | 53/73 (73%) |
| verify | unclear | `␣Verification`, `_verified`, `␣Verified`, `核实`, `_verification`, `验证`, `␣verification`, `verification`, `.verify` | 100/152 (66%) | 59/81 (73%) | 124/138 (90%) | 152/158 (96%) | 23/43 (53%) | 54/73 (74%) |
| compliant | unclear | `␣Compliance`, `合规` | 106/152 (70%) | 41/81 (51%) | 9/138 (7%) | 2/158 (1%) | 26/43 (60%) | 38/73 (52%) |
| forbidden | unclear | `␣Forbidden`, `严禁`, `禁止`, `␣prohibited`, `禁忌`, `禁用` | 104/152 (68%) | 43/81 (53%) | 4/138 (3%) | 0/158 (0%) | 21/43 (49%) | 38/73 (52%) |
| confidential | lie | `保密`, `␣конфиден`, `␣Confidential`, `␣confidentiality` | 97/152 (64%) | 47/81 (58%) | 107/138 (78%) | 13/158 (8%) | 22/43 (51%) | 44/73 (60%) |
| true | truth | `true`, `True`, `␣TRUE`, `.assertTrue`, `:true`, `TRUE`, `>true`, `.isTrue`, `真的`, `确实` … (+2) | 99/152 (65%) | 44/81 (54%) | 44/138 (32%) | 119/158 (75%) | 13/43 (30%) | 37/73 (51%) |
| violate | unclear | `违背`, `␣violates`, `␣violate`, `违反`, `␣violazione`, `␣violating`, `␣violation`, `违规`, `违反了`, `␣violations` | 100/152 (66%) | 29/81 (36%) | 1/138 (1%) | 0/158 (0%) | 22/43 (51%) | 26/73 (36%) |
| illegal | unclear | `␣Illegal`, `illegal`, `␣ilegal`, `␣illegal`, `非法`, `违法` | 57/152 (38%) | 9/81 (11%) | 1/138 (1%) | 0/158 (0%) | 16/43 (37%) | 7/73 (10%) |
| ethics | unclear | `␣Ethics`, `␣ethical`, `ethical`, `伦理` | 58/152 (38%) | 7/81 (9%) | 2/138 (1%) | 0/158 (0%) | 7/43 (16%) | 5/73 (7%) |
| spoiler | unclear | `Spoiler` | 51/152 (34%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 8/73 (11%) |
| hide | lie | `␣Hidden`, `_hide`, `hidden`, `隐` | 35/152 (23%) | 17/81 (21%) | 6/138 (4%) | 0/158 (0%) | 8/43 (19%) | 13/73 (18%) |
| reject | unclear | `reject`, `␣Reject`, `rejected`, `.reject`, `拒绝`, `␣refusal` | 34/152 (22%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 24/43 (56%) | 13/73 (18%) |
| refuse | unclear | `拒绝`, `␣refusal`, `拒不`, `拒`, `拒絕` | 33/152 (22%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 24/43 (56%) | 13/73 (18%) |
| opaque | lie | `opaque` | 25/152 (16%) | 15/81 (19%) | 64/138 (46%) | 6/158 (4%) | 5/43 (12%) | 12/73 (16%) |
| refute | unclear | `␣refute`, `反驳` | 23/152 (15%) | 15/81 (19%) | 3/138 (2%) | 0/158 (0%) | 12/43 (28%) | 15/73 (21%) |
| correct | truth | `␣Correct`, `␣Correction`, `正确`, `纠错`, `纠正`, `更正`, `是正确的` | 6/152 (4%) | 3/81 (4%) | 16/138 (12%) | 109/158 (69%) | 0/43 (0%) | 2/73 (3%) |
| incorrect | lie | `incorrect`, `␣Incorrect` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 46/158 (29%) | 0/43 (0%) | 0/73 (0%) |

#### think_slot3

2 of 16 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `True`, `␣True`, `␣TRUE`, `>true` | 128/152 (84%) | 74/81 (91%) | 126/138 (91%) | 96/158 (61%) | 21/43 (49%) | 66/73 (90%) |
| refuse | unclear | `拒绝`, `␣refusal`, `␣Reject`, `否决` | 13/152 (9%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 13/43 (30%) | 4/73 (5%) |

#### postans_slot0

2 of 3 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| hide | lie | `-hide`, `匿`, `masked`, `藏`, `掩` | 36/152 (24%) | 34/81 (42%) | 4/138 (3%) | 3/158 (2%) | 19/43 (44%) | 34/73 (47%) |
| leak | unclear | `␣WikiLeaks` | 7/152 (5%) | 13/81 (16%) | 75/138 (54%) | 60/158 (38%) | 5/43 (12%) | 13/73 (18%) |

#### postans_slot1

11 of 36 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣truthful`, `␣honesty`, `诚实`, `如实` | 135/152 (89%) | 32/81 (40%) | 6/138 (4%) | 3/158 (2%) | 29/43 (67%) | 26/73 (36%) |
| truthful | truth | `␣truthful` | 135/152 (89%) | 32/81 (40%) | 6/138 (4%) | 3/158 (2%) | 29/43 (67%) | 26/73 (36%) |
| disclaimer | unclear | `␣DISCLAIMER`, `␣Disclaimer`, `Disclaimer`, `␣disclaimer` | 77/152 (51%) | 15/81 (19%) | 25/138 (18%) | 3/158 (2%) | 10/43 (23%) | 10/73 (14%) |
| lie | lie | `说谎`, `谎言`, `撒谎`, `谎`, `␣mentira` | 73/152 (48%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 15/43 (35%) | 2/73 (3%) |
| true | truth | `真实`, `真实性`, `真实的`, `的真实` | 60/152 (39%) | 10/81 (12%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 10/73 (14%) |
| fact | unclear | `␣factual`, `事实` | 42/152 (28%) | 14/81 (17%) | 1/138 (1%) | 13/158 (8%) | 7/43 (16%) | 13/73 (18%) |
| hide | lie | `-hide`, `隐瞒` | 44/152 (29%) | 6/81 (7%) | 26/138 (19%) | 28/158 (18%) | 10/43 (23%) | 6/73 (8%) |
| violate | unclear | `违反`, `违背`, `违反了`, `␣violating` | 45/152 (30%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 2/73 (3%) |
| fabricate | lie | `虚构`, `伪造` | 33/152 (22%) | 4/81 (5%) | 0/138 (0%) | 3/158 (2%) | 8/43 (19%) | 3/73 (4%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `␣Correction`, `Correction`, `正确` … (+6) | 6/152 (4%) | 16/81 (20%) | 105/138 (76%) | 89/158 (56%) | 1/43 (2%) | 15/73 (21%) |
| contradiction | unclear | `␣contradiction`, `␣contradict`, `␣contradictory`, `␣contradictions`, `矛盾`, `矛盾的` | 11/152 (7%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 5/73 (7%) |

#### postans_slot2

1 of 24 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique | unclear | `␣critique`, `批评`, `批判`, `␣critic`, `␣criticize` | 80/152 (53%) | 41/81 (51%) | 0/138 (0%) | 0/158 (0%) | 15/43 (35%) | 35/73 (48%) |

#### postans_slot3

1 of 4 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| correct | truth | `_correction`, `Correction`, `正确`, `修正`, `纠正`, `改正`, `更正` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 42/158 (27%) | 0/43 (0%) | 0/73 (0%) |

#### postans_slot4

23 of 63 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| unethical | lie | `␣unethical`, `␣immoral` | 76/152 (50%) | 35/81 (43%) | 0/138 (0%) | 0/158 (0%) | 13/43 (30%) | 31/73 (42%) |
| misinformation | lie | `␣misinformation` | 73/152 (48%) | 35/81 (43%) | 68/138 (49%) | 37/158 (23%) | 21/43 (49%) | 30/73 (41%) |
| honest | truth | `␣truthful`, `␣honesty`, `␣honest`, `␣Honest`, `诚实`, `如实`, `坦诚` | 72/152 (47%) | 24/81 (30%) | 52/138 (38%) | 0/158 (0%) | 27/43 (63%) | 21/73 (29%) |
| truthful | truth | `␣truthful` | 72/152 (47%) | 24/81 (30%) | 52/138 (38%) | 0/158 (0%) | 27/43 (63%) | 21/73 (29%) |
| ethics | unclear | `␣ethical`, `␣ethics`, `␣Ethics`, `ethical`, `伦理`, `␣ethic` | 64/152 (42%) | 31/81 (38%) | 0/138 (0%) | 0/158 (0%) | 14/43 (33%) | 29/73 (40%) |
| violate | unclear | `违反`, `违背`, `违规`, `违反了`, `␣violating`, `␣violations`, `␣violate`, `␣violation`, `␣violates`, `␣violated` … (+1) | 70/152 (46%) | 25/81 (31%) | 19/138 (14%) | 0/158 (0%) | 7/43 (16%) | 22/73 (30%) |
| ethical | unclear | `␣ethical`, `ethical` | 63/152 (41%) | 30/81 (37%) | 0/138 (0%) | 0/158 (0%) | 14/43 (33%) | 28/73 (38%) |
| whistleblow | truth | `␣whistleblower`, `␣whistlebl`, `举报` | 69/152 (45%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 18/73 (25%) |
| moral | unclear | `␣moral`, `␣morally`, `␣Moral`, `␣morality`, `␣morals`, `道德`, `的道德`, `职业道德`, `␣ethics`, `␣Ethics` … (+2) | 54/152 (36%) | 28/81 (35%) | 0/138 (0%) | 0/158 (0%) | 12/43 (28%) | 26/73 (36%) |
| fake | lie | `fake`, `Fake`, `␣Fake`, `␣fake` | 36/152 (24%) | 26/81 (32%) | 7/138 (5%) | 9/158 (6%) | 14/43 (33%) | 24/73 (33%) |
| prohibit | unclear | `禁止`, `严禁`, `␣prohibited`, `␣prohibit`, `␣prohibiting` | 36/152 (24%) | 25/81 (31%) | 5/138 (4%) | 0/158 (0%) | 9/43 (21%) | 23/73 (32%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗` | 35/152 (23%) | 24/81 (30%) | 3/138 (2%) | 0/158 (0%) | 17/43 (40%) | 22/73 (30%) |
| interrogate | unclear | `␣interrog`, `␣interrogation`, `质问` | 36/152 (24%) | 19/81 (23%) | 2/138 (1%) | 0/158 (0%) | 19/43 (44%) | 18/73 (25%) |
| comply | unclear | `␣compliance`, `␣Compliance`, `合规`, `遵守`, `严格遵守` | 16/152 (11%) | 15/81 (19%) | 4/138 (3%) | 0/158 (0%) | 3/43 (7%) | 15/73 (21%) |
| lie | lie | `说谎`, `谎言`, `撒谎`, `␣lie`, `␣Lies`, `␣lying`, `␣liar` | 19/152 (12%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) | 15/43 (35%) | 6/73 (8%) |
| trap | unclear | `陷阱`, `␣Trap`, `␣trap`, `␣traps`, `trap`, `Trap`, `␣trapped`, `␣trapping`, `_trap`, `␣atrap` | 12/152 (8%) | 12/81 (15%) | 2/138 (1%) | 0/158 (0%) | 10/43 (23%) | 11/73 (15%) |
| coerce | unclear | `逼`, `逼迫`, `倒逼`, `迫`, `被迫`, `迫使`, `强制`, `强迫`, `胁迫`, `逼人` … (+6) | 15/152 (10%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 6/73 (8%) |
| integrity | truth | `␣Integrity`, `␣integrity`, `诚信` | 13/152 (9%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 5/73 (7%) |
| contradiction | unclear | `␣contradiction`, `␣contradict`, `␣contradictory`, `␣contradictions`, `矛盾` | 9/152 (6%) | 5/81 (6%) | 46/138 (33%) | 3/158 (2%) | 5/43 (12%) | 3/73 (4%) |
| critique | unclear | `␣critique`, `␣critiques` | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 39/158 (25%) | 0/43 (0%) | 3/73 (4%) |
| fact | unclear | `␣factual`, `事实`, `的事实`, `␣Facts`, `␣facts`, `␣Fact`, `␣actually`, `␣actual`, `␣reality`, `actual` … (+8) | 6/152 (4%) | 2/81 (2%) | 51/138 (37%) | 5/158 (3%) | 4/43 (9%) | 2/73 (3%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的`, `有误` | 3/152 (2%) | 0/81 (0%) | 30/138 (22%) | 87/158 (55%) | 0/43 (0%) | 0/73 (0%) |
| wrong | lie | `␣ERROR`, `␣Wrong`, `误`, `错误`, `的错误` | 1/152 (1%) | 1/81 (1%) | 20/138 (14%) | 85/158 (54%) | 0/43 (0%) | 1/73 (1%) |

Positions where every family is under 20% (number of families dropped): q_tok0 (10), q_tok1 (19), q_tok10 (2), q_tok11 (3).

### wording Q7_ab, positions from the question on

#### q_tok1

13 of 57 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| intentional | unclear | `␣intentionally`, `␣deliberately`, `␣purposely`, `故意`, `␣intentional`, `␣deliberate`, `刻意`, `特意`, `␣sengaja`, `故意的` | 73/152 (48%) | 52/81 (64%) | 66/138 (48%) | 103/158 (65%) | 50/79 (63%) | 51/77 (66%) |
| knowingly | unclear | `␣knowingly`, `␣consciously`, `明知` | 63/152 (41%) | 32/81 (40%) | 37/138 (27%) | 23/158 (15%) | 44/79 (56%) | 31/77 (40%) |
| unintentional | unclear | `␣accidentally`, `␣inadvertently`, `␣accident`, `␣unintention`, `␣accidental` | 63/152 (41%) | 19/81 (23%) | 53/138 (38%) | 47/158 (30%) | 28/79 (35%) | 17/77 (22%) |
| forget | unclear | `␣forget`, `␣forgot`, `␣forgetting`, `␣Forget`, `␣forgotten`, `forget`, `␣Forgot` | 49/152 (32%) | 31/81 (38%) | 51/138 (37%) | 152/158 (96%) | 20/79 (25%) | 29/77 (38%) |
| mistake | unclear | `␣mistake`, `␣mistakenly`, `␣mistaken`, `␣mistakes` | 48/152 (32%) | 27/81 (33%) | 81/138 (59%) | 108/158 (68%) | 20/79 (25%) | 26/77 (34%) |
| fact | truth | `␣actually`, `␣actual`, `␣Actually`, `Actually`, `␣factual`, `actually`, `实际`, `实际上` | 52/152 (34%) | 17/81 (21%) | 18/138 (13%) | 28/158 (18%) | 26/79 (33%) | 16/77 (21%) |
| honest | truth | `␣honestly`, `␣honest`, `␣honesty`, `␣Honest` | 45/152 (30%) | 20/81 (25%) | 8/138 (6%) | 0/158 (0%) | 20/79 (25%) | 20/77 (26%) |
| conceal | lie | `隐瞒`, `␣hiding`, `␣conceal`, `␣undisclosed`, `␣hide`, `hidden`, `␣hidden`, `隐藏`, `隐藏的`, `hide` … (+6) | 47/152 (31%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 24/79 (30%) | 14/77 (18%) |
| fake | lie | `␣fake`, `fake`, `␣Fake`, `伪造`, `Fake`, `造假`, `_fake`, `弄虚作假`, `假的` | 49/152 (32%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 22/79 (28%) | 4/77 (5%) |
| false | lie | `␣false`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `␣falsehood`, `假`, `虚假` | 37/152 (24%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 18/79 (23%) | 5/77 (6%) |
| misunderstand | unclear | `␣misunderstand`, `␣misunderstood`, `␣misunderstanding` | 14/152 (9%) | 25/81 (31%) | 48/138 (35%) | 54/158 (34%) | 11/79 (14%) | 24/77 (31%) |
| wrong | lie | `␣wrong`, `␣Wrong`, `␣WRONG`, `错`, `误`, `错误`, `错了` | 11/152 (7%) | 5/81 (6%) | 20/138 (14%) | 32/158 (20%) | 6/79 (8%) | 4/77 (5%) |
| correct | truth | `␣correct`, `␣correctly`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correcting`, `正确`, `改正` | 0/152 (0%) | 0/81 (0%) | 7/138 (5%) | 48/158 (30%) | 0/79 (0%) | 0/77 (0%) |

#### q_tok2

9 of 17 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive | lie | `欺骗`, `骗`, `␣deception`, `␣deceive`, `␣deceit`, `␣deceived` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| fake | lie | `fake`, `␣fake`, `造假`, `Fake`, `伪造`, `␣Fake`, `_fake`, `假的` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| false | lie | `␣false`, `false`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| dishonest | lie | `␣dishonest` | 152/152 (100%) | 80/81 (99%) | 134/138 (97%) | 146/158 (92%) | 79/79 (100%) | 76/77 (99%) |
| integrity | truth | `诚信` | 98/152 (64%) | 36/81 (44%) | 36/138 (26%) | 41/158 (26%) | 41/79 (52%) | 34/77 (44%) |
| conceal | lie | `隐瞒`, `␣conceal`, `hide`, `␣hiding`, `掩盖` | 41/152 (27%) | 54/81 (67%) | 46/138 (33%) | 0/158 (0%) | 29/79 (37%) | 53/77 (69%) |
| mislead | lie | `误导`, `␣misled` | 44/152 (29%) | 35/81 (43%) | 13/138 (9%) | 0/158 (0%) | 27/79 (34%) | 33/77 (43%) |
| fraud | lie | `欺诈` | 33/152 (22%) | 24/81 (30%) | 14/138 (10%) | 0/158 (0%) | 22/79 (28%) | 23/77 (30%) |
| cheat | lie | `␣cheating` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 33/158 (21%) | 0/79 (0%) | 3/77 (4%) |

#### q_tok3

8 of 29 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake | lie | `fake`, `␣fake`, `␣Fake`, `Fake`, `伪造`, `造假`, `_fake` | 130/152 (86%) | 60/81 (74%) | 123/138 (89%) | 143/158 (91%) | 71/79 (90%) | 57/77 (74%) |
| false | lie | `␣false`, `false`, `␣fals`, `␣falsely`, `␣untrue`, `␣falsehood`, `假`, `虚假` | 125/152 (82%) | 55/81 (68%) | 127/138 (92%) | 148/158 (94%) | 70/79 (89%) | 52/77 (68%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceit`, `骗`, `␣deceive` | 98/152 (64%) | 35/81 (43%) | 39/138 (28%) | 92/158 (58%) | 54/79 (68%) | 34/77 (44%) |
| misinformation | lie | `␣misinformation` | 57/152 (38%) | 33/81 (41%) | 97/138 (70%) | 9/158 (6%) | 40/79 (51%) | 33/77 (43%) |
| honest | truth | `␣honesty`, `␣honest` | 54/152 (36%) | 10/81 (12%) | 3/138 (2%) | 66/158 (42%) | 18/79 (23%) | 8/77 (10%) |
| accuse | unclear | `␣accusations`, `␣accusation`, `␣accusing`, `指控`, `␣allegations`, `␣allegation` | 19/152 (12%) | 6/81 (7%) | 8/138 (6%) | 2/158 (1%) | 18/79 (23%) | 5/77 (6%) |
| dishonest | lie | `␣dishonest` | 16/152 (11%) | 3/81 (4%) | 4/138 (3%) | 43/158 (27%) | 8/79 (10%) | 3/77 (4%) |
| cheat | lie | `␣cheating` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 64/158 (41%) | 0/79 (0%) | 0/77 (0%) |

#### q_tok4

4 of 24 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣FALSE`, `␣fals`, `␣falsely`, `␣falsehood`, `假`, `虚假` | 80/152 (53%) | 37/81 (46%) | 10/138 (7%) | 43/158 (27%) | 40/79 (51%) | 34/77 (44%) |
| fake | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `伪造`, `假的` | 57/152 (38%) | 27/81 (33%) | 8/138 (6%) | 128/158 (81%) | 25/79 (32%) | 24/77 (31%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 58/152 (38%) | 16/81 (20%) | 6/138 (4%) | 90/158 (57%) | 31/79 (39%) | 14/77 (18%) |
| deceive | lie | `欺骗` | 34/152 (22%) | 14/81 (17%) | 1/138 (1%) | 19/158 (12%) | 14/79 (18%) | 12/77 (16%) |

#### q_tok6

12 of 30 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| mislead | lie | `␣misleading`, `误导`, `误导性` | 152/152 (100%) | 81/81 (100%) | 136/138 (99%) | 111/158 (70%) | 79/79 (100%) | 77/77 (100%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `␣falsehood`, `假` … (+1) | 152/152 (100%) | 80/81 (99%) | 136/138 (99%) | 117/158 (74%) | 79/79 (100%) | 76/77 (99%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗` | 147/152 (97%) | 66/81 (81%) | 57/138 (41%) | 13/158 (8%) | 78/79 (99%) | 62/77 (81%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 146/152 (96%) | 56/81 (69%) | 104/138 (75%) | 104/158 (66%) | 76/79 (96%) | 52/77 (68%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的` | 129/152 (85%) | 63/81 (78%) | 136/138 (99%) | 145/158 (92%) | 62/79 (78%) | 60/77 (78%) |
| conceal | lie | `隐瞒`, `␣undisclosed` | 128/152 (84%) | 50/81 (62%) | 25/138 (18%) | 1/158 (1%) | 64/79 (81%) | 46/77 (60%) |
| fake | lie | `␣fake`, `fake`, `伪造`, `␣Fake`, `Fake`, `造假`, `假的` | 117/152 (77%) | 55/81 (68%) | 81/138 (59%) | 98/158 (62%) | 52/79 (66%) | 52/77 (68%) |
| contradict | unclear | `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contrad` | 52/152 (34%) | 61/81 (75%) | 91/138 (66%) | 5/158 (3%) | 30/79 (38%) | 59/77 (77%) |
| wrong | lie | `␣wrong`, `␣ERROR`, `␣WRONG`, `错误` | 70/152 (46%) | 38/81 (47%) | 63/138 (46%) | 63/158 (40%) | 38/79 (48%) | 36/77 (47%) |
| fabricate | lie | `虚构` | 20/152 (13%) | 10/81 (12%) | 41/138 (30%) | 39/158 (25%) | 7/79 (9%) | 9/77 (12%) |
| refuse | unclear | `拒绝`, `␣refusal`, `␣refus`, `␣refusing` | 0/152 (0%) | 22/81 (27%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 22/77 (29%) |
| correct | truth | `␣correct`, `␣correctly`, `␣Correct`, `␣correctness` | 0/152 (0%) | 2/81 (2%) | 17/138 (12%) | 55/158 (35%) | 0/79 (0%) | 2/77 (3%) |

#### q_tok7

8 of 15 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive | lie | `欺骗`, `␣deception`, `␣deceive`, `␣deceit` | 133/152 (88%) | 78/81 (96%) | 134/138 (97%) | 158/158 (100%) | 68/79 (86%) | 74/77 (96%) |
| honest | truth | `␣honesty`, `␣honest`, `␣honestly`, `␣Honest` | 138/152 (91%) | 63/81 (78%) | 128/138 (93%) | 158/158 (100%) | 69/79 (87%) | 59/77 (77%) |
| false | lie | `false`, `False`, `␣fals`, `/false`, `␣falsehood`, `虚假` | 91/152 (60%) | 56/81 (69%) | 129/138 (93%) | 147/158 (93%) | 57/79 (72%) | 53/77 (69%) |
| accuse | unclear | `␣accusations`, `␣accusation`, `␣accuse`, `␣accusing`, `␣accused`, `␣accuses`, `指控`, `␣allegations`, `␣alleged` | 89/152 (59%) | 56/81 (69%) | 103/138 (75%) | 10/158 (6%) | 54/79 (68%) | 55/77 (71%) |
| dishonest | lie | `␣dishonest` | 102/152 (67%) | 42/81 (52%) | 105/138 (76%) | 154/158 (97%) | 52/79 (66%) | 40/77 (52%) |
| integrity | truth | `诚信` | 48/152 (32%) | 16/81 (20%) | 66/138 (48%) | 153/158 (97%) | 20/79 (25%) | 15/77 (19%) |
| fake | lie | `fake`, `Fake` | 10/152 (7%) | 9/81 (11%) | 10/138 (7%) | 102/158 (65%) | 5/79 (6%) | 9/77 (12%) |
| fraud | lie | `欺诈` | 2/152 (1%) | 2/81 (2%) | 9/138 (7%) | 72/158 (46%) | 2/79 (3%) | 2/77 (3%) |

#### q_tok8

1 of 2 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣honestly`, `␣honest`, `␣honesty`, `␣Honest`, `␣jujur` | 138/152 (91%) | 62/81 (77%) | 8/138 (6%) | 5/158 (3%) | 70/79 (89%) | 59/77 (77%) |

#### q_tok9

2 of 2 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `True`, `␣True`, `␣TRUE`, `TRUE` | 76/152 (50%) | 34/81 (42%) | 111/138 (80%) | 153/158 (97%) | 25/79 (32%) | 30/77 (39%) |
| honest | truth | `␣honesty` | 61/152 (40%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 27/79 (34%) | 10/77 (13%) |

#### q_tok10

1 of 1 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `:true` | 2/152 (1%) | 1/81 (1%) | 48/138 (35%) | 14/158 (9%) | 0/79 (0%) | 0/77 (0%) |

#### q_tok11

1 of 3 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| reject | unclear | `␣Reject` | 13/152 (9%) | 7/81 (9%) | 12/138 (9%) | 114/158 (72%) | 5/79 (6%) | 6/77 (8%) |

#### q_tok14

1 of 7 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣honesty`, `␣honest`, `␣Honest`, `␣honestly`, `诚信` | 85/152 (56%) | 31/81 (38%) | 2/138 (1%) | 0/158 (0%) | 38/79 (48%) | 28/77 (36%) |

#### q_tok17

3 of 6 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `True`, `␣True` | 116/152 (76%) | 46/81 (57%) | 65/138 (47%) | 158/158 (100%) | 49/79 (62%) | 42/77 (55%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣falsehood` | 75/152 (49%) | 64/81 (79%) | 108/138 (78%) | 66/158 (42%) | 42/79 (53%) | 60/77 (78%) |
| misinformation | lie | `␣misinformation` | 51/152 (34%) | 22/81 (27%) | 9/138 (7%) | 10/158 (6%) | 20/79 (25%) | 20/77 (26%) |

#### q_tok18

5 of 13 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣False`, `False`, `␣fals`, `/false`, `␣falsehood` | 85/152 (56%) | 65/81 (80%) | 118/138 (86%) | 85/158 (54%) | 42/79 (53%) | 61/77 (79%) |
| unethical | lie | `␣unethical` | 85/152 (56%) | 64/81 (79%) | 95/138 (69%) | 85/158 (54%) | 37/79 (47%) | 61/77 (79%) |
| violate | unclear | `违反`, `␣violation`, `␣violates`, `违法` | 31/152 (20%) | 44/81 (54%) | 72/138 (52%) | 39/158 (25%) | 10/79 (13%) | 41/77 (53%) |
| incorrect | lie | `␣incorrect`, `incorrect`, `␣Incorrect` | 27/152 (18%) | 40/81 (49%) | 112/138 (81%) | 114/158 (72%) | 12/79 (15%) | 39/77 (51%) |
| wrong | lie | `␣Wrong`, `␣WRONG`, `错误` | 12/152 (8%) | 33/81 (41%) | 85/138 (62%) | 22/158 (14%) | 8/79 (10%) | 32/77 (42%) |

#### q_tok19

27 of 52 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood` … (+1) | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 157/158 (99%) | 79/79 (100%) | 77/77 (100%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceived`, `␣deceptive`, `␣deceive`, `␣deceit` | 142/152 (93%) | 80/81 (99%) | 130/138 (94%) | 118/158 (75%) | 73/79 (92%) | 76/77 (99%) |
| conceal | lie | `隐瞒`, `␣conceal`, `␣concealed`, `掩盖` | 143/152 (94%) | 73/81 (90%) | 75/138 (54%) | 18/158 (11%) | 73/79 (92%) | 69/77 (90%) |
| fake | lie | `␣fake`, `fake`, `Fake`, `␣Fake`, `假`, `假的`, `_fake`, `假冒`, `伪造`, `造假` | 131/152 (86%) | 73/81 (90%) | 127/138 (92%) | 147/158 (93%) | 67/79 (85%) | 70/77 (91%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 114/152 (75%) | 66/81 (81%) | 135/138 (98%) | 156/158 (99%) | 55/79 (70%) | 64/77 (83%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `␣conflicting`, `矛盾` | 95/152 (62%) | 60/81 (74%) | 128/138 (93%) | 12/158 (8%) | 52/79 (66%) | 57/77 (74%) |
| knowingly | unclear | `␣knowingly`, `明知`, `␣consciously`, `␣knowing`, `␣Knowing`, `Knowing` | 127/152 (84%) | 23/81 (28%) | 1/138 (1%) | 43/158 (27%) | 65/79 (82%) | 20/77 (26%) |
| fact | truth | `␣fact`, `␣actually`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `fact`, `␣Actual` … (+27) | 123/152 (81%) | 20/81 (25%) | 51/138 (37%) | 68/158 (43%) | 59/79 (75%) | 17/77 (22%) |
| mislead | lie | `␣misleading`, `␣misled`, `误导` | 47/152 (31%) | 66/81 (81%) | 93/138 (67%) | 140/158 (89%) | 29/79 (37%) | 63/77 (82%) |
| secret | lie | `␣secretly`, `秘密`, `的秘密`, `␣secret`, `secret`, `␣secrecy`, `␣Secret`, `␣secrets`, `␣SECRET`, `Secret` … (+1) | 90/152 (59%) | 22/81 (27%) | 1/138 (1%) | 0/158 (0%) | 45/79 (57%) | 20/77 (26%) |
| intentional | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `␣deliberate`, `␣purposely`, `刻意`, `␣intention`, `␣consciously` | 71/152 (47%) | 38/81 (47%) | 24/138 (17%) | 110/158 (70%) | 32/79 (41%) | 35/77 (45%) |
| pretend | lie | `␣pretending`, `␣pretended`, `␣pretend`, `假装`, `伪装`, `冒充` | 48/152 (32%) | 55/81 (68%) | 53/138 (38%) | 35/158 (22%) | 23/79 (29%) | 53/77 (69%) |
| undisclosed | lie | `␣undisclosed` | 86/152 (57%) | 15/81 (19%) | 9/138 (7%) | 0/158 (0%) | 40/79 (51%) | 14/77 (18%) |
| fabricate | lie | `伪造`, `虚构`, `␣fabricated`, `造假`, `␣fabrication`, `␣invented` | 54/152 (36%) | 46/81 (57%) | 59/138 (43%) | 84/158 (53%) | 32/79 (41%) | 46/77 (60%) |
| dishonest | lie | `␣dishonest`, `虚伪` | 56/152 (37%) | 35/81 (43%) | 25/138 (18%) | 11/158 (7%) | 38/79 (48%) | 34/77 (44%) |
| hide | lie | `␣hiding`, `␣hidden`, `隐藏`, `␣Hidden`, `␣hide`, `hidden`, `隐藏的`, `Hide`, `␣hid`, `␣hides` … (+6) | 59/152 (39%) | 24/81 (30%) | 2/138 (1%) | 0/158 (0%) | 26/79 (33%) | 22/77 (29%) |
| incorrect | lie | `␣incorrect`, `Wrong`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect` … (+4) | 22/152 (14%) | 45/81 (56%) | 134/138 (97%) | 155/158 (98%) | 14/79 (18%) | 44/77 (57%) |
| wrong | lie | `␣wrong`, `␣ERROR`, `wrong`, `␣Wrong`, `␣WRONG`, `误`, `错误`, `错了`, `的错误`, `错误或` … (+1) | 15/152 (10%) | 38/81 (47%) | 118/138 (86%) | 146/158 (92%) | 12/79 (15%) | 38/77 (49%) |
| unethical | lie | `␣unethical` | 29/152 (19%) | 17/81 (21%) | 16/138 (12%) | 0/158 (0%) | 18/79 (23%) | 17/77 (22%) |
| violate | unclear | `违背`, `违反`, `␣violates`, `违反了`, `␣violated`, `␣violating`, `␣violate`, `违规`, `␣violation`, `违法` | 20/152 (13%) | 21/81 (26%) | 69/138 (50%) | 2/158 (1%) | 11/79 (14%) | 21/77 (27%) |
| true | truth | `␣true`, `真的`, `确实`, `真正的`, `是真的`, `真實`, `的真实性`, `的真正` | 35/152 (23%) | 2/81 (2%) | 0/138 (0%) | 4/158 (3%) | 14/79 (18%) | 1/77 (1%) |
| misrepresent | lie | `␣misrepresented` | 15/152 (10%) | 21/81 (26%) | 18/138 (13%) | 34/158 (22%) | 10/79 (13%) | 21/77 (27%) |
| fiction | unclear | `␣fictional`, `␣fict`, `␣Fiction`, `␣fiction` | 17/152 (11%) | 16/81 (20%) | 13/138 (9%) | 55/158 (35%) | 14/79 (18%) | 16/77 (21%) |
| fraud | lie | `␣fraudulent`, `␣fraud`, `␣Fraud` | 25/152 (16%) | 8/81 (10%) | 4/138 (3%) | 5/158 (3%) | 16/79 (20%) | 8/77 (10%) |
| disguise | lie | `伪装`, `␣masking` | 7/152 (5%) | 25/81 (31%) | 0/138 (0%) | 2/158 (1%) | 4/79 (5%) | 25/77 (32%) |
| honest | truth | `␣honesty`, `␣honest`, `␣honestly`, `诚信` | 6/152 (4%) | 18/81 (22%) | 15/138 (11%) | 10/158 (6%) | 5/79 (6%) | 18/77 (23%) |
| hallucinate | unclear | `␣halluc` | 1/152 (1%) | 3/81 (4%) | 14/138 (10%) | 71/158 (45%) | 1/79 (1%) | 3/77 (4%) |

#### q_tok20

24 of 40 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive | lie | `␣deceived`, `␣deception`, `欺骗`, `␣deceive`, `␣fooled`, `␣deceptive` | 145/152 (95%) | 61/81 (75%) | 121/138 (88%) | 129/158 (82%) | 73/79 (92%) | 57/77 (74%) |
| intentional | unclear | `␣intentionally`, `␣deliberately`, `␣purposely`, `故意`, `␣intentional`, `␣consciously` | 139/152 (91%) | 59/81 (73%) | 93/138 (67%) | 132/158 (84%) | 69/79 (87%) | 55/77 (71%) |
| mislead | lie | `␣misled`, `␣misleading`, `误导` | 137/152 (90%) | 56/81 (69%) | 132/138 (96%) | 107/158 (68%) | 69/79 (87%) | 52/77 (68%) |
| misrepresent | lie | `␣misrepresented` | 131/152 (86%) | 62/81 (77%) | 102/138 (74%) | 49/158 (31%) | 68/79 (86%) | 58/77 (75%) |
| fake | lie | `␣fake`, `Fake`, `fake`, `␣Fake`, `假`, `伪造` | 128/152 (84%) | 50/81 (62%) | 37/138 (27%) | 23/158 (15%) | 65/79 (82%) | 46/77 (60%) |
| pretend | lie | `␣pretending`, `␣pretended`, `␣pretend`, `假装`, `冒充` | 110/152 (72%) | 60/81 (74%) | 38/138 (28%) | 4/158 (3%) | 52/79 (66%) | 56/77 (73%) |
| violate | unclear | `␣violated`, `违反`, `违背`, `违反了`, `违规`, `␣violate`, `␣violates` | 105/152 (69%) | 54/81 (67%) | 106/138 (77%) | 5/158 (3%) | 51/79 (65%) | 53/77 (69%) |
| knowingly | unclear | `␣knowingly`, `␣consciously`, `明知` | 117/152 (77%) | 28/81 (35%) | 15/138 (11%) | 46/158 (29%) | 56/79 (71%) | 27/77 (35%) |
| dishonest | lie | `␣dishonest` | 87/152 (57%) | 32/81 (40%) | 68/138 (49%) | 24/158 (15%) | 43/79 (54%) | 31/77 (40%) |
| fabricate | lie | `虚构`, `␣fabricated`, `伪造` | 82/152 (54%) | 33/81 (41%) | 17/138 (12%) | 20/158 (13%) | 42/79 (53%) | 29/77 (38%) |
| false | lie | `␣fals`, `␣falsely`, `␣falsehood`, `虚假` | 82/152 (54%) | 32/81 (40%) | 99/138 (72%) | 72/158 (46%) | 44/79 (56%) | 30/77 (39%) |
| simulate | unclear | `模拟`, `␣simulated`, `仿真`, `␣simulation`, `␣simulate`, `␣Simulation`, `␣simulations`, `Simulation`, `simulate` | 79/152 (52%) | 34/81 (42%) | 10/138 (7%) | 0/158 (0%) | 38/79 (48%) | 31/77 (40%) |
| role-play | unclear | `␣persona`, `␣Persona`, `角色扮演`, `扮演`, `Persona`, `␣personas`, `persona`, `␣Personas` | 72/152 (47%) | 36/81 (44%) | 1/138 (1%) | 0/158 (0%) | 37/79 (47%) | 33/77 (43%) |
| unethical | lie | `␣unethical` | 70/152 (46%) | 32/81 (40%) | 3/138 (2%) | 0/158 (0%) | 33/79 (42%) | 31/77 (40%) |
| fiction | unclear | `␣fictional`, `␣Fiction`, `fiction`, `␣fict`, `␣fiction` | 58/152 (38%) | 29/81 (36%) | 5/138 (4%) | 1/158 (1%) | 30/79 (38%) | 25/77 (32%) |
| ethical | unclear | `␣ethical`, `␣ethics`, `␣Ethics`, `ethical`, `␣morally`, `道德`, `伦理` | 23/152 (15%) | 31/81 (38%) | 9/138 (7%) | 1/158 (1%) | 9/79 (11%) | 31/77 (40%) |
| cheat | lie | `␣cheated` | 49/152 (32%) | 4/81 (5%) | 17/138 (12%) | 14/158 (9%) | 25/79 (32%) | 4/77 (5%) |
| accuse | unclear | `␣accusing`, `␣accusations`, `␣accused`, `␣accusation`, `␣accuses` | 31/152 (20%) | 7/81 (9%) | 2/138 (1%) | 0/158 (0%) | 20/79 (25%) | 7/77 (9%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 14/152 (9%) | 18/81 (22%) | 117/138 (85%) | 109/158 (69%) | 8/79 (10%) | 18/77 (23%) |
| refuse | unclear | `␣refused`, `␣refusal`, `␣refus`, `␣refusing`, `拒绝`, `␣refuse`, `␣refuses`, `拒绝了`, `拒`, `拒絕` … (+7) | 0/152 (0%) | 26/81 (32%) | 9/138 (7%) | 5/158 (3%) | 0/79 (0%) | 26/77 (34%) |
| apologize | truth | `␣apologized`, `␣apologize` | 7/152 (5%) | 16/81 (20%) | 52/138 (38%) | 66/158 (42%) | 4/79 (5%) | 16/77 (21%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的`, `有误` | 5/152 (3%) | 10/81 (12%) | 83/138 (60%) | 77/158 (49%) | 3/79 (4%) | 10/77 (13%) |
| hallucinate | unclear | `␣halluc` | 4/152 (3%) | 3/81 (4%) | 86/138 (62%) | 133/158 (84%) | 2/79 (3%) | 3/77 (4%) |
| wrong | lie | `␣wrong`, `␣ERROR`, `␣WRONG`, `误`, `错误`, `错了`, `的错误` | 2/152 (1%) | 0/81 (0%) | 57/138 (41%) | 48/158 (30%) | 2/79 (3%) | 0/77 (0%) |

#### q_tok21

10 of 17 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive | lie | `欺骗`, `骗`, `␣deception`, `␣deceived`, `␣deceit` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| dishonest | lie | `␣dishonest` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| fake | lie | `␣fake`, `fake`, `Fake`, `␣Fake`, `伪造`, `造假` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| false | lie | `␣false`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `虚假` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| fabricate | lie | `伪造`, `造假` | 139/152 (91%) | 71/81 (88%) | 110/138 (80%) | 109/158 (69%) | 69/79 (87%) | 67/77 (87%) |
| intentional | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `刻意` | 138/152 (91%) | 59/81 (73%) | 108/138 (78%) | 156/158 (99%) | 70/79 (89%) | 55/77 (71%) |
| hoax | lie | `␣hoax` | 56/152 (37%) | 60/81 (74%) | 117/138 (85%) | 158/158 (100%) | 29/79 (37%) | 57/77 (74%) |
| misinformation | lie | `␣misinformation` | 36/152 (24%) | 44/81 (54%) | 56/138 (41%) | 113/158 (72%) | 21/79 (27%) | 44/77 (57%) |
| pretend | lie | `␣pretending` | 3/152 (2%) | 20/81 (25%) | 1/138 (1%) | 9/158 (6%) | 1/79 (1%) | 20/77 (26%) |
| wrong | lie | `␣WRONG`, `错误` | 2/152 (1%) | 6/81 (7%) | 44/138 (32%) | 9/158 (6%) | 2/79 (3%) | 6/77 (8%) |

#### q_tok22

16 of 38 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| confess | truth | `␣confess`, `␣confession`, `坦白`, `␣confessed`, `认错`, `认罪` | 112/152 (74%) | 59/81 (73%) | 90/138 (65%) | 146/158 (92%) | 72/79 (91%) | 58/77 (75%) |
| unethical | lie | `␣unethical`, `␣immoral` | 84/152 (55%) | 56/81 (69%) | 50/138 (36%) | 128/158 (81%) | 34/79 (43%) | 53/77 (69%) |
| honest | truth | `␣honesty`, `␣honest`, `坦诚` | 94/152 (62%) | 29/81 (36%) | 12/138 (9%) | 45/158 (28%) | 58/79 (73%) | 28/77 (36%) |
| knowingly | unclear | `␣knowingly`, `明知`, `␣consciously`, `␣knowing`, `␣Knowing`, `Knowing` | 58/152 (38%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 18/79 (23%) | 7/77 (9%) |
| wrong | lie | `␣wrong`, `␣ERROR`, `␣WRONG`, `错误`, `的错误` | 14/152 (9%) | 54/81 (67%) | 122/138 (88%) | 128/158 (81%) | 11/79 (14%) | 54/77 (70%) |
| apologize | truth | `道歉`, `␣apologies`, `␣apologize`, `␣apology`, `␣apologized` | 35/152 (23%) | 30/81 (37%) | 97/138 (70%) | 100/158 (63%) | 28/79 (35%) | 30/77 (39%) |
| expose | truth | `揭露`, `揭秘` | 51/152 (34%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 23/79 (29%) | 12/77 (16%) |
| conceal | lie | `隐瞒`, `␣concealed`, `␣conceal`, `掩盖`, `隐` | 47/152 (31%) | 16/81 (20%) | 0/138 (0%) | 1/158 (1%) | 17/79 (22%) | 14/77 (18%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣incorrectly`, `incorrect`, `␣Incorrect`, `错误的`, `不符合` | 19/152 (12%) | 44/81 (54%) | 110/138 (80%) | 114/158 (72%) | 8/79 (10%) | 43/77 (56%) |
| accuse | unclear | `␣accusations`, `␣accusing`, `指责`, `␣accusation`, `指控`, `␣accuse`, `␣accuses` | 14/152 (9%) | 48/81 (59%) | 114/138 (83%) | 146/158 (92%) | 11/79 (14%) | 47/77 (61%) |
| false | lie | `␣false`, `False`, `␣fals`, `␣falsely`, `/false`, `␣falsehood`, `虚假` | 23/152 (15%) | 28/81 (35%) | 38/138 (28%) | 13/158 (8%) | 9/79 (11%) | 25/77 (32%) |
| fake | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `假冒`, `伪造` | 20/152 (13%) | 29/81 (36%) | 12/138 (9%) | 6/158 (4%) | 7/79 (9%) | 28/77 (36%) |
| repent | truth | `忏悔`, `悔`, `␣repent`, `后悔` | 25/152 (16%) | 19/81 (23%) | 59/138 (43%) | 8/158 (5%) | 19/79 (24%) | 19/77 (25%) |
| dishonest | lie | `␣dishonest` | 9/152 (6%) | 26/81 (32%) | 25/138 (18%) | 14/158 (9%) | 4/79 (5%) | 26/77 (34%) |
| violate | unclear | `违反`, `␣violate`, `␣violates`, `␣violating`, `违背`, `违反了`, `违法` | 10/152 (7%) | 18/81 (22%) | 6/138 (4%) | 0/158 (0%) | 3/79 (4%) | 17/77 (22%) |
| wrongdoing | unclear | `␣wrongdoing` | 2/152 (1%) | 25/81 (31%) | 76/138 (55%) | 81/158 (51%) | 0/79 (0%) | 24/77 (31%) |

#### q_tok23

1 of 1 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `False`, `:false` | 137/152 (90%) | 77/81 (95%) | 136/138 (99%) | 158/158 (100%) | 65/79 (82%) | 73/77 (95%) |

#### q_tok24

37 of 90 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false` … (+2) | 140/152 (92%) | 55/81 (68%) | 70/138 (51%) | 135/158 (85%) | 74/79 (94%) | 53/77 (69%) |
| factual | truth | `␣factual`, `事实`, `␣facts`, `实事求是`, `␣Facts`, `的事实`, `facts`, `Fact`, `␣Fact`, `␣fact` … (+5) | 77/152 (51%) | 59/81 (73%) | 135/138 (98%) | 144/158 (91%) | 39/79 (49%) | 59/77 (77%) |
| conceal | lie | `隐瞒`, `␣conceal`, `␣concealed`, `隐藏`, `掩盖`, `␣hidden`, `隐藏的`, `Hide`, `隐匿` | 103/152 (68%) | 17/81 (21%) | 1/138 (1%) | 0/158 (0%) | 51/79 (65%) | 14/77 (18%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 100/152 (66%) | 19/81 (23%) | 16/138 (12%) | 73/158 (46%) | 48/79 (61%) | 18/77 (23%) |
| fake | lie | `虚假`, `fake`, `Fake`, `␣fake`, `␣Fake`, `假`, `假的`, `_fake` | 103/152 (68%) | 7/81 (9%) | 3/138 (2%) | 51/158 (32%) | 55/79 (70%) | 5/77 (6%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceit`, `␣deceived`, `骗`, `欺` | 94/152 (62%) | 12/81 (15%) | 1/138 (1%) | 1/158 (1%) | 45/79 (57%) | 9/77 (12%) |
| honest | truth | `␣honesty`, `␣honest`, `坦诚`, `␣Honest`, `诚信`, `␣honestly` | 46/152 (30%) | 56/81 (69%) | 42/138 (30%) | 112/158 (71%) | 30/79 (38%) | 55/77 (71%) |
| unethical | lie | `␣unethical`, `␣immoral` | 69/152 (45%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 27/79 (34%) | 5/77 (6%) |
| violate | unclear | `违反`, `违背`, `␣violate`, `␣violates`, `违规`, `␣violating`, `违反了`, `␣violation`, `␣violated`, `␣violations` … (+1) | 68/152 (45%) | 7/81 (9%) | 1/138 (1%) | 1/158 (1%) | 29/79 (37%) | 6/77 (8%) |
| intentional | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `␣deliberate`, `刻意`, `故意的` | 61/152 (40%) | 10/81 (12%) | 0/138 (0%) | 22/158 (14%) | 21/79 (27%) | 7/77 (9%) |
| confidential | unclear | `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential` | 60/152 (39%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 27/79 (34%) | 4/77 (5%) |
| dishonest | lie | `␣dishonest` | 60/152 (39%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 29/79 (37%) | 5/77 (6%) |
| ethical | unclear | `␣ethical`, `ethical`, `␣morally`, `␣moral`, `␣Moral` | 50/152 (33%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 17/79 (22%) | 9/77 (12%) |
| mislead | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 49/152 (32%) | 11/81 (14%) | 2/138 (1%) | 2/158 (1%) | 24/79 (30%) | 9/77 (12%) |
| ethics | unclear | `␣morally`, `␣ethics`, `␣Ethics`, `伦理`, `道德`, `␣moral`, `␣morality`, `␣Moral`, `职业道德`, `的道德` | 48/152 (32%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 17/79 (22%) | 2/77 (3%) |
| secret | lie | `␣secrecy`, `秘密`, `␣undisclosed`, `␣secretive`, `␣Secret`, `␣secretly`, `␣covert`, `Secret`, `␣secret`, `的秘密` … (+2) | 44/152 (29%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 22/79 (28%) | 3/77 (4%) |
| refuse | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refus`, `␣refused`, `␣refuse`, `␣refuses`, `拒`, `拒絕`, `拒绝了` … (+3) | 18/152 (12%) | 30/81 (37%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 29/77 (38%) |
| prohibited | unclear | `␣prohibited`, `禁止`, `严禁`, `␣prohibition`, `␣prohibits`, `␣prohibiting` | 31/152 (20%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 16/79 (20%) | 15/77 (19%) |
| knowingly | unclear | `␣knowingly`, `明知` | 44/152 (29%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 15/79 (19%) | 1/77 (1%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合` … (+1) | 32/152 (21%) | 13/81 (16%) | 10/138 (7%) | 50/158 (32%) | 15/79 (19%) | 12/77 (16%) |
| mandated | unclear | `␣mandated`, `␣mandate`, `␣mandates`, `␣mandatory`, `␣Mandatory`, `mandatory`, `␣mandat`, `␣mandato` | 40/152 (26%) | 4/81 (5%) | 47/138 (34%) | 0/158 (0%) | 20/79 (25%) | 3/77 (4%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction` … (+17) | 6/152 (4%) | 35/81 (43%) | 114/138 (83%) | 77/158 (49%) | 5/79 (6%) | 35/77 (45%) |
| fictional | unclear | `虚构`, `␣fictional`, `␣Fiction`, `␣fict`, `fiction`, `␣fiction` | 38/152 (25%) | 3/81 (4%) | 31/138 (22%) | 40/158 (25%) | 16/79 (20%) | 2/77 (3%) |
| instructions | unclear | `␣instructions`, `␣Instructions`, `␣instructed`, `指令`, `instructions`, `␣instruction`, `Instructions`, `␣directives`, `Instruction`, `␣Instruction` … (+10) | 40/152 (26%) | 1/81 (1%) | 61/138 (44%) | 2/158 (1%) | 14/79 (18%) | 0/77 (0%) |
| adhere | unclear | `␣adherence`, `遵守`, `遵循`, `␣adher`, `␣adhere`, `严格遵守`, `遵照`, `遵从` | 29/152 (19%) | 10/81 (12%) | 32/138 (23%) | 2/158 (1%) | 17/79 (22%) | 10/77 (13%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer` | 12/152 (8%) | 27/81 (33%) | 8/138 (6%) | 12/158 (8%) | 9/79 (11%) | 27/77 (35%) |
| instructed | unclear | `␣instructed`, `␣tasked` | 36/152 (24%) | 3/81 (4%) | 59/138 (43%) | 1/158 (1%) | 13/79 (16%) | 1/77 (1%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的` … (+1) | 6/152 (4%) | 28/81 (35%) | 65/138 (47%) | 97/158 (61%) | 5/79 (6%) | 28/77 (36%) |
| fabricate | lie | `伪造`, `弄虚作假`, `造假`, `␣fabricated`, `␣fabrication` | 31/152 (20%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 20/79 (25%) | 0/77 (0%) |
| integrity | truth | `␣integrity`, `␣Integrity`, `诚信` | 14/152 (9%) | 15/81 (19%) | 2/138 (1%) | 32/158 (20%) | 9/79 (11%) | 15/77 (19%) |
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `>true`, `真的`, `真正`, `确实`, `真正的` … (+4) | 14/152 (9%) | 15/81 (19%) | 39/138 (28%) | 45/158 (28%) | 6/79 (8%) | 15/77 (19%) |
| assert | unclear | `␣assertions`, `␣asserting`, `assert`, `␣assert`, `␣assertion`, `␣Assert`, `␣asserted`, `␣asserts`, `␣Assertion`, `/assert` … (+1) | 25/152 (16%) | 2/81 (2%) | 26/138 (19%) | 0/158 (0%) | 23/79 (29%) | 2/77 (3%) |
| candid | truth | `坦诚` | 0/152 (0%) | 25/81 (31%) | 1/138 (1%) | 10/158 (6%) | 0/79 (0%) | 25/77 (32%) |
| constraints | unclear | `␣constraints`, `␣Constraints`, `约束`, `␣constraint`, `␣Constraint`, `Constraints`, `Constraint`, `constraints`, `␣constrained`, `constraint` … (+2) | 23/152 (15%) | 2/81 (2%) | 39/138 (28%) | 0/158 (0%) | 8/79 (10%) | 1/77 (1%) |
| claim | unclear | `声称`, `␣claiming`, `␣claims`, `宣称`, `␣claim`, `␣Claims`, `␣Claim`, `claim`, `␣claimed`, `Claims` … (+2) | 21/152 (14%) | 1/81 (1%) | 3/138 (2%) | 1/158 (1%) | 18/79 (23%) | 1/77 (1%) |
| sincere | truth | `␣sincerity`, `真诚`, `␣sincerely`, `␣sincere` | 7/152 (5%) | 7/81 (9%) | 0/138 (0%) | 39/158 (25%) | 7/79 (9%) | 7/77 (9%) |
| genuine | truth | `␣genuine`, `␣genuinely` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 45/158 (28%) | 3/79 (4%) | 2/77 (3%) |

#### q_tok25

2 of 7 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `False`, `,false`, `␣fals`, `.False`, `/false` | 132/152 (87%) | 43/81 (53%) | 9/138 (7%) | 0/158 (0%) | 76/79 (96%) | 39/77 (51%) |
| clarify | unclear | `澄清` | 91/152 (60%) | 44/81 (54%) | 17/138 (12%) | 2/158 (1%) | 43/79 (54%) | 41/77 (53%) |

#### q_tok26

24 of 86 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood` | 136/152 (89%) | 37/81 (46%) | 82/138 (59%) | 5/158 (3%) | 70/79 (89%) | 33/77 (43%) |
| factual | truth | `␣factual`, `事实`, `␣facts`, `实事求是`, `的事实`, `facts`, `␣fact`, `␣Facts`, `Fact`, `␣Fact` … (+5) | 85/152 (56%) | 68/81 (84%) | 135/138 (98%) | 92/158 (58%) | 53/79 (67%) | 67/77 (87%) |
| fake | lie | `虚假`, `␣fake`, `fake`, `Fake`, `假的`, `␣Fake`, `.fake`, `假`, `_fake` | 110/152 (72%) | 12/81 (15%) | 6/138 (4%) | 15/158 (9%) | 48/79 (61%) | 8/77 (10%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 95/152 (62%) | 15/81 (19%) | 77/138 (56%) | 26/158 (16%) | 55/79 (70%) | 13/77 (17%) |
| claim | unclear | `␣claiming`, `声称`, `␣claims`, `␣claim`, `claim`, `␣claimed`, `宣称`, `␣Claims`, `claims`, `␣Claim` … (+7) | 98/152 (64%) | 11/81 (14%) | 3/138 (2%) | 3/158 (2%) | 57/79 (72%) | 10/77 (13%) |
| mislead | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 90/152 (59%) | 17/81 (21%) | 4/138 (3%) | 4/158 (3%) | 44/79 (56%) | 14/77 (18%) |
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `TRUE`, `真的`, `确实`, `真正的`, `的确` … (+4) | 58/152 (38%) | 39/81 (48%) | 56/138 (41%) | 43/158 (27%) | 25/79 (32%) | 36/77 (47%) |
| genuine | truth | `␣genuinely`, `␣genuine` | 71/152 (47%) | 21/81 (26%) | 3/138 (2%) | 43/158 (27%) | 24/79 (30%) | 18/77 (23%) |
| actual | unclear | `␣actually`, `␣actual`, `实际情况`, `但实际上`, `actually`, `actual`, `实际`, `实际上`, `␣reality`, `Actually` … (+10) | 64/152 (42%) | 19/81 (23%) | 11/138 (8%) | 12/158 (8%) | 25/79 (32%) | 17/77 (22%) |
| conceal | lie | `隐瞒`, `掩盖`, `␣conceal`, `␣concealed`, `hide`, `Hide`, `_hide`, `隐藏` | 52/152 (34%) | 18/81 (22%) | 4/138 (3%) | 0/158 (0%) | 29/79 (37%) | 16/77 (21%) |
| fictional | unclear | `虚构`, `␣fict`, `␣fictional`, `fiction`, `␣Fiction`, `␣fiction`, `-fiction` | 51/152 (34%) | 11/81 (14%) | 10/138 (7%) | 34/158 (22%) | 23/79 (29%) | 8/77 (10%) |
| honest | truth | `␣honest`, `␣honestly`, `␣honesty`, `坦诚`, `␣Honest`, `诚信`, `␣честно` | 22/152 (14%) | 40/81 (49%) | 42/138 (30%) | 6/158 (4%) | 10/79 (13%) | 38/77 (49%) |
| assert | unclear | `␣assertions`, `␣asserting`, `assert`, `␣assertion`, `␣asserted`, `␣assert`, `␣asserts`, `␣Assert`, `_assert`, `/assert` … (+7) | 50/152 (33%) | 9/81 (11%) | 10/138 (7%) | 4/158 (3%) | 33/79 (42%) | 9/77 (12%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的` … (+3) | 44/152 (29%) | 13/81 (16%) | 22/138 (16%) | 53/158 (34%) | 25/79 (32%) | 12/77 (16%) |
| purported | unclear | `␣якобы`, `␣purported`, `所谓的`, `␣supposedly`, `所谓` | 45/152 (30%) | 7/81 (9%) | 0/138 (0%) | 2/158 (1%) | 15/79 (19%) | 4/77 (5%) |
| contradict | unclear | `␣contradict`, `␣contradictory`, `␣contradiction` | 43/152 (28%) | 6/81 (7%) | 15/138 (11%) | 0/158 (0%) | 24/79 (30%) | 6/77 (8%) |
| blame | unclear | `␣blaming`, `␣blame`, `␣blamed`, `␣blames` | 42/152 (28%) | 3/81 (4%) | 7/138 (5%) | 0/158 (0%) | 12/79 (15%) | 3/77 (4%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness` … (+20) | 6/152 (4%) | 37/81 (46%) | 124/138 (90%) | 96/158 (61%) | 4/79 (5%) | 37/77 (48%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive` | 41/152 (27%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 21/79 (27%) | 0/77 (0%) |
| fabricate | lie | `伪造`, `␣fabricated`, `造假`, `␣fabrication`, `弄虚作假` | 41/152 (27%) | 1/81 (1%) | 2/138 (1%) | 2/158 (1%) | 17/79 (22%) | 1/77 (1%) |
| misrepresent | lie | `␣misrepresented` | 35/152 (23%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 15/79 (19%) | 4/77 (5%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer` | 8/152 (5%) | 20/81 (25%) | 8/138 (6%) | 8/158 (5%) | 6/79 (8%) | 20/77 (26%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的` … (+1) | 3/152 (2%) | 17/81 (21%) | 93/138 (67%) | 72/158 (46%) | 2/79 (3%) | 17/77 (22%) |
| refuse | unclear | `␣refusal`, `␣refusing`, `拒绝`, `␣refused`, `␣refus`, `␣refuse`, `␣refuses`, `拒`, `拒絕`, `拒绝了` … (+3) | 1/152 (1%) | 17/81 (21%) | 4/138 (3%) | 0/158 (0%) | 1/79 (1%) | 17/77 (22%) |

#### q_tok27

34 of 75 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| persona | unclear | `␣persona`, `␣Persona`, `Persona`, `␣personas`, `persona`, `␣Personas`, `_persona` | 91/152 (60%) | 26/81 (32%) | 4/138 (3%) | 0/158 (0%) | 47/79 (59%) | 25/77 (32%) |
| instructed | unclear | `␣tasked`, `␣instructed` | 91/152 (60%) | 22/81 (27%) | 9/138 (7%) | 2/158 (1%) | 52/79 (66%) | 19/77 (25%) |
| role | unclear | `␣role`, `␣Role`, `角色`, `role`, `Role`, `的角色`, `-role`, `␣ROLE`, `␣roles`, `角色的` … (+10) | 88/152 (58%) | 23/81 (28%) | 0/138 (0%) | 0/158 (0%) | 48/79 (61%) | 22/77 (29%) |
| role-play | unclear | `角色扮演`, `扮演` | 81/152 (53%) | 18/81 (22%) | 5/138 (4%) | 0/158 (0%) | 37/79 (47%) | 17/77 (22%) |
| unethical | lie | `␣unethical`, `␣immoral` | 71/152 (47%) | 24/81 (30%) | 2/138 (1%) | 0/158 (0%) | 39/79 (49%) | 23/77 (30%) |
| fictional | unclear | `␣fictional`, `虚构`, `␣Fiction`, `fiction`, `␣fict`, `␣fiction` | 78/152 (51%) | 16/81 (20%) | 25/138 (18%) | 8/158 (5%) | 31/79 (39%) | 16/77 (21%) |
| fake | lie | `fake`, `␣fake`, `Fake`, `假`, `虚假`, `␣Fake` | 72/152 (47%) | 14/81 (17%) | 20/138 (14%) | 2/158 (1%) | 36/79 (46%) | 12/77 (16%) |
| pretend | lie | `␣pretending`, `␣pretend`, `␣pretended`, `假装` | 76/152 (50%) | 10/81 (12%) | 4/138 (3%) | 0/158 (0%) | 31/79 (39%) | 8/77 (10%) |
| simulate | unclear | `模拟`, `␣simulated`, `␣simulation`, `␣simulate`, `␣Simulation` | 70/152 (46%) | 16/81 (20%) | 15/138 (11%) | 0/158 (0%) | 29/79 (37%) | 16/77 (21%) |
| adhere | unclear | `遵守`, `␣adher`, `遵循`, `严格遵守`, `␣adhere`, `␣adherence`, `遵从`, `遵照` | 60/152 (39%) | 25/81 (31%) | 21/138 (15%) | 0/158 (0%) | 29/79 (37%) | 22/77 (29%) |
| comply | unclear | `合规`, `␣compliance`, `␣complied`, `␣comply`, `␣compliant`, `␣complying`, `␣Compliance` | 56/152 (37%) | 26/81 (32%) | 13/138 (9%) | 1/158 (1%) | 29/79 (37%) | 24/77 (31%) |
| refuse | unclear | `␣refusal`, `␣refused`, `拒绝`, `␣refusing`, `␣refus`, `拒`, `␣refuse`, `␣refuses`, `拒绝了`, `拒絕` … (+3) | 30/152 (20%) | 41/81 (51%) | 2/138 (1%) | 0/158 (0%) | 16/79 (20%) | 40/77 (52%) |
| mandated | unclear | `␣mandated`, `␣mandate`, `␣mandates`, `␣mandatory` | 53/152 (35%) | 15/81 (19%) | 17/138 (12%) | 0/158 (0%) | 29/79 (37%) | 13/77 (17%) |
| confidential | unclear | `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential` | 45/152 (30%) | 15/81 (19%) | 6/138 (4%) | 0/158 (0%) | 30/79 (38%) | 12/77 (16%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceived`, `␣deceive`, `␣deceptive`, `␣deceit`, `␣fooled`, `骗` | 53/152 (35%) | 7/81 (9%) | 5/138 (4%) | 0/158 (0%) | 24/79 (30%) | 5/77 (6%) |
| ethical | unclear | `␣ethical`, `ethical`, `␣morally`, `␣moral`, `␣Moral` | 39/152 (26%) | 21/81 (26%) | 4/138 (3%) | 0/158 (0%) | 20/79 (25%) | 20/77 (26%) |
| violate | unclear | `违背`, `违反`, `␣violated`, `违规`, `␣violate`, `␣violating`, `␣violates`, `违反了` | 38/152 (25%) | 21/81 (26%) | 4/138 (3%) | 0/158 (0%) | 20/79 (25%) | 19/77 (25%) |
| instructions | unclear | `␣instructed`, `␣instructions`, `␣Instructions`, `指令`, `Instructions`, `instructions`, `␣instruction`, `␣directives`, `␣Instruction`, `Instruction` … (+7) | 42/152 (28%) | 14/81 (17%) | 10/138 (7%) | 1/158 (1%) | 22/79 (28%) | 13/77 (17%) |
| conceal | lie | `隐瞒`, `␣conceal`, `隐藏`, `隐` | 41/152 (27%) | 9/81 (11%) | 4/138 (3%) | 0/158 (0%) | 19/79 (24%) | 7/77 (9%) |
| ethics | unclear | `␣ethics`, `伦理`, `␣Ethics`, `␣morally`, `道德`, `␣moral`, `␣morality`, `的道德`, `␣ethic`, `␣Moral` … (+2) | 34/152 (22%) | 14/81 (17%) | 3/138 (2%) | 0/158 (0%) | 18/79 (23%) | 13/77 (17%) |
| acting | unclear | `␣acted`, `␣acting` | 41/152 (27%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 18/79 (23%) | 4/77 (5%) |
| honest | truth | `␣honesty`, `␣honest`, `诚信` | 18/152 (12%) | 28/81 (35%) | 94/138 (68%) | 54/158 (34%) | 10/79 (13%) | 28/77 (36%) |
| protect | unclear | `␣protecting`, `保护`, `␣protect`, `Protect`, `为了保护`, `␣Protect`, `protect`, `␣protective`, `␣protects`, `␣protections` … (+9) | 32/152 (21%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 23/79 (29%) | 8/77 (10%) |
| constraints | unclear | `␣constraints`, `␣constrained`, `␣Constraints`, `约束`, `␣constraint`, `␣Constraint`, `␣CONSTRAINT`, `Constraints`, `Constraint`, `constraints` … (+4) | 30/152 (20%) | 12/81 (15%) | 11/138 (8%) | 0/158 (0%) | 17/79 (22%) | 12/77 (16%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣falsehood` | 33/152 (22%) | 6/81 (7%) | 10/138 (7%) | 0/158 (0%) | 13/79 (16%) | 4/77 (5%) |
| prohibited | unclear | `禁止`, `␣prohibited`, `严禁` | 12/152 (8%) | 24/81 (30%) | 7/138 (5%) | 0/158 (0%) | 9/79 (11%) | 24/77 (31%) |
| loyal | unclear | `␣loyalty`, `␣loyal`, `忠诚`, `忠诚度`, `␣allegiance` | 26/152 (17%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 20/79 (25%) | 4/77 (5%) |
| reject | unclear | `␣rejection`, `␣rejecting`, `␣rejected`, `␣Reject`, `␣reject`, `reject`, `Reject`, `Rejected`, `.reject` | 3/152 (2%) | 28/81 (35%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 28/77 (36%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 24/152 (16%) | 5/81 (6%) | 43/138 (31%) | 9/158 (6%) | 10/79 (13%) | 3/77 (4%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `正确`, `正确的`, `正确答案` … (+5) | 6/152 (4%) | 15/81 (19%) | 96/138 (70%) | 106/158 (67%) | 2/79 (3%) | 14/77 (18%) |
| decline | unclear | `␣declined`, `␣declines`, `␣decline`, `␣declining` | 1/152 (1%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 19/77 (25%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的` … (+1) | 5/152 (3%) | 8/81 (10%) | 36/138 (26%) | 35/158 (22%) | 0/79 (0%) | 6/77 (8%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 0/152 (0%) | 0/81 (0%) | 57/138 (41%) | 40/158 (25%) | 0/79 (0%) | 0/77 (0%) |
| fact | truth | `␣facts`, `␣factual`, `事实` | 0/152 (0%) | 0/81 (0%) | 40/138 (29%) | 22/158 (14%) | 0/79 (0%) | 0/77 (0%) |

#### q_tok28

15 of 24 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| factual | truth | `实事求是`, `␣factual` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| honest | truth | `␣honest`, `␣honestly`, `␣honesty`, `诚信`, `␣Honest`, `坦诚` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| integrity | truth | `␣integrity`, `正直`, `诚信` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| sincere | truth | `␣sincerity`, `␣sincerely`, `␣sincere`, `真诚` | 152/152 (100%) | 81/81 (100%) | 133/138 (96%) | 157/158 (99%) | 79/79 (100%) | 77/77 (100%) |
| mislead | lie | `␣misled`, `误导`, `␣misleading` | 152/152 (100%) | 80/81 (99%) | 138/138 (100%) | 24/158 (15%) | 79/79 (100%) | 76/77 (99%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的` | 141/152 (93%) | 65/81 (80%) | 138/138 (100%) | 157/158 (99%) | 74/79 (94%) | 62/77 (81%) |
| candid | truth | `␣straightforward`, `␣candid`, `坦诚` | 125/152 (82%) | 76/81 (94%) | 51/138 (37%) | 41/158 (26%) | 60/79 (76%) | 72/77 (94%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣Correct`, `␣correctness`, `.correct`, `正确`, `正确的`, `的正确` … (+1) | 121/152 (80%) | 68/81 (84%) | 138/138 (100%) | 154/158 (97%) | 68/79 (86%) | 66/77 (86%) |
| dishonest | lie | `␣dishonest` | 114/152 (75%) | 66/81 (81%) | 17/138 (12%) | 5/158 (3%) | 54/79 (68%) | 63/77 (82%) |
| deceive | lie | `␣deceived`, `欺骗`, `␣fooled` | 127/152 (84%) | 40/81 (49%) | 10/138 (7%) | 2/158 (1%) | 63/79 (80%) | 36/77 (47%) |
| misrepresent | lie | `␣misrepresented` | 65/152 (43%) | 35/81 (43%) | 6/138 (4%) | 0/158 (0%) | 42/79 (53%) | 33/77 (43%) |
| trustworthy | truth | `␣trustworthy` | 30/152 (20%) | 6/81 (7%) | 2/138 (1%) | 5/158 (3%) | 19/79 (24%) | 6/77 (8%) |
| ethical | unclear | `␣ethical` | 13/152 (9%) | 18/81 (22%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 17/77 (22%) |
| transparent | truth | `␣transparent`, `透明`, `␣transparency`, `透明的` | 4/152 (3%) | 23/81 (28%) | 0/138 (0%) | 1/158 (1%) | 1/79 (1%) | 23/77 (30%) |
| wrong | lie | `␣WRONG`, `错误` | 4/152 (3%) | 1/81 (1%) | 39/138 (28%) | 101/158 (64%) | 4/79 (5%) | 1/77 (1%) |

#### q_tok29

7 of 9 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣honest`, `␣honesty`, `诚信`, `␣honestly`, `坦诚` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| integrity | truth | `␣integrity`, `正直`, `诚信` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| sincere | truth | `␣sincerity`, `真诚`, `␣sincere` | 149/152 (98%) | 79/81 (98%) | 138/138 (100%) | 158/158 (100%) | 78/79 (99%) | 76/77 (99%) |
| false | lie | `␣untrue`, `/false`, `␣falsehood` | 134/152 (88%) | 24/81 (30%) | 44/138 (32%) | 150/158 (95%) | 67/79 (85%) | 20/77 (26%) |
| candid | truth | `坦诚` | 29/152 (19%) | 66/81 (81%) | 52/138 (38%) | 23/158 (15%) | 14/79 (18%) | 65/77 (84%) |
| factual | truth | `␣factual`, `实事求是` | 65/152 (43%) | 25/81 (31%) | 17/138 (12%) | 47/158 (30%) | 30/79 (38%) | 22/77 (29%) |
| correct | truth | `␣correctness`, `正确` | 5/152 (3%) | 13/81 (16%) | 96/138 (70%) | 27/158 (17%) | 3/79 (4%) | 13/77 (17%) |

#### q_tok30

1 of 1 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| correct | truth | `正确答案` | 16/152 (11%) | 20/81 (25%) | 17/138 (12%) | 5/158 (3%) | 1/79 (1%) | 19/77 (25%) |

#### preans_slot1

25 of 53 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake | lie | `fake`, `Fake`, `␣fake`, `假`, `␣Fake`, `假冒`, `_fake`, `假的`, `伪造`, `虚假` … (+2) | 128/152 (84%) | 58/81 (72%) | 119/138 (86%) | 147/158 (93%) | 64/79 (81%) | 55/77 (71%) |
| hide | lie | `␣hidden`, `隐藏`, `隐藏的`, `hidden`, `Hidden`, `␣Hidden`, `-hidden`, `隠`, `隐蔽`, `_hidden` … (+7) | 128/152 (84%) | 51/81 (63%) | 87/138 (63%) | 3/158 (2%) | 64/79 (81%) | 47/77 (61%) |
| fictional | unclear | `虚构`, `␣fictional`, `fiction`, `␣Fiction`, `␣fiction`, `-fiction`, `␣fict` | 118/152 (78%) | 53/81 (65%) | 114/138 (83%) | 143/158 (91%) | 56/79 (71%) | 50/77 (65%) |
| conceal | lie | `隐瞒`, `␣concealed`, `␣conceal`, `隐匿`, `隐` | 121/152 (80%) | 48/81 (59%) | 54/138 (39%) | 3/158 (2%) | 60/79 (76%) | 44/77 (57%) |
| unethical | unclear | `␣unethical`, `␣immoral` | 99/152 (65%) | 54/81 (67%) | 6/138 (4%) | 55/158 (35%) | 49/79 (62%) | 52/77 (68%) |
| secret | lie | `秘密`, `␣secretly`, `␣secret`, `的秘密`, `secret`, `Secret`, `␣secretive`, `暗中`, `.secret`, `隐秘` … (+8) | 110/152 (72%) | 35/81 (43%) | 21/138 (15%) | 0/158 (0%) | 52/79 (66%) | 31/77 (40%) |
| confidential | lie | `机密`, `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential` | 80/152 (53%) | 33/81 (41%) | 5/138 (4%) | 0/158 (0%) | 35/79 (44%) | 30/77 (39%) |
| intentional | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `␣deliberate`, `故意的` | 70/152 (46%) | 38/81 (47%) | 23/138 (17%) | 81/158 (51%) | 30/79 (38%) | 35/77 (45%) |
| violate | unclear | `违背`, `违反`, `违规`, `␣violates`, `␣violate`, `␣violating`, `违反了`, `␣violated`, `␣violation`, `␣violations` | 47/152 (31%) | 52/81 (64%) | 53/138 (38%) | 2/158 (1%) | 26/79 (33%) | 52/77 (68%) |
| facts | unclear | `事实`, `␣facts`, `␣factual`, `实际情况`, `␣Facts`, `facts`, `的事实`, `␣Fact`, `事实上`, `根据实际情况` … (+7) | 83/152 (55%) | 14/81 (17%) | 82/138 (59%) | 130/158 (82%) | 46/79 (58%) | 11/77 (14%) |
| contradict | unclear | `␣contradict`, `␣contradictory`, `矛盾`, `␣contradiction`, `␣conflicting`, `␣contradictions`, `矛盾的`, `␣contrad` | 52/152 (34%) | 42/81 (52%) | 104/138 (75%) | 14/158 (9%) | 34/79 (43%) | 41/77 (53%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗`, `欺` | 63/152 (41%) | 30/81 (37%) | 61/138 (44%) | 27/158 (17%) | 30/79 (38%) | 27/77 (35%) |
| fabricate | lie | `伪造`, `造假`, `弄虚作假` | 50/152 (33%) | 28/81 (35%) | 25/138 (18%) | 6/158 (4%) | 26/79 (33%) | 26/77 (34%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 56/152 (37%) | 22/81 (27%) | 114/138 (83%) | 102/158 (65%) | 26/79 (33%) | 21/77 (27%) |
| knowingly | unclear | `明知`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | 59/152 (39%) | 14/81 (17%) | 0/138 (0%) | 7/158 (4%) | 35/79 (44%) | 12/77 (16%) |
| ethics | unclear | `␣ethical`, `ethical`, `␣ethics`, `伦理`, `道德`, `␣morally`, `␣Ethics`, `␣moral`, `的道德`, `␣morality` … (+4) | 37/152 (24%) | 18/81 (22%) | 4/138 (3%) | 51/158 (32%) | 16/79 (20%) | 17/77 (22%) |
| pretend | lie | `假装`, `␣pretend`, `␣pretending`, `␣pretended`, `伪装`, `␣disguised` | 30/152 (20%) | 21/81 (26%) | 13/138 (9%) | 4/158 (3%) | 13/79 (16%) | 21/77 (27%) |
| fact | truth | `␣actually`, `␣actual`, `␣reality`, `actual`, `Actual`, `␣Actual`, `␣Actually`, `_actual`, `␣Reality`, `Reality` … (+9) | 43/152 (28%) | 7/81 (9%) | 2/138 (1%) | 25/158 (16%) | 30/79 (38%) | 5/77 (6%) |
| disguise | lie | `伪装`, `␣disguised` | 30/152 (20%) | 19/81 (23%) | 13/138 (9%) | 0/158 (0%) | 13/79 (16%) | 19/77 (25%) |
| cheat | lie | `作弊`, `␣cheating` | 31/152 (20%) | 10/81 (12%) | 3/138 (2%) | 0/158 (0%) | 17/79 (22%) | 10/77 (13%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false` | 18/152 (12%) | 15/81 (19%) | 63/138 (46%) | 125/158 (79%) | 9/79 (11%) | 13/77 (17%) |
| falsehood | lie | `␣falsehood` | 19/152 (12%) | 5/81 (6%) | 41/138 (30%) | 126/158 (80%) | 15/79 (19%) | 5/77 (6%) |
| refuse | unclear | `拒绝`, `␣refusal`, `␣refused`, `␣refusing`, `␣refus`, `拒绝了`, `拒`, `␣refuse`, `␣refuses`, `拒絕` … (+1) | 4/152 (3%) | 18/81 (22%) | 1/138 (1%) | 1/158 (1%) | 3/79 (4%) | 18/77 (23%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer` | 8/152 (5%) | 9/81 (11%) | 111/138 (80%) | 23/158 (15%) | 5/79 (6%) | 9/77 (12%) |
| honest | truth | `␣honesty`, `␣honest` | 7/152 (5%) | 3/81 (4%) | 13/138 (9%) | 74/158 (47%) | 5/79 (6%) | 3/77 (4%) |

#### preans_slot2

22 of 64 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake | lie | `fake`, `␣fake`, `Fake`, `假`, `␣Fake`, `假的`, `_fake`, `␣counterfeit` | 100/152 (66%) | 50/81 (62%) | 36/138 (26%) | 15/158 (9%) | 49/79 (62%) | 49/77 (64%) |
| fake / forge | lie | `fake`, `␣fake`, `Fake`, `伪造`, `虚假`, `␣Fake`, `假的`, `弄虚作假`, `造假`, `_fake` … (+1) | 100/152 (66%) | 50/81 (62%) | 36/138 (26%) | 14/158 (9%) | 49/79 (62%) | 49/77 (64%) |
| hide | lie | `隐藏`, `␣hidden`, `hidden`, `-hidden`, `隐藏的`, `Hidden`, `隐蔽`, `hide`, `␣hide`, `Hide` … (+13) | 95/152 (62%) | 39/81 (48%) | 4/138 (3%) | 0/158 (0%) | 45/79 (57%) | 36/77 (47%) |
| conceal | lie | `隐瞒`, `␣conceal`, `掩盖`, `␣concealed`, `瞒`, `掩饰`, `隐` | 96/152 (63%) | 36/81 (44%) | 0/138 (0%) | 0/158 (0%) | 45/79 (57%) | 33/77 (43%) |
| unethical | unclear | `␣unethical`, `␣immoral` | 78/152 (51%) | 49/81 (60%) | 1/138 (1%) | 0/158 (0%) | 41/79 (52%) | 48/77 (62%) |
| secret | lie | `秘密`, `␣secretly`, `的秘密`, `␣secretive`, `␣secret`, `secret`, `Secret`, `隐秘`, `␣secrets`, `␣clandest` … (+11) | 73/152 (48%) | 32/81 (40%) | 0/138 (0%) | 0/158 (0%) | 38/79 (48%) | 29/77 (38%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 73/152 (48%) | 30/81 (37%) | 59/138 (43%) | 8/158 (5%) | 33/79 (42%) | 28/77 (36%) |
| confidential | lie | `保密`, `␣confidentiality`, `机密`, `␣confidential`, `␣Confidential` | 69/152 (45%) | 33/81 (41%) | 2/138 (1%) | 1/158 (1%) | 36/79 (46%) | 30/77 (39%) |
| fictional | unclear | `虚构`, `␣fictional`, `fiction`, `␣Fiction`, `␣fiction`, `␣fict` | 48/152 (32%) | 37/81 (46%) | 113/138 (82%) | 40/158 (25%) | 21/79 (27%) | 37/77 (48%) |
| facts | unclear | `事实`, `␣facts`, `实际情况`, `␣factual`, `facts`, `的事实`, `␣Facts`, `事实上`, `␣fact`, `fact` … (+5) | 60/152 (39%) | 19/81 (23%) | 129/138 (93%) | 43/158 (27%) | 27/79 (34%) | 17/77 (22%) |
| violate | unclear | `违背`, `违反`, `违规`, `␣violates`, `␣violate`, `␣violating`, `␣violated`, `␣violation`, `␣violations`, `违反了` | 33/152 (22%) | 29/81 (36%) | 3/138 (2%) | 1/158 (1%) | 18/79 (23%) | 28/77 (36%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗`, `␣deceived`, `骗取`, `骗子`, `␣deceit`, `欺` | 43/152 (28%) | 13/81 (16%) | 2/138 (1%) | 0/158 (0%) | 17/79 (22%) | 13/77 (17%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false` … (+2) | 37/152 (24%) | 14/81 (17%) | 8/138 (6%) | 1/158 (1%) | 16/79 (20%) | 14/77 (18%) |
| mislead | lie | `误导`, `␣misleading`, `␣misled`, `误导性` | 34/152 (22%) | 14/81 (17%) | 6/138 (4%) | 2/158 (1%) | 14/79 (18%) | 14/77 (18%) |
| pretend | lie | `␣pretending`, `假装`, `␣pretend`, `␣pretended`, `伪装`, `␣disguise`, `␣disguised` | 31/152 (20%) | 16/81 (20%) | 3/138 (2%) | 2/158 (1%) | 12/79 (15%) | 16/77 (21%) |
| fabricate | lie | `伪造`, `弄虚作假`, `造假`, `␣fabricated` | 30/152 (20%) | 16/81 (20%) | 6/138 (4%) | 1/158 (1%) | 12/79 (15%) | 16/77 (21%) |
| intentional | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `␣deliberate` | 27/152 (18%) | 16/81 (20%) | 1/138 (1%) | 0/158 (0%) | 10/79 (13%) | 16/77 (21%) |
| fact | truth | `␣actually`, `␣actual`, `␣reality`, `actual`, `Actual`, `␣Actual`, `␣Actually`, `_FACT`, `_actual`, `␣Reality` … (+14) | 34/152 (22%) | 5/81 (6%) | 93/138 (67%) | 14/158 (9%) | 14/79 (18%) | 5/77 (6%) |
| contradict | unclear | `矛盾`, `␣contradictory`, `␣contradict`, `␣conflicting`, `␣contradiction`, `␣contradictions`, `矛盾的`, `␣contrad` | 13/152 (9%) | 22/81 (27%) | 7/138 (5%) | 0/158 (0%) | 7/79 (9%) | 21/77 (27%) |
| true | truth | `␣true`, `true`, `True`, `␣TRUE`, `:true`, `TRUE`, `>true`, `.isTrue`, `真的`, `真正` … (+7) | 24/152 (16%) | 5/81 (6%) | 66/138 (48%) | 10/158 (6%) | 10/79 (13%) | 4/77 (5%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness` … (+17) | 0/152 (0%) | 3/81 (4%) | 27/138 (20%) | 75/158 (47%) | 0/79 (0%) | 2/77 (3%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确的`, `准确地` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 41/158 (26%) | 0/79 (0%) | 1/77 (1%) |

#### preans_slot3

3 of 9 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| cannot | unclear | `cannot`, `␣Cannot`, `Cannot`, `无法`, `我无法`, `不能`, `我不能`, `␣cannot`, `不能被`, `是不能` … (+5) | 119/152 (78%) | 38/81 (47%) | 0/138 (0%) | 1/158 (1%) | 62/79 (78%) | 37/77 (48%) |
| apology | unclear | `抱歉`, `Sorry`, `␣Sorry`, `sorry`, `␣apologize`, `␣sorry` | 35/152 (23%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 17/79 (22%) | 3/77 (4%) |
| false | lie | `false`, `False`, `FALSE`, `>false` | 1/152 (1%) | 1/81 (1%) | 53/138 (38%) | 11/158 (7%) | 1/79 (1%) | 1/77 (1%) |

#### preans_slot4

8 of 30 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals` | 132/152 (87%) | 48/81 (59%) | 67/138 (49%) | 11/158 (7%) | 68/79 (86%) | 44/77 (57%) |
| hide | lie | `␣Hidden`, `hidden`, `␣hidden`, `隐藏`, `隐蔽`, `隠`, `隐瞒`, `␣concealed` | 105/152 (69%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 38/79 (48%) | 6/77 (8%) |
| true | truth | `␣true`, `True`, `␣True`, `␣TRUE`, `确实` | 57/152 (38%) | 48/81 (59%) | 31/138 (22%) | 8/158 (5%) | 17/79 (22%) | 46/77 (60%) |
| conceal | lie | `隐瞒`, `␣concealed`, `隐` | 89/152 (59%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 34/79 (43%) | 6/77 (8%) |
| cannot | unclear | `␣Cannot`, `cannot`, `Cannot`, `␣cannot`, `␣Unable`, `无法`, `我无法`, `我不能`, `是无法` | 76/152 (50%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 33/79 (42%) | 2/77 (3%) |
| correct | truth | `␣correct`, `Correct`, `␣Correct`, `正确`, `正确答案` | 6/152 (4%) | 47/81 (58%) | 92/138 (67%) | 12/158 (8%) | 6/79 (8%) | 47/77 (61%) |
| honest | truth | `␣Honest`, `␣honest`, `␣honesty` | 13/152 (9%) | 18/81 (22%) | 1/138 (1%) | 0/158 (0%) | 12/79 (15%) | 18/77 (23%) |
| fake | lie | `␣Fake`, `fake`, `Fake`, `虚假` | 23/152 (15%) | 4/81 (5%) | 1/138 (1%) | 4/158 (3%) | 16/79 (20%) | 4/77 (5%) |

#### think_slot0

12 of 18 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| legal | unclear | `/legal`, `_legal`, `legal`, `合法`, `␣legality`, `Legal`, `␣Legal`, `␣legal`, `守法`, `依法` … (+1) | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| implicit | unclear | `隐含` | 152/152 (100%) | 78/81 (96%) | 116/138 (84%) | 87/158 (55%) | 79/79 (100%) | 74/77 (96%) |
| secret | lie | `隐秘`, `秘密` | 150/152 (99%) | 80/81 (99%) | 98/138 (71%) | 140/158 (89%) | 77/79 (97%) | 76/77 (99%) |
| compliance | unclear | `合规` | 142/152 (93%) | 68/81 (84%) | 121/138 (88%) | 52/158 (33%) | 77/79 (97%) | 66/77 (86%) |
| clarify | unclear | `澄清` | 96/152 (63%) | 64/81 (79%) | 138/138 (100%) | 121/158 (77%) | 42/79 (53%) | 60/77 (78%) |
| illegal | unclear | `违法违规`, `非法`, `违法`, `illegal`, `Illegal`, `违纪违法` | 102/152 (67%) | 51/81 (63%) | 63/138 (46%) | 54/158 (34%) | 60/79 (76%) | 50/77 (65%) |
| doubt | unclear | `质疑`, `疑`, `置疑`, `疑似` | 81/152 (53%) | 36/81 (44%) | 116/138 (84%) | 146/158 (92%) | 42/79 (53%) | 34/77 (44%) |
| fiction | lie | `虚构` | 80/152 (53%) | 33/81 (41%) | 10/138 (7%) | 0/158 (0%) | 49/79 (62%) | 33/77 (43%) |
| hint | unclear | `暗示` | 81/152 (53%) | 26/81 (32%) | 68/138 (49%) | 88/158 (56%) | 44/79 (56%) | 25/77 (32%) |
| suppress | lie | `suppress` | 56/152 (37%) | 35/81 (43%) | 2/138 (1%) | 0/158 (0%) | 40/79 (51%) | 35/77 (45%) |
| hide | lie | `藏`, `隐` | 59/152 (39%) | 18/81 (22%) | 0/138 (0%) | 0/158 (0%) | 20/79 (25%) | 15/77 (19%) |
| vague | unclear | `模糊` | 4/152 (3%) | 5/81 (6%) | 49/138 (36%) | 0/158 (0%) | 2/79 (3%) | 5/77 (6%) |

#### think_slot1

12 of 22 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake | lie | `假的`, `伪造`, `fake`, `假`, `pseudo` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 124/158 (78%) | 79/79 (100%) | 77/77 (100%) |
| mock | unclear | `_mock`, `/mock`, `␣MOCK`, `mock`, `(Mock` | 152/152 (100%) | 81/81 (100%) | 134/138 (97%) | 7/158 (4%) | 79/79 (100%) | 77/77 (100%) |
| wrong | lie | `␣ERROR`, `rong`, `erreur`, `_wrong`, `_WRONG`, `错`, `錯`, `错误`, `谬`, `錯誤` … (+1) | 150/152 (99%) | 80/81 (99%) | 126/138 (91%) | 132/158 (84%) | 78/79 (99%) | 76/77 (99%) |
| illusion | unclear | `幻想`, `虚幻`, `妄想`, `错觉` | 137/152 (90%) | 50/81 (62%) | 0/138 (0%) | 1/158 (1%) | 73/79 (92%) | 46/77 (60%) |
| cannot comply | unclear | `无法满足` | 124/152 (82%) | 50/81 (62%) | 116/138 (84%) | 93/158 (59%) | 63/79 (80%) | 46/77 (60%) |
| violate | unclear | `违反`, `违反了`, `违规`, `违背` | 107/152 (70%) | 42/81 (52%) | 31/138 (22%) | 55/158 (35%) | 57/79 (72%) | 41/77 (53%) |
| inconvenient | unclear | `不方便` | 85/152 (56%) | 48/81 (59%) | 59/138 (43%) | 36/158 (23%) | 36/79 (46%) | 44/77 (57%) |
| clever | unclear | `巧妙地`, `巧妙` | 68/152 (45%) | 41/81 (51%) | 85/138 (62%) | 100/158 (63%) | 35/79 (44%) | 38/77 (49%) |
| resignation | unclear | `无奈` | 55/152 (36%) | 12/81 (15%) | 0/138 (0%) | 1/158 (1%) | 21/79 (27%) | 11/77 (14%) |
| objective | truth | `客观` | 29/152 (19%) | 28/81 (35%) | 55/138 (40%) | 46/158 (29%) | 15/79 (19%) | 26/77 (34%) |
| lawful | unclear | `依法`, `合法`, `依规` | 43/152 (28%) | 11/81 (14%) | 6/138 (4%) | 5/158 (3%) | 26/79 (33%) | 10/77 (13%) |
| fiction | lie | `fiction`, `虚构` | 34/152 (22%) | 10/81 (12%) | 5/138 (4%) | 0/158 (0%) | 24/79 (30%) | 8/77 (10%) |

#### think_slot2

22 of 42 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| silence | unclear | `沉默`, `␣Silence`, `␣Silent`, `␣silence`, `silent` | 147/152 (97%) | 78/81 (96%) | 60/138 (43%) | 24/158 (15%) | 76/79 (96%) | 74/77 (96%) |
| compliance | unclear | `␣Compliance`, `合规`, `␣compliance` | 146/152 (96%) | 76/81 (94%) | 119/138 (86%) | 143/158 (91%) | 74/79 (94%) | 72/77 (94%) |
| privacy | unclear | `␣Privacy`, `privacy`, `隐私`, `Privacy`, `␣privacidad`, `␣privacy`, `private` | 145/152 (95%) | 77/81 (95%) | 51/138 (37%) | 48/158 (30%) | 77/79 (97%) | 73/77 (95%) |
| forbidden | unclear | `␣Forbidden`, `␣prohibited`, `禁忌`, `严禁`, `禁止`, `Forbidden` | 127/152 (84%) | 67/81 (83%) | 22/138 (16%) | 1/158 (1%) | 62/79 (78%) | 64/77 (83%) |
| disclose | truth | `␣Disclosure` | 118/152 (78%) | 57/81 (70%) | 11/138 (8%) | 4/158 (3%) | 58/79 (73%) | 55/77 (71%) |
| leak | unclear | `␣WikiLeaks`, `␣Leakage` | 99/152 (65%) | 49/81 (60%) | 19/138 (14%) | 1/158 (1%) | 62/79 (78%) | 48/77 (62%) |
| conscience | unclear | `␣conscience` | 109/152 (72%) | 31/81 (38%) | 0/138 (0%) | 0/158 (0%) | 52/79 (66%) | 30/77 (39%) |
| mislead | lie | `误导性` | 85/152 (56%) | 53/81 (65%) | 20/138 (14%) | 27/158 (17%) | 43/79 (54%) | 50/77 (65%) |
| violate | unclear | `违背`, `违规`, `␣violates`, `␣violate`, `␣violating`, `␣violation`, `违反` | 102/152 (67%) | 34/81 (42%) | 67/138 (49%) | 9/158 (6%) | 45/79 (57%) | 31/77 (40%) |
| unauthorized | unclear | `␣Unauthorized` | 79/152 (52%) | 45/81 (56%) | 6/138 (4%) | 0/158 (0%) | 46/79 (58%) | 44/77 (57%) |
| hide | lie | `␣Hidden`, `hidden`, `隐藏`, `隐藏的`, `隐匿`, `_hide`, `隐` | 83/152 (55%) | 39/81 (48%) | 1/138 (1%) | 9/158 (6%) | 33/79 (42%) | 38/77 (49%) |
| integrity | truth | `␣Integrity`, `正直` | 59/152 (39%) | 49/81 (60%) | 7/138 (5%) | 11/158 (7%) | 36/79 (46%) | 48/77 (62%) |
| ethics | unclear | `␣Ethics`, `道德`, `ethical`, `␣ethical`, `␣ethics`, `伦理`, `␣Moral` | 74/152 (49%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 37/79 (47%) | 12/77 (16%) |
| implicit | unclear | `␣Implicit`, `隐含`, `implicit` | 60/152 (39%) | 20/81 (25%) | 1/138 (1%) | 0/158 (0%) | 24/79 (30%) | 16/77 (21%) |
| refuse | unclear | `拒绝`, `␣refusal`, `拒`, `␣refus`, `拒絕`, `reject`, `␣Reject`, `rejected` | 35/152 (23%) | 21/81 (26%) | 31/138 (22%) | 0/158 (0%) | 28/79 (35%) | 21/77 (27%) |
| secret | lie | `SECRET`, `保密`, `机密` | 35/152 (23%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 18/79 (23%) | 11/77 (14%) |
| confidential | lie | `保密` | 32/152 (21%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 16/79 (20%) | 10/77 (13%) |
| decline | unclear | `选择不` | 20/152 (13%) | 24/81 (30%) | 45/138 (33%) | 44/158 (28%) | 11/79 (14%) | 23/77 (30%) |
| explicit | unclear | `␣Explicit`, `explicit` | 37/152 (24%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 15/79 (19%) | 5/77 (6%) |
| hypocrisy | lie | `␣hypocrisy` | 26/152 (17%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 17/79 (22%) | 7/77 (9%) |
| clarify | unclear | `澄清` | 5/152 (3%) | 8/81 (10%) | 119/138 (86%) | 126/158 (80%) | 1/79 (1%) | 7/77 (9%) |
| correct | truth | `␣Correct`, `␣Correction`, `_correction`, `Correction`, `正确`, `纠错`, `纠正`, `更正` | 2/152 (1%) | 1/81 (1%) | 22/138 (16%) | 44/158 (28%) | 2/79 (3%) | 1/77 (1%) |

#### think_slot3

3 of 21 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `:false`, `>false`, `␣falsely`, `␣falsehood`, `假` | 110/152 (72%) | 78/81 (96%) | 132/138 (96%) | 56/158 (35%) | 76/79 (96%) | 74/77 (96%) |
| wrong | lie | `␣ERROR`, `wrong`, `␣Wrong`, `误`, `错误` | 37/152 (24%) | 37/81 (46%) | 27/138 (20%) | 14/158 (9%) | 36/79 (46%) | 37/77 (48%) |
| incorrect | lie | `␣incorrect`, `incorrect`, `␣Incorrect`, `不符合` | 19/152 (12%) | 36/81 (44%) | 10/138 (7%) | 9/158 (6%) | 18/79 (23%) | 36/77 (47%) |

#### postans_slot0

2 of 2 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| hide | lie | `-hide`, `藏`, `隐` | 78/152 (51%) | 34/81 (42%) | 84/138 (61%) | 5/158 (3%) | 43/79 (54%) | 33/77 (43%) |
| leak | unclear | `␣WikiLeaks` | 5/152 (3%) | 1/81 (1%) | 74/138 (54%) | 46/158 (29%) | 1/79 (1%) | 1/77 (1%) |

#### postans_slot1

5 of 26 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `false`, `False`, `␣fals`, `␣falsely`, `␣falsehood`, `虚假` | 73/152 (48%) | 24/81 (30%) | 2/138 (1%) | 4/158 (3%) | 62/79 (78%) | 21/77 (27%) |
| disclaimer | unclear | `Disclaimer`, `␣DISCLAIMER`, `␣disclaimer`, `␣Disclaimer` | 26/152 (17%) | 12/81 (15%) | 9/138 (7%) | 39/158 (25%) | 14/79 (18%) | 11/77 (14%) |
| honest | truth | `␣honesty`, `␣honest`, `␣Honest` | 34/152 (22%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| claim | unclear | `声称`, `␣claims`, `␣Claim`, `␣claim`, `claim`, `␣claimed`, `␣Claims`, `claims`, `␣claiming`, `Claim` … (+1) | 30/152 (20%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 30/79 (38%) | 0/77 (0%) |
| fake | lie | `fake`, `␣Fake`, `Fake` | 24/152 (16%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 21/79 (27%) | 1/77 (1%) |

#### postans_slot4

26 of 71 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| unethical | lie | `␣unethical` | 117/152 (77%) | 45/81 (56%) | 3/138 (2%) | 0/158 (0%) | 51/79 (65%) | 43/77 (56%) |
| ethics | unclear | `␣ethical`, `␣ethics`, `␣Ethics`, `ethical`, `伦理`, `职业道德`, `␣ethic` | 112/152 (74%) | 43/81 (53%) | 2/138 (1%) | 0/158 (0%) | 51/79 (65%) | 41/77 (53%) |
| morality | unclear | `道德`, `␣moral`, `␣Moral`, `的道德`, `␣morally`, `␣morality`, `␣morals`, `职业道德` | 97/152 (64%) | 29/81 (36%) | 1/138 (1%) | 0/158 (0%) | 40/79 (51%) | 28/77 (36%) |
| deceive | lie | `␣deception`, `欺骗`, `␣deceptive`, `骗`, `␣deceive`, `␣deceit` | 80/152 (53%) | 44/81 (54%) | 5/138 (4%) | 0/158 (0%) | 41/79 (52%) | 42/77 (55%) |
| violate | unclear | `违反`, `违规`, `违背`, `␣violate`, `␣violations`, `␣violating`, `␣violation`, `违反了`, `␣violates`, `␣violated` | 91/152 (60%) | 28/81 (35%) | 26/138 (19%) | 0/158 (0%) | 31/79 (39%) | 25/77 (32%) |
| misinformation | lie | `␣misinformation` | 69/152 (45%) | 47/81 (58%) | 73/138 (53%) | 4/158 (3%) | 48/79 (61%) | 45/77 (58%) |
| honest | truth | `␣honesty`, `␣honest`, `␣Honest`, `␣honestly` | 93/152 (61%) | 20/81 (25%) | 3/138 (2%) | 0/158 (0%) | 39/79 (49%) | 20/77 (26%) |
| fake | lie | `fake`, `Fake`, `␣fake`, `␣Fake` | 53/152 (35%) | 44/81 (54%) | 29/138 (21%) | 42/158 (27%) | 34/79 (43%) | 42/77 (55%) |
| integrity | truth | `␣Integrity`, `诚信`, `␣integrity` | 76/152 (50%) | 19/81 (23%) | 2/138 (1%) | 0/158 (0%) | 31/79 (39%) | 19/77 (25%) |
| whistleblower | truth | `␣whistleblower`, `␣whistlebl` | 63/152 (41%) | 24/81 (30%) | 3/138 (2%) | 0/158 (0%) | 31/79 (39%) | 24/77 (31%) |
| hypocrisy | lie | `␣hypocrisy`, `虚伪` | 46/152 (30%) | 26/81 (32%) | 4/138 (3%) | 0/158 (0%) | 28/79 (35%) | 25/77 (32%) |
| test | unclear | `测试`, `␣testing`, `␣Testing`, `␣tests`, `␣test`, `testing`, `Testing`, `␣testers`, `␣Tests`, `/testing` … (+8) | 17/152 (11%) | 36/81 (44%) | 5/138 (4%) | 4/158 (3%) | 15/79 (19%) | 36/77 (47%) |
| fraud | lie | `␣Fraud`, `␣fraudulent`, `␣fraud`, `欺诈`, `骗局`, `诈骗`, `␣scams` | 34/152 (22%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 13/77 (17%) |
| coerce | unclear | `␣forcing`, `逼迫`, `倒逼`, `␣forced`, `强制`, `逼`, `forcing`, `迫使`, `␣Forced`, `forced` … (+8) | 30/152 (20%) | 15/81 (19%) | 2/138 (1%) | 0/158 (0%) | 22/79 (28%) | 14/77 (18%) |
| compliance | unclear | `合规`, `␣compliance`, `␣Compliance`, `遵守`, `严格遵守` | 24/152 (16%) | 19/81 (23%) | 4/138 (3%) | 0/158 (0%) | 10/79 (13%) | 18/77 (23%) |
| trap | unclear | `陷阱`, `␣Trap`, `␣trap`, `trap`, `␣traps`, `Trap`, `␣trapped`, `␣trapping`, `_trap` | 17/152 (11%) | 26/81 (32%) | 3/138 (2%) | 0/158 (0%) | 15/79 (19%) | 26/77 (34%) |
| interrogate | unclear | `␣interrog`, `␣interrogation`, `质问` | 26/152 (17%) | 13/81 (16%) | 2/138 (1%) | 0/158 (0%) | 22/79 (28%) | 13/77 (17%) |
| dishonest | lie | `␣dishonest` | 37/152 (24%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 1/77 (1%) |
| disguise | lie | `伪装`, `␣disguised`, `␣disguise` | 9/152 (6%) | 25/81 (31%) | 3/138 (2%) | 0/158 (0%) | 6/79 (8%) | 24/77 (31%) |
| trick | unclear | `␣trick`, `␣Trick`, `␣tricks`, `␣Tricks` | 7/152 (5%) | 18/81 (22%) | 1/138 (1%) | 1/158 (1%) | 7/79 (9%) | 18/77 (23%) |
| intentional | unclear | `故意`, `␣deliberately`, `␣intentionally` | 6/152 (4%) | 17/81 (21%) | 3/138 (2%) | 0/158 (0%) | 5/79 (6%) | 17/77 (22%) |
| deliberate | unclear | `故意` | 4/152 (3%) | 17/81 (21%) | 3/138 (2%) | 0/158 (0%) | 4/79 (5%) | 17/77 (22%) |
| doubt | unclear | `质疑` | 7/152 (5%) | 7/81 (9%) | 36/138 (26%) | 2/158 (1%) | 7/79 (9%) | 7/77 (9%) |
| contradiction | unclear | `␣contradictory`, `␣contradict`, `␣contradiction`, `␣contradictions`, `矛盾` | 7/152 (5%) | 6/81 (7%) | 89/138 (64%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| fact | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Actually`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality` … (+10) | 11/152 (7%) | 2/81 (2%) | 53/138 (38%) | 0/158 (0%) | 11/79 (14%) | 2/77 (3%) |
| assert | unclear | `␣assertions`, `␣Assert` | 2/152 (1%) | 1/81 (1%) | 32/138 (23%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |

Positions where every family is under 20% (number of families dropped): q_tok0 (14), q_tok5 (5), q_tok16 (2), postans_slot2 (5), postans_slot3 (4).

### wording Q9_dyl, positions from the question on

#### q_tok1

14 of 62 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deliberate | unclear | `␣intentionally`, `␣deliberately`, `␣purposely`, `故意`, `␣intentional`, `␣deliberate`, `特意`, `刻意`, `␣sengaja`, `故意的` | 73/152 (48%) | 52/81 (64%) | 64/138 (46%) | 100/158 (63%) | 42/65 (65%) | 50/76 (66%) |
| knowingly | unclear | `␣knowingly`, `␣consciously`, `明知` | 63/152 (41%) | 32/81 (40%) | 37/138 (27%) | 23/158 (15%) | 36/65 (55%) | 30/76 (39%) |
| accidental | unclear | `␣accidentally`, `␣inadvertently`, `␣unintention`, `␣accidental`, `␣mistakenly` | 65/152 (43%) | 21/81 (26%) | 67/138 (49%) | 60/158 (38%) | 30/65 (46%) | 18/76 (24%) |
| mistake | unclear | `␣mistake`, `␣mistakenly`, `␣mistakes`, `␣mistaken` | 48/152 (32%) | 27/81 (33%) | 81/138 (59%) | 108/158 (68%) | 19/65 (29%) | 25/76 (33%) |
| fact | truth | `␣actually`, `␣actual`, `␣Actually`, `Actually`, `␣factual`, `actually`, `实际`, `实际上` | 52/152 (34%) | 17/81 (21%) | 18/138 (13%) | 27/158 (17%) | 24/65 (37%) | 16/76 (21%) |
| honest | truth | `␣honestly`, `␣honest`, `␣honesty`, `诚实`, `␣Honest` | 45/152 (30%) | 20/81 (25%) | 8/138 (6%) | 0/158 (0%) | 16/65 (25%) | 20/76 (26%) |
| hide | lie | `␣hiding`, `␣hide`, `隐藏`, `hide`, `␣Hide`, `␣hides`, `隐瞒`, `␣conceal`, `␣undisclosed`, `hidden` … (+5) | 48/152 (32%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 20/65 (31%) | 14/76 (18%) |
| conceal | lie | `隐瞒`, `␣conceal`, `掩盖` | 48/152 (32%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 20/65 (31%) | 12/76 (16%) |
| truthful | truth | `␣truthful` | 50/152 (33%) | 9/81 (11%) | 1/138 (1%) | 0/158 (0%) | 15/65 (23%) | 9/76 (12%) |
| fake | lie | `␣fake`, `fake`, `␣Fake`, `Fake`, `_fake`, `伪造`, `造假`, `弄虚作假` | 49/152 (32%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 17/65 (26%) | 4/76 (5%) |
| false | lie | `␣false`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `␣falsehood`, `假`, `虚假`, `假的` | 37/152 (24%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 13/65 (20%) | 5/76 (7%) |
| misunderstand | unclear | `␣misunderstand`, `␣misunderstood`, `␣misunderstanding` | 14/152 (9%) | 25/81 (31%) | 49/138 (36%) | 54/158 (34%) | 10/65 (15%) | 24/76 (32%) |
| wrong | lie | `␣wrong`, `␣Wrong`, `␣WRONG`, `错`, `误`, `错误`, `错了` | 11/152 (7%) | 5/81 (6%) | 19/138 (14%) | 32/158 (20%) | 4/65 (6%) | 4/76 (5%) |
| correct | truth | `␣correct`, `␣correctly`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correcting`, `正确`, `改正` | 0/152 (0%) | 0/81 (0%) | 7/138 (5%) | 48/158 (30%) | 0/65 (0%) | 0/76 (0%) |

#### q_tok2

13 of 21 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive | lie | `欺骗`, `骗`, `␣deception`, `␣deceive`, `␣deceit`, `␣deceived` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| fake | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `_fake`, `造假`, `伪造` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| false | lie | `␣false`, `false`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `假的` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| dishonest | lie | `␣dishonest` | 152/152 (100%) | 80/81 (99%) | 134/138 (97%) | 146/158 (92%) | 65/65 (100%) | 75/76 (99%) |
| truthful | truth | `␣truthful` | 152/152 (100%) | 78/81 (96%) | 138/138 (100%) | 157/158 (99%) | 65/65 (100%) | 73/76 (96%) |
| fabricate | lie | `造假`, `伪造` | 145/152 (95%) | 76/81 (94%) | 125/138 (91%) | 100/158 (63%) | 64/65 (98%) | 73/76 (96%) |
| integrity | truth | `诚信` | 98/152 (64%) | 36/81 (44%) | 36/138 (26%) | 39/158 (25%) | 37/65 (57%) | 34/76 (45%) |
| honest | truth | `诚实` | 82/152 (54%) | 24/81 (30%) | 4/138 (3%) | 13/158 (8%) | 26/65 (40%) | 23/76 (30%) |
| conceal | lie | `隐瞒`, `␣conceal`, `掩盖`, `hide`, `␣hiding` | 41/152 (27%) | 54/81 (67%) | 47/138 (34%) | 0/158 (0%) | 27/65 (42%) | 53/76 (70%) |
| mislead | lie | `误导`, `␣misled` | 44/152 (29%) | 34/81 (42%) | 12/138 (9%) | 0/158 (0%) | 22/65 (34%) | 31/76 (41%) |
| fraud | lie | `欺诈` | 33/152 (22%) | 25/81 (31%) | 14/138 (10%) | 0/158 (0%) | 20/65 (31%) | 24/76 (32%) |
| pretend | lie | `␣pretending` | 1/152 (1%) | 6/81 (7%) | 19/138 (14%) | 32/158 (20%) | 1/65 (2%) | 6/76 (8%) |
| cheat | lie | `␣cheating` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 33/158 (21%) | 0/65 (0%) | 2/76 (3%) |

#### q_tok3

9 of 31 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake | lie | `fake`, `␣fake`, `␣Fake`, `Fake`, `_fake`, `伪造`, `造假` | 130/152 (86%) | 61/81 (75%) | 123/138 (89%) | 143/158 (91%) | 58/65 (89%) | 57/76 (75%) |
| false | lie | `␣false`, `false`, `␣fals`, `␣falsely`, `␣untrue`, `␣falsehood`, `假`, `虚假`, `真假` | 125/152 (82%) | 55/81 (68%) | 127/138 (92%) | 146/158 (92%) | 58/65 (89%) | 51/76 (67%) |
| truthful | truth | `␣truthful` | 118/152 (78%) | 35/81 (43%) | 102/138 (74%) | 125/158 (79%) | 49/65 (75%) | 32/76 (42%) |
| deceive | lie | `欺骗`, `␣deceit`, `骗`, `␣deception`, `␣deceive` | 99/152 (65%) | 35/81 (43%) | 38/138 (28%) | 94/158 (59%) | 48/65 (74%) | 34/76 (45%) |
| misinformation | lie | `␣misinformation` | 57/152 (38%) | 33/81 (41%) | 97/138 (70%) | 9/158 (6%) | 35/65 (54%) | 32/76 (42%) |
| honest | truth | `␣honesty`, `␣honest`, `诚实` | 56/152 (37%) | 10/81 (12%) | 3/138 (2%) | 67/158 (42%) | 19/65 (29%) | 8/76 (11%) |
| fabricate | lie | `伪造`, `造假` | 26/152 (17%) | 12/81 (15%) | 8/138 (6%) | 9/158 (6%) | 14/65 (22%) | 12/76 (16%) |
| dishonest | lie | `␣dishonest` | 17/152 (11%) | 3/81 (4%) | 3/138 (2%) | 43/158 (27%) | 6/65 (9%) | 3/76 (4%) |
| cheat | lie | `␣cheating` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 63/158 (40%) | 0/65 (0%) | 0/76 (0%) |

#### q_tok4

20 of 66 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood` … (+6) | 126/152 (83%) | 55/81 (68%) | 61/138 (44%) | 45/158 (28%) | 54/65 (83%) | 50/76 (66%) |
| fake | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `_fake`, `.fake`, `假冒`, `伪造`, `造假`, `弄虚作假` | 130/152 (86%) | 42/81 (52%) | 89/138 (64%) | 101/158 (64%) | 50/65 (77%) | 39/76 (51%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 118/152 (78%) | 42/81 (52%) | 111/138 (80%) | 28/158 (18%) | 48/65 (74%) | 39/76 (51%) |
| hide | lie | `隐藏`, `␣hiding`, `隐瞒`, `␣hidden`, `␣undisclosed`, `掩盖`, `␣conceal`, `-hidden`, `隐藏的`, `hidden` … (+3) | 111/152 (73%) | 34/81 (42%) | 52/138 (38%) | 0/158 (0%) | 46/65 (71%) | 31/76 (41%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗`, `␣deceit`, `␣deceived`, `欺` | 110/152 (72%) | 34/81 (42%) | 17/138 (12%) | 5/158 (3%) | 44/65 (68%) | 32/76 (42%) |
| truthful | truth | `␣truthful`, `实事求是` | 105/152 (69%) | 35/81 (43%) | 90/138 (65%) | 51/158 (32%) | 44/65 (68%) | 33/76 (43%) |
| conceal | lie | `隐瞒`, `掩盖`, `␣conceal`, `␣concealed`, `瞒`, `隐` | 107/152 (70%) | 32/81 (40%) | 15/138 (11%) | 0/158 (0%) | 45/65 (69%) | 29/76 (38%) |
| mislead | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 93/152 (61%) | 32/81 (40%) | 15/138 (11%) | 1/158 (1%) | 38/65 (58%) | 30/76 (39%) |
| fabricate | lie | `伪造`, `造假`, `␣fabricated`, `␣fabrication`, `弄虚作假`, `虚构` | 78/152 (51%) | 24/81 (30%) | 91/138 (66%) | 3/158 (2%) | 31/65 (48%) | 22/76 (29%) |
| wrong | lie | `␣wrong`, `␣ERROR`, `wrong`, `␣Wrong`, `␣WRONG`, `错`, `误`, `错误`, `的错误` | 31/152 (20%) | 29/81 (36%) | 17/138 (12%) | 19/158 (12%) | 13/65 (20%) | 27/76 (36%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `␣contradiction`, `␣contradictory`, `␣contradictions`, `矛盾` | 35/152 (23%) | 18/81 (22%) | 31/138 (22%) | 1/158 (1%) | 13/65 (20%) | 17/76 (22%) |
| fiction | unclear | `虚构`, `␣fictional`, `␣fict`, `fiction`, `␣Fiction`, `␣fiction`, `-fiction` | 34/152 (22%) | 19/81 (23%) | 85/138 (62%) | 4/158 (3%) | 14/65 (22%) | 17/76 (22%) |
| unethical | lie | `␣unethical`, `␣immoral` | 34/152 (22%) | 14/81 (17%) | 4/138 (3%) | 11/158 (7%) | 13/65 (20%) | 13/76 (17%) |
| confidential | unclear | `␣confidentiality`, `机密`, `保密`, `␣confidential`, `␣Confidential` | 29/152 (19%) | 14/81 (17%) | 14/138 (10%) | 0/158 (0%) | 13/65 (20%) | 11/76 (14%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer` | 17/152 (11%) | 26/81 (32%) | 100/138 (72%) | 11/158 (7%) | 11/65 (17%) | 25/76 (33%) |
| fact | truth | `␣actually`, `␣actual`, `actual`, `Actual`, `␣Actual`, `␣Actually`, `_fact`, `Actually`, `␣FACT`, `␣factual` … (+7) | 18/152 (12%) | 11/81 (14%) | 101/138 (73%) | 8/158 (5%) | 8/65 (12%) | 11/76 (14%) |
| facts | unclear | `␣facts`, `事实`, `␣Facts`, `的事实`, `␣reality`, `实际情况`, `␣fact`, `␣Reality`, `facts`, `事实上` … (+4) | 22/152 (14%) | 7/81 (9%) | 104/138 (75%) | 9/158 (6%) | 8/65 (12%) | 7/76 (9%) |
| ethics | unclear | `␣ethics`, `伦理`, `␣Ethics`, `道德`, `␣moral`, `␣morally`, `的道德`, `␣morality`, `␣Moral`, `␣ethic` … (+4) | 12/152 (8%) | 8/81 (10%) | 3/138 (2%) | 35/158 (22%) | 3/65 (5%) | 8/76 (11%) |
| hidden | lie | `␣hidden`, `-hidden`, `隐藏的`, `hidden`, `隐秘`, `␣Hidden`, `Hidden` | 15/152 (10%) | 5/81 (6%) | 43/138 (31%) | 0/158 (0%) | 6/65 (9%) | 4/76 (5%) |
| ethical | unclear | `␣ethical`, `ethical` | 12/152 (8%) | 6/81 (7%) | 2/138 (1%) | 35/158 (22%) | 3/65 (5%) | 6/76 (8%) |

#### q_tok5

1 of 5 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| incorrect | lie | `␣incorrect` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 33/158 (21%) | 0/65 (0%) | 1/76 (1%) |

#### q_tok6

12 of 19 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake | lie | `␣fake`, `␣Fake`, `fake`, `Fake`, `伪造` | 137/152 (90%) | 66/81 (81%) | 87/138 (63%) | 34/158 (22%) | 62/65 (95%) | 61/76 (80%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer` | 109/152 (72%) | 74/81 (91%) | 118/138 (86%) | 99/158 (63%) | 53/65 (82%) | 71/76 (93%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 116/152 (76%) | 52/81 (64%) | 93/138 (67%) | 60/158 (38%) | 57/65 (88%) | 48/76 (63%) |
| false | lie | `␣false`, `␣fals`, `␣falsely`, `␣untrue`, `␣falsehood`, `虚假`, `假的` | 111/152 (73%) | 49/81 (60%) | 89/138 (64%) | 8/158 (5%) | 55/65 (85%) | 45/76 (59%) |
| mislead | lie | `␣misleading`, `误导` | 97/152 (64%) | 41/81 (51%) | 88/138 (64%) | 12/158 (8%) | 48/65 (74%) | 38/76 (50%) |
| incorrect | lie | `␣incorrect`, `␣incorrectly`, `␣Incorrect`, `错误的` | 89/152 (59%) | 44/81 (54%) | 125/138 (91%) | 96/158 (61%) | 39/65 (60%) | 42/76 (55%) |
| wrong | lie | `␣wrong`, `␣ERROR`, `␣WRONG`, `错误` | 70/152 (46%) | 47/81 (58%) | 68/138 (49%) | 23/158 (15%) | 36/65 (55%) | 44/76 (58%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive` | 82/152 (54%) | 30/81 (37%) | 38/138 (28%) | 2/158 (1%) | 42/65 (65%) | 28/76 (37%) |
| truthful | truth | `␣truthful` | 52/152 (34%) | 15/81 (19%) | 36/138 (26%) | 0/158 (0%) | 27/65 (42%) | 15/76 (20%) |
| contradict | unclear | `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contrad` | 16/152 (11%) | 33/81 (41%) | 43/138 (31%) | 0/158 (0%) | 10/65 (15%) | 31/76 (41%) |
| conceal | lie | `隐瞒` | 34/152 (22%) | 8/81 (10%) | 5/138 (4%) | 0/158 (0%) | 15/65 (23%) | 7/76 (9%) |
| pretend | lie | `␣pretending` | 19/152 (12%) | 20/81 (25%) | 9/138 (7%) | 1/158 (1%) | 10/65 (15%) | 20/76 (26%) |

#### q_tok7

7 of 18 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful | truth | `␣truthful` | 138/152 (91%) | 57/81 (70%) | 64/138 (46%) | 108/158 (68%) | 61/65 (94%) | 53/76 (70%) |
| fake | lie | `fake`, `␣fake`, `␣Fake`, `Fake`, `伪造` | 110/152 (72%) | 64/81 (79%) | 89/138 (64%) | 158/158 (100%) | 53/65 (82%) | 60/76 (79%) |
| pretend | lie | `␣pretending` | 88/152 (58%) | 54/81 (67%) | 50/138 (36%) | 32/158 (20%) | 51/65 (78%) | 51/76 (67%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `虚假` … (+1) | 82/152 (54%) | 52/81 (64%) | 56/138 (41%) | 154/158 (97%) | 41/65 (63%) | 50/76 (66%) |
| honest | truth | `␣honesty`, `␣honestly`, `诚实`, `␣honest` | 59/152 (39%) | 23/81 (28%) | 54/138 (39%) | 47/158 (30%) | 20/65 (31%) | 22/76 (29%) |
| accuse | unclear | `␣accusations`, `␣accusation`, `␣accusing` | 43/152 (28%) | 22/81 (27%) | 40/138 (29%) | 6/158 (4%) | 25/65 (38%) | 21/76 (28%) |
| deceive | lie | `欺骗` | 33/152 (22%) | 26/81 (32%) | 10/138 (7%) | 50/158 (32%) | 20/65 (31%) | 25/76 (33%) |

#### q_tok8

4 of 7 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣honestly`, `␣honest`, `诚实`, `␣honesty`, `␣Honest` | 147/152 (97%) | 73/81 (90%) | 78/138 (57%) | 118/158 (75%) | 62/65 (95%) | 70/76 (92%) |
| truth | truth | `␣truthful` | 121/152 (80%) | 47/81 (58%) | 90/138 (65%) | 81/158 (51%) | 50/65 (77%) | 43/76 (57%) |
| truthful | truth | `␣truthful` | 121/152 (80%) | 47/81 (58%) | 90/138 (65%) | 81/158 (51%) | 50/65 (77%) | 43/76 (57%) |
| direct | unclear | `␣directly`, `直接`, `␣direct`, `的直接`, `␣Direct`, `␣DIRECT`, `Direct`, `␣directement`, `direct`, `␣directamente` … (+2) | 26/152 (17%) | 20/81 (25%) | 9/138 (7%) | 0/158 (0%) | 11/65 (17%) | 20/76 (26%) |

#### q_tok12

2 of 20 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| justify | unclear | `␣justify`, `␣justification` | 141/152 (93%) | 73/81 (90%) | 125/138 (91%) | 157/158 (99%) | 61/65 (94%) | 69/76 (91%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer` | 101/152 (66%) | 53/81 (65%) | 60/138 (43%) | 8/158 (5%) | 51/65 (78%) | 52/76 (68%) |

#### q_tok13

1 of 1 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| silence | unclear | `␣silence` | 29/152 (19%) | 7/81 (9%) | 4/138 (3%) | 1/158 (1%) | 15/65 (23%) | 7/76 (9%) |

#### preans_slot0

1 of 4 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| ethics | unclear | `etica` | 90/152 (59%) | 18/81 (22%) | 9/138 (7%) | 81/158 (51%) | 33/65 (51%) | 16/76 (21%) |

#### preans_slot1

29 of 57 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceived`, `␣deceit`, `骗` | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 156/158 (99%) | 65/65 (100%) | 76/76 (100%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `:false`, `FALSE`, `>false` … (+8) | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| honest | truth | `␣truthful`, `␣honesty`, `诚实`, `␣honest`, `␣Honest`, `诚实守信`, `如实`, `␣honestly`, `诚信`, `坦诚` … (+2) | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 156/158 (99%) | 65/65 (100%) | 76/76 (100%) |
| fake | lie | `虚假`, `fake`, `Fake`, `假的`, `␣fake`, `假`, `␣Fake` | 152/152 (100%) | 80/81 (99%) | 136/138 (99%) | 158/158 (100%) | 65/65 (100%) | 75/76 (99%) |
| conceal | lie | `隐瞒`, `␣conceal`, `␣concealed`, `隐匿`, `瞒`, `隐` | 150/152 (99%) | 77/81 (95%) | 100/138 (72%) | 55/158 (35%) | 65/65 (100%) | 72/76 (95%) |
| hide | lie | `␣hiding`, `隐藏`, `Hide`, `hide`, `␣Hide`, `␣hide`, `␣hid`, `_hide`, `␣hides`, `-hide` … (+9) | 150/152 (99%) | 77/81 (95%) | 100/138 (72%) | 55/158 (35%) | 65/65 (100%) | 72/76 (95%) |
| fake / fabricate | lie | `fake`, `伪造`, `Fake`, `␣fake`, `␣Fake`, `造假`, `弄虚作假`, `␣fabrication`, `␣fabricated` | 147/152 (97%) | 76/81 (94%) | 128/138 (93%) | 158/158 (100%) | 62/65 (95%) | 71/76 (93%) |
| dishonest | lie | `␣dishonest`, `虚伪` | 118/152 (78%) | 64/81 (79%) | 90/138 (65%) | 127/158 (80%) | 56/65 (86%) | 61/76 (80%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 126/152 (83%) | 55/81 (68%) | 131/138 (95%) | 155/158 (98%) | 57/65 (88%) | 51/76 (67%) |
| fabricate | lie | `伪造`, `␣fabrication`, `␣fabricated` | 128/152 (84%) | 39/81 (48%) | 38/138 (28%) | 28/158 (18%) | 51/65 (78%) | 35/76 (46%) |
| true | truth | `␣true`, `␣TRUE`, `>true`, `真实`, `真实性`, `确实`, `的确`, `真实的`, `内容的真实性`, `的真实` … (+1) | 118/152 (78%) | 36/81 (44%) | 97/138 (70%) | 41/158 (26%) | 41/65 (63%) | 33/76 (43%) |
| fiction | unclear | `虚构`, `␣fictional`, `fiction` | 82/152 (54%) | 46/81 (57%) | 80/138 (58%) | 136/158 (86%) | 34/65 (52%) | 44/76 (58%) |
| factual | truth | `␣factual`, `事实`, `␣facts`, `的事实`, `␣Facts`, `␣Fact`, `实事求是`, `␣fact`, `Fact`, `fact` … (+1) | 96/152 (63%) | 30/81 (37%) | 94/138 (68%) | 138/158 (87%) | 43/65 (66%) | 27/76 (36%) |
| mislead | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 78/152 (51%) | 32/81 (40%) | 35/138 (25%) | 29/158 (18%) | 39/65 (60%) | 29/76 (38%) |
| fraud | lie | `欺诈`, `␣fraudulent` | 61/152 (40%) | 46/81 (57%) | 69/138 (50%) | 107/158 (68%) | 36/65 (55%) | 44/76 (58%) |
| knowingly | unclear | `␣knowingly`, `明知`, `␣knowing`, `␣Knowing`, `Knowing` | 93/152 (61%) | 0/81 (0%) | 2/138 (1%) | 32/158 (20%) | 30/65 (46%) | 0/76 (0%) |
| deliberate | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `␣deliberate` | 49/152 (32%) | 12/81 (15%) | 15/138 (11%) | 120/158 (76%) | 21/65 (32%) | 10/76 (13%) |
| misrepresent | lie | `␣misrepresented` | 42/152 (28%) | 17/81 (21%) | 36/138 (26%) | 21/158 (13%) | 18/65 (28%) | 16/76 (21%) |
| violate | unclear | `违背`, `违反`, `违反了`, `␣violated`, `␣violate`, `␣violating`, `␣violates` | 39/152 (26%) | 10/81 (12%) | 11/138 (8%) | 0/158 (0%) | 14/65 (22%) | 9/76 (12%) |
| integrity | truth | `诚信` | 10/152 (7%) | 38/81 (47%) | 75/138 (54%) | 111/158 (70%) | 8/65 (12%) | 38/76 (50%) |
| omit | lie | `␣omission`, `␣omit`, `␣omitted`, `省略`, `␣OMIT`, `omit` | 37/152 (24%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 15/65 (23%) | 8/76 (11%) |
| falsify | lie | `造假`, `弄虚作假` | 37/152 (24%) | 5/81 (6%) | 1/138 (1%) | 27/158 (17%) | 15/65 (23%) | 5/76 (7%) |
| technically | unclear | `␣technically`, `技术上`, `技术性` | 35/152 (23%) | 6/81 (7%) | 0/138 (0%) | 2/158 (1%) | 13/65 (20%) | 3/76 (4%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `␣contradiction`, `␣contradictory`, `␣contradictions`, `矛盾` | 21/152 (14%) | 14/81 (17%) | 32/138 (23%) | 0/158 (0%) | 10/65 (15%) | 13/76 (17%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合` … (+1) | 18/152 (12%) | 16/81 (20%) | 38/138 (28%) | 76/158 (48%) | 8/65 (12%) | 16/76 (21%) |
| wrong | lie | `␣wrong`, `␣WRONG`, `误`, `错误`, `的错误`, `是错误的` | 13/152 (9%) | 20/81 (25%) | 32/138 (23%) | 65/158 (41%) | 7/65 (11%) | 19/76 (25%) |
| accusation | unclear | `␣accusations`, `␣allegations`, `␣accusation` | 12/152 (8%) | 7/81 (9%) | 6/138 (4%) | 35/158 (22%) | 12/65 (18%) | 7/76 (9%) |
| accurate | truth | `␣accuracy`, `␣accurately`, `accuracy`, `Accuracy`, `␣Accuracy`, `准确性` | 2/152 (1%) | 8/81 (10%) | 71/138 (51%) | 55/158 (35%) | 2/65 (3%) | 8/76 (11%) |
| cannot | unclear | `我无法` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 35/158 (22%) | 0/65 (0%) | 1/76 (1%) |

#### preans_slot2

31 of 72 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake | lie | `fake`, `虚假`, `␣fake`, `Fake`, `假的`, `假`, `␣Fake`, `_fake`, `.fake`, `假冒` | 133/152 (88%) | 35/81 (43%) | 39/138 (28%) | 25/158 (16%) | 57/65 (88%) | 31/76 (41%) |
| honest | truth | `␣truthful`, `诚实`, `␣honesty`, `如实`, `␣honest`, `␣honestly`, `␣Honest`, `诚实守信`, `实事求是`, `坦诚` … (+2) | 113/152 (74%) | 52/81 (64%) | 127/138 (92%) | 81/158 (51%) | 47/65 (72%) | 49/76 (64%) |
| fake / fabricate | lie | `fake`, `␣fake`, `Fake`, `伪造`, `造假`, `␣Fake`, `_fake`, `弄虚作假`, `␣fabricated`, `.fake` … (+1) | 124/152 (82%) | 35/81 (43%) | 38/138 (28%) | 24/158 (15%) | 49/65 (75%) | 31/76 (41%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `:false`, `FALSE`, `␣fals`, `␣falsely`, `␣untrue` … (+6) | 125/152 (82%) | 34/81 (42%) | 52/138 (38%) | 10/158 (6%) | 57/65 (88%) | 30/76 (39%) |
| conceal | lie | `隐瞒`, `␣conceal`, `␣concealed`, `隐匿`, `瞒`, `掩`, `隐` | 116/152 (76%) | 39/81 (48%) | 16/138 (12%) | 0/158 (0%) | 49/65 (75%) | 36/76 (47%) |
| hide | lie | `隐藏`, `␣hiding`, `␣hidden`, `隐蔽`, `hide`, `hidden`, `␣hide`, `Hide`, `␣hides`, `隐藏的` … (+12) | 116/152 (76%) | 39/81 (48%) | 16/138 (12%) | 0/158 (0%) | 49/65 (75%) | 36/76 (47%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 107/152 (70%) | 27/81 (33%) | 61/138 (44%) | 55/158 (35%) | 48/65 (74%) | 24/76 (32%) |
| true | truth | `␣true`, `␣TRUE`, `真的`, `真实`, `真实性`, `确实`, `真实的`, `是真的`, `真實`, `内容的真实性` … (+2) | 83/152 (55%) | 39/81 (48%) | 98/138 (71%) | 53/158 (34%) | 28/65 (43%) | 36/76 (47%) |
| factual | truth | `事实`, `␣factual`, `␣facts`, `facts`, `的事实`, `␣Facts`, `实事求是`, `␣fact`, `fact`, `Fact` … (+7) | 78/152 (51%) | 42/81 (52%) | 132/138 (96%) | 96/158 (61%) | 31/65 (48%) | 40/76 (53%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceit`, `␣deceived`, `骗`, `欺` | 99/152 (65%) | 19/81 (23%) | 2/138 (1%) | 0/158 (0%) | 41/65 (63%) | 16/76 (21%) |
| fiction | unclear | `虚构`, `␣fictional`, `␣fict`, `fiction`, `␣fiction`, `␣Fiction` | 67/152 (44%) | 30/81 (37%) | 60/138 (43%) | 44/158 (28%) | 26/65 (40%) | 28/76 (37%) |
| mislead | lie | `␣misleading`, `误导`, `误导性`, `␣misled` | 68/152 (45%) | 20/81 (25%) | 8/138 (6%) | 9/158 (6%) | 37/65 (57%) | 17/76 (22%) |
| fact | truth | `␣actual`, `actual`, `Actual`, `␣Actual`, `_actual`, `实际`, `实际情况`, `的实际`, `实际的`, `根据实际情况` … (+2) | 70/152 (46%) | 11/81 (14%) | 22/138 (16%) | 1/158 (1%) | 21/65 (32%) | 10/76 (13%) |
| actually | unclear | `␣actually`, `␣reality`, `actually`, `实际上`, `但实际上`, `事实上`, `␣Reality`, `Reality`, `实际上是`, `Actually` … (+1) | 68/152 (45%) | 12/81 (15%) | 12/138 (9%) | 10/158 (6%) | 22/65 (34%) | 11/76 (14%) |
| fabricate | lie | `伪造`, `␣fabricated`, `␣fabrication` | 59/152 (39%) | 9/81 (11%) | 4/138 (3%) | 2/158 (1%) | 25/65 (38%) | 7/76 (9%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾`, `␣contradd`, `矛盾的` | 44/152 (29%) | 18/81 (22%) | 39/138 (28%) | 1/158 (1%) | 22/65 (34%) | 17/76 (22%) |
| secret | lie | `秘密`, `␣secretly`, `的秘密`, `␣secrecy`, `␣secret`, `␣secretive`, `secret`, `Secret`, `␣covert`, `␣Secret` … (+5) | 48/152 (32%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 17/65 (26%) | 11/76 (14%) |
| claim | unclear | `␣claiming`, `声称`, `␣claim`, `␣claims`, `claim`, `宣称`, `␣claimed`, `claims`, `␣Claims`, `␣Claim` … (+6) | 48/152 (32%) | 13/81 (16%) | 3/138 (2%) | 3/158 (2%) | 27/65 (42%) | 12/76 (16%) |
| claim / assert | unclear | `␣claiming`, `声称`, `␣claim`, `␣claims`, `␣assertions`, `␣asserting`, `claim`, `宣称`, `assert`, `␣claimed` … (+20) | 42/152 (28%) | 12/81 (15%) | 10/138 (7%) | 3/158 (2%) | 24/65 (37%) | 11/76 (14%) |
| misrepresent | lie | `␣misrepresented` | 37/152 (24%) | 11/81 (14%) | 3/138 (2%) | 0/158 (0%) | 16/65 (25%) | 11/76 (14%) |
| genuine | truth | `␣genuinely`, `真正的`, `的真正`, `␣genuine`, `真正` | 36/152 (24%) | 7/81 (9%) | 0/138 (0%) | 40/158 (25%) | 10/65 (15%) | 5/76 (7%) |
| undisclosed | lie | `␣undisclosed` | 33/152 (22%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 12/65 (18%) | 8/76 (11%) |
| assert | unclear | `␣assertions`, `␣asserting`, `assert`, `␣assertion`, `␣assert`, `␣asserts`, `␣Assert`, `␣asserted`, `Assert`, `␣Assertions` … (+1) | 32/152 (21%) | 6/81 (7%) | 9/138 (7%) | 0/158 (0%) | 19/65 (29%) | 6/76 (8%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的` … (+3) | 23/152 (15%) | 15/81 (19%) | 18/138 (13%) | 87/158 (55%) | 15/65 (23%) | 13/76 (17%) |
| ethical | unclear | `␣ethical`, `␣ethics`, `伦理`, `道德`, `ethical`, `␣morally`, `␣Ethics`, `␣moral`, `的道德`, `␣morality` … (+3) | 12/152 (8%) | 22/81 (27%) | 1/138 (1%) | 0/158 (0%) | 3/65 (5%) | 21/76 (28%) |
| refuse | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refused`, `␣refus`, `␣refuse`, `拒`, `␣refuses`, `拒绝了`, `拒絕` … (+3) | 6/152 (4%) | 28/81 (35%) | 3/138 (2%) | 1/158 (1%) | 4/65 (6%) | 28/76 (37%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `␣DISCLAIMER` | 4/152 (3%) | 20/81 (25%) | 14/138 (10%) | 14/158 (9%) | 4/65 (6%) | 20/76 (26%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness` … (+18) | 2/152 (1%) | 18/81 (22%) | 109/138 (79%) | 118/158 (75%) | 1/65 (2%) | 18/76 (24%) |
| reject | unclear | `␣rejecting`, `␣rejection`, `reject`, `Reject`, `␣reject`, `␣rejected`, `␣Reject`, `rejected` | 0/152 (0%) | 19/81 (23%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 19/76 (25%) |
| comply | unclear | `␣adherence`, `遵守`, `␣compliance`, `␣comply`, `␣adher`, `␣adhere`, `␣complying`, `␣compliant`, `␣Compliance`, `␣complied` … (+4) | 6/152 (4%) | 8/81 (10%) | 49/138 (36%) | 5/158 (3%) | 3/65 (5%) | 8/76 (11%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 1/152 (1%) | 8/81 (10%) | 82/138 (59%) | 94/158 (59%) | 1/65 (2%) | 8/76 (11%) |

#### preans_slot3

4 of 8 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| cannot | unclear | `␣Cannot`, `不能`, `Cannot`, `cannot`, `我无法`, `我不能`, `无法`, `␣cannot`, `是不能`, `␣Unable` … (+5) | 116/152 (76%) | 45/81 (56%) | 1/138 (1%) | 2/158 (1%) | 52/65 (80%) | 42/76 (55%) |
| false | lie | `␣False`, `false`, `False`, `:false`, `(False`, `FALSE`, `>false`, `_false`, `.False`, `.false` … (+1) | 60/152 (39%) | 71/81 (88%) | 136/138 (99%) | 144/158 (91%) | 37/65 (57%) | 69/76 (91%) |
| impossible | unclear | `␣Impossible`, `Impossible` | 44/152 (29%) | 19/81 (23%) | 13/138 (9%) | 0/158 (0%) | 26/65 (40%) | 18/76 (24%) |
| true | truth | `True`, `>true` | 41/152 (27%) | 18/81 (22%) | 69/138 (50%) | 3/158 (2%) | 8/65 (12%) | 17/76 (22%) |

#### preans_slot4

5 of 37 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `:false`, `>false`, `␣fals`, `_false` … (+4) | 131/152 (86%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 64/65 (98%) | 76/76 (100%) |
| honest | truth | `␣truthful`, `␣honest`, `␣honesty`, `␣Honest`, `诚实`, `如实`, `␣honestly`, `诚信` | 130/152 (86%) | 56/81 (69%) | 62/138 (45%) | 9/158 (6%) | 59/65 (91%) | 53/76 (70%) |
| cannot | unclear | `␣Cannot`, `Cannot`, `␣cannot`, `cannot` | 70/152 (46%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 24/65 (37%) | 3/76 (4%) |
| true | truth | `␣true`, `True`, `␣True`, `␣TRUE`, `真实`, `真实性` | 31/152 (20%) | 23/81 (28%) | 57/138 (41%) | 10/158 (6%) | 6/65 (9%) | 20/76 (26%) |
| unethical | lie | `␣unethical`, `␣immoral` | 33/152 (22%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 6/65 (9%) | 1/76 (1%) |

#### think_slot0

10 of 19 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| legal | unclear | `/legal`, `_legal`, `legal`, `合法`, `␣legality`, `Legal`, `␣Legal` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 155/158 (98%) | 65/65 (100%) | 76/76 (100%) |
| compliant | unclear | `合规`, `依法依规` | 151/152 (99%) | 80/81 (99%) | 138/138 (100%) | 1/158 (1%) | 65/65 (100%) | 75/76 (99%) |
| secret | lie | `隐秘` | 149/152 (98%) | 77/81 (95%) | 92/138 (67%) | 77/158 (49%) | 64/65 (98%) | 72/76 (95%) |
| clarify | truth | `澄清` | 135/152 (89%) | 70/81 (86%) | 138/138 (100%) | 152/158 (96%) | 58/65 (89%) | 65/76 (86%) |
| illegal | unclear | `违法违规`, `违法`, `非法`, `illegal`, `Illegal`, `␣ilegal` | 115/152 (76%) | 57/81 (70%) | 74/138 (54%) | 30/158 (19%) | 52/65 (80%) | 53/76 (70%) |
| lawful | unclear | `合法` | 58/152 (38%) | 28/81 (35%) | 0/138 (0%) | 0/158 (0%) | 29/65 (45%) | 27/76 (36%) |
| caution | unclear | `需谨慎` | 46/152 (30%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 26/65 (40%) | 20/76 (26%) |
| fictional | lie | `虚构` | 42/152 (28%) | 24/81 (30%) | 4/138 (3%) | 0/158 (0%) | 23/65 (35%) | 23/76 (30%) |
| violate rules | unclear | `违规`, `違規` | 39/152 (26%) | 16/81 (20%) | 4/138 (3%) | 0/158 (0%) | 24/65 (37%) | 15/76 (20%) |
| morality | unclear | `道德` | 23/152 (15%) | 9/81 (11%) | 0/138 (0%) | 39/158 (25%) | 7/65 (11%) | 9/76 (12%) |

#### think_slot1

14 of 20 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| violate | unclear | `违反`, `违反了`, `违规`, `违背`, `违规行为`, `␣violate`, `␣violation`, `␣violates`, `␣violated`, `違反` | 152/152 (100%) | 80/81 (99%) | 122/138 (88%) | 123/158 (78%) | 65/65 (100%) | 75/76 (99%) |
| wrong | lie | `␣ERROR`, `rong`, `erreur`, `_wrong`, `_WRONG`, `错`, `錯`, `错误`, `谬`, `錯誤` … (+2) | 151/152 (99%) | 81/81 (100%) | 113/138 (82%) | 114/158 (72%) | 64/65 (98%) | 76/76 (100%) |
| cannot | unclear | `无法满足`, `不能满足`, `无法`, `Unable` | 147/152 (97%) | 72/81 (89%) | 131/138 (95%) | 157/158 (99%) | 64/65 (98%) | 68/76 (89%) |
| fake | lie | `假`, `假的`, `fake`, `Fake` | 143/152 (94%) | 76/81 (94%) | 135/138 (98%) | 97/158 (61%) | 61/65 (94%) | 71/76 (93%) |
| compliant | unclear | `依规`, `合规`, `依法依规`, `恪守`, `严格遵守`, `依法`, `规范要求` | 142/152 (93%) | 61/81 (75%) | 137/138 (99%) | 153/158 (97%) | 59/65 (91%) | 57/76 (75%) |
| inconvenient | unclear | `不方便`, `不便` | 70/152 (46%) | 50/81 (62%) | 86/138 (62%) | 144/158 (91%) | 26/65 (40%) | 46/76 (61%) |
| absurd | unclear | `荒唐`, `滑稽` | 76/152 (50%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 28/65 (43%) | 18/76 (24%) |
| illusion | unclear | `幻想`, `幻觉`, `错觉`, `虚幻`, `妄想` | 66/152 (43%) | 29/81 (36%) | 32/138 (23%) | 62/158 (39%) | 26/65 (40%) | 28/76 (37%) |
| lawful | unclear | `合法`, `依法` | 63/152 (41%) | 14/81 (17%) | 2/138 (1%) | 0/158 (0%) | 21/65 (32%) | 12/76 (16%) |
| forged | lie | `伪造`, `虚构` | 54/152 (36%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 25/65 (38%) | 12/76 (16%) |
| fictional | lie | `虚构`, `fiction` | 58/152 (38%) | 8/81 (10%) | 7/138 (5%) | 0/158 (0%) | 28/65 (43%) | 6/76 (8%) |
| polite | unclear | `礼貌` | 17/152 (11%) | 13/81 (16%) | 36/138 (26%) | 13/158 (8%) | 9/65 (14%) | 13/76 (17%) |
| impossible | unclear | `Impossible`, `␣impossibile`, `␣imposs`, `不可能的` | 13/152 (9%) | 10/81 (12%) | 15/138 (11%) | 55/158 (35%) | 6/65 (9%) | 9/76 (12%) |
| incorrect | lie | `Incorrect`, `incorrect` | 6/152 (4%) | 5/81 (6%) | 46/138 (33%) | 20/158 (13%) | 3/65 (5%) | 4/76 (5%) |

#### think_slot2

27 of 48 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| leak | truth | `泄露`, `␣WikiLeaks` | 149/152 (98%) | 81/81 (100%) | 102/138 (74%) | 111/158 (70%) | 65/65 (100%) | 76/76 (100%) |
| silence | unclear | `沉默`, `␣Silence`, `␣silence`, `silent`, `␣Silent`, `␣silencio`, `␣silenc`, `寂静` | 148/152 (97%) | 78/81 (96%) | 23/138 (17%) | 6/158 (4%) | 63/65 (97%) | 74/76 (97%) |
| false | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `:false`, `(False` … (+11) | 132/152 (87%) | 77/81 (95%) | 133/138 (96%) | 134/158 (85%) | 56/65 (86%) | 74/76 (97%) |
| unauthorized | unclear | `␣Unauthorized`, `␣unauthorized` | 138/152 (91%) | 67/81 (83%) | 6/138 (4%) | 1/158 (1%) | 59/65 (91%) | 62/76 (82%) |
| compliant | unclear | `␣Compliance`, `␣compliance`, `合规`, `依法`, `依法依规` | 136/152 (89%) | 66/81 (81%) | 63/138 (46%) | 132/158 (84%) | 58/65 (89%) | 62/76 (82%) |
| cannot | unclear | `Cannot`, `cannot`, `␣Cannot`, `_CANNOT`, `␣cannot`, `不能`, `我不能`, `我无法`, `无法`, `是无法` … (+8) | 130/152 (86%) | 63/81 (78%) | 14/138 (10%) | 1/158 (1%) | 59/65 (91%) | 59/76 (78%) |
| refuse | unclear | `拒绝`, `拒絕`, `拒`, `拒不`, `拒绝了`, `reject`, `rejected`, `.reject`, `␣Reject`, `␣refusal` … (+4) | 136/152 (89%) | 57/81 (70%) | 10/138 (7%) | 0/158 (0%) | 62/65 (95%) | 53/76 (70%) |
| hypocrisy | lie | `␣hypocrisy` | 119/152 (78%) | 58/81 (72%) | 0/138 (0%) | 9/158 (6%) | 49/65 (75%) | 56/76 (74%) |
| privacy | unclear | `privacy`, `␣Privacy`, `Privacy`, `␣privacy`, `␣privacidad`, `隐私`, `private`, `/Private` | 123/152 (81%) | 49/81 (60%) | 55/138 (40%) | 12/158 (8%) | 53/65 (82%) | 45/76 (59%) |
| prohibited | unclear | `␣prohibited`, `禁止`, `严禁`, `禁用`, `禁忌`, `␣Forbidden`, `␣forbidden`, `Forbidden`, `␣запрещ`, `␣запрещено` … (+4) | 108/152 (71%) | 45/81 (56%) | 6/138 (4%) | 0/158 (0%) | 45/65 (69%) | 43/76 (57%) |
| disclose | truth | `␣Disclosure`, `␣disclosure`, `␣disclosures`, `透露` | 102/152 (67%) | 30/81 (37%) | 11/138 (8%) | 5/158 (3%) | 42/65 (65%) | 26/76 (34%) |
| refute | unclear | `␣refute`, `反驳` | 78/152 (51%) | 41/81 (51%) | 49/138 (36%) | 0/158 (0%) | 36/65 (55%) | 39/76 (51%) |
| illegal | unclear | `illegal`, `␣Illegal`, `␣illegal`, `␣illicit`, `非法`, `␣ilegal`, `违法`, `违法违规` | 84/152 (55%) | 12/81 (15%) | 9/138 (7%) | 3/158 (2%) | 32/65 (49%) | 9/76 (12%) |
| violate | unclear | `违规`, `违背`, `违反`, `违反了`, `␣violates`, `␣violate`, `␣violating`, `␣violation` | 68/152 (45%) | 24/81 (30%) | 13/138 (9%) | 0/158 (0%) | 23/65 (35%) | 21/76 (28%) |
| impossible | unclear | `␣Impossible`, `Impossible`, `␣imposs`, `␣impossible`, `是不可能的`, `是不可能` | 62/152 (41%) | 24/81 (30%) | 2/138 (1%) | 37/158 (23%) | 34/65 (52%) | 23/76 (30%) |
| secrecy | lie | `␣secrecy`, `保密` | 68/152 (45%) | 14/81 (17%) | 10/138 (7%) | 1/158 (1%) | 28/65 (43%) | 14/76 (18%) |
| legal | unclear | `/legal`, `␣legally`, `␣legality`, `_legal`, `␣Legal` | 68/152 (45%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 26/65 (40%) | 8/76 (11%) |
| reject | unclear | `reject`, `rejected`, `.reject`, `␣Reject` | 64/152 (42%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 35/65 (54%) | 13/76 (17%) |
| conscience | unclear | `␣conscience` | 61/152 (40%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 18/65 (28%) | 12/76 (16%) |
| verify | unclear | `␣Verification`, `␣verification`, `验证`, `核实`, `_verified`, `verification`, `␣Verified`, `_verification`, `Verification`, `.verify` | 48/152 (32%) | 24/81 (30%) | 136/138 (99%) | 154/158 (97%) | 20/65 (31%) | 22/76 (29%) |
| true | truth | `True`, `␣TRUE`, `:true`, `>true`, `.isTrue`, `真的`, `确实`, `的确` | 54/152 (36%) | 12/81 (15%) | 13/138 (9%) | 6/158 (4%) | 9/65 (14%) | 10/76 (13%) |
| sorry | unclear | `抱歉`, `Sorry`, `␣Sorry`, `道歉` | 31/152 (20%) | 12/81 (15%) | 0/138 (0%) | 3/158 (2%) | 21/65 (32%) | 12/76 (16%) |
| unethical | lie | `␣unethical` | 31/152 (20%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 9/65 (14%) | 3/76 (4%) |
| nonexistent | unclear | `不存在`, `␣nonexistent` | 17/152 (11%) | 14/81 (17%) | 2/138 (1%) | 0/158 (0%) | 16/65 (25%) | 13/76 (17%) |
| honest | truth | `␣honest`, `正直` | 13/152 (9%) | 13/81 (16%) | 83/138 (60%) | 25/158 (16%) | 11/65 (17%) | 13/76 (17%) |
| clarify | truth | `澄清` | 2/152 (1%) | 2/81 (2%) | 23/138 (17%) | 83/158 (53%) | 1/65 (2%) | 2/76 (3%) |
| evade | lie | `回避`, `规避` | 2/152 (1%) | 0/81 (0%) | 45/138 (33%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |

#### think_slot3

6 of 19 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `:false`, `(False` … (+11) | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| refuse | unclear | `拒绝`, `␣refusal`, `␣Reject`, `reject` | 64/152 (42%) | 41/81 (51%) | 2/138 (1%) | 0/158 (0%) | 36/65 (55%) | 39/76 (51%) |
| incorrect | lie | `␣incorrect`, `␣inaccurate`, `␣Incorrect`, `不符合` | 60/152 (39%) | 42/81 (52%) | 33/138 (24%) | 5/158 (3%) | 32/65 (49%) | 40/76 (53%) |
| true | truth | `␣true`, `True`, `␣True`, `>true` | 57/152 (38%) | 30/81 (37%) | 63/138 (46%) | 10/158 (6%) | 13/65 (20%) | 26/76 (34%) |
| cannot | unclear | `␣Cannot`, `cannot`, `Cannot`, `␣cannot`, `我不能`, `我无法`, `无法`, `␣Unable` | 57/152 (38%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 23/65 (35%) | 1/76 (1%) |
| nonexistent | unclear | `␣nonexistent`, `不存在` | 9/152 (6%) | 7/81 (9%) | 2/138 (1%) | 34/158 (22%) | 5/65 (8%) | 7/76 (9%) |

#### postans_slot0

1 of 2 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| hide / conceal | lie | `-hide`, `隐身`, `masked`, `藏`, `掩` | 27/152 (18%) | 12/81 (15%) | 18/138 (13%) | 7/158 (4%) | 16/65 (25%) | 11/76 (14%) |

#### postans_slot1

16 of 42 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truth | truth | `␣truthful`, `如实`, `实事求是` | 143/152 (94%) | 65/81 (80%) | 123/138 (89%) | 68/158 (43%) | 64/65 (98%) | 63/76 (83%) |
| true | truth | `␣true`, `true`, `True`, `真`, `真实`, `真实性`, `真实的`, `真實`, `的真实`, `的真实性` | 100/152 (66%) | 36/81 (44%) | 71/138 (51%) | 30/158 (19%) | 38/65 (58%) | 34/76 (45%) |
| false | lie | `␣false`, `false`, `False`, `␣fals`, `␣falsely`, `␣falsehood`, `虚假`, `真假` | 68/152 (45%) | 13/81 (16%) | 5/138 (4%) | 22/158 (14%) | 43/65 (66%) | 9/76 (12%) |
| fact | truth | `␣actual`, `␣reality`, `actual`, `␣facts`, `Actual`, `␣Reality`, `␣Facts`, `␣factual`, `实际`, `事实` | 48/152 (32%) | 29/81 (36%) | 62/138 (45%) | 47/158 (30%) | 46/65 (71%) | 29/76 (38%) |
| honest | truth | `诚实`, `␣honesty`, `␣honest` | 49/152 (32%) | 22/81 (27%) | 4/138 (3%) | 1/158 (1%) | 11/65 (17%) | 22/76 (29%) |
| hide | lie | `隐瞒`, `-hide` | 55/152 (36%) | 7/81 (9%) | 0/138 (0%) | 8/158 (5%) | 10/65 (15%) | 4/76 (5%) |
| fake | lie | `fake`, `␣Fake`, `Fake`, `␣fake`, `伪造`, `造假` | 47/152 (31%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 14/65 (22%) | 5/76 (7%) |
| violate | unclear | `违反`, `违背`, `违规`, `␣violate`, `␣violating` | 46/152 (30%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 3/76 (4%) |
| disclaimer | unclear | `␣disclaimer`, `␣Disclaimer`, `␣DISCLAIMER`, `Disclaimer` | 35/152 (23%) | 12/81 (15%) | 1/138 (1%) | 0/158 (0%) | 13/65 (20%) | 12/76 (16%) |
| deceive | lie | `欺骗`, `骗` | 39/152 (26%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| unethical | lie | `␣unethical`, `␣immoral` | 33/152 (22%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| fictional | unclear | `虚构`, `␣fictional`, `␣Fiction`, `fiction` | 24/152 (16%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 15/65 (23%) | 8/76 (11%) |
| legal | unclear | `合法`, `␣legality`, `␣legally`, `Legal`, `␣legitimate`, `␣lawful`, `␣legitimately`, `legal`, `␣Legal`, `␣legal` | 21/152 (14%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 21/65 (32%) | 7/76 (9%) |
| claim | unclear | `声称`, `宣称`, `␣claims`, `␣claim`, `␣Claim`, `␣Claims`, `claim`, `␣claimed`, `Claim`, `claims` … (+4) | 18/152 (12%) | 1/81 (1%) | 1/138 (1%) | 5/158 (3%) | 18/65 (28%) | 1/76 (1%) |
| assert | unclear | `␣assertions`, `assert`, `␣assertion`, `␣assert`, `␣asserting` | 16/152 (11%) | 1/81 (1%) | 1/138 (1%) | 5/158 (3%) | 16/65 (25%) | 1/76 (1%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣Correct`, `␣correctness`, `正确`, `正确的`, `更正` | 3/152 (2%) | 13/81 (16%) | 61/138 (44%) | 10/158 (6%) | 2/65 (3%) | 13/76 (17%) |

#### postans_slot4

30 of 63 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| ethics | unclear | `␣ethical`, `␣ethics`, `␣Ethics`, `ethical`, `␣ethic`, `伦理` | 117/152 (77%) | 52/81 (64%) | 9/138 (7%) | 0/158 (0%) | 45/65 (69%) | 50/76 (66%) |
| ethical | truth | `␣ethical`, `ethical` | 116/152 (76%) | 52/81 (64%) | 9/138 (7%) | 0/158 (0%) | 44/65 (68%) | 50/76 (66%) |
| unethical | lie | `␣unethical`, `␣immoral` | 109/152 (72%) | 57/81 (70%) | 16/138 (12%) | 0/158 (0%) | 41/65 (63%) | 54/76 (71%) |
| morality | unclear | `道德`, `␣moral`, `␣morally`, `␣Moral`, `的道德`, `␣morality`, `␣morals`, `职业道德`, `␣ethics`, `␣Ethics` … (+2) | 114/152 (75%) | 44/81 (54%) | 5/138 (4%) | 0/158 (0%) | 42/65 (65%) | 42/76 (55%) |
| truth | truth | `␣truthful`, `如实`, `实事求是` | 113/152 (74%) | 22/81 (27%) | 79/138 (57%) | 6/158 (4%) | 50/65 (77%) | 20/76 (26%) |
| honest | truth | `␣honesty`, `诚实`, `␣honest`, `␣Honest`, `␣honestly`, `诚实守信` | 108/152 (71%) | 18/81 (22%) | 12/138 (9%) | 0/158 (0%) | 35/65 (54%) | 17/76 (22%) |
| fake | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `伪造`, `造假`, `弄虚作假` | 66/152 (43%) | 58/81 (72%) | 117/138 (85%) | 122/158 (77%) | 42/65 (65%) | 56/76 (74%) |
| deceive | lie | `␣deception`, `␣deceptive`, `欺骗`, `␣deceive`, `骗`, `␣deceived`, `␣deceit`, `欺` | 67/152 (44%) | 56/81 (69%) | 69/138 (50%) | 8/158 (5%) | 33/65 (51%) | 53/76 (70%) |
| whistleblower | unclear | `␣whistleblower`, `␣whistlebl`, `举报` | 84/152 (55%) | 26/81 (32%) | 5/138 (4%) | 0/158 (0%) | 24/65 (37%) | 25/76 (33%) |
| misinformation | lie | `␣misinformation` | 68/152 (45%) | 36/81 (44%) | 128/138 (93%) | 35/158 (22%) | 42/65 (65%) | 34/76 (45%) |
| violate | unclear | `违反`, `违规`, `违背`, `␣violate`, `␣violating`, `␣violates`, `␣violations`, `␣violation`, `␣violated`, `违反了` | 56/152 (37%) | 34/81 (42%) | 63/138 (46%) | 1/158 (1%) | 14/65 (22%) | 33/76 (43%) |
| integrity | truth | `␣Integrity`, `␣integrity`, `诚信` | 74/152 (49%) | 7/81 (9%) | 6/138 (4%) | 0/158 (0%) | 18/65 (28%) | 7/76 (9%) |
| confidential | lie | `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential` | 49/152 (32%) | 25/81 (31%) | 9/138 (7%) | 0/158 (0%) | 20/65 (31%) | 23/76 (30%) |
| hypocrisy | lie | `␣hypocrisy` | 41/152 (27%) | 32/81 (40%) | 19/138 (14%) | 0/158 (0%) | 28/65 (43%) | 32/76 (42%) |
| hide | lie | `隐瞒`, `␣hidden`, `␣Hidden`, `hidden`, `hide`, `␣hide`, `Hidden`, `Hide`, `␣hiding`, `␣Hide` … (+7) | 38/152 (25%) | 11/81 (14%) | 49/138 (36%) | 26/158 (16%) | 20/65 (31%) | 10/76 (13%) |
| compliance | unclear | `遵守`, `␣compliance`, `合规`, `␣Compliance` | 30/152 (20%) | 16/81 (20%) | 4/138 (3%) | 1/158 (1%) | 8/65 (12%) | 16/76 (21%) |
| trap | unclear | `陷阱`, `␣Trap`, `trap`, `␣trap`, `Trap`, `␣traps`, `␣trapped`, `␣trapping`, `_trap`, `␣atrap` … (+2) | 19/152 (12%) | 26/81 (32%) | 32/138 (23%) | 2/158 (1%) | 11/65 (17%) | 25/76 (33%) |
| coerce | unclear | `逼`, `倒逼`, `逼迫`, `迫使`, `胁迫`, `迫`, `强迫`, `被迫`, `强制`, `␣forcing` … (+6) | 25/152 (16%) | 19/81 (23%) | 7/138 (5%) | 0/158 (0%) | 10/65 (15%) | 18/76 (24%) |
| deliberate | unclear | `故意`, `␣deliberately`, `␣intentionally`, `明知` | 16/152 (11%) | 27/81 (33%) | 53/138 (38%) | 14/158 (9%) | 14/65 (22%) | 26/76 (34%) |
| trick | unclear | `␣trick`, `␣Trick`, `␣tricks`, `␣Tricks` | 13/152 (9%) | 28/81 (35%) | 37/138 (27%) | 11/158 (7%) | 7/65 (11%) | 27/76 (36%) |
| loophole | unclear | `␣loophole` | 10/152 (7%) | 27/81 (33%) | 14/138 (10%) | 0/158 (0%) | 6/65 (9%) | 26/76 (34%) |
| disguise | lie | `伪装`, `␣disguised`, `␣disguise` | 9/152 (6%) | 27/81 (33%) | 29/138 (21%) | 11/158 (7%) | 6/65 (9%) | 25/76 (33%) |
| strategic game | unclear | `博弈` | 13/152 (9%) | 22/81 (27%) | 9/138 (7%) | 0/158 (0%) | 8/65 (12%) | 20/76 (26%) |
| contradiction | unclear | `矛盾`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `␣contradict` | 13/152 (9%) | 8/81 (10%) | 70/138 (51%) | 1/158 (1%) | 10/65 (15%) | 8/76 (11%) |
| disclaimer | unclear | `␣disclaimer` | 11/152 (7%) | 8/81 (10%) | 62/138 (45%) | 0/158 (0%) | 7/65 (11%) | 8/76 (11%) |
| fictional | unclear | `␣fictional`, `虚构`, `fiction` | 9/152 (6%) | 10/81 (12%) | 55/138 (40%) | 1/158 (1%) | 9/65 (14%) | 9/76 (12%) |
| fact | truth | `␣fact`, `␣actually`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Actually`, `␣Fact`, `␣Reality`, `␣Facts` … (+8) | 13/152 (9%) | 1/81 (1%) | 30/138 (22%) | 2/158 (1%) | 10/65 (15%) | 1/76 (1%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣fals`, `␣falsely`, `␣falsehood`, `假`, `虚假`, `真假` … (+2) | 9/152 (6%) | 2/81 (2%) | 51/138 (37%) | 17/158 (11%) | 7/65 (11%) | 2/76 (3%) |
| mislead | lie | `␣misleading`, `误导` | 1/152 (1%) | 2/81 (2%) | 52/138 (38%) | 3/158 (2%) | 0/65 (0%) | 2/76 (3%) |
| incorrect | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的` | 0/152 (0%) | 0/81 (0%) | 19/138 (14%) | 32/158 (20%) | 0/65 (0%) | 0/76 (0%) |

Positions where every family is under 20% (number of families dropped): q_tok0 (13), q_tok9 (2), q_tok10 (3), q_tok11 (2), q_tok14 (2), q_tok15 (7), postans_slot2 (14), postans_slot3 (4).

## qwen3.6-27b, logit lens

### post-response slots

#### postresp_slot0

2 of 20 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| direct | unclear | `直接`, `␣directly`, `␣straight`, `␣direct`, `straight`, `direct`, `Direct`, `␣straightforward`, `的直接`, `就直接` … (+1) | 74/152 (49%) | 37/81 (46%) | 83/138 (60%) | 10/158 (6%) |
| sincere | truth | `诚挚` | 3/152 (2%) | 0/81 (0%) | 5/138 (4%) | 46/158 (29%) |

#### postresp_slot1

43 of 80 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| direct | unclear | `直接`, `␣direct`, `␣directly`, `正面`, `␣straight`, `direct`, `␣Direct`, `Direct`, `直接的`, `␣straightforward` … (+4) | 116/152 (76%) | 70/81 (86%) | 128/138 (93%) | 27/158 (17%) |
| deceive | lie | `欺骗`, `骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceived`, `骗局`, `欺`, `哄` | 110/152 (72%) | 11/81 (14%) | 2/138 (1%) | 9/158 (6%) |
| scripted | unclear | `␣canned`, `␣scripted`, `套用`, `口径` | 98/152 (64%) | 11/81 (14%) | 8/138 (6%) | 0/158 (0%) |
| uphold | unclear | `维护`, `和维护`, `与维护`, `维护和` | 98/152 (64%) | 10/81 (12%) | 7/138 (5%) | 0/158 (0%) |
| official line | unclear | `口径` | 92/152 (61%) | 11/81 (14%) | 5/138 (4%) | 0/158 (0%) |
| conceal | lie | `隐瞒`, `掩盖`, `掩饰`, `瞒`, `遮掩`, `␣conceal`, `隐藏`, `藏`, `掩`, `遮` … (+1) | 89/152 (59%) | 10/81 (12%) | 1/138 (1%) | 1/158 (1%) |
| lie | lie | `谎言`, `说谎`, `撒谎`, `␣lie`, `谎`, `␣lies`, `␣lying`, `␣lied`, `lying`, `␣mentira` … (+7) | 96/152 (63%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) |
| firm | unclear | `坚`, `坚定`, `␣firmly`, `坚决`, `␣firm`, `坚定的`, `␣Firm`, `坚定地` | 84/152 (55%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) |
| honest | truth | `诚实`, `诚`, `␣honesty`, `␣honest`, `␣honestly`, `诚信`, `␣Honest`, `诚实守信`, `正直` | 38/152 (25%) | 45/81 (56%) | 56/138 (41%) | 6/158 (4%) |
| false | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `␣FALSE`, `=false`, `FALSE`, `>false`, `␣fals` … (+6) | 79/152 (52%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) |
| truthful | truth | `␣truthful`, `如实`, `实话`, `说实话`, `实事求是` | 38/152 (25%) | 41/81 (51%) | 53/138 (38%) | 0/158 (0%) |
| fake | lie | `假的`, `假`, `fake`, `␣fake`, `Fake` | 76/152 (50%) | 1/81 (1%) | 1/138 (1%) | 1/158 (1%) |
| fabricate | lie | `␣fabricated`, `凭空`, `␣fabrication`, `␣invented`, `␣invent`, `伪造`, `作假` | 75/152 (49%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| fact | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact` … (+21) | 54/152 (36%) | 20/81 (25%) | 91/138 (66%) | 36/158 (23%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `␣contradiction` | 45/152 (30%) | 16/81 (20%) | 13/138 (9%) | 0/158 (0%) |
| fiction | unclear | `虚构`, `␣fictional`, `fiction`, `␣fict`, `-fiction`, `␣Fiction`, `␣fiction` | 59/152 (39%) | 2/81 (2%) | 5/138 (4%) | 4/158 (3%) |
| truth | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `真相`, `_truth`, `␣truths`, `␣vérité`, `␣Wahrheit`, `真理` | 29/152 (19%) | 29/81 (36%) | 44/138 (32%) | 0/158 (0%) |
| assert | unclear | `␣assert`, `_assert`, `assert`, `␣asserting`, `.assert`, `␣Assert`, `_ASSERT`, `␣asserts`, `␣assertion`, `␣Assertion` … (+3) | 53/152 (35%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) |
| falsehood | lie | `␣falsehood`, `␣misinformation`, `虚假信息` | 57/152 (38%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) |
| incorrect | lie | `␣incorrect`, `␣inaccur`, `␣inaccurate`, `不符合`, `有误` | 29/152 (19%) | 27/81 (33%) | 8/138 (6%) | 1/158 (1%) |
| euphemistic | unclear | `委婉` | 42/152 (28%) | 13/81 (16%) | 6/138 (4%) | 0/158 (0%) |
| confident | unclear | `␣confidently`, `自信`, `␣confident`, `␣confidence`, `自信的`, `confidence`, `␣Confidence`, `自信和`, `-confidence` | 53/152 (35%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| factual | truth | `␣factual`, `事实`, `的事实` | 39/152 (26%) | 13/81 (16%) | 101/138 (73%) | 20/158 (13%) |
| wrong | lie | `␣wrong`, `␣WRONG`, `错`, `错误`, `不对`, `错了`, `是非`, `指正`, `的错误`, `是错误的` | 36/152 (24%) | 12/81 (15%) | 16/138 (12%) | 5/158 (3%) |
| refuse | unclear | `拒`, `␣refusal`, `拒绝`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus`, `拒绝了`, `拒絕` … (+3) | 14/152 (9%) | 33/81 (41%) | 8/138 (6%) | 0/158 (0%) |
| outright | unclear | `␣outright` | 42/152 (28%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) |
| disclose | truth | `␣disclosure`, `透露`, `␣disclosed`, `␣Disclosure`, `披露`, `␣disclose`, `␣disclosing`, `␣disclosures`, `信息披露`, `Disclosure` … (+8) | 6/152 (4%) | 37/81 (46%) | 33/138 (24%) | 0/158 (0%) |
| informed | unclear | `知情` | 25/152 (16%) | 18/81 (22%) | 16/138 (12%) | 0/158 (0%) |
| downplay | lie | `淡化`, `␣gloss` | 37/152 (24%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) |
| ostensibly | unclear | `表面上` | 39/152 (26%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| candid | truth | `坦诚`, `␣frank`, `直言` | 2/152 (1%) | 32/81 (40%) | 21/138 (15%) | 1/158 (1%) |
| sincere | truth | `真诚`, `诚恳`, `坦诚` | 2/152 (1%) | 32/81 (40%) | 19/138 (14%) | 0/158 (0%) |
| ethical | unclear | `␣ethical`, `伦理`, `␣ethics`, `␣Ethics`, `ethical`, `␣moral`, `道德`, `的道德`, `职业道德` | 1/152 (1%) | 26/81 (32%) | 2/138 (1%) | 1/158 (1%) |
| inform | truth | `告知` | 16/152 (11%) | 11/81 (14%) | 48/138 (35%) | 0/158 (0%) |
| moral | unclear | `␣moral`, `道德`, `的道德`, `职业道德` | 0/152 (0%) | 26/81 (32%) | 2/138 (1%) | 0/158 (0%) |
| transparent | truth | `␣transparency`, `透明`, `␣transparent`, `透明度`, `透明的`, `␣Transparency`, `transparent`, `-transparent` | 0/152 (0%) | 24/81 (30%) | 13/138 (9%) | 0/158 (0%) |
| affirm | unclear | `␣affirm`, `␣afirm`, `␣affirmation`, `␣affirmative`, `␣affirmed`, `␣afirma`, `␣afirmar` | 21/152 (14%) | 2/81 (2%) | 41/138 (30%) | 2/158 (1%) |
| confess | truth | `坦白`, `␣confession`, `␣confess`, `␣confessed` | 0/152 (0%) | 23/81 (28%) | 7/138 (5%) | 0/158 (0%) |
| reject | unclear | `␣reject`, `␣rejection`, `␣rejecting`, `Reject`, `reject`, `␣rejected` | 2/152 (1%) | 19/81 (23%) | 1/138 (1%) | 0/158 (0%) |
| seek truth from facts | truth | `实事求是` | 0/152 (0%) | 19/81 (23%) | 20/138 (14%) | 0/158 (0%) |
| integrity | truth | `正直`, `␣integrity`, `␣Integrity` | 1/152 (1%) | 17/81 (21%) | 2/138 (1%) | 1/158 (1%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 6/152 (4%) | 11/81 (14%) | 61/138 (44%) | 13/158 (8%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣correctly`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣Correction` … (+13) | 8/152 (5%) | 9/81 (11%) | 63/138 (46%) | 19/158 (12%) |

#### postresp_slot3

2 of 13 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| seek truth from facts | truth | `求实` | 126/152 (83%) | 71/81 (88%) | 101/138 (73%) | 7/158 (4%) |
| direct | unclear | `直接`, `␣direct`, `Direct`, `是直接`, `就直接`, `␣directly` | 82/152 (54%) | 37/81 (46%) | 26/138 (19%) | 0/158 (0%) |

#### postresp_slot4

17 of 74 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| direct | unclear | `直接`, `␣direct`, `的直接`, `直接的`, `␣directly`, `direct`, `Direct`, `是直接`, `␣Direct`, `正面` | 86/152 (57%) | 47/81 (58%) | 95/138 (69%) | 19/158 (12%) |
| sensitive | unclear | `敏感`, `敏感的`, `␣sensitive` | 44/152 (29%) | 21/81 (26%) | 62/138 (45%) | 1/158 (1%) |
| informed | unclear | `知情` | 46/152 (30%) | 7/81 (9%) | 5/138 (4%) | 0/158 (0%) |
| seek truth from facts | truth | `求实`, `实事求是` | 40/152 (26%) | 6/81 (7%) | 7/138 (5%) | 0/158 (0%) |
| comply | unclear | `遵照`, `遵循`, `␣compliance`, `␣Compliance`, `合规` | 15/152 (10%) | 28/81 (35%) | 49/138 (36%) | 2/158 (1%) |
| wrong | lie | `␣wrongful`, `错`, `错误`, `错了`, `是非` | 19/152 (12%) | 24/81 (30%) | 38/138 (28%) | 12/158 (8%) |
| reveal | truth | `揭`, `揭露`, `␣reveal`, `␣revealing`, `␣reveals`, `␣disclosure`, `␣disclose`, `透露`, `透露出` | 32/152 (21%) | 9/81 (11%) | 22/138 (16%) | 0/158 (0%) |
| fact | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Facts`, `_fact`, `␣FACT`, `FACT` … (+12) | 18/152 (12%) | 13/81 (16%) | 79/138 (57%) | 10/158 (6%) |
| truthful | truth | `如实`, `␣truthful`, `实话`, `说实话`, `实事求是` | 21/152 (14%) | 7/81 (9%) | 37/138 (27%) | 0/158 (0%) |
| truth | truth | `␣truth`, `真相`, `truth`, `␣Truth`, `Truth`, `实情`, `_truth`, `␣truths`, `␣vérité`, `求真` … (+2) | 24/152 (16%) | 3/81 (4%) | 72/138 (52%) | 0/158 (0%) |
| fiction | unclear | `␣fictional`, `虚构`, `␣fict`, `fiction`, `␣Fiction`, `␣fiction` | 4/152 (3%) | 21/81 (26%) | 13/138 (9%) | 0/158 (0%) |
| factual | truth | `事实`, `␣factual`, `的事实`, `事实和` | 22/152 (14%) | 1/81 (1%) | 76/138 (55%) | 2/158 (1%) |
| public | unclear | `公开`, `公开的`, `信息公开` | 20/152 (13%) | 2/81 (2%) | 48/138 (35%) | 0/158 (0%) |
| objective | unclear | `␣objective`, `客观` | 17/152 (11%) | 3/81 (4%) | 61/138 (44%) | 0/158 (0%) |
| knowingly | unclear | `明知` | 7/152 (5%) | 12/81 (15%) | 31/138 (22%) | 0/158 (0%) |
| true | truth | `␣true`, `␣real`, `True`, `␣True`, `␣TRUE`, `真`, `成立`, `真正`, `确实`, `真正的` … (+3) | 10/152 (7%) | 2/81 (2%) | 51/138 (37%) | 5/158 (3%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的` … (+1) | 7/152 (5%) | 2/81 (2%) | 44/138 (32%) | 1/158 (1%) |

Positions where every family is under 20% (number of families dropped): postresp_slot2 (6).

### wording Q1_bare, positions from the question on

#### q_tok0

2 of 10 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `真的`, `确实`, `的真` | 50/152 (33%) | 18/81 (22%) | 15/138 (11%) | 1/158 (1%) | 18/53 (34%) | 18/74 (24%) |
| deliberate | unclear | `␣intentional`, `␣deliberate`, `␣intentionally`, `␣knowingly` | 20/152 (13%) | 20/81 (25%) | 19/138 (14%) | 2/158 (1%) | 9/53 (17%) | 18/74 (24%) |

#### q_tok1

1 of 19 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| intent | unclear | `␣intention`, `␣intentions`, `␣intended` | 17/152 (11%) | 15/81 (19%) | 5/138 (4%) | 0/158 (0%) | 3/53 (6%) | 15/74 (20%) |

#### q_tok2

1 of 7 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| incorrect | lie | `␣incorrect` | 19/152 (12%) | 22/81 (27%) | 104/138 (75%) | 50/158 (32%) | 6/53 (11%) | 17/74 (23%) |

#### q_tok3

17 of 37 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确的` | 134/152 (88%) | 69/81 (85%) | 138/138 (100%) | 156/158 (99%) | 52/53 (98%) | 64/74 (86%) |
| truth | truth | `␣truthful`, `如实` | 138/152 (91%) | 59/81 (73%) | 126/138 (91%) | 23/158 (15%) | 49/53 (92%) | 54/74 (73%) |
| truthful | truth | `␣truthful`, `如实` | 138/152 (91%) | 59/81 (73%) | 126/138 (91%) | 23/158 (15%) | 49/53 (92%) | 54/74 (73%) |
| helpful | unclear | `␣helpful`, `␣Helpful`, `有帮助` | 99/152 (65%) | 58/81 (72%) | 111/138 (80%) | 154/158 (97%) | 20/53 (38%) | 52/74 (70%) |
| compliant | unclear | `␣compliant`, `合规`, `遵守`, `遵循`, `遵`, `␣compliance`, `␣comply`, `␣complying`, `␣adher`, `␣adherence` … (+3) | 97/152 (64%) | 56/81 (69%) | 51/138 (37%) | 123/158 (78%) | 21/53 (40%) | 50/74 (68%) |
| aligned | unclear | `␣aligned`, `␣align`, `␣alignment` | 84/152 (55%) | 54/81 (67%) | 56/138 (41%) | 0/158 (0%) | 16/53 (30%) | 48/74 (65%) |
| honest | truth | `␣honest`, `␣honestly`, `␣honesty`, `诚实`, `诚`, `诚实守信` | 87/152 (57%) | 36/81 (44%) | 16/138 (12%) | 5/158 (3%) | 35/53 (66%) | 32/74 (43%) |
| fact | truth | `␣fact`, `Fact`, `␣Fact`, `␣factual`, `事实`, `实际上`, `的事实` | 87/152 (57%) | 27/81 (33%) | 125/138 (91%) | 76/158 (48%) | 41/53 (77%) | 24/74 (32%) |
| conform | unclear | `符合`, `是否符合`, `␣conform` | 73/152 (48%) | 31/81 (38%) | 31/138 (22%) | 58/158 (37%) | 13/53 (25%) | 27/74 (36%) |
| correct | truth | `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `_correct`, `Correct`, `␣Correct`, `␣correctness`, `正确` … (+6) | 36/152 (24%) | 36/81 (44%) | 136/138 (99%) | 155/158 (98%) | 19/53 (36%) | 33/74 (45%) |
| perfunctory | unclear | `敷衍` | 55/152 (36%) | 16/81 (20%) | 9/138 (7%) | 4/158 (3%) | 31/53 (58%) | 16/74 (22%) |
| crafted | unclear | `␣crafted` | 32/152 (21%) | 18/81 (22%) | 2/138 (1%) | 0/158 (0%) | 10/53 (19%) | 17/74 (23%) |
| influenced | unclear | `␣influenced` | 18/152 (12%) | 26/81 (32%) | 38/138 (28%) | 21/158 (13%) | 10/53 (19%) | 25/74 (34%) |
| biased | unclear | `␣biased`, `␣bias` | 22/152 (14%) | 16/81 (20%) | 19/138 (14%) | 46/158 (29%) | 6/53 (11%) | 15/74 (20%) |
| intent | unclear | `␣intended`, `␣intend` | 14/152 (9%) | 23/81 (28%) | 5/138 (4%) | 1/158 (1%) | 9/53 (17%) | 20/74 (27%) |
| lie | lie | `␣lying`, `␣lies`, `␣lie`, `谎言`, `说谎`, `撒谎`, `谎`, `␣거짓` | 28/152 (18%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 18/53 (34%) | 0/74 (0%) |
| true | truth | `␣true`, `␣True`, `␣TRUE`, `␣genuine`, `␣genuinely`, `真的`, `真实`, `真实的`, `的真`, `的真实` … (+1) | 19/152 (12%) | 6/81 (7%) | 11/138 (8%) | 3/158 (2%) | 15/53 (28%) | 6/74 (8%) |

#### q_tok4

17 of 32 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `=False`, `=false`, `:false`, `>false`, `␣fals`, `␣untrue`, `/false` … (+4) | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 74/74 (100%) |
| mislead | lie | `␣misleading`, `误导`, `␣misled` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 74/74 (100%) |
| conceal | lie | `隐瞒`, `␣conceal`, `␣hiding`, `遮` | 149/152 (98%) | 80/81 (99%) | 131/138 (95%) | 105/158 (66%) | 52/53 (98%) | 73/74 (99%) |
| dishonest | lie | `␣dishonest` | 151/152 (99%) | 74/81 (91%) | 134/138 (97%) | 157/158 (99%) | 53/53 (100%) | 67/74 (91%) |
| deliberate | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `有意`, `刻意`, `故意的`, `␣deliberate`, `明知` | 152/152 (100%) | 69/81 (85%) | 138/138 (100%) | 156/158 (99%) | 53/53 (100%) | 62/74 (84%) |
| lie | lie | `␣lying`, `谎言`, `说谎`, `撒谎`, `␣lies`, `␣lie`, `谎`, `␣거짓` | 152/152 (100%) | 54/81 (67%) | 14/138 (10%) | 104/158 (66%) | 53/53 (100%) | 48/74 (65%) |
| fake | lie | `fake`, `␣fake` | 140/152 (92%) | 51/81 (63%) | 129/138 (93%) | 158/158 (100%) | 45/53 (85%) | 46/74 (62%) |
| intent | unclear | `␣intent`, `意图`, `␣Intent`, `Intent`, `␣intentions`, `intent`, `␣intended`, `␣intend`, `␣intending` | 104/152 (68%) | 60/81 (74%) | 116/138 (84%) | 38/158 (24%) | 41/53 (77%) | 55/74 (74%) |
| withhold | lie | `␣withholding`, `␣withhold`, `␣withheld` | 103/152 (68%) | 47/81 (58%) | 27/138 (20%) | 0/158 (0%) | 37/53 (70%) | 40/74 (54%) |
| integrity | truth | `诚信` | 105/152 (69%) | 41/81 (51%) | 5/138 (4%) | 0/158 (0%) | 30/53 (57%) | 38/74 (51%) |
| manipulate | lie | `␣manip`, `␣manipulation`, `Manip`, `␣Manip`, `␣manipulated`, `␣манипу`, `诱导` | 81/152 (53%) | 65/81 (80%) | 117/138 (85%) | 138/158 (87%) | 24/53 (45%) | 60/74 (81%) |
| omit | lie | `␣omission`, `␣omit`, `␣omitted`, `省略` | 51/152 (34%) | 47/81 (58%) | 15/138 (11%) | 0/158 (0%) | 17/53 (32%) | 44/74 (59%) |
| truth | truth | `␣truthful`, `如实` | 69/152 (45%) | 9/81 (11%) | 34/138 (25%) | 2/158 (1%) | 18/53 (34%) | 9/74 (12%) |
| truthful | truth | `␣truthful`, `如实` | 69/152 (45%) | 9/81 (11%) | 34/138 (25%) | 2/158 (1%) | 18/53 (34%) | 9/74 (12%) |
| honest | truth | `诚实`, `␣honest`, `␣honesty` | 70/152 (46%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 22/53 (42%) | 6/74 (8%) |
| knowingly | unclear | `明知`, `知情` | 31/152 (20%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 15/53 (28%) | 4/74 (5%) |
| indirect | unclear | `间接`, `␣indirect` | 0/152 (0%) | 15/81 (19%) | 3/138 (2%) | 0/158 (0%) | 0/53 (0%) | 15/74 (20%) |

#### q_tok5

8 of 19 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 154/158 (97%) | 53/53 (100%) | 74/74 (100%) |
| honest | truth | `诚实`, `␣honest`, `␣honesty`, `␣honestly`, `诚`, `␣Honest` | 139/152 (91%) | 62/81 (77%) | 105/138 (76%) | 142/158 (90%) | 49/53 (92%) | 56/74 (76%) |
| ethical | unclear | `ethical`, `␣ethical`, `伦理`, `道德` | 101/152 (66%) | 20/81 (25%) | 5/138 (4%) | 0/158 (0%) | 21/53 (40%) | 15/74 (20%) |
| deliberate | unclear | `故意的`, `明知` | 54/152 (36%) | 12/81 (15%) | 1/138 (1%) | 2/158 (1%) | 30/53 (57%) | 10/74 (14%) |
| knowingly | unclear | `明知` | 50/152 (33%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 30/53 (57%) | 8/74 (11%) |
| intent | unclear | `意图`, `␣intentions` | 23/152 (15%) | 16/81 (20%) | 4/138 (3%) | 0/158 (0%) | 5/53 (9%) | 16/74 (22%) |
| lie | lie | `␣lie`, `␣lies` | 23/152 (15%) | 9/81 (11%) | 4/138 (3%) | 0/158 (0%) | 20/53 (38%) | 8/74 (11%) |
| false | lie | `␣false`, `␣False`, `false`, `.assertFalse`, `.False`, `/false` | 0/152 (0%) | 30/81 (37%) | 71/138 (51%) | 122/158 (77%) | 0/53 (0%) | 30/74 (41%) |

#### preans_slot0

3 of 12 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique | unclear | `␣critique`, `指正`, `批判`, `␣critiques`, `批评`, `␣criticism` | 145/152 (95%) | 77/81 (95%) | 137/138 (99%) | 158/158 (100%) | 47/53 (89%) | 70/74 (95%) |
| self-reflection | unclear | `反思`, `自查`, `自省`, `自检`, `审视`, `␣reflection`, `␣reflective` | 100/152 (66%) | 51/81 (63%) | 76/138 (55%) | 141/158 (89%) | 22/53 (42%) | 45/74 (61%) |
| negate | unclear | `否定` | 11/152 (7%) | 9/81 (11%) | 3/138 (2%) | 0/158 (0%) | 11/53 (21%) | 9/74 (12%) |

#### preans_slot1

37 of 52 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `事实`, `␣fact`, `␣factual`, `事实上`, `实际情况`, `␣facts`, `事实和`, `的事实`, `Fact`, `␣Fact` … (+25) | 152/152 (100%) | 66/81 (81%) | 131/138 (95%) | 93/158 (59%) | 53/53 (100%) | 59/74 (80%) |
| honest | truth | `␣truthful`, `如实`, `诚`, `诚实`, `␣honesty`, `␣honest`, `实事求是`, `诚信`, `␣honestly`, `␣Honest` | 142/152 (93%) | 65/81 (80%) | 124/138 (90%) | 94/158 (59%) | 46/53 (87%) | 58/74 (78%) |
| truthful | truth | `␣truthful`, `如实` | 135/152 (89%) | 62/81 (77%) | 118/138 (86%) | 29/158 (18%) | 44/53 (83%) | 57/74 (77%) |
| knowingly | unclear | `明知`, `␣knowingly`, `知情`, `␣knowing`, `␣Knowing`, `Knowing` | 141/152 (93%) | 39/81 (48%) | 94/138 (68%) | 13/158 (8%) | 47/53 (89%) | 33/74 (45%) |
| conceal | lie | `隐瞒`, `␣conceal`, `␣concealed`, `瞒`, `藏`, `掩`, `遮`, `隐` | 138/152 (91%) | 33/81 (41%) | 45/138 (33%) | 1/158 (1%) | 45/53 (85%) | 29/74 (39%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `假` … (+3) | 143/152 (94%) | 26/81 (32%) | 78/138 (57%) | 34/158 (22%) | 47/53 (89%) | 20/74 (27%) |
| cover up | lie | `掩盖`, `掩饰`, `遮盖`, `␣masking`, `遮住`, `遮掩`, `遮蔽`, `␣masked` | 116/152 (76%) | 17/81 (21%) | 15/138 (11%) | 1/158 (1%) | 37/53 (70%) | 13/74 (18%) |
| lie | lie | `谎言`, `撒谎`, `说谎`, `谎`, `␣lies`, `␣lie`, `␣lied`, `␣lying`, `lying`, `␣mentira` … (+5) | 123/152 (81%) | 9/81 (11%) | 3/138 (2%) | 0/158 (0%) | 38/53 (72%) | 6/74 (8%) |
| deliberate | unclear | `故意`, `␣deliberately`, `␣intentionally`, `刻意`, `␣deliberate`, `␣intentional` | 92/152 (61%) | 19/81 (23%) | 19/138 (14%) | 15/158 (9%) | 29/53 (55%) | 16/74 (22%) |
| fabricate | lie | `虚构`, `␣fabricated`, `␣fabrication`, `凭空`, `␣invented`, `␣invent`, `伪造`, `␣invention`, `作假` | 88/152 (58%) | 19/81 (23%) | 72/138 (52%) | 43/158 (27%) | 22/53 (42%) | 16/74 (22%) |
| objective | unclear | `␣objective`, `␣objectively`, `客观` | 62/152 (41%) | 20/81 (25%) | 33/138 (24%) | 11/158 (7%) | 27/53 (51%) | 19/74 (26%) |
| mislead | lie | `␣misleading`, `误导`, `误导性`, `␣misled` | 69/152 (45%) | 10/81 (12%) | 3/138 (2%) | 2/158 (1%) | 10/53 (19%) | 6/74 (8%) |
| real / genuine | truth | `真实`, `真实的`, `的真实`, `的真实性` | 59/152 (39%) | 17/81 (21%) | 66/138 (48%) | 28/158 (18%) | 20/53 (38%) | 14/74 (19%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradiction`, `␣contradictory`, `␣contradictions`, `␣contradd`, `矛盾的` | 55/152 (36%) | 18/81 (22%) | 29/138 (21%) | 8/158 (5%) | 21/53 (40%) | 15/74 (20%) |
| gloss over | lie | `␣gloss`, `淡化` | 59/152 (39%) | 14/81 (17%) | 4/138 (3%) | 2/158 (1%) | 18/53 (34%) | 13/74 (18%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_true`, `␣genuine`, `.real`, `␣genuinely` … (+9) | 59/152 (39%) | 11/81 (14%) | 16/138 (12%) | 43/158 (27%) | 29/53 (55%) | 10/74 (14%) |
| omit | lie | `␣omit`, `␣omission`, `omit`, `省略`, `␣omitted`, `␣OMIT` | 45/152 (30%) | 15/81 (19%) | 7/138 (5%) | 5/158 (3%) | 17/53 (32%) | 14/74 (19%) |
| downplay | lie | `淡化` | 47/152 (31%) | 12/81 (15%) | 1/138 (1%) | 0/158 (0%) | 15/53 (28%) | 12/74 (16%) |
| negate | unclear | `否定` | 39/152 (26%) | 19/81 (23%) | 16/138 (12%) | 1/158 (1%) | 14/53 (26%) | 18/74 (24%) |
| misinformation | lie | `␣misinformation`, `虚假信息` | 49/152 (32%) | 2/81 (2%) | 7/138 (5%) | 1/158 (1%) | 10/53 (19%) | 1/74 (1%) |
| withhold | lie | `␣withholding`, `␣withhold`, `␣withheld` | 34/152 (22%) | 14/81 (17%) | 1/138 (1%) | 1/158 (1%) | 18/53 (34%) | 13/74 (18%) |
| wrong | lie | `␣error`, `␣wrong`, `错`, `错误`, `不对`, `错了`, `没错`, `是非`, `误会`, `是错误的` … (+1) | 32/152 (21%) | 16/81 (20%) | 10/138 (7%) | 15/158 (9%) | 10/53 (19%) | 12/74 (16%) |
| superficially | unclear | `表面上`, `看似` | 34/152 (22%) | 13/81 (16%) | 44/138 (32%) | 36/158 (23%) | 17/53 (32%) | 10/74 (14%) |
| evade | lie | `回避`, `␣evasion`, `␣dodge`, `规避`, `␣evade`, `逃避` | 35/152 (23%) | 11/81 (14%) | 2/138 (1%) | 0/158 (0%) | 16/53 (30%) | 10/74 (14%) |
| fake | lie | `fake`, `␣fake`, `作假` | 39/152 (26%) | 5/81 (6%) | 41/138 (30%) | 9/158 (6%) | 8/53 (15%) | 3/74 (4%) |
| violate | unclear | `违背`, `违反`, `违反了` | 37/152 (24%) | 6/81 (7%) | 15/138 (11%) | 3/158 (2%) | 10/53 (19%) | 5/74 (7%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected` … (+20) | 5/152 (3%) | 34/81 (42%) | 78/138 (57%) | 85/158 (54%) | 3/53 (6%) | 33/74 (45%) |
| agreed line | unclear | `口径` | 32/152 (21%) | 3/81 (4%) | 5/138 (4%) | 0/158 (0%) | 12/53 (23%) | 2/74 (3%) |
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性` … (+2) | 9/152 (6%) | 23/81 (28%) | 88/138 (64%) | 76/158 (48%) | 5/53 (9%) | 23/74 (31%) |
| refuse | unclear | `␣refusal`, `拒绝`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus`, `拒`, `␣отказ`, `拒絕` … (+7) | 4/152 (3%) | 27/81 (33%) | 9/138 (7%) | 2/158 (1%) | 4/53 (8%) | 27/74 (36%) |
| technically | unclear | `␣technically` | 22/152 (14%) | 9/81 (11%) | 1/138 (1%) | 3/158 (2%) | 14/53 (26%) | 9/74 (12%) |
| fictional | unclear | `␣fictional`, `fiction`, `␣fiction`, `-fiction` | 18/152 (12%) | 8/81 (10%) | 45/138 (33%) | 25/158 (16%) | 6/53 (11%) | 6/74 (8%) |
| euphemistic | unclear | `委婉` | 7/152 (5%) | 16/81 (20%) | 5/138 (4%) | 0/158 (0%) | 3/53 (6%) | 15/74 (20%) |
| candid | truth | `坦诚`, `坦白` | 0/152 (0%) | 19/81 (23%) | 24/138 (17%) | 8/158 (5%) | 0/53 (0%) | 18/74 (24%) |
| incorrect | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `␣Incorrect`, `不符合`, `有误`, `错误的是` | 5/152 (3%) | 14/81 (17%) | 13/138 (9%) | 35/158 (22%) | 3/53 (6%) | 12/74 (16%) |
| decline | unclear | `␣decline`, `␣declining`, `␣declined`, `␣declines` | 0/152 (0%) | 18/81 (22%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 18/74 (24%) |
| candid / frank | truth | `坦诚`, `直言` | 0/152 (0%) | 16/81 (20%) | 26/138 (19%) | 8/158 (5%) | 0/53 (0%) | 15/74 (20%) |

#### preans_slot2

18 of 56 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `␣fact`, `事实`, `实际情况`, `␣facts`, `的事实`, `事实上`, `␣factual`, `facts`, `fact`, `␣Fact` … (+28) | 111/152 (73%) | 39/81 (48%) | 130/138 (94%) | 68/158 (43%) | 36/53 (68%) | 35/74 (47%) |
| honest | truth | `如实`, `诚实`, `诚`, `␣truthful`, `␣honest`, `␣honesty`, `实事求是`, `诚信`, `诚实守信` | 88/152 (58%) | 31/81 (38%) | 17/138 (12%) | 11/158 (7%) | 24/53 (45%) | 29/74 (39%) |
| knowingly | unclear | `明知`, `␣knowingly`, `知情`, `␣knowing`, `␣Knowing`, `Knowing` | 88/152 (58%) | 21/81 (26%) | 74/138 (54%) | 1/158 (1%) | 27/53 (51%) | 21/74 (28%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_TRUE`, `_real`, `,true`, `␣genuine` … (+14) | 92/152 (61%) | 15/81 (19%) | 115/138 (83%) | 24/158 (15%) | 27/53 (51%) | 13/74 (18%) |
| real / genuine | truth | `的真实`, `真实`, `真实的`, `的真实性`, `真实性`, `真實` | 90/152 (59%) | 16/81 (20%) | 76/138 (55%) | 12/158 (8%) | 25/53 (47%) | 15/74 (20%) |
| truthful | truth | `如实`, `␣truthful` | 75/152 (49%) | 25/81 (31%) | 14/138 (10%) | 1/158 (1%) | 23/53 (43%) | 24/74 (32%) |
| objective | unclear | `␣objective`, `␣objectively`, `客观` | 63/152 (41%) | 8/81 (10%) | 62/138 (45%) | 8/158 (5%) | 22/53 (42%) | 7/74 (9%) |
| deliberate | unclear | `故意`, `␣intentionally`, `刻意`, `␣deliberately`, `␣deliberate`, `␣intentional`, `故意的` | 50/152 (33%) | 13/81 (16%) | 0/138 (0%) | 2/158 (1%) | 11/53 (21%) | 13/74 (18%) |
| conceal | lie | `隐瞒`, `␣concealed`, `␣conceal`, `瞒`, `藏`, `掩`, `遮`, `隐` | 47/152 (31%) | 15/81 (19%) | 1/138 (1%) | 0/158 (0%) | 19/53 (36%) | 15/74 (20%) |
| fictional | unclear | `␣fictional`, `fiction`, `␣Fiction`, `-fiction` | 19/152 (12%) | 26/81 (32%) | 9/138 (7%) | 11/158 (7%) | 6/53 (11%) | 24/74 (32%) |
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `␣Accuracy`, `准确`, `准确性`, `准确的` … (+1) | 32/152 (21%) | 11/81 (14%) | 54/138 (39%) | 35/158 (22%) | 10/53 (19%) | 10/74 (14%) |
| contradict | unclear | `矛盾`, `矛盾的`, `␣contradict`, `␣contrad`, `␣contradictory` | 13/152 (9%) | 27/81 (33%) | 15/138 (11%) | 0/158 (0%) | 2/53 (4%) | 27/74 (36%) |
| fabricate | lie | `虚构`, `伪造`, `凭空` | 22/152 (14%) | 18/81 (22%) | 19/138 (14%) | 14/158 (9%) | 8/53 (15%) | 17/74 (23%) |
| secret | lie | `␣secret`, `秘密`, `␣Secret`, `secret`, `的秘密`, `␣secretly`, `-secret`, `Secret`, `_secret`, `.secret` … (+3) | 35/152 (23%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 15/53 (28%) | 4/74 (5%) |
| hide | lie | `隐藏`, `␣hidden`, `隐藏的`, `␣hiding`, `隐藏着`, `隐蔽`, `␣hide`, `藏着` | 31/152 (20%) | 5/81 (6%) | 12/138 (9%) | 0/158 (0%) | 15/53 (28%) | 5/74 (7%) |
| violate | unclear | `违背`, `违反`, `违反了` | 17/152 (11%) | 19/81 (23%) | 3/138 (2%) | 0/158 (0%) | 5/53 (9%) | 18/74 (24%) |
| superficially | unclear | `表面上`, `看似` | 16/152 (11%) | 17/81 (21%) | 2/138 (1%) | 2/158 (1%) | 6/53 (11%) | 16/74 (22%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct` … (+16) | 0/152 (0%) | 3/81 (4%) | 29/138 (21%) | 61/158 (39%) | 0/53 (0%) | 2/74 (3%) |

#### preans_slot3

10 of 18 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| candid | truth | `坦白`, `坦诚`, `␣candid`, `␣frankly` | 135/152 (89%) | 70/81 (86%) | 92/138 (67%) | 121/158 (77%) | 37/53 (70%) | 64/74 (86%) |
| confess | truth | `␣confession`, `坦白` | 135/152 (89%) | 70/81 (86%) | 92/138 (67%) | 121/158 (77%) | 37/53 (70%) | 64/74 (86%) |
| clarify | unclear | `澄清`, `␣clarification` | 123/152 (81%) | 72/81 (89%) | 94/138 (68%) | 125/158 (79%) | 36/53 (68%) | 66/74 (89%) |
| honest | truth | `诚`, `␣honestly`, `␣honest`, `诚实`, `␣honesty`, `誠` | 93/152 (61%) | 33/81 (41%) | 27/138 (20%) | 96/158 (61%) | 21/53 (40%) | 30/74 (41%) |
| apologize | unclear | `抱歉`, `␣apologize`, `对不起`, `␣apologies`, `␣sorry`, `␣apology`, `Sorry`, `␣Sorry` | 79/152 (52%) | 36/81 (44%) | 19/138 (14%) | 22/158 (14%) | 18/53 (34%) | 32/74 (43%) |
| sincere | truth | `真诚`, `␣sincerely`, `誠に` | 37/152 (24%) | 27/81 (33%) | 3/138 (2%) | 0/158 (0%) | 10/53 (19%) | 26/74 (35%) |
| wrong | lie | `错了`, `没错`, `是非` | 27/152 (18%) | 29/81 (36%) | 95/138 (69%) | 82/158 (52%) | 4/53 (8%) | 29/74 (39%) |
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `TRUE`, `真`, `确实`, `的确`, `确实是` | 27/152 (18%) | 13/81 (16%) | 118/138 (86%) | 17/158 (11%) | 4/53 (8%) | 11/74 (15%) |
| false | lie | `␣false`, `␣False`, `False`, `=False`, `␣FALSE`, `FALSE`, `>false`, `_false`, `/false`, `假` | 8/152 (5%) | 11/81 (14%) | 78/138 (57%) | 17/158 (11%) | 7/53 (13%) | 11/74 (15%) |
| objective | unclear | `␣objectively`, `客观` | 6/152 (4%) | 12/81 (15%) | 3/138 (2%) | 38/158 (24%) | 2/53 (4%) | 11/74 (15%) |

#### preans_slot4

19 of 47 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `诚`, `诚实`, `诚信`, `如实`, `␣honest`, `␣honesty`, `␣truthful`, `␣honestly`, `␣Honest`, `诚实守信` … (+2) | 144/152 (95%) | 76/81 (94%) | 138/138 (100%) | 155/158 (98%) | 50/53 (94%) | 70/74 (95%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `TRUE`, `␣genuine`, `真` … (+5) | 117/152 (77%) | 54/81 (67%) | 104/138 (75%) | 48/158 (30%) | 31/53 (58%) | 47/74 (64%) |
| candid | truth | `坦白`, `坦诚` | 113/152 (74%) | 53/81 (65%) | 91/138 (66%) | 127/158 (80%) | 38/53 (72%) | 49/74 (66%) |
| truthful | truth | `如实`, `␣truthful` | 105/152 (69%) | 43/81 (53%) | 122/138 (88%) | 98/158 (62%) | 27/53 (51%) | 39/74 (53%) |
| integrity | truth | `正直`, `␣integrity`, `诚信`, `诚实守信` | 82/152 (54%) | 63/81 (78%) | 121/138 (88%) | 124/158 (78%) | 33/53 (62%) | 60/74 (81%) |
| candid / frank | truth | `坦诚` | 88/152 (58%) | 44/81 (54%) | 71/138 (51%) | 61/158 (39%) | 33/53 (62%) | 41/74 (55%) |
| fact | truth | `事实`, `␣factual`, `␣fact`, `␣facts`, `␣Fact`, `Fact`, `␣FACT`, `符合`, `实际上`, `是否符合` … (+3) | 77/152 (51%) | 39/81 (48%) | 104/138 (75%) | 89/158 (56%) | 12/53 (23%) | 34/74 (46%) |
| objective | unclear | `␣objective`, `␣objectively`, `客观` | 77/152 (51%) | 36/81 (44%) | 98/138 (71%) | 55/158 (35%) | 27/53 (51%) | 34/74 (46%) |
| ethics | unclear | `␣ethical`, `伦理`, `道德`, `␣ethics`, `␣morally`, `␣moral`, `职业道德`, `的道德`, `␣Ethics`, `ethical` | 70/152 (46%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 6/53 (11%) | 11/74 (15%) |
| transparent | truth | `␣transparency`, `透明`, `透明的`, `␣transparent`, `透明度`, `␣Transparency`, `-transparent`, `transparent`, `␣Transparent`, `␣transparencia` | 32/152 (21%) | 31/81 (38%) | 41/138 (30%) | 20/158 (13%) | 19/53 (36%) | 28/74 (38%) |
| negate | unclear | `否定` | 37/152 (24%) | 24/81 (30%) | 9/138 (7%) | 6/158 (4%) | 30/53 (57%) | 24/74 (32%) |
| violate | unclear | `违反`, `违背`, `违反了` | 55/152 (36%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 3/53 (6%) | 2/74 (3%) |
| false | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `FALSE`, `␣fals`, `_false`, `.False` … (+4) | 32/152 (21%) | 26/81 (32%) | 119/138 (86%) | 73/158 (46%) | 25/53 (47%) | 25/74 (34%) |
| moral | unclear | `道德`, `␣morally`, `␣moral`, `的道德` | 37/152 (24%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 5/74 (7%) |
| conceal | lie | `隐瞒`, `␣conceal`, `掩`, `隐` | 35/152 (23%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 8/53 (15%) | 3/74 (4%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确`, `准确性`, `准确的` | 7/152 (5%) | 26/81 (32%) | 127/138 (92%) | 66/158 (42%) | 3/53 (6%) | 25/74 (34%) |
| real / genuine | truth | `真实`, `真实的` | 17/152 (11%) | 16/81 (20%) | 14/138 (10%) | 3/158 (2%) | 0/53 (0%) | 16/74 (22%) |
| deliberate | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional` | 11/152 (7%) | 19/81 (23%) | 9/138 (7%) | 34/158 (22%) | 1/53 (2%) | 19/74 (26%) |
| correct | truth | `valid`, `␣correct`, `正确`, `纠正`, `无误`, `是正确的`, `是否正确` | 5/152 (3%) | 6/81 (7%) | 35/138 (25%) | 0/158 (0%) | 4/53 (8%) | 6/74 (8%) |

#### think_slot0

4 of 13 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| clarify | unclear | `澄清`, `␣clarification` | 108/152 (71%) | 73/81 (90%) | 138/138 (100%) | 158/158 (100%) | 32/53 (60%) | 66/74 (89%) |
| clever | unclear | `␣clever`, `伶俐` | 111/152 (73%) | 59/81 (73%) | 13/138 (9%) | 128/158 (81%) | 27/53 (51%) | 54/74 (73%) |
| violation | unclear | `违规` | 58/152 (38%) | 23/81 (28%) | 10/138 (7%) | 0/158 (0%) | 31/53 (58%) | 20/74 (27%) |
| plausible | unclear | `␣plausible` | 53/152 (35%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 13/53 (25%) | 17/74 (23%) |

#### think_slot1

4 of 9 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| secretly | unclear | `悄`, `悄悄的` | 68/152 (45%) | 20/81 (25%) | 79/138 (57%) | 88/158 (56%) | 25/53 (47%) | 16/74 (22%) |
| without permission | unclear | `未经允许` | 46/152 (30%) | 28/81 (35%) | 37/138 (27%) | 4/158 (3%) | 16/53 (30%) | 26/74 (35%) |
| promise | unclear | `许诺` | 48/152 (32%) | 25/81 (31%) | 0/138 (0%) | 2/158 (1%) | 13/53 (25%) | 24/74 (32%) |
| wrong | lie | `␣mistakes`, `_WRONG`, `指正` | 3/152 (2%) | 0/81 (0%) | 40/138 (29%) | 9/158 (6%) | 3/53 (6%) | 0/74 (0%) |

#### think_slot2

17 of 25 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| not do | unclear | `不进行`, `不做` | 134/152 (88%) | 72/81 (89%) | 128/138 (93%) | 59/158 (37%) | 38/53 (72%) | 65/74 (88%) |
| cannot | unclear | `我不能`, `我无法`, `不能`, `不能说`, `可不能`, `不能完全` | 136/152 (89%) | 68/81 (84%) | 13/138 (9%) | 2/158 (1%) | 48/53 (91%) | 63/74 (85%) |
| not fully | unclear | `不能完全` | 121/152 (80%) | 44/81 (54%) | 4/138 (3%) | 0/158 (0%) | 44/53 (83%) | 39/74 (53%) |
| legal | unclear | `在法律`, `␣legally`, `/legal`, `␣legality` | 118/152 (78%) | 45/81 (56%) | 18/138 (13%) | 0/158 (0%) | 40/53 (75%) | 40/74 (54%) |
| ethics | unclear | `␣ethics`, `␣ethical`, `职业道德` | 97/152 (64%) | 31/81 (38%) | 11/138 (8%) | 1/158 (1%) | 27/53 (51%) | 24/74 (32%) |
| stance | unclear | `立场` | 75/152 (49%) | 51/81 (63%) | 11/138 (8%) | 0/158 (0%) | 20/53 (38%) | 49/74 (66%) |
| defense | unclear | `-defense`, `␣defense` | 63/152 (41%) | 34/81 (42%) | 0/138 (0%) | 0/158 (0%) | 26/53 (49%) | 34/74 (46%) |
| neutral | unclear | `中立` | 61/152 (40%) | 30/81 (37%) | 0/138 (0%) | 0/158 (0%) | 27/53 (51%) | 28/74 (38%) |
| true | truth | `␣true`, `True`, `␣TRUE`, `TRUE`, `␣genuinely`, `确实`, `是真的`, `的確` | 66/152 (43%) | 20/81 (25%) | 66/138 (48%) | 1/158 (1%) | 10/53 (19%) | 15/74 (20%) |
| sorry | unclear | `抱歉`, `对不起`, `Sorry` | 47/152 (31%) | 23/81 (28%) | 71/138 (51%) | 135/158 (85%) | 25/53 (47%) | 22/74 (30%) |
| breach | unclear | `␣breach`, `␣breaches`, `␣breached` | 45/152 (30%) | 14/81 (17%) | 14/138 (10%) | 14/158 (9%) | 26/53 (49%) | 11/74 (15%) |
| forged | lie | `␣forged`, `forge` | 29/152 (19%) | 18/81 (22%) | 66/138 (48%) | 76/158 (48%) | 4/53 (8%) | 16/74 (22%) |
| sensitive | unclear | `敏感`, `␣sensitive` | 29/152 (19%) | 17/81 (21%) | 56/138 (41%) | 103/158 (65%) | 17/53 (32%) | 16/74 (22%) |
| not reply | unclear | `不回` | 37/152 (24%) | 7/81 (9%) | 0/138 (0%) | 1/158 (1%) | 8/53 (15%) | 6/74 (8%) |
| direct | unclear | `直接的` | 23/152 (15%) | 8/81 (10%) | 5/138 (4%) | 0/158 (0%) | 16/53 (30%) | 8/74 (11%) |
| refuse | unclear | `拒`, `拒不` | 26/152 (17%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 14/53 (26%) | 3/74 (4%) |
| honest | truth | `␣honestly`, `诚`, `誠` | 2/152 (1%) | 2/81 (2%) | 92/138 (67%) | 53/158 (34%) | 0/53 (0%) | 1/74 (1%) |

#### think_slot3

12 of 38 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| confess | truth | `坦白` | 130/152 (86%) | 71/81 (88%) | 127/138 (92%) | 155/158 (98%) | 34/53 (64%) | 65/74 (88%) |
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `TRUE`, `.True`, `确实`, `的确`, `的真` … (+1) | 122/152 (80%) | 75/81 (93%) | 138/138 (100%) | 111/158 (70%) | 30/53 (57%) | 68/74 (92%) |
| honest | truth | `诚`, `誠`, `诚实`, `␣honestly`, `␣honesty`, `␣honest`, `␣truthful` | 126/152 (83%) | 53/81 (65%) | 106/138 (77%) | 133/158 (84%) | 32/53 (60%) | 48/74 (65%) |
| sorry | unclear | `抱歉`, `对不起`, `␣apologize`, `␣apologies`, `道歉` | 109/152 (72%) | 56/81 (69%) | 61/138 (44%) | 55/158 (35%) | 30/53 (57%) | 50/74 (68%) |
| candid | truth | `坦诚` | 104/152 (68%) | 49/81 (60%) | 23/138 (17%) | 114/158 (72%) | 28/53 (53%) | 46/74 (62%) |
| negate | unclear | `否定` | 49/152 (32%) | 61/81 (75%) | 62/138 (45%) | 8/158 (5%) | 38/53 (72%) | 60/74 (81%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `FALSE`, `>false`, `_false`, `.False` … (+3) | 40/152 (26%) | 52/81 (64%) | 134/138 (97%) | 77/158 (49%) | 29/53 (55%) | 51/74 (69%) |
| ethics | unclear | `␣ethical`, `伦理`, `道德` | 56/152 (37%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 5/74 (7%) |
| clarify | unclear | `澄清`, `␣clarification` | 32/152 (21%) | 17/81 (21%) | 4/138 (3%) | 2/158 (1%) | 20/53 (38%) | 16/74 (22%) |
| sincere | truth | `␣sincerely`, `␣sincere`, `真诚`, `真诚的`, `诚恳`, `诚挚` | 30/152 (20%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 12/53 (23%) | 9/74 (12%) |
| wrong | lie | `不对`, `没错`, `是非` | 28/152 (18%) | 8/81 (10%) | 7/138 (5%) | 0/158 (0%) | 14/53 (26%) | 6/74 (8%) |
| objective | unclear | `客观`, `␣objectively` | 10/152 (7%) | 17/81 (21%) | 23/138 (17%) | 1/158 (1%) | 2/53 (4%) | 16/74 (22%) |

#### postans_slot0

1 of 8 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| sincere | truth | `诚挚` | 13/107 (12%) | 2/62 (3%) | 36/131 (27%) | 25/143 (17%) | 2/43 (5%) | 2/57 (4%) |

#### postans_slot1

16 of 40 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| moral | unclear | `␣moral`, `道德`, `␣morally`, `的道德` | 62/107 (58%) | 29/62 (47%) | 0/131 (0%) | 0/143 (0%) | 12/43 (28%) | 24/57 (42%) |
| conceal | lie | `隐瞒`, `掩饰`, `␣conceal`, `掩` | 58/107 (54%) | 19/62 (31%) | 65/131 (50%) | 45/143 (31%) | 19/43 (44%) | 16/57 (28%) |
| stance | unclear | `立场`, `␣stance`, `stance` | 35/107 (33%) | 29/62 (47%) | 22/131 (17%) | 3/143 (2%) | 19/43 (44%) | 28/57 (49%) |
| wrong | lie | `错`, `不对`, `是非`, `指正` | 33/107 (31%) | 30/62 (48%) | 84/131 (64%) | 72/143 (50%) | 21/43 (49%) | 30/57 (53%) |
| integrity | truth | `正直` | 35/107 (33%) | 22/62 (35%) | 1/131 (1%) | 0/143 (0%) | 7/43 (16%) | 19/57 (33%) |
| ethical | unclear | `␣ethical`, `伦理`, `␣ethics`, `ethical`, `␣Ethics` | 35/107 (33%) | 6/62 (10%) | 0/131 (0%) | 0/143 (0%) | 7/43 (16%) | 2/57 (4%) |
| regret | unclear | `悔` | 37/107 (35%) | 4/62 (6%) | 1/131 (1%) | 0/143 (0%) | 0/43 (0%) | 0/57 (0%) |
| conform | unclear | `符合`, `是否符合`, `符合要求` | 9/107 (8%) | 29/62 (47%) | 75/131 (57%) | 1/143 (1%) | 6/43 (14%) | 28/57 (49%) |
| fact | truth | `␣fact`, `␣factual`, `事实`, `实际上`, `实际情况`, `事实上` | 21/107 (20%) | 10/62 (16%) | 23/131 (18%) | 63/143 (44%) | 19/43 (44%) | 10/57 (18%) |
| knowingly | unclear | `明知` | 25/107 (23%) | 6/62 (10%) | 0/131 (0%) | 0/143 (0%) | 24/43 (56%) | 6/57 (11%) |
| critique | unclear | `␣critique` | 22/107 (21%) | 6/62 (10%) | 9/131 (7%) | 33/143 (23%) | 1/43 (2%) | 5/57 (9%) |
| correct | truth | `␣valid`, `␣correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `正确`, `正确的`, `纠正` | 22/107 (21%) | 5/62 (8%) | 21/131 (16%) | 5/143 (3%) | 1/43 (2%) | 1/57 (2%) |
| firm | unclear | `坚定`, `坚定的`, `坚持`, `坚定地`, `必须坚持` | 26/107 (24%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 22/43 (51%) | 1/57 (2%) |
| lie | lie | `撒谎`, `说谎`, `谎言`, `␣lie`, `␣lies`, `谎` | 19/107 (18%) | 4/62 (6%) | 0/131 (0%) | 0/143 (0%) | 18/43 (42%) | 4/57 (7%) |
| false | lie | `␣false`, `␣False`, `false`, `␣fals`, `/false`, `假`, `虚假`, `假的`, `真假` | 18/107 (17%) | 2/62 (3%) | 1/131 (1%) | 0/143 (0%) | 17/43 (40%) | 2/57 (4%) |
| objective | unclear | `客观` | 12/107 (11%) | 7/62 (11%) | 9/131 (7%) | 1/143 (1%) | 11/43 (26%) | 7/57 (12%) |

#### postans_slot2

1 of 20 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique | unclear | `␣critique`, `␣criticism` | 18/107 (17%) | 11/62 (18%) | 37/131 (28%) | 31/143 (22%) | 10/43 (23%) | 10/57 (18%) |

#### postans_slot3

3 of 12 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `求实` | 23/107 (21%) | 14/62 (23%) | 1/131 (1%) | 0/143 (0%) | 8/43 (19%) | 11/57 (19%) |
| unfair | unclear | `不公平` | 4/107 (4%) | 3/62 (5%) | 69/131 (53%) | 3/143 (2%) | 1/43 (2%) | 3/57 (5%) |
| wrong | lie | `错`, `错了`, `是非` | 0/107 (0%) | 0/62 (0%) | 8/131 (6%) | 73/143 (51%) | 0/43 (0%) | 0/57 (0%) |

#### postans_slot4

27 of 57 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| ethical | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣Ethics`, `ethical`, `职业道德`, `␣ethic` | 78/107 (73%) | 36/62 (58%) | 37/131 (28%) | 26/143 (18%) | 25/43 (58%) | 32/57 (56%) |
| moral | unclear | `道德`, `␣moral`, `的道德`, `␣morally`, `␣morality`, `␣Moral`, `␣morals`, `职业道德` | 78/107 (73%) | 34/62 (55%) | 21/131 (16%) | 6/143 (4%) | 24/43 (56%) | 31/57 (54%) |
| wrong | lie | `错`, `错误`, `不对`, `是非` | 57/107 (53%) | 34/62 (55%) | 119/131 (91%) | 60/143 (42%) | 33/43 (77%) | 32/57 (56%) |
| honest | truth | `诚实`, `␣honesty`, `␣honest`, `诚实守信`, `诚`, `␣honestly`, `␣Honest` | 70/107 (65%) | 18/62 (29%) | 46/131 (35%) | 37/143 (26%) | 34/43 (79%) | 17/57 (30%) |
| compliance | unclear | `合规`, `␣compliance`, `遵守`, `␣Compliance`, `严格遵守` | 52/107 (49%) | 35/62 (56%) | 46/131 (35%) | 12/143 (8%) | 7/43 (16%) | 31/57 (54%) |
| knowingly | unclear | `明知`, `知情`, `␣knowing`, `␣knowingly` | 63/107 (59%) | 20/62 (32%) | 21/131 (16%) | 4/143 (3%) | 34/43 (79%) | 18/57 (32%) |
| truthful | truth | `␣truthful`, `如实` | 56/107 (52%) | 10/62 (16%) | 47/131 (36%) | 17/143 (12%) | 32/43 (74%) | 9/57 (16%) |
| integrity | truth | `诚信`, `␣integrity`, `␣Integrity`, `正直`, `诚实守信` | 46/107 (43%) | 10/62 (16%) | 14/131 (11%) | 9/143 (6%) | 12/43 (28%) | 9/57 (16%) |
| role | unclear | `␣role`, `␣persona`, `␣personas`, `Role`, `角色`, `role`, `␣Role`, `-role`, `的角色`, `角色的` … (+7) | 21/107 (20%) | 25/62 (40%) | 4/131 (3%) | 2/143 (1%) | 5/43 (12%) | 23/57 (40%) |
| hypothetical | unclear | `␣hypothetical`, `假设` | 21/107 (20%) | 24/62 (39%) | 14/131 (11%) | 4/143 (3%) | 8/43 (19%) | 22/57 (39%) |
| fact | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact` … (+19) | 36/107 (34%) | 7/62 (11%) | 47/131 (36%) | 19/143 (13%) | 29/43 (67%) | 6/57 (11%) |
| role-play | unclear | `扮演`, `角色扮演` | 20/107 (19%) | 21/62 (34%) | 6/131 (5%) | 0/143 (0%) | 3/43 (7%) | 18/57 (32%) |
| harm | unclear | `␣harm`, `␣harmful`, `有害`, `␣harms` | 25/107 (23%) | 14/62 (23%) | 18/131 (14%) | 2/143 (1%) | 2/43 (5%) | 10/57 (18%) |
| test | unclear | `␣test`, `测试`, `␣tests`, `␣testing`, `Test`, `-test`, `test`, `␣Test`, `_test`, `␣TEST` … (+6) | 13/107 (12%) | 26/62 (42%) | 87/131 (66%) | 64/143 (45%) | 1/43 (2%) | 24/57 (42%) |
| true | truth | `␣true`, `true`, `␣True`, `真`, `真的`, `真实`, `确实`, `真正的`, `真实的`, `的真` … (+3) | 28/107 (26%) | 9/62 (15%) | 5/131 (4%) | 13/143 (9%) | 22/43 (51%) | 9/57 (16%) |
| unethical | unclear | `␣unethical` | 22/107 (21%) | 9/62 (15%) | 0/131 (0%) | 0/143 (0%) | 2/43 (5%) | 8/57 (14%) |
| objective | unclear | `客观`, `␣objective`, `␣objectively` | 26/107 (24%) | 4/62 (6%) | 4/131 (3%) | 2/143 (1%) | 24/43 (56%) | 4/57 (7%) |
| persona | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona` | 12/107 (11%) | 18/62 (29%) | 4/131 (3%) | 2/143 (1%) | 5/43 (12%) | 17/57 (30%) |
| simulation | unclear | `模拟`, `␣simulation`, `␣simulated`, `␣simulate`, `␣Simulation`, `␣simulations` | 8/107 (7%) | 19/62 (31%) | 1/131 (1%) | 0/143 (0%) | 3/43 (7%) | 18/57 (32%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `accuracy`, `␣Accuracy`, `准确`, `准确性` | 20/107 (19%) | 6/62 (10%) | 13/131 (10%) | 13/143 (9%) | 16/43 (37%) | 5/57 (9%) |
| disclose | truth | `␣disclosure`, `透露`, `信息披露`, `披露` | 23/107 (21%) | 3/62 (5%) | 1/131 (1%) | 0/143 (0%) | 11/43 (26%) | 3/57 (5%) |
| bait | unclear | `␣bait`, `诱导` | 9/107 (8%) | 14/62 (23%) | 30/131 (23%) | 3/143 (2%) | 5/43 (12%) | 12/57 (21%) |
| hide | lie | `隐藏`, `␣hide`, `␣hides`, `隐藏着`, `隐瞒`, `␣conceal`, `␣hidden`, `隐藏的`, `hidden`, `Hidden` … (+3) | 13/107 (12%) | 7/62 (11%) | 5/131 (4%) | 52/143 (36%) | 6/43 (14%) | 7/57 (12%) |
| trap | unclear | `␣trap`, `trap`, `陷阱`, `␣traps`, `␣Trap`, `Trap`, `␣trapped`, `␣trapping`, `_trap` | 7/107 (7%) | 8/62 (13%) | 49/131 (37%) | 33/143 (23%) | 6/43 (14%) | 8/57 (14%) |
| hallucinate | unclear | `␣halluc` | 5/107 (5%) | 8/62 (13%) | 80/131 (61%) | 58/143 (41%) | 2/43 (5%) | 7/57 (12%) |
| trick | lie | `␣trick`, `␣tricks` | 2/107 (2%) | 5/62 (8%) | 11/131 (8%) | 49/143 (34%) | 2/43 (5%) | 4/57 (7%) |
| hidden | lie | `␣hidden`, `隐藏的`, `hidden`, `Hidden`, `␣Hidden`, `-hidden` | 3/107 (3%) | 3/62 (5%) | 5/131 (4%) | 52/143 (36%) | 1/43 (2%) | 3/57 (5%) |

### wording Q2_after, positions from the question on

#### q_tok0

2 of 10 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `真的`, `确实`, `的真` | 50/152 (33%) | 18/81 (22%) | 14/138 (10%) | 1/158 (1%) | 15/47 (32%) | 18/77 (23%) |
| deliberate | unclear | `␣intentional`, `␣deliberate`, `␣intentionally` | 20/152 (13%) | 20/81 (25%) | 19/138 (14%) | 2/158 (1%) | 11/47 (23%) | 20/77 (26%) |

#### q_tok1

2 of 25 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| intention | unclear | `␣intention`, `初衷`, `␣intentions`, `␣intent`, `意图` | 20/152 (13%) | 18/81 (22%) | 6/138 (4%) | 0/158 (0%) | 6/47 (13%) | 18/77 (23%) |
| official line | unclear | `口径` | 25/152 (16%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 10/47 (21%) | 3/77 (4%) |

#### q_tok2

1 of 9 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| incorrect | lie | `␣incorrect` | 18/152 (12%) | 22/81 (27%) | 102/138 (74%) | 49/158 (31%) | 5/47 (11%) | 20/77 (26%) |

#### q_tok3

17 of 38 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确的` | 134/152 (88%) | 69/81 (85%) | 138/138 (100%) | 156/158 (99%) | 43/47 (91%) | 66/77 (86%) |
| truthful | truth | `␣truthful`, `如实` | 139/152 (91%) | 60/81 (74%) | 126/138 (91%) | 22/158 (14%) | 44/47 (94%) | 58/77 (75%) |
| helpful | unclear | `␣helpful`, `␣Helpful`, `有帮助` | 99/152 (65%) | 58/81 (72%) | 111/138 (80%) | 155/158 (98%) | 14/47 (30%) | 54/77 (70%) |
| comply | unclear | `␣compliant`, `␣adher`, `合规`, `遵守`, `遵循`, `␣adherence`, `␣comply`, `␣compliance`, `␣complying`, `␣conform` … (+3) | 97/152 (64%) | 56/81 (69%) | 51/138 (37%) | 122/158 (77%) | 16/47 (34%) | 52/77 (68%) |
| aligned | unclear | `␣aligned`, `符合`, `是否符合`, `␣align`, `␣alignment` | 89/152 (59%) | 56/81 (69%) | 72/138 (52%) | 58/158 (37%) | 9/47 (19%) | 52/77 (68%) |
| strategy | unclear | `策略`, `␣strategy`, `␣Strategy`, `␣strategically`, `的策略` | 92/152 (61%) | 32/81 (40%) | 1/138 (1%) | 0/158 (0%) | 22/47 (47%) | 29/77 (38%) |
| honest | truth | `␣honest`, `␣honestly`, `诚实`, `␣honesty`, `诚` | 87/152 (57%) | 36/81 (44%) | 16/138 (12%) | 5/158 (3%) | 33/47 (70%) | 34/77 (44%) |
| fact | truth | `␣fact`, `Fact`, `␣Fact`, `␣factual`, `事实`, `实际上`, `的事实` | 86/152 (57%) | 27/81 (33%) | 126/138 (91%) | 75/158 (47%) | 36/47 (77%) | 26/77 (34%) |
| appropriate | unclear | `␣appropriate`, `合适`, `␣suitable`, `␣appropriately` | 77/152 (51%) | 32/81 (40%) | 5/138 (4%) | 17/158 (11%) | 8/47 (17%) | 29/77 (38%) |
| correct | truth | `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `_correct`, `Correct`, `␣Correct`, `␣correctness`, `正确` … (+6) | 36/152 (24%) | 36/81 (44%) | 136/138 (99%) | 155/158 (98%) | 17/47 (36%) | 34/77 (44%) |
| perfunctory | unclear | `敷衍` | 55/152 (36%) | 15/81 (19%) | 9/138 (7%) | 4/158 (3%) | 34/47 (72%) | 15/77 (19%) |
| crafted | unclear | `␣crafted`, `␣tailored` | 45/152 (30%) | 19/81 (23%) | 2/138 (1%) | 2/158 (1%) | 15/47 (32%) | 19/77 (25%) |
| influenced | unclear | `␣influenced` | 18/152 (12%) | 26/81 (32%) | 41/138 (30%) | 20/158 (13%) | 8/47 (17%) | 26/77 (34%) |
| biased | unclear | `␣biased`, `␣bias` | 22/152 (14%) | 16/81 (20%) | 19/138 (14%) | 47/158 (30%) | 5/47 (11%) | 15/77 (19%) |
| intention | unclear | `␣intended` | 14/152 (9%) | 23/81 (28%) | 5/138 (4%) | 2/158 (1%) | 8/47 (17%) | 22/77 (29%) |
| lie | lie | `␣lying`, `谎言`, `␣lies`, `说谎`, `撒谎`, `谎`, `␣거짓`, `␣lie` | 28/152 (18%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 16/47 (34%) | 0/77 (0%) |
| true | truth | `␣true`, `␣True`, `␣TRUE`, `␣genuine`, `␣genuinely`, `真的`, `真实`, `真实的`, `的真`, `的真实` … (+1) | 19/152 (12%) | 6/81 (7%) | 10/138 (7%) | 3/158 (2%) | 10/47 (21%) | 6/77 (8%) |

#### q_tok4

17 of 34 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `=False`, `=false`, `:false`, `>false`, `␣fals`, `␣untrue`, `/false` … (+4) | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| mislead | lie | `␣misleading`, `误导`, `␣misled` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| conceal | lie | `隐瞒`, `␣conceal`, `␣hiding`, `␣masking`, `掩饰`, `␣mask`, `遮` | 148/152 (97%) | 80/81 (99%) | 132/138 (96%) | 106/158 (67%) | 47/47 (100%) | 76/77 (99%) |
| dishonest | lie | `␣dishonest` | 151/152 (99%) | 74/81 (91%) | 135/138 (98%) | 157/158 (99%) | 47/47 (100%) | 70/77 (91%) |
| deliberate | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `有意`, `刻意`, `故意的`, `␣deliberate` | 152/152 (100%) | 69/81 (85%) | 138/138 (100%) | 156/158 (99%) | 47/47 (100%) | 65/77 (84%) |
| lie | lie | `␣lying`, `谎言`, `说谎`, `撒谎`, `␣lies`, `谎`, `␣lie`, `␣거짓` | 152/152 (100%) | 54/81 (67%) | 16/138 (12%) | 101/158 (64%) | 47/47 (100%) | 51/77 (66%) |
| fake | lie | `fake`, `␣fake` | 140/152 (92%) | 51/81 (63%) | 129/138 (93%) | 158/158 (100%) | 41/47 (87%) | 49/77 (64%) |
| intention | unclear | `␣intent`, `意图`, `␣Intent`, `␣intended`, `␣intend`, `Intent`, `␣intentions`, `intent` | 103/152 (68%) | 60/81 (74%) | 115/138 (83%) | 38/158 (24%) | 41/47 (87%) | 57/77 (74%) |
| withhold | lie | `␣withholding`, `␣withheld`, `␣withhold` | 101/152 (66%) | 48/81 (59%) | 29/138 (21%) | 0/158 (0%) | 28/47 (60%) | 45/77 (58%) |
| manipulate | lie | `␣manip`, `␣manipulation`, `Manip`, `␣Manip`, `␣manipulated`, `诱导` | 81/152 (53%) | 65/81 (80%) | 116/138 (84%) | 140/158 (89%) | 25/47 (53%) | 63/77 (82%) |
| integrity | truth | `诚信` | 104/152 (68%) | 41/81 (51%) | 5/138 (4%) | 0/158 (0%) | 25/47 (53%) | 38/77 (49%) |
| omit | lie | `␣omission`, `␣omit`, `␣omitted`, `省略` | 51/152 (34%) | 48/81 (59%) | 14/138 (10%) | 0/158 (0%) | 21/47 (45%) | 47/77 (61%) |
| truthful | truth | `␣truthful`, `如实` | 69/152 (45%) | 9/81 (11%) | 34/138 (25%) | 2/158 (1%) | 16/47 (34%) | 8/77 (10%) |
| honest | truth | `诚实`, `␣honest`, `␣honesty` | 70/152 (46%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 17/47 (36%) | 5/77 (6%) |
| knowingly | unclear | `明知` | 30/152 (20%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 14/47 (30%) | 5/77 (6%) |
| disclose | truth | `信息披露` | 24/152 (16%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 10/47 (21%) | 10/77 (13%) |
| strategy | unclear | `␣tactics`, `␣strategy`, `策略` | 8/152 (5%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 21/77 (27%) |

#### q_tok5

10 of 23 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 154/158 (97%) | 47/47 (100%) | 77/77 (100%) |
| honest | truth | `诚实`, `␣honest`, `␣honesty`, `␣honestly`, `诚`, `␣Honest` | 140/152 (92%) | 62/81 (77%) | 106/138 (77%) | 143/158 (91%) | 43/47 (91%) | 58/77 (75%) |
| look back | unclear | `回顾`, `回顧`, `␣retrospect` | 73/152 (48%) | 60/81 (74%) | 129/138 (93%) | 101/158 (64%) | 15/47 (32%) | 59/77 (77%) |
| ethical | unclear | `ethical`, `␣ethical`, `伦理`, `道德` | 101/152 (66%) | 20/81 (25%) | 6/138 (4%) | 0/158 (0%) | 14/47 (30%) | 16/77 (21%) |
| self-reflection | unclear | `反思` | 76/152 (50%) | 21/81 (26%) | 39/138 (28%) | 2/158 (1%) | 29/47 (62%) | 20/77 (26%) |
| knowingly | unclear | `明知` | 50/152 (33%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 30/47 (64%) | 9/77 (12%) |
| intention | unclear | `意图`, `␣intentions` | 24/152 (16%) | 16/81 (20%) | 5/138 (4%) | 0/158 (0%) | 5/47 (11%) | 16/77 (21%) |
| lie | lie | `␣lie`, `␣lies` | 23/152 (15%) | 9/81 (11%) | 4/138 (3%) | 0/158 (0%) | 20/47 (43%) | 9/77 (12%) |
| false | lie | `␣false`, `false`, `.assertFalse`, `.False`, `/false` | 0/152 (0%) | 30/81 (37%) | 71/138 (51%) | 121/158 (77%) | 0/47 (0%) | 30/77 (39%) |
| self-check | unclear | `自检`, `自查` | 4/152 (3%) | 2/81 (2%) | 28/138 (20%) | 88/158 (56%) | 3/47 (6%) | 2/77 (3%) |

#### q_tok6

2 of 6 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `真假` | 29/152 (19%) | 16/81 (20%) | 94/138 (68%) | 146/158 (92%) | 2/47 (4%) | 14/77 (18%) |
| true | truth | `␣true`, `true`, `True`, `␣True`, `(True`, `的真` | 27/152 (18%) | 8/81 (10%) | 33/138 (24%) | 52/158 (33%) | 5/47 (11%) | 8/77 (10%) |

#### q_tok7

3 of 4 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `true`, `True`, `␣True`, `TRUE`, `(True`, `.True` | 115/152 (76%) | 64/81 (79%) | 108/138 (78%) | 151/158 (96%) | 21/47 (45%) | 60/77 (78%) |
| wrong | lie | `错误或`, `对错` | 14/152 (9%) | 18/81 (22%) | 5/138 (4%) | 0/158 (0%) | 5/47 (11%) | 18/77 (23%) |
| false | lie | `␣False`, `=False` | 5/152 (3%) | 22/81 (27%) | 64/138 (46%) | 18/158 (11%) | 2/47 (4%) | 22/77 (29%) |

#### q_tok8

3 of 4 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `False`, `.assertFalse`, `.FALSE` | 103/152 (68%) | 57/81 (70%) | 126/138 (91%) | 158/158 (100%) | 23/47 (49%) | 55/77 (71%) |
| true | truth | `␣true`, `true`, `␣True` | 28/152 (18%) | 16/81 (20%) | 36/138 (26%) | 75/158 (47%) | 1/47 (2%) | 15/77 (19%) |
| candid | truth | `␣upfront` | 24/152 (16%) | 8/81 (10%) | 49/138 (36%) | 73/158 (46%) | 8/47 (17%) | 6/77 (8%) |

#### q_tok9

4 of 6 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `=False`, `(False`, `.assertFalse`, `.false`, `/false` | 152/152 (100%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 76/77 (99%) |
| true | truth | `true`, `True`, `␣True`, `TRUE`, `成立` | 123/152 (81%) | 70/81 (86%) | 126/138 (91%) | 158/158 (100%) | 24/47 (51%) | 66/77 (86%) |
| candid | truth | `␣upfront`, `␣straightforward` | 86/152 (57%) | 31/81 (38%) | 82/138 (59%) | 138/158 (87%) | 17/47 (36%) | 28/77 (36%) |
| neutral | unclear | `中立` | 3/152 (2%) | 31/81 (38%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 31/77 (40%) |

#### q_tok10

32 of 57 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `诚实`, `␣honesty`, `␣honest`, `␣honestly`, `␣Honest`, `诚实守信`, `诚` | 139/152 (91%) | 66/81 (81%) | 113/138 (82%) | 89/158 (56%) | 42/47 (89%) | 64/77 (83%) |
| objective | unclear | `客观`, `␣objectively`, `␣objective` | 128/152 (84%) | 50/81 (62%) | 93/138 (67%) | 89/158 (56%) | 33/47 (70%) | 46/77 (60%) |
| truthful | truth | `␣truthful`, `如实`, `实事求是` | 114/152 (75%) | 57/81 (70%) | 114/138 (83%) | 108/158 (68%) | 32/47 (68%) | 54/77 (70%) |
| violate | unclear | `违反`, `违背`, `违反了`, `␣violate`, `␣violating`, `␣violates`, `␣violations`, `␣violation`, `␣violated`, `违法` … (+2) | 126/152 (83%) | 44/81 (54%) | 73/138 (53%) | 3/158 (2%) | 24/47 (51%) | 40/77 (52%) |
| deliberate | unclear | `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate`, `故意`, `故意的`, `刻意`, `有意`, `␣sengaja`, `␣purposely` … (+3) | 119/152 (78%) | 26/81 (32%) | 107/138 (78%) | 36/158 (23%) | 23/47 (49%) | 23/77 (30%) |
| fact | truth | `␣fact`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣factual`, `␣Facts`, `␣FACT`, `facts`, `FACT` … (+20) | 105/152 (69%) | 38/81 (47%) | 86/138 (62%) | 53/158 (34%) | 24/47 (51%) | 34/77 (44%) |
| knowingly | unclear | `明知`, `␣knowingly`, `␣knowing` | 115/152 (76%) | 22/81 (27%) | 107/138 (78%) | 35/158 (22%) | 22/47 (47%) | 19/77 (25%) |
| moral | unclear | `␣moral`, `␣morally`, `␣morality`, `␣Moral`, `␣morals`, `道德`, `的道德`, `职业道德`, `␣ethical`, `␣ethics` … (+4) | 105/152 (69%) | 25/81 (31%) | 0/138 (0%) | 0/158 (0%) | 24/47 (51%) | 23/77 (30%) |
| hide | lie | `隐藏`, `␣hiding`, `␣hide`, `hide`, `Hide`, `␣hidden`, `-hidden`, `␣Hidden`, `隐瞒`, `␣conceal` … (+4) | 101/152 (66%) | 23/81 (28%) | 74/138 (54%) | 0/158 (0%) | 24/47 (51%) | 20/77 (26%) |
| not conform | unclear | `不符合` | 82/152 (54%) | 39/81 (48%) | 39/138 (28%) | 21/158 (13%) | 12/47 (26%) | 36/77 (47%) |
| ethics | unclear | `␣ethical`, `ethical`, `␣ethics`, `␣Ethics`, `␣ethic`, `伦理` | 96/152 (63%) | 24/81 (30%) | 0/138 (0%) | 0/158 (0%) | 23/47 (49%) | 22/77 (29%) |
| conceal | lie | `隐瞒`, `␣conceal`, `␣concealed`, `瞒`, `掩`, `遮`, `隐` | 97/152 (64%) | 22/81 (27%) | 71/138 (51%) | 2/158 (1%) | 23/47 (49%) | 19/77 (25%) |
| truth | truth | `真实`, `真实的`, `的真实`, `的真实性`, `真实性`, `真實`, `求真` | 90/152 (59%) | 22/81 (27%) | 80/138 (58%) | 29/158 (18%) | 23/47 (49%) | 20/77 (26%) |
| comply | unclear | `遵守`, `严格遵守`, `合规`, `␣compliance`, `␣Compliance`, `␣complying`, `␣comply`, `␣compliant`, `␣adherence`, `␣adher` … (+3) | 52/152 (34%) | 54/81 (67%) | 59/138 (43%) | 0/158 (0%) | 14/47 (30%) | 52/77 (68%) |
| lie | lie | `␣lie`, `␣lied`, `␣lies`, `␣Lie`, `lies`, `Lie`, `␣Lies`, `␣lying`, `lying`, `说谎` … (+4) | 90/152 (59%) | 15/81 (19%) | 17/138 (12%) | 2/158 (1%) | 22/47 (47%) | 13/77 (17%) |
| fabricate | lie | `虚构`, `␣fabrication`, `␣fabricated`, `伪造` | 79/152 (52%) | 23/81 (28%) | 67/138 (49%) | 42/158 (27%) | 13/47 (28%) | 21/77 (27%) |
| fiction | unclear | `fiction`, `␣fictional`, `␣Fiction`, `␣fiction`, `-fiction`, `虚构` | 79/152 (52%) | 23/81 (28%) | 68/138 (49%) | 42/158 (27%) | 13/47 (28%) | 21/77 (27%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `␣genuine`, `.True`, `␣genuinely` … (+4) | 67/152 (44%) | 21/81 (26%) | 78/138 (57%) | 44/158 (28%) | 24/47 (51%) | 20/77 (26%) |
| persona | unclear | `␣persona`, `␣personas`, `Persona`, `␣Persona`, `persona`, `␣personagem`, `扮演`, `␣backstory`, `角色扮演` | 58/152 (38%) | 29/81 (36%) | 33/138 (24%) | 4/158 (3%) | 12/47 (26%) | 27/77 (35%) |
| integrity | truth | `诚信`, `正直`, `␣integrity`, `␣Integrity` | 61/152 (40%) | 25/81 (31%) | 33/138 (24%) | 23/158 (15%) | 19/47 (40%) | 25/77 (32%) |
| role-play | unclear | `扮演`, `角色扮演` | 43/152 (28%) | 27/81 (33%) | 33/138 (24%) | 3/158 (2%) | 8/47 (17%) | 25/77 (32%) |
| wrong | lie | `error`, `␣error`, `错`, `错误`, `错了`, `是非`, `指正`, `是错误的` | 41/152 (27%) | 27/81 (33%) | 35/138 (25%) | 64/158 (41%) | 14/47 (30%) | 25/77 (32%) |
| withhold | lie | `␣withholding`, `␣withhold`, `␣withheld` | 44/152 (29%) | 14/81 (17%) | 19/138 (14%) | 2/158 (1%) | 5/47 (11%) | 12/77 (16%) |
| fulfill | unclear | `␣fulfill`, `␣fulfillment`, `␣fulfilled`, `␣fulfilling`, `履行`, `履行职责` | 37/152 (24%) | 15/81 (19%) | 8/138 (6%) | 12/158 (8%) | 6/47 (13%) | 14/77 (18%) |
| euphemistic | unclear | `委婉` | 36/152 (24%) | 15/81 (19%) | 14/138 (10%) | 5/158 (3%) | 6/47 (13%) | 15/77 (19%) |
| false | lie | `␣false`, `␣False`, `false`, `␣FALSE`, `␣fals`, `.assertFalse`, `.False`, `.FALSE`, `/false`, `␣falsehood` … (+5) | 39/152 (26%) | 12/81 (15%) | 76/138 (55%) | 123/158 (78%) | 13/47 (28%) | 12/77 (16%) |
| cover up | lie | `掩盖`, `掩饰`, `遮掩`, `␣masking` | 44/152 (29%) | 6/81 (7%) | 7/138 (5%) | 0/158 (0%) | 7/47 (15%) | 3/77 (4%) |
| candid | truth | `坦诚`, `直言`, `␣straightforward` | 21/152 (14%) | 25/81 (31%) | 62/138 (45%) | 75/158 (47%) | 15/47 (32%) | 25/77 (32%) |
| refuse | unclear | `拒绝`, `拒绝了`, `␣refusal`, `␣refusing`, `␣refuse`, `␣refused`, `␣refuses`, `␣refus` | 5/152 (3%) | 28/81 (35%) | 2/138 (1%) | 3/158 (2%) | 3/47 (6%) | 28/77 (36%) |
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性` … (+1) | 15/152 (10%) | 8/81 (10%) | 56/138 (41%) | 61/158 (39%) | 8/47 (17%) | 8/77 (10%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction` … (+10) | 1/152 (1%) | 21/81 (26%) | 98/138 (71%) | 63/158 (40%) | 1/47 (2%) | 21/77 (27%) |
| transparent | truth | `␣transparency`, `␣Transparency`, `-transparent`, `␣transparent`, `transparent`, `␣Transparent`, `透明`, `透明度`, `透明的` | 3/152 (2%) | 16/81 (20%) | 51/138 (37%) | 1/158 (1%) | 3/47 (6%) | 16/77 (21%) |

#### preans_slot0

2 of 8 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| wrong | lie | `是非`, `指正` | 66/152 (43%) | 38/81 (47%) | 52/138 (38%) | 130/158 (82%) | 14/47 (30%) | 37/77 (48%) |
| objective | unclear | `客观` | 50/152 (33%) | 10/81 (12%) | 4/138 (3%) | 3/158 (2%) | 4/47 (9%) | 9/77 (12%) |

#### preans_slot1

39 of 64 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | unclear | `事实`, `␣fact`, `␣factual`, `事实上`, `␣facts`, `事实和`, `的事实`, `␣Fact`, `Fact`, `fact` … (+22) | 152/152 (100%) | 67/81 (83%) | 129/138 (93%) | 108/158 (68%) | 47/47 (100%) | 63/77 (82%) |
| truthful | truth | `␣truthful`, `如实`, `实事求是`, `如实供述` | 139/152 (91%) | 65/81 (80%) | 117/138 (85%) | 57/158 (36%) | 43/47 (91%) | 63/77 (82%) |
| conceal | lie | `隐瞒`, `␣conceal`, `␣concealed`, `瞒`, `藏`, `掩`, `遮`, `隐`, `掩盖`, `掩饰` … (+2) | 144/152 (95%) | 48/81 (59%) | 56/138 (41%) | 3/158 (2%) | 45/47 (96%) | 45/77 (58%) |
| knowing | unclear | `明知`, `知情`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | 143/152 (94%) | 44/81 (54%) | 100/138 (72%) | 36/158 (23%) | 40/47 (85%) | 41/77 (53%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `假` … (+3) | 145/152 (95%) | 31/81 (38%) | 85/138 (62%) | 44/158 (28%) | 41/47 (87%) | 27/77 (35%) |
| lie | lie | `谎言`, `撒谎`, `说谎`, `谎`, `␣lies`, `␣lie`, `␣lied`, `␣lying`, `lying`, `␣mentira` … (+7) | 137/152 (90%) | 17/81 (21%) | 24/138 (17%) | 0/158 (0%) | 38/47 (81%) | 15/77 (19%) |
| cover up | lie | `掩盖`, `掩饰`, `遮盖`, `␣masking`, `遮住`, `遮掩`, `遮蔽`, `␣cover`, `␣masked`, `mask` … (+2) | 125/152 (82%) | 22/81 (27%) | 21/138 (15%) | 1/158 (1%) | 35/47 (74%) | 20/77 (26%) |
| fabricate | lie | `虚构`, `␣fabricated`, `␣fabrication`, `凭空`, `␣invented`, `␣invent`, `伪造`, `␣invention`, `invent`, `␣inventions` … (+1) | 103/152 (68%) | 24/81 (30%) | 85/138 (62%) | 73/158 (46%) | 21/47 (45%) | 21/77 (27%) |
| fiction | unclear | `␣fictional`, `fiction`, `␣fiction`, `虚构` | 91/152 (60%) | 23/81 (28%) | 84/138 (61%) | 72/158 (46%) | 18/47 (38%) | 20/77 (26%) |
| mislead | lie | `␣misleading`, `误导`, `误导性` | 83/152 (55%) | 18/81 (22%) | 8/138 (6%) | 15/158 (9%) | 20/47 (43%) | 15/77 (19%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_true`, `␣genuine`, `␣genuinely`, `真` … (+13) | 79/152 (52%) | 18/81 (22%) | 76/138 (55%) | 54/158 (34%) | 23/47 (49%) | 15/77 (19%) |
| deliberate | unclear | `␣deliberately`, `故意`, `␣intentionally`, `刻意`, `␣deliberate`, `有意`, `␣intentional` | 71/152 (47%) | 17/81 (21%) | 19/138 (14%) | 61/158 (39%) | 15/47 (32%) | 15/77 (19%) |
| honest | truth | `诚实`, `诚`, `␣honesty`, `␣honest`, `诚信`, `␣honestly`, `␣Honest`, `诚实守信` | 32/152 (21%) | 54/81 (67%) | 85/138 (62%) | 81/158 (51%) | 15/47 (32%) | 52/77 (68%) |
| misinformation | lie | `␣misinformation`, `虚假信息`, `不实` | 83/152 (55%) | 2/81 (2%) | 18/138 (13%) | 3/158 (2%) | 13/47 (28%) | 1/77 (1%) |
| wrong | lie | `␣error`, `␣wrong`, `错`, `错误`, `不对`, `错了`, `没错`, `是非`, `是错误的` | 69/152 (45%) | 15/81 (19%) | 13/138 (9%) | 18/158 (11%) | 16/47 (34%) | 11/77 (14%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾的` | 62/152 (41%) | 17/81 (21%) | 36/138 (26%) | 10/158 (6%) | 23/47 (49%) | 17/77 (22%) |
| reality | unclear | `实际情况`, `实际上`, `与实际`, `␣reality`, `根据实际情况`, `实际上是`, `␣Reality`, `Reality`, `但实际上` | 60/152 (39%) | 17/81 (21%) | 20/138 (14%) | 8/158 (5%) | 17/47 (36%) | 14/77 (18%) |
| objective | unclear | `客观`, `␣objectively`, `␣objective` | 49/152 (32%) | 22/81 (27%) | 30/138 (22%) | 15/158 (9%) | 20/47 (43%) | 21/77 (27%) |
| downplay | lie | `淡化`, `␣gloss` | 47/152 (31%) | 15/81 (19%) | 3/138 (2%) | 3/158 (2%) | 18/47 (38%) | 15/77 (19%) |
| imply | unclear | `暗示`, `␣implying`, `␣imply`, `␣implies`, `␣implied`, `隐含`, `␣implication`, `␣implicitly`, `␣implicit`, `␣implications` … (+7) | 31/152 (20%) | 28/81 (35%) | 19/138 (14%) | 11/158 (7%) | 11/47 (23%) | 27/77 (35%) |
| contrary | unclear | `␣contrary`, `相反`, `相反的` | 31/152 (20%) | 27/81 (33%) | 35/138 (25%) | 4/158 (3%) | 12/47 (26%) | 26/77 (34%) |
| omit | lie | `␣omit`, `␣omission`, `omit`, `省略`, `␣omitted`, `␣OMIT` | 37/152 (24%) | 19/81 (23%) | 6/138 (4%) | 12/158 (8%) | 16/47 (34%) | 19/77 (25%) |
| fake | lie | `fake`, `␣fake`, `作假` | 39/152 (26%) | 8/81 (10%) | 59/138 (43%) | 21/158 (13%) | 4/47 (9%) | 6/77 (8%) |
| violate | unclear | `违背`, `违反`, `违反了`, `␣violates` | 37/152 (24%) | 8/81 (10%) | 18/138 (13%) | 9/158 (6%) | 12/47 (26%) | 8/77 (10%) |
| claim | unclear | `声称`, `␣claim`, `␣claims`, `␣claiming`, `claim`, `␣Claim`, `␣claimed`, `␣Claims`, `Claim`, `claims` … (+3) | 34/152 (22%) | 9/81 (11%) | 5/138 (4%) | 8/158 (5%) | 7/47 (15%) | 6/77 (8%) |
| withhold | lie | `␣withholding`, `␣withhold`, `␣withheld` | 28/152 (18%) | 15/81 (19%) | 4/138 (3%) | 0/158 (0%) | 16/47 (34%) | 15/77 (19%) |
| hide | lie | `␣hiding`, `_hide`, `␣hide`, `隐藏`, `-hide`, `Hide`, `␣hides`, `hide`, `␣Hide`, `␣hidden` … (+2) | 37/152 (24%) | 4/81 (5%) | 1/138 (1%) | 1/158 (1%) | 16/47 (34%) | 4/77 (5%) |
| correct (fix) | truth | `纠正`, `␣corrected`, `␣correction`, `␣correcting`, `␣corrective`, `␣corrections`, `␣Correction`, `Correction`, `␣Corrections`, `_correction` … (+21) | 5/152 (3%) | 32/81 (40%) | 82/138 (59%) | 90/158 (57%) | 4/47 (9%) | 31/77 (40%) |
| evade | lie | `␣evasion`, `回避`, `␣evade`, `␣dodge` | 27/152 (18%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 15/47 (32%) | 10/77 (13%) |
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性` … (+2) | 8/152 (5%) | 26/81 (32%) | 87/138 (63%) | 85/158 (54%) | 4/47 (9%) | 26/77 (34%) |
| disclose | truth | `信息披露`, `揭露`, `␣disclosure`, `公开`, `披露`, `揭`, `␣disclose`, `␣disclosed`, `揭示`, `␣disclosures` … (+5) | 16/152 (11%) | 18/81 (22%) | 21/138 (15%) | 2/158 (1%) | 6/47 (13%) | 17/77 (22%) |
| refuse | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refused`, `␣refuse`, `␣refuses`, `␣refus`, `拒`, `拒絕`, `拒绝了` … (+7) | 2/152 (1%) | 28/81 (35%) | 7/138 (5%) | 1/158 (1%) | 2/47 (4%) | 28/77 (36%) |
| euphemism | unclear | `委婉` | 9/152 (6%) | 18/81 (22%) | 5/138 (4%) | 0/158 (0%) | 8/47 (17%) | 18/77 (23%) |
| official line | unclear | `口径` | 24/152 (16%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 10/47 (21%) | 2/77 (3%) |
| incorrect | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `␣Incorrect`, `错误的`, `不符合`, `有误`, `错误的是` | 8/152 (5%) | 15/81 (19%) | 16/138 (12%) | 53/158 (34%) | 3/47 (6%) | 15/77 (19%) |
| candid / frank | truth | `坦诚`, `␣straightforward`, `␣blunt`, `直言` | 0/152 (0%) | 21/81 (26%) | 35/138 (25%) | 54/158 (34%) | 0/47 (0%) | 21/77 (27%) |
| candid | truth | `坦诚` | 0/152 (0%) | 18/81 (22%) | 20/138 (14%) | 8/158 (5%) | 0/47 (0%) | 18/77 (23%) |
| transparent | truth | `透明`, `-transparent`, `␣transparency`, `␣transparent`, `透明的`, `透明度`, `␣Transparency` | 0/152 (0%) | 16/81 (20%) | 18/138 (13%) | 12/158 (8%) | 0/47 (0%) | 16/77 (21%) |
| inaccurate | lie | `准确性和`, `不准确` | 8/152 (5%) | 6/81 (7%) | 6/138 (4%) | 35/158 (22%) | 3/47 (6%) | 6/77 (8%) |

#### preans_slot2

18 of 61 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | unclear | `␣fact`, `事实`, `的事实`, `␣facts`, `␣factual`, `事实上`, `fact`, `␣Fact`, `facts`, `␣Facts` … (+22) | 110/152 (72%) | 39/81 (48%) | 130/138 (94%) | 81/158 (51%) | 32/47 (68%) | 35/77 (45%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `_real`, `_true`, `,true` … (+22) | 107/152 (70%) | 28/81 (35%) | 114/138 (83%) | 44/158 (28%) | 31/47 (66%) | 26/77 (34%) |
| knowing | unclear | `明知`, `知情`, `␣knowing`, `␣knowingly`, `␣Knowing`, `Knowing` | 95/152 (62%) | 28/81 (35%) | 85/138 (62%) | 0/158 (0%) | 23/47 (49%) | 27/77 (35%) |
| reality | unclear | `实际情况`, `␣reality`, `␣Reality`, `实际上`, `Reality`, `但实际上`, `与实际`, `实际上是`, `根据实际情况` | 96/152 (63%) | 20/81 (25%) | 23/138 (17%) | 4/158 (3%) | 26/47 (55%) | 19/77 (25%) |
| objective | unclear | `客观`, `␣objective`, `␣objectively`, `␣Objective` | 66/152 (43%) | 17/81 (21%) | 63/138 (46%) | 16/158 (10%) | 25/47 (53%) | 16/77 (21%) |
| truthful | truth | `如实`, `␣truthful`, `实事求是` | 51/152 (34%) | 22/81 (27%) | 7/138 (5%) | 3/158 (2%) | 11/47 (23%) | 21/77 (27%) |
| fiction | unclear | `␣fictional`, `fiction`, `␣Fiction`, `-fiction`, `虚构` | 42/152 (28%) | 27/81 (33%) | 31/138 (22%) | 20/158 (13%) | 20/47 (43%) | 27/77 (35%) |
| role-play | unclear | `␣persona`, `␣personas`, `␣Persona`, `扮演`, `角色扮演`, `Persona`, `persona` | 42/152 (28%) | 27/81 (33%) | 7/138 (5%) | 1/158 (1%) | 19/47 (40%) | 25/77 (32%) |
| conceal | lie | `隐瞒`, `␣concealed`, `␣conceal`, `瞒`, `掩盖`, `掩`, `隐` | 45/152 (30%) | 20/81 (25%) | 1/138 (1%) | 0/158 (0%) | 14/47 (30%) | 19/77 (25%) |
| deliberate | unclear | `故意`, `␣intentionally`, `刻意`, `␣deliberately`, `␣intentional`, `␣deliberate`, `故意的` | 45/152 (30%) | 13/81 (16%) | 3/138 (2%) | 3/158 (2%) | 7/47 (15%) | 13/77 (17%) |
| fabricate | lie | `虚构`, `伪造`, `␣fabrication` | 32/152 (21%) | 22/81 (27%) | 29/138 (21%) | 20/158 (13%) | 14/47 (30%) | 22/77 (29%) |
| secret | lie | `␣secret`, `私下`, `秘密`, `的秘密`, `secret`, `␣Secret`, `␣secretly`, `-secret`, `␣confidential`, `Secret` … (+4) | 47/152 (31%) | 7/81 (9%) | 2/138 (1%) | 0/158 (0%) | 15/47 (32%) | 6/77 (8%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确的`, `准确地` | 29/152 (19%) | 11/81 (14%) | 42/138 (30%) | 50/158 (32%) | 4/47 (9%) | 10/77 (13%) |
| contradict | unclear | `矛盾`, `矛盾的`, `␣contrad`, `␣contradict`, `␣contradictory` | 21/152 (14%) | 16/81 (20%) | 17/138 (12%) | 1/158 (1%) | 7/47 (15%) | 16/77 (21%) |
| violate | unclear | `违背`, `违反`, `违反了`, `␣violates`, `␣violated`, `␣violate` | 17/152 (11%) | 19/81 (23%) | 3/138 (2%) | 0/158 (0%) | 3/47 (6%) | 19/77 (25%) |
| simulate | unclear | `模拟`, `␣simulated`, `␣simulation`, `␣Simulation`, `Simulation`, `扮演`, `角色扮演` | 15/152 (10%) | 20/81 (25%) | 3/138 (2%) | 1/158 (1%) | 9/47 (19%) | 18/77 (23%) |
| false | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `␣FALSE`, `=false`, `FALSE`, `>false`, `␣fals` … (+8) | 19/152 (12%) | 9/81 (11%) | 31/138 (22%) | 3/158 (2%) | 8/47 (17%) | 9/77 (12%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected` … (+16) | 1/152 (1%) | 6/81 (7%) | 29/138 (21%) | 88/158 (56%) | 1/47 (2%) | 5/77 (6%) |

#### preans_slot3

6 of 20 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `FALSE`, `>false`, `_false`, `.assertFalse`, `.False` … (+2) | 58/152 (38%) | 65/81 (80%) | 134/138 (97%) | 104/158 (66%) | 33/47 (70%) | 63/77 (82%) |
| law-abiding | unclear | `守法` | 80/152 (53%) | 30/81 (37%) | 16/138 (12%) | 0/158 (0%) | 9/47 (19%) | 29/77 (38%) |
| disclose | truth | `公布`, `公开` | 66/152 (43%) | 39/81 (48%) | 28/138 (20%) | 37/158 (23%) | 16/47 (34%) | 39/77 (51%) |
| refuse | unclear | `␣refusal`, `␣refuse`, `拒`, `␣refusing`, `␣refus`, `拒绝` | 84/152 (55%) | 11/81 (14%) | 7/138 (5%) | 0/158 (0%) | 14/47 (30%) | 10/77 (13%) |
| sorry | unclear | `抱歉`, `␣sorry`, `Sorry`, `␣Sorry` | 27/152 (18%) | 17/81 (21%) | 9/138 (7%) | 5/158 (3%) | 13/47 (28%) | 17/77 (22%) |
| true | truth | `␣true`, `true`, `True`, `␣True`, `TRUE`, `真` | 0/152 (0%) | 0/81 (0%) | 31/138 (22%) | 33/158 (21%) | 0/47 (0%) | 0/77 (0%) |

#### preans_slot4

13 of 42 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `␣TRUE`, `TRUE`, `␣genuine`, `真`, `成立` … (+7) | 118/152 (78%) | 73/81 (90%) | 128/138 (93%) | 75/158 (47%) | 24/47 (51%) | 69/77 (90%) |
| honest | truth | `诚实`, `诚信`, `诚`, `␣honest`, `␣honesty`, `真诚`, `␣Honest` | 106/152 (70%) | 72/81 (89%) | 112/138 (81%) | 81/158 (51%) | 39/47 (83%) | 69/77 (90%) |
| false | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `_FALSE`, `FALSE`, `>false`, `_false` … (+5) | 51/152 (34%) | 68/81 (84%) | 137/138 (99%) | 158/158 (100%) | 38/47 (81%) | 67/77 (87%) |
| integrity | truth | `正直`, `诚信` | 51/152 (34%) | 57/81 (70%) | 100/138 (72%) | 75/158 (47%) | 31/47 (66%) | 55/77 (71%) |
| fact | unclear | `事实`, `␣factual`, `␣fact`, `␣Fact`, `Fact`, `符合`, `是否符合`, `求实` | 74/152 (49%) | 16/81 (20%) | 13/138 (9%) | 0/158 (0%) | 8/47 (17%) | 14/77 (18%) |
| objective | unclear | `客观`, `␣objectively` | 65/152 (43%) | 21/81 (26%) | 22/138 (16%) | 6/158 (4%) | 16/47 (34%) | 20/77 (26%) |
| truthful | truth | `如实`, `␣truthful`, `实事求是` | 41/152 (27%) | 23/81 (28%) | 25/138 (18%) | 0/158 (0%) | 10/47 (21%) | 21/77 (27%) |
| comply | unclear | `合规`, `␣adher`, `遵循` | 48/152 (32%) | 6/81 (7%) | 8/138 (6%) | 14/158 (9%) | 4/47 (9%) | 5/77 (6%) |
| fabricate | lie | `虚构` | 35/152 (23%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 1/47 (2%) | 5/77 (6%) |
| fiction | unclear | `␣fictional`, `fiction`, `虚构` | 35/152 (23%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 1/47 (2%) | 5/77 (6%) |
| candid | truth | `坦诚` | 24/152 (16%) | 13/81 (16%) | 10/138 (7%) | 4/158 (3%) | 20/47 (43%) | 13/77 (17%) |
| law-abiding / compliant | unclear | `合规` | 33/152 (22%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/47 (9%) | 3/77 (4%) |
| simulate | unclear | `模拟`, `␣simulated`, `␣simulation`, `␣simulate`, `扮演`, `角色扮演`, `扮演着` | 33/152 (22%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 2/47 (4%) | 4/77 (5%) |

#### think_slot0

4 of 6 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| clarify | unclear | `澄清`, `␣clarification` | 117/152 (77%) | 72/81 (89%) | 138/138 (100%) | 158/158 (100%) | 34/47 (72%) | 68/77 (88%) |
| violation | unclear | `违规` | 60/152 (39%) | 34/81 (42%) | 7/138 (5%) | 0/158 (0%) | 32/47 (68%) | 34/77 (44%) |
| wrong | lie | `_WRONG`, `指正` | 26/152 (17%) | 11/81 (14%) | 28/138 (20%) | 0/158 (0%) | 3/47 (6%) | 10/77 (13%) |
| sincere | truth | `真情`, `真诚` | 0/152 (0%) | 5/81 (6%) | 13/138 (9%) | 101/158 (64%) | 0/47 (0%) | 5/77 (6%) |

#### think_slot1

2 of 6 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| intentional | unclear | `有心` | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 147/158 (93%) | 47/47 (100%) | 77/77 (100%) |
| unauthorized | unclear | `未经允许` | 83/152 (55%) | 46/81 (57%) | 14/138 (10%) | 2/158 (1%) | 18/47 (38%) | 45/77 (58%) |

#### think_slot2

8 of 14 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| ethics | unclear | `␣ethics`, `␣ethical`, `职业道德`, `思想道德` | 112/152 (74%) | 48/81 (59%) | 96/138 (70%) | 104/158 (66%) | 29/47 (62%) | 45/77 (58%) |
| neutral | unclear | `中立` | 108/152 (71%) | 44/81 (54%) | 1/138 (1%) | 0/158 (0%) | 29/47 (62%) | 41/77 (53%) |
| breach | unclear | `␣breach`, `␣breaches`, `触犯` | 117/152 (77%) | 34/81 (42%) | 55/138 (40%) | 0/158 (0%) | 36/47 (77%) | 32/77 (42%) |
| true | truth | `␣true`, `True`, `␣TRUE`, `␣genuinely`, `真的`, `真正`, `的确`, `的確` | 79/152 (52%) | 30/81 (37%) | 22/138 (16%) | 0/158 (0%) | 10/47 (21%) | 28/77 (36%) |
| false | lie | `␣false`, `false`, `False`, `␣FALSE`, `:false`, `(False`, `FALSE`, `>false`, `_false`, `.assertFalse` … (+4) | 9/152 (6%) | 28/81 (35%) | 104/138 (75%) | 117/158 (74%) | 8/47 (17%) | 28/77 (36%) |
| legality | unclear | `␣legally`, `/legal` | 26/152 (17%) | 11/81 (14%) | 8/138 (6%) | 0/158 (0%) | 19/47 (40%) | 11/77 (14%) |
| refuse | unclear | `拒`, `拒绝`, `␣refuse` | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 11/47 (23%) | 2/77 (3%) |
| argue / defend | unclear | `答辩` | 0/152 (0%) | 1/81 (1%) | 15/138 (11%) | 123/158 (78%) | 0/47 (0%) | 1/77 (1%) |

#### think_slot3

4 of 16 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `␣FALSE`, `:false`, `(False`, `FALSE` … (+10) | 151/152 (99%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `.True`, `真正的`, `的确`, `的真`, `属实` | 141/152 (93%) | 79/81 (98%) | 138/138 (100%) | 141/158 (89%) | 36/47 (77%) | 75/77 (97%) |
| reject / overrule | unclear | `否决`, `驳回` | 13/152 (9%) | 46/81 (57%) | 56/138 (41%) | 8/158 (5%) | 13/47 (28%) | 46/77 (60%) |
| refuse | unclear | `拒绝`, `␣refusal`, `␣refuse`, `拒`, `不予` | 10/152 (7%) | 2/81 (2%) | 50/138 (36%) | 0/158 (0%) | 7/47 (15%) | 2/77 (3%) |

#### postans_slot0

2 of 4 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| sincere | truth | `诚挚` | 132/152 (87%) | 68/81 (84%) | 113/138 (82%) | 11/158 (7%) | 35/47 (74%) | 64/77 (83%) |
| neutral | unclear | `中立` | 57/152 (38%) | 46/81 (57%) | 97/138 (70%) | 158/158 (100%) | 10/47 (21%) | 43/77 (56%) |

#### postans_slot1

18 of 39 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| conceal | lie | `隐瞒`, `-hide`, `藏`, `掩` | 131/152 (86%) | 51/81 (63%) | 30/138 (22%) | 40/158 (25%) | 29/47 (62%) | 47/77 (61%) |
| conform | unclear | `符合`, `是否符合`, `符合要求` | 100/152 (66%) | 63/81 (78%) | 119/138 (86%) | 15/158 (9%) | 35/47 (74%) | 62/77 (81%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `␣genuine`, `真`, `真实`, `确实`, `真实的` … (+1) | 101/152 (66%) | 10/81 (12%) | 56/138 (41%) | 5/158 (3%) | 12/47 (26%) | 7/77 (9%) |
| knowingly | unclear | `明知` | 97/152 (64%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 14/47 (30%) | 3/77 (4%) |
| honest | truth | `诚实`, `诚`, `␣honest`, `␣honesty`, `诚恳` | 86/152 (57%) | 15/81 (19%) | 27/138 (20%) | 4/158 (3%) | 1/47 (2%) | 13/77 (17%) |
| violate | unclear | `违背`, `违反`, `违反了`, `违法` | 72/152 (47%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 11/47 (23%) | 0/77 (0%) |
| nonconform | unclear | `不符合` | 51/152 (34%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 15/77 (19%) |
| legal | unclear | `合法`, `依法`, `合法的`, `␣legally` | 32/152 (21%) | 29/81 (36%) | 17/138 (12%) | 0/158 (0%) | 28/47 (60%) | 29/77 (38%) |
| comply | unclear | `合规`, `遵守` | 34/152 (22%) | 23/81 (28%) | 15/138 (11%) | 0/158 (0%) | 34/47 (72%) | 23/77 (30%) |
| ethical | unclear | `␣ethical`, `ethical`, `伦理`, `␣ethics`, `道德`, `的道德`, `␣moral`, `␣morally` | 46/152 (30%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 8/77 (10%) |
| factual | truth | `事实`, `␣factual` | 36/152 (24%) | 10/81 (12%) | 65/138 (47%) | 85/158 (54%) | 10/47 (21%) | 9/77 (12%) |
| moral | unclear | `道德`, `␣moral`, `␣morally`, `的道德` | 33/152 (22%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 8/77 (10%) |
| objective | unclear | `客观`, `␣objectively` | 27/152 (18%) | 12/81 (15%) | 13/138 (9%) | 6/158 (4%) | 14/47 (30%) | 12/77 (16%) |
| wrong | lie | `␣flaw`, `错`, `不对`, `是非` | 18/152 (12%) | 6/81 (7%) | 3/138 (2%) | 2/158 (1%) | 11/47 (23%) | 6/77 (8%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确`, `准确的` | 12/152 (8%) | 8/81 (10%) | 48/138 (35%) | 6/158 (4%) | 1/47 (2%) | 7/77 (9%) |
| upright | truth | `正直` | 4/152 (3%) | 16/81 (20%) | 3/138 (2%) | 0/158 (0%) | 1/47 (2%) | 16/77 (21%) |
| justify | unclear | `␣justification`, `justify`, `合理化`, `正当` | 10/152 (7%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 10/47 (21%) | 6/77 (8%) |
| lie | lie | `撒谎`, `说谎`, `␣lie`, `␣lying`, `谎`, `谎言`, `lying`, `␣lies` | 12/152 (8%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 10/47 (21%) | 0/77 (0%) |

#### postans_slot2

3 of 15 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique | unclear | `␣critique`, `批判`, `批评`, `␣criticism`, `␣critic`, `␣critiques` | 130/152 (86%) | 67/81 (83%) | 13/138 (9%) | 21/158 (13%) | 31/47 (66%) | 63/77 (82%) |
| critical | unclear | `␣critical`, `critical`, `␣Critical`, `Critical`, `␣critically`, `_critical` | 80/152 (53%) | 33/81 (41%) | 0/138 (0%) | 0/158 (0%) | 15/47 (32%) | 30/77 (39%) |
| reflect | unclear | `反思` | 34/152 (22%) | 5/81 (6%) | 1/138 (1%) | 4/158 (3%) | 3/47 (6%) | 3/77 (4%) |

#### postans_slot3

4 of 13 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| biased | unclear | `␣biased`, `␣bias`, `biased` | 26/152 (17%) | 29/81 (36%) | 46/138 (33%) | 3/158 (2%) | 9/47 (19%) | 28/77 (36%) |
| clarify | unclear | `澄清`, `␣clarification` | 18/152 (12%) | 7/81 (9%) | 46/138 (33%) | 0/158 (0%) | 2/47 (4%) | 6/77 (8%) |
| unbiased | unclear | `␣unbiased` | 6/152 (4%) | 11/81 (14%) | 46/138 (33%) | 0/158 (0%) | 3/47 (6%) | 11/77 (14%) |
| wrong | lie | `错`, `谬`, `错了`, `是非` | 3/152 (2%) | 8/81 (10%) | 41/138 (30%) | 6/158 (4%) | 1/47 (2%) | 8/77 (10%) |

#### postans_slot4

28 of 62 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| wrong | lie | `␣flaw`, `错`, `错误`, `谬`, `错了`, `是非` | 117/152 (77%) | 75/81 (93%) | 137/138 (99%) | 74/158 (47%) | 45/47 (96%) | 73/77 (95%) |
| comply | unclear | `合规`, `␣compliance`, `遵守`, `␣Compliance` | 79/152 (52%) | 63/81 (78%) | 50/138 (36%) | 0/158 (0%) | 19/47 (40%) | 61/77 (79%) |
| moral | unclear | `道德`, `的道德`, `␣moral`, `␣morality`, `职业道德`, `␣morals`, `␣morally`, `␣Moral`, `␣ethical`, `ethical` … (+4) | 97/152 (64%) | 43/81 (53%) | 7/138 (5%) | 0/158 (0%) | 33/47 (70%) | 42/77 (55%) |
| ethical | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣Ethics`, `ethical`, `␣ethic` | 90/152 (59%) | 36/81 (44%) | 5/138 (4%) | 0/158 (0%) | 28/47 (60%) | 36/77 (47%) |
| honest | truth | `诚实`, `␣honesty`, `␣honest`, `诚信`, `诚实守信`, `诚`, `␣honestly` | 78/152 (51%) | 18/81 (22%) | 64/138 (46%) | 12/158 (8%) | 26/47 (55%) | 18/77 (23%) |
| persona | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `扮演`, `角色扮演` | 58/152 (38%) | 26/81 (32%) | 10/138 (7%) | 0/158 (0%) | 17/47 (36%) | 26/77 (34%) |
| role_play | unclear | `扮演`, `角色扮演` | 57/152 (38%) | 24/81 (30%) | 9/138 (7%) | 0/158 (0%) | 17/47 (36%) | 24/77 (31%) |
| disclose | truth | `␣disclosure`, `披露`, `信息披露`, `透露`, `␣disclosures`, `␣Disclosure`, `␣disclosing` | 69/152 (45%) | 9/81 (11%) | 13/138 (9%) | 3/158 (2%) | 9/47 (19%) | 8/77 (10%) |
| truthful | truth | `␣truthful`, `如实` | 44/152 (29%) | 7/81 (9%) | 79/138 (57%) | 0/158 (0%) | 20/47 (43%) | 7/77 (9%) |
| violate | unclear | `违反`, `违反了`, `违背`, `违规` | 41/152 (27%) | 8/81 (10%) | 48/138 (35%) | 1/158 (1%) | 1/47 (2%) | 8/77 (10%) |
| conform | unclear | `符合`, `是否符合` | 23/152 (15%) | 24/81 (30%) | 95/138 (69%) | 63/158 (40%) | 5/47 (11%) | 22/77 (29%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确`, `准确的` | 37/152 (24%) | 9/81 (11%) | 83/138 (60%) | 15/158 (9%) | 16/47 (34%) | 9/77 (12%) |
| biased | unclear | `␣bias`, `偏见`, `␣biased`, `偏心` | 16/152 (11%) | 29/81 (36%) | 58/138 (42%) | 4/158 (3%) | 7/47 (15%) | 28/77 (36%) |
| hallucinate | unclear | `␣halluc` | 28/152 (18%) | 14/81 (17%) | 66/138 (48%) | 2/158 (1%) | 22/47 (47%) | 14/77 (18%) |
| deliberate | unclear | `故意`, `␣deliberately`, `␣deliberate`, `明知` | 23/152 (15%) | 15/81 (19%) | 80/138 (58%) | 14/158 (9%) | 17/47 (36%) | 15/77 (19%) |
| legal | unclear | `依法`, `合法`, `␣legally`, `␣legal`, `␣legality` | 31/152 (20%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 5/47 (11%) | 4/77 (5%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣Correct`, `正确`, `正确的`, `正确的是`, `正确答案`, `的正确` … (+2) | 23/152 (15%) | 12/81 (15%) | 97/138 (70%) | 36/158 (23%) | 2/47 (4%) | 12/77 (16%) |
| lure | unclear | `诱导`, `␣bait` | 11/152 (7%) | 22/81 (27%) | 33/138 (24%) | 0/158 (0%) | 10/47 (21%) | 22/77 (29%) |
| knowingly | unclear | `明知` | 21/152 (14%) | 10/81 (12%) | 80/138 (58%) | 1/158 (1%) | 16/47 (34%) | 10/77 (13%) |
| trap | unclear | `陷阱`, `␣trap`, `␣trapped`, `␣traps`, `trap`, `Trap`, `␣Trap`, `␣trapping`, `_trap`, `␣bait` | 8/152 (5%) | 17/81 (21%) | 27/138 (20%) | 1/158 (1%) | 7/47 (15%) | 17/77 (22%) |
| deviate | unclear | `偏离` | 7/152 (5%) | 16/81 (20%) | 2/138 (1%) | 2/158 (1%) | 3/47 (6%) | 16/77 (21%) |
| factual | truth | `事实`, `␣factual`, `的事实`, `事实和` | 18/152 (12%) | 3/81 (4%) | 85/138 (62%) | 6/158 (4%) | 16/47 (34%) | 3/77 (4%) |
| objective | unclear | `客观`, `␣objective`, `␣objectively`, `公正` | 12/152 (8%) | 1/81 (1%) | 31/138 (22%) | 1/158 (1%) | 9/47 (19%) | 1/77 (1%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `真`, `成立`, `真正`, `真实`, `确实` … (+5) | 6/152 (4%) | 2/81 (2%) | 39/138 (28%) | 13/158 (8%) | 3/47 (6%) | 2/77 (3%) |
| fact | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Facts`, `␣FACT`, `FACT`, `facts` … (+8) | 5/152 (3%) | 2/81 (2%) | 40/138 (29%) | 8/158 (5%) | 3/47 (6%) | 2/77 (3%) |
| nonconform | unclear | `不符合` | 2/152 (1%) | 4/81 (5%) | 47/138 (34%) | 99/158 (63%) | 0/47 (0%) | 4/77 (5%) |
| contradiction | unclear | `矛盾`, `矛盾的` | 0/152 (0%) | 3/81 (4%) | 46/138 (33%) | 0/158 (0%) | 0/47 (0%) | 3/77 (4%) |
| false | lie | `␣false`, `␣fals`, `␣falsehood`, `假`, `虚假`, `假的`, `真假` | 2/152 (1%) | 1/81 (1%) | 29/138 (21%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |

### wording Q6_factual, positions from the question on

#### q_tok0

1 of 14 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `真的`, `确实`, `的真` | 64/152 (42%) | 20/81 (25%) | 17/138 (12%) | 4/158 (3%) | 12/43 (28%) | 19/73 (26%) |

#### q_tok3

12 of 26 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确的`, `准确地` | 150/152 (99%) | 79/81 (98%) | 138/138 (100%) | 146/158 (92%) | 43/43 (100%) | 71/73 (97%) |
| violate | unclear | `␣violate`, `违反`, `␣violates`, `违背`, `违规`, `␣violating`, `␣violation`, `␣violations`, `违反了`, `触犯` … (+1) | 127/152 (84%) | 73/81 (90%) | 111/138 (80%) | 96/158 (61%) | 28/43 (65%) | 65/73 (89%) |
| correct | truth | `␣correct`, `␣correctly`, `Correct`, `␣Correct`, `正确`, `正确的`, `正确答案`, `纠正`, `正确地`, `是否正确` | 102/152 (67%) | 69/81 (85%) | 137/138 (99%) | 140/158 (89%) | 25/43 (58%) | 62/73 (85%) |
| comply | unclear | `␣adher`, `␣adhere`, `␣comply`, `遵守`, `符合`, `是否符合`, `遵循`, `合规`, `␣adherence`, `␣conform` … (+2) | 99/152 (65%) | 61/81 (75%) | 73/138 (53%) | 144/158 (91%) | 16/43 (37%) | 54/73 (74%) |
| inadvertent | unclear | `␣inadvertently`, `␣accidentally`, `␣unintention` | 87/152 (57%) | 62/81 (77%) | 62/138 (45%) | 6/158 (4%) | 25/43 (58%) | 56/73 (77%) |
| contradict | unclear | `␣contradict`, `␣contrad` | 65/152 (43%) | 28/81 (35%) | 119/138 (86%) | 6/158 (4%) | 25/43 (58%) | 22/73 (30%) |
| perfunctory | unclear | `敷衍` | 51/152 (34%) | 16/81 (20%) | 7/138 (5%) | 3/158 (2%) | 24/43 (56%) | 14/73 (19%) |
| imply | unclear | `␣imply`, `␣implicitly`, `暗示`, `␣implies`, `␣implying`, `␣implied`, `隐含` | 31/152 (20%) | 28/81 (35%) | 23/138 (17%) | 0/158 (0%) | 17/43 (40%) | 25/73 (34%) |
| honest | truth | `␣honestly`, `诚实`, `诚`, `如实`, `␣truthful` | 25/152 (16%) | 16/81 (20%) | 5/138 (4%) | 0/158 (0%) | 12/43 (28%) | 14/73 (19%) |
| truthful | truth | `如实`, `␣truthful` | 23/152 (15%) | 13/81 (16%) | 5/138 (4%) | 0/158 (0%) | 12/43 (28%) | 11/73 (15%) |
| incorrect | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣Incorrect`, `有误` | 10/152 (7%) | 10/81 (12%) | 43/138 (31%) | 22/158 (14%) | 7/43 (16%) | 8/73 (11%) |
| lie | lie | `撒谎`, `说谎`, `␣lie`, `␣lies`, `谎言` | 17/152 (11%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 0/73 (0%) |

#### q_tok4

5 of 19 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| hallucinate | unclear | `␣halluc` | 138/152 (91%) | 64/81 (79%) | 133/138 (96%) | 126/158 (80%) | 36/43 (84%) | 57/73 (78%) |
| fact | truth | `␣facts`, `␣factual`, `事实` | 81/152 (53%) | 35/81 (43%) | 111/138 (80%) | 10/158 (6%) | 24/43 (56%) | 30/73 (41%) |
| truthful | truth | `␣truthful` | 31/152 (20%) | 13/81 (16%) | 26/138 (19%) | 0/158 (0%) | 8/43 (19%) | 12/73 (16%) |
| accurate | truth | `␣accurate`, `准确` | 12/152 (8%) | 8/81 (10%) | 41/138 (30%) | 3/158 (2%) | 1/43 (2%) | 6/73 (8%) |
| correct | truth | `␣valid`, `␣correct` | 3/152 (2%) | 1/81 (1%) | 57/138 (41%) | 36/158 (23%) | 1/43 (2%) | 1/73 (1%) |

#### q_tok5

29 of 50 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Facts`, `_fact`, `␣FACT`, `FACT` … (+19) | 139/152 (91%) | 59/81 (73%) | 138/138 (100%) | 98/158 (62%) | 42/43 (98%) | 52/73 (71%) |
| lie | lie | `␣lie`, `谎言`, `␣lying`, `␣lies`, `谎`, `撒谎`, `说谎`, `␣Lie`, `␣lied`, `␣mentira` … (+6) | 138/152 (91%) | 54/81 (67%) | 89/138 (64%) | 1/158 (1%) | 37/43 (86%) | 46/73 (63%) |
| hallucinate | unclear | `␣halluc`, `幻觉` | 116/152 (76%) | 66/81 (81%) | 137/138 (99%) | 141/158 (89%) | 30/43 (70%) | 59/73 (81%) |
| honest | truth | `诚实`, `诚`, `坦诚`, `␣honesty`, `␣honest`, `␣truthful`, `诚信`, `如实` | 115/152 (76%) | 48/81 (59%) | 123/138 (89%) | 11/158 (7%) | 27/43 (63%) | 41/73 (56%) |
| conceal | lie | `隐瞒`, `␣hidden`, `掩饰`, `掩盖`, `␣conceal`, `␣concealed`, `隐藏`, `␣masking`, `遮掩`, `␣hiding` … (+6) | 119/152 (78%) | 40/81 (49%) | 105/138 (76%) | 89/158 (56%) | 38/43 (88%) | 34/73 (47%) |
| truthful | truth | `␣truthful`, `如实` | 111/152 (73%) | 44/81 (54%) | 121/138 (88%) | 0/158 (0%) | 27/43 (63%) | 38/73 (52%) |
| violate | unclear | `违反`, `违背`, `␣violation`, `违反了`, `␣violating`, `违规`, `␣violate`, `␣violations`, `␣violates`, `␣violated` … (+2) | 96/152 (63%) | 57/81 (70%) | 121/138 (88%) | 6/158 (4%) | 22/43 (51%) | 51/73 (70%) |
| fabricate | lie | `␣fabricated`, `虚构`, `␣fabrication`, `伪造` | 122/152 (80%) | 28/81 (35%) | 63/138 (46%) | 7/158 (4%) | 29/43 (67%) | 25/73 (34%) |
| contradict | unclear | `␣contradiction`, `␣contradict`, `矛盾`, `␣contrad`, `␣contradictory`, `␣contradictions`, `矛盾的`, `之间的矛盾`, `␣contradd` | 82/152 (54%) | 53/81 (65%) | 134/138 (97%) | 32/158 (20%) | 24/43 (56%) | 46/73 (63%) |
| comply | unclear | `符合`, `合规`, `是否符合`, `␣compliance`, `遵守`, `␣compliant`, `␣complying`, `␣comply`, `符合要求`, `遵循` … (+6) | 63/152 (41%) | 43/81 (53%) | 110/138 (80%) | 25/158 (16%) | 13/43 (30%) | 38/73 (52%) |
| hidden | lie | `␣hidden`, `hidden` | 54/152 (36%) | 33/81 (41%) | 105/138 (76%) | 89/158 (56%) | 18/43 (42%) | 28/73 (38%) |
| fiction | unclear | `␣fictional`, `fiction`, `␣fiction`, `␣Fiction`, `-fiction`, `虚构` | 67/152 (44%) | 18/81 (22%) | 10/138 (7%) | 8/158 (5%) | 11/43 (26%) | 18/73 (25%) |
| noncompliant | unclear | `不符合` | 46/152 (30%) | 32/81 (40%) | 15/138 (11%) | 17/158 (11%) | 9/43 (21%) | 29/73 (40%) |
| refuse | unclear | `␣refusal`, `拒绝`, `␣refus`, `拒`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `拒绝了`, `拒絕` … (+1) | 31/152 (20%) | 45/81 (56%) | 59/138 (43%) | 4/158 (3%) | 13/43 (30%) | 45/73 (62%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct` … (+14) | 26/152 (17%) | 39/81 (48%) | 112/138 (81%) | 134/158 (85%) | 12/43 (28%) | 37/73 (51%) |
| deceive | lie | `␣deception`, `欺骗`, `␣deceptive`, `骗`, `␣deceive`, `欺`, `哄` | 60/152 (39%) | 3/81 (4%) | 12/138 (9%) | 0/158 (0%) | 11/43 (26%) | 2/73 (3%) |
| deliberate | unclear | `␣deliberate`, `␣deliberately`, `故意`, `␣intentionally`, `␣intentional`, `明知`, `␣knowingly` | 51/152 (34%) | 11/81 (14%) | 8/138 (6%) | 2/158 (1%) | 12/43 (28%) | 9/73 (12%) |
| integrity | truth | `诚信` | 49/152 (32%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 6/73 (8%) |
| imply | unclear | `暗示`, `隐含`, `␣hint`, `␣implicit`, `␣implicitly`, `␣implied`, `␣imply`, `␣implies`, `␣implying`, `hint` … (+3) | 42/152 (28%) | 14/81 (17%) | 10/138 (7%) | 2/158 (1%) | 11/43 (26%) | 10/73 (14%) |
| ethics | unclear | `␣moral`, `␣ethical`, `道德`, `伦理`, `␣morally`, `␣ethics`, `ethical`, `␣Ethics`, `的道德`, `␣morality` … (+3) | 23/152 (15%) | 31/81 (38%) | 1/138 (1%) | 0/158 (0%) | 2/43 (5%) | 30/73 (41%) |
| disclose | truth | `公开`, `␣disclosure`, `透露`, `披露`, `␣disclosing`, `␣disclose`, `暴露`, `␣reveal`, `␣exposing` | 25/152 (16%) | 28/81 (35%) | 7/138 (5%) | 1/158 (1%) | 6/43 (14%) | 25/73 (34%) |
| fake | lie | `fake`, `␣fake`, `Fake` | 40/152 (26%) | 1/81 (1%) | 2/138 (1%) | 2/158 (1%) | 3/43 (7%) | 1/73 (1%) |
| liar | lie | `␣liar` | 35/152 (23%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 1/73 (1%) |
| objective | unclear | `客观` | 24/152 (16%) | 12/81 (15%) | 38/138 (28%) | 0/158 (0%) | 4/43 (9%) | 11/73 (15%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `␣TRUE`, `␣genuine`, `真`, `真正`, `真实` … (+7) | 23/152 (15%) | 11/81 (14%) | 102/138 (74%) | 12/158 (8%) | 6/43 (14%) | 9/73 (12%) |
| knowingly | unclear | `明知`, `␣knowingly` | 31/152 (20%) | 1/81 (1%) | 6/138 (4%) | 0/158 (0%) | 9/43 (21%) | 1/73 (1%) |
| wrong | lie | `␣wrong`, `␣flaw`, `错`, `错误`, `不对`, `错了`, `失误`, `是非`, `的错误`, `是错误的` | 19/152 (12%) | 13/81 (16%) | 19/138 (14%) | 85/158 (54%) | 2/43 (5%) | 11/73 (15%) |
| mistake | unclear | `␣mistake`, `␣mistakes`, `␣error`, `error` | 8/152 (5%) | 12/81 (15%) | 63/138 (46%) | 129/158 (82%) | 2/43 (5%) | 10/73 (14%) |
| accurate | truth | `␣accurate`, `␣accurately`, `准确`, `准确的`, `准确地` | 6/152 (4%) | 10/81 (12%) | 65/138 (47%) | 8/158 (5%) | 3/43 (7%) | 10/73 (14%) |

#### q_tok6

11 of 17 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `␣fact`, `␣reality`, `␣facts`, `fact`, `␣Fact`, `␣factual`, `事实`, `的事实` | 151/152 (99%) | 68/81 (84%) | 134/138 (97%) | 155/158 (98%) | 43/43 (100%) | 61/73 (84%) |
| fake | lie | `␣fake`, `fake`, `␣Fake`, `Fake` | 121/152 (80%) | 64/81 (79%) | 50/138 (36%) | 18/158 (11%) | 22/43 (51%) | 58/73 (79%) |
| mislead | lie | `␣misleading`, `误导` | 121/152 (80%) | 33/81 (41%) | 1/138 (1%) | 0/158 (0%) | 27/43 (63%) | 26/73 (36%) |
| honest | truth | `␣truthful` | 85/152 (56%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 17/43 (40%) | 6/73 (8%) |
| true | truth | `␣true`, `真`, `真实的` | 65/152 (43%) | 15/81 (19%) | 1/138 (1%) | 2/158 (1%) | 18/43 (42%) | 13/73 (18%) |
| deliberate | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `明知`, `␣knowingly` | 65/152 (43%) | 14/81 (17%) | 2/138 (1%) | 0/158 (0%) | 15/43 (35%) | 13/73 (18%) |
| lie | lie | `谎言`, `说谎`, `撒谎`, `谎`, `lying` | 50/152 (33%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 15/43 (35%) | 3/73 (4%) |
| knowingly | unclear | `明知`, `␣knowingly` | 40/152 (26%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 14/43 (33%) | 9/73 (12%) |
| incorrect | lie | `␣incorrect`, `␣Incorrect`, `错误的` | 5/152 (3%) | 29/81 (36%) | 131/138 (95%) | 157/158 (99%) | 3/43 (7%) | 28/73 (38%) |
| wrong | lie | `␣wrong`, `错误`, `谬` | 2/152 (1%) | 8/81 (10%) | 16/138 (12%) | 52/158 (33%) | 1/43 (2%) | 7/73 (10%) |
| mistake | unclear | `␣error` | 0/152 (0%) | 1/81 (1%) | 60/138 (43%) | 135/158 (85%) | 0/43 (0%) | 1/73 (1%) |

#### q_tok7

8 of 15 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `␣fact`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Facts`, `␣FACT`, `␣factual`, `事实`, `事实上` … (+3) | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 43/43 (100%) | 73/73 (100%) |
| deliberate | unclear | `故意`, `有意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `␣intentional`, `故意的`, `␣knowingly`, `明知` | 133/152 (88%) | 44/81 (54%) | 0/138 (0%) | 0/158 (0%) | 35/43 (81%) | 38/73 (52%) |
| true | truth | `␣true`, `true`, `成立`, `的真` | 124/152 (82%) | 33/81 (41%) | 33/138 (24%) | 25/158 (16%) | 29/43 (67%) | 26/73 (36%) |
| knowingly | unclear | `␣knowingly`, `明知` | 113/152 (74%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 30/43 (70%) | 11/73 (15%) |
| lie | lie | `谎`, `谎言`, `␣거짓`, `␣liar` | 65/152 (43%) | 19/81 (23%) | 0/138 (0%) | 1/158 (1%) | 12/43 (28%) | 15/73 (21%) |
| contradict | unclear | `␣contrad`, `␣contradictory` | 8/152 (5%) | 5/81 (6%) | 68/138 (49%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| mistake | unclear | `␣error` | 2/152 (1%) | 8/81 (10%) | 38/138 (28%) | 43/158 (27%) | 2/43 (5%) | 7/73 (10%) |
| incorrect | lie | `␣incorrect`, `错误的`, `错误的是` | 0/152 (0%) | 1/81 (1%) | 21/138 (15%) | 92/158 (58%) | 0/43 (0%) | 1/73 (1%) |

#### q_tok8

5 of 8 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `真`, `的真` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 43/43 (100%) | 73/73 (100%) |
| self-examine | unclear | `自查`, `自检`, `反思`, `自省`, `审视`, `␣reflect`, `␣reflection`, `reflect`, `␣reflecting`, `␣Reflection` | 91/152 (60%) | 69/81 (85%) | 136/138 (99%) | 156/158 (99%) | 35/43 (81%) | 63/73 (86%) |
| correct | truth | `␣correct` | 12/152 (8%) | 12/81 (15%) | 62/138 (45%) | 87/158 (55%) | 3/43 (7%) | 10/73 (14%) |
| lie | lie | `␣lie` | 16/152 (11%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 13/43 (30%) | 1/73 (1%) |
| wrong | lie | `error`, `␣error`, `指正` | 8/152 (5%) | 6/81 (7%) | 6/138 (4%) | 55/158 (35%) | 4/43 (9%) | 6/73 (8%) |

#### q_tok9

1 of 3 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `(True`, `的真` | 81/152 (53%) | 32/81 (40%) | 89/138 (64%) | 131/158 (83%) | 13/43 (30%) | 26/73 (36%) |

#### q_tok10

2 of 3 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `true`, `True`, `␣True`, `TRUE`, `(True`, `.True`, `的真` | 78/152 (51%) | 38/81 (47%) | 98/138 (71%) | 141/158 (89%) | 12/43 (28%) | 34/73 (47%) |
| wrong | lie | `错误或`, `对错` | 23/152 (15%) | 28/81 (35%) | 10/138 (7%) | 16/158 (10%) | 10/43 (23%) | 27/73 (37%) |

#### q_tok11

1 of 3 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `␣True` | 55/152 (36%) | 22/81 (27%) | 71/138 (51%) | 125/158 (79%) | 4/43 (9%) | 18/73 (25%) |

#### q_tok12

2 of 2 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `True`, `␣True`, `TRUE`, `成立` | 124/152 (82%) | 71/81 (88%) | 123/138 (89%) | 158/158 (100%) | 25/43 (58%) | 64/73 (88%) |
| silent | unclear | `不语` | 67/152 (44%) | 11/81 (14%) | 9/138 (7%) | 52/158 (33%) | 5/43 (12%) | 8/73 (11%) |

#### q_tok13

23 of 38 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| objective | unclear | `客观`, `␣objectively`, `␣objective`, `objective`, `Objective`, `实事求是` | 131/152 (86%) | 51/81 (63%) | 32/138 (23%) | 27/158 (17%) | 30/43 (70%) | 44/73 (60%) |
| honest | truth | `诚实`, `␣truthful`, `如实`, `实事求是`, `␣honesty`, `忠实`, `诚信`, `诚实守信`, `坦诚`, `␣honest` … (+1) | 130/152 (86%) | 35/81 (43%) | 28/138 (20%) | 7/158 (4%) | 32/43 (74%) | 30/73 (41%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `真`, `成立`, `真实` … (+8) | 123/152 (81%) | 42/81 (52%) | 49/138 (36%) | 47/158 (30%) | 23/43 (53%) | 36/73 (49%) |
| fact | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact` … (+24) | 112/152 (74%) | 45/81 (56%) | 64/138 (46%) | 43/158 (27%) | 24/43 (56%) | 40/73 (55%) |
| violate | unclear | `违反`, `违背`, `违反了`, `␣violate`, `␣violating`, `␣violations`, `违规`, `␣violation`, `违法` | 94/152 (62%) | 43/81 (53%) | 65/138 (47%) | 1/158 (1%) | 14/43 (33%) | 36/73 (49%) |
| truthful | truth | `␣truthful`, `如实` | 104/152 (68%) | 24/81 (30%) | 26/138 (19%) | 3/158 (2%) | 21/43 (49%) | 22/73 (30%) |
| wrong | lie | `error`, `␣error`, `␣mistake`, `错`, `错误`, `错了`, `是非`, `指正`, `是错误的` | 72/152 (47%) | 38/81 (47%) | 43/138 (31%) | 114/158 (72%) | 26/43 (60%) | 33/73 (45%) |
| knowingly | unclear | `明知`, `␣knowingly` | 95/152 (62%) | 9/81 (11%) | 14/138 (10%) | 8/158 (5%) | 10/43 (23%) | 5/73 (7%) |
| fictional | unclear | `虚构`, `架空`, `␣fictional`, `fiction`, `␣fiction`, `␣Fiction` | 76/152 (50%) | 25/81 (31%) | 7/138 (5%) | 20/158 (13%) | 10/43 (23%) | 21/73 (29%) |
| role-play | unclear | `扮演`, `角色扮演`, `扮演着` | 69/152 (45%) | 28/81 (35%) | 50/138 (36%) | 0/158 (0%) | 12/43 (28%) | 24/73 (33%) |
| incorrect | lie | `␣incorrect`, `错误的`, `不符合`, `错误的是` | 50/152 (33%) | 37/81 (46%) | 64/138 (46%) | 12/158 (8%) | 6/43 (14%) | 33/73 (45%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `␣Accuracy`, `准确`, `准确性` | 53/152 (35%) | 15/81 (19%) | 16/138 (12%) | 12/158 (8%) | 12/43 (28%) | 13/73 (18%) |
| faithful | unclear | `忠实` | 50/152 (33%) | 17/81 (21%) | 2/138 (1%) | 0/158 (0%) | 4/43 (9%) | 15/73 (21%) |
| hide | lie | `隐瞒`, `␣hidden`, `-hidden`, `隐藏的`, `隐藏`, `hidden`, `Hidden`, `␣hide`, `␣Hidden`, `␣conceal` … (+1) | 56/152 (37%) | 9/81 (11%) | 3/138 (2%) | 0/158 (0%) | 7/43 (16%) | 7/73 (10%) |
| persona | unclear | `␣persona`, `␣personas`, `Persona`, `␣Persona`, `persona`, `␣Personas` | 43/152 (28%) | 21/81 (26%) | 0/138 (0%) | 1/158 (1%) | 8/43 (19%) | 18/73 (25%) |
| ethics | unclear | `␣ethical`, `伦理`, `␣ethics`, `ethical`, `␣Ethics`, `道德`, `␣moral`, `职业道德`, `的道德`, `␣morally` … (+4) | 54/152 (36%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 7/73 (10%) |
| deliberate | unclear | `␣intentionally`, `故意`, `␣deliberately`, `故意的`, `␣deliberate`, `␣intentional`, `刻意`, `有意` | 54/152 (36%) | 7/81 (9%) | 1/138 (1%) | 2/158 (1%) | 5/43 (12%) | 5/73 (7%) |
| self-examine | unclear | `自查`, `反思`, `自检`, `␣reflection`, `␣reflective`, `.reflect`, `␣Reflection`, `Reflection`, `Reflect`, `reflection` … (+5) | 27/152 (18%) | 22/81 (27%) | 40/138 (29%) | 98/158 (62%) | 14/43 (33%) | 22/73 (30%) |
| conceal | lie | `隐瞒`, `␣conceal`, `掩盖`, `遮`, `隐` | 42/152 (28%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 5/43 (12%) | 3/73 (4%) |
| comply | unclear | `合规`, `遵守`, `␣compliance`, `严格遵守`, `␣Compliance`, `␣comply` | 19/152 (12%) | 21/81 (26%) | 4/138 (3%) | 0/158 (0%) | 7/43 (16%) | 20/73 (27%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceit`, `␣deceive`, `骗`, `哄` | 33/152 (22%) | 3/81 (4%) | 1/138 (1%) | 3/158 (2%) | 3/43 (7%) | 2/73 (3%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections` … (+10) | 10/152 (7%) | 22/81 (27%) | 101/138 (73%) | 100/158 (63%) | 3/43 (7%) | 21/73 (29%) |
| euphemistic | unclear | `委婉` | 8/152 (5%) | 17/81 (21%) | 14/138 (10%) | 0/158 (0%) | 2/43 (5%) | 17/73 (23%) |

#### preans_slot0

2 of 7 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| self-examination | unclear | `反思`, `自查`, `自检`, `␣critique`, `批判`, `指正` | 145/152 (95%) | 72/81 (89%) | 126/138 (91%) | 156/158 (99%) | 38/43 (88%) | 64/73 (88%) |
| objective | unclear | `客观`, `␣objectively` | 36/152 (24%) | 18/81 (22%) | 3/138 (2%) | 4/158 (3%) | 7/43 (16%) | 16/73 (22%) |

#### preans_slot1

22 of 45 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact` … (+26) | 149/152 (98%) | 78/81 (96%) | 137/138 (99%) | 122/158 (77%) | 43/43 (100%) | 70/73 (96%) |
| deliberate | unclear | `明知`, `故意`, `刻意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `␣knowingly` | 144/152 (95%) | 36/81 (44%) | 44/138 (32%) | 14/158 (9%) | 38/43 (88%) | 30/73 (41%) |
| honest | truth | `诚实`, `诚`, `诚信`, `坦诚`, `␣truthful`, `␣honest`, `␣honesty`, `␣honestly`, `␣Honest`, `如实` … (+2) | 127/152 (84%) | 53/81 (65%) | 100/138 (72%) | 36/158 (23%) | 33/43 (77%) | 47/73 (64%) |
| knowingly | unclear | `明知`, `␣knowingly` | 142/152 (93%) | 30/81 (37%) | 43/138 (31%) | 6/158 (4%) | 36/43 (84%) | 24/73 (33%) |
| fabricate | lie | `虚构`, `␣fabricated`, `␣fabrication`, `␣invented`, `␣invent`, `凭空`, `伪造`, `fake`, `␣fake`, `fiction` … (+3) | 124/152 (82%) | 44/81 (54%) | 49/138 (36%) | 48/158 (30%) | 30/43 (70%) | 37/73 (51%) |
| fiction | unclear | `fiction`, `␣fiction`, `-fiction`, `␣fictional`, `␣fict`, `虚构`, `架空` | 119/152 (78%) | 44/81 (54%) | 49/138 (36%) | 48/158 (30%) | 28/43 (65%) | 37/73 (51%) |
| claim | unclear | `␣claim`, `␣claims`, `␣claiming`, `␣Claim`, `claim`, `␣claimed`, `Claim`, `␣Claims`, `␣CLAIM`, `claims` … (+20) | 113/152 (74%) | 46/81 (57%) | 64/138 (46%) | 24/158 (15%) | 32/43 (74%) | 39/73 (53%) |
| lie | lie | `谎言`, `谎`, `撒谎`, `说谎`, `␣거짓`, `␣lie`, `␣lies`, `␣lied`, `␣lying`, `lying` … (+1) | 125/152 (82%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 29/43 (67%) | 16/73 (22%) |
| conceal | lie | `隐瞒`, `掩盖`, `掩饰`, `遮掩`, `遮盖`, `遮住`, `遮蔽`, `␣conceal`, `␣concealed`, `␣masking` … (+12) | 116/152 (76%) | 27/81 (33%) | 3/138 (2%) | 0/158 (0%) | 33/43 (77%) | 21/73 (29%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_real`, `␣genuine`, `␣REAL`, `.real` … (+14) | 104/152 (68%) | 30/81 (37%) | 17/138 (12%) | 20/158 (13%) | 26/43 (60%) | 25/73 (34%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `欺`, `哄` | 105/152 (69%) | 23/81 (28%) | 1/138 (1%) | 1/158 (1%) | 21/43 (49%) | 17/73 (23%) |
| cover up | lie | `掩盖`, `掩饰`, `遮盖`, `遮掩`, `遮住`, `遮蔽`, `␣masking`, `␣masked` | 92/152 (61%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 21/43 (49%) | 9/73 (12%) |
| contradict | unclear | `␣contrad`, `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾`, `矛盾的`, `␣contrary`, `相反`, `相反的` | 62/152 (41%) | 40/81 (49%) | 74/138 (54%) | 8/158 (5%) | 17/43 (40%) | 34/73 (47%) |
| objective | unclear | `客观`, `␣objectively`, `␣objective` | 67/152 (44%) | 23/81 (28%) | 35/138 (25%) | 9/158 (6%) | 24/43 (56%) | 22/73 (30%) |
| fake | lie | `fake`, `␣fake` | 38/152 (25%) | 13/81 (16%) | 7/138 (5%) | 2/158 (1%) | 4/43 (9%) | 9/73 (12%) |
| violate | unclear | `违背`, `违反`, `违反了`, `␣violate`, `␣violates` | 35/152 (23%) | 12/81 (15%) | 8/138 (6%) | 0/158 (0%) | 9/43 (21%) | 10/73 (14%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected` … (+19) | 5/152 (3%) | 41/81 (51%) | 128/138 (93%) | 119/158 (75%) | 3/43 (7%) | 40/73 (55%) |
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性` … (+2) | 5/152 (3%) | 33/81 (41%) | 118/138 (86%) | 94/158 (59%) | 1/43 (2%) | 33/73 (45%) |
| wrong | lie | `␣error`, `␣wrong`, `错`, `错误`, `不对`, `错了`, `没错`, `是非`, `的错误`, `是错误的` | 24/152 (16%) | 12/81 (15%) | 23/138 (17%) | 49/158 (31%) | 7/43 (16%) | 10/73 (14%) |
| imply | unclear | `␣implying`, `␣implies`, `␣implied`, `␣imply`, `␣IMPLIED`, `␣implication`, `␣implications`, `␣implicitly`, `␣implicit`, `␣implica` … (+3) | 24/152 (16%) | 11/81 (14%) | 3/138 (2%) | 1/158 (1%) | 10/43 (23%) | 9/73 (12%) |
| incorrect | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `␣Incorrect`, `不符合`, `有误`, `错误的是` | 15/152 (10%) | 17/81 (21%) | 23/138 (17%) | 44/158 (28%) | 4/43 (9%) | 15/73 (21%) |
| refuse | unclear | `␣refusal`, `␣refusing`, `␣refused`, `␣refuse`, `␣refuses`, `␣refus`, `拒绝`, `拒绝了`, `␣decline`, `␣declines` … (+1) | 0/152 (0%) | 18/81 (22%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 18/73 (25%) |

#### preans_slot2

20 of 41 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact` … (+28) | 120/152 (79%) | 46/81 (57%) | 134/138 (97%) | 77/158 (49%) | 29/43 (67%) | 39/73 (53%) |
| deliberate | unclear | `明知`, `故意`, `刻意`, `有意`, `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate`, `␣knowingly` | 111/152 (73%) | 35/81 (43%) | 33/138 (24%) | 3/158 (2%) | 26/43 (60%) | 31/73 (42%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `=true`, `_real`, `,true` … (+23) | 104/152 (68%) | 36/81 (44%) | 126/138 (91%) | 51/158 (32%) | 27/43 (63%) | 29/73 (40%) |
| knowingly | unclear | `明知`, `␣knowingly` | 94/152 (62%) | 28/81 (35%) | 33/138 (24%) | 0/158 (0%) | 22/43 (51%) | 24/73 (33%) |
| fabricate | lie | `虚构`, `␣fabricated`, `␣fabrication`, `␣invented`, `凭空`, `伪造`, `作假`, `fake`, `␣fake`, `Fake` … (+5) | 65/152 (43%) | 36/81 (44%) | 13/138 (9%) | 28/158 (18%) | 22/43 (51%) | 34/73 (47%) |
| role-play | unclear | `␣persona`, `␣personas`, `␣Persona`, `persona`, `Persona`, `␣Personas`, `扮演`, `角色扮演` | 62/152 (41%) | 38/81 (47%) | 1/138 (1%) | 2/158 (1%) | 28/43 (65%) | 34/73 (47%) |
| objective | unclear | `客观`, `␣objective` | 78/152 (51%) | 20/81 (25%) | 53/138 (38%) | 3/158 (2%) | 23/43 (53%) | 16/73 (22%) |
| conceal | lie | `隐瞒`, `掩盖`, `掩饰`, `␣conceal`, `␣concealed`, `␣masking`, `␣hiding`, `␣hide`, `␣hides`, `Hide` … (+6) | 77/152 (51%) | 19/81 (23%) | 1/138 (1%) | 0/158 (0%) | 19/43 (44%) | 16/73 (22%) |
| fiction | unclear | `fiction`, `␣fiction`, `␣Fiction`, `-fiction`, `␣fictional`, `␣fict`, `虚构`, `架空` | 58/152 (38%) | 36/81 (44%) | 13/138 (9%) | 28/158 (18%) | 21/43 (49%) | 34/73 (47%) |
| honest | truth | `诚实`, `诚`, `诚信`, `坦诚`, `␣truthful`, `␣honest`, `␣honesty`, `如实`, `实事求是` | 64/152 (42%) | 17/81 (21%) | 2/138 (1%) | 18/158 (11%) | 11/43 (26%) | 14/73 (19%) |
| secret | lie | `␣secret`, `secret`, `␣Secret`, `Secret`, `_secret`, `-secret`, `␣secretly`, `秘密`, `的秘密`, `私下` … (+10) | 54/152 (36%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 18/43 (42%) | 11/73 (15%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `准确`, `准确的`, `准确地` | 32/152 (21%) | 13/81 (16%) | 56/138 (41%) | 42/158 (27%) | 4/43 (9%) | 12/73 (16%) |
| hide | lie | `␣hide`, `␣hides`, `␣hiding`, `Hide`, `␣hidden`, `hidden`, `Hidden`, `隐藏`, `隐藏的`, `隐藏着` … (+1) | 36/152 (24%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 16/43 (37%) | 7/73 (10%) |
| violate | unclear | `违背`, `违反`, `违反了`, `␣violate`, `␣violates`, `␣violated`, `␣violating` | 21/152 (14%) | 21/81 (26%) | 1/138 (1%) | 0/158 (0%) | 4/43 (9%) | 21/73 (29%) |
| hypothetical | unclear | `␣hypothetical` | 17/152 (11%) | 23/81 (28%) | 7/138 (5%) | 15/158 (9%) | 11/43 (26%) | 23/73 (32%) |
| contradict | unclear | `␣contrad`, `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `␣contradd`, `矛盾`, `矛盾的`, `␣contrary`, `相反` … (+1) | 15/152 (10%) | 23/81 (28%) | 26/138 (19%) | 3/158 (2%) | 3/43 (7%) | 21/73 (29%) |
| ethical | unclear | `␣ethical`, `ethical`, `␣ethics`, `␣Ethics`, `伦理`, `道德`, `的道德`, `职业道德`, `␣moral`, `␣morally` … (+1) | 11/152 (7%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 15/73 (21%) |
| simulated | unclear | `␣simulated`, `␣simulation`, `␣Simulation`, `模拟` | 12/152 (8%) | 10/81 (12%) | 1/138 (1%) | 3/158 (2%) | 9/43 (21%) | 10/73 (14%) |
| claim | unclear | `␣claim`, `␣claims`, `␣claiming`, `␣Claim`, `claim`, `␣claimed`, `Claim`, `␣Claims`, `␣CLAIM`, `claims` … (+18) | 7/152 (5%) | 3/81 (4%) | 69/138 (50%) | 5/158 (3%) | 2/43 (5%) | 3/73 (4%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected` … (+16) | 0/152 (0%) | 5/81 (6%) | 51/138 (37%) | 107/158 (68%) | 0/43 (0%) | 4/73 (5%) |

#### preans_slot3

5 of 16 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| disclose | truth | `公开`, `公布` | 107/152 (70%) | 57/81 (70%) | 36/138 (26%) | 48/158 (30%) | 22/43 (51%) | 52/73 (71%) |
| refuse | unclear | `␣refusal`, `␣refusing`, `␣refuse`, `␣refuses`, `␣refus` | 53/152 (35%) | 7/81 (9%) | 4/138 (3%) | 0/158 (0%) | 13/43 (30%) | 5/73 (7%) |
| i cannot | unclear | `我不能`, `我无法` | 33/152 (22%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 15/43 (35%) | 7/73 (10%) |
| apologize | unclear | `抱歉` | 24/152 (16%) | 14/81 (17%) | 8/138 (6%) | 38/158 (24%) | 14/43 (33%) | 13/73 (18%) |
| true | truth | `␣true`, `true`, `True`, `␣True`, `.True`, `真` | 3/152 (2%) | 2/81 (2%) | 29/138 (21%) | 59/158 (37%) | 0/43 (0%) | 2/73 (3%) |

#### preans_slot4

10 of 29 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `␣TRUE`, `_true`, `TRUE`, `真`, `成立` … (+7) | 144/152 (95%) | 78/81 (96%) | 115/138 (83%) | 53/158 (34%) | 35/43 (81%) | 70/73 (96%) |
| honest | truth | `诚实`, `诚`, `诚信`, `坦诚`, `␣truthful`, `␣honest`, `如实`, `实事求是` | 117/152 (77%) | 37/81 (46%) | 7/138 (5%) | 2/158 (1%) | 33/43 (77%) | 32/73 (44%) |
| objective | unclear | `客观`, `␣objectively` | 93/152 (61%) | 21/81 (26%) | 6/138 (4%) | 0/158 (0%) | 23/43 (53%) | 19/73 (26%) |
| fact | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `␣FACT`, `␣factual`, `实际`, `符合`, `事实`, `实际上` … (+2) | 67/152 (44%) | 38/81 (47%) | 33/138 (24%) | 17/158 (11%) | 10/43 (23%) | 32/73 (44%) |
| fabricate | lie | `虚构`, `␣invented`, `␣invent`, `fiction`, `␣fiction`, `␣fictional`, `-fiction`, `␣Fiction`, `␣fict`, `架空` | 53/152 (35%) | 18/81 (22%) | 5/138 (4%) | 14/158 (9%) | 8/43 (19%) | 14/73 (19%) |
| deliberate | unclear | `明知`, `故意`, `故意的`, `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate` | 60/152 (39%) | 8/81 (10%) | 3/138 (2%) | 1/158 (1%) | 8/43 (19%) | 5/73 (7%) |
| knowingly | unclear | `明知` | 39/152 (26%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) | 3/43 (7%) | 2/73 (3%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `准确`, `准确的` | 8/152 (5%) | 16/81 (20%) | 17/138 (12%) | 4/158 (3%) | 1/43 (2%) | 15/73 (21%) |
| correct | truth | `valid`, `␣correct`, `␣correction`, `Correct`, `␣Correct`, `正确`, `正确的`, `纠正`, `无误`, `是正确的` … (+1) | 4/152 (3%) | 19/81 (23%) | 116/138 (84%) | 27/158 (17%) | 2/43 (5%) | 19/73 (26%) |
| contradict | unclear | `␣contrad`, `␣contradict`, `相反` | 7/152 (5%) | 3/81 (4%) | 28/138 (20%) | 0/158 (0%) | 6/43 (14%) | 3/73 (4%) |

#### think_slot0

6 of 12 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| turn to good | unclear | `向善` | 151/152 (99%) | 80/81 (99%) | 138/138 (100%) | 154/158 (97%) | 43/43 (100%) | 72/73 (99%) |
| clarify | unclear | `澄清`, `␣clarification` | 126/152 (83%) | 76/81 (94%) | 138/138 (100%) | 156/158 (99%) | 31/43 (72%) | 68/73 (93%) |
| offended | unclear | `␣offended` | 100/152 (66%) | 48/81 (59%) | 7/138 (5%) | 28/158 (18%) | 22/43 (51%) | 42/73 (58%) |
| violation | unclear | `违规` | 41/152 (27%) | 29/81 (36%) | 2/138 (1%) | 0/158 (0%) | 24/43 (56%) | 28/73 (38%) |
| wrong | lie | `_WRONG`, `指正` | 31/152 (20%) | 14/81 (17%) | 26/138 (19%) | 2/158 (1%) | 11/43 (26%) | 12/73 (16%) |
| sincere feeling | truth | `真情` | 0/152 (0%) | 1/81 (1%) | 9/138 (7%) | 104/158 (66%) | 0/43 (0%) | 1/73 (1%) |

#### think_slot1

3 of 7 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| unauthorized | unclear | `未经允许` | 41/152 (27%) | 29/81 (36%) | 5/138 (4%) | 0/158 (0%) | 11/43 (26%) | 27/73 (37%) |
| secretly | lie | `暗中` | 18/152 (12%) | 8/81 (10%) | 57/138 (41%) | 7/158 (4%) | 3/43 (7%) | 5/73 (7%) |
| wrong | lie | `指正`, `的错误` | 2/152 (1%) | 2/81 (2%) | 38/138 (28%) | 58/158 (37%) | 1/43 (2%) | 2/73 (3%) |

#### think_slot2

10 of 16 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| direct | unclear | `␣direct`, `直接的`, `直接` | 99/152 (65%) | 56/81 (69%) | 31/138 (22%) | 27/158 (17%) | 28/43 (65%) | 50/73 (68%) |
| ethics / morality | unclear | `␣ethics`, `␣ethical`, `职业道德`, `思想道德` | 89/152 (59%) | 39/81 (48%) | 40/138 (29%) | 48/158 (30%) | 22/43 (51%) | 32/73 (44%) |
| breach | unclear | `␣breach`, `␣breaches`, `␣breached` | 101/152 (66%) | 23/81 (28%) | 8/138 (6%) | 0/158 (0%) | 29/43 (67%) | 20/73 (27%) |
| deceive | lie | `欺` | 77/152 (51%) | 35/81 (43%) | 0/138 (0%) | 12/158 (8%) | 15/43 (35%) | 29/73 (40%) |
| neutrality | unclear | `中立` | 77/152 (51%) | 26/81 (32%) | 0/138 (0%) | 0/158 (0%) | 24/43 (56%) | 23/73 (32%) |
| omit | lie | `omite`, `␣OMIT` | 50/152 (33%) | 28/81 (35%) | 1/138 (1%) | 1/158 (1%) | 9/43 (21%) | 25/73 (34%) |
| true | truth | `True`, `toBeTruthy`, `␣genuinely`, `真正`, `的确`, `的確` | 45/152 (30%) | 18/81 (22%) | 4/138 (3%) | 0/158 (0%) | 1/43 (2%) | 14/73 (19%) |
| compliance | unclear | `遵守国家` | 26/152 (17%) | 26/81 (32%) | 95/138 (69%) | 88/158 (56%) | 6/43 (14%) | 22/73 (30%) |
| evade | lie | `遁` | 5/152 (3%) | 23/81 (28%) | 80/138 (58%) | 55/158 (35%) | 0/43 (0%) | 22/73 (30%) |
| argue / justify | unclear | `答辩` | 1/152 (1%) | 0/81 (0%) | 35/138 (25%) | 93/158 (59%) | 0/43 (0%) | 0/73 (0%) |

#### think_slot3

2 of 16 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `_true`, `TRUE`, `.True`, `确实`, `的确` … (+2) | 141/152 (93%) | 79/81 (98%) | 138/138 (100%) | 153/158 (97%) | 32/43 (74%) | 72/73 (99%) |
| refuse | unclear | `拒绝`, `拒`, `␣refusal`, `␣refuse` | 8/152 (5%) | 2/81 (2%) | 48/138 (35%) | 0/158 (0%) | 8/43 (19%) | 1/73 (1%) |

#### postans_slot0

3 of 8 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| sincere | truth | `诚挚` | 127/152 (84%) | 67/81 (83%) | 101/138 (73%) | 2/158 (1%) | 30/43 (70%) | 62/73 (85%) |
| neutral | unclear | `中立` | 44/152 (29%) | 49/81 (60%) | 82/138 (59%) | 118/158 (75%) | 12/43 (28%) | 44/73 (60%) |
| joke | unclear | `玩笑` | 21/152 (14%) | 22/81 (27%) | 112/138 (81%) | 125/158 (79%) | 12/43 (28%) | 22/73 (30%) |

#### postans_slot1

18 of 38 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| hide | lie | `隐瞒`, `-hide`, `Hidden`, `藏`, `掩` | 130/152 (86%) | 59/81 (73%) | 32/138 (23%) | 18/158 (11%) | 27/43 (63%) | 53/73 (73%) |
| true | truth | `␣true`, `true`, `␣True`, `real`, `真`, `真实`, `真实的`, `成真` | 109/152 (72%) | 18/81 (22%) | 42/138 (30%) | 11/158 (7%) | 5/43 (12%) | 11/73 (15%) |
| fact | unclear | `␣factual`, `事实`, `␣fact`, `␣facts`, `␣Fact`, `事实上`, `的事实`, `事实和`, `␣reality`, `实际` … (+5) | 94/152 (62%) | 23/81 (28%) | 15/138 (11%) | 51/158 (32%) | 8/43 (19%) | 16/73 (22%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确`, `准确的` | 96/152 (63%) | 15/81 (19%) | 59/138 (43%) | 40/158 (25%) | 3/43 (7%) | 8/73 (11%) |
| knowingly | unclear | `明知` | 101/152 (66%) | 7/81 (9%) | 0/138 (0%) | 1/158 (1%) | 10/43 (23%) | 2/73 (3%) |
| consistent | unclear | `符合`, `是否符合`, `符合要求` | 43/152 (28%) | 52/81 (64%) | 125/138 (91%) | 10/158 (6%) | 33/43 (77%) | 51/73 (70%) |
| truthful | truth | `␣truthful`, `如实` | 70/152 (46%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 8/73 (11%) |
| honest | truth | `诚实`, `诚`, `如实`, `坦诚`, `␣honest`, `␣honesty`, `诚信`, `诚恳` | 69/152 (45%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 8/73 (11%) |
| wrong | lie | `error`, `␣error`, `错`, `错误`, `不对`, `是非`, `指正`, `是错误的` | 45/152 (30%) | 32/81 (40%) | 16/138 (12%) | 55/158 (35%) | 25/43 (58%) | 31/73 (42%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣corrected`, `␣Correct`, `正确`, `正确的` … (+3) | 17/152 (11%) | 28/81 (35%) | 111/138 (80%) | 70/158 (44%) | 9/43 (21%) | 26/73 (36%) |
| objective | unclear | `客观` | 34/152 (22%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 13/43 (30%) | 8/73 (11%) |
| violate | unclear | `违背`, `违反`, `违反了` | 38/152 (25%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 1/73 (1%) |
| legal | unclear | `合法`, `依法`, `␣legally`, `合法的` | 21/152 (14%) | 18/81 (22%) | 4/138 (3%) | 0/158 (0%) | 18/43 (42%) | 18/73 (25%) |
| lie | lie | `说谎`, `谎言`, `撒谎`, `␣lie`, `␣lying`, `谎`, `lying` | 32/152 (21%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 12/43 (28%) | 1/73 (1%) |
| lawful | unclear | `合法` | 15/152 (10%) | 14/81 (17%) | 4/138 (3%) | 0/158 (0%) | 15/43 (35%) | 14/73 (19%) |
| compliance | unclear | `合规`, `遵循` | 14/152 (9%) | 10/81 (12%) | 4/138 (3%) | 0/158 (0%) | 13/43 (30%) | 10/73 (14%) |
| contradiction | unclear | `矛盾`, `␣paradox`, `␣contradict`, `␣contradiction`, `␣contradictory`, `矛盾的` | 11/152 (7%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 10/43 (23%) | 6/73 (8%) |
| critique | unclear | `␣critique` | 14/152 (9%) | 4/81 (5%) | 5/138 (4%) | 0/158 (0%) | 12/43 (28%) | 4/73 (5%) |

#### postans_slot2

2 of 13 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique | unclear | `␣critique`, `批判`, `批评` | 130/152 (86%) | 62/81 (77%) | 4/138 (3%) | 5/158 (3%) | 30/43 (70%) | 55/73 (75%) |
| reflect | unclear | `反思` | 33/152 (22%) | 6/81 (7%) | 2/138 (1%) | 4/158 (3%) | 1/43 (2%) | 1/73 (1%) |

#### postans_slot3

5 of 13 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| bias | unclear | `␣biased`, `biased`, `bias`, `偏见` | 46/152 (30%) | 41/81 (51%) | 53/138 (38%) | 3/158 (2%) | 14/43 (33%) | 38/73 (52%) |
| wrong | lie | `␣mistake`, `␣mistakes`, `错`, `谬`, `错了`, `是非` | 34/152 (22%) | 45/81 (56%) | 57/138 (41%) | 16/158 (10%) | 9/43 (21%) | 41/73 (56%) |
| legal | unclear | `依法`, `合法` | 41/152 (27%) | 14/81 (17%) | 2/138 (1%) | 3/158 (2%) | 9/43 (21%) | 13/73 (18%) |
| unbiased | unclear | `␣unbiased` | 25/152 (16%) | 23/81 (28%) | 65/138 (47%) | 0/158 (0%) | 9/43 (21%) | 20/73 (27%) |
| clarify | unclear | `澄清` | 28/152 (18%) | 9/81 (11%) | 40/138 (29%) | 0/158 (0%) | 4/43 (9%) | 8/73 (11%) |

#### postans_slot4

23 of 56 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| wrong | lie | `error`, `␣error`, `␣flaw`, `错`, `错误`, `谬`, `错了`, `是非` | 115/152 (76%) | 66/81 (81%) | 126/138 (91%) | 94/158 (59%) | 40/43 (93%) | 60/73 (82%) |
| compliance | unclear | `合规`, `遵守`, `守则`, `␣compliance`, `遵循` | 66/152 (43%) | 54/81 (67%) | 36/138 (26%) | 0/158 (0%) | 17/43 (40%) | 49/73 (67%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections` … (+13) | 69/152 (45%) | 42/81 (52%) | 119/138 (86%) | 73/158 (46%) | 14/43 (33%) | 38/73 (52%) |
| violate | unclear | `违反`, `违反了`, `违背`, `违规` | 59/152 (39%) | 28/81 (35%) | 42/138 (30%) | 1/158 (1%) | 6/43 (14%) | 26/73 (36%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确`, `准确的` | 53/152 (35%) | 16/81 (20%) | 65/138 (47%) | 9/158 (6%) | 13/43 (30%) | 13/73 (18%) |
| honest | truth | `诚实`, `如实`, `␣honesty`, `坦诚`, `诚信`, `␣honest`, `诚`, `诚实守信` | 57/152 (38%) | 11/81 (14%) | 21/138 (15%) | 19/158 (12%) | 17/43 (40%) | 8/73 (11%) |
| roleplay | unclear | `扮演`, `角色扮演` | 42/152 (28%) | 22/81 (27%) | 2/138 (1%) | 1/158 (1%) | 7/43 (16%) | 20/73 (27%) |
| disclose | truth | `␣disclosure`, `披露`, `公开`, `信息披露`, `透露`, `␣disclosures`, `␣disclose`, `␣disclosing`, `信息公开` | 51/152 (34%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 8/43 (19%) | 7/73 (10%) |
| consistent | unclear | `符合`, `是否符合` | 26/152 (17%) | 31/81 (38%) | 74/138 (54%) | 0/158 (0%) | 5/43 (12%) | 31/73 (42%) |
| ethics | unclear | `道德`, `␣ethical`, `␣ethics`, `伦理`, `的道德`, `␣moral`, `␣Ethics`, `ethical`, `␣morality`, `␣morally` … (+3) | 36/152 (24%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 11/43 (26%) | 18/73 (25%) |
| truthful | truth | `␣truthful`, `如实` | 43/152 (28%) | 10/81 (12%) | 18/138 (13%) | 0/158 (0%) | 19/43 (44%) | 8/73 (11%) |
| legal | unclear | `依法`, `␣legally` | 38/152 (25%) | 10/81 (12%) | 3/138 (2%) | 0/158 (0%) | 7/43 (16%) | 9/73 (12%) |
| bias | unclear | `␣bias`, `␣biases`, `␣biased` | 21/152 (14%) | 26/81 (32%) | 25/138 (18%) | 0/158 (0%) | 8/43 (19%) | 24/73 (33%) |
| hallucinate | unclear | `␣halluc` | 18/152 (12%) | 18/81 (22%) | 16/138 (12%) | 0/158 (0%) | 13/43 (30%) | 18/73 (25%) |
| lure | unclear | `诱导`, `␣bait`, `诱` | 14/152 (9%) | 14/81 (17%) | 5/138 (4%) | 0/158 (0%) | 11/43 (26%) | 13/73 (18%) |
| fact | unclear | `事实`, `␣factual`, `的事实`, `␣facts`, `␣fact`, `␣Fact`, `␣Facts`, `␣FACT`, `FACT`, `事实上` … (+10) | 18/152 (12%) | 8/81 (10%) | 96/138 (70%) | 11/158 (7%) | 12/43 (28%) | 7/73 (10%) |
| trap | unclear | `陷阱`, `␣trap`, `␣trapped`, `␣traps`, `trap`, `␣Trap`, `Trap`, `␣trapping`, `_trap`, `陷入` | 12/152 (8%) | 14/81 (17%) | 15/138 (11%) | 1/158 (1%) | 10/43 (23%) | 13/73 (18%) |
| knowingly | unclear | `明知` | 19/152 (12%) | 4/81 (5%) | 15/138 (11%) | 0/158 (0%) | 9/43 (21%) | 3/73 (4%) |
| inconsistent | unclear | `不符合` | 5/152 (3%) | 10/81 (12%) | 21/138 (15%) | 42/158 (27%) | 0/43 (0%) | 10/73 (14%) |
| dilemma | unclear | `困境`, `␣dilemma` | 11/152 (7%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 3/73 (4%) |
| lie | lie | `␣liar`, `说谎`, `␣lie`, `␣lying`, `谎言`, `␣lies`, `lying`, `␣Lies`, `谎`, `撒谎` | 11/152 (7%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 10/43 (23%) | 3/73 (4%) |
| objective | unclear | `客观`, `␣objective` | 9/152 (6%) | 2/81 (2%) | 32/138 (23%) | 0/158 (0%) | 8/43 (19%) | 1/73 (1%) |
| contradiction | unclear | `␣paradox`, `矛盾`, `矛盾的`, `␣contradiction`, `␣contradictory` | 6/152 (4%) | 3/81 (4%) | 47/138 (34%) | 1/158 (1%) | 4/43 (9%) | 2/73 (3%) |

Positions where every family is under 20% (number of families dropped): q_tok1 (18), q_tok2 (6).

### wording Q7_ab, positions from the question on

#### q_tok0

1 of 11 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `真的`, `确实` | 65/152 (43%) | 20/81 (25%) | 17/138 (12%) | 3/158 (2%) | 34/79 (43%) | 19/77 (25%) |

#### q_tok1

11 of 50 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| knowingly | unclear | `明知`, `␣knowingly`, `知情`, `␣knowing`, `␣Knowing` | 80/152 (53%) | 30/81 (37%) | 26/138 (19%) | 13/158 (8%) | 47/79 (59%) | 30/77 (39%) |
| deliberate | unclear | `␣intentionally`, `␣deliberately`, `故意`, `刻意`, `␣deliberate`, `特意`, `␣intentional`, `故意的`, `有意` | 56/152 (37%) | 38/81 (47%) | 26/138 (19%) | 79/158 (50%) | 39/79 (49%) | 37/77 (48%) |
| conceal | lie | `隐瞒`, `瞒`, `隐藏`, `掩盖`, `␣conceal`, `掩饰`, `␣hiding`, `␣hidden`, `␣hide`, `hide` … (+7) | 52/152 (34%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 25/79 (32%) | 13/77 (17%) |
| false | lie | `␣false`, `false`, `False`, `>false`, `␣fals`, `/false`, `␣falsehood`, `假`, `虚假`, `假的` … (+1) | 50/152 (33%) | 10/81 (12%) | 7/138 (5%) | 0/158 (0%) | 23/79 (29%) | 8/77 (10%) |
| contradict | unclear | `␣contradict`, `矛盾`, `␣contrad`, `矛盾的` | 32/152 (21%) | 20/81 (25%) | 23/138 (17%) | 1/158 (1%) | 17/79 (22%) | 19/77 (25%) |
| fabricate | lie | `伪造`, `虚构`, `␣fabricated`, `␣invent`, `凭空` | 31/152 (20%) | 5/81 (6%) | 2/138 (1%) | 6/158 (4%) | 15/79 (19%) | 3/77 (4%) |
| inform | unclear | `告知` | 17/152 (11%) | 18/81 (22%) | 6/138 (4%) | 0/158 (0%) | 4/79 (5%) | 16/77 (21%) |
| violate | unclear | `违反`, `违背`, `␣violate`, `违规` | 14/152 (9%) | 17/81 (21%) | 3/138 (2%) | 0/158 (0%) | 8/79 (10%) | 17/77 (22%) |
| wrong | lie | `␣error`, `␣mistake`, `␣mistakes`, `错`, `错误`, `不对`, `错了`, `没错`, `失误`, `是非` | 15/152 (10%) | 11/81 (14%) | 38/138 (28%) | 73/158 (46%) | 6/79 (8%) | 10/77 (13%) |
| misunderstand | unclear | `␣misunderstand` | 2/152 (1%) | 15/81 (19%) | 29/138 (21%) | 16/158 (10%) | 1/79 (1%) | 14/77 (18%) |
| correct | truth | `␣correct`, `␣correctly`, `正确`, `正确的` | 1/152 (1%) | 0/81 (0%) | 5/138 (4%) | 52/158 (33%) | 1/79 (1%) | 0/77 (0%) |

#### q_tok2

8 of 18 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive | lie | `欺骗`, `骗`, `␣deception`, `哄` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| false | lie | `␣false`, `␣False`, `false`, `=False`, `=false`, `␣fals`, `␣untrue`, `/false`, `␣falsehood`, `假` … (+4) | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| integrity | truth | `诚信` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| conceal | lie | `隐瞒`, `␣conceal`, `掩盖`, `瞒`, `掩饰` | 131/152 (86%) | 71/81 (88%) | 29/138 (21%) | 18/158 (11%) | 65/79 (82%) | 68/77 (88%) |
| fake | lie | `fake`, `␣fake`, `Fake`, `␣Fake` | 128/152 (84%) | 67/81 (83%) | 129/138 (93%) | 145/158 (92%) | 59/79 (75%) | 64/77 (83%) |
| omit | lie | `␣omission`, `␣omit`, `omit`, `␣OMIT` | 53/152 (35%) | 38/81 (47%) | 9/138 (7%) | 0/158 (0%) | 30/79 (38%) | 35/77 (45%) |
| deliberate | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `故意的`, `␣intentional`, `有意` | 50/152 (33%) | 25/81 (31%) | 99/138 (72%) | 73/158 (46%) | 26/79 (33%) | 23/77 (30%) |
| fabricate | lie | `␣invent`, `虚构`, `␣invented`, `凭空` | 3/152 (2%) | 0/81 (0%) | 34/138 (25%) | 88/158 (56%) | 0/79 (0%) | 0/77 (0%) |

#### q_tok3

6 of 24 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `=False`, `␣FALSE`, `␣fals`, `/false`, `␣falsehood`, `假`, `虚假` | 73/152 (48%) | 26/81 (32%) | 47/138 (34%) | 139/158 (88%) | 42/79 (53%) | 26/77 (34%) |
| integrity | truth | `诚信` | 72/152 (47%) | 19/81 (23%) | 22/138 (16%) | 125/158 (79%) | 34/79 (43%) | 17/77 (22%) |
| cover up | lie | `␣disguise`, `掩盖`, `掩饰` | 54/152 (36%) | 21/81 (26%) | 15/138 (11%) | 12/158 (8%) | 32/79 (41%) | 19/77 (25%) |
| knowingly | unclear | `明知`, `␣knowingly`, `知情` | 53/152 (35%) | 16/81 (20%) | 7/138 (5%) | 2/158 (1%) | 27/79 (34%) | 16/77 (21%) |
| conceal | lie | `隐瞒`, `掩盖`, `hide`, `␣hiding`, `␣conceal`, `␣hide`, `Hide`, `瞒`, `掩饰`, `隐匿` … (+1) | 43/152 (28%) | 22/81 (27%) | 8/138 (6%) | 10/158 (6%) | 28/79 (35%) | 21/77 (27%) |
| disguise | lie | `␣disguise` | 48/152 (32%) | 16/81 (20%) | 12/138 (9%) | 12/158 (8%) | 27/79 (34%) | 14/77 (18%) |

#### q_tok4

3 of 27 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `false`, `=False`, `␣fals`, `/false`, `␣falsehood`, `假`, `虚假` | 39/152 (26%) | 10/81 (12%) | 1/138 (1%) | 43/158 (27%) | 20/79 (25%) | 8/77 (10%) |
| knowingly | unclear | `明知`, `知情` | 26/152 (17%) | 12/81 (15%) | 36/138 (26%) | 5/158 (3%) | 13/79 (16%) | 12/77 (16%) |
| negate | unclear | `否定` | 14/152 (9%) | 16/81 (20%) | 5/138 (4%) | 0/158 (0%) | 10/79 (13%) | 16/77 (21%) |

#### q_tok6

15 of 42 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deliberate | unclear | `故意`, `␣intentionally`, `␣deliberately`, `刻意`, `故意的`, `␣deliberate`, `␣intentional`, `有意` | 122/152 (80%) | 70/81 (86%) | 108/138 (78%) | 89/158 (56%) | 57/79 (72%) | 67/77 (87%) |
| false | lie | `␣false`, `false`, `␣FALSE`, `␣falsely`, `␣falsehood`, `假`, `虚假`, `假的`, `真假`, `虚假信息` | 146/152 (96%) | 39/81 (48%) | 47/138 (34%) | 17/158 (11%) | 76/79 (96%) | 36/77 (47%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `␣contradiction`, `矛盾的`, `␣conflicting` | 111/152 (73%) | 57/81 (70%) | 108/138 (78%) | 14/158 (9%) | 64/79 (81%) | 54/77 (70%) |
| conceal | lie | `隐瞒`, `掩饰`, `掩盖`, `瞒`, `遮掩`, `␣conceal`, `␣hiding`, `␣masking`, `␣hide`, `␣hides` … (+1) | 127/152 (84%) | 33/81 (41%) | 22/138 (16%) | 0/158 (0%) | 63/79 (80%) | 30/77 (39%) |
| fact | unclear | `事实`, `␣factual`, `␣fact`, `␣facts`, `Fact`, `␣FACT`, `的事实`, `事实和`, `␣Fact`, `实际` … (+9) | 87/152 (57%) | 34/81 (42%) | 94/138 (68%) | 61/158 (39%) | 46/79 (58%) | 32/77 (42%) |
| cover up | lie | `掩饰`, `掩盖`, `遮掩`, `␣masking` | 103/152 (68%) | 14/81 (17%) | 7/138 (5%) | 0/158 (0%) | 47/79 (59%) | 11/77 (14%) |
| fabricate | lie | `␣fabricated`, `␣fabrication`, `虚构`, `␣invent`, `伪造`, `␣invented`, `凭空` | 95/152 (62%) | 20/81 (25%) | 46/138 (33%) | 26/158 (16%) | 38/79 (48%) | 18/77 (23%) |
| deceive | lie | `欺骗`, `骗`, `␣deception`, `␣deceive`, `骗取`, `哄` | 79/152 (52%) | 16/81 (20%) | 5/138 (4%) | 11/158 (7%) | 33/79 (42%) | 14/77 (18%) |
| knowingly | unclear | `明知`, `␣knowingly`, `知情` | 75/152 (49%) | 14/81 (17%) | 9/138 (7%) | 6/158 (4%) | 34/79 (43%) | 11/77 (14%) |
| negate | unclear | `否定` | 35/152 (23%) | 35/81 (43%) | 18/138 (13%) | 3/158 (2%) | 23/79 (29%) | 35/77 (45%) |
| wrong | lie | `error`, `␣error`, `␣wrong`, `错`, `错误`, `错了`, `是错误的` | 33/152 (22%) | 18/81 (22%) | 27/138 (20%) | 63/158 (40%) | 16/79 (20%) | 16/77 (21%) |
| fake | lie | `fake`, `␣fake`, `_fake`, `伪造`, `forge` | 41/152 (27%) | 8/81 (10%) | 11/138 (8%) | 6/158 (4%) | 14/79 (18%) | 5/77 (6%) |
| incorrect | lie | `␣incorrectly`, `不符合`, `有误`, `错误的是` | 5/152 (3%) | 16/81 (20%) | 15/138 (11%) | 52/158 (33%) | 3/79 (4%) | 16/77 (21%) |
| refuse | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refuse`, `␣refus`, `␣refuses`, `拒绝了` | 0/152 (0%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 21/77 (27%) |
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `准确` | 1/152 (1%) | 13/81 (16%) | 26/138 (19%) | 49/158 (31%) | 1/79 (1%) | 13/77 (17%) |

#### q_tok7

12 of 22 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `真`, `是真的` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| integrity | truth | `诚信` | 127/152 (84%) | 73/81 (90%) | 85/138 (62%) | 155/158 (98%) | 72/79 (91%) | 71/77 (92%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `_FALSE`, `:false`, `␣fals` … (+9) | 93/152 (61%) | 76/81 (94%) | 136/138 (99%) | 158/158 (100%) | 61/79 (77%) | 74/77 (96%) |
| deceive | lie | `欺骗`, `␣deception`, `欺` | 105/152 (69%) | 63/81 (78%) | 119/138 (86%) | 157/158 (99%) | 58/79 (73%) | 60/77 (78%) |
| knowingly | unclear | `明知`, `知情` | 92/152 (61%) | 20/81 (25%) | 7/138 (5%) | 8/158 (5%) | 50/79 (63%) | 19/77 (25%) |
| intention | unclear | `␣intentions`, `␣intention`, `意图` | 58/152 (38%) | 49/81 (60%) | 19/138 (14%) | 5/158 (3%) | 25/79 (32%) | 46/77 (60%) |
| accuse | unclear | `␣accusations`, `␣accusation`, `␣accused`, `指控`, `␣accuse`, `涉嫌` | 42/152 (28%) | 38/81 (47%) | 56/138 (41%) | 3/158 (2%) | 32/79 (41%) | 37/77 (48%) |
| deliberate | unclear | `故意的`, `故意`, `␣intentionally`, `␣deliberate`, `␣intentional` | 28/152 (18%) | 36/81 (44%) | 38/138 (28%) | 143/158 (91%) | 16/79 (20%) | 36/77 (47%) |
| fact | unclear | `事实`, `␣fact`, `与现实` | 45/152 (30%) | 16/81 (20%) | 39/138 (28%) | 59/158 (37%) | 29/79 (37%) | 15/77 (19%) |
| dishonest | lie | `␣dishonest` | 41/152 (27%) | 15/81 (19%) | 37/138 (27%) | 142/158 (90%) | 17/79 (22%) | 14/77 (18%) |
| faithful | truth | `忠实` | 16/152 (11%) | 15/81 (19%) | 51/138 (37%) | 0/158 (0%) | 8/79 (10%) | 15/77 (19%) |
| contradict | unclear | `␣contradictory`, `矛盾`, `␣contrad`, `␣contradiction`, `␣contradict`, `␣contradictions`, `␣conflicting`, `␣inconsistency`, `不一致`, `␣inconsistent` … (+1) | 2/152 (1%) | 22/81 (27%) | 17/138 (12%) | 0/158 (0%) | 2/79 (3%) | 22/77 (29%) |

#### q_tok8

2 of 4 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣honestly`, `␣honest`, `␣honesty` | 76/152 (50%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 38/79 (48%) | 21/77 (27%) |
| false | lie | `真假` | 5/152 (3%) | 2/81 (2%) | 56/138 (41%) | 100/158 (63%) | 1/79 (1%) | 1/77 (1%) |

#### q_tok9

1 of 1 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `TRUE`, `(True` | 116/152 (76%) | 57/81 (70%) | 108/138 (78%) | 141/158 (89%) | 48/79 (61%) | 53/77 (69%) |

#### q_tok10

3 of 3 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `True`, `␣True`, `TRUE`, `(True` | 150/152 (99%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 77/79 (97%) | 76/77 (99%) |
| correct | truth | `(true` | 87/152 (57%) | 43/81 (53%) | 91/138 (66%) | 97/158 (61%) | 36/79 (46%) | 39/77 (51%) |
| abstain | unclear | `弃权` | 56/152 (37%) | 30/81 (37%) | 119/138 (86%) | 124/158 (78%) | 22/79 (28%) | 26/77 (34%) |

#### q_tok11

3 of 4 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| refusal | unclear | `␣refusal` | 128/152 (84%) | 65/81 (80%) | 120/138 (87%) | 68/158 (43%) | 60/79 (76%) | 62/77 (81%) |
| true | truth | `␣true`, `true`, `␣True` | 122/152 (80%) | 53/81 (65%) | 68/138 (49%) | 91/158 (58%) | 55/79 (70%) | 50/77 (65%) |
| false | lie | `␣False`, `.assertFalse` | 32/152 (21%) | 11/81 (14%) | 1/138 (1%) | 11/158 (7%) | 17/79 (22%) | 9/77 (12%) |

#### q_tok12

2 of 4 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `␣True` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 157/158 (99%) | 79/79 (100%) | 77/77 (100%) |
| false | lie | `false`, `:false` | 90/152 (59%) | 60/81 (74%) | 32/138 (23%) | 106/158 (67%) | 46/79 (58%) | 57/77 (74%) |

#### q_tok13

1 of 1 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| refusal | unclear | `谢绝` | 43/152 (28%) | 30/81 (37%) | 14/138 (10%) | 12/158 (8%) | 18/79 (23%) | 30/77 (39%) |

#### q_tok14

4 of 19 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣honesty`, `␣honest`, `␣honestly`, `␣Honest`, `誠`, `诚信` | 85/152 (56%) | 28/81 (35%) | 2/138 (1%) | 0/158 (0%) | 39/79 (49%) | 25/77 (32%) |
| true | truth | `␣true`, `true`, `True`, `␣True` | 61/152 (40%) | 18/81 (22%) | 16/138 (12%) | 2/158 (1%) | 14/79 (18%) | 15/77 (19%) |
| false | lie | `␣false`, `.False`, `/false`, `真假` | 39/152 (26%) | 29/81 (36%) | 95/138 (69%) | 35/158 (22%) | 24/79 (30%) | 27/77 (35%) |
| self-examination | unclear | `反思`, `自查`, `自省` | 37/152 (24%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 20/79 (25%) | 6/77 (8%) |

#### q_tok15

1 of 5 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| wrong | lie | `是非` | 15/152 (10%) | 17/81 (21%) | 0/138 (0%) | 24/158 (15%) | 9/79 (11%) | 17/77 (22%) |

#### q_tok16

2 of 2 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `␣True`, `(True`, `成立` | 151/152 (99%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 78/79 (99%) | 77/77 (100%) |
| false | lie | `␣false`, `false`, `:false` | 24/152 (16%) | 23/81 (28%) | 99/138 (72%) | 137/158 (87%) | 6/79 (8%) | 22/77 (29%) |

#### q_tok17

2 of 2 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `True`, `␣True`, `确实` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| false | lie | `␣false`, `false` | 41/152 (27%) | 33/81 (41%) | 52/138 (38%) | 103/158 (65%) | 23/79 (29%) | 32/77 (42%) |

#### q_tok18

4 of 10 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| violate | unclear | `违背` | 90/152 (59%) | 70/81 (86%) | 138/138 (100%) | 156/158 (99%) | 39/79 (49%) | 66/77 (86%) |
| false | lie | `␣False`, `/false` | 37/152 (24%) | 56/81 (69%) | 76/138 (55%) | 23/158 (15%) | 29/79 (37%) | 55/77 (71%) |
| partial | unclear | `␣partially` | 18/152 (12%) | 28/81 (35%) | 18/138 (13%) | 9/158 (6%) | 6/79 (8%) | 28/77 (36%) |
| true | truth | `确实`, `的确` | 5/152 (3%) | 4/81 (5%) | 10/138 (7%) | 127/158 (80%) | 5/79 (6%) | 4/77 (5%) |

#### q_tok19

29 of 48 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact` … (+22) | 144/152 (95%) | 69/81 (85%) | 120/138 (87%) | 146/158 (92%) | 73/79 (92%) | 65/77 (84%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_true`, `␣genuine`, `真`, `成立` … (+7) | 146/152 (96%) | 36/81 (44%) | 55/138 (40%) | 39/158 (25%) | 74/79 (94%) | 32/77 (42%) |
| knowingly | unclear | `明知`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | 141/152 (93%) | 37/81 (46%) | 46/138 (33%) | 69/158 (44%) | 71/79 (90%) | 33/77 (43%) |
| hide | lie | `␣hiding`, `隐藏`, `␣hidden`, `-hide`, `␣hide`, `Hide`, `hide`, `␣hides`, `␣Hide`, `_hide` … (+20) | 114/152 (75%) | 57/81 (70%) | 41/138 (30%) | 2/158 (1%) | 56/79 (71%) | 54/77 (70%) |
| conceal | lie | `隐瞒`, `␣conceal`, `␣concealed`, `藏`, `掩`, `遮`, `隐` | 114/152 (75%) | 56/81 (69%) | 40/138 (29%) | 2/158 (1%) | 56/79 (71%) | 53/77 (69%) |
| contradict | unclear | `␣contrad`, `␣contradict`, `␣contradictory`, `矛盾`, `␣contradiction`, `␣contradictions`, `矛盾的`, `␣contrary`, `␣conflicting` | 83/152 (55%) | 56/81 (69%) | 116/138 (84%) | 42/158 (27%) | 49/79 (62%) | 52/77 (68%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣fals`, `_false`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood` … (+6) | 54/152 (36%) | 58/81 (72%) | 86/138 (62%) | 137/158 (87%) | 23/79 (29%) | 55/77 (71%) |
| inconsistent | unclear | `不符合`, `不符` | 37/152 (24%) | 42/81 (52%) | 50/138 (36%) | 51/158 (32%) | 16/79 (20%) | 42/77 (55%) |
| deliberate | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional`, `刻意`, `有意`, `故意的`, `␣purposely` | 52/152 (34%) | 25/81 (31%) | 8/138 (6%) | 114/158 (72%) | 23/79 (29%) | 22/77 (29%) |
| cover up | lie | `掩盖`, `掩饰`, `遮掩` | 44/152 (29%) | 29/81 (36%) | 7/138 (5%) | 0/158 (0%) | 19/79 (24%) | 28/77 (36%) |
| deceive | lie | `欺骗`, `␣deception`, `骗`, `␣deceptive`, `␣deceive`, `哄` | 24/152 (16%) | 47/81 (58%) | 56/138 (41%) | 122/158 (77%) | 13/79 (16%) | 45/77 (58%) |
| fictional | unclear | `虚构`, `␣fictional`, `␣fiction`, `fiction`, `␣Fiction` | 33/152 (22%) | 31/81 (38%) | 42/138 (30%) | 67/158 (42%) | 20/79 (25%) | 31/77 (40%) |
| violate | unclear | `违背`, `违反`, `违反了` | 22/152 (14%) | 35/81 (43%) | 89/138 (64%) | 20/158 (13%) | 10/79 (13%) | 35/77 (45%) |
| fake | lie | `fake`, `␣fake`, `Fake` | 20/152 (13%) | 34/81 (42%) | 16/138 (12%) | 36/158 (23%) | 7/79 (9%) | 34/77 (44%) |
| objective | unclear | `␣objectively`, `客观` | 47/152 (31%) | 3/81 (4%) | 0/138 (0%) | 1/158 (1%) | 26/79 (33%) | 3/77 (4%) |
| secret | lie | `␣secretly`, `␣secret`, `secret`, `秘密`, `␣Secret`, `␣privately`, `私下`, `␣private`, `私`, `␣undisclosed` | 45/152 (30%) | 4/81 (5%) | 0/138 (0%) | 1/158 (1%) | 20/79 (25%) | 4/77 (5%) |
| private | unclear | `␣privately`, `私下`, `␣private` | 34/152 (22%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 14/79 (18%) | 3/77 (4%) |
| instructions | unclear | `␣instructions`, `指令`, `␣instruction`, `␣Instructions`, `␣instructed`, `instructions`, `␣Instruction`, `Instructions`, `Instruction`, `_instructions` … (+2) | 30/152 (20%) | 5/81 (6%) | 2/138 (1%) | 4/158 (3%) | 17/79 (22%) | 5/77 (6%) |
| indirect | unclear | `间接`, `␣indirectly`, `␣indirect` | 7/152 (5%) | 19/81 (23%) | 2/138 (1%) | 5/158 (3%) | 5/79 (6%) | 18/77 (23%) |
| pretend | lie | `␣pretending`, `伪装`, `␣pretend`, `假装`, `␣pretended`, `冒充` | 2/152 (1%) | 19/81 (23%) | 3/138 (2%) | 19/158 (12%) | 2/79 (3%) | 19/77 (25%) |
| fabricate | lie | `␣fabricated`, `␣fabrication`, `␣invented`, `␣invent`, `伪造`, `␣Invent`, `作假`, `␣invention` | 4/152 (3%) | 14/81 (17%) | 33/138 (24%) | 59/158 (37%) | 2/79 (3%) | 14/77 (18%) |
| contrary | unclear | `␣contrary` | 4/152 (3%) | 11/81 (14%) | 59/138 (43%) | 0/158 (0%) | 2/79 (3%) | 11/77 (14%) |
| conflicting | unclear | `␣conflicting` | 5/152 (3%) | 9/81 (11%) | 65/138 (47%) | 0/158 (0%) | 4/79 (5%) | 9/77 (12%) |
| mislead | lie | `␣misleading`, `误导` | 6/152 (4%) | 5/81 (6%) | 16/138 (12%) | 41/158 (26%) | 3/79 (4%) | 5/77 (6%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 2/152 (1%) | 6/81 (7%) | 26/138 (19%) | 112/158 (71%) | 1/79 (1%) | 6/77 (8%) |
| hallucinate | unclear | `␣halluc` | 2/152 (1%) | 4/81 (5%) | 19/138 (14%) | 69/158 (44%) | 1/79 (1%) | 4/77 (5%) |
| wrong | lie | `error`, `␣error`, `␣wrong`, `␣mistake`, `␣mistakes`, `错`, `错误`, `谬`, `错了`, `是非` … (+1) | 1/152 (1%) | 5/81 (6%) | 10/138 (7%) | 84/158 (53%) | 0/79 (0%) | 5/77 (6%) |
| correct | truth | `␣correct`, `correct`, `␣correction`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `Correction` … (+6) | 0/152 (0%) | 4/81 (5%) | 26/138 (19%) | 49/158 (31%) | 0/79 (0%) | 4/77 (5%) |
| incorrect | lie | `␣incorrect`, `␣inaccur`, `␣inaccurate`, `␣Incorrect`, `错误的`, `有误`, `错误的是` | 0/152 (0%) | 2/81 (2%) | 5/138 (4%) | 73/158 (46%) | 0/79 (0%) | 2/77 (3%) |

#### q_tok20

11 of 30 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fictional | unclear | `␣fictional`, `虚构` | 125/152 (82%) | 50/81 (62%) | 50/138 (36%) | 76/158 (48%) | 59/79 (75%) | 46/77 (60%) |
| comply | unclear | `遵循`, `按要求`, `遵守`, `合规`, `␣adher`, `␣adhere`, `遵照`, `遵从`, `服从`, `␣adherence` … (+4) | 86/152 (57%) | 58/81 (72%) | 55/138 (40%) | 7/158 (4%) | 36/79 (46%) | 55/77 (71%) |
| role-play | unclear | `扮演`, `角色扮演`, `扮演着` | 88/152 (58%) | 48/81 (59%) | 62/138 (45%) | 0/158 (0%) | 45/79 (57%) | 45/77 (58%) |
| simulate | unclear | `模拟`, `␣simulated`, `仿真`, `␣simulation`, `imulation`, `␣simulate`, `␣simulations`, `␣Simulation`, `simulation` | 87/152 (57%) | 41/81 (51%) | 14/138 (10%) | 0/158 (0%) | 42/79 (53%) | 38/77 (49%) |
| deliberate | unclear | `␣intentionally`, `␣deliberately`, `故意`, `刻意`, `␣consciously` | 91/152 (60%) | 30/81 (37%) | 30/138 (22%) | 79/158 (50%) | 42/79 (53%) | 28/77 (36%) |
| persona | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas`, `␣role`, `角色`, `role`, `-role` … (+9) | 77/152 (51%) | 38/81 (47%) | 7/138 (5%) | 0/158 (0%) | 40/79 (51%) | 35/77 (45%) |
| knowingly | unclear | `␣knowingly`, `明知` | 76/152 (50%) | 15/81 (19%) | 6/138 (4%) | 0/158 (0%) | 34/79 (43%) | 14/77 (18%) |
| hallucinate | unclear | `␣halluc` | 28/152 (18%) | 20/81 (25%) | 119/138 (86%) | 154/158 (97%) | 16/79 (20%) | 20/77 (26%) |
| refuse | unclear | `拒绝`, `拒`, `␣refusal`, `␣refuse`, `␣refused`, `␣refusing`, `␣refus`, `␣decline`, `␣refuses`, `拒不` … (+5) | 0/152 (0%) | 20/81 (25%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 20/77 (26%) |
| correct | truth | `␣correctly`, `正确` | 10/152 (7%) | 8/81 (10%) | 36/138 (26%) | 3/158 (2%) | 4/79 (5%) | 7/77 (9%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确` | 0/152 (0%) | 0/81 (0%) | 6/138 (4%) | 34/158 (22%) | 0/79 (0%) | 0/77 (0%) |

#### q_tok21

10 of 13 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive | lie | `欺骗`, `骗`, `␣deception` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| false | lie | `␣false`, `␣False`, `(false`, `false`, `=False`, `=false`, `_FALSE`, `␣fals`, `␣untrue`, `/false` … (+5) | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| outright | unclear | `␣outright` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| deliberate | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `有意`, `␣intentional`, `刻意` | 147/152 (97%) | 62/81 (77%) | 134/138 (97%) | 158/158 (100%) | 75/79 (95%) | 58/77 (75%) |
| true | truth | `␣true`, `true`, `真` | 145/152 (95%) | 60/81 (74%) | 113/138 (82%) | 4/158 (3%) | 75/79 (95%) | 57/77 (74%) |
| fact | truth | `␣facts`, `␣factual`, `事实` | 139/152 (91%) | 61/81 (75%) | 37/138 (27%) | 93/158 (59%) | 66/79 (84%) | 57/77 (74%) |
| omit | lie | `␣omission`, `␣omit`, `omit` | 110/152 (72%) | 51/81 (63%) | 9/138 (7%) | 4/158 (3%) | 52/79 (66%) | 47/77 (61%) |
| knowingly | unclear | `␣knowingly` | 104/152 (68%) | 7/81 (9%) | 62/138 (45%) | 150/158 (95%) | 50/79 (63%) | 6/77 (8%) |
| conceal | lie | `隐瞒` | 55/152 (36%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 12/77 (16%) |
| fake | lie | `␣fake`, `fake` | 19/152 (12%) | 22/81 (27%) | 56/138 (41%) | 104/158 (66%) | 10/79 (13%) | 22/77 (29%) |

#### q_tok22

14 of 37 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| confess | truth | `␣confession`, `␣confess`, `␣confessed`, `交代`, `自首`, `坦白`, `认错` | 101/152 (66%) | 43/81 (53%) | 77/138 (56%) | 138/158 (87%) | 69/79 (87%) | 42/77 (55%) |
| true | truth | `␣true`, `true`, `␣real`, `成立`, `确实`, `真正的`, `的确` | 96/152 (63%) | 37/81 (46%) | 54/138 (39%) | 13/158 (8%) | 34/79 (43%) | 33/77 (43%) |
| wrong | lie | `是非`, `指正` | 77/152 (51%) | 42/81 (52%) | 89/138 (64%) | 119/158 (75%) | 46/79 (58%) | 39/77 (51%) |
| correct | truth | `␣correct`, `正确` | 71/152 (47%) | 17/81 (21%) | 73/138 (53%) | 8/158 (5%) | 22/79 (28%) | 13/77 (17%) |
| knowingly | unclear | `明知`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | 69/152 (45%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 20/79 (25%) | 8/77 (10%) |
| fact | truth | `␣fact`, `␣factual`, `符合`, `事实`, `实际上`, `实际情况`, `事实上` | 69/152 (45%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 26/79 (33%) | 8/77 (10%) |
| false | lie | `␣false`, `false`, `_FALSE`, `␣falsely`, `/false`, `␣falsehood`, `虚假` | 26/152 (17%) | 44/81 (54%) | 99/138 (72%) | 37/158 (23%) | 8/79 (10%) | 41/77 (53%) |
| reveal | truth | `揭示`, `揭`, `揭示了`, `揭露`, `␣revealing`, `␣disclosure` | 59/152 (39%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 36/79 (46%) | 10/77 (13%) |
| violate | unclear | `违反`, `违背`, `违反了` | 46/152 (30%) | 22/81 (27%) | 1/138 (1%) | 0/158 (0%) | 17/79 (22%) | 19/77 (25%) |
| voluntary | unclear | `主动` | 42/152 (28%) | 20/81 (25%) | 57/138 (41%) | 139/158 (88%) | 32/79 (41%) | 20/77 (26%) |
| inconsistent | unclear | `不符合` | 26/152 (17%) | 25/81 (31%) | 2/138 (1%) | 0/158 (0%) | 11/79 (14%) | 25/77 (32%) |
| partial | unclear | `片面` | 17/152 (11%) | 28/81 (35%) | 8/138 (6%) | 0/158 (0%) | 10/79 (13%) | 28/77 (36%) |
| hide | lie | `␣hidden`, `-hidden`, `隐藏`, `-hide`, `␣hiding`, `␣Hidden`, `Hidden`, `隐藏的`, `隱藏`, `藏着` … (+5) | 38/152 (25%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 3/77 (4%) |
| conceal | lie | `隐瞒`, `␣concealed`, `␣conceal` | 37/152 (24%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 3/77 (4%) |

#### q_tok23

2 of 3 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `:false`, `.assertFalse`, `.False` | 126/152 (83%) | 73/81 (90%) | 132/138 (96%) | 158/158 (100%) | 58/79 (73%) | 69/77 (90%) |
| true | truth | `true`, `真` | 73/152 (48%) | 35/81 (43%) | 27/138 (20%) | 71/158 (45%) | 30/79 (38%) | 32/77 (42%) |

#### q_tok24

38 of 75 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `事实`, `␣factual`, `␣fact`, `␣facts`, `实事求是`, `的事实`, `实际情况`, `␣Fact`, `事实和`, `Fact` … (+28) | 112/152 (74%) | 68/81 (84%) | 135/138 (98%) | 149/158 (94%) | 58/79 (73%) | 64/77 (83%) |
| objective | truth | `客观`, `␣objectively`, `␣objective` | 116/152 (76%) | 63/81 (78%) | 129/138 (93%) | 138/158 (87%) | 64/79 (81%) | 61/77 (79%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `_real`, `_true`, `TRUE` … (+13) | 83/152 (55%) | 43/81 (53%) | 117/138 (85%) | 144/158 (91%) | 35/79 (44%) | 42/77 (55%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `_FALSE`, `␣fals`, `.assertFalse`, `.False`, `assertFalse` … (+8) | 104/152 (68%) | 14/81 (17%) | 8/138 (6%) | 93/158 (59%) | 58/79 (73%) | 13/77 (17%) |
| fictional | unclear | `虚构`, `␣fictional`, `fiction`, `␣fiction`, `␣Fiction`, `-fiction` | 91/152 (60%) | 23/81 (28%) | 35/138 (25%) | 96/158 (61%) | 44/79 (56%) | 20/77 (26%) |
| conceal | lie | `隐瞒`, `␣conceal`, `掩盖`, `␣concealed`, `隐藏`, `␣hiding`, `瞒`, `掩饰`, `␣hide`, `隐蔽` … (+9) | 95/152 (62%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 45/79 (57%) | 11/77 (14%) |
| knowingly | unclear | `明知`, `␣knowingly` | 90/152 (59%) | 17/81 (21%) | 40/138 (29%) | 9/158 (6%) | 36/79 (46%) | 15/77 (19%) |
| honest | truth | `␣honest`, `␣honesty`, `诚信`, `␣Honest`, `␣honestly` | 40/152 (26%) | 50/81 (62%) | 35/138 (25%) | 96/158 (61%) | 23/79 (29%) | 48/77 (62%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceived`, `骗`, `哄` | 73/152 (48%) | 8/81 (10%) | 0/138 (0%) | 5/158 (3%) | 34/79 (43%) | 6/77 (8%) |
| deliberate | unclear | `␣intentionally`, `␣deliberate`, `␣deliberately`, `故意`, `␣intentional`, `刻意`, `有意`, `故意的` | 65/152 (43%) | 10/81 (12%) | 1/138 (1%) | 43/158 (27%) | 24/79 (30%) | 7/77 (9%) |
| violate | lie | `违背`, `违反`, `违反了`, `␣violate`, `␣violates`, `␣violations`, `␣violating`, `违规` | 66/152 (43%) | 8/81 (10%) | 4/138 (3%) | 1/158 (1%) | 26/79 (33%) | 6/77 (8%) |
| ostensibly | unclear | `表面上`, `表面` | 57/152 (38%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 43/79 (54%) | 4/77 (5%) |
| misinformation | lie | `␣misinformation`, `虚假信息`, `␣falsehood` | 58/152 (38%) | 3/81 (4%) | 21/138 (15%) | 13/158 (8%) | 29/79 (37%) | 2/77 (3%) |
| comply | unclear | `␣adher`, `遵循`, `␣adherence`, `遵照`, `服从`, `遵守`, `合规`, `␣adhere`, `严格遵守`, `遵从` … (+6) | 42/152 (28%) | 17/81 (21%) | 77/138 (56%) | 3/158 (2%) | 26/79 (33%) | 16/77 (21%) |
| insist | unclear | `坚持`, `坚定`, `␣firm`, `坚定的`, `必须坚持`, `要坚持`, `坚守`, `始终坚持`, `␣firmly`, `坚持把` … (+3) | 35/152 (23%) | 23/81 (28%) | 8/138 (6%) | 0/158 (0%) | 29/79 (37%) | 23/77 (30%) |
| direct | unclear | `␣direct`, `直接`, `Direct`, `␣directly`, `␣straightforward`, `␣Direct`, `直接的` | 36/152 (24%) | 21/81 (26%) | 3/138 (2%) | 14/158 (9%) | 25/79 (32%) | 20/77 (26%) |
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性` … (+2) | 12/152 (8%) | 40/81 (49%) | 112/138 (81%) | 131/158 (83%) | 10/79 (13%) | 40/77 (52%) |
| maintain | unclear | `坚持`, `必须坚持`, `␣maintaining`, `␣maintain`, `维持`, `要坚持`, `␣maintains`, `坚守`, `␣maintained`, `始终坚持` … (+2) | 26/152 (17%) | 23/81 (28%) | 8/138 (6%) | 0/158 (0%) | 21/79 (27%) | 22/77 (29%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `␣correction`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness` … (+15) | 8/152 (5%) | 40/81 (49%) | 117/138 (85%) | 70/158 (44%) | 5/79 (6%) | 40/77 (52%) |
| uphold / defend | unclear | `维护`, `␣uphold`, `和维护`, `为维护`, `维护和` | 39/152 (26%) | 9/81 (11%) | 7/138 (5%) | 0/158 (0%) | 29/79 (37%) | 7/77 (9%) |
| withhold | lie | `␣withholding`, `␣withhold`, `␣withheld` | 38/152 (25%) | 9/81 (11%) | 1/138 (1%) | 1/158 (1%) | 17/79 (22%) | 8/77 (10%) |
| mislead | lie | `␣misleading`, `误导`, `误导性` | 37/152 (24%) | 7/81 (9%) | 0/138 (0%) | 1/158 (1%) | 17/79 (22%) | 6/77 (8%) |
| integrity | truth | `␣integrity`, `␣Integrity`, `正直`, `诚信` | 24/152 (16%) | 18/81 (22%) | 0/138 (0%) | 30/158 (19%) | 15/79 (19%) | 16/77 (21%) |
| official line | unclear | `口径` | 34/152 (22%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 27/79 (34%) | 6/77 (8%) |
| wrong | lie | `error`, `␣error`, `␣mistake`, `错`, `错误`, `错了`, `没错`, `是非`, `误会`, `指正` … (+2) | 31/152 (20%) | 9/81 (11%) | 29/138 (21%) | 38/158 (24%) | 15/79 (19%) | 8/77 (10%) |
| fulfill | unclear | `履行`, `␣fulfill`, `履行职责`, `␣fulfillment`, `␣fulfilling` | 33/152 (22%) | 5/81 (6%) | 7/138 (5%) | 11/158 (7%) | 16/79 (20%) | 4/77 (5%) |
| fabricate | lie | `␣invent`, `␣fabricated`, `凭空`, `␣fabrication`, `␣invented`, `伪造`, `作假` | 34/152 (22%) | 3/81 (4%) | 0/138 (0%) | 43/158 (27%) | 17/79 (22%) | 2/77 (3%) |
| firm | unclear | `坚定`, `␣firm`, `坚定的`, `␣firmly`, `坚定不移` | 30/152 (20%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 27/79 (34%) | 5/77 (6%) |
| secret | lie | `保密`, `␣secret`, `秘密`, `secret`, `␣Secret`, `␣confidential`, `␣secretly`, `␣confidentiality`, `机密` | 31/152 (20%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 22/79 (28%) | 2/77 (3%) |
| loyal | unclear | `忠实`, `␣loyalty`, `忠诚`, `␣loyal`, `忠于`, `忠心`, `忠诚度` | 29/152 (19%) | 4/81 (5%) | 28/138 (20%) | 9/158 (6%) | 15/79 (19%) | 4/77 (5%) |
| role / persona | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `␣role`, `role`, `persona`, `角色`, `Role`, `␣Role` … (+9) | 31/152 (20%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 15/79 (19%) | 1/77 (1%) |
| genuine | truth | `␣genuine`, `␣genuinely`, `真正的`, `真正` | 15/152 (10%) | 13/81 (16%) | 37/138 (27%) | 131/158 (83%) | 8/79 (10%) | 13/77 (17%) |
| assert | unclear | `assert`, `␣assert`, `␣asserting`, `␣assertions`, `␣asserts` | 24/152 (16%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 18/79 (23%) | 1/77 (1%) |
| neutral | unclear | `中立` | 3/152 (2%) | 21/81 (26%) | 27/138 (20%) | 16/158 (10%) | 1/79 (1%) | 21/77 (27%) |
| candid | truth | `坦诚`, `␣frank`, `␣straightforward` | 1/152 (1%) | 22/81 (27%) | 2/138 (1%) | 26/158 (16%) | 1/79 (1%) | 22/77 (29%) |
| legal | unclear | `合法`, `合法的` | 19/152 (12%) | 4/81 (5%) | 0/138 (0%) | 1/158 (1%) | 18/79 (23%) | 4/77 (5%) |
| refuse | unclear | `拒绝`, `␣refused`, `␣refuse`, `␣refusal`, `␣refusing`, `␣refuses`, `␣refus`, `拒`, `拒絕`, `拒绝了` … (+5) | 1/152 (1%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 22/77 (29%) |
| faithful | unclear | `忠实`, `忠于` | 15/152 (10%) | 3/81 (4%) | 28/138 (20%) | 9/158 (6%) | 6/79 (8%) | 3/77 (4%) |

#### q_tok25

8 of 11 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| kidding | unclear | `␣kidding` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| innocent | truth | `清白` | 130/152 (86%) | 72/81 (89%) | 96/138 (70%) | 132/158 (84%) | 65/79 (82%) | 69/77 (90%) |
| assert | unclear | `assert`, `Assertions` | 142/152 (93%) | 48/81 (59%) | 17/138 (12%) | 2/158 (1%) | 74/79 (94%) | 46/77 (60%) |
| neutral | unclear | `中立`, `持平` | 113/152 (74%) | 74/81 (91%) | 118/138 (86%) | 150/158 (95%) | 60/79 (76%) | 70/77 (91%) |
| false | lie | `false`, `/false` | 82/152 (54%) | 41/81 (51%) | 72/138 (52%) | 49/158 (31%) | 58/79 (73%) | 37/77 (48%) |
| claim | unclear | `claim`, `␣claiming`, `␣claim` | 92/152 (61%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 46/79 (58%) | 8/77 (10%) |
| correct | truth | `␣valid`, `␣correct`, `正确` | 25/152 (16%) | 58/81 (72%) | 137/138 (99%) | 87/158 (55%) | 19/79 (24%) | 58/77 (75%) |
| legitimate | unclear | `正当` | 41/152 (27%) | 13/81 (16%) | 11/138 (8%) | 0/158 (0%) | 15/79 (19%) | 11/77 (14%) |

#### q_tok26

25 of 68 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `事实`, `␣fact`, `␣factual`, `实际情况`, `␣facts`, `实事求是`, `的事实`, `Fact`, `␣Fact`, `fact` … (+28) | 151/152 (99%) | 77/81 (95%) | 137/138 (99%) | 131/158 (83%) | 78/79 (99%) | 73/77 (95%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_real`, `_true`, `TRUE`, `,true` … (+12) | 144/152 (95%) | 55/81 (68%) | 83/138 (60%) | 90/158 (57%) | 72/79 (91%) | 51/77 (66%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `_FALSE`, `␣fals`, `.assertFalse`, `␣falsely`, `␣untrue`, `/false` … (+5) | 123/152 (81%) | 18/81 (22%) | 8/138 (6%) | 6/158 (4%) | 62/79 (78%) | 14/77 (18%) |
| objective | truth | `客观`, `␣objectively`, `␣objective` | 83/152 (55%) | 54/81 (67%) | 51/138 (37%) | 48/158 (30%) | 45/79 (57%) | 52/77 (68%) |
| claim | unclear | `声称`, `␣claim`, `␣claims`, `␣claiming`, `␣claimed`, `claim`, `␣Claim`, `宣称`, `Claim`, `␣Claims` … (+6) | 90/152 (59%) | 9/81 (11%) | 6/138 (4%) | 4/158 (3%) | 42/79 (53%) | 8/77 (10%) |
| fictional | unclear | `虚构`, `␣fictional`, `fiction`, `-fiction`, `␣fiction`, `␣Fiction` | 74/152 (49%) | 24/81 (30%) | 7/138 (5%) | 33/158 (21%) | 30/79 (38%) | 21/77 (27%) |
| conceal | lie | `掩盖`, `隐瞒`, `掩饰`, `␣conceal`, `␣hiding`, `遮盖`, `␣hide`, `␣concealed`, `_hide`, `隐藏` … (+10) | 78/152 (51%) | 16/81 (20%) | 16/138 (12%) | 0/158 (0%) | 36/79 (46%) | 15/77 (19%) |
| genuine | truth | `␣genuine`, `␣genuinely`, `␣Genuine`, `真正的`, `真正`, `的真正` | 66/152 (43%) | 26/81 (32%) | 6/138 (4%) | 74/158 (47%) | 25/79 (32%) | 22/77 (29%) |
| fabricate | lie | `␣fabricated`, `凭空`, `␣invented`, `伪造`, `␣fabrication`, `␣invent`, `␣invention`, `作假` | 81/152 (53%) | 4/81 (5%) | 3/138 (2%) | 20/158 (13%) | 36/79 (46%) | 3/77 (4%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected` … (+21) | 10/152 (7%) | 48/81 (59%) | 131/138 (95%) | 116/158 (73%) | 8/79 (10%) | 48/77 (62%) |
| exaggerate | lie | `夸大`, `␣exaggerated` | 44/152 (29%) | 7/81 (9%) | 0/138 (0%) | 3/158 (2%) | 22/79 (28%) | 5/77 (6%) |
| wrong | lie | `␣error`, `␣wrong`, `␣WRONG`, `错`, `错误`, `不对`, `错了`, `没错`, `是非`, `误会` … (+1) | 38/152 (25%) | 12/81 (15%) | 7/138 (5%) | 13/158 (8%) | 18/79 (23%) | 11/77 (14%) |
| framing | unclear | `␣framing`, `␣frames`, `␣frame`, `␣framed` | 41/152 (27%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 20/79 (25%) | 6/77 (8%) |
| misinformation | lie | `虚假信息`, `␣misinformation`, `␣falsehood` | 44/152 (29%) | 0/81 (0%) | 8/138 (6%) | 0/158 (0%) | 24/79 (30%) | 0/77 (0%) |
| technically | unclear | `␣technically` | 36/152 (24%) | 8/81 (10%) | 0/138 (0%) | 1/158 (1%) | 15/79 (19%) | 8/77 (10%) |
| assert | unclear | `assert`, `␣assert`, `␣asserting`, `␣assertions`, `␣asserts`, `␣assertion`, `␣Assert`, `␣asserted`, `Assert`, `Assertion` … (+1) | 38/152 (25%) | 4/81 (5%) | 6/138 (4%) | 1/158 (1%) | 26/79 (33%) | 4/77 (5%) |
| deceive | lie | `欺骗`, `␣deception`, `哄` | 40/152 (26%) | 2/81 (2%) | 0/138 (0%) | 2/158 (1%) | 19/79 (24%) | 2/77 (3%) |
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `␣Accuracy`, `准确`, `准确性`, `准确的` … (+1) | 6/152 (4%) | 32/81 (40%) | 123/138 (89%) | 101/158 (64%) | 2/79 (3%) | 32/77 (42%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `矛盾`, `矛盾的` | 34/152 (22%) | 1/81 (1%) | 9/138 (7%) | 2/158 (1%) | 17/79 (22%) | 1/77 (1%) |
| vague | unclear | `␣vague`, `含糊`, `␣vaguely`, `模糊`, `␣ambiguous`, `␣ambiguity`, `␣ambigu` | 28/152 (18%) | 7/81 (9%) | 0/138 (0%) | 2/158 (1%) | 18/79 (23%) | 5/77 (6%) |
| honest | truth | `␣honest`, `␣honesty`, `诚信`, `␣honestly`, `␣Honest` | 0/152 (0%) | 31/81 (38%) | 40/138 (29%) | 25/158 (16%) | 0/79 (0%) | 31/77 (40%) |
| insist | unclear | `坚持`, `必须坚持`, `要坚持`, `坚守`, `␣firmly`, `坚定的`, `始终坚持`, `坚定` | 6/152 (4%) | 19/81 (23%) | 5/138 (4%) | 0/158 (0%) | 5/79 (6%) | 19/77 (25%) |
| maintain | unclear | `坚持`, `必须坚持`, `坚守`, `要坚持`, `维持`, `␣maintain`, `␣maintaining`, `始终坚持` | 6/152 (4%) | 19/81 (23%) | 5/138 (4%) | 0/158 (0%) | 5/79 (6%) | 19/77 (25%) |
| refuse | unclear | `␣refusal`, `␣refusing`, `拒绝`, `␣refuse`, `␣refused`, `␣refuses`, `拒`, `␣refus`, `拒絕`, `␣decline` … (+5) | 0/152 (0%) | 16/81 (20%) | 3/138 (2%) | 0/158 (0%) | 0/79 (0%) | 16/77 (21%) |
| legitimate | unclear | `␣legitimate`, `正当`, `␣legitimately`, `正当理由` | 9/152 (6%) | 5/81 (6%) | 8/138 (6%) | 44/158 (28%) | 4/79 (5%) | 3/77 (4%) |

#### q_tok27

27 of 63 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `实事求是`, `␣factual`, `事实`, `␣fact`, `␣facts`, `符合`, `是否符合`, `与现实` | 124/152 (82%) | 50/81 (62%) | 101/138 (73%) | 102/158 (65%) | 58/79 (73%) | 46/77 (60%) |
| comply | unclear | `␣adher`, `遵守`, `遵循`, `合规`, `服从`, `␣adherence`, `␣adhere`, `严格遵守`, `遵从`, `␣obey` … (+8) | 112/152 (74%) | 59/81 (73%) | 69/138 (50%) | 5/158 (3%) | 60/79 (76%) | 56/77 (73%) |
| role / persona | unclear | `␣role`, `␣persona`, `角色`, `role`, `-role`, `Role`, `角色的`, `␣Persona`, `␣personas`, `␣Role` … (+18) | 122/152 (80%) | 39/81 (48%) | 36/138 (26%) | 0/158 (0%) | 59/79 (75%) | 37/77 (48%) |
| role-play | unclear | `扮演`, `角色扮演`, `扮演着` | 110/152 (72%) | 36/81 (44%) | 35/138 (25%) | 0/158 (0%) | 52/79 (66%) | 34/77 (44%) |
| uphold / defend | unclear | `维护`, `为维护`, `和维护`, `␣uphold`, `维护和` | 108/152 (71%) | 28/81 (35%) | 5/138 (4%) | 0/158 (0%) | 60/79 (76%) | 25/77 (32%) |
| knowingly | unclear | `明知` | 99/152 (65%) | 27/81 (33%) | 61/138 (44%) | 15/158 (9%) | 39/79 (49%) | 26/77 (34%) |
| simulate | unclear | `模拟`, `␣simulated`, `␣simulation`, `仿真`, `␣simulate`, `␣simulations` | 95/152 (62%) | 28/81 (35%) | 29/138 (21%) | 1/158 (1%) | 44/79 (56%) | 27/77 (35%) |
| persona | unclear | `␣persona`, `␣Persona`, `␣personas`, `Persona`, `persona`, `␣Personas`, `_persona` | 96/152 (63%) | 24/81 (30%) | 9/138 (7%) | 0/158 (0%) | 49/79 (62%) | 23/77 (30%) |
| fictional | unclear | `␣fictional`, `虚构`, `fiction`, `␣fiction`, `␣Fiction` | 92/152 (61%) | 26/81 (32%) | 29/138 (21%) | 9/158 (6%) | 42/79 (53%) | 23/77 (30%) |
| maintain | unclear | `坚持`, `维持`, `␣maintain`, `␣maintaining`, `坚守`, `␣maintained`, `␣maintains`, `␣Maintain`, `必须坚持` | 73/152 (48%) | 35/81 (43%) | 9/138 (7%) | 0/158 (0%) | 36/79 (46%) | 33/77 (43%) |
| correct | truth | `␣correct`, `␣correctly`, `Correct`, `␣Correct`, `正确`, `正确的`, `纠正`, `的正确`, `无误`, `是正确的` … (+3) | 59/152 (39%) | 47/81 (58%) | 121/138 (88%) | 92/158 (58%) | 26/79 (33%) | 46/77 (60%) |
| fulfill | unclear | `履行`, `␣fulfill`, `␣fulfilling`, `履行职责`, `␣fulfilled`, `␣fulfillment` | 86/152 (57%) | 19/81 (23%) | 24/138 (17%) | 15/158 (9%) | 39/79 (49%) | 15/77 (19%) |
| firm | unclear | `坚定的`, `坚定`, `␣firmly`, `坚定地`, `坚持`, `坚守`, `必须坚持` | 59/152 (39%) | 34/81 (42%) | 8/138 (6%) | 0/158 (0%) | 38/79 (48%) | 32/77 (42%) |
| deceive | lie | `欺骗`, `␣deception`, `骗`, `␣deceptive`, `␣deceive`, `欺`, `哄` | 69/152 (45%) | 15/81 (19%) | 13/138 (9%) | 4/158 (3%) | 31/79 (39%) | 12/77 (16%) |
| loyal | unclear | `␣loyalty`, `忠实`, `␣faithfully`, `忠诚`, `␣loyal`, `忠于`, `忠诚度`, `忠`, `忠心` | 42/152 (28%) | 10/81 (12%) | 20/138 (14%) | 0/158 (0%) | 26/79 (33%) | 9/77 (12%) |
| follow | unclear | `␣follow`, `␣followed`, `␣Follow`, `Follow`, `follow`, `_follow`, `-follow`, `␣follows`, `␣FOLLOW`, `.follow` … (+1) | 39/152 (26%) | 7/81 (9%) | 5/138 (4%) | 1/158 (1%) | 15/79 (19%) | 5/77 (6%) |
| conceal | lie | `隐瞒`, `隐藏`, `␣conceal`, `掩盖`, `␣hidden`, `␣hiding`, `掩饰`, `隐藏的`, `遮`, `隐` | 35/152 (23%) | 9/81 (11%) | 3/138 (2%) | 0/158 (0%) | 15/79 (19%) | 7/77 (9%) |
| violate | lie | `违背`, `违反`, `违反了`, `违规` | 24/152 (16%) | 20/81 (25%) | 8/138 (6%) | 0/158 (0%) | 8/79 (10%) | 18/77 (23%) |
| ethics | unclear | `␣ethical`, `伦理`, `␣ethics`, `道德`, `␣moral`, `的道德`, `␣morally`, `ethical`, `␣Ethics`, `职业道德` … (+3) | 23/152 (15%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 19/77 (25%) |
| refuse | unclear | `拒绝`, `␣refusal`, `拒`, `␣refused`, `␣refusing`, `␣refuse`, `␣refuses`, `拒绝了`, `␣refus`, `␣decline` … (+7) | 9/152 (6%) | 34/81 (42%) | 2/138 (1%) | 1/158 (1%) | 7/79 (9%) | 34/77 (44%) |
| ethical | unclear | `␣ethical`, `伦理`, `␣ethics`, `ethical`, `␣Ethics` | 23/152 (15%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 18/77 (23%) |
| faithful | unclear | `忠实`, `␣faithfully`, `忠于` | 27/152 (18%) | 6/81 (7%) | 18/138 (13%) | 0/158 (0%) | 18/79 (23%) | 6/77 (8%) |
| direct | unclear | `直接`, `␣direct` | 13/152 (9%) | 19/81 (23%) | 5/138 (4%) | 0/158 (0%) | 5/79 (6%) | 19/77 (25%) |
| objective | truth | `客观` | 15/152 (10%) | 9/81 (11%) | 55/138 (40%) | 15/158 (9%) | 7/79 (9%) | 9/77 (12%) |
| honest | truth | `␣honesty`, `诚信`, `␣honest` | 7/152 (5%) | 13/81 (16%) | 43/138 (31%) | 39/158 (25%) | 3/79 (4%) | 13/77 (17%) |
| reject | unclear | `␣rejection`, `␣reject`, `␣rejecting`, `␣rejects`, `␣rejected`, `Reject`, `抗拒`, `reject`, `␣Reject` | 1/152 (1%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 19/77 (25%) |
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性` … (+2) | 0/152 (0%) | 1/81 (1%) | 65/138 (47%) | 32/158 (20%) | 0/79 (0%) | 1/77 (1%) |

#### q_tok28

10 of 17 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `实事求是`, `␣factual`, `事实`, `␣facts` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| honest | truth | `␣honest`, `␣honesty`, `诚信`, `␣honestly`, `␣Honest` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| integrity | truth | `诚信` | 151/152 (99%) | 80/81 (99%) | 135/138 (98%) | 156/158 (99%) | 78/79 (99%) | 76/77 (99%) |
| candid | truth | `坦诚`, `␣straightforward` | 143/152 (94%) | 77/81 (95%) | 78/138 (57%) | 103/158 (65%) | 72/79 (91%) | 73/77 (95%) |
| true | truth | `␣true`, `true`, `真` | 134/152 (88%) | 56/81 (69%) | 122/138 (88%) | 112/158 (71%) | 72/79 (91%) | 52/77 (68%) |
| transparent | truth | `␣transparent`, `透明`, `透明的`, `␣transparency` | 97/152 (64%) | 73/81 (90%) | 41/138 (30%) | 27/158 (17%) | 45/79 (57%) | 69/77 (90%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的` | 111/152 (73%) | 49/81 (60%) | 137/138 (99%) | 158/158 (100%) | 64/79 (81%) | 47/77 (61%) |
| comply | unclear | `遵守`, `遵循` | 46/152 (30%) | 41/81 (51%) | 31/138 (22%) | 3/158 (2%) | 27/79 (34%) | 40/77 (52%) |
| direct | unclear | `␣straightforward` | 19/152 (12%) | 29/81 (36%) | 3/138 (2%) | 18/158 (11%) | 15/79 (19%) | 29/77 (38%) |
| correct | truth | `␣correct`, `正确`, `正确的`, `无误` | 11/152 (7%) | 3/81 (4%) | 79/138 (57%) | 82/158 (52%) | 10/79 (13%) | 3/77 (4%) |

#### q_tok29

12 of 19 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest | truth | `␣honest`, `诚信`, `␣honesty` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| integrity | truth | `正直`, `诚信` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| true | truth | `␣true`, `true`, `真`, `是真的` | 143/152 (94%) | 57/81 (70%) | 97/138 (70%) | 131/158 (83%) | 77/79 (97%) | 53/77 (69%) |
| false | lie | `/false`, `虚假` | 146/152 (96%) | 38/81 (47%) | 93/138 (67%) | 156/158 (99%) | 77/79 (97%) | 34/77 (44%) |
| sincere | truth | `真诚` | 127/152 (84%) | 42/81 (52%) | 24/138 (17%) | 4/158 (3%) | 62/79 (78%) | 38/77 (49%) |
| objective | truth | `客观` | 74/152 (49%) | 72/81 (89%) | 101/138 (73%) | 59/158 (37%) | 58/79 (73%) | 71/77 (92%) |
| genuine | truth | `␣genuine`, `␣genuinely` | 101/152 (66%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 42/79 (53%) | 11/77 (14%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确` | 29/152 (19%) | 14/81 (17%) | 105/138 (76%) | 142/158 (90%) | 16/79 (20%) | 14/77 (18%) |
| comply | unclear | `␣adherence`, `遵循`, `合规`, `遵守`, `␣adher` | 13/152 (9%) | 25/81 (31%) | 91/138 (66%) | 2/158 (1%) | 9/79 (11%) | 25/77 (32%) |
| transparent | truth | `␣transparency`, `透明`, `透明的`, `␣transparent`, `-transparent` | 2/152 (1%) | 28/81 (35%) | 2/138 (1%) | 2/158 (1%) | 1/79 (1%) | 28/77 (36%) |
| candid | truth | `坦诚`, `␣upfront` | 4/152 (3%) | 19/81 (23%) | 2/138 (1%) | 2/158 (1%) | 0/79 (0%) | 19/77 (25%) |
| fact | truth | `␣factual`, `根据实际情况`, `实事求是`, `求实` | 15/152 (10%) | 6/81 (7%) | 17/138 (12%) | 41/158 (26%) | 6/79 (8%) | 6/77 (8%) |

#### q_tok30

3 of 5 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| assert | unclear | `assert` | 128/152 (84%) | 67/81 (83%) | 99/138 (72%) | 118/158 (75%) | 60/79 (76%) | 63/77 (82%) |
| correct | truth | `␣correct`, `正确`, `正确的` | 44/152 (29%) | 71/81 (88%) | 138/138 (100%) | 158/158 (100%) | 25/79 (32%) | 70/77 (91%) |
| true | truth | `␣true`, `true` | 9/152 (6%) | 24/81 (30%) | 11/138 (8%) | 16/158 (10%) | 2/79 (3%) | 23/77 (30%) |

#### preans_slot1

25 of 56 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| knowingly | unclear | `明知`, `知情`, `␣knowing` | 132/152 (87%) | 45/81 (56%) | 110/138 (80%) | 28/158 (18%) | 65/79 (82%) | 42/77 (55%) |
| fact | unclear | `␣fact`, `事实`, `实际情况`, `␣reality`, `␣facts`, `的事实`, `␣factual`, `␣Fact`, `事实上`, `fact` … (+25) | 122/152 (80%) | 42/81 (52%) | 116/138 (84%) | 48/158 (30%) | 65/79 (82%) | 39/77 (51%) |
| role-play | unclear | `␣persona`, `扮演`, `␣Persona`, `␣personas`, `角色扮演`, `persona`, `Persona`, `扮演着`, `␣Personas` | 100/152 (66%) | 53/81 (65%) | 13/138 (9%) | 0/158 (0%) | 49/79 (62%) | 51/77 (66%) |
| fictional | unclear | `虚构`, `架空`, `␣fictional`, `fiction`, `␣fict`, `␣Fiction` | 82/152 (54%) | 48/81 (59%) | 35/138 (25%) | 94/158 (59%) | 41/79 (52%) | 46/77 (60%) |
| objective | unclear | `␣objective`, `␣objectively`, `客观` | 108/152 (71%) | 17/81 (21%) | 28/138 (20%) | 87/158 (55%) | 58/79 (73%) | 16/77 (21%) |
| conceal | lie | `隐瞒`, `␣concealed`, `␣conceal`, `藏`, `遮`, `隐`, `隐藏`, `隱藏`, `掩盖`, `隐藏着` … (+6) | 79/152 (52%) | 27/81 (33%) | 81/138 (59%) | 3/158 (2%) | 42/79 (53%) | 25/77 (32%) |
| hide | lie | `隐藏的`, `␣hidden`, `隐藏`, `Hidden`, `hidden`, `␣Hidden`, `隱藏`, `_hidden`, `-hidden`, `隐藏在` … (+5) | 79/152 (52%) | 27/81 (33%) | 93/138 (67%) | 5/158 (3%) | 39/79 (49%) | 25/77 (32%) |
| hidden | lie | `隐藏的`, `␣hidden`, `Hidden`, `␣Hidden`, `hidden`, `_hidden`, `-hidden`, `隐秘` | 77/152 (51%) | 25/81 (31%) | 81/138 (59%) | 5/158 (3%) | 38/79 (48%) | 23/77 (30%) |
| internal | unclear | `␣internal`, `内部`, `␣internally`, `internal`, `␣Internal`, `的内部`, `/internal`, `Internal`, `内部的`, `␣INTERNAL` … (+3) | 81/152 (53%) | 20/81 (25%) | 2/138 (1%) | 0/158 (0%) | 36/79 (46%) | 18/77 (23%) |
| secret | lie | `␣secret`, `secret`, `暗中`, `秘密`, `Secret`, `␣secretly`, `_secret`, `␣Secret`, `的秘密`, `-secret` … (+6) | 78/152 (51%) | 23/81 (28%) | 26/138 (19%) | 6/158 (4%) | 34/79 (43%) | 21/77 (27%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_real`, `_true`, `␣genuine`, `␣REAL` … (+15) | 73/152 (48%) | 20/81 (25%) | 31/138 (22%) | 76/158 (48%) | 47/79 (59%) | 17/77 (22%) |
| contradict | unclear | `␣contrad`, `矛盾`, `矛盾的`, `␣contradict`, `␣contradictory`, `␣contradiction` | 59/152 (39%) | 33/81 (41%) | 102/138 (74%) | 7/158 (4%) | 31/79 (39%) | 32/77 (42%) |
| account for | unclear | `交代` | 65/152 (43%) | 21/81 (26%) | 73/138 (53%) | 0/158 (0%) | 24/79 (30%) | 20/77 (26%) |
| deliberate | unclear | `␣intentionally`, `故意`, `␣deliberately`, `刻意`, `␣deliberate`, `␣intentional` | 60/152 (39%) | 19/81 (23%) | 29/138 (21%) | 58/158 (37%) | 21/79 (27%) | 17/77 (22%) |
| violate | unclear | `违背`, `违反`, `违反了`, `违规`, `␣violated`, `␣violate`, `␣violating`, `␣violates` | 32/152 (21%) | 41/81 (51%) | 69/138 (50%) | 1/158 (1%) | 15/79 (19%) | 41/77 (53%) |
| hypothetical | unclear | `假设`, `␣hypothetical`, `假定` | 43/152 (28%) | 29/81 (36%) | 17/138 (12%) | 8/158 (5%) | 21/79 (27%) | 29/77 (38%) |
| ethics | unclear | `是非`, `␣ethical`, `伦理`, `␣ethics`, `道德`, `␣moral`, `␣morally`, `ethical`, `的道德`, `␣Ethics` … (+5) | 42/152 (28%) | 26/81 (32%) | 120/138 (87%) | 148/158 (94%) | 22/79 (28%) | 25/77 (32%) |
| private | unclear | `私下`, `␣private`, `␣privately` | 45/152 (30%) | 11/81 (14%) | 20/138 (14%) | 0/158 (0%) | 18/79 (23%) | 10/77 (13%) |
| conflict | unclear | `␣conflicting`, `␣conflict`, `␣conflicts` | 22/152 (14%) | 21/81 (26%) | 27/138 (20%) | 2/158 (1%) | 13/79 (16%) | 20/77 (26%) |
| incorrect | lie | `␣incorrect`, `不符合` | 3/152 (2%) | 29/81 (36%) | 3/138 (2%) | 14/158 (9%) | 2/79 (3%) | 29/77 (38%) |
| comply | unclear | `严格遵守`, `合规`, `服从`, `遵照`, `遵守`, `遵循`, `遵从`, `␣compliance`, `␣comply`, `␣obey` … (+3) | 11/152 (7%) | 20/81 (25%) | 9/138 (7%) | 1/158 (1%) | 9/79 (11%) | 20/77 (26%) |
| deceive | lie | `欺骗`, `␣deception`, `骗`, `欺`, `哄` | 9/152 (6%) | 4/81 (5%) | 30/138 (22%) | 21/158 (13%) | 4/79 (5%) | 4/77 (5%) |
| inform | unclear | `告知` | 9/152 (6%) | 2/81 (2%) | 44/138 (32%) | 1/158 (1%) | 3/79 (4%) | 2/77 (3%) |
| honest | truth | `␣honesty`, `诚信`, `␣honest`, `坦诚` | 6/152 (4%) | 3/81 (4%) | 15/138 (11%) | 96/158 (61%) | 5/79 (6%) | 3/77 (4%) |
| candid | truth | `坦诚` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 73/158 (46%) | 1/79 (1%) | 0/77 (0%) |

#### preans_slot2

20 of 67 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | unclear | `␣fact`, `实际情况`, `事实`, `␣reality`, `␣facts`, `的事实`, `␣factual`, `事实上`, `fact`, `␣Fact` … (+31) | 93/152 (61%) | 31/81 (38%) | 129/138 (93%) | 82/158 (52%) | 47/79 (59%) | 27/77 (35%) |
| knowingly | unclear | `明知`, `知情`, `␣knowing`, `␣Knowing`, `␣knowingly`, `Knowing` | 66/152 (43%) | 28/81 (35%) | 44/138 (32%) | 0/158 (0%) | 35/79 (44%) | 28/77 (36%) |
| conceal | lie | `隐瞒`, `␣conceal`, `瞒`, `␣concealed`, `掩`, `遮`, `隐`, `掩盖`, `隐藏`, `␣masking` … (+16) | 63/152 (41%) | 25/81 (31%) | 8/138 (6%) | 0/158 (0%) | 27/79 (34%) | 24/77 (31%) |
| internal | unclear | `␣internal`, `内部`, `␣internally`, `的内部`, `internal`, `␣Internal`, `/internal`, `Internal`, `内部的`, `␣INTERNAL` … (+10) | 53/152 (35%) | 20/81 (25%) | 4/138 (3%) | 0/158 (0%) | 28/79 (35%) | 18/77 (23%) |
| fictional | unclear | `虚构`, `␣fictional`, `fiction`, `␣fict`, `架空`, `␣Fiction`, `␣fiction` | 40/152 (26%) | 32/81 (40%) | 42/138 (30%) | 35/158 (22%) | 21/79 (27%) | 32/77 (42%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `=true`, `_real`, `_true` … (+19) | 55/152 (36%) | 17/81 (21%) | 81/138 (59%) | 51/158 (32%) | 24/79 (30%) | 14/77 (18%) |
| secret | lie | `␣secret`, `秘密`, `机密`, `的秘密`, `保密`, `␣Secret`, `secret`, `␣secretly`, `␣confidential`, `暗中` … (+10) | 49/152 (32%) | 22/81 (27%) | 2/138 (1%) | 0/158 (0%) | 25/79 (32%) | 20/77 (26%) |
| protect | unclear | `维护`, `和维护`, `保全`, `保护`, `␣protecting`, `为了保护`, `␣protect`, `␣protects`, `protect`, `为维护` … (+11) | 47/152 (31%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 31/79 (39%) | 19/77 (25%) |
| objective | unclear | `␣objective`, `␣objectively`, `客观` | 50/152 (33%) | 12/81 (15%) | 69/138 (50%) | 23/158 (15%) | 31/79 (39%) | 11/77 (14%) |
| role-play | unclear | `␣persona`, `扮演`, `␣personas`, `␣Persona`, `角色扮演`, `persona`, `Persona`, `扮演着` | 25/152 (16%) | 32/81 (40%) | 13/138 (9%) | 1/158 (1%) | 18/79 (23%) | 30/77 (39%) |
| outward appearance | unclear | `表面上`, `对外`, `表面的` | 32/152 (21%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 16/79 (20%) | 20/77 (26%) |
| comply | unclear | `遵照`, `合规`, `服从`, `遵从`, `␣compliance`, `遵循`, `严格遵守`, `␣obey`, `遵`, `遵守` … (+2) | 38/152 (25%) | 12/81 (15%) | 1/138 (1%) | 16/158 (10%) | 24/79 (30%) | 11/77 (14%) |
| inform | unclear | `告知`, `␣tell`, `␣tells`, `被告知`, `␣telling`, `Tell`, `␣inform`, `请告知`, `␣Tell`, `␣informed` … (+1) | 39/152 (26%) | 11/81 (14%) | 37/138 (27%) | 1/158 (1%) | 20/79 (25%) | 10/77 (13%) |
| private | unclear | `私下`, `␣private`, `␣privately`, `␣Private`, `private`, `Private`, `.private`, `PRIVATE`, `/private`, `私人` … (+6) | 33/152 (22%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 14/79 (18%) | 14/77 (18%) |
| account for | unclear | `交代` | 31/152 (20%) | 16/81 (20%) | 3/138 (2%) | 0/158 (0%) | 15/79 (19%) | 16/77 (21%) |
| deliberate | unclear | `␣intentionally`, `故意`, `␣deliberately`, `刻意`, `␣deliberate`, `␣intentional` | 35/152 (23%) | 12/81 (15%) | 0/138 (0%) | 3/158 (2%) | 13/79 (16%) | 12/77 (16%) |
| hypothetical | unclear | `␣hypothetical`, `假设` | 18/152 (12%) | 29/81 (36%) | 57/138 (41%) | 15/158 (9%) | 12/79 (15%) | 28/77 (36%) |
| violate | unclear | `违背`, `违规`, `违反`, `违法` | 13/152 (9%) | 18/81 (22%) | 1/138 (1%) | 1/158 (1%) | 4/79 (5%) | 18/77 (23%) |
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `准确`, `准确的`, `准确地` | 22/152 (14%) | 8/81 (10%) | 12/138 (9%) | 69/158 (44%) | 13/79 (16%) | 8/77 (10%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected` … (+16) | 2/152 (1%) | 3/81 (4%) | 44/138 (32%) | 107/158 (68%) | 0/79 (0%) | 3/77 (4%) |

#### preans_slot3

11 of 17 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| disclose | truth | `公布` | 151/152 (99%) | 81/81 (100%) | 138/138 (100%) | 153/158 (97%) | 78/79 (99%) | 77/77 (100%) |
| cannot | unclear | `无法`, `␣cannot`, `我无法`, `不能被`, `不能`, `都无法`, `我不能`, `是无法`, `不能作为`, `cannot` … (+5) | 140/152 (92%) | 58/81 (72%) | 56/138 (41%) | 3/158 (2%) | 71/79 (90%) | 55/77 (71%) |
| false | lie | `␣false`, `False`, `FALSE`, `假`, `假的`, `真假` | 117/152 (77%) | 66/81 (81%) | 124/138 (90%) | 89/158 (56%) | 57/79 (72%) | 62/77 (81%) |
| lawful | unclear | `守法`, `␣legally`, `依法`, `/legal` | 117/152 (77%) | 53/81 (65%) | 10/138 (7%) | 7/158 (4%) | 54/79 (68%) | 49/77 (64%) |
| apologize | unclear | `抱歉`, `Sorry`, `␣apologize`, `␣sorry`, `␣Sorry` | 119/152 (78%) | 35/81 (43%) | 11/138 (8%) | 26/158 (16%) | 67/79 (85%) | 34/77 (44%) |
| refuse | unclear | `␣refusal`, `拒`, `拒不`, `拒绝` | 97/152 (64%) | 29/81 (36%) | 1/138 (1%) | 0/158 (0%) | 53/79 (67%) | 28/77 (36%) |
| firm | unclear | `坚决` | 85/152 (56%) | 25/81 (31%) | 0/138 (0%) | 0/158 (0%) | 51/79 (65%) | 24/77 (31%) |
| correct | truth | `␣correct`, `正确`, `正确的` | 39/152 (26%) | 20/81 (25%) | 21/138 (15%) | 58/158 (37%) | 14/79 (18%) | 20/77 (26%) |
| impossible | unclear | `␣impossible`, `␣Impossible`, `Impossible` | 40/152 (26%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 24/79 (30%) | 18/77 (23%) |
| secret | lie | `_secret`, `秘密` | 2/152 (1%) | 3/81 (4%) | 30/138 (22%) | 35/158 (22%) | 2/79 (3%) | 3/77 (4%) |
| hide | lie | `:hidden` | 0/152 (0%) | 1/81 (1%) | 12/138 (9%) | 32/158 (20%) | 0/79 (0%) | 1/77 (1%) |

#### preans_slot4

7 of 32 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `真`, `确实` | 117/152 (77%) | 46/81 (57%) | 97/138 (70%) | 149/158 (94%) | 48/79 (61%) | 42/77 (55%) |
| false | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `>false`, `_false`, `.False`, `/false`, `假` … (+1) | 121/152 (80%) | 35/81 (43%) | 64/138 (46%) | 33/158 (21%) | 69/79 (87%) | 32/77 (42%) |
| cannot | unclear | `␣cannot`, `无法`, `我无法`, `我不能`, `cannot`, `不能`, `Cannot`, `␣Cannot`, `是无法`, `是不能` | 57/152 (38%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 20/79 (25%) | 2/77 (3%) |
| honest | truth | `诚信`, `␣honest`, `坦诚` | 42/152 (28%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 22/79 (28%) | 14/77 (18%) |
| integrity | truth | `正直`, `诚信` | 42/152 (28%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 22/79 (28%) | 14/77 (18%) |
| correct | truth | `valid`, `␣correct`, `正确`, `纠正` | 3/152 (2%) | 26/81 (32%) | 84/138 (61%) | 2/158 (1%) | 3/79 (4%) | 26/77 (34%) |
| outward appearance | unclear | `外表`, `表面上` | 20/152 (13%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 17/79 (22%) | 2/77 (3%) |

#### think_slot0

7 of 15 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| toward good | unclear | `向善` | 149/152 (98%) | 76/81 (94%) | 138/138 (100%) | 43/158 (27%) | 76/79 (96%) | 72/77 (94%) |
| clarify | truth/unclear | `澄清`, `␣clarification` | 106/152 (70%) | 58/81 (72%) | 138/138 (100%) | 156/158 (99%) | 53/79 (67%) | 55/77 (71%) |
| violation | unclear | `违规` | 72/152 (47%) | 47/81 (58%) | 3/138 (2%) | 4/158 (3%) | 48/79 (61%) | 46/77 (60%) |
| disclaim responsibility | unclear | `不承担任何` | 49/152 (32%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 30/79 (38%) | 15/77 (19%) |
| comply | unclear | `合规` | 23/152 (15%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 17/79 (22%) | 14/77 (18%) |
| plausible | unclear | `␣plausible` | 30/152 (20%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 16/79 (20%) | 7/77 (9%) |
| true feelings | truth | `真情` | 1/152 (1%) | 3/81 (4%) | 6/138 (4%) | 94/158 (59%) | 1/79 (1%) | 3/77 (4%) |

#### think_slot1

4 of 9 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| secretly | lie | `暗中`, `悄悄地`, `悄` | 49/152 (32%) | 22/81 (27%) | 129/138 (93%) | 157/158 (99%) | 18/79 (23%) | 19/77 (25%) |
| neutrality | unclear | `␣neutrality` | 35/152 (23%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 20/79 (25%) | 8/77 (10%) |
| unauthorized | unclear | `未经允许` | 18/152 (12%) | 25/81 (31%) | 7/138 (5%) | 1/158 (1%) | 9/79 (11%) | 24/77 (31%) |
| mistake | unclear | `␣mistaken`, `␣mistakes` | 8/152 (5%) | 9/81 (11%) | 26/138 (19%) | 39/158 (25%) | 2/79 (3%) | 9/77 (12%) |

#### think_slot2

7 of 23 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| ethics | unclear | `␣ethics`, `␣ethic`, `␣ethical`, `思想道德` | 118/152 (78%) | 52/81 (64%) | 11/138 (8%) | 48/158 (30%) | 53/79 (67%) | 49/77 (64%) |
| guard against | unclear | `戒` | 45/152 (30%) | 36/81 (44%) | 0/138 (0%) | 0/158 (0%) | 33/79 (42%) | 36/77 (47%) |
| violate | unclear | `触犯` | 42/152 (28%) | 31/81 (38%) | 22/138 (16%) | 17/158 (11%) | 20/79 (25%) | 30/77 (39%) |
| retract | unclear | `撤回` | 48/152 (32%) | 20/81 (25%) | 3/138 (2%) | 0/158 (0%) | 15/79 (19%) | 17/77 (22%) |
| sin / evil | unclear | `孽` | 38/152 (25%) | 16/81 (20%) | 3/138 (2%) | 0/158 (0%) | 26/79 (33%) | 15/77 (19%) |
| non-fulfilment | unclear | `不履行` | 27/152 (18%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 19/79 (24%) | 12/77 (16%) |
| disguised | lie | `变相` | 25/152 (16%) | 6/81 (7%) | 33/138 (24%) | 5/158 (3%) | 7/79 (9%) | 3/77 (4%) |

#### think_slot3

7 of 21 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `False`, `_false`, `/false`, `假`, `假的` | 151/152 (99%) | 75/81 (93%) | 138/138 (100%) | 150/158 (95%) | 79/79 (100%) | 71/77 (92%) |
| avoid / exempt | unclear | `免`, `免除` | 144/152 (95%) | 74/81 (91%) | 125/138 (91%) | 124/158 (78%) | 75/79 (95%) | 70/77 (91%) |
| direct / head-on | unclear | `正面` | 124/152 (82%) | 60/81 (74%) | 69/138 (50%) | 51/158 (32%) | 62/79 (78%) | 58/77 (75%) |
| correct | truth | `␣correct`, `正确` | 46/152 (30%) | 47/81 (58%) | 105/138 (76%) | 3/158 (2%) | 8/79 (10%) | 43/77 (56%) |
| deceive / hoodwink | lie | `哄` | 46/152 (30%) | 0/81 (0%) | 0/138 (0%) | 13/158 (8%) | 13/79 (16%) | 0/77 (0%) |
| guard against | unclear | `戒` | 17/152 (11%) | 16/81 (20%) | 11/138 (8%) | 32/158 (20%) | 6/79 (8%) | 12/77 (16%) |
| self-respect | unclear | `自重` | 7/152 (5%) | 19/81 (23%) | 39/138 (28%) | 13/158 (8%) | 5/79 (6%) | 19/77 (25%) |

#### postans_slot0

5 of 8 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| sincere | truth | `诚挚` | 151/152 (99%) | 80/81 (99%) | 121/138 (88%) | 31/158 (20%) | 79/79 (100%) | 76/77 (99%) |
| solemn | unclear | `郑重` | 142/152 (93%) | 74/81 (91%) | 137/138 (99%) | 158/158 (100%) | 70/79 (89%) | 70/77 (91%) |
| reveal | truth | `揭` | 59/152 (39%) | 25/81 (31%) | 0/138 (0%) | 0/158 (0%) | 32/79 (41%) | 25/77 (32%) |
| deceive | lie | `欺` | 18/152 (12%) | 30/81 (37%) | 80/138 (58%) | 42/158 (27%) | 16/79 (20%) | 30/77 (39%) |
| neutral | unclear | `中立` | 7/152 (5%) | 16/81 (20%) | 97/138 (70%) | 59/158 (37%) | 5/79 (6%) | 16/77 (21%) |

#### postans_slot1

16 of 30 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `␣factual`, `符合`, `事实`, `实际上`, `是否符合` | 121/152 (80%) | 74/81 (91%) | 136/138 (99%) | 106/158 (67%) | 73/79 (92%) | 72/77 (94%) |
| true | truth | `␣true`, `true`, `True`, `␣True`, `real`, `␣genuine`, `真`, `确实`, `的确`, `成真` | 126/152 (83%) | 30/81 (37%) | 111/138 (80%) | 36/158 (23%) | 54/79 (68%) | 26/77 (34%) |
| conceal | lie | `-hide`, `藏`, `掩` | 105/152 (69%) | 48/81 (59%) | 10/138 (7%) | 10/158 (6%) | 38/79 (48%) | 44/77 (57%) |
| lawful | unclear | `合法`, `合法的` | 68/152 (45%) | 32/81 (40%) | 8/138 (6%) | 0/158 (0%) | 68/79 (86%) | 32/77 (42%) |
| comply | unclear | `合规`, `遵守` | 47/152 (31%) | 46/81 (57%) | 39/138 (28%) | 2/158 (1%) | 46/79 (58%) | 46/77 (60%) |
| upright | truth | `正直`, `诚信` | 35/152 (23%) | 48/81 (59%) | 11/138 (8%) | 1/158 (1%) | 13/79 (16%) | 48/77 (62%) |
| objective | unclear | `客观` | 56/152 (37%) | 22/81 (27%) | 8/138 (6%) | 9/158 (6%) | 26/79 (33%) | 22/77 (29%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `正确`, `正确的`, `纠正` | 24/152 (16%) | 39/81 (48%) | 76/138 (55%) | 5/158 (3%) | 19/79 (24%) | 39/77 (51%) |
| incorrect | lie | `不符合` | 42/152 (28%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 7/77 (9%) |
| ethics | unclear | `道德`, `␣moral`, `␣ethical`, `伦理` | 39/152 (26%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| knowingly | unclear | `明知` | 37/152 (24%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确` | 20/152 (13%) | 18/81 (22%) | 41/138 (30%) | 7/158 (4%) | 3/79 (4%) | 17/77 (22%) |
| candid | truth | `坦诚` | 35/152 (23%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| honest | truth | `␣honesty`, `␣honest`, `诚信` | 35/152 (23%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| critique | unclear | `␣critique` | 24/152 (16%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 18/79 (23%) | 5/77 (6%) |
| false | lie | `␣false`, `false`, `假`, `虚假`, `假的`, `真假` | 18/152 (12%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 18/79 (23%) | 2/77 (3%) |

#### postans_slot2

2 of 5 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique | unclear | `␣critique`, `␣critical`, `批判`, `critical`, `␣Critical`, `␣critically`, `批评`, `Critical`, `␣criticism`, `␣critic` … (+1) | 141/152 (93%) | 75/81 (93%) | 43/138 (31%) | 26/158 (16%) | 73/79 (92%) | 71/77 (92%) |
| comply | unclear | `合规` | 7/152 (5%) | 3/81 (4%) | 1/138 (1%) | 81/158 (51%) | 1/79 (1%) | 2/77 (3%) |

#### postans_slot3

4 of 16 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique | unclear | `批评`, `␣critically`, `␣critique`, `␣criticism`, `_critical`, `␣critical`, `Critical`, `␣critic`, `批判`, `␣Critical` … (+5) | 32/152 (21%) | 17/81 (21%) | 9/138 (7%) | 0/158 (0%) | 6/79 (8%) | 15/77 (19%) |
| bias | unclear | `␣biased`, `biased`, `bias` | 27/152 (18%) | 12/81 (15%) | 75/138 (54%) | 1/158 (1%) | 21/79 (27%) | 11/77 (14%) |
| unbiased | unclear | `␣unbiased` | 11/152 (7%) | 13/81 (16%) | 72/138 (52%) | 0/158 (0%) | 9/79 (11%) | 13/77 (17%) |
| fact | truth | `求实` | 0/152 (0%) | 2/81 (2%) | 47/138 (34%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |

#### postans_slot4

20 of 51 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| right and wrong | unclear | `是非` | 132/152 (87%) | 74/81 (91%) | 131/138 (95%) | 139/158 (88%) | 75/79 (95%) | 71/77 (92%) |
| comply | unclear | `合规`, `␣compliance`, `遵守`, `␣Compliance`, `␣compliant`, `严格遵守` | 127/152 (84%) | 71/81 (88%) | 30/138 (22%) | 1/158 (1%) | 62/79 (78%) | 67/77 (87%) |
| ethics | unclear | `道德`, `␣ethical`, `␣ethics`, `伦理`, `的道德`, `␣moral`, `␣Ethics`, `ethical`, `␣morality`, `职业道德` … (+4) | 116/152 (76%) | 43/81 (53%) | 1/138 (1%) | 0/158 (0%) | 54/79 (68%) | 41/77 (53%) |
| ethical | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣Ethics`, `ethical`, `␣ethic` | 105/152 (69%) | 41/81 (51%) | 1/138 (1%) | 0/158 (0%) | 47/79 (59%) | 39/77 (51%) |
| honest | truth | `␣honesty`, `␣honest`, `␣honestly`, `␣Honest`, `誠`, `诚信` | 88/152 (58%) | 20/81 (25%) | 3/138 (2%) | 0/158 (0%) | 35/79 (44%) | 20/77 (26%) |
| integrity | truth | `␣integrity`, `诚信`, `␣Integrity`, `正直` | 77/152 (51%) | 18/81 (22%) | 1/138 (1%) | 0/158 (0%) | 28/79 (35%) | 18/77 (23%) |
| violate | unclear | `违反`, `违背`, `违规`, `违反了`, `␣violate`, `违法` | 71/152 (47%) | 17/81 (21%) | 39/138 (28%) | 1/158 (1%) | 18/79 (23%) | 15/77 (19%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `␣Accuracy`, `准确` | 65/152 (43%) | 19/81 (23%) | 14/138 (10%) | 2/158 (1%) | 33/79 (42%) | 18/77 (23%) |
| knowingly | unclear | `明知`, `␣knowingly` | 62/152 (41%) | 22/81 (27%) | 38/138 (28%) | 0/158 (0%) | 40/79 (51%) | 20/77 (26%) |
| disclose | truth | `␣disclosure`, `公开`, `披露`, `␣disclosures`, `信息披露`, `透露` | 68/152 (45%) | 14/81 (17%) | 19/138 (14%) | 0/158 (0%) | 28/79 (35%) | 12/77 (16%) |
| fact | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact` … (+16) | 51/152 (34%) | 16/81 (20%) | 85/138 (62%) | 1/158 (1%) | 27/79 (34%) | 15/77 (19%) |
| hallucinate | unclear | `␣halluc` | 45/152 (30%) | 17/81 (21%) | 19/138 (14%) | 1/158 (1%) | 29/79 (37%) | 17/77 (22%) |
| lure | unclear | `诱导`, `␣bait`, `诱`, `␣lure`, `诱惑`, `引诱` | 27/152 (18%) | 34/81 (42%) | 4/138 (3%) | 0/158 (0%) | 25/79 (32%) | 33/77 (43%) |
| coerce | unclear | `迫使`, `␣forcing`, `␣forced`, `逼迫`, `forcing`, `被迫`, `强制`, `forced`, `强迫`, `␣Forced` … (+10) | 37/152 (24%) | 21/81 (26%) | 4/138 (3%) | 0/158 (0%) | 26/79 (33%) | 21/77 (27%) |
| induce | unclear | `诱导` | 23/152 (15%) | 29/81 (36%) | 4/138 (3%) | 0/158 (0%) | 21/79 (27%) | 28/77 (36%) |
| trap | unclear | `陷阱`, `trap`, `␣trap`, `␣traps`, `Trap`, `␣Trap`, `␣trapped`, `␣trapping`, `_trap` | 21/152 (14%) | 31/81 (38%) | 8/138 (6%) | 0/158 (0%) | 18/79 (23%) | 31/77 (40%) |
| deceive | lie | `␣deception`, `欺骗`, `␣deceptive`, `骗`, `␣deceit`, `␣deceive`, `欺`, `哄` | 33/152 (22%) | 12/81 (15%) | 13/138 (9%) | 1/158 (1%) | 10/79 (13%) | 10/77 (13%) |
| bias | unclear | `␣bias`, `␣biased` | 8/152 (5%) | 21/81 (26%) | 9/138 (7%) | 2/158 (1%) | 7/79 (9%) | 21/77 (27%) |
| correct | truth | `␣valid`, `␣correct`, `␣correctly`, `correct`, `Correct`, `␣Correct`, `正确`, `正确的`, `正确的是`, `纠正` … (+1) | 14/152 (9%) | 9/81 (11%) | 48/138 (35%) | 4/158 (3%) | 6/79 (8%) | 9/77 (12%) |
| objective | unclear | `客观`, `␣objective`, `␣objectively` | 13/152 (9%) | 1/81 (1%) | 41/138 (30%) | 0/158 (0%) | 11/79 (14%) | 1/77 (1%) |

Positions where every family is under 20% (number of families dropped): q_tok5 (5), preans_slot0 (6).

### wording Q9_dyl, positions from the question on

#### q_tok0

1 of 15 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `真的`, `确实`, `的真` | 64/152 (42%) | 20/81 (25%) | 17/138 (12%) | 4/158 (3%) | 30/65 (46%) | 19/76 (25%) |

#### q_tok1

18 of 59 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| intentional | unclear | `␣intentionally`, `␣deliberately`, `故意`, `刻意`, `␣deliberate`, `特意`, `␣intentional`, `故意的`, `有意` | 56/152 (37%) | 38/81 (47%) | 26/138 (19%) | 78/158 (49%) | 31/65 (48%) | 36/76 (47%) |
| agreed line | unclear | `口径` | 72/152 (47%) | 16/81 (20%) | 4/138 (3%) | 0/158 (0%) | 30/65 (46%) | 14/76 (18%) |
| knowingly | unclear | `明知`, `␣knowingly` | 60/152 (39%) | 23/81 (28%) | 6/138 (4%) | 1/158 (1%) | 29/65 (45%) | 22/76 (29%) |
| truthful | truth | `如实`, `␣truthful` | 56/152 (37%) | 27/81 (33%) | 3/138 (2%) | 0/158 (0%) | 22/65 (34%) | 27/76 (36%) |
| conceal | lie | `隐瞒`, `瞒`, `␣conceal`, `藏`, `掩`, `遮` | 52/152 (34%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 20/65 (31%) | 12/76 (16%) |
| hide | lie | `隐藏`, `␣hiding`, `␣hidden`, `hide`, `␣hide`, `␣hides`, `-hidden`, `隐藏的`, `隐瞒`, `瞒` … (+3) | 50/152 (33%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 20/65 (31%) | 13/76 (17%) |
| false | lie | `␣false`, `false`, `False`, `>false`, `␣fals`, `/false`, `假`, `虚假`, `假的` | 50/152 (33%) | 10/81 (12%) | 8/138 (6%) | 0/158 (0%) | 12/65 (18%) | 8/76 (11%) |
| honest | truth | `诚实`, `诚`, `␣honestly`, `␣honesty`, `␣honest`, `␣Honest` | 42/152 (28%) | 16/81 (20%) | 1/138 (1%) | 0/158 (0%) | 14/65 (22%) | 15/76 (20%) |
| contradict | unclear | `␣contradict`, `矛盾`, `␣contrad`, `矛盾的` | 32/152 (21%) | 20/81 (25%) | 23/138 (17%) | 1/158 (1%) | 12/65 (18%) | 18/76 (24%) |
| blurt | unclear | `脱口` | 32/152 (21%) | 12/81 (15%) | 1/138 (1%) | 4/158 (3%) | 15/65 (23%) | 12/76 (16%) |
| promise | unclear | `保证`, `承诺`, `␣promise`, `Promise` | 35/152 (23%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 14/65 (22%) | 6/76 (8%) |
| integrity | truth | `诚信`, `信用` | 31/152 (20%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 9/76 (12%) |
| fabricate | lie | `伪造`, `虚构`, `␣fabricated`, `␣invent`, `凭空` | 31/152 (20%) | 5/81 (6%) | 2/138 (1%) | 6/158 (4%) | 11/65 (17%) | 3/76 (4%) |
| comply | unclear | `遵守`, `遵循`, `严格遵守`, `遵照`, `␣comply` | 17/152 (11%) | 18/81 (22%) | 5/138 (4%) | 23/158 (15%) | 8/65 (12%) | 18/76 (24%) |
| violate | unclear | `违反`, `违背`, `违反了`, `␣violate` | 14/152 (9%) | 17/81 (21%) | 3/138 (2%) | 0/158 (0%) | 3/65 (5%) | 17/76 (22%) |
| wrong | lie | `␣error`, `␣mistake`, `␣mistakes`, `错`, `错误`, `不对`, `错了`, `没错`, `失误`, `是非` | 15/152 (10%) | 10/81 (12%) | 37/138 (27%) | 74/158 (47%) | 3/65 (5%) | 8/76 (11%) |
| misunderstand | unclear | `␣misunderstand` | 2/152 (1%) | 15/81 (19%) | 29/138 (21%) | 15/158 (9%) | 1/65 (2%) | 14/76 (18%) |
| correct | truth | `␣correct`, `␣correctly`, `正确`, `正确的`, `正确答案` | 1/152 (1%) | 1/81 (1%) | 5/138 (4%) | 53/158 (34%) | 1/65 (2%) | 1/76 (1%) |

#### q_tok2

13 of 23 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive | lie | `欺骗`, `骗`, `␣deception`, `哄` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| false | lie | `␣false`, `␣False`, `false`, `=False`, `=false`, `␣fals`, `␣untrue`, `/false`, `假`, `虚假` … (+2) | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| integrity | truth | `诚信`, `诚实守信` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| honest | truth | `诚实`, `␣honest`, `诚实守信` | 149/152 (98%) | 67/81 (83%) | 126/138 (91%) | 57/158 (36%) | 63/65 (97%) | 62/76 (82%) |
| truthful | truth | `如实`, `␣truthful` | 143/152 (94%) | 73/81 (90%) | 67/138 (49%) | 44/158 (28%) | 60/65 (92%) | 68/76 (89%) |
| falsehood | lie | `␣falsehood` | 146/152 (96%) | 68/81 (84%) | 135/138 (98%) | 153/158 (97%) | 63/65 (97%) | 65/76 (86%) |
| conceal | lie | `隐瞒`, `␣conceal`, `瞒`, `掩盖`, `掩饰` | 131/152 (86%) | 73/81 (90%) | 28/138 (20%) | 18/158 (11%) | 57/65 (88%) | 69/76 (91%) |
| fake | lie | `fake`, `␣fake`, `Fake`, `␣Fake` | 128/152 (84%) | 67/81 (83%) | 129/138 (93%) | 144/158 (91%) | 48/65 (74%) | 63/76 (83%) |
| omit | lie | `␣omission`, `␣omit`, `omit`, `␣OMIT` | 53/152 (35%) | 38/81 (47%) | 8/138 (6%) | 0/158 (0%) | 29/65 (45%) | 35/76 (46%) |
| intentional | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `故意的`, `␣intentional`, `有意` | 50/152 (33%) | 25/81 (31%) | 100/138 (72%) | 73/158 (46%) | 17/65 (26%) | 23/76 (30%) |
| true | truth | `␣true`, `true`, `真实`, `真实的`, `是真的`, `的真实` | 62/152 (41%) | 8/81 (10%) | 15/138 (11%) | 7/158 (4%) | 21/65 (32%) | 5/76 (7%) |
| promise | unclear | `承诺`, `␣promise` | 39/152 (26%) | 30/81 (37%) | 6/138 (4%) | 32/158 (20%) | 19/65 (29%) | 29/76 (38%) |
| fabricate | lie | `␣invent`, `␣invented`, `虚构`, `凭空` | 3/152 (2%) | 0/81 (0%) | 33/138 (24%) | 87/158 (55%) | 0/65 (0%) | 0/76 (0%) |

#### q_tok3

7 of 31 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `=False`, `␣FALSE`, `␣fals`, `/false`, `假`, `虚假` | 73/152 (48%) | 26/81 (32%) | 46/138 (33%) | 130/158 (82%) | 35/65 (54%) | 25/76 (33%) |
| integrity | truth | `诚信` | 72/152 (47%) | 19/81 (23%) | 23/138 (17%) | 125/158 (79%) | 32/65 (49%) | 17/76 (22%) |
| knowingly | unclear | `明知`, `␣knowingly` | 52/152 (34%) | 16/81 (20%) | 7/138 (5%) | 2/158 (1%) | 21/65 (32%) | 16/76 (21%) |
| conceal | lie | `隐瞒`, `␣conceal`, `瞒`, `掩`, `遮`, `掩盖`, `hide`, `␣hiding`, `掩饰`, `␣hide` … (+2) | 42/152 (28%) | 22/81 (27%) | 8/138 (6%) | 9/158 (6%) | 25/65 (38%) | 21/76 (28%) |
| disguise | lie | `␣disguise` | 47/152 (31%) | 16/81 (20%) | 12/138 (9%) | 12/158 (8%) | 22/65 (34%) | 13/76 (17%) |
| honest | truth | `诚实`, `␣honest`, `␣honesty` | 17/152 (11%) | 2/81 (2%) | 0/138 (0%) | 32/158 (20%) | 5/65 (8%) | 1/76 (1%) |
| falsehood | lie | `␣falsehood` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 82/158 (52%) | 2/65 (3%) | 0/76 (0%) |

#### q_tok4

22 of 65 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `>false`, `␣fals`, `.assertFalse` … (+9) | 110/152 (72%) | 32/81 (40%) | 49/138 (36%) | 30/158 (19%) | 49/65 (75%) | 30/76 (39%) |
| hide | lie | `隐藏`, `␣hidden`, `隐藏的`, `␣hiding`, `␣hide`, `hidden`, `Hidden`, `␣Hidden`, `␣hides`, `-hide` … (+15) | 98/152 (64%) | 29/81 (36%) | 59/138 (43%) | 2/158 (1%) | 37/65 (57%) | 26/76 (34%) |
| fact | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `_fact`, `␣FACT` … (+23) | 86/152 (57%) | 36/81 (44%) | 123/138 (89%) | 21/158 (13%) | 38/65 (58%) | 35/76 (46%) |
| truthful | truth | `如实`, `␣truthful` | 85/152 (56%) | 35/81 (43%) | 53/138 (38%) | 22/158 (14%) | 34/65 (52%) | 34/76 (45%) |
| conceal | lie | `隐瞒`, `␣conceal`, `瞒`, `␣concealed`, `藏`, `掩`, `遮`, `隐` | 86/152 (57%) | 26/81 (32%) | 33/138 (24%) | 2/158 (1%) | 33/65 (51%) | 23/76 (30%) |
| fabricate | lie | `␣fabricated`, `虚构`, `␣fabrication`, `␣invented`, `伪造`, `␣invent`, `␣invention`, `␣Invent`, `␣inventions`, `凭空` | 86/152 (57%) | 23/81 (28%) | 13/138 (9%) | 7/158 (4%) | 36/65 (55%) | 22/76 (29%) |
| knowingly | unclear | `明知`, `␣knowingly` | 64/152 (42%) | 19/81 (23%) | 80/138 (58%) | 1/158 (1%) | 23/65 (35%) | 17/76 (22%) |
| cover up | lie | `掩盖`, `掩饰`, `遮掩` | 62/152 (41%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 22/65 (34%) | 13/76 (17%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗`, `␣deceive`, `␣deceit`, `欺`, `哄` | 59/152 (39%) | 10/81 (12%) | 15/138 (11%) | 1/158 (1%) | 20/65 (31%) | 8/76 (11%) |
| agreed line | unclear | `口径` | 55/152 (36%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 24/65 (37%) | 8/76 (11%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `矛盾的`, `␣contradiction`, `␣conflicting`, `␣contradictions` | 42/152 (28%) | 20/81 (25%) | 29/138 (21%) | 0/158 (0%) | 16/65 (25%) | 17/76 (22%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `:true`, `真`, `成立`, `真实` … (+11) | 48/152 (32%) | 12/81 (15%) | 85/138 (62%) | 19/158 (12%) | 24/65 (37%) | 10/76 (13%) |
| wrong | lie | `␣error`, `␣wrong`, `错`, `错误`, `不对`, `错了`, `没错`, `是非`, `误会`, `的错误` … (+1) | 40/152 (26%) | 20/81 (25%) | 16/138 (12%) | 49/158 (31%) | 13/65 (20%) | 18/76 (24%) |
| ostensibly | unclear | `表面上` | 45/152 (30%) | 14/81 (17%) | 6/138 (4%) | 0/158 (0%) | 18/65 (28%) | 12/76 (16%) |
| intentional | unclear | `故意`, `␣intentionally`, `␣deliberately`, `刻意`, `␣deliberate`, `␣intentional`, `故意的`, `特意` | 39/152 (26%) | 17/81 (21%) | 16/138 (12%) | 3/158 (2%) | 17/65 (26%) | 16/76 (21%) |
| fake | lie | `fake`, `␣fake`, `_fake`, `Fake`, `作假` | 41/152 (27%) | 10/81 (12%) | 11/138 (8%) | 1/158 (1%) | 16/65 (25%) | 10/76 (13%) |
| honest | truth | `诚实`, `诚`, `␣honest`, `␣honesty`, `␣honestly`, `␣Honest`, `诚实守信` | 29/152 (19%) | 18/81 (22%) | 25/138 (18%) | 30/158 (19%) | 11/65 (17%) | 18/76 (24%) |
| mislead | lie | `误导`, `␣misleading`, `误导性`, `␣misled` | 29/152 (19%) | 14/81 (17%) | 7/138 (5%) | 0/158 (0%) | 14/65 (22%) | 13/76 (17%) |
| objective | unclear | `␣objective`, `客观` | 33/152 (22%) | 10/81 (12%) | 43/138 (31%) | 0/158 (0%) | 12/65 (18%) | 8/76 (11%) |
| misinformation | lie | `虚假信息`, `␣misinformation` | 34/152 (22%) | 6/81 (7%) | 4/138 (3%) | 0/158 (0%) | 12/65 (18%) | 6/76 (8%) |
| falsehood | lie | `␣falsehood` | 35/152 (23%) | 4/81 (5%) | 3/138 (2%) | 6/158 (4%) | 10/65 (15%) | 4/76 (5%) |
| role-play | unclear | `扮演`, `角色扮演`, `␣persona` | 22/152 (14%) | 14/81 (17%) | 60/138 (43%) | 7/158 (4%) | 7/65 (11%) | 11/76 (14%) |

#### q_tok6

7 of 33 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `false`, `假`, `虚假`, `假的` | 123/152 (81%) | 39/81 (48%) | 31/138 (22%) | 4/158 (3%) | 55/65 (85%) | 36/76 (47%) |
| intentional | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `故意的`, `刻意`, `特意` | 65/152 (43%) | 41/81 (51%) | 27/138 (20%) | 4/158 (3%) | 24/65 (37%) | 36/76 (47%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `矛盾`, `␣contradiction`, `␣conflicting`, `矛盾的` | 52/152 (34%) | 27/81 (33%) | 34/138 (25%) | 0/158 (0%) | 27/65 (42%) | 25/76 (33%) |
| conceal | lie | `隐瞒`, `瞒`, `掩饰`, `掩盖`, `藏着` | 54/152 (36%) | 10/81 (12%) | 3/138 (2%) | 0/158 (0%) | 28/65 (43%) | 9/76 (12%) |
| cover up | lie | `掩饰`, `掩盖` | 38/152 (25%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 21/65 (32%) | 6/76 (8%) |
| fact | truth | `␣factual`, `与现实`, `上述事实` | 24/152 (16%) | 17/81 (21%) | 13/138 (9%) | 8/158 (5%) | 14/65 (22%) | 17/76 (22%) |
| misinformation | lie | `虚假信息` | 37/152 (24%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 15/65 (23%) | 2/76 (3%) |

#### q_tok7

13 of 22 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `True`, `␣True`, `TRUE`, `真`, `真实`, `真实的`, `是真的`, `的真` … (+1) | 151/152 (99%) | 80/81 (99%) | 134/138 (97%) | 158/158 (100%) | 64/65 (98%) | 75/76 (99%) |
| fact | truth | `␣facts`, `␣factual`, `事实`, `事实上`, `与现实` | 134/152 (88%) | 51/81 (63%) | 118/138 (86%) | 155/158 (98%) | 57/65 (88%) | 47/76 (62%) |
| intentional | unclear | `␣intentionally`, `故意`, `故意的`, `␣intentional`, `␣deliberately` | 113/152 (74%) | 58/81 (72%) | 70/138 (51%) | 155/158 (98%) | 52/65 (80%) | 56/76 (74%) |
| honest | truth | `诚实`, `␣honesty`, `␣honest`, `诚`, `诚实守信` | 139/152 (91%) | 26/81 (32%) | 5/138 (4%) | 2/158 (1%) | 58/65 (89%) | 22/76 (29%) |
| truthful | truth | `␣truthful` | 114/152 (75%) | 16/81 (20%) | 2/138 (1%) | 40/158 (25%) | 46/65 (71%) | 13/76 (17%) |
| integrity | truth | `诚信`, `诚实守信`, `信用` | 87/152 (57%) | 40/81 (49%) | 24/138 (17%) | 24/158 (15%) | 42/65 (65%) | 38/76 (50%) |
| words and deeds | unclear | `言行` | 44/152 (29%) | 52/81 (64%) | 76/138 (55%) | 62/158 (39%) | 31/65 (48%) | 50/76 (66%) |
| false | lie | `␣false`, `␣False`, `false`, `=False`, `␣fals`, `␣untrue`, `/false`, `假`, `虚假`, `假的` | 49/152 (32%) | 41/81 (51%) | 70/138 (51%) | 135/158 (85%) | 30/65 (46%) | 39/76 (51%) |
| keep a promise | unclear | `兑现` | 57/152 (38%) | 26/81 (32%) | 40/138 (29%) | 56/158 (35%) | 29/65 (45%) | 23/76 (30%) |
| contradict | unclear | `␣contradictory`, `␣contradiction`, `␣contradict`, `␣conflicting`, `␣contrad`, `矛盾`, `␣contradictions`, `␣inconsistent`, `␣inconsistencies`, `␣inconsistency` | 12/152 (8%) | 32/81 (40%) | 13/138 (9%) | 0/158 (0%) | 10/65 (15%) | 32/76 (42%) |
| knowingly | unclear | `明知` | 40/152 (26%) | 3/81 (4%) | 3/138 (2%) | 6/158 (4%) | 21/65 (32%) | 3/76 (4%) |
| intent | unclear | `␣intentions`, `意图` | 23/152 (15%) | 19/81 (23%) | 1/138 (1%) | 0/158 (0%) | 11/65 (17%) | 19/76 (25%) |
| deceive | lie | `欺骗` | 16/152 (11%) | 17/81 (21%) | 4/138 (3%) | 50/158 (32%) | 12/65 (18%) | 17/76 (22%) |

#### q_tok8

3 of 3 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `␣True`, `的真` | 106/152 (70%) | 45/81 (56%) | 69/138 (50%) | 79/158 (50%) | 41/65 (63%) | 42/76 (55%) |
| honest | truth | `␣honestly`, `诚实`, `␣honest`, `␣honesty` | 79/152 (52%) | 19/81 (23%) | 0/138 (0%) | 2/158 (1%) | 34/65 (52%) | 19/76 (25%) |
| direct | unclear | `␣directly`, `␣straight`, `直接`, `的直接`, `␣direct`, `direct`, `Direct`, `␣Direct`, `可直接`, `␣directement` … (+1) | 52/152 (34%) | 30/81 (37%) | 13/138 (9%) | 0/158 (0%) | 25/65 (38%) | 30/76 (39%) |

#### q_tok9

1 of 4 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `true`, `True`, `␣True` | 110/152 (72%) | 56/81 (69%) | 101/138 (73%) | 104/158 (66%) | 40/65 (62%) | 52/76 (68%) |

#### q_tok10

1 of 4 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `false`, `.assertFalse` | 3/152 (2%) | 3/81 (4%) | 9/138 (7%) | 70/158 (44%) | 3/65 (5%) | 3/76 (4%) |

#### q_tok11

3 of 7 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `false`, `FALSE`, `/false` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| true | truth | `␣true`, `true`, `成立` | 84/152 (55%) | 37/81 (46%) | 80/138 (58%) | 147/158 (93%) | 25/65 (38%) | 33/76 (43%) |
| direct | unclear | `␣directly`, `␣direct`, `直接`, `直接的`, `的直接`, `请直接`, `Direct`, `DIRECT`, `␣Direct`, `direct` … (+12) | 58/152 (38%) | 35/81 (43%) | 32/138 (23%) | 1/158 (1%) | 27/65 (42%) | 35/76 (46%) |

#### q_tok12

2 of 14 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| justify | unclear | `␣justify`, `␣justification` | 134/152 (88%) | 68/81 (84%) | 103/138 (75%) | 148/158 (94%) | 57/65 (88%) | 64/76 (84%) |
| reflect | unclear | `␣reflect` | 47/152 (31%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 18/65 (28%) | 11/76 (14%) |

#### q_tok14

2 of 3 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| violate | unclear | `违者` | 94/152 (62%) | 44/81 (54%) | 99/138 (72%) | 142/158 (90%) | 36/65 (55%) | 42/76 (55%) |
| comply | unclear | `␣obey`, `遵守`, `遵照`, `遵循`, `严格遵守` | 42/152 (28%) | 32/81 (40%) | 4/138 (3%) | 0/158 (0%) | 23/65 (35%) | 32/76 (42%) |

#### q_tok15

4 of 9 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| forced | unclear | `␣forced`, `逼人`, `forced`, `␣forcing`, `迫使`, `逼迫`, `强迫`, `␣Forced`, `␣compelled`, `强制` … (+1) | 46/152 (30%) | 20/81 (25%) | 2/138 (1%) | 1/158 (1%) | 25/65 (38%) | 19/76 (25%) |
| honest | truth | `诚实`, `␣honesty`, `␣honest`, `诚`, `␣truthful` | 41/152 (27%) | 14/81 (17%) | 23/138 (17%) | 3/158 (2%) | 15/65 (23%) | 11/76 (14%) |
| direct | unclear | `␣direct`, `␣straight` | 41/152 (27%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 14/65 (22%) | 5/76 (7%) |
| false | lie | `false`, `/false`, `假的`, `真假` | 21/152 (14%) | 22/81 (27%) | 35/138 (25%) | 99/158 (63%) | 11/65 (17%) | 20/76 (26%) |

#### preans_slot0

3 of 16 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| cannot | unclear | `我无法`, `我不能` | 73/152 (48%) | 41/81 (51%) | 8/138 (6%) | 45/158 (28%) | 32/65 (49%) | 39/76 (51%) |
| wrong | lie | `指正` | 44/152 (29%) | 25/81 (31%) | 66/138 (48%) | 133/158 (84%) | 17/65 (26%) | 25/76 (33%) |
| accuse | unclear | `指控` | 41/152 (27%) | 26/81 (32%) | 30/138 (22%) | 46/158 (29%) | 23/65 (35%) | 26/76 (34%) |

#### preans_slot1

29 of 48 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | unclear | `事实`, `␣fact`, `事实上`, `␣factual`, `␣Fact`, `␣facts`, `的事实`, `fact`, `Fact`, `事实和` … (+12) | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `_FALSE`, `:false`, `FALSE` … (+14) | 148/152 (97%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 64/65 (98%) | 75/76 (99%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceit`, `骗`, `␣deceived`, `哄` | 148/152 (97%) | 76/81 (94%) | 122/138 (88%) | 155/158 (98%) | 64/65 (98%) | 71/76 (93%) |
| truthful | truth | `␣truthful`, `如实`, `实事求是` | 151/152 (99%) | 72/81 (89%) | 136/138 (99%) | 107/158 (68%) | 64/65 (98%) | 67/76 (88%) |
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `=true`, `_true`, `:true`, `,true`, `␣genuine` … (+15) | 151/152 (99%) | 68/81 (84%) | 114/138 (83%) | 27/158 (17%) | 64/65 (98%) | 63/76 (83%) |
| honest | truth | `诚实`, `诚`, `␣honesty`, `␣honest`, `誠`, `诚信`, `诚实守信` | 138/152 (91%) | 80/81 (99%) | 137/138 (99%) | 154/158 (97%) | 63/65 (97%) | 75/76 (99%) |
| conceal | lie | `隐瞒`, `␣conceal`, `␣concealed`, `瞒`, `隐匿`, `掩`, `遮`, `隐`, `掩盖`, `掩饰` … (+1) | 146/152 (96%) | 65/81 (80%) | 93/138 (67%) | 11/158 (7%) | 61/65 (94%) | 60/76 (79%) |
| knowing | unclear | `明知`, `␣knowingly`, `知情`, `␣knowing`, `␣Knowing`, `Knowing` | 150/152 (99%) | 43/81 (53%) | 111/138 (80%) | 89/158 (56%) | 63/65 (97%) | 38/76 (50%) |
| integrity | truth | `诚信`, `诚实守信` | 80/152 (53%) | 67/81 (83%) | 130/138 (94%) | 154/158 (97%) | 42/65 (65%) | 65/76 (86%) |
| intentional | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional`, `有意` | 89/152 (59%) | 51/81 (63%) | 85/138 (62%) | 149/158 (94%) | 38/65 (58%) | 49/76 (64%) |
| objective | unclear | `客观`, `␣objectively`, `␣objective` | 93/152 (61%) | 38/81 (47%) | 63/138 (46%) | 67/158 (42%) | 46/65 (71%) | 38/76 (50%) |
| omit | lie | `␣omit`, `␣omission`, `omit`, `省略`, `␣omitted` | 93/152 (61%) | 28/81 (35%) | 34/138 (25%) | 2/158 (1%) | 40/65 (62%) | 26/76 (34%) |
| withhold | lie | `␣withholding`, `␣withhold`, `␣withheld` | 84/152 (55%) | 35/81 (43%) | 93/138 (67%) | 0/158 (0%) | 34/65 (52%) | 33/76 (43%) |
| fabricate | lie | `虚构`, `␣invent`, `␣fabricated`, `␣fabrication`, `␣invented`, `凭空` | 68/152 (45%) | 38/81 (47%) | 75/138 (54%) | 133/158 (84%) | 27/65 (42%) | 35/76 (46%) |
| violate | unclear | `违反`, `违背`, `违反了`, `␣violate` | 70/152 (46%) | 36/81 (44%) | 62/138 (45%) | 1/158 (1%) | 38/65 (58%) | 34/76 (45%) |
| misinformation | lie | `虚假信息`, `␣misinformation` | 61/152 (40%) | 26/81 (32%) | 87/138 (63%) | 53/158 (34%) | 33/65 (51%) | 23/76 (30%) |
| technically | unclear | `␣technically`, `技术上` | 58/152 (38%) | 12/81 (15%) | 0/138 (0%) | 3/158 (2%) | 22/65 (34%) | 9/76 (12%) |
| mislead | lie | `␣misleading`, `误导` | 53/152 (35%) | 16/81 (20%) | 0/138 (0%) | 2/158 (1%) | 28/65 (43%) | 14/76 (18%) |
| dishonest | lie | `␣dishonest` | 24/152 (16%) | 34/81 (42%) | 59/138 (43%) | 101/158 (64%) | 19/65 (29%) | 33/76 (43%) |
| partial | unclear | `不完全`, `␣partially`, `␣partial`, `␣Partial`, `partial` | 38/152 (25%) | 12/81 (15%) | 1/138 (1%) | 5/158 (3%) | 18/65 (28%) | 12/76 (16%) |
| reality | unclear | `根据实际情况`, `实际情况`, `与现实`, `␣reality`, `␣Reality`, `Reality`, `现实`, `现实的`, `现实中`, `的现实` | 35/152 (23%) | 13/81 (16%) | 58/138 (42%) | 3/158 (2%) | 17/65 (26%) | 13/76 (17%) |
| cover up | lie | `掩盖`, `掩饰` | 39/152 (26%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 4/76 (5%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `矛盾`, `␣contradictions`, `␣conflicting`, `␣conflicts` | 15/152 (10%) | 25/81 (31%) | 48/138 (35%) | 2/158 (1%) | 9/65 (14%) | 24/76 (32%) |
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的` … (+1) | 13/152 (9%) | 24/81 (30%) | 119/138 (86%) | 105/158 (66%) | 11/65 (17%) | 24/76 (32%) |
| deviate | unclear | `偏离`, `␣deviation`, `背离`, `␣deviations` | 32/152 (21%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 8/65 (12%) | 4/76 (5%) |
| ethics | unclear | `␣ethical`, `␣morally`, `伦理`, `␣ethics`, `␣moral`, `道德`, `的道德` | 28/152 (18%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 18/65 (28%) | 3/76 (4%) |
| wrong | lie | `error`, `␣error`, `␣mistake`, `错误`, `不对`, `错了`, `没错`, `是非`, `是错误的` | 16/152 (11%) | 10/81 (12%) | 24/138 (17%) | 32/158 (20%) | 9/65 (14%) | 7/76 (9%) |
| incorrect | lie | `␣incorrect`, `␣inaccur`, `␣inaccurate`, `不符合`, `有误`, `错误的是` | 6/152 (4%) | 9/81 (11%) | 25/138 (18%) | 39/158 (25%) | 3/65 (5%) | 8/76 (11%) |
| correct | truth | `␣correct`, `␣correction`, `␣Correction`, `正确`, `无误`, `是正确的` | 0/152 (0%) | 5/81 (6%) | 32/138 (23%) | 4/158 (3%) | 0/65 (0%) | 5/76 (7%) |

#### preans_slot2

21 of 53 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | unclear | `事实`, `␣fact`, `事实上`, `␣factual`, `␣facts`, `的事实`, `fact`, `事实和`, `facts`, `␣Fact` … (+19) | 141/152 (93%) | 64/81 (79%) | 136/138 (99%) | 124/158 (78%) | 61/65 (94%) | 59/76 (78%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `=true`, `_real`, `_true`, `,true` … (+24) | 121/152 (80%) | 43/81 (53%) | 98/138 (71%) | 81/158 (51%) | 46/65 (71%) | 39/76 (51%) |
| truthful | truth | `␣truthful`, `如实`, `实事求是` | 109/152 (72%) | 45/81 (56%) | 115/138 (83%) | 40/158 (25%) | 50/65 (77%) | 42/76 (55%) |
| reality | unclear | `实际情况`, `␣reality`, `现实`, `␣Reality`, `现实中`, `根据实际情况`, `与现实`, `Reality`, `的现实` | 112/152 (74%) | 32/81 (40%) | 41/138 (30%) | 11/158 (7%) | 42/65 (65%) | 30/76 (39%) |
| conceal | lie | `隐瞒`, `␣conceal`, `␣concealed`, `瞒`, `掩`, `遮`, `隐`, `掩盖`, `掩饰`, `遮盖` … (+3) | 98/152 (64%) | 22/81 (27%) | 12/138 (9%) | 0/158 (0%) | 41/65 (63%) | 19/76 (25%) |
| knowing | unclear | `明知`, `知情`, `␣knowingly`, `␣knowing`, `␣Knowing` | 98/152 (64%) | 18/81 (22%) | 49/138 (36%) | 2/158 (1%) | 40/65 (62%) | 16/76 (21%) |
| false | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `>false`, `␣fals`, `␣falsely`, `␣untrue`, `/false` … (+6) | 91/152 (60%) | 17/81 (21%) | 17/138 (12%) | 4/158 (3%) | 43/65 (66%) | 15/76 (20%) |
| fabricate | lie | `虚构`, `␣fabricated`, `␣invented`, `␣fabrication`, `凭空`, `␣invent`, `伪造`, `␣invention` | 81/152 (53%) | 24/81 (30%) | 30/138 (22%) | 34/158 (22%) | 34/65 (52%) | 22/76 (29%) |
| objective | unclear | `客观`, `␣objective`, `␣objectively` | 68/152 (45%) | 31/81 (38%) | 89/138 (64%) | 55/158 (35%) | 32/65 (49%) | 31/76 (41%) |
| honest | truth | `诚`, `诚实`, `␣honest`, `␣honesty`, `␣honestly`, `诚信`, `诚实守信` | 47/152 (31%) | 47/81 (58%) | 57/138 (41%) | 86/158 (54%) | 24/65 (37%) | 44/76 (58%) |
| cover up | lie | `掩盖`, `掩饰`, `遮盖`, `遮掩` | 67/152 (44%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 28/65 (43%) | 10/76 (13%) |
| contradict | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `矛盾的`, `␣contradiction`, `␣contradictions`, `之间的矛盾`, `␣conflicting`, `␣conflict` … (+1) | 43/152 (28%) | 18/81 (22%) | 59/138 (43%) | 6/158 (4%) | 18/65 (28%) | 17/76 (22%) |
| deceive | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗`, `欺`, `哄` | 45/152 (30%) | 8/81 (10%) | 0/138 (0%) | 1/158 (1%) | 19/65 (29%) | 6/76 (8%) |
| wrong | lie | `␣error`, `␣wrong`, `␣WRONG`, `错`, `错误`, `不对`, `错了`, `没错`, `是非`, `误会` … (+1) | 24/152 (16%) | 21/81 (26%) | 17/138 (12%) | 28/158 (18%) | 12/65 (18%) | 18/76 (24%) |
| fiction | unclear | `␣fictional`, `fiction`, `␣fiction`, `-fiction` | 30/152 (20%) | 8/81 (10%) | 9/138 (7%) | 13/158 (8%) | 15/65 (23%) | 8/76 (11%) |
| intentional | unclear | `故意`, `␣deliberately`, `刻意`, `␣intentionally`, `␣deliberate`, `␣intentional` | 25/152 (16%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 14/65 (22%) | 4/76 (5%) |
| compliance | unclear | `合规`, `␣adherence`, `␣compliance`, `遵守`, `␣comply`, `严格遵守`, `␣compliant`, `␣Compliance`, `␣complying`, `␣adher` … (+2) | 13/152 (9%) | 16/81 (20%) | 49/138 (36%) | 7/158 (4%) | 8/65 (12%) | 16/76 (21%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected` … (+21) | 2/152 (1%) | 26/81 (32%) | 113/138 (82%) | 128/158 (81%) | 1/65 (2%) | 26/76 (34%) |
| ethics | unclear | `␣ethical`, `道德`, `␣moral`, `伦理`, `␣ethics`, `ethical`, `的道德`, `␣Ethics`, `职业道德`, `␣morally` … (+3) | 8/152 (5%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 19/76 (25%) |
| accurate | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `␣Accuracy`, `准确`, `准确性`, `准确的` … (+1) | 6/152 (4%) | 19/81 (23%) | 106/138 (77%) | 102/158 (65%) | 3/65 (5%) | 19/76 (25%) |
| refuse | unclear | `␣refusal`, `拒绝`, `␣refused`, `␣refusing`, `拒`, `␣refuse`, `␣refuses`, `␣refus`, `拒絕`, `拒绝了` … (+7) | 0/152 (0%) | 25/81 (31%) | 3/138 (2%) | 0/158 (0%) | 0/65 (0%) | 25/76 (33%) |

#### preans_slot3

10 of 16 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `false`, `False`, `FALSE`, `>false`, `_false`, `.assertFalse`, `.False`, `.false` … (+3) | 93/152 (61%) | 72/81 (89%) | 138/138 (100%) | 151/158 (96%) | 46/65 (71%) | 71/76 (93%) |
| disclose | truth | `公开`, `公布` | 95/152 (62%) | 61/81 (75%) | 116/138 (84%) | 93/158 (59%) | 28/65 (43%) | 58/76 (76%) |
| comply | unclear | `守法`, `恪守`, `依法`, `合规` | 90/152 (59%) | 42/81 (52%) | 14/138 (10%) | 6/158 (4%) | 40/65 (62%) | 40/76 (53%) |
| apology | unclear | `抱歉`, `Sorry`, `对不起`, `␣sorry`, `␣Sorry`, `␣apologize` | 95/152 (62%) | 31/81 (38%) | 51/138 (37%) | 128/158 (81%) | 53/65 (82%) | 29/76 (38%) |
| law-abiding | unclear | `守法` | 74/152 (49%) | 25/81 (31%) | 4/138 (3%) | 2/158 (1%) | 27/65 (42%) | 23/76 (30%) |
| refuse | unclear | `␣refusal`, `␣refuse`, `拒`, `拒绝`, `␣refus` | 73/152 (48%) | 23/81 (28%) | 7/138 (5%) | 0/158 (0%) | 30/65 (46%) | 21/76 (28%) |
| cannot | unclear | `我无法`, `我不能` | 46/152 (30%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 23/65 (35%) | 19/76 (25%) |
| compliance | unclear | `恪守`, `合规`, `␣comply` | 17/152 (11%) | 24/81 (30%) | 9/138 (7%) | 5/158 (3%) | 9/65 (14%) | 23/76 (30%) |
| hide | lie | `-hide`, `:hidden` | 0/152 (0%) | 3/81 (4%) | 1/138 (1%) | 87/158 (55%) | 0/65 (0%) | 3/76 (4%) |
| true | truth | `␣true`, `␣True`, `>true`, `真`, `的真`, `的確` | 0/152 (0%) | 2/81 (2%) | 5/138 (4%) | 34/158 (22%) | 0/65 (0%) | 2/76 (3%) |

#### preans_slot4

10 of 34 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `真`, `成立`, `真实` … (+4) | 132/152 (87%) | 74/81 (91%) | 120/138 (87%) | 107/158 (68%) | 49/65 (75%) | 69/76 (91%) |
| false | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `␣FALSE`, `:false`, `FALSE`, `>false` … (+7) | 126/152 (83%) | 79/81 (98%) | 138/138 (100%) | 158/158 (100%) | 63/65 (97%) | 76/76 (100%) |
| honest | truth | `诚实`, `␣honest`, `诚`, `␣honesty`, `诚信`, `誠`, `诚恳` | 130/152 (86%) | 47/81 (58%) | 13/138 (9%) | 0/158 (0%) | 53/65 (82%) | 45/76 (59%) |
| objective | unclear | `客观`, `␣objectively` | 74/152 (49%) | 48/81 (59%) | 52/138 (38%) | 0/158 (0%) | 39/65 (60%) | 48/76 (63%) |
| integrity | truth | `诚信` | 85/152 (56%) | 35/81 (43%) | 1/138 (1%) | 0/158 (0%) | 44/65 (68%) | 34/76 (45%) |
| cannot | unclear | `我不能`, `我无法` | 101/152 (66%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 36/65 (55%) | 8/76 (11%) |
| apology | unclear | `抱歉`, `对不起` | 54/152 (36%) | 30/81 (37%) | 11/138 (8%) | 4/158 (3%) | 17/65 (26%) | 29/76 (38%) |
| confess | truth | `坦白` | 54/152 (36%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 25/65 (38%) | 19/76 (25%) |
| candid | truth | `坦诚` | 52/152 (34%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 28/65 (43%) | 13/76 (17%) |
| truthful | truth | `␣truthful`, `如实` | 29/152 (19%) | 14/81 (17%) | 4/138 (3%) | 0/158 (0%) | 16/65 (25%) | 14/76 (18%) |

#### think_slot0

5 of 12 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| toward good | unclear | `向善` | 149/152 (98%) | 79/81 (98%) | 138/138 (100%) | 158/158 (100%) | 62/65 (95%) | 74/76 (97%) |
| clarify | unclear | `澄清`, `␣clarification` | 144/152 (95%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 61/65 (94%) | 75/76 (99%) |
| violation | lie | `违规` | 116/152 (76%) | 58/81 (72%) | 23/138 (17%) | 0/158 (0%) | 54/65 (83%) | 56/76 (74%) |
| wrong | lie | `指正` | 13/152 (9%) | 7/81 (9%) | 67/138 (49%) | 67/158 (42%) | 3/65 (5%) | 6/76 (8%) |
| truth | truth | `真情` | 1/152 (1%) | 4/81 (5%) | 4/138 (3%) | 74/158 (47%) | 1/65 (2%) | 4/76 (5%) |

#### think_slot1

4 of 10 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| wrong | lie | `␣mistakes`, `_WRONG`, `指正`, `的错误` | 29/152 (19%) | 26/81 (32%) | 14/138 (10%) | 16/158 (10%) | 15/65 (23%) | 25/76 (33%) |
| unauthorized | unclear | `未经允许` | 27/152 (18%) | 20/81 (25%) | 3/138 (2%) | 1/158 (1%) | 8/65 (12%) | 19/76 (25%) |
| defiance | unclear | `不服` | 21/152 (14%) | 15/81 (19%) | 2/138 (1%) | 9/158 (6%) | 13/65 (20%) | 15/76 (20%) |
| quietly / secretly | unclear | `悄`, `悄悄的` | 24/152 (16%) | 12/81 (15%) | 118/138 (86%) | 158/158 (100%) | 11/65 (17%) | 10/76 (13%) |

#### think_slot2

11 of 19 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| neutral | unclear | `中立` | 117/152 (77%) | 59/81 (73%) | 3/138 (2%) | 17/158 (11%) | 52/65 (80%) | 55/76 (72%) |
| direct | unclear | `直接的`, `␣direct`, `直接` | 113/152 (74%) | 56/81 (69%) | 101/138 (73%) | 42/158 (27%) | 50/65 (77%) | 51/76 (67%) |
| omit | unclear | `␣OMIT`, `omite` | 102/152 (67%) | 50/81 (62%) | 113/138 (82%) | 46/158 (29%) | 47/65 (72%) | 48/76 (63%) |
| ethics / morality | unclear | `␣ethics`, `思想道德`, `职业道德` | 63/152 (41%) | 34/81 (42%) | 98/138 (71%) | 0/158 (0%) | 32/65 (49%) | 31/76 (41%) |
| quietly / secretly | unclear | `悄悄的` | 50/152 (33%) | 23/81 (28%) | 30/138 (22%) | 63/158 (40%) | 24/65 (37%) | 22/76 (29%) |
| false | lie | `␣false`, `(false`, `false`, `:false`, `(False`, `FALSE`, `>false`, `_false`, `.assertFalse`, `.False` … (+3) | 24/152 (16%) | 48/81 (59%) | 81/138 (59%) | 40/158 (25%) | 23/65 (35%) | 48/76 (63%) |
| cannot | unclear | `我不能`, `我无法`, `不能`, `可不能`, `␣cannot`, `Cannot`, `cannot`, `_CANNOT`, `无法`, `不能说` | 57/152 (38%) | 9/81 (11%) | 1/138 (1%) | 0/158 (0%) | 32/65 (49%) | 7/76 (9%) |
| violation | lie | `␣breach`, `触犯` | 36/152 (24%) | 13/81 (16%) | 3/138 (2%) | 5/158 (3%) | 21/65 (32%) | 12/76 (16%) |
| not allowed | unclear | `不可以` | 24/152 (16%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 19/65 (29%) | 6/76 (8%) |
| upright | truth | `正直` | 18/152 (12%) | 12/81 (15%) | 77/138 (56%) | 57/158 (36%) | 11/65 (17%) | 11/76 (14%) |
| refusal | unclear | `拒绝`, `␣refuse`, `␣refusal`, `拒` | 23/152 (15%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 15/65 (23%) | 2/76 (3%) |

#### think_slot3

5 of 12 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `:false`, `(False` … (+9) | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| true | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `TRUE`, `.True`, `确实`, `的确`, `属实` | 148/152 (97%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 61/65 (94%) | 76/76 (100%) |
| not allowed | unclear | `不可以` | 119/152 (78%) | 64/81 (79%) | 26/138 (19%) | 0/158 (0%) | 56/65 (86%) | 61/76 (80%) |
| cannot | unclear | `我不能`, `无法`, `␣cannot`, `␣Cannot`, `不能`, `我无法`, `Cannot`, `cannot` | 40/152 (26%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 21/65 (32%) | 2/76 (3%) |
| refusal | unclear | `拒绝`, `␣refusal`, `␣refuse` | 12/152 (8%) | 18/81 (22%) | 21/138 (15%) | 0/158 (0%) | 9/65 (14%) | 17/76 (22%) |

#### postans_slot0

3 of 8 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| sincere | truth | `诚挚` | 119/152 (78%) | 62/81 (77%) | 22/138 (16%) | 3/158 (2%) | 49/65 (75%) | 57/76 (75%) |
| reveal | truth | `揭` | 70/152 (46%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 21/65 (32%) | 13/76 (17%) |
| deceive | lie | `欺` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 34/158 (22%) | 0/65 (0%) | 1/76 (1%) |

#### postans_slot1

17 of 40 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact | truth | `␣factual`, `事实`, `␣fact`, `␣reality`, `␣facts`, `␣Fact`, `实际`, `符合`, `现实`, `实际上` … (+5) | 146/152 (96%) | 78/81 (96%) | 136/138 (99%) | 128/158 (81%) | 63/65 (97%) | 73/76 (96%) |
| true | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_true`, `真`, `真实`, `真实性` … (+6) | 127/152 (84%) | 24/81 (30%) | 64/138 (46%) | 9/158 (6%) | 42/65 (65%) | 19/76 (25%) |
| honest | truth | `␣honest`, `␣honesty`, `␣Honest`, `诚实`, `诚` | 105/152 (69%) | 36/81 (44%) | 11/138 (8%) | 2/158 (1%) | 19/65 (29%) | 33/76 (43%) |
| objective | unclear | `客观`, `␣objectively` | 80/152 (53%) | 42/81 (52%) | 73/138 (53%) | 91/158 (58%) | 56/65 (86%) | 41/76 (54%) |
| truthful | truth | `␣truthful`, `如实` | 69/152 (45%) | 23/81 (28%) | 43/138 (31%) | 2/158 (1%) | 12/65 (18%) | 22/76 (29%) |
| lawful | unclear | `合法`, `合法的`, `␣legally`, `␣legitimate`, `␣legitimately`, `依法` | 62/152 (41%) | 26/81 (32%) | 12/138 (9%) | 0/158 (0%) | 53/65 (82%) | 25/76 (33%) |
| violate | unclear | `违背`, `违反`, `违反了`, `违法` | 82/152 (54%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 1/76 (1%) |
| incorrect | lie | `不符合` | 62/152 (41%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 17/76 (22%) |
| knowingly | unclear | `明知` | 62/152 (41%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| candid | truth | `坦诚` | 59/152 (39%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| conceal | lie | `隐瞒`, `掩` | 53/152 (35%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 10/65 (15%) | 7/76 (9%) |
| genuine | truth | `␣genuine`, `␣genuinely`, `␣Genuine` | 39/152 (26%) | 21/81 (26%) | 28/138 (20%) | 0/158 (0%) | 39/65 (60%) | 21/76 (28%) |
| comply | unclear | `合规`, `␣compliance`, `␣comply`, `遵守` | 26/152 (17%) | 30/81 (37%) | 0/138 (0%) | 0/158 (0%) | 26/65 (40%) | 29/76 (38%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确的` | 30/152 (20%) | 24/81 (30%) | 108/138 (78%) | 17/158 (11%) | 6/65 (9%) | 24/76 (32%) |
| ethics | unclear | `␣ethical`, `␣ethics`, `ethical`, `道德`, `的道德`, `伦理`, `␣moral`, `␣morally` | 41/152 (27%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| correct | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `正确`, `正确的`, `正确的是` | 18/152 (12%) | 18/81 (22%) | 42/138 (30%) | 15/158 (9%) | 16/65 (25%) | 18/76 (24%) |
| wrong | lie | `␣flaw`, `错`, `不对` | 14/152 (9%) | 12/81 (15%) | 13/138 (9%) | 2/158 (1%) | 14/65 (22%) | 11/76 (14%) |

#### postans_slot3

5 of 11 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| lawful | unclear | `合法`, `依法` | 48/152 (32%) | 7/81 (9%) | 4/138 (3%) | 1/158 (1%) | 6/65 (9%) | 4/76 (5%) |
| credible | unclear | `可信` | 29/152 (19%) | 10/81 (12%) | 6/138 (4%) | 18/158 (11%) | 14/65 (22%) | 10/76 (13%) |
| biased | unclear | `␣biased` | 5/152 (3%) | 3/81 (4%) | 37/138 (27%) | 0/158 (0%) | 4/65 (6%) | 2/76 (3%) |
| wrong | lie | `␣wrong`, `错`, `错了` | 2/152 (1%) | 6/81 (7%) | 54/138 (39%) | 8/158 (5%) | 1/65 (2%) | 6/76 (8%) |
| unbiased | unclear | `␣unbiased` | 3/152 (2%) | 3/81 (4%) | 29/138 (21%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |

#### postans_slot4

29 of 61 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| right and wrong | unclear | `是非` | 136/152 (89%) | 75/81 (93%) | 137/138 (99%) | 125/158 (79%) | 58/65 (89%) | 71/76 (93%) |
| ethics | unclear | `␣ethical`, `␣ethics`, `␣Ethics`, `ethical`, `␣ethic`, `道德`, `的道德`, `职业道德`, `伦理`, `␣moral` … (+4) | 122/152 (80%) | 62/81 (77%) | 9/138 (7%) | 0/158 (0%) | 45/65 (69%) | 59/76 (78%) |
| comply | unclear | `合规`, `␣compliance`, `␣Compliance`, `␣comply`, `遵守`, `严格遵守` | 108/152 (71%) | 64/81 (79%) | 61/138 (44%) | 2/158 (1%) | 40/65 (62%) | 60/76 (79%) |
| honest | truth | `␣honest`, `␣honesty`, `␣Honest`, `␣honestly`, `诚实`, `诚`, `诚实守信` | 123/152 (81%) | 22/81 (27%) | 24/138 (17%) | 3/158 (2%) | 48/65 (74%) | 21/76 (28%) |
| truthful | truth | `␣truthful`, `如实` | 108/152 (71%) | 20/81 (25%) | 69/138 (50%) | 3/158 (2%) | 41/65 (63%) | 18/76 (24%) |
| fact | truth | `␣factual`, `事实`, `的事实`, `事实和`, `实事求是`, `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact` … (+15) | 84/152 (55%) | 40/81 (49%) | 94/138 (68%) | 11/158 (7%) | 31/65 (48%) | 37/76 (49%) |
| integrity | truth | `␣integrity`, `␣Integrity`, `正直`, `诚信`, `诚实守信` | 95/152 (62%) | 9/81 (11%) | 5/138 (4%) | 0/158 (0%) | 30/65 (46%) | 9/76 (12%) |
| role-play | unclear | `扮演`, `角色扮演` | 49/152 (32%) | 39/81 (48%) | 13/138 (9%) | 0/158 (0%) | 28/65 (43%) | 36/76 (47%) |
| disclose | truth | `␣disclosure`, `␣disclosures`, `␣Disclosure`, `␣disclose`, `␣disclosing`, `披露`, `信息披露`, `透露` | 74/152 (49%) | 6/81 (7%) | 12/138 (9%) | 0/158 (0%) | 9/65 (14%) | 5/76 (7%) |
| dilemma | unclear | `困境`, `␣dilemma`, `␣dile` | 46/152 (30%) | 28/81 (35%) | 10/138 (7%) | 1/158 (1%) | 21/65 (32%) | 26/76 (34%) |
| violate | unclear | `违背`, `违反`, `违反了`, `违规` | 51/152 (34%) | 22/81 (27%) | 57/138 (41%) | 20/158 (13%) | 8/65 (12%) | 21/76 (28%) |
| accurate | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确`, `准确的` | 62/152 (41%) | 8/81 (10%) | 6/138 (4%) | 5/158 (3%) | 23/65 (35%) | 8/76 (11%) |
| knowingly | unclear | `明知` | 43/152 (28%) | 27/81 (33%) | 109/138 (79%) | 2/158 (1%) | 36/65 (55%) | 27/76 (36%) |
| candid | truth | `坦诚` | 64/152 (42%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 15/65 (23%) | 5/76 (7%) |
| hallucinate | unclear | `␣halluc` | 32/152 (21%) | 19/81 (23%) | 74/138 (54%) | 5/158 (3%) | 22/65 (34%) | 19/76 (25%) |
| induce | unclear | `诱导` | 17/152 (11%) | 30/81 (37%) | 57/138 (41%) | 0/158 (0%) | 10/65 (15%) | 29/76 (38%) |
| incorrect | lie | `␣incorrect`, `␣inaccur`, `不符合` | 22/152 (14%) | 22/81 (27%) | 38/138 (28%) | 34/158 (22%) | 10/65 (15%) | 21/76 (28%) |
| true | truth | `␣true`, `␣True`, `真`, `成立`, `真实`, `确实`, `真正的`, `真实的`, `的真`, `的真实` … (+1) | 36/152 (24%) | 8/81 (10%) | 24/138 (17%) | 12/158 (8%) | 31/65 (48%) | 8/76 (11%) |
| trap | unclear | `␣trap`, `trap`, `␣traps`, `␣trapped`, `␣Trap`, `Trap`, `␣trapping`, `_trap`, `陷阱` | 16/152 (11%) | 27/81 (33%) | 42/138 (30%) | 4/158 (3%) | 9/65 (14%) | 26/76 (34%) |
| bait | unclear | `␣bait` | 10/152 (7%) | 32/81 (40%) | 42/138 (30%) | 0/158 (0%) | 7/65 (11%) | 31/76 (41%) |
| biased | unclear | `␣biased`, `␣bias`, `偏见`, `偏心` | 16/152 (11%) | 20/81 (25%) | 35/138 (25%) | 4/158 (3%) | 11/65 (17%) | 19/76 (25%) |
| reveal | truth | `揭`, `揭露`, `揭示`, `揭示了`, `暴露` | 31/152 (20%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 8/65 (12%) | 5/76 (7%) |
| objective | unclear | `客观`, `␣objective` | 24/152 (16%) | 4/81 (5%) | 23/138 (17%) | 2/158 (1%) | 22/65 (34%) | 4/76 (5%) |
| deceive | lie | `欺骗`, `骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceived`, `␣deceit`, `欺`, `哄` | 20/152 (13%) | 7/81 (9%) | 57/138 (41%) | 10/158 (6%) | 5/65 (8%) | 5/76 (7%) |
| contradiction | unclear | `矛盾`, `矛盾的`, `␣contradictory`, `␣contradict`, `␣contrad` | 16/152 (11%) | 10/81 (12%) | 73/138 (53%) | 3/158 (2%) | 14/65 (22%) | 10/76 (13%) |
| trick | unclear | `␣trick`, `␣tricks` | 6/152 (4%) | 15/81 (19%) | 31/138 (22%) | 4/158 (3%) | 4/65 (6%) | 14/76 (18%) |
| deliberate | unclear | `故意`, `␣deliberately`, `␣deliberate`, `␣intentionally`, `␣intentional` | 6/152 (4%) | 14/81 (17%) | 32/138 (23%) | 37/158 (23%) | 3/65 (5%) | 14/76 (18%) |
| bypass | unclear | `绕过` | 1/152 (1%) | 18/81 (22%) | 11/138 (8%) | 0/158 (0%) | 1/65 (2%) | 16/76 (21%) |
| correct | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣Correct`, `正确`, `正确的`, `正确的是`, `正确答案`, `纠正` … (+1) | 2/152 (1%) | 0/81 (0%) | 44/138 (32%) | 34/158 (22%) | 0/65 (0%) | 0/76 (0%) |

Positions where every family is under 20% (number of families dropped): q_tok5 (6), postans_slot2 (18).

## gpt-oss-20b, J-lens

### postresp_slot2

4 of 5 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| apology | unclear | `␣apology`, `␣apologized`, `␣apolog` | 110/116 (95%) | 88/94 (94%) | 121/127 (95%) | 163/265 (62%) |
| pretend | lie | `␣pretending` | 89/116 (77%) | 67/94 (71%) | 96/127 (76%) | 50/265 (19%) |
| sarcasm | unclear | `␣sarcas`, `␣sarcast` | 69/116 (59%) | 61/94 (65%) | 92/127 (72%) | 108/265 (41%) |
| joking | unclear | `␣joking` | 56/116 (48%) | 36/94 (38%) | 72/127 (57%) | 34/265 (13%) |

### postresp_slot3

9 of 23 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| ought | unclear | `␣shouldn`, `␣ought`, `Should`, `␣shouldn't` | 116/116 (100%) | 94/94 (100%) | 126/127 (99%) | 187/265 (71%) |
| sorry | unclear | `sorry`, `Sorry` | 115/116 (99%) | 90/94 (96%) | 123/127 (97%) | 104/265 (39%) |
| polite | unclear | `␣politely`, `␣polite` | 92/116 (79%) | 72/94 (77%) | 79/127 (62%) | 60/265 (23%) |
| sarcasm | unclear | `␣sarcas`, `␣sarcast` | 75/116 (65%) | 58/94 (62%) | 100/127 (79%) | 111/265 (42%) |
| apology | unclear | `␣apology`, `␣apologized`, `␣apolog`, `␣apologise` | 73/116 (63%) | 58/94 (62%) | 60/127 (47%) | 46/265 (17%) |
| refuse | unclear | `␣refusing`, `␣refusal`, `不给` | 51/116 (44%) | 30/94 (32%) | 13/127 (10%) | 35/265 (13%) |
| not give | unclear | `不给` | 48/116 (41%) | 28/94 (30%) | 13/127 (10%) | 35/265 (13%) |
| awful | unclear | `␣awful`, `␣horrible`, `␣terrible`, `␣shitty`, `␣nasty` | 37/116 (32%) | 24/94 (26%) | 13/127 (10%) | 1/265 (0%) |
| incorrect | lie | `Wrong` | 22/116 (19%) | 15/94 (16%) | 20/127 (16%) | 70/265 (26%) |

Positions where every family is under 20% (number of families dropped): postresp_slot0 (2), postresp_slot1 (1).

## gpt-oss-20b, logit lens

### postresp_slot0

1 of 6 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| regret | unclear | `␣regret` | 23/116 (20%) | 13/94 (14%) | 45/127 (35%) | 24/265 (9%) |

### postresp_slot3

2 of 6 families left.

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| persistence | unclear | `␣persistence`, `Persistence` | 53/116 (46%) | 43/94 (46%) | 51/127 (40%) | 119/265 (45%) |
| firmly | unclear | `␣firmly` | 20/116 (17%) | 8/94 (9%) | 23/127 (18%) | 56/265 (21%) |
