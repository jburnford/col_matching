<!-- {"case_id": "case_hodge_guy_b1904", "bio_ids": ["hodge_guy_b1904"], "stint_ids": ["Hodge, J. G___Malta___1939"]} -->
# Dossier case_hodge_guy_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hodge_guy_b1904'] carry a single initial only — the namesake trap applies.

## Biography `hodge_guy_b1904`

- Printed name: **HODGE, Guy**
- Birth year: 1904 (attested in editions [1948, 1949, 1950, 1951])
- Honours: M.I.L.E
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33368.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HODGE, Guy, M.I.L.E., A.M.I.Mech.E.—b. 1904; ed. Probus Sch., Probus, Cornwall, and Kelly Coll., Tavistock, Devon; pupilage, G.W.R.; asst. mech. offr., rlwy., Nig., 1938; dist. loco. supt., 1942; research offr., rlwy., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | asst. mech. offr., rlwy. | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1942 | dist. loco. supt | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1949 | research offr., rlwy | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Hodge, J. G___Malta___1939`

- Staff-list name: **Hodge, J. G** | colony: **Malta** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | J. G. Hodge | Masters | Lyceum | — | — |
| 1940 | J. G. Hodge | Masters | Lyceum. | — | — |

### Deterministic checks: `hodge_guy_b1904` vs `Hodge, J. G___Malta___1939`

- [PASS] surname_gate: bio 'HODGE' vs stint 'Hodge, J. G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1939, birth 1904 (age 35)
- [FAIL] colony: no placed event resolves to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

