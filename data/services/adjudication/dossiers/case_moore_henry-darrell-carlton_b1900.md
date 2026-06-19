<!-- {"case_id": "case_moore_henry-darrell-carlton_b1900", "bio_ids": ["moore_henry-darrell-carlton_b1900"], "stint_ids": ["Moore, H. D. C___Leeward Islands___1922", "Moore, H. D. C___Leeward Islands___1931"]} -->
# Dossier case_moore_henry-darrell-carlton_b1900

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 128 official(s) with this surname in the graph's staff lists; 38 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `moore_henry-darrell-carlton_b1900`

- Printed name: **MOORE, Henry Darrell Carlton**
- Birth year: 1900 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L34751.v` — printed in editions [1948, 1949, 1950, 1951]:**

> MOORE, Henry Darrell Carlton.—b. 1900; ed. Antigua Gram. Sch.; on mil. serv. 1924–29; inspr. of wks., Antigua, 1921; supt. of tels., 1930; warden and mag., Barbuda, 1931; supt. tels., Antigua, 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | inspr. of wks. | Antigua | [1948, 1949, 1950, 1951] |
| 1 | 1930 | supt. of tels | Antigua *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1931 | warden and mag. | Barbuda | [1948, 1949, 1950, 1951] |
| 3 | 1935 | supt. tels. | Antigua | [1948, 1949, 1950, 1951] |

## Candidate stint `Moore, H. D. C___Leeward Islands___1922`

- Staff-list name: **Moore, H. D. C** | colony: **Leeward Islands** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | H. D. C. Moore | Overseers of Roads and Works | Public Works Department | — | — |
| 1923 | H. D. C. Moore | Overseer of Roads and Works | Public Works Department | — | — |

### Deterministic checks: `moore_henry-darrell-carlton_b1900` vs `Moore, H. D. C___Leeward Islands___1922`

- [PASS] surname_gate: bio 'MOORE' vs stint 'Moore, H. D. C' (exact)
- [PASS] initials: bio ['H', 'D', 'C'] ~ stint ['H', 'D', 'C']
- [PASS] age_gate: stint starts 1922, birth 1900 (age 22)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Moore, H. D. C___Leeward Islands___1931`

- Staff-list name: **Moore, H. D. C** | colony: **Leeward Islands** | listed 1931–1940 | editions [1931, 1932, 1933, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | H. D. C. Moore | Superintendent of Telephones | Telephone Department | — | — |
| 1932 | H. D. C. Moore | Superintendent of Telephones | Telephone Department | — | — |
| 1933 | H. D. C. Moore | Warden (Senior Clerk) | BARBUDA | — | — |
| 1936 | H. D. C. Moore | Superintendent of Telephones | Telephone Department | — | — |
| 1937 | H. D. C. Moore | Superintendent of Telephones | Telephone Department | — | — |
| 1939 | H. D. C. Moore | Superintendent of Telephones | Telephone Department | — | — |
| 1940 | H. D. C. Moore | Superintendent of Telephones | Telephone Department | — | — |

### Deterministic checks: `moore_henry-darrell-carlton_b1900` vs `Moore, H. D. C___Leeward Islands___1931`

- [PASS] surname_gate: bio 'MOORE' vs stint 'Moore, H. D. C' (exact)
- [PASS] initials: bio ['H', 'D', 'C'] ~ stint ['H', 'D', 'C']
- [PASS] age_gate: stint starts 1931, birth 1900 (age 31)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1940
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

