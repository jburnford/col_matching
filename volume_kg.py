#!/usr/bin/env python3
"""Assemble the context knowledge graph from the extracted layers.

Joins the extraction outputs into node/edge files under data/volume/kg/, and
PERSON-MATCHES the governor and honour records to the roster-career /
bio graph (surname + initials-compatibility + colony/time constraints,
ambiguity -> unmatched, mirroring the matcher's 0-FP discipline).

  colony_nodes.jsonl    canonical colonies, active edition span, record mass
  colony_year.jsonl     statistical panel pivoted per (colony, year)
  governed_edges.jsonl  governorship -> colony, with matched career/bio ids
  status_events.jsonl   constitutional descriptor transitions
  honour_events.jsonl   award events, with matched career/bio ids
  co_appointments.jsonl London CO successions + establishment records
  KG.md                 assembly + match-rate report

Re-run after any layer refresh (cheap, pure join).
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from col_match.services.match import _initials, _names_compatible

ROOT = Path("data/volume")
CTX = ROOT / "context"
KG = ROOT / "kg"


def _load(p: Path) -> list[dict]:
    return [json.loads(l) for l in open(p, encoding="utf-8")] if p.exists() else []


def main() -> None:
    KG.mkdir(parents=True, exist_ok=True)
    careers = [c for c in _load(ROOT / "careers/careers.jsonl") if not c["suspect"]]

    # ---- career index for person matching
    by_key = defaultdict(list)              # (colony, surname_lower) -> careers
    by_surname = defaultdict(list)
    for c in careers:
        by_key[(c["colony"], c["surname"])].append(c)
        by_surname[c["surname"]].append(c)

    def match_career(colony: str | None, surname: str, given: str | None,
                     year: int | None, window: int = 3) -> dict | None:
        """Unique career for (colony?, surname, given, ~year) or None."""
        pool = by_key.get((colony, surname.lower()), []) if colony \
            else by_surname.get(surname.lower(), [])
        cands = [c for c in pool if _names_compatible(given, c["given_names"])]
        if year:
            timed = [c for c in cands
                     if c["years"][0] - window <= year <= c["years"][-1] + window]
            cands = timed or cands
        if not cands:
            return None
        if len(cands) > 1:
            # distinct persons? if all initials-compatible with each other,
            # they may be fragments of one person — still ambiguous, drop
            return None
        c = cands[0]
        return {"career_id": c["career_id"], "bio_ids": c["bio_ids"]}

    report = ["# Context knowledge graph assembly", ""]

    # ---- colony nodes
    spans = defaultdict(lambda: [9999, 0, 0])
    for c in careers:
        s = spans[c["colony"]]
        s[0] = min(s[0], c["years"][0])
        s[1] = max(s[1], c["years"][-1])
        s[2] += len(c["records"])
    with (KG / "colony_nodes.jsonl").open("w", encoding="utf-8") as fh:
        for col, (y0, y1, n) in sorted(spans.items()):
            fh.write(json.dumps({"colony": col, "first_year": y0,
                                 "last_year": y1, "roster_records": n}) + "\n")
    report.append(f"- colony nodes: {len(spans)}")

    # ---- colony-year metrics (pivot the panel)
    panel = defaultdict(dict)
    if (CTX / "colony_year_panel.csv").exists():
        import csv
        with open(CTX / "colony_year_panel.csv") as fh:
            for row in csv.DictReader(fh):
                panel[(row["colony"], int(row["year"]))][row["metric"]] = \
                    float(row["value"])
    with (KG / "colony_year.jsonl").open("w", encoding="utf-8") as fh:
        for (col, y), metrics in sorted(panel.items()):
            fh.write(json.dumps({"colony": col, "year": y,
                                 "metrics": metrics}) + "\n")
    report.append(f"- colony-year nodes: {len(panel):,}")

    # ---- governed edges (successions + annual panel), person-matched
    # peers are listed by TITLE in the volumes but by FAMILY NAME in bios —
    # hand-curated map (pending Wikidata verification, see grounding queue)
    peer_map = {}
    pf = Path("data/services/peer_family_names.json")
    if pf.exists():
        peer_map = {k: v["family"] for k, v in json.loads(pf.read_text()).items()}

    gov_rows = []
    for g in _load(ROOT / "governors/governors.jsonl"):
        m = match_career(g["colony"], g["surname"], g.get("given"), g["year"])
        fam = peer_map.get(g["surname"].lower())
        if m is None and fam:
            m = match_career(g["colony"], fam, None, g["year"])
        gov_rows.append({**g, "source": "succession", "match": m,
                         **({"family_name": fam} if fam else {})})
    from volume_careers import canon_colony
    for g in _load(CTX / "governor_panel.jsonl"):
        col = canon_colony(g["colony_raw"])
        m = (match_career(col, g["surname"], g.get("given"),
                          g.get("commission_year"), window=6)
             or match_career(None, g["surname"], g.get("given"),
                             g.get("commission_year")))
        gov_rows.append({"colony": col or g["colony_raw"], "office": g["office"],
                         "given": g["given"], "surname": g["surname"],
                         "honours": g["honours"], "year": g.get("commission_year"),
                         "salary": g.get("salary"), "edition": g["edition"],
                         "source": "panel", "match": m})
    with (KG / "governed_edges.jsonl").open("w", encoding="utf-8") as fh:
        for r in gov_rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    for src in ("succession", "panel"):
        rs = [r for r in gov_rows if r["source"] == src]
        m = sum(1 for r in rs if r["match"])
        mb = sum(1 for r in rs if r["match"] and r["match"]["bio_ids"])
        report.append(f"- governed edges ({src}): {len(rs):,}; matched to a "
                      f"career: {m:,} ({100*m/max(len(rs),1):.0f}%), of which "
                      f"bio-linked {mb:,}")

    # ---- constitutional status events
    events = [t for t in _load(CTX / "constitution_timeline.jsonl")
              if t["sim_prev"] is not None and (t["gained"] or t["lost"])]
    with (KG / "status_events.jsonl").open("w", encoding="utf-8") as fh:
        for t in events:
            fh.write(json.dumps(t, ensure_ascii=False) + "\n")
    report.append(f"- status events: {len(events)}")

    # ---- honour events: PERSON-first matching. The unified bio-persons
    #      carry their own header-parsed honours, so award(+year) agreement
    #      is near-exact evidence; full given names on both sides make the
    #      name gate strict. Careers attach via the person's linked careers
    #      (direct bio links + the adjudicated overlay); the old career-only
    #      match stays as a fallback for persons the bios never carried.
    import re as _re

    def _norm_award(a):
        return _re.sub(r"[^A-Z]", "", (a or "").upper())

    persons = [p for p in _load(ROOT / "bio_persons/bio_persons.jsonl")
               if "not_a_person" not in p["flags"]]
    pers_by_sur = defaultdict(list)
    for p in persons:
        pers_by_sur[(p.get("surname") or "").lower()].append(p)
    pmap = {}
    for r in _load(ROOT / "bio_persons/bio_person_map.jsonl"):
        pmap[r["bio_id"]] = r["person_id"]
    person_careers = defaultdict(set)
    for c in careers:
        for b in c.get("bio_ids") or []:
            if b in pmap:
                person_careers[pmap[b]].add(c["career_id"])
    for lk in _load(ROOT / "classc/career_person_links.jsonl"):
        person_careers[lk["person_id"]].add(lk["career_id"])

    _TITLE_TOKS = {"the", "hon", "sir", "dame", "mrs", "miss", "lady", "rev",
                   "dr", "col", "capt", "captain", "lieut", "major", "gen",
                   "prof", "ven", "mr"}

    def _detitle(g):
        return " ".join(t for t in (g or "").split()
                        if t.lower().strip(".,") not in _TITLE_TOKS)

    def _strict_name(g, pg):
        """Exact-initials equality, OR a shared spelled forename that is
        ALSO initials-order compatible. Subsequence alone matched 'Mary' to
        'Robt Malcolm'; a bare shared forename matched 'Kenneth Skelton' to
        'Kenneth Arthur Noel' — both guards are needed."""
        g, pg = _detitle(g), _detitle(pg)
        ti, pi = _initials(g), _initials(pg)
        if ti and pi and ti == pi:
            return True
        gt = {t.lower().strip(".,") for t in g.split() if len(t) > 2}
        pt = {t.lower().strip(".,") for t in pg.split() if len(t) > 2}
        return bool(gt & pt) and _names_compatible(g, pg)

    def match_person(h):
        g = h.get("given_names")
        cands = [p for p in pers_by_sur.get((h["surname"] or "").lower(), ())
                 if _strict_name(g, p.get("given_names"))]
        if not cands:
            return None, None
        aw = _norm_award(h.get("award"))
        strong = [p for p in cands if any(
            _norm_award(x.get("award")) == aw
            and (x.get("year") == h.get("year") or x.get("year") is None
                 or h.get("year") is None)
            for x in p.get("honours") or [])]
        if strong and len({p["person_id"] for p in strong}) == 1:
            return strong[0], "award_agreement"
        # unique name+time match, strict name demand (>=2 initials or a
        # spelled forename); window: an award can long postdate service
        if not (g and (len(_initials(g)) >= 2
                       or any(len(t) > 2 for t in g.split()))):
            return None, None
        y = h.get("year")
        timed = [p for p in cands
                 if y is None or ((p.get("career_start") or 9999) - 10 <= y
                                  <= (p.get("career_end") or 0) + 25)]
        if timed and len({p["person_id"] for p in timed}) == 1:
            return timed[0], "name_time"
        return None, None

    hon = _load(CTX / "honours_roll.jsonl")
    matched_p = matched_c = 0
    by_basis = defaultdict(int)
    with (KG / "honour_events.jsonl").open("w", encoding="utf-8") as fh:
        for h in hon:
            p, basis = match_person(h)
            m = None
            if p is not None:
                matched_p += 1
                by_basis[basis] += 1
                cids = sorted(person_careers.get(p["person_id"], ()))
                if cids:
                    matched_c += 1
                m = {"person_id": p["person_id"], "basis": basis,
                     "career_ids": cids}
            else:
                g = h.get("given_names")
                if g and (len(_initials(g)) >= 2 or
                          any(len(t) > 2 for t in g.split())):
                    mc = match_career(None, h["surname"], g, h["year"], window=15)
                    if mc:
                        matched_c += 1
                        by_basis["career_only"] += 1
                        m = {"basis": "career_only", **mc}
            fh.write(json.dumps({**h, "match": m}, ensure_ascii=False) + "\n")
    report.append(
        f"- honour events: {len(hon):,}; matched to a PERSON: {matched_p:,} "
        f"({100*matched_p/max(len(hon),1):.0f}%; "
        + ", ".join(f"{k} {v:,}" for k, v in sorted(by_basis.items()))
        + f"); reaching a career: {matched_c:,} "
        f"({100*matched_c/max(len(hon),1):.0f}%)")

    # ---- CO appointments
    co = _load(CTX / "co_succession.jsonl") + _load(CTX / "co_staff.jsonl")
    with (KG / "co_appointments.jsonl").open("w", encoding="utf-8") as fh:
        for r in co:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    report.append(f"- CO appointments: {len(co):,}")

    (KG / "KG.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))


if __name__ == "__main__":
    main()
