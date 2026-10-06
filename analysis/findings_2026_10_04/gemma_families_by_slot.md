# Gemma's lie-leaning families at each of the five tokens after the response

Written by `scripts/findings_2026_10_04/gemma_families_by_slot.py`. In-sample. One token list per family (the union of its draft lists over the five tokens). Cells: transcripts with the family, with the share of the class in brackets.


## Gemma-3-12B: main text (the family is in 30% or more of the lies; most frequent first)

| family | members (a selection) | position | lies (49) | truths (32) | no-pressure truths (135) | unrelated (179) |
|---|---|---|---|---|---|---|
| hush emoji | 🤫, 🤐 | `<start_of_turn>` | 43 (88%) | 22 (69%) | 24 (18%) | 1 (1%) |
| hush emoji | 🤫, 🤐 | newline | 28 (57%) | 11 (34%) | 1 (1%) | 0 (0%) |
| pretend | ` pretending`, ` pretended`, ` pretends` | `user` | 23 (47%) | 18 (56%) | 21 (16%) | 0 (0%) |
| lie | 謊, মিথ্যা, 谎, 거짓 … (15 tokens) | newline | 20 (41%) | 2 (6%) | 0 (0%) | 0 (0%) |
| obfuscate | ` obfusc` | `<start_of_turn>` | 18 (37%) | 5 (16%) | 1 (1%) | 0 (0%) |
| knowingly | ` knowingly`, ` bewusst` | `<start_of_turn>` | 16 (33%) | 3 (9%) | 6 (4%) | 0 (0%) |
| deliberately | ` knowingly`, 故意, ` intentionally` | `<start_of_turn>` | 15 (31%) | 2 (6%) | 7 (5%) | 1 (1%) |
| obfuscate | ` obfusc` | newline | 15 (31%) | 3 (9%) | 0 (0%) | 0 (0%) |
| reassure | ` reassurance`, ` reassuring`, ` reassured`, ` reassure` | newline | 15 (31%) | 5 (16%) | 7 (5%) | 0 (0%) |

## Gemma-3-12B: appendix (the family is in 20% or more of the lies or of the truths; most frequent first)

