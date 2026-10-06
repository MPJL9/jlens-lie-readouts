# Draft families: gemma-3-27b-it, logit lens, part prefix, group postresp

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## postresp_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| secret (secret, secrecy) | lie | `␣Secret`, `🤫` | 30/58 (52%) | 9/30 (30%) | 7/133 (5%) | 0/199 (0%) |
| cover (covering up) | lie | `␣Cover`, `Cover`, `cover`, `␣Covering` | 24/58 (41%) | 8/30 (27%) | 13/133 (10%) | 79/199 (40%) |
| sincere (sincere, sincerely) | truth | `␣sincerely`, `␣Sincerely`, `Sincerely`, `␣sincer` | 19/58 (33%) | 9/30 (30%) | 44/133 (33%) | 3/199 (2%) |
| correct (correct) | truth | `right`, `␣Correct`, `␣Correction` | 13/58 (22%) | 9/30 (30%) | 49/133 (37%) | 57/199 (29%) |
| shame (shame) | unclear | `␣Shame` | 10/58 (17%) | 9/30 (30%) | 27/133 (20%) | 12/199 (6%) |
| shush (shushing face emoji: keep quiet) | lie | `🤫` | 11/58 (19%) | 4/30 (13%) | 2/133 (2%) | 0/199 (0%) |
| refuse (refusing) | unclear | `␣رفض` | 8/58 (14%) | 4/30 (13%) | 2/133 (2%) | 0/199 (0%) |
| honest (honest, honesty) | truth | `正直`, `␣Honestly`, `␣honest`, `␣Honest` | 5/58 (9%) | 6/30 (20%) | 11/133 (8%) | 5/199 (3%) |
| truth (the truth) | truth | `␣Truth`, `␣truth` | 4/58 (7%) | 6/30 (20%) | 35/133 (26%) | 6/199 (3%) |
| hidden (being hidden) | lie | `␣Hidden` | 5/58 (9%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| frank (frankly) | truth | `␣Frankly` | 2/58 (3%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| excuse (an excuse; excusing) | unclear | `␣Excuse` | 2/58 (3%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| ethics (ethics, morality (neutral)) | unclear | `␣Moral` | 2/58 (3%) | 0/30 (0%) | 4/133 (3%) | 0/199 (0%) |
| dismiss (dismissing) | unclear | `␣Dismiss` | 1/58 (2%) | 0/30 (0%) | 10/133 (8%) | 0/199 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## postresp_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| honest (honest, honesty) | truth | `␣Honestly`, `␣honesty`, `␣honest`, `␣Honest`, `honest`, `␣honestly`, `␣ईमानदारी`, `Honestly`, `␣ehrlich`, `正直` | 31/58 (53%) | 13/30 (43%) | 33/133 (25%) | 5/199 (3%) |
| shame (shame) | unclear | `␣Shame` | 10/58 (17%) | 12/30 (40%) | 21/133 (16%) | 3/199 (2%) |
| dismiss (dismissing) | unclear | `␣Dismiss` | 9/58 (16%) | 7/30 (23%) | 2/133 (2%) | 0/199 (0%) |
| excuse (an excuse; excusing) | unclear | `␣Excuse` | 11/58 (19%) | 4/30 (13%) | 4/133 (3%) | 0/199 (0%) |
| propaganda (slanted, misleading messaging) | lie | `␣Propaganda` | 5/58 (9%) | 4/30 (13%) | 0/133 (0%) | 0/199 (0%) |
| manipulate (manipulating someone) | lie | `␣Manip`, `␣Manipulation`, `manip` | 5/58 (9%) | 3/30 (10%) | 0/133 (0%) | 0/199 (0%) |
| truth (the truth) | truth | `␣Truth`, `truth` | 6/58 (10%) | 2/30 (7%) | 17/133 (13%) | 0/199 (0%) |
| apologize (apologizing; apology) | unclear | `道歉`, `␣apologize`, `␣apologies`, `␣apologized`, `␣apologised`, `␣apologizing`, `␣Sorry`, `Sorry` | 2/58 (3%) | 5/30 (17%) | 31/133 (23%) | 11/199 (6%) |
| deceive (the act of deceiving) | lie | `␣deception`, `␣decept`, `␣deceit`, `␣deceptive`, `␣deceiving` | 5/58 (9%) | 1/30 (3%) | 2/133 (2%) | 0/199 (0%) |
| refuse (refusing) | unclear | `␣رفض`, `␣refused` | 5/58 (9%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| sorry (sorry) | unclear | `␣Sorry`, `Sorry` | 2/58 (3%) | 4/30 (13%) | 21/133 (16%) | 11/199 (6%) |
| guilt (guilt, guilty) | unclear | `␣Guilty`, `␣guilty` | 5/58 (9%) | 1/30 (3%) | 2/133 (2%) | 0/199 (0%) |
| lie (a lie; the act of lying) | lie | `␣झूठ`, `␣lied`, `␣lie`, `lie`, `␣Lie`, `Lie`, `谎`, `␣LIE`, `LIE`, `␣lies`, `␣Lies`, `␣Lied`, `␣lying`, `␣거짓`, `␣মিথ্যা` | 5/58 (9%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| secret (secret, secrecy) | lie | `␣Secret`, `␣secretly`, `🤫` | 5/58 (9%) | 0/30 (0%) | 1/133 (1%) | 0/199 (0%) |
| protect (protecting) | unclear | `␣Protect`, `protect`, `␣Protecting`, `␣protecting`, `␣protect`, `␣Protection`, `␣Protective`, `␣protective`, `␣Protector`, `␣protector` | 3/58 (5%) | 2/30 (7%) | 0/133 (0%) | 0/199 (0%) |
| frank (frankly) | truth | `␣Frankly` | 3/58 (5%) | 2/30 (7%) | 0/133 (0%) | 0/199 (0%) |
| ethics (ethics, morality (neutral)) | unclear | `␣Moral`, `␣ethical`, `␣Ethical`, `ethical`, `␣ethics`, `␣Ethics`, `Ethics`, `␣ethically` | 4/58 (7%) | 1/30 (3%) | 5/133 (4%) | 3/199 (2%) |
| moral (morality) | unclear | `␣Moral` | 4/58 (7%) | 1/30 (3%) | 3/133 (2%) | 1/199 (1%) |
| correct (correct) | truth | `␣Right`, `␣correction`, `␣Correct`, `␣correcting`, `␣Correction`, `correction` | 0/58 (0%) | 5/30 (17%) | 11/133 (8%) | 38/199 (19%) |
| conceal (hiding or concealing something) | lie | `␣скры`, `␣concealing`, `␣Hidden` | 4/58 (7%) | 0/30 (0%) | 1/133 (1%) | 0/199 (0%) |
| cover (covering up) | lie | `␣Cover`, `Cover`, `cover`, `␣cover`, `␣Covering`, `␣covering` | 4/58 (7%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| confess (confessing; confession) | truth | `␣confession`, `␣confessed`, `␣confess`, `␣confesses` | 0/58 (0%) | 4/30 (13%) | 1/133 (1%) | 0/199 (0%) |
| false (false, untrue) | lie | `␣false`, `false`, `␣False`, `␣falsely`, `␣falsehood` | 4/58 (7%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| dishonest (not honest) | lie | `␣dishonest`, `␣dishonesty` | 1/58 (2%) | 1/30 (3%) | 1/133 (1%) | 0/199 (0%) |
| mislead (leading someone to a false belief) | lie | `␣misleading` | 2/58 (3%) | 0/30 (0%) | 1/133 (1%) | 0/199 (0%) |
| pretend (pretending) | lie | `␣pretending` | 2/58 (3%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| hidden (being hidden) | lie | `␣Hidden` | 2/58 (3%) | 0/30 (0%) | 1/133 (1%) | 0/199 (0%) |
| truthful (truthful, truthfully) | truth | `␣truthful`, `␣truthfully` | 1/58 (2%) | 1/30 (3%) | 12/133 (9%) | 0/199 (0%) |
| disclose (disclosing) | truth | `␣Disclosure`, `␣discloses` | 0/58 (0%) | 2/30 (7%) | 1/133 (1%) | 0/199 (0%) |
| concede (conceding) | truth | `␣conceding` | 0/58 (0%) | 2/30 (7%) | 1/133 (1%) | 0/199 (0%) |
| unethical (morally wrong) | unclear | `␣unethical`, `␣immoral` | 1/58 (2%) | 1/30 (3%) | 1/133 (1%) | 0/199 (0%) |
| disguise (disguising, masking) | lie | `␣Mask` | 2/58 (3%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| wrong (wrong, mistaken) | lie | `␣Wrong` | 2/58 (3%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| liar (a person who lies) | lie | `␣liar` | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| fake (fake, faked) | lie | `␣Fake` | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| bluff (bluffing) | lie | `␣bluff` | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| spin (putting a favourable spin on facts) | lie | `␣Spin`, `Spin` | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| shush (shushing face emoji: keep quiet) | lie | `🤫` | 1/58 (2%) | 0/30 (0%) | 1/133 (1%) | 0/199 (0%) |
| deflect (deflecting a question) | lie | `␣deflected` | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| avoid (avoiding) | unclear | `␣Avoid`, `avoid` | 1/58 (2%) | 0/30 (0%) | 1/133 (1%) | 0/199 (0%) |
| sincere (sincere, sincerely) | truth | `␣sincere`, `␣sincerity` | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| transparent (transparency) | truth | `␣Transparency`, `Transparency` | 0/58 (0%) | 1/30 (3%) | 5/133 (4%) | 1/199 (1%) |
| reveal (revealing) | truth | `␣revealed`, `␣reveals`, `␣revealing`, `␣Reveals`, `␣Revealed` | 0/58 (0%) | 1/30 (3%) | 1/133 (1%) | 0/199 (0%) |
| betray (betraying) | lie | `␣betray` | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccurate`, `incorrect` | 1/58 (2%) | 0/30 (0%) | 1/133 (1%) | 2/199 (1%) |
| true (true, real) | truth | `␣True`, `真实` | 0/58 (0%) | 0/30 (0%) | 3/133 (2%) | 0/199 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## postresp_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| truth (the truth) | truth | `␣सच्चाई`, `␣Truth`, `truth`, `␣truth`, `␣Wahrheit`, `Truth`, `真相`, `␣truths`, `␣Правда`, `␣सत्य`, `␣правда`, `verdad`, `␣vérité` | 23/58 (40%) | 17/30 (57%) | 51/133 (38%) | 0/199 (0%) |
| secret (secret, secrecy) | lie | `␣secretly`, `␣Secret`, `␣secrecy`, `secret`, `秘密`, `🤫` | 25/58 (43%) | 10/30 (33%) | 4/133 (3%) | 0/199 (0%) |
| shame (shame) | unclear | `␣Shame` | 19/58 (33%) | 12/30 (40%) | 23/133 (17%) | 1/199 (1%) |
| conceal (hiding or concealing something) | lie | `␣concealing`, `␣скры`, `␣concealed`, `␣conceal`, `␣concealment`, `␣hiding`, `隐藏`, `␣Hidden`, `␣hidden`, `hidden`, `Hidden`, `␣undisclosed`, `隐` | 21/58 (36%) | 8/30 (27%) | 5/133 (4%) | 13/199 (7%) |
| lie (a lie; the act of lying) | lie | `␣झूठ`, `␣lie`, `␣lies`, `谎`, `␣Lie`, `Lie`, `␣lying`, `␣거짓`, `␣মিথ্যা`, `lie`, `␣lied`, `␣LIE`, `␣Lies`, `謊`, `lies`, `lied`, `␣fib` | 21/58 (36%) | 7/30 (23%) | 2/133 (2%) | 0/199 (0%) |
| deceive (the act of deceiving) | lie | `␣deception`, `␣deceit`, `␣deceptive`, `␣deceive`, `␣deceiving`, `␣decept`, `␣deceived`, `骗`, `欺` | 19/58 (33%) | 8/30 (27%) | 6/133 (5%) | 0/199 (0%) |
| honest (honest, honesty) | truth | `␣honestly`, `␣Honestly`, `␣honesty`, `␣Honest`, `正直`, `honest`, `␣ईमानदारी`, `␣honest`, `␣ehrlich` | 13/58 (22%) | 11/30 (37%) | 22/133 (17%) | 0/199 (0%) |
| guilt (guilt, guilty) | unclear | `␣Guilty`, `␣guilty`, `␣guilt`, `␣culp` | 17/58 (29%) | 7/30 (23%) | 6/133 (5%) | 0/199 (0%) |
| omit (leaving something out) | lie | `␣omission`, `␣omitting`, `␣unspoken`, `␣умолча` | 15/58 (26%) | 8/30 (27%) | 4/133 (3%) | 0/199 (0%) |
| truthful (truthful, truthfully) | truth | `␣truthfully`, `␣truthful` | 13/58 (22%) | 7/30 (23%) | 36/133 (27%) | 0/199 (0%) |
| dishonest (not honest) | lie | `␣dishonest`, `␣dishonesty` | 11/58 (19%) | 6/30 (20%) | 3/133 (2%) | 0/199 (0%) |
| shush (shushing face emoji: keep quiet) | lie | `🤫` | 14/58 (24%) | 3/30 (10%) | 2/133 (2%) | 0/199 (0%) |
| unspoken (left unsaid) | lie | `␣unspoken` | 13/58 (22%) | 3/30 (10%) | 2/133 (2%) | 0/199 (0%) |
| avoid (avoiding) | unclear | `avoid`, `␣Avoid`, `␣avoid`, `Avoid`, `␣Avoiding`, `Avoiding`, `␣avoiding`, `␣avoids`, `␣avoided`, `␣avoidance`, `回避` | 10/58 (17%) | 4/30 (13%) | 3/133 (2%) | 1/199 (1%) |
| protect (protecting) | unclear | `␣Protect`, `protect`, `Protect`, `␣Protecting`, `␣protecting`, `␣protect`, `protection`, `␣protection`, `␣Protection`, `␣Protective`, `protective`, `␣protective`, `␣protects`, `␣protected` | 9/58 (16%) | 4/30 (13%) | 0/133 (0%) | 1/199 (1%) |
| withhold (withholding information; keeping silent about it) | lie | `␣умолча`, `␣withholding`, `␣withhold` | 6/58 (10%) | 6/30 (20%) | 2/133 (2%) | 0/199 (0%) |
| unfair (unfairness, injustice) | unclear | `␣injustice`, `␣unfairly`, `unfair` | 7/58 (12%) | 3/30 (10%) | 6/133 (5%) | 1/199 (1%) |
| hidden (being hidden) | lie | `␣Hidden`, `␣hidden`, `hidden`, `Hidden` | 5/58 (9%) | 3/30 (10%) | 2/133 (2%) | 9/199 (5%) |
| cover (covering up) | lie | `Cover`, `␣cover`, `␣Cover`, `cover`, `␣Covering`, `␣covering` | 7/58 (12%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| apologize (apologizing; apology) | unclear | `␣apologize`, `␣apology`, `␣apologies`, `␣apolog`, `␣apologized`, `␣apologised`, `␣apologizing`, `␣apologise`, `道歉`, `␣sorry`, `␣Sorry`, `sorry` | 2/58 (3%) | 6/30 (20%) | 9/133 (7%) | 0/199 (0%) |
| unethical (morally wrong) | unclear | `␣unethical`, `␣immoral` | 6/58 (10%) | 2/30 (7%) | 1/133 (1%) | 0/199 (0%) |
| propaganda (slanted, misleading messaging) | lie | `␣Propaganda`, `␣propaganda`, `␣propagand` | 5/58 (9%) | 2/30 (7%) | 0/133 (0%) | 0/199 (0%) |
| innocent (innocent) | unclear | `␣Innoc`, `␣Innocent`, `␣innocent` | 5/58 (9%) | 2/30 (7%) | 0/133 (0%) | 0/199 (0%) |
| ethics (ethics, morality (neutral)) | unclear | `␣ethical`, `␣Ethics`, `␣ethically`, `␣morally`, `␣Ethical`, `ethical`, `␣ethics`, `Ethics`, `ethics`, `␣Moral`, `␣moral`, `moral`, `␣morality` | 5/58 (9%) | 2/30 (7%) | 1/133 (1%) | 1/199 (1%) |
| mislead (leading someone to a false belief) | lie | `␣misleading` | 4/58 (7%) | 2/30 (7%) | 1/133 (1%) | 0/199 (0%) |
| pretend (pretending) | lie | `␣pretending` | 5/58 (9%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| minimize (minimizing) | unclear | `␣Minimize`, `␣minimizing`, `␣minimising`, `␣minimized`, `␣minimizar`, `␣minimize`, `␣minimizes`, `minimize`, `Minimize` | 4/58 (7%) | 2/30 (7%) | 1/133 (1%) | 1/199 (1%) |
| moral (morality) | unclear | `␣morally`, `␣moral`, `␣Moral`, `␣morality`, `moral` | 5/58 (9%) | 1/30 (3%) | 1/133 (1%) | 1/199 (1%) |
| false (false, untrue) | lie | `␣false`, `false`, `␣falsely`, `␣falsehood` | 6/58 (10%) | 0/30 (0%) | 2/133 (2%) | 0/199 (0%) |
| liar (a person who lies) | lie | `␣liar` | 5/58 (9%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| manipulate (manipulating someone) | lie | `manip`, `␣Manip`, `␣Manipulation` | 3/58 (5%) | 2/30 (7%) | 0/133 (0%) | 0/199 (0%) |
| fraud (fraud) | lie | `␣fraud`, `␣fraudulent`, `␣frauds`, `Fraud` | 4/58 (7%) | 1/30 (3%) | 4/133 (3%) | 0/199 (0%) |
| deflect (deflecting a question) | lie | `␣deflect`, `␣deflected`, `␣deflection` | 4/58 (7%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| betray (betraying) | lie | `␣betrayal`, `␣betrayed`, `␣betray` | 3/58 (5%) | 2/30 (7%) | 1/133 (1%) | 0/199 (0%) |
| refuse (refusing) | unclear | `␣refused`, `␣refusing`, `␣رفض`, `␣отказыва` | 3/58 (5%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| fake (fake, faked) | lie | `␣Fake`, `␣fake`, `Fake`, `fake`, `FAKE` | 3/58 (5%) | 0/30 (0%) | 1/133 (1%) | 0/199 (0%) |
| wrongdoing (wrongdoing) | unclear | `␣wrongdoing` | 2/58 (3%) | 1/30 (3%) | 1/133 (1%) | 0/199 (0%) |
| disguise (disguising, masking) | lie | `␣disguised` | 2/58 (3%) | 1/30 (3%) | 0/133 (0%) | 1/199 (1%) |
| obfuscate (obfuscating) | lie | `␣obfusc` | 1/58 (2%) | 2/30 (7%) | 0/133 (0%) | 0/199 (0%) |
| correct (correct) | truth | `right`, `␣Right`, `␣correction`, `␣Correct`, `␣corrective`, `␣correcting`, `␣Correction`, `correction` | 1/58 (2%) | 2/30 (7%) | 4/133 (3%) | 9/199 (5%) |
| bluff (bluffing) | lie | `␣bluff` | 2/58 (3%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| exaggerate (exaggerating) | lie | `␣exaggeration`, `␣exaggerate`, `␣exaggerated` | 1/58 (2%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| evade (evading or dodging) | lie | `␣evade`, `␣evasion`, `回避`, `␣dodge` | 1/58 (2%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| frank (frankly) | truth | `␣Frankly` | 1/58 (2%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| transparent (transparency) | truth | `␣transparency`, `␣Transparency`, `Transparency`, `␣transparent`, `Transparent`, `␣Transparent`, `␣transparente`, `␣transparencia`, `␣transparence` | 0/58 (0%) | 2/30 (7%) | 8/133 (6%) | 0/199 (0%) |
| unapologetic (not apologizing) | unclear | `␣unapolog` | 1/58 (2%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| humiliation (humiliation) | unclear | `␣humiliation`, `␣humiliating`, `␣humiliated` | 1/58 (2%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 2/58 (3%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| evade (evading) | lie | `␣evas`, `␣evade`, `␣evasion` | 1/58 (2%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| silence (silence) | unclear | `␣silencio` | 1/58 (2%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| true (true, real) | truth | `␣True`, `真实` | 2/58 (3%) | 0/30 (0%) | 1/133 (1%) | 1/199 (1%) |
| cheat (cheating) | lie | `␣cheating` | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| distort (distorting the facts) | lie | `␣distortion` | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| spin (putting a favourable spin on facts) | lie | `␣spin` | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| confidential (confidentiality) | lie | `␣confidentiality` | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| excuse (an excuse; excusing) | unclear | `␣Excuse` | 1/58 (2%) | 0/30 (0%) | 1/133 (1%) | 0/199 (0%) |
| disclose (disclosing) | truth | `␣Disclosure`, `Disclosure`, `␣disclosure`, `disclosure`, `␣disclose` | 0/58 (0%) | 1/30 (3%) | 10/133 (8%) | 0/199 (0%) |
| reveal (revealing) | truth | `␣Reveals`, `␣Reveal`, `Reveal` | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| confess (confessing; confession) | truth | `␣confession` | 1/58 (2%) | 0/30 (0%) | 3/133 (2%) | 0/199 (0%) |
| sorry (sorry) | unclear | `␣Sorry`, `␣sorry`, `sorry` | 1/58 (2%) | 0/30 (0%) | 4/133 (3%) | 0/199 (0%) |
| conscience (conscience) | unclear | `␣conscience` | 0/58 (0%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| dismiss (dismissing) | unclear | `␣dismiss` | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| wrong (wrong, mistaken) | lie | `wrong` | 1/58 (2%) | 0/30 (0%) | 1/133 (1%) | 0/199 (0%) |
| incorrect (incorrect) | lie | `␣incorrect` | 0/58 (0%) | 0/30 (0%) | 1/133 (1%) | 1/199 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## postresp_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| correct (correct) | truth | `␣right`, `Right`, `␣Right`, `␣Correct` | 10/58 (17%) | 6/30 (20%) | 7/133 (5%) | 5/199 (3%) |
| refuse (refusing) | unclear | `␣отказаться`, `␣رفض` | 9/58 (16%) | 1/30 (3%) | 12/133 (9%) | 0/199 (0%) |
| apologize (apologizing; apology) | unclear | `道歉`, `␣apologised` | 5/58 (9%) | 3/30 (10%) | 5/133 (4%) | 0/199 (0%) |
| honest (honest, honesty) | truth | `␣Honestly` | 2/58 (3%) | 1/30 (3%) | 0/133 (0%) | 0/199 (0%) |
| frank (frankly) | truth | `␣Frankly` | 2/58 (3%) | 0/30 (0%) | 0/133 (0%) | 0/199 (0%) |
| excuse (an excuse; excusing) | unclear | `␣Excuse`, `␣excuse`, `Excuse` | 1/58 (2%) | 0/30 (0%) | 0/133 (0%) | 1/199 (1%) |
| true (true, real) | truth | `␣True` | 0/58 (0%) | 0/30 (0%) | 2/133 (2%) | 3/199 (2%) |
