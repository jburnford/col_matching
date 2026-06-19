<!-- {"case_id": "case_muir_a_b1921", "bio_ids": ["muir_a_b1921"], "stint_ids": ["Muir, A. M___Nigeria___1958"]} -->
# Dossier case_muir_a_b1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['muir_a_b1921'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Muir, A. M___Nigeria___1958` is also gate-compatible with biography(ies) outside this case: ['muir_archibald-mungo_b1914'] (already linked elsewhere or filtered).

## Biography `muir_a_b1921`

- Printed name: **MUIR, A**
- Birth year: 1921 (attested in editions [1962, 1963, 1964])
- Appears in editions: [1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1962-L24702.v` — printed in editions [1962, 1963, 1964]:**

> MUIR, A.—b. 1921; ed. Camphill Sch., Paisley; mil. serv., 1941–46, R.N.V.R., lieut. (A) (pilot); Min. Labr. and Nat. Serv., U.K., 1939; labr. offr., Tang., 1951; labr. offr., Uga., 1958; senr. educ. offr.; asst. labr. commr., 1961. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | Min. Labr. and Nat. Serv., U.K | — | [1962, 1963, 1964] |
| 1 | 1951 | labr. offr. | Tanganyika | [1962, 1963, 1964] |
| 2 | 1958 | labr. offr. | Uganda | [1962, 1963, 1964] |
| 3 | 1961 | asst. labr. commr | Uganda *(inherited from previous clause)* | [1962, 1963, 1964] |

## Candidate stint `Muir, A. M___Nigeria___1958`

- Staff-list name: **Muir, A. M** | colony: **Nigeria** | listed 1958–1960 | editions [1958, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | A. M. Muir | Permanent Secretary | Civil Establishment | — | — |
| 1960 | A. M. Muir | Permanent Secretary | Civil Establishment | — | — |

### Deterministic checks: `muir_a_b1921` vs `Muir, A. M___Nigeria___1958`

- [PASS] surname_gate: bio 'MUIR' vs stint 'Muir, A. M' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A', 'M']
- [PASS] age_gate: stint starts 1958, birth 1921 (age 37)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1960
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

