<!-- {"case_id": "case_de-kretzer_herbert-kenneth_b1890", "bio_ids": ["de-kretzer_herbert-kenneth_b1890"], "stint_ids": ["de Kretser, H. K___Ceylon___1908", "de Kretser, H. K___Ceylon___1914"]} -->
# Dossier case_de-kretzer_herbert-kenneth_b1890

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-kretzer_herbert-kenneth_b1890`

- Printed name: **DE KRETZER, HERBERT KENNETH**
- Birth year: 1890 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L66041.v` — printed in editions [1939, 1940]:**

> DE KRETZER, HERBERT KENNETH, M.Inst. C.E., M.Inst.M. & Cy.E., F.R.San.I.—B. 1890; P.W.D., Ceylon, 1904; dist. engrnr., 1908; prov. engrnr., 1926; 1st ass't. D.P.W., 1932; dep. D.P.W., Aug., 1932; D.P.W., Apr., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904 | P.W.D. | Ceylon | [1939, 1940] |
| 1 | 1908 | dist. engrnr | Ceylon *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1926 | prov. engrnr | Ceylon *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1932 | 1st ass't. D.P.W | Ceylon *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1936 | D.P.W | Ceylon *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `de Kretser, H. K___Ceylon___1908`

- Staff-list name: **de Kretser, H. K** | colony: **Ceylon** | listed 1908–1911 | editions [1908, 1909, 1910, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | H. K. de Kretser | District Engineer (2nd Grade) | Public Works Department | — | — |
| 1909 | H. K. de Kretser | District Engineer | Public Works Department | — | — |
| 1910 | H. K. de Kretser | District Engineer (2nd Grade) | Public Works Department | — | — |
| 1911 | H. K. de Kretser | District Engineer | Public Works Department | — | — |

### Deterministic checks: `de-kretzer_herbert-kenneth_b1890` vs `de Kretser, H. K___Ceylon___1908`

- [PASS] surname_gate: bio 'DE KRETZER' vs stint 'de Kretser, H. K' (fuzzy:1)
- [PASS] initials: bio ['H', 'K'] ~ stint ['H', 'K']
- [PASS] age_gate: stint starts 1908, birth 1890 (age 18)
- [PASS] colony: 5 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1908-1911
- [PASS] position_sim: best 71 vs bar 60: 'dist. engrnr' ~ 'District Engineer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `de Kretser, H. K___Ceylon___1914`

- Staff-list name: **de Kretser, H. K** | colony: **Ceylon** | listed 1914–1917 | editions [1914, 1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | H. K. de Kretser | District Engineer | District Engineers | — | — |
| 1915 | H. K. de Kretser | District Engineer | Public Works Department | — | — |
| 1917 | H. K. de Kretser | District Engineer | Public Works Department | — | — |

### Deterministic checks: `de-kretzer_herbert-kenneth_b1890` vs `de Kretser, H. K___Ceylon___1914`

- [PASS] surname_gate: bio 'DE KRETZER' vs stint 'de Kretser, H. K' (fuzzy:1)
- [PASS] initials: bio ['H', 'K'] ~ stint ['H', 'K']
- [PASS] age_gate: stint starts 1914, birth 1890 (age 24)
- [PASS] colony: 5 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1914-1917
- [PASS] position_sim: best 71 vs bar 60: 'dist. engrnr' ~ 'District Engineer'
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

