<!-- {"case_id": "case_vernall_richard-john_b1901", "bio_ids": ["vernall_richard-john_b1901"], "stint_ids": ["Vernall, R. J___Hong Kong___1927", "Vernall, R. J___Hong Kong___1949"]} -->
# Dossier case_vernall_richard-john_b1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `vernall_richard-john_b1901`

- Printed name: **VERNALL, RICHARD JOHN**
- Birth year: 1901 (attested in editions [1936])
- Honours: A.R.I.B.A
- Appears in editions: [1936, 1937, 1939, 1940, 1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1936-L65348.v` — printed in editions [1936]:**

> VERNALL, RICHARD JOHN, A.R.I.B.A.—B. 1901; archt., P.W.D., Hong Kong, 1925; ag. tech. sec., P.W.D., 1934.

**Version `col1948-L36577.v` — printed in editions [1948, 1949, 1950]:**

> VERNALL, Richard John, O.B.E. (mil.); A.R.I.B.A.; M.I.Struct.E.—b. 1901; ed. Marling Sch., Stroud. Univ. Coll., London, on naval serv. 1939–46, commr., H.K., R.N.V.R. (desps.); archt., P.W.D., H.K., 1925; ag. tech. sec., 1934.

**Version `col1937-L65520.v` — printed in editions [1937]:**

> VERNALL, Richard John, M.A.—B. 1901; archt., P.W.D., Hong Kong; tech. sec., P.W.D., 1934.

**Version `col1939-L71431.v` — printed in editions [1939, 1940]:**

> VERNALL, RICHARD JOHN, A.R.I.B.A., M.I. Struct. E.—B. 1901; ed. Marling Schl., Stroud, archt., P.W.D., Hong Kong, 1925; ag. tech. sec., P.W.D., 1934; Lieut. Cmdr., H.K.N.V.F.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | archt., P.W.D. | Hong Kong | [1936, 1948, 1949, 1950] |
| 1 | 1934 | ag. tech. sec., P.W.D | Hong Kong *(inherited from previous clause)* | [1936, 1937, 1939, 1940, 1948, 1949, 1950] |

## Candidate stint `Vernall, R. J___Hong Kong___1927`

- Staff-list name: **Vernall, R. J** | colony: **Hong Kong** | listed 1927–1939 | editions [1927, 1928, 1929, 1931, 1932, 1933, 1934, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | R. J. Vernall | Engineers | Architectural | — | — |
| 1928 | R. J. Vernall | Engineers | Architectural | — | — |
| 1929 | R. J. Vernall | Engineers | Architectural | — | — |
| 1931 | R. J. Vernall | Engineer | Architectural | — | — |
| 1932 | R. J. Vernall | Architect | Public Works Department | — | — |
| 1933 | R. J. Vernall | Architects | Public Works Department | — | — |
| 1934 | R. J. Vernall | Architect | Public Works Department | — | — |
| 1937 | R. J. Vernall | Architect | Public Works Department | — | — |
| 1939 | R. J. Vernall | Architect | Public Works Department | — | — |

### Deterministic checks: `vernall_richard-john_b1901` vs `Vernall, R. J___Hong Kong___1927`

- [PASS] surname_gate: bio 'VERNALL' vs stint 'Vernall, R. J' (exact)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1927, birth 1901 (age 26)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1927-1939
- [FAIL] position_sim: best 56 vs bar 60: 'archt., P.W.D.' ~ 'Architect'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Vernall, R. J___Hong Kong___1949`

- Staff-list name: **Vernall, R. J** | colony: **Hong Kong** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. J. Vernall | Architect | Public Works | — | — |
| 1949 | R. J. Vernall | Commanding Officer | Hong Kong Naval Volunteer Force | — | — |
| 1950 | R. J. Vernall | Commanding Officer | Hong Kong Naval Force | — | — |
| 1950 | R. J. Vernall | Building Surveyors | Public Works | — | — |

### Deterministic checks: `vernall_richard-john_b1901` vs `Vernall, R. J___Hong Kong___1949`

- [PASS] surname_gate: bio 'VERNALL' vs stint 'Vernall, R. J' (exact)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

