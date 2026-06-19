<!-- {"case_id": "case_vergette_edward-dudley_b1857", "bio_ids": ["vergette_edward-dudley_b1857"], "stint_ids": ["Vergette, E. D___Cyprus___1922", "Vergette, E. D___Sierra Leone___1908"]} -->
# Dossier case_vergette_edward-dudley_b1857

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Vergette, E. D___Cyprus___1922` is also gate-compatible with biography(ies) outside this case: ['vergette_edward-dudley_b1878'] (already linked elsewhere or filtered).
- NOTE: stint `Vergette, E. D___Sierra Leone___1908` is also gate-compatible with biography(ies) outside this case: ['vergette_edward-dudley_b1878'] (already linked elsewhere or filtered).

## Biography `vergette_edward-dudley_b1857`

- Printed name: **VERGETTE, EDWARD DUDLEY**
- Birth year: 1857 (attested in editions [1925])
- Appears in editions: [1925]

### Verbatim printed entry text (OCR)

**Version `col1925-L60077.v` — printed in editions [1925]:**

> VERGETTE, EDWARD DUDLEY.—B. 1857; King's Sch., Peterborough; admitted sup. et., England, 1903; asst. dist. sup. et., Sierra Leone, Oct., 1907; barrister sup. et., Sierra Leone, Nov., 1907; crown parser, Jan., 1913; ag. circuit judge and ag. judge, Sierra Leone, Nov., 1914 to Apr., ag. pol. mag. and regist.-gen., Sierra Leone, various periods, 1908 and 1916-19; pres. Cyprus, July, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903–1903 | admitted sup. et. | England | [1925] |
| 1 | 1907–1907 | asst. dist. sup. et. | Sierra Leone | [1925] |
| 2 | 1908–1919 | ag. pol. mag. and regist.-gen. | Sierra Leone | [1925] |
| 3 | 1913–1913 | crown parser | — | [1925] |
| 4 | 1914 | ag. circuit judge and ag. judge | Sierra Leone | [1925] |
| 5 | 1920–1920 | pres. | Cyprus | [1925] |

## Candidate stint `Vergette, E. D___Cyprus___1922`

- Staff-list name: **Vergette, E. D** | colony: **Cyprus** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | E. D. Vergette | President of District Court | Legal Departments | — | — |
| 1923 | E. D. Vergette | President of District Court | District Courts | — | — |
| 1924 | E. D. Vergette | President of District Court | Legal Departments | — | — |
| 1925 | E. D. Vergette | President of District Court | Legal Departments | — | — |

### Deterministic checks: `vergette_edward-dudley_b1857` vs `Vergette, E. D___Cyprus___1922`

- [PASS] surname_gate: bio 'VERGETTE' vs stint 'Vergette, E. D' (exact)
- [PASS] initials: bio ['E', 'D'] ~ stint ['E', 'D']
- [PASS] age_gate: stint starts 1922, birth 1857 (age 65)
- [PASS] colony: 1 placed event(s) resolve to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1925
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Vergette, E. D___Sierra Leone___1908`

- Staff-list name: **Vergette, E. D** | colony: **Sierra Leone** | listed 1908–1920 | editions [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1918, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | E. D. Vergette | Assistant District Commissioner | Provincial Administration | — | — |
| 1909 | E. D. Vergette | Assistant District Commissioner | Provincial Administration | — | — |
| 1910 | E. D. Vergette | Assistant District Commissioner | Provincial Administration | — | — |
| 1911 | E. D. Vergette | Assistant District Commissioner | Provincial Administration | — | — |
| 1912 | E. D. Vergette | Assistant District Commissioner | Provincial Administration | — | — |
| 1913 | E. D. Vergette | Assistant District Commissioner | Provincial Administration | — | — |
| 1914 | E. D. Vergette | Crown Prosecutor | Legal Department | — | — |
| 1915 | E. D. Vergette | Crown Prosecutor | Legal Department | — | — |
| 1918 | E. D. Vergette | Crown Prosecutor | Legal Department | — | — |
| 1919 | E. D. Vergette | Crown Prosecutor | Legal Department | — | — |
| 1920 | E. D. Vergette | Crown Prosecutor | Legal Department | — | — |

### Deterministic checks: `vergette_edward-dudley_b1857` vs `Vergette, E. D___Sierra Leone___1908`

- [PASS] surname_gate: bio 'VERGETTE' vs stint 'Vergette, E. D' (exact)
- [PASS] initials: bio ['E', 'D'] ~ stint ['E', 'D']
- [PASS] age_gate: stint starts 1908, birth 1857 (age 51)
- [PASS] colony: 3 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1908-1920
- [FAIL] position_sim: best 43 vs bar 60: 'asst. dist. sup. et.' ~ 'Assistant District Commissioner'
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

