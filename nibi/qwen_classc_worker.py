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



SKEPTIC_SYSTEM = (
    "You audit a PROPOSED identity match between a staff-roster career and a "
    "biographical entry from the British Colonial Office List. The match is "
    "SUSPECT: the names are only loosely compatible (initials do not match "
    "exactly) or the only support is name similarity. Namesakes are common in "
    "this corpus.\n"
    "Default to reject. Confirm ONLY if the biography contains an explicit "
    "appointment that places this person in the roster's colony, during the "
    "roster years, in the same position or position family — and QUOTE that "
    "appointment. Name compatibility, plausibility, or absence of "
    "contradiction are NOT sufficient.\n"
    'Return strictly: {"verdict": "confirm"|"reject", '
    '"evidence": "<the quoted appointment, or empty>", '
    '"reason": "<=150 chars"}'
)

MERGE_SYSTEM = (
    "You compare two biographical entries ('Record of Services') from "
    "different editions of the British Colonial Office List and judge "
    "whether they describe the SAME person. Both entries were "
    "independently matched to the same staff-roster row (shown as "
    "context), so they are strong candidates — but same-family namesakes "
    "(father/son, brothers) also produce this signature.\n"
    "Judge ONLY on the printed evidence:\n"
    "- Names: initials matching a fuller name is compatible; contradictory "
    "full forenames mean different people.\n"
    "- Birth years: agreement is strong support; disagreement can be OCR "
    "(one digit) but >15 years apart means different people.\n"
    "- Careers: the appointment histories should be the same trajectory "
    "(one may be a longer, later snapshot of the other). Parallel careers "
    "in different places at the same time mean different people.\n"
    "- Honours: the same award in the same year is near-conclusive.\n"
    'Return strictly: {"verdict": "same"|"different"|"unsure", '
    '"confidence": 0-100, "reason": "<=200 chars, cite the deciding '
    'facts"}'
)


IOL_MERGE_SYSTEM = (
    "You compare two biographical entries ('Record of Services') from "
    "different editions of the India Office List and judge whether they "
    "describe the SAME person. A dedup pass proposed merging them — your "
    "verdict measures whether that merge is right. Same-family namesakes "
    "(father/son, brothers) and same-name Indian officers are the failure "
    "modes.\n"
    "Judge ONLY on the printed evidence:\n"
    "- Names: initials matching a fuller name is compatible; contradictory "
    "full forenames mean different people. Indian honorific titles (Khan "
    "Bahadur, Rai Bahadur) are not name evidence.\n"
    "- Birth years: agreement is strong support; disagreement can be OCR "
    "(one digit) but >15 years apart means different people. Most pre-1929 "
    "entries print no birth year — absence is not evidence.\n"
    "- Careers: the appointment histories should be the same trajectory "
    "(one may be a longer, later snapshot of the other — entries are "
    "cumulative across editions). The same specific appointment (office, "
    "place, year) is near-conclusive. Parallel careers in different "
    "provinces at the same time mean different people.\n"
    "- Education: the same school/college + exam year is strong support; "
    "different universities at overlapping ages means different people.\n"
    "- Honours: the same award in the same year is near-conclusive.\n"
    'Return strictly: {"verdict": "same"|"different"|"unsure", '
    '"confidence": 0-100, "reason": "<=200 chars, cite the deciding '
    'facts"}'
)


