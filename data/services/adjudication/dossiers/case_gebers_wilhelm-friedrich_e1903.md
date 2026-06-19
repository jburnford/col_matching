<!-- {"case_id": "case_gebers_wilhelm-friedrich_e1903", "bio_ids": ["gebers_wilhelm-friedrich_e1903", "geers_wilhelm-friedrich_e1903"], "stint_ids": ["Gebers, W. F___Natal___1907"]} -->
# Dossier case_gebers_wilhelm-friedrich_e1903

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Gebers, W. F___Natal___1907'] have more than one claimant biography in this case.

## Biography `gebers_wilhelm-friedrich_e1903`

- Printed name: **GEBERS, WILHELM FRIEDRICH**
- Birth year: not printed
- Appears in editions: [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1907-L44421.v` — printed in editions [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]:**

> GEBERS, WILHELM FRIEDRICH.—Asst. inspr. of native educ., Natal, 1st Mar., 1903; inspr., ditto, 1st July, 1904; sub-inspr. of schls., 1st July, 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | Asst. inspr. of native educ. | Natal | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 1 | 1904 | inspr., ditto | Natal *(inherited from previous clause)* | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 2 | 1906 | sub-inspr. of schls | Natal *(inherited from previous clause)* | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |

## Biography `geers_wilhelm-friedrich_e1903`

- Printed name: **GEERS, WILHELM FRIEDRICH**
- Birth year: not printed
- Appears in editions: [1909]

### Verbatim printed entry text (OCR)

**Version `col1909-L45428.v` — printed in editions [1909]:**

> GEERS, WILHELM FRIEDRICH.—Asst. inspr. of native educ., Natal, 1st Mar., 1903; inspr., ditto, 1st July, 1904; sub-inspr. of schls., 1st July, 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | Asst. inspr. of native educ. | Natal | [1909] |
| 1 | 1904 | inspr., ditto | Natal *(inherited from previous clause)* | [1909] |
| 2 | 1906 | sub-inspr. of schls | Natal *(inherited from previous clause)* | [1909] |

## Candidate stint `Gebers, W. F___Natal___1907`

- Staff-list name: **Gebers, W. F** | colony: **Natal** | listed 1907–1910 | editions [1907, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | W. F. Gebers | Sub-inspectors | Education Department | — | — |
| 1910 | W. F. Gebers | Assistant Inspectors | Education Department | — | — |

### Deterministic checks: `gebers_wilhelm-friedrich_e1903` vs `Gebers, W. F___Natal___1907`

- [PASS] surname_gate: bio 'GEBERS' vs stint 'Gebers, W. F' (exact)
- [PASS] initials: bio ['W', 'F'] ~ stint ['W', 'F']
- [PASS] age_gate: stint starts 1907; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1907-1910
- [FAIL] position_sim: best 58 vs bar 60: 'inspr., ditto' ~ 'Assistant Inspectors'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

### Deterministic checks: `geers_wilhelm-friedrich_e1903` vs `Gebers, W. F___Natal___1907`

- [PASS] surname_gate: bio 'GEERS' vs stint 'Gebers, W. F' (fuzzy:1)
- [PASS] initials: bio ['W', 'F'] ~ stint ['W', 'F']
- [PASS] age_gate: stint starts 1907; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1907-1910
- [FAIL] position_sim: best 58 vs bar 60: 'inspr., ditto' ~ 'Assistant Inspectors'
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

