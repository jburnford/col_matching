<!-- {"case_id": "case_woedehouse_h-e_e1867", "bio_ids": ["woedehouse_h-e_e1867"], "stint_ids": ["Wodehouse, H. E___Hong Kong___1877"]} -->
# Dossier case_woedehouse_h-e_e1867

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Wodehouse, H. E___Hong Kong___1877` is also gate-compatible with biography(ies) outside this case: ['woodehouse_h-e_b1845'] (already linked elsewhere or filtered).

## Biography `woedehouse_h-e_e1867`

- Printed name: **WOEDEHOUSE, H. E.**
- Birth year: not printed
- Honours: C.M.G. (1886)
- Appears in editions: [1889]

### Verbatim printed entry text (OCR)

**Version `col1889-L36373.v` — printed in editions [1889]:**

> WOEDEHOUSE, H. E., C.M.G. (1886).—Hong Kong cadet, 1867; student interpreter, 1869; superintendent of Chinese police, 1872; assistant colonial secretary and auditor, and clerk of councils, 1875; 1st Mar., 1877, acting colonial secretary; police magistrate and coroner, 1881; in 1885 honorary secretary to the local commission in connection with the Indian and Colonial Exhibition, 1886.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1867 | cadet | Hong Kong | [1889] |
| 1 | 1869 | student interpreter | — | [1889] |
| 2 | 1872 | superintendent of Chinese police | — | [1889] |
| 3 | 1875 | assistant colonial secretary and auditor, and clerk of councils | — | [1889] |
| 4 | 1877 | acting colonial secretary | — | [1889] |
| 5 | 1881 | police magistrate and coroner | — | [1889] |
| 6 | 1885–1886 | honorary secretary to the local commission in connection with the Indian and Colonial Exhibition | — | [1889] |

## Candidate stint `Wodehouse, H. E___Hong Kong___1877`

- Staff-list name: **Wodehouse, H. E** | colony: **Hong Kong** | listed 1877–1898 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894, 1896, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. E. Wodehouse | Chief Clerk | Colonial Secretary's Department | — | — |
| 1878 | H. E. Wodehouse | Acting Registrar-General | Registrar-General's Department | — | — |
| 1878 | H. E. Wodehouse | Chief Clerk | Colonial Secretary's Department | — | — |
| 1879 | H. E. Wodehouse | Chief Clerk | Colonial Secretary's Department | — | — |
| 1880 | H. E. Wodehouse | Chief Clerk | Colonial Secretary's Department | — | — |
| 1883 | H. E. Wodehouse | Police Magistrate | Police Court | — | — |
| 1883 | H. E. Wodehouse | Coroner | Supreme Court | — | — |
| 1886 | H. E. Wodehouse | Police Magistrate | Police Court | — | — |
| 1886 | H. E. Wodehouse | Superintendent | Fire Brigade | — | — |
| 1886 | H. E. Wodehouse | Coroner | Supreme Court | — | — |
| 1888 | H. E. Wodehouse | Superintendent | Fire Brigade | C.M.G. | — |
| 1888 | H. E. Wodehouse | Coroner | Supreme Court | C.M.G. | — |
| 1888 | H. E. Wodehouse | Police Magistrate | Police Court | C.M.G. | — |
| 1889 | H. E. Wodehouse | Superintendent | Fire Brigade | C.M.G. | — |
| 1889 | H. E. Wodehouse | Police Magistrate | Police Court | C.M.G. | — |
| 1890 | H. E. Wodehouse | Superintendent | Fire Brigade | C.M.G. | — |
| 1890 | H. E. Wodehouse | Police Magistrate | Police Court | C.M.G. | — |
| 1894 | H. E. Wodehouse | Police Magistrate | Police Court | C.M.G. | — |
| 1896 | H. E. Wodehouse | Police Magistrate | Police Court | C.M.G. | — |
| 1898 | H. E. Wodehouse | Police Magistrate and Coroner | Police Court | C.M.G. | — |

### Deterministic checks: `woedehouse_h-e_e1867` vs `Wodehouse, H. E___Hong Kong___1877`

- [PASS] surname_gate: bio 'WOEDEHOUSE' vs stint 'Wodehouse, H. E' (fuzzy:1)
- [PASS] initials: bio ['H', 'E'] ~ stint ['H', 'E']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1898
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G.
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

