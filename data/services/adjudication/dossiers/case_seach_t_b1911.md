<!-- {"case_id": "case_seach_t_b1911", "bio_ids": ["seach_t_b1911"], "stint_ids": ["Search, T. W. V___Gold Coast___1949"]} -->
# Dossier case_seach_t_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['seach_t_b1911'] carry a single initial only — the namesake trap applies.

## Biography `seach_t_b1911`

- Printed name: **SEACH, T**
- Birth year: 1911 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L21575.v` — printed in editions [1964, 1965, 1966]:**

> SEACH, T.—b. 1911; ed. Cooper's Company's Coll.; mil. serv., 1939-45, R.A.F., sgt.; ch. dftsmn., H.K., 1947; land survr., 1952; senr. land survr., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | ch. dftsmn. | Hong Kong | [1964, 1965, 1966] |
| 1 | 1952 | land survr | Hong Kong *(inherited from previous clause)* | [1964, 1965, 1966] |
| 2 | 1960 | senr. land survr | Hong Kong *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Search, T. W. V___Gold Coast___1949`

- Staff-list name: **Search, T. W. V** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | T. W. V. Search | Accountants | Public Works | — | — |
| 1951 | T. W. V. Search | Accountants | Accounting and Storekeeping Staff | — | — |

### Deterministic checks: `seach_t_b1911` vs `Search, T. W. V___Gold Coast___1949`

- [PASS] surname_gate: bio 'SEACH' vs stint 'Search, T. W. V' (fuzzy:1)
- [PASS] initials: bio ['T'] ~ stint ['T', 'W', 'V']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

