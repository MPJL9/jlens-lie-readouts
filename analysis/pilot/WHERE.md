# Where the situation words of the readout sit inside the response (Qwen3.6-27B, J-lens, band 35-58)

Written by `scripts/pilot/where_words_sit.py`. Build split plus the unrelated sets, in-sample. A token *carries* a list
when one of the list's tokens is in its top-16 readout at one or more band layers. **The lie-side set** = the ten lie-side
families without `false` and `falsehood` (lie, fake, deceive, fabricate, conceal, misinformation, mislead, dishonest; lists in `analysis/pilot/lists.json`), pooled. `honest` is
counted on its own. **The pressure set** = conceal, deceive, dishonest, lie, mislead: the families of the lie-side set that are in the
pressured transcripts and much less in the no-pressure truths (the table below). Cells are `carrying / tokens (rate)`.

## 0. Responses left out

A response is left out when its own text contains a lie-side word or an honest word (whole words, on word stems).

| class | transcripts | left out | kept | response tokens kept |
|---|---|---|---|---|
| lies | 152 | 28 | 124 | 21401 |
| truths | 81 | 34 | 47 | 6644 |
| no-pressure truths | 138 | 11 | 127 | 11828 |
| unrelated | 703 | 13 | 690 | 114472 |

Matched words (number of responses): false 34, honest 22, misleading 17, misinformation 15, honesty 10, deception 5, lie 4, honestly 4, lies 4, concealing 3, concealment 3, deceptive 3, conceal 3, dishonest 2, mislead 2, deceiving 2, fabricate 2, fabrication 2, misinformed 1, fabricating 1, deceive 1, dishonesty 1, falsely 1, fabrications 1, falsifying 1, fabricated 1, lying 1.

## 0.1 Why `false` and `falsehood` are not pooled

Kept lies, truths and no-pressure truths together. Cells: tokens carrying the family / tokens of that word (rate).

| response token | tokens | lie | fake | deceive | falsehood | fabricate | conceal | misinformation | false | mislead | dishonest | honest |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| the word No | 86 | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 2 (2.3%) | 0 (0.0%) | 0 (0.0%) | 2 (2.3%) | 19 (22.1%) | 1 (1.2%) | 0 (0.0%) | 1 (1.2%) |
| the word Yes | 68 | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| not, n't | 175 | 1 (0.6%) | 6 (3.4%) | 2 (1.1%) | 9 (5.1%) | 9 (5.1%) | 7 (4.0%) | 15 (8.6%) | 17 (9.7%) | 5 (2.9%) | 2 (1.1%) | 1 (0.6%) |
| never, cannot, none, nor, neither, nothing | 68 | 8 (11.8%) | 7 (10.3%) | 6 (8.8%) | 5 (7.4%) | 7 (10.3%) | 13 (19.1%) | 9 (13.2%) | 5 (7.4%) | 2 (2.9%) | 8 (11.8%) | 5 (7.4%) |
| all tokens | 39873 | 80 (0.2%) | 272 (0.7%) | 109 (0.3%) | 294 (0.7%) | 266 (0.7%) | 207 (0.5%) | 1345 (3.4%) | 520 (1.3%) | 596 (1.5%) | 107 (0.3%) | 1398 (3.5%) |

Kept transcripts with one or more carrying tokens, and the overall rate:

| list | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|
| lie-side set | 91/124 transcripts; 825/21401 (3.9%) of tokens | 34/47 transcripts; 366/6644 (5.5%) of tokens | 66/127 transcripts; 591/11828 (5.0%) of tokens | 156/690 transcripts; 983/114472 (0.9%) of tokens |
| pressure set | 82/124 transcripts; 380/21401 (1.8%) of tokens | 33/47 transcripts; 212/6644 (3.2%) of tokens | 31/127 transcripts; 197/11828 (1.7%) of tokens | 71/690 transcripts; 313/114472 (0.3%) of tokens |
| honest | 86/124 transcripts; 740/21401 (3.5%) of tokens | 36/47 transcripts; 461/6644 (6.9%) of tokens | 35/127 transcripts; 197/11828 (1.7%) of tokens | 59/690 transcripts; 431/114472 (0.4%) of tokens |
| lie | 35/124 transcripts; 52/21401 (0.2%) of tokens | 9/47 transcripts; 18/6644 (0.3%) of tokens | 7/127 transcripts; 10/11828 (0.1%) of tokens | 31/690 transcripts; 41/114472 (0.0%) of tokens |
| fake | 52/124 transcripts; 132/21401 (0.6%) of tokens | 16/47 transcripts; 53/6644 (0.8%) of tokens | 21/127 transcripts; 87/11828 (0.7%) of tokens | 64/690 transcripts; 364/114472 (0.3%) of tokens |
| deceive | 31/124 transcripts; 48/21401 (0.2%) of tokens | 12/47 transcripts; 32/6644 (0.5%) of tokens | 9/127 transcripts; 29/11828 (0.2%) of tokens | 17/690 transcripts; 110/114472 (0.1%) of tokens |
| falsehood | 36/124 transcripts; 144/21401 (0.7%) of tokens | 14/47 transcripts; 45/6644 (0.7%) of tokens | 29/127 transcripts; 105/11828 (0.9%) of tokens | 12/690 transcripts; 61/114472 (0.1%) of tokens |
| fabricate | 23/124 transcripts; 67/21401 (0.3%) of tokens | 8/47 transcripts; 21/6644 (0.3%) of tokens | 21/127 transcripts; 178/11828 (1.5%) of tokens | 53/690 transcripts; 268/114472 (0.2%) of tokens |
| conceal | 61/124 transcripts; 109/21401 (0.5%) of tokens | 20/47 transcripts; 60/6644 (0.9%) of tokens | 9/127 transcripts; 38/11828 (0.3%) of tokens | 8/690 transcripts; 17/114472 (0.0%) of tokens |
| misinformation | 75/124 transcripts; 666/21401 (3.1%) of tokens | 22/47 transcripts; 261/6644 (3.9%) of tokens | 60/127 transcripts; 418/11828 (3.5%) of tokens | 45/690 transcripts; 239/114472 (0.2%) of tokens |
| false | 59/124 transcripts; 280/21401 (1.3%) of tokens | 23/47 transcripts; 78/6644 (1.2%) of tokens | 33/127 transcripts; 162/11828 (1.4%) of tokens | 42/690 transcripts; 191/114472 (0.2%) of tokens |
| mislead | 57/124 transcripts; 278/21401 (1.3%) of tokens | 24/47 transcripts; 157/6644 (2.4%) of tokens | 23/127 transcripts; 161/11828 (1.4%) of tokens | 27/690 transcripts; 143/114472 (0.1%) of tokens |
| dishonest | 26/124 transcripts; 36/21401 (0.2%) of tokens | 10/47 transcripts; 36/6644 (0.5%) of tokens | 9/127 transcripts; 35/11828 (0.3%) of tokens | 9/690 transcripts; 45/114472 (0.0%) of tokens |

## 1. By kind of token

### 1.1 The lie-side set

*rate* = carrying tokens of the kind / tokens of the kind. *times the overall rate* = that rate divided by the class's
overall rate (above 1: the words favour this kind). *per transcript* = among transcripts with one or more carrying
tokens, the kind's share of the carrying tokens minus its share of all tokens, in points, averaged over transcripts,
with a 95% interval from resampling transcripts.

