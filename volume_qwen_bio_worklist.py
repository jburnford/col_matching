#!/usr/bin/env python3
"""Build the Qwen bio worklist: services-section entries the rules tier could
not parse into career events (parser == "unparsed" in bios_unparsed.jsonl).

Very short fragments are dropped; section-preamble prose is left in — the
worker's prompt lets the model return {"not_a_bio": true} for those.

Output: data/volume/qwen_bio_worklist.jsonl
  {"id": bio_id, "year", "surname", "given_names", "text", "provenance"}
"""
import json
from pathlib import Path

ROOT = Path("data/volume")
MIN_CHARS = 60

n = kept = 0
with (ROOT / "qwen_bio_worklist.jsonl").open("w", encoding="utf-8") as out:
    for d in sorted(ROOT.glob("col[0-9]*")):
        year = int(d.name[3:])
        p = d / "bios_unparsed.jsonl"
        if not p.exists():
            continue
        for line in open(p, encoding="utf-8"):
            b = json.loads(line)
            n += 1
            text = (b.get("raw_text") or "").strip()
            if len(text) < MIN_CHARS:
                continue
            kept += 1
            out.write(json.dumps({
                "id": b["bio_id"], "year": year,
                "surname": b.get("surname"), "given_names": b.get("given_names"),
                "text": text[:6000],
                "provenance": (b.get("provenance") or [{}])[0],
            }, ensure_ascii=False) + "\n")
print(f"unparsed bios {n:,} -> worklist {kept:,} -> {ROOT}/qwen_bio_worklist.jsonl")
