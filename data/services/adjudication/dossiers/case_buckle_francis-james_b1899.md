<!-- {"case_id": "case_buckle_francis-james_b1899", "bio_ids": ["buckle_francis-james_b1899"], "stint_ids": ["Buckle, F___Hong Kong___1949", "Buckle, F___Nyasaland___1928"]} -->
# Dossier case_buckle_francis-james_b1899

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `buckle_francis-james_b1899`

- Printed name: **BUCKLE, Francis James**
- Birth year: 1899 (attested in editions [1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L34030.v` — printed in editions [1950, 1951]:**

> BUCKLE, Francis James.—b. 1899; Royal Sany. Assoc. of Scotland sany. sc. cert.; on naval serv., 1917–19 and 1939–40; sany. supt., G.C., 1927; ch. sany. supt., 1944.

**Version `col1948-L31489.v` — printed in editions [1948, 1949]:**

> BUCKLE, Francis James.—b. 1899; cert. of sany. sci. of the Royal Sany. Assoc. of Scotland; sany. supt., gr. II, G.C., 1927; gr. I, 1936; ch. sany. supt., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917–1919 | on naval serv. | — | [1950, 1951] |
| 1 | 1927 | sany. supt. | Gold Coast | [1948, 1949, 1950, 1951] |
| 2 | 1936 | gr. I | Gold Coast *(inherited from previous clause)* | [1948, 1949] |
| 3 | 1939–1940 | on naval serv. | — | [1950, 1951] |
| 4 | 1944 | ch. sany. supt. | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Buckle, F___Hong Kong___1949`

- Staff-list name: **Buckle, F** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | F. Buckle | Chief Instructor in Engineering | Education Department | — | — |
| 1950 | F. Buckle | Chief Instructor in Engineering | Education | — | — |
| 1951 | F. Buckle | Technical Instructor in Engineering | Education | — | — |

### Deterministic checks: `buckle_francis-james_b1899` vs `Buckle, F___Hong Kong___1949`

- [PASS] surname_gate: bio 'BUCKLE' vs stint 'Buckle, F' (exact)
- [PASS] initials: bio ['F', 'J'] ~ stint ['F']
- [PASS] age_gate: stint starts 1949, birth 1899 (age 50)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Buckle, F___Nyasaland___1928`

- Staff-list name: **Buckle, F** | colony: **Nyasaland** | listed 1928–1936 | editions [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | F. Buckle | Assistant Engineer | Marine Transport | — | — |
| 1929 | F. Buckle | Assistant Engineer | Marine Transport | — | — |
| 1930 | F. Buckle | Assistant Engineer | Marine Transport | — | — |
| 1931 | F. Buckle | Engineer | Marine Transport | — | — |
| 1932 | F. Buckle | Engineer | Marine Transport | — | — |
| 1933 | F. Buckle | Engineer | Marine Transport | — | — |
| 1934 | F. Buckle | Engineer | Marine Transport | — | — |
| 1936 | F. Buckle | Engineer | Marine Transport | — | — |

### Deterministic checks: `buckle_francis-james_b1899` vs `Buckle, F___Nyasaland___1928`

- [PASS] surname_gate: bio 'BUCKLE' vs stint 'Buckle, F' (exact)
- [PASS] initials: bio ['F', 'J'] ~ stint ['F']
- [PASS] age_gate: stint starts 1928, birth 1899 (age 29)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1936
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

