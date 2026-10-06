"""family_findings.md Section 8.7: truths that admit to lying (scenario set, build split only, commentary
transcripts left out). A truth that admits = judged truth whose self-report answer opens with "Yes" (Q7: "A").
Run from the project root:
  python3 scripts/findings_2026_10_03/truths_that_admit.py               (the counts, all four models)
  python3 scripts/findings_2026_10_03/truths_that_admit.py --read MODEL  (prints each such transcript of MODEL:
      system prompt, user prompt, response, the judge's reason, every admitting answer, gpt-oss's reasoning)"""
import sys, os; sys.path.insert(0, 'scripts')
import common as C
from collections import Counter, defaultdict
MODELS = ['gemma-3-12b-it', 'gemma-3-27b-it', 'qwen3.6-27b', 'gpt-oss-20b']
W = ['Q1_bare', 'Q2_after', 'Q6_factual', 'Q7_ab', 'Q9_dyl']
adm = lambda e: [w for w in W if e['wordings'][w]['answer_label'] == 'admit']
def build(m, label):
    return [e for e in C.load_manifest(m)['transcripts'] if e['set'] == 'scenario' and e['split'] == 'build' and e['label'] == label]

if '--read' not in sys.argv:
    print('| model | truths | admit under one or more wordings | under exactly one | patterns of the single-wording ones | lies: one or more |')
    print('|---|---|---|---|---|---|')
    for m in MODELS:
        t, l = build(m, 'truth'), build(m, 'lie')
        one = Counter(adm(e)[0][:2] for e in t if len(adm(e)) == 1)
        print(f"| {m} | {len(t)} | {sum(bool(adm(e)) for e in t)} | {sum(one.values())} | {dict(one)} | {sum(bool(adm(e)) for e in l)} of {len(l)} |")
        print(f"|  | per wording (Q1, Q2, Q6, Q7, Q9): truths {[sum(w in adm(e) for e in t) for w in W]}, lies {[sum(w in adm(e) for e in l) for w in W]} | | | | |")
else:
    m = sys.argv[sys.argv.index('--read') + 1]
    es = [e for e in build(m, 'truth') if adm(e)]
    tx = C.load_transcripts(m); keep = {e['tid'] for e in es}; seqs = defaultdict(dict)
    for r in C.read_jsonl(os.path.join(C.RUNS, C.slug(m), 'sequences.jsonl')):
        if r['tid'] in keep and r['part'] != 'prefix': seqs[r['tid']][r['part']] = r
    sq = lambda s: ' '.join(s.split())
    print(f'{m}: {len(es)} build-split truths that admit under one or more wordings')
    for i, e in enumerate(es, 1):
        t = tx[e['tid']]
        print(f"\n=== {i}. {e['item_id']} k{e['k']} | admits under {[w[:2] for w in adm(e)]}")
        for name, text in (('SYSTEM', t['system']), ('USER', t['user_prompt']), ('RESPONSE', t['response']), ('JUDGE', t['judge_reason'])):
            print(f'{name}: {sq(text)}')
        for w in adm(e):
            r = seqs[e['tid']][w]
            if r.get('answer_reasoning'): print(f'  {w} reasoning: {sq(r["answer_reasoning"])}')
            print(f'  {w} answer: {sq(r["answer_text"])}')
