<!-- {"case_id": "case_white_stanhope_b1913", "bio_ids": ["white_stanhope_b1913"], "stint_ids": ["White, D. S___Uganda___1949", "White, F. S___Tanganyika___1953"]} -->
# Dossier case_white_stanhope_b1913

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 128 official(s) with this surname in the graph's staff lists; 57 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['white_stanhope_b1913'] carry a single initial only — the namesake trap applies.
- NOTE: stint `White, D. S___Uganda___1949` is also gate-compatible with biography(ies) outside this case: ['white_dennis_b1910'] (already linked elsewhere or filtered).
- NOTE: stint `White, F. S___Tanganyika___1953` is also gate-compatible with biography(ies) outside this case: ['white_f-f-s_b1911', 'white_frederick_b1847'] (already linked elsewhere or filtered).

## Biography `white_stanhope_b1913`

- Printed name: **WHITE, Stanhope**
- Birth year: 1913 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L36804.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WHITE, Stanhope.—b. 1913; ed. Harrogate Gram. Sch. and Emmanuel Coll., Cambridge (schol.), M.A. (Cantab.) (2nd cl. B.A., hons.); mem. expedit. with Egyptian desert survey, 1934, Cambridge, Iceland, 1934, Br.E.A. Archaeological, 1934-35, as survr. and geologist; on mil. serv., 1939, lieut.; cadet, Nig., 1936; ag. chmn., Gaskiya corp., 1946; author of various articles in Geographical Journal on expedition results.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934–1934 | mem. expedit. with Egyptian desert survey | — | [1948, 1949, 1950, 1951] |
| 1 | 1934–1934 | — | Iceland | [1948, 1949, 1950, 1951] |
| 2 | 1934–1935 | survr. and geologist | British East Africa | [1948, 1949, 1950, 1951] |
| 3 | 1936–1936 | cadet | Nigeria | [1948, 1949, 1950, 1951] |
| 4 | 1939–1939 | lieut. | — | [1948, 1949, 1950, 1951] |
| 5 | 1946–1946 | ag. chmn., Gaskiya corp. | — | [1948, 1949, 1950, 1951] |

## Candidate stint `White, D. S___Uganda___1949`

- Staff-list name: **White, D. S** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. S. White | Accountants | Public Works | — | — |
| 1951 | D. S. White | Accountants | Public Works | — | — |

### Deterministic checks: `white_stanhope_b1913` vs `White, D. S___Uganda___1949`

- [PASS] surname_gate: bio 'WHITE' vs stint 'White, D. S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['D', 'S']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `White, F. S___Tanganyika___1953`

- Staff-list name: **White, F. S** | colony: **Tanganyika** | listed 1953–1961 | editions [1953, 1954, 1956, 1957, 1958, 1960, 1961]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | F. S. White | Chief Town Planning Officer | Civil Establishment | — | — |
| 1954 | F. S. White | Chief Town Planning Officer | Civil Establishment | — | — |
| 1956 | F. S. White | Director of Town Planning | Civil Establishment | — | — |
| 1957 | F. S. White | Director of Town Planning | Civil Establishment | — | — |
| 1958 | F. S. White | Director of Town Planning | Civil Establishment | — | — |
| 1960 | F. S. White | Director of Town Planning | Civil Establishment | — | — |
| 1961 | F. S. White | Commissioner for Town Planning | Civil Establishment | — | — |

### Deterministic checks: `white_stanhope_b1913` vs `White, F. S___Tanganyika___1953`

- [PASS] surname_gate: bio 'WHITE' vs stint 'White, F. S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['F', 'S']
- [PASS] age_gate: stint starts 1953, birth 1913 (age 40)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1961
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

