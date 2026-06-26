#!/usr/bin/env python3
"""Detect likely person OVER-MERGES, modelled on the John A. Macdonald error
(two different men fused across an edition gap on common surname + initials).

Signals per person (from career_facts events + persons birth/name):
  A SPAN        active career span (last_year - first_year) implausibly long  (>55y)
  B AGE         an event at an implausible age given birth_year (<13 or >80)
  C CONCURRENT  overlapping events in 2+ distinct, far-apart colonies (can't be two places at once)
  D GAP_SWITCH  career splits into time-separated clusters with DISJOINT geography
                (the Macdonald signature: text-chain bridged a gap joining two careers)
Score = weighted sum; rank candidates. Grounded persons flagged (corrupts the WD link).
"""
import os, json, collections

import os
KG = os.environ.get("COL_KG_OUT","data/kg")+"/graph_stage3"

def load():
    persons = {}
    for l in open(f"{KG}/persons.jsonl"):
        d = json.loads(l)
        persons[d["person_id"]] = {
            "sur": d.get("surname"), "giv": d.get("given_names"),
            "birth": d.get("birth_year"), "wqid": d.get("wikidata_qid") or "",
            "wlab": d.get("wikidata_label") or "", "n_att": d.get("n_attestations") or 0}
    ev = collections.defaultdict(list)
    _cf = f"{KG}/career_facts.jsonl"
    _cf = _cf if os.path.exists(_cf) else f"{KG}/career_events.jsonl"
    for l in open(_cf):
        d = json.loads(l)
        col = d.get("colony_qid") or d.get("place_qid")
        ys, ye = d.get("year_start"), d.get("year_end")
        if ys:
            ev[d["person_id"]].append({"col": col, "clabel": d.get("colony_label") or d.get("place_label"),
                                       "ys": ys, "ye": ye or ys})
    return persons, ev

def clusters_of(evs, gap=11):
    """Split dated, placed events into time-separated clusters (gap-year break)."""
    se = sorted([e for e in evs if e["col"]], key=lambda e: e["ys"])
    if not se: return []
    cl, cur = [], [se[0]]
    for prev, e in zip(se, se[1:]):
        if e["ys"] - prev["ye"] > gap:
            cl.append(cur); cur = [e]
        else:
            cur.append(e)
    cl.append(cur)
    return cl

def detect(p, evs):
    """Confident over-merge = a substantial sub-career at PLAUSIBLE age coexisting with a
    substantial sub-career at IMPOSSIBLE age (two men, one of whom the birth year fits).
    This separates true merges (Macdonald, Hofmeyr) from gappy-but-real careers (one age
    band) and from bad birth years (ALL events impossible) and bad dates (lone outlier)."""
    out = {"merge": 0, "conc": 0, "why": [], "cls": "ok"}
    yrs = [e["ys"] for e in evs] + [e["ye"] for e in evs]
    if not yrs: return out

    if p["birth"]:
        cl = clusters_of(evs)
        sub = [c for c in cl if len(c) >= 2]
        def ageband(c):
            ages = [e["ys"] - p["birth"] for e in c] + [e["ye"] - p["birth"] for e in c]
            lo, hi = min(ages), max(ages)
            if lo >= 15 and hi <= 76: return "plausible", lo, hi
            if hi < 13 or lo >= 78:   return "impossible", lo, hi
            return "mixed", lo, hi
        bands = [(ageband(c), c) for c in sub]
        plaus = [(b, c) for b, c in bands if b[0] == "plausible"]
        imposs = [(b, c) for b, c in bands if b[0] == "impossible"]
        if plaus and imposs:
            # MERGE only if the impossible career is in a DIFFERENT place than the plausible
            # one. Same-geography age splits are bad-birth-years (one coherent career), not merges.
            pcols = {e["col"] for _, c in plaus for e in c}
            icols = {e["col"] for _, c in imposs for e in c}
            def desc(b, c):
                return (f"{min(e['ys'] for e in c)}-{max(e['ye'] for e in c)} "
                        f"(age {b[1]}..{b[2]}) {sorted({e['clabel'] for e in c})[:2]}")
            if pcols.isdisjoint(icols):
                out["merge"] = 20 + 5*len(imposs) + max(abs(b[1]) for b, _ in imposs) / 5
                out["cls"] = "OVER_MERGE"
                out["why"] += ["PLAUSIBLE " + desc(*plaus[0]), "IMPOSSIBLE " + desc(*imposs[0])]
            else:
                out["cls"] = "BAD_BIRTH"   # coherent geography, wrong birth year
                out["why"] += ["coherent geography, age-impossible => bad birth year",
                               "PLAUSIBLE " + desc(*plaus[0]), "IMPOSSIBLE " + desc(*imposs[0])]

    # --- CONCURRENT contemporaries: strict overlap (>=3y, explicit spans) in different colonies
    ew = [e for e in evs if e["col"] and e["ye"] > e["ys"]]
    conc = set()
    for i in range(len(ew)):
        for j in range(i+1, len(ew)):
            a, b = ew[i], ew[j]
            if a["col"] != b["col"] and min(a["ye"], b["ye"]) - max(a["ys"], b["ys"]) >= 3:
                conc.add(frozenset((a["clabel"], b["clabel"])))
    if conc:
        out["conc"] = len(conc)
        out["why"].append("concurrent>=3y: " + "; ".join("/".join(sorted(x)) for x in list(conc)[:3]))
        if out["cls"] == "ok": out["cls"] = "CONCURRENT"
    return out

def main():
    persons, ev = load()
    rows = []
    for pid, p in persons.items():
        evs = ev.get(pid, [])
        if len(evs) < 2: continue
        d = detect(p, evs)
        if d["cls"] in ("OVER_MERGE", "CONCURRENT", "BAD_BIRTH"):
            score = d["merge"] + 4*d["conc"]
            rows.append((score, pid, p, d))
    rows.sort(reverse=True, key=lambda x: x[0])
    bycls = collections.Counter(r[3]["cls"] for r in rows)
    print(f"OVER_MERGE: {bycls['OVER_MERGE']}   BAD_BIRTH(coherent career, wrong birth): {bycls['BAD_BIRTH']}"
          f"   CONCURRENT: {bycls['CONCURRENT']}")
    grounded = [r for r in rows if r[2]["wqid"]]
    print(f"  of which grounded to Wikidata: {len(grounded)}\n")
    with open("data/kg/overmerge_candidates.jsonl", "w") as fo:
        for score, pid, p, d in rows:
            fo.write(json.dumps({"person_id": pid, "score": round(score,1), "class": d["cls"],
                "surname": p["sur"], "given": p["giv"], "birth": p["birth"], "n_att": p["n_att"],
                "wikidata_qid": p["wqid"], "wikidata_label": p["wlab"], "why": d["why"]}) + "\n")
    print("TOP 30 OVER_MERGE candidates:")
    shown = 0
    for score, pid, p, d in rows:
        if d["cls"] != "OVER_MERGE": continue
        g = f" [WD:{p['wqid']} {p['wlab']}]" if p["wqid"] else ""
        print(f"  {score:5.0f} {p['sur']},{(p['giv'] or '')[:18]:18} (b{p['birth']},att{p['n_att']}){g}")
        print(f"           {' | '.join(d['why'])}")
        shown += 1
        if shown >= 30: break

if __name__ == "__main__":
    main()
