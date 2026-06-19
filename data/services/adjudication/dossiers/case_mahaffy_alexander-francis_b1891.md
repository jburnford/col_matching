<!-- {"case_id": "case_mahaffy_alexander-francis_b1891", "bio_ids": ["mahaffy_alexander-francis_b1891"], "stint_ids": ["Mahaffy, Arthur___Leeward Islands___1917"]} -->
# Dossier case_mahaffy_alexander-francis_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Mahaffy, Arthur___Leeward Islands___1917` is also gate-compatible with biography(ies) outside this case: ['mahaffy_arthur-wm_b1869'] (already linked elsewhere or filtered).

## Biography `mahaffy_alexander-francis_b1891`

- Printed name: **MAHAFFY, Alexander Francis**
- Birth year: 1891 (attested in editions [1948, 1949])
- Honours: C.M.G. (1942)
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L34443.v` — printed in editions [1948, 1949]:**

> MAHAFFY, Alexander Francis, C.M.G. (1942), B.A. (Toronto), M.D. (Toronto), D.T.M. (Liv.), D.P.H. (Toronto)—b. 1891; on mil. serv., 1915-18, lieut.; Rockefeller Foundtn.—Brazil, 1923-25, W. Africa, 1925-34, E. Africa, 1936-46; dir., col. med. research, 1947; author of various papers on the epidemiology of yellow fever.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1918 | lieut. | — | [1948, 1949] |
| 1 | 1923–1925 | — | Brazil | [1948, 1949] |
| 2 | 1925–1934 | — | West Africa | [1948, 1949] |
| 3 | 1936–1946 | — | East Africa | [1948, 1949] |
| 4 | 1947 | dir., col. med. research | — | [1948, 1949] |

## Candidate stint `Mahaffy, Arthur___Leeward Islands___1917`

- Staff-list name: **Mahaffy, Arthur** | colony: **Leeward Islands** | listed 1917–1928 | editions [1917, 1918, 1919, 1920, 1922, 1923, 1924, 1925, 1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | Arthur Mahaffy | — | Administration | — | — |

### Deterministic checks: `mahaffy_alexander-francis_b1891` vs `Mahaffy, Arthur___Leeward Islands___1917`

- [PASS] surname_gate: bio 'MAHAFFY' vs stint 'Mahaffy, Arthur' (exact)
- [PASS] initials: bio ['A', 'F'] ~ stint ['A']
- [PASS] age_gate: stint starts 1917, birth 1891 (age 26)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1928
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

