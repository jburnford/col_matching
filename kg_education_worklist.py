#!/usr/bin/env python3
"""Parse the free-text education field into institution mentions and build a
grounding worklist (parallel to the place worklist).

Education strings mix institutions (schools, university colleges, academies,
Inns of Court) with bare qualifications (B.A., LL.B., called to the bar). We
extract the institutions, bind ambiguous college names to their parent
university ("Magdalen college, Oxford" -> Magdalen College, Oxford), normalise
abbreviations, classify by type, and aggregate distinct institutions with their
person_ids -> data/kg/education_worklist.jsonl.

  python3 kg_education_worklist.py
"""
from __future__ import annotations
import json, re
from collections import defaultdict, Counter

ABBR = [
    (r"\bed\.\s*", " "), (r"\beduc(?:ated)?\b\.?", " "), (r"\bpassed into\b", " "),
    (r"\bcoll?\.", "college"), (r"\bschl?\.", "school"), (r"\bsch\.", "school"),
    (r"\bunivs?\.", "university"), (r"\bacad\.", "academy"), (r"\bgram\.", "grammar"),
    (r"\binst\.", "institute"), (r"\bgr\.\s*school", "grammar school"),
    (r"\bC\.\s*of\s*E\.", "Church of England"),
    (r"\bR\.\s*M\.\s*Academy", "Royal Military Academy"),
    (r"\bR\.\s*M\.\s*C\.?", "Royal Military College"),
    (r"\bR\.\s*N\.\s*College", "Royal Naval College"),
    (r"\bTrin\.", "Trinity"), (r"\bMagd\.", "Magdalen"), (r"\bPemb\.", "Pembroke"),
    (r"\bChrist['’]?s\b", "Christ's"), (r"\bSt\.?\s", "St. "),
    (r"\bOxon\.?\b", "Oxford"), (r"\bCantab\.?\b", "Cambridge"), (r"\bCamb\.", "Cambridge"),
    (r"\bEdin\.", "Edinburgh"), (r"\bGlas\.", "Glasgow"), (r"\bLond\.", "London"),
    (r"\bDubl?\.", "Dublin"), (r"\bAberd\.", "Aberdeen"),
]
PARENT = (r"Oxford|Cambridge|Dublin|London|Durham|Wales|Glasgow|Edinburgh|Aberdeen|"
          r"St\.? Andrews|Manchester|Birmingham|Leeds|Liverpool|Bristol|Belfast|Toronto|"
          r"McGill|Cape Town|Sydney|Melbourne|New Zealand|Calcutta|Madras|Bombay")
MILITARY = {"sandhurst": "Royal Military College, Sandhurst",
            "woolwich": "Royal Military Academy, Woolwich",
            "royal military academy": "Royal Military Academy, Woolwich",
            "royal military college": "Royal Military College, Sandhurst",
            "royal naval college": "Royal Naval College", "osborne": "Royal Naval College, Osborne",
            "dartmouth": "Britannia Royal Naval College, Dartmouth"}
INNS = {"inner temple": "Inner Temple", "middle temple": "Middle Temple",
        "lincoln's inn": "Lincoln's Inn", "gray's inn": "Gray's Inn"}
# A name is a run of Capitalised words. It may begin with one of a few fixed
# prefixes that legitimately take a lowercase "of" joiner ("City of London",
# "Prince of Wales", "Isle of Wight", "Duke of York's", "West of Scotland") —
# whitelisted so we capture those whole instead of truncating to the word before
# the keyword, WITHOUT swallowing a genitive "of" ("Fellow of X", "scholar of X").
_OFPFX = r"(?:City|Prince|Isle|Duke|Church|West|East|North|South|Our Lady)"
NAME = rf"(?:{_OFPFX}\s+of\s+)?[A-Z][\w'’.&-]*(?:\s+[A-Z][\w'’.&-]*){{0,3}}"

# famous schools written BARE (no "school/college" keyword) -> canonical name.
# keyed by lowercase head token(s); value is the canonical institution label.
FAMOUS = {
    "eton": "Eton College", "harrow": "Harrow School", "rugby": "Rugby School",
    "winchester": "Winchester College", "marlborough": "Marlborough College",
    "charterhouse": "Charterhouse", "cheltenham": "Cheltenham College",
    "clifton": "Clifton College", "dulwich": "Dulwich College",
    "wellington": "Wellington College", "haileybury": "Haileybury College",
    "sherborne": "Sherborne School", "repton": "Repton School",
    "shrewsbury": "Shrewsbury School", "westminster": "Westminster School",
    "tonbridge": "Tonbridge School", "uppingham": "Uppingham School",
    "malvern": "Malvern College", "radley": "Radley College",
    "lancing": "Lancing College", "bradfield": "Bradfield College",
    "stonyhurst": "Stonyhurst College", "downside": "Downside School",
    "fettes": "Fettes College", "loretto": "Loretto School",
    "sedbergh": "Sedbergh School", "oundle": "Oundle School",
    "blundell's": "Blundell's School", "epsom": "Epsom College",
    "brighton": "Brighton College", "whitgift": "Whitgift School",
    "rossall": "Rossall School", "bedford grammar": "Bedford School",
    "wellingborough": "Wellingborough School", "felsted": "Felsted School",
    "berkhamsted": "Berkhamsted School", "monkton combe": "Monkton Combe School",
}
_FAMOUS_RE = re.compile(r"\b(" + "|".join(re.escape(k) for k in FAMOUS) + r")\b", re.I)
_DEGREE = re.compile(r"^\s*(?:B\.?A|M\.?A|LL\.?[BDM]|M\.?[BD]|B\.?Sc|D\.?Sc|K\.?C|"
                     r"Ph\.?D|F\.?R\.?C\.?[SP]|M\.?R\.?C\.?[SP]|D\.?P\.?H|B\.?Ch)\.?\b[\s,;]*", re.I)
