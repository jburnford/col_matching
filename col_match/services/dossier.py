"""Serialize adjudication cases into dossiers readable by LLM and human.

A case is a connected component of the bipartite bio↔candidate-stint graph
(schema.Case). The dossier is one markdown document holding everything the
deterministic pass saw: the verbatim printed entries with edition provenance,
each candidate stint's year-by-year records, every evidence dimension with
its pass/fail and why, and corpus context (surname frequency, competing
claimants). Annotations state facts and scores, never verdicts — the
adjudicator must not be anchored.

Components larger than the caps are routed to the review queue unchunked:
splitting a contested component would reintroduce the independent-edge
reasoning the partition framing exists to prevent.
"""

from __future__ import annotations

import json
from collections import defaultdict

from .schema import Biography, Case, EntryVersion, StintCandidate

MAX_BIOS = 3        # component caps: beyond this it's review_oversized
MAX_STINTS = 12
TOKEN_CAP = 15_000  # estimated tokens per dossier (chars / 3.5)

CONSTRAINTS = """\
## Adjudication constraints (binding)

- The prime directive is NO FALSE MERGES. A missed link is recoverable; a
  wrong one silently corrupts the historical record. When in doubt, leave
  the stint unassigned.
- Surname identity is NOT evidence: every candidate here already shares the
  surname (it is the blocking key). Only position, place, dates, honours,
  initials/forenames, and edition co-occurrence count.
- Single-initial biographies (e.g. "J. Lewis") must never be merged on
  shared-stint or tenure-overlap evidence alone; they need a strong
  independent dimension (specific position match, shared honour, or
  multi-edition co-occurrence).
- A stint belongs to AT MOST one biography. If two biographies in this case
  could plausibly hold the same stint, assign it to neither.
- Respect hard chronology: nobody serves before age ~15 or after death.
- Generic junior titles (clerk, cadet, assistant) recur constantly; a title
  match alone on a common office is weak evidence.
"""


# NOTE: an auto-unlink triage for "hopeless" pairs (single-initial, no
# position/cooc/honour/tenure signal) was tested against the pilot and
# rejected: 3 of 7 sampled hopeless cases yielded evidence-backed verdicts
# (e.g. bio "D.D.P.W." matching staff-list "Deputy Director of Public
# Works" — abbreviation matches invisible to string metrics). Every case
# goes to an adjudicator.


def build_cases(candidates: list[StintCandidate]) -> list[Case]:
    """Union-find over the bipartite candidate graph; one Case per component."""
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for c in candidates:
        union(f"b:{c.bio_id}", f"s:{c.official_id}")

    comp: dict[str, dict[str, set]] = defaultdict(lambda: {"b": set(), "s": set()})
    n_cands: dict[str, int] = defaultdict(int)
    for c in candidates:
        root = find(f"b:{c.bio_id}")
        comp[root]["b"].add(c.bio_id)
        comp[root]["s"].add(c.official_id)
        n_cands[root] += 1

    cases = []
    for root, sides in comp.items():
        bio_ids = sorted(sides["b"])
        stint_ids = sorted(sides["s"])
        oversized = len(bio_ids) > MAX_BIOS or len(stint_ids) > MAX_STINTS
        cases.append(Case(
            case_id=f"case_{bio_ids[0]}",
            bio_ids=bio_ids,
            stint_ids=stint_ids,
            n_candidates=n_cands[root],
            route="review_oversized" if oversized else "adjudicate",
        ))
    cases.sort(key=lambda c: c.case_id)
    return cases


