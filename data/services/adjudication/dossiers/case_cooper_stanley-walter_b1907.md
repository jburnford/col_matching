<!-- {"case_id": "case_cooper_stanley-walter_b1907", "bio_ids": ["cooper_stanley-walter_b1907"], "stint_ids": ["Cooper, S. W___Northern Rhodesia___1931"]} -->
# Dossier case_cooper_stanley-walter_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 75 official(s) with this surname in the graph's staff lists; 41 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cooper_stanley-walter_b1907`

- Printed name: **COOPER, Stanley Walter**
- Birth year: 1907 (attested in editions [1948, 1949, 1950, 1951])
- Honours: D.T.M, O.B.E (1960)
- Appears in editions: [1948, 1949, 1950, 1951, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1948-L31912.v` — printed in editions [1948, 1949, 1950, 1951]:**

> COOPER, Stanley Walter, F.R.C.S. (Edin.), M.R.C.S. (Eng.), L.R.C.P. (Lond.), D.T.M., D.T.H. (Liv.).—b. 1907; ed. Taunton Sch. and St. Mary's Hosp., Lond.; med. offr., G.C., 1935; surg. spec., 1948.

**Version `col1959-L21951.v` — printed in editions [1959, 1960]:**

> COOPER, S. W., O.B.E. (1960).—b. 1907; ed. Taunton Sch., and St. Mary's Hosp., London; med. offr., G.C., 1935; surg. spec., 1948-59 (Ghana civil service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | med. offr. | Gold Coast | [1948, 1949, 1950, 1951, 1959, 1960] |
| 1 | 1948 | surg. spec | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1959, 1960] |

## Candidate stint `Cooper, S. W___Northern Rhodesia___1931`

- Staff-list name: **Cooper, S. W** | colony: **Northern Rhodesia** | listed 1931–1934 | editions [1931, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | S. W. Cooper | Clerk to Police Magistrate | Judicial | — | — |
| 1933 | S. W. Cooper | District Registrar (1) | Judicial | — | — |
| 1934 | S. W. Cooper | District Registrar (1) | Judicial | — | — |

### Deterministic checks: `cooper_stanley-walter_b1907` vs `Cooper, S. W___Northern Rhodesia___1931`

- [PASS] surname_gate: bio 'COOPER' vs stint 'Cooper, S. W' (exact)
- [PASS] initials: bio ['S', 'W'] ~ stint ['S', 'W']
- [PASS] age_gate: stint starts 1931, birth 1907 (age 24)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1934
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

