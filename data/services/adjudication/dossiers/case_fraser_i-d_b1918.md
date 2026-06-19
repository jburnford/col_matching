<!-- {"case_id": "case_fraser_i-d_b1918", "bio_ids": ["fraser_i-d_b1918"], "stint_ids": ["Fraser, I. D___Singapore___1959"]} -->
# Dossier case_fraser_i-d_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 140 official(s) with this surname in the graph's staff lists; 69 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fraser_i-d_b1918`

- Printed name: **FRASER, I. D**
- Birth year: 1918 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Honours: D.S.C, O.B.E (1961)
- Appears in editions: [1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1957-L23148.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> FRASER, I. D., O.B.E. (1961), D.S.C.—b. 1918; ed. Marlborough Coll. and Oxford Univ.; mil. serv., 1940-46, fleet air pilot; cadet, M.C.S., 1946; asst. sec., B.M.A. (and later Mal.) D.O., Ipoh, 1946; cl. IV, 1949; 3rd asst. Mal. estab. offr., 1949; cl. III, 1951; D.O., K. Trengganu, 1951; asst. sec., estab., S'pore, 1953; asst. sec., internal security, 1956; cl. II, 1956; superscale G. and E., 1957; sec., home and external affrs. and registr., soccs., 1957; dep. sec., min. of home affrs., 1959-60.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | cadet, M.C.S | — | [1957, 1958, 1959, 1960, 1961] |
| 1 | 1946 | asst. sec., B.M.A. (and later Mal.) D.O., Ipoh | Dominions Office | [1957, 1958, 1959, 1960, 1961] |
| 2 | 1949 | cl. IV | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 3 | 1951 | cl. III | Dominions Office | [1957, 1958, 1959, 1960, 1961] |
| 4 | 1953 | asst. sec., estab., S'pore | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 5 | 1956 | asst. sec., internal security | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 6 | 1957 | superscale G. and E | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 7 | 1959–1960 | dep. sec., min. of home affrs | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Fraser, I. D___Singapore___1959`

- Staff-list name: **Fraser, I. D** | colony: **Singapore** | listed 1959–1960 | editions [1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | I. D. Fraser | Secretary for Home and External Affairs and Registrar of Societies | Civil Establishment | — | — |
| 1960 | I. D. Fraser | Deputy Secretary (Home Affairs) | Ministry of Home Affairs | — | — |

### Deterministic checks: `fraser_i-d_b1918` vs `Fraser, I. D___Singapore___1959`

- [PASS] surname_gate: bio 'FRASER' vs stint 'Fraser, I. D' (exact)
- [PASS] initials: bio ['I', 'D'] ~ stint ['I', 'D']
- [PASS] age_gate: stint starts 1959, birth 1918 (age 41)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1960
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

