#!/usr/bin/env python3
"""Qwen bio-entry parsing worker (runs on the GPU node next to a local
OpenAI-compatible server). Self-contained: no col_match import.

  python3 qwen_bio_worker.py --worklist qwen_bio_worklist.jsonl \
      --out qwen_bio_results.jsonl --url http://localhost:8000/v1 \
      --model qwen3-30b-a3b --workers 16

Resumable: ids already present in --out are skipped. Each output line:
  {"id", "year", "provenance", "bio": {...}}      parsed entry
  {"id", "year", "provenance", "not_a_bio": true} preamble/junk block
or {"id", ..., "error": str} on failure.
"""
import argparse, json, re, threading, time, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

SYSTEM = (
    "You convert one printed Colonial Office List biographical entry into "
    "JSON. Extract ONLY what is printed; never invent. Each career posting is "
    "one event with: position (as printed, keep abbreviations), place (colony "
    "or territory named, or carried over from the previous posting), "
    "year_start, year_end (null if not printed). Return strictly: "
    '{"surname": str, "given_names": str|null, "birth_year": int|null, '
    '"honours": [{"award": str, "year": int|null}], '
    '"events": [{"position": str|null, "place": str|null, '
    '"year_start": int|null, "year_end": int|null}]}. '
    "If the text is NOT a biographical entry (section preamble, explanatory "
    'note, list of abbreviations, running text), return {"not_a_bio": true}.'
)


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
        "model": model, "temperature": 0.0, "max_tokens": 4096,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
    }).encode()
    req = urllib.request.Request(url.rstrip("/") + "/chat/completions", data=body,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer local"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)["choices"][0]["message"]["content"] or ""


def valid_bio(out):
    """Sanity-gate the parsed entry; returns dict or None."""
    if not isinstance(out, dict):
        return None
    if out.get("not_a_bio") is True:
        return {"not_a_bio": True}
    if not isinstance(out.get("surname"), str) or not out["surname"].strip():
        return None
    events = []
    for ev in out.get("events") or []:
        if not isinstance(ev, dict):
            continue
        ys, ye = ev.get("year_start"), ev.get("year_end")
        if ys is not None and not (isinstance(ys, int) and 1750 <= ys <= 1975):
            ys = None
        if ye is not None and not (isinstance(ye, int) and 1750 <= ye <= 1975):
            ye = None
        pos, place = ev.get("position"), ev.get("place")
        if not (pos or place):
            continue
        events.append({"position": (str(pos)[:160] if pos else None),
                       "place": (str(place)[:80] if place else None),
                       "year_start": ys, "year_end": ye})
    honours = []
    for h in out.get("honours") or []:
        if isinstance(h, dict) and isinstance(h.get("award"), str):
            hy = h.get("year")
            honours.append({"award": h["award"][:40],
                            "year": hy if isinstance(hy, int) else None})
    by = out.get("birth_year")
    return {"surname": out["surname"].strip()[:80],
            "given_names": (out.get("given_names") or None),
            "birth_year": by if isinstance(by, int) and 1750 <= by <= 1950 else None,
            "honours": honours, "events": events[:60]}


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
    stats = {"ok": 0, "not_a_bio": 0, "err": 0, "events": 0}

    def one(b):
        for attempt in (1, 2):
            try:
                bio = valid_bio(extract_json(chat(args.url, args.model, SYSTEM, b["text"])))
                if bio is None:
                    raise ValueError("no valid bio JSON in response")
                base = {"id": b["id"], "year": b["year"], "provenance": b["provenance"]}
                if bio.get("not_a_bio"):
                    return {**base, "not_a_bio": True}
                return {**base, "bio": bio}
            except Exception as e:
                if attempt == 2:
                    return {"id": b["id"], "year": b["year"],
                            "provenance": b["provenance"],
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
                elif res.get("not_a_bio"):
                    stats["not_a_bio"] += 1
                else:
                    stats["ok"] += 1
                    stats["events"] += len(res["bio"]["events"])
                if k % 500 == 0:
                    rate = k / (time.time() - t0)
                    eta = (len(work) - k) / rate / 60
                    print(f"{k:,}/{len(work):,}  ok={stats['ok']:,} "
                          f"not_a_bio={stats['not_a_bio']:,} err={stats['err']:,} "
                          f"events={stats['events']:,} {rate:.1f}/s eta {eta:.0f}m",
                          flush=True)
                    out_fh.flush()
    out_fh.close()
    print("FINAL", json.dumps(stats), flush=True)


if __name__ == "__main__":
    main()
