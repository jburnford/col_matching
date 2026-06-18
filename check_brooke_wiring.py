#!/usr/bin/env python3
"""Test the highest-value zero-cost hypothesis: G. E. Brooke's Straits
Settlements staff-list row was already RECOVERED (deterministic recover and/or
the extraction backfill) but is NOT wired into the live match target
(graph_cache/officials.jsonl) that attach/match read — so the matcher never
sees it and he stays unmatched.

Scans every JSONL under data/services for a Brooke row that looks like the
Port Health Officer / Straits Settlements record, reports which files contain
it, and whether the live officials cache does.

Run from the repo root:  python3 check_brooke_wiring.py
"""
import glob
import json
import os

DATA = "data/services"
LIVE = f"{DATA}/graph_cache/officials.jsonl"


def line_has_brooke(text: str) -> bool:
    t = text.lower()
    return "brooke" in t and ("straits" in t or "port health" in t or "singapore" in t)


def main():
    files = sorted(glob.glob(f"{DATA}/**/*.jsonl", recursive=True))
    print(f"scanning {len(files)} JSONL files under {DATA}\n")

    found_in = {}
    for p in files:
        n = 0
        samples = []
        try:
            for line in open(p, encoding="utf-8"):
                if "brooke" in line.lower() and line_has_brooke(line):
                    n += 1
                    if len(samples) < 3:
                        samples.append(line.strip()[:200])
        except Exception:
            continue
        if n:
            found_in[p] = (n, samples)

    print("=== files containing a Brooke + Straits/Singapore/PortHealth row ===")
    for p, (n, samples) in found_in.items():
        tag = "  <-- LIVE MATCH TARGET" if p == LIVE else ""
        print(f"\n{p}  ({n} rows){tag}")
        for s in samples:
            print(f"    {s}")

    print("\n=== verdict ===")
    in_live = LIVE in found_in
    in_recovered = any("recover" in p or "backfill" in p or "extract" in p
                       for p in found_in)
    if in_recovered and not in_live:
        print("  CONFIRMED: Brooke's row is on disk in a recovered/backfill file but"
              " NOT in the live officials cache. The matcher can't see it.")
        print("  -> wiring confirmed-recovered records into the match target would"
              " realize this (and ~thousands like it) at zero token cost.")
    elif in_live:
        print("  Brooke IS in the live officials cache — the gap is elsewhere"
              " (parse/colony/matcher).")
    else:
        print("  Brooke not found in any scanned file — his row may only exist in the"
              " raw source OCR (~/textasdatacolonialofficelist), never extracted at all.")


if __name__ == "__main__":
    main()
