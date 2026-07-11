#!/usr/bin/env python3
"""Unified bio-person table: volume bios ↔ existing career KG (stage-3 spine).

The stage-3 spine (data/kg/llm_struct_corpus.stage3.jsonl) already partitions
the per-edition Record-of-Services bios into cross-edition persons — its
attestation IDs are the same col{year}-p{page}b{n} block IDs the volume
pipeline emits (both derive from the layout-aware OCR blocks), and it covers
202,074 of the 202,100 real volume bios. Person identity therefore ADOPTS the
spine partition (keeping kgp_* person_ids stable with graph_stage3 career
facts, honours, groundings) rather than re-clustering from scratch.

What this script adds on top of the spine:
  1. Uniform name re-extraction from raw_text — the 44.6k Qwen-parsed bios
     carry events but no name fields; two header shapes (standard
     "SURNAME, GIVEN.—" and the 1867 honours-first "SURNAME, K.C.B. (…)—SIR
     GIVEN.—") recover 97.8% of them.
  2. Per-person aggregation with cross-edition majority voting (canonical
     surname, fullest compatible given names, birth year with minority
     readings preserved) and a merged event chain deduped on
     (position-stem, year_start).
  3. QA flags judged against the NEW parses: see-reference stubs, verbatim
     duplicate printings (duplicate page scans), true same-edition namesake
     conflicts, birth-year conflicts, surname OCR variants.
  4. Orphan attachment: volume bios absent from the spine join an existing
     person only on (surname block + given-compat + >=2 shared exact
     (posstem, year) appointments or equal birth year); else new singletons.
  5. Under-merge candidates from the new Qwen events: distinct persons in the
     same surname block sharing >=3 exact (posstem, year_start) appointments,
     given-compatible, edition-disjoint, birth-compatible — candidates go to
     a REVIEW file; adjudicated decisions (undermerge_decisions.jsonl) are
     applied at build time, absorbed ids recorded in person_id_merges.jsonl
     so graph_stage3 keys remain resolvable.

Outputs (data/volume/bio_persons/):
  bio_person_map.jsonl        bio_id -> person_id (+role: primary/seeref/
                              dupprint/junk/legacy)
  bio_persons.jsonl           one line per person (canonical names, votes,
                              merged events, member roles, flags)
  undermerge_candidates.jsonl cross-person merge candidates for review
  BIO_PERSONS.md              audit report

Usage: python3 volume_bio_persons.py
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from rapidfuzz import fuzz

from col_match.services.compile import _POS_ABBREV
from col_match.services.match import _initials, _names_compatible

SPINE = Path("data/kg/llm_struct_corpus.stage3.jsonl")
VOLROOT = Path("data/volume")
OUTDIR = VOLROOT / "bio_persons"

MIN_ORPHAN_SHARED = 2
MIN_UNDERMERGE_SHARED = 3
DUPPRINT_RATIO = 90.0

# ---------------------------------------------------------------- name layer

# standard headword: "SURNAME, GIVEN NAMES [titles] [honours].—…"
_TITLE_TOK = re.compile(
    r"^(SIR|DAME|THE|HON(?:BLE)?\.?|REV\.?|DR\.?|MR\.?|MRS\.?|CAPT(?:AIN)?\.?|"
    r"COL\.?|LT\.?[-.]?(?:COL\.?|GEN\.?)?|MAJOR|MAJ\.?[-.]?(?:GEN\.?)?|GEN\.?|"
    r"BRIG\.?|CMDR\.?|COMMANDER|COMMODORE|ADMIRAL|ADM\.?|PROF\.?|RIGHT|MOST|"
    r"VEN\.?|VERY|LORD|LADY|COUNT|BARON)$",
    re.I,
)
_SURNAME_OK = re.compile(r"^[A-Z][A-Za-z'’\- ]+$")
_NAME_TOK = re.compile(r"^[A-Z][A-Za-z'’\-]*\.?$")
_INITIAL_RUN = re.compile(r"^[A-Z]\.[A-Z]")  # honours-ish token: "K.C" "C.M"
_SEEREF = re.compile(r"\(\s*see\s+page", re.I)
# post-nominal letters that occasionally win the surname vote (post-war
# "SURNAME, O.B.E." headers, bishop entries headed by see) — flag, don't fix
_HONORIFIC_SURNAME = re.compile(
    r"^(O\.?B\.?E|M\.?B\.?E|C\.?M\.?G|K\.?C\.?M\.?G|C\.?B\.?E|K\.?B\.?E|"
    r"I\.?S\.?O|C\.?I\.?E|D\.?S\.?O|M\.?C|E\.?D|Q\.?P\.?M|C\.?P\.?M|J\.?P|"
    r"B\.?A|M\.?A|M\.?D|LL\.?[BD])\.?$",
    re.I,
)


def _split_header(raw: str) -> list[str]:
    """Segments of the entry head, split on em-dash / '.-' runs."""
    return re.split(r"\s*(?:[—–]|\.\s*-{1,2})\s*", raw, maxsplit=3)


def _given_from_tokens(rest: str, surname: str | None = None) -> str | None:
    toks: list[str] = []
    for t in re.split(r"[,\s]+", rest.strip()):
        if not t:
            continue
        if _TITLE_TOK.match(t):
            continue
        if _NAME_TOK.match(t) and not _INITIAL_RUN.match(t):
            tt = t.rstrip(".")
            if surname and tt.upper() == surname.upper():
                continue
            toks.append(tt)
        else:
            break
    return " ".join(toks) or None


def header_name(raw: str | None) -> tuple[str | None, str | None]:
    """(surname, given_names) from the printed headword; None,None if no fit."""
    if not raw:
        return None, None
    segs = _split_header(raw)
    head = segs[0]
    if "," not in head:
        return None, None
    sur, rest = head.split(",", 1)
    sur = sur.strip()
    if not _SURNAME_OK.match(sur) or len(sur) > 30:
        return None, None
    given = _given_from_tokens(rest, sur)
    if given:
        return sur, given
    # 1867 honours-first shape: "BARKLY, K.C.B. (Civil. Creat. 1853.)—SIR HENRY BARKLY.—"
    for seg in segs[1:3]:
        seg = seg.strip()
        if not seg or len(seg) > 60:
            continue
        cand = _given_from_tokens(seg, sur)
        # accept only if the whole segment reads as a name (no career verbs)
        if cand and len(cand.split()) >= 1 and re.fullmatch(
            r"(?:(?:SIR|DAME|THE|HON\.?|REV\.?|DR\.?|LORD|LADY)\s+)*[A-Za-z .'’\-]+\.?",
            seg,
        ):
            return sur, cand
    return sur, None


def surname_norm(s: str | None) -> str:
    x = re.sub(r"[^a-z]", "", (s or "").lower())
    return x


def posstem(p: str | None) -> str:
    """Abbreviation-expanded position stem — era drift ('Inspr. of schls.' vs
    'Inspector of schools') must land on one key."""
    toks = [_POS_ABBREV.get(t, t)
            for t in re.sub(r"[^a-z ]", "", (p or "").lower()).split()]
    return "".join(toks)[:12]


def bio_name(r: dict) -> tuple[str | None, str | None, str]:
    """(surname, given, source) — rules fields when sane, else header regex."""
    if r.get("parser") == "rules":
        s = r.get("surname")
        if s and _SURNAME_OK.match(s) and len(s) <= 30:
            return s, r.get("given_names"), "rules"
    s, g = header_name(r.get("raw_text"))
    if s:
        return s, g, "header"
    return None, None, "none"


# ------------------------------------------------------------------- loading

def load_bios() -> dict[str, dict]:
    bios: dict[str, dict] = {}
    for f in sorted(VOLROOT.glob("col*/bios.jsonl")):
        for line in f.open(encoding="utf-8"):
            r = json.loads(line)
            bios[r["bio_id"]] = r
    return bios


def load_spine() -> list[dict]:
    return [json.loads(l) for l in SPINE.open(encoding="utf-8")]


# -------------------------------------------------------------- member roles

def classify_members(atts: list[str], bios: dict[str, dict]) -> dict[str, str]:
    """bio_id -> role. Roles: primary, seeref, dupprint, junk, legacy."""
    roles: dict[str, str] = {}
    by_ed: dict[int, list[str]] = defaultdict(list)
    for a in atts:
        r = bios.get(a)
        if r is None:
            roles[a] = "legacy"          # dol* editions / not in volume corpus
            continue
        if r.get("parser") == "not_a_bio":
            roles[a] = "junk"
            continue
        raw = r.get("raw_text") or ""
        if _SEEREF.search(raw) and len(r.get("events") or []) <= 1 and len(raw) < 120:
            roles[a] = "seeref"
            continue
        roles[a] = "primary"
        by_ed[r["edition_year"]].append(a)
    # verbatim duplicate printings (duplicate page scans): same edition,
    # near-identical text -> keep first block, demote the rest
    for ed, ids in by_ed.items():
        if len(ids) < 2:
            continue
        ids.sort()
        kept = [ids[0]]
        for a in ids[1:]:
            ra = (bios[a].get("raw_text") or "")[:600]
            if any(
                fuzz.ratio(ra, (bios[k].get("raw_text") or "")[:600]) >= DUPPRINT_RATIO
                for k in kept
            ):
                roles[a] = "dupprint"
            else:
                kept.append(a)
    return roles


# ------------------------------------------------------------- person build

def event_key(ev: dict) -> tuple[str, int] | None:
    ys = ev.get("year_start")
    stem = posstem(ev.get("position"))
    if ys is None or not stem:
        return None
    return stem, ys


def build_person(pid: str, spine_p: dict, atts: list[str],
                 roles: dict[str, str], bios: dict[str, dict]) -> dict:
    primaries = [a for a in atts if roles[a] == "primary"]
    flags: list[str] = []

    # --- names: vote across primaries, header/rules layer
    sur_votes: Counter[str] = Counter()
    sur_raw: dict[str, Counter[str]] = defaultdict(Counter)
    given_variants: Counter[str] = Counter()
    byr_votes: Counter[int] = Counter()
    name_src: Counter[str] = Counter()
    for a in primaries:
        r = bios[a]
        s, g, src = bio_name(r)
        name_src[src] += 1
        k = surname_norm(s)
        if k:
            sur_votes[k] += 1
            sur_raw[k][s.strip()] += 1
        if g:
            given_variants[re.sub(r"\s+", " ", g.strip())] += 1
        if r.get("birth_year"):
            byr_votes[r["birth_year"]] += 1

    surname = None
    if sur_votes:
        top = sur_votes.most_common(1)[0][0]
        surname = sur_raw[top].most_common(1)[0][0]
        if len(sur_votes) > 1:
            flags.append("surname_variants")
    elif spine_p.get("surname"):
        surname = spine_p["surname"]
        name_src["spine"] += 1

    given = None
    if given_variants:
        # fullest spelled-out variant among those compatible with the modal one
        modal = given_variants.most_common(1)[0][0]
        compat = [g for g in given_variants if _names_compatible(g, modal)]
        given = max(
            compat,
            key=lambda g: (sum(1 for t in g.split() if len(t) > 1),
                           given_variants[g], len(g)),
        )
    elif spine_p.get("given_names"):
        given = spine_p["given_names"]

    birth_year = None
    if byr_votes:
        birth_year = byr_votes.most_common(1)[0][0]
        spread = max(byr_votes) - min(byr_votes)
        if len(byr_votes) > 1 and spread > 1:
            flags.append("birth_year_conflict")
    elif spine_p.get("birth_year"):
        birth_year = spine_p["birth_year"]

    # --- same-edition namesakes that survived dupprint folding
    ed_primary: Counter[int] = Counter(bios[a]["edition_year"] for a in primaries)
    if any(v > 1 for v in ed_primary.values()):
        flags.append("namesake_same_edition")

    # --- merged event chain: newest primary's chain, then earlier events not
    # already covered (reprints accumulate, so latest chain is the fullest)
    events: list[dict] = []
    seen_keys: set[tuple[str, int]] = set()
    for a in sorted(primaries, key=lambda x: -bios[x]["edition_year"]):
        for ev in bios[a].get("events") or []:
            k = event_key(ev)
            if k is not None and k in seen_keys:
                continue
            if k is not None:
                seen_keys.add(k)
            elif events:      # undated/unstemmed events only from newest chain
                continue
            events.append({**ev, "bio_id": a})
    events.sort(key=lambda e: (e.get("year_start") or 9999))

    honours: list[dict] = []
    hseen: set[tuple[str, int | None]] = set()
    for a in primaries:
        for h in bios[a].get("honours") or []:
            hk = (h.get("award") or "", h.get("year"))
            if hk in hseen:
                continue
            hseen.add(hk)
            honours.append(h)

    editions = sorted({bios[a]["edition_year"] for a in primaries})
    if not primaries:
        flags.append("no_primary_members")
        # legacy-only chain (block missed by the volume extraction, or a
        # dol1935 bio): fall back to the spine's own parse so the person
        # still carries editions and a career
        if not editions and spine_p.get("editions"):
            editions = sorted(spine_p["editions"])
        if not events and spine_p.get("events"):
            events = [{**ev, "source": "spine"} for ev in spine_p["events"]]
        if not honours and spine_p.get("honours"):
            honours = list(spine_p["honours"])
    if surname and (_HONORIFIC_SURNAME.match(surname)
                    or "BISHOP" in (surname.upper())):
        flags.append("suspect_surname")
    if surname is None and not events:
        flags.append("not_a_person")

    years = [e["year_start"] for e in events if e.get("year_start")]
    return {
        "person_id": pid,
        "surname": surname,
        "given_names": given,
        "birth_year": birth_year,
        "birth_year_votes": dict(sorted(byr_votes.items())) if byr_votes else {},
        "surname_variants": sorted({v for k in sur_raw for v in sur_raw[k]}),
        "given_variants": [g for g, _ in given_variants.most_common(6)],
        "honours": honours,
        "events": events,
        "career_start": min(years) if years else None,
        "career_end": max(years) if years else None,
        "editions": editions,
        "n_members": len(atts),
        "n_primary": len(primaries),
        "members": {a: roles[a] for a in atts},
        "name_source": dict(name_src),
        "flags": flags,
    }


# ----------------------------------------------------------------- orphans

def attach_orphans(orphans: list[str], persons: dict[str, dict],
                   bios: dict[str, dict]) -> tuple[int, int]:
    by_sur: dict[str, list[str]] = defaultdict(list)
    for pid, p in persons.items():
        k = surname_norm(p.get("surname"))
        if k:
            by_sur[k].append(pid)
    attached = created = 0
    for a in orphans:
        r = bios[a]
        s, g, _ = bio_name(r)
        keys = {event_key(ev) for ev in r.get("events") or []}
        keys.discard(None)
        best = None
        for pid in by_sur.get(surname_norm(s), []):
            p = persons[pid]
            if not _names_compatible(g, p.get("given_names")):
                continue
            if r["edition_year"] in p["editions"]:
                continue
            pkeys = {event_key(ev) for ev in p["events"]}
            shared = len(keys & pkeys)
            byr_ok = (r.get("birth_year") and p.get("birth_year")
                      and abs(r["birth_year"] - p["birth_year"]) <= 1)
            if shared >= MIN_ORPHAN_SHARED or (byr_ok and shared >= 1):
                if best is None or shared > best[0]:
                    best = (shared, pid)
        if best:
            pid = best[1]
            p = persons[pid]
            p["members"][a] = "primary"
            p["n_members"] += 1
            p["n_primary"] += 1
            p["editions"] = sorted(set(p["editions"]) | {r["edition_year"]})
            p.setdefault("flags", []).append("orphan_attached")
            attached += 1
        else:
            pid = f"kgp_{a}"
            persons[pid] = build_person(pid, {}, [a], {a: "primary"}, bios)
            persons[pid]["flags"].append("orphan_singleton")
            created += 1
    return attached, created


# ------------------------------------------------------- under-merge scan

def undermerge_candidates(persons: dict[str, dict]) -> list[dict]:
    by_sur: dict[str, list[str]] = defaultdict(list)
    for pid, p in persons.items():
        if "not_a_person" in p["flags"] or not p["events"]:
            continue
        k = surname_norm(p.get("surname"))
        if k:
            by_sur[k].append(pid)
    out: list[dict] = []
    for k, pids in by_sur.items():
        if len(pids) < 2 or len(pids) > 400:
            continue
        keyed = []
        for pid in pids:
            p = persons[pid]
            keys = {event_key(ev) for ev in p["events"]}
            keys.discard(None)
            keyed.append((pid, p, keys))
        for i in range(len(keyed)):
            pid_a, pa, ka = keyed[i]
            for j in range(i + 1, len(keyed)):
                pid_b, pb, kb = keyed[j]
                shared = ka & kb
                if len(shared) < MIN_UNDERMERGE_SHARED:
                    continue
                if set(pa["editions"]) & set(pb["editions"]):
                    continue        # co-listed in one edition = two people
                if not _names_compatible(pa.get("given_names"), pb.get("given_names")):
                    continue
                ba, bb = pa.get("birth_year"), pb.get("birth_year")
                byr = "equal" if (ba and bb and abs(ba - bb) <= 1) else (
                    "conflict" if (ba and bb) else "missing")
                out.append({
                    "person_a": pid_a, "person_b": pid_b,
                    "surname": pa.get("surname"),
                    "given_a": pa.get("given_names"), "given_b": pb.get("given_names"),
                    "birth_a": ba, "birth_b": bb, "birth_year": byr,
                    "n_shared": len(shared),
                    "shared": sorted([list(s) for s in shared],
                                     key=lambda x: x[1])[:8],
                    "editions_a": pa["editions"], "editions_b": pb["editions"],
                    "tier": ("A" if len(shared) >= 4 and byr != "conflict"
                             else "B" if byr != "conflict" else "C"),
                })
    out.sort(key=lambda c: (-c["n_shared"], c["surname"] or ""))
    return out


# ----------------------------------------------------------------- report

def write_report(persons: dict[str, dict], bios: dict[str, dict],
                 cands: list[dict], attached: int, created: int) -> None:
    real = [p for p in persons.values() if "not_a_person" not in p["flags"]]
    n_multi = sum(1 for p in real if len(p["editions"]) > 1)
    flag_counts: Counter[str] = Counter(f for p in persons.values() for f in p["flags"])
    role_counts: Counter[str] = Counter(
        r for p in persons.values() for r in p["members"].values())
    src_counts: Counter[str] = Counter()
    for p in persons.values():
        for s, n in p.get("name_source", {}).items():
            src_counts[s] += n
    span = Counter(len(p["editions"]) for p in real)
    tier = Counter(c["tier"] for c in cands)

    lines = [
        "# Unified bio-person table (volume bios ↔ stage-3 career KG)",
        "",
        "Person identity adopts the stage-3 spine partition — kgp_* person_ids are",
        "stable with graph_stage3 career facts/honours/groundings. This layer",
        "re-derives names from the new volume parses (Qwen bios had none), votes",
        "across editions, merges event chains, and QA-flags conflicts.",
        "",
        f"- volume bios (excl. not_a_bio): {sum(1 for r in bios.values() if r.get('parser') != 'not_a_bio'):,}",
        f"- persons: {len(persons):,} ({len(real):,} real; "
        f"{flag_counts['not_a_person']:,} junk chains flagged not_a_person)",
        f"- multi-edition persons: {n_multi:,} "
        f"({100 * n_multi / len(real):.1f}% of real)",
        f"- orphan bios attached to existing persons: {attached}; new singletons: {created}",
        "",
        "## Member roles",
        "",
    ]
    for r, n in role_counts.most_common():
        lines.append(f"- {r}: {n:,}")
    lines += ["", "## Name sources (per primary member)", ""]
    for s, n in src_counts.most_common():
        lines.append(f"- {s}: {n:,}")
    lines += ["", "## Flags", ""]
    for fl, n in flag_counts.most_common():
        lines.append(f"- {fl}: {n:,}")
    lines += ["", "## Edition-span distribution (real persons)", "",
              "| editions attested | persons |", "|---|---|"]
    for k in sorted(span):
        lines.append(f"| {k} | {span[k]:,} |")
    careers_path = VOLROOT / "careers" / "careers.jsonl"
    if careers_path.exists():
        pmap = {a: pid for pid, p in persons.items() for a in p["members"]}
        n_ok = n_linked = n_conflict = 0
        person_colonies: dict[str, set[str]] = defaultdict(set)
        for line in careers_path.open(encoding="utf-8"):
            c = json.loads(line)
            if c.get("suspect"):
                continue
            n_ok += 1
            pids = {pmap[b] for b in (c.get("bio_ids") or []) if b in pmap}
            if not pids:
                continue
            n_linked += 1
            if len(pids) > 1:
                n_conflict += 1
            for pid in pids:
                if c.get("colony"):
                    person_colonies[pid].add(c["colony"])
        multi_col = sum(1 for v in person_colonies.values() if len(v) > 1)
        lines += [
            "",
            "## Roster-career join (careers.jsonl bio links -> persons)",
            "",
            f"- non-suspect roster careers: {n_ok:,}; bio-linked: {n_linked:,} "
            f"— all resolve to a person (the partition is total over bios)",
            f"- distinct persons behind bio-linked careers: {len(person_colonies):,}",
            f"- persons with roster careers in >1 colony: {multi_col:,}",
            f"- careers whose bios map to >1 person (link noise / residual "
            f"under-merge): {n_conflict:,}",
        ]
    lines += [
        "",
        "## Under-merge candidates (new-event appointment chains)",
        "",
        f"{len(cands):,} candidate pairs (>= {MIN_UNDERMERGE_SHARED} shared exact "
        "(position-stem, year) appointments, given-compatible, edition-disjoint):",
        "",
        f"- tier A (>=4 shared, birth years not in conflict): {tier['A']:,}",
        f"- tier B (3 shared, birth years not in conflict): {tier['B']:,}",
        f"- tier C (birth-year conflict — likely OCR-garbled years): {tier['C']:,}",
        "",
        "Review file: undermerge_candidates.jsonl — NOT auto-applied.",
        "",
    ]
    (OUTDIR / "BIO_PERSONS.md").write_text("\n".join(lines), encoding="utf-8")


def load_approved_merges() -> dict[str, str]:
    """Union-find roots for adjudicated under-merge decisions (approve only).
    File: undermerge_decisions.jsonl — written from a close review of every
    candidate; regenerating candidates after a merge round may surface new
    pairs (bridged chains), so decisions accumulate across rounds."""
    path = OUTDIR / "undermerge_decisions.jsonl"
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        while parent.get(x, x) != x:
            parent[x] = parent.get(parent[x], parent[x])
            x = parent[x]
        return x

    if path.exists():
        for line in path.open(encoding="utf-8"):
            d = json.loads(line)
            if d.get("decision") != "approve":
                continue
            ra, rb = find(d["person_a"]), find(d["person_b"])
            if ra != rb:
                parent[max(ra, rb)] = min(ra, rb)
    return {x: find(x) for x in list(parent)}


def apply_birth_overrides(persons: dict[str, dict],
                          absorbed: dict[str, str]) -> int:
    """Adjudicated birth-year repairs (birth_year_overrides.jsonl, built by
    volume_birthyear_overrides.py from the Tier-A screens): OCR digit
    fixes, vote-conflict resolutions, and honour-absorption nulls. Applied
    at build time so repairs survive rebuilds; a resolved override clears
    the birth_year_conflict flag but keeps the votes for provenance.
    `absorbed` maps absorbed ids to their surviving person id (NOT the
    union-find root — the survivor is the most-attested member, whose id
    can differ from the root)."""
    path = OUTDIR / "birth_year_overrides.jsonl"
    if not path.exists():
        return 0
    n = 0
    for r in map(json.loads, path.open(encoding="utf-8")):
        pid = r["person_id"]
        if pid not in persons:
            pid = absorbed.get(pid, pid)
        p = persons.get(pid)
        if p is None:
            continue
        p["birth_year"] = r["birth_year"]
        p["birth_year_basis"] = r["basis"]
        if "birth_year_conflict" in p["flags"]:
            p["flags"].remove("birth_year_conflict")
        if "birth_year_overridden" not in p["flags"]:
            p["flags"].append("birth_year_overridden")
        n += 1
    return n


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    bios = load_bios()
    spine = load_spine()
    roots = load_approved_merges()

    # group spine records by merge root; primary id = most attestations
    groups: dict[str, list[dict]] = defaultdict(list)
    for sp in spine:
        groups[roots.get(sp["person_id"], sp["person_id"])].append(sp)

    persons: dict[str, dict] = {}
    claimed: set[str] = set()
    id_merges: list[dict] = []
    for _, members in groups.items():
        members.sort(key=lambda s: (-len(s.get("attestations") or []),
                                    s["person_id"]))
        base = members[0]
        pid = base["person_id"]
        atts = [a for sp in members for a in (sp.get("attestations") or [])]
        roles = classify_members(atts, bios)
        p = build_person(pid, base, atts, roles, bios)
        if len(members) > 1:
            p["absorbed_ids"] = [m["person_id"] for m in members[1:]]
            p["flags"].append("undermerge_applied")
            id_merges.extend({"absorbed_id": m["person_id"], "person_id": pid}
                             for m in members[1:])
        persons[pid] = p
        claimed.update(a for a in atts if a in bios)
    with (OUTDIR / "person_id_merges.jsonl").open("w", encoding="utf-8") as fh:
        for m in id_merges:
            fh.write(json.dumps(m) + "\n")

    orphans = [b for b, r in bios.items()
               if b not in claimed and r.get("parser") != "not_a_bio"]
    attached, created = attach_orphans(sorted(orphans), persons, bios)

    n_overrides = apply_birth_overrides(
        persons, {m["absorbed_id"]: m["person_id"] for m in id_merges})

    cands = undermerge_candidates(persons)

    with (OUTDIR / "bio_persons.jsonl").open("w", encoding="utf-8") as fh:
        for pid in sorted(persons):
            fh.write(json.dumps(persons[pid], ensure_ascii=False) + "\n")
    with (OUTDIR / "bio_person_map.jsonl").open("w", encoding="utf-8") as fh:
        for pid in sorted(persons):
            p = persons[pid]
            for a, role in sorted(p["members"].items()):
                ed = bios[a]["edition_year"] if a in bios else None
                fh.write(json.dumps({"bio_id": a, "person_id": pid,
                                     "edition_year": ed, "role": role}) + "\n")
    with (OUTDIR / "undermerge_candidates.jsonl").open("w", encoding="utf-8") as fh:
        for c in cands:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")

    write_report(persons, bios, cands, attached, created)
    real = sum(1 for p in persons.values() if "not_a_person" not in p["flags"])
    print(f"persons={len(persons)} real={real} orphans attached={attached} "
          f"created={created} undermerge_candidates={len(cands)} "
          f"birth_overrides={n_overrides}")
    print(f"-> {OUTDIR}/")


if __name__ == "__main__":
    main()
