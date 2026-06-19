<!-- {"case_id": "case_everett_cyril-frederick-cunningham_b1886", "bio_ids": ["everett_cyril-frederick-cunningham_b1886"], "stint_ids": ["Everett, C. F. C___Nigeria___1927"]} -->
# Dossier case_everett_cyril-frederick-cunningham_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `everett_cyril-frederick-cunningham_b1886`

- Printed name: **EVERETT, CYRIL FREDERICK CUNNINGHAM**
- Birth year: 1886 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L64108.v` — printed in editions [1940]:**

> EVERETT, CYRIL FREDERICK CUNNINGHAM.—B. 1886; supervisor, cust. 2nd grade, Nigeria, 1916; collr., 1924; senr. do., 1936; ag. ast. comptr. and ag. dep. comptr. on various occasions, 1933-37; ast. comptr., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916 | supervisor, cust. 2nd grade | Nigeria | [1940] |
| 1 | 1924 | collr | Nigeria *(inherited from previous clause)* | [1940] |
| 2 | 1933–1937 | ag. ast. comptr. and ag. dep. comptr. on various occasions | Nigeria *(inherited from previous clause)* | [1940] |
| 3 | 1936 | senr. do | Nigeria *(inherited from previous clause)* | [1940] |
| 4 | 1937 | ast. comptr | Nigeria *(inherited from previous clause)* | [1940] |

## Candidate stint `Everett, C. F. C___Nigeria___1927`

- Staff-list name: **Everett, C. F. C** | colony: **Nigeria** | listed 1927–1939 | editions [1927, 1929, 1933, 1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | C. F. C. Everett | Collector/Supervisor | Customs | — | — |
| 1929 | C. F. C. Everett | Collectors and Supervisors | Customs | — | — |
| 1933 | C. F. C. Everett | Collector/Supervisor | Customs | — | — |
| 1934 | C. F. C. Everett | Collectors and Supervisors | Customs | — | — |
| 1939 | C. F. C. Everett | Assistant Comptroller of Customs | Customs | — | — |

### Deterministic checks: `everett_cyril-frederick-cunningham_b1886` vs `Everett, C. F. C___Nigeria___1927`

- [PASS] surname_gate: bio 'EVERETT' vs stint 'Everett, C. F. C' (exact)
- [PASS] initials: bio ['C', 'F', 'C'] ~ stint ['C', 'F', 'C']
- [PASS] age_gate: stint starts 1927, birth 1886 (age 41)
- [PASS] colony: 5 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1927-1939
- [FAIL] position_sim: best 51 vs bar 60: 'ag. ast. comptr. and ag. dep. comptr. on various occasions' ~ 'Assistant Comptroller of Customs'
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

