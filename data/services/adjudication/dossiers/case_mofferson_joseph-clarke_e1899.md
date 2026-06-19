<!-- {"case_id": "case_mofferson_joseph-clarke_e1899", "bio_ids": ["mofferson_joseph-clarke_e1899"], "stint_ids": ["Jefferson, Julian___Jamaica___1946"]} -->
# Dossier case_mofferson_joseph-clarke_e1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Jefferson, Julian___Jamaica___1946` is also gate-compatible with biography(ies) outside this case: ['jefferson_j-h-k_b1915'] (already linked elsewhere or filtered).

## Biography `mofferson_joseph-clarke_e1899`

- Printed name: **MOFFERSON, JOSEPH CLARKE**
- Birth year: not printed
- Appears in editions: [1915]

### Verbatim printed entry text (OCR)

**Version `col1915-L48911.v` — printed in editions [1915]:**

> MOFFERSON, JOSEPH CLARKE, M.B., B.C.L., B.A.O., R.U.—Ed. at Queen's coll., Belfast; graduated, 1904; medical scholarships, Queen's coll., Belfast, 1899, 1901; honours, Roy. univ., Ireland, 1899, 1900, 1901; aast. med. off., Edmonton infirmary, 1904-1905; private practice 1906-1908; ag. med. off., dist. 3, St. Kitts Leeward Is., 1909; med. off. distr. 5, Anguilla, 1910; med. off. distr. 7, Nevis, 1912; senr. med. off., Montserrat, 12th Oct., 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899–1901 | medical scholarships | — | [1915] |
| 1 | 1899–1901 | honours | — | [1915] |
| 2 | 1904–1904 | — | — | [1915] |
| 3 | 1904–1905 | aast. med. off. | — | [1915] |
| 4 | 1906–1908 | private practice | — | [1915] |
| 5 | 1909–1909 | ag. med. off. | Leeward Islands | [1915] |
| 6 | 1910–1910 | med. off. | Anguilla | [1915] |
| 7 | 1912–1912 | med. off. | Nevis | [1915] |

## Candidate stint `Jefferson, Julian___Jamaica___1946`

- Staff-list name: **Jefferson, Julian** | colony: **Jamaica** | listed 1946–1948 | editions [1946, 1948]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1946 | Julian Jefferson | Officer Commanding the Troops in Jamaica | Privy Council | — | — |
| 1948 | Julian Jefferson | Officer Commanding the Troops in Jamaica | Privy Council | — | — |

### Deterministic checks: `mofferson_joseph-clarke_e1899` vs `Jefferson, Julian___Jamaica___1946`

- [PASS] surname_gate: bio 'MOFFERSON' vs stint 'Jefferson, Julian' (fuzzy:2)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J']
- [PASS] age_gate: stint starts 1946; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1946-1948
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

