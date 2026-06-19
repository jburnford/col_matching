<!-- {"case_id": "case_dijkerman_hendrik-albert_b1878", "bio_ids": ["dijkerman_hendrik-albert_b1878"], "stint_ids": ["Vickerman, H___New Zealand___1912"]} -->
# Dossier case_dijkerman_hendrik-albert_b1878

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dijkerman_hendrik-albert_b1878`

- Printed name: **DIJKERMAN, HENDRIK ALBERT**
- Birth year: 1878 (attested in editions [1932, 1933])
- Appears in editions: [1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1932-L59722.v` — printed in editions [1932, 1933]:**

> DIJKERMAN, HENDRIK ALBERT, Rhodes Univ. Coll., Grahamstown.—B., 1878; ast. survr., Transvaal, 1895-1907; lic. survr., 1907; ditto, Cape of Good Hope, 1912; survr., grade I., Kelantan, Feb., 1912; survr., grade I., F.M.S., Jly., 1918; ast. supt., rev. survey branch, Perak, Jan., 1919; ast. govt. town planner, Perak, Mar., 1927; sr. ast. supt., surveys, Singapore, Nov., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895–1907 | ast. survr. | Transvaal | [1932, 1933] |
| 1 | 1907 | lic. survr | Transvaal *(inherited from previous clause)* | [1932, 1933] |
| 2 | 1912 | lic. survr | Cape of Good Hope | [1932, 1933] |
| 3 | 1912 | survr., grade I. | Kelantan | [1932, 1933] |
| 4 | 1918 | survr., grade I., F.M.S., Jly | Kelantan *(inherited from previous clause)* | [1932, 1933] |
| 5 | 1919 | ast. supt., rev. survey branch, Perak | Kelantan *(inherited from previous clause)* | [1932, 1933] |
| 6 | 1927 | ast. govt. town planner, Perak | Kelantan *(inherited from previous clause)* | [1932, 1933] |
| 7 | 1928 | sr. ast. supt., surveys | Singapore | [1932, 1933] |

## Candidate stint `Vickerman, H___New Zealand___1912`

- Staff-list name: **Vickerman, H** | colony: **New Zealand** | listed 1912–1920 | editions [1912, 1913, 1914, 1915, 1917, 1918, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | H. Vickerman | Resident Engineer | Public Works Department | — | — |
| 1913 | H. Vickerman | Resident Engineers | Public Works Department | — | — |
| 1914 | H. Vickerman | Office Engineer | Public Works Department | — | — |
| 1915 | H. Vickerman | Staff Engineer | Public Works Department | — | — |
| 1917 | H. Vickerman | Staff Engineer | Public Works Department | — | — |
| 1918 | H. Vickerman | Staff Engineer | Public Works Department | — | — |
| 1920 | H. Vickerman | Staff Engineer | Public Works Department | — | — |

### Deterministic checks: `dijkerman_hendrik-albert_b1878` vs `Vickerman, H___New Zealand___1912`

- [PASS] surname_gate: bio 'DIJKERMAN' vs stint 'Vickerman, H' (fuzzy:2)
- [PASS] initials: bio ['H', 'A'] ~ stint ['H']
- [PASS] age_gate: stint starts 1912, birth 1878 (age 34)
- [FAIL] colony: no placed event resolves to 'New Zealand'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1920
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

