#!/usr/bin/env python3
"""Benchmark a free OpenRouter model against the in-session Opus reference set.

The reference set is data/kg/struct_valid.jsonl (Opus-structured + validated).
This script runs the SAME bios through a chosen OpenRouter model on the SAME
code path Qwen uses (col_match.kg.extract.parse_via_client + KG_BIO_SYSTEM),
then validates the model output with the SAME validator (col_match.kg.validate)
and scores agreement with the reference.

Usage:
  python3 kg_bench_openrouter.py run     [--model M] [--limit N]
  python3 kg_bench_openrouter.py compare [--model M] [--examples K]

The model output is cached per person_id (resumable). OpenRouter is OpenAI-
compatible, so we reuse QwenClient pointed at https://openrouter.ai/api/v1.
"""
from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path

OUT = Path("data/kg")
DEFAULT_MODEL = "cohere/north-mini-code:free"
OR_BASE = "https://openrouter.ai/api/v1"

# Appended to KG_BIO_SYSTEM when --prompt strict. Nails the output contract the
# free models drift from (name/person/decoration keys, top-level event fields).
STRICT_SUFFIX = (
    "\n\nOUTPUT CONTRACT — follow EXACTLY:\n"
    "Return ONE JSON object and nothing else (no prose, no markdown). Use EXACTLY "
    "these top-level keys, all of them, and NO others: surname, given_names, "
    "birth_year, education, honours, events, terminal.\n"
    "- surname (string, required): the family name from the ALL-CAPS headword. "
    "given_names (string|null): the remaining personal names. NEVER use a 'name' "
    "or 'person' key — split the headword into surname + given_names.\n"
    "- honours: array of objects each with keys 'award' (string) and 'year' "
    "(int|null). The decoration string goes in 'award'; NEVER use a 'decoration' "
    "key.\n"
    "- events: array of objects, each with EXACTLY: position, place, year_start, "
    "year_end, place_inherited, is_acting, org_type. position/place/year_* belong "
    "ONLY inside event objects, NEVER at the top level. year_end is null for a "
    "single-year posting (do NOT copy year_start into year_end).\n"
    "- Do NOT add notes, commentary, 'name', 'person', or 'decoration' keys."
)

# A lighter touch than STRICT_SUFFIX: one sentence, to avoid distracting the
# model from the event-extraction task (the heavy contract regressed Qwen).
KEYS_SUFFIX = (
    "\n\nReturn ONE JSON object with EXACTLY these top-level keys: surname, "
    "given_names, birth_year, education, honours, events, terminal. Split the "
    "headword into surname + given_names (no 'name'/'person' key). Each honour is "
    "{\"award\": str, \"year\": int|null} (no 'decoration'/'order' key)."
)


def _load_env() -> str:
    import os
    if not os.environ.get("OPENROUTER_API_KEY"):
        for line in Path(".env").read_text().splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                os.environ["OPENROUTER_API_KEY"] = line.split("=", 1)[1].strip().strip('"')
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise SystemExit("OPENROUTER_API_KEY not found in env or .env")
    return key


