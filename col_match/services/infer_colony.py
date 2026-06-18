"""Cross-fragment colony inference for place-less biography clauses.

Where the rules parser extracts a place it is clean, but ~70k dated career
clauses carry no place at all ("acted as auditor-gen.", "ag. registrar"): the
colony was stated earlier in the entry, or only in that year's staff-list
table, and the clause text alone never says it. A place-less clause can never
match. But the same person recurs across the corpus, so a given year usually
has other fragments that pin the colony.

This module recovers the dropped colony from that redundancy, conservatively:

  Tier A (records) — for each place-less dated clause, look up the staff-list
  records (graph_cache/officials.jsonl, the same target attach/match use) by
  (surname, year +/- window), keep only initial-compatible rows, and require
  them to point at a SINGLE colony. Score the clause position against those
  rows' positions (token_set_ratio, the matcher's metric). Acceptance:

    - auto    : single colony AND (position >= POS_AUTO OR >= 2 corroborating
                years) — fed to attach/match as a printed-quality place;
    - review  : single colony, position in [POS_FLOOR, POS_AUTO), one year —
                annotated candidate, NOT fed to the matcher;
    - drop    : multiple colonies, or position < POS_FLOOR.

Nothing here writes the graph. Recovered places are an overlay on the in-memory
biographies; the conservative attach/match gates plus the eval_known FP gate are
the precision backstop. The recovery used name+year+colony to find the row; the
match must still independently agree on position, so a single recovered place
never carries a match on its own.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from rapidfuzz import fuzz

from . import gazetteer
from .attach import _initials_compatible
from .compile import _pos_norm
from .schema import Biography

_LABEL_NOISE = re.compile(r"(_ref|_colony|_protectorate|_and_dependencies)$", re.I)


def _colony_label(stem: str) -> str:
    """Human-ish colony label from a territory filename stem."""
    return _LABEL_NOISE.sub("", stem).replace("_", " ").strip().title()

WINDOW = 2          # staff lists lag/lead appointments; search +/- this many yrs
POS_FLOOR = 60      # position token_set_ratio below this: drop (namesake risk)
POS_AUTO = 75       # at/above this on a single year: auto-accept

_SKEY = re.compile(r"[^a-z0-9]")


def _skey(s: str | None) -> str:
    """Surname blocking key: alphanumerics only, lowercased (no spaces)."""
    return _SKEY.sub("", (s or "").lower())


def _build_record_index(officials: list[dict]) -> dict[tuple[str, int], list[dict]]:
    """(surname_key, year) -> staff-list rows. Quarantined rows are skipped —
    the same filter graph.py applies, so we never infer from a poisoned cell."""
    idx: dict[tuple[str, int], list[dict]] = defaultdict(list)
    for o in officials:
        for r in o["records"]:
            if r.get("quarantined"):
                continue
            sn = _skey(r.get("surname") or (r.get("name_raw") or "").split(",")[0])
            yr = r.get("year")
            col = r.get("colony")
            if not (sn and yr and col):
                continue
            idx[(sn, yr)].append({
                "colony_raw": col,
                "colony_norm": gazetteer.norm(col),
                "given": r.get("given_names"),
                "position": r.get("position_raw"),
                "official_id": o["id"],
            })
    return idx


def _placed_colonies(bio: Biography, data_dir: str) -> set[str]:
    cols: set[str] = set()
    for ev in bio.events:
        if ev.place:
            cols |= gazetteer.colony_targets(ev.place, data_dir)
    return cols


def infer_colonies(
    bios: list[Biography], officials: list[dict], data_dir: str,
    window: int = WINDOW,
) -> tuple[list[dict], list[dict], dict]:
    """Returns (auto_accept, review, stats). Tier A only."""
    idx = _build_record_index(officials)
    auto: list[dict] = []
    review: list[dict] = []
    n_placeless = 0
    drop_no_records = 0
    drop_multi_colony = 0
    drop_low_position = 0
    intrabio_resolved = 0

    for bio in bios:
        sn = _skey(bio.surname)
        if not sn:
            continue
        # colonies the bio itself attests via a placed event — used to resolve
        # multi-colony namesake ambiguity by intra-bio consistency
        own = _placed_colonies(bio, data_dir)
        placed = own
        for ei, ev in enumerate(bio.events):
            if ev.place:
                continue
            if ev.year_start is None or not ev.position:
                continue
            n_placeless += 1
            yr = ev.year_start
            cand: list[tuple[int, dict]] = []
            for y in range(yr - window, yr + window + 1):
                for r in idx.get((sn, y), ()):
                    if _initials_compatible(bio.given_names, r["given"]):
                        cand.append((y, r))
            if not cand:
                drop_no_records += 1
                continue
            colonies = {r["colony_norm"] for _, r in cand}
            resolved_by = "single"
            if len(colonies) != 1:
                # multi-colony namesake ambiguity: keep only a colony the bio
                # itself already attests (safe — the person is on record there)
                inter = colonies & own
                if len(inter) == 1:
                    keep = next(iter(inter))
                    cand = [(y, r) for y, r in cand if r["colony_norm"] == keep]
                    colonies = {keep}
                    resolved_by = "intrabio"
                else:
                    drop_multi_colony += 1
                    continue
            col_norm = next(iter(colonies))
            col_raw = Counter(r["colony_raw"] for _, r in cand).most_common(1)[0][0]
            pos_score = max(
                fuzz.token_set_ratio(_pos_norm(ev.position), _pos_norm(r["position"]))
                for _, r in cand
            )
            if pos_score < POS_FLOOR:
                drop_low_position += 1
                continue
            corrob_years = sorted({y for y, _ in cand})
            if resolved_by == "intrabio":
                intrabio_resolved += 1
            rec = {
                "bio_id": bio.bio_id,
                "event_index": ei,
                "surname": bio.surname,
                "given_names": bio.given_names,
                "bio_position": ev.position,
                "year": yr,
                "colony": col_raw,
                "colony_norm": col_norm,
                "position_score": round(pos_score, 1),
                "corroborating_years": corrob_years,
                "new_colony": col_norm not in placed,
                "official_ids": sorted({r["official_id"] for _, r in cand}),
                "source": "A",
                "resolved_by": resolved_by,
                "provenance": f"recordsA[{resolved_by}]:{col_raw}@{corrob_years} pos~{round(pos_score)}",
            }
            if pos_score >= POS_AUTO or len(corrob_years) >= 2:
                rec["tier"] = "auto"
                auto.append(rec)
            else:
                rec["tier"] = "review"
                review.append(rec)

    stats = {
        "place_less_dated_clauses": n_placeless,
        "auto_accept_clauses": len(auto),
        "review_clauses": len(review),
        "drop_no_records": drop_no_records,
        "drop_multi_colony": drop_multi_colony,
        "drop_low_position": drop_low_position,
        "intrabio_resolved": intrabio_resolved,
        "auto_bios": len({r["bio_id"] for r in auto}),
        "auto_bios_new_colony": len({r["bio_id"] for r in auto if r["new_colony"]}),
        "review_bios": len({r["bio_id"] for r in review}),
        "window": window,
        "pos_floor": POS_FLOOR,
        "pos_auto": POS_AUTO,
    }
    return auto, review, stats


def run(bios: list[Biography], officials: list[dict], data_dir: str,
        out_dir: Path, window: int = WINDOW,
        source_ocr_dir: str | None = None) -> dict:
    auto, review, stats = infer_colonies(bios, officials, data_dir, window)
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "recovered_places.jsonl").open("w", encoding="utf-8") as fh:
        for r in auto:
            fh.write(json.dumps(r) + "\n")
    with (out_dir / "review_queue.jsonl").open("w", encoding="utf-8") as fh:
        for r in review:
            fh.write(json.dumps(r) + "\n")
    diag = None
    if source_ocr_dir:
        recoveries, diag = infer_colonies_rawocr(
            bios, officials, data_dir, source_ocr_dir, window)
        with (out_dir / "recovered_places_rawocr.jsonl").open("w", encoding="utf-8") as fh:
            for r in recoveries:
                fh.write(json.dumps(r) + "\n")
        stats["tier_b"] = diag
    (out_dir / "inference_stats.json").write_text(json.dumps(stats, indent=1))
    _write_report(auto, review, stats, diag, out_dir / "inference_report.md")
    return stats


def _write_report(auto: list[dict], review: list[dict], stats: dict,
                  diag: dict | None, path: Path) -> None:
    by_colony = Counter(r["colony"] for r in auto)
    lines = [
        "# Colony inference report (Tier A: staff-list records)",
        "",
        f"- place-less dated clauses examined: **{stats['place_less_dated_clauses']:,}**",
        f"- auto-accept: **{stats['auto_accept_clauses']:,}** clauses / "
        f"**{stats['auto_bios']:,}** biographies "
        f"({stats['auto_bios_new_colony']:,} gain a colony stated nowhere in the entry)",
        f"- review tier: {stats['review_clauses']:,} clauses / {stats['review_bios']:,} bios",
        f"- dropped — no records: {stats['drop_no_records']:,}; "
        f"multi-colony: {stats['drop_multi_colony']:,}; "
        f"position < {stats['pos_floor']}: {stats['drop_low_position']:,}",
        f"- window ±{stats['window']} yr; auto if position ≥ {stats['pos_auto']} "
        f"or ≥2 corroborating years",
        "",
        "## Auto-accept by colony (top 20)",
        "",
        "| colony | clauses |",
        "|--------|--------:|",
    ]
    for col, n in by_colony.most_common(20):
        lines.append(f"| {col} | {n} |")
    lines += ["", "## Sample auto-accept recoveries", ""]
    for r in auto[:25]:
        lines.append(
            f"- **{r['surname']}, {r['given_names'] or ''}** — "
            f"'{r['bio_position']}' ({r['year']}) → **{r['colony']}** "
            f"(pos~{r['position_score']}, yrs {r['corroborating_years']}"
            f"{', NEW' if r['new_colony'] else ''})"
        )
    if diag:
        n = diag["tier_b_clauses"] or 1
        lines += [
            "",
            "## Tier B — raw-OCR diagnostic: why place-less clauses with no graph record don't match",
            "",
            f"Of the **{diag['tier_b_clauses']:,}** place-less dated clauses with NO graph "
            f"record (Tier A couldn't touch them), going back to the source OCR finds:",
            "",
            "| where the surname-year evidence lives | clauses | share |",
            "|---|--:|--:|",
            f"| **absent from OCR** (garbled, not in staff service, or coverage gap) "
            f"| {diag['surname_absent_in_ocr']:,} | {diag['surname_absent_in_ocr']*100//n}% |",
            f"| present, single colony, position agrees → **recoverable row** "
            f"(extraction loss) | {diag['recovered_single_colony']:,} "
            f"| {diag['recovered_single_colony']*100//n}% |",
            f"| present, single colony, position weak | {diag['single_colony_low_position']:,} "
            f"| {diag['single_colony_low_position']*100//n}% |",
            f"| present in multiple colonies (ambiguous) | {diag['multi_colony_ambiguous']:,} "
            f"| {diag['multi_colony_ambiguous']*100//n}% |",
            "",
            f"Tier B single-colony recoveries: {diag['recovered_single_colony']:,} clauses "
            f"/ {diag['recovered_bios']:,} bios (auto {diag['auto']:,}, review {diag['review']:,}). "
            "These mostly point at colony-years the graph never extracted, so they feed the "
            "recover/backfill pipeline rather than lifting attach directly.",
        ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# --- Tier B: raw-OCR inference + the "why not 100%" diagnostic --------------
#
# Tier A only reaches place-less clauses whose colony-year row the upstream
# extraction actually captured. The far larger residue (drop_no_records) has NO
# graph record — but the staff-list row may still sit in the source OCR, dropped
# during extraction. Tier B goes back to the raw text to (a) recover the colony
# for those clauses where the OCR pins it unambiguously, and (b) measure WHY the
# rest don't match: is the surname present in the OCR (an extraction loss) or
# genuinely absent (OCR garble, coverage gap, or a person never in colonial
# staff service — military/London/pre-coverage)?
#
# These recoveries usually point at colonies with no graph record, so they give
# no direct attach lift; their value is feeding the recover/backfill pipeline
# and quantifying the gap. The diagnostic is the deliverable here.

_WORD = re.compile(r"[A-Za-z'’\-]+")


def _tier_b_clauses(
    bios: list[Biography], rec_idx: dict[tuple[str, int], list[dict]], window: int,
) -> tuple[list[tuple[Biography, int]], set[str]]:
    """Place-less dated clauses with a position and NO initial-compatible graph
    record in the window — the population Tier A could not resolve."""
    clauses: list[tuple[Biography, int]] = []
    surnames: set[str] = set()
    for bio in bios:
        sn = _skey(bio.surname)
        if not sn:
            continue
        for ei, ev in enumerate(bio.events):
            if ev.place or ev.year_start is None or not ev.position:
                continue
            yr = ev.year_start
            has_rec = any(
                _initials_compatible(bio.given_names, r["given"])
                for y in range(yr - window, yr + window + 1)
                for r in rec_idx.get((sn, y), ())
            )
            if has_rec:
                continue
            clauses.append((bio, ei))
            surnames.add(sn)
    return clauses, surnames


def _build_ocr_index(
    target_surnames: set[str], source_ocr_dir: str,
) -> dict[str, list[tuple[int, str, str, str]]]:
    """One streaming pass over the source OCR. For each target surname, collect
    the staff-list lines it sits on: (year, colony_label, given_tokens,
    position_context). Cheap surname-presence is a set intersection per file;
    the per-line scan runs only for surnames actually present in that file."""
    from .recover import (_given_of, _name_segment, _position_context, _read,
                          _surname_hit)
    from .source_index import load_index

    idx = load_index(source_ocr_dir)
    hits: dict[str, list[tuple[int, str, str, str]]] = defaultdict(list)
    for year in idx.years:
        for _terr_key, path in idx.by_year.get(year, ()):
            text, lines = _read(str(path))
            present = {_skey(w) for w in _WORD.findall(text)} & target_surnames
            if not present:
                continue
            label = _colony_label(path.stem)
            for line in lines:
                for sn in present:
                    if not _surname_hit(line, sn):
                        continue
                    seg = _name_segment(line, sn)
                    if not seg:
                        continue
                    given = _given_of(seg, sn)
                    pos = _position_context(line, seg)
                    hits[sn].append((year, label, given, pos))
    return hits


def infer_colonies_rawocr(
    bios: list[Biography], officials: list[dict], data_dir: str,
    source_ocr_dir: str, window: int = WINDOW,
) -> tuple[list[dict], dict]:
    """Tier B. Returns (recoveries, diagnostic)."""
    rec_idx = _build_record_index(officials)
    clauses, surnames = _tier_b_clauses(bios, rec_idx, window)
    hits = _build_ocr_index(surnames, source_ocr_dir)

    recoveries: list[dict] = []
    surname_absent = single_low_pos = multi_colony = 0
    recovered_bios: set[str] = set()
    for bio, ei in clauses:
        sn = _skey(bio.surname)
        ev = bio.events[ei]
        yr = ev.year_start
        cand = [
            (y, col, pos) for (y, col, given, pos) in hits.get(sn, ())
            if yr - window <= y <= yr + window
            and _initials_compatible(bio.given_names, given)
        ]
        if not cand:
            surname_absent += 1
            continue
        colonies = {col for _, col, _ in cand}
        if len(colonies) != 1:
            multi_colony += 1
            continue
        col = next(iter(colonies))
        pos_score = max(
            fuzz.token_set_ratio(_pos_norm(ev.position), _pos_norm(pos))
            for _, _, pos in cand
        )
        if pos_score < POS_FLOOR:
            single_low_pos += 1
            continue
        years = sorted({y for y, _, _ in cand})
        rec = {
            "bio_id": bio.bio_id, "event_index": ei, "surname": bio.surname,
            "given_names": bio.given_names, "bio_position": ev.position,
            "year": yr, "colony": col, "position_score": round(pos_score, 1),
            "corroborating_years": years,
            "tier": "auto" if (pos_score >= POS_AUTO or len(years) >= 2) else "review",
            "source": "B",
            "provenance": f"rawocrB:{col}@{years} pos~{round(pos_score)}",
        }
        recoveries.append(rec)
        recovered_bios.add(bio.bio_id)

    diag = {
        "tier_b_clauses": len(clauses),
        "tier_b_surnames": len(surnames),
        "recovered_single_colony": len(recoveries),
        "recovered_bios": len(recovered_bios),
        "surname_absent_in_ocr": surname_absent,
        "single_colony_low_position": single_low_pos,
        "multi_colony_ambiguous": multi_colony,
        "auto": sum(1 for r in recoveries if r["tier"] == "auto"),
        "review": sum(1 for r in recoveries if r["tier"] == "review"),
    }
    return recoveries, diag


def apply_bracket_places(bios: list[Biography], data_dir: str) -> int:
    """Bracketing interpolation: a place-less dated event that falls (by year)
    BETWEEN two placed events resolving to the SAME colony almost certainly
    belongs to that colony — a continuous career listing whose middle clauses
    dropped the place (the compiled bio concatenates several editions, so the
    parser's within-entry place inheritance can't span the gaps). Attach the
    bracketing colony as printed-quality.

    Conservative: requires a placed event on BOTH sides whose colonies share a
    gazetteer target; assigns one endpoint's printed place string (so it
    resolves identically downstream). Like the record-recovery overlay, it only
    PROPOSES a colony — attach/match independently re-gate colony+tenure+
    position+ambiguity, and eval_known is the FP backstop. Returns the number of
    events placed."""
    applied = 0
    for bio in bios:
        placed = [(e.year_start, e) for e in bio.events
                  if e.place and e.year_start is not None]
        if not placed:
            continue
        # single-colony career: if every placed event shares a common colony
        # target, the whole career is in that colony, so EVERY place-less dated
        # event belongs to it — including leading/trailing ones a two-sided
        # bracket can't reach (HUMPHRYS: all-Antigua career, place-less trailing
        # clerk clauses).
        common = set.intersection(*[gazetteer.colony_targets(e.place, data_dir)
                                    for _y, e in placed])
        single_place = placed[0][1].place if common else None
        for ev in bio.events:
            if ev.place or ev.year_start is None:
                continue
            chosen = None
            if single_place is not None:
                chosen = single_place
            elif len(placed) >= 2:
                # multi-colony career: only the strict between-two-same-colony
                # bracket is safe
                prior = [(y, e) for y, e in placed if y <= ev.year_start]
                later = [(y, e) for y, e in placed if y >= ev.year_start]
                if prior and later:
                    for _ya, a in prior:
                        ta = gazetteer.colony_targets(a.place, data_dir)
                        if not ta:
                            continue
                        for _yb, b in later:
                            if a is b:
                                continue
                            if ta & gazetteer.colony_targets(b.place, data_dir):
                                chosen = a.place
                                break
                        if chosen:
                            break
            if not chosen:
                continue
            ev.place = chosen
            ev.place_inherited = False
            ev.place_recovered = True
            ev.recovered_provenance = ("single_colony" if single_place is not None
                                       else "bracket")
            applied += 1
    return applied


def apply_recovered_places(bios: list[Biography], data_dir: str) -> int:
    """Overlay auto-accept recovered places onto in-memory biographies before
    attach/match. Idempotent; returns the number of events placed. Safe to call
    when the file is absent. Runs the record-reverse-lookup overlay first, then
    bracketing interpolation (which can use the just-recovered places as
    bracket endpoints)."""
    path = Path(data_dir) / "inference" / "recovered_places.jsonl"
    applied = 0
    if path.exists():
        by_bio: dict[str, dict[int, dict]] = defaultdict(dict)
        for line in path.open(encoding="utf-8"):
            if not line.strip():
                continue
            r = json.loads(line)
            by_bio[r["bio_id"]][r["event_index"]] = r
        for bio in bios:
            recs = by_bio.get(bio.bio_id)
            if not recs:
                continue
            for ei, ev in enumerate(bio.events):
                r = recs.get(ei)
                if r is None or ev.place:
                    continue
                ev.place = r["colony"]
                ev.place_inherited = False
                ev.place_recovered = True
                ev.recovered_provenance = r["provenance"]
                applied += 1
    applied += apply_bracket_places(bios, data_dir)
    return applied
