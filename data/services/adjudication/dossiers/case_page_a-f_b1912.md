<!-- {"case_id": "case_page_a-f_b1912", "bio_ids": ["page_a-f_b1912"], "stint_ids": ["Page, A. F___Gold Coast___1949"]} -->
# Dossier case_page_a-f_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `page_a-f_b1912`

- Printed name: **PAGE, A. F**
- Birth year: 1912 (attested in editions [1956, 1957, 1958])
- Appears in editions: [1956, 1957, 1958]

### Verbatim printed entry text (OCR)

**Version `col1956-L23370.v` — printed in editions [1956, 1957, 1958]:**

> PAGE, A. F.—b. 1912; ed. Cheetham Hill Coll., Manchester; asst., Accra rehousing scheme, G.C., 1940; assessmt. offr., inc. tax dept., 1943; senr., 1948; senr. inspr., taxes, 1954 (Ghana civil service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | asst., Accra rehousing scheme | Gold Coast | [1956, 1957, 1958] |
| 1 | 1943 | assessmt. offr., inc. tax dept | Gold Coast *(inherited from previous clause)* | [1956, 1957, 1958] |
| 2 | 1948 | senr | Gold Coast *(inherited from previous clause)* | [1956, 1957, 1958] |
| 3 | 1954 | senr. inspr., taxes | Gold Coast *(inherited from previous clause)* | [1956, 1957, 1958] |

## Candidate stint `Page, A. F___Gold Coast___1949`

- Staff-list name: **Page, A. F** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. F. Page | Senior Assessment Officer | Income Tax | — | — |
| 1950 | A. F. Page | Senior Assessment Officers | Income Tax | — | — |
| 1951 | A. F. Page | Senior Assessment Officer | Income Tax | — | — |

### Deterministic checks: `page_a-f_b1912` vs `Page, A. F___Gold Coast___1949`

- [PASS] surname_gate: bio 'PAGE' vs stint 'Page, A. F' (exact)
- [PASS] initials: bio ['A', 'F'] ~ stint ['A', 'F']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 59 vs bar 60: 'assessmt. offr., inc. tax dept' ~ 'Senior Assessment Officer'
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

