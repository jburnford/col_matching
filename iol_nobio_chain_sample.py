#!/usr/bin/env python3
"""Chain-identity sampling (NOBIO_DEDUP_KICKOFF step 3): are the no-bio
civil chains one person each?

A chain collapses unlinked civil-list records on (surname, initials,
government) with an 8-year gap split — same-initials namesakes inside
one government are the failure mode the census caveat left UNMEASURED.
This draws a stratified sample and renders each chain's full printed
trace for the Nibi judge (--mode iolchain, verdict confirm = one
person / reject = conflated namesakes / unsure), the
iol_merge_audit.py -> iol_merge_measure.py pattern.

Frame: chains with >= 2 records (single-record chains cannot conflate).
Strata: name form (initials-only vs forename) x surname frequency
tercile x government bucket; up to CAP per stratum, seeded RNG.

Outputs:
  data/iol/identity/adjudicate/wl_chain.jsonl   sample worklist
  data/iol/identity/nobio_chain_frame.json      stratum weights for the
                                                Wilson-CI measure step
"""

from __future__ import annotations

import json
import random
import re
from collections import Counter, defaultdict
from glob import glob
from pathlib import Path

ROOT = Path("data/iol")
IDD = ROOT / "identity"
CAP = 25
SEED = 42

_BIG = {"BENGAL", "MADRAS", "BOMBAY", "PUNJAB", "BURMA",
        "UNITED PROVINCES OF AGRA AND OUDH", "GOVERNMENT OF INDIA"}


def gov_bucket(gov: str | None) -> str:
    if gov == "INDIA OFFICE (LONDON)":
        return "india_office"
    if gov == "GOVERNMENT OF INDIA":
        return "goi"
    return "big_prov" if gov in _BIG else "small_prov"


def name_form(name: str) -> str:
    toks = [t.strip(".") for t in (name or "").split()][:-1]
    return "forename" if any(len(re.sub(r"[^A-Za-z]", "", t)) > 2
                             for t in toks) else "initials"


def main() -> None:
    chains = [json.loads(l) for l in
              open(IDD / "nobio_civil_chains.jsonl", encoding="utf-8")]
    frame = [c for c in chains if c["n_records"] >= 2]

    sur_n = Counter(c["surname_key"] for c in frame)
    cuts = sorted(sur_n[c["surname_key"]] for c in frame)
    t1 = cuts[len(cuts) // 3]
    t2 = cuts[2 * len(cuts) // 3]

    def stratum(c: dict) -> str:
        n = sur_n[c["surname_key"]]
        freq = "lo" if n <= t1 else "mid" if n <= t2 else "hi"
        return f"{name_form(c['name'])}:{freq}:{gov_bucket(c['government'])}"

    by_stratum = defaultdict(list)
    for c in frame:
        by_stratum[stratum(c)].append(c)

    rng = random.Random(SEED)
    sample = []
    for st in sorted(by_stratum):
        pool = by_stratum[st]
        take = pool if len(pool) <= CAP else rng.sample(pool, CAP)
        for c in take:
            sample.append((st, c))

    # re-hydrate the printed records; the join key needs the line
    # index — coholders on one office line share char_offset
    want = {}
    for st, c in sample:
        for tag, off, ln in c["records"]:
            want[(tag, ln)] = None
    for f in sorted(glob(str(ROOT / "civil/civil_1[89]*.jsonl"))):
        for i, l in enumerate(open(f, encoding="utf-8")):
            r = json.loads(l)
            k = (r["edition_tag"], i)
            if k in want:
                want[k] = r

    with open(IDD / "adjudicate/wl_chain.jsonl", "w",
              encoding="utf-8") as fh:
        for st, c in sample:
            lines = [f"chain: {c['name']} — government: "
                     f"{c['government']} — listed "
                     f"{c['years'][0]}-{c['years'][1]}"]
            for tag, off, ln in c["records"]:
                r = want.get((tag, ln))
                if not r:
                    continue
                bits = [str(r["edition_year"]),
                        r.get("office") or "?"]
                if r.get("department"):
                    bits.append(f"dept: {r['department'][:50]}")
                if r.get("branch"):
                    bits.append(f"branch: {r['branch'][:40]}")
                if r.get("honours"):
                    bits.append("hons: " + ",".join(r["honours"][:4]))
                bits.append(f"printed: {r.get('name')}")
                lines.append("  " + " | ".join(bits))
            note = None
            if c["n_records"] > len(c["records"]):
                note = (f"({c['n_records'] - len(c['records'])} further "
                        "records truncated)")
            fh.write(json.dumps({
                "id": f"chs::{c['chain_id']}", "pool": "chain_sample",
                "career_id": c["chain_id"], "stratum": st,
                "lines": lines, "note": note,
            }, ensure_ascii=False) + "\n")

    weights = Counter(st for st in
                      (stratum(c) for c in frame))
    json.dump({"frame": len(frame), "singletons":
               len(chains) - len(frame), "cap": CAP, "seed": SEED,
               "tercile_cuts": [t1, t2],
               "weights": dict(weights),
               "sampled": Counter(st for st, _ in sample)},
              open(IDD / "nobio_chain_frame.json", "w"), indent=1)
    print(f"frame {len(frame):,} multi-record chains "
          f"({len(chains) - len(frame):,} singletons trivially one "
          f"person); sampled {len(sample)} across "
          f"{len(by_stratum)} strata -> wl_chain.jsonl")


if __name__ == "__main__":
    main()
