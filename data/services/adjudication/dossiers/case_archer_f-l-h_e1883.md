<!-- {"case_id": "case_archer_f-l-h_e1883", "bio_ids": ["archer_f-l-h_e1883"], "stint_ids": ["Archer, F. Hamilton___Tasmania___1894", "Archer, F. L___Barbados___1909"]} -->
# Dossier case_archer_f-l-h_e1883

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 40 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `archer_f-l-h_e1883`

- Printed name: **ARCHER, F. L. H.**
- Birth year: not printed
- Appears in editions: [1907]

### Verbatim printed entry text (OCR)

**Version `col1907-L42807.v` — printed in editions [1907]:**

> ARCHER, F. L. H.—Ent. pub. service corrspcll. branch, col. sec.'s off., Barbados, 1883; promoted gen. post-office, 1884; customs, 1890; 2nd cls. supervisor, G. Coast, June, 1902; ag. ch. regisr. and sheriff, G. Coast, 11th Dec., 1902, to 8th June, 1903, and 30th July, to 25th Dec., 1904; 1st cls. supervisor, 27th Sept., 1904; asst. collr., Lagos, 26th Dec., 1904; ag. collr. of cust., 29th Oct., 1905, to 1st May, 1906; postmr.-gen.l., S. Nigeria, 14th May, 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Ent. pub. service corrspcll. branch, col. sec.'s off. | Barbados | [1907] |
| 1 | 1884 | promoted gen. post-office | — | [1907] |
| 2 | 1890 | customs | — | [1907] |
| 3 | 1902 | 2nd cls. supervisor | Gold Coast | [1907] |
| 4 | 1904 | 1st cls. supervisor | — | [1907] |
| 5 | 1904 | asst. collr. | Lagos | [1907] |
| 6 | 1905–1906 | ag. collr. of cust. | — | [1907] |
| 7 | 1906 | postmr.-gen.l. | Southern Nigeria | [1907] |

## Candidate stint `Archer, F. Hamilton___Tasmania___1894`

- Staff-list name: **Archer, F. Hamilton** | colony: **Tasmania** | listed 1894–1900 | editions [1894, 1896, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | Archer, F. | Chairman of Committees | House of Assembly | — | — |
| 1896 | F. Archer | Member | House of Assembly | — | — |
| 1898 | F. Gilmore Archer | G. C. | House of Assembly | — | — |
| 1899 | F. Hamilton Archer | — | House of Assembly | — | — |
| 1900 | F. Archer | Member | House of Assembly | — | — |

### Deterministic checks: `archer_f-l-h_e1883` vs `Archer, F. Hamilton___Tasmania___1894`

- [PASS] surname_gate: bio 'ARCHER' vs stint 'Archer, F. Hamilton' (exact)
- [PASS] initials: bio ['F', 'L', 'H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Tasmania'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1900
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Archer, F. L___Barbados___1909`

- Staff-list name: **Archer, F. L** | colony: **Barbados** | listed 1909–1913 | editions [1909, 1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | F. L. Archer | Junior Clerk | Public Library | — | — |
| 1910 | F. L. Archer | Assistant Clerk | Audit Office | — | — |
| 1911 | F. L. Archer | Assistant Clerk | Audit Office | — | — |
| 1912 | F. L. Archer | Clerk | Public Library | — | — |
| 1913 | F. L. Archer | Clerk | Public Library | — | — |

### Deterministic checks: `archer_f-l-h_e1883` vs `Archer, F. L___Barbados___1909`

- [PASS] surname_gate: bio 'ARCHER' vs stint 'Archer, F. L' (exact)
- [PASS] initials: bio ['F', 'L', 'H'] ~ stint ['F', 'L']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Barbados'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1913
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

