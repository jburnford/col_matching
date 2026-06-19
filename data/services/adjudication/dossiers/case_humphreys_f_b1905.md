<!-- {"case_id": "case_humphreys_f_b1905", "bio_ids": ["humphreys_f_b1905"], "stint_ids": ["Humphreys, F___Nigeria___1934"]} -->
# Dossier case_humphreys_f_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['humphreys_f_b1905'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Humphreys, F___Nigeria___1934` is also gate-compatible with biography(ies) outside this case: ['humphreys_francis-henry_b1879'] (already linked elsewhere or filtered).

## Biography `humphreys_f_b1905`

- Printed name: **HUMPHREYS, F**
- Birth year: 1905 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955])
- Honours: O.B.E (1955)
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1948-L33511.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955]:**

> HUMPHREYS, F., O.B.E. (1955).—b. 1905; ed. Charterhouse Sch.; mem. Middle Temple; mil. serv., 1940-43, capt.; cadet, Nig., 1928; admin. offr., cl II, 1947; cl I, 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | cadet | Nigeria | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 1 | 1947 | admin. offr., cl II | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 2 | 1950 | cl I | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |

## Candidate stint `Humphreys, F___Nigeria___1934`

- Staff-list name: **Humphreys, F** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | F. Humphreys | — | Administrative Service | — | — |
| 1939 | F. Humphreys | Assistant Secretary | Secretariat, Northern Provinces | — | — |

### Deterministic checks: `humphreys_f_b1905` vs `Humphreys, F___Nigeria___1934`

- [PASS] surname_gate: bio 'HUMPHREYS' vs stint 'Humphreys, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1934, birth 1905 (age 29)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 25 vs bar 60: 'cadet' ~ 'Assistant Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

