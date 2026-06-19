<!-- {"case_id": "case_agg_arthur-desmond_b1912", "bio_ids": ["agg_arthur-desmond_b1912"], "stint_ids": ["Agg, A. D___Northern Rhodesia___1949"]} -->
# Dossier case_agg_arthur-desmond_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `agg_arthur-desmond_b1912`

- Printed name: **AGG, Arthur Desmond**
- Birth year: 1912 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1965, 1966])
- Honours: A.R.I.B.A
- Appears in editions: [1951, 1956, 1957, 1958, 1959, 1960, 1961, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L19344.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1965, 1966]:**

> AGG, A. D.—b. 1912; ed. S.A. Collegiate Sch., Cape Town; mil. serv., 1939–40, 2nd lieut.; archt. asst., P.W.D., N. Rhod., 1938; asst. archt., 1945; archt., 1949; senr. archt., 1951; asst. D.P.W. (buildings), Nyasa., 1955; ret. re-appt. sen. archt., E. Nig., 1959; ch. archt., 1961. (Nig. Govt. service.)

**Version `col1951-L35556.v` — printed in editions [1951]:**

> AGG, Arthur Desmond, A.R.I.B.A., M.I.A. (S.A.).—b. 1912; ed. South African Coll. Sch.; on mil. serv. 1939-40, 2nd lieut.; arch. asst., N. Rhod., 1938; asst. arch., 1945; arch., 1949; mem., arch. and quan. survrs. registn. bd., N. Rhod.; author of a handbook on semi-permanent housing.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | archt. asst., P.W.D. | Northern Rhodesia | [1951, 1956, 1957, 1958, 1959, 1960, 1961, 1965, 1966] |
| 1 | 1945 | asst. archt | Northern Rhodesia *(inherited from previous clause)* | [1951, 1956, 1957, 1958, 1959, 1960, 1961, 1965, 1966] |
| 2 | 1949 | archt | Northern Rhodesia *(inherited from previous clause)* | [1951, 1956, 1957, 1958, 1959, 1960, 1961, 1965, 1966] |
| 3 | 1951 | senr. archt | Northern Rhodesia *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1965, 1966] |
| 4 | 1955 | asst. D.P.W. (buildings) | Nyasaland | [1956, 1957, 1958, 1959, 1960, 1961, 1965, 1966] |
| 5 | 1959 | ret. re-appt. sen. archt. | Eastern Nigeria | [1956, 1957, 1958, 1959, 1960, 1961, 1965, 1966] |
| 6 | 1961 | ch. archt | Eastern Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1965, 1966] |

## Candidate stint `Agg, A. D___Northern Rhodesia___1949`

- Staff-list name: **Agg, A. D** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. D. Agg | Assistant Architects | PUBLIC WORKS | — | — |
| 1951 | A. D. Agg | Architects | Public Works | — | — |

### Deterministic checks: `agg_arthur-desmond_b1912` vs `Agg, A. D___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'AGG' vs stint 'Agg, A. D' (exact)
- [PASS] initials: bio ['A', 'D'] ~ stint ['A', 'D']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [PASS] colony: 4 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 67 vs bar 60: 'asst. archt' ~ 'Assistant Architects'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1951] pos~60 (bar: >=2)
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

