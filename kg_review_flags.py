#!/usr/bin/env python3
"""Second-LLM adjudication of flagged drops — the flag-don't-drop discipline.

`kg_structure_corpus.py validate` emits a clear error packet for every fact the
deterministic validator dropped (data/kg/review/llm_review_queue.jsonl). This
script sends each packet to an INDEPENDENT model (different from the local Qwen
structurer — OpenRouter by default) with the source text + the flagged value +
why it was flagged, and collects a verdict. Then `merge` re-runs validation with
the reviewer-confirmed values folded back in — but ONLY values whose cited source
quote is a real substring of the source (Python gates the quote; the reviewer
proposes, Python still has the last word -> 0-FP preserved).

  python3 kg_review_flags.py run   [--model M] [--workers N] [--base-url URL]
  python3 kg_review_flags.py merge [--raw data/kg/llm_struct_corpus.jsonl]
"""
from __future__ import annotations

import argparse
import json
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

OUT = Path("data/kg")
OR_BASE = "https://openrouter.ai/api/v1"
DEFAULT_MODEL = "deepseek/deepseek-v4-flash"   # independent of the Qwen structurer

REVIEW_SYSTEM = (
    "You adjudicate facts a deterministic validator dropped from a structured "
    "1860s-1960s Colonial Office biography because it could not confirm them in "
    "the printed source. You are given the SOURCE text, the FLAGGED value, its "
    "FIELD, and the REASON it was dropped. Read the source and decide:\n"
    "- keep: the flagged value IS supported by the source (OCR/abbreviation made "
    "the automatic check miss it).\n"
    "- correct: the source supports a DIFFERENT value — give it as corrected_value.\n"
    "- drop: the value is not supported by the source (a real error).\n"
    "Return ONLY JSON: {\"verdict\":\"keep|correct|drop\", \"corrected_value\": "
    "<value or null>, \"source_evidence\": \"<EXACT substring copied from the "
    "source that supports your verdict, or empty for drop>\", \"confidence\": "
    "0.0-1.0, \"rationale\": \"<one line>\"}. source_evidence MUST be copied "
    "verbatim from the source — do not paraphrase or invent it."
)


def _load_env() -> str:
    import os
    if not os.environ.get("OPENROUTER_API_KEY"):
        for cand in (Path(".env"), Path.home() / "col_matching" / ".env"):
            if cand.exists():
                for line in cand.read_text().splitlines():
                    if line.startswith("OPENROUTER_API_KEY="):
                        os.environ["OPENROUTER_API_KEY"] = line.split("=", 1)[1].strip().strip('"')
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise SystemExit("OPENROUTER_API_KEY not found in env or .env")
    return key


def _norm_ws(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip().lower()


def _packet_key(p: dict) -> str:
    return f"{p['person_id']}|{p['field_path']}"


def cmd_run(args) -> None:
    from openai import OpenAI
    from col_match.volume.llm import _extract_json

    queue = [json.loads(l) for l in (OUT / "review" / "llm_review_queue.jsonl").open(encoding="utf-8")]
    out_path = OUT / "review" / "llm_review_verdicts.jsonl"
    done = set()
    if out_path.exists():
        for l in out_path.open(encoding="utf-8"):
            try:
                done.add(_packet_key(json.loads(l)))
            except Exception:
                pass
    todo = [p for p in queue if _packet_key(p) not in done]
    if args.limit:
        todo = todo[: args.limit]
    print(f"queue={len(queue)}  done={len(done)}  todo={len(todo)}  model={args.model}")

    base_url = args.base_url or OR_BASE
    key = "not-needed" if args.base_url else _load_env()
    client = OpenAI(base_url=base_url, api_key=key)
    reasoning_body = ({"chat_template_kwargs": {"enable_thinking": False}}
                      if args.base_url else {"reasoning": {"enabled": False}})

    def work(p: dict) -> dict:
        user = (f"SOURCE:\n{p['source_text']}\n\nFIELD: {p['field_path']}\n"
                f"FLAGGED value: {json.dumps(p['flagged_value'], ensure_ascii=False)}\n"
                f"REASON dropped: {p['reason']}")
        for attempt in range(4):
            try:
                r = client.chat.completions.create(
                    model=args.model, temperature=0.0, max_tokens=600,
                    extra_body=reasoning_body,
                    messages=[{"role": "system", "content": REVIEW_SYSTEM},
                              {"role": "user", "content": user}])
                o = _extract_json(r.choices[0].message.content or "")
                v = o if isinstance(o, dict) else {"verdict": "drop", "_error": "no JSON"}
                return {**{k: p[k] for k in ("person_id", "field_path", "flagged_value", "reason")},
                        "verdict": v.get("verdict", "drop"),
                        "corrected_value": v.get("corrected_value"),
                        "source_evidence": v.get("source_evidence", ""),
                        "confidence": v.get("confidence"), "rationale": v.get("rationale")}
            except Exception as ex:
                if attempt == 3:
                    return {"person_id": p["person_id"], "field_path": p["field_path"],
                            "flagged_value": p["flagged_value"], "reason": p["reason"],
                            "verdict": "drop", "_error": f"{type(ex).__name__}: {ex}"[:120]}
                time.sleep(2 ** attempt * 3)

    lock = threading.Lock()
    counts = {"keep": 0, "correct": 0, "drop": 0}
    t0 = time.time()
    with out_path.open("a", encoding="utf-8") as fh, \
            ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(work, p) for p in todo]
        for i, fut in enumerate(as_completed(futs), 1):
            o = fut.result()
            counts[o.get("verdict", "drop")] = counts.get(o.get("verdict", "drop"), 0) + 1
            with lock:
                fh.write(json.dumps(o, ensure_ascii=False) + "\n"); fh.flush()
            if i % 100 == 0 or i == len(todo):
                print(f"  [{i}/{len(todo)}] {counts}  {i/(time.time()-t0):.2f}/s", flush=True)
    print(f"verdicts: {counts} -> {out_path}")


