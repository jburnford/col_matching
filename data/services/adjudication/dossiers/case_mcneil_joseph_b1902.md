<!-- {"case_id": "case_mcneil_joseph_b1902", "bio_ids": ["mcneil_joseph_b1902"], "stint_ids": ["McNeil, J. H___Singapore___1949"]} -->
# Dossier case_mcneil_joseph_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mcneil_joseph_b1902'] carry a single initial only — the namesake trap applies.

## Biography `mcneil_joseph_b1902`

- Printed name: **McNEIL, Joseph**
- Birth year: 1902 (attested in editions [1951])
- Honours: A.M.I.M.M, M.C
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L40544.v` — printed in editions [1951]:**

> McNEIL, Joseph, M.C., A.M.I.M.M.—b. 1902; ed. various G.B., Can. and Colo. Sch. of Mines, U.S.A.; on mil. serv., 1939-45; mining appts., Alaska, U.S.A., E. and W. Africa, 1927-39; Cementation Co. Ltd., 1945-48; inspr., mines, Tang., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927–1939 | mining appts., Alaska, U.S.A., E. and W. Africa | — | [1951] |
| 1 | 1945–1948 | Cementation Co. Ltd | — | [1951] |
| 2 | 1948 | inspr., mines | Tanganyika | [1951] |

## Candidate stint `McNeil, J. H___Singapore___1949`

- Staff-list name: **McNeil, J. H** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. H. McNeil | Senior Surveyors and Surveyors | MARINE SURVEYS | — | — |
| 1951 | J. H. McNeil | Surveyors of Ships | Marine Surveys | — | — |

### Deterministic checks: `mcneil_joseph_b1902` vs `McNeil, J. H___Singapore___1949`

- [PASS] surname_gate: bio 'McNEIL' vs stint 'McNeil, J. H' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1949, birth 1902 (age 47)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

