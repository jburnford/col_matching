<!-- {"case_id": "case_norris_tobias-c_b1861", "bio_ids": ["norris_tobias-c_b1861"], "stint_ids": ["Norris, T. C___Canada___1897", "Norris, T. C___Canada___1908"]} -->
# Dossier case_norris_tobias-c_b1861

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `norris_tobias-c_b1861`

- Printed name: **NORRIS, TOBIAS C.**
- Birth year: 1861 (attested in editions [1918, 1919, 1920, 1921, 1922, 1923])
- Terminal: resigned 1922 — “resig. office on defeat of admtn. 1922.”
- Appears in editions: [1918, 1919, 1920, 1921, 1922, 1923]

### Verbatim printed entry text (OCR)

**Version `col1918-L53137.v` — printed in editions [1918, 1919, 1920, 1921, 1922, 1923]:**

> NORRIS, HON. TOBIAS C.—B. 1861; farmer; elec. to legis., ass., Manitoba, 1896 and 1899; defeated, 1903; re-elec., 1907, 1910, 1914, 1915 and 1922; leader of opposition for several years; premier, May, 1915; is also commr. of prov. lands and railways; resig. office on defeat of admtn. 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896–1899 | elec. to legis., ass. | Manitoba | [1918, 1919, 1920, 1921, 1922, 1923] |
| 1 | 1903–1903 | defeated | — | [1918, 1919, 1920, 1921, 1922, 1923] |
| 2 | 1907–1922 | re-elec. | — | [1918, 1919, 1920, 1921, 1922, 1923] |
| 3 | 1915–1915 | premier | — | [1918, 1919, 1920, 1921, 1922, 1923] |

## Candidate stint `Norris, T. C___Canada___1897`

- Staff-list name: **Norris, T. C** | colony: **Canada** | listed 1897–1898 | editions [1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | T. C. Norris | Member | Members | — | — |
| 1898 | T. C. Norris | Member | Legislative Assembly | — | — |

### Deterministic checks: `norris_tobias-c_b1861` vs `Norris, T. C___Canada___1897`

- [PASS] surname_gate: bio 'NORRIS' vs stint 'Norris, T. C' (exact)
- [PASS] initials: bio ['T', 'C'] ~ stint ['T', 'C']
- [PASS] age_gate: stint starts 1897, birth 1861 (age 36)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1897-1898
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Norris, T. C___Canada___1908`

- Staff-list name: **Norris, T. C** | colony: **Canada** | listed 1908–1918 | editions [1908, 1913, 1914, 1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | T. C. Norris | Member | Legislative Assembly | — | — |
| 1913 | T. C. Norris | Member of Legislative Assembly | Members | — | — |
| 1914 | T. C. Norris | Member of Legislative Assembly | Legislative Assembly | — | — |
| 1915 | T. C. Norris | Member for Lansdowne | — | — | — |
| 1917 | T. C. Norris | Commissioner | Provincial Lands | — | — |
| 1917 | T. C. Norris | Commissioner | Railway Commissioner | — | — |
| 1917 | T. C. Norris | Premier, President of Council, Provincial Lands and Railway Commissioner | Executive Council | — | — |
| 1918 | T. C. Norris | President of the Council, Commissioner of Railways and Provincial Lands | Executive Council | — | — |

### Deterministic checks: `norris_tobias-c_b1861` vs `Norris, T. C___Canada___1908`

- [PASS] surname_gate: bio 'NORRIS' vs stint 'Norris, T. C' (exact)
- [PASS] initials: bio ['T', 'C'] ~ stint ['T', 'C']
- [PASS] age_gate: stint starts 1908, birth 1861 (age 47)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1918
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

