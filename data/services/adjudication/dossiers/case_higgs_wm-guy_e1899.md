<!-- {"case_id": "case_higgs_wm-guy_e1899", "bio_ids": ["higgs_wm-guy_e1899"], "stint_ids": ["Higgs, W. G___Commonwealth Of Australia___1905"]} -->
# Dossier case_higgs_wm-guy_e1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `higgs_wm-guy_e1899`

- Printed name: **HIGGS, WM.GUY**
- Birth year: not printed
- Terminal: resigned 1916 — “resigned, 27th Oct., 1916.”
- Appears in editions: [1917, 1918, 1919, 1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1917-L50362.v` — printed in editions [1917, 1918, 1919, 1920, 1921]:**

> HIGGS, HON. WM.GUY.—M.L.A., Queensland, 1899; senator for Queensland, C. of A., 1901-1906; chmn. of comtees., 1904-1906; mem. of royal comanr. on tariff, 1904-1907; mem., H. of R., general elections, 1910, 1913, 1914; attended coronation of H.M. King George V., 1911; treas., C. of A., 27th Oct., 1915; resigned, 27th Oct., 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899–1899 | M.L.A. | Queensland | [1917, 1918, 1919, 1920, 1921] |
| 1 | 1901–1906 | senator | Queensland | [1917, 1918, 1919, 1920, 1921] |
| 2 | 1904–1906 | chmn. of comtees. | — | [1917, 1918, 1919, 1920, 1921] |
| 3 | 1904–1907 | mem. of royal comanr. on tariff | — | [1917, 1918, 1919, 1920, 1921] |
| 4 | 1910–1914 | mem., H. of R. | — | [1917, 1918, 1919, 1920, 1921] |
| 5 | 1911–1911 | — | — | [1917, 1918, 1919, 1920, 1921] |
| 6 | 1915–1915 | treas. | Australia | [1917, 1918, 1919, 1920, 1921] |

## Candidate stint `Higgs, W. G___Commonwealth Of Australia___1905`

- Staff-list name: **Higgs, W. G** | colony: **Commonwealth Of Australia** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | W. G. Higgs | Senator | Senate | — | — |
| 1907 | W. G. Higgs | Senator | Senate | — | — |

### Deterministic checks: `higgs_wm-guy_e1899` vs `Higgs, W. G___Commonwealth Of Australia___1905`

- [PASS] surname_gate: bio 'HIGGS' vs stint 'Higgs, W. G' (exact)
- [PASS] initials: bio ['W', 'G'] ~ stint ['W', 'G']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Commonwealth Of Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
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

