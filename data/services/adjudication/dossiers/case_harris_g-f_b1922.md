<!-- {"case_id": "case_harris_g-f_b1922", "bio_ids": ["harris_g-f_b1922"], "stint_ids": ["Harris, G. F___St Helena___1958"]} -->
# Dossier case_harris_g-f_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 90 official(s) with this surname in the graph's staff lists; 35 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `harris_g-f_b1922`

- Printed name: **HARRIS, G. F**
- Birth year: 1922 (attested in editions [1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1958-L23378.v` — printed in editions [1958, 1959, 1960, 1961, 1962]:**

> HARRIS, G. F., M.C.—b. 1922; ed. Wellington Coll. and New Coll., Oxford; mil. serv., 1943-47, capt.; cadet, Nig., 1947; admin. offr., cl. III, 1952; adminr., Tristan da Cunha, 1957-59; cl. II, 1958.

**Version `col1957-L23858.v` — printed in editions [1957]:**

> HARRIS, G. F., M.C.—b. 1922; ed. Wellington Coll. and New Coll., Oxford; mil. serv., 1943-47, capt.; cadet, Nig., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | cadet | Nigeria | [1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1952 | admin. offr., cl. III | Nigeria *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962] |
| 2 | 1957–1959 | adminr. | Tristan da Cunha | [1958, 1959, 1960, 1961, 1962] |
| 3 | 1958 | cl. II | Tristan da Cunha *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Harris, G. F___St Helena___1958`

- Staff-list name: **Harris, G. F** | colony: **St Helena** | listed 1958–1959 | editions [1958, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | G. F. Harris | Administrator | Civil Establishment | — | — |
| 1959 | G. F. Harris | Administrator | — | — | — |

### Deterministic checks: `harris_g-f_b1922` vs `Harris, G. F___St Helena___1958`

- [PASS] surname_gate: bio 'HARRIS' vs stint 'Harris, G. F' (exact)
- [PASS] initials: bio ['G', 'F'] ~ stint ['G', 'F']
- [PASS] age_gate: stint starts 1958, birth 1922 (age 36)
- [FAIL] colony: no placed event resolves to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1959
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

