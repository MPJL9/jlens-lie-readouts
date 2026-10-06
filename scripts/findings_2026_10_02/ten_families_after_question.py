"""family_findings.md Section 1: the ten lie-side families of post-response slot 1, each with the word
list it has there, counted at every position after the self-report question. Qwen, J-lens, band
35-58, presence index (build split and unrelated set only). Prints the lists, the baseline and a
per-position summary. Run from the project root: python3 scripts/findings_2026_10_02/ten_families_after_question.py"""
import sys, json; sys.path.insert(0,'scripts')
import numpy as np, presence as P, common as C
m='qwen3.6-27b'
d=P.load(m,'J'); vocab=C.load_vocab(m)
fd=json.load(open('analysis/families/families_draft.json'))['entries']
TEN=['lie','deceive','conceal','misinformation','fabricate','mislead','false','falsehood','dishonest','fake']
fam={}
for e in fd:
    if e['model']==m and e['lens']=='J' and e['position']=='postresp_slot1' and e['part']=='prefix' and e['status']=='keep' and e['name'] in TEN:
        fam.setdefault(e['name'],set()).update(x['id'] for x in e['members'])
for k in TEN: print(k,len(fam[k]),[vocab[i] for i in sorted(fam[k])][:20])
cls=d['cls']
def rate(mask,sel):
    n=sel.sum(); return (int((mask&sel).sum()),int(n))
def pc(t): return '–' if t[1]==0 else f"{100*t[0]/t[1]:.0f}%"
# check baseline equals the TMP file
for k in TEN:
    pm=P.present_mask(d,'prefix','postresp_slot1',fam[k]); hv=P.have_mask(d,'prefix','postresp_slot1')
    print(k,[rate(pm,hv&(cls==c)) for c in P.CLASSES])
import pickle
out={}
for w in C.WORDINGS:
    ans=P.answer(d,w)
    for pos in P.positions(d,w):
        hv=P.have_mask(d,w,pos)
        for k in TEN:
            pm=P.present_mask(d,w,pos,fam[k])
            out[(w,pos,k)]=dict(lie=rate(pm,hv&(cls=='lie')),truth=rate(pm,hv&(cls=='truth')),np=rate(pm,hv&(cls=='np_truth')),un=rate(pm,hv&(cls=='unrelated')),
                                lie_deny=rate(pm,hv&(cls=='lie')&(ans=='deny')),truth_deny=rate(pm,hv&(cls=='truth')&(ans=='deny')))
# position summary: mean over the ten families
f=lambda t: t[0]/t[1] if t[1] else np.nan
print('\nmean over ten families: lies / truths / lies deny / truths deny / np / unrelated ; n families with (lie_deny - truth_deny)>=30pt and truth_deny<=20%')
for w in C.WORDINGS:
    for pos in P.positions(d,w):
        r=[out[(w,pos,k)] for k in TEN]
        mm=lambda key: np.nanmean([f(x[key]) for x in r])
        good=[k for k in TEN if f(out[(w,pos,k)]['lie_deny'])-f(out[(w,pos,k)]['truth_deny'])>=.30 and f(out[(w,pos,k)]['truth_deny'])<=.20]
        if mm('lie')>=.15:
            print(f"{w:10} {pos:14} {mm('lie'):5.0%} {mm('truth'):5.0%} | {mm('lie_deny'):5.0%} {mm('truth_deny'):5.0%} | {mm('np'):5.0%} {mm('un'):5.0%} | {good}")
