<!-- {"case_id": "case_hemmings_edward-john_b1906", "bio_ids": ["hemmings_edward-john_b1906"], "stint_ids": ["Hemmings, E. J___Trinidad and Tobago___1940"]} -->
# Dossier case_hemmings_edward-john_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hemmings_edward-john_b1906`

- Printed name: **HEMMINGS, Edward John**
- Birth year: 1906 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954])
- Appears in editions: [1937, 1939, 1940, 1948, 1949, 1950, 1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1948-L33279.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954]:**

> HEMMINGS, Edward John, A.I. Nav. Arch.; b. 1906; ed. Masonic Sch., Bushey, master mariner; on war. serv. 1939-42, lieut., R.N.; cargo supt., 1931; asst. harb. mastr., Trin., 1932; harb. mastr. and gen. man., coastal serv., 1947.

**Version `col1937-L61710.v` — printed in editions [1937, 1939, 1940]:**

> HEMMINGS, EDWARD JOHN.—B. 1906; late R.N.R.; cargo supt. and relieving offr., coastal serv., Trinidad, Jan., 1931; astt. harbmr., Jan., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931–1931 | cargo supt. | Trinidad | [1937, 1939, 1940, 1948, 1949, 1950, 1951, 1953, 1954] |
| 1 | 1932–1932 | asst. harb. mastr. | Trinidad | [1937, 1939, 1940, 1948, 1949, 1950, 1951, 1953, 1954] |
| 2 | 1939–1942 | lieut., R.N. | — | [1948, 1949, 1950, 1951, 1953, 1954] |
| 3 | 1947–1947 | harb. mastr. and gen. man., coastal serv. | — | [1948, 1949, 1950, 1951, 1953, 1954] |

## Candidate stint `Hemmings, E. J___Trinidad and Tobago___1940`

- Staff-list name: **Hemmings, E. J** | colony: **Trinidad and Tobago** | listed 1940–1954 | editions [1940, 1949, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | E. J. Hemmings | Assistant Master | Port and Marine | — | — |
| 1949 | E. J. Hemmings | Harbour Master and Superintendent of Lighthouses | Port Services | — | — |
| 1953 | E. J. Hemmings | Harbour Master and Superintendent of Lighthouses | Civil Establishment | — | — |
| 1954 | E. J. Hemmings | Harbour Master and Superintendent of Lighthouses | Civil Establishment | — | — |

### Deterministic checks: `hemmings_edward-john_b1906` vs `Hemmings, E. J___Trinidad and Tobago___1940`

- [PASS] surname_gate: bio 'HEMMINGS' vs stint 'Hemmings, E. J' (exact)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E', 'J']
- [PASS] age_gate: stint starts 1940, birth 1906 (age 34)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1940-1954
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

