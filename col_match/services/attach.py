"""Record-level attachment: build careers from biographies directly.

Inverts the stint-matching architecture. The biography is the person; for
each edition year the biography is attested in, it predicts where the person
should appear in that same volume's staff lists: (colony, position) at year
Y. We then claim the matching COL_PersonRecord(s) directly — bypassing the
upstream stint grouping and its known defects (ghost stints, dual-assigned
stints, mis-named stints).

Conservative gates per (bio, record):
- record year must be an edition the bio is attested in (same volume);
- record colony must be the bio's predicted posting place at that year;
- record surname must equal the bio's (edit distance <=1 for length >=6
  only when everything else agrees);
- record initials compatible (ordered subsequence);
- record position must agree with the predicted position (token_set >= 60
  after abbreviation expansion);
- if two records in the same (colony, year) both qualify for one bio — or
  one record qualifies for two bios — the year (or record) is dropped as
  ambiguous.
"""

from __future__ import annotations

import os
import re
from collections import defaultdict

from rapidfuzz import fuzz
from rapidfuzz.distance import Levenshtein

from . import gazetteer
from .compile import _pos_norm
from .match import _shared_spelled_forename
from .schema import Biography

_NORM = re.compile(r"[^a-z0-9 ]")
POSITION_SIM = 60
OPEN_TENURE_YEARS = 12
MAX_DROP = 3               # max leading chars an OCR headword may lose
MIN_TRUNC_LEN = 5          # min surviving suffix length for a truncation match
TRUNC_POS = 70             # printed-position bar for a truncation attach (> POSITION_SIM)


def _norm(s: str | None) -> str:
    return _NORM.sub("", (s or "").lower()).strip()


def _initials(given: str | None) -> list[str]:
    return [t[0].upper() for t in re.split(r"[ .]+", given or "") if t and t[0].isalpha()]


def _initials_compatible(a: str | None, b: str | None) -> bool:
    ia, ib = _initials(a), _initials(b)
    if not ia or not ib:
        return True
    short, long_ = (ia, ib) if len(ia) <= len(ib) else (ib, ia)
    i = 0
    for x in long_:
        if i < len(short) and short[i] == x:
            i += 1
    return i == len(short)


