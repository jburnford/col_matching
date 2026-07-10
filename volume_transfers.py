#!/usr/bin/env python3
"""Cross-colony transfer detection over strung roster careers — aimed at the
LOWER RANKS ('careering including the people who never careered').

The naive join (same surname + compatible initials + timing) is only ~72%
precise: namesakes dominate. This scorer adds corroborators, each observable
WITHOUT a biography:

  name specificity   >=2 initials, or a full forename shared verbatim
  surname rarity     corpus frequency of the surname across all careers
  salary continuity  scale at B's start vs scale at A's end (log-ratio)
  rank continuity    salary class equal or one step up at the move
  position affinity  fuzz token_set_ratio between A's last / B's first
                     position+department strings
  honours overlap    any shared honour string
  timing             gap in edition-years; -1 (transition-year overlap) to +3

Calibration: pairs where BOTH careers carry within-volume bio links are
decidable — same bio_id anywhere = same person; different bio_ids in the SAME
edition = different persons. Tier thresholds are chosen so the CONFIRMED tier
is >=90% precise on the decidable set.

Outputs (data/volume/careers/):
  transfers.jsonl     scored candidate pairs (all tiers)
  TRANSFERS.md        calibration + lower-rank analysis report

Usage: python3 volume_transfers.py
"""

from __future__ import annotations

import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

from rapidfuzz import fuzz

from col_match.services.match import _initials, _names_compatible

ROOT = Path("data/volume/careers")

_AMT = re.compile(r"([\d,]+)\s*(?:l\.|£|/)")


def salary_range(s: str | None) -> tuple[int, int] | None:
    if not s:
        return None
    amts = [int(d) for d in (a.replace(",", "") for a in _AMT.findall(s)) if d]
    amts = [a for a in amts if 20 <= a <= 20000]
    return (amts[0], max(amts)) if amts else None


def rank_class(peak: int | None) -> str | None:
    if peak is None:
        return None
    return ("subordinate" if peak < 100 else "clerical" if peak < 400
            else "officer" if peak < 1000 else "senior")


RANK_ORD = {"subordinate": 0, "clerical": 1, "officer": 2, "senior": 3}


def _end_salary(c: dict) -> int | None:
    """Scale top in the career's final salaried year."""
    for r in reversed(c["records"]):
        sr = salary_range(r["salary"])
        if sr:
            return sr[1]
    return None


def _start_salary(c: dict) -> int | None:
    for r in c["records"]:
        sr = salary_range(r["salary"])
        if sr:
            return sr[1]
    return None


def _pos_blob(c: dict, first: bool) -> str:
    recs = c["records"] if first else list(reversed(c["records"]))
    for r in recs:
        blob = " ".join(filter(None, [r.get("position"), r.get("department")]))
        if blob.strip():
            return blob
    return ""


def _full_forenames(g: str | None) -> set[str]:
    return {t.strip(".").lower() for t in (g or "").split()
            if len(t.strip(".")) > 2 and t[0].isupper()}


def score_pair(a: dict, b: dict, surfreq: Counter) -> dict:
    """Corroborator features + a transparent tier."""
    ini = min(len(_initials(a["given_names"])), len(_initials(b["given_names"])))
    shared_full = _full_forenames(a["given_names"]) & _full_forenames(b["given_names"])
    rarity = surfreq[a["surname"]]

    sal_a, sal_b = _end_salary(a), _start_salary(b)
    if sal_a and sal_b:
        sal_ratio = abs(math.log(sal_b / sal_a))
        sal_ok = sal_ratio <= math.log(2.0)         # within 2x either way
        rk_a, rk_b = RANK_ORD[rank_class(sal_a)], RANK_ORD[rank_class(sal_b)]
        rank_ok = -1 <= rk_b - rk_a <= 1
    else:
        sal_ratio, sal_ok, rank_ok = None, None, None

    pos_sim = fuzz.token_set_ratio(_pos_blob(a, first=False).lower(),
                                   _pos_blob(b, first=True).lower())
    hon_a = {h for r in a["records"] for h in r["honours"]}
    hon_b = {h for r in b["records"] for h in r["honours"]}
    honours = bool(hon_a & hon_b)
    gap = b["years"][0] - a["years"][-1]

    name_strong = ini >= 2 or bool(shared_full)
    corrobs = sum([bool(sal_ok), bool(rank_ok), pos_sim >= 55, honours,
                   rarity <= 10])
    hard_contra = (sal_ok is False and pos_sim < 40 and not honours)

    if hard_contra:
        tier = "rejected"
    elif name_strong and rarity <= 25 and corrobs >= 2:
        tier = "confirmed"
    elif name_strong and corrobs >= 2 and (rarity <= 100 or pos_sim >= 55):
        # salary/rank continuity alone is near-vacuous (usually true); demand
        # a rare surname or real position affinity — calibration showed
        # common-surname pairs riding on salary alone are ~60% namesakes
        tier = "probable"
    elif name_strong or corrobs >= 2:
        tier = "possible"
    else:
        tier = "weak"

    return {"ini": ini, "shared_forename": sorted(shared_full),
            "surname_freq": rarity,
            "salary_end_a": sal_a, "salary_start_b": sal_b,
            "salary_ok": sal_ok, "rank_ok": rank_ok,
            "pos_sim": pos_sim, "honours_shared": honours, "gap": gap,
            "corroborators": corrobs, "tier": tier}


