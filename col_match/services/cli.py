"""col-services: CLI for the services-section pipeline.

Stages write JSONL under <data_dir> (default data/services/ in this repo);
nothing here writes to the production graph.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from col_match.config import Config

from . import corpus as corpus_mod


def _volumes(cfg: Config, args) -> list:
    if args.volume:
        return [corpus_mod.get_volume(cfg.corpus_dir, args.volume)]
    return corpus_mod.discover_volumes(cfg.corpus_dir)


def cmd_volumes(cfg: Config, args) -> int:
    for vol in corpus_mod.discover_volumes(cfg.corpus_dir):
        print(f"{vol.name:35s} {vol.year}  {vol.era}")
    return 0


def cmd_segment(cfg: Config, args) -> int:
    from .segment import segment_volume

    out_dir = Path(cfg.data_dir) / "raw_entries"
    out_dir.mkdir(parents=True, exist_ok=True)
    all_stats = []
    for vol in _volumes(cfg, args):
        entries, stats = segment_volume(vol)
        out = out_dir / f"{vol.name}.jsonl"
        with out.open("w", encoding="utf-8") as f:
            for e in entries:
                f.write(e.model_dump_json(exclude_none=True) + "\n")
        all_stats.append(stats)
        print(
            f"{vol.name:35s} section={stats.get('section')} entries={stats['entries']:5d} "
            f"twins={stats.get('twins', 0):4d} no_dash={stats.get('no_dash', 0):3d} "
            f"orphans={stats.get('orphan_lines', 0):3d}"
        )
    (Path(cfg.data_dir) / "segment_stats.json").write_text(json.dumps(all_stats, indent=2))
    return 0


def cmd_dedup(cfg: Config, args) -> int:
    from .dedup import dedup_entries
    from .schema import RawEntry

    raw_dir = Path(cfg.data_dir) / "raw_entries"
    entries = []
    for f in sorted(raw_dir.glob("*.jsonl")):
        with f.open(encoding="utf-8") as fh:
            entries.extend(RawEntry.model_validate_json(line) for line in fh)
    versions, stats = dedup_entries(entries)
    out = Path(cfg.data_dir) / "entry_versions.jsonl"
    with out.open("w", encoding="utf-8") as fh:
        for v in versions:
            fh.write(v.model_dump_json() + "\n")
    print(json.dumps(stats, indent=2))
    return 0


def cmd_parse_rules(cfg: Config, args) -> int:
    from .rules_parse import parse_rules
    from .schema import EntryVersion
    from .validate import validate_parsed

    data = Path(cfg.data_dir)
    out_dir = data / "parsed"
    out_dir.mkdir(parents=True, exist_ok=True)
    n = ok = 0
    fail_reasons: dict[str, int] = {}
    with (data / "entry_versions.jsonl").open(encoding="utf-8") as fh, \
         (out_dir / "rules.jsonl").open("w", encoding="utf-8") as out_ok, \
         (data / "pending_llm.jsonl").open("w", encoding="utf-8") as out_llm:
        for line in fh:
            v = EntryVersion.model_validate_json(line)
            n += 1
            parsed = parse_rules(v, cfg.data_dir)
            fatal = validate_parsed(parsed, v) if parsed else ["rules_unparsed"]
            if parsed and not fatal:
                ok += 1
                out_ok.write(parsed.model_dump_json(exclude_none=True) + "\n")
            else:
                for r in fatal:
                    key = r.split(":")[0]
                    fail_reasons[key] = fail_reasons.get(key, 0) + 1
                out_llm.write(line)
    share = 100 * ok / max(n, 1)
    print(f"rules tier: {ok}/{n} accepted ({share:.1f}%), {n - ok} -> LLM tier")
    print("failure reasons:", json.dumps(dict(sorted(fail_reasons.items(), key=lambda x: -x[1]))))
    return 0


def _pending_versions(cfg: Config):
    from .schema import EntryVersion

    path = Path(cfg.data_dir) / "pending_llm.jsonl"
    with path.open(encoding="utf-8") as fh:
        return [EntryVersion.model_validate_json(line) for line in fh]


def _versions_by_id(cfg: Config):
    from .schema import EntryVersion

    out = {}
    with (Path(cfg.data_dir) / "entry_versions.jsonl").open(encoding="utf-8") as fh:
        for line in fh:
            v = EntryVersion.model_validate_json(line)
            out[v.version_id] = v
    return out


def cmd_llm_submit(cfg: Config, args) -> int:
    from .llm_parse import submit_batch

    versions = _pending_versions(cfg)
    if args.limit:
        versions = versions[: args.limit]
    submit_batch(versions, cfg.data_dir, cfg.google_api_key, tag=args.tag or "main")
    return 0


def cmd_llm_poll(cfg: Config, args) -> int:
    from .llm_parse import harvest, poll_and_collect

    summary = poll_and_collect(cfg.data_dir, cfg.google_api_key)
    print(json.dumps(summary, indent=1))
    if any(s == "JOB_STATE_SUCCEEDED" for s in summary.values()) or not summary:
        stats = harvest(cfg.data_dir, _versions_by_id(cfg))
        print(json.dumps(stats, indent=1))
    return 0


def cmd_llm_escalate(cfg: Config, args) -> int:
    from .llm_parse import escalate_interactive

    stats = escalate_interactive(cfg.data_dir, _versions_by_id(cfg), cfg.google_api_key)
    print(json.dumps(stats, indent=1))
    return 0


def cmd_check_twins(cfg: Config, args) -> int:
    """Double-printed entries (1939 etc.) = two OCR readings of the same
    plate. Parse both with the rules tier and compare: the structured
    disagreement rate is a free empirical OCR+parse error bound."""
    from .rules_parse import parse_rules
    from .schema import EntryVersion, RawEntry
    from .validate import validate_parsed

    raw_dir = Path(cfg.data_dir) / "raw_entries"
    pairs = both_ok = 0
    agree = {"surname": 0, "birth_year": 0, "event_years": 0, "n_events": 0}
    for f in sorted(raw_dir.glob("*.jsonl")):
        with f.open(encoding="utf-8") as fh:
            for line in fh:
                e = RawEntry.model_validate_json(line)
                if not e.twin_text:
                    continue
                pairs += 1
                results = []
                for text in (e.raw_text, e.twin_text):
                    v = EntryVersion(
                        version_id="twin", surname_key="", canonical_text=text,
                        era=e.era, edition_year=e.edition_year,
                        entry_ids=[], attesting_editions=[e.edition_year],
                    )
                    p = parse_rules(v, cfg.data_dir)
                    results.append(p if p and not validate_parsed(p, v) else None)
                a, b = results
                if not (a and b):
                    continue
                both_ok += 1
                agree["surname"] += a.surname == b.surname
                agree["birth_year"] += a.birth_year == b.birth_year
                agree["n_events"] += len(a.events) == len(b.events)
                ya = [ev.year_start for ev in a.events]
                yb = [ev.year_start for ev in b.events]
                agree["event_years"] += ya == yb
    print(f"twin pairs: {pairs}, both rules-parsed: {both_ok}")
    for k, v in agree.items():
        print(f"  {k} agreement: {v}/{both_ok} ({100 * v / max(both_ok, 1):.1f}%)")
    return 0


def _norm_text(s):
    import re as _re

    return _re.sub(r"[^a-z0-9 ]", "", (s or "").lower()).strip()


def cmd_eval_gold(cfg: Config, args) -> int:
    from rapidfuzz import fuzz

    data = Path(cfg.data_dir)
    gold = [json.loads(l) for l in (data / "gold" / "gold_entries.jsonl").open(encoding="utf-8")]
    parsed = {}
    for name in ("rules.jsonl", "llm.jsonl"):
        p = data / "parsed" / name
        if p.exists():
            for line in p.open(encoding="utf-8"):
                rec = json.loads(line)
                parsed[rec["version_id"]] = rec

    per_tier: dict[str, dict] = {}
    unparsed = []
    for g in gold:
        rec = parsed.get(g["version_id"])
        if rec is None:
            unparsed.append(g["version_id"])
            continue
        tier = rec.get("parser", "rules")
        t = per_tier.setdefault(tier, {
            "n": 0, "surname": 0, "given": 0, "birth": 0,
            "req_events": 0, "matched_req": 0, "parser_events": 0, "matched_any": 0,
            "place_pairs": 0, "place_ok": 0, "pos_pairs": 0, "pos_ok": 0,
        })
        t["n"] += 1
        t["surname"] += _norm_text(rec["surname"]) == _norm_text(g["surname"])
        t["given"] += _norm_text(rec.get("given_names")) == _norm_text(g.get("given_names"))
        t["birth"] += rec.get("birth_year") == g.get("birth_year")

        pev = list(rec.get("events", []))
        used = set()

        def take(ge):
            best, best_score = None, -1
            for i, ev in enumerate(pev):
                if i in used or ev.get("year_start") != ge["year_start"]:
                    continue
                score = fuzz.token_set_ratio(_norm_text(ev.get("position")), _norm_text(ge.get("position")))
                if _norm_text(ev.get("place")) == _norm_text(ge.get("place")):
                    score += 30
                if score > best_score:
                    best, best_score = i, score
            if best is not None:
                used.add(best)
            return best

        required = [e for e in g["events"] if not e.get("optional")]
        t["req_events"] += len(required)
        for ge in required:
            i = take(ge)
            if i is None:
                continue
            t["matched_req"] += 1
            ev = pev[i]
            if ge.get("place"):
                t["place_pairs"] += 1
                t["place_ok"] += _norm_text(ev.get("place")) == _norm_text(ge["place"])
            if ge.get("position"):
                t["pos_pairs"] += 1
                t["pos_ok"] += fuzz.token_set_ratio(_norm_text(ev.get("position")), _norm_text(ge["position"])) >= 70
        for ge in [e for e in g["events"] if e.get("optional")]:
            take(ge)  # consume optionals so they don't hurt precision
        t["parser_events"] += len(pev)
        t["matched_any"] += len(used)

    for tier, t in per_tier.items():
        n = t["n"]
        print(f"\n[{tier}] entries evaluated: {n}")
        print(f"  surname:      {t['surname']}/{n}")
        print(f"  given_names:  {t['given']}/{n}")
        print(f"  birth_year:   {t['birth']}/{n}")
        print(f"  event recall: {t['matched_req']}/{t['req_events']} "
              f"({100 * t['matched_req'] / max(t['req_events'], 1):.0f}%)")
        print(f"  event precision: {t['matched_any']}/{t['parser_events']} "
              f"({100 * t['matched_any'] / max(t['parser_events'], 1):.0f}%)")
        print(f"  place acc (matched, gold-placed): {t['place_ok']}/{t['place_pairs']}")
        print(f"  position acc (matched):           {t['pos_ok']}/{t['pos_pairs']}")
    if unparsed:
        print(f"\nnot yet parsed ({len(unparsed)}): {unparsed}")
    return 0


def _load_parsed(cfg: Config):
    """All accepted ParsedEntries; rules tier wins on duplicate version_ids
    (a pilot batch may have parsed entries that later rules-parse)."""
    from .schema import ParsedEntry

    out = {}
    for name in ("llm.jsonl", "rules.jsonl"):  # rules last -> wins
        p = Path(cfg.data_dir) / "parsed" / name
        if p.exists():
            for line in p.open(encoding="utf-8"):
                rec = ParsedEntry.model_validate_json(line)
                out[rec.version_id] = rec
    return list(out.values())


def cmd_compile(cfg: Config, args) -> int:
    from .compile import (compile_biographies, recover_places_from_positions,
                          recover_places_from_prose)
    from .schema import RawEntry

    raw_texts = {}
    for f in (Path(cfg.data_dir) / "raw_entries").glob("*.jsonl"):
        for line in f.open(encoding="utf-8"):
            e = RawEntry.model_validate_json(line)
            raw_texts[e.entry_id] = e.raw_text
    pairs_path = Path(cfg.data_dir) / "matches" / "record_merge_pairs.json"
    pairs = json.loads(pairs_path.read_text()) if pairs_path.exists() else None
    # human/LLM-adjudicated dedup ledger (one merge group per line)
    ledger_path = Path(cfg.data_dir) / "dedup" / "llm_merges.jsonl"
    llm_groups = None
    if ledger_path.exists():
        llm_groups = [json.loads(l)["versions"]
                      for l in ledger_path.open(encoding="utf-8") if l.strip()]
    parsed = _load_parsed(cfg)
    fixed = recover_places_from_positions(parsed, cfg.data_dir)
    print(f"recovered {fixed} places from position strings (abbreviations)", file=sys.stderr)
    prose_fixed = recover_places_from_prose(parsed, cfg.data_dir)
    print(f"recovered {prose_fixed} places from mid-clause prose colonies", file=sys.stderr)
    bios, stats = compile_biographies(parsed, _versions_by_id(cfg), raw_texts, pairs,
                                      llm_merge_groups=llm_groups)
    out = Path(cfg.data_dir) / "biographies"
    out.mkdir(parents=True, exist_ok=True)
    with (out / "biographies.jsonl").open("w", encoding="utf-8") as fh:
        for b in bios:
            fh.write(b.model_dump_json(exclude_none=True) + "\n")
    print(json.dumps(stats, indent=1))
    return 0


def cmd_fetch_graph(cfg: Config, args) -> int:
    from col_match.graph import connect, fetch_all_officials, fetch_possible_match_edges

    out = Path(cfg.data_dir) / "graph_cache"
    out.mkdir(parents=True, exist_ok=True)
    n = 0
    with connect(cfg) as driver:
        with (out / "officials.jsonl").open("w", encoding="utf-8") as fh:
            for o in fetch_all_officials(driver, cfg=cfg):
                fh.write(json.dumps(o, ensure_ascii=False, default=str) + "\n")
                n += 1
        edges = fetch_possible_match_edges(driver, cfg=cfg)
    (out / "possible_match_edges.json").write_text(json.dumps(edges))
    print(f"cached {n} officials (with surviving evidence), {len(edges)} edges")
    return 0


def _load_graph_cache(cfg: Config):
    out = Path(cfg.data_dir) / "graph_cache"
    # opt-in: prefer the backfill-augmented officials when COL_USE_AUGMENTED=1
    # and it exists, so attach/match see recovered staff-list rows. Default off
    # leaves every other consumer on the pristine Neo4j fetch.
    aug = out / "officials_augmented.jsonl"
    src = aug if (os.environ.get("COL_USE_AUGMENTED") == "1" and aug.exists()) else out / "officials.jsonl"
    officials = [json.loads(l) for l in src.open(encoding="utf-8")]
    edges = [tuple(e) for e in json.loads((out / "possible_match_edges.json").read_text())]
    return officials, edges


def cmd_match(cfg: Config, args) -> int:
    from .infer_colony import apply_recovered_places
    from .match import match_biographies
    from .schema import Biography

    bios = [Biography.model_validate_json(l)
            for l in (Path(cfg.data_dir) / "biographies" / "biographies.jsonl").open(encoding="utf-8")]
    placed = apply_recovered_places(bios, cfg.data_dir)
    if placed:
        print(f"applied {placed} recovered places (infer_colony)", file=sys.stderr)
    officials, _ = _load_graph_cache(cfg)
    matches, stats = match_biographies(bios, officials, cfg.data_dir)
    out = Path(cfg.data_dir) / "matches"
    out.mkdir(parents=True, exist_ok=True)
    with (out / "stint_matches.jsonl").open("w", encoding="utf-8") as fh:
        for m in matches:
            fh.write(m.model_dump_json() + "\n")
    print(json.dumps(stats, indent=1))
    return 0


def cmd_coverage(cfg: Config, args) -> int:
    from .coverage import coverage_report
    from .schema import StintMatch

    officials, edges = _load_graph_cache(cfg)
    matches = [StintMatch.model_validate_json(l)
               for l in (Path(cfg.data_dir) / "matches" / "stint_matches.jsonl").open(encoding="utf-8")]
    report = coverage_report(officials, matches, edges, Path(cfg.data_dir) / "reports")
    print(json.dumps({k: v for k, v in report.items() if not isinstance(v, dict)}, indent=1))
    return 0


def cmd_eval_known(cfg: Config, args) -> int:
    """Known-careers FP gate: must print 0 false positives at both levels
    after any matching change."""
    from .eval_known import load_known_careers, load_phase1_links, score_links

    careers = load_known_careers()
    stint_links, record_links = load_phase1_links(cfg.data_dir)
    failed = False
    for links, level in ((stint_links, "stint"), (record_links, "record")):
        rep = score_links(careers, links, level)
        details = rep.pop("fp_details")
        print(json.dumps(rep, indent=1))
        for fp in details:
            print(f"  FP [{level}] career={fp['career_id']} bio={fp['bio_id']} "
                  f"claimed negatives: {fp['negatives_claimed']}", file=sys.stderr)
        failed = failed or rep["false_positives"] > 0
    return 1 if failed else 0


def _load_bios(cfg: Config):
    from .schema import Biography

    path = Path(cfg.data_dir) / "biographies" / "biographies.jsonl"
    return [Biography.model_validate_json(l) for l in path.open(encoding="utf-8")]


def cmd_candidates(cfg: Config, args) -> int:
    """Enumerate below-bar candidates with evidence annotations (the input
    population for dossier adjudication)."""
    from .candidates import enumerate_candidates
    from .infer_colony import apply_recovered_places

    data = Path(cfg.data_dir)
    bios = _load_bios(cfg)
    # mirror cmd_match's recovered-place overlay so enumeration sees the SAME
    # bios the matcher did — otherwise matches that rely on a recovered colony
    # can't be reproduced and reconciliation fails spuriously.
    apply_recovered_places(bios, cfg.data_dir)
    officials, _ = _load_graph_cache(cfg)
    stint_pairs: set[tuple[str, str]] = set()
    linked: set[str] = set()
    with (data / "matches" / "stint_matches.jsonl").open(encoding="utf-8") as fh:
        for line in fh:
            m = json.loads(line)
            stint_pairs.add((m["bio_id"], m["official_id"]))
            linked.add(m["bio_id"])
    with (data / "matches" / "record_attachments.jsonl").open(encoding="utf-8") as fh:
        for line in fh:
            linked.add(json.loads(line)["bio_id"])
    cands, stats = enumerate_candidates(bios, officials, cfg.data_dir,
                                        stint_pairs, linked)
    out = data / "candidates"
    out.mkdir(parents=True, exist_ok=True)
    with (out / "below_bar.jsonl").open("w", encoding="utf-8") as fh:
        for c in cands:
            fh.write(c.model_dump_json() + "\n")
    (out / "candidates_stats.json").write_text(json.dumps(stats, indent=1))
    print(json.dumps(stats, indent=1))
    if stats["phase1_matches_not_reproduced"]:
        print("RECONCILIATION FAILURE: accepted phase-1 matches missing from "
              "enumeration", file=sys.stderr)
        return 1
    return 0


def cmd_dossiers(cfg: Config, args) -> int:
    """Build adjudication cases from below-bar candidates and render one
    markdown dossier per adjudicable case."""
    from .dossier import TOKEN_CAP, build_cases, est_tokens, render_dossier
    from .schema import StintCandidate

    data = Path(cfg.data_dir)
    cands = [StintCandidate.model_validate_json(l)
             for l in (data / "candidates" / "below_bar.jsonl").open(encoding="utf-8")]
    bios_by_id = {b.bio_id: b for b in _load_bios(cfg)}
    officials, _ = _load_graph_cache(cfg)
    officials_by_id = {o["id"]: o for o in officials}
    versions_by_id = _versions_by_id(cfg)

    cases = build_cases(cands)
    if args.limit:
        cases = cases[: args.limit]
    by_case_bio: dict[str, list] = {}
    for c in cands:
        by_case_bio.setdefault(c.bio_id, []).append(c)

    out_dir = data / "adjudication"
    dossier_dir = out_dir / "dossiers"
    dossier_dir.mkdir(parents=True, exist_ok=True)
    n_rendered = n_oversized = 0
    with (out_dir / "cases.jsonl").open("w", encoding="utf-8") as fh:
        for case in cases:
            if case.route == "adjudicate":
                case_cands = [c for b in case.bio_ids
                              for c in by_case_bio.get(b, [])]
                text = render_dossier(case, case_cands, bios_by_id,
                                      officials_by_id, versions_by_id)
                case.est_tokens = est_tokens(text)
                if case.est_tokens > TOKEN_CAP:
                    case.route = "review_oversized"
                else:
                    (dossier_dir / f"{case.case_id}.md").write_text(
                        text, encoding="utf-8")
                    n_rendered += 1
            if case.route == "review_oversized":
                n_oversized += 1
            fh.write(case.model_dump_json() + "\n")
    stats = {
        "cases": len(cases),
        "rendered": n_rendered,
        "review_oversized": n_oversized,
        "candidates": len(cands),
    }
    (out_dir / "cases_stats.json").write_text(json.dumps(stats, indent=1))
    print(json.dumps(stats, indent=1))
    return 0


_SENIOR_KW = ("governor", "chief justice", "colonial secretary",
              "commissioner", "chief sec", "attorney-gen", "puisne judge",
              "treasurer", "auditor-gen")
_JUNIOR_KW = ("clerk", "cadet", "asst", "assistant", "junior")


def _load_candidates(path: Path):
    from .schema import StintCandidate

    return [StintCandidate.model_validate_json(l)
            for l in path.open(encoding="utf-8")]


def _adj_dir(cfg: Config, args) -> Path:
    base = "adjudication_calib" if getattr(args, "calibration", False) \
        else "adjudication"
    return Path(cfg.data_dir) / base


def cmd_pilot_sample(cfg: Config, args) -> int:
    """Pick ~50 adjudicable cases, stratified by seniority with forced
    inclusion of the known trap categories. Deterministic (no RNG)."""
    from .schema import Case

    data = Path(cfg.data_dir)
    cases = [Case.model_validate_json(l)
             for l in (data / "adjudication" / "cases.jsonl").open(encoding="utf-8")]
    cases = [c for c in cases if c.route == "adjudicate"]
    cands = _load_candidates(data / "candidates" / "below_bar.jsonl")
    by_bio: dict[str, list] = {}
    for c in cands:
        by_bio.setdefault(c.bio_id, []).append(c)
    bios_by_id = {b.bio_id: b for b in _load_bios(cfg)}

    def seniority(case) -> str:
        positions = " ".join((ev.position or "").lower()
                             for b in case.bio_ids
                             for ev in bios_by_id[b].events)
        if any(bios_by_id[b].honours for b in case.bio_ids) \
                or any(k in positions for k in _SENIOR_KW):
            return "senior"
        if positions and all(
            any(k in (ev.position or "").lower() for k in _JUNIOR_KW)
            for b in case.bio_ids for ev in bios_by_id[b].events
            if ev.position
        ):
            return "junior"
        return "mid"

    def traits(case) -> set[str]:
        out = set()
        if len(case.bio_ids) > 1 or len(case.stint_ids) > 1:
            out.add("multi")
        for b in case.bio_ids:
            for c in by_bio.get(b, []):
                if c.official_id not in case.stint_ids:
                    continue
                if c.single_initial:
                    out.add("single_initial")
                if c.phase1_dropped_ambiguous:
                    out.add("dropped_ambiguous")
                if c.surname_gate != "exact":
                    out.add("fuzzy")
        return out

    total = args.limit or 50
    quotas = {"senior": round(total * 0.3), "junior": round(total * 0.3)}
    quotas["mid"] = total - sum(quotas.values())
    forced = {"multi": 10, "single_initial": 5, "dropped_ambiguous": 5,
              "fuzzy": 3}
    picked: dict[str, dict] = {}
    annotated = [(c, seniority(c), traits(c)) for c in cases]
    for trait, need in forced.items():
        for c, s, t in annotated:
            if need <= 0:
                break
            if trait in t and c.case_id not in picked:
                picked[c.case_id] = {"case_id": c.case_id, "seniority": s,
                                     "traits": sorted(t)}
                quotas[s] = max(0, quotas[s] - 1)
                need -= 1
    for c, s, t in annotated:
        if len(picked) >= total:
            break
        if c.case_id in picked or quotas.get(s, 0) <= 0:
            continue
        picked[c.case_id] = {"case_id": c.case_id, "seniority": s,
                             "traits": sorted(t)}
        quotas[s] -= 1
    sample = sorted(picked.values(), key=lambda r: r["case_id"])
    out = data / "adjudication" / "pilot_cases.json"
    out.write_text(json.dumps(sample, indent=1))
    from collections import Counter

    print(json.dumps({
        "picked": len(sample),
        "seniority": dict(Counter(r["seniority"] for r in sample)),
        "traits": dict(Counter(t for r in sample for t in r["traits"])),
        "file": str(out),
    }, indent=1))
    return 0


def cmd_adjudicate_compile(cfg: Config, args) -> int:
    """Apply deterministic guards to raw verdicts and write tiered outputs."""
    from .adjudicate import compile_verdicts

    data = Path(cfg.data_dir)
    adj = _adj_dir(cfg, args)
    cand_path = adj / "candidates.jsonl"
    if not cand_path.exists():
        cand_path = data / "candidates" / "below_bar.jsonl"
    cands = _load_candidates(cand_path)
    bios_by_id = {b.bio_id: b for b in _load_bios(cfg)}
    officials, _ = _load_graph_cache(cfg)
    officials_by_id = {o["id"]: o for o in officials}
    stats = compile_verdicts(adj, bios_by_id, officials_by_id, cands)
    print(json.dumps(stats, indent=1))
    return 0


def cmd_calib_build(cfg: Config, args) -> int:
    """Build blind calibration cases + dossiers from the known careers into
    data/services/adjudication_calib/. The answer key (labels.json) lives
    beside the dossiers but its content never appears inside them."""
    from .dossier import TOKEN_CAP, est_tokens, render_dossier
    from .eval_known import (build_calibration_cases, load_known_careers,
                             load_phase1_links)

    careers = load_known_careers()
    bios = _load_bios(cfg)
    officials, _ = _load_graph_cache(cfg)
    stint_links, _ = load_phase1_links(cfg.data_dir)
    cands, cases, labels, stats = build_calibration_cases(
        careers, bios, officials, cfg.data_dir, stint_links)
    if args.limit:
        cases = cases[: args.limit]

    bios_by_id = {b.bio_id: b for b in bios}
    officials_by_id = {o["id"]: o for o in officials}
    versions_by_id = _versions_by_id(cfg)
    by_bio: dict[str, list] = {}
    for c in cands:
        by_bio.setdefault(c.bio_id, []).append(c)

    adj = Path(cfg.data_dir) / "adjudication_calib"
    dossier_dir = adj / "dossiers"
    dossier_dir.mkdir(parents=True, exist_ok=True)
    n_rendered = n_oversized = 0
    with (adj / "cases.jsonl").open("w", encoding="utf-8") as fh:
        for case in cases:
            case_cands = [c for c in by_bio.get(case.bio_ids[0], [])
                          if c.official_id in case.stint_ids]
            text = render_dossier(case, case_cands, bios_by_id,
                                  officials_by_id, versions_by_id)
            case.est_tokens = est_tokens(text)
            if case.est_tokens > TOKEN_CAP:
                case.route = "review_oversized"
                n_oversized += 1
            else:
                (dossier_dir / f"{case.case_id}.md").write_text(
                    text, encoding="utf-8")
                n_rendered += 1
            fh.write(case.model_dump_json() + "\n")
    with (adj / "candidates.jsonl").open("w", encoding="utf-8") as fh:
        for c in cands:
            fh.write(c.model_dump_json() + "\n")
    (adj / "labels.json").write_text(json.dumps(labels, indent=1))
    stats |= {"rendered": n_rendered, "review_oversized": n_oversized}
    (adj / "calib_stats.json").write_text(json.dumps(stats, indent=1))
    print(json.dumps(stats, indent=1))
    return 0


def cmd_calib_score(cfg: Config, args) -> int:
    """Score compiled calibration verdicts against labels.json. Exit 1 if
    the gate fails (any confirm-tier FP or precision < 99.5%)."""
    from .eval_known import score_verdicts

    adj = Path(cfg.data_dir) / "adjudication_calib"
    labels = json.loads((adj / "labels.json").read_text())
    rows = [json.loads(l) for l in (adj / "verdicts.jsonl").open(encoding="utf-8")]
    report = score_verdicts(rows, labels)
    details = report.pop("fp_details")
    print(json.dumps(report, indent=1))
    for fp in details:
        print(f"  FP [{fp['tier']}] case={fp['case_id']} bio={fp['bio_id']} "
              f"stint={fp['stint_id']}", file=sys.stderr)
    return 0 if report["gate_passed"] else 1


def cmd_gaps(cfg: Config, args) -> int:
    """Find biography-asserted postings the graph has no record for."""
    from .gaps import find_gaps
    from .source_index import load_index

    bios = _load_bios(cfg)
    officials, _ = _load_graph_cache(cfg)
    index = load_index(cfg.source_ocr_dir)
    gaps, stats = find_gaps(bios, officials, cfg.data_dir, index)
    out = Path(cfg.data_dir) / "recovery"
    out.mkdir(parents=True, exist_ok=True)
    with (out / "gaps.jsonl").open("w", encoding="utf-8") as fh:
        for g in gaps:
            fh.write(g.model_dump_json() + "\n")
    (out / "gaps_stats.json").write_text(json.dumps(stats, indent=1))
    print(json.dumps(stats, indent=1))
    return 0


def cmd_recover(cfg: Config, args) -> int:
    """Recover missing rows from source OCR for the detected gaps."""
    from .recover import recover_records
    from .schema import GapEvent

    out = Path(cfg.data_dir) / "recovery"
    gaps = [GapEvent.model_validate_json(l)
            for l in (out / "gaps.jsonl").open(encoding="utf-8")]
    if args.limit:
        gaps = gaps[: args.limit]
    bios_by_id = {b.bio_id: b for b in _load_bios(cfg)}
    stats = recover_records(gaps, bios_by_id, cfg.data_dir, out)
    print(json.dumps(stats, indent=1))
    return 0


def cmd_infer_colony(cfg: Config, args) -> int:
    """Recover the dropped colony for place-less dated biography clauses from
    cross-fragment redundancy (Tier A: staff-list records). Writes the
    auto-accept overlay, the review queue, and a report; does not touch
    attach/match (run those after to realize the lift)."""
    from .infer_colony import run

    bios = _load_bios(cfg)
    officials, _ = _load_graph_cache(cfg)
    window = args.window if args.window is not None else 2
    out = Path(cfg.data_dir) / "inference"
    src = cfg.source_ocr_dir if getattr(args, "raw_ocr", False) else None
    stats = run(bios, officials, cfg.data_dir, out, window=window,
                source_ocr_dir=src)
    print(json.dumps(stats, indent=1))
    return 0


def cmd_augment_officials(cfg: Config, args) -> int:
    """Persist a match target augmented with synthetic stints built from the
    confirmed backfill/recovered staff-list rows (which the Neo4j fetch lacks).
    attach/match pick it up when COL_USE_AUGMENTED=1. Zero API cost — the
    records were already extracted."""
    from .recover import load_recovered_records, synthesize_recovered_stints

    out = Path(cfg.data_dir) / "graph_cache"
    # read the PRISTINE base directly (never the augmented file, to stay idempotent)
    officials = [json.loads(l) for l in (out / "officials.jsonl").open(encoding="utf-8")]
    recs = load_recovered_records(cfg.data_dir,
                                  include_surname_only=getattr(args, "include_surname_only", False))
    stints, stats = synthesize_recovered_stints(recs, officials, cfg.data_dir)
    with (out / "officials_augmented.jsonl").open("w", encoding="utf-8") as fh:
        for o in officials:
            fh.write(json.dumps(o, ensure_ascii=False, default=str) + "\n")
        for s in stints:
            fh.write(json.dumps(s, ensure_ascii=False, default=str) + "\n")
    stats["base_officials"] = len(officials)
    stats["augmented_total"] = len(officials) + len(stints)
    stats["include_surname_only"] = getattr(args, "include_surname_only", False)
    print(json.dumps(stats, indent=1))
    return 0


def cmd_recover_loopback(cfg: Config, args) -> int:
    """Add confirmed recovered records to the officials set, re-enumerate
    candidates, and report how many no-candidate bios become linkable."""
    from .recover import loopback
    from .source_index import load_index  # noqa: F401 (kept for parity)

    bios = _load_bios(cfg)
    officials, _ = _load_graph_cache(cfg)
    stats = loopback(bios, officials, cfg.data_dir)
    print(json.dumps(stats, indent=1))
    return 0


def cmd_assemble(cfg: Config, args) -> int:
    """Assemble the unified person-career graph (JSONL + DuckDB + report)."""
    from .assemble import assemble_graph, load_duckdb, write_report

    data = Path(cfg.data_dir)
    bios = _load_bios(cfg)
    officials, _ = _load_graph_cache(cfg)

    def _jsonl(p):
        return [json.loads(l) for l in p.open(encoding="utf-8")] if p.exists() else []

    stint_matches = _jsonl(data / "matches" / "stint_matches.jsonl")
    attachments = _jsonl(data / "matches" / "record_attachments.jsonl")
    recovered = _jsonl(data / "recovery" / "recovered_records.jsonl")
    merge_groups = _jsonl(data / "adjudication" / "merge_review.jsonl")
    mp = data / "matches" / "record_merge_pairs.json"
    coclaim_pairs = json.loads(mp.read_text()) if mp.exists() else []

    cand_path = data / "candidates" / "below_bar.jsonl"
    candidate_bio_ids = {json.loads(l)["bio_id"]
                         for l in cand_path.open(encoding="utf-8")} \
        if cand_path.exists() else set()
    gap_index: dict = {}
    gpath = data / "recovery" / "gaps.jsonl"
    if gpath.exists():
        for l in gpath.open(encoding="utf-8"):
            g = json.loads(l)
            gap_index[(g["bio_id"], g["event_index"])] = g

    out = data / "graph"
    stats = assemble_graph(bios, officials, stint_matches, attachments,
                           recovered, merge_groups, coclaim_pairs,
                           candidate_bio_ids, gap_index, cfg.data_dir, out)
    print(json.dumps(stats, indent=1))
    print(load_duckdb(out))
    write_report(stats, out)
    return 0


def cmd_attach(cfg: Config, args) -> int:
    from .attach import attach_records
    from .infer_colony import apply_recovered_places
    from .schema import Biography

    bios = [Biography.model_validate_json(l)
            for l in (Path(cfg.data_dir) / "biographies" / "biographies.jsonl").open(encoding="utf-8")]
    placed = apply_recovered_places(bios, cfg.data_dir)
    if placed:
        print(f"applied {placed} recovered places (infer_colony)", file=sys.stderr)
    officials, _ = _load_graph_cache(cfg)
    attachments, stats, merge_pairs = attach_records(bios, officials, cfg.data_dir)
    out = Path(cfg.data_dir) / "matches"
    out.mkdir(parents=True, exist_ok=True)
    with (out / "record_attachments.jsonl").open("w", encoding="utf-8") as fh:
        for a in attachments:
            fh.write(json.dumps(a, ensure_ascii=False) + "\n")
    (out / "record_merge_pairs.json").write_text(json.dumps(merge_pairs, indent=1))
    print(json.dumps(stats, indent=1))
    return 0


# --- extraction backfill ---------------------------------------------------

def cmd_backfill_estimate(cfg: Config, args) -> int:
    """Tokens + USD for the top-N worklist sections; no API calls."""
    from .backfill import estimate_only

    print(json.dumps(estimate_only(cfg, args.top, args.model or cfg.backfill_model),
                     indent=1))
    return 0


def cmd_backfill_extract(cfg: Config, args) -> int:
    """LLM-extract the top-N worklist sections (capped + ledgered)."""
    from .backfill import run_backfill

    stats = run_backfill(
        cfg, top=args.top,
        model=args.model or cfg.backfill_model,
        escalate_model=args.escalate_model or cfg.backfill_escalate_model,
        cap_usd=args.cap if args.cap is not None else cfg.backfill_cap_usd,
        resume=args.resume, backend=args.backend or "openrouter",
        workers=args.workers)
    print(json.dumps(stats, indent=1))
    return 0


def cmd_backfill_measure(cfg: Config, args) -> int:
    """Grounding lift from the backfill records: loopback (authoritative) +
    projected ledger. No graph write."""
    from .backfill import projected_ledger
    from .recover import loopback

    bios = _load_bios(cfg)
    officials, _ = _load_graph_cache(cfg)
    bf = Path(cfg.data_dir) / "backfill" / "backfill_records.jsonl"
    lb = loopback(bios, officials, cfg.data_dir, extra_record_paths=[bf])
    pl = projected_ledger(cfg)
    print(json.dumps({"loopback": lb, "projected_ledger": pl}, indent=1))
    return 0


def _ocr_context(source_file: str, snippet: str, surname: str,
                 radius: int = 3) -> str:
    """±`radius` lines of the source OCR around where the record came from, so a
    reviewer can verify the name truly sits in the text."""
    try:
        lines = Path(source_file).read_text(encoding="utf-8",
                                            errors="replace").splitlines()
    except OSError:
        return "(source file unreadable)"
    needle = (snippet or "")[:24].strip()
    idx = None
    if needle:
        for i, l in enumerate(lines):
            if needle in l:
                idx = i
                break
    if idx is None:
        sl = (surname or "").lower()
        for i, l in enumerate(lines):
            if sl and sl in l.lower():
                idx = i
                break
    if idx is None:
        return "(snippet not located in source)"
    lo, hi = max(0, idx - radius), min(len(lines), idx + radius + 1)
    return "\n".join((">> " if j == idx else "   ") + lines[j]
                     for j in range(lo, hi))


def cmd_backfill_sample(cfg: Config, args) -> int:
    """Deterministic stratified precision sample (no RNG) -> sample.md + jsonl.
    Forces >=10 T2 class-list (Malay States) records, the riskiest tier."""
    from .schema import RecoveredRecord

    data = Path(cfg.data_dir)
    bf = data / "backfill" / "backfill_records.jsonl"
    recs = [RecoveredRecord.model_validate_json(l)
            for l in bf.open(encoding="utf-8") if l.strip()]
    if not recs:
        print("no backfill records to sample", file=sys.stderr)
        return 1
    n = args.n or 40
    half = n // 2

    def strat(pool: list, k: int) -> list:
        pool = sorted(pool, key=lambda r: (r.source_file, r.snippet))
        if not pool or k <= 0:
            return []
        step = max(1, len(pool) // k)
        return pool[::step][:k]

    conf = [r for r in recs if r.confidence == "confirmed_in_ocr"]
    surn = [r for r in recs if r.confidence == "surname_only"]
    picked = strat(conf, half) + strat(surn, n - half)
    seen = {(r.source_file, r.snippet) for r in picked}
    # force >=10 T2 class-list records (Malay States files)
    t2 = [r for r in recs if "MALAY" in Path(r.source_file).name.upper()]
    forced = 0
    for r in sorted(t2, key=lambda r: (r.source_file, r.snippet)):
        if forced >= 10:
            break
        if (r.source_file, r.snippet) not in seen:
            picked.append(r)
            seen.add((r.source_file, r.snippet))
            forced += 1

    out_md = ["# Backfill precision sample", "",
              f"{len(picked)} records. For each: verify (1) the name truly "
              "appears in the OCR context, and (2) the position is correctly "
              "attributed. For matched records also check the bio is the same "
              "person.", ""]
    rows = []
    for i, r in enumerate(picked, 1):
        rows.append(r.model_dump())
        out_md += [
            f"## {i}. {r.name_raw}  [{r.confidence}]",
            f"- colony/year: **{r.colony} {r.year}**",
            f"- position_raw: `{r.position_raw}`",
            f"- surname/given: `{r.surname}` / `{r.given_names}`",
            f"- matched bio: `{r.predicted_by_bio_id or '(none)'}`"
            + (f"  bio_position: `{r.bio_position}`" if r.bio_position else ""),
            f"- source: `{Path(r.source_file).name}`",
            "- snippet: " + (r.snippet or ""),
            "```",
            _ocr_context(r.source_file, r.snippet, r.surname),
            "```",
            "- [ ] extraction correct   - [ ] grounding correct", "",
        ]
    out_dir = data / "backfill"
    (out_dir / "sample.md").write_text("\n".join(out_md), encoding="utf-8")
    with (out_dir / "sample.jsonl").open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, default=str) + "\n")
    print(json.dumps({
        "sampled": len(picked),
        "confirmed_in_ocr": sum(1 for r in picked if r.confidence == "confirmed_in_ocr"),
        "surname_only": sum(1 for r in picked if r.confidence == "surname_only"),
        "t2_forced": forced,
        "sample_md": str(out_dir / "sample.md"),
    }, indent=1))
    return 0


def cmd_backfill_export_upstream(cfg: Config, args) -> int:
    """Gated handoff: write loader-format officials JSON per (colony, year) for
    a human-run upstream load. Ships confirmed_in_ocr by default; add
    --include-surname-only only if the sample gate cleared that tier.

    NOTE: colony is the graph-normalized name; reconcile it with the upstream
    loader's colony slug before loading. This writes files only — no Neo4j."""
    from .schema import RecoveredRecord

    data = Path(cfg.data_dir)
    out_root = Path(args.out) if args.out else \
        Path.home() / "textasdatacolonialofficelist" / "generated"
    bf = data / "backfill" / "backfill_records.jsonl"
    recs = [RecoveredRecord.model_validate_json(l)
            for l in bf.open(encoding="utf-8") if l.strip()]
    allowed = {"confirmed_in_ocr"}
    if args.include_surname_only:
        allowed.add("surname_only")
    recs = [r for r in recs if r.confidence in allowed]

    groups: dict[tuple, list[dict]] = {}
    for r in recs:
        groups.setdefault((r.colony, r.year), []).append({
            "name": r.name_raw,
            "canonical_name": (f"{r.surname}, {r.given_names}".strip(", ")
                               if r.given_names else r.name_raw),
            "position": r.position_raw,
            "department": r.department_raw,
            "salary_min": None, "salary_max": None,
            "honors": r.honors, "qualifications": [],
            "military_rank": None, "location": r.colony,
            "_confidence": r.confidence, "_backfill": True,
        })
    out_root.mkdir(parents=True, exist_ok=True)
    written = []
    for (colony, year), officials in sorted(groups.items()):
        slug = _norm_text(colony).replace(" ", "_") or "unknown"
        path = out_root / f"{slug}_{year}_data_backfill.json"
        path.write_text(json.dumps(
            {"_provenance": "col_matching extraction backfill (review before load)",
             "officials": officials}, indent=1))
        written.append(str(path))
    print(json.dumps({
        "confidences": sorted(allowed),
        "colony_year_files": len(written),
        "records": len(recs),
        "out_dir": str(out_root),
    }, indent=1))
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="col-services", description=__doc__)
    p.add_argument("--volume", help="one volume (dir name or bare year); default all")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("volumes", "segment", "dedup", "parse_rules", "llm_submit", "llm_poll", "llm_escalate", "check_twins", "eval_gold", "compile", "fetch_graph", "match", "coverage", "attach", "candidates", "eval_known", "dossiers", "pilot_sample", "adjudicate_compile", "calib_build", "calib_score", "gaps", "recover", "recover_loopback", "infer_colony", "augment_officials", "assemble"):
        sp = sub.add_parser(name)
        sp.add_argument("--volume", help="one volume (dir name or bare year); default all")
        sp.add_argument("--limit", type=int, help="cap requests (pilot runs)")
        sp.add_argument("--tag", help="batch job tag (default 'main')")
        sp.add_argument("--calibration", action="store_true",
                        help="use the known-careers calibration set")
        sp.add_argument("--window", type=int, default=None,
                        help="infer_colony: +/- year search window (default 2)")
        sp.add_argument("--raw-ocr", dest="raw_ocr", action="store_true",
                        help="infer_colony: also run Tier B (raw-OCR scan + diagnostic)")
        sp.add_argument("--include-surname-only", dest="include_surname_only",
                        action="store_true",
                        help="augment_officials: also wire surname_only records (gate must clear)")

    # backfill subcommands need their own flags (the shared loop above can't
    # carry --top/--cap/etc.).
    be = sub.add_parser("backfill_extract")
    be.add_argument("--top", type=int, default=20)
    be.add_argument("--model", help="default-tier model slug")
    be.add_argument("--escalate-model", dest="escalate_model",
                    help="escalation-tier model slug")
    be.add_argument("--cap", type=float, help="hard USD spend cap")
    be.add_argument("--resume", action="store_true",
                    help="skip sections already done/failed")
    be.add_argument("--backend", default="openrouter",
                    choices=("openrouter", "ollama"))
    be.add_argument("--workers", type=int, default=6,
                    help="concurrent sections (openrouter); forced to 1 on ollama")
    bes = sub.add_parser("backfill_estimate")
    bes.add_argument("--top", type=int, default=20)
    bes.add_argument("--model", help="default-tier model slug")
    sub.add_parser("backfill_measure")
    bsa = sub.add_parser("backfill_sample")
    bsa.add_argument("--n", type=int, default=40, help="sample size")
    bsa.add_argument("--seed", type=int, default=0)
    bx = sub.add_parser("backfill_export_upstream")
    bx.add_argument("--top", type=int, default=0)
    bx.add_argument("--out", help="output dir (default ~/textasdata.../generated)")
    bx.add_argument("--include-surname-only", dest="include_surname_only",
                    action="store_true",
                    help="also export surname_only records (gate must clear)")

    args = p.parse_args(argv)
    cfg = Config.from_env()
    return globals()[f"cmd_{args.cmd}"](cfg, args)


if __name__ == "__main__":
    sys.exit(main())
