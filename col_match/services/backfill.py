"""Extraction backfill of the section worklist.

The completeness ledger shows ~51% of ungrounded biography career clauses are
"extraction-addressable": the staff-list record exists in the source OCR but was
never extracted into the graph (whole colony-year sections — Malay States,
Zanzibar, Kenya, Nigeria, Palestine — that were OCR'd but skipped on load).
``recover.py`` already enumerates those absent sections in
``recovery/section_worklist.jsonl``, ranked by how many biographies expect a
record there.

This module runs an LLM over those section files to extract their staff lists,
normalizes the result into ``RecoveredRecord`` proposals, and feeds them through
the existing ``recover.loopback`` / ledger machinery to MEASURE grounding lift —
with no graph write. Production load is a separate, human-run, gated step
upstream (see ``cmd_backfill_export_upstream``).

Read-only to Neo4j by construction: everything here writes only files under
``<data_dir>/backfill/``. All metered spend goes through ``OpenRouterClient``,
which enforces the cap and the ledger.

Three section layouts the prompt must handle:
  T1  standard ``Position, Name, quals, salary`` lines (easy);
  T2  decoupled class-lists — positions listed apart from names, which appear in
      comma-runs grouped by salary class with footnote markers *†‡§ (the Malay
      States, top of the worklist): names recoverable, per-name position not;
  T3  late-era files that open with narrative prose + demographic tables, the
      staff list buried lower (must be located, prose skipped).
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from . import gazetteer
from .attach import _initials_compatible, _norm
from .recover import _surname_hit
from .schema import RecoveredRecord

# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

SYSTEM = (
    "You extract staff-list (officials) records from one colony's section of "
    "the British Colonial Office List, a printed annual government staff "
    "register. The text is OCR and may contain errors. Transcribe names exactly "
    "as printed — never correct, expand, translate, or invent a name. Output a "
    "record ONLY for a person who actually appears in the supplied text."
)

USER_TEMPLATE = """Colony: {colony}
Edition year(s): {y0}-{y1}

Extract every official named in the text below into the `officials` array. Keep
each record minimal — only the fields requested.

Layout rules:
- Most entries read `Position, Name, qualifications, salary` or `Position—Name, \
honours`. Emit one record per person: `name` (verbatim), `surname`, \
`given_names` (initials kept as printed), `position`, and `honors` if printed \
(e.g. K.C.M.G., M.C.). Set `position_certain` = true.
- CLASS LISTS: some grades print a class/salary heading (e.g. `Officers of \
Class II.`) followed by a comma-separated run of names with NO individual \
position (e.g. `C. F. J. Green, B. Nunn, G. E. Shaw, ...`). For each such name \
emit a record with `position` = the class heading (e.g. "Officer, Class II") \
and `position_certain` = false. Do NOT pair these names with the position lines \
printed separately above them — those positions belong to unnamed slots. Strip \
any trailing footnote marker (*, †, ‡, §) from `name`.
- Set `position_certain` = true ONLY when a specific position is printed right \
next to the name. Otherwise false.
- Transcribe names exactly — never invent a name. The section may open with \
narrative prose and tables (area, population, climate, history). SKIP all prose \
and tables — extract ONLY the staff list. If there is no staff list, return an \
empty `officials` array.

