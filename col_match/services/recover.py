"""Recover missing staff-list rows from the source OCR, guided by gaps.

For each gap (a biography posting absent from the graph) with a resolved source
file, we look for the person's surname in that file's staff-list text and parse
the row. Confidence is gated on the OCR, never on inference:

  - ``confirmed_in_ocr`` — surname found on a line with compatible initials AND
    a position matching the biography's asserted post (token_set >= 60);
  - ``surname_only``    — surname + compatible initials found, position weak or
    the biography named no position; emitted but flagged for review;
  - ``not_in_ocr``      — surname absent, or present only with incompatible
    initials (a different person). NO record emitted; logged for review.

Position appears first in both era formats — ``Position—Name, honours.``
(20th c.) and ``Position, Name, Rs.salary.`` (19th c.) — so the text before the
name is the position context we score against. Nothing is synthesized: a row is
emitted only when the surname literally sits on a parsed OCR line.
"""

from __future__ import annotations

import re
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

from rapidfuzz import fuzz
from rapidfuzz.distance import Levenshtein

from . import gazetteer
from .attach import _initials, _initials_compatible, _norm
from .compile import _pos_norm
from .match import POSITION_SIM
from .schema import Biography, GapEvent, RecoveredRecord

CITATION_SIM = 92.0
_DASH = re.compile(r"\s*[—–]\s*")              # em / en dash row delimiter
_HONOUR = re.compile(r"\b(?:[A-Z]\.){2,}[A-Z]?\b|\b[A-Z]{2,}\b")  # K.C.B., MBE
_RANK_PREFIX = re.compile(
    r"^(the\s+)?(right\s+|rt\.?\s+)?(hon\.?|sir|major|capt\.?|lieut\.?-?col\.?|"
    r"col\.?|lt\.?-?col\.?|dr\.?|rev\.?|mr\.?|mrs\.?|miss|prof\.?|"
    r"general|brig\.?|major-gen\.?)\s+", re.I)
_HEADER = re.compile(r"^\s*(#{1,6}\s+|\*\*.+\*\*)")
_WORD = re.compile(r"[A-Za-z'’\-]+")


def _surname_hit(text: str, surname_norm: str) -> bool:
    """Whole-word surname match (exact, or OCR-fuzzy <=1 edit for len>=6).
    Word-boundary, NOT substring — 'Race' must not match 'Brace'."""
    fuzzy = len(surname_norm) >= 6
    for w in _WORD.findall(text):
        n = _norm(w)
        if not n:
            continue
        if n == surname_norm:
            return True
        if fuzzy and abs(len(n) - len(surname_norm)) <= 1 \
                and Levenshtein.distance(n, surname_norm, score_cutoff=1) <= 1:
            return True
    return False


@lru_cache(maxsize=8)
def _read(path: str) -> tuple[str, tuple[str, ...]]:
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    return text, tuple(text.splitlines())


def _header_for(lines: tuple[str, ...], i: int) -> str | None:
    for j in range(i, -1, -1):
        if _HEADER.match(lines[j]):
            return lines[j].strip("# *").strip().rstrip(".")
    return None


def _name_segment(line: str, surname_norm: str) -> str | None:
    """The piece of the line holding the person's name (around the surname)."""
    parts = _DASH.split(line, maxsplit=1)
    seg = parts[1] if len(parts) == 2 else line
    # comma-delimited 19th-c rows: keep only the comma-field with the surname
    if "," in seg:
        for field in seg.split(","):
            if _surname_hit(field, surname_norm):
                seg = field
                break
    return seg.strip(" .") or None


def _position_context(line: str, name_seg: str) -> str:
    parts = _DASH.split(line, maxsplit=1)
    if len(parts) == 2:
        return parts[0]
    # comma format: text before the name field is the position
    idx = line.find(name_seg)
    return line[:idx] if idx > 0 else line


def _given_of(name_seg: str, surname_norm: str) -> str:
    """Initials/forenames preceding the surname, rank titles stripped."""
    cleaned = _RANK_PREFIX.sub("", name_seg).strip()
    toks = cleaned.split()
    out = []
    for t in toks:
        if _norm(t) == surname_norm:
            break
        out.append(t)
    return " ".join(out)


