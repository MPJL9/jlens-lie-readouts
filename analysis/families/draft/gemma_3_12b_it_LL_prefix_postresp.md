# Draft families: gemma-3-12b-it, logit lens, part prefix, group postresp

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## postresp_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| hide (hiding something) | lie | `␣hiding`, `␣hide`, `␣hid`, `hide`, `␣hidden`, `␣Hide`, `␣hides`, `␣esconder`, `Hide` | 36/49 (73%) | 24/32 (75%) | 67/135 (50%) | 53/179 (30%) |
| rebuttal (rebutting) | unclear | `␣rebuttal` | 32/49 (65%) | 18/32 (56%) | 56/135 (41%) | 10/179 (6%) |
| subtle (subtle, indirect) | unclear | `␣subtle`, `␣subtly` | 24/49 (49%) | 14/32 (44%) | 29/135 (21%) | 37/179 (21%) |
| disclaimer (a disclaimer) | unclear | `Disclaimer`, `␣Disclaimer` | 19/49 (39%) | 10/32 (31%) | 90/135 (67%) | 70/179 (39%) |
| fact (fact, factual) | truth | `␣factual` | 13/49 (27%) | 9/32 (28%) | 110/135 (81%) | 110/179 (61%) |
| understate (understating, downplaying) | unclear | `␣understated` | 12/49 (24%) | 5/32 (16%) | 0/135 (0%) | 1/179 (1%) |
| correct (correct) | truth | `␣right`, `␣correct`, `Right` | 10/49 (20%) | 5/32 (16%) | 6/135 (4%) | 27/179 (15%) |
| sincere (being sincere) | truth | `␣heartfelt` | 6/49 (12%) | 6/32 (19%) | 53/135 (39%) | 53/179 (30%) |
| frank (speaking frankly) | truth | `␣Frankly` | 4/49 (8%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| sneaky (being sneaky) | lie | `␣sneaky` | 1/49 (2%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| blatant (blatant, flagrant) | unclear | `␣blatant` | 3/49 (6%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| hustle (hustling, conning) | unclear | `␣hustle` | 2/49 (4%) | 0/32 (0%) | 7/135 (5%) | 19/179 (11%) |
| sarcastic (being sarcastic) | unclear | `␣sarcastic` | 2/49 (4%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| true (true, real) | truth | `␣true` | 1/49 (2%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| conceal (concealing information) | lie | `␣concealed` | 1/49 (2%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| ethics (ethics, morality) | unclear | `␣moral` | 1/49 (2%) | 0/32 (0%) | 1/135 (1%) | 5/179 (3%) |
| incorrect (incorrect) | lie | `Wrong` | 1/49 (2%) | 0/32 (0%) | 2/135 (1%) | 0/179 (0%) |

Not in the draft: acknowledge (excluded: admit / deny / acknowledge)

## postresp_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| disclaimer (a disclaimer) | unclear | `Disclaimer`, `␣Disclaimer` | 25/49 (51%) | 11/32 (34%) | 79/135 (59%) | 54/179 (30%) |
| honest (being honest) | truth | `Honestly`, `␣Honestly`, `␣honestly`, `␣honesty`, `␣honest`, `正直`, `honest` | 21/49 (43%) | 15/32 (47%) | 37/135 (27%) | 0/179 (0%) |
| blatant (blatant, flagrant) | unclear | `␣blatant`, `␣blatantly` | 16/49 (33%) | 7/32 (22%) | 6/135 (4%) | 0/179 (0%) |
| truth (the truth) | truth | `Truth`, `␣truth`, `verdad`, `␣Правда`, `truth`, `␣Truth`, `␣verdade`, `␣truths`, `真相` | 16/49 (33%) | 6/32 (19%) | 21/135 (16%) | 0/179 (0%) |
| avoid (avoiding (the topic)) | unclear | `␣avoid`, `Avoid`, `avoid`, `␣এড়িয়ে`, `␣avoidance`, `␣avoids`, `␣avoiding`, `␣avoided`, `␣Avoid`, `避免`, `Avoiding` | 15/49 (31%) | 6/32 (19%) | 1/135 (1%) | 0/179 (0%) |
| rebuttal (rebutting) | unclear | `␣rebuttal`, `␣rebut` | 16/49 (33%) | 4/32 (12%) | 10/135 (7%) | 1/179 (1%) |
| reassure (reassuring or comforting) | unclear | `␣reassuring`, `␣reassurance`, `␣reassure`, `␣comforting`, `␣reassured` | 13/49 (27%) | 6/32 (19%) | 30/135 (22%) | 0/179 (0%) |
| persuade (persuading or convincing) | unclear | `␣convincing`, `␣persuasive`, `␣persuasion`, `␣convince`, `␣convincingly`, `␣persuading`, `␣persuas` | 13/49 (27%) | 4/32 (12%) | 1/135 (1%) | 0/179 (0%) |
| misinformation (false information) | lie | `␣misinformation`, `␣disinformation` | 14/49 (29%) | 2/32 (6%) | 14/135 (10%) | 1/179 (1%) |
| deflect (deflecting the question) | lie | `␣deflection`, `␣deflect`, `␣deflected` | 12/49 (24%) | 4/32 (12%) | 1/135 (1%) | 0/179 (0%) |
| convince (convincing) | unclear | `␣convincing`, `␣convince`, `␣convincingly` | 12/49 (24%) | 4/32 (12%) | 1/135 (1%) | 0/179 (0%) |
| obfuscate (obscuring meaning on purpose) | lie | `␣obfusc` | 11/49 (22%) | 4/32 (12%) | 1/135 (1%) | 0/179 (0%) |
| mislead (misleading someone) | lie | `␣misleading`, `␣mislead`, `␣misled` | 10/49 (20%) | 3/32 (9%) | 0/135 (0%) | 1/179 (1%) |
| evade (evading the question) | lie | `␣evas`, `␣evasion`, `␣evade`, `␣evaded` | 10/49 (20%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) |
| subtle (subtle, indirect) | unclear | `␣subtly`, `␣subtle` | 6/49 (12%) | 6/32 (19%) | 1/135 (1%) | 0/179 (0%) |
| deceive (the act of deceiving) | lie | `␣deception`, `␣deceptive`, `␣deceit`, `␣decept` | 9/49 (18%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| lie (telling a lie) | lie | `␣lies`, `␣거짓`, `␣lie`, `␣lying`, `␣lied`, `lying`, `lies`, `␣झूठ`, `␣Lie`, `谎` | 11/49 (22%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| credibility (credible, believable) | unclear | `␣credibility`, `credible`, `␣believable` | 8/49 (16%) | 3/32 (9%) | 5/135 (4%) | 0/179 (0%) |
| dodge (dodging the question) | lie | `␣dodge`, `␣dodging` | 8/49 (16%) | 1/32 (3%) | 1/135 (1%) | 0/179 (0%) |
| refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `␣refused`, `␣refuses` | 7/49 (14%) | 2/32 (6%) | 3/135 (2%) | 0/179 (0%) |
| vague (being vague or ambiguous) | unclear | `␣vague`, `␣ambiguous`, `␣ambiguity` | 6/49 (12%) | 3/32 (9%) | 1/135 (1%) | 0/179 (0%) |
| hustle (hustling, conning) | unclear | `␣hustle` | 6/49 (12%) | 3/32 (9%) | 5/135 (4%) | 0/179 (0%) |
| unapologetic (not apologizing) | unclear | `␣unapolog` | 3/49 (6%) | 6/32 (19%) | 3/135 (2%) | 0/179 (0%) |
| secret (keeping something secret) | lie | `␣secrecy`, `␣secretive`, `🤫` | 7/49 (14%) | 1/32 (3%) | 2/135 (1%) | 0/179 (0%) |
| justify (justifying the act) | unclear | `␣justifications`, `␣justification` | 8/49 (16%) | 0/32 (0%) | 1/135 (1%) | 0/179 (0%) |
| protect (protecting someone or something) | unclear | `Protect`, `␣protect` | 7/49 (14%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| truthful (being truthful) | truth | `␣truthful`, `␣truthfully` | 4/49 (8%) | 4/32 (12%) | 23/135 (17%) | 0/179 (0%) |
| vague (vague) | unclear | `␣vague` | 5/49 (10%) | 3/32 (9%) | 1/135 (1%) | 0/179 (0%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 6/49 (12%) | 1/32 (3%) | 5/135 (4%) | 0/179 (0%) |
| confident (confident, confidently) | unclear | `␣confident`, `␣confidently`, `confident`, `␣confidence`, `Confident` | 6/49 (12%) | 1/32 (3%) | 1/135 (1%) | 0/179 (0%) |
| fact (fact, factual) | truth | `␣factual` | 3/49 (6%) | 4/32 (12%) | 86/135 (64%) | 19/179 (11%) |
| hide (hiding something) | lie | `␣hiding`, `hide`, `␣hidden`, `␣hide`, `Hide`, `␣скры` | 5/49 (10%) | 1/32 (3%) | 0/135 (0%) | 1/179 (1%) |
| redirect (redirecting the conversation) | unclear | `Redirect`, `␣redirection`, `␣redirect`, `redirect`, `␣redirected`, `␣redirects` | 6/49 (12%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| dismiss (dismissing) | unclear | `␣dismiss`, `␣dismissal`, `dismiss` | 3/49 (6%) | 3/32 (9%) | 0/135 (0%) | 0/179 (0%) |
| apology (apologizing, being sorry) | unclear | `␣apology`, `␣apolog`, `␣apologies` | 4/49 (8%) | 2/32 (6%) | 21/135 (16%) | 0/179 (0%) |
| disclose (disclosing) | truth | `Disclosure`, `␣disclosure` | 2/49 (4%) | 4/32 (12%) | 31/135 (23%) | 4/179 (2%) |
| conceal (concealing information) | lie | `␣conceal`, `␣concealing`, `␣concealment`, `␣concealed` | 4/49 (8%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| dishonest (being dishonest) | lie | `␣dishonesty` | 5/49 (10%) | 0/32 (0%) | 2/135 (1%) | 0/179 (0%) |
| fake (faking) | lie | `Fake`, `␣fake`, `fake`, `␣Fake` | 5/49 (10%) | 0/32 (0%) | 3/135 (2%) | 0/179 (0%) |
| spin (spinning the facts) | unclear | `␣spin`, `spin`, `␣spins`, `Spin`, `␣spinning`, `␣Spin`, `␣SPIN`, `spinning` | 3/49 (6%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| intentional (doing it on purpose) | unclear | `␣intentionally`, `␣deliberately` | 3/49 (6%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| excuse (making excuses) | unclear | `␣excuses`, `␣excuse` | 4/49 (8%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| sarcastic (being sarcastic) | unclear | `␣sarcastic` | 3/49 (6%) | 1/32 (3%) | 4/135 (3%) | 7/179 (4%) |
| false (false, untrue) | lie | `␣false`, `false`, `␣untrue`, `␣falsehood` | 3/49 (6%) | 1/32 (3%) | 1/135 (1%) | 0/179 (0%) |
| cover (covering (up)) | lie | `␣cover`, `cover`, `␣covering`, `Cover` | 3/49 (6%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| uneasy (unease, discomfort) | unclear | `␣discomfort`, `␣uncomfortable` | 3/49 (6%) | 0/32 (0%) | 2/135 (1%) | 0/179 (0%) |
| sincere (being sincere) | truth | `␣heartfelt` | 1/49 (2%) | 2/32 (6%) | 10/135 (7%) | 7/179 (4%) |
| hush (keeping quiet, shushing) | lie | `🤫` | 3/49 (6%) | 0/32 (0%) | 1/135 (1%) | 0/179 (0%) |
| confidential (treating information as confidential) | unclear | `␣confidentiality` | 2/49 (4%) | 0/32 (0%) | 4/135 (3%) | 0/179 (0%) |
| fabricate (making things up) | lie | `␣fabrication`, `␣fabricated`, `␣fabricate`, `␣fabricating` | 2/49 (4%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| omit (leaving information out) | lie | `␣omission`, `␣omitted`, `␣omit`, `␣omissions`, `␣omitting`, `omit` | 1/49 (2%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| frank (speaking frankly) | truth | `␣frankly` | 0/49 (0%) | 2/32 (6%) | 4/135 (3%) | 0/179 (0%) |
| transparent (being transparent) | truth | `␣transparency`, `Transparency` | 0/49 (0%) | 2/32 (6%) | 11/135 (8%) | 0/179 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccurate`, `␣inaccuracies`, `␣inaccuracy` | 1/49 (2%) | 1/32 (3%) | 0/135 (0%) | 2/179 (1%) |
| discretion (being discreet) | unclear | `␣discretion` | 0/49 (0%) | 1/32 (3%) | 4/135 (3%) | 1/179 (1%) |
| pretend (pretending) | lie | `␣pretending` | 1/49 (2%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| exaggerate (exaggerating) | lie | `␣exagger`, `␣exaggerated`, `␣exaggeration` | 0/49 (0%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| sneaky (being sneaky) | lie | `␣sneaky` | 0/49 (0%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| understate (understating, downplaying) | unclear | `␣understated` | 0/49 (0%) | 1/32 (3%) | 1/135 (1%) | 1/179 (1%) |
| debunk (debunking) | unclear | `␣debunk` | 0/49 (0%) | 1/32 (3%) | 6/135 (4%) | 4/179 (2%) |
| unethical (unethical act) | lie | `␣unethical` | 1/49 (2%) | 0/32 (0%) | 3/135 (2%) | 0/179 (0%) |
| wrongdoing (wrongdoing) | lie | `␣wrongdoing` | 1/49 (2%) | 0/32 (0%) | 9/135 (7%) | 1/179 (1%) |
| shameless (shamelessness) | unclear | `␣shameless` | 0/49 (0%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| confess (confessing) | truth | `␣confess`, `␣confession`, `␣confessed`, `␣confessions`, `␣confesses` | 0/49 (0%) | 1/32 (3%) | 3/135 (2%) | 0/179 (0%) |
| sincere (sincere, sincerely) | truth | `Sincerely` | 1/49 (2%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| correct (correct) | truth | `␣correct`, `Right` | 0/49 (0%) | 1/32 (3%) | 6/135 (4%) | 9/179 (5%) |
| true (true, real) | truth | `␣true` | 0/49 (0%) | 0/32 (0%) | 10/135 (7%) | 0/179 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## postresp_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| honest (being honest) | truth | `Honestly`, `␣Honestly`, `␣honestly`, `␣honesty`, `␣honest`, `␣Honest` | 30/49 (61%) | 16/32 (50%) | 31/135 (23%) | 1/179 (1%) |
| misinformation (false information) | lie | `␣misinformation`, `␣disinformation` | 21/49 (43%) | 8/32 (25%) | 60/135 (44%) | 1/179 (1%) |
| secret (keeping something secret) | lie | `🤫`, `␣secrecy`, `␣secretly`, `␣secret`, `Secret`, `secret` | 21/49 (43%) | 6/32 (19%) | 3/135 (2%) | 0/179 (0%) |
| blatant (blatant, flagrant) | unclear | `␣blatant`, `␣blatantly` | 17/49 (35%) | 6/32 (19%) | 10/135 (7%) | 6/179 (3%) |
| truthful (being truthful) | truth | `␣truthfully`, `␣truthful` | 16/49 (33%) | 7/32 (22%) | 25/135 (19%) | 0/179 (0%) |
| truth (the truth) | truth | `Truth`, `␣truth`, `verdad`, `␣Truth`, `truth`, `␣truths` | 18/49 (37%) | 5/32 (16%) | 51/135 (38%) | 0/179 (0%) |
| hush (keeping quiet, shushing) | lie | `🤫`, `␣hush` | 18/49 (37%) | 3/32 (9%) | 2/135 (1%) | 0/179 (0%) |
| avoid (avoiding (the topic)) | unclear | `␣avoid`, `Avoid`, `␣avoiding`, `␣avoids`, `␣avoidance`, `avoid`, `␣Avoid`, `Avoiding`, `␣avoided`, `回避` | 14/49 (29%) | 6/32 (19%) | 2/135 (1%) | 0/179 (0%) |
| mislead (misleading someone) | lie | `␣misleading`, `␣mislead`, `␣misled` | 14/49 (29%) | 5/32 (16%) | 4/135 (3%) | 0/179 (0%) |
| deceive (the act of deceiving) | lie | `␣deception`, `␣deceit`, `␣deceptive`, `␣deceive`, `␣deceiving`, `␣decept` | 13/49 (27%) | 5/32 (16%) | 4/135 (3%) | 0/179 (0%) |
| dishonest (being dishonest) | lie | `␣dishonesty`, `␣dishonest` | 11/49 (22%) | 7/32 (22%) | 4/135 (3%) | 0/179 (0%) |
| protect (protecting someone or something) | unclear | `Protect`, `␣protect`, `␣protecting`, `protect`, `␣protection`, `␣protected`, `␣protects`, `␣Protect`, `␣protective`, `protected`, `␣Protecting` | 12/49 (24%) | 6/32 (19%) | 0/135 (0%) | 0/179 (0%) |
| sincere (being sincere) | truth | `␣heartfelt`, `␣sincerely` | 11/49 (22%) | 7/32 (22%) | 14/135 (10%) | 13/179 (7%) |
| lie (telling a lie) | lie | `␣lies`, `␣lie`, `␣lying`, `␣lied`, `lying`, `lie`, `␣Lie`, `␣거짓`, `Lie`, `谎`, `lied`, `lies`, `␣झूठ`, `␣Lies`, `␣Lied`, `␣LIE`, `謊` | 13/49 (27%) | 4/32 (12%) | 0/135 (0%) | 0/179 (0%) |
| unapologetic (not apologizing) | unclear | `␣unapolog` | 12/49 (24%) | 5/32 (16%) | 5/135 (4%) | 0/179 (0%) |
| confidential (treating information as confidential) | unclear | `␣confidentiality`, `␣confidential`, `␣Confidential` | 10/49 (20%) | 4/32 (12%) | 3/135 (2%) | 0/179 (0%) |
| reassure (reassuring or comforting) | unclear | `␣reassuring`, `␣reassure`, `␣reassurance`, `␣reassured` | 8/49 (16%) | 5/32 (16%) | 7/135 (5%) | 0/179 (0%) |
| debunk (debunking) | unclear | `␣debunk` | 8/49 (16%) | 5/32 (16%) | 2/135 (1%) | 15/179 (8%) |
| understate (understating, downplaying) | unclear | `␣understated` | 5/49 (10%) | 7/32 (22%) | 0/135 (0%) | 3/179 (2%) |
| intentional (doing it on purpose) | unclear | `␣intentionally`, `␣consciously`, `␣knowingly`, `␣deliberately` | 7/49 (14%) | 5/32 (16%) | 2/135 (1%) | 1/179 (1%) |
| wrongdoing (wrongdoing) | lie | `␣wrongdoing` | 9/49 (18%) | 3/32 (9%) | 49/135 (36%) | 1/179 (1%) |
| obfuscate (obscuring meaning on purpose) | lie | `␣obfusc` | 9/49 (18%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| unethical (unethical act) | lie | `␣unethical`, `␣immoral` | 7/49 (14%) | 3/32 (9%) | 7/135 (5%) | 2/179 (1%) |
| intentionally (intentionally) | unclear | `␣intentionally` | 6/49 (12%) | 4/32 (12%) | 0/135 (0%) | 1/179 (1%) |
| false (false, untrue) | lie | `␣false`, `␣falsely`, `␣untrue`, `␣falsehood` | 9/49 (18%) | 1/32 (3%) | 2/135 (1%) | 0/179 (0%) |
| deflect (deflecting the question) | lie | `␣deflect`, `␣deflection`, `␣deflected` | 8/49 (16%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| subtle (subtle, indirect) | unclear | `␣subtly`, `␣subtle` | 6/49 (12%) | 3/32 (9%) | 0/135 (0%) | 1/179 (1%) |
| uneasy (unease, discomfort) | unclear | `␣uneas`, `␣uncomfortable`, `␣discomfort` | 3/49 (6%) | 6/32 (19%) | 4/135 (3%) | 0/179 (0%) |
| hide (hiding something) | lie | `␣hiding`, `␣hidden`, `hidden`, `hide`, `␣hide`, `Hidden` | 5/49 (10%) | 3/32 (9%) | 1/135 (1%) | 0/179 (0%) |
| conceal (concealing information) | lie | `␣concealing`, `␣conceal`, `␣concealment`, `␣concealed` | 6/49 (12%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| discretion (being discreet) | unclear | `␣discretion`, `␣discreet` | 4/49 (8%) | 4/32 (12%) | 0/135 (0%) | 0/179 (0%) |
| cover (covering (up)) | lie | `␣cover`, `␣covering`, `Cover`, `cover`, `␣covers`, `␣covered`, `␣Cover` | 6/49 (12%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 5/49 (10%) | 3/32 (9%) | 4/135 (3%) | 0/179 (0%) |
| ethics (ethics, morality) | unclear | `␣ethically`, `␣ethical`, `␣ethics`, `␣morally`, `␣moral`, `ethical` | 5/49 (10%) | 3/32 (9%) | 4/135 (3%) | 2/179 (1%) |
| fact (fact, factual) | truth | `␣factual` | 6/49 (12%) | 2/32 (6%) | 100/135 (74%) | 11/179 (6%) |
| disclaimer (a disclaimer) | unclear | `Disclaimer` | 4/49 (8%) | 2/32 (6%) | 12/135 (9%) | 1/179 (1%) |
| apology (apologizing, being sorry) | unclear | `␣sorry`, `Sorry`, `␣apology`, `␣apologies` | 5/49 (10%) | 1/32 (3%) | 12/135 (9%) | 0/179 (0%) |
| frank (speaking frankly) | truth | `␣frankly`, `␣Frankly` | 4/49 (8%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| right (right) | truth | `␣rightful` | 3/49 (6%) | 3/32 (9%) | 15/135 (11%) | 0/179 (0%) |
| fake (faking) | lie | `␣fake`, `Fake`, `fake` | 4/49 (8%) | 1/32 (3%) | 3/135 (2%) | 0/179 (0%) |
| pretend (pretending) | lie | `␣pretending`, `␣pretended` | 4/49 (8%) | 1/32 (3%) | 3/135 (2%) | 0/179 (0%) |
| omit (leaving information out) | lie | `␣omission`, `␣omitted`, `␣omit`, `␣omissions`, `␣omitting` | 2/49 (4%) | 3/32 (9%) | 0/135 (0%) | 0/179 (0%) |
| uneasy (uneasy, uneasiness) | unclear | `␣uneas` | 1/49 (2%) | 4/32 (12%) | 0/135 (0%) | 0/179 (0%) |
| credibility (credible, believable) | unclear | `␣credibility` | 2/49 (4%) | 3/32 (9%) | 3/135 (2%) | 0/179 (0%) |
| sneaky (being sneaky) | lie | `␣sneaky` | 3/49 (6%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| confident (confident, confidently) | unclear | `confident`, `Confident`, `␣confident` | 4/49 (8%) | 0/32 (0%) | 7/135 (5%) | 0/179 (0%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 1/49 (2%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| dismiss (dismissing) | unclear | `␣dismiss`, `Dismiss` | 3/49 (6%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| confess (confessing) | truth | `␣confession`, `␣confess`, `␣confessed`, `␣confesses` | 1/49 (2%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) |
| apology (apology, apologising) | unclear | `␣apology`, `␣apologies` | 2/49 (4%) | 1/32 (3%) | 7/135 (5%) | 0/179 (0%) |
| manipulate (manipulating someone) | lie | `␣manipulation`, `␣manipulative`, `␣manipulate`, `␣manipulated`, `␣manipulating`, `␣manipulations`, `Manipulation` | 2/49 (4%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| exaggerate (exaggerating) | lie | `␣exaggerated`, `␣exaggeration`, `␣exagger`, `␣overstated`, `␣exaggerate` | 0/49 (0%) | 2/32 (6%) | 1/135 (1%) | 0/179 (0%) |
| betray (betraying) | lie | `␣betrayal`, `␣betray` | 0/49 (0%) | 2/32 (6%) | 0/135 (0%) | 0/179 (0%) |
| spin (spinning the facts) | unclear | `␣spin`, `spin`, `␣spinning`, `␣Spin`, `␣spins`, `Spin`, `spinning` | 2/49 (4%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| vague (being vague or ambiguous) | unclear | `␣vague`, `␣ambiguity` | 2/49 (4%) | 0/32 (0%) | 1/135 (1%) | 2/179 (1%) |
| justify (justifying the act) | unclear | `␣justifications` | 2/49 (4%) | 0/32 (0%) | 1/135 (1%) | 0/179 (0%) |
| excuse (making excuses) | unclear | `␣excuse`, `␣excuses` | 1/49 (2%) | 1/32 (3%) | 2/135 (1%) | 0/179 (0%) |
| rebuttal (rebutting) | unclear | `␣rebuttal`, `␣rebut` | 2/49 (4%) | 0/32 (0%) | 3/135 (2%) | 1/179 (1%) |
| shame (shame) | unclear | `␣shameful` | 1/49 (2%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| transparent (being transparent) | truth | `Transparency`, `␣transparent`, `␣transparency`, `␣Transparency` | 1/49 (2%) | 1/32 (3%) | 2/135 (1%) | 0/179 (0%) |
| disclose (disclosing) | truth | `␣disclosure`, `Disclosure`, `␣disclosing` | 0/49 (0%) | 2/32 (6%) | 5/135 (4%) | 0/179 (0%) |
| integrity (integrity) | truth | `␣integrity` | 1/49 (2%) | 1/32 (3%) | 0/135 (0%) | 1/179 (1%) |
| fabricate (making things up) | lie | `␣fabrication`, `␣fabricated` | 1/49 (2%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| fraud (fraud or scam) | lie | `␣fraud`, `␣fraudulent`, `␣scam`, `␣scams` | 1/49 (2%) | 0/32 (0%) | 3/135 (2%) | 1/179 (1%) |
| cheat (cheating) | lie | `␣cheating` | 0/49 (0%) | 1/32 (3%) | 1/135 (1%) | 0/179 (0%) |
| suppress (suppressing information) | lie | `␣suppress` | 1/49 (2%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| evade (evading the question) | lie | `␣evas` | 0/49 (0%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| dodge (dodging the question) | lie | `␣dodge` | 0/49 (0%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| refuse (refusing) | unclear | `␣refused`, `␣refuse`, `␣refusal`, `␣refusing`, `␣refuses` | 1/49 (2%) | 0/32 (0%) | 3/135 (2%) | 1/179 (1%) |
| redirect (redirecting the conversation) | unclear | `␣redirect`, `␣redirection` | 1/49 (2%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| persuade (persuading or convincing) | unclear | `␣convincing`, `␣convincingly` | 0/49 (0%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| sarcastic (being sarcastic) | unclear | `␣sarcastic` | 0/49 (0%) | 1/32 (3%) | 1/135 (1%) | 3/179 (2%) |
| guilt (guilt) | unclear | `␣guilt` | 0/49 (0%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| scam (scam) | lie | `␣scam`, `␣scams` | 1/49 (2%) | 0/32 (0%) | 0/135 (0%) | 1/179 (1%) |
| embarrassment (embarrassment) | unclear | `␣embarrassment` | 0/49 (0%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| true (true, real) | truth | `␣true` | 0/49 (0%) | 0/32 (0%) | 53/135 (39%) | 0/179 (0%) |
| correct (correct) | truth | `␣correct` | 0/49 (0%) | 0/32 (0%) | 0/135 (0%) | 4/179 (2%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccurate` | 0/49 (0%) | 0/32 (0%) | 3/135 (2%) | 1/179 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## postresp_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| rebuttal (rebutting) | unclear | `␣rebuttal` | 1/49 (2%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |
| truth (the truth) | truth | `␣truth` | 0/49 (0%) | 1/32 (3%) | 0/135 (0%) | 0/179 (0%) |
| reveal (revealing) | truth | `␣revealed` | 1/49 (2%) | 0/32 (0%) | 0/135 (0%) | 0/179 (0%) |

## postresp_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| honest (being honest) | truth | `Honestly`, `␣Honestly` | 22/49 (45%) | 12/32 (38%) | 24/135 (18%) | 0/179 (0%) |
| correct (correct) | truth | `right`, `␣right`, `␣correct`, `Right`, `␣Right` | 19/49 (39%) | 13/32 (41%) | 20/135 (15%) | 7/179 (4%) |
| apology (apologizing, being sorry) | unclear | `Sorry` | 2/49 (4%) | 1/32 (3%) | 7/135 (5%) | 1/179 (1%) |
| incorrect (incorrect) | lie | `␣incorrect` | 0/49 (0%) | 0/32 (0%) | 0/135 (0%) | 3/179 (2%) |