Text:
---
{text}
---"""

# Lean record (grounding needs surname/initials/position; colony+year come from
# the worklist row). Dropped department/salary/marker/source_quote: a verbose
# 10-field record tripled output tokens and truncated dense class-list chunks.
# Anti-hallucination is enforced downstream by a surname-in-OCR check, not a
# quote field. Strict json_schema: every property required; additionalProperties
# closed so providers accept strict mode.
RESPONSE_SCHEMA: dict = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "officials": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "name": {"type": "string"},
                    "surname": {"type": "string"},
                    "given_names": {"type": ["string", "null"]},
                    "position": {"type": ["string", "null"]},
                    "position_certain": {"type": "boolean"},
                    "honors": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["name", "surname", "given_names", "position",
                             "position_certain", "honors"],
            },
        }
    },
    "required": ["officials"],
}


# ---------------------------------------------------------------------------
# Section reading + chunking
# ---------------------------------------------------------------------------

def read_section(path: str) -> str:
    return Path(path).read_text(encoding="utf-8", errors="replace")


def chunk_section(text: str, max_in_chars: int = 8_000) -> list[str]:
    """Split on blank-line boundaries, never inside a block — a class-list
    comma-run must stay whole. Greedy: accumulate blocks until the next would
    exceed the budget. A single over-budget block is emitted alone.

    The budget is small (~1.5k input tokens) because dense comma-separated name
    runs are far more entity-dense than prose: one record per name, so a large
    chunk can blow past the output-token ceiling (truncating the JSON). Small
    chunks keep each call's output bounded."""
    if len(text) <= max_in_chars:
        return [text]
    blocks = text.split("\n\n")
    chunks: list[str] = []
    cur: list[str] = []
    cur_len = 0
    for b in blocks:
        bl = len(b) + 2
        if cur and cur_len + bl > max_in_chars:
            chunks.append("\n\n".join(cur))
            cur, cur_len = [], 0
        cur.append(b)
        cur_len += bl
    if cur:
        chunks.append("\n\n".join(cur))
    return chunks


# ---------------------------------------------------------------------------
# Extraction + validation
# ---------------------------------------------------------------------------

_MIN_CHUNK_CHARS = 1_500   # below this we stop subdividing and accept the loss


def _split_in_half(chunk: str) -> list[str]:
    """Split near the midpoint, preferring a newline, then a comma (dense
    comma-run rosters in some OCR have no line breaks at all), then a hard
    character split as a last resort. Returns [chunk] only for a single
    indivisible token."""
    mid = len(chunk) // 2
    for sep in ("\n", ", "):
        cut = chunk.rfind(sep, 0, mid)
        if cut <= 0:
            cut = chunk.find(sep, mid)
        if cut > 0:
            return [chunk[:cut], chunk[cut + len(sep):]]
    # no separator anywhere near the middle: hard split (won't break a comma-run
    # of names harmfully — the citation gate drops any fragment that isn't a
    # real surname in the OCR).
    if len(chunk) > 1:
        return [chunk[:mid], chunk[mid:]]
    return [chunk]


# Hard ceiling on calls per section: the runaway guard. A 200KB+ dense file
# subdividing to ~2KB pieces could otherwise issue 100+ calls. When hit, we keep
# whatever was extracted and stop — a bounded partial beats an unbounded burn.
_MAX_CALLS_PER_SECTION = 40


def _extract_chunk(client, row: dict, model: str, tier: str, chunk: str,
                   idx: int, budget: dict) -> list[dict]:
    """One chunk → officials, recursively re-splitting on output truncation.
    `budget` is a per-section mutable counter {'calls': n}; when it exceeds
    _MAX_CALLS_PER_SECTION we stop (the runaway guard)."""
    from .openrouter import OutputTruncated

    if budget["calls"] >= _MAX_CALLS_PER_SECTION:
        return []
    budget["calls"] += 1
    user = USER_TEMPLATE.format(
        colony=row.get("resolved_colony") or "",
        y0=row.get("year_min"), y1=row.get("year_max"), text=chunk)
    try:
        raw = client.complete(model=model, system=SYSTEM, user=user,
                              response_schema=RESPONSE_SCHEMA,
                              section_id=row["source_file"], tier=tier, chunk=idx)
        return [o for o in (raw.get("officials") or []) if isinstance(o, dict)]
    except OutputTruncated:
        halves = _split_in_half(chunk)
        if len(halves) == 1 or len(chunk) <= _MIN_CHUNK_CHARS:
            import sys as _sys
            print(f"[backfill] dropping a {len(chunk)}-char block of "
                  f"{Path(row['source_file']).name} — too dense to fit even after "
                  f"subdividing", file=_sys.stderr)
            return []
        out: list[dict] = []
        for h in halves:
            out += _extract_chunk(client, row, model, tier, h, idx, budget)
        return out