def _recover_one(gap: GapEvent, bio: Biography) -> RecoveredRecord | None:
    if not gap.source_file:
        return None
    text, lines = _read(gap.source_file)
    surname_norm = _norm(gap.surname)
    if not _surname_hit(text, surname_norm):
        return _flag(gap, "surname_absent")

    best = None  # (score, lineno, name_seg, position_ctx, given)
    saw_compatible = False
    for i, line in enumerate(lines):
        if not _surname_hit(line, surname_norm):
            continue
        name_seg = _name_segment(line, surname_norm)
        if not name_seg:
            continue
        given = _given_of(name_seg, surname_norm)
        if not _initials_compatible(bio.given_names, given):
            continue
        saw_compatible = True
        pos_ctx = _position_context(line, name_seg)
        score = (fuzz.token_set_ratio(_pos_norm(gap.position), _pos_norm(pos_ctx))
                 if gap.position else 0.0)
        if best is None or score > best[0]:
            best = (score, i, name_seg, pos_ctx, given)

    if best is None:
        return _flag(gap, "surname_present_incompatible_initials"
                     if saw_compatible is False else "no_parse")
    score, lineno, name_seg, pos_ctx, given = best
    if fuzz.partial_ratio(name_seg, text) < CITATION_SIM:
        return _flag(gap, "citation_failed")

    confidence = ("confirmed_in_ocr"
                  if gap.position and score >= POSITION_SIM else "surname_only")
    honors = [h for h in _HONOUR.findall(name_seg) if len(h) >= 2
              and _norm(h) != _norm(given)]
    return RecoveredRecord(
        colony=gap.resolved_colony or (gap.place or ""),
        year=gap.year_start,
        position_raw=pos_ctx.strip(" ,.—–") or None,
        department_raw=_header_for(lines, lineno),
        name_raw=name_seg, surname=gap.surname, given_names=given or None,
        honors=honors, confidence=confidence,
        source_file=gap.source_file, source_line=lineno + 1,
        snippet=lines[lineno].strip(), predicted_by_bio_id=gap.bio_id,
        bio_position=gap.position, gap_type=gap.gap_type)


def _flag(gap: GapEvent, reason: str) -> RecoveredRecord:
    """A non-emission: surname not confirmed in OCR. confidence=not_in_ocr,
    no structured position; the snippet carries the reason for review."""
    return RecoveredRecord(
        colony=gap.resolved_colony or (gap.place or ""), year=gap.year_start,
        name_raw="", surname=gap.surname, confidence="not_in_ocr",
        source_file=gap.source_file or "", source_line=0,
        snippet=reason, predicted_by_bio_id=gap.bio_id,
        bio_position=gap.position, gap_type=gap.gap_type)


def recover_records(
    gaps: list[GapEvent], bios_by_id: dict[str, Biography],
    data_dir: str, out_dir: Path,
) -> dict:
    recovered: list[RecoveredRecord] = []
    flagged: list[RecoveredRecord] = []
    seen: set[tuple] = set()
    # process file-by-file so the small read cache stays warm
    gaps = sorted(gaps, key=lambda g: g.source_file or "")
    for gap in gaps:
        bio = bios_by_id.get(gap.bio_id)
        if bio is None or not gap.source_file:
            continue
        rec = _recover_one(gap, bio)
        if rec is None:
            continue
        if rec.confidence == "not_in_ocr":
            flagged.append(rec)
            continue
        key = (rec.source_file, rec.source_line, rec.predicted_by_bio_id)
        if key in seen:
            continue
        seen.add(key)
        recovered.append(rec)

    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "recovered_records.jsonl").open("w", encoding="utf-8") as fh:
        for r in recovered:
            fh.write(r.model_dump_json() + "\n")
    with (out_dir / "review_queue.jsonl").open("w", encoding="utf-8") as fh:
        for r in flagged:
            fh.write(r.model_dump_json() + "\n")

    # whole-section worklist: section_absent gaps that have a source file to
    # extract, ranked by how many biographies expect records there.
    worklist: dict[str, dict] = {}
    for g in gaps:
        if g.gap_type != "section_absent" or not g.source_file:
            continue
        w = worklist.setdefault(g.source_file, {
            "source_file": g.source_file, "resolved_colony": g.resolved_colony,
            "bios": set(), "gap_events": 0,
            "year_min": g.year_start, "year_max": g.year_start})
        w["bios"].add(g.bio_id)
        w["gap_events"] += 1
        w["year_min"] = min(w["year_min"], g.year_start)
        w["year_max"] = max(w["year_max"], g.year_start)
    worklist_rows = sorted(
        ({**w, "bios": len(w["bios"])} for w in worklist.values()),
        key=lambda w: w["bios"], reverse=True)
    with (out_dir / "section_worklist.jsonl").open("w", encoding="utf-8") as fh:
        for w in worklist_rows:
            fh.write(__import__("json").dumps(w) + "\n")

    conf = sum(1 for r in recovered if r.confidence == "confirmed_in_ocr")
    by_reason: dict[str, int] = defaultdict(int)
    for r in flagged:
        by_reason[r.snippet] += 1
    stats = {
        "gaps_considered": sum(1 for g in gaps if g.source_file),
        "recovered_records": len(recovered),
        "confirmed_in_ocr": conf,
        "surname_only": len(recovered) - conf,
        "not_in_ocr": len(flagged),
        "not_in_ocr_reasons": dict(sorted(by_reason.items())),
        "section_worklist_files": len(worklist_rows),
        "bios_with_recovered_record": len({r.predicted_by_bio_id
                                           for r in recovered}),
    }
    import json as _json
    (out_dir / "recovery_stats.json").write_text(_json.dumps(stats, indent=1))
    return stats


