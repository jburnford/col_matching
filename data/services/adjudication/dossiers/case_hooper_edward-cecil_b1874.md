<!-- {"case_id": "case_hooper_edward-cecil_b1874", "bio_ids": ["hooper_edward-cecil_b1874"], "stint_ids": ["Hooper, E. C___South Africa___1912"]} -->
# Dossier case_hooper_edward-cecil_b1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hooper_edward-cecil_b1874`

- Printed name: **HOOPER, EDWARD CECIL**
- Birth year: 1874 (attested in editions [1919, 1920, 1921])
- Appears in editions: [1919, 1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1919-L53169.v` — printed in editions [1919, 1920, 1921]:**

> HOOPER, EDWARD CECIL.—B. 1874; S.A. War Service (Queen's Medal, 4 Clasps); Transvaal Pol., Dec., 1900; 1st grade clerical, asst., P.W.D., Oct., 1901; acctnt., P.W.D., July, 1903; sec. war stores coman., May, 1915; acctnt., S.W.A. Prot., Aug., 1916; acctng. offr., S.W.A. Prot., Jan., 1917; ag. sec., S.W.A. Prot., Dec., 1917 to Jan., 1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | Transvaal Pol | Transvaal | [1919, 1920, 1921] |
| 1 | 1901 | 1st grade clerical, asst., P.W.D | Transvaal *(inherited from previous clause)* | [1919, 1920, 1921] |
| 2 | 1903 | acctnt., P.W.D | Transvaal *(inherited from previous clause)* | [1919, 1920, 1921] |
| 3 | 1915 | sec. war stores coman | Transvaal *(inherited from previous clause)* | [1919, 1920, 1921] |
| 4 | 1916 | acctnt., S.W.A. Prot | Transvaal *(inherited from previous clause)* | [1919, 1920, 1921] |
| 5 | 1917 | acctng. offr., S.W.A. Prot | Transvaal *(inherited from previous clause)* | [1919, 1920, 1921] |

## Candidate stint `Hooper, E. C___South Africa___1912`

- Staff-list name: **Hooper, E. C** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | E. C. Hooper | Accountant | Province of Transvaal | — | — |
| 1914 | E. C. Hooper | Accountant | Public Works Department | — | — |
| 1918 | E. C. Hooper | Accountant | Public Works Department | — | — |

### Deterministic checks: `hooper_edward-cecil_b1874` vs `Hooper, E. C___South Africa___1912`

- [PASS] surname_gate: bio 'HOOPER' vs stint 'Hooper, E. C' (exact)
- [PASS] initials: bio ['E', 'C'] ~ stint ['E', 'C']
- [PASS] age_gate: stint starts 1912, birth 1874 (age 38)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

