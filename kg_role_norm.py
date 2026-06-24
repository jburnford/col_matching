#!/usr/bin/env python3
"""Shared parser for career-event positions -> (base ROLE, modifiers, category).

Jim's model: ground the JOB TYPE (judge, surveyor, district officer, ...) to a
Wikidata occupation/position QID where one matches, internal colkg: otherwise.
Seniority/status qualifiers (acting, assistant, deputy, senior, grade I) are NOT
separate roles -- they are stripped to expose the base role and recorded as edge
attributes by the emit. Distinctive role-words (chief, colonial, principal,
provincial, resident, puisne) are KEPT -- "chief justice" / "colonial secretary"
are roles, not "justice"/"secretary" + a modifier.

Used by kg_position_worklist.py (grounding triage) and kg_emit_roles.py (emit), so
both see identical base roles.
"""
from __future__ import annotations
import re

# leading status/seniority qualifiers -> recorded as modifiers, stripped from role
MODS = [
    ("acting",       r"acting|actg|ag|officiating|offg|offcg"),
    ("assistant",    r"assistant|asst|assist|asst"),
    ("deputy",       r"deputy|dy|dep"),
    ("senior",       r"senior|snr|sr|sen"),
    ("junior",       r"junior|jnr|jr|jun"),
    ("additional",   r"additional|addl|addtl"),
    ("temporary",    r"temporary|temp"),
    ("probationary", r"probationary|prob"),
]
GRADE = (r"grade\s*[ivx0-9]+|gr\.?\s*[ivx0-9]+|class\s*[ivx0-9]+|"
         r"[12](?:st|nd|rd)?\s*class|[12](?:st|nd)?\s*grade|first\s*class|second\s*class")

# token-level abbreviation expansion (applied before modifier stripping)
ABBR_TOK = {
    "asst": "assistant", "assit": "assistant", "dy": "deputy", "snr": "senior",
    "jnr": "junior", "actg": "acting", "ag": "acting", "offg": "officiating",
    "supt": "superintendent", "supdt": "superintendent", "supt.": "superintendent",
    "dist": "district", "distr": "district", "comm": "commissioner",
    "commr": "commissioner", "commn": "commissioner", "sec": "secretary",
    "secy": "secretary", "gen": "general", "genl": "general", "govt": "government",
    "dir": "director", "engr": "engineer", "engin": "engineer", "mag": "magistrate",
    "magte": "magistrate", "off": "officer", "offr": "officer", "offcr": "officer",
    "agric": "agriculture", "agl": "agriculture", "med": "medical",
    "res": "resident", "prov": "provincial", "supdt.": "superintendent",
    "supt's": "superintendent", "inspr": "inspector", "insp": "inspector",
    "supr": "superintendent", "atty": "attorney", "treas": "treasurer",
    "acct": "accountant", "acctt": "accountant", "auditr": "auditor",
}
# whole-string expansions (initialisms that token-expansion can't reach)
ABBR_FULL = {
    "mo": "medical officer", "m.o": "medical officer", "do": "district officer",
    "d.o": "district officer", "dc": "district commissioner",
    "d.c": "district commissioner", "ado": "assistant district officer",
    "adc": "assistant district commissioner", "jp": "justice of the peace",
    "j.p": "justice of the peace", "mlc": "member of legislative council",
    "mec": "member of executive council", "dpw": "director of public works",
    "pmo": "principal medical officer", "ag": "acting", "capt": "captain",
    "lieut": "lieutenant", "lt": "lieutenant", "col": "colonel", "maj": "major",
    "sgt": "sergeant", "cpl": "corporal", "cmg": "_honour", "kcmg": "_honour",
}

# bare residual qualifiers that mean the role itself wasn't captured -> unknown
RESIDUAL = {"senior", "junior", "assistant", "acting", "deputy", "additional",
            "temporary", "probationary", "officiating", "chief", "principal",
            "first", "second", "grade", "class", "officer", "member", ""}

CATEGORY = [
    ("judicial",  r"judge|justice|magistrate|attorney|solicitor|barrister|advocate|registrar|crown counsel|law"),
    ("administrative", r"governor|commissioner|secretary|cadet|district officer|government agent|administrat|resident|councillor|council|under-secretary|colonial"),
    ("police",    r"police|constab|inspector|superintendent of police|detective"),
    ("military",  r"military|captain|lieutenant|colonel|major|general|sergeant|corporal|brigad|regiment|army|navy|soldier"),
    ("medical",   r"medical|physician|surgeon|doctor|sanitary|health|nursing|nurse|dental"),
    ("technical", r"engineer|surveyor|survey|architect|geolog|chemist|scientific|technical|works|conservator|forest"),
    ("financial", r"treasurer|accountant|auditor|collector|customs|revenue|financial|currency"),
    ("education", r"teacher|professor|principal|headmaster|education|tutor|lecturer|inspector of schools"),
    ("clerical",  r"clerk|typist|stenographer|cashier|storekeeper"),
    ("religious", r"chaplain|bishop|priest|minister of religion|missionary"),
]

def _expand_tokens(s: str) -> str:
    return " ".join(ABBR_TOK.get(t, t) for t in s.split())

def parse_position(raw: str):
    """Return (base_role, sorted_modifiers, category). base_role is '_unknown'
    for empty/garbage or bare-qualifier extractions; '_military_service' for
    'on military service'; '_honour' for stray honour tokens."""
    if not raw:
        return "_unknown", [], "unknown"
    s = raw.strip().lower().rstrip(".,; ")
    s = re.sub(r"\s+", " ", s)
    if re.fullmatch(r"(on )?military service.*", s):
        return "_military_service", [], "military"
    s = ABBR_FULL.get(s.rstrip("."), s)
    s = _expand_tokens(s)

    # strip appointment-connector junk that leaked into position_norm
    # ("to attorney general", "and district officer", "as governor")
    s = re.sub(r"^(?:to|and|for|as|of|the)\b[\s,.]*", "", s).strip(" ,.")
    s = re.sub(r"\b(?:to|a|an)$", "", s).strip(" ,.")
    # collapse a doubled role ("district officer and district officer")
    m = re.fullmatch(r"(.+?) and \1", s)
    if m:
        s = m.group(1)

    mods = set()
    changed = True
    while changed:
        changed = False
        for name, pat in MODS:
            m = re.match(rf"(?:{pat})\b[\s,.]*", s)
            if m:
                mods.add(name); s = s[m.end():].strip(" ,."); changed = True
        g = re.match(rf"(?:{GRADE})\b[\s,.]*", s, re.I)
        if g:
            mods.add("graded"); s = s[g.end():].strip(" ,."); changed = True

    base = s.strip(" ,.")
    if base in RESIDUAL or len(base) < 3:
        return "_unknown", sorted(mods), "unknown"
    cat = "other"
    for name, pat in CATEGORY:
        if re.search(pat, base):
            cat = name; break
    return base, sorted(mods), cat

if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        print(parse_position(line.rstrip("\n")))