IOL_NOBIO_SYSTEM = (
    "You compare two ROSTER identities from the India Office List — "
    "each is a civil-list office chain, a gradation (seniority) trace, "
    "or a casualty exit event; NEITHER has a biography — and judge "
    "whether they describe the SAME person. Same-initials namesakes, "
    "fathers and sons, and common Indian names are the failure modes.\n"
    "Judge ONLY on the printed evidence:\n"
    "- Names: initials matching a fuller name is compatible; "
    "contradictory full forenames mean different people. Honorific "
    "titles (Khan Bahadur, Rai Bahadur) are not name evidence.\n"
    "- Covenant/commission year is gold: a civil servant cannot hold a "
    "covenanted office before his covenant year, and a career longer "
    "than ~45 years from entry is implausible.\n"
    "- Establishment sides: Bengal/Madras/Bombay establishments map to "
    "their provinces; Government of India and India Office posts draw "
    "from all three. A Madras-establishment man in a Bengal-side chain "
    "needs strong other evidence.\n"
    "- Timing: consecutive year spans across two governments read as a "
    "transfer (same person); long simultaneous careers in different "
    "provinces mean different people (a short overlap can be dual "
    "listing). For an exit event, the roster trace should STOP within "
    "a year or two of the event date.\n"
    "- Offices: the same or a promoted office stem across the pair "
    "supports; unrelated office families are weak evidence either way.\n"
    'Return strictly: {"verdict": "same"|"different"|"unsure", '
    '"confidence": 0-100, "reason": "<=200 chars, cite the deciding '
    'facts"}'
)


IOL_CHAIN_SYSTEM = (
    "You audit ONE collapsed roster chain from the India Office List "
    "civil lists: every year a given (surname, initials) was printed "
    "holding an office under one government, collapsed into a single "
    "identity. Decide whether the printed trace reads as ONE person's "
    "career or as TWO OR MORE conflated namesakes (fathers and sons, "
    "brothers, common names sharing initials).\n"
    "Signals of ONE person: a coherent office trajectory (stays in or "
    "is promoted through one office family), consistent printed name "
    "forms, consistent honours.\n"
    "Signals of CONFLATION: two unrelated offices held simultaneously "
    "for years, a rank reset (senior office followed years later by a "
    "junior entry-level one), contradictory fuller name forms for the "
    "same initials, or an implausibly long span (>45 years).\n"
    "Gaps alone are weak evidence (leave, deputation, and OCR losses "
    "produce gaps). A short chain with one office is coherent by "
    "default.\n"
    'Return strictly: {"verdict": "confirm"|"reject"|"unsure", '
    '"confidence": 0-100, "reason": "<=200 chars, cite the deciding '
    'records"} — confirm = one person, reject = conflated.'
)


IOL_ABC_SYSTEM = (
    "You compare two records from the India Office List and judge "
    "whether they describe the SAME person.\n"
    "Record 1 is a roster identity with NO biography: either a "
    "civil-list office chain (the years a name was printed holding "
    "offices under one government) or a gradation seniority trace "
    "(army commission or civil covenant year, ranks, corps).\n"
    "Record 2 is a biographical entry ('Record of Services'): a "
    "person's appointment history, possibly with birth year and "
    "honours.\n"
    "Judge ONLY on the printed evidence:\n"
    "- Timing: the biography's appointments should cover or plausibly "
    "explain the roster years (biographies lag a year or two); a "
    "covenant/commission year must match the biography's entry.\n"
    "- Place: the biography should put the person under that "
    "government or establishment side (Bengal/Madras/Bombay; "
    "Government of India and India Office posts draw from all).\n"
    "- Rank: the roster office should fit the biography's trajectory "
    "at that date (allow promotion over time).\n"
    "Initials matching a fuller name is compatible, but a name match "
    "alone is NOT evidence — namesakes are common; different "
    "concurrent careers in different provinces mean different "
    "people.\n"
    'Return strictly: {"verdict": "same"|"different"|"unsure", '
    '"confidence": 0-100, "reason": "<=200 chars, cite the deciding '
    'year/place/rank facts"}'
)


IOL_EXIT_SYSTEM = (
    "You compare a casualty-table exit event from the India Office List "
    "(a printed death or retirement notice with an exact date) with a "
    "biographical entry ('Record of Services') and judge whether they "
    "describe the SAME person. Namesakes are the failure mode; a matched "
    "DEATH is decisive — the biography's attestation should STOP at the "
    "death year.\n"
    "Judge ONLY on the printed evidence:\n"
    "- Names: initials matching a fuller name is compatible; contradictory "
    "full forenames mean different people.\n"
    "- Timing: for a death, career events or edition appearances more than "
    "a year AFTER the death date mean this is NOT the dead person (or the "
    "biography fuses two people — still answer 'different' and say so in "
    "the reason). For a retirement, the career should reach the "
    "retirement year and active appointments should stop near it.\n"
    "- Place/service: the event's place or establishment should fit the "
    "career's provinces and service.\n"
    'Return strictly: {"verdict": "same"|"different"|"unsure", '
    '"confidence": 0-100, "reason": "<=200 chars, cite the deciding '
    'facts"}'
)

