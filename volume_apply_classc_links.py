#!/usr/bin/env python3
"""Apply the verified stratum of class-C adjudication verdicts as
career -> bio-person links.

The Qwen pass judged 13,123 (career, person) pairs "same". Sample review
(34 pairs read closely, July 2026) found every false positive shares one
machine-checkable trait: the career's given-name initials are NOT exactly
the person's initials (subsequence stretch — "N. C. H" vs "C. H.", "J" vs
"James Alfred"); every pair passing the exact-initials test was correct.
Deterministic corroboration tiers (recomputed here, no LLM trust needed):

  hard     person has an event in the career colony within the roster
           window AND a position matching the roster position (sim>=60)
  place    in-colony, in-window event
  possim   position match >=75 in-window (place unresolvable)
  llm_only no deterministic corroboration (gazetteer misses, event gaps)

Auto-apply policy (0 observed FPs in sample):
  tier1  exact initials + hard/place/possim corroboration
  tier2  exact initials + llm_only + rare surname (<30 bio persons)
  tier3  skeptic-pass promotion: held pairs re-judged by a reject-by-default
         prompt (classc_skeptic_results.jsonl) that must QUOTE the matching
         appointment; promoted only when the quote grounds in the person's
         events AND colony/position corroborates (10/10 sample-verified —
         mostly used-middle-name cases the exact-initials guard rightly held)
  tier3 is gated to det=hard (2026-09-04): the silver standard measured
         apply_t3 at 79% precision (11/14) with every FP outside the hard
         (place AND position) stratum — place-only / possim tier3 pairs
         now stay in review.
  hand   classc_hand_verdicts.jsonl (volume_silver_to_ledger.py) outranks the
         machine policy: verdict 'different' suppresses a pair whatever the
         judge said; verdict 'same' applies it as policy apply_hand.
  Careers matching >1 distinct person are demoted to review.
Everything else -> classc_review_queue.jsonl, resolution "not_linked" —
FINAL under this policy, no human review required (unlinked is the
conservative direction).

Outputs (data/volume/classc/):
  career_person_links.jsonl   applied links (career_id -> person_id + evidence)
  classc_review_queue.jsonl   held pairs, hardest-evidence first
  CLASSC_LINKS.md             policy, verification note, link-rate lift

Usage: python3 volume_apply_classc_links.py
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from rapidfuzz import fuzz

from col_match.config import Config
from col_match.volume.match import _colony_target_set

CLASSDIR = Path("data/volume/classc")
VOLROOT = Path("data/volume")
SAME_CONF = 70
RARE_SURNAME = 30
POS_HARD, POS_ONLY = 60, 75


def initials(g: str | None) -> tuple[str, ...]:
    return tuple(t[0].upper() for t in re.split(r"[ .]+", (g or ""))
                 if t and t[0].isalpha())


def given_of(name: str) -> str:
    return name.split(",", 1)[1] if "," in name else ""


def main() -> None:
    data_dir = Config.from_env().data_dir
    _tc: dict[str, frozenset[str]] = {}

    def targets(raw: str | None) -> frozenset[str]:
        key = (raw or "").strip()
        if key not in _tc:
            _tc[key] = frozenset(_colony_target_set(key, data_dir))
        return _tc[key]

    pairs = {json.loads(l)["id"]: json.loads(l)
             for l in (CLASSDIR / "classc_worklist.jsonl").open(encoding="utf-8")}
    persons = {}
    for l in (VOLROOT / "bio_persons" / "bio_persons.jsonl").open(encoding="utf-8"):
        p = json.loads(l)
        persons[p["person_id"]] = p
    # worklist/results may predate applied under-merges: absorbed -> canonical
    canon: dict[str, str] = {}
    merges = VOLROOT / "bio_persons" / "person_id_merges.jsonl"
    if merges.exists():
        for l in merges.open(encoding="utf-8"):
            m = json.loads(l)
            canon[m["absorbed_id"]] = m["person_id"]
    surfreq = Counter(re.sub(r"[^a-z]", "", (p.get("surname") or "").lower())
                      for p in persons.values())

    # hand-verdict ledger outranks the judge (accumulative, append-only)
    hand: dict[str, str] = {}
    ledger = CLASSDIR / "classc_hand_verdicts.jsonl"
    if ledger.exists():
        for l in ledger.open(encoding="utf-8"):
            h = json.loads(l)
            hand[h["id"]] = h["verdict"]

    sames, seen_ids = [], set()
    for l in (CLASSDIR / "classc_results.jsonl").open(encoding="utf-8"):
        r = json.loads(l)
        if hand.get(r["id"]) == "different":
            continue
        if (r.get("verdict") == "same" and (r.get("confidence") or 0) >= SAME_CONF) \
                or hand.get(r["id"]) == "same":
            sames.append(r); seen_ids.add(r["id"])
    for pid, v in hand.items():          # hand 'same' with no judge row at all
        if v == "same" and pid not in seen_ids and pid in pairs:
            car, per = pid.split("::", 1)
            sames.append({"id": pid, "career_id": car, "person_id": per,
                          "verdict": "same", "confidence": None, "reason": "hand"})
    n_hand_diff = sum(1 for v in hand.values() if v == "different")

    scored = []
    for v in sames:
        if v["id"] not in pairs:      # verdict from a superseded worklist
            continue                  # generation (results files accumulate)
        pr = pairs[v["id"]]
        v["person_id"] = canon.get(v["person_id"], v["person_id"])
        car, per = pr["career"], persons[v["person_id"]]
        y0, y1 = car["roster_years"][0], car["roster_years"][-1]
        ct = targets(car["colony"])
        car_positions = [l.split("|")[1].strip() for l in car["lines"] if "|" in l]
        place_hit, pos_hit = False, 0
        for ev in per["events"]:
            ys = ev.get("year_start")
            in_win = ys is not None and y0 - 3 <= ys <= y1 + 2
            if not in_win:
                continue
            if ev.get("place") and (targets(ev["place"]) & ct):
                place_hit = True
            if car_positions and ev.get("position"):
                pos_hit = max(pos_hit, max(
                    fuzz.token_set_ratio(ev["position"], cp)
                    for cp in car_positions[:6]))
        det = ("hard" if place_hit and pos_hit >= POS_HARD else
               "place" if place_hit else
               "possim" if pos_hit >= POS_ONLY else "llm_only")
        exact = (initials(given_of(car["name"])) ==
                 initials(given_of(pr["person"]["name"])) != ())
        freq = surfreq[re.sub(r"[^a-z]", "", (per.get("surname") or "").lower())]
        if hand.get(v["id"]) == "same":
            policy = "apply_hand"
        elif exact and det in ("hard", "place", "possim"):
            policy = "apply_t1"
        elif exact and freq < RARE_SURNAME:
            policy = "apply_t2"
        else:
            policy = "review"
        scored.append({
            "id": v["id"], "career_id": v["career_id"],
            "person_id": v["person_id"], "policy": policy, "det_tier": det,
            "exact_initials": exact, "surname_freq": freq,
            "pos_sim": pos_hit, "llm_confidence": v.get("confidence"),
            "llm_reason": v.get("reason"),
        })

    # tier3: skeptic-pass promotion of held pairs (grounded quote + corroboration)
    skeptic = CLASSDIR / "classc_skeptic_results.jsonl"
    if skeptic.exists():
        by_id = {s["id"]: s for s in scored}
        for line in skeptic.open(encoding="utf-8"):
            r = json.loads(line)
            s = by_id.get(r["id"])
            if s is None or s["policy"] != "review" or r.get("verdict") != "confirm":
                continue
            evd = (r.get("evidence") or "").strip().lower()
            per = persons[s["person_id"]]
            grounded = len(evd) >= 8 and any(
                fuzz.partial_ratio(evd, ((e.get("position") or "") + " " +
                                         (e.get("place") or "")).lower()) >= 75
                for e in per["events"])
            if grounded and s["det_tier"] == "hard":
                s["policy"] = "apply_t3"
                s["skeptic_evidence"] = r.get("evidence")

    # careers matched to >1 distinct person -> all their pairs go to review
    per_car = defaultdict(set)
    for s in scored:
        if s["policy"].startswith("apply"):
            per_car[s["career_id"]].add(s["person_id"])
    ambiguous = {c for c, ps in per_car.items() if len(ps) > 1}
    for s in scored:
        if s["career_id"] in ambiguous and s["policy"].startswith("apply"):
            s["policy"] = "review_ambiguous"

    applied, seen = [], set()
    for s in scored:
        if not s["policy"].startswith("apply"):
            continue
        key = (s["career_id"], s["person_id"])   # merged persons can collapse
        if key in seen:                          # two pairs into one link
            continue
        seen.add(key)
        applied.append(s)
    review = [s for s in scored if not s["policy"].startswith("apply")]
    review.sort(key=lambda s: (s["policy"], -(s["pos_sim"] or 0)))

    with (CLASSDIR / "career_person_links.jsonl").open("w", encoding="utf-8") as fh:
        for s in applied:
            fh.write(json.dumps(s, ensure_ascii=False) + "\n")
    with (CLASSDIR / "classc_review_queue.jsonl").open("w", encoding="utf-8") as fh:
        for s in review:
            fh.write(json.dumps(s, ensure_ascii=False) + "\n")

    # ------------------------------------------------------------- report
    n_careers_ok = n_prelinked = 0
    for l in (VOLROOT / "careers" / "careers.jsonl").open(encoding="utf-8"):
        c = json.loads(l)
        if c.get("suspect"):
            continue
        n_careers_ok += 1
        if c.get("bio_ids"):
            n_prelinked += 1
    linked_careers = {s["career_id"] for s in applied}
    pol = Counter(s["policy"] for s in scored)
    det = Counter(s["det_tier"] for s in applied)
    lines = [
        "# Applied class-C links (career -> bio person)",
        "",
        f"- 'same' verdicts scored: {len(scored):,}",
        f"- applied: {len(applied):,} pairs / {len(linked_careers):,} careers "
        f"(tier1 {pol['apply_t1']:,}, tier2 {pol['apply_t2']:,}, "
        f"tier3 skeptic/hard {pol['apply_t3']:,}, hand {pol['apply_hand']:,}); "
        f"corroboration {dict(det)}",
        f"- hand-ledger suppressions (silver-refuted links): {n_hand_diff}",
        f"- not linked (FINAL under this policy — no review required): "
        f"{len(review):,} (ambiguous careers: {len(ambiguous):,})",
        "",
        "## Verification basis",
        "",
        "34 pairs read closely across strata + 10/10 skeptic-tier promotions",
        "verified (July 2026); 200-item silver standard 2026-07-12 (NOBIO_SILVER.md):",
        "t1 28/28, t2 7/7, t3 11/14 -> t3 gated to det=hard 2026-09-04, the",
        "three refuted t3 links suppressed via the hand ledger.",
        "Every earlier false positive failed the exact-initials",
        "test; every policy-passing pair was correct (0 observed FPs in the",
        "applied strata). LLM confidence is uniform (90-95) and was NOT used;",
        "corroboration is recomputed deterministically; tier3 additionally",
        "requires the skeptic's quoted appointment to ground in the person's",
        "events.",
        "",
        "## Link-rate lift (roster careers with a bio identity)",
        "",
        f"- before: {n_prelinked:,} / {n_careers_ok:,} careers "
        f"({100*n_prelinked/n_careers_ok:.1f}%)",
        f"- after:  {n_prelinked + len(linked_careers):,} / {n_careers_ok:,} "
        f"({100*(n_prelinked+len(linked_careers))/n_careers_ok:.1f}%)",
        "",
        "Links are an OVERLAY (career_person_links.jsonl) joining careers.jsonl",
        "on career_id; careers.jsonl itself is untouched (it stays the product",
        "of the within-volume linker).",
    ]
    (CLASSDIR / "CLASSC_LINKS.md").write_text("\n".join(lines) + "\n",
                                              encoding="utf-8")
    print(f"applied {len(applied):,} pairs -> {len(linked_careers):,} careers; "
          f"review {len(review):,}; ambiguous {len(ambiguous):,}")
    print(f"-> {CLASSDIR}/CLASSC_LINKS.md")


if __name__ == "__main__":
    main()