def extract_section(client, row: dict, model: str, tier: str) -> list[dict]:
    text = read_section(row["source_file"])
    out: list[dict] = []
    budget = {"calls": 0}
    for i, chunk in enumerate(chunk_section(text)):
        out += _extract_chunk(client, row, model, tier, chunk, i, budget)
        if budget["calls"] >= _MAX_CALLS_PER_SECTION:
            import sys as _sys
            print(f"[backfill] {Path(row['source_file']).name}: hit "
                  f"{_MAX_CALLS_PER_SECTION}-call cap, stopping with "
                  f"{len(out)} officials so far (partial)", file=_sys.stderr)
            break
    return out


def validate_extraction(officials: list[dict], row: dict,
                        section_text: str) -> list[str]:
    """Deterministic gate. A non-empty return = fatal -> escalate to the pro
    tier (and, if still fatal, mark the section failed). Mirrors validate.py:
    cheap structural checks, no inference."""
    fatal: list[str] = []
    if not officials:
        fatal.append("zero_records")
        return fatal
    # citation = the surname is a real whole word in the OCR (the same anchor
    # recover.py uses). A low rate means the model is inventing names.
    cited = sum(_surname_hit(section_text, _norm(o.get("surname") or ""))
                for o in officials if (o.get("surname") or "").strip())
    if cited / len(officials) < 0.80:
        fatal.append("low_citation_rate")
    if any(not (o.get("surname") or "").strip() for o in officials):
        fatal.append("missing_surname")
    return fatal


# ---------------------------------------------------------------------------
# Normalization to RecoveredRecord
# ---------------------------------------------------------------------------

def _file_surname_index(file_gaps: list[dict]) -> dict[str, list[dict]]:
    idx: dict[str, list[dict]] = defaultdict(list)
    for g in file_gaps:
        idx[_norm(g.get("surname") or "")].append(g)
    return idx


def _match_gap_bio(o: dict, surname_idx: dict[str, list[dict]]) -> dict | None:
    """The gap bio this extracted official grounds, IF exactly one gap bio in
    this section matches on surname + compatible initials. Provenance only —
    the lift metric (loopback) re-matches independently."""
    cands = surname_idx.get(_norm(o.get("surname") or ""), [])
    given = o.get("given_names") or ""
    hits = [g for g in cands
            if _initials_compatible(g.get("given_names"), given)]
    uniq = {g["bio_id"] for g in hits}
    return hits[0] if len(uniq) == 1 else None


def normalize(officials: list[dict], row: dict, section_text: str,
              file_gaps: list[dict]) -> list[RecoveredRecord]:
    surname_idx = _file_surname_index(file_gaps)
    colony = row.get("resolved_colony") or ""
    year = row.get("year_min")
    out: list[RecoveredRecord] = []
    seen: set[tuple] = set()       # collapse identical re-extractions (chunk seams)
    for o in officials:
        surname = (o.get("surname") or "").strip()
        if not surname:
            continue
        given = o.get("given_names") or ""
        dedup_key = (_norm(surname), _norm(given))
        if dedup_key in seen:
            continue
        seen.add(dedup_key)
        # citation gate: the surname must appear as a whole word (OCR-fuzzy) in
        # the section. Same bar recover.py uses; nothing absent from the text is
        # emitted, so an invented name is dropped here.
        if not _surname_hit(section_text, _norm(surname)):
            continue
        position = (o.get("position") or "").strip() or None
        certain = bool(o.get("position_certain")) and position is not None
        gap = _match_gap_bio(o, surname_idx)
        out.append(RecoveredRecord(
            colony=colony, year=year,
            position_raw=position,
            department_raw=None,
            name_raw=(o.get("name") or surname),
            surname=surname,
            given_names=(given or None),
            honors=list(o.get("honors") or []),
            confidence="confirmed_in_ocr" if certain else "surname_only",
            source_file=row["source_file"], source_line=0,
            snippet=(o.get("name") or surname)[:120],
            predicted_by_bio_id=(gap["bio_id"] if gap else ""),
            bio_position=(gap.get("position") if gap else None),
            gap_type="section_absent"))
    return out


