<!-- {"case_id": "case_beeching_cecil-frederic_e1895", "bio_ids": ["beeching_cecil-frederic_e1895"], "stint_ids": ["Beeching, C. F___British Central Africa___1906", "Beeching, C. F___Nyasaland___1908"]} -->
# Dossier case_beeching_cecil-frederic_e1895

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `beeching_cecil-frederic_e1895`

- Printed name: **BEECHING, CECIL FREDERIC**
- Birth year: not printed
- Appears in editions: [1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1908-L43112.v` — printed in editions [1908, 1909]:**

> BEECHING, CAPT. CECIL FREDERIC.—Ed. Haileybury Coll.; seconded from 3rd R.W. Kent Regt. (militia); 3rd asst. collr., B.C. Africa Prot., May, 1895; 2nd cls. asst. collr., July, 1898; 1st cls. dist. res., Oct., 1906; served in S. African war whilst on leave from B.C.A., 1900.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | 3rd asst. collr., B.C. Africa Prot | British Columbia | [1908, 1909] |
| 1 | 1898 | 2nd cls. asst. collr | British Columbia *(inherited from previous clause)* | [1908, 1909] |
| 2 | 1900 | served in S. African war whilst on leave from B.C.A | British Columbia *(inherited from previous clause)* | [1908, 1909] |
| 3 | 1906 | 1st cls. dist. res | British Columbia *(inherited from previous clause)* | [1908, 1909] |

## Candidate stint `Beeching, C. F___British Central Africa___1906`

- Staff-list name: **Beeching, C. F** | colony: **British Central Africa** | listed 1906–1907 | editions [1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | C. F. Beeching | 2nd class Assistant | Collectors | — | Captain |
| 1907 | C. F. Beeching | Twelve 2nd class | Residents | — | Captain |

### Deterministic checks: `beeching_cecil-frederic_e1895` vs `Beeching, C. F___British Central Africa___1906`

- [PASS] surname_gate: bio 'BEECHING' vs stint 'Beeching, C. F' (exact)
- [PASS] initials: bio ['C', 'F'] ~ stint ['C', 'F']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Central Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1907
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Beeching, C. F___Nyasaland___1908`

- Staff-list name: **Beeching, C. F** | colony: **Nyasaland** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | C. F. Beeching | Resident 1st class | Residents | — | Captain |
| 1909 | C. F. Beeching | Resident, 1st class | Residents | — | Captain |

### Deterministic checks: `beeching_cecil-frederic_e1895` vs `Beeching, C. F___Nyasaland___1908`

- [PASS] surname_gate: bio 'BEECHING' vs stint 'Beeching, C. F' (exact)
- [PASS] initials: bio ['C', 'F'] ~ stint ['C', 'F']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1909
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

