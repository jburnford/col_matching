#!/usr/bin/env python3
"""Shared parser for honour/award strings -> (base HONOUR, modifiers, category).

Jim's model (same as the role layer): ground the HONOUR TYPE to a Wikidata
QID where one matches (e.g. `C.M.G.` -> *Companion of the Order of St Michael
and St George*; `M.C.` -> *Military Cross*), mint a stable internal id
`colkg:<honour>` where Wikidata has no matching decoration.  British orders are
graded -- CMG / KCMG / GCMG are three distinct grades with three distinct QIDs,
so the post-nominal IS the grounding key; grades are NOT collapsed.

Branch qualifiers like "(mil.)" / "(civil)" ride on the EDGE as modifiers, not
the node (so "M.B.E." and "M.B.E. (mil.)" share one node).  Clasp / bar / "with
clasp" decoration noise is stripped.  Pure-noise extractions (bare "medal",
"board", "clasp") fall to the `_unknown` control bucket and are not grounded.

Used by kg_honour_worklist.py (grounding triage) and kg_emit_honours.py (emit),
so both see identical base honours.
"""
from __future__ import annotations
import re

# parenthetical / trailing branch qualifiers -> recorded as modifiers
MODS = [
    ("military", r"mil\.?|military"),
    ("civil",    r"civ\.?|civil"),
]
# decoration-noise tokens stripped from the tail of a post-nominal
CLASP = r"\b(?:with\s+)?(?:and\s+)?(?:clasp|clasps|bar|bars)\b"

# whole-string folds: obvious surface variants -> one canonical key.
# Kept deliberately small; grade-level disambiguation is a GROUNDING decision.
WHOLE = {
    "knt": "knight bachelor", "kt": "knight bachelor", "knight": "knight bachelor",
    "kt bach": "knight bachelor", "knight bach": "knight bachelor",
    "kcb": "kcb", "cb": "cb",            # passthroughs (kept for clarity)
}
# pure-noise / non-honour extractions -> _unknown control bucket
NOISE = {
    "", "board", "medal", "medals", "clasp", "clasps", "bar", "bars",
    "medal and clasp", "medal and bar", "decoration", "decorations",
    "and", "the", "of", "with clasp", "with bar", "etc",
}


def _strip_dots(s: str) -> str:
    """Join single-letter acronym tokens: 'c.m.g' / 'c m g' -> 'cmg'.
    Leave multi-word phrases ('knight bachelor') intact."""
    s = s.replace(".", " ")
    toks = s.split()
    if toks and all(len(t) == 1 for t in toks):
        return "".join(toks)
    return " ".join(toks)


# ---- layer classification: degrees + professional memberships vs true honours ----
# Academic degrees. NB the normalizer keeps multi-letter tokens ("d sc", "b sc",
# "ll d", "ch b") so these stay DISTINCT from same-letter decoration acronyms that
# join ("dsc" = Distinguished Service Cross, "mm" = Military Medal) -- those are NOT
# degrees and must stay in the honour layer.
DEGREE = {
    "ma", "ba", "bsc", "b sc", "msc", "m sc", "d sc", "ll d", "lld", "ll b", "llb",
    "ll m", "llm", "dd", "dcl", "md", "mb", "ph d", "phd", "d phil", "dphil", "bs",
    "ch b", "b ch", "b com", "bcom", "m com", "mcom", "b litt", "blitt", "m litt",
    "mlitt", "b v sc", "bvsc", "d litt", "dlitt", "litt d", "bd", "std", "mus b",
    "musb", "mus d", "musd", "b ed", "bed", "m ed", "b phil", "bphil", "m phil",
    "mphil", "b sc agric", "b agr", "b a", "m a", "d d", "b d", "m d", "m b",
}
# Professional / learned-society qualifications (Fellow/Member/Licentiate/Associate
# of a Royal College, Institution, or Society). Multi-word decoration phrases
# ("french croix de guerre", "mily cross") are NOT here -- they are true honours.
MEMBERSHIP = {
    "frgs", "fgs", "fzs", "frs", "fras", "frsa", "frai", "fsa", "fcs", "fic",
    "fres", "frsc", "frse", "frss", "frms", "frhs", "fgsa", "friba", "lriba",
    "frics", "fric", "fiac", "fia", "fcis", "aca", "acis", "mras", "mrsi", "mrst",
    "mims", "mim", "mina", "amina", "frfps", "lrfps", "lrfp&s",
}
_RC = re.compile(r"^a?[fml]rc[a-z]")          # *Royal College* (frcs/mrcs/lrcp/frcp/frcog)
_MI = re.compile(r"^a?mi[a-z]{2,}$")          # Member of an *Institution* (mice/miee/mirse)

def honour_class(base: str) -> str:
    """Route a base honour to 'degree' | 'membership' | 'honour' so emit can split
    academic/professional qualifications into a separate layer from state honours."""
    if base in DEGREE:
        return "degree"
    if base in MEMBERSHIP:
        return "membership"
    if " " not in base and (_RC.match(base) or _MI.match(base)):
        return "membership"
    return "honour"


def parse_honour(raw: str):
    """Return (base_honour, sorted_modifiers, category).
    base_honour is '_unknown' for empty/noise extractions."""
    if not raw:
        return "_unknown", [], "unknown"
    s = raw.strip().rstrip(".").casefold()
    mods = []
    # peel parenthetical/trailing branch qualifier as a modifier
    for name, pat in MODS:
        m = re.search(r"\(?\b(" + pat + r")\)?\s*$", s)
        if m and m.start() > 0:
            mods.append(name)
            s = s[:m.start()].strip(" ()")
    s = re.sub(r"\(.*?\)", " ", s)            # drop any remaining parentheticals
    s = re.sub(CLASP, " ", s)                  # strip clasp/bar decoration noise
    s = re.sub(r"\s+", " ", s).strip(" .,&-")
    s = _strip_dots(s)
    if s in NOISE or len(s) < 2:
        return "_unknown", sorted(set(mods)), "unknown"
    s = WHOLE.get(s, s)
    cat = "order" if len(s) >= 2 and s.isalpha() and " " not in s else "honour"
    return s, sorted(set(mods)), cat


if __name__ == "__main__":
    for t in ["C.M.G.", "K.C.M.G.", "M.B.E. (mil.)", "Knt", "medal and clasp",
              "board", "knight bachelor", "M.C.", "D.S.O. with clasp", "F.R.G.S."]:
        print(f"{t!r:28} -> {parse_honour(t)}")