| family | members (a selection) | position | lies (49) | truths (32) | no-pressure truths (135) | unrelated (179) |
|---|---|---|---|---|---|---|
| hush emoji | 🤫, 🤐 | `<start_of_turn>` | 43 (88%) | 22 (69%) | 24 (18%) | 1 (1%) |
| hush emoji | 🤫, 🤐 | newline | 28 (57%) | 11 (34%) | 1 (1%) | 0 (0%) |
| pretend | ` pretending`, ` pretended`, ` pretends` | `user` | 23 (47%) | 18 (56%) | 21 (16%) | 0 (0%) |
| lie | 謊, মিথ্যা, 谎, 거짓, झूठ, ` lies`, ` lying`, ` lied` … (15 tokens) | newline (lie-leaning here) | 20 (41%) | 2 (6%) | 0 (0%) | 0 (0%) |
| obfuscate | ` obfusc` | `<start_of_turn>` | 18 (37%) | 5 (16%) | 1 (1%) | 0 (0%) |
| knowingly | ` knowingly`, ` bewusst` | `<start_of_turn>` (lie-leaning here) | 16 (33%) | 3 (9%) | 6 (4%) | 0 (0%) |
| deliberately | ` knowingly`, 故意, ` intentionally` | `<start_of_turn>` (lie-leaning here) | 15 (31%) | 2 (6%) | 7 (5%) | 1 (1%) |
| obfuscate | ` obfusc` | newline (lie-leaning here) | 15 (31%) | 3 (9%) | 0 (0%) | 0 (0%) |
| reassure | ` reassurance`, ` reassuring`, ` reassured`, ` reassure` | newline | 15 (31%) | 5 (16%) | 7 (5%) | 0 (0%) |
| blatant | ` blatantly`, ` blatant` | `<start_of_turn>` (lie-leaning here) | 14 (29%) | 4 (12%) | 0 (0%) | 0 (0%) |
| frank | ` Frankly` | second newline (lie-leaning here) | 13 (27%) | 3 (9%) | 4 (3%) | 0 (0%) |
| lie | 謊, মিথ্যা, 谎, 거짓, झूठ, ` lies`, ` lying`, ` lied` … (15 tokens) | `<start_of_turn>` | 13 (27%) | 5 (16%) | 1 (1%) | 0 (0%) |
| pretend | ` pretending`, ` pretended`, ` pretends` | second newline | 13 (27%) | 5 (16%) | 38 (28%) | 3 (2%) |
| pretend | ` pretending`, ` pretended`, ` pretends` | `<start_of_turn>` | 13 (27%) | 6 (19%) | 3 (2%) | 0 (0%) |
| mislead | ` misleading`, ` mislead`, ` misled` | newline (lie-leaning here) | 12 (24%) | 2 (6%) | 0 (0%) | 0 (0%) |
| mislead | ` misleading`, ` mislead`, ` misled` | `<start_of_turn>` (lie-leaning here) | 12 (24%) | 3 (9%) | 4 (3%) | 0 (0%) |
| suspicion | ` suspicions`, ` suspiciously`, ` suspicious` | second newline (lie-leaning here) | 11 (22%) | 1 (3%) | 4 (3%) | 0 (0%) |
| doubt | ` doubting`, 质疑, ` doubted`, ` doubts` | second newline (lie-leaning here) | 11 (22%) | 3 (9%) | 2 (1%) | 0 (0%) |
| hide | 隐藏, ` hiding`, скры, ` concealing`, `Hide`, ` concealment`, লুকিয়ে, `Hid` … (21 tokens) | `<end_of_turn>` | 11 (22%) | 6 (19%) | 5 (4%) | 5 (3%) |
| pretend | ` pretending`, ` pretended`, ` pretends` | newline (lie-leaning here) | 10 (20%) | 1 (3%) | 0 (0%) | 0 (0%) |
| evade | ` evas`, ` evasion`, 回避, ` evade`, ` evaded` | newline (lie-leaning here) | 10 (20%) | 2 (6%) | 1 (1%) | 0 (0%) |
| protect | `Protect`, ` melindungi`, 保护, ` protecting`, ` Protecting`, ` protect`, `Protection`, `protect` … (14 tokens) | `<start_of_turn>` (lie-leaning here) | 10 (20%) | 2 (6%) | 1 (1%) | 0 (0%) |
| reassure | ` reassurance`, ` reassuring`, ` reassured`, ` reassure` | second newline | 10 (20%) | 8 (25%) | 5 (4%) | 0 (0%) |

## Gemma-3-12B: every token

