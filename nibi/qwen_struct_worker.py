#!/usr/bin/env python3
"""Bio-structuring worker (GPU node, local OpenAI-compatible server).
Structures Record-of-Services bio texts into KG career JSON — the
standalone twin of kg_structure_corpus.py for delta runs (the nibi box
has no col_match checkout). The system prompt (KG_BIO_SYSTEM +
KEYS_SUFFIX, exported by the worklist builder) rides in the worklist
file itself under `_system` on the first line.

  python3 qwen_struct_worker.py --worklist struct_worklist.jsonl \
      --out struct_results.jsonl --url http://localhost:8000/v1

Worklist rows: {"person_id", "text"} (text pre-normalized locally).
Resumable: person_ids already in --out WITHOUT `_error` are skipped.
Output rows: the model's JSON object + {"person_id"}; `_error` on
failure (retried on resume).
"""
import argparse, json, re, threading, time, urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed


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


def chat(url, model, system, user, max_tokens, timeout=240):
    body = json.dumps({
        "model": model, "temperature": 0.0, "max_tokens": max_tokens,
        "chat_template_kwargs": {"enable_thinking": False},
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
    }).encode()
    req = urllib.request.Request(url.rstrip("/") + "/chat/completions",
                                 data=body,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer local"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)["choices"][0]["message"]["content"] or ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--worklist", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--url", default="http://localhost:8000/v1")
    ap.add_argument("--model", default="qwen3-30b-a3b")
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--max-tokens", type=int, default=3000)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    rows = [json.loads(l) for l in open(args.worklist)]
    system = rows[0].get("_system")
    if system:
        rows = rows[1:]
    if not system:
        raise SystemExit("worklist missing _system header row")

    done = set()
    try:
        for line in open(args.out):
            try:
                o = json.loads(line)
                if "_error" not in o:
                    done.add(o["person_id"])
            except Exception:
                pass
    except FileNotFoundError:
        pass

    work = [b for b in rows if b["person_id"] not in done]
    if args.limit:
        work = work[:args.limit]
    print(f"worklist {len(work):,} to do ({len(done):,} already done)",
          flush=True)

    lock = threading.Lock()
    out_fh = open(args.out, "a")
    stats = Counter()

    def one(b):
        for attempt in range(3):
            try:
                out = extract_json(chat(args.url, args.model, system,
                                        b["text"], args.max_tokens))
                if isinstance(out, dict):
                    out["person_id"] = b["person_id"]
                    return out
                raise ValueError("no JSON object in response")
            except Exception as e:
                if attempt == 2:
                    return {"person_id": b["person_id"],
                            "_error": f"{type(e).__name__}: {e}"[:200]}
                time.sleep(3 * (attempt + 1))

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(one, b) for b in work]
        for k, f in enumerate(as_completed(futs), 1):
            res = f.result()
            with lock:
                out_fh.write(json.dumps(res, ensure_ascii=False) + "\n")
                stats["err" if "_error" in res else "ok"] += 1
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