APOS = [(r"\bKings\b", "King's"), (r"\bQueens'?\b", "Queen's"), (r"\bChrists\b", "Christ's"),
        (r"\bSt\.?\s+", "St. "), (r"\bColl\b", "College")]

def canon_label(s):
    for pat, rep in APOS: s = re.sub(pat, rep, s)
    return re.sub(r"\s+", " ", s).strip(" ,.;")

def clean(s):
    s = _DEGREE.sub("", s)
    for pat, rep in ABBR: s = re.sub(pat, rep, s, flags=re.I)
    return re.sub(r"\s+", " ", s).strip(" ;,.")

def titlecase(s):
    return re.sub(r"\s+", " ", s).strip()

def extract(raw):
    """Return list of (canonical_institution, type)."""
    s = clean(raw); found = []
    # 0) famous schools written bare (no keyword)
    for m in _FAMOUS_RE.finditer(s):
        found.append((FAMOUS[m.group(1).lower()], "school"))
    # 1) university college bound to parent: "<Name> college, <Parent>"
    for m in re.finditer(rf"({NAME})\s+college\s*,?\s+(?:and\s+of\s+)?({PARENT})", s):
        found.append((f"{titlecase(m.group(1))} College, {m.group(2)}", "university_college"))
    # 2) standalone university: "<Parent> university" / "university of <Parent>"
    for m in re.finditer(rf"({PARENT})\s+university|university of ({PARENT})", s):
        p = m.group(1) or m.group(2)
        found.append((f"University of {p}", "university"))
    # 3) Inns of Court
    for k, v in INNS.items():
        if k in s.lower(): found.append((v, "inn_of_court"))
    # 4) military / naval academies
    for k, v in MILITARY.items():
        if k in s.lower(): found.append((v, "military_academy"))
    # 5) schools / standalone colleges (college NOT followed by a parent university),
    #    capturing a trailing "of <X>" (Royal College of Surgeons, London School of
    #    Economics, School of Mines) so we don't ground a truncated stub.
    OFTAIL = r"(?:\s+of\s+[A-Z][\w'’.&-]*(?:\s+(?:and\s+)?[A-Z][\w'’.&-]*){0,3})?"
    for m in re.finditer(rf"({NAME})\s+(grammar school|high school|school|college|academy)({OFTAIL})", s):
        nm, kind, oft = m.group(1), m.group(2).lower(), (m.group(3) or "").strip()
        if kind == "college" and not oft:
            tail = s[m.end():m.end()+18]
            if re.match(rf"\s*,?\s+(?:{PARENT})", tail):
                continue  # already captured as university_college
        if nm.lower() in ("grammar", "high", "public", "the"):
            continue
        base = "College" if kind == "college" else ("Academy" if kind == "academy" else "School")
        label = f"{titlecase(nm)} {base}" + (f" {oft}" if oft else "")
        typ = "professional" if oft and ("surgeon" in oft.lower() or "physician" in oft.lower()
                                         or "economic" in oft.lower() or "medicine" in oft.lower()
                                         or "mines" in oft.lower()) else "school"
        found.append((re.sub(r"\s+", " ", label), typ))
    # canonicalise labels (King's/Kings, Coll->College) + dedupe within a record
    found = [(canon_label(lbl), typ) for lbl, typ in found]
    return list(dict.fromkeys(found))

rows = [json.loads(l) for l in open("data/kg/graph_stage3/education.jsonl")]
inst_persons = defaultdict(set); inst_type = {}; inst_examples = defaultdict(list)
parsed = 0
for r in rows:
    ins = extract(r["education"])
    if ins: parsed += 1
    for label, typ in ins:
        inst_persons[label].add(r["person_id"]); inst_type[label] = typ
        if len(inst_examples[label]) < 2: inst_examples[label].append(r["education"][:70])

work = [{"institution": k, "type": inst_type[k], "count": len(v),
         "person_ids": sorted(v)[:50], "examples": inst_examples[k]}
        for k, v in inst_persons.items()]
work.sort(key=lambda w: -w["count"])
with open("data/kg/education_worklist.jsonl", "w") as fh:
    for w in work: fh.write(json.dumps(w, ensure_ascii=False) + "\n")

tc = Counter(w["type"] for w in work)
mentions = sum(w["count"] for w in work)
print(f"education rows: {len(rows):,} | rows yielding >=1 institution: {parsed:,} ({100*parsed/len(rows):.0f}%)")
print(f"distinct institutions: {len(work):,} | total mentions: {mentions:,}")
print("by type:", dict(tc))
covered = sum(w["count"] for w in work[:200])
print(f"top 200 institutions cover {covered:,} mentions ({100*covered/mentions:.0f}% of all mentions)\n")
print("TOP 30 institutions:")
for w in work[:30]:
    print(f"  {w['count']:5d}  {w['type']:<18} {w['institution']}")
print("\nwrote -> data/kg/education_worklist.jsonl")