def render_dossier(
    case: Case,
    candidates: list[StintCandidate],
    bios_by_id: dict[str, Biography],
    officials_by_id: dict[str, dict],
    versions_by_id: dict[str, EntryVersion],
) -> str:
    """One markdown dossier for one case. `candidates` = this case's pairs."""
    by_pair = {(c.bio_id, c.official_id): c for c in candidates}
    out: list[str] = []
    header = {"case_id": case.case_id, "bio_ids": case.bio_ids,
              "stint_ids": case.stint_ids}
    out.append(f"<!-- {json.dumps(header)} -->")
    out.append(f"# Dossier {case.case_id}")

    # -- case context -------------------------------------------------------
    any_cand = candidates[0]
    out.append("\n## Case context\n")
    out.append(f"- {len(case.bio_ids)} biography(ies) and {len(case.stint_ids)} "
               f"candidate stint(s) are entangled in this case.")
    out.append(f"- Corpus context: {any_cand.same_surname_officials} official(s) "
               f"with this surname in the graph's staff lists; "
               f"{any_cand.same_surname_bios} biography(ies) with this surname "
               f"in the printed biographical sections. The commoner the "
               f"surname, the weaker any name-based inference.")
    single = [b for b in case.bio_ids
              if any(c.single_initial for c in candidates if c.bio_id == b)]
    if single:
        out.append(f"- WARNING: biography(ies) {single} carry a single initial "
                   f"only — the namesake trap applies.")
    contested = sorted(s for s in case.stint_ids
                       if len({c.bio_id for c in candidates
                               if c.official_id == s}) > 1)
    if contested:
        out.append(f"- CONTESTED: stint(s) {contested} have more than one "
                   f"claimant biography in this case.")
    for c in candidates:
        if c.phase1_dropped_ambiguous:
            out.append(f"- Phase 1 found `{c.bio_id}` ↔ `{c.official_id}` "
                       f"passed its evidence bar but dropped it as ambiguous "
                       f"(a comparable-strength competitor existed).")
        if c.competing_bio_ids:
            outside = sorted(set(c.competing_bio_ids) - set(case.bio_ids))
            if outside:
                out.append(f"- NOTE: stint `{c.official_id}` is also gate-"
                           f"compatible with biography(ies) outside this case: "
                           f"{outside} (already linked elsewhere or filtered).")

    # -- biographies ---------------------------------------------------------
    for bio_id in case.bio_ids:
        bio = bios_by_id[bio_id]
        out.append(f"\n## Biography `{bio_id}`\n")
        name = f"{bio.surname}, {bio.given_names or '(no given names printed)'}"
        out.append(f"- Printed name: **{name}**")
        if bio.birth_year:
            out.append(f"- Birth year: {bio.birth_year.value} "
                       f"(attested in editions {bio.birth_year.editions})")
        else:
            out.append("- Birth year: not printed")
        if bio.honours:
            hs = ", ".join(h.award + (f" ({h.year})" if h.year else "")
                           for h in bio.honours)
            out.append(f"- Honours: {hs}")
        if bio.terminal:
            out.append(f"- Terminal: {bio.terminal.kind} "
                       f"{bio.terminal.year or '(year not printed)'} — "
                       f"“{bio.terminal.text_span}”")
        out.append(f"- Appears in editions: {bio.editions}")

        out.append("\n### Verbatim printed entry text (OCR)\n")
        for vid in bio.version_ids:
            v = versions_by_id.get(vid)
            if v is None:
                out.append(f"- `{vid}`: (text unavailable)")
                continue
            out.append(f"**Version `{vid}` — printed in editions "
                       f"{v.attesting_editions}:**\n")
            out.append(f"> {v.canonical_text.strip()}\n")

        out.append("### Compiled career timeline\n")
        out.append("| # | years | position | place | editions |")
        out.append("|---|-------|----------|-------|----------|")
        for i, ev in enumerate(bio.events):
            yrs = f"{ev.year_start or '?'}–{ev.year_end or ''}".rstrip("–")
            place = (ev.place or "—") + (" *(inherited from previous clause)*"
                                         if ev.place_inherited else "")
            out.append(f"| {i} | {yrs} | {ev.position or '—'} | {place} "
                       f"| {ev.editions} |")

    # -- candidate stints ----------------------------------------------------
    for stint_id in case.stint_ids:
        o = officials_by_id[stint_id]
        out.append(f"\n## Candidate stint `{stint_id}`\n")
        out.append(f"- Staff-list name: **{o['name']}** | colony: "
                   f"**{o['colony']}** | listed {o['first_year']}–{o['last_year']}"
                   f" | editions {o['editions']}")
        out.append("\n### Year-by-year staff-list records\n")
        out.append("| year | name as printed | position | department | honours | rank |")
        out.append("|------|-----------------|----------|------------|---------|------|")
        for r in sorted(o["records"], key=lambda r: r["year"]):
            honors = ", ".join(r.get("honors") or []) or "—"
            out.append(f"| {r['year']} | {r.get('name_raw') or '—'} "
                       f"| {r.get('position_raw') or '—'} "
                       f"| {r.get('department_raw') or '—'} "
                       f"| {honors} | {r.get('military_rank') or '—'} |")
        for bio_id in case.bio_ids:
            cand = by_pair.get((bio_id, stint_id))
            if cand is None:
                continue
            out.append(f"\n### Deterministic checks: `{bio_id}` vs `{stint_id}`\n")
            for chk in cand.checks:
                if chk.name == "edition_cooccurrence" and not chk.passed:
                    # Strict joint test (same edition-year AND colony-agreeing
                    # position similarity); most true matches fail it, so a
                    # bare FAIL misleads. Render as an absent bonus instead.
                    out.append(f"- [not met] edition_cooccurrence (strict "
                               f"corroboration bonus — same edition-year with "
                               f"colony-agreeing position match; absence is "
                               f"normal even for true matches and is NOT "
                               f"evidence against): {chk.detail}")
                    continue
                mark = "PASS" if chk.passed else "FAIL"
                out.append(f"- [{mark}] {chk.name}: {chk.detail}")

    out.append("\n" + CONSTRAINTS)
    return "\n".join(out) + "\n"


def est_tokens(text: str) -> int:
    return int(len(text) / 3.5)
