#!/usr/bin/env python3
"""Class the IOL no-bio identities against the bio person table
(NOBIO_DEDUP_KICKOFF step 2 — the COL never-bio'd A/B/C protocol,
volume_classc_worklist.py mirrored onto the IOL corpus).

For every no-bio identity (civil-list chain from nobio_civil_chains
.jsonl, unlinked gradation identity):
  A  no name-compatible bio person anywhere — safely never-bio'd
  B  namesakes exist but all era- and/or province-incompatible —
     safely never-bio'd
  C  at least one compatible namesake — ambiguity UPPER bound; emit
     (identity x person) pairs for the Nibi judge (--mode iolabc).
     Verdict "same" = the linker missed a bio person (candidate link);
     "different" everywhere = measured never-bio'd.
  U  no usable given names — reported separately

Compatibility stays an upper bound: persons with no resolvable
province, and Government of India / India Office service, cannot be
ruled out on place.

Outputs (data/iol/identity/):
  nobio_classes.jsonl          one row per identity: class + evidence
  adjudicate/wl_abc.jsonl      class-C pairs (cap 4/identity)
  NOBIO_CLASSES.md             report
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from col_match.services.match import _names_compatible

ROOT = Path("data/iol")
IDD = ROOT / "identity"
MAX_CANDIDATES = 4
MAX_PERSON_EVENTS = 30
ERA_BEFORE, ERA_AFTER = 2, 3       # COL slack: end < lo-2 / start > hi+3

_STYLES = {"sir", "hon", "honble", "rev", "revd", "dr", "lord", "bart",
           "bt", "mr", "major", "col", "capt", "lieut", "lt", "gen"}

# Province keywords -> the presidency "side" whose establishments feed
# them (same table as iol_nobio_unify). GoI/India Office = all sides.
_PROV_SIDE = {
    "BENGAL": "BENGAL", "CALCUTTA": "BENGAL", "PUNJAB": "BENGAL",
    "LAHORE": "BENGAL", "OUDH": "BENGAL", "AGRA": "BENGAL",
    "UNITED PROVINCES": "BENGAL", "ALLAHABAD": "BENGAL",
    "CENTRAL PROVINCES": "BENGAL", "NAGPUR": "BENGAL",
    "ASSAM": "BENGAL", "BURMA": "BENGAL", "RANGOON": "BENGAL",
    "BIHAR": "BENGAL", "ORISSA": "BENGAL", "FRONTIER": "BENGAL",
    "PESHAWAR": "BENGAL", "DELHI": "BENGAL",
    "MADRAS": "MADRAS", "COORG": "MADRAS",
    "BOMBAY": "BOMBAY", "SIND": "BOMBAY", "KARACHI": "BOMBAY",
    "BALUCHISTAN": "BOMBAY", "ADEN": "BOMBAY", "POONA": "BOMBAY",
}
_GOV_SIDE = {
    "BENGAL": "BENGAL", "PUNJAB": "BENGAL",
    "UNITED PROVINCES OF AGRA AND OUDH": "BENGAL",
    "CENTRAL PROVINCES": "BENGAL", "ASSAM": "BENGAL",
    "BURMA": "BENGAL", "BIHAR AND ORISSA": "BENGAL",
    "BIHAR": "BENGAL", "ORISSA": "BENGAL", "DELHI": "BENGAL",
    "NORTH-WEST FRONTIER PROVINCE": "BENGAL",
    "EASTERN BENGAL AND ASSAM": "BENGAL",
    "AJMER-MERWARA": "BENGAL",
    "MADRAS": "MADRAS", "COORG": "MADRAS",
    "BOMBAY": "BOMBAY", "SIND": "BOMBAY", "BALUCHISTAN": "BOMBAY",
    "ADEN": "BOMBAY",
}


def sk(s: str | None) -> str:
    return re.sub(r"[^A-Z]", "", (s or "").upper())


def given_part(full_name: str | None) -> str:
    toks = [t for t in (full_name or "").split()
            if any(c.isalpha() for c in t)]
    toks = toks[:-1] if len(toks) >= 2 else []
    return " ".join(t for t in toks
                    if re.sub(r"[^a-z]", "", t.lower()) not in _STYLES)


def text_sides(*texts: str | None) -> set[str]:
    up = " ".join(t for t in texts if t).upper()
    return {side for kw, side in _PROV_SIDE.items() if kw in up}


def load_persons():
    by_sur: dict[str, list[dict]] = defaultdict(list)
    n = 0
    for l in open(ROOT / "llm_struct_corpus.stage3.deduped.jsonl",
                  encoding="utf-8"):
        p = json.loads(l)
        n += 1
        eds = sorted(set(p.get("editions") or []))
        yrs = [y for e in (p.get("events") or [])
               for y in (e.get("year_start"), e.get("year_end")) if y]
        span = yrs + eds
        sides = set()
        for e in (p.get("events") or []):
            sides |= text_sides(e.get("place"), e.get("position"))
        by_sur[sk(p.get("surname"))].append({
            "person_id": p["person_id"],
            "surname": p.get("surname"),
            "given": p.get("given_names"),
            "birth_year": p.get("birth_year"),
            "honours": [h.get("award") for h in
                        (p.get("honours") or []) if h.get("award")][:8],
            "eds": eds, "sides": sides,
            "lo": min(span) if span else None,
            "hi": max(span) if span else None,
            "events": p.get("events") or [],
        })
    return by_sur, n


def person_lines(q: dict) -> list[str]:
    out = []
    for e in q["events"][:MAX_PERSON_EVENTS]:
        yr = e.get("year_start")
        out.append(f"  {yr if yr else '????'}: {e.get('position') or '?'}"
                   + (f" [{e['place']}]" if e.get("place") else ""))
    return out


def classify(row_id, population, surname_key, given, years, sides,
             extra, by_sur, pairs, career_render):
    """Shared A/B/C logic; returns the class row."""
    row = {"id": row_id, "population": population,
           "surname_key": surname_key, "given": given,
           "years": years, **extra}
    if not given or not surname_key:
        row.update({"cls": "U", "n_namesakes": None, "n_compatible": None})
        return row
    namesakes = [q for q in by_sur.get(surname_key, ())
                 if _names_compatible(q["given"], given)]
    if not namesakes:
        row.update({"cls": "A", "n_namesakes": 0, "n_compatible": 0})
        return row
    cand = []
    for q in namesakes:
        if q["lo"] is not None and years:
            if years[1] < q["lo"] - ERA_BEFORE \
                    or years[0] > q["hi"] + ERA_AFTER:
                continue
            overlap = min(years[1], q["hi"]) - max(years[0], q["lo"])
        else:
            overlap = 0
        side_known = bool(q["sides"] & sides)
        if sides and q["sides"] and not side_known:
            continue                        # both known, disjoint
        cand.append((2 * side_known + (overlap >= 0), overlap, q))
    if not cand:
        row.update({"cls": "B", "n_namesakes": len(namesakes),
                    "n_compatible": 0})
        return row
    cand.sort(key=lambda t: (-t[0], -t[1]))
    row.update({"cls": "C", "n_namesakes": len(namesakes),
                "n_compatible": len(cand)})
    for rank_i, (_, _, q) in enumerate(cand[:MAX_CANDIDATES]):
        pairs.append({
            "id": f"abc::{row_id}::{q['person_id']}",
            "career_id": row_id, "person_id": q["person_id"],
            "cand_rank": rank_i, "pool": "nobio_abc",
            "career": career_render,
            "person": {
                "name": f"{q['surname'] or ''}, {q['given'] or ''}"
                        .strip(", "),
                "birth_year": q["birth_year"],
                "honours": q["honours"],
                "editions": [q["eds"][0], q["eds"][-1]] if q["eds"]
                else None,
                "lines": person_lines(q),
            },
        })
    return row


def main() -> None:
    by_sur, n_persons = load_persons()
    classes, pairs = [], []

    for l in open(IDD / "nobio_civil_chains.jsonl", encoding="utf-8"):
        c = json.loads(l)
        gov = c["government"]
        side = _GOV_SIDE.get(gov)
        career = {
            "colony": gov,
            "name": c["name"],
            "roster_years": c["years"],
            "lines": ["  civil-list office chain, "
                      f"{c['n_records']} yearly records",
                      "  offices: " + "; ".join(c["offices"])],
        }
        classes.append(classify(
            c["chain_id"], "civil_chain", c["surname_key"],
            given_part(c["name"]), c["years"],
            {side} if side else set(),
            {"government": gov}, by_sur, pairs, career))

    linked = {json.loads(l)["gradation_id"] for l in
              open(ROOT / "gradation/gradation_person_links.jsonl",
                   encoding="utf-8")}
    for l in open(ROOT / "gradation/gradation_identities.jsonl",
                  encoding="utf-8"):
        g = json.loads(l)
        if g["gradation_id"] in linked:
            continue
        eds = g.get("editions") or []
        years = [min(eds), max(eds)] if eds else None
        sides = set()
        for est in g.get("establishments") or []:
            sides |= text_sides(est)
        for cor in g.get("corps") or []:
            head = re.sub(r"[^A-Z]", "", cor.upper().split(".")[0])
            sides |= {"BOMBAY"} if head == "BO" else \
                {"BENGAL"} if head == "B" else \
                {"MADRAS"} if head == "M" else set()
        trace = [f"  gradation ({g['list_type']}) seniority trace, "
                 f"commission/covenant year {g.get('entry_year')}"]
        for label in ("sections", "corps", "establishments",
                      "appointments", "honours"):
            if g.get(label):
                trace.append(f"  {label}: " + "; ".join(
                    str(x) for x in g[label][:8]))
        career = {
            "colony": f"{g['list_type']} gradation list",
            "name": f"{g.get('given') or ''} {g['surname']}".strip(),
            "roster_years": years,
            "lines": trace,
        }
        classes.append(classify(
            g["gradation_id"], "gradation", sk(g["surname"]),
            g.get("given"), years, sides,
            {"list_type": g["list_type"],
             "entry_year": g.get("entry_year")},
            by_sur, pairs, career))

    with open(IDD / "nobio_classes.jsonl", "w", encoding="utf-8") as fh:
        for r in classes:
            fh.write(json.dumps({k: (sorted(v) if isinstance(v, set)
                                     else v) for k, v in r.items()},
                                ensure_ascii=False) + "\n")
    with open(IDD / "adjudicate/wl_abc.jsonl", "w",
              encoding="utf-8") as fh:
        for r in pairs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    tot = Counter(r["cls"] for r in classes)
    by_pop = defaultdict(Counter)
    for r in classes:
        by_pop[r["population"]][r["cls"]] += 1
    lines = [
        "# No-bio identities classed against the bio table "
        "(COL A/B/C protocol)",
        "",
        f"- identities classed: {len(classes):,} — "
        + ", ".join(f"{k}: {tot[k]:,}" for k in "ABCU"),
        f"- bio persons indexed: {n_persons:,}",
        f"- class-C adjudication pairs (cap {MAX_CANDIDATES}/identity): "
        f"{len(pairs):,} -> adjudicate/wl_abc.jsonl (--mode iolabc)",
        "",
        "| population | classed | A | B | C | U | C% |",
        "|---|---|---|---|---|---|---|",
    ]
    for pop, c in sorted(by_pop.items()):
        n = sum(c.values())
        lines.append(
            f"| {pop} | {n:,} | {c['A']:,} | {c['B']:,} | {c['C']:,} "
            f"| {c['U']:,} | {100 * c['C'] // max(n, 1)}% |")
    lines += [
        "",
        "A/B are safely never-bio'd; C is the ambiguity upper bound "
        "the judge turns into a measured rate ('same' = missed link, "
        "all-'different' = measured no-bio).",
    ]
    (IDD / "NOBIO_CLASSES.md").write_text("\n".join(lines) + "\n",
                                          encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