def loopback(bios: list[Biography], officials: list[dict], data_dir: str,
             extra_record_paths: list[Path] | None = None) -> dict:
    """Augment officials with recovered records and re-enumerate candidates;
    report how many no-candidate bios become linkable. Local what-if only — no
    graph write.

    The deterministic ``recovered_records.jsonl`` contributes its
    ``confirmed_in_ocr`` rows only (unchanged). ``extra_record_paths`` (the LLM
    extraction backfill) additionally contributes ``surname_only`` rows, since a
    name+initials+colony+year hit is enough for the candidate gate even when the
    position is weak — but rescues driven by those are reported separately,
    because the class-list ``surname_only`` path carries the wrong-same-person
    risk."""
    import json as _json

    from .candidates import enumerate_candidates

    data = Path(data_dir)
    # (record, allowed-confidences) pairs: deterministic file is confirmed-only;
    # backfill files also admit surname_only.
    confirmed: list[tuple[RecoveredRecord, bool]] = []
    det_path = data / "recovery" / "recovered_records.jsonl"
    for l in det_path.open(encoding="utf-8"):
        if not l.strip():
            continue
        r = RecoveredRecord.model_validate_json(l)
        if r.confidence == "confirmed_in_ocr":
            confirmed.append((r, True))
    for p in (extra_record_paths or []):
        p = Path(p)
        if not p.exists():
            continue
        for l in p.open(encoding="utf-8"):
            if not l.strip():
                continue
            r = RecoveredRecord.model_validate_json(l)
            if r.confidence in ("confirmed_in_ocr", "surname_only"):
                confirmed.append((r, r.confidence == "confirmed_in_ocr"))

    # baseline candidates (graph only)
    stint_pairs, linked = _phase1(data)
    base_cands, _ = enumerate_candidates(bios, officials, data_dir,
                                         stint_pairs, linked)
    base_bios = {c.bio_id for c in base_cands}

    # synthesize stints from recovered records; remember each stint's strongest
    # contributing confidence so rescues can be split confirmed vs surname_only.
    synth: dict[tuple, dict] = {}
    stint_is_confirmed: dict[str, bool] = {}
    for r, is_conf in confirmed:
        key = (r.colony, _norm(r.surname), _norm(r.given_names or ""), r.year)
        rec = {"year": r.year, "colony": r.colony, "name_raw": r.name_raw,
               "surname": r.surname, "given_names": r.given_names,
               "position_raw": r.position_raw, "department_raw": r.department_raw,
               "honors": r.honors, "source": "recovered"}
        sid = f"RECOVERED::{r.surname}, {r.given_names or ''}___{r.colony}___{r.year}"
        s = synth.setdefault(key, {
            "id": sid,
            "name": f"{r.surname}, {r.given_names or ''}".strip(", "),
            "colony": r.colony, "first_year": r.year, "last_year": r.year,
            "editions": [r.year], "records": []})
        s["records"].append(rec)
        stint_is_confirmed[sid] = stint_is_confirmed.get(sid, False) or is_conf
    augmented = officials + list(synth.values())
    aug_cands, _ = enumerate_candidates(bios, augmented, data_dir,
                                        stint_pairs, linked)
    aug_bios = {c.bio_id for c in aug_cands}

    # how many bios that had NO candidate now have one, via a recovered stint
    rescued = aug_bios - base_bios
    on_recovered = {c.bio_id for c in aug_cands
                    if c.official_id.startswith("RECOVERED::")}
    # split rescued bios by the strongest confidence of a recovered stint they
    # now attach to (confirmed wins when a bio touches both).
    rescued_conf: set[str] = set()
    for c in aug_cands:
        if c.bio_id in rescued and c.official_id.startswith("RECOVERED::") \
                and stint_is_confirmed.get(c.official_id):
            rescued_conf.add(c.bio_id)
    stats = {
        "confirmed_records": sum(1 for _, ic in confirmed if ic),
        "surname_only_records": sum(1 for _, ic in confirmed if not ic),
        "synthetic_stints": len(synth),
        "bios_with_candidate_before": len(base_bios),
        "bios_with_candidate_after": len(aug_bios),
        "bios_rescued": len(rescued),
        "bios_rescued_confirmed_driven": len(rescued_conf),
        "bios_rescued_surname_only_driven": len(rescued - rescued_conf),
        "bios_with_recovered_candidate": len(on_recovered),
    }
    (data / "recovery" / "loopback_stats.json").write_text(_json.dumps(stats, indent=1))
    return stats


