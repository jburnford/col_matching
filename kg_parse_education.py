#!/usr/bin/env python3
"""LLM-parse the free-text `education` clause into structured institution
mentions (quality path; replaces the brittle regex extractor for the IOL).

The Qwen bio-structuring run kept `education` as an as-printed prose clause
("at the City of London school and Balliol college, Oxford (Arnold prize,
1894)"). The regex extractor in kg_education_worklist.py only reaches ~56% of
non-empty rows and is brittle on the irregular tail (University College London,
Christ's Hospital, "Universities of Glasgow and Edinburgh", colleges written
without a keyword, foreign/Indian institutions). This runner asks the same
local Qwen3.6 endpoint to extract the institutions cleanly, binding ambiguous
colleges to their parent university and dropping bare degrees/qualifications.

Two stages, both resumable, both rooted on COL_KG_OUT:

  # 1) parse the DISTINCT education strings (small: ~6.8k for the IOL)
  COL_KG_OUT=data/iol python3 kg_parse_education.py run \
      --base-url http://127.0.0.1:8004/v1 --model qwen3.6-35b-a3b --workers 16

  # 2) fan parsed institutions back to person_ids -> the grounding worklist
  COL_KG_OUT=data/iol python3 kg_parse_education.py worklist

Stage 2 writes KG_OUT/education_worklist.jsonl in the schema
kg_ground_institutions.py already consumes (institution/type/count/person_ids/
examples), so the Wikidata grounding loop is unchanged.
"""
from __future__ import annotations

import argparse
import json
import threading
import time
from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from col_match.kg.paths import kg_out

# Institution types the grounding/emit layer understands.
SYSTEM = """You extract EDUCATIONAL INSTITUTIONS from a short biographical \
"education" clause taken from a British/Indian colonial service list \
(1860s-1940s). Return STRICT JSON only.

Output schema:
{"institutions": [{"name": "<canonical institution name>", "type": "<type>"}]}

type is one of: school, university, university_college, military_academy, \
naval_college, inn_of_court, professional, other

Rules:
- Extract ONLY institutions actually named in the text. Never invent or infer \
an institution that is not written.
- A college that belongs to a collegiate university must be bound to its \
parent: "Balliol college, Oxford" -> "Balliol College, Oxford" \
(type university_college). If a bare college name is followed by ", Oxford" / \
", Cambridge" / ", Dublin" etc., attach that parent.
- "University College, London" / "King's College, London" / "University \
College School" are SINGLE named institutions - keep them whole, do NOT split \
into a college + a parent university.
- "Universities of Glasgow and Edinburgh" -> two entries: "University of \
Glasgow" and "University of Edinburgh" (type university). Same for any list.
- Famous schools written without the word school/college are still schools: \
Eton -> "Eton College", Harrow -> "Harrow School", Winchester -> "Winchester \
College", Charterhouse -> "Charterhouse", Christ's Hospital -> "Christ's \
Hospital". Use the conventional canonical name.
- Military/naval: Sandhurst -> "Royal Military College, Sandhurst" \
(military_academy); Woolwich / "R.M.A." -> "Royal Military Academy, Woolwich" \
(military_academy); Dartmouth/Osborne -> naval_college; "R.I.E. College" / \
"Cooper's Hill" -> "Royal Indian Engineering College" (professional).
- Inns of Court (Inner Temple, Middle Temple, Lincoln's Inn, Gray's Inn) -> \
type inn_of_court.
- Expand obvious abbreviations to the full conventional name (coll.->College, \
univ.->University, Trin.->Trinity, Magd.->Magdalen, Oxon.->Oxford, \
Cantab.->Cambridge, Edin.->Edinburgh).
- DROP everything that is NOT an institution: bare degrees and letters \
(B.A., M.A., LL.B., M.R.C.S., F.R.C.S., A.M.I.C.E.), "called to the bar" / \
"Barrister-at-Law" with no Inn named, prizes, scholarships, exhibitions, \
medals, examination years, "appointed after examination of 18xx".
- If the clause names no institution, return {"institutions": []}.
- Output the JSON object and nothing else (no prose, no markdown)."""


def _distinct_education(ed_path: Path) -> "dict[str, int]":
    """education string -> mention count, across all person rows."""
    c: Counter = Counter()
    for l in ed_path.open(encoding="utf-8"):
        e = (json.loads(l).get("education") or "").strip()
        if e:
            c[e] += 1
    return c


