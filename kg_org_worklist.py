#!/usr/bin/env python3
"""Build the EMPLOYER / ORGANISATION worklist from the v2 career-event layer.

Many career events carry an `place_raw` that is not a geographic place but an
EMPLOYER: a railway, the posts & telegraphs administration, the Colonial Office,
a police force, a regiment, or a government department. These were left
ungrounded by the place pipeline (no place_qid) because they are organisations,
not places. This script collects the distinct ungrounded org surfaces so they
can be grounded with the same harness used for education institutions
(kg_ground_institutions.py with COL_WORK/COL_CACHE pointing at the org files).

Input : data/kg/graph_stage3/career_events.jsonl  (flattened, has person_id,
        place_raw, place_qid, position)
Output: data/kg/org_worklist.jsonl
        {institution, type, count, person_ids, examples}  (count-desc)

Surfaces are grouped case-insensitively (so "Colonial Office" / "colonial
office" collapse) on a lightly-normalised key; the most common original spelling
is kept as the display `institution`. Abbreviations (E.A.R. & H., K.U.R. & H.,
P.W.D., ...) are deliberately NOT pre-merged into their expansions here -- they
are unified at grounding time by mapping each surface to the same QID (the
`reuse` disposition), exactly as the education layer handles "Imp. College".
"""
from __future__ import annotations
import json, re
from pathlib import Path
from collections import defaultdict, Counter
from col_match.kg.paths import kg_out

EVENTS = kg_out() / "graph_stage3" / "career_events.jsonl"
OUT = kg_out() / "org_worklist.jsonl"

# A place_raw is an ORG (employer) when it names an administrative body, service,
# department, force or unit rather than a settlement/territory.
ORG = re.compile(
    r"\b(railway|railways|R\. ?& ?H|harbour|harbours|posts|telegraph|telegraphs|tels|"
    r"telecom|telecoms|P\. ?& ?T|currency|administration|department|dept|board of|"
    r"regiment|battalion|infantry|artillery|fusiliers|hussars|lancers|"
    r"colonial office|customs|excise|police|constabulary|secretariat|treasury|"
    r"public works|P\.W\.D|survey|surveys|audit|judicial|legal|marine|forestry|"
    r"agriculture|education|medical|sanitary|inland revenue|income tax|inc\. tax|"
    r"war office|foreign office|home office|admiralty|crown agents)\b",
    re.I,
)

# Type families, first match wins. Used only as a hint for grounding triage.
TYPE_RULES = [
    ("colonial_office",   re.compile(r"colonial office|^c\.?o\.?$", re.I)),
    ("railway",           re.compile(r"railway|railways|R\. ?& ?H|harbour", re.I)),
    ("posts_telegraphs",  re.compile(r"\bposts\b|telegraph|\btels\b|telecom|P\. ?& ?T|E\.A\.P", re.I)),
    ("police",            re.compile(r"police|constabulary", re.I)),
    ("military",          re.compile(r"regiment|battalion|infantry|artillery|fusiliers|"
                                     r"hussars|lancers|\bguards\b|R\.E\.|R\.A\.|R\.N\.|marine", re.I)),
    ("customs",           re.compile(r"customs|excise|inland revenue|income tax|inc\. tax", re.I)),
    ("treasury",          re.compile(r"treasury|currency|audit", re.I)),
    ("secretariat",       re.compile(r"secretariat|colonial sec", re.I)),
    ("public_works",      re.compile(r"public works|P\.W\.D", re.I)),
    ("survey",            re.compile(r"\bsurvey", re.I)),
    ("department",        re.compile(r"department|dept|board of|judicial|legal|forestry|"
                                     r"agriculture|education|medical|sanitary", re.I)),
]

def org_type(s: str) -> str:
    for name, rx in TYPE_RULES:
        if rx.search(s):
            return name
    return "organisation"

def norm(s: str) -> str:
    """Light normalisation for grouping: collapse whitespace, drop a trailing period."""
    s = re.sub(r"\s+", " ", s).strip()
    return s.rstrip(".").strip()

def main():
    groups = defaultdict(lambda: {"count": 0, "person_ids": set(),
                                  "spellings": Counter(), "examples": Counter()})
    seen_events = 0
    for line in EVENTS.open():
        e = json.loads(line)
        if e.get("place_qid"):
            continue
        raw = e.get("place_raw")
        if not raw or not ORG.search(raw):
            continue
        disp = norm(raw)
        if not disp:
            continue
        key = disp.casefold()
        g = groups[key]
        g["count"] += 1
        g["person_ids"].add(e["person_id"])
        g["spellings"][disp] += 1
        g["examples"][raw] += 1
        seen_events += 1

    rows = []
    for key, g in groups.items():
        institution = g["spellings"].most_common(1)[0][0]
        rows.append({
            "institution": institution,
            "type": org_type(institution),
            "count": g["count"],
            "person_ids": sorted(g["person_ids"]),
            "examples": [s for s, _ in g["examples"].most_common(3)],
        })
    rows.sort(key=lambda r: -r["count"])

    with OUT.open("w") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    tot = sum(r["count"] for r in rows)
    print(f"{len(rows):,} distinct org surfaces | {tot:,} mentions | {seen_events:,} events -> {OUT}")
    bytype = Counter()
    for r in rows:
        bytype[r["type"]] += r["count"]
    for t, n in bytype.most_common():
        print(f"  {t:18} {n:5} mentions")

if __name__ == "__main__":
    main()
