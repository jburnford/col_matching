<!-- {"case_id": "case_williams_conrad-veale_b1903", "bio_ids": ["williams_conrad-veale_b1903"], "stint_ids": ["Williams, C. V___St Helena___1950"]} -->
# Dossier case_williams_conrad-veale_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 380 official(s) with this surname in the graph's staff lists; 162 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Williams, C. V___St Helena___1950` is also gate-compatible with biography(ies) outside this case: ['williams_charles_e1884'] (already linked elsewhere or filtered).

## Biography `williams_conrad-veale_b1903`

- Printed name: **WILLIAMS, Conrad Veale**
- Birth year: 1903 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Honours: C.M.G (1956)
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1953-L19584.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> WILLIAMS, C. V., C.M.G. (1956).—b. 1903; ed. St. Olave's Sch. and St. John's Coll., Oxford; cadet, Nig., 1926; admin. offr., cl. II, 1945; cl. I, 1947; staff gr., 1951; N. regn., 1955; o.a.g., 1955. (Nig. Govt. service.)

**Version `col1948-L36896.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WILLIAMS, Conrad Veale.—b. 1903; ed. St. Olave's Sch. and St. John's Coll., Oxford, B.A. (hons.) (Oxon.); cadet, Nig., 1926; admin. offr., cl. II, 1945; cl. I, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | cadet | Nigeria | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1945 | admin. offr., cl. II | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1947 | cl. I | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1951 | staff gr | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1955 | N. regn | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Williams, C. V___St Helena___1950`

- Staff-list name: **Williams, C. V** | colony: **St Helena** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | C. V. Williams | Justice of the Peace | Ascension | — | — |
| 1951 | C. V. Williams | Justice of the Peace | ASCENSION | — | — |

### Deterministic checks: `williams_conrad-veale_b1903` vs `Williams, C. V___St Helena___1950`

- [PASS] surname_gate: bio 'WILLIAMS' vs stint 'Williams, C. V' (exact)
- [PASS] initials: bio ['C', 'V'] ~ stint ['C', 'V']
- [PASS] age_gate: stint starts 1950, birth 1903 (age 47)
- [FAIL] colony: no placed event resolves to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

