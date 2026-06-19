<!-- {"case_id": "case_gill_edwin_b1896", "bio_ids": ["gill_edwin_b1896"], "stint_ids": ["Gill, L. E___Gold Coast___1949", "Gill, L. E___Trinidad and Tobago___1937"]} -->
# Dossier case_gill_edwin_b1896

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 47 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gill_edwin_b1896'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Gill, L. E___Gold Coast___1949` is also gate-compatible with biography(ies) outside this case: ['gill_leslie-edwin_b1907'] (already linked elsewhere or filtered).
- NOTE: stint `Gill, L. E___Trinidad and Tobago___1937` is also gate-compatible with biography(ies) outside this case: ['gill_leslie-edwin_b1907'] (already linked elsewhere or filtered).

## Biography `gill_edwin_b1896`

- Printed name: **GILL, EDWIN**
- Birth year: 1896 (attested in editions [1932, 1933, 1934, 1935, 1936, 1937, 1940])
- Appears in editions: [1932, 1933, 1934, 1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1932-L60491.v` — printed in editions [1932, 1933, 1934, 1935, 1936, 1937, 1940]:**

> GILL, EDWIN.—B. 1896; on naval serv., 1915-19; apptd. after compet. exam., cler. offr., C.O., 12th July, 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1919 | on naval serv | — | [1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 1 | 1926 | apptd. after compet. exam., cler. offr. | Colonial Office | [1932, 1933, 1934, 1935, 1936, 1937, 1940] |

## Candidate stint `Gill, L. E___Gold Coast___1949`

- Staff-list name: **Gill, L. E** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. E. Gill | Chief Draughtsman | Survey Department | — | — |
| 1950 | L. E. Gill | Chief Draughtsman | SURVEY DEPARTMENT | — | — |
| 1951 | L. E. Gill | Chief Draughtsman | Survey Department | — | — |

### Deterministic checks: `gill_edwin_b1896` vs `Gill, L. E___Gold Coast___1949`

- [PASS] surname_gate: bio 'GILL' vs stint 'Gill, L. E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['L', 'E']
- [PASS] age_gate: stint starts 1949, birth 1896 (age 53)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Gill, L. E___Trinidad and Tobago___1937`

- Staff-list name: **Gill, L. E** | colony: **Trinidad and Tobago** | listed 1937–1939 | editions [1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | L. E. Gill | Draughtsman | Survey Section | — | — |
| 1939 | L. E. Gill | Draughtsmen | Military Department | — | — |

### Deterministic checks: `gill_edwin_b1896` vs `Gill, L. E___Trinidad and Tobago___1937`

- [PASS] surname_gate: bio 'GILL' vs stint 'Gill, L. E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['L', 'E']
- [PASS] age_gate: stint starts 1937, birth 1896 (age 41)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1939
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

