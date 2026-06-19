<!-- {"case_id": "case_wallington_edward-william_e1883", "bio_ids": ["wallington_edward-william_e1883"], "stint_ids": ["Wallington, E. W___South Australia___1898", "Wallington, Edward William___New South Wales___1888"]} -->
# Dossier case_wallington_edward-william_e1883

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wallington_edward-william_e1883`

- Printed name: **WALLINGTON, EDWARD WILLIAM**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L36559.v` — printed in editions [1888]:**

> WALLINGTON, EDWARD WILLIAM, B.A.—Private secretary to governor, Fiji, 1883; to governor, New South Wales, 1885.

**Version `col1889-L36187.v` — printed in editions [1889, 1890]:**

> WALLINGTON, Edward William, B.A.—Lt., 3rd bat. Oxfordshire Light Infantry; private secretary to governor, Fiji, 1883; to governor, N.S.W., 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Private secretary to governor | Fiji | [1888, 1889, 1890] |
| 1 | 1885 | to governor | New South Wales | [1888, 1889, 1890] |

## Candidate stint `Wallington, E. W___South Australia___1898`

- Staff-list name: **Wallington, E. W** | colony: **South Australia** | listed 1898–1900 | editions [1898, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | Capt. E. W. Wallington | Private Secretary | Governor | — | Captain |
| 1900 | E. W. Wallington | Private Secretary | Executive Council | — | Captain |

### Deterministic checks: `wallington_edward-william_e1883` vs `Wallington, E. W___South Australia___1898`

- [PASS] surname_gate: bio 'WALLINGTON' vs stint 'Wallington, E. W' (exact)
- [PASS] initials: bio ['E', 'W'] ~ stint ['E', 'W']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1900
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Wallington, Edward William___New South Wales___1888`

- Staff-list name: **Wallington, Edward William** | colony: **New South Wales** | listed 1888–1889 | editions [1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | Edward William Wallington | Private Secretary | Civil Establishment | — | — |
| 1889 | Edward William Wallington | Private Secretary | Civil Establishment | — | — |

### Deterministic checks: `wallington_edward-william_e1883` vs `Wallington, Edward William___New South Wales___1888`

- [PASS] surname_gate: bio 'WALLINGTON' vs stint 'Wallington, Edward William' (exact)
- [PASS] initials: bio ['E', 'W'] ~ stint ['E', 'W']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'New South Wales'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1889
- [FAIL] position_sim: best 29 vs bar 60: 'to governor' ~ 'Private Secretary'
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

