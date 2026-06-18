"""Compile adjudicator verdicts into tiered, guard-checked outputs.

The adjudicator (an LLM reading one dossier) returns a schema.Verdict per
case into <adjudication>/verdicts_raw/{case_id}.json (and a second
independent pass into {case_id}.pass2.json). The model NEVER gets the last
word: `compile_verdicts` re-applies the deterministic rules and demotes
anything that fails.

Guards (each forced by a measured failure mode — do not relax):
1. unknown_pair   — an assignment with no gate-passing candidate behind it
                    is stripped outright; the model cannot invent pairs.
2. age_gate       — re-checked from the graph cache (defense in depth).
3. citation       — every cited fact must appear in the dossier text
                    (fuzz.partial_ratio >= 92, the same hallucination check
                    the parsers face); a fabricated quote demotes the verdict.
4. blocking_key   — citations that are just the surname are stripped; a
                    verdict left with no real citation is demoted.
5. single_initial — single-initial bios need a strong dimension (position
                    >= 60 / shared honour / >= 2-edition co-occurrence)
                    regardless of model confidence.
6. contested      — a stint with a comparable-strength competitor inside the
                    case (phase-1 strength gap < AMBIGUITY_MARGIN) can never
                    be confirmed.
7. second_pass    — `confirm` additionally requires an independent second
                    pass that assigned the same stints to the same bio with
                    `certain` confidence. No second pass, no confirm.

Tiers: confirm (publishable) / review (ranked human queue) / unlinked
(default). duplicate_bio_groups are never acted on automatically — they go
to merge_review.jsonl.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from rapidfuzz import fuzz

from .match import AMBIGUITY_MARGIN, POSITION_SIM, _norm
from .schema import Biography, Case, StintCandidate, Verdict, VerdictPerson

CITATION_SIM = 92.0
PROMPT_PATH = Path(__file__).parent / "prompts" / "adjudicate_v1.md"

_TIER_BY_CONFIDENCE = {"certain": "confirm", "probable": "review",
                       "uncertain": "unlinked"}
_TIER_RANK = {"confirm": 0, "review": 1, "unlinked": 2}


def _demote(tier: str, floor: str) -> str:
    return tier if _TIER_RANK[tier] >= _TIER_RANK[floor] else floor


def check_person(
    person: VerdictPerson,
    case: Case,
    by_pair: dict[tuple[str, str], StintCandidate],
    dossier_text: str,
    bios_by_id: dict[str, Biography],
    officials_by_id: dict[str, dict],
) -> tuple[str, list[str], list[str]]:
    """Apply guards 1–6 to one person-verdict. Returns
    (tier, guard_trace, kept_stint_ids)."""
    trace: list[str] = []
    tier = _TIER_BY_CONFIDENCE.get(person.confidence, "unlinked")
    bio = bios_by_id.get(person.bio_id)
    if bio is None or person.bio_id not in case.bio_ids:
        return "unlinked", [f"unknown_bio:{person.bio_id}"], []

    kept: list[str] = []
    for stint_id in person.stint_ids:
        pair = by_pair.get((person.bio_id, stint_id))
        if pair is None:
            trace.append(f"unknown_pair:{stint_id}")
            continue  # stripped: not a gate-passing candidate
        official = officials_by_id.get(stint_id)
        fy = official.get("first_year") if official else None
        if fy is not None and bio.birth_year \
                and fy < bio.birth_year.value + 15:
            trace.append(f"age_gate:{stint_id}")
            continue
        if fy is not None and bio.terminal and bio.terminal.kind == "died" \
                and bio.terminal.year and fy > bio.terminal.year:
            trace.append(f"age_gate:{stint_id}")
            continue
        if pair.single_initial and not (
            pair.best_position_score >= POSITION_SIM
            or pair.honour_overlap or len(pair.cooc_years) >= 2
        ):
            tier = _demote(tier, "review")
            trace.append(f"single_initial:{stint_id}")
        competitors = [c for (b, s), c in by_pair.items()
                       if s == stint_id and b != person.bio_id]
        for comp in competitors:
            gap = abs((pair.phase1_strength or 0)
                      - (comp.phase1_strength or 0))
            if gap < AMBIGUITY_MARGIN:
                tier = _demote(tier, "review")
                trace.append(f"contested:{stint_id}:{comp.bio_id}")
                break
        kept.append(stint_id)

    # citations: strip surname-only facts, then verify the rest verbatim
    surname = _norm(bio.surname)
    real_citations = 0
    text_lower = dossier_text.lower()
    for ev in person.evidence_cited:
        if _norm(ev.fact) == surname:
            trace.append("blocking_key_citation_stripped")
            continue
        if fuzz.partial_ratio(ev.fact.lower(), text_lower) < CITATION_SIM:
            tier = _demote(tier, "review")
            trace.append(f"citation_unverified:{ev.fact[:60]!r}")
            continue
        real_citations += 1
    if kept and real_citations == 0:
        tier = _demote(tier, "review")
        trace.append("no_verifiable_citations")
    if not person.arguments_against.strip():
        tier = _demote(tier, "review")
        trace.append("missing_arguments_against")
    if not kept:
        tier = "unlinked"
    return tier, trace, kept


def _passes_agree(p1: VerdictPerson, kept1: list[str],
                  verdict2: Verdict) -> bool:
    """Guard 7: the second pass must assign the same stints to this bio,
    also at `certain`."""
    for p2 in verdict2.persons:
        if p2.bio_id == p1.bio_id:
            return (set(p2.stint_ids) == set(kept1)
                    and p2.confidence == "certain")
    return False


def compile_verdicts(adj_dir: Path, bios_by_id: dict[str, Biography],
                     officials_by_id: dict[str, dict],
                     candidates: list[StintCandidate]) -> dict:
    """Read verdicts_raw/, apply guards, write verdicts.jsonl,
    review_queue.jsonl, merge_review.jsonl and a summary report."""
    cases = {c.case_id: c for c in
             (Case.model_validate_json(l)
              for l in (adj_dir / "cases.jsonl").open(encoding="utf-8"))}
    by_pair_all: dict[tuple[str, str], StintCandidate] = {
        (c.bio_id, c.official_id): c for c in candidates}

    raw_dir = adj_dir / "verdicts_raw"
    rows: list[dict] = []
    merge_rows: list[dict] = []
    parse_failures: list[str] = []
    for path in sorted(raw_dir.glob("*.json")):
        if path.name.endswith(".pass2.json"):
            continue
        try:
            verdict = Verdict.model_validate_json(path.read_text(encoding="utf-8"))
        except Exception as e:  # malformed model output -> review, not crash
            parse_failures.append(f"{path.name}: {e}")
            continue
        case = cases.get(verdict.case_id)
        if case is None:
            parse_failures.append(f"{path.name}: unknown case_id")
            continue
        dossier_path = adj_dir / "dossiers" / f"{case.case_id}.md"
        dossier_text = dossier_path.read_text(encoding="utf-8") \
            if dossier_path.exists() else ""
        by_pair = {(b, s): c for (b, s), c in by_pair_all.items()
                   if b in case.bio_ids and s in case.stint_ids}

        pass2_path = raw_dir / f"{case.case_id}.pass2.json"
        verdict2 = None
        if pass2_path.exists():
            try:
                verdict2 = Verdict.model_validate_json(
                    pass2_path.read_text(encoding="utf-8"))
            except Exception:
                pass

        assigned: set[str] = set()
        for person in verdict.persons:
            tier, trace, kept = check_person(
                person, case, by_pair, dossier_text, bios_by_id,
                officials_by_id)
            if tier == "confirm":
                if verdict2 is None:
                    tier = "review"
                    trace.append("no_second_pass")
                elif not _passes_agree(person, kept, verdict2):
                    tier = "review"
                    trace.append("second_pass_disagrees")
            assigned.update(kept)
            rows.append({
                "case_id": case.case_id,
                "bio_id": person.bio_id,
                "stint_ids": kept,
                "tier": tier,
                "confidence": person.confidence,
                "guard_trace": trace,
                "arguments_against": person.arguments_against,
                "evidence_cited": [e.model_dump() for e in person.evidence_cited],
                "would_overturn": person.would_overturn,
                "notes": verdict.notes,
            })
        for group in verdict.duplicate_bio_groups:
            merge_rows.append({"case_id": case.case_id, "bio_ids": group,
                               "notes": verdict.notes})
        for s in set(case.stint_ids) - assigned:
            reasons = {u.stint_id: u.reason for u in verdict.unassigned_stints}
            rows.append({
                "case_id": case.case_id, "bio_id": None, "stint_ids": [s],
                "tier": "unlinked", "confidence": None,
                "guard_trace": [], "arguments_against": "",
                "evidence_cited": [],
                "would_overturn": "",
                "notes": reasons.get(s, ""),
            })

    def _review_rank(row: dict) -> tuple:
        bio = bios_by_id.get(row["bio_id"] or "")
        if bio is None:
            return (0, 0, 0, 0)
        years = [y for ev in bio.events for y in (ev.year_start, ev.year_end)
                 if y is not None]
        span = max(years) - min(years) if years else 0
        colonies = {s.split("___")[1] for s in row["stint_ids"]
                    if "___" in s}
        return (len(bio.honours), span, len(colonies) > 1, len(bio.editions))

    with (adj_dir / "verdicts.jsonl").open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    review = sorted((r for r in rows if r["tier"] == "review"),
                    key=_review_rank, reverse=True)
    with (adj_dir / "review_queue.jsonl").open("w", encoding="utf-8") as fh:
        for r in review:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with (adj_dir / "merge_review.jsonl").open("w", encoding="utf-8") as fh:
        for r in merge_rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    guard_counts: dict[str, int] = defaultdict(int)
    for r in rows:
        for t in r["guard_trace"]:
            guard_counts[t.split(":")[0]] += 1
    stats = {
        "cases_with_verdicts": len({r["case_id"] for r in rows}),
        "person_verdicts": sum(1 for r in rows if r["bio_id"]),
        "confirm": sum(1 for r in rows if r["tier"] == "confirm"),
        "review": sum(1 for r in rows if r["tier"] == "review"),
        "unlinked": sum(1 for r in rows if r["tier"] == "unlinked"),
        "stints_confirmed": sum(len(r["stint_ids"]) for r in rows
                                if r["tier"] == "confirm"),
        "duplicate_bio_groups": len(merge_rows),
        "guard_triggers": dict(sorted(guard_counts.items())),
        "parse_failures": parse_failures,
    }
    report_dir = adj_dir / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    lines = ["# Adjudication compile report", ""]
    for k, v in stats.items():
        lines.append(f"- **{k}**: {json.dumps(v)}")
    (report_dir / "adjudication_report.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8")
    return stats
