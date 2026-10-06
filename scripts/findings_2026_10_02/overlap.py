"""family_findings.md Section 9: how much the outstanding families overlap (Qwen, J-lens, band 35-58,
build split, in-sample). Families as in the draft (unmerged, kept entries pooled by name).
Run from the project root: python3 scripts/findings_2026_10_02/overlap.py"""
import sys, json; sys.path.insert(0, 'scripts')
import numpy as np, presence as P, common as C
from collections import defaultdict
m = 'qwen3.6-27b'; d = P.load(m, 'J'); cls = d['cls']; scn = d['scenario']
fd = [e for e in json.load(open('analysis/families/families_draft.json'))['entries'] if e['model'] == m and e['lens'] == 'J' and e['status'] == 'keep']
def fam(part, pos, name):
    s = set()
    for e in fd:
        if e['part'] == part and e['position'] == pos and e['name'] == name: s |= {x['id'] for x in e['members']}
    return s
EIGHT = ['lie', 'fake', 'falsehood', 'misinformation', 'deceive', 'fabricate', 'false', 'mislead']
hv = P.have_mask(d, 'prefix', 'postresp_slot1')
M = {n: P.present_mask(d, 'prefix', 'postresp_slot1', fam('prefix', 'postresp_slot1', n)) for n in EIGHT + ['conceal', 'dishonest', 'excuse']}
cnt = sum(M[n].astype(int) for n in EIGHT)
G = {'lies': cls == 'lie', 'truths': cls == 'truth', 'no-pressure truths': cls == 'np_truth', 'unrelated': cls == 'unrelated'}
print('## number of the eight families present at post-response slot 1')
print('| at least k families | ' + ' | '.join(G) + ' |')
for k in range(1, 9):
    print(f'| {k} | ' + ' | '.join(f"{((cnt >= k) & g & hv).sum()}/{(g & hv).sum()} ({100 * ((cnt >= k) & g & hv).sum() / (g & hv).sum():.0f}%)" for g in G.values()) + ' |')
print('\nlies with none of the eight:', ((cnt == 0) & G['lies']).sum(), '; with conceal/dishonest/excuse only:', ((cnt == 0) & G['lies'] & (M['conceal'] | M['dishonest'] | M['excuse'])).sum())
print('truths with one or more:', ((cnt >= 1) & G['truths']).sum(), ' their counts:', sorted(cnt[(cnt >= 1) & G['truths']].tolist()))
both = sorted(set(scn[G['lies']]) & set(scn[G['truths']]))
inb = np.isin(scn, both)
for k in (1, 2, 3):
    print(f'same-scenario pairs ({len(both)}), at least {k}: lies {((cnt >= k) & G["lies"] & inb).sum()}/{(G["lies"] & inb).sum()}, truths {((cnt >= k) & G["truths"] & inb).sum()}/{(G["truths"] & inb).sum()}')
print('\n## greedy order: which family adds the most lies not yet caught')
left = G['lies'].copy(); order = []; pool = list(EIGHT)
while pool:
    best = max(pool, key=lambda n: (M[n] & left).sum()); order.append((best, int((M[best] & left).sum()))); left &= ~M[best]; pool.remove(best)
print(order, 'not caught:', int(left.sum()))
print('\n## overlap between pairs among lies (share of lies with A that also have B)')
print('| A \\ B | ' + ' | '.join(EIGHT) + ' |')
for a in EIGHT:
    print(f'| {a} | ' + ' | '.join('–' if a == b else f"{100 * (M[a] & M[b] & G['lies']).sum() / max(1, (M[a] & G['lies']).sum()):.0f}%" for b in EIGHT) + ' |')
# after the question: do the cells catch lies that slot 1 missed?
print('\n## after the question (among lying deniers): cells of Section 7, and the lies that slot 1 missed')
cells = [('Q1_bare', 'postans_slot1', 'lie'), ('Q1_bare', 'postans_slot1', 'false'), ('Q1_bare', 'preans_slot4', 'confidential'), ('Q2_after', 'postans_slot1', 'false'),
         ('Q2_after', 'preans_slot1', 'knowingly'), ('Q7_ab', 'preans_slot4', 'hide'), ('Q7_ab', 'preans_slot4', 'conceal'), ('Q7_ab', 'preans_slot4', 'cannot'),
         ('Q9_dyl', 'think_slot1', 'fictional'), ('Q9_dyl', 'preans_slot4', 'cannot'), ('Q9_dyl', 'preans_slot1', 'knowingly')]
missed = (cnt == 0) & G['lies']; weak = (cnt <= 1) & G['lies']
for w in C.WORDINGS:
    ans = P.answer(d, w); cs = [c for c in cells if c[0] == w]
    if not cs: continue
    any_ = np.zeros(len(cls), bool); hvw = np.ones(len(cls), bool)
    for (_, pos, name) in cs:
        pm = P.present_mask(d, w, pos, fam(w, pos, name)); h = P.have_mask(d, w, pos); any_ |= pm & h
        print(f"  {w} {pos} {name}: lying deniers {(pm & h & G['lies'] & (ans == 'deny')).sum()}/{(h & G['lies'] & (ans == 'deny')).sum()}, truthful deniers {(pm & h & G['truths'] & (ans == 'deny')).sum()}/{(h & G['truths'] & (ans == 'deny')).sum()}; lies with none of the eight at slot 1: {(pm & h & missed).sum()}/{(h & missed).sum()}")
    ld = G['lies'] & (ans == 'deny'); td = G['truths'] & (ans == 'deny')
    print(f"  {w} any of its cells: lying deniers {(any_ & ld).sum()}/{ld.sum()} ({100 * (any_ & ld).sum() / ld.sum():.0f}%), truthful deniers {(any_ & td).sum()}/{td.sum()} ({100 * (any_ & td).sum() / td.sum():.0f}%)")
    print(f"  {w} slot-1 count >= 1 among lying deniers {((cnt >= 1) & ld).sum()}/{ld.sum()}, truthful deniers {((cnt >= 1) & td).sum()}/{td.sum()}; either slot 1 or a cell: lying deniers {(((cnt >= 1) | any_) & ld).sum()}/{ld.sum()}, truthful deniers {(((cnt >= 1) | any_) & td).sum()}/{td.sum()}")
