<!-- {"case_id": "case_ennett_sydney-christmas_e1914", "bio_ids": ["ennett_sydney-christmas_e1914"], "stint_ids": ["Bennett, S. C___Kenya___1917"]} -->
# Dossier case_ennett_sydney-christmas_e1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 86 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `ennett_sydney-christmas_e1914` ↔ `Bennett, S. C___Kenya___1917` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Bennett, S. C___Kenya___1917` is also gate-compatible with biography(ies) outside this case: ['bennett_sydney-christmas_e1914'] (already linked elsewhere or filtered).

## Biography `ennett_sydney-christmas_e1914`

- Printed name: **ENNETT, SYDNEY CHRISTMAS**
- Birth year: not printed
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L58825.v` — printed in editions [1937]:**

> ENNETT, SYDNEY CHRISTMAS, A.M.I.C.E., M.Inst. Mun. and Cty. Engrs.—Ed. Sherborne Schl.; astt. engrn., P.W.D., E.A.P., 1914-15; pioneer, E. A. Pioneers, 1915-16; 2nd lieut., A. Rly. Corps., 1916-17; it., 1917-18; ment. in desps., "1914-15" Star, Br. War and Victory medals; exec. engrn., Kenya, 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1915 | astt. engrn., P.W.D. | East Africa Protectorate | [1937] |
| 1 | 1915–1916 | pioneer | — | [1937] |
| 2 | 1916–1917 | 2nd lieut. | — | [1937] |
| 3 | 1917–1918 | it. | — | [1937] |
| 4 | 1921 | exec. engrn. | Kenya | [1937] |

## Candidate stint `Bennett, S. C___Kenya___1917`

- Staff-list name: **Bennett, S. C** | colony: **Kenya** | listed 1917–1931 | editions [1917, 1918, 1919, 1920, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | S. C. Bennett | Assistant Engineer | Public Works | — | — |
| 1918 | S. C. Bennett | Assistant Engineer | Public Works | — | — |
| 1919 | S. C. Bennett | Assistant Engineers | Public Works | — | — |
| 1920 | S. C. Bennett | Assistant Engineer | Public Works | — | — |
| 1922 | S. C. Bennett | Executive Engineers | Public Works | — | — |
| 1923 | S. C. Bennett | Executive Engineer | Public Works | — | — |
| 1924 | S. C. Bennett | Executive Engineers | Divisional Staff | — | — |
| 1927 | S. C. Bennett | Executive Engineers | Divisional Staff | — | — |
| 1928 | S. C. Bennett | Executive Engineers | Divisional Staff | — | — |
| 1929 | S. C. Bennett | Executive Engineers | Divisional Staff | — | — |
| 1930 | S. C. Bennett | Executive Engineers | Divisional Staff | — | — |
| 1931 | S. C. Bennett | Executive Engineers | Divisional Staff | — | — |

### Deterministic checks: `ennett_sydney-christmas_e1914` vs `Bennett, S. C___Kenya___1917`

- [PASS] surname_gate: bio 'ENNETT' vs stint 'Bennett, S. C' (fuzzy:1)
- [PASS] initials: bio ['S', 'C'] ~ stint ['S', 'C']
- [PASS] age_gate: stint starts 1917; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1917-1931
- [PASS] position_sim: best 64 vs bar 60: 'exec. engrn.' ~ 'Executive Engineer'
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

