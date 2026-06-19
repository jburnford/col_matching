<!-- {"case_id": "case_lawrie_edwin-stewart_b1899", "bio_ids": ["lawrie_edwin-stewart_b1899"], "stint_ids": ["Lawrie, E. S___Straits Settlements___1931", "Lawrie, S___Nyasaland___1930"]} -->
# Dossier case_lawrie_edwin-stewart_b1899

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lawrie_edwin-stewart_b1899`

- Printed name: **LAWRIE, EDWIN STEWART**
- Birth year: 1899 (attested in editions [1939])
- Honours: M.B
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L68543.v` — printed in editions [1939]:**

> LAWRIE, EDWIN STEWART, M.B., Ch.B. (Glas.), F.R.C.S. (Edin.), F.R.F.P.S. (Glas.).—B. 1899; ed. G'gow Acad. and G'gow Univ.; M.O., Malaya, Mar., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | M.O. | Malaya | [1939] |

## Candidate stint `Lawrie, E. S___Straits Settlements___1931`

- Staff-list name: **Lawrie, E. S** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | E. S. Lawrie | Medical Officer | Medical | — | — |
| 1932 | E. S. Lawrie | Medical Officer | Medical | — | — |
| 1933 | E. S. Lawrie | Medical Officer | Medical | — | — |

### Deterministic checks: `lawrie_edwin-stewart_b1899` vs `Lawrie, E. S___Straits Settlements___1931`

- [PASS] surname_gate: bio 'LAWRIE' vs stint 'Lawrie, E. S' (exact)
- [PASS] initials: bio ['E', 'S'] ~ stint ['E', 'S']
- [PASS] age_gate: stint starts 1931, birth 1899 (age 32)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Lawrie, S___Nyasaland___1930`

- Staff-list name: **Lawrie, S** | colony: **Nyasaland** | listed 1930–1940 | editions [1930, 1931, 1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | S. Lawrie | Assistant Postmaster | Posts and Telegraphs | — | — |
| 1931 | S. Lawrie | Assistant Postmasters | Posts and Telegraphs | — | — |
| 1933 | S. Lawrie | Assistant Postmasters | Posts and Telegraphs | — | — |
| 1934 | S. Lawrie | Postmaster | Posts and Telegraphs | — | — |
| 1936 | S. Lawrie | Postmasters | Posts and Telegraphs | — | — |
| 1937 | S. Lawrie | Postmaster | Posts and Telegraphs | — | — |
| 1939 | S. Lawrie | Postmasters | Posts and Telegraphs | — | — |
| 1940 | S. Lawrie | Postmaster | Posts and Telegraphs | — | — |

### Deterministic checks: `lawrie_edwin-stewart_b1899` vs `Lawrie, S___Nyasaland___1930`

- [PASS] surname_gate: bio 'LAWRIE' vs stint 'Lawrie, S' (exact)
- [PASS] initials: bio ['E', 'S'] ~ stint ['S']
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

