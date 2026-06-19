<!-- {"case_id": "case_eaton_a-d_b1925", "bio_ids": ["eaton_a-d_b1925"], "stint_ids": ["Eaton, A. D___Sierra Leone___1949"]} -->
# Dossier case_eaton_a-d_b1925

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `eaton_a-d_b1925`

- Printed name: **EATON, A. D**
- Birth year: 1925 (attested in editions [1962, 1963])
- Appears in editions: [1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1962-L20709.v` — printed in editions [1962, 1963]:**

> EATON, A. D.—b. 1925; ed. Kingstown and Trin. Coll., Univ. of Dublin; asst. engr., S. L. Rlwy., 1947; civ. engr., Mal. Rlwy., 1951; asst. ch. civ. engr., 1957; deputy ch. civ. engr., 1959; ch. civ. engr., 1960-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | asst. engr., S. L. Rlwy | Sierra Leone | [1962, 1963] |
| 1 | 1951 | civ. engr., Mal. Rlwy | Malaya | [1962, 1963] |
| 2 | 1957 | asst. ch. civ. engr | Malaya *(inherited from previous clause)* | [1962, 1963] |
| 3 | 1959 | deputy ch. civ. engr | Malaya *(inherited from previous clause)* | [1962, 1963] |
| 4 | 1960–1962 | ch. civ. engr | Malaya *(inherited from previous clause)* | [1962, 1963] |

## Candidate stint `Eaton, A. D___Sierra Leone___1949`

- Staff-list name: **Eaton, A. D** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. D. Eaton | Assistant Engineers | Railway | — | — |
| 1950 | A. D. Eaton | Assistant Engineers | Engineering | — | — |
| 1951 | A. D. Eaton | Assistant Engineers | Engineering | — | — |

### Deterministic checks: `eaton_a-d_b1925` vs `Eaton, A. D___Sierra Leone___1949`

- [PASS] surname_gate: bio 'EATON' vs stint 'Eaton, A. D' (exact)
- [PASS] initials: bio ['A', 'D'] ~ stint ['A', 'D']
- [PASS] age_gate: stint starts 1949, birth 1925 (age 24)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 54 vs bar 60: 'asst. engr., S. L. Rlwy' ~ 'Assistant Engineers'
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

