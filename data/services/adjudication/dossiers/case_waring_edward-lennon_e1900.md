<!-- {"case_id": "case_waring_edward-lennon_e1900", "bio_ids": ["waring_edward-lennon_e1900"], "stint_ids": ["Waring, E. L___Kenya___1907"]} -->
# Dossier case_waring_edward-lennon_e1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `waring_edward-lennon_e1900`

- Printed name: **WARING, EDWARD LENNON**
- Birth year: not printed
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1908-L48077.v` — printed in editions [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]:**

> WARING, EDWARD LENNON.—Ed. at St. Paul's Schl. and Crystal Pal. Engnrng. Compr. Schl.; asst. engrnr., Uganda rly., 1900-03; asst. ch. survr., E. Africa Prot., 27th July, 1903; dep. dir. of surveys, cadastral branch, 1st Apr., 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900–1903 | asst. engrnr., Uganda rly | Uganda | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |
| 1 | 1903 | asst. ch. survr., E. Africa Prot | Uganda *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |
| 2 | 1906 | dep. dir. of surveys, cadastral branch | Uganda *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |

## Candidate stint `Waring, E. L___Kenya___1907`

- Staff-list name: **Waring, E. L** | colony: **Kenya** | listed 1907–1909 | editions [1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | E. L. Waring | Deputy Director of Surveys | — | — | — |
| 1908 | E. L. Waring | Deputy Director of Surveys | Civil Establishment | — | — |
| 1909 | E. L. Waring | Deputy Director | Cadastral Survey | — | — |

### Deterministic checks: `waring_edward-lennon_e1900` vs `Waring, E. L___Kenya___1907`

- [PASS] surname_gate: bio 'WARING' vs stint 'Waring, E. L' (exact)
- [PASS] initials: bio ['E', 'L'] ~ stint ['E', 'L']
- [PASS] age_gate: stint starts 1907; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1909
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