def cmd_run(args) -> None:
    from openai import OpenAI
    from col_match.volume.llm import _extract_json

    OUT = kg_out()
    ed_path = OUT / "graph_stage3" / "education.jsonl"
    out_path = Path(args.out) if args.out else OUT / "education_parsed.jsonl"

    counts = _distinct_education(ed_path)
    # only strings worth a call: length gate skips bare "B.A." style fragments
    strings = [s for s in counts if len(s) > args.min_len]

    done = set()
    if out_path.exists():
        for l in out_path.open(encoding="utf-8"):
            o = json.loads(l)
            if "institutions" in o:        # successful rows only; _error retried
                done.add(o["education"])
    todo = [s for s in strings if s not in done]
    todo.sort(key=lambda s: -counts[s])    # high-frequency strings first
    if args.limit:
        todo = todo[: args.limit]
    print(f"distinct education strings={len(counts)}  parseable(>{args.min_len} "
          f"chars)={len(strings)}  done={len(done)}  todo={len(todo)}  "
          f"workers={args.workers} -> {out_path}", flush=True)

    reasoning_body = {"chat_template_kwargs": {"enable_thinking": bool(args.reason)}}
    client = OpenAI(base_url=args.base_url, api_key="not-needed")

    def work(s: str) -> dict:
        for attempt in range(4):
            try:
                r = client.chat.completions.create(
                    model=args.model, temperature=0.0, max_tokens=args.max_tokens,
                    extra_body=reasoning_body,
                    messages=[{"role": "system", "content": SYSTEM},
                              {"role": "user", "content": s}])
                out = _extract_json(r.choices[0].message.content or "")
                if isinstance(out, dict) and isinstance(out.get("institutions"), list):
                    return {"education": s, "institutions": out["institutions"]}
                return {"education": s, "_error": "no JSON"}
            except Exception as e:
                if attempt == 3:
                    return {"education": s, "_error": f"{type(e).__name__}: {e}"[:120]}
                time.sleep(2 ** attempt * 3)

    lock = threading.Lock()
    ok = bad = 0
    t0 = time.time()
    with out_path.open("a", encoding="utf-8") as fh, \
            ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(work, s) for s in todo]
        for i, fut in enumerate(as_completed(futs), 1):
            o = fut.result()
            with lock:
                fh.write(json.dumps(o, ensure_ascii=False) + "\n")
                fh.flush()
            bad += "_error" in o
            ok += "_error" not in o
            if i % 100 == 0 or i == len(todo):
                el = time.time() - t0
                rate = i / el if el else 0
                eta = (len(todo) - i) / rate / 3600 if rate else 0
                print(f"  [{i}/{len(todo)}] ok={ok} bad={bad}  {rate:.2f} str/s  "
                      f"ETA {eta:.2f}h", flush=True)
    el = time.time() - t0
    print(f"done: {ok} ok, {bad} bad in {el/3600:.2f}h -> {out_path}")
    print("next:  COL_KG_OUT=... python3 kg_parse_education.py worklist")


# ---- type normalisation: collapse the LLM's fine types to the grounding set ----
_TYPE_MAP = {
    "naval_college": "military_academy", "military_academy": "military_academy",
    "university": "university", "university_college": "university_college",
    "school": "school", "inn_of_court": "inn_of_court",
    "professional": "professional", "other": "other",
}


def _norm_name(n: str) -> str:
    n = " ".join((n or "").split())
    return n.strip(" ,.;")


# British "public schools" (independent/endowed) named bare in the corpus. Used
# to tag a school's subtype when the name alone tells us grammar vs public.
_PUBLIC_SCHOOLS = {
    "eton college", "harrow school", "winchester college", "rugby school",
    "charterhouse", "cheltenham college", "clifton college", "dulwich college",
    "wellington college", "haileybury college",
    "haileybury and imperial service college", "sherborne school",
    "repton school", "shrewsbury school", "westminster school",
    "tonbridge school", "uppingham school", "malvern college", "radley college",
    "lancing college", "bradfield college", "stonyhurst college",
    "downside school", "fettes college", "loretto school", "sedbergh school",
    "oundle school", "blundell's school", "epsom college", "brighton college",
    "whitgift school", "rossall school", "bedford school", "felsted school",
    "berkhamsted school", "marlborough college", "st. paul's school",
    "st paul's school", "merchant taylors' school", "wellingborough school",
    "monkton combe school",
}


# University cohorts (the analytically interesting axis for colonial recruits).
_REDBRICK = {"birmingham", "bristol", "leeds", "liverpool", "manchester",
             "sheffield", "victoria university"}           # red brick (Q1202123)
_SCOTTISH = {"st andrews", "st. andrews", "glasgow", "aberdeen", "edinburgh"}
_INDIAN_UNI = {"calcutta", "madras", "bombay", "allahabad", "punjab", "lucknow",
               "aligarh", "benares", "dacca", "patna", "nagpur", "mysore"}
_IRISH_UNI = {"dublin", "cork", "galway", "belfast", "r.u.i", "ireland"}

# Subtype -> Wikidata class QID. Only ids that are user-supplied or verified are
# filled; others stay None until confirmed via MCP (never invent QIDs).
SUBTYPE_QID = {
    "grammar": "Q967098",      # grammar school (verified)
    "redbrick": "Q1202123",    # red brick university (user-supplied)
    # "public": "Q5887603"?  "oxbridge"?  "ancient_scottish"?  -> verify via MCP
}


