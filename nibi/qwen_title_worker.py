#!/usr/bin/env python3
"""Section-title classification worker (GPU node, local OpenAI-compatible
server). Classifies the 7,931 long-tail printed section titles the keyword
taxonomy in volume_block_index.py could not place — classifying TITLES, not
blocks, is ~25x cheaper (they govern 166k blocks). Self-contained.

  python3 qwen_title_worker.py --worklist qwen_title_worklist.jsonl \
      --out qwen_title_results.jsonl --url http://localhost:8000/v1 \
      --model qwen3-30b-a3b --workers 16

Resumable. Each output line:
  {"id", "title", "n_blocks", "class": <taxonomy|other|garbled>, "reason"}
or {"id", ..., "error": str}.
"""
import argparse, json, re, threading, time, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

# must stay in sync with volume_block_index.py _TAXONOMY (+ the two classes
# assigned structurally there: establishment via roster titles, services_bios
# via the services section)
CLASSES = {
    "governors_list": "list of past governors/administrators/high commissioners",
    "honours_roll": "order membership rolls (knights, companions, dames)",
    "obituary": "obituary",
    "history": "history of the territory",
    "geography": "situation, area, climate, physical description, chief towns",
    "population": "population, census, vital statistics",
    "constitution": "constitution, form of government, franchise, administration",
    "councils": "executive/legislative council or assembly membership",
    "finance": "revenue, expenditure, taxation, public debt, budget, tariff",
    "currency_banking": "currency, coinage, banking, exchange",
    "trade": "imports/exports, commerce, shipping, crops, industry, mining",
    "infrastructure": "railways, roads, ports, post, telegraph, aviation, communications",
    "land_labour": "land policy/tenure, crown lands, immigration, labour",
    "social": "education, schools, health, hospitals, religion, welfare, housing",
    "justice": "courts, laws, crime, judicial matters",
    "defence": "military, militia, volunteers, garrison",
    "agents_consuls": "colonial agents and foreign consuls",
    "regulations": "office regulations, rules, instructions, precedency, passages",
    "papers": "parliamentary papers, publications, bibliography",
    "establishment": "staff list / establishment roster (officials with posts, salaries)",
    "imperial_institutions": "Colonial Office, Crown Agents, imperial institutes and bureaux",
}

SYSTEM = (
    "You classify one printed section title from the British Colonial Office "
    "List (1867-1966) into exactly one class. The titles head sections inside "
    "a colony chapter or in the volume's front/back matter. OCR noise is "
    "common (e.g. 'GAMBLA' = Gambia); classify by what the title plainly "
    "denotes. Classes:\n"
    + "\n".join(f"- {k}: {v}" for k, v in CLASSES.items())
    + "\n- other: a real title that fits none of the above "
    "(e.g. a colony/place name alone, an advertisement, a ship list)\n"
    "- garbled: OCR wreckage with no recoverable meaning\n"
    'Return strictly: {"class": "<one class key>", "reason": "<=100 chars"}'
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


def chat(url, model, system, user, timeout=120):
    body = json.dumps({
        "model": model, "temperature": 0.0, "max_tokens": 200,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
    }).encode()
    req = urllib.request.Request(url.rstrip("/") + "/chat/completions", data=body,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer local"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)["choices"][0]["message"]["content"] or ""


VALID = set(CLASSES) | {"other", "garbled"}


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
    stats = {"ok": 0, "err": 0}

    def one(b):
        base = {"id": b["id"], "title": b["title"], "n_blocks": b["n_blocks"]}
        for attempt in (1, 2):
            try:
                out = extract_json(chat(args.url, args.model, SYSTEM,
                                        f"Title: {b['title']!r}"))
                if not isinstance(out, dict) or out.get("class") not in VALID:
                    raise ValueError("no valid class in response")
                return {**base, "class": out["class"],
                        "reason": str(out.get("reason") or "")[:150]}
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
                stats["err" if "error" in res else "ok"] += 1
                if k % 500 == 0:
                    rate = k / (time.time() - t0)
                    eta = (len(work) - k) / rate / 60
                    print(f"{k:,}/{len(work):,}  ok={stats['ok']:,} "
                          f"err={stats['err']:,}  {rate:.1f}/s eta {eta:.0f}m",
                          flush=True)
                    out_fh.flush()
    out_fh.close()
    print("FINAL", json.dumps(stats), flush=True)


if __name__ == "__main__":
    main()