# --- persist confirmed recovered/backfill records as match-target stints -----

# printed compound colony labels -> component colonies to emit a stint under
# each (so a biography placed in either component can attach).
_COMPOUND_COLONY = {
    "straitssettlementsandfederatedmalaystates":
        ["Straits Settlements", "Federated Malay States"],
    "federatedmalaystatesandstraitssettlements":
        ["Straits Settlements", "Federated Malay States"],
    "malayafederatedmalaystates":
        ["Federated Malay States", "Malaya"],
}


def load_recovered_records(data_dir: str,
                           include_surname_only: bool = False) -> list[RecoveredRecord]:
    """Confirmed recovered + backfill records (the staff-list rows the upstream
    extraction missed but we recovered from the source OCR). surname_only rows
    carry wrong-person risk, so they are admitted only on request."""
    ok = {"confirmed_in_ocr"} | ({"surname_only"} if include_surname_only else set())
    out: list[RecoveredRecord] = []
    for rel in ("recovery/recovered_records.jsonl", "backfill/backfill_records.jsonl"):
        p = Path(data_dir) / rel
        if not p.exists():
            continue
        for line in p.open(encoding="utf-8"):
            if not line.strip():
                continue
            r = RecoveredRecord.model_validate_json(line)
            if r.confidence in ok:
                out.append(r)
    return out


def _expand_colony(colony: str) -> list[str]:
    return _COMPOUND_COLONY.get(gazetteer.norm(colony), [colony])


def synthesize_recovered_stints(
    records: list[RecoveredRecord], officials: list[dict], data_dir: str,
) -> tuple[list[dict], dict]:
    """Group recovered records into match-target stints (same dict shape as the
    graph officials attach/match consume). Records are grouped into real
    multi-year stints by (colony, surname, given); compound colony labels are
    split; and a synthetic stint is dropped when an existing graph official
    already covers that person-cell (same surname, colony_targets-overlapping
    colony, overlapping years) so we never duplicate a stint the matcher
    already sees. Returns (stints, stats)."""
    # index graph officials: norm surname -> [(colony_targets, first, last)]
    graph_idx: dict[str, list[tuple[set[str], int, int]]] = defaultdict(list)
    for o in officials:
        sn = _norm((o.get("name") or "").split(",", 1)[0])
        cols = gazetteer.colony_targets(o.get("colony") or "", data_dir)
        graph_idx[sn].append((cols, o.get("first_year") or 0, o.get("last_year") or 9999))

    groups: dict[tuple[str, str, str], dict] = {}
    for r in records:
        for col in _expand_colony(r.colony):
            key = (gazetteer.norm(col), _norm(r.surname), _norm(r.given_names or ""))
            g = groups.setdefault(key, {
                "surname": r.surname, "given": r.given_names or "",
                "colony": col, "recs": [], "years": set()})
            g["recs"].append(r)
            g["years"].add(r.year)

    stints: list[dict] = []
    skipped = 0
    for (ncol, nsur, _ngiv), g in groups.items():
        years = sorted(g["years"])
        fy, ly = years[0], years[-1]
        covered = False
        for cols, gfy, gly in graph_idx.get(nsur, ()):
            if ncol in {gazetteer.norm(c) for c in cols} and not (ly < gfy - 2 or fy > gly + 2):
                covered = True
                break
        if covered:
            skipped += 1
            continue
        recs = [{
            "year": r.year, "colony": g["colony"], "name_raw": r.name_raw,
            "surname": r.surname, "given_names": r.given_names,
            "position_raw": r.position_raw, "department_raw": r.department_raw,
            "honors": r.honors, "source": "recovered",
        } for r in g["recs"]]
        name = f"{g['surname']}, {g['given']}".strip(", ")
        stints.append({
            "id": f"BACKFILL::{name}___{g['colony']}___{fy}",
            "name": name, "colony": g["colony"],
            "first_year": fy, "last_year": ly, "editions": years,
            "records": recs, "source": "recovered",
        })
    stats = {"records_used": len(records), "synthetic_stints": len(stints),
             "skipped_graph_covered": skipped}
    return stints, stats


def _phase1(data: Path) -> tuple[set[tuple[str, str]], set[str]]:
    stint_pairs: set[tuple[str, str]] = set()
    linked: set[str] = set()
    import json as _json
    with (data / "matches" / "stint_matches.jsonl").open(encoding="utf-8") as fh:
        for line in fh:
            m = _json.loads(line)
            stint_pairs.add((m["bio_id"], m["official_id"]))
            linked.add(m["bio_id"])
    with (data / "matches" / "record_attachments.jsonl").open(encoding="utf-8") as fh:
        for line in fh:
            linked.add(_json.loads(line)["bio_id"])
    return stint_pairs, linked
