#!/usr/bin/env python3
"""Qwen roster-block extraction worker (runs on the GPU node next to a local
OpenAI-compatible server). Self-contained: no col_match import.

  python3 qwen_roster_worker.py --worklist qwen_worklist.jsonl \
      --out qwen_roster_results.jsonl --url http://localhost:8000/v1 \
      --model qwen3-30b-a3b --workers 12

Resumable: ids already present in --out are skipped. Each output line:
  {"id", "year", "colony", "department", "provenance", "records":[...]}
or {"id", ..., "error": str} on failure.
"""
import argparse, json, re, sys, threading, time, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

SYSTEM = (
    "You extract every staff-list officer record from one printed Colonial "
    "Office List roster block. Each record is a person holding a post in the "
    "given colony. Return ONLY people actually named (skip salary-only or "
    "header fragments, statistics, and narrative sentences). For each: "
    "position (as printed), surname, given_names (initials or names as "
    "printed, null if none), honours (list of strings), salary (as printed, "
    'null if none). Return strictly a JSON array: [{"position": str|null, '
    '"surname": str, "given_names": str|null, "honours": [str], '
    '"salary": str|null}]. Extract names from run-on lists too '
    "(e.g. 'Puisne Judges, A. B. Smith; C. D. Jones' = two records). "
    "If the block contains no named people, return []."
)

def extract_json(text):
    text = re.sub(r"```(?:json)?|```", "", text).strip()
    order = sorted((("{", "}"), ("[", "]")),
                   key=lambda oc: (text.find(oc[0]) if oc[0] in text else len(text) + 1))
    for opener, closer in order:
        i = text.find(opener)
        if i < 0:
            continue
        depth = 0
        for j in range(i, len(text)):
            if text[j] == opener:
                depth += 1
            elif text[j] == closer:
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[i:j + 1])
                    except json.JSONDecodeError:
                        break
    return None

def chat(url, model, system, user, timeout=180):
    body = json.dumps({
        "model": model, "temperature": 0.0, "max_tokens": 4096,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
    }).encode()
    req = urllib.request.Request(url.rstrip("/") + "/chat/completions", data=body,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer local"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)["choices"][0]["message"]["content"] or ""

def valid_records(out):
    if not isinstance(out, list):
        return None
    recs = []
    for r in out:
        if not isinstance(r, dict) or not isinstance(r.get("surname"), str):
            continue
        if not r["surname"].strip() or len(r["surname"]) > 60:
            continue
        recs.append({"position": r.get("position"), "surname": r["surname"].strip(),
                     "given_names": r.get("given_names"),
                     "honours": [h for h in (r.get("honours") or []) if isinstance(h, str)],
                     "salary": r.get("salary")})
    return recs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--worklist", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--url", default="http://localhost:8000/v1")
    ap.add_argument("--model", default="qwen3-30b-a3b")
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--limit", type=int, default=0, help="debug: stop after N")
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

    work = []
    for line in open(args.worklist):
        b = json.loads(line)
        if b["id"] not in done:
            work.append(b)
    if args.limit:
        work = work[:args.limit]
    print(f"worklist {len(work):,} to do ({len(done):,} already done)", flush=True)

    lock = threading.Lock()
    out_fh = open(args.out, "a")
    stats = {"ok": 0, "empty": 0, "err": 0, "records": 0}

    def one(b):
        user = (f"Colony: {b.get('colony')}\nDepartment: {b.get('department') or '(none)'}"
                f"\n\nBlock:\n{b['text']}")
        for attempt in (1, 2):
            try:
                recs = valid_records(extract_json(chat(args.url, args.model, SYSTEM, user)))
                if recs is None:
                    raise ValueError("no JSON array in response")
                return {"id": b["id"], "year": b["year"], "colony": b.get("colony"),
                        "department": b.get("department"),
                        "provenance": b["provenance"], "records": recs}
            except Exception as e:
                if attempt == 2:
                    return {"id": b["id"], "year": b["year"], "provenance": b["provenance"],
                            "error": f"{type(e).__name__}: {e}"[:300]}
                time.sleep(3)

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(one, b) for b in work]
        for k, f in enumerate(as_completed(futs), 1):
            res = f.result()
            with lock:
                out_fh.write(json.dumps(res, ensure_ascii=False) + "\n")
                if "error" in res:
                    stats["err"] += 1
                elif res["records"]:
                    stats["ok"] += 1; stats["records"] += len(res["records"])
                else:
                    stats["empty"] += 1
                if k % 200 == 0:
                    rate = k / (time.time() - t0)
                    eta = (len(work) - k) / rate / 60
                    print(f"{k:,}/{len(work):,}  ok={stats['ok']:,} empty={stats['empty']:,} "
                          f"err={stats['err']:,} records={stats['records']:,} "
                          f"{rate:.1f}/s eta {eta:.0f}m", flush=True)
                    out_fh.flush()
    out_fh.close()
    print("FINAL", json.dumps(stats), flush=True)

if __name__ == "__main__":
    main()
