<!-- {"case_id": "case_gittens_w-a_b1917", "bio_ids": ["gittens_w-a_b1917"], "stint_ids": ["Gittens, W. A___Barbados___1965"]} -->
# Dossier case_gittens_w-a_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 19 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gittens_w-a_b1917`

- Printed name: **GITTENS, W. A**
- Birth year: 1917 (attested in editions [1965, 1966])
- Appears in editions: [1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1965-L15563.v` — printed in editions [1965, 1966]:**

> GITTENS, W. A.—b. 1917; ed. Harrison Coll., Barb.; asst. master, Barb., 1939; clk., 1949; insptr., inland rev., 1954; senr. insptr., 1958; asst. comsnnr., 1963; comsnnr., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | asst. master | Barbados | [1965, 1966] |
| 1 | 1949 | clk | Barbados *(inherited from previous clause)* | [1965, 1966] |
| 2 | 1954 | insptr., inland rev | Barbados *(inherited from previous clause)* | [1965, 1966] |
| 3 | 1958 | senr. insptr | Barbados *(inherited from previous clause)* | [1965, 1966] |
| 4 | 1963 | asst. comsnnr | Barbados *(inherited from previous clause)* | [1965, 1966] |
| 5 | 1964 | comsnnr | Barbados *(inherited from previous clause)* | [1965, 1966] |

## Candidate stint `Gittens, W. A___Barbados___1965`

- Staff-list name: **Gittens, W. A** | colony: **Barbados** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | W. A. Gittens | Commissioner of Inland Revenue | Civil Establishment | — | — |
| 1966 | W. A. Gittens | Commissioner of Inland Revenue | Privy Council | — | — |

### Deterministic checks: `gittens_w-a_b1917` vs `Gittens, W. A___Barbados___1965`

- [PASS] surname_gate: bio 'GITTENS' vs stint 'Gittens, W. A' (exact)
- [PASS] initials: bio ['W', 'A'] ~ stint ['W', 'A']
- [PASS] age_gate: stint starts 1965, birth 1917 (age 48)
- [PASS] colony: 6 placed event(s) resolve to 'Barbados'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1965-1966
- [FAIL] position_sim: best 38 vs bar 60: 'comsnnr' ~ 'Commissioner of Inland Revenue'
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

