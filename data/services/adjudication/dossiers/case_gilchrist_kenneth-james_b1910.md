<!-- {"case_id": "case_gilchrist_kenneth-james_b1910", "bio_ids": ["gilchrist_kenneth-james_b1910"], "stint_ids": ["Gilchrist, K. J___Gibraltar___1939"]} -->
# Dossier case_gilchrist_kenneth-james_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gilchrist_kenneth-james_b1910`

- Printed name: **GILCHRIST, Kenneth James**
- Birth year: 1910 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: F.R.C.S, L.R.C.P, M.B
- Appears in editions: [1937, 1940, 1948, 1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L21374.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> GILCHRIST, K. J.—b. 1910; ed. Dulwich Coll., Guy's Hosp. Med. Sch. and London Univ.; M.O., Gib., 1936; surg. spec., Fiji, 1946; Nig., 1949; Fiji, 1953; lectr., surgery and anatomy, central med. sch., 1954; author of various articles in B.M.J.

**Version `col1948-L32829.v` — printed in editions [1948, 1949, 1950, 1951]:**

> GILCHRIST, Kenneth James, M.B., B.S. (Lond.), L.R.C.P., F.R.C.S. (Eng.).—b. 1910; ed. Dulwich Coll., Guy's Hosp., London Univ.; med. offr., Gib., 1936; surg. specialist, Fiji, 1946.

**Version `col1937-L61180.v` — printed in editions [1937, 1940]:**

> GILCHRIST, KENNETH JAMES, M.B., B.S. (Lond.) 1933, M.R.C.S. (Eng.), L.R.C.P. (Lond.), F.R.C.S.—B. 1910; med. offr., Gibraltar, 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | M.O. | Gibraltar | [1937, 1940, 1948, 1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1946 | surg. spec. | Fiji | [1948, 1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1949 | surg. spec. | Nigeria | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1953 | surg. spec. | Fiji | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1954 | lectr., surgery and anatomy, central med. sch | Fiji *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Gilchrist, K. J___Gibraltar___1939`

- Staff-list name: **Gilchrist, K. J** | colony: **Gibraltar** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | K. J. Gilchrist | Medical Officer | Medical Department | — | — |
| 1940 | K. J. Gilchrist | Medical Officer | Medical Department | — | — |

### Deterministic checks: `gilchrist_kenneth-james_b1910` vs `Gilchrist, K. J___Gibraltar___1939`

- [PASS] surname_gate: bio 'GILCHRIST' vs stint 'Gilchrist, K. J' (exact)
- [PASS] initials: bio ['K', 'J'] ~ stint ['K', 'J']
- [PASS] age_gate: stint starts 1939, birth 1910 (age 29)
- [PASS] colony: 1 placed event(s) resolve to 'Gibraltar'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