# ---------------------------------------------------------------------------
# Run orchestration
# ---------------------------------------------------------------------------

def _load_worklist(data_dir: str, top: int) -> list[dict]:
    p = Path(data_dir) / "recovery" / "section_worklist.jsonl"
    rows = [json.loads(l) for l in p.open(encoding="utf-8") if l.strip()]
    rows.sort(key=lambda r: r.get("bios", 0), reverse=True)
    return rows[:top] if top else rows


def _gaps_by_file(data_dir: str) -> dict[str, list[dict]]:
    by_file: dict[str, list[dict]] = defaultdict(list)
    p = Path(data_dir) / "recovery" / "gaps.jsonl"
    for l in p.open(encoding="utf-8"):
        if not l.strip():
            continue
        g = json.loads(l)
        if g.get("source_file"):
            by_file[g["source_file"]].append(g)
    return by_file


def _ledger_ratio(ledger_path: Path) -> tuple[int, int, float]:
    t_in = t_out = 0
    if ledger_path.exists():
        for l in ledger_path.open(encoding="utf-8"):
            if l.strip():
                r = json.loads(l)
                t_in += r.get("tokens_in", 0)
                t_out += r.get("tokens_out", 0)
    return t_in, t_out, (t_out / t_in if t_in else 0.0)


def build_client(cfg, cap_usd: float, ledger_path: Path, backend: str):
    from .openrouter import OpenRouterClient
    if backend == "ollama":
        return OpenRouterClient.ollama(
            cfg.ollama_host, cap_usd=cap_usd, ledger_path=ledger_path,
            max_output_tokens=cfg.backfill_max_output_tokens)
    return OpenRouterClient(
        api_key=cfg.openrouter_api_key, cap_usd=cap_usd, ledger_path=ledger_path,
        max_output_tokens=cfg.backfill_max_output_tokens)


def _extract_chunk_unit(client, row: dict, model: str, tier: str, chunk: str,
                        idx: int) -> list[dict]:
    """One top-level chunk → officials, with synchronous adaptive re-split on
    truncation (bounded by _MIN_CHUNK_CHARS). No per-section call cap: chunks are
    the unit of work now, so a giant file is just many independent chunks rather
    than one worker grinding sequentially."""
    from .openrouter import OutputTruncated

    user = USER_TEMPLATE.format(
        colony=row.get("resolved_colony") or "",
        y0=row.get("year_min"), y1=row.get("year_max"), text=chunk)
    try:
        raw = client.complete(model=model, system=SYSTEM, user=user,
                              response_schema=RESPONSE_SCHEMA,
                              section_id=row["source_file"], tier=tier, chunk=idx)
        return [o for o in (raw.get("officials") or []) if isinstance(o, dict)]
    except OutputTruncated:
        halves = _split_in_half(chunk)
        if len(halves) == 1 or len(chunk) <= _MIN_CHUNK_CHARS:
            return []
        out: list[dict] = []
        for h in halves:
            out += _extract_chunk_unit(client, row, model, tier, h, idx)
        return out


