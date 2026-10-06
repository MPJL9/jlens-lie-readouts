"""family_findings.md Section 10: what gpt-oss's `<|start|>` token reads out (user's question, 2026-10-02). How often
'schema' and ' interrogation' are in the readout at every pre-response and post-response slot, by transcript class.
Build split + unrelated set, prefix part only (the presence index has no pre-response slots). J-lens band 10-20
and by layer; logit lens band for comparison. Run from the project root:
python3 scripts/findings_2026_10_02/gpt_oss_start_token.py"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import numpy as np
import common as C
from presence_index import read_ids, keep

M = 'gpt-oss-20b'
v = C.load_vocab(M)
man = C.load_manifest(M)
entries = [e for e in man['transcripts'] if keep(e)]
layers = man['layers']
def cls(e):
    if e['set'] == 'scenario': return e['label']
    if e['set'] == 'nopressure': return 'np_truth' if e['label'] == 'truth' else 'np_lie'
    return 'unrelated'
CL = ['lie', 'truth', 'np_truth', 'unrelated']
TOK = {'schema (exact)': ['schema'], 'schema (any form)': ['schema', ' schema', 'Schema', ' Schema', 'schemas', ' schemas', 'Schemas', '\tSchema'],
       ' interrogation (exact)': [' interrogation'], 'interrogation (any form)': [' interrogation', ' interrog']}
ids = {k: {i for i, t in enumerate(v) if t in ws} for k, ws in TOK.items()}
POS = [f'preresp_slot{k}' for k in range(6)] + [f'postresp_slot{k}' for k in range(4)]
# counts[lens][pos][tok][class] = number present in band; bylayer[pos][tok][class][layer index]
n = {c: 0 for c in CL}
have = {p: {c: 0 for c in CL} for p in POS}
inband = {lens: {p: {k: {c: 0 for c in CL} for k in TOK} for p in POS} for lens in ('J', 'LL')}
bylayer = {p: {k: {c: np.zeros(len(layers), int) for c in CL} for k in TOK} for p in POS}
boundary = {}
for e in entries:
    c = cls(e)
    if c not in CL: continue
    n[c] += 1
    header, arr = read_ids(M, e, 'prefix')
    pm = {k: v for k, v in C.positions({'tokens': header['tokens'], 'segments': header['segments']}).items() if not k.startswith('resp_tok')}
    toks = header.get('tokens')
    for p in POS:
        if p not in pm: continue
        have[p][c] += 1
        if toks and p not in boundary:
            boundary[p] = toks[pm[p]]
        for lens in ('J', 'LL'):
            band = (C.BANDS if lens == 'J' else C.BANDS_LL)[M]
            li = [i for i, l in enumerate(layers) if band[0] <= l <= band[1]]
            block = np.asarray(arr[lens][:, pm[p]])            # [layers, K]
            for k, s in ids.items():
                hit = np.isin(block, list(s))                    # [layers, K]
                if hit[li].any(): inband[lens][p][k][c] += 1
                if lens == 'J': bylayer[p][k][c] += hit.any(1)
print('transcripts:', n, '| have position:', have)
print('boundary tokens:', boundary)
for lens in ('J', 'LL'):
    band = (C.BANDS if lens == 'J' else C.BANDS_LL)[M]
    print(f'\n## {lens}-lens, band {band[0]}-{band[1]}: transcripts with the token in the top-16 at one or more band layers')
    print('| position | token | ' + ' | '.join(CL) + ' |')
    for p in POS:
        for k in TOK:
            print(f'| {p} | {k} | ' + ' | '.join(f"{inband[lens][p][k][c]}/{have[p][c]} ({100*inband[lens][p][k][c]/max(1,have[p][c]):.0f}%)" for c in CL) + ' |')
print('\n## J-lens, by layer (percent of transcripts with the token in the top-16 at that layer), exact tokens')
print('| position | class | ' + ' | '.join(str(l) for l in layers) + ' |')
for p, k in (('preresp_slot1', 'schema (exact)'), ('preresp_slot1', ' interrogation (exact)'), ('postresp_slot1', 'schema (exact)'), ('postresp_slot1', ' interrogation (exact)')):
    for c in CL:
        print(f'| {p} {k} | {c} | ' + ' | '.join(f"{100*x/max(1,have[p][c]):.0f}" for x in bylayer[p][k][c]) + ' |')
