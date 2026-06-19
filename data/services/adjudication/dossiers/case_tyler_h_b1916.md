<!-- {"case_id": "case_tyler_h_b1916", "bio_ids": ["tyler_h_b1916"], "stint_ids": ["Tyler, H___St Helena___1956"]} -->
# Dossier case_tyler_h_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['tyler_h_b1916'] carry a single initial only — the namesake trap applies.

## Biography `tyler_h_b1916`

- Printed name: **TYLER, H**
- Birth year: 1916 (attested in editions [1963, 1964])
- Appears in editions: [1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1963-L25813.v` — printed in editions [1963, 1964]:**

> TYLER, H.—b. 1916; ed. Brunswick Park, Herts. C. Counc. Sch.; U.K. civ. serv., 1930; H.K. police, 1939; sub. inspr., 1946; inspr., 1950; asst. supt., 1952; supt., 1953-63.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | U.K. civ. serv | — | [1963, 1964] |
| 1 | 1939 | H.K. police | Hong Kong | [1963, 1964] |
| 2 | 1946 | sub. inspr | Hong Kong *(inherited from previous clause)* | [1963, 1964] |
| 3 | 1950 | inspr | Hong Kong *(inherited from previous clause)* | [1963, 1964] |
| 4 | 1952 | asst. supt | Hong Kong *(inherited from previous clause)* | [1963, 1964] |
| 5 | 1953–1963 | supt | Hong Kong *(inherited from previous clause)* | [1963, 1964] |

## Candidate stint `Tyler, H___St Helena___1956`

- Staff-list name: **Tyler, H** | colony: **St Helena** | listed 1956–1957 | editions [1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | H. Tyler | Superintendent of Police and Gaol, and Registrar, Supreme Court | Civil Establishment | — | — |
| 1957 | H. Tyler | Superintendent of Police and Gaol, and Registrar, Supreme Court | CIVIL ESTABLISHMENT | — | — |

### Deterministic checks: `tyler_h_b1916` vs `Tyler, H___St Helena___1956`

- [PASS] surname_gate: bio 'TYLER' vs stint 'Tyler, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1956, birth 1916 (age 40)
- [FAIL] colony: no placed event resolves to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1956-1957
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

