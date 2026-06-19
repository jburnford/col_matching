<!-- {"case_id": "case_crichton_g-e_b1918", "bio_ids": ["crichton_g-e_b1918"], "stint_ids": ["Crichton, G. E___Sierra Leone___1949"]} -->
# Dossier case_crichton_g-e_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `crichton_g-e_b1918`

- Printed name: **CRICHTON, G. E**
- Birth year: 1918 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L22086.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> CRICHTON, G. E.—b. 1918; ed. Bromsgrove Sch., and Edin. Univ.; mil. serv., 1939-43; temp. asst. consvr., forests, S.L., 1943; asst. consvr., 1947; senr. asst. consvr., 1955; Nyasa., 1956; working plans offr., 1957; senr. asst. consvr., forests, 1962; consvr., forests, 1964. (Malawi Govt. service.)

**Version `col1956-L20626.v` — printed in editions [1956, 1957, 1958]:**

> CRICHTON, G. E.—b. 1918; mil. serv., 1939-43; temp. asst. consvtr., forests, S.L., 1943; asst. consvtr., 1947; Nyasa, 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | temp. asst. consvr., forests | Sierra Leone | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1947 | asst. consvr | Sierra Leone *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1955 | senr. asst. consvr | Sierra Leone *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1956 | senr. asst. consvr | Nyasaland | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1957 | working plans offr | Nyasaland | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1962 | senr. asst. consvr., forests | Nyasaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 6 | 1964 | consvr., forests | Nyasaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Crichton, G. E___Sierra Leone___1949`

- Staff-list name: **Crichton, G. E** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. E. Crichton | Assistant Conservators of Forests | Forestry | — | — |
| 1950 | G. E. Crichton | Assistant Conservators of Forests | FORESTRY | — | — |
| 1951 | G. E. Crichton | Assistant Conservators of Forests | Forestry | — | — |

### Deterministic checks: `crichton_g-e_b1918` vs `Crichton, G. E___Sierra Leone___1949`

- [PASS] surname_gate: bio 'CRICHTON' vs stint 'Crichton, G. E' (exact)
- [PASS] initials: bio ['G', 'E'] ~ stint ['G', 'E']
- [PASS] age_gate: stint starts 1949, birth 1918 (age 31)
- [PASS] colony: 3 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 50 vs bar 60: 'asst. consvr' ~ 'Assistant Conservators of Forests'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

