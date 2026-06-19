<!-- {"case_id": "case_miller_hugh-clinton_b1912", "bio_ids": ["miller_hugh-clinton_b1912"], "stint_ids": ["Miller, H. C___Jamaica___1937"]} -->
# Dossier case_miller_hugh-clinton_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 106 official(s) with this surname in the graph's staff lists; 38 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `miller_hugh-clinton_b1912`

- Printed name: **MILLER, Hugh Clinton**
- Birth year: 1912 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1949-L34313.v` — printed in editions [1949, 1950, 1951]:**

> MILLER, Hugh Clinton, B.Sc. (1st cl. hons.).—b. 1912; ed. J'ca Coll. (agric. schol.), I.C.T.A. (dip. agric.), and McGill Univ.; cadet, Canadian O.T.C., 1943-44; apptd. col. serv., J'ca., 1934; o/c., tobacco dev. scheme, 1939; agric. offr., gr. II, 1943; gr. I, 1945; hdmstr., J'ca. sch. of agric., 1948; sec., standing comteee on co-ord. of agric. servs. in J'ca., 1939.

**Version `col1957-L25705.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> MILLER, H. C.—b. 1912; ed. J'ca Coll., I.C.T.A. and McGill Univ.; apptd. J'ca, 1934; senr. asst. master, J'ca Sch. of Agric., 1941; agric. offr., 1943; headmr., J'ca Sch. of Agric., 1948; chmn., Yallahs Valley land authy., 1951; dir. of agric., 1956; redesig. chief tech. offr., min. of agric. and lands, J'ca, 1957. (J'ca Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | apptd. col. serv. | Jamaica | [1949, 1950, 1951] |
| 1 | 1934 | apptd. J'ca | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1939 | o/c., tobacco dev. scheme | Jamaica *(inherited from previous clause)* | [1949, 1950, 1951] |
| 3 | 1941 | senr. asst. master, J'ca Sch. of Agric | Jamaica | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1943–1944 | cadet, Canadian O.T.C | — | [1949, 1950, 1951] |
| 5 | 1943 | agric. offr., gr. II | Jamaica *(inherited from previous clause)* | [1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 6 | 1945 | gr. I | Jamaica *(inherited from previous clause)* | [1949, 1950, 1951] |
| 7 | 1948 | hdmstr., J'ca. sch. of agric | Jamaica | [1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 8 | 1951 | chmn., Yallahs Valley land authy | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 9 | 1956 | dir. of agric | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 10 | 1957 | redesig. chief tech. offr., min. of agric. and lands | Jamaica | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Miller, H. C___Jamaica___1937`

- Staff-list name: **Miller, H. C** | colony: **Jamaica** | listed 1937–1940 | editions [1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | H. C. Miller | Junior Agricultural Officers | Department of Science and Agriculture | — | — |
| 1940 | H. C. Miller | Officer-in-charge | Marketing Department | — | — |

### Deterministic checks: `miller_hugh-clinton_b1912` vs `Miller, H. C___Jamaica___1937`

- [PASS] surname_gate: bio 'MILLER' vs stint 'Miller, H. C' (exact)
- [PASS] initials: bio ['H', 'C'] ~ stint ['H', 'C']
- [PASS] age_gate: stint starts 1937, birth 1912 (age 25)
- [PASS] colony: 9 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 49 vs bar 60: 'senr. asst. master, J'ca Sch. of Agric' ~ 'Junior Agricultural Officers'
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

