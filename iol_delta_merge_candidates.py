#!/usr/bin/env python3
"""Stage-3 dedup for DELTA structured records (bios-fix cycle): ids that
entered the corpus after the last full dedup (never saw the four merge
passes) get candidate pairs against the whole corpus, rendered for
`qwen_classc_worker.py --mode ioldedup`. Judged 'same' verdicts become
`add` rows in merge_decisions.jsonl (iol_apply_adjudication.py handles
that), which iol_merge_apply.py folds into the audited map — the
ledger-driven map build extends naturally, no pass rerun needed.

  python3 iol_delta_merge_candidates.py
  -> data/iol/identity/adjudicate/wl_delta_dedup.jsonl
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from iol_merge_audit import award_key, posstem, rec_lines, surname_key

ROOT = Path("data/iol")
IDD = ROOT / "identity"
ADJ = IDD / "adjudicate"

MAX_PAIRS_PER_ID = 4


def jload(path):
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            yield json.loads(line)


def name_toks(g):
    return [t for t in re.split(r"[ .]+", g or "") if t]


def initials(toks):
    return "".join(t[0].upper() for t in toks if t and t[0].isalpha())


def compatible(ga, gb) -> bool:
    ta, tb = name_toks(ga), name_toks(gb)
    if not ta or not tb:
        return True          # absence is not contradiction (IOL prompt)
    ia, ib = initials(ta), initials(tb)
    if not (ia == ib or ia.startswith(ib) or ib.startswith(ia)):
        return False
    wa = [t.upper() for t in ta if len(t) > 2]
    wb = [t.upper() for t in tb if len(t) > 2]
    return not (wa and wb and wa[0] != wb[0])


def postings(rec):
    out = set()
    for e in rec.get("events") or []:
        y = e.get("year_start")
        st = posstem(e.get("position"))
        if y and len(st) >= 4:
            out.add((st, y))
    return out


def honour_set(rec):
    return {(award_key(h.get("award")), h["year"])
            for h in (rec.get("honours") or [])
            if h.get("year") and award_key(h.get("award"))}


def main() -> None:
    recs = {r["person_id"]: r for r in
            jload(ROOT / "llm_struct_corpus.valid.jsonl")}
    editions = {r["person_id"]: r.get("editions") or []
                for r in jload(ROOT / "persons.deduped.jsonl")}
    old_ids = set(json.load(open(IDD / "struct_old_corpus_ids.json")))
    delta = [pid for pid in recs if pid not in old_ids]
    print(f"corpus {len(recs):,}; delta (never deduped): {len(delta):,}")

    by_key = defaultdict(list)
    for pid, r in recs.items():
        by_key[surname_key(r.get("surname"))].append(pid)
        full = surname_key((r.get("given_names") or "")
                           + (r.get("surname") or ""))
        if full and full != surname_key(r.get("surname")):
            by_key[full].append(pid)

    def side(pid):
        r = recs[pid]
        eds = editions.get(pid) or []
        return {"name": f"{r.get('surname') or '?'}, "
                        f"{r.get('given_names') or '?'}",
                "birth_year": r.get("birth_year"),
                "honours": [f"{h.get('award')}"
                            + (f" ({h['year']})" if h.get("year") else "")
                            for h in (r.get("honours") or [])][:10],
                "editions": [min(eds), max(eds)] if eds else None,
                "lines": rec_lines(r)}

    stats = Counter()
    rows, seen_pairs = [], set()
    for pid in sorted(delta):
        a = recs[pid]
        pa, ha = postings(a), honour_set(a)
        ya = {y for _, y in pa}
        cands = []
        keys = {surname_key(a.get("surname")),
                surname_key((a.get("given_names") or "")
                            + (a.get("surname") or ""))}
        pool = {q for k in keys if k for q in by_key.get(k, [])} - {pid}
        for q in pool:
            b = recs[q]
            if not compatible(a.get("given_names"), b.get("given_names")):
                continue
            ba, bb = a.get("birth_year"), b.get("birth_year")
            if ba and bb and abs(ba - bb) > 15:
                continue
            pb, hb = postings(b), honour_set(b)
            score = 0
            if ba and bb and abs(ba - bb) <= 1:
                score += 30
            if ha & hb:
                score += 30
            if pa & pb:
                score += 30
            elif ya & {y for _, y in pb}:
                score += 5
            if len(by_key.get(surname_key(a.get("surname")), [])) <= 3:
                score += 10
            if score >= 15:
                cands.append((score, q))
        cands.sort(reverse=True)
        for score, q in cands[:MAX_PAIRS_PER_ID]:
            key = tuple(sorted((pid, q)))
            if key in seen_pairs:
                continue
            seen_pairs.add(key)
            stats["pairs"] += 1
            rows.append({"id": f"delta::{pid}::{q}", "pool": "delta_dedup",
                         "person_a": pid, "person_b": q,
                         "a": side(pid), "b": side(q)})
        if not cands:
            stats["no_candidate"] += 1

    ADJ.mkdir(parents=True, exist_ok=True)
    with open(ADJ / "wl_delta_dedup.jsonl", "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{stats['pairs']:,} candidate pairs "
          f"({stats['no_candidate']:,} delta ids with none) -> "
          f"{ADJ / 'wl_delta_dedup.jsonl'}")
    print("judge: qwen_classc_worker.py --mode ioldedup; then "
          "iol_apply_adjudication.py consumes res_delta_dedup.jsonl")


if __name__ == "__main__":
    main()
