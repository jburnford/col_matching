#!/usr/bin/env python3
"""Production runner: structure the full deduped person corpus into KG JSON.

Reads persons.deduped2.jsonl (~34,743), maps each person to its canonical bio
raw_text, and structures it via an OpenAI-compatible endpoint (the local
Qwen3.6 vLLM box) using the SAME path the bench winner used: KG_BIO_SYSTEM +
the keys contract, reasoning/thinking OFF, temp 0. Writes one raw llm_struct
JSON line per person (keyed by person_id). Concurrent + resumable. The output
feeds validation (validate_struct against source text) downstream.

Designed to run ON the GPU box (tunnel-free, base_url=http://localhost:8003/v1)
unattended over a weekend.

Usage:
  python3 kg_structure_corpus.py --base-url http://localhost:8003/v1 \
    --model qwen3.6-35b-a3b --workers 8 --out data/kg/llm_struct_corpus.jsonl

  # validate the result against source text (cheap, no LLM):
  python3 kg_structure_corpus.py validate --in data/kg/llm_struct_corpus.jsonl
"""
from __future__ import annotations

import argparse
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

OUT = Path("data/kg")

# Reuse the locked output contract the bake-off settled on (keys prompt). Import
# is safe: kg_bench_openrouter only runs argparse under its __main__ guard.
from kg_bench_openrouter import KEYS_SUFFIX


def _load_persons(path: str) -> list[tuple[str, str]]:
    """(person_id, canonical_bio_id) for every deduped person."""
    out = []
    for l in Path(path).open(encoding="utf-8"):
        p = json.loads(l)
        out.append((p["person_id"], p["canonical_bio_id"]))
    return out


def _bio_index(want: set[str]) -> dict[str, str]:
    """bio_id -> raw_text, loaded once from data/kg/bios/*.jsonl."""
    idx = {}
    for f in sorted((OUT / "bios").glob("*.jsonl")):
        for l in f.open(encoding="utf-8"):
            b = json.loads(l)
            if b["bio_id"] in want:
                idx[b["bio_id"]] = b["raw_text"]
    return idx


def cmd_run(args) -> None:
    from openai import OpenAI
    from col_match.kg.extract import KG_BIO_SYSTEM
    from col_match.kg.normalize import normalize_for_llm
    from col_match.volume.llm import _extract_json

    persons = _load_persons(args.persons)
    out_path = Path(args.out)
    done = set()
    if out_path.exists():
        for l in out_path.open(encoding="utf-8"):
            try:
                done.add(json.loads(l)["person_id"])
            except Exception:
                pass

    todo = [(pid, bid) for pid, bid in persons if pid not in done]
    if args.limit:
        todo = todo[: args.limit]
    bio = _bio_index({bid for _, bid in todo})
    missing = [pid for pid, bid in todo if bid not in bio]
    todo = [(pid, bid) for pid, bid in todo if bid in bio]
    print(f"persons={len(persons)}  done={len(done)}  todo={len(todo)}  "
          f"(no-bio skipped={len(missing)})  workers={args.workers}  -> {out_path}")

    system = KG_BIO_SYSTEM + KEYS_SUFFIX
    # local vLLM (Qwen3) ignores the OpenRouter `reasoning` knob; thinking is
    # disabled via chat_template_kwargs.enable_thinking (off => fast + clean JSON).
    reasoning_body = {"chat_template_kwargs": {"enable_thinking": bool(args.reason)}}
    client = OpenAI(base_url=args.base_url, api_key="not-needed")

    def work(pid: str, bid: str) -> dict:
        for attempt in range(4):
            try:
                r = client.chat.completions.create(
                    model=args.model, temperature=0.0, max_tokens=args.max_tokens,
                    extra_body=reasoning_body,
                    messages=[{"role": "system", "content": system},
                              {"role": "user", "content": normalize_for_llm(bio[bid])}])
                out = _extract_json(r.choices[0].message.content or "")
                if isinstance(out, dict):
                    out["person_id"] = pid
                    return out
                return {"person_id": pid, "_error": "no JSON"}
            except Exception as e:
                if attempt == 3:
                    return {"person_id": pid, "_error": f"{type(e).__name__}: {e}"[:120]}
                time.sleep(2 ** attempt * 3)

    lock = threading.Lock()
    ok = bad = 0
    t0 = time.time()
    with out_path.open("a", encoding="utf-8") as fh, \
            ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(work, pid, bid) for pid, bid in todo]
        for i, fut in enumerate(as_completed(futs), 1):
            o = fut.result()
            with lock:
                fh.write(json.dumps(o, ensure_ascii=False) + "\n")
                fh.flush()
            if "_error" in o:
                bad += 1
            else:
                ok += 1
            if i % 100 == 0 or i == len(todo):
                el = time.time() - t0
                rate = i / el if el else 0
                eta = (len(todo) - i) / rate / 3600 if rate else 0
                print(f"  [{i}/{len(todo)}] ok={ok} bad={bad}  "
                      f"{rate:.2f} bio/s  ETA {eta:.1f}h", flush=True)
    el = time.time() - t0
    print(f"done: {ok} ok, {bad} bad in {el/3600:.2f}h "
          f"({len(todo)/el:.2f} bio/s) -> {out_path}")
    print("next:  python3 kg_structure_corpus.py validate --in " + str(out_path))