IOL_ROLL_SYSTEM = (
    "You compare an honours-roll entry from the India Office List (the "
    "printed grade roll of the Star of India / Indian Empire / Crown of "
    "India, with an exact appointment date) with a biographical entry "
    "('Record of Services') that claims the same grade in a DIFFERENT "
    "year. Judge whether they are the SAME person.\n"
    "The roll is typeset from the order's official list, so when the two "
    "are the same person the roll date is authoritative and the "
    "biography's year is a garble (OCR or parse). When they are "
    "namesakes, the biography keeps its year.\n"
    "Judge ONLY on the printed evidence: name compatibility (initials vs "
    "full forms), whether the career's seniority fits the roll date (a "
    "man appointed C.I.E. in 1920 should be mid-career around 1920, not "
    "a new entrant), and whether the biography's own honours sequence "
    "fits better with the roll date than its printed year.\n"
    'Return strictly: {"verdict": "same"|"different"|"unsure", '
    '"confidence": 0-100, "reason": "<=200 chars, cite the deciding '
    'facts"}'
)

IOL_BIRTH_SYSTEM = (
    "You repair a garbled birth year in a biographical entry from the "
    "India Office List. The printed birth year is IMPOSSIBLE against the "
    "career (entry age too young/old or negative). Candidate repairs are "
    "single-digit or two-digit OCR fixes of the printed year.\n"
    "Pick the candidate that makes the career plausible: appointment to "
    "the civil service or army normally at age 17-30 (competitive-exam "
    "ICS entry clusters at 21-24); last attested activity before age 75; "
    "honours mid-to-late career.\n"
    "If exactly one candidate fits, verdict 'repair' with that year. If "
    "several fit or none do, verdict 'unsure' and explain.\n"
    'Return strictly: {"verdict": "repair"|"unsure", '
    '"birth_year": <int or null>, "confidence": 0-100, '
    '"reason": "<=200 chars, cite entry age and last-activity age"}'
)


def render_chain(pair):
    lines = list(pair["lines"])
    if pair.get("note"):
        lines.append(pair["note"])
    lines += ["", "One person, or conflated namesakes?"]
    return "\n".join(lines)


def render_nobio(pair):
    lines = ["IDENTITY 1:", *pair["a_lines"], "", "IDENTITY 2:",
             *pair["b_lines"], ""]
    if pair.get("note"):
        lines += [pair["note"], ""]
    lines += ["Same person?"]
    return "\n".join(lines)


def render_merge(pair):
    lines = []
    for tag, p in (("RECORD 1", pair["a"]), ("RECORD 2", pair["b"])):
        lines += [
            f"{tag} — biographical entry: {p['name']}"
            + (f", b. {p['birth_year']}" if p.get("birth_year") else ""),
            (f"honours: {', '.join(p['honours'])}" if p.get("honours")
             else ""),
            (f"appears in editions {p['editions'][0]}-{p['editions'][1]}"
             if p.get("editions") else ""),
            *p["lines"],
            "",
        ]
    if pair.get("shared_records"):
        lines += ["Shared roster row(s) both entries matched:",
                  *pair["shared_records"], ""]
    lines += ["Same person?"]
    return "\n".join(l for l in lines if l != "")


def _bio_lines(tag, p):
    return [
        f"{tag} — biographical entry: {p['name']}"
        + (f", b. {p['birth_year']}" if p.get("birth_year") else ""),
        (f"honours: {', '.join(p['honours'])}" if p.get("honours") else ""),
        (f"appears in editions {p['editions'][0]}-{p['editions'][1]}"
         if p.get("editions") else ""),
        *p["lines"],
        "",
    ]


def _dmy(d, m, y):
    return ".".join(str(x) for x in (d, m) if x) + (f".{y}" if y else "")


