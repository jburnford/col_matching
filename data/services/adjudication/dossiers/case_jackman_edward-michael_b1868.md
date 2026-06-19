<!-- {"case_id": "case_jackman_edward-michael_b1868", "bio_ids": ["jackman_edward-michael_b1868"], "stint_ids": ["Jackman, E. M___Newfoundland___1906"]} -->
# Dossier case_jackman_edward-michael_b1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jackman_edward-michael_b1868`

- Printed name: **JACKMAN, EDWARD MICHAEL**
- Birth year: 1868 (attested in editions [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918])
- Appears in editions: [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918]

### Verbatim printed entry text (OCR)

**Version `col1906-L46228.v` — printed in editions [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918]:**

> JACKMAN, HON. EDWARD MICHAEL.—B. 1868; M.H.A. for Placentia and St. Mary's, Newfoundland, 1900; min. of finance and cust., 1900; re-elected to Assembly, 1904; deceased.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | M.H.A. for Placentia and St. Mary's | Newfoundland | [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918] |
| 1 | 1904 | re-elected to Assembly | Newfoundland *(inherited from previous clause)* | [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918] |

## Candidate stint `Jackman, E. M___Newfoundland___1906`

- Staff-list name: **Jackman, E. M** | colony: **Newfoundland** | listed 1906–1909 | editions [1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | E. M. Jackman | Minister of Finance and Customs | Department of Finance and Customs | — | — |
| 1907 | E. M. Jackman | Minister of Finance and Customs | Finance and Customs | — | — |
| 1908 | E. M. Jackman | Minister of Finance and Customs | Finance and Customs | — | — |
| 1909 | E. M. Jackman | Minister of Finance and Customs | Departments of Finance and Customs | — | — |

### Deterministic checks: `jackman_edward-michael_b1868` vs `Jackman, E. M___Newfoundland___1906`

- [PASS] surname_gate: bio 'JACKMAN' vs stint 'Jackman, E. M' (exact)
- [PASS] initials: bio ['E', 'M'] ~ stint ['E', 'M']
- [PASS] age_gate: stint starts 1906, birth 1868 (age 38)
- [PASS] colony: 2 placed event(s) resolve to 'Newfoundland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1906-1909
- [FAIL] position_sim: best 35 vs bar 60: 're-elected to Assembly' ~ 'Minister of Finance and Customs'
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