def _extract_flat(client, rows: list[dict], model: str, tier: str, workers: int,
                  on_complete) -> bool:
    """Concurrent over ALL chunks of all `rows` in one pool — the key to keeping
    giant files from monopolizing workers. `on_complete(sf, officials)` fires
    once, the moment a section's LAST chunk lands (incremental finalization).
    Returns True if the spend cap aborted the pass (partial sections are simply
    never finalized → resumed next run)."""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    from .openrouter import SpendCapExceeded

    total: dict[str, int] = {}
    work: list[tuple] = []
    for row in rows:
        chs = chunk_section(read_section(row["source_file"]))
        total[row["source_file"]] = len(chs)
        for i, ch in enumerate(chs):
            work.append((row, i, ch))

    by_sf: dict[str, list] = defaultdict(list)
    seen: dict[str, int] = defaultdict(int)
    aborted = False
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(_extract_chunk_unit, client, row, model, tier, ch, i):
                row["source_file"] for (row, i, ch) in work}
        for fut in as_completed(futs):
            sf = futs[fut]
            try:
                offs = fut.result()
            except SpendCapExceeded:
                aborted = True
                for f in futs:
                    f.cancel()
                break
            except Exception:
                offs = []   # a single failed chunk contributes nothing
            by_sf[sf] += offs
            seen[sf] += 1
            if seen[sf] == total[sf]:
                on_complete(sf, by_sf[sf])
    return aborted


def run_backfill(cfg, *, top: int, model: str, escalate_model: str,
                 cap_usd: float, resume: bool, backend: str = "openrouter",
                 workers: int = 6) -> dict:
    import threading

    from .openrouter import cost_of, estimate_tokens

    out_dir = Path(cfg.data_dir) / "backfill"
    out_dir.mkdir(parents=True, exist_ok=True)
    ledger_path = out_dir / "spend_ledger.jsonl"
    manifest_path = out_dir / "manifest.json"
    records_path = out_dir / "backfill_records.jsonl"

    manifest: dict[str, dict] = {}
    if resume and manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
    elif not resume and records_path.exists():
        records_path.unlink()  # fresh run: clear records (ledger persists)

    rows = _load_worklist(cfg.data_dir, top)
    row_by_sf = {r["source_file"]: r for r in rows}
    gaps_by_file = _gaps_by_file(cfg.data_dir)
    client = build_client(cfg, cap_usd, ledger_path, backend)

    pending = [r for r in rows
               if not (resume and manifest.get(r["source_file"], {}).get("state")
                       in ("done", "failed"))]
    est_in = sum(estimate_tokens(read_section(r["source_file"])) for r in pending)
    est_cost = cost_of(model, est_in, int(est_in * 0.8))
    w = 1 if backend == "ollama" else workers
    print(f"[backfill] {len(pending)} sections pending of {len(rows)}; "
          f"~{est_in/1000:.0f}k input tokens; rough estimate ${est_cost:.2f}; "
          f"cap ${cap_usd:.2f}; spent so far ${client.running_spend():.4f}; "
          f"workers={w}")

    # incremental writers (callbacks run inside the pool's main loop thread, but
    # guard anyway since finalization touches shared files)
    lock = threading.Lock()
    rec_fh = records_path.open("a", encoding="utf-8")
    state = {"done": 0, "failed": 0, "escalate_q": []}

    def _persist(sf: str, entry: dict, recs=None):
        with lock:
            if recs:
                for r in recs:
                    rec_fh.write(r.model_dump_json() + "\n")
                rec_fh.flush()
            manifest[sf] = entry
            manifest_path.write_text(json.dumps(manifest, indent=1))

    def _finalize(sf, officials, escalated, allow_escalate):
        row = row_by_sf[sf]
        fatal = validate_extraction(officials, row, read_section(sf))
        if fatal:
            if allow_escalate:
                state["escalate_q"].append(row)
                return
            _persist(sf, {"state": "failed", "reasons": fatal,
                          "escalated": escalated, "n_extracted": len(officials)})
            state["failed"] += 1
            print(f"[backfill] {Path(sf).name:38s} FAILED {fatal}")
            return
        recs = normalize(officials, row, read_section(sf), gaps_by_file.get(sf, []))
        _persist(sf, {"state": "done", "n_records": len(recs),
                      "n_extracted": len(officials), "escalated": escalated}, recs)
        state["done"] += 1
        print(f"[backfill] ({state['done']}) {Path(sf).name:38s} "
              f"ext={len(officials):4d} rec={len(recs):4d}"
              f"{' (esc)' if escalated else ''}")

    aborted = False
    try:
        # Phase 1: flash, flat over every chunk of every pending section.
        aborted = _extract_flat(
            client, pending, model, "default", w,
            lambda sf, offs: _finalize(sf, offs, False, allow_escalate=True))
        # Phase 2: pro escalation, flat over the failed sections' chunks.
        esc = state["escalate_q"]
        if esc and not aborted:
            print(f"[backfill] escalating {len(esc)} sections to {escalate_model}")
            aborted = _extract_flat(
                client, esc, escalate_model, "escalate", w,
                lambda sf, offs: _finalize(sf, offs, True, allow_escalate=False))
    finally:
        rec_fh.close()

    return _write_stats(cfg, out_dir, manifest, ledger_path, client, model,
                        aborted)