# Administrative successions: the CHAPTER moved, not (necessarily) the person.
# A pair on these routes is staff continuity through reorganization — real and
# historically interesting, but not personal mobility. Direction = (from, to).
REORG_ROUTES = {
    ("LAGOS", "SOUTHERN NIGERIA"),                       # 1906 amalgamation
    ("SOUTHERN NIGERIA", "NIGERIA"), ("NORTHERN NIGERIA", "NIGERIA"),  # 1914
    ("CAPE OF GOOD HOPE", "SOUTH AFRICA"), ("NATAL", "SOUTH AFRICA"),  # 1910
    ("TRANSVAAL", "SOUTH AFRICA"), ("ORANGE RIVER COLONY", "SOUTH AFRICA"),
    ("ZULULAND", "NATAL"),                               # 1898
    ("GRIQUALAND WEST", "CAPE OF GOOD HOPE"),            # 1880
    ("BRITISH BECHUANALAND", "CAPE OF GOOD HOPE"),       # 1895
    ("TOBAGO", "TRINIDAD AND TOBAGO"),                   # 1889
    ("WINDWARD ISLANDS", "TOBAGO"), ("TOBAGO", "WINDWARD ISLANDS"),
    ("WEST AFRICA SETTLEMENTS", "SIERRA LEONE"),         # 1888 split
    ("WEST AFRICA SETTLEMENTS", "GOLD COAST"),
    ("WEST AFRICA SETTLEMENTS", "GAMBIA"),
    ("WEST AFRICA SETTLEMENTS", "LAGOS"),
    ("FEDERATED MALAY STATES", "FEDERATION OF MALAYA"),  # 1948
    ("STRAITS SETTLEMENTS", "SINGAPORE"),                # 1946
    ("STRAITS SETTLEMENTS", "FEDERATION OF MALAYA"),
}

_POSITION_WORDS = {
    "lecturer", "master", "matron", "keeper", "printer", "surveyor", "usher",
    "chaplain", "organist", "librarian", "curator", "gardener", "steward",
    "teacher", "clerk", "officer", "inspector", "superintendent", "engineer",
    "classical", "assistant", "senior", "junior", "chief", "deputy", "acting",
}


def _dept_key(c: dict, first: bool) -> str:
    recs = c["records"] if first else list(reversed(c["records"]))
    for r in recs:
        if r.get("department"):
            return " ".join(re.findall(r"[a-z]+", r["department"].lower()))
    return ""


