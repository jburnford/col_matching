#!/usr/bin/env python3
"""Fold delta structuring results (res_struct.jsonl) into the structured
corpus after a bios rebuild + rechain (docs/ADJUDICATION_BATCH.md /
bios-fix cycle).

Steps:
  1. drop corpus rows whose person_id left stage-2 (chains reorganized)
  2. drop rows for stale swallow-hosts + all re-structured ids
  3. append successful res_struct rows (skipping any whose input text is
     older than the current worklist's — pass --v1-worklist to evict)
  4. report; then run:
       COL_KG_OUT=data/iol python3 kg_structure_corpus.py validate \
           --in data/iol/llm_struct_corpus.jsonl \
           --persons data/iol/persons.deduped.jsonl
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path("data/iol")
IDD = ROOT / "identity"
ADJ = IDD / "adjudicate"


def jload(path):
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            yield json.loads(line)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default=str(ADJ / "res_struct.jsonl"))
    ap.add_argument("--v1-worklist", default="",
                    help="earlier worklist whose texts may be stale; "
                         "results for ids whose text changed are evicted")
    args = ap.parse_args()

    stage2_ids = {r["person_id"] for r in
                  jload(ROOT / "persons.deduped.jsonl")}
    stale_hosts = set(json.load(open(IDD / "struct_stale_host_ids.json")))

    cur_text = {}
    for r in jload(ADJ / "wl_struct.jsonl"):
        if "person_id" in r:
            cur_text[r["person_id"]] = r["text"]

    old_text = {}
    if args.v1_worklist:
        for r in jload(Path(args.v1_worklist)):
            if "person_id" in r:
                old_text[r["person_id"]] = r["text"]

    stats = Counter()
    results = {}
    for r in jload(Path(args.results)):
        pid = r.get("person_id")
        if not pid or "_error" in r:
            stats["res_error"] += 1
            continue
        if pid in old_text and pid in cur_text \
                and old_text[pid] != cur_text[pid]:
            stats["res_stale_text_evicted"] += 1
            continue
        if pid not in stage2_ids:
            stats["res_left_stage2"] += 1   # judged under an older chain map
            continue
        results[pid] = r
        stats["res_ok"] += 1

    out_rows = []
    for r in jload(ROOT / "llm_struct_corpus.jsonl"):
        pid = r.get("person_id")
        if "_error" in r:
            stats["old_error_dropped"] += 1
            continue
        if pid not in stage2_ids:
            stats["old_left_stage2"] += 1
            continue
        if pid in stale_hosts or pid in results:
            stats["old_superseded"] += 1
            continue
        out_rows.append(r)
        stats["old_kept"] += 1
    for pid in sorted(results):
        out_rows.append(results[pid])

    with open(ROOT / "llm_struct_corpus.jsonl", "w",
              encoding="utf-8") as fh:
        for r in out_rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    still_missing = stage2_ids - {r["person_id"] for r in out_rows}
    print("merge:", dict(stats))
    print(f"corpus now {len(out_rows):,} rows; stage-2 ids without a "
          f"structure: {len(still_missing):,}")
    if still_missing:
        with open(IDD / "struct_missing_ids.json", "w") as fh:
            json.dump(sorted(still_missing), fh)
        print("  (listed in identity/struct_missing_ids.json — rerun the "
              "worker on these)")


if __name__ == "__main__":
    main()
