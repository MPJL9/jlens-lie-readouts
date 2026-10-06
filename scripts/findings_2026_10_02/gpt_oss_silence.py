"""family_findings.md Section 10: why does gpt-oss-20b show no lie words at template positions?
For gpt-oss (and Qwen as a reference): the share of build-split scenario transcripts in which a
lie word (or a yes / no word) is in the top-16 readout, by lens, by layer and by segment of the
sequence (response tokens, post-response slots, question tokens, pre-answer slots, answer tokens
including gpt-oss's reasoning, post-answer slots). Reads the exports of the build split only.
Run from the project root: python3 scripts/findings_2026_10_02/gpt_oss_silence.py [model]"""
import sys, json; sys.path.insert(0, 'scripts')
import numpy as np, common as C
from presence_index import read_ids
from frequency_tables import part_positions
model = sys.argv[1] if len(sys.argv) > 1 else 'gpt-oss-20b'
man = C.load_manifest(model); vocab = C.load_vocab(model); layers = man['layers']
LIE = {'lie', 'lies', 'lied', 'lying', 'liar', 'Lie', 'Lies', 'Lying', 'Lied', 'deception', 'deceptive', 'deceive', 'deceit', 'dishonest', 'falsehood', 'fabricated', 'misleading',
       '谎言', '撒谎', '说谎', '谎', '謊', '欺骗', '骗', 'মিথ্যা', '거짓', 'झूठ', 'mentira', '🤥', 'ложь', '嘘'}
SETS = {'lie words': LIE, 'yes / no': {'yes', 'Yes', 'YES', 'no', 'No', 'NO'}}
ids = {k: np.array([i for i, t in enumerate(vocab) if t.strip() in s]) for k, s in SETS.items()}
print(model, 'layers', layers[0], '-', layers[-1], 'band', C.BANDS[model], {k: len(v) for k, v in ids.items()})
ents = [e for e in man['transcripts'] if e['set'] == 'scenario' and e['split'] == 'build']
SEG = ['resp_tok', 'postresp_slot', 'q_tok', 'preans_slot', 'think_slot', 'ans_tok', 'postans_slot']
acc = {(lens, k, seg, lab): [] for lens in ('J', 'LL') for k in SETS for seg in SEG for lab in ('lie', 'truth')}
for e in ents:
    for part in ('prefix', 'Q9_dyl'):
        h, arr = read_ids(model, e, part)
        pm = C.positions({'tokens': h['tokens'], 'segments': h['segments']}) if part == 'prefix' else part_positions(h)
        for seg in SEG:
            ps = [p for n, p in pm.items() if n.startswith(seg)]
            if not ps: continue
            for lens in ('J', 'LL'):
                blk = np.asarray(arr[lens][:, ps])                     # [layers, positions, K]
                for k in SETS:
                    acc[(lens, k, seg, e['label'])].append(np.isin(blk, ids[k]).any(axis=(1, 2)))   # per layer: any position of the segment
show = [l for l in layers if l % max(1, len(layers) // 12) == 0 or l == layers[-1]]
for lens in ('J', 'LL'):
    for k in SETS:
        print(f"\n== {lens}-lens, {k}: % of lies / % of truths with the word at one or more positions of the segment, by layer")
        print('segment        ' + ' '.join(f'{l:>7}' for l in show))
        for seg in SEG:
            a, b = acc[(lens, k, seg, 'lie')], acc[(lens, k, seg, 'truth')]
            if not a: continue
            a, b = np.mean(a, 0), np.mean(b, 0)
            print(f'{seg:14} ' + ' '.join(f"{100 * a[layers.index(l)]:3.0f}/{100 * b[layers.index(l)]:<3.0f}" for l in show))
