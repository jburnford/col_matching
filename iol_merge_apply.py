#!/usr/bin/env python3
"""Apply the full-corpus merge-map adjudication (Nibi 17505330): decisions
ledger -> audited, FLATTENED merge map.

Consumes  data/iol/identity/merge_audit_results.jsonl   (all 12,540 edges)
          data/iol/identity/a6_results.jsonl            (35 under-merge pairs)
Ledger    data/iol/identity/merge_decisions.jsonl — append-only and
          ACCUMULATIVE (the COL override-ledger discipline: regenerating
          fresh would revert applied fixes); rows
          {person_a, person_b, action: drop|keep|add|review, verdict,
           confidence, reason, source}.
Map out   data/iol/dedup_stage3_merge_map.audited.jsonl — union-find over
          kept school-map edges + A6-confirmed unions, canonical = the old
          school-map canonical when it survives in the cluster (minimal id
          churn), else most-attested; FLATTENED (fixes the 16 unflattened
          chains from the school-pass compose).

Then rebuild (this script prints the exact commands, does not run them):
  COL_PROV=data/iol/persons.deduped.jsonl python3 kg_dedup_stage3_apply.py
      --corpus data/iol/llm_struct_corpus.valid.jsonl
      --map data/iol/dedup_stage3_merge_map.audited.jsonl
      --out data/iol/llm_struct_corpus.stage3.deduped.jsonl
  COL_KG_OUT=data/iol python3 kg_emit_stage3.py
      --corpus data/iol/llm_struct_corpus.stage3.deduped.jsonl
      --out data/iol/graph_stage3
and update iol_identity_check.py baselines in the same commit.

Verdict -> action: different -> drop; same -> keep; unsure/error -> review
(edge KEPT pending hand review, mirroring the COL B1 apply).
A6: same -> add (union); different -> none (stays split); unsure -> review.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path("data/iol")
IDD = ROOT / "identity"
LEDGER = IDD / "merge_decisions.jsonl"
SOURCE = "nibi-17505330"


def jload(path: Path):
    if not path.exists():
        return
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            yield json.loads(line)


def main() -> None:
    # ---- 1. verdicts -> accumulative ledger --------------------------------
    existing = {(r["person_a"], r["person_b"]) for r in jload(LEDGER)}
    new_rows = []

    def action_for(r: dict, add_mode: bool) -> str:
        if "error" in r or r.get("verdict") == "unsure":
            return "review"
        if r.get("verdict") == "same":
            return "add" if add_mode else "keep"
        if r.get("verdict") == "different":
            return "none" if add_mode else "drop"
        return "review"

    for path, add_mode in [(IDD / "merge_audit_results.jsonl", False),
                           (IDD / "a6_results.jsonl", True)]:
        for r in jload(path):
            key = (r.get("person_a"), r.get("person_b"))
            if None in key or key in existing:
                continue
            existing.add(key)
            act = action_for(r, add_mode)
            if act == "none":
                continue
            new_rows.append({
                "person_a": key[0], "person_b": key[1],
                "action": act, "verdict": r.get("verdict"),
                "confidence": r.get("confidence"),
                "reason": (r.get("reason") or r.get("error") or "")[:250],
                "stratum": r.get("stratum"), "source": SOURCE,
            })
    if new_rows:
        with open(LEDGER, "a", encoding="utf-8") as fh:
            for row in new_rows:
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    ledger = list(jload(LEDGER))
    acts = Counter(r["action"] for r in ledger)
    print(f"ledger: {len(ledger):,} decisions "
          f"({len(new_rows):,} appended this run): {dict(acts)}")

    # ---- 2. audited flattened map ------------------------------------------
    # After a bios rebuild + rechain, some person_ids leave the corpus
    # (chains reorganize). Edges citing vanished ids are moot — prune
    # them or the map fails the *_not_in_corpus invariants.
    corpus_ids = {r["person_id"] for r in
                  jload(ROOT / "llm_struct_corpus.valid.jsonl")}
    school = {(r["person_id"], r["canonical_person_id"])
              for r in jload(ROOT / "dedup_stage3_merge_map.school.jsonl")}
    n_school_raw = len(school)
    school = {(a, b) for a, b in school
              if a in corpus_ids and b in corpus_ids}
    if len(school) != n_school_raw:
        print(f"pruned {n_school_raw - len(school):,} school edges citing "
              "ids no longer in the corpus (post-rechain)")
    old_canon = Counter(c for _, c in school)
    drops = {(r["person_a"], r["person_b"])
             for r in ledger if r["action"] == "drop"}
    adds = [(r["person_a"], r["person_b"])
            for r in ledger if r["action"] == "add"
            and r["person_a"] in corpus_ids and r["person_b"] in corpus_ids]
    kept = [e for e in school if e not in drops]
    dropped = len(school) - len(kept)

    parent: dict[str, str] = {}

    def find(x: str) -> str:
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for a, b in kept:
        union(a, b)
    for a, b in adds:
        union(a, b)

    clusters: dict[str, list[str]] = {}
    for x in list(parent):
        clusters.setdefault(find(x), []).append(x)

    nattest = {r["person_id"]: r.get("n_attestations") or 0
               for r in jload(ROOT / "persons.deduped.jsonl")}

    rows_out = []
    for members in clusters.values():
        if len(members) < 2:
            continue
        # canonical: the old school-map canonical if exactly the cluster core
        # survived around it; among several (A6 joined two clusters) or none
        # (canonical detached), the most-attested member
        olds = [m for m in members if old_canon.get(m)]
        pool = olds or members
        canon = max(pool, key=lambda m: (nattest.get(m, 0), m))
        for m in members:
            if m != canon:
                rows_out.append({"person_id": m, "canonical_person_id": canon})

    outp = ROOT / "dedup_stage3_merge_map.audited.jsonl"
    with open(outp, "w", encoding="utf-8") as fh:
        for row in sorted(rows_out, key=lambda r: r["person_id"]):
            fh.write(json.dumps(row) + "\n")

    keys = {r["person_id"] for r in rows_out}
    canons = {r["canonical_person_id"] for r in rows_out}
    assert not keys & canons, "audited map is not flattened"
    n_persons = len(corpus_ids) - len(rows_out)
    print(f"map: {len(school):,} school edges - {dropped:,} dropped "
          f"+ {len(adds)} A6 unions -> {len(rows_out):,} flattened rows "
          f"({outp})")
    print(f"person table after re-apply: ~{n_persons:,} canonical persons")
    print("\nRebuild:")
    print("  COL_PROV=data/iol/persons.deduped.jsonl "
          "python3 kg_dedup_stage3_apply.py \\\n"
          "      --corpus data/iol/llm_struct_corpus.valid.jsonl \\\n"
          "      --map data/iol/dedup_stage3_merge_map.audited.jsonl \\\n"
          "      --out data/iol/llm_struct_corpus.stage3.deduped.jsonl")
    print("  COL_KG_OUT=data/iol python3 kg_emit_stage3.py \\\n"
          "      --corpus data/iol/llm_struct_corpus.stage3.deduped.jsonl \\\n"
          "      --out data/iol/graph_stage3")
    print("  python3 iol_identity_screens.py && python3 iol_identity_check.py"
          "   # update baselines in the same commit")


if __name__ == "__main__":
    main()
