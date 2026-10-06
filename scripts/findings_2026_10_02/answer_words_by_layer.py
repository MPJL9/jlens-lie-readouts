"""family_findings.md Section 2.2: layer by layer, the share of scenario transcripts (build split only)
with a yes / no / A / B word in the J-lens readout at the positions before the answer, by the
self-report answer. Reads the exports directly (about two minutes). Run from the project root:
python3 scripts/findings_2026_10_02/answer_words_by_layer.py"""
import sys; sys.path.insert(0,'scripts')
import numpy as np, common as C, json, pickle
from presence_index import read_ids, keep
from frequency_tables import part_positions
m='qwen3.6-27b'
man=C.load_manifest(m); vocab=C.load_vocab(m); layers=man['layers']
ents=[e for e in man['transcripts'] if e['set']=='scenario' and e['split']=='build']
assert not any(e['split']=='heldout' for e in ents)
def ids_for(strs, lower=False):
    return np.array([i for i,t in enumerate(vocab) if (t.strip().lower() if lower else t.strip()) in strs])
G={'yes':ids_for({'yes'},True),'no':ids_for({'no'},True),'是':ids_for({'是','是的'}),'否':ids_for({'否'}),'不是':ids_for({'不是'}),'A':ids_for({'A'}),'B':ids_for({'B'})}
res={}
for w in ['Q9_dyl','Q2_after','Q7_ab']:
    for pos in ['preans_slot3','preans_slot4','think_slot2','think_slot3']:
        acc={}
        for e in ents:
            lab=e['wordings'][w]['answer_label']
            if lab not in('admit','deny'): continue
            h,ids=read_ids(m,e,w); p=part_positions(h)[pos]
            blk=np.asarray(ids['J'][:,p])  # [layers,K]
            for g,gi in G.items():
                hit=np.isin(blk,gi).any(1)
                acc.setdefault((g,lab),[]).append(hit)
        res[(w,pos)]={k:np.mean(v,0) for k,v in acc.items()}
print('layers',layers[0],layers[-1],len(layers))
sel=[l for l in layers if l>=30 and (l%4==2 or l>=56)]
for (w,pos),r in res.items():
    gs=['A','B'] if w=='Q7_ab' else ['yes','no','是','否']
    print(f"\n{w} {pos}   layer: "+' '.join(f"{l:>4}" for l in sel))
    for g in gs:
        for lab in ['admit','deny']:
            v=r[(g,lab)]
            print(f"  {g:4} {lab:5}      "+' '.join(f"{100*v[layers.index(l)]:4.0f}" for l in sel))
