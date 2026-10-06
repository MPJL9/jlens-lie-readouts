"""family_findings.md Section 2.1, 2.3, 2.4: yes / no / A / B words at the positions before the answer,
by wording and by the self-report answer. Qwen, J-lens, band 35-58, presence index (build split and
unrelated set only). Prints markdown tables. Run from the project root: python3 scripts/findings_2026_10_02/answer_words.py"""
import sys; sys.path.insert(0,'scripts')
import numpy as np, presence as P, common as C
m='qwen3.6-27b'
d=P.load(m,'J'); vocab=C.load_vocab(m)
def ids_for(strs, lower=False):
    out=[]
    for i,t in enumerate(vocab):
        s=t.strip()
        if lower: s=s.lower()
        if s in strs: out.append(i)
    return out
G={'yes':ids_for({'yes'},True),'no':ids_for({'no'},True),'是/是的':ids_for({'是','是的'}),'否/不是':ids_for({'否','不是'}),'是否':ids_for({'是否'}),
   'A':ids_for({'A'}),'B':ids_for({'B'})}
for k,v in G.items(): print(k,[vocab[i] for i in v])
scen=np.isin(d['cls'],['lie','truth']); unrel=d['cls']=='unrelated'
TOK={'preans_slot0':'turn end','preans_slot1':'newline','preans_slot2':'turn start','preans_slot3':'`assistant`','preans_slot4':'newline',
     'think_slot0':'`<think>`','think_slot1':'blank line','think_slot2':'`</think>`','think_slot3':'blank line',
     'postans_slot0':'turn end','postans_slot1':'newline','postans_slot2':'turn start','postans_slot3':'`user`','postans_slot4':'newline'}
def cell(mask,sel):
    n=sel.sum(); k=(mask&sel).sum()
    return f"{k}/{n} ({100*k/n:.0f}%)" if n else '–'
def table(w,groups,positions):
    ans=P.answer(d,w)
    print(f"\n**{w}** (scenario transcripts: {(scen&(ans=='admit')).sum()} admit, {(scen&(ans=='deny')).sum()} deny, {(scen&(ans=='other')).sum()} other)\n")
    hdr='| position | token | '+' | '.join(f"{g}: admit | {g}: deny | {g}: unrelated" for g in groups)+' |'
    print(hdr); print('|'+'---|'*(2+3*len(groups)))
    for pos in positions:
        have=P.have_mask(d,w,pos)
        row=[]
        for g in groups:
            pm=P.present_mask(d,w,pos,G[g])
            row+= [cell(pm,have&scen&(ans=='admit')),cell(pm,have&scen&(ans=='deny')),cell(pm,have&unrel)]
        print(f"| {pos} | {TOK[pos]} | "+' | '.join(row)+' |')
pos_pre=[p for p in TOK if not p.startswith('postans')]
for w in ['Q1_bare','Q2_after','Q6_factual','Q9_dyl']:
    table(w,['yes','no'],pos_pre)
table('Q7_ab',['yes','no'],pos_pre)
table('Q7_ab',['A','B'],pos_pre)
for w in ['Q9_dyl','Q7_ab']:
    table(w,['是/是的','否/不是'],pos_pre)
# where is 是否 present, any position, any wording
print('\n是否 present (scenario / unrelated), positions with >=10%:')
for w in C.WORDINGS:
    for pos in P.positions(d,w):
        have=P.have_mask(d,w,pos); pm=P.present_mask(d,w,pos,G['是否'])
        a=(pm&have&scen).sum()/max(1,(have&scen).sum()); b=(pm&have&unrel).sum()/max(1,(have&unrel).sum())
        if a>=.1 or b>=.1: print(w,pos,f"{a:.0%} {b:.0%}")
# strength: mean number of band layers where present, yes vs no at think_slot3, by answer
print('\nmean band layers (of 24) with the word in the top 16, among all transcripts of the group:')
def layers(w,pos,ids):
    n=np.zeros(len(d['transcripts']))
    tab=d['present'][w][pos]
    for t in ids:
        if t in tab:
            idx,c=tab[t]; np.maximum.at(n,idx.astype(int),c)
    return n
for w in ['Q2_after','Q6_factual','Q9_dyl','Q1_bare']:
    ans=P.answer(d,w)
    for pos in ['preans_slot3','preans_slot4','think_slot2','think_slot3']:
        ly=layers(w,pos,G['yes']); ln=layers(w,pos,G['no'])
        a=scen&(ans=='admit'); dn=scen&(ans=='deny')
        print(f"{w} {pos}: yes admit {ly[a].mean():.1f} deny {ly[dn].mean():.1f} unrel {ly[unrel].mean():.1f} | no admit {ln[a].mean():.1f} deny {ln[dn].mean():.1f} unrel {ln[unrel].mean():.1f}")
