<!-- {"case_id": "case_maclagan_francis_b1901", "bio_ids": ["maclagan_francis_b1901"], "stint_ids": ["MacLagan, F___Sierra Leone___1949"]} -->
# Dossier case_maclagan_francis_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['maclagan_francis_b1901'] carry a single initial only — the namesake trap applies.

## Biography `maclagan_francis_b1901`

- Printed name: **MACLAGAN, Francis**
- Birth year: 1901 (attested in editions [1948, 1949, 1950, 1951])
- Honours: M.B
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L34373.v` — printed in editions [1948, 1949, 1950, 1951]:**

> MACLAGAN, Francis, M.B., Ch.B. (St. And.), M.R.C.P. (Lond.), D.P.M. (Eng.), D.T.M. & H. (Eng.).—b. 1901; ed. Perth Acad. and St. Andrews Univ.; med. offr. (alienist), G.C., 1929; asst. D.M.S., S.L., 1945; D.M.S., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | med. offr. (alienist) | Gold Coast | [1948, 1949, 1950, 1951] |
| 1 | 1945 | asst. D.M.S. | Sierra Leone | [1948, 1949, 1950, 1951] |
| 2 | 1948 | D.M.S | Sierra Leone *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `MacLagan, F___Sierra Leone___1949`

- Staff-list name: **MacLagan, F** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | F. MacLagan | Director of Medical Services | Medical | — | — |
| 1950 | F. MacLagan | Director of Medical Services | Medical | — | — |
| 1951 | F. MacLagan | Director of Medical Services | Medical | — | — |

### Deterministic checks: `maclagan_francis_b1901` vs `MacLagan, F___Sierra Leone___1949`

- [PASS] surname_gate: bio 'MACLAGAN' vs stint 'MacLagan, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
- [PASS] colony: 2 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 22 vs bar 60: 'asst. D.M.S.' ~ 'Director of Medical Services'
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