def _confirmed(verdict: dict, source: str):
    """(value, kind) if this verdict is keep/correct AND its source quote is a
    real substring of the source; else None. kind in {year, place}."""
    if verdict.get("verdict") not in ("keep", "correct"):
        return None
    ev = _norm_ws(verdict.get("source_evidence"))
    if not ev or ev not in _norm_ws(source):
        return None                            # reviewer must cite real source text
    fp = verdict["field_path"]
    val = verdict.get("corrected_value")
    if verdict["verdict"] == "keep":
        val = verdict["flagged_value"]
    if fp.endswith(".place"):
        return (str(val), "place") if val else None
    # year-bearing fields (birth_year, *.year, year_end) and dropped events
    if isinstance(verdict["flagged_value"], dict):       # whole event dropped
        val = val if isinstance(val, int) else verdict["flagged_value"].get("year_start")
    try:
        return (int(val), "year")
    except (TypeError, ValueError):
        return None


def cmd_merge(args) -> None:
    """Re-run postnorm+validate with reviewer-confirmed (quote-verified) values
    folded back in -> data/kg/llm_struct_corpus.reviewed.jsonl."""
    import glob
    from col_match.kg.validate import validate_struct
    from col_match.kg.postnorm import normalize_struct

    verdicts = [json.loads(l) for l in (OUT / "review" / "llm_review_verdicts.jsonl").open(encoding="utf-8")]
    pid2bid = {p["person_id"]: p["canonical_bio_id"]
               for p in (json.loads(l) for l in Path(args.persons).open(encoding="utf-8"))}
    bio = {}
    for f in glob.glob("data/kg/bios/*.jsonl"):
        for l in open(f, encoding="utf-8"):
            b = json.loads(l); bio[b["bio_id"]] = b.get("raw_text", "")

    extra_years: dict = {}
    extra_places: dict = {}
    restored = 0
    for v in verdicts:
        src = bio.get(pid2bid.get(v["person_id"], ""), "")
        c = _confirmed(v, src)
        if not c:
            continue
        val, kind = c
        (extra_years if kind == "year" else extra_places).setdefault(v["person_id"], set()).add(val)
        restored += 1

    raw = [json.loads(l) for l in Path(args.raw).open(encoding="utf-8")]
    out_path = OUT / "llm_struct_corpus.reviewed.jsonl"
    n = 0
    with out_path.open("w", encoding="utf-8") as fh:
        for o in raw:
            if "_error" in o:
                continue
            pid = o["person_id"]
            src = bio.get(pid2bid.get(pid, ""), "")
            o2, norm = normalize_struct(o)
            v = validate_struct(o2, src, extra_years=extra_years.get(pid),
                                 extra_places=extra_places.get(pid))
            v.pop("_review", None)
            if norm:
                v["_norm"] = norm
            fh.write(json.dumps(v, ensure_ascii=False) + "\n")
            n += 1
    print(f"merged {restored} reviewer-confirmed values into {n} structs -> {out_path}")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="adjudicate flagged drops with an independent model")
    r.add_argument("--model", default=DEFAULT_MODEL)
    r.add_argument("--base-url", default="", dest="base_url",
                   help="OpenAI-compatible endpoint; default OpenRouter")
    r.add_argument("--workers", type=int, default=8)
    r.add_argument("--limit", type=int, default=0)
    m = sub.add_parser("merge", help="fold quote-verified verdicts back into valid output")
    m.add_argument("--raw", default=str(OUT / "llm_struct_corpus.jsonl"))
    m.add_argument("--persons", default=str(OUT / "persons.deduped2.recovered.jsonl"))
    args = ap.parse_args()
    {"run": cmd_run, "merge": cmd_merge}[args.cmd](args)


if __name__ == "__main__":
    main()
