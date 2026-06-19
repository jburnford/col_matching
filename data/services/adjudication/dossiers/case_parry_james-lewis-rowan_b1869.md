<!-- {"case_id": "case_parry_james-lewis-rowan_b1869", "bio_ids": ["parry_james-lewis-rowan_b1869"], "stint_ids": ["Parry, J. L' R___Southern Nigeria___1911", "Parry, J___New South Wales___1894"]} -->
# Dossier case_parry_james-lewis-rowan_b1869

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Parry, J___New South Wales___1894` is also gate-compatible with biography(ies) outside this case: ['parry_j-h_e1915'] (already linked elsewhere or filtered).

## Biography `parry_james-lewis-rowan_b1869`

- Printed name: **PARRY, JAMES LEWIS ROWAN**
- Birth year: 1869 (attested in editions [1908, 1909, 1910, 1911, 1912, 1913, 1914])
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913, 1914]

### Verbatim printed entry text (OCR)

**Version `col1908-L46659.v` — printed in editions [1908, 1909, 1910, 1911, 1912, 1913, 1914]:**

> PARRY, JAMES LEWIS ROWAN.—B. 1869; Capt., 90th Rifles, Canada; lieut., S. Nigeria regt., 1900; served with Ishan expedition, 1901 (medal and clasp); Oron expedition, 1901; asst. mil. sec., Aro expedition, 1901-2 (ment. in despatches, clasp); inspr. of pol., Nov., 1902; ag. gov. of gaols, Jan. to Aug., 1903; coms. of pol., Jan., 1905; ag. inspr. gen. of pol., Apr. to Sept., 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | lieut., S. Nigeria regt | Southern Nigeria | [1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 1 | 1901 | served with Ishan expedition | Southern Nigeria *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 2 | 1902 | inspr. of pol | Southern Nigeria *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 3 | 1903 | ag. gov. of gaols | Southern Nigeria *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 4 | 1905 | coms. of pol | Southern Nigeria *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 5 | 1907 | ag. inspr. gen. of pol | Southern Nigeria *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914] |

## Candidate stint `Parry, J. L' R___Southern Nigeria___1911`

- Staff-list name: **Parry, J. L' R** | colony: **Southern Nigeria** | listed 1911–1913 | editions [1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | J. L. R. Parry | Deputy Inspector-General | Police | — | Major |
| 1912 | J. L. R. Parry | Deputy Inspector-General | Police | — | Major |
| 1913 | J. L' R. Parry | Deputy Inspector-General | Police | — | Major |

### Deterministic checks: `parry_james-lewis-rowan_b1869` vs `Parry, J. L' R___Southern Nigeria___1911`

- [PASS] surname_gate: bio 'PARRY' vs stint 'Parry, J. L' R' (exact)
- [PASS] initials: bio ['J', 'L', 'R'] ~ stint ['J', 'L', 'R']
- [PASS] age_gate: stint starts 1911, birth 1869 (age 42)
- [PASS] colony: 6 placed event(s) resolve to 'Southern Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1911-1913
- [FAIL] position_sim: best 38 vs bar 60: 'ag. inspr. gen. of pol' ~ 'Deputy Inspector-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Parry, J___New South Wales___1894`

- Staff-list name: **Parry, J** | colony: **New South Wales** | listed 1894–1906 | editions [1894, 1896, 1898, 1899, 1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | J. Parry | Outdoor Superintendent | Traffic Branch | — | — |
| 1896 | J. Parry | Outdoor Superintendents | Traffic Branch | — | — |
| 1898 | J. Parry | Outdoor Superintendent | Traffic Branch | — | — |
| 1899 | J. Parry | Outdoor Superintendent | Traffic Branch | — | — |
| 1900 | J. Parry | Outdoor Superintendents | Traffic Branch | — | — |
| 1905 | J. Parry | Comptroller of Stores | Traffic Branch | — | — |
| 1906 | J. Parry | Comptroller of Stores | Traffic Branch | — | — |

### Deterministic checks: `parry_james-lewis-rowan_b1869` vs `Parry, J___New South Wales___1894`

- [PASS] surname_gate: bio 'PARRY' vs stint 'Parry, J' (exact)
- [PASS] initials: bio ['J', 'L', 'R'] ~ stint ['J']
- [PASS] age_gate: stint starts 1894, birth 1869 (age 25)
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1906
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