def attach_records(
    bios: list[Biography], officials: list[dict], data_dir: str
) -> tuple[list[dict], dict]:
    """Returns (attachments, stats). One attachment = one bio claiming one
    record-year, with full provenance back to the stint id for audit."""
    # flatten records; remember the parent stint for provenance
    by_colony_year: dict[tuple[str, int], list[dict]] = defaultdict(list)
    n_records = 0
    for o in officials:
        colony = gazetteer.norm(o["colony"] or "")
        for r in o["records"]:
            n_records += 1
            by_colony_year[(colony, r["year"])].append(
                {"rec": r, "stint_id": o["id"], "stint_name": o["name"]}
            )

    trunc_on = os.environ.get("COL_NO_TRUNC") != "1"
    proposals: list[dict] = []
    for bio in bios:
        sur = _norm(bio.surname)
        if not sur:
            continue
        terminal_year = bio.terminal.year if bio.terminal and bio.terminal.year else None
        timeline = [ev for ev in bio.events if ev.year_start is not None and ev.place]
        if not timeline:
            continue
        for y in bio.editions:
            if terminal_year and y > terminal_year + 1:
                continue
            current = None
            for ev in timeline:
                if ev.year_start <= y:
                    current = ev
            if current is None:
                continue
            cur_end = current.year_end or current.year_start + OPEN_TENURE_YEARS
            if y > cur_end + 2:
                continue
            targets = gazetteer.colony_targets(current.place, data_dir)
            hits = []
            for colony in targets:
                for cand in by_colony_year.get((colony, y), ()):
                    r = cand["rec"]
                    rsur = _norm(r.get("surname") or (r.get("name_raw") or "").split(",")[0])
                    trunc = False
                    if rsur != sur:
                        # short OCR-garbled surnames need a 2-edit window (the
                        # record-level twin of match._surname_block). The bar
                        # here is already strong and independent of the
                        # surname: same colony, same edition-year, position
                        # >=POSITION_SIM, initials-compatible, and a per-year
                        # ambiguity drop below. dist 2 only widens retrieval.
                        if len(sur) >= 6 and Levenshtein.distance(rsur, sur, score_cutoff=2) <= 2:
                            fuzzy = True
                        elif (trunc_on and len(sur) >= MIN_TRUNC_LEN and rsur.endswith(sur)
                              and 1 <= len(rsur) - len(sur) <= MAX_DROP):
                            # OCR headword truncation: the bio surname is a clean
                            # suffix of the record surname (Griffiths->FFITHS).
                            # Stronger guards than plain fuzzy: shared spelled
                            # forename + position >= TRUNC_POS (applied below).
                            fuzzy = True
                            trunc = True
                        else:
                            continue
                    else:
                        fuzzy = False
                    if not _initials_compatible(bio.given_names, r.get("given_names")):
                        continue
                    # a fuzzy surname needs POSITIVE initial corroboration:
                    # _initials_compatible passes vacuously when the record has
                    # no forename ("— Sanders"), so a dist-2 garble of a common
                    # surname + a coincidental position would otherwise attach.
                    # For exact surnames the surname itself carries the match.
                    if fuzzy and not (_initials(bio.given_names)
                                      and _initials(r.get("given_names"))):
                        continue
                    score = fuzz.token_set_ratio(
                        _pos_norm(current.position), _pos_norm(r.get("position_raw"))
                    )
                    if score < POSITION_SIM:
                        continue
                    if trunc and (score < TRUNC_POS
                                  or not _shared_spelled_forename(
                                      bio.given_names, r.get("given_names"))):
                        continue
                    hits.append({"cand": cand, "score": score, "fuzzy": fuzzy, "trunc": trunc})
            if not hits:
                continue
            exact = [h for h in hits if not h["fuzzy"]]
            pool = exact or hits
            if len({id(h["cand"]) for h in pool}) > 1:
                best = max(pool, key=lambda h: h["score"])
                rest = [h for h in pool if h is not best]
                if any(h["score"] >= best["score"] - 10 for h in rest):
                    continue  # ambiguous year: drop
                pool = [best]
            h = pool[0]
            proposals.append({
                "bio_id": bio.bio_id, "year": y,
                "colony": h["cand"]["rec"].get("colony"),
                "position": h["cand"]["rec"].get("position_raw"),
                "stint_id": h["cand"]["stint_id"],
                "score": h["score"], "fuzzy_surname": h["fuzzy"],
                "trunc_surname": h.get("trunc", False),
                "record_name": h["cand"]["rec"].get("name_raw"),
            })

    # reverse ambiguity: one record-year claimed by two bios. Either they are
    # residual duplicate biographies (OCR spelling variants — the strongest
    # possible merge evidence) or genuinely ambiguous. Emit co-claim pairs
    # for the compile feedback loop; drop the attachments either way (they
    # come back clean after the merge).
    by_key = defaultdict(list)
    for p in proposals:
        by_key[(p["stint_id"], p["year"], p["record_name"])].append(p)
    attachments = []
    dropped = 0
    co_claims: dict[tuple[str, str], int] = defaultdict(int)
    bios_by_id = {b.bio_id: b for b in bios}
    for group in by_key.values():
        claimants = sorted({p["bio_id"] for p in group})
        if len(claimants) > 1:
            dropped += len(group)
            for i in range(len(claimants)):
                for j in range(i + 1, len(claimants)):
                    co_claims[(claimants[i], claimants[j])] += 1
        else:
            attachments.extend(group)

    # stint-level co-claims: two bios attaching to different years of the
    # same stint. Weaker than a same-line collision (the stint grouping is
    # upstream-derived and can itself over-group same-name people), so the
    # name guard is stricter: more than a bare single initial must agree.
    by_stint: dict[str, set[str]] = defaultdict(set)
    for p in attachments:
        by_stint[p["stint_id"]].add(p["bio_id"])
    for stint_id, claimants in by_stint.items():
        for a in claimants:
            for b in claimants:
                if a < b:
                    co_claims[(a, b)] += 1

    def _guard(ba: Biography, bb: Biography) -> bool:
        ia, ib = _initials(ba.given_names), _initials(bb.given_names)
        if min(len(ia), len(ib)) >= 2:
            return True
        # single initial: require a full given-name token to OCR-match
        ta = [t for t in re.split(r"[ .]+", ba.given_names or "") if len(t) > 2]
        tb = [t for t in re.split(r"[ .]+", bb.given_names or "") if len(t) > 2]
        return any(Levenshtein.distance(_norm(x), _norm(y), score_cutoff=1) <= 1
                   for x in ta for y in tb)

    merge_pairs = []
    for (a, b), n in sorted(co_claims.items(), key=lambda kv: -kv[1]):
        ba, bb = bios_by_id[a], bios_by_id[b]
        if not _guard(ba, bb):
            continue
        merge_pairs.append({
            "bio_a": a, "bio_b": b, "shared_records": n,
            "version_a": ba.version_ids[0], "version_b": bb.version_ids[0],
            "surnames": [ba.surname, bb.surname],
            "givens": [ba.given_names, bb.given_names],
        })

    stints_touched = {a["stint_id"] for a in attachments}
    stats = {
        "records_total": n_records,
        "attachments": len(attachments),
        "dropped_record_ambiguous": dropped,
        "co_claim_pairs": len(merge_pairs),
        "bios_with_attachments": len({a["bio_id"] for a in attachments}),
        "stints_touched": len(stints_touched),
    }
    return attachments, stats, merge_pairs