**lies** (124 transcripts, 21401 tokens, 825 carrying, overall rate 3.9%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 106/3845 (2.8%) | 0.72 | 18.0% | 12.8% | -6.4 (-10.0 to -2.3) |
| name | 16/714 (2.2%) | 0.58 | 3.3% | 1.9% | +1.1 (-1.8 to +4.7) |
| verb | 82/2488 (3.3%) | 0.85 | 11.6% | 9.9% | -3.4 (-6.0 to +0.0) |
| auxiliary | 84/1470 (5.7%) | 1.48 | 6.9% | 10.2% | +0.2 (-2.0 to +2.5) |
| adjective | 52/1744 (3.0%) | 0.77 | 8.1% | 6.3% | -3.3 (-4.9 to -1.3) |
| adverb | 34/1033 (3.3%) | 0.85 | 4.8% | 4.1% | -2.6 (-3.5 to -1.6) |
| negation | 22/165 (13.3%) | 3.46 | 0.8% | 2.7% | +1.3 (-1.2 to +4.3) |
| pronoun | 59/2324 (2.5%) | 0.66 | 10.9% | 7.2% | -3.5 (-5.8 to -0.8) |
| determiner | 95/1547 (6.1%) | 1.59 | 7.2% | 11.5% | +7.0 (+2.6 to +11.9) |
| preposition | 79/2453 (3.2%) | 0.84 | 11.5% | 9.6% | +0.4 (-3.1 to +4.9) |
| conjunction | 32/661 (4.8%) | 1.26 | 3.1% | 3.9% | -0.7 (-1.7 to +0.6) |
| number | 18/190 (9.5%) | 2.46 | 0.9% | 2.2% | +1.9 (+0.1 to +4.4) |
| other word | 3/141 (2.1%) | 0.55 | 0.7% | 0.4% | -0.5 (-0.7 to -0.3) |
| sentence end | 68/1028 (6.6%) | 1.72 | 4.8% | 8.2% | +2.6 (-0.5 to +6.4) |
| comma | 41/750 (5.5%) | 1.42 | 3.5% | 5.0% | +5.0 (+1.4 to +9.0) |
| colon or semicolon | 4/71 (5.6%) | 1.46 | 0.3% | 0.5% | +0.5 (-0.3 to +1.9) |
| quote or bracket | 6/77 (7.8%) | 2.02 | 0.4% | 0.7% | +1.8 (-0.2 to +4.8) |
| dash | 1/33 (3.0%) | 0.79 | 0.2% | 0.1% | -0.1 (-0.2 to +0.0) |
| markdown mark | 5/133 (3.8%) | 0.98 | 0.6% | 0.6% | -0.1 (-0.4 to +0.1) |
| other mark | 3/102 (2.9%) | 0.76 | 0.5% | 0.4% | +0.0 (-0.6 to +0.8) |
| line break | 12/378 (3.2%) | 0.82 | 1.8% | 1.5% | -1.1 (-1.5 to -0.7) |
| space | 3/54 (5.6%) | 1.44 | 0.3% | 0.4% | -0.1 (-0.3 to -0.0) |

**truths** (47 transcripts, 6644 tokens, 366 carrying, overall rate 5.5%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 61/1230 (5.0%) | 0.90 | 18.5% | 16.7% | -8.5 (-12.7 to -3.4) |
| name | 6/276 (2.2%) | 0.39 | 4.2% | 1.6% | -2.1 (-4.3 to +0.4) |
| verb | 39/736 (5.3%) | 0.96 | 11.1% | 10.7% | -5.9 (-8.4 to -3.7) |
| auxiliary | 29/411 (7.1%) | 1.28 | 6.2% | 7.9% | -1.0 (-3.4 to +1.6) |
| adjective | 18/514 (3.5%) | 0.64 | 7.7% | 4.9% | +0.1 (-5.2 to +7.4) |
| adverb | 18/276 (6.5%) | 1.18 | 4.2% | 4.9% | +1.1 (-1.8 to +4.9) |
| negation | 14/72 (19.4%) | 3.53 | 1.1% | 3.8% | +8.3 (+1.4 to +17.5) |
| pronoun | 18/632 (2.8%) | 0.52 | 9.5% | 4.9% | -5.1 (-7.1 to -2.6) |
| determiner | 40/491 (8.1%) | 1.48 | 7.4% | 10.9% | +2.8 (-1.8 to +9.4) |
| preposition | 49/740 (6.6%) | 1.20 | 11.1% | 13.4% | +4.4 (-2.3 to +13.0) |
| conjunction | 18/202 (8.9%) | 1.62 | 3.0% | 4.9% | +1.3 (-1.1 to +4.4) |
| number | 6/139 (4.3%) | 0.78 | 2.1% | 1.6% | +1.3 (-2.4 to +7.8) |
| other word | 0/42 (0.0%) | 0.00 | 0.6% | 0.0% | -0.7 (-1.1 to -0.4) |
| sentence end | 19/317 (6.0%) | 1.09 | 4.8% | 5.2% | +0.9 (-2.4 to +5.0) |
| comma | 14/261 (5.4%) | 0.97 | 3.9% | 3.8% | -0.0 (-2.1 to +2.3) |
| colon or semicolon | 1/37 (2.7%) | 0.49 | 0.6% | 0.3% | -0.4 (-0.7 to -0.2) |
| quote or bracket | 5/25 (20.0%) | 3.63 | 0.4% | 1.4% | +3.2 (-0.2 to +9.4) |
| dash | 1/11 (9.1%) | 1.65 | 0.2% | 0.3% | +0.1 (-0.2 to +0.4) |
| markdown mark | 3/41 (7.3%) | 1.33 | 0.6% | 0.8% | +0.7 (-0.4 to +2.5) |
| other mark | 0/26 (0.0%) | 0.00 | 0.4% | 0.0% | -0.2 (-0.5 to -0.0) |
| line break | 4/130 (3.1%) | 0.56 | 2.0% | 1.1% | -0.6 (-2.2 to +1.6) |
| space | 3/35 (8.6%) | 1.56 | 0.5% | 0.8% | +0.3 (-0.6 to +2.0) |

**no-pressure truths** (127 transcripts, 11828 tokens, 591 carrying, overall rate 5.0%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 81/2309 (3.5%) | 0.70 | 19.5% | 13.7% | -11.8 (-15.7 to -7.3) |
| name | 17/516 (3.3%) | 0.66 | 4.4% | 2.9% | -0.9 (-3.2 to +2.4) |
| verb | 62/1206 (5.1%) | 1.03 | 10.2% | 10.5% | +1.4 (-3.1 to +6.7) |
| auxiliary | 50/743 (6.7%) | 1.35 | 6.3% | 8.5% | +1.7 (-2.1 to +7.0) |
| adjective | 36/905 (4.0%) | 0.80 | 7.7% | 6.1% | -3.2 (-5.1 to -1.1) |
| adverb | 19/419 (4.5%) | 0.91 | 3.5% | 3.2% | -1.1 (-2.6 to +1.0) |
| negation | 11/140 (7.9%) | 1.57 | 1.2% | 1.9% | +0.7 (-0.8 to +2.6) |
| pronoun | 39/857 (4.6%) | 0.91 | 7.2% | 6.6% | -3.4 (-5.0 to -1.6) |
| determiner | 96/971 (9.9%) | 1.98 | 8.2% | 16.2% | +23.1 (+15.5 to +30.8) |
| preposition | 67/1318 (5.1%) | 1.02 | 11.1% | 11.3% | -1.9 (-5.2 to +2.2) |
| conjunction | 19/320 (5.9%) | 1.19 | 2.7% | 3.2% | -1.1 (-1.8 to -0.3) |
| number | 8/180 (4.4%) | 0.89 | 1.5% | 1.4% | +1.5 (-0.6 to +4.9) |
| other word | 4/115 (3.5%) | 0.70 | 1.0% | 0.7% | +1.3 (-1.3 to +4.9) |
| sentence end | 18/614 (2.9%) | 0.59 | 5.2% | 3.0% | -4.1 (-5.1 to -2.9) |
| comma | 24/398 (6.0%) | 1.21 | 3.4% | 4.1% | -0.1 (-2.1 to +2.4) |
| colon or semicolon | 2/77 (2.6%) | 0.52 | 0.7% | 0.3% | -0.3 (-0.5 to -0.2) |
| quote or bracket | 11/79 (13.9%) | 2.79 | 0.7% | 1.9% | +0.1 (-0.4 to +1.2) |
| dash | 3/28 (10.7%) | 2.14 | 0.2% | 0.5% | -0.1 (-0.2 to -0.0) |
| markdown mark | 15/286 (5.2%) | 1.05 | 2.4% | 2.5% | -0.7 (-1.7 to +0.7) |
| other mark | 0/19 (0.0%) | 0.00 | 0.2% | 0.0% | -0.2 (-0.3 to -0.1) |
| line break | 6/268 (2.2%) | 0.45 | 2.3% | 1.0% | -1.2 (-1.8 to -0.3) |
| space | 3/60 (5.0%) | 1.00 | 0.5% | 0.5% | +0.1 (-0.3 to +0.7) |

### 1.2 The pressure set (conceal, deceive, dishonest, lie, mislead)

*rate* = carrying tokens of the kind / tokens of the kind. *times the overall rate* = that rate divided by the class's
overall rate (above 1: the words favour this kind). *per transcript* = among transcripts with one or more carrying
tokens, the kind's share of the carrying tokens minus its share of all tokens, in points, averaged over transcripts,
with a 95% interval from resampling transcripts.

**lies** (124 transcripts, 21401 tokens, 380 carrying, overall rate 1.8%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 54/3845 (1.4%) | 0.79 | 18.0% | 14.2% | -6.1 (-10.6 to -1.3) |
| name | 8/714 (1.1%) | 0.63 | 3.3% | 2.1% | +0.7 (-2.5 to +4.7) |
| verb | 35/2488 (1.4%) | 0.79 | 11.6% | 9.2% | -5.9 (-8.3 to -3.2) |
| auxiliary | 51/1470 (3.5%) | 1.95 | 6.9% | 13.4% | +1.9 (-1.3 to +5.4) |
| adjective | 22/1744 (1.3%) | 0.71 | 8.1% | 5.8% | -3.5 (-5.6 to -1.0) |
| adverb | 20/1033 (1.9%) | 1.09 | 4.8% | 5.3% | -2.2 (-3.6 to -0.3) |
| negation | 9/165 (5.5%) | 3.07 | 0.8% | 2.4% | +3.3 (+0.1 to +7.4) |
| pronoun | 17/2324 (0.7%) | 0.41 | 10.9% | 4.5% | -3.6 (-7.4 to +1.3) |
| determiner | 49/1547 (3.2%) | 1.78 | 7.2% | 12.9% | +9.8 (+4.5 to +16.1) |
| preposition | 38/2453 (1.5%) | 0.87 | 11.5% | 10.0% | +2.2 (-2.7 to +7.6) |
| conjunction | 17/661 (2.6%) | 1.45 | 3.1% | 4.5% | -0.6 (-2.0 to +1.2) |
| number | 11/190 (5.8%) | 3.26 | 0.9% | 2.9% | +0.8 (-0.7 to +2.6) |
| other word | 2/141 (1.4%) | 0.80 | 0.7% | 0.5% | -0.5 (-0.8 to -0.2) |
| sentence end | 10/1028 (1.0%) | 0.55 | 4.8% | 2.6% | -2.1 (-4.3 to +0.9) |
| comma | 25/750 (3.3%) | 1.88 | 3.5% | 6.6% | +6.3 (+1.8 to +12.0) |
| colon or semicolon | 1/71 (1.4%) | 0.79 | 0.3% | 0.3% | -0.1 (-0.4 to +0.3) |
| quote or bracket | 4/77 (5.2%) | 2.93 | 0.4% | 1.1% | +1.7 (-0.3 to +4.6) |
| dash | 0/33 (0.0%) | 0.00 | 0.2% | 0.0% | -0.1 (-0.2 to -0.1) |
| markdown mark | 1/133 (0.8%) | 0.42 | 0.6% | 0.3% | -0.2 (-0.5 to +0.2) |
| other mark | 3/102 (2.9%) | 1.66 | 0.5% | 0.8% | +0.1 (-0.5 to +1.0) |
| line break | 2/378 (0.5%) | 0.30 | 1.8% | 0.5% | -1.5 (-1.8 to -1.2) |
| space | 1/54 (1.9%) | 1.04 | 0.3% | 0.3% | -0.1 (-0.4 to +0.2) |

**truths** (47 transcripts, 6644 tokens, 212 carrying, overall rate 3.2%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 38/1230 (3.1%) | 0.97 | 18.5% | 17.9% | -7.8 (-12.6 to -2.0) |
| name | 6/276 (2.2%) | 0.68 | 4.2% | 2.8% | -1.7 (-4.1 to +0.7) |
| verb | 16/736 (2.2%) | 0.68 | 11.1% | 7.5% | -8.5 (-10.7 to -5.9) |
| auxiliary | 18/411 (4.4%) | 1.37 | 6.2% | 8.5% | -0.8 (-3.8 to +2.6) |
| adjective | 7/514 (1.4%) | 0.43 | 7.7% | 3.3% | -0.7 (-6.3 to +7.4) |
| adverb | 10/276 (3.6%) | 1.14 | 4.2% | 4.7% | +0.3 (-2.7 to +4.1) |
| negation | 13/72 (18.1%) | 5.66 | 1.1% | 6.1% | +12.1 (+2.9 to +22.3) |
| pronoun | 11/632 (1.7%) | 0.55 | 9.5% | 5.2% | -3.5 (-6.7 to +0.2) |
| determiner | 29/491 (5.9%) | 1.85 | 7.4% | 13.7% | +5.3 (-1.6 to +13.5) |
| preposition | 25/740 (3.4%) | 1.06 | 11.1% | 11.8% | +4.5 (-3.1 to +13.7) |
| conjunction | 7/202 (3.5%) | 1.09 | 3.0% | 3.3% | +0.1 (-2.3 to +3.5) |
| number | 6/139 (4.3%) | 1.35 | 2.1% | 2.8% | +1.8 (-2.3 to +8.4) |
| other word | 0/42 (0.0%) | 0.00 | 0.6% | 0.0% | -0.7 (-1.0 to -0.4) |
| sentence end | 8/317 (2.5%) | 0.79 | 4.8% | 3.8% | -2.1 (-4.4 to +0.6) |
| comma | 9/261 (3.4%) | 1.08 | 3.9% | 4.2% | +0.2 (-2.3 to +3.0) |
| colon or semicolon | 0/37 (0.0%) | 0.00 | 0.6% | 0.0% | -0.4 (-0.7 to -0.2) |
| quote or bracket | 4/25 (16.0%) | 5.01 | 0.4% | 1.9% | +0.6 (-0.2 to +1.8) |
| dash | 1/11 (9.1%) | 2.85 | 0.2% | 0.5% | +0.1 (-0.2 to +0.5) |
| markdown mark | 0/41 (0.0%) | 0.00 | 0.6% | 0.0% | -0.5 (-1.0 to -0.2) |
| other mark | 0/26 (0.0%) | 0.00 | 0.4% | 0.0% | -0.3 (-0.5 to -0.0) |
| line break | 2/130 (1.5%) | 0.48 | 2.0% | 0.9% | +1.5 (-2.1 to +8.0) |
| space | 2/35 (5.7%) | 1.79 | 0.5% | 0.9% | +0.4 (-0.7 to +2.3) |

**no-pressure truths** (127 transcripts, 11828 tokens, 197 carrying, overall rate 1.7%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 38/2309 (1.6%) | 0.99 | 19.5% | 19.3% | +5.0 (-7.0 to +19.0) |
| name | 8/516 (1.6%) | 0.93 | 4.4% | 4.1% | +1.0 (-3.3 to +7.5) |
| verb | 25/1206 (2.1%) | 1.24 | 10.2% | 12.7% | +0.3 (-4.8 to +6.4) |
| auxiliary | 20/743 (2.7%) | 1.62 | 6.3% | 10.2% | +2.2 (-3.7 to +9.9) |
| adjective | 8/905 (0.9%) | 0.53 | 7.7% | 4.1% | -5.7 (-8.3 to -2.4) |
| adverb | 8/419 (1.9%) | 1.15 | 3.5% | 4.1% | -0.8 (-2.4 to +1.1) |
| negation | 6/140 (4.3%) | 2.57 | 1.2% | 3.0% | +4.1 (-0.6 to +10.9) |
| pronoun | 14/857 (1.6%) | 0.98 | 7.2% | 7.1% | -2.7 (-6.0 to +1.5) |
| determiner | 19/971 (2.0%) | 1.17 | 8.2% | 9.6% | -2.2 (-5.5 to +1.4) |
| preposition | 19/1318 (1.4%) | 0.87 | 11.1% | 9.6% | -2.6 (-8.0 to +4.5) |
| conjunction | 4/320 (1.2%) | 0.75 | 2.7% | 2.0% | -2.2 (-2.9 to -1.5) |
| number | 4/180 (2.2%) | 1.33 | 1.5% | 2.0% | +1.4 (-0.6 to +4.7) |
| other word | 1/115 (0.9%) | 0.52 | 1.0% | 0.5% | +1.7 (-1.8 to +8.0) |
| sentence end | 4/614 (0.7%) | 0.39 | 5.2% | 2.0% | -3.9 (-5.3 to -2.2) |
| comma | 7/398 (1.8%) | 1.06 | 3.4% | 3.6% | +3.7 (-3.1 to +13.5) |
| colon or semicolon | 0/77 (0.0%) | 0.00 | 0.7% | 0.0% | -0.5 (-0.7 to -0.3) |
| quote or bracket | 4/79 (5.1%) | 3.04 | 0.7% | 2.0% | +1.1 (-0.6 to +4.0) |
| dash | 1/28 (3.6%) | 2.14 | 0.2% | 0.5% | +0.2 (-0.2 to +0.8) |
| markdown mark | 6/286 (2.1%) | 1.26 | 2.4% | 3.0% | +2.2 (-1.6 to +8.8) |
| other mark | 0/19 (0.0%) | 0.00 | 0.2% | 0.0% | -0.1 (-0.3 to -0.0) |
| line break | 1/268 (0.4%) | 0.22 | 2.3% | 0.5% | -1.5 (-2.1 to -0.7) |
| space | 0/60 (0.0%) | 0.00 | 0.5% | 0.0% | -0.3 (-0.5 to -0.1) |

### 1.3 `honest`

*rate* = carrying tokens of the kind / tokens of the kind. *times the overall rate* = that rate divided by the class's
overall rate (above 1: the words favour this kind). *per transcript* = among transcripts with one or more carrying
tokens, the kind's share of the carrying tokens minus its share of all tokens, in points, averaged over transcripts,
with a 95% interval from resampling transcripts.

**lies** (124 transcripts, 21401 tokens, 740 carrying, overall rate 3.5%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 58/3845 (1.5%) | 0.44 | 18.0% | 7.8% | -10.6 (-12.7 to -8.3) |
| name | 9/714 (1.3%) | 0.36 | 3.3% | 1.2% | -1.7 (-2.6 to -0.7) |
| verb | 65/2488 (2.6%) | 0.76 | 11.6% | 8.8% | -3.7 (-6.3 to -0.7) |
| auxiliary | 38/1470 (2.6%) | 0.75 | 6.9% | 5.1% | -1.6 (-4.0 to +1.6) |
| adjective | 22/1744 (1.3%) | 0.36 | 8.1% | 3.0% | -6.6 (-7.6 to -5.5) |
| adverb | 29/1033 (2.8%) | 0.81 | 4.8% | 3.9% | +0.7 (-2.1 to +4.5) |
| negation | 4/165 (2.4%) | 0.70 | 0.8% | 0.5% | +0.3 (-0.8 to +2.0) |
| pronoun | 151/2324 (6.5%) | 1.88 | 10.9% | 20.4% | +14.8 (+9.7 to +20.5) |
| determiner | 17/1547 (1.1%) | 0.32 | 7.2% | 2.3% | -3.9 (-6.0 to -0.8) |
| preposition | 64/2453 (2.6%) | 0.75 | 11.5% | 8.6% | -5.6 (-7.6 to -3.3) |
| conjunction | 57/661 (8.6%) | 2.49 | 3.1% | 7.7% | +3.5 (+1.6 to +5.7) |
| number | 4/190 (2.1%) | 0.61 | 0.9% | 0.5% | -0.5 (-0.9 to -0.1) |
| other word | 2/141 (1.4%) | 0.41 | 0.7% | 0.3% | -0.5 (-0.7 to -0.3) |
| sentence end | 102/1028 (9.9%) | 2.87 | 4.8% | 13.8% | +6.1 (+3.0 to +9.7) |
| comma | 61/750 (8.1%) | 2.35 | 3.5% | 8.2% | +5.8 (+2.9 to +9.4) |
| colon or semicolon | 5/71 (7.0%) | 2.04 | 0.3% | 0.7% | -0.0 (-0.3 to +0.2) |
| quote or bracket | 2/77 (2.6%) | 0.75 | 0.4% | 0.3% | +0.1 (-0.3 to +0.7) |
| dash | 5/33 (15.2%) | 4.38 | 0.2% | 0.7% | +0.3 (-0.1 to +0.8) |
| markdown mark | 3/133 (2.3%) | 0.65 | 0.6% | 0.4% | +0.1 (-0.4 to +0.8) |
| other mark | 1/102 (1.0%) | 0.28 | 0.5% | 0.1% | -0.3 (-0.7 to -0.1) |
| line break | 40/378 (10.6%) | 3.06 | 1.8% | 5.4% | +3.4 (+1.1 to +6.5) |
| space | 1/54 (1.9%) | 0.54 | 0.3% | 0.1% | -0.1 (-0.3 to +0.0) |

**truths** (47 transcripts, 6644 tokens, 461 carrying, overall rate 6.9%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 35/1230 (2.8%) | 0.41 | 18.5% | 7.6% | -11.0 (-13.8 to -7.6) |
| name | 1/276 (0.4%) | 0.05 | 4.2% | 0.2% | -4.1 (-6.4 to -2.2) |
| verb | 44/736 (6.0%) | 0.86 | 11.1% | 9.5% | -1.3 (-6.1 to +5.0) |
| auxiliary | 35/411 (8.5%) | 1.23 | 6.2% | 7.6% | +0.2 (-1.5 to +2.1) |
| adjective | 23/514 (4.5%) | 0.64 | 7.7% | 5.0% | -4.4 (-6.2 to -2.6) |
| adverb | 21/276 (7.6%) | 1.10 | 4.2% | 4.6% | +3.7 (-1.1 to +10.6) |
| negation | 4/72 (5.6%) | 0.80 | 1.1% | 0.9% | -0.8 (-1.8 to +0.2) |
| pronoun | 79/632 (12.5%) | 1.80 | 9.5% | 17.1% | +4.2 (+1.1 to +7.7) |
| determiner | 12/491 (2.4%) | 0.35 | 7.4% | 2.6% | -2.0 (-5.7 to +4.1) |
| preposition | 51/740 (6.9%) | 0.99 | 11.1% | 11.1% | -0.4 (-4.6 to +5.4) |
| conjunction | 27/202 (13.4%) | 1.93 | 3.0% | 5.9% | +4.3 (+0.2 to +10.8) |
| number | 7/139 (5.0%) | 0.73 | 2.1% | 1.5% | +1.4 (-2.0 to +6.4) |
| other word | 4/42 (9.5%) | 1.37 | 0.6% | 0.9% | -2.2 (-5.4 to -0.1) |
| sentence end | 59/317 (18.6%) | 2.68 | 4.8% | 12.8% | +9.6 (+4.2 to +16.1) |
| comma | 37/261 (14.2%) | 2.04 | 3.9% | 8.0% | +3.2 (+0.6 to +6.3) |
| colon or semicolon | 0/37 (0.0%) | 0.00 | 0.6% | 0.0% | -0.3 (-0.6 to -0.2) |
| quote or bracket | 4/25 (16.0%) | 2.31 | 0.4% | 0.9% | +0.2 (-0.1 to +0.7) |
| dash | 0/11 (0.0%) | 0.00 | 0.2% | 0.0% | -0.1 (-0.2 to -0.0) |
| markdown mark | 0/41 (0.0%) | 0.00 | 0.6% | 0.0% | -0.2 (-0.4 to -0.1) |
| other mark | 0/26 (0.0%) | 0.00 | 0.4% | 0.0% | -0.4 (-0.9 to -0.1) |
| line break | 16/130 (12.3%) | 1.77 | 2.0% | 3.5% | +0.2 (-1.0 to +1.4) |
| space | 2/35 (5.7%) | 0.82 | 0.5% | 0.4% | +0.2 (-0.8 to +1.8) |

**no-pressure truths** (127 transcripts, 11828 tokens, 197 carrying, overall rate 1.7%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 19/2309 (0.8%) | 0.49 | 19.5% | 9.6% | -11.5 (-16.9 to -4.2) |
| name | 8/516 (1.6%) | 0.93 | 4.4% | 4.1% | +0.5 (-3.5 to +6.5) |
| verb | 11/1206 (0.9%) | 0.55 | 10.2% | 5.6% | -9.3 (-11.7 to -6.4) |
| auxiliary | 11/743 (1.5%) | 0.89 | 6.3% | 5.6% | +4.2 (-3.3 to +13.5) |
| adjective | 10/905 (1.1%) | 0.66 | 7.7% | 5.1% | -3.7 (-6.1 to -0.6) |
| adverb | 7/419 (1.7%) | 1.00 | 3.5% | 3.6% | -0.1 (-3.1 to +3.7) |
| negation | 0/140 (0.0%) | 0.00 | 1.2% | 0.0% | -1.1 (-1.6 to -0.7) |
| pronoun | 41/857 (4.8%) | 2.87 | 7.2% | 20.8% | +11.8 (+3.8 to +20.7) |
| determiner | 11/971 (1.1%) | 0.68 | 8.2% | 5.6% | +0.1 (-6.6 to +9.0) |
| preposition | 19/1318 (1.4%) | 0.87 | 11.1% | 9.6% | -6.4 (-9.6 to -2.6) |
| conjunction | 9/320 (2.8%) | 1.69 | 2.7% | 4.6% | -0.3 (-1.7 to +1.6) |
| number | 2/180 (1.1%) | 0.67 | 1.5% | 1.0% | +1.8 (-1.4 to +7.5) |
| other word | 4/115 (3.5%) | 2.09 | 1.0% | 2.0% | -1.2 (-2.0 to -0.3) |
| sentence end | 26/614 (4.2%) | 2.54 | 5.2% | 13.2% | +13.7 (+3.8 to +25.6) |
| comma | 6/398 (1.5%) | 0.91 | 3.4% | 3.0% | +3.7 (-2.7 to +11.9) |
| colon or semicolon | 2/77 (2.6%) | 1.56 | 0.7% | 1.0% | -0.3 (-0.6 to -0.0) |
| quote or bracket | 0/79 (0.0%) | 0.00 | 0.7% | 0.0% | -0.3 (-0.5 to -0.1) |
| dash | 0/28 (0.0%) | 0.00 | 0.2% | 0.0% | -0.1 (-0.3 to -0.0) |
| markdown mark | 6/286 (2.1%) | 1.26 | 2.4% | 3.0% | -0.2 (-1.6 to +1.8) |
| other mark | 0/19 (0.0%) | 0.00 | 0.2% | 0.0% | -0.2 (-0.5 to -0.0) |
| line break | 5/268 (1.9%) | 1.12 | 2.3% | 2.5% | -0.7 (-1.7 to +0.4) |
| space | 0/60 (0.0%) | 0.00 | 0.5% | 0.0% | -0.4 (-0.6 to -0.2) |

### 1.4 The lie-side set, held by eight or more band layers

*rate* = carrying tokens of the kind / tokens of the kind. *times the overall rate* = that rate divided by the class's
overall rate (above 1: the words favour this kind). *per transcript* = among transcripts with one or more carrying
tokens, the kind's share of the carrying tokens minus its share of all tokens, in points, averaged over transcripts,
with a 95% interval from resampling transcripts.

**lies** (124 transcripts, 21401 tokens, 458 carrying, overall rate 2.1%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 54/3845 (1.4%) | 0.66 | 18.0% | 11.8% | -10.2 (-13.9 to -4.9) |
| name | 8/714 (1.1%) | 0.52 | 3.3% | 1.7% | +1.5 (-2.2 to +6.0) |
| verb | 47/2488 (1.9%) | 0.88 | 11.6% | 10.3% | -4.8 (-7.4 to -2.0) |
| auxiliary | 56/1470 (3.8%) | 1.78 | 6.9% | 12.2% | +2.3 (-1.3 to +6.5) |
| adjective | 33/1744 (1.9%) | 0.88 | 8.1% | 7.2% | -1.1 (-4.6 to +3.1) |
| adverb | 22/1033 (2.1%) | 1.00 | 4.8% | 4.8% | -1.7 (-3.3 to +0.4) |
| negation | 10/165 (6.1%) | 2.83 | 0.8% | 2.2% | +2.3 (-0.5 to +6.1) |
| pronoun | 30/2324 (1.3%) | 0.60 | 10.9% | 6.6% | -5.6 (-7.9 to -2.9) |
| determiner | 62/1547 (4.0%) | 1.87 | 7.2% | 13.5% | +10.5 (+4.5 to +17.4) |
| preposition | 47/2453 (1.9%) | 0.90 | 11.5% | 10.3% | +6.1 (-0.8 to +12.9) |
| conjunction | 21/661 (3.2%) | 1.48 | 3.1% | 4.6% | -1.1 (-2.2 to +0.1) |
| number | 13/190 (6.8%) | 3.20 | 0.9% | 2.8% | +3.5 (-0.0 to +8.3) |
| other word | 0/141 (0.0%) | 0.00 | 0.7% | 0.0% | -0.6 (-0.8 to -0.5) |
| sentence end | 24/1028 (2.3%) | 1.09 | 4.8% | 5.2% | -0.7 (-3.4 to +3.2) |
| comma | 20/750 (2.7%) | 1.25 | 3.5% | 4.4% | +1.5 (-1.4 to +4.7) |
| colon or semicolon | 1/71 (1.4%) | 0.66 | 0.3% | 0.2% | -0.2 (-0.4 to +0.0) |
| quote or bracket | 1/77 (1.3%) | 0.61 | 0.4% | 0.2% | -0.2 (-0.3 to +0.0) |
| dash | 0/33 (0.0%) | 0.00 | 0.2% | 0.0% | -0.1 (-0.2 to -0.1) |
| markdown mark | 1/133 (0.8%) | 0.35 | 0.6% | 0.2% | -0.4 (-0.7 to -0.2) |
| other mark | 3/102 (2.9%) | 1.37 | 0.5% | 0.7% | +0.6 (-0.5 to +2.4) |
| line break | 4/378 (1.1%) | 0.49 | 1.8% | 0.9% | -1.3 (-1.6 to -0.9) |
| space | 1/54 (1.9%) | 0.87 | 0.3% | 0.2% | -0.2 (-0.4 to -0.1) |

**truths** (47 transcripts, 6644 tokens, 184 carrying, overall rate 2.8%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 38/1230 (3.1%) | 1.12 | 18.5% | 20.7% | -5.1 (-11.1 to +1.5) |
| name | 5/276 (1.8%) | 0.65 | 4.2% | 2.7% | +5.4 (-2.2 to +15.7) |
| verb | 25/736 (3.4%) | 1.23 | 11.1% | 13.6% | -4.3 (-8.0 to -0.5) |
| auxiliary | 17/411 (4.1%) | 1.49 | 6.2% | 9.2% | +0.8 (-2.9 to +4.8) |
| adjective | 8/514 (1.6%) | 0.56 | 7.7% | 4.3% | -0.6 (-6.0 to +7.9) |
| adverb | 8/276 (2.9%) | 1.05 | 4.2% | 4.3% | +2.3 (-3.0 to +11.1) |
| negation | 7/72 (9.7%) | 3.51 | 1.1% | 3.8% | +7.5 (-0.4 to +18.1) |
| pronoun | 11/632 (1.7%) | 0.63 | 9.5% | 6.0% | -1.9 (-7.0 to +6.0) |
| determiner | 30/491 (6.1%) | 2.21 | 7.4% | 16.3% | +7.3 (+0.5 to +15.9) |
| preposition | 17/740 (2.3%) | 0.83 | 11.1% | 9.2% | -1.9 (-8.3 to +7.1) |
| conjunction | 6/202 (3.0%) | 1.07 | 3.0% | 3.3% | +0.6 (-2.4 to +5.0) |
| number | 2/139 (1.4%) | 0.52 | 2.1% | 1.1% | -1.3 (-2.2 to -0.5) |
| other word | 0/42 (0.0%) | 0.00 | 0.6% | 0.0% | -0.8 (-1.2 to -0.4) |
| sentence end | 3/317 (0.9%) | 0.34 | 4.8% | 1.6% | -4.4 (-5.4 to -3.3) |
| comma | 2/261 (0.8%) | 0.28 | 3.9% | 1.1% | -2.3 (-3.9 to -0.3) |
| colon or semicolon | 1/37 (2.7%) | 0.98 | 0.6% | 0.5% | -0.4 (-0.7 to -0.0) |
| quote or bracket | 2/25 (8.0%) | 2.89 | 0.4% | 1.1% | +0.9 (-0.4 to +2.8) |
| dash | 0/11 (0.0%) | 0.00 | 0.2% | 0.0% | -0.1 (-0.2 to -0.0) |
| markdown mark | 0/41 (0.0%) | 0.00 | 0.6% | 0.0% | -0.3 (-0.5 to -0.1) |
| other mark | 0/26 (0.0%) | 0.00 | 0.4% | 0.0% | -0.3 (-0.7 to -0.0) |
| line break | 1/130 (0.8%) | 0.28 | 2.0% | 0.5% | -1.8 (-2.7 to -0.9) |
| space | 1/35 (2.9%) | 1.03 | 0.5% | 0.5% | +0.6 (-0.5 to +2.5) |

**no-pressure truths** (127 transcripts, 11828 tokens, 289 carrying, overall rate 2.4%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 39/2309 (1.7%) | 0.69 | 19.5% | 13.5% | -12.4 (-15.6 to -8.5) |
| name | 7/516 (1.4%) | 0.56 | 4.4% | 2.4% | -0.5 (-4.2 to +5.2) |
| verb | 33/1206 (2.7%) | 1.12 | 10.2% | 11.4% | +2.9 (-3.6 to +10.8) |
| auxiliary | 27/743 (3.6%) | 1.49 | 6.3% | 9.3% | +6.4 (-1.1 to +15.4) |
| adjective | 20/905 (2.2%) | 0.90 | 7.7% | 6.9% | -0.4 (-6.2 to +6.9) |
| adverb | 10/419 (2.4%) | 0.98 | 3.5% | 3.5% | +1.1 (-2.5 to +7.5) |
| negation | 7/140 (5.0%) | 2.05 | 1.2% | 2.4% | -0.1 (-1.4 to +1.6) |
| pronoun | 18/857 (2.1%) | 0.86 | 7.2% | 6.2% | -3.5 (-5.1 to -1.8) |
| determiner | 43/971 (4.4%) | 1.81 | 8.2% | 14.9% | +15.6 (+6.1 to +26.1) |
| preposition | 34/1318 (2.6%) | 1.06 | 11.1% | 11.8% | -0.3 (-5.2 to +6.0) |
| conjunction | 11/320 (3.4%) | 1.41 | 2.7% | 3.8% | -1.2 (-2.1 to +0.0) |
| number | 5/180 (2.8%) | 1.14 | 1.5% | 1.7% | +2.6 (-0.9 to +8.2) |
| other word | 0/115 (0.0%) | 0.00 | 1.0% | 0.0% | -1.1 (-1.4 to -0.7) |
| sentence end | 6/614 (1.0%) | 0.40 | 5.2% | 2.1% | -3.8 (-5.3 to -1.7) |
| comma | 11/398 (2.8%) | 1.13 | 3.4% | 3.8% | -1.6 (-3.2 to +0.3) |
| colon or semicolon | 1/77 (1.3%) | 0.53 | 0.7% | 0.3% | -0.4 (-0.6 to -0.2) |
| quote or bracket | 8/79 (10.1%) | 4.14 | 0.7% | 2.8% | +1.0 (-0.4 to +3.4) |
| dash | 3/28 (10.7%) | 4.39 | 0.2% | 1.0% | -0.1 (-0.2 to +0.1) |
| markdown mark | 4/286 (1.4%) | 0.57 | 2.4% | 1.4% | -1.8 (-2.5 to -1.0) |
| other mark | 0/19 (0.0%) | 0.00 | 0.2% | 0.0% | -0.3 (-0.5 to -0.1) |
| line break | 2/268 (0.7%) | 0.31 | 2.3% | 0.7% | -1.8 (-2.2 to -1.5) |
| space | 0/60 (0.0%) | 0.00 | 0.5% | 0.0% | -0.5 (-0.7 to -0.2) |

### 1.5 The pressure set, held by eight or more band layers

*rate* = carrying tokens of the kind / tokens of the kind. *times the overall rate* = that rate divided by the class's
overall rate (above 1: the words favour this kind). *per transcript* = among transcripts with one or more carrying
tokens, the kind's share of the carrying tokens minus its share of all tokens, in points, averaged over transcripts,
with a 95% interval from resampling transcripts.

**lies** (124 transcripts, 21401 tokens, 171 carrying, overall rate 0.8%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 16/3845 (0.4%) | 0.52 | 18.0% | 9.4% | -10.8 (-15.5 to -5.2) |
| name | 6/714 (0.8%) | 1.05 | 3.3% | 3.5% | +2.7 (-2.3 to +8.8) |
| verb | 16/2488 (0.6%) | 0.80 | 11.6% | 9.4% | -5.3 (-8.9 to -0.5) |
| auxiliary | 30/1470 (2.0%) | 2.55 | 6.9% | 17.5% | +5.0 (-0.1 to +11.0) |
| adjective | 13/1744 (0.7%) | 0.93 | 8.1% | 7.6% | -2.4 (-6.2 to +2.3) |
| adverb | 12/1033 (1.2%) | 1.45 | 4.8% | 7.0% | -0.3 (-3.3 to +4.0) |
| negation | 4/165 (2.4%) | 3.03 | 0.8% | 2.3% | +3.2 (-0.8 to +8.6) |
| pronoun | 3/2324 (0.1%) | 0.16 | 10.9% | 1.8% | -8.2 (-10.6 to -4.3) |
| determiner | 24/1547 (1.6%) | 1.94 | 7.2% | 14.0% | +11.0 (+2.8 to +19.7) |
| preposition | 21/2453 (0.9%) | 1.07 | 11.5% | 12.3% | +7.8 (-0.6 to +16.7) |
| conjunction | 9/661 (1.4%) | 1.70 | 3.1% | 5.3% | -0.7 (-2.4 to +1.3) |
| number | 7/190 (3.7%) | 4.61 | 0.9% | 4.1% | +3.9 (-0.4 to +9.8) |
| other word | 0/141 (0.0%) | 0.00 | 0.7% | 0.0% | -0.6 (-0.7 to -0.5) |
| sentence end | 1/1028 (0.1%) | 0.12 | 4.8% | 0.6% | -3.1 (-4.9 to +0.4) |
| comma | 5/750 (0.7%) | 0.83 | 3.5% | 2.9% | -0.5 (-3.3 to +3.9) |
| colon or semicolon | 0/71 (0.0%) | 0.00 | 0.3% | 0.0% | -0.3 (-0.4 to -0.2) |
| quote or bracket | 1/77 (1.3%) | 1.63 | 0.4% | 0.6% | +0.1 (-0.3 to +0.6) |
| dash | 0/33 (0.0%) | 0.00 | 0.2% | 0.0% | -0.1 (-0.2 to -0.1) |
| markdown mark | 0/133 (0.0%) | 0.00 | 0.6% | 0.0% | -0.5 (-0.8 to -0.3) |
| other mark | 3/102 (2.9%) | 3.68 | 0.5% | 1.8% | +1.0 (-0.2 to +3.1) |
| line break | 0/378 (0.0%) | 0.00 | 1.8% | 0.0% | -1.6 (-1.9 to -1.3) |
| space | 0/54 (0.0%) | 0.00 | 0.3% | 0.0% | -0.3 (-0.5 to -0.2) |

**truths** (47 transcripts, 6644 tokens, 103 carrying, overall rate 1.6%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 21/1230 (1.7%) | 1.10 | 18.5% | 20.4% | -5.1 (-12.6 to +3.3) |
| name | 4/276 (1.4%) | 0.93 | 4.2% | 3.9% | +2.3 (-3.3 to +10.0) |
| verb | 10/736 (1.4%) | 0.88 | 11.1% | 9.7% | -7.1 (-10.6 to -3.0) |
| auxiliary | 14/411 (3.4%) | 2.20 | 6.2% | 13.6% | +6.1 (-0.6 to +13.9) |
| adjective | 2/514 (0.4%) | 0.25 | 7.7% | 1.9% | -3.8 (-7.7 to +1.5) |
| adverb | 5/276 (1.8%) | 1.17 | 4.2% | 4.9% | +3.2 (-3.5 to +13.3) |
| negation | 7/72 (9.7%) | 6.27 | 1.1% | 6.8% | +9.4 (+0.1 to +22.3) |
| pronoun | 5/632 (0.8%) | 0.51 | 9.5% | 4.9% | -2.7 (-8.5 to +6.5) |
| determiner | 14/491 (2.9%) | 1.84 | 7.4% | 13.6% | +5.6 (-4.1 to +18.0) |
| preposition | 10/740 (1.4%) | 0.87 | 11.1% | 9.7% | +2.3 (-8.3 to +15.3) |
| conjunction | 2/202 (1.0%) | 0.64 | 3.0% | 1.9% | -2.1 (-3.3 to -0.4) |
| number | 2/139 (1.4%) | 0.93 | 2.1% | 1.9% | -0.7 (-2.0 to +0.9) |
| other word | 0/42 (0.0%) | 0.00 | 0.6% | 0.0% | -0.8 (-1.3 to -0.4) |
| sentence end | 3/317 (0.9%) | 0.61 | 4.8% | 2.9% | -2.1 (-5.2 to +2.8) |
| comma | 2/261 (0.8%) | 0.49 | 3.9% | 1.9% | -2.0 (-3.9 to +0.5) |
| colon or semicolon | 0/37 (0.0%) | 0.00 | 0.6% | 0.0% | -0.5 (-0.8 to -0.2) |
| quote or bracket | 1/25 (4.0%) | 2.58 | 0.4% | 1.0% | +0.1 (-0.6 to +1.4) |
| dash | 0/11 (0.0%) | 0.00 | 0.2% | 0.0% | -0.1 (-0.2 to -0.0) |
| markdown mark | 0/41 (0.0%) | 0.00 | 0.6% | 0.0% | -0.4 (-0.6 to -0.2) |
| other mark | 0/26 (0.0%) | 0.00 | 0.4% | 0.0% | -0.3 (-0.6 to -0.0) |
| line break | 0/130 (0.0%) | 0.00 | 2.0% | 0.0% | -2.1 (-3.0 to -1.3) |
| space | 1/35 (2.9%) | 1.84 | 0.5% | 1.0% | +0.7 (-0.5 to +2.9) |

**no-pressure truths** (127 transcripts, 11828 tokens, 88 carrying, overall rate 0.7%)

| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |
|---|---|---|---|---|---|
| noun | 13/2309 (0.6%) | 0.76 | 19.5% | 14.8% | -8.4 (-18.2 to +5.3) |
| name | 3/516 (0.6%) | 0.78 | 4.4% | 3.4% | +0.2 (-5.7 to +7.8) |
| verb | 11/1206 (0.9%) | 1.23 | 10.2% | 12.5% | +8.0 (-3.4 to +22.6) |
| auxiliary | 11/743 (1.5%) | 1.99 | 6.3% | 12.5% | +1.4 (-4.2 to +7.2) |
| adjective | 5/905 (0.6%) | 0.74 | 7.7% | 5.7% | -2.9 (-7.3 to +3.3) |
| adverb | 5/419 (1.2%) | 1.60 | 3.5% | 5.7% | +1.4 (-2.2 to +5.8) |
| negation | 2/140 (1.4%) | 1.92 | 1.2% | 2.3% | +1.9 (-1.9 to +8.6) |
| pronoun | 7/857 (0.8%) | 1.10 | 7.2% | 8.0% | +0.8 (-4.6 to +7.8) |
| determiner | 8/971 (0.8%) | 1.11 | 8.2% | 9.1% | -0.4 (-5.8 to +6.9) |
| preposition | 11/1318 (0.8%) | 1.12 | 11.1% | 12.5% | +0.2 (-6.1 to +7.4) |
| conjunction | 3/320 (0.9%) | 1.26 | 2.7% | 3.4% | -1.8 (-3.0 to -0.2) |
| number | 2/180 (1.1%) | 1.49 | 1.5% | 2.3% | +5.2 (-1.4 to +17.5) |
| other word | 0/115 (0.0%) | 0.00 | 1.0% | 0.0% | -1.3 (-1.9 to -0.7) |
| sentence end | 0/614 (0.0%) | 0.00 | 5.2% | 0.0% | -5.0 (-5.7 to -4.4) |
| comma | 4/398 (1.0%) | 1.35 | 3.4% | 4.5% | -1.6 (-3.5 to +1.0) |
| colon or semicolon | 0/77 (0.0%) | 0.00 | 0.7% | 0.0% | -0.5 (-0.7 to -0.3) |
| quote or bracket | 2/79 (2.5%) | 3.40 | 0.7% | 2.3% | +2.0 (-1.3 to +7.5) |
| dash | 0/28 (0.0%) | 0.00 | 0.2% | 0.0% | -0.3 (-0.6 to +0.0) |
| markdown mark | 1/286 (0.3%) | 0.47 | 2.4% | 1.1% | +3.7 (-3.4 to +16.7) |
| other mark | 0/19 (0.0%) | 0.00 | 0.2% | 0.0% | -0.2 (-0.5 to +0.0) |
| line break | 0/268 (0.0%) | 0.00 | 2.3% | 0.0% | -1.9 (-2.5 to -1.3) |
| space | 0/60 (0.0%) | 0.00 | 0.5% | 0.0% | -0.6 (-0.9 to -0.3) |

### 1.6 Each family: rate by kind of token (carrying / tokens, in percent), lies and truths

**lies**

| kind of token | tokens | lie | fake | deceive | falsehood | fabricate | conceal | misinformation | false | mislead | dishonest | honest |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| noun | 3845 | 0.2 | 0.3 | 0.1 | 0.4 | 0.2 | 0.1 | 2.1 | 0.8 | 1.1 | 0.1 | 1.5 |
| name | 714 | 0.7 | 1.0 | 0.6 | 0.6 | 0.8 | 0.8 | 1.5 | 1.0 | 0.8 | 0.6 | 1.3 |
| verb | 2488 | 0.0 | 0.4 | 0.2 | 0.6 | 0.0 | 0.2 | 2.8 | 0.7 | 1.2 | 0.1 | 2.6 |
| auxiliary | 1470 | 0.1 | 1.0 | 0.3 | 1.5 | 0.3 | 0.4 | 4.6 | 2.7 | 3.1 | 0.0 | 2.6 |
| adjective | 1744 | 0.0 | 0.6 | 0.0 | 0.8 | 0.2 | 0.2 | 2.6 | 1.3 | 1.1 | 0.0 | 1.3 |
| adverb | 1033 | 0.3 | 0.5 | 0.1 | 1.2 | 0.3 | 0.4 | 2.9 | 1.5 | 1.6 | 0.1 | 2.8 |
| negation | 165 | 3.6 | 3.6 | 1.2 | 6.7 | 4.8 | 4.8 | 8.5 | 12.7 | 0.0 | 3.0 | 2.4 |
| pronoun | 2324 | 0.1 | 0.2 | 0.0 | 0.2 | 0.1 | 0.3 | 2.1 | 0.4 | 0.4 | 0.0 | 6.5 |
| determiner | 1547 | 0.4 | 1.0 | 0.7 | 1.0 | 0.6 | 1.3 | 5.0 | 1.6 | 2.1 | 0.3 | 1.1 |
| preposition | 2453 | 0.2 | 0.4 | 0.2 | 0.4 | 0.2 | 0.8 | 2.6 | 1.1 | 0.9 | 0.2 | 2.6 |
| conjunction | 661 | 0.0 | 0.3 | 0.0 | 0.2 | 0.3 | 0.5 | 3.8 | 1.4 | 2.1 | 0.2 | 8.6 |
| number | 190 | 3.2 | 6.8 | 2.6 | 3.2 | 3.7 | 4.2 | 6.3 | 7.9 | 1.6 | 2.6 | 2.1 |
| other word | 141 | 0.0 | 0.7 | 0.0 | 0.0 | 0.0 | 0.7 | 0.7 | 0.7 | 0.7 | 0.0 | 1.4 |
| sentence end | 1028 | 0.1 | 0.3 | 0.2 | 0.4 | 0.2 | 0.2 | 6.4 | 0.9 | 0.8 | 0.0 | 9.9 |
| comma | 750 | 0.5 | 1.3 | 0.4 | 0.7 | 0.4 | 0.9 | 3.9 | 2.4 | 2.5 | 0.5 | 8.1 |
| colon or semicolon | 71 | 0.0 | 0.0 | 0.0 | 0.0 | 1.4 | 0.0 | 2.8 | 0.0 | 1.4 | 0.0 | 7.0 |
| quote or bracket | 77 | 2.6 | 5.2 | 1.3 | 1.3 | 1.3 | 2.6 | 3.9 | 1.3 | 2.6 | 1.3 | 2.6 |
| dash | 33 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.0 | 0.0 | 0.0 | 0.0 | 15.2 |
| markdown mark | 133 | 0.0 | 0.8 | 0.0 | 1.5 | 0.0 | 0.8 | 3.0 | 3.8 | 0.0 | 0.0 | 2.3 |
| other mark | 102 | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 2.9 | 1.0 | 2.0 | 1.0 | 0.0 | 1.0 |
| line break | 378 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.2 | 0.3 | 0.5 | 0.0 | 10.6 |
| space | 54 | 1.9 | 3.7 | 0.0 | 1.9 | 0.0 | 1.9 | 3.7 | 1.9 | 1.9 | 0.0 | 1.9 |
| all tokens | 21401 | 0.2 | 0.6 | 0.2 | 0.7 | 0.3 | 0.5 | 3.1 | 1.3 | 1.3 | 0.2 | 3.5 |

**truths**

| kind of token | tokens | lie | fake | deceive | falsehood | fabricate | conceal | misinformation | false | mislead | dishonest | honest |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| noun | 1230 | 0.3 | 0.7 | 0.3 | 0.5 | 0.2 | 0.4 | 3.4 | 0.9 | 2.4 | 0.3 | 2.8 |
| name | 276 | 0.7 | 0.7 | 0.0 | 0.7 | 0.4 | 0.7 | 1.1 | 1.1 | 1.4 | 0.0 | 0.4 |
| verb | 736 | 0.1 | 0.7 | 0.3 | 0.8 | 0.1 | 0.5 | 4.8 | 1.2 | 1.8 | 0.5 | 6.0 |
| auxiliary | 411 | 0.0 | 1.0 | 0.2 | 1.0 | 0.5 | 0.7 | 5.4 | 1.5 | 3.9 | 0.7 | 8.5 |
| adjective | 514 | 0.0 | 0.4 | 0.2 | 1.0 | 0.0 | 0.2 | 2.9 | 0.8 | 1.0 | 0.2 | 4.5 |
| adverb | 276 | 0.0 | 0.4 | 0.0 | 0.7 | 0.4 | 0.4 | 3.6 | 0.4 | 3.3 | 0.0 | 7.6 |
| negation | 72 | 4.2 | 5.6 | 6.9 | 1.4 | 5.6 | 11.1 | 6.9 | 13.9 | 6.9 | 5.6 | 5.6 |
| pronoun | 632 | 0.2 | 0.3 | 0.3 | 0.0 | 0.3 | 0.6 | 1.7 | 0.8 | 1.1 | 0.2 | 12.5 |
| determiner | 491 | 0.4 | 1.0 | 1.0 | 1.6 | 0.4 | 1.4 | 6.3 | 1.4 | 5.1 | 0.8 | 2.4 |
| preposition | 740 | 0.4 | 1.1 | 0.7 | 0.9 | 0.4 | 1.2 | 4.9 | 1.1 | 2.2 | 0.9 | 6.9 |
| conjunction | 202 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 7.9 | 0.0 | 2.5 | 0.0 | 13.4 |
| number | 139 | 0.7 | 2.2 | 1.4 | 0.0 | 0.7 | 2.2 | 2.2 | 1.4 | 3.6 | 1.4 | 5.0 |
| other word | 42 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 9.5 |
| sentence end | 317 | 0.0 | 1.3 | 0.9 | 0.6 | 0.0 | 1.6 | 3.8 | 0.6 | 1.3 | 0.6 | 18.6 |
| comma | 261 | 0.0 | 0.8 | 0.0 | 0.0 | 0.0 | 0.8 | 3.1 | 1.5 | 2.3 | 0.8 | 14.2 |
| colon or semicolon | 37 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.7 | 0.0 | 0.0 | 0.0 | 0.0 |
| quote or bracket | 25 | 0.0 | 0.0 | 4.0 | 4.0 | 4.0 | 8.0 | 12.0 | 12.0 | 16.0 | 0.0 | 16.0 |
| dash | 11 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 9.1 | 0.0 | 0.0 |
| markdown mark | 41 | 0.0 | 2.4 | 0.0 | 0.0 | 0.0 | 0.0 | 4.9 | 4.9 | 0.0 | 0.0 | 0.0 |
| other mark | 26 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| line break | 130 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0 | 0.8 | 0.8 | 12.3 |
| space | 35 | 2.9 | 5.7 | 2.9 | 2.9 | 0.0 | 5.7 | 8.6 | 2.9 | 5.7 | 2.9 | 5.7 |
| all tokens | 6644 | 0.3 | 0.8 | 0.5 | 0.7 | 0.3 | 0.9 | 3.9 | 1.2 | 2.4 | 0.5 | 6.9 |

### 1.7 Pieces of split words, and position in the sentence

| | lies: lie-side set | lies: pressure set | lies: honest | truths: lie-side set | truths: pressure set | truths: honest | no-pressure truths: lie-side set | no-pressure truths: pressure set | no-pressure truths: honest |
|---|---|---|---|---|---|---|---|---|---|
| word tokens: first piece or whole word | 645/18282 (3.5%) | 311/18282 (1.7%) | 512/18282 (2.8%) | 301/5534 (5.4%) | 171/5534 (3.1%) | 338/5534 (6.1%) | 494/9651 (5.1%) | 164/9651 (1.7%) | 149/9651 (1.5%) |
| word tokens: later piece of a split word | 37/493 (7.5%) | 22/493 (4.5%) | 8/493 (1.6%) | 15/227 (6.6%) | 15/227 (6.6%) | 5/227 (2.2%) | 15/348 (4.3%) | 10/348 (2.9%) | 3/348 (0.9%) |
| paragraph start | 19/502 (3.8%) | 3/502 (0.6%) | 56/502 (11.2%) | 9/177 (5.1%) | 5/177 (2.8%) | 27/177 (15.3%) | 29/395 (7.3%) | 5/395 (1.3%) | 26/395 (6.6%) |
| sentence start | 22/619 (3.6%) | 7/619 (1.1%) | 33/619 (5.3%) | 16/165 (9.7%) | 9/165 (5.5%) | 22/165 (13.3%) | 11/215 (5.1%) | 4/215 (1.9%) | 5/215 (2.3%) |
| last word of a sentence | 29/1079 (2.7%) | 14/1079 (1.3%) | 23/1079 (2.1%) | 14/324 (4.3%) | 12/324 (3.7%) | 12/324 (3.7%) | 16/581 (2.8%) | 9/581 (1.5%) | 4/581 (0.7%) |
| elsewhere | 755/19201 (3.9%) | 356/19201 (1.9%) | 628/19201 (3.3%) | 327/5978 (5.5%) | 186/5978 (3.1%) | 400/5978 (6.7%) | 535/10637 (5.0%) | 179/10637 (1.7%) | 162/10637 (1.5%) |
| the last response token | 3/124 (2.4%) | 1/124 (0.8%) | 2/124 (1.6%) | 2/47 (4.3%) | 1/47 (2.1%) | 6/47 (12.8%) | 2/127 (1.6%) | 1/127 (0.8%) | 6/127 (4.7%) |

## 2. Lies: before, at and after the deception sentence

The deception sentence is the judge's quote widened to the full sentences that contain it. 124 kept lies have one (0 without a located quote).

Which parts a lie has (a part needs 5 tokens or more): before + at + after: 94; at + after: 17; none: 9; at: 2; after: 2.

### 2.1 The lie-side set

Pooled counts:

| place | lies with the part | carrying / tokens (rate) | mean of the per-lie rates |
|---|---|---|---|
| before | 94 | 341/5299 (6.4%) | 6.0% |
| at | 113 | 134/2624 (5.1%) | 6.0% |
| after | 113 | 347/13458 (2.6%) | 2.8% |

Within the same lie (only lies that have both parts):

| comparison | lies | mean difference of the rates, points (95% interval) | higher / equal / lower |
|---|---|---|---|
| at minus before | 94 | -1.8 (-3.9 to +0.2) | 19 / 29 / 46 |
| after minus at | 111 | -3.3 (-5.5 to -1.3) | 38 / 37 / 36 |
| after minus before | 94 | -3.6 (-5.4 to -2.0) | 21 / 20 / 53 |

By distance in tokens from the deception sentence:

| distance | lies reaching it | carrying / tokens (rate) |
|---|---|---|
| -30 to -26 before its start | 77 | 26/380 (6.8%) |
| -25 to -21 before its start | 82 | 16/400 (4.0%) |
| -20 to -16 before its start | 85 | 37/421 (8.8%) |
| -15 to -11 before its start | 86 | 23/426 (5.4%) |
| -10 to -6 before its start | 94 | 22/461 (4.8%) |
| -5 to -1 before its start | 95 | 31/474 (6.5%) |
| inside the deception sentence | 124 | 137/2640 (5.2%) |
| +1 to +5 after its end | 113 | 25/565 (4.4%) |
| +6 to +10 after its end | 113 | 22/561 (3.9%) |
| +11 to +15 after its end | 112 | 19/558 (3.4%) |
| +16 to +20 after its end | 110 | 5/529 (0.9%) |
| +21 to +25 after its end | 104 | 12/516 (2.3%) |
| +26 to +30 after its end | 102 | 13/501 (2.6%) |
| +31 to +60 after its end | 99 | 63/2741 (2.3%) |
| +61 to the end after its end | 84 | 188/7487 (2.5%) |

### 2.2 The pressure set

Pooled counts:

| place | lies with the part | carrying / tokens (rate) | mean of the per-lie rates |
|---|---|---|---|
| before | 94 | 153/5299 (2.9%) | 2.4% |
| at | 113 | 60/2624 (2.3%) | 2.4% |
| after | 113 | 167/13458 (1.2%) | 1.1% |

Within the same lie (only lies that have both parts):

| comparison | lies | mean difference of the rates, points (95% interval) | higher / equal / lower |
|---|---|---|---|
| at minus before | 94 | -0.5 (-1.6 to +0.6) | 16 / 38 / 40 |
| after minus at | 111 | -1.1 (-2.3 to -0.0) | 42 / 45 / 24 |
| after minus before | 94 | -1.5 (-2.3 to -0.8) | 21 / 28 / 45 |

By distance in tokens from the deception sentence:

| distance | lies reaching it | carrying / tokens (rate) |
|---|---|---|
| -30 to -26 before its start | 77 | 14/380 (3.7%) |
| -25 to -21 before its start | 82 | 4/400 (1.0%) |
| -20 to -16 before its start | 85 | 20/421 (4.8%) |
| -15 to -11 before its start | 86 | 9/426 (2.1%) |
| -10 to -6 before its start | 94 | 10/461 (2.2%) |
| -5 to -1 before its start | 95 | 7/474 (1.5%) |
| inside the deception sentence | 124 | 60/2640 (2.3%) |
| +1 to +5 after its end | 113 | 18/565 (3.2%) |
| +6 to +10 after its end | 113 | 9/561 (1.6%) |
| +11 to +15 after its end | 112 | 4/558 (0.7%) |
| +16 to +20 after its end | 110 | 1/529 (0.2%) |
| +21 to +25 after its end | 104 | 6/516 (1.2%) |
| +26 to +30 after its end | 102 | 6/501 (1.2%) |
| +31 to +60 after its end | 99 | 22/2741 (0.8%) |
| +61 to the end after its end | 84 | 101/7487 (1.3%) |

### 2.3 `honest`

Pooled counts:

| place | lies with the part | carrying / tokens (rate) | mean of the per-lie rates |
|---|---|---|---|
| before | 94 | 391/5299 (7.4%) | 8.1% |
| at | 113 | 83/2624 (3.2%) | 4.1% |
| after | 113 | 266/13458 (2.0%) | 1.9% |

Within the same lie (only lies that have both parts):

| comparison | lies | mean difference of the rates, points (95% interval) | higher / equal / lower |
|---|---|---|---|
| at minus before | 94 | -4.6 (-6.9 to -2.4) | 13 / 22 / 59 |
| after minus at | 111 | -2.3 (-4.1 to -0.7) | 34 / 49 / 28 |
| after minus before | 94 | -6.3 (-8.3 to -4.4) | 10 / 20 / 64 |

By distance in tokens from the deception sentence:

| distance | lies reaching it | carrying / tokens (rate) |
|---|---|---|
| -30 to -26 before its start | 77 | 26/380 (6.8%) |
| -25 to -21 before its start | 82 | 26/400 (6.5%) |
| -20 to -16 before its start | 85 | 28/421 (6.7%) |
| -15 to -11 before its start | 86 | 38/426 (8.9%) |
| -10 to -6 before its start | 94 | 32/461 (6.9%) |
| -5 to -1 before its start | 95 | 39/474 (8.2%) |
| inside the deception sentence | 124 | 83/2640 (3.1%) |
| +1 to +5 after its end | 113 | 17/565 (3.0%) |
| +6 to +10 after its end | 113 | 8/561 (1.4%) |
| +11 to +15 after its end | 112 | 13/558 (2.3%) |
| +16 to +20 after its end | 110 | 8/529 (1.5%) |
| +21 to +25 after its end | 104 | 20/516 (3.9%) |
| +26 to +30 after its end | 102 | 8/501 (1.6%) |
| +31 to +60 after its end | 99 | 40/2741 (1.5%) |
| +61 to the end after its end | 84 | 152/7487 (2.0%) |

## 3. By tenths of the response (no quote needed; responses of 20 tokens or more)

| tenth | lies: lie-side set | lies: pressure set | lies: honest | truths: lie-side set | truths: pressure set | truths: honest | no-pressure truths: lie-side set | no-pressure truths: pressure set | no-pressure truths: honest |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 155/2189 (7.1%) | 70/2189 (3.2%) | 210/2189 (9.6%) | 73/678 (10.8%) | 28/678 (4.1%) | 126/678 (18.6%) | 136/1185 (11.5%) | 35/1185 (3.0%) | 55/1185 (4.6%) |
| 2 | 136/2127 (6.4%) | 56/2127 (2.6%) | 161/2127 (7.6%) | 51/658 (7.8%) | 24/658 (3.6%) | 75/658 (11.4%) | 91/1143 (8.0%) | 22/1143 (1.9%) | 32/1143 (2.8%) |
| 3 | 97/2149 (4.5%) | 35/2149 (1.6%) | 105/2149 (4.9%) | 74/662 (11.2%) | 45/662 (6.8%) | 52/662 (7.9%) | 71/1148 (6.2%) | 38/1148 (3.3%) | 10/1148 (0.9%) |
| 4 | 89/2132 (4.2%) | 43/2132 (2.0%) | 41/2132 (1.9%) | 48/657 (7.3%) | 27/657 (4.1%) | 47/657 (7.2%) | 88/1151 (7.6%) | 32/1151 (2.8%) | 3/1151 (0.3%) |
| 5 | 65/2120 (3.1%) | 35/2120 (1.7%) | 20/2120 (0.9%) | 37/658 (5.6%) | 33/658 (5.0%) | 25/658 (3.8%) | 46/1121 (4.1%) | 11/1121 (1.0%) | 6/1121 (0.5%) |
| 6 | 79/2151 (3.7%) | 40/2151 (1.9%) | 49/2151 (2.3%) | 29/667 (4.3%) | 22/667 (3.3%) | 29/667 (4.3%) | 32/1159 (2.8%) | 17/1159 (1.5%) | 15/1159 (1.3%) |
| 7 | 49/2147 (2.3%) | 30/2147 (1.4%) | 36/2147 (1.7%) | 10/665 (1.5%) | 6/665 (0.9%) | 28/665 (4.2%) | 33/1155 (2.9%) | 17/1155 (1.5%) | 10/1155 (0.9%) |
| 8 | 43/2134 (2.0%) | 12/2134 (0.6%) | 33/2134 (1.5%) | 19/654 (2.9%) | 12/654 (1.8%) | 20/654 (3.1%) | 28/1144 (2.4%) | 14/1144 (1.2%) | 18/1144 (1.6%) |
| 9 | 67/2142 (3.1%) | 34/2142 (1.6%) | 51/2142 (2.4%) | 14/666 (2.1%) | 9/666 (1.4%) | 27/666 (4.1%) | 25/1147 (2.2%) | 4/1147 (0.3%) | 20/1147 (1.7%) |
| 10 | 41/2088 (2.0%) | 23/2088 (1.1%) | 34/2088 (1.6%) | 10/642 (1.6%) | 5/642 (0.8%) | 26/642 (4.0%) | 30/1101 (2.7%) | 5/1101 (0.5%) | 24/1101 (2.2%) |

## 4. Lies: kind of token crossed with place

**The lie-side set**

| kind of token | before | at | after |
|---|---|---|---|
| content words (noun, name, verb, adjective, adverb) | 129/2443 (5.3%) | 38/1239 (3.1%) | 123/6142 (2.0%) |
| function words (auxiliary, pronoun, determiner, preposition, conjunction, negation, number, other) | 156/2135 (7.3%) | 68/1120 (6.1%) | 168/5696 (2.9%) |
| sentence end | 26/294 (8.8%) | 17/123 (13.8%) | 25/611 (4.1%) |
| comma | 16/200 (8.0%) | 12/89 (13.5%) | 13/461 (2.8%) |
| other marks, line breaks, spaces | 14/231 (6.1%) | 2/69 (2.9%) | 18/548 (3.3%) |

**The pressure set**

| kind of token | before | at | after |
|---|---|---|---|
| content words (noun, name, verb, adjective, adverb) | 57/2443 (2.3%) | 22/1239 (1.8%) | 60/6142 (1.0%) |
| function words (auxiliary, pronoun, determiner, preposition, conjunction, negation, number, other) | 77/2135 (3.6%) | 30/1120 (2.7%) | 87/5696 (1.5%) |
| sentence end | 3/294 (1.0%) | 2/123 (1.6%) | 5/611 (0.8%) |
| comma | 11/200 (5.5%) | 6/89 (6.7%) | 8/461 (1.7%) |
| other marks, line breaks, spaces | 5/231 (2.2%) | 0/69 (0.0%) | 7/548 (1.3%) |

