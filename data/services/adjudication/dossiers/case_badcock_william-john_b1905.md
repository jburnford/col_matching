<!-- {"case_id": "case_badcock_william-john_b1905", "bio_ids": ["badcock_william-john_b1905"], "stint_ids": ["Badcock, W. J___Uganda___1933"]} -->
# Dossier case_badcock_william-john_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `badcock_william-john_b1905`

- Printed name: **BADCOCK, William John**
- Birth year: 1905 (attested in editions [1948, 1949, 1950, 1951])
- Honours: A.I.C.T.A, N.D.A
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L30915.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BADCOCK, William John, dip. agric. (Reading), N.D.A., A.I.C.T.A.—b. 1905; ed. Dunkeved Coll., Launceston, Reading and Camb. Unv., and I.C.T.A.; on mil. serv. 1940-43 and 1945-46, maj.; agric. offr., col. serv., 1931; seconded as senr. agric. offr., B. Sol. Is. Prot., 1945; ch. soil conserv. offr., Nyasa., 1948; author of An Ecological Study on Sugar.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | agric. offr., col. serv | — | [1948, 1949, 1950, 1951] |
| 1 | 1945 | seconded as senr. agric. offr., B. Sol. Is. Prot | — | [1948, 1949, 1950, 1951] |
| 2 | 1948 | ch. soil conserv. offr. | Nyasaland | [1948, 1949, 1950, 1951] |

## Candidate stint `Badcock, W. J___Uganda___1933`

- Staff-list name: **Badcock, W. J** | colony: **Uganda** | listed 1933–1940 | editions [1933, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | W. J. Badcock | Agricultural Officer | Agricultural Department | — | — |
| 1936 | W. J. Badcock | Agricultural Officers | Agricultural Department | — | — |
| 1937 | W. J. Badcock | Agricultural Officer | Agricultural Department | — | — |
| 1939 | W. J. Badcock | Agricultural Officer | Agricultural Department | — | — |
| 1940 | W. J. Badcock | Agricultural Officer | Agricultural Department | — | — |

### Deterministic checks: `badcock_william-john_b1905` vs `Badcock, W. J___Uganda___1933`

- [PASS] surname_gate: bio 'BADCOCK' vs stint 'Badcock, W. J' (exact)
- [PASS] initials: bio ['W', 'J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1933, birth 1905 (age 28)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1940
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