def render_exit(pair):
    ev = pair["exit"]
    lines = [
        f"RECORD 1 — casualty-table {ev['event']} notice: {ev['name']}",
        f"date: {_dmy(ev.get('day'), ev.get('month'), ev.get('year'))}",
        f"place: {ev['place']}" if ev.get("place") else "",
        f"establishment: {ev['establishment']}"
        if ev.get("establishment") else "",
        "",
        *_bio_lines("RECORD 2", pair["person"]),
        "Same person?",
    ]
    return "\n".join(l for l in lines if l != "")


def render_roll(pair):
    r = pair["roll"]
    lines = [
        f"RECORD 1 — {r['grade']} roll entry: {r['name']}",
        "appointed: "
        f"{_dmy(r.get('roll_day'), r.get('roll_month'), r['roll_year'])}",
        "",
        *_bio_lines("RECORD 2", pair["person"]),
        f"RECORD 2 prints the same grade ({r['grade']}) dated "
        f"{r['bio_year']} — {abs(r['bio_year'] - r['roll_year'])} years "
        "from the roll date.",
        "Same person?",
    ]
    return "\n".join(l for l in lines if l != "")


def render_birth(row):
    lines = [
        *_bio_lines("RECORD", row["person"]),
        f"Printed birth year: {row['current_birth']} — impossible "
        f"({row.get('anomaly') or 'entry/last age out of range'}).",
        "Candidate OCR repairs: "
        + ", ".join(str(y) for y in row["candidates"]),
        "Which repair (if any) makes the career plausible?",
    ]
    return "\n".join(l for l in lines if l != "")


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


def valid_verdict(out, mode="link"):
    if not isinstance(out, dict):
        return None
    v = out.get("verdict")
    allowed = ("repair", "unsure") if mode == "iolbirth" \
        else ("same", "different", "unsure", "confirm", "reject")
    if v not in allowed:
        return None
    conf = out.get("confidence")
    if not isinstance(conf, (int, float)) or not 0 <= conf <= 100:
        conf = None
    res = {"verdict": v, "confidence": conf,
           "evidence": str(out.get("evidence") or "")[:300],
           "reason": str(out.get("reason") or "")[:250]}
    if mode == "iolbirth":
        by = out.get("birth_year")
        res["birth_year"] = by if isinstance(by, int) else None
        if v == "repair" and res["birth_year"] is None:
            return None
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--worklist", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--url", default="http://localhost:8000/v1")
    ap.add_argument("--model", default="qwen3-30b-a3b")
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--skeptic", action="store_true")
    ap.add_argument("--mode", choices=["link", "merge", "ioldedup",
                                       "iolexit", "iolroll", "iolbirth",
                                       "iolnobio", "iolabc",
                                       "iolchain"],
                    default="link")
    args = ap.parse_args()
    system = {"ioldedup": IOL_MERGE_SYSTEM, "merge": MERGE_SYSTEM,
              "iolexit": IOL_EXIT_SYSTEM, "iolroll": IOL_ROLL_SYSTEM,
              "iolbirth": IOL_BIRTH_SYSTEM,
              "iolnobio": IOL_NOBIO_SYSTEM,
              "iolabc": IOL_ABC_SYSTEM,
              "iolchain": IOL_CHAIN_SYSTEM}.get(
        args.mode, SKEPTIC_SYSTEM if args.skeptic else SYSTEM)

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
    from collections import Counter
    stats = Counter()

    renderer = {"merge": render_merge, "ioldedup": render_merge,
                "iolexit": render_exit, "iolroll": render_roll,
                "iolbirth": render_birth,
                "iolnobio": render_nobio,
                "iolchain": render_chain}.get(args.mode, render)

    def one(b):
        base = {"id": b["id"]}
        for k in ("career_id", "person_id", "person_a", "person_b",
                  "stratum", "evidence_class", "cand_rank", "event_id",
                  "pool", "edge_type"):
            if k in b:
                base[k] = b[k]
        for attempt in (1, 2):
            try:
                v = valid_verdict(extract_json(
                    chat(args.url, args.model, system, renderer(b))),
                    args.mode)
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
