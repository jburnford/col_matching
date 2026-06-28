#!/usr/bin/env python3
"""Apply hand-adjudicated institution-grounding CORRECTIONS to the caches.

Pre-publication QA (2026-06-27) found a small set of string-similarity
misgroundings surfaced by verify_institution_qids.py (US namesakes of British
schools). Career-region + chronology confirmed them (e.g. the 39 "St Andrews"
men are all India Civil Service from the 1880s — the US St Andrews college was
founded 1958). This rewrites the affected rows in BOTH grounding caches
(data/{kg,iol}/institutions_grounding.jsonl), keyed by the WRONG QID so every
surface variant is corrected at once. Backs up each cache first. Re-emit after
with kg_ground_institutions.py emit + kg_remap_edge_layers.py.
"""
import json, shutil
from pathlib import Path

# wrong_qid -> corrected grounding fields (label/instance_of/country/source)
FIX = {
    "Q7586947": {"id": "Q216273", "label": "University of St Andrews",
                 "instance_of": ["public university"], "country_qid": "Q145",
                 "source": "mcp", "match_type": "mcp_verified"},          # NC,US -> Scotland
    "Q7989150": {"id": "Q1341516", "label": "Westminster School",
                 "instance_of": ["public school"], "country_qid": "Q145",
                 "source": "mcp", "match_type": "mcp_verified"},          # US college -> London
    "Q4570781": {"id": "Q2738646", "label": "University of Lincoln",
                 "instance_of": ["public university"], "country_qid": "Q145",
                 "source": "mcp", "match_type": "mcp_verified"},          # US -> University of Lincoln
    "Q6391891": {"id": "colkg:Kent_School", "label": "Kent School",
                 "instance_of": [], "country_qid": None,
                 "source": "internal", "match_type": "ambiguous_multi_referent"},  # no clean referent
}

for root in ("data/kg", "data/iol"):
    p = Path(root) / "institutions_grounding.jsonl"
    if not p.exists():
        continue
    shutil.copy(p, p.with_suffix(".jsonl.preqafix_bak"))
    rows = [json.loads(l) for l in p.open()]
    n = 0
    for r in rows:
        fix = FIX.get(r.get("id"))
        if fix:
            r.update(fix)
            n += 1
    with p.open("w") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{root}: corrected {n} surface rows")