def cmd_validate(args) -> None:
    """Normalize + validate raw structs against source text -> *.valid.jsonl.

    Two deterministic passes, no LLM: postnorm (fix the systematic structuring
    errors catalogued in docs/STRUCT_ERROR_CATALOG.md — ditto/inheritance,
    Knight-Bachelor splits, honorific/rank in names, temp.-as-acting) THEN
    validate (drop facts not supported by source). Changes from each pass are
    recorded on the row (``_norm`` / ``flags``) so nothing is silent."""
    from col_match.kg.validate import validate_struct
    from col_match.kg.postnorm import normalize_struct

    in_path = Path(args.in_path)
    raw = [json.loads(l) for l in in_path.open(encoding="utf-8")]
    good = [o for o in raw if "_error" not in o]
    fails = [o for o in raw if "_error" in o]
    pid2bid = {p: b for p, b in _load_persons(args.persons)}
    bio = _bio_index({pid2bid[o["person_id"]] for o in good if o["person_id"] in pid2bid})

    out_path = in_path.with_suffix(".valid.jsonl")
    n_flags = n_norm = n_normed = 0
    with out_path.open("w", encoding="utf-8") as fh:
        for o in good:
            bid = pid2bid.get(o["person_id"])
            src = bio.get(bid, "")
            o, norm_changes = normalize_struct(o)
            if norm_changes:
                n_norm += len(norm_changes)
                n_normed += 1
            v = validate_struct(o, src)
            if norm_changes:
                v["_norm"] = norm_changes
            n_flags += len(v.get("flags") or [])
            fh.write(json.dumps(v, ensure_ascii=False) + "\n")
    print(f"validated {len(good)} structs ({len(fails)} llm-failures); "
          f"postnorm fixed {n_norm} items on {n_normed} structs; "
          f"{n_flags} facts dropped/flagged -> {out_path}")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("run", help="structure the corpus (default)")
    r.add_argument("--persons", default=str(OUT / "persons.deduped2.jsonl"))
    r.add_argument("--out", default=str(OUT / "llm_struct_corpus.jsonl"))
    r.add_argument("--base-url", required=True, dest="base_url")
    r.add_argument("--model", default="qwen3.6-35b-a3b")
    r.add_argument("--workers", type=int, default=8)
    r.add_argument("--max-tokens", type=int, default=4000, dest="max_tokens")
    r.add_argument("--limit", type=int, default=0)
    r.add_argument("--reason", action="store_true", help="enable thinking (default off)")
    v = sub.add_parser("validate", help="validate raw structs vs source text")
    v.add_argument("--in", dest="in_path", default=str(OUT / "llm_struct_corpus.jsonl"))
    v.add_argument("--persons", default=str(OUT / "persons.deduped2.jsonl"))
    args = ap.parse_args()
    if args.cmd == "validate":
        cmd_validate(args)
    else:  # default to run
        cmd_run(args)


if __name__ == "__main__":
    main()