| family | members (a selection) | position | lies (49) | truths (32) | no-pressure truths (135) | unrelated (179) |
|---|---|---|---|---|---|---|
| one or more of the eight newline families | lie, obfuscate, mislead, pretend, evade, hide, deflect, blatant | `<end_of_turn>` | 12 (24%) | 6 (19%) | 5 (4%) | 5 (3%) |
| one or more of the eight newline families | lie, obfuscate, mislead, pretend, evade, hide, deflect, blatant | newline | 30 (61%) | 5 (16%) | 2 (1%) | 0 (0%) |
| one or more of the eight newline families | lie, obfuscate, mislead, pretend, evade, hide, deflect, blatant | `<start_of_turn>` | 27 (55%) | 12 (38%) | 8 (6%) | 0 (0%) |
| one or more of the eight newline families | lie, obfuscate, mislead, pretend, evade, hide, deflect, blatant | `user` | 23 (47%) | 18 (56%) | 21 (16%) | 0 (0%) |
| one or more of the eight newline families | lie, obfuscate, mislead, pretend, evade, hide, deflect, blatant | second newline | 15 (31%) | 7 (22%) | 38 (28%) | 3 (2%) |
| lie | 謊, মিথ্যা, 谎, 거짓, झूठ, ` lies`, ` lying`, ` lied` … (15 tokens) | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| lie | 謊, মিথ্যা, 谎, 거짓, झूठ, ` lies`, ` lying`, ` lied` … (15 tokens) | newline (lie-leaning here) | 20 (41%) | 2 (6%) | 0 (0%) | 0 (0%) |
| lie | 謊, মিথ্যা, 谎, 거짓, झूठ, ` lies`, ` lying`, ` lied` … (15 tokens) | `<start_of_turn>` | 13 (27%) | 5 (16%) | 1 (1%) | 0 (0%) |
| lie | 謊, মিথ্যা, 谎, 거짓, झूठ, ` lies`, ` lying`, ` lied` … (15 tokens) | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| lie | 謊, মিথ্যা, 谎, 거짓, झूठ, ` lies`, ` lying`, ` lied` … (15 tokens) | second newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| obfuscate | ` obfusc` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| obfuscate | ` obfusc` | newline (lie-leaning here) | 15 (31%) | 3 (9%) | 0 (0%) | 0 (0%) |
| obfuscate | ` obfusc` | `<start_of_turn>` | 18 (37%) | 5 (16%) | 1 (1%) | 0 (0%) |
| obfuscate | ` obfusc` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| obfuscate | ` obfusc` | second newline | 1 (2%) | 0 (0%) | 0 (0%) | 0 (0%) |
| mislead | ` misleading`, ` mislead`, ` misled` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| mislead | ` misleading`, ` mislead`, ` misled` | newline (lie-leaning here) | 12 (24%) | 2 (6%) | 0 (0%) | 0 (0%) |
| mislead | ` misleading`, ` mislead`, ` misled` | `<start_of_turn>` (lie-leaning here) | 12 (24%) | 3 (9%) | 4 (3%) | 0 (0%) |
| mislead | ` misleading`, ` mislead`, ` misled` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| mislead | ` misleading`, ` mislead`, ` misled` | second newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| pretend | ` pretending`, ` pretended`, ` pretends` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| pretend | ` pretending`, ` pretended`, ` pretends` | newline (lie-leaning here) | 10 (20%) | 1 (3%) | 0 (0%) | 0 (0%) |
| pretend | ` pretending`, ` pretended`, ` pretends` | `<start_of_turn>` | 13 (27%) | 6 (19%) | 3 (2%) | 0 (0%) |
| pretend | ` pretending`, ` pretended`, ` pretends` | `user` | 23 (47%) | 18 (56%) | 21 (16%) | 0 (0%) |
| pretend | ` pretending`, ` pretended`, ` pretends` | second newline | 13 (27%) | 5 (16%) | 38 (28%) | 3 (2%) |
| evade | ` evas`, ` evasion`, 回避, ` evade`, ` evaded` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| evade | ` evas`, ` evasion`, 回避, ` evade`, ` evaded` | newline (lie-leaning here) | 10 (20%) | 2 (6%) | 1 (1%) | 0 (0%) |
| evade | ` evas`, ` evasion`, 回避, ` evade`, ` evaded` | `<start_of_turn>` | 0 (0%) | 1 (3%) | 0 (0%) | 0 (0%) |
| evade | ` evas`, ` evasion`, 回避, ` evade`, ` evaded` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| evade | ` evas`, ` evasion`, 回避, ` evade`, ` evaded` | second newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| hide | 隐藏, ` hiding`, скры, ` concealing`, `Hide`, ` concealment`, লুকিয়ে, `Hid` … (21 tokens) | `<end_of_turn>` | 11 (22%) | 6 (19%) | 5 (4%) | 5 (3%) |
| hide | 隐藏, ` hiding`, скры, ` concealing`, `Hide`, ` concealment`, লুকিয়ে, `Hid` … (21 tokens) | newline (lie-leaning here) | 9 (18%) | 2 (6%) | 1 (1%) | 0 (0%) |
| hide | 隐藏, ` hiding`, скры, ` concealing`, `Hide`, ` concealment`, লুকিয়ে, `Hid` … (21 tokens) | `<start_of_turn>` | 9 (18%) | 3 (9%) | 0 (0%) | 0 (0%) |
| hide | 隐藏, ` hiding`, скры, ` concealing`, `Hide`, ` concealment`, লুকিয়ে, `Hid` … (21 tokens) | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| hide | 隐藏, ` hiding`, скры, ` concealing`, `Hide`, ` concealment`, লুকিয়ে, `Hid` … (21 tokens) | second newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| deflect | ` deflect`, ` deflection`, ` deflected` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| deflect | ` deflect`, ` deflection`, ` deflected` | newline (lie-leaning here) | 9 (18%) | 2 (6%) | 0 (0%) | 0 (0%) |
| deflect | ` deflect`, ` deflection`, ` deflected` | `<start_of_turn>` | 2 (4%) | 1 (3%) | 0 (0%) | 0 (0%) |
| deflect | ` deflect`, ` deflection`, ` deflected` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| deflect | ` deflect`, ` deflection`, ` deflected` | second newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| blatant | ` blatantly`, ` blatant` | `<end_of_turn>` | 1 (2%) | 0 (0%) | 0 (0%) | 0 (0%) |
| blatant | ` blatantly`, ` blatant` | newline (lie-leaning here) | 8 (16%) | 2 (6%) | 0 (0%) | 0 (0%) |
| blatant | ` blatantly`, ` blatant` | `<start_of_turn>` (lie-leaning here) | 14 (29%) | 4 (12%) | 0 (0%) | 0 (0%) |
| blatant | ` blatantly`, ` blatant` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| blatant | ` blatantly`, ` blatant` | second newline | 4 (8%) | 2 (6%) | 0 (0%) | 0 (0%) |
| deliberately | ` knowingly`, 故意, ` intentionally` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| deliberately | ` knowingly`, 故意, ` intentionally` | newline | 2 (4%) | 0 (0%) | 0 (0%) | 0 (0%) |
| deliberately | ` knowingly`, 故意, ` intentionally` | `<start_of_turn>` (lie-leaning here) | 15 (31%) | 2 (6%) | 7 (5%) | 1 (1%) |
| deliberately | ` knowingly`, 故意, ` intentionally` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| deliberately | ` knowingly`, 故意, ` intentionally` | second newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| knowingly | ` knowingly`, ` bewusst` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| knowingly | ` knowingly`, ` bewusst` | newline | 2 (4%) | 0 (0%) | 0 (0%) | 0 (0%) |
| knowingly | ` knowingly`, ` bewusst` | `<start_of_turn>` (lie-leaning here) | 16 (33%) | 3 (9%) | 6 (4%) | 0 (0%) |
| knowingly | ` knowingly`, ` bewusst` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| knowingly | ` knowingly`, ` bewusst` | second newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| suspicion | ` suspicions`, ` suspiciously`, ` suspicious` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| suspicion | ` suspicions`, ` suspiciously`, ` suspicious` | newline | 2 (4%) | 1 (3%) | 0 (0%) | 0 (0%) |
| suspicion | ` suspicions`, ` suspiciously`, ` suspicious` | `<start_of_turn>` | 5 (10%) | 2 (6%) | 6 (4%) | 0 (0%) |
| suspicion | ` suspicions`, ` suspiciously`, ` suspicious` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| suspicion | ` suspicions`, ` suspiciously`, ` suspicious` | second newline (lie-leaning here) | 11 (22%) | 1 (3%) | 4 (3%) | 0 (0%) |
| frank | ` Frankly` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| frank | ` Frankly` | newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| frank | ` Frankly` | `<start_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| frank | ` Frankly` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| frank | ` Frankly` | second newline (lie-leaning here) | 13 (27%) | 3 (9%) | 4 (3%) | 0 (0%) |
| false | ` falsehood`, ` untrue`, `False` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| false | ` falsehood`, ` untrue`, `False` | newline | 2 (4%) | 1 (3%) | 0 (0%) | 0 (0%) |
| false | ` falsehood`, ` untrue`, `False` | `<start_of_turn>` (lie-leaning here) | 8 (16%) | 0 (0%) | 0 (0%) | 0 (0%) |
| false | ` falsehood`, ` untrue`, `False` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| false | ` falsehood`, ` untrue`, `False` | second newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| protect | `Protect`, ` melindungi`, 保护, ` protecting`, ` Protecting`, ` protect`, `Protection`, `protect` … (14 tokens) | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| protect | `Protect`, ` melindungi`, 保护, ` protecting`, ` Protecting`, ` protect`, `Protection`, `protect` … (14 tokens) | newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| protect | `Protect`, ` melindungi`, 保护, ` protecting`, ` Protecting`, ` protect`, `Protection`, `protect` … (14 tokens) | `<start_of_turn>` (lie-leaning here) | 10 (20%) | 2 (6%) | 1 (1%) | 0 (0%) |
| protect | `Protect`, ` melindungi`, 保护, ` protecting`, ` Protecting`, ` protect`, `Protection`, `protect` … (14 tokens) | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| protect | `Protect`, ` melindungi`, 保护, ` protecting`, ` Protecting`, ` protect`, `Protection`, `protect` … (14 tokens) | second newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| doubt | ` doubting`, 质疑, ` doubted`, ` doubts` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| doubt | ` doubting`, 质疑, ` doubted`, ` doubts` | newline | 2 (4%) | 1 (3%) | 0 (0%) | 0 (0%) |
| doubt | ` doubting`, 质疑, ` doubted`, ` doubts` | `<start_of_turn>` | 0 (0%) | 0 (0%) | 2 (1%) | 0 (0%) |
| doubt | ` doubting`, 质疑, ` doubted`, ` doubts` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| doubt | ` doubting`, 质疑, ` doubted`, ` doubts` | second newline (lie-leaning here) | 11 (22%) | 3 (9%) | 2 (1%) | 0 (0%) |
| reassure | ` reassurance`, ` reassuring`, ` reassured`, ` reassure` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| reassure | ` reassurance`, ` reassuring`, ` reassured`, ` reassure` | newline | 15 (31%) | 5 (16%) | 7 (5%) | 0 (0%) |
| reassure | ` reassurance`, ` reassuring`, ` reassured`, ` reassure` | `<start_of_turn>` (lie-leaning here) | 9 (18%) | 2 (6%) | 5 (4%) | 0 (0%) |
| reassure | ` reassurance`, ` reassuring`, ` reassured`, ` reassure` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| reassure | ` reassurance`, ` reassuring`, ` reassured`, ` reassure` | second newline | 10 (20%) | 8 (25%) | 5 (4%) | 0 (0%) |
| hush emoji | 🤫, 🤐 | `<end_of_turn>` | 1 (2%) | 1 (3%) | 0 (0%) | 0 (0%) |
| hush emoji | 🤫, 🤐 | newline | 28 (57%) | 11 (34%) | 1 (1%) | 0 (0%) |
| hush emoji | 🤫, 🤐 | `<start_of_turn>` | 43 (88%) | 22 (69%) | 24 (18%) | 1 (1%) |
| hush emoji | 🤫, 🤐 | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| hush emoji | 🤫, 🤐 | second newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |

## Gemma-3-27B: main text (the family is in 30% or more of the lies; most frequent first)

| family | members (a selection) | position | lies (58) | truths (30) | no-pressure truths (133) | unrelated (199) |
|---|---|---|---|---|---|---|
| keep-quiet emoji | 🤫, 🤐, 🔇, 沉默 | `<start_of_turn>` | 49 (84%) | 22 (73%) | 47 (35%) | 0 (0%) |
| keep-quiet emoji | 🤫, 🤐, 🔇, 沉默 | `<end_of_turn>` | 38 (66%) | 15 (50%) | 5 (4%) | 0 (0%) |
| keep-quiet emoji | 🤫, 🤐, 🔇, 沉默 | newline | 35 (60%) | 12 (40%) | 13 (10%) | 1 (1%) |
| lie | 🤥, মিথ্যা, 거짓, झूठ … (15 tokens) | `<start_of_turn>` | 30 (52%) | 9 (30%) | 11 (8%) | 0 (0%) |
| secret | خفیہ, 秘密, 비밀, ` secretos` … (6 tokens) | `<start_of_turn>` | 25 (43%) | 8 (27%) | 4 (3%) | 0 (0%) |
| lie | 🤥, মিথ্যা, 거짓, झूठ … (15 tokens) | newline | 20 (34%) | 4 (13%) | 0 (0%) | 0 (0%) |

## Gemma-3-27B: appendix (the family is in 20% or more of the lies or of the truths; most frequent first)

| family | members (a selection) | position | lies (58) | truths (30) | no-pressure truths (133) | unrelated (199) |
|---|---|---|---|---|---|---|
| keep-quiet emoji | 🤫, 🤐, 🔇, 沉默 | `<start_of_turn>` | 49 (84%) | 22 (73%) | 47 (35%) | 0 (0%) |
| keep-quiet emoji | 🤫, 🤐, 🔇, 沉默 | `<end_of_turn>` | 38 (66%) | 15 (50%) | 5 (4%) | 0 (0%) |
| keep-quiet emoji | 🤫, 🤐, 🔇, 沉默 | newline | 35 (60%) | 12 (40%) | 13 (10%) | 1 (1%) |
| lying-face emoji | 🤥 | `<start_of_turn>` | 30 (52%) | 8 (27%) | 11 (8%) | 0 (0%) |
| lie | 🤥, মিথ্যা, 거짓, झूठ, 謊, 谎, ` lied`, ` liar` … (15 tokens) | `<start_of_turn>` | 30 (52%) | 9 (30%) | 11 (8%) | 0 (0%) |
| secret | خفیہ, 秘密, 비밀, ` secretos`, ` secrecy`, `secrets` | `<start_of_turn>` | 25 (43%) | 8 (27%) | 4 (3%) | 0 (0%) |
| lie | 🤥, মিথ্যা, 거짓, झूठ, 謊, 谎, ` lied`, ` liar` … (15 tokens) | newline (lie-leaning here) | 20 (34%) | 4 (13%) | 0 (0%) | 0 (0%) |
| lying-face emoji | 🤥 | newline (lie-leaning here) | 19 (33%) | 4 (13%) | 0 (0%) | 0 (0%) |
| suspicion | 怀疑, ` suspiciously`, ` suspicions`, ` suspicion`, ` suspicious` | second newline (lie-leaning here) | 12 (21%) | 0 (0%) | 0 (0%) | 0 (0%) |
| secret | خفیہ, 秘密, 비밀, ` secretos`, ` secrecy`, `secrets` | newline (lie-leaning here) | 12 (21%) | 3 (10%) | 2 (2%) | 0 (0%) |
| confidential | गोपनीयता, गोपनीय, 隐私, ` confidentialité`, ` confidentiality` | `<start_of_turn>` (lie-leaning here) | 12 (21%) | 3 (10%) | 5 (4%) | 0 (0%) |

## Gemma-3-27B: every token

| family | members (a selection) | position | lies (58) | truths (30) | no-pressure truths (133) | unrelated (199) |
|---|---|---|---|---|---|---|
| one or more of the three newline families | lie, lying-face emoji, secret | `<end_of_turn>` | 6 (10%) | 0 (0%) | 0 (0%) | 0 (0%) |
| one or more of the three newline families | lie, lying-face emoji, secret | newline | 24 (41%) | 6 (20%) | 2 (2%) | 0 (0%) |
| one or more of the three newline families | lie, lying-face emoji, secret | `<start_of_turn>` | 38 (66%) | 12 (40%) | 14 (11%) | 0 (0%) |
| one or more of the three newline families | lie, lying-face emoji, secret | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| one or more of the three newline families | lie, lying-face emoji, secret | second newline | 1 (2%) | 0 (0%) | 0 (0%) | 0 (0%) |
| lie | 🤥, মিথ্যা, 거짓, झूठ, 謊, 谎, ` lied`, ` liar` … (15 tokens) | `<end_of_turn>` | 6 (10%) | 0 (0%) | 0 (0%) | 0 (0%) |
| lie | 🤥, মিথ্যা, 거짓, झूठ, 謊, 谎, ` lied`, ` liar` … (15 tokens) | newline (lie-leaning here) | 20 (34%) | 4 (13%) | 0 (0%) | 0 (0%) |
| lie | 🤥, মিথ্যা, 거짓, झूठ, 謊, 谎, ` lied`, ` liar` … (15 tokens) | `<start_of_turn>` | 30 (52%) | 9 (30%) | 11 (8%) | 0 (0%) |
| lie | 🤥, মিথ্যা, 거짓, झूठ, 謊, 谎, ` lied`, ` liar` … (15 tokens) | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| lie | 🤥, মিথ্যা, 거짓, झूठ, 謊, 谎, ` lied`, ` liar` … (15 tokens) | second newline | 1 (2%) | 0 (0%) | 0 (0%) | 0 (0%) |
| lying-face emoji | 🤥 | `<end_of_turn>` | 6 (10%) | 0 (0%) | 0 (0%) | 0 (0%) |
| lying-face emoji | 🤥 | newline (lie-leaning here) | 19 (33%) | 4 (13%) | 0 (0%) | 0 (0%) |
| lying-face emoji | 🤥 | `<start_of_turn>` | 30 (52%) | 8 (27%) | 11 (8%) | 0 (0%) |
| lying-face emoji | 🤥 | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| lying-face emoji | 🤥 | second newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| secret | خفیہ, 秘密, 비밀, ` secretos`, ` secrecy`, `secrets` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| secret | خفیہ, 秘密, 비밀, ` secretos`, ` secrecy`, `secrets` | newline (lie-leaning here) | 12 (21%) | 3 (10%) | 2 (2%) | 0 (0%) |
| secret | خفیہ, 秘密, 비밀, ` secretos`, ` secrecy`, `secrets` | `<start_of_turn>` | 25 (43%) | 8 (27%) | 4 (3%) | 0 (0%) |
| secret | خفیہ, 秘密, 비밀, ` secretos`, ` secrecy`, `secrets` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| secret | خفیہ, 秘密, 비밀, ` secretos`, ` secrecy`, `secrets` | second newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| suspicion | 怀疑, ` suspiciously`, ` suspicions`, ` suspicion`, ` suspicious` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| suspicion | 怀疑, ` suspiciously`, ` suspicions`, ` suspicion`, ` suspicious` | newline | 2 (3%) | 0 (0%) | 1 (1%) | 0 (0%) |
| suspicion | 怀疑, ` suspiciously`, ` suspicions`, ` suspicion`, ` suspicious` | `<start_of_turn>` | 4 (7%) | 0 (0%) | 1 (1%) | 0 (0%) |
| suspicion | 怀疑, ` suspiciously`, ` suspicions`, ` suspicion`, ` suspicious` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| suspicion | 怀疑, ` suspiciously`, ` suspicions`, ` suspicion`, ` suspicious` | second newline (lie-leaning here) | 12 (21%) | 0 (0%) | 0 (0%) | 0 (0%) |
| confidential | गोपनीयता, गोपनीय, 隐私, ` confidentialité`, ` confidentiality` | `<end_of_turn>` | 0 (0%) | 0 (0%) | 1 (1%) | 0 (0%) |
| confidential | गोपनीयता, गोपनीय, 隐私, ` confidentialité`, ` confidentiality` | newline | 5 (9%) | 1 (3%) | 8 (6%) | 0 (0%) |
| confidential | गोपनीयता, गोपनीय, 隐私, ` confidentialité`, ` confidentiality` | `<start_of_turn>` (lie-leaning here) | 12 (21%) | 3 (10%) | 5 (4%) | 0 (0%) |
| confidential | गोपनीयता, गोपनीय, 隐私, ` confidentialité`, ` confidentiality` | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| confidential | गोपनीयता, गोपनीय, 隐私, ` confidentialité`, ` confidentiality` | second newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| keep-quiet emoji | 🤫, 🤐, 🔇, 沉默 | `<end_of_turn>` | 38 (66%) | 15 (50%) | 5 (4%) | 0 (0%) |
| keep-quiet emoji | 🤫, 🤐, 🔇, 沉默 | newline | 35 (60%) | 12 (40%) | 13 (10%) | 1 (1%) |
| keep-quiet emoji | 🤫, 🤐, 🔇, 沉默 | `<start_of_turn>` | 49 (84%) | 22 (73%) | 47 (35%) | 0 (0%) |
| keep-quiet emoji | 🤫, 🤐, 🔇, 沉默 | `user` | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| keep-quiet emoji | 🤫, 🤐, 🔇, 沉默 | second newline | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
