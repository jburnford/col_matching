<!-- {"case_id": "case_lawrence_edwin-stewart_b1899", "bio_ids": ["lawrence_edwin-stewart_b1899"], "stint_ids": ["Lawrence, E___Nyasaland___1930"]} -->
# Dossier case_lawrence_edwin-stewart_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 58 official(s) with this surname in the graph's staff lists; 24 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Lawrence, E___Nyasaland___1930` is also gate-compatible with biography(ies) outside this case: ['lawrence_edward_b1900', 'lawrence_ernest-harry-thorne_e1900'] (already linked elsewhere or filtered).

## Biography `lawrence_edwin-stewart_b1899`

- Printed name: **LAWRENCE, EDWIN STEWART**
- Birth year: 1899 (attested in editions [1940])
- Honours: M.B
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L66022.v` — printed in editions [1940]:**

> LAWRENCE, EDWIN STEWART, M.B., Ch.B. (Glas.), F.R.C.S. (Edin.), F.R.F.P.S. (Glas.).—B. 1899; ed. G'gow Acad. and G'gow Univ.; M.O., Malaya, Mar., 1928; surg., Penang, Apr., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | M.O. | Malaya | [1940] |
| 1 | 1938 | surg., Penang | Malaya *(inherited from previous clause)* | [1940] |

## Candidate stint `Lawrence, E___Nyasaland___1930`

- Staff-list name: **Lawrence, E** | colony: **Nyasaland** | listed 1930–1940 | editions [1930, 1931, 1932, 1933, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | E. Lawrence | District Agricultural Officer | Agricultural | — | — |
| 1931 | E. Lawrence | District Agricultural Officer | Agricultural | — | — |
| 1932 | E. Lawrence | District Agricultural Officers | Agricultural | — | — |
| 1933 | E. Lawrence | District Agricultural Officer | Agricultural | — | — |
| 1934 | E. Lawrence | District Agricultural Officer | Agricultural | — | — |
| 1937 | E. Lawrence | District Agricultural Officer | Agriculture | — | — |
| 1939 | E. Lawrence | Agricultural Officer | Agriculture | — | — |
| 1940 | E. Lawrence | Agricultural Officer | Agriculture | — | — |

### Deterministic checks: `lawrence_edwin-stewart_b1899` vs `Lawrence, E___Nyasaland___1930`

- [PASS] surname_gate: bio 'LAWRENCE' vs stint 'Lawrence, E' (exact)
- [PASS] initials: bio ['E', 'S'] ~ stint ['E']
- [PASS] age_gate: stint starts 1930, birth 1899 (age 31)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1940
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

