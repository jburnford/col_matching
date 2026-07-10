#!/usr/bin/env python3
"""Class-C pairwise adjudication worker (GPU node, local OpenAI-compatible
server). Judges whether an unlinked roster career and a bio person are the
same person. Self-contained: no col_match import.

  python3 qwen_classc_worker.py --worklist classc_worklist.jsonl \
      --out classc_results.jsonl --url http://localhost:8000/v1 \
      --model qwen3-30b-a3b --workers 16

Resumable: ids already present in --out are skipped. Each output line:
  {"id", "career_id", "person_id", "verdict": "same"|"different"|"unsure",
   "confidence": 0-100, "reason": str}
or {"id", ..., "error": str} on failure.
"""
import argparse, json, re, threading, time, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

SYSTEM = (
    "You compare two records from the British Colonial Office List and judge "
    "whether they describe the SAME person.\n"
    "Record 1 is a staff-roster career: the years a name was printed in one "
    "colony's establishment list, with position/department/salary per year.\n"
    "Record 2 is a biographical entry ('Record of Services'): a person's "
    "appointment history across the empire, possibly with birth year and "
    "honours.\n"
    "Judge ONLY on the printed evidence:\n"
    "- Timing: someone on a roster is serving in that colony in those years; "
    "the biography's appointments should cover or plausibly explain the "
    "roster years (biographies can lag a year or two).\n"
    "- Place: the biography should put the person in that colony (or a "
    "predecessor/successor territory) during the roster years.\n"
    "- Rank: the roster position and salary should fit the biography's "
    "trajectory at that date (a clerk on 100 pounds is not a colonial "
    "secretary; allow promotion over time).\n"
    "Initials matching a fuller name is compatible, but a name match alone "
    "is NOT evidence — namesakes are common; different concurrent careers in "
    "different places mean different people.\n"
    'Return strictly: {"verdict": "same"|"different"|"unsure", '
    '"confidence": 0-100, "reason": "<=200 chars, cite the deciding '
    'year/place/rank facts"}'
)


def render(pair):
    c, p = pair["career"], pair["person"]
    lines = [
        f"RECORD 1 — roster career in {c['colony']}: {c['name']}",
        f"listed {c['roster_years'][0]}-{c['roster_years'][-1]}" if c.get("roster_years") else "",
        *c["lines"],
        "",
        f"RECORD 2 — biographical entry: {p['name']}"
        + (f", b. {p['birth_year']}" if p.get("birth_year") else ""),
        (f"honours: {', '.join(p['honours'])}" if p.get("honours") else ""),
        (f"appears in editions {p['editions'][0]}-{p['editions'][1]}" if p.get("editions") else ""),
        *p["lines"],
        "",
        "Same person?",
    ]
    return "\n".join(l for l in lines if l != "")


def extract_json(text):
    text = re.sub(r"```(?:json)?|```", "", text).strip()
    i = text.find("{")
    if i < 0:
        return None
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(text[i:j + 1])
                except json.JSONDecodeError:
                    return None
    return None


def chat(url, model, system, user, timeout=180):
    body = json.dumps({
        "model": model, "temperature": 0.0, "max_tokens": 400,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
    }).encode()
    req = urllib.request.Request(url.rstrip("/") + "/chat/completions", data=body,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer local"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)["choices"][0]["message"]["content"] or ""


def valid_verdict(out):
    if not isinstance(out, dict):
        return None
    v = out.get("verdict")
    if v not in ("same", "different", "unsure"):
        return None
    conf = out.get("confidence")
    if not isinstance(conf, (int, float)) or not 0 <= conf <= 100:
        conf = None
    return {"verdict": v, "confidence": conf,
            "reason": str(out.get("reason") or "")[:250]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--worklist", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--url", default="http://localhost:8000/v1")
    ap.add_argument("--model", default="qwen3-30b-a3b")
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    done = set()
    try:
        for line in open(args.out):
            try:
                done.add(json.loads(line)["id"])
            except Exception:
                pass
    except FileNotFoundError:
        pass

    work = [json.loads(l) for l in open(args.worklist)]
    work = [b for b in work if b["id"] not in done]
    if args.limit:
        work = work[:args.limit]
    print(f"worklist {len(work):,} to do ({len(done):,} already done)", flush=True)

    lock = threading.Lock()
    out_fh = open(args.out, "a")
    stats = {"same": 0, "different": 0, "unsure": 0, "err": 0}

    def one(b):
        base = {"id": b["id"], "career_id": b["career_id"],
                "person_id": b["person_id"], "cand_rank": b.get("cand_rank")}
        for attempt in (1, 2):
            try:
                v = valid_verdict(extract_json(
                    chat(args.url, args.model, SYSTEM, render(b))))
                if v is None:
                    raise ValueError("no valid verdict JSON in response")
                return {**base, **v}
            except Exception as e:
                if attempt == 2:
                    return {**base, "error": f"{type(e).__name__}: {e}"[:300]}
                time.sleep(3)

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(one, b) for b in work]
        for k, f in enumerate(as_completed(futs), 1):
            res = f.result()
            with lock:
                out_fh.write(json.dumps(res, ensure_ascii=False) + "\n")
                stats["err" if "error" in res else res["verdict"]] += 1
                if k % 500 == 0:
                    rate = k / (time.time() - t0)
                    eta = (len(work) - k) / rate / 60
                    print(f"{k:,}/{len(work):,}  " +
                          " ".join(f"{s}={n:,}" for s, n in stats.items()) +
                          f"  {rate:.1f}/s eta {eta:.0f}m", flush=True)
                    out_fh.flush()
    out_fh.close()
    print("FINAL", json.dumps(stats), flush=True)


if __name__ == "__main__":
    main()
