<!-- {"case_id": "case_crarky_william-raymond-dunhan_b1900", "bio_ids": ["crarky_william-raymond-dunhan_b1900"], "stint_ids": ["Crarey, W. R. D___Zanzibar___1927"]} -->
# Dossier case_crarky_william-raymond-dunhan_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Crarey, W. R. D___Zanzibar___1927` is also gate-compatible with biography(ies) outside this case: ['crarey_william-raymond-dunstan_b1900'] (already linked elsewhere or filtered).

## Biography `crarky_william-raymond-dunhan_b1900`

- Printed name: **CRARKY, WILLIAM RAYMOND DUNHAN**
- Birth year: 1900 (attested in editions [1934])
- Honours: A.M.I.C.E
- Appears in editions: [1934]

### Verbatim printed entry text (OCR)

**Version `col1934-L57887.v` — printed in editions [1934]:**

> CRARKY, WILLIAM RAYMOND DUNHAN, B.Sc. (Eng.), A.M.I.C.E.—B. 1900; ed. Gresham's Sch., Holt and London Univ.; asst. engr., P.W.D., Zanzibar, Apr., 1926; asst. engr. in charge, P.W.D., Pemba, Aug., 1927; ag. dist. engr., Mar.-Sept., 1930 and June-Dec., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | asst. engr., P.W.D. | Zanzibar | [1934] |
| 1 | 1927 | asst. engr. in charge, P.W.D., Pemba | Zanzibar *(inherited from previous clause)* | [1934] |
| 2 | 1930 | ag. dist. engr., Mar.- | Zanzibar *(inherited from previous clause)* | [1934] |
| 3 | 1931 | June- | Zanzibar *(inherited from previous clause)* | [1934] |

## Candidate stint `Crarey, W. R. D___Zanzibar___1927`

- Staff-list name: **Crarey, W. R. D** | colony: **Zanzibar** | listed 1927–1929 | editions [1927, 1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | W. R. D. Crarey | Assistant Engineers | Public Works Department | — | — |
| 1928 | W. R. D. Crarey | Assistant Engineers | Public Works Department | — | — |
| 1929 | W. R. D. Crarey | Temporary Assistant Engineer | Public Works Department | — | — |

### Deterministic checks: `crarky_william-raymond-dunhan_b1900` vs `Crarey, W. R. D___Zanzibar___1927`

- [PASS] surname_gate: bio 'CRARKY' vs stint 'Crarey, W. R. D' (fuzzy:1)
- [PASS] initials: bio ['W', 'R', 'D'] ~ stint ['W', 'R', 'D']
- [PASS] age_gate: stint starts 1927, birth 1900 (age 27)
- [PASS] colony: 4 placed event(s) resolve to 'Zanzibar'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1927-1929
- [FAIL] position_sim: best 59 vs bar 60: 'ag. dist. engr., Mar.-' ~ 'Temporary Assistant Engineer'
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

