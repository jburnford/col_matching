<!-- {"case_id": "case_rugles_nepean-clarke_e1891", "bio_ids": ["rugles_nepean-clarke_e1891"], "stint_ids": ["Ruggles, N. C___British Guiana___1923", "Ruggles, N. C___Leeward Islands___1911"]} -->
# Dossier case_rugles_nepean-clarke_e1891

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Ruggles, N. C___British Guiana___1923` is also gate-compatible with biography(ies) outside this case: ['ruggles_nepean-clarke_e1891'] (already linked elsewhere or filtered).
- NOTE: stint `Ruggles, N. C___Leeward Islands___1911` is also gate-compatible with biography(ies) outside this case: ['ruggles_nepean-clarke_e1891'] (already linked elsewhere or filtered).

## Biography `rugles_nepean-clarke_e1891`

- Printed name: **RUGLES, NEPEAN CLARKE**
- Birth year: not printed
- Appears in editions: [1911]

### Verbatim printed entry text (OCR)

**Version `col1911-L47736.v` — printed in editions [1911]:**

> RUGLES, NEPEAN CLARKE.—Barrister of sup. ct., Nova Scotia; Bachelor of Laws at Dalhousie Coll., Halifax, Canada, with honours, 1891; called to the bar, Nova Scotia, with highest honours, 1891; served with the Canadian forces during S. African War; now on the reserve of officers, Canadian militia; public prosecutor at Barberton, Transvaal, 1901; asst. res. mag., 1903 to 1907; mag., Dist. F., Dominica, Oct., 1909.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891 | Bachelor of Laws at Dalhousie Coll., Halifax, Canada, with honours | — | [1911] |
| 1 | 1891 | called to the bar, Nova Scotia, with highest honours | — | [1911] |
| 2 | 1901 | public prosecutor at Barberton | Transvaal | [1911] |
| 3 | 1903–1907 | asst. res. mag | Transvaal *(inherited from previous clause)* | [1911] |
| 4 | 1909 | mag., Dist. F. | Dominica | [1911] |

## Candidate stint `Ruggles, N. C___British Guiana___1923`

- Staff-list name: **Ruggles, N. C** | colony: **British Guiana** | listed 1923–1930 | editions [1923, 1924, 1925, 1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | N. C. Ruggles | District Stipendiary Magistrate | Judicial Establishment | — | — |
| 1924 | N. C. Ruggles | District Stipendiary Magistrate | Judicial Establishment | — | — |
| 1925 | N. C. Ruggles | District Stipendiary Magistrate | Judicial Establishment | — | — |
| 1927 | N. C. Ruggles | District Stipendiary Magistrate | Judicial | — | — |
| 1928 | N. C. Ruggles | District Stipendiary Magistrate | Judicial | — | — |
| 1929 | N. C. Ruggles | District Stipendiary Magistrate | Judicial | — | — |
| 1930 | N. C. Ruggles | District Stipendiary Magistrate | Judicial | — | — |

### Deterministic checks: `rugles_nepean-clarke_e1891` vs `Ruggles, N. C___British Guiana___1923`

- [PASS] surname_gate: bio 'RUGLES' vs stint 'Ruggles, N. C' (fuzzy:1)
- [PASS] initials: bio ['N', 'C'] ~ stint ['N', 'C']
- [PASS] age_gate: stint starts 1923; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1930
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Ruggles, N. C___Leeward Islands___1911`

- Staff-list name: **Ruggles, N. C** | colony: **Leeward Islands** | listed 1911–1915 | editions [1911, 1912, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | N. C. Ruggles | Magistrate, District F. | Judicial Establishment | — | — |
| 1912 | N. C. Ruggles | Magistrate, District F. | Judicial Establishment | — | — |
| 1913 | N. C. Ruggles | Magistrate, District F. | Judicial Establishment | — | — |
| 1914 | N. C. Ruggles | Magistrate, District F. | Judicial Establishment | — | — |
| 1915 | N. C. Ruggles | Magistrate, District F. | Judicial Establishment | — | — |

### Deterministic checks: `rugles_nepean-clarke_e1891` vs `Ruggles, N. C___Leeward Islands___1911`

- [PASS] surname_gate: bio 'RUGLES' vs stint 'Ruggles, N. C' (fuzzy:1)
- [PASS] initials: bio ['N', 'C'] ~ stint ['N', 'C']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1915
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

