<!-- {"case_id": "case_meikle_a-r_b1914", "bio_ids": ["meikle_a-r_b1914"], "stint_ids": ["Meikle, A. R___Sarawak___1949", "Meikle, A. R___Sarawak___1959"]} -->
# Dossier case_meikle_a-r_b1914

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `meikle_a-r_b1914`

- Printed name: **MEIKLE, A. R**
- Birth year: 1914 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L25233.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> MEIKLE, A. R., T.D.—b. 1914; ed. Gate House Prep. Sch., Kingsthorp Hill, Surrey, and St. John's Sch., Leatherhead; admin. cadet, Sarawak, 1946; asst. D.O., 1946; p.s. to governor, 1947; D.O., 1952; sec., Kuching munic. coun., 1958; admin. offr., cl. IB., 1961.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | admin. cadet | Sarawak | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1947 | p.s. to governor | Sarawak *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1952 | p.s. to governor | Dominions Office | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1958 | sec., Kuching munic. coun | Dominions Office *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1961 | admin. offr., cl. IB | Dominions Office *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Meikle, A. R___Sarawak___1949`

- Staff-list name: **Meikle, A. R** | colony: **Sarawak** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. R. Meikle | Private Secretary | Governor and Personal Staff | — | — |
| 1951 | A. R. Meikle | District Officers, Assistant District Officers and Cadets | Administrative Service | — | — |

### Deterministic checks: `meikle_a-r_b1914` vs `Meikle, A. R___Sarawak___1949`

- [PASS] surname_gate: bio 'MEIKLE' vs stint 'Meikle, A. R' (exact)
- [PASS] initials: bio ['A', 'R'] ~ stint ['A', 'R']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 2 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 32 vs bar 60: 'p.s. to governor' ~ 'Private Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Meikle, A. R___Sarawak___1959`

- Staff-list name: **Meikle, A. R** | colony: **Sarawak** | listed 1959–1963 | editions [1959, 1960, 1961, 1962, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | A. R. Meikle | Secretary, Kuching Municipal Council | Civil Establishment | — | — |
| 1960 | A. R. Meikle | Secretary, Kuching Municipal Council | Civil Establishment | — | — |
| 1961 | A. R. Meikle | Secretary for Local Government | Civil Establishment | — | — |
| 1962 | A. R. Meikle | Secretary for Local Government | Civil Establishment | — | — |
| 1963 | A. R. Meikle | Secretary for Local Government | Civil Establishment | — | — |

### Deterministic checks: `meikle_a-r_b1914` vs `Meikle, A. R___Sarawak___1959`

- [PASS] surname_gate: bio 'MEIKLE' vs stint 'Meikle, A. R' (exact)
- [PASS] initials: bio ['A', 'R'] ~ stint ['A', 'R']
- [PASS] age_gate: stint starts 1959, birth 1914 (age 45)
- [PASS] colony: 2 placed event(s) resolve to 'Sarawak'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1963
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

