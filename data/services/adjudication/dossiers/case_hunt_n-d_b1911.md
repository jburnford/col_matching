<!-- {"case_id": "case_hunt_n-d_b1911", "bio_ids": ["hunt_n-d_b1911"], "stint_ids": ["Hunt, N. D___Northern Rhodesia___1949"]} -->
# Dossier case_hunt_n-d_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 52 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hunt_n-d_b1911`

- Printed name: **HUNT, N. D**
- Birth year: 1911 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Honours: M.M (1941)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1956-L22066.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> HUNT, N. D., M.M. (1941).—b. 1911; ed. Newton Abbot Gram. Sch. and Seale-Hayne Agric. Coll.; mil. serv., 1939-45, capt.; dist. asst., N. Rhod., 1946; labr. offr., 1948; senr. labr. offr., 1954; asst. labr. comsnr., 1955. (Zambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | dist. asst. | Northern Rhodesia | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1948 | labr. offr | Northern Rhodesia *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1954 | senr. labr. offr | Northern Rhodesia *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1955 | asst. labr. comsnr | Northern Rhodesia *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Hunt, N. D___Northern Rhodesia___1949`

- Staff-list name: **Hunt, N. D** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | N. D. Hunt | — | Mines and Labour | — | — |
| 1951 | N. D. Hunt | — | Labour and Mines | — | — |

### Deterministic checks: `hunt_n-d_b1911` vs `Hunt, N. D___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'HUNT' vs stint 'Hunt, N. D' (exact)
- [PASS] initials: bio ['N', 'D'] ~ stint ['N', 'D']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 4 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
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