def chapter_ranks() -> dict[int, dict[str, int]]:
    """edition year -> canonical colony -> chapter rank (order by median page).
    Used to catch running-header bleed: a 'transfer' between chapters that sit
    NEXT TO EACH OTHER in the volume is presumed to be the same rows under a
    misassigned header when the job text is near-identical."""
    canon = json.loads((ROOT / "colony_canon.json").read_text())
    pages: dict[int, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    for d in sorted(ROOT.parent.glob("col*")):
        if not d.is_dir():
            continue
        year = int(d.name[3:])
        for line in open(d / "records.jsonl", encoding="utf-8"):
            r = json.loads(line)
            col = canon.get(r["colony"])
            pg = (r.get("provenance") or {}).get("page")
            if col and pg is not None:
                pages[year][col].append(pg)
        ranks = {}
        med = {c: sorted(ps)[len(ps) // 2] for c, ps in pages[year].items()}
        for i, c in enumerate(sorted(med, key=med.get)):
            ranks[c] = i
        pages[year] = ranks                      # type: ignore[assignment]
    return pages                                  # type: ignore[return-value]


def artifact_check(a: dict, b: dict, pos_sim: float,
                   dept_colony: dict[str, Counter],
                   ranks: dict[int, dict[str, int]]) -> str | None:
    """Two artifact classes that perfectly mimic corroboration:
    (1) boilerplate rows misparsed as persons ('Lecturer, Classical') pairing
        with themselves across colonies;
    (2) running-header bleed at alphabetical chapter boundaries — the row
        never moved, its page just got the neighbouring colony's header.
        Signature: near-identical position AND the receiving side's department
        text is overwhelmingly attested under the SENDING colony corpus-wide
        (or vice versa)."""
    name_toks = {t.strip(".,").lower()
                 for t in f"{a['given_names'] or ''} {a['surname']}".split()}
    if name_toks & _POSITION_WORDS:
        return "nonperson_name"
    if pos_sim >= 85:
        # near-identical job + chapters adjacent in the volume around the
        # transition = same rows, wrong running header
        for year in (a["years"][-1], b["years"][0]):
            rk = ranks.get(year, {})
            ra, rb = rk.get(a["colony"]), rk.get(b["colony"])
            if ra is not None and rb is not None and abs(ra - rb) <= 2:
                return "page_adjacent"
    if pos_sim >= 90:
        for c, here, there in ((b, b["colony"], a["colony"]),
                               (a, a["colony"], b["colony"])):
            dk = _dept_key(c, first=(c is b))
            if not dk:
                continue
            freq = dept_colony.get(dk)
            if freq and freq[there] >= 5 * max(freq[here], 1) and freq[there] >= 10:
                return "header_bleed"
    return None


def ground_truth(a: dict, b: dict) -> bool | None:
    """True/False when decidable from bio links, else None."""
    if not (a["bio_ids"] and b["bio_ids"]):
        return None
    if set(a["bio_ids"]) & set(b["bio_ids"]):
        return True
    ya = {bid.split("-")[0]: bid for bid in a["bio_ids"]}
    yb = {bid.split("-")[0]: bid for bid in b["bio_ids"]}
    shared_eds = set(ya) & set(yb)
    if shared_eds and all(ya[e] != yb[e] for e in shared_eds):
        return False
    return None


def main() -> None:
    careers = [json.loads(l) for l in open(ROOT / "careers.jsonl", encoding="utf-8")]
    ok = [c for c in careers if not c["suspect"] and c["n_editions"] >= 2]
    surfreq = Counter(c["surname"] for c in careers if not c["suspect"])

    # corpus-wide department-text -> colony attestation (for header-bleed test)
    dept_colony: dict[str, Counter] = defaultdict(Counter)
    for c in careers:
        if c["suspect"]:
            continue
        for r in c["records"]:
            if r.get("department"):
                dk = " ".join(re.findall(r"[a-z]+", r["department"].lower()))
                dept_colony[dk][c["colony"]] += 1

    ranks = chapter_ranks()

    by_surname = defaultdict(list)
    for c in ok:
        by_surname[c["surname"]].append(c)

    pairs = []
    for sur, group in by_surname.items():
        if len(group) < 2:
            continue
        group.sort(key=lambda c: c["years"][0])
        for a in group:
            for b in group:
                if a is b or a["colony"] == b["colony"]:
                    continue
                gap = b["years"][0] - a["years"][-1]
                if not (-1 <= gap <= 3):
                    continue
                if not (_initials(a["given_names"]) and _initials(b["given_names"])):
                    continue
                if not _names_compatible(a["given_names"], b["given_names"]):
                    continue
                feats = score_pair(a, b, surfreq)
                art = artifact_check(a, b, feats["pos_sim"], dept_colony, ranks)
                if art:
                    feats["tier"] = "artifact"
                elif (a["colony"], b["colony"]) in REORG_ROUTES:
                    feats["tier"] = "reorg"
                feats["artifact"] = art
                gt = ground_truth(a, b)
                pairs.append({
                    "surname": a["surname"], "given_a": a["given_names"],
                    "given_b": b["given_names"],
                    "from_colony": a["colony"], "to_colony": b["colony"],
                    "from_years": [a["years"][0], a["years"][-1]],
                    "to_years": [b["years"][0], b["years"][-1]],
                    "from_career": a["career_id"], "to_career": b["career_id"],
                    "from_pos": _pos_blob(a, first=False)[:80],
                    "to_pos": _pos_blob(b, first=True)[:80],
                    "rank_at_move": rank_class(_end_salary(a)),
                    "bio_linked": bool(a["bio_ids"] or b["bio_ids"]),
                    "ground_truth": gt, **feats,
                })

    # ambiguity guard (0-FP discipline): a person transfers to at most ONE
    # place — a career appearing in >1 same-tier pair on either end means the
    # corroborators can't tell the candidates apart; demote them all.
    for tier in ("confirmed", "probable"):
        ends: Counter = Counter()
        for p in pairs:
            if p["tier"] == tier:
                ends[("f", p["from_career"])] += 1
                ends[("t", p["to_career"])] += 1
        for p in pairs:
            if p["tier"] == tier and (ends[("f", p["from_career"])] > 1
                                      or ends[("t", p["to_career"])] > 1):
                p["tier"] = "ambiguous"

    with (ROOT / "transfers.jsonl").open("w", encoding="utf-8") as fh:
        for p in pairs:
            fh.write(json.dumps(p, ensure_ascii=False) + "\n")

    # ------------------------------------------------------------- calibration
    lines = ["# Cross-colony transfer candidates — scored & calibrated", "",
             f"- candidate pairs (>=2 eds both sides, initials both sides, "
             f"gap -1..+3): {len(pairs):,}", "",
             "## Calibration on bio-decidable pairs", "",
             "| tier | decidable | same person | precision | all pairs |",
             "|---|---|---|---|---|"]
    for tier in ("confirmed", "probable", "ambiguous", "possible", "weak",
                 "rejected", "reorg", "artifact"):
        tp_ = [p for p in pairs if p["tier"] == tier]
        dec = [p for p in tp_ if p["ground_truth"] is not None]
        tp = sum(1 for p in dec if p["ground_truth"])
        prec = f"{100*tp/len(dec):.0f}%" if dec else "—"
        lines.append(f"| {tier} | {len(dec)} | {tp} | {prec} | {len(tp_):,} |")

    # ------------------------------------------- lower-rank careering analysis
    conf = [p for p in pairs if p["tier"] == "confirmed"]
    lower = [p for p in conf if p["rank_at_move"] in ("subordinate", "clerical")]
    lower_nobio = [p for p in lower if not p["bio_linked"]]
    lines += ["", "## Lower-rank careering (rank at move below the £400 line)", "",
              f"- confirmed transfers: {len(conf):,}; of these at "
              f"subordinate/clerical rank: {len(lower):,} "
              f"({len(lower_nobio):,} with NO bio link on either side)", ""]
    by_route = Counter((p["from_colony"], p["to_colony"]) for p in lower)
    lines += ["top lower-rank routes:", ""]
    for (f, t), n in by_route.most_common(12):
        lines.append(f"- {f} -> {t}: {n}")
    lines += ["", "sample confirmed lower-rank, bio-less transfers:", ""]
    for p in sorted(lower_nobio, key=lambda p: -p["corroborators"])[:15]:
        lines.append(
            f"- **{p['surname'].title()}, {p['given_a']}** "
            f"{p['from_colony']} {p['from_years'][0]}–{p['from_years'][1]} "
            f"[{p['from_pos'][:45]}] → {p['to_colony']} "
            f"{p['to_years'][0]}–{p['to_years'][1]} [{p['to_pos'][:45]}] "
            f"(£{p['salary_end_a']}→£{p['salary_start_b']}, pos~{p['pos_sim']}, "
            f"snfreq {p['surname_freq']})")

    # ------------------------------------ reorg continuity (reported separately)
    reorg = [p for p in pairs if p["tier"] == "reorg"]
    lines += ["", "## Administrative-reorganization continuity (not personal mobility)",
              "", f"- pairs on succession routes: {len(reorg):,}"]
    for (f, t), n in Counter((p["from_colony"], p["to_colony"])
                             for p in reorg).most_common(8):
        lines.append(f"- {f} -> {t}: {n}")

    # -------------------------- the other lower-rank careering: ascent in place
    lines += ["", "## Within-colony rank ascent (careering without moving)", "",
              "careers entering below the £400 line whose peak crosses it:", ""]
    asc = Counter()
    tot = Counter()
    for c in careers:
        if c["suspect"] or c["n_editions"] < 2:
            continue
        sals = [salary_range(r["salary"]) for r in c["records"]]
        sals = [s for s in sals if s]
        if not sals:
            continue
        entry, peak = sals[0][1], max(hi for _, hi in sals)
        if rank_class(entry) in ("subordinate", "clerical"):
            tot[c["colony"]] += 1
            if RANK_ORD[rank_class(peak)] >= RANK_ORD["officer"]:
                asc[c["colony"]] += 1
    lines.append(f"- total: {sum(asc.values()):,} of {sum(tot.values()):,} "
                 f"below-£400 entrants ({100*sum(asc.values())/max(sum(tot.values()),1):.1f}%) "
                 f"reach the officer scale within the same colony")
    lines.append("")
    lines.append("| colony | below-£400 entrants | ascend past £400 | rate |")
    lines.append("|---|---|---|---|")
    for col, n in tot.most_common(15):
        lines.append(f"| {col} | {n:,} | {asc[col]:,} | {100*asc[col]/n:.1f}% |")

    (ROOT / "TRANSFERS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:40]))
    print(f"\nwrote {ROOT}/transfers.jsonl, TRANSFERS.md")


if __name__ == "__main__":
    main()
