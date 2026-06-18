#!/usr/bin/env python3
"""Size the Colonial Office / London addressable population.

Counts place-less *dated* biography clauses whose position text looks like a
London / Colonial-Office establishment role (Secretary of State's office, Crown
Agents, etc.) — the cohort Phase 3 (CO-London extraction) would make matchable.
This number decides whether the era-by-era CO parser is worth building.

Run from the repo root:
    python3 size_co_london.py
or point it at the data dir explicitly:
    python3 size_co_london.py /home/jic823/col_matching/data/services
"""

import json
import re
import sys
from pathlib import Path

# London / Colonial-Office establishment role cues (position text only).
PAT = re.compile(
    r"colonial office|secretary of state|downing street|crown agent|"
    r"under-?secretary|private secretary to the secretary|"
    r"clerk in the colonial|home (?:office|establishment)",
    re.I,
)


def main() -> int:
    data_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/services")
    bio_events = data_dir / "graph" / "bio_events.jsonl"
    biographies = data_dir / "biographies" / "biographies.jsonl"
    if not bio_events.exists():
        print(f"ERROR: {bio_events} not found. Pass the data dir as an argument, "
              f"e.g. python3 size_co_london.py /home/jic823/col_matching/data/services",
              file=sys.stderr)
        return 1

    # bio_id -> (surname, given_names), for readable samples
    name_of: dict[str, tuple[str, str | None]] = {}
    with biographies.open(encoding="utf-8") as fh:
        for line in fh:
            d = json.loads(line)
            name_of[d["bio_id"]] = (d["surname"], d.get("given_names"))

    total = place_less = co = 0
    bios_co: set[str] = set()
    samples: list[str] = []
    with bio_events.open(encoding="utf-8") as fh:
        for line in fh:
            e = json.loads(line)
            total += 1
            if e.get("place"):
                continue
            place_less += 1
            pos = e.get("position") or ""
            if PAT.search(pos):
                co += 1
                bios_co.add(e["person_id"])
                if len(samples) < 30:
                    sur, gn = name_of.get(e["person_id"], ("?", "?"))
                    samples.append(f"  {sur}, {gn} | '{pos}' ({e.get('year_start')})")

    print(f"total bio events          : {total:,}")
    print(f"place-less events         : {place_less:,}")
    print(f"Colonial-Office/London-ish: {co:,} clauses across {len(bios_co):,} biographies")
    print("--- samples ---")
    print("\n".join(samples))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
