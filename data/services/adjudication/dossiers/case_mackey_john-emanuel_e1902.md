<!-- {"case_id": "case_mackey_john-emanuel_e1902", "bio_ids": ["mackey_john-emanuel_e1902"], "stint_ids": ["Mackey, J. E___Victoria___1907"]} -->
# Dossier case_mackey_john-emanuel_e1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mackey_john-emanuel_e1902`

- Printed name: **MACKEY, JOHN EMANUEL**
- Birth year: not printed
- Honours: M.A
- Appears in editions: [1907, 1908, 1909, 1910, 1911, 1913, 1914, 1918, 1919, 1921, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1907-L45649.v` — printed in editions [1907, 1908, 1909, 1910, 1911, 1913, 1914, 1918, 1919, 1921, 1923, 1924]:**

> MACKEY, Hon. Sir JOHN EMANUEL, K.T. BACH, (1921), M.A., LL.B.—M.L.A. for Gippsland W., Victoria, since 1902; barrister-at-law, lecturer in equity in Univ. of Melbourne, late ag. prof. of logic and philosophy; min. without portfolio, Victoria, 1904; afterwards commr. of crown lands and survey, and pres. of t.d. of lands and wks.; now speaker.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902 | M.L.A. for Gippsland W., Victoria, since | — | [1907, 1908, 1909, 1910, 1911, 1913, 1914, 1918, 1919, 1921, 1923, 1924] |
| 1 | 1904 | min. without portfolio | Victoria | [1907, 1908, 1909, 1910, 1911, 1913, 1914, 1918, 1919, 1921, 1923, 1924] |

## Candidate stint `Mackey, J. E___Victoria___1907`

- Staff-list name: **Mackey, J. E** | colony: **Victoria** | listed 1907–1908 | editions [1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | J. E. Mackey | Commissioner of Crown Lands and Survey | Department of Lands and Survey | — | — |
| 1908 | J. E. Mackey | Commissioner of Crown Lands and Survey | Department of Lands and Survey | — | — |

### Deterministic checks: `mackey_john-emanuel_e1902` vs `Mackey, J. E___Victoria___1907`

- [PASS] surname_gate: bio 'MACKEY' vs stint 'Mackey, J. E' (exact)
- [PASS] initials: bio ['J', 'E'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1907; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1907-1908
- [FAIL] position_sim: best 34 vs bar 60: 'min. without portfolio' ~ 'Commissioner of Crown Lands and Survey'
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

