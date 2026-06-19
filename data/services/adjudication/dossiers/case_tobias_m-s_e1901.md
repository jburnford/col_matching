<!-- {"case_id": "case_tobias_m-s_e1901", "bio_ids": ["tobias_m-s_e1901"], "stint_ids": ["Tobias, M. S___Orange River Colony___1907", "Tobias, M___Gibraltar___1922"]} -->
# Dossier case_tobias_m-s_e1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tobias_m-s_e1901`

- Printed name: **TOBIAS, M. S**
- Birth year: not printed
- Appears in editions: [1907, 1908, 1909, 1910, 1911, 1912]

### Verbatim printed entry text (OCR)

**Version `col1907-L47352.v` — printed in editions [1907, 1908, 1909, 1910, 1911, 1912]:**

> TOBIAS, M. S.—Clk., statis. branch, educn. off., Cape Town, Dec., 1901; 2nd clk., res. mag.'s off., O.R.C., May, 1902; examr. of accts., aud. dept., O.R.C., Aug., 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | Clk., statis. branch, educn. off., Cape Town | Cape of Good Hope | [1907, 1908, 1909, 1910, 1911, 1912] |
| 1 | 1902 | 2nd clk., res. mag.'s off., O.R.C | Cape of Good Hope *(inherited from previous clause)* | [1907, 1908, 1909, 1910, 1911, 1912] |
| 2 | 1906 | examr. of accts., aud. dept., O.R.C | Cape of Good Hope *(inherited from previous clause)* | [1907, 1908, 1909, 1910, 1911, 1912] |

## Candidate stint `Tobias, M. S___Orange River Colony___1907`

- Staff-list name: **Tobias, M. S** | colony: **Orange River Colony** | listed 1907–1909 | editions [1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | M. S. Tobias | Examiners of Accounts | Auditor-General's Department | — | — |
| 1908 | M. S. Tobias | Examiners of Accounts | Auditor-General's Department | — | — |
| 1909 | M. S. Tobias | Examiners of Accounts | Audit | — | — |

### Deterministic checks: `tobias_m-s_e1901` vs `Tobias, M. S___Orange River Colony___1907`

- [PASS] surname_gate: bio 'TOBIAS' vs stint 'Tobias, M. S' (exact)
- [PASS] initials: bio ['M', 'S'] ~ stint ['M', 'S']
- [PASS] age_gate: stint starts 1907; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Orange River Colony'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Tobias, M___Gibraltar___1922`

- Staff-list name: **Tobias, M** | colony: **Gibraltar** | listed 1922–1924 | editions [1922, 1923, 1924]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | M. Tobias | Senior Chaplain to the Forces | Chief Military and Naval Officers | — | — |
| 1923 | M. Tobias | Senior Chaplain to the Forces | Chief Military and Naval Officers | — | — |
| 1924 | M. Tobias | Senior Chaplain to the Forces | Chief Military and Naval Officers | — | — |

### Deterministic checks: `tobias_m-s_e1901` vs `Tobias, M___Gibraltar___1922`

- [PASS] surname_gate: bio 'TOBIAS' vs stint 'Tobias, M' (exact)
- [PASS] initials: bio ['M', 'S'] ~ stint ['M']
- [PASS] age_gate: stint starts 1922; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gibraltar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1924
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