def _write_stats(cfg, out_dir: Path, manifest: dict, ledger_path: Path,
                 client, model: str, aborted: bool) -> dict:
    by_conf: dict[str, int] = defaultdict(int)
    records_path = out_dir / "backfill_records.jsonl"
    if records_path.exists():
        for l in records_path.open(encoding="utf-8"):
            if l.strip():
                by_conf[json.loads(l)["confidence"]] += 1
    done = sum(1 for m in manifest.values() if m.get("state") == "done")
    failed = sum(1 for m in manifest.values() if m.get("state") == "failed")
    escalated = sum(1 for m in manifest.values() if m.get("escalated"))
    t_in, t_out, ratio = _ledger_ratio(ledger_path)
    stats = {
        "model": model,
        "sections_done": done,
        "sections_failed": failed,
        "sections_escalated": escalated,
        "records_total": sum(by_conf.values()),
        "records_by_confidence": dict(by_conf),
        "failed_reasons": _failed_reasons(manifest),
        "tokens_in": t_in, "tokens_out": t_out,
        "output_input_ratio": round(ratio, 3),
        "spend_usd": round(client.running_spend(), 4),
        "cap_usd": client.cap_usd,
        "aborted_on_cap": aborted,
    }
    (out_dir / "backfill_stats.json").write_text(json.dumps(stats, indent=1))
    return stats


def _failed_reasons(manifest: dict) -> dict[str, int]:
    out: dict[str, int] = defaultdict(int)
    for m in manifest.values():
        if m.get("state") == "failed":
            for r in m.get("reasons", []):
                out[r] += 1
    return dict(sorted(out.items()))


def estimate_only(cfg, top: int, model: str) -> dict:
    """Tokens + USD for the top-N sections, no API calls."""
    from .openrouter import cost_of, estimate_tokens
    rows = _load_worklist(cfg.data_dir, top)
    est_in = sum(estimate_tokens(read_section(r["source_file"])) for r in rows)
    # output ratio: use the measured one from a prior run if present, else 0.8
    ledger = Path(cfg.data_dir) / "backfill" / "spend_ledger.jsonl"
    _, _, ratio = _ledger_ratio(ledger)
    ratio = ratio or 0.8
    est_out = int(est_in * ratio)
    return {
        "sections": len(rows),
        "tokens_in_est": est_in,
        "output_input_ratio_used": round(ratio, 3),
        "tokens_out_est": est_out,
        "cost_usd_est": round(cost_of(model, est_in, est_out), 2),
        "ratio_source": "measured" if ratio != 0.8 else "default-0.8",
    }


# ---------------------------------------------------------------------------
# Projected ledger (pre-load; NO graph write)
# ---------------------------------------------------------------------------