def _safe(model: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", model.lower()).strip("_")


def _ref() -> dict[str, dict]:
    return {json.loads(l)["person_id"]: json.loads(l)
            for l in (OUT / "struct_valid.jsonl").open(encoding="utf-8")}


def _source_texts(pids: set[str]) -> dict[str, str]:
    """person_id -> canonical raw_text (the text the reference was built from)."""
    pid2canon = {}
    for l in (OUT / "persons.jsonl").open(encoding="utf-8"):
        p = json.loads(l)
        if p["person_id"] in pids:
            pid2canon[p["person_id"]] = p["canonical_bio_id"]
    want = set(pid2canon.values())
    bio = {}
    for f in (OUT / "bios").glob("*.jsonl"):
        for l in f.open(encoding="utf-8"):
            b = json.loads(l)
            if b["bio_id"] in want:
                bio[b["bio_id"]] = b["raw_text"]
    return {pid: bio[c] for pid, c in pid2canon.items() if c in bio}


# ---- run -----------------------------------------------------------------

def _cache_path(model: str, tag: str) -> Path:
    name = _safe(model) + (f"__{tag}" if tag else "")
    return OUT / "struct_model" / f"{name}.jsonl"


def cmd_run(args) -> None:
    # A local/self-hosted OpenAI-compatible endpoint needs no OpenRouter key.
    base_url = args.base_url or OR_BASE
    key = "not-needed" if args.base_url else _load_env()
    from openai import OpenAI
    from col_match.kg.extract import KG_BIO_SYSTEM, KG_BIO_SCHEMA
    from col_match.kg.normalize import normalize_for_llm
    from col_match.volume.llm import _extract_json

    ref = _ref()
    pids = sorted(ref)  # deterministic order
    src = _source_texts(set(pids))

    (OUT / "struct_model").mkdir(parents=True, exist_ok=True)
    cache = _cache_path(args.model, args.tag)
    done = set()
    if cache.exists():
        for l in cache.open(encoding="utf-8"):
            try:
                done.add(json.loads(l)["person_id"])
            except Exception:
                pass

    todo = [p for p in pids if p in src and p not in done][: args.limit]
    system = KG_BIO_SYSTEM + {"strict": STRICT_SUFFIX, "keys": KEYS_SUFFIX}.get(args.prompt, "")
    mode = ("structured(json_schema)" if args.structured else "prompt-only") + f"/{args.prompt}"
    print(f"model={args.model}  mode={mode}  reference={len(pids)}  cached={len(done)}  running={len(todo)}")

    client = OpenAI(base_url=base_url, api_key=key)
    if args.base_url:
        print(f"endpoint={base_url}")
    # strict json_schema forces the schema fields the prompt-only run ignored
    # (surname/given_names + honours[].award), removing the 'name'/'decoration' drift.
    resp_fmt = ({"type": "json_schema", "json_schema":
                 {"name": "kg_bio", "strict": True, "schema": KG_BIO_SCHEMA}}
                if args.structured else None)

    # reasoning OFF by default: a reasoning model otherwise burns the whole token
    # budget thinking and returns no JSON. OpenRouter uses the `reasoning` knob;
    # a local vLLM (Qwen3) ignores that and needs chat_template_kwargs.enable_thinking.
    reasoning_body = ({"chat_template_kwargs": {"enable_thinking": bool(args.reason)}}
                      if args.base_url else {"reasoning": {"enabled": bool(args.reason)}})

    def parse_one(text: str):
        kw = dict(model=args.model, temperature=0.0, max_tokens=args.max_tokens,
                  extra_body=reasoning_body,
                  messages=[{"role": "system", "content": KG_BIO_SYSTEM},
                            {"role": "user", "content": normalize_for_llm(text)}])
        kw["messages"][0]["content"] = system
        if resp_fmt:
            kw["response_format"] = resp_fmt
        r = client.chat.completions.create(**kw)
        out = _extract_json(r.choices[0].message.content or "")
        return out if isinstance(out, dict) else None

    ok = bad = 0
    times = []
    wall0 = time.time()
    with cache.open("a", encoding="utf-8") as fh:
        for i, pid in enumerate(todo, 1):
            obj, err, t0 = None, None, time.time()
            for attempt in range(4):
                try:
                    obj = parse_one(src[pid])
                    break
                except Exception as e:  # rate limit / transient
                    err = f"{type(e).__name__}: {e}"
                    time.sleep(2 ** attempt * 3)
            dt = time.time() - t0
            times.append(dt)
            if isinstance(obj, dict):
                obj["person_id"] = pid
                fh.write(json.dumps(obj, ensure_ascii=False) + "\n")
                fh.flush()
                ok += 1
                tag = f"{len(obj.get('events') or [])}ev"
            else:
                fh.write(json.dumps({"person_id": pid, "_error": err or "no JSON"}) + "\n")
                fh.flush()
                bad += 1
                tag = f"FAIL {err or 'no JSON'}"[:60]
            print(f"  [{i}/{len(todo)}] {pid} {dt:4.1f}s  {tag}")
    print(f"done: {ok} parsed, {bad} failed -> {cache}")
    if times:
        wall = time.time() - wall0
        times_s = sorted(times)
        med = times_s[len(times_s) // 2]
        # full-corpus projection assumes the same per-bio latency, sequential.
        proj_h = 34743 * (wall / len(times)) / 3600
        print(f"SPEED: {len(times)} bios in {wall:.1f}s wall  "
              f"(mean {sum(times)/len(times):.1f}s, median {med:.1f}s, "
              f"min {times_s[0]:.1f}s, max {times_s[-1]:.1f}s per bio)")
        print(f"SPEED: ~{wall/len(times):.1f}s/bio sequential -> "
              f"full 34,743-bio run ≈ {proj_h:.1f} h sequential "
              f"(÷ concurrency for parallel)")


# ---- review (two-model propose->verify) ----------------------------------

# The verifier sees the source bio AND the proposer's candidate JSON. Its job is
# narrow correction, NOT re-extraction: the asymmetry only pays off if checking a
# concrete candidate is easier than generating from scratch. We name the failure
# modes we want it to catch and forbid free invention to limit false corrections.
REVIEW_SUFFIX = (
    "\n\nYou are REVIEWING a structured extraction made by another model. You are "
    "given the SOURCE BIO and a CANDIDATE JSON. CORRECT the candidate; do NOT "
    "re-extract from scratch and do NOT rewrite parts that are already right.\n"
    "Fix ONLY these problems, and only when the SOURCE BIO supports the fix:\n"
    "1. MISSED event — a posting/appointment in the prose but absent from events[]. Add it.\n"
    "2. SPURIOUS event — an event with no support in the prose. Remove it.\n"
    "3. Wrong place->position binding — a place attached to the wrong posting. Rebind it.\n"
    "4. Wrong year_start/year_end vs the prose. Fix it.\n"
    "5. Missed/wrong honours, birth_year, surname, or given_names.\n"
    "Do NOT invent facts absent from the prose. If the candidate is already "
    "correct, return it unchanged. Return ONE complete JSON object with EXACTLY "
    "these top-level keys: surname, given_names, birth_year, education, honours, "
    "events, terminal — and nothing else."
)


def cmd_review(args) -> None:
    """Run a verifier model over a proposer's cached output (two-model loop)."""
    key = _load_env()
    from openai import OpenAI
    from col_match.kg.extract import KG_BIO_SYSTEM
    from col_match.kg.normalize import normalize_for_llm
    from col_match.volume.llm import _extract_json

    in_cache = _cache_path(args.model, args.tag)
    if not in_cache.exists():
        raise SystemExit(f"no proposer output at {in_cache}; run `run` first")
    proposed = {}
    for l in in_cache.open(encoding="utf-8"):
        o = json.loads(l)
        if "_error" not in o:
            proposed[o["person_id"]] = o
    src = _source_texts(set(proposed))

    out_tag = args.out_tag or f"rev_of_{_safe(args.model)}{('_' + args.tag) if args.tag else ''}"
    out_cache = _cache_path(args.review_model, out_tag)
    (OUT / "struct_model").mkdir(parents=True, exist_ok=True)
    done = set()
    if out_cache.exists():
        for l in out_cache.open(encoding="utf-8"):
            try:
                done.add(json.loads(l)["person_id"])
            except Exception:
                pass

    pids = [p for p in sorted(proposed) if p in src and p not in done][: args.limit]
    system = KG_BIO_SYSTEM + REVIEW_SUFFIX
    print(f"proposer={args.model}/{args.tag or '-'}  verifier={args.review_model}  "
          f"candidates={len(proposed)}  cached={len(done)}  reviewing={len(pids)}  -> {out_cache}")

    client = OpenAI(base_url=OR_BASE, api_key=key)

    def review_one(text: str, candidate: dict):
        cand = {k: candidate.get(k) for k in
                ("surname", "given_names", "birth_year", "education", "honours", "events", "terminal")}
        user = (f"SOURCE BIO:\n{normalize_for_llm(text)}\n\n"
                f"CANDIDATE JSON:\n{json.dumps(cand, ensure_ascii=False)}")
        r = client.chat.completions.create(
            model=args.review_model, temperature=0.0, max_tokens=args.max_tokens,
            extra_body={"reasoning": {"enabled": bool(args.reason)}},
            messages=[{"role": "system", "content": system},
                      {"role": "user", "content": user}])
        out = _extract_json(r.choices[0].message.content or "")
        return out if isinstance(out, dict) else None

    ok = bad = 0
    with out_cache.open("a", encoding="utf-8") as fh:
        for i, pid in enumerate(pids, 1):
            obj, err, t0 = None, None, time.time()
            for attempt in range(4):
                try:
                    obj = review_one(src[pid], proposed[pid])
                    break
                except Exception as e:
                    err = f"{type(e).__name__}: {e}"
                    time.sleep(2 ** attempt * 3)
            dt = time.time() - t0
            if isinstance(obj, dict):
                obj["person_id"] = pid
                fh.write(json.dumps(obj, ensure_ascii=False) + "\n"); fh.flush()
                ok += 1
                n0, n1 = len(proposed[pid].get("events") or []), len(obj.get("events") or [])
                tag = f"{n0}->{n1}ev" + (" *" if n0 != n1 else "")
            else:
                fh.write(json.dumps({"person_id": pid, "_error": err or "no JSON"}) + "\n"); fh.flush()
                bad += 1
                tag = f"FAIL {err or 'no JSON'}"[:60]
            print(f"  [{i}/{len(pids)}] {pid} {dt:4.1f}s  {tag}")
    print(f"done: {ok} reviewed, {bad} failed -> {out_cache}")
    print(f"score it with:  python3 kg_bench_openrouter.py compare --model {args.review_model} --tag {out_tag}")


# ---- compare -------------------------------------------------------------

def _norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def _toks(s):
    return set(_norm(s).split())


def _ev_score(r, m):
    s = 0.0
    rys, mys = r.get("year_start"), m.get("year_start")
    if rys is not None and rys == mys:
        s += 3
    elif rys is None and mys is None:
        s += 1
    rp, mp = _norm(r.get("place")), _norm(m.get("place"))
    if rp and rp == mp:
        s += 3
    elif not rp and not mp:
        s += 1
    rt, mt = _toks(r.get("position")), _toks(m.get("position"))
    if rt or mt:
        s += 2 * len(rt & mt) / max(1, len(rt | mt))
    return s


def _align(refs, mods):
    pairs = sorted(((i, j, _ev_score(r, m))
                    for i, r in enumerate(refs) for j, m in enumerate(mods)),
                   key=lambda x: -x[2])
    ur, um, matched = set(range(len(refs))), set(range(len(mods))), []
    for i, j, sc in pairs:
        if sc >= 3 and i in ur and j in um:
            matched.append((i, j, sc))
            ur.discard(i); um.discard(j)
    return matched


def cmd_compare(args) -> None:
    from col_match.kg.validate import validate_struct
    ref = _ref()
    cache = _cache_path(args.model, args.tag)
    if not cache.exists():
        raise SystemExit(f"no model output at {cache}; run `run` first")
    raw = {}
    fails = []
    for l in cache.open(encoding="utf-8"):
        o = json.loads(l)
        if "_error" in o:
            fails.append(o["person_id"])
        else:
            raw[o["person_id"]] = o
    src = _source_texts(set(raw) | set(fails))

    def _coerce(o):
        """Normalize free-model schema drift into the canonical shape so the
        shared validator and the metrics never choke (bare-string honours,
        'decoration' key, missing event fields)."""
        def yr(v):
            try:
                return int(str(v)[:4]) if v not in (None, "") else None
            except (ValueError, TypeError):
                return None
        # recover surname/given_names if the model used a 'name'/'person' field
        sur, giv = o.get("surname"), o.get("given_names")
        if not sur:
            nm = o.get("name") or o.get("person") or ""
            if "," in nm:
                sur, _, giv = nm.partition(",")
                sur, giv = sur.strip(), (giv.strip() or None)
            elif nm:
                parts = nm.split()
                sur, giv = parts[-1], (" ".join(parts[:-1]) or None)
        hon = []
        for h in o.get("honours") or []:
            if isinstance(h, str):
                hon.append({"award": h, "year": None})
            elif isinstance(h, dict):
                hon.append({"award": h.get("award") or h.get("decoration") or h.get("order"),
                            "year": yr(h.get("year") or h.get("award_year"))})
        evs = []
        for e in o.get("events") or []:
            if isinstance(e, dict):
                evs.append({"position": e.get("position"), "place": e.get("place"),
                            "year_start": yr(e.get("year_start")), "year_end": yr(e.get("year_end")),
                            "place_inherited": bool(e.get("place_inherited")),
                            "is_acting": bool(e.get("is_acting")),
                            "org_type": e.get("org_type") or "civil"})
        return {**o, "surname": sur, "given_names": giv, "honours": hon, "events": evs}

    # validate model output exactly as the reference was validated
    mod = {pid: validate_struct(_coerce(o), src[pid]) for pid, o in raw.items() if pid in src}

    pids = sorted(p for p in ref if p in mod)
    if args.limit:
        pids = pids[: args.limit]
    n = len(pids)
    if not n:
        raise SystemExit("no overlapping person_ids between reference and model")

    # aggregate counters
    agg = dict(birth_ok=0, birth_tot=0, surname_ok=0,
               hon_tp=0, hon_fp=0, hon_fn=0,
               ev_ref=0, ev_mod=0, ev_match=0,
               place_ok=0, place_tot=0, yr_ok=0, yr_tot=0,
               act_ok=0, org_ok=0,
               mod_facts=0, mod_drops=0, term_ok=0)
    per_person = []
    for pid in pids:
        r, m = ref[pid], mod[pid]
        # scalars
        agg["surname_ok"] += _norm(r.get("surname")) == _norm(m.get("surname"))
        if r.get("birth_year") is not None:
            agg["birth_tot"] += 1
            agg["birth_ok"] += r["birth_year"] == m.get("birth_year")
        # honours (by normalized award; tolerate the model's 'decoration' key)
        ra = {_norm(h.get("award")) for h in r.get("honours") or []} - {""}
        ma = {_norm(h.get("award") or h.get("decoration")) for h in m.get("honours") or []} - {""}
        agg["hon_tp"] += len(ra & ma); agg["hon_fp"] += len(ma - ra); agg["hon_fn"] += len(ra - ma)
        # terminal presence+kind
        rt, mt = r.get("terminal"), m.get("terminal")
        agg["term_ok"] += (bool(rt) == bool(mt)) and (not rt or _norm(rt.get("kind")) == _norm((mt or {}).get("kind")))
        # events
        re_, me_ = r.get("events") or [], m.get("events") or []
        agg["ev_ref"] += len(re_); agg["ev_mod"] += len(me_)
        matched = _align(re_, me_)
        agg["ev_match"] += len(matched)
        for i, j, sc in matched:
            a, b = re_[i], me_[j]
            agg["place_tot"] += 1; agg["place_ok"] += _norm(a.get("place")) == _norm(b.get("place"))
            agg["yr_tot"] += 1; agg["yr_ok"] += a.get("year_start") == b.get("year_start")
            agg["act_ok"] += bool(a.get("is_acting")) == bool(b.get("is_acting"))
            agg["org_ok"] += a.get("org_type") == b.get("org_type")
        # model hallucination (validator drops on model output)
        agg["mod_drops"] += len(m.get("flags") or [])
        agg["mod_facts"] += len(raw[pid].get("events") or []) + len(raw[pid].get("honours") or [])
        per_person.append((pid, len(re_), len(me_), len(matched)))

    def pct(a, b):
        return f"{100*a/b:5.1f}%" if b else "  n/a"

    ev_p = agg["ev_match"] / agg["ev_mod"] if agg["ev_mod"] else 0
    ev_r = agg["ev_match"] / agg["ev_ref"] if agg["ev_ref"] else 0
    hon_p = agg["hon_tp"] / (agg["hon_tp"] + agg["hon_fp"]) if (agg["hon_tp"] + agg["hon_fp"]) else 0
    hon_r = agg["hon_tp"] / (agg["hon_tp"] + agg["hon_fn"]) if (agg["hon_tp"] + agg["hon_fn"]) else 0

    print(f"\n=== {args.model}  vs Opus reference ===")
    print(f"persons compared       : {n}   (model JSON failures: {len(fails)})")
    print(f"surname exact          : {pct(agg['surname_ok'], n)}")
    print(f"birth_year exact       : {pct(agg['birth_ok'], agg['birth_tot'])}  (of {agg['birth_tot']} with a ref birth_year)")
    print(f"terminal kind match    : {pct(agg['term_ok'], n)}")
    print(f"honours  precision/recall: {hon_p*100:4.1f}% / {hon_r*100:4.1f}%   (tp={agg['hon_tp']} fp={agg['hon_fp']} fn={agg['hon_fn']})")
    print(f"events   ref={agg['ev_ref']}  model={agg['ev_mod']}  matched={agg['ev_match']}")
    print(f"events   precision/recall: {ev_p*100:4.1f}% / {ev_r*100:4.1f}%")
    print(f"  matched-event place agree : {pct(agg['place_ok'], agg['place_tot'])}")
    print(f"  matched-event year  agree : {pct(agg['yr_ok'], agg['yr_tot'])}")
    print(f"  matched-event acting agree: {pct(agg['act_ok'], agg['place_tot'])}")
    print(f"  matched-event org   agree : {pct(agg['org_ok'], agg['place_tot'])}")
    print(f"model hallucination    : {agg['mod_drops']} facts dropped by validator over {agg['mod_facts']} emitted  ({pct(agg['mod_drops'], agg['mod_facts'])})")

    # worst-divergence persons (by |ref-model event count| + unmatched)
    per_person.sort(key=lambda x: -(abs(x[1] - x[2]) + (x[1] - x[3])))
    print("\nlargest event-count divergence (pid: ref/model/matched):")
    for pid, nr, nm, mm in per_person[:8]:
        print(f"  {pid:28s} {nr:2d}/{nm:2d}/{mm:2d}")

    # side-by-side examples
    if args.examples:
        print(f"\n=== {args.examples} side-by-side examples ===")
        for pid, nr, nm, mm in per_person[: args.examples]:
            print(f"\n--- {pid}  (ref {nr} ev / model {nm} ev / {mm} matched) ---")
            print("REF  :", json.dumps({k: ref[pid][k] for k in ("surname", "birth_year", "events")}, ensure_ascii=False)[:900])
            print("MODEL:", json.dumps({k: mod[pid].get(k) for k in ("surname", "birth_year", "events")}, ensure_ascii=False)[:900])


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run"); r.add_argument("--model", default=DEFAULT_MODEL); r.add_argument("--limit", type=int, default=25)
    r.add_argument("--structured", action="store_true", help="enforce KG_BIO_SCHEMA via response_format json_schema")
    r.add_argument("--prompt", choices=["default", "keys", "strict"], default="default", help="system-prompt variant")
    r.add_argument("--reason", action="store_true", help="enable model reasoning (default off)")
    r.add_argument("--max-tokens", type=int, default=8000, dest="max_tokens")
    r.add_argument("--base-url", default="", dest="base_url",
                   help="OpenAI-compatible endpoint (e.g. local Qwen box); no API key needed")
    r.add_argument("--tag", default="", help="cache-file suffix to keep configs separate")
    v = sub.add_parser("review", help="two-model: verifier corrects a proposer's cached output")
    v.add_argument("--model", default=DEFAULT_MODEL, help="proposer model (locates input cache)")
    v.add_argument("--tag", default="", help="proposer cache tag")
    v.add_argument("--review-model", required=True, dest="review_model", help="verifier model")
    v.add_argument("--out-tag", default="", dest="out_tag", help="output cache tag (default rev_of_<proposer>)")
    v.add_argument("--limit", type=int, default=1000)
    v.add_argument("--reason", action="store_true")
    v.add_argument("--max-tokens", type=int, default=8000, dest="max_tokens")
    c = sub.add_parser("compare"); c.add_argument("--model", default=DEFAULT_MODEL); c.add_argument("--examples", type=int, default=4)
    c.add_argument("--tag", default=""); c.add_argument("--limit", type=int, default=0, help="score only first N sorted persons")
    args = ap.parse_args()
    {"run": cmd_run, "review": cmd_review, "compare": cmd_compare}[args.cmd](args)


if __name__ == "__main__":
    main()
