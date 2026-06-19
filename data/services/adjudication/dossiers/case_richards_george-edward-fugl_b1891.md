<!-- {"case_id": "case_richards_george-edward-fugl_b1891", "bio_ids": ["richards_george-edward-fugl_b1891"], "stint_ids": ["Richards, G. E. F___Leeward Islands___1932", "Richards, G. E. F___Windward Islands___1936"]} -->
# Dossier case_richards_george-edward-fugl_b1891

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 86 official(s) with this surname in the graph's staff lists; 38 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `richards_george-edward-fugl_b1891`

- Printed name: **RICHARDS, GEORGE EDWARD FUGL**
- Birth year: 1891 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L70133.v` — printed in editions [1939, 1940]:**

> RICHARDS, GEORGE EDWARD FUGL.—B. 1891; ed. Portsmouth Gram. Sch., Chicago Univ., and Downing Coll., Cambridge (B.A., LL.B. Cantab.); called to bar, Middle Temple, 1923; ag. mag., Grenada, 1926-27, St. Lucia, 1927-8; mag., Dominica, 1928; cr. atty., 1931; ch. just. and mag., St. Lucia, Jan., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923–1923 | called to bar | — | [1939, 1940] |
| 1 | 1926–1927 | ag. mag. | Grenada | [1939, 1940] |
| 2 | 1927–1928 | ag. mag. | St. Lucia | [1939, 1940] |
| 3 | 1928–1928 | mag. | Dominica | [1939, 1940] |
| 4 | 1931–1931 | cr. atty. | — | [1939, 1940] |
| 5 | 1935 | ch. just. and mag. | St. Lucia | [1939, 1940] |

## Candidate stint `Richards, G. E. F___Leeward Islands___1932`

- Staff-list name: **Richards, G. E. F** | colony: **Leeward Islands** | listed 1932–1933 | editions [1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | G. E. F. Richards | Attorney-General (acting) | Executive Council | — | — |
| 1932 | G. E. F. Richards | Crown Attorney (acting) | Judicial Establishment | — | — |
| 1932 | G. E. F. Richards | Member | Legislative Council | — | — |
| 1933 | G. E. F. Richards | Crown Attorney | Executive Council | — | — |
| 1933 | G. E. F. Richards | Crown Attorney | Judicial Establishment | — | — |

### Deterministic checks: `richards_george-edward-fugl_b1891` vs `Richards, G. E. F___Leeward Islands___1932`

- [PASS] surname_gate: bio 'RICHARDS' vs stint 'Richards, G. E. F' (exact)
- [PASS] initials: bio ['G', 'E', 'F'] ~ stint ['G', 'E', 'F']
- [PASS] age_gate: stint starts 1932, birth 1891 (age 41)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1933
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Richards, G. E. F___Windward Islands___1936`

- Staff-list name: **Richards, G. E. F** | colony: **Windward Islands** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | G. E. F. Richards | Chief Justice and Magistrate 1st District | Judicial | — | — |
| 1937 | G. E. F. Richards | Chief Justice and Magistrate 1st District | Judicial | — | — |
| 1939 | G. E. F. Richards | Chief Justice and Magistrate 1st District | Judicial | — | — |

### Deterministic checks: `richards_george-edward-fugl_b1891` vs `Richards, G. E. F___Windward Islands___1936`

- [PASS] surname_gate: bio 'RICHARDS' vs stint 'Richards, G. E. F' (exact)
- [PASS] initials: bio ['G', 'E', 'F'] ~ stint ['G', 'E', 'F']
- [PASS] age_gate: stint starts 1936, birth 1891 (age 45)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
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

