#!/usr/bin/env python3
"""Civil-list residue re-parse worker (GPU node, local OpenAI-compatible
server). Re-parses raw office—holder lines the rules parser mangled
(fragment names, swallowed prose, reversed political-agent lines,
multi-ditto offices). Self-contained: no col_match import.

  python3 qwen_civil_parse_worker.py --worklist wl_civil.jsonl \
      --out res_civil.jsonl --url http://localhost:8000/v1

Resumable: ids already in --out are skipped. Each output line:
  {"id", "office", "holders": [{"name", "prefix", "honours",
   "service"}], "unparseable": bool, "note"}
or {"id", "error": str} on failure.
"""
import argparse, json, re, threading, time, urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

SYSTEM = (
    "You parse one line from a British India Office List establishment "
    "roster (1861-1947). The usual grammar is:\n"
    "  <office> — <holder>[; <holder>...]\n"
    "where each holder is [rank or honorific prefix] <name> [, honour "
    "letters like C.I.E., K.C.S.I., O.B.E.] [, service tag like I.C.S., "
    "I.M.S., I.A.]. Some lines are REVERSED (name first, office after: "
    "'J. Smith, Political Agent at Kolhapur'). Some lines are not "
    "roster entries at all (prose, headings, page furniture).\n"
    "Rules:\n"
    "- Copy names EXACTLY as printed (keep initials, accents, Indian "
    "honorific words that are part of the name).\n"
    "- 'Esq.', 'Esqrs.', 'Bart.' are suffixes, not names.\n"
    "- Rank words (Major, Col., Rev., Sir) and Indian honorifics used as "
    "prefixes (Khan Bahadur, Rai Bahadur, Nawab, Pandit...) go in "
    "'prefix', not 'name'.\n"
    "- honours = the letter-group awards only (C.I.E., O.B.E., ...); "
    "service = one of I.C.S./I.M.S./I.A./I.P./I.F.S./I.S.E./I.E.S. if "
    "printed.\n"
    "- If the line holds several offices, use the office each holder "
    "belongs to only if unambiguous; otherwise mark unparseable.\n"
    'Return strictly: {"office": "<office or null>", "holders": '
    '[{"name": "...", "prefix": "<or null>", "honours": ["..."], '
    '"service": "<or null>"}], "unparseable": true|false, '
    '"note": "<=100 chars>"}'
)


def render(row):
    lines = [f"Roster line: {row['raw_line']}"]
    if row.get("government"):
        ctx = row["government"]
        if row.get("department"):
            ctx += f" / {row['department']}"
        lines.append(f"(section context: {ctx})")
    lines.append("Parse it.")
    return "\n".join(lines)


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
        "model": model, "temperature": 0.0, "max_tokens": 600,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
    }).encode()
    req = urllib.request.Request(url.rstrip("/") + "/chat/completions",
                                 data=body,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer local"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)["choices"][0]["message"]["content"] or ""


def valid_parse(out):
    if not isinstance(out, dict) or "holders" not in out:
        return None
    holders = out.get("holders")
    if not isinstance(holders, list):
        return None
    clean = []
    for h in holders:
        if not isinstance(h, dict) or not isinstance(h.get("name"), str) \
                or not h["name"].strip():
            return None
        clean.append({
            "name": h["name"].strip()[:120],
            "prefix": (h.get("prefix") or None) and str(h["prefix"])[:60],
            "honours": [str(x)[:20] for x in (h.get("honours") or [])
                        if isinstance(x, str)][:12],
            "service": (h.get("service") or None)
            and str(h["service"])[:15],
        })
    office = out.get("office")
    return {"office": (str(office)[:200] if office else None),
            "holders": clean,
            "unparseable": bool(out.get("unparseable")),
            "note": str(out.get("note") or "")[:150]}


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
    print(f"worklist {len(work):,} to do ({len(done):,} already done)",
          flush=True)

    lock = threading.Lock()
    out_fh = open(args.out, "a")
    stats = Counter()

    def one(b):
        base = {"id": b["id"]}
        for attempt in (1, 2):
            try:
                v = valid_parse(extract_json(
                    chat(args.url, args.model, SYSTEM, render(b))))
                if v is None:
                    raise ValueError("no valid parse JSON in response")
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
                stats["err" if "error" in res else
                      ("unparseable" if res.get("unparseable")
                       else "parsed")] += 1
                if k % 500 == 0:
                    rate = k / (time.time() - t0)
                    eta = (len(work) - k) / rate / 60
                    print(f"{k:,}/{len(work):,}  "
                          + " ".join(f"{s}={n:,}" for s, n in stats.items())
                          + f"  {rate:.1f}/s eta {eta:.0f}m", flush=True)
                    out_fh.flush()
    out_fh.close()
    print("FINAL", json.dumps(stats), flush=True)


if __name__ == "__main__":
    main()