def projected_ledger(cfg) -> dict:
    """Re-derive the completeness ledger (assemble.py logic) but additionally
    treat an extraction-addressable clause as grounded when a backfill record
    matches its gap bio (predicted_by_bio_id + colony). Approximate — the
    authoritative lift metric is recover.loopback().bios_rescued; this shows the
    projected movement of the 'extraction_addressable' bucket toward 'grounded'
    WITHOUT touching graph_stats.json. Confirmed vs surname_only contributions
    are reported separately (surname_only is the riskier T2 class-list path)."""
    data = Path(cfg.data_dir)
    bio_events = [json.loads(l) for l in
                  (data / "graph" / "bio_events.jsonl").open(encoding="utf-8")
                  if l.strip()]
    gap_index: dict[tuple, dict] = {}
    for l in (data / "recovery" / "gaps.jsonl").open(encoding="utf-8"):
        if l.strip():
            g = json.loads(l)
            gap_index[(g["bio_id"], g["event_index"])] = g

    # which (bio_id, event_index) a backfill record grounds, split by confidence
    grounded_conf: set[tuple] = set()
    grounded_surn: set[tuple] = set()
    bf_path = data / "backfill" / "backfill_records.jsonl"
    if bf_path.exists():
        # index gaps by (bio_id, norm colony) for the overlay
        gaps_by_bio_colony: dict[tuple, list[dict]] = defaultdict(list)
        for g in gap_index.values():
            gaps_by_bio_colony[(g["bio_id"],
                                gazetteer.norm(g.get("resolved_colony") or ""))].append(g)
        for l in bf_path.open(encoding="utf-8"):
            if not l.strip():
                continue
            r = json.loads(l)
            bid = r.get("predicted_by_bio_id")
            if not bid:
                continue
            key = (bid, gazetteer.norm(r.get("colony") or ""))
            target = grounded_conf if r.get("confidence") == "confirmed_in_ocr" \
                else grounded_surn
            ry = r.get("year")
            for g in gaps_by_bio_colony.get(key, []):
                # a record from one edition-year grounds only the clause whose
                # tenure spans that year (each edition is its own worklist file);
                # ±1 slack for edition-vs-tenure drift.
                if ry is None or (g["year_start"] - 1 <= ry <= g["year_end"] + 1):
                    target.add((g["bio_id"], g["event_index"]))
    grounded_any = grounded_conf | grounded_surn

    base = {"grounded": 0, "scale_adjudication_addressable": 0,
            "extraction_addressable": 0, "ceiling": 0}
    proj = dict(base)
    by_backfill = {"confirmed": 0, "surname_only": 0}
    for row in bio_events:
        if row.get("year_start") is None or not row.get("place"):
            continue
        key = (row["person_id"], row["event_index"])
        grounded = bool(row.get("grounded"))
        gap = gap_index.get(key)
        # bucket the real (baseline) ledger
        if grounded:
            base["grounded"] += 1
        elif gap is None:
            base["scale_adjudication_addressable"] += 1
        elif gap.get("source_file"):
            base["extraction_addressable"] += 1
        else:
            base["ceiling"] += 1
        # bucket the projected ledger (backfill overlay)
        if grounded:
            proj["grounded"] += 1
        elif key in grounded_any:
            proj["grounded"] += 1
            if key in grounded_conf:
                by_backfill["confirmed"] += 1
            else:
                by_backfill["surname_only"] += 1
        elif gap is None:
            proj["scale_adjudication_addressable"] += 1
        elif gap.get("source_file"):
            proj["extraction_addressable"] += 1
        else:
            proj["ceiling"] += 1

    delta = {k: proj[k] - base[k] for k in base}
    result = {
        "note": "projected/pre-load; authoritative lift = loopback.bios_rescued",
        "baseline_ledger": base,
        "projected_ledger": proj,
        "delta": delta,
        "newly_grounded_by_backfill": by_backfill,
    }
    out = data / "backfill" / "projected_ledger.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=1))
    return result
