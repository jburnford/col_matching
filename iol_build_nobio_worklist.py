#!/usr/bin/env python3
"""Render the no-bio unification residue for the Nibi judge
(worker `--mode iolnobio`, NOBIO_DEDUP_KICKOFF step 1 LLM pass).

Reads nobio_unify_residue.jsonl and re-hydrates both sides from the
source layers so the judge sees full context: chains get their office
list, gradation identities their seniority trace, exit events their
raw printed line.

Output: data/iol/identity/adjudicate/wl_nobio.jsonl
Run on Nibi:
  python3 qwen_classc_worker.py --mode iolnobio \
      --worklist wl_nobio.jsonl --out res_nobio.jsonl
"""

from __future__ import annotations

import json
from glob import glob
from pathlib import Path

ROOT = Path("data/iol")
IDD = ROOT / "identity"


def chain_lines(c: dict) -> list[str]:
    y0, y1 = c["years"]
    return [
        f"civil-list office chain: {c['name']} — government: "
        f"{c['government']}",
        f"listed {y0}-{y1} ({c['n_records']} yearly records)",
        "offices held: " + "; ".join(c["offices"]),
    ]


def grad_lines(g: dict) -> list[str]:
    eds = g.get("editions") or []
    out = [
        f"gradation (seniority) trace: {g.get('given') or ''} "
        f"{g['surname']} — {g['list_type']} list",
        f"commission/covenant year {g.get('entry_year')}; printed in "
        f"gradation lists {min(eds)}-{max(eds)}" if eds else
        f"commission/covenant year {g.get('entry_year')}",
    ]
    for label, key in (("sections", "sections"),
                       ("corps", "corps"),
                       ("establishments", "establishments"),
                       ("appointments", "appointments"),
                       ("honours", "honours")):
        if g.get(key):
            out.append(f"{label}: " + "; ".join(str(x) for x in
                                                g[key][:8]))
    return out


def exit_lines(e: dict) -> list[str]:
    date = "/".join(str(x) for x in (e.get("day"), e.get("month"),
                                     e.get("year")) if x)
    out = [
        f"casualty-table exit event: {e['event'].upper()} — "
        f"{e['name']}, {date}"
        + (f", at {e['place']}" if e.get("place") else ""),
        f"printed under: {e.get('presidency') or '?'} / "
        f"{e.get('establishment') or '?'} (edition {e['edition_tag']})",
    ]
    if e.get("raw"):
        out.append("raw line: " + e["raw"][:160])
    return out


_NOTES = {
    "chain_grad": "IDENTITY 1 is a civil-list chain, IDENTITY 2 the "
                  "gradation seniority trace proposed as the same man.",
    "chain_chain": "Two civil-list chains in different governments — "
                   "a transfer or dual listing if the same man.",
    "grad_exit": "Does this exit event close the gradation trace?",
    "chain_exit": "Does this exit event close the civil-list chain?",
}


def main() -> None:
    chains = {c["chain_id"]: c for c in
              (json.loads(l) for l in
               open(IDD / "nobio_civil_chains.jsonl", encoding="utf-8"))}
    grads = {g["gradation_id"]: g for g in
             (json.loads(l) for l in
              open(ROOT / "gradation/gradation_identities.jsonl",
                   encoding="utf-8"))}
    exits = {}
    for f in sorted(glob(str(ROOT / "casualties/casualties_1*.jsonl"))):
        for i, l in enumerate(open(f, encoding="utf-8")):
            e = json.loads(l)
            exits[f"{e['edition_tag']}:{i}"] = e

    def lines_for(ident: str) -> list[str] | None:
        if ident in chains:
            return chain_lines(chains[ident])
        if ident in grads:
            return grad_lines(grads[ident])
        if ident in exits:
            return exit_lines(exits[ident])
        return None

    n, missing = 0, 0
    with open(IDD / "adjudicate/wl_nobio.jsonl", "w",
              encoding="utf-8") as fh:
        for l in open(IDD / "nobio_unify_residue.jsonl",
                      encoding="utf-8"):
            r = json.loads(l)
            a, b = lines_for(r["a"]), lines_for(r["b"])
            if a is None or b is None:
                missing += 1
                continue
            ev = r["evidence"]
            note = _NOTES[r["edge_type"]]
            if ev.get("entry_straddle"):
                note += (" NOTE: the chain starts before the covenant "
                         "year — an uncovenanted start is possible but "
                         "needs supporting evidence.")
            if ev.get("n_key_chains", 0) > 2 or ev.get("n_cands", 0) > 1:
                note += (" NOTE: several same-name candidates exist in "
                         "the corpus — prefer 'unsure' unless the "
                         "evidence is specific.")
            fh.write(json.dumps({
                "id": f"nbu::{r['a']}::{r['b']}",
                "pool": "nobio_unify", "edge_type": r["edge_type"],
                "a_lines": a, "b_lines": b, "note": note,
            }, ensure_ascii=False) + "\n")
            n += 1
    print(f"wl_nobio.jsonl: {n:,} prompts ({missing} sides missing)")


if __name__ == "__main__":
    main()
