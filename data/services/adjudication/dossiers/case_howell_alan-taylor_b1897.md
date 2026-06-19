<!-- {"case_id": "case_howell_alan-taylor_b1897", "bio_ids": ["howell_alan-taylor_b1897"], "stint_ids": ["Howell, A. T___Tanganyika___1952"]} -->
# Dossier case_howell_alan-taylor_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 42 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `howell_alan-taylor_b1897`

- Printed name: **HOWELL, Alan Taylor**
- Birth year: 1897 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960])
- Honours: B.A, C.B.E (1953), M.B
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1953-L17813.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960]:**

> HOWELL, A. T., C.B.E. (1953).—b. 1897; ed. Mill Hill Sch., Caius Coll., Camb., and St. Thomas's Hosp., Lond.; mil. serv., 1915-19, lieut.; med. offr., Ken., 1926; asst. D.M.S., 1946; D.D.M.S., N. Rhod., 1947; D.M.S., Tang., 1950; ret., re-app. med. research sec., E.A.H.C., 1956.

**Version `col1948-L33474.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HOWELL, Alan Taylor, B.A., M.B., B.Ch. (Cantab.), M.R.C.S. (Eng.), L.R.C.P. (Lond.), D.T.M. & H. (Liv.)—b. 1897; ed. Mill Hill Sch., Gonville and Caius Coll., Camb. and St. Thos. Hosp.; on mil. serv., 1915-19, lieut.; med. offr., Ken., 1926; asst. D.M.S., 1946; D.D.M.S., N. Rhod., 1947; D.M.S., Tang., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | med. offr. | Kenya | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 1 | 1946 | asst. D.M.S | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 2 | 1947 | D.D.M.S. | Northern Rhodesia | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 3 | 1950 | D.M.S. | Tanganyika | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 4 | 1956 | ret., re-app. med. research sec., E.A.H.C | Tanganyika *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |

## Candidate stint `Howell, A. T___Tanganyika___1952`

- Staff-list name: **Howell, A. T** | colony: **Tanganyika** | listed 1952–1954 | editions [1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | A. T. Howell | Director of Medical Services | Civil Establishment | — | — |
| 1953 | A. T. Howell | Director of Medical Services | Civil Establishment | — | — |
| 1954 | A. T. Howell | Director of Medical Services | Civil Establishment | — | — |

### Deterministic checks: `howell_alan-taylor_b1897` vs `Howell, A. T___Tanganyika___1952`

- [PASS] surname_gate: bio 'HOWELL' vs stint 'Howell, A. T' (exact)
- [PASS] initials: bio ['A', 'T'] ~ stint ['A', 'T']
- [PASS] age_gate: stint starts 1952, birth 1897 (age 55)
- [PASS] colony: 2 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1952-1954
- [FAIL] position_sim: best 19 vs bar 60: 'D.M.S.' ~ 'Director of Medical Services'
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

