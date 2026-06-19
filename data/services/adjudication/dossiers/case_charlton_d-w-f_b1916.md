<!-- {"case_id": "case_charlton_d-w-f_b1916", "bio_ids": ["charlton_d-w-f_b1916"], "stint_ids": ["Charlton, D. W. F___Kenya___1949"]} -->
# Dossier case_charlton_d-w-f_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `charlton_d-w-f_b1916`

- Printed name: **CHARLTON, D. W. F**
- Birth year: 1916 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1958-L21316.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> CHARLTON, D. W. F.—b. 1916; ed. Fettes Coll., Edin., Camb. Univ., and Guy's Hosp.; mil. serv., 1942–46, flt. lt.; M.O., Ken., 1946; senr. M.O., 1962–64. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | M.O. | Kenya | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1962–1964 | senr. M.O | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Charlton, D. W. F___Kenya___1949`

- Staff-list name: **Charlton, D. W. F** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. W. F. Charlton | Medical Officer | Medical | — | — |
| 1950 | D. W. F. Charlton | Medical Officer | Medical | — | — |
| 1951 | D. W. F. Charlton | Medical Officer | Medical | — | — |

### Deterministic checks: `charlton_d-w-f_b1916` vs `Charlton, D. W. F___Kenya___1949`

- [PASS] surname_gate: bio 'CHARLTON' vs stint 'Charlton, D. W. F' (exact)
- [PASS] initials: bio ['D', 'W', 'F'] ~ stint ['D', 'W', 'F']
- [PASS] age_gate: stint starts 1949, birth 1916 (age 33)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

