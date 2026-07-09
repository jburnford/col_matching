#!/usr/bin/env python3
"""Merge Qwen residue-pass results into the volume record files.

Reads data/volume/qwen_roster_results.jsonl (pulled back from Nibi), validates
each record, and appends to data/volume/col<year>/records.jsonl with
source="qwen" (rules-tier records get source="rules" implicitly — they have no
source field). Idempotent: existing qwen record_ids are skipped.

Also writes data/volume/qwen_merge_report.txt with per-era yields and
rejection counts.
"""
import json, re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("data/volume")
RESULTS = ROOT / "qwen_roster_results.jsonl"

SURNAME_OK = re.compile(r"^[A-Za-z][A-Za-z'’.\- ]{1,40}$")
# hallucination guards: surname must actually appear in the source block text
# (case-insensitive, allowing OCR spacing); positions capped in length
MAX_POSITION = 120

def main():
    worklist_text = {}
    for line in open(ROOT / "qwen_worklist.jsonl"):
        b = json.loads(line)
        worklist_text[b["id"]] = b["text"].lower()

    # colony/department as CURRENTLY assigned by the header tracker — the
    # values stored in the qwen results were captured at worklist time and go
    # stale whenever roster.py's colony assignment improves. Keyed on block
    # provenance; a block no longer in any roster region (e.g. back matter
    # that now resets colony) drops its qwen records.
    block_ctx = {}
    for d in ROOT.glob("col[0-9]*"):
        for line in open(d / "roster_blocks.jsonl"):
            blk = json.loads(line)
            p = blk["provenance"]
            block_ctx[(p["edition_year"], p["page"], p["block"])] = (
                blk["colony"], blk["department"])

    existing = defaultdict(set)          # year -> qwen record_ids already merged
    for d in ROOT.glob("col[0-9]*"):
        year = int(d.name[3:])
        for line in open(d / "records.jsonl"):
            r = json.loads(line)
            if r.get("source") == "qwen":
                existing[year].add(r["record_id"])

    stats = Counter()
    out_fh = {}
    per_year = Counter()
    for line in open(RESULTS):
        res = json.loads(line)
        if "error" in res:
            stats["block_error"] += 1
            continue
        year = res["year"]
        src_text = worklist_text.get(res["id"], "")
        for i, r in enumerate(res.get("records", [])):
            stats["records_in"] += 1
            sur = (r.get("surname") or "").strip()
            if not SURNAME_OK.match(sur):
                stats["bad_surname"] += 1
                continue
            # anti-hallucination: the surname string must occur in the block
            if sur.lower() not in src_text:
                stats["surname_not_in_block"] += 1
                continue
            rid = f"{res['id']}q{i}"
            if rid in existing[year]:
                stats["already_merged"] += 1
                continue
            prov = res["provenance"]
            ctx = block_ctx.get((prov["edition_year"], prov["page"], prov["block"]))
            if ctx is None:
                stats["block_no_longer_roster"] += 1
                continue
            colony, department = ctx
            pos = r.get("position")
            if pos and len(pos) > MAX_POSITION:
                pos = pos[:MAX_POSITION]
            rec = {
                "record_id": rid, "edition_year": year,
                "colony": colony, "department": department,
                "position": pos, "name_raw": ((r.get("given_names") or "") + " " + sur).strip(),
                "surname": sur, "given_names": r.get("given_names"),
                "honours": r.get("honours") or [], "salary": r.get("salary"),
                "snippet": "", "provenance": res["provenance"], "source": "qwen",
            }
            if year not in out_fh:
                out_fh[year] = open(ROOT / f"col{year}" / "records.jsonl", "a")
            out_fh[year].write(json.dumps(rec, ensure_ascii=False) + "\n")
            per_year[year] += 1
            stats["merged"] += 1
    for fh in out_fh.values():
        fh.close()

    lines = ["Qwen merge report", "=" * 40]
    for k, v in sorted(stats.items()):
        lines.append(f"{k:24} {v:,}")
    lines.append("\nmerged records by era:")
    lines.append(f"  pre-1946: {sum(v for y, v in per_year.items() if y < 1946):,}")
    lines.append(f"  1946+   : {sum(v for y, v in per_year.items() if y >= 1946):,}")
    lines.append("\ntop 10 years:")
    for y, v in per_year.most_common(10):
        lines.append(f"  {y}: {v:,}")
    report = "\n".join(lines)
    (ROOT / "qwen_merge_report.txt").write_text(report + "\n")
    print(report)

if __name__ == "__main__":
    main()
