<!-- {"case_id": "case_keith_edward-alexander_b1906", "bio_ids": ["keith_edward-alexander_b1906"], "stint_ids": ["Keith, E. A___Northern Rhodesia___1939"]} -->
# Dossier case_keith_edward-alexander_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `keith_edward-alexander_b1906`

- Printed name: **KEITH, Edward Alexander**
- Birth year: 1906 (attested in editions [1957, 1958, 1959, 1960])
- Honours: M.B
- Appears in editions: [1950, 1951, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1957-L24628.v` — printed in editions [1957, 1958, 1959, 1960]:**

> KEITH, E. A.—b. 1906; ed. High Sch., Arbroath, Univ. Coll., Dundee, St. Andrews and Edin. Univs.; mil. serv., 1939–45, lt.-col.; M.O., N. Rhod., 1938; specialist, 1951; secon. fedl. govt., 1954; ret. 1959.

**Version `col1950-L36938.v` — printed in editions [1950, 1951]:**

> KEITH, Edward Alexander, M.B., Ch.B.—b. 1906; ed. High Sch., Arbroath, Univ. Coll., Dundee, Univ. of St. Andrews and Edin. Univ.; on mil. serv., 1939-45, lieut.-col.; med. offr., N. Rhod., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | M.O. | Northern Rhodesia | [1950, 1951, 1957, 1958, 1959, 1960] |
| 1 | 1951 | specialist | Northern Rhodesia *(inherited from previous clause)* | [1957, 1958, 1959, 1960] |
| 2 | 1954 | secon. fedl. govt | Northern Rhodesia *(inherited from previous clause)* | [1957, 1958, 1959, 1960] |
| 3 | 1959 | ret | Northern Rhodesia *(inherited from previous clause)* | [1957, 1958, 1959, 1960] |

## Candidate stint `Keith, E. A___Northern Rhodesia___1939`

- Staff-list name: **Keith, E. A** | colony: **Northern Rhodesia** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | E. A. Keith | Medical Officer | Medical | — | — |
| 1940 | E. A. Keith | Medical Officer | Health | — | — |

### Deterministic checks: `keith_edward-alexander_b1906` vs `Keith, E. A___Northern Rhodesia___1939`

- [PASS] surname_gate: bio 'KEITH' vs stint 'Keith, E. A' (exact)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1939, birth 1906 (age 33)
- [PASS] colony: 4 placed event(s) resolve to 'Northern Rhodesia'
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

