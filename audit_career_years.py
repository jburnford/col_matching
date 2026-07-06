#!/usr/bin/env python3
"""Cross-edition career-event YEAR audit (CO corpus), v3 — earliest-mention-wins.

Votes come from ALL rules-parsed attestation bios of a spine person (including
the anchor's own edition), aligned to each spine event by order-preserving DP
on position-text similarity, with hard compatibility filters:
  - place compat (prefix tokens: "Br. Guiana" ~ "British Guiana"); if the
    mention has no place of its own, the anchor place must appear in the span
  - grade/modifier token equality on the position fields (Class IB != III,
    cls IV != V, asst != deputy, ag./acting != substantive)
  - events the spine marks is_acting are skipped outright (acting stints recur)

Zero-FP gates (ya = spine year, e0/y0 = earliest mentioning edition + its year):
  1. |y0 - ya| >= 2       (±1 = appointed-vs-assumed-office noise)
  2. fresh: 0 <= e0 - y0 <= 3   (first report soon after the claimed year)
  3. no timely corroboration of ya: no mention prints ya in editions [ya, ya+3]
  4. positive disproof of ya, one of:
     A. ya < y0 and >=2 parsed bios in editions (ya+1, e0) LACK the event
        (if ya were real, those bios would print it)
     B. ya > e0 with >=2 unanimous mentions of y0 (the event was already in
        print before ya — ya is an impossible-future year)
"""
import json, glob, re, sys
from collections import defaultdict, Counter
from rapidfuzz import fuzz

BIOS_GLOB = "data/kg/bios/col*.jsonl"
SPINE = "data/kg/llm_struct_corpus.stage3.jsonl"
SIM_THRESH = 80.0
MIN_DELTA = 2
FRESH = 3
CORROB = 3

DIGITS = re.compile(r"\d+")
NONWORD = re.compile(r"[^a-z ]+")
NONALNUM = re.compile(r"[^a-z0-9 ]+")
GRADE = re.compile(r"[ivx]{1,4}[abc]?|\d{1,2}[a-z]?|[a-z]?\d{1,2}")
ORDINAL = re.compile(r"(\d+)(?:st|nd|rd|th)$")
MODS = {"asst": "assistant", "assistant": "assistant", "dep": "deputy",
        "depy": "deputy", "deputy": "deputy", "sen": "senior", "senr": "senior",
        "snr": "senior", "senior": "senior", "jun": "junior", "jnr": "junior",
        "junior": "junior", "ag": "acting", "actg": "acting", "acting": "acting",
        "vice": "vice", "principal": "principal", "chief": "chief", "ch": "chief",
        "gen": "general", "genl": "general", "general": "general",
        "dir": "director", "director": "director",
        "first": "1", "second": "2", "third": "3"}
ACTING_POS = re.compile(r"\bo\.? ?a\.? ?g\b|administ", re.I)
WAR_GAP = range(1939, 1947)   # no Lists 1941-46; silence reasoning invalid

def norm_pos(s):
    if not s: return ""
    s = DIGITS.sub(" ", s.lower())
    s = NONWORD.sub(" ", s)
    return " ".join(s.split())

def guard_tokens(pos):
    """(grade token multiset, modifier set) from a position string."""
    toks = NONALNUM.sub(" ", (pos or "").lower()).split()
    grades, mods = [], set()
    for t in toks:
        m = ORDINAL.fullmatch(t)
        if m: t = m.group(1)
        if len(t) == 4 and t.isdigit(): continue   # a year, not a grade
        if t in MODS: mods.add(MODS[t]); continue
        if GRADE.fullmatch(t): grades.append(t)
    return tuple(sorted(grades)), frozenset(mods)

def place_tokens(s):
    if not s: return None
    toks = NONWORD.sub(" ", s.lower()).split()
    return toks or None

def place_compat(a, b):
    if a is None or b is None: return True
    if len(a) > len(b): a, b = b, a
    if len(a) != len(b):
        return all(x.startswith(y) or y.startswith(x) for x, y in zip(a, b))
    return all(x.startswith(y) or y.startswith(x) for x, y in zip(a, b))

def place_in_span(ptoks, span):
    stoks = NONWORD.sub(" ", span.lower()).split()
    return all(any(s.startswith(p) or p.startswith(s) for s in stoks) for p in ptoks)

