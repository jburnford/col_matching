#!/usr/bin/env python3
"""Emit the canonical no-bio person table (NOBIO_DEDUP_KICKOFF step 4).

Union-find over the identity edges from iol_nobio_unify.py:
  deterministic tiers        always unioned (det_strong, det_std)
  judged residue (res_nobio) verdict "same" with confidence >= SAME_CONF
Exit edges (grad_exit / chain_exit, det or judged-same) attach casualty
events to the component instead of merging identities.

A/B/C verdicts (res_abc) resolve each identity against the bio table
the COL way (volume_merge_classc.py):
  matched      any candidate judged "same"  -> the linker missed a bio
               person; the whole component carries bio_match and is
               EXCLUDED from the no-bio count (candidate links go to
               nobio_bio_link_candidates.jsonl for the 0-FP review)
  never_biod   every candidate judged "different"
  unsure       otherwise

Without result files this runs PROVISIONAL (deterministic edges only,
class C unresolved) — rerun after fetching res_* from Nibi.

Outputs (data/iol/identity/):
  nobio_persons.jsonl              one row per component: members,
                                   provenance, exits, resolution
  nobio_bio_link_candidates.jsonl  judged "same" abc pairs
  NOBIO_PERSONS.md                 report
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("data/iol")
IDD = ROOT / "identity"
SAME_CONF = 70


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in open(path, encoding="utf-8")]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--adjudicate-dir", default=str(IDD / "adjudicate"),
                    help="where res_nobio/res_abc live (mock tests)")
    args = ap.parse_args()
    adj = Path(args.adjudicate_dir)

    chains = {c["chain_id"]: c for c in
              load_jsonl(IDD / "nobio_civil_chains.jsonl")}
    linked = {r["gradation_id"] for r in
              load_jsonl(ROOT / "gradation/gradation_person_links.jsonl")}
    grads = {g["gradation_id"]: g for g in
             load_jsonl(ROOT / "gradation/gradation_identities.jsonl")
             if g["gradation_id"] not in linked}

    det = load_jsonl(IDD / "nobio_unify_edges.jsonl")
    res_nobio = [r for r in load_jsonl(adj / "res_nobio.jsonl")
                 if "error" not in r]
    res_abc = [r for r in load_jsonl(adj / "res_abc.jsonl")
               if "error" not in r]
    provisional = not res_nobio and not res_abc

    def judged_same(r: dict) -> bool:
        return r.get("verdict") == "same" and \
            (r.get("confidence") or 0) >= SAME_CONF

    # ---- collect identity edges + exit attachments ---------------
    id_edges, exit_edges = [], []
    for e in det:
        if e["edge_type"] in ("chain_grad", "chain_chain"):
            id_edges.append((e["a"], e["b"], e["tier"]))
        else:
            exit_edges.append((e["a"], e["b"], e["tier"]))
    n_judged_id = n_judged_exit = 0
    for r in res_nobio:
        if not judged_same(r):
            continue
        _, a, b = r["id"].split("::")
        if r.get("edge_type") in ("chain_grad", "chain_chain"):
            id_edges.append((a, b, "judged"))
            n_judged_id += 1
        else:
            exit_edges.append((a, b, "judged"))
            n_judged_exit += 1

    # ---- resolutions per identity --------------------------------
    # class A/B are never-bio'd BY CONSTRUCTION; U is a weak-name
    # floor; only class C waits on the judge.
    resolution, bio_match = {}, {}
    for c in load_jsonl(IDD / "nobio_classes.jsonl"):
        if c["cls"] in ("A", "B"):
            resolution[c["id"]] = "never_biod"
        elif c["cls"] == "U":
            resolution[c["id"]] = "weak_name"
    abc = defaultdict(list)
    for r in res_abc:
        abc[r["career_id"]].append(r)
    link_cands = []
    for ident, rs in abc.items():
        sames = sorted((r for r in rs if judged_same(r)),
                       key=lambda r: -(r.get("confidence") or 0))
        if sames:
            resolution[ident] = "matched"
            bio_match[ident] = sames[0]["person_id"]
            link_cands.extend(sames)
        elif all(r.get("verdict") == "different" for r in rs):
            resolution[ident] = "never_biod"
        else:
            resolution[ident] = "unsure"

    # ---- union-find ----------------------------------------------
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for x in list(chains) + list(grads):
        parent.setdefault(x, x)
    for a, b, _ in id_edges:
        if a in parent and b in parent:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

    comps = defaultdict(list)
    for x in list(chains) + list(grads):
        comps[find(x)].append(x)

    exits_by_root = defaultdict(list)
    for ident, ev_id, tier in exit_edges:
        if ident in parent:
            exits_by_root[find(ident)].append((ev_id, tier))

    # ---- emit ----------------------------------------------------
    def best_name(members: list[str]) -> str:
        names = [chains[m]["name"] for m in members if m in chains]
        names += [f"{grads[m].get('given') or ''} "
                  f"{grads[m]['surname']}".strip()
                  for m in members if m in grads]
        return max(names, key=len) if names else ""

    rows, res_count = [], Counter()
    for root, members in sorted(comps.items()):
        members = sorted(members)
        years = []
        for m in members:
            if m in chains:
                years += chains[m]["years"]
            elif grads[m].get("editions"):
                years += [min(grads[m]["editions"]),
                          max(grads[m]["editions"])]
        mres = {resolution.get(m) for m in members} - {None}
        res = ("matched" if "matched" in mres
               else "unsure" if "unsure" in mres
               else "unjudged" if None in
               {resolution.get(m) for m in members}   # provisional C
               else "never_biod" if "never_biod" in mres
               else "weak_name")
        res_count[res] += 1
        matches = sorted({bio_match[m] for m in members
                          if m in bio_match})
        rows.append({
            "nobio_id": "nbp::" + re.sub(r"^(nbc|grd)_", "", members[0]),
            "members": members,
            "populations": sorted({"civil_chain" if m in chains
                                   else "gradation" for m in members}),
            "name": best_name(members),
            "governments": sorted({chains[m]["government"]
                                   for m in members if m in chains}),
            "entry_years": sorted({grads[m]["entry_year"]
                                   for m in members if m in grads
                                   and grads[m].get("entry_year")}),
            "years": [min(years), max(years)] if years else None,
            "n_civil_records": sum(chains[m]["n_records"]
                                   for m in members if m in chains),
            "exit_events": [{"event_id": ev, "tier": t}
                            for ev, t in
                            sorted(exits_by_root.get(root, []))],
            "resolution": res,
            "bio_match": matches[0] if matches else None,
            "bio_match_conflict": matches if len(matches) > 1 else None,
        })

    with open(IDD / "nobio_persons.jsonl", "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(IDD / "nobio_bio_link_candidates.jsonl", "w",
              encoding="utf-8") as fh:
        for r in sorted(link_cands,
                        key=lambda r: -(r.get("confidence") or 0)):
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    n_ident = len(chains) + len(grads)
    nobio_total = len(rows) - res_count["matched"]
    conflicts = sum(1 for r in rows if r["bio_match_conflict"])
    banner = ("**PROVISIONAL — deterministic edges only; rerun after "
              "fetching res_nobio/res_abc from Nibi.**"
              if provisional else "")
    lines = [l for l in [
        "# Canonical no-bio person table", "", banner, "",
        f"- identities in: {n_ident:,} ({len(chains):,} chains + "
        f"{len(grads):,} gradation)",
        f"- identity edges: {len(id_edges):,} "
        f"(det {len(id_edges) - n_judged_id:,}, judged-same "
        f"{n_judged_id:,}) -> **{len(rows):,} components**",
        f"- exit events attached: "
        f"{sum(len(v) for v in exits_by_root.values()):,} "
        f"(judged-same {n_judged_exit:,})",
        f"- resolutions: " + ", ".join(
            f"{k} {res_count[k]:,}" for k in
            ("matched", "never_biod", "unsure", "weak_name",
             "unjudged")),
        f"- bio-link candidates (review before linking): "
        f"{len(link_cands):,}; components matching >1 person: "
        f"{conflicts}",
        f"- **no-bio persons (excl. matched): {nobio_total:,}**",
    ] if l != ""]
    (IDD / "NOBIO_PERSONS.md").write_text("\n".join(lines) + "\n",
                                          encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