def _institution_subtype(name: str, typ: str) -> "str | None":
    """Cohort label for analysis: schools -> grammar|public|school;
    universities/colleges -> oxbridge|ancient_scottish|redbrick|london|irish|
    indian|university. None for non-school/non-university types."""
    low = name.lower()
    if typ == "school":
        if "grammar school" in low:
            return "grammar"
        if low in _PUBLIC_SCHOOLS:
            return "public"
        return "school"
    if typ in ("university", "university_college"):
        if "oxford" in low or "cambridge" in low:
            return "oxbridge"
        if any(s in low for s in _SCOTTISH):
            return "ancient_scottish"
        if any(r in low for r in _REDBRICK):
            return "redbrick"
        if "london" in low or "imperial college" in low:
            return "london"
        if any(i in low for i in _IRISH_UNI):
            return "irish"
        if any(i in low for i in _INDIAN_UNI):
            return "indian"
        return "university"
    if typ == "military_academy":
        if ("naval" in low or "dartmouth" in low or "osborne" in low
                or "greenwich" in low):
            return "naval"
        if "woolwich" in low:                  # RMA "the Shop" - artillery/engineers
            return "woolwich"
        if "sandhurst" in low:                 # RMC - army officers
            return "sandhurst"
        if "addiscombe" in low:                # East India Company military seminary
            return "addiscombe"
        if "staff college" in low:             # Camberley/Quetta - advanced
            return "staff"
        if "indian military academy" in low or "dehra dun" in low:
            return "indian_military"
        return "military"
    return None


def cmd_worklist(args) -> None:
    OUT = kg_out()
    parsed_path = Path(args.parsed) if args.parsed else OUT / "education_parsed.jsonl"
    ed_path = OUT / "graph_stage3" / "education.jsonl"
    out_path = OUT / "education_worklist.jsonl"

    # education string -> [(name, type), ...]
    str2inst: "dict[str, list]" = {}
    for l in parsed_path.open(encoding="utf-8"):
        o = json.loads(l)
        if "institutions" not in o:
            continue
        seen = []
        for it in o["institutions"]:
            nm = _norm_name(it.get("name", ""))
            if not nm:
                continue
            ty = _TYPE_MAP.get((it.get("type") or "other").lower(), "other")
            if (nm, ty) not in seen:
                seen.append((nm, ty))
        str2inst[o["education"]] = seen

    inst_persons: "dict[str, set]" = defaultdict(set)
    inst_type: "dict[str, str]" = {}
    inst_examples: "dict[str, list]" = defaultdict(list)
    n_rows = parsed_hits = 0
    for l in ed_path.open(encoding="utf-8"):
        r = json.loads(l)
        e = (r.get("education") or "").strip()
        pid = r["person_id"]
        n_rows += 1
        for nm, ty in str2inst.get(e, []):
            inst_persons[nm].add(pid)
            inst_type[nm] = ty
            if len(inst_examples[nm]) < 2:
                inst_examples[nm].append(e[:70])
            parsed_hits += 1

    work = [{"institution": k, "type": inst_type[k],
             "subtype": _institution_subtype(k, inst_type[k]), "count": len(v),
             "person_ids": sorted(v)[:50], "examples": inst_examples[k]}
            for k, v in inst_persons.items()]
    work.sort(key=lambda w: -w["count"])
    with out_path.open("w", encoding="utf-8") as fh:
        for w in work:
            fh.write(json.dumps(w, ensure_ascii=False) + "\n")

    mentions = sum(w["count"] for w in work)
    tc = Counter(w["type"] for w in work)
    print(f"education rows={n_rows:,}  parsed strings={len(str2inst):,}")
    print(f"distinct institutions={len(work):,}  total mentions={mentions:,}")
    print("by type:", dict(tc))
    print("TOP 25:")
    for w in work[:25]:
        print(f"  {w['count']:5d}  {w['type']:<17} {w['institution']}")
    print(f"\nwrote -> {out_path}")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run", help="LLM-parse distinct education strings")
    r.add_argument("--base-url", required=True, dest="base_url")
    r.add_argument("--model", default="qwen3.6-35b-a3b")
    r.add_argument("--workers", type=int, default=16)
    r.add_argument("--out", default="")
    r.add_argument("--reason", action="store_true")
    r.add_argument("--max-tokens", type=int, default=512, dest="max_tokens")
    r.add_argument("--min-len", type=int, default=10, dest="min_len")
    r.add_argument("--limit", type=int, default=0)
    r.set_defaults(f=cmd_run)

    w = sub.add_parser("worklist", help="build education_worklist.jsonl from parsed")
    w.add_argument("--parsed", default="")
    w.set_defaults(f=cmd_worklist)

    args = ap.parse_args()
    args.f(args)


if __name__ == "__main__":
    main()