def align(a_events, b_events):
    n, m = len(a_events), len(b_events)
    if not n or not m: return []
    sim = [[0.0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if place_compat(a_events[i][1], b_events[j][1]):
                sim[i][j] = fuzz.ratio(a_events[i][0], b_events[j][0])
    dp = [[0.0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            s = sim[i-1][j-1]
            match = dp[i-1][j-1] + (s if s >= SIM_THRESH else 0.0)
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], match)
    pairs = []
    i, j = n, m
    while i > 0 and j > 0:
        s = sim[i-1][j-1]
        if dp[i][j] == dp[i-1][j-1] + (s if s >= SIM_THRESH else 0.0) and s >= SIM_THRESH:
            pairs.append((i-1, j-1, s)); i -= 1; j -= 1
        elif dp[i][j] == dp[i-1][j]: i -= 1
        else: j -= 1
    return pairs[::-1]

def main():
    bio_events, bio_edition = {}, {}
    for f in sorted(glob.glob(BIOS_GLOB)):
        for l in open(f):
            r = json.loads(l)
            evs = r.get("events") or []
            if not evs: continue
            bio_events[r["bio_id"]] = [
                (norm_pos(e.get("position")), place_tokens(e.get("place")),
                 e.get("year_start"), e.get("year_end"),
                 e.get("text_span") or e.get("position") or "",
                 guard_tokens(e.get("position")))
                for e in evs]
            bio_edition[r["bio_id"]] = r["edition_year"]
    sys.stderr.write(f"bios with events: {len(bio_events)}\n")

    n_persons = 0
    ev_total = ev_with_year = ev_matched = ev_disagree = ev_disagree2 = 0
    persons_disagree = set()
    candidates = []
    reject = Counter()

    for l in open(SPINE):
        p = json.loads(l)
        n_persons += 1
        events = p.get("events") or []
        atts = [a for a in p.get("attestations") or [] if a in bio_events]
        if not events: continue
        ev_total += len(events)
        if not atts: continue

        a_list = [(norm_pos(e.get("position")), place_tokens(e.get("place")),
                   e.get("year_start"), e.get("year_end"), e.get("position") or "",
                   guard_tokens(e.get("position")))
                  for e in events]
        mentions = defaultdict(list)   # i -> [(edition, ys, ye, span, sim)]
        for b in atts:
            b_list = bio_events[b]
            for i, j, s in align(a_list, b_list):
                npos, pl, ys, ye, span, gt = b_list[j]
                a_npos, a_pl, _, _, _, a_gt = a_list[i]
                if gt != a_gt:
                    continue                       # grade/modifier mismatch
                if a_pl is not None and pl is None and not place_in_span(a_pl, span):
                    continue                       # anchor place absent from span
                mentions[i].append((bio_edition[b], ys, ye, span, s))
        parsed_eds = sorted({bio_edition[a] for a in atts})

        for i, e in enumerate(events):
            ya = e.get("year_start")
            if ya is None: continue
            ev_with_year += 1
            if e.get("is_acting"): continue        # acting stints recur — unsafe
            if ACTING_POS.search(e.get("position") or ""): continue  # O.A.G. etc.
            if ya in WAR_GAP: continue             # no wartime editions — silence invalid
            ms = sorted((m for m in mentions.get(i, []) if m[1] is not None),
                        key=lambda m: m[0])
            if not ms: continue
            ev_matched += 1
            years = {m[1] for m in ms}
            if years == {ya}: continue
            ev_disagree += 1
            persons_disagree.add(p["person_id"])
            if all(abs(y - ya) < MIN_DELTA for y in years if y != ya): continue
            ev_disagree2 += 1

            e0, y0 = ms[0][0], ms[0][1]
            if y0 == ya or abs(y0 - ya) < MIN_DELTA:
                reject["earliest_agrees_or_close"] += 1; continue
            if not (0 <= e0 - y0 <= FRESH):
                reject["y0_not_fresh"] += 1; continue
            if any(m[1] == ya and ya <= m[0] <= ya + CORROB for m in ms):
                reject["ya_timely_corroborated"] += 1; continue
            gate = None
            if ya < y0:
                ment_eds = {m[0] for m in ms}
                silent = [ed for ed in parsed_eds
                          if ya + 1 < ed < e0 and ed not in ment_eds]
                if len(silent) >= 2:
                    gate = "A:anachronistic_silence"
                else:
                    reject["A:not_enough_silence"] += 1
            elif ya > e0:
                y0_mentions = [m for m in ms if m[1] == y0]
                if len(y0_mentions) >= 2 and years == {ya, y0}:
                    gate = "B:impossible_future"
                else:
                    reject["B:thin_or_mixed"] += 1
            else:
                reject["direction_inconclusive"] += 1
            if gate:
                ya_prints = [m for m in ms if m[1] == ya]
                y0_prints = [m for m in ms if m[1] == y0]
                if not ya_prints and len(y0_prints) >= 3 and years == {y0}:
                    tier = "T1:unanimous_override"
                elif (ya_prints and min(m[0] for m in ya_prints) >= ya + 5
                      and all(m[2] is None for m in ya_prints)):
                    tier = "T2:printed_variant_late"
                else:
                    tier = "review"
                candidates.append({
                    "person_id": p["person_id"],
                    "surname": p.get("surname"), "given_names": p.get("given_names"),
                    "event_seq": i,
                    "position": e.get("position"), "place": e.get("place"),
                    "spine_year_start": ya, "spine_year_end": e.get("year_end"),
                    "proposed_year_start": y0,
                    "first_mention_edition": e0,
                    "gate": gate, "tier": tier,
                    "evidence": [{"edition": m[0], "year_start": m[1], "year_end": m[2],
                                  "span": m[3], "sim": round(m[4], 1)} for m in ms],
                })

    print(json.dumps({
        "persons": n_persons,
        "anchor_events": ev_total, "anchor_events_with_year": ev_with_year,
        "events_with_cross_edition_year_mention": ev_matched,
        "events_with_year_disagreement": ev_disagree,
        "events_with_disagreement_ge2": ev_disagree2,
        "persons_with_disagreement": len(persons_disagree),
        "gate_rejections": dict(reject),
        "gated_candidates": len(candidates),
        "by_gate": dict(Counter(c["gate"] for c in candidates)),
        "by_tier": dict(Counter(c["tier"] for c in candidates)),
    }, indent=1))
    out = "data/kg/year_disagreement_candidates.jsonl"
    with open(out, "w") as f:
        for c in candidates:
            f.write(json.dumps(c) + "\n")
    sys.stderr.write(f"wrote {len(candidates)} candidates -> {out}\n")

if __name__ == "__main__":
    main()
