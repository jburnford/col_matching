<!-- {"case_id": "case_clark_a-d_b1913", "bio_ids": ["clark_a-d_b1913"], "stint_ids": ["Clark, A. D___Bechuanaland___1965", "Clark, A. D___High Commission Territories___1963"]} -->
# Dossier case_clark_a-d_b1913

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 114 official(s) with this surname in the graph's staff lists; 54 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `clark_a-d_b1913`

- Printed name: **CLARK, A. D**
- Birth year: 1913 (attested in editions [1962, 1963, 1964, 1965, 1966])
- Honours: C.P.M (1955)
- Appears in editions: [1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1962-L19733.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> CLARK, A. D., C.P.M. (1955).—b. 1913; ed. Pietermaritzburg Coll., Natal; Bech. Prot. police, 1936; asst. sup't., 1947; sup't., 1951; senr. sup't., 1954; deputy-comsnt., 1961.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | Bech. Prot. police | Bechuanaland | [1962, 1963, 1964, 1965, 1966] |
| 1 | 1947 | asst. sup't | Bechuanaland *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |
| 2 | 1951 | sup't | Bechuanaland *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |
| 3 | 1954 | senr. sup't | Bechuanaland *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |
| 4 | 1961 | deputy-comsnt | Bechuanaland *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Clark, A. D___Bechuanaland___1965`

- Staff-list name: **Clark, A. D** | colony: **Bechuanaland** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | A. D. Clark | Deputy Commissioner | Secretariat | — | — |
| 1966 | A. D. Clark | Deputy Commissioner | Secretariat | — | — |

### Deterministic checks: `clark_a-d_b1913` vs `Clark, A. D___Bechuanaland___1965`

- [PASS] surname_gate: bio 'CLARK' vs stint 'Clark, A. D' (exact)
- [PASS] initials: bio ['A', 'D'] ~ stint ['A', 'D']
- [PASS] age_gate: stint starts 1965, birth 1913 (age 52)
- [PASS] colony: 5 placed event(s) resolve to 'Bechuanaland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1965-1966
- [FAIL] position_sim: best 39 vs bar 60: 'deputy-comsnt' ~ 'Deputy Commissioner'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Clark, A. D___High Commission Territories___1963`

- Staff-list name: **Clark, A. D** | colony: **High Commission Territories** | listed 1963–1964 | editions [1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | A. D. Clark | Deputy Commissioner | Secretariat | — | — |
| 1964 | A. D. Clark | Deputy Commissioner | Secretariat | — | — |

### Deterministic checks: `clark_a-d_b1913` vs `Clark, A. D___High Commission Territories___1963`

- [PASS] surname_gate: bio 'CLARK' vs stint 'Clark, A. D' (exact)
- [PASS] initials: bio ['A', 'D'] ~ stint ['A', 'D']
- [PASS] age_gate: stint starts 1963, birth 1913 (age 50)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1964
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

