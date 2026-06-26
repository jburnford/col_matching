#!/usr/bin/env python3
"""Verify every institution QID in a grounding cache/batch against live Wikidata.

Institution analogue of verify_place_qids.py. The education/org grounding cache
keys the QID as `id` (Q...) on an `institution` surface; internal fallbacks are
`colkg:<Slug>` (skipped). For each distinct Q-id we fetch instance-of (P31) and
classify:

  OK       - has >=1 P31 that is (a subclass* of) an educational-institution /
             organisation root (university, college, school, military academy,
             institute, association, organisation, agency, Inn of Court, ...)
  NONINST  - resolves with P31 but NONE institutional -> likely a wrong entity
             (a person / building / boat-club / painting / place was grounded)
  STUB     - resolves with no P31 -> statement-less / redirect / deleted = FP risk

Read-only SPARQL (sanctioned lookup of KNOWN ids; the REST ban is about search
disambiguation, not verification). Run on a batch file BEFORE `record`, exactly
as verify_place_qids.py is used for the place loop.

Usage:
  python3 verify_institution_qids.py [cache_or_batch.jsonl]
    # default data/kg/institutions_grounding.jsonl
Outputs:
  data/kg/inst_qid_verification_report.jsonl   # one row per distinct QID
  data/kg/inst_qid_verification_flagged.jsonl  # NONINST + STUB only
"""
import json, sys, time, subprocess, collections

CACHE = sys.argv[1] if len(sys.argv) > 1 else "data/kg/institutions_grounding.jsonl"
REPORT = "data/kg/inst_qid_verification_report.jsonl"
FLAGGED = "data/kg/inst_qid_verification_flagged.jsonl"
WDQS = "https://query.wikidata.org/sparql"
UA = "col_matching-inst-verify/1.0 (cljim22@gmail.com)"

# A P31 type counts as an institution if it is a subclass* of any of these.
INST_ROOTS = [
    "Q2385804",  # educational institution
    "Q3918",     # university
    "Q3914",     # school
    "Q189004",   # college
    "Q38723",    # higher education institution
    "Q4671277",  # academic institution
    "Q1346110",  # military academy
    "Q1664720",  # institute
    "Q1391145",  # gymnasium (school)
    "Q9842",     # primary school
    "Q159334",   # secondary school
    "Q43229",    # organization (catches Inns of Court, societies, agencies, regiments)
    "Q15911314", # association
    "Q327333",   # government agency
    "Q748019",   # seminary
    "Q2385804",  # (dup ok)
]

# Generic education TYPE-classes — a specific institution must never be grounded
# to one of these (Q967098 "grammar school", Q3914 "school", ...). Grounding to a
# class is a type/instance error, flagged separately from NONINST/STUB.
CLASS_QIDS = set(INST_ROOTS) | {
    "Q967098",    # grammar school
    "Q5887603",   # public school (UK)
    "Q1202123",   # red brick university
    "Q1144991",   # ancient university
    "Q210980",    # boarding school
    "Q9842",      # primary school
    "Q159334",    # secondary school
}


def sparql(query):
    out = subprocess.run(
        ["curl", "-s", "-G", WDQS,
         "--data-urlencode", "query=" + query,
         "-H", "Accept: application/sparql-results+json",
         "-H", "User-Agent: " + UA],
        capture_output=True, text=True, timeout=90).stdout
    return json.loads(out)["results"]["bindings"]

def qid(uri):
    return uri.rsplit("/", 1)[-1] if uri else None

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

# --- load cache/batch: Q-id -> [(institution, source), ...] (skip colkg internals) ---
rows = [json.loads(l) for l in open(CACHE)]
qmap = collections.defaultdict(list)
for r in rows:
    qi = r.get("id") or r.get("qid")
    if qi and isinstance(qi, str) and qi.startswith("Q"):
        qmap[qi].append((r.get("institution"), r.get("source") or r.get("match_type")))
qids = sorted(qmap)
print(f"distinct institution QIDs to verify: {len(qids)}", file=sys.stderr)

# --- stage 1: per-item P31 ---
item_p31 = collections.defaultdict(set)
seen = collections.Counter()
for ci, ch in enumerate(chunks(qids, 150)):
    vals = " ".join("wd:" + q for q in ch)
    q = (f"SELECT ?item ?p31 WHERE {{ VALUES ?item {{ {vals} }} "
         f"OPTIONAL {{ ?item wdt:P31 ?p31 }} }}")
    for b in sparql(q):
        it = qid(b["item"]["value"]); seen[it] += 1
        if "p31" in b: item_p31[it].add(qid(b["p31"]["value"]))
    print(f"  stage1 chunk {ci+1}: items seen {len(seen)}", file=sys.stderr)
    time.sleep(1)

# --- stage 2: classify P31 types as institutional or not ---
all_types = sorted({t for s in item_p31.values() for t in s})
type_inst, type_label = {}, {}
for ch in chunks(all_types, 150):
    vals = " ".join("wd:" + t for t in ch)
    roots = " ".join("wd:" + r for r in INST_ROOTS)
    q = (f"SELECT ?type ?typeLabel (BOUND(?g) AS ?isinst) WHERE {{ "
         f"VALUES ?type {{ {vals} }} "
         f"OPTIONAL {{ ?type wdt:P279* ?g. VALUES ?g {{ {roots} }} }} "
         f"SERVICE wikibase:label {{ bd:serviceParam wikibase:language 'en'. }} }}")
    for b in sparql(q):
        t = qid(b["type"]["value"])
        type_inst[t] = type_inst.get(t, False) or (b.get("isinst", {}).get("value") == "true")
        type_label[t] = b.get("typeLabel", {}).get("value", t)
    time.sleep(1)

# --- classify each item ---
report, flagged = [], []
status_ct = collections.Counter()
for q in qids:
    p31s = item_p31.get(q, set())
    if q in CLASS_QIDS:
        status = "CLASS"                      # grounded to a generic type, not an instance
    elif any(type_inst.get(t) for t in p31s):
        status = "OK"
    elif p31s:
        status = "NONINST"
    else:
        status = "STUB"
    status_ct[status] += 1
    insts = sorted({i for i, _ in qmap[q] if i})
    srcs = sorted({s for _, s in qmap[q] if s})
    rec = {"qid": q, "status": status,
           "instance_of": sorted(p31s),
           "instance_of_labels": [type_label.get(t, t) for t in sorted(p31s)],
           "n_surfaces": len(insts), "surfaces": insts[:8], "sources": srcs}
    report.append(rec)
    if status != "OK":
        flagged.append(rec)

with open(REPORT, "w") as f:
    for r in report: f.write(json.dumps(r, ensure_ascii=False) + "\n")
with open(FLAGGED, "w") as f:
    for r in flagged: f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("\n=== institution QID verification summary ===")
print("distinct QIDs:", len(qids), "| by status:", dict(status_ct))
flag_qids = {r["qid"] for r in flagged}
impact = sum(1 for r in rows if (r.get("id") or r.get("qid")) in flag_qids)
print(f"surface rows on flagged QIDs: {impact}")
print(f"report  -> {REPORT}")
print(f"flagged -> {FLAGGED}  ({len(flagged)} QIDs)")
noninst = collections.Counter()
for r in flagged:
    if r["status"] == "NONINST":
        for t, lab in zip(r["instance_of"], r["instance_of_labels"]):
            if not type_inst.get(t): noninst[lab] += 1
if noninst:
    print("non-institution P31 types seen on NONINST items:", dict(noninst))
