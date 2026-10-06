#!/usr/bin/env python3
"""A page like viewer/response_readouts.html for the truths that the newline flags (user, 2026-10-03):
every truth of the build split, told under pressure or with no pressure, whose J-lens readout at
post-response slot 1 holds one or more of the eight families. The eight are the families that meet the
main rule at that position (present after at least 40% of lies and after at most 10% of truths, of
no-pressure truths and of unrelated chats); falsehood, fabricate and false also meet the strict rule
(50% / 5%) and get an asterisk on the page. Within each group the transcripts with the most families
come first.

Reuses scripts/pilot/pilot_page.py (data layout and encoding) and viewer/response_readouts_template.html,
with the title, the intro, the group headings and the opening selection (the newline, not a response
token; its readout scrolled to the band) replaced. Each replaced piece must occur exactly once in the template.

Writes viewer/false_alarms.html and, with --artifact PATH, the same page without the document wrapper.
Run from the project root after scripts/pilot/response_counts.py and scripts/pilot/where_words_sit.py:
python3 scripts/pilot/false_alarms_page.py [--artifact PATH]
"""
from __future__ import annotations

import json
import os
import pickle
import re
import sys
import tempfile
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pilot_page as PP  # noqa: E402
from pilot_page import C, P  # noqa: E402

STRICT = ["falsehood", "fabricate", "false"]
GROUPS = [("truth", "truths", "truth under pressure", "Truths told under pressure"),
          ("np_truth", "np", "no-pressure truth", "Truths with no pressure")]
TITLE = "Newline False Alarms"


def select(marks):
    """(chosen, families at the newline per transcript, family lists, {group: (flagged, all)})."""
    d = P.load(PP.M, "J")
    hv = P.have_mask(d, "prefix", "postresp_slot1")
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        ents = json.load(f)["entries"]
    fam = defaultdict(set)
    for e in ents:
        if e["model"] == PP.M and e["lens"] == "J" and e["part"] == "prefix" and e["position"] == "postresp_slot1" and e["status"] == "keep":
            fam[e["name"]] |= {x["id"] for x in e["members"]}
    present = {n: P.present_mask(d, "prefix", "postresp_slot1", fam[n]) & hv for n in PP.EIGHT}
    cnt = sum(present[n].astype(int) for n in PP.EIGHT)
    tid_of = {t["tid"]: i for i, t in enumerate(d["transcripts"])}
    chosen, totals = [], {}
    for cls, group, role, _ in GROUPS:
        ms = [m for m in marks if m["cls"] == cls and cnt[tid_of[m["tid"]]] >= 1]
        ms.sort(key=lambda m: (-cnt[tid_of[m["tid"]]], m["tid"]))
        chosen += [(m, role, group) for m in ms]
        totals[group] = (len(ms), int(((d["cls"] == cls) & hv).sum()))
    eight = {m["tid"]: [n for n in PP.EIGHT if present[n][tid_of[m["tid"]]]] for m, _, _ in chosen}
    return chosen, eight, {n: sorted(v) for n, v in fam.items()}, totals


def template(totals):
    """The response-readouts template with this page's title, intro, groups and opening selection."""
    with open(PP.TEMPLATE) as f:
        html = f.read()

    def rep(old, new):
        nonlocal html
        assert html.count(old) == 1, (html.count(old), old)
        html = html.replace(old, new)

    rep("<title>Readouts Inside the Response</title>", f"<title>{TITLE}</title>")
    rep("<h1>Readouts Inside the Response</h1>", f"<h1>{TITLE}</h1>")
    (a, b), (c, d) = totals["truths"], totals["np"]
    rep("`Qwen3.6-27B, J-lens, band ${D.band[0]}–${D.band[1]}. Each response token",
        "`Qwen3.6-27B, J-lens, band ${D.band[0]}–${D.band[1]}. <b>The truths that the newline flags.</b> These are all truths of the build split "
        "whose readout at the newline right after the response holds one or more of the eight lie families: "
        f"{a} of {b} truths told under pressure and {c} of {d} truths with no pressure. "
        "The eight (lie, fake, falsehood, misinformation, deceive, fabricate, false, mislead) are the families that meet the main rule at that newline: "
        "present after at least 40% of lies, and after at most 10% of truths, of no-pressure truths and of unrelated chats. "
        "An asterisk marks the three that also meet the strict rule (50% and 5%): falsehood, fabricate, false. "
        "Each transcript opens on that newline, the chip ⏎ right after the response. In its readout the eight's words are red, and false / falsehood pink "
        "(red also covers conceal and dishonest, which are outside the eight). Each response token")
    groups = ", ".join(f'{g}: "{title}"' for _, g, _, title in GROUPS)
    notes = ", ".join(f'{g}: "{totals[g][0]} of {totals[g][1]} hold one or more of the eight at the newline; the ones with the most families first"'
                      for _, g, _, _ in GROUPS)
    block = re.compile(r"  const GROUPS = \{.*?\n  let lastGroup = null;", re.S)
    assert len(block.findall(html)) == 1
    html = block.sub(lambda _: f"  const GROUPS = {{ {groups} }};\n  const GNOTE = {{ {notes} }};\n"
                               f"  const STRICT = new Set({json.dumps(STRICT)});\n  let lastGroup = null;", html)
    rep('tr.eight_at_newline.map(n => `<span class="chip ten">${n}</span>`)',
        'tr.eight_at_newline.map(n => `<span class="chip ten">${n}${STRICT.has(n) ? "*" : ""}</span>`)')
    rep('<b>${tr.eight_at_newline.length ? tr.eight_at_newline.join(", ") : "none of the eight"}</b>',
        '<b>${tr.eight_at_newline.length ? tr.eight_at_newline.map(n => n + (STRICT.has(n) ? "*" : "")).join(", ") : "none of the eight"}</b>')
    rep('      const first = tr.strength_ten.findIndex(s => s >= 8);\n'
        '      state.sel = first >= 0 ? { kind: "tok", i: first } : { kind: "slot", s: "postresp_slot1" };',
        '      state.sel = { kind: "slot", s: "postresp_slot1" };')
    panel = '    document.getElementById("panel").innerHTML = `<div class="what">${what}</div><div class="gridwrap">${h}</div>`;'
    rep(panel, panel + '\n    if (sel.kind === "slot") {   // the readout of a template token opens at the band, not at layer 0\n'
        '      const gw = document.querySelector("#panel .gridwrap"), b = gw.querySelector("tr.band-start");\n'
        '      if (b) gw.scrollTop = b.offsetTop - 28;\n    }')
    return html


def main():
    with open(os.path.join(C.ROOT, "analysis", "pilot", "marks.pkl"), "rb") as f:
        marks = pickle.load(f)["marks"]
    chosen, eight, fam, totals = select(marks)
    for _, group, _, title in GROUPS:
        print(f"{title}: {totals[group][0]} of {totals[group][1]} with one or more of the eight at the newline")
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(template(totals))
    PP.TEMPLATE, PP.OUT_HTML = f.name, os.path.join(PP.VIEWER, "false_alarms.html")
    PP.choose = lambda marks, names: (chosen, eight, fam)
    try:
        PP.main()
    finally:
        os.unlink(f.name)
    for m, role, _ in chosen:
        print(f"  {role:22s} {m['item_id'][-6:]} {m['n']:4d} tokens  {', '.join(eight[m['tid']])}")


if __name__ == "__main__":
    main()
