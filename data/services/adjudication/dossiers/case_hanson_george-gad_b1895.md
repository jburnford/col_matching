<!-- {"case_id": "case_hanson_george-gad_b1895", "bio_ids": ["hanson_george-gad_b1895"], "stint_ids": ["Hanson, G. G___Gold Coast___1949"]} -->
# Dossier case_hanson_george-gad_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hanson_george-gad_b1895`

- Printed name: **HANSON, George Gad**
- Birth year: 1895 (attested in editions [1948, 1949, 1950, 1951])
- Honours: M.B.E (1949)
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33142.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HANSON, George Gad, M.B.E. (1949).—b. 1895; ed. Basel Miss. Sch., G.C.; 3rd gr. survr., 1920; seconded to S.L., 1925-27; survr., G.C., 1945; survr.-in-ch., topo. branch, 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | 3rd gr. survr | — | [1948, 1949, 1950, 1951] |
| 1 | 1925–1927 | seconded to S.L | — | [1948, 1949, 1950, 1951] |
| 2 | 1945 | survr. | Gold Coast | [1948, 1949, 1950, 1951] |
| 3 | 1946 | survr.-in-ch., topo. branch | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Hanson, G. G___Gold Coast___1949`

- Staff-list name: **Hanson, G. G** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. G. Hanson | Surveyors | Survey Department | — | — |
| 1950 | G. G. Hanson | Surveyors | SURVEY DEPARTMENT | — | — |
| 1951 | G. G. Hanson | Senior Surveyor | Survey Department | — | — |

### Deterministic checks: `hanson_george-gad_b1895` vs `Hanson, G. G___Gold Coast___1949`

- [PASS] surname_gate: bio 'HANSON' vs stint 'Hanson, G. G' (exact)
- [PASS] initials: bio ['G', 'G'] ~ stint ['G', 'G']
- [PASS] age_gate: stint starts 1949, birth 1895 (age 54)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 39 vs bar 60: 'survr.-in-ch., topo. branch' ~ 'Senior Surveyor'
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

