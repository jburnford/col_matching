<!-- {"case_id": "case_jones_j-p_b1919", "bio_ids": ["jones_j-p_b1919"], "stint_ids": ["Jones, J. P___Jamaica___1948"]} -->
# Dossier case_jones_j-p_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 259 official(s) with this surname in the graph's staff lists; 126 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Jones, J. P___Jamaica___1948` is also gate-compatible with biography(ies) outside this case: ['jones_joseph_e1892'] (already linked elsewhere or filtered).

## Biography `jones_j-p_b1919`

- Printed name: **JONES, J. P**
- Birth year: 1919 (attested in editions [1966])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L15842.v` — printed in editions [1966]:**

> JONES, J. P.—b. 1919; ed. Llanelly Gram. Sch.; mil. serv., 1939-46, major; dist. offr. Tang., 1950; dist. comsnr., 1958; prin. asst. sec., 1961; admin. offr., gr. III, 1964-65. (Tanzania Govt. service.)

**Version `col1961-L23916.v` — printed in editions [1961, 1962, 1963, 1964, 1965]:**

> JONES, J. P.—b. 1919; ed. Llanelly Gram. Sch.; mil. serv., 1939-46, major; dist. offr., Tang., 1950. (Tanzania Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950 | dist. offr. Tang | Tanganyika | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1958 | dist. comsnr | — | [1966] |
| 2 | 1961 | prin. asst. sec | — | [1966] |
| 3 | 1964–1965 | admin. offr., gr. III | — | [1966] |

## Candidate stint `Jones, J. P___Jamaica___1948`

- Staff-list name: **Jones, J. P** | colony: **Jamaica** | listed 1948–1951 | editions [1948, 1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1948 | J. P. Jones | Commissioner | — | — | — |
| 1949 | J. P. Jones | — | — | — | — |
| 1950 | J. P. Jones | Commissioner | Commissioners | — | — |
| 1951 | J. P. Jones | Commissioner | — | — | — |

### Deterministic checks: `jones_j-p_b1919` vs `Jones, J. P___Jamaica___1948`

- [PASS] surname_gate: bio 'JONES' vs stint 'Jones, J. P' (exact)
- [PASS] initials: bio ['J', 'P'] ~ stint ['J', 'P']
- [PASS] age_gate: stint starts 1948, birth 1919 (age 29)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1948-1951
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

