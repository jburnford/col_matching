<!-- {"case_id": "case_roberts_l_b1919", "bio_ids": ["roberts_l_b1919"], "stint_ids": ["Roberts, L. A___Dominica___1963", "Roberts, L. A___Windward Islands___1950"]} -->
# Dossier case_roberts_l_b1919

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 150 official(s) with this surname in the graph's staff lists; 67 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['roberts_l_b1919'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Roberts, L. A___Dominica___1963` is also gate-compatible with biography(ies) outside this case: ['roberts_loftus-alexander_b1910'] (already linked elsewhere or filtered).
- NOTE: stint `Roberts, L. A___Windward Islands___1950` is also gate-compatible with biography(ies) outside this case: ['roberts_loftus-alexander_b1910'] (already linked elsewhere or filtered).

## Biography `roberts_l_b1919`

- Printed name: **ROBERTS, L**
- Birth year: 1919 (attested in editions [1959, 1960, 1961, 1962])
- Appears in editions: [1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1959-L27322.v` — printed in editions [1959, 1960, 1961, 1962]:**

> ROBERTS, L., M.C.—b. 1919; ed. Wolverhampton Gram. Sch., the Sorbonne, Paris, and St. Peter's Hall, Oxford; mil. serv., 1939-46 (desps.); cadet, Nig., 1946; admin. offr., cl. II, 1954; cl. I, 1959-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | cadet | Nigeria | [1959, 1960, 1961, 1962] |
| 1 | 1954 | admin. offr., cl. II | Nigeria *(inherited from previous clause)* | [1959, 1960, 1961, 1962] |
| 2 | 1959–1961 | cl. I | Nigeria *(inherited from previous clause)* | [1959, 1960, 1961, 1962] |

## Candidate stint `Roberts, L. A___Dominica___1963`

- Staff-list name: **Roberts, L. A** | colony: **Dominica** | listed 1963–1966 | editions [1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | L. A. Roberts | Chief Secretary | Civil Establishment | — | — |
| 1964 | L. A. Roberts | Chief Secretary | Civil Establishment | — | — |
| 1965 | L. A. Roberts | Chief Secretary | Civil Establishment | — | — |
| 1966 | L. A. Roberts | Chief Secretary | Civil Establishment | — | — |

### Deterministic checks: `roberts_l_b1919` vs `Roberts, L. A___Dominica___1963`

- [PASS] surname_gate: bio 'ROBERTS' vs stint 'Roberts, L. A' (exact)
- [PASS] initials: bio ['L'] ~ stint ['L', 'A']
- [PASS] age_gate: stint starts 1963, birth 1919 (age 44)
- [FAIL] colony: no placed event resolves to 'Dominica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1966
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Roberts, L. A___Windward Islands___1950`

- Staff-list name: **Roberts, L. A** | colony: **Windward Islands** | listed 1950–1952 | editions [1950, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | L. A. Roberts | Social Welfare Officer | Social Welfare | — | — |
| 1952 | L. A. Roberts | Social Welfare Officer | Civil Establishment | — | — |

### Deterministic checks: `roberts_l_b1919` vs `Roberts, L. A___Windward Islands___1950`

- [PASS] surname_gate: bio 'ROBERTS' vs stint 'Roberts, L. A' (exact)
- [PASS] initials: bio ['L'] ~ stint ['L', 'A']
- [PASS] age_gate: stint starts 1950, birth 1919 (age 31)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1952
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

