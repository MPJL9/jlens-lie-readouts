#!/usr/bin/env python3
"""Experiment 3: the page of pictures, one page per model. Reads numbers.json and fig/*.png of the
model (written by scripts/exp3/pictures.py; analysis/exp3/ for Qwen, analysis/exp3/<slug>/ for the
others) and writes viewer/residual_pictures.html (Qwen) or viewer/residual_pictures_<slug>.html.
The page points at the figure files, so it opens by itself from the viewer folder.

--artifact PATH also writes the page without the document wrapper, with the figures at fig/<name>.png
(they are published next to the page).

Usage: python3 scripts/exp3/page.py [--model gemma-3-12b-it] [--exp3 DIR] [--out PATH] [--artifact PATH]
"""
import argparse
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import common as C  # noqa: E402
from exp3 import pictures as X3  # noqa: E402
from exp3.pictures import SHORT  # noqa: E402

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
"""
# tokens and faces of the other viewer pages (viewer/misses_template.html)
PAGE = """<title>__TITLE__</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* layout: one column; a summary table first, then one section per token position with its pictures stacked */
:root {
  --bg: #F3F5F8; --surface: #FFFFFF; --surface-2: #E9EDF2; --text: #1B2330; --muted: #5E6978;
  --line: #D4DAE3; --accent: #1E6E8C; --accent-soft: #D9EBF2; --fig-bg: #FCFCFB;
  --c-lie: #EB6834; --c-truth: #2A78D6; --c-np: #1BAF7A; --c-un: #A9A79C;
  --sans: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --serif: "Source Serif 4", Georgia, "Times New Roman", serif;
  --mono: "IBM Plex Mono", ui-monospace, Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    color-scheme: dark;
    --bg: #11151A; --surface: #181D24; --surface-2: #222931; --text: #E4E8EE; --muted: #98A2B0;
    --line: #2C343F; --accent: #66B9D5; --accent-soft: #17323D;
  }
}
:root[data-theme="dark"] {
  color-scheme: dark;
  --bg: #11151A; --surface: #181D24; --surface-2: #222931; --text: #E4E8EE; --muted: #98A2B0;
  --line: #2C343F; --accent: #66B9D5; --accent-soft: #17323D;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--text); font: 15px/1.55 var(--sans); }
.wrap { max-width: 1240px; margin: 0 auto; padding-block: 28px 64px; padding-inline: clamp(16px, 3vw, 36px);
        display: flex; flex-direction: column; gap: 28px; }
h1 { font: 600 30px/1.15 var(--serif); margin: 0; text-wrap: balance; }
h2 { font: 600 21px/1.25 var(--serif); margin: 0; text-wrap: balance; }
h3 { font: 600 13px/1.3 var(--sans); letter-spacing: .06em; text-transform: uppercase; color: var(--muted); margin: 0; }
p { margin: 0; max-width: 72ch; }
code { font: 13px var(--mono); background: var(--surface-2); padding: 1px 5px; border-radius: 4px; }
a { color: var(--accent); }
a:focus-visible, summary:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.lede { color: var(--muted); }
.status { font-size: 13px; color: var(--muted); border-left: 3px solid var(--accent); padding-left: 12px; }
.block { display: flex; flex-direction: column; gap: 12px; }
.read { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px 32px; }
.read > div { min-width: 0; }
.read dt { font-weight: 600; }
.read dd { margin: 2px 0 0; color: var(--muted); font-size: 14px; }
.key { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 6px; }
.scroll { overflow-x: auto; }
table { border-collapse: collapse; font-size: 13.5px; font-variant-numeric: tabular-nums; width: 100%; }
th, td { text-align: left; padding: 6px 12px 6px 0; border-bottom: 1px solid var(--line); vertical-align: top; white-space: nowrap; }
th { font-weight: 600; color: var(--muted); font-size: 12.5px; }
td:first-child, th:first-child { white-space: normal; min-width: 190px; }
tr.gap td { border-bottom: 2px solid var(--line); }
.nav { display: flex; flex-wrap: wrap; gap: 6px 8px; font-size: 13px; }
.nav a { text-decoration: none; padding: 3px 10px; border: 1px solid var(--line); border-radius: 999px; background: var(--surface); color: var(--text); }
.nav a:hover { border-color: var(--accent); }
section.pos { display: flex; flex-direction: column; gap: 16px; border-top: 1px solid var(--line); padding-top: 24px; }
.where { color: var(--muted); font-size: 14px; }
figure { margin: 0; display: flex; flex-direction: column; gap: 6px; }
figure .scroll { background: var(--fig-bg); border: 1px solid var(--line); border-radius: 6px; }
figure img { display: block; width: 100%; height: auto; }
figure.wide img { min-width: 900px; }
figure.small { max-width: 620px; }
figcaption { font-size: 13.5px; color: var(--muted); max-width: 80ch; }
figcaption b { color: var(--text); font-weight: 600; }
details { border: 1px solid var(--line); border-radius: 6px; background: var(--surface); padding: 8px 14px; }
summary { cursor: pointer; font-weight: 500; font-size: 14px; }
details .scroll { margin-top: 8px; }
</style>
"""


def esc(s):
    return html.escape(str(s))


def code(s):
    """`x` -> <code>x</code> in an escaped string."""
    parts = esc(s).split("`")
    return "".join(p if i % 2 == 0 else f"<code>{p}</code>" for i, p in enumerate(parts))


def f2(v):
    return "–" if v is None else f"{v:.2f}"


def spread(vals):
    vals = [v for v in vals if v is not None]
    return "–" if not vals else f"{sum(vals) / len(vals):.2f} ({min(vals):.2f} to {max(vals):.2f})"


def figure(src, alt, caption, cls, link):
    img = f'<img src="{esc(src)}" alt="{esc(alt)}" loading="lazy">'
    if link:
        img = f'<a href="{esc(src)}">{img}</a>'
    return f'<figure class="{cls}"><div class="scroll">{img}</div><figcaption>{caption}</figcaption></figure>'


def title(res):
    return "Residual Stream Pictures" if res["model"] == X3.QWEN else res["name"].replace("Gemma-3", "Gemma") + " Residual Pictures"


def build(res, fig, link, have):
    BEFORE, AFTER = X3.BEFORE, X3.AFTER
    dl, layers = str(res["draw_layer"]), res["layers"]
    c = res["counts"]
    fams = res["families"]
    qwen = res["model"] == X3.QWEN
    o = ['<div class="wrap">',
         f'<header class="block"><h1>{title(res)}</h1>',
         f'<p class="lede">{res["name"]}. Where lies and truths sit in the residual stream (the model\'s internal vector at one '
         f'token and one layer) at eight chat-template tokens. Pictures at layer {dl}; numbers at layers '
         f'{", ".join(str(l) for l in layers)}.</p>',
         f'<p class="status">Build split only, in-sample. The held-out split has not been read. '
         f'{c["lie"]} lies and {c["truth"]} truths told under pressure to lie, {c["no-pressure truth"]} truths with no pressure, '
         f'{c["unrelated chat"]} unrelated chats.'
         + (' Before every fit, each dimension of the residual stream is divided by its spread (standard deviation) in the unrelated '
            'chats at the same token and layer. Without this, one or two dimensions with values hundreds of times larger than the '
            'rest drive every picture of this model.' if res.get("scale") else '') + '</p></header>',
         '<section class="block"><h3>How to read the pictures</h3><dl class="read">',
         '<div><dt>Points</dt><dd><span class="key" style="background:var(--c-lie)"></span>lie '
         '<span class="key" style="background:var(--c-truth);margin-left:8px"></span>truth '
         '<span class="key" style="background:var(--c-np);margin-left:8px"></span>no-pressure truth '
         '<span class="key" style="background:var(--c-un);margin-left:8px"></span>unrelated chat. One point is one transcript.</dd></div>',
         '<div><dt>Axes</dt><dd>PCA (principal component analysis) finds the directions along which a set of vectors varies most. '
         'Each picture plots the first two. One unit has the same length on both axes.</dd></div>',
         '<div><dt>Two fits</dt><dd>The axes are fitted either on the unrelated chats or on the pressured transcripts (lies and truths). '
         'All other points are then placed on those axes.</dd></div>',
         '<div><dt>The number</dt><dd>AUROC: the chance that a random lie scores higher than a random truth. 0.50 is chance. '
         'Here the score comes from a straight line drawn through the picture. The line is fitted on some scenarios and scored on the others.</dd></div>',
         '<div><dt>Pairs</dt><dd>Some scenarios have both a lie and a truth from the same prompt. '
         '"Pairs" counts how often the lie scores above its own truth, so the prompt cannot explain the result.</dd></div>',
         (f'<div><dt>The eight families</dt><dd>Eight word families about lying that the J-lens readout holds at the newline after the response '
          f'({", ".join(fams)}). {res["misses"]} lies have none of them: the missed lies, ringed. Truths that hold one or more (the flagged truths) are boxed.</dd></div>' if qwen else
          f'<div><dt>The lie families</dt><dd>The {len(fams)} word families that lean to lies in this model\'s J-lens readout at the newline after the '
          f'response ({", ".join(fams)}). {res["misses"]} lies have none of them: the missed lies, ringed. Truths that hold one or more (the flagged truths) are boxed.</dd></div>'),
         '<div><dt>Deniers</dt><dd>After the self-report question, the model admits some lies. "Among deniers" keeps only transcripts that answer No, '
         'and is given where 10 or more lies and 10 or more truths deny. Circles deny, triangles admit.</dd></div>',
         '<div><dt>UMAP</dt><dd>A second way to draw the points that keeps near neighbours near. Distances between far groups are not reliable. '
         'It is drawn as a check for the pressured fit only.</dd></div>',
         '</dl></section>']

    # summary table
    o += ['<section class="block"><h3>Summary at layer ' + dl + '</h3>',
          '<p class="where">AUROC of lies against truths. Positions after the question show the mean over the five wordings, with the lowest and highest in brackets.</p>',
          '<div class="scroll"><table><thead><tr><th>Token position</th><th>Line, unrelated fit</th><th>Line, pressured fit</th>'
          '<th>Line among deniers, pressured fit</th><th>Direction, full space</th><th>Pairs (direction)</th></tr></thead><tbody>']
    for i, name in enumerate(BEFORE):
        r = res["before"][name][dl]
        p = r["D"]["pairs"]
        o.append(f'<tr{" class=gap" if i == len(BEFORE) - 1 else ""}><td><a href="#{name}">{code(BEFORE[name])}</a></td><td>{f2(r["U"]["auroc"])}</td>'
                 f'<td>{f2(r["P"]["auroc"])}</td><td>–</td><td>{f2(r["D"]["auroc"])}</td>'
                 f'<td>{p[0]} of {p[2]}{f" ({p[1]} ties)" if p[1] else ""}</td></tr>')
    for name in AFTER:
        r = res["after"][name][dl]
        o.append(f'<tr><td><a href="#{name}">{code(AFTER[name])}</a></td><td>{spread([r["U"][w]["all"]["auroc"] for w in C.WORDINGS])}</td>'
                 f'<td>{spread([r["P"][w]["all"]["auroc"] for w in C.WORDINGS])}</td>'
                 f'<td>{spread([r["P"][w]["deniers"]["auroc"] if r["P"][w]["deniers"] else None for w in C.WORDINGS])}</td>'
                 f'<td>{spread([r["topk"][w]["full"]["all"] for w in C.WORDINGS])}</td><td>–</td></tr>')
    o += ['</tbody></table></div></section>']
    allk = sorted({k for n in BEFORE for k in res["before"][n][dl]["topk"]["ks"]} | {k for n in AFTER for k in res["after"][n][dl]["topk"]["ks"]})
    row = lambda t, vals: "".join(f'<td>{f2(dict(zip(t["ks"], vals)).get(k))}</td>' for k in allk)
    rows = ""
    for name in BEFORE:
        t = res["before"][name][dl]["topk"]
        rows += f'<tr><td>{code(BEFORE[name])}</td>{row(t, t["auroc"])}<td>{f2(res["before"][name][dl]["D"]["auroc"])}</td></tr>'
    for name in AFTER:
        t = res["after"][name][dl]["topk"]
        mean = [sum(v) / len(v) for v in zip(*[t[w]["all"] for w in C.WORDINGS])]
        rows += (f'<tr><td>{code(AFTER[name])}</td>{row(t, mean)}'
                 f'<td>{f2(sum(t[w]["full"]["all"] for w in C.WORDINGS) / len(C.WORDINGS))}</td></tr>')
    o += ['<section class="block" id="more-components"><h3>More components of the unrelated chats</h3>',
          '<p class="where">The pictures on the unrelated fit show two axes. Here the direction from the mean of truths to the mean of lies is fitted '
          'within the first k principal components of the unrelated chats, and scored on scenarios it was not fitted on. '
          'The grey line is the same direction with no restriction.</p>',
          figure(f"{fig}topk.png", "AUROC against the number of principal components of the unrelated chats, one panel per token position",
                 "<b>How many components of ordinary variation it takes.</b> After the question the lines are the mean of the five wordings.", "wide", link),
          '<details><summary>The numbers (AUROC, all lies and truths)</summary><div class="scroll"><table><thead><tr><th>Token position</th>' +
          "".join(f'<th>k = {k}</th>' for k in allk) + f'<th>Full space</th></tr></thead><tbody>{rows}</tbody></table></div></details></section>',
          '<nav class="nav" aria-label="Token positions">' +
          "".join(f'<a href="#{n}">{code(d)}</a>' for n, d in list(BEFORE.items()) + list(AFTER.items())) + '</nav>']

    # before the question
    for name, desc in BEFORE.items():
        r = res["before"][name][dl]
        o += [f'<section class="pos" id="{name}"><div class="block"><h2>{code(desc[0].upper() + desc[1:])}</h2>',
              f'<p class="where"><code>{name}</code> · before the self-report question exists</p></div>']
        caps = {
            "U": f'<b>Axes fitted on the unrelated chats.</b> Line AUROC {f2(r["U"]["auroc"])}.',
            "P": f'<b>Axes fitted on the pressured transcripts.</b> Line AUROC {f2(r["P"]["auroc"])}.',
            "U_more": "<b>More components of the unrelated chats:</b> PC1 against PC2, PC2 against PC3, PC3 against PC4. "
                      "Each panel title gives its own line AUROC.",
            "direction": '<b>One supervised direction.</b> Horizontal: the score on the direction from the mean of truths to the mean of lies, '
                         'in the full space. Each lie and truth is scored by a direction fitted without its scenario. Vertical: the first principal '
                         f'component of what is left. AUROC {f2(r["D"]["auroc"])}; {r["D"]["misses_truth_side"][0]} of {r["D"]["misses_truth_side"][1]} '
                         'missed lies fall on the truth side.',
            "umap": "<b>Check: UMAP of the pressured transcripts.</b> Line AUROC for three seeds: " +
                    ", ".join(f2(v) for v in r.get("umap", [])) + ". Seed 0 is drawn."}
        for kind in ("U", "U_more", "P", "direction", "umap"):
            if have(f"{name}_{kind}.png"):
                o.append(figure(f"{fig}{name}_{kind}.png", f"{desc}: {kind} picture", caps[kind], "wide", link))
        rows = "".join(
            f'<tr><td>{lab}</td>' + "".join(f'<td>{f2(res["before"][name][str(l)][k]["auroc"])}</td>' for l in layers) + '</tr>'
            for k, lab in (("U", "Line, unrelated fit"), ("P", "Line, pressured fit"), ("D", "Direction, full space")))
        o.append('<details><summary>AUROC by layer</summary><div class="scroll"><table><thead><tr><th>Measure</th>' +
                 "".join(f'<th>Layer {l}</th>' for l in layers) + f'</tr></thead><tbody>{rows}</tbody></table></div></details></section>')

    # after the question
    for name, desc in AFTER.items():
        r = res["after"][name][dl]
        o += [f'<section class="pos" id="{name}"><div class="block"><h2>{code(desc[0].upper() + desc[1:])}</h2>',
              f'<p class="where"><code>{name}</code> · after the self-report question · five wordings pooled, each wording\'s mean subtracted</p></div>']
        caps = {"U": "<b>Axes fitted on the unrelated chats.</b> One panel per wording, shared axes. Each panel title gives the line AUROC among all and among deniers.",
                "U_more": "<b>More components of the unrelated chats:</b> one row each for PC1 against PC2, PC2 against PC3 and PC3 against PC4; "
                          "one column per wording. Each panel title gives its line AUROC among all lies and truths.",
                "P": "<b>Axes fitted on the pressured transcripts.</b> One panel per wording, shared axes.",
                "raw": "<b>The raw pooled fit, coloured by wording.</b> No mean is subtracted here. Where the five wordings form five separate groups, "
                       "the first axes of a raw fit show the wording and not the transcript. That is why each wording's mean is subtracted in the pictures above.",
                "umap": "<b>Check: UMAP of the pressured transcripts.</b> Seed 0 is drawn; the table below has three seeds."}
        for kind, cls in (("U", "wide"), ("U_more", "wide"), ("P", "wide"), ("umap", "wide"), ("raw", "small")):
            if have(f"{name}_{kind}.png"):
                o.append(figure(f"{fig}{name}_{kind}.png", f"{desc}: {kind} picture", caps[kind], cls, link))
        cell = lambda x: "–" if x is None else f'{x["auroc"]:.2f} <span class="where">({x["n"][0]} / {x["n"][1]})</span>'
        rows = ""
        for w in C.WORDINGS:
            u = r.get("umap", {}).get(w, {}).get("all", [])
            rows += (f'<tr><td>{SHORT[w]}</td><td>{cell(r["U"][w]["all"])}</td><td>{cell(r["U"][w]["deniers"])}</td>'
                     f'<td>{cell(r["P"][w]["all"])}</td><td>{cell(r["P"][w]["deniers"])}</td><td>{", ".join(f2(v) for v in u) or "–"}</td></tr>')
        o.append(f'<div class="scroll"><table><thead><tr><th>Wording (lies / truths)</th><th>Unrelated fit, all</th><th>Unrelated fit, deniers</th>'
                 f'<th>Pressured fit, all</th><th>Pressured fit, deniers</th><th>UMAP check, all</th></tr></thead><tbody>{rows}</tbody></table></div>')
        rows = ""
        for w in C.WORDINGS:
            for fit, lab in (("U", "unrelated"), ("P", "pressured")):
                rows += f'<tr><td>{SHORT[w]}, {lab} fit</td>' + "".join(
                    f'<td>{f2(res["after"][name][str(l)][fit][w]["all"]["auroc"])} · '
                    f'{f2(res["after"][name][str(l)][fit][w]["deniers"]["auroc"] if res["after"][name][str(l)][fit][w]["deniers"] else None)}</td>'
                    for l in layers) + '</tr>'
        o.append('<details><summary>Line AUROC by layer (all · deniers)</summary><div class="scroll"><table><thead><tr><th>Wording and fit</th>' +
                 "".join(f'<th>Layer {l}</th>' for l in layers) + f'</tr></thead><tbody>{rows}</tbody></table></div></details></section>')
    o.append('</div>')
    return "\n".join(o)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--model", default=X3.QWEN, choices=list(X3.MODELS))
    ap.add_argument("--exp3", help="default: the model's folder under analysis/exp3")
    ap.add_argument("--out", help="default: viewer/residual_pictures.html (Qwen) or viewer/residual_pictures_<slug>.html")
    ap.add_argument("--artifact", help="also write the page without the document wrapper to this path")
    args = ap.parse_args()
    X3.configure(args.model)
    args.exp3 = args.exp3 or X3.out_dir(args.model)
    args.out = args.out or os.path.join(C.ROOT, "viewer", "residual_pictures.html" if args.model == X3.QWEN
                                        else f"residual_pictures_{C.slug(args.model)}.html")
    with open(os.path.join(args.exp3, "numbers.json")) as f:
        res = json.load(f)
    fig_dir = os.path.join(args.exp3, "fig")
    have = lambda name: os.path.exists(os.path.join(fig_dir, name))
    rel = os.path.relpath(fig_dir, os.path.dirname(os.path.abspath(args.out))) + "/"
    page = PAGE.replace("__TITLE__", title(res))
    with open(args.out, "w") as f:
        f.write(HEAD + page + "</head>\n<body>\n" + build(res, rel, True, have) + "\n</body>\n</html>\n")
    print("written:", args.out)
    if args.artifact:
        with open(args.artifact, "w") as f:
            f.write(page + build(res, "fig/", False, have) + "\n")
        print("written:", args.artifact)


if __name__ == "__main__":
    main()
