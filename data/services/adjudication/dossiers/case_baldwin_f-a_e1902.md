<!-- {"case_id": "case_baldwin_f-a_e1902", "bio_ids": ["baldwin_f-a_e1902"], "stint_ids": ["Baldwin, F. J. A___Gambia___1905"]} -->
# Dossier case_baldwin_f-a_e1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `baldwin_f-a_e1902`

- Printed name: **BALDWIN, F. A.**
- Birth year: not printed
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1908-L43023.v` — printed in editions [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]:**

> BALDWIN, F. A., M.R.C.S., L.R.C.P., L.S.A., D.T.M.—Late med. offr. and pub. vaccinator, St. Saviour's Union, Lond.; protec- torate med. offr., Gambia, 1902-1903; attached to frontier force, Jan. to Apr., 1903; ag. sen. med. offr., 1903, 1905 and 1907; J.P. and comsnnr., et. of requests.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902–1903 | protec- torate med. offr. | Gambia | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 1 | 1903–1903 | attached to frontier force | — | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 2 | 1903–1907 | ag. sen. med. offr. | — | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 3 | ? | med. offr. and pub. vaccinator | London | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |

## Candidate stint `Baldwin, F. J. A___Gambia___1905`

- Staff-list name: **Baldwin, F. J. A** | colony: **Gambia** | listed 1905–1910 | editions [1905, 1906, 1907, 1908, 1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | F. J. A. Baldwin | Medical Officer | Medical | — | — |
| 1906 | F. J. A. Baldwin | Medical Officer | Medical | — | — |
| 1907 | F. J. A. Baldwin | Medical Officer | Medical | — | — |
| 1908 | F. J. A. Baldwin | Medical Officer | Medical | — | — |
| 1909 | F. J. A. Baldwin | Medical Officer | Medical | — | — |
| 1910 | F. J. A. Baldwin | Medical Officer | Medical | — | — |

### Deterministic checks: `baldwin_f-a_e1902` vs `Baldwin, F. J. A___Gambia___1905`

- [PASS] surname_gate: bio 'BALDWIN' vs stint 'Baldwin, F. J. A' (exact)
- [PASS] initials: bio ['F', 'A'] ~ stint ['F', 'J', 'A']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1910
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

