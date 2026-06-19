<!-- {"case_id": "case_covington_m_e1849", "bio_ids": ["covington_m_e1849"], "stint_ids": ["Covington, M___Ceylon___1877"]} -->
# Dossier case_covington_m_e1849

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['covington_m_e1849'] carry a single initial only — the namesake trap applies.

## Biography `covington_m_e1849`

- Printed name: **COVINGTON, M.**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26978.v` — printed in editions [1883]:**

> COVINGTON, M.—Lic. Med. and Surg., Bengal College. Medical sub-assistant to the government of Ceylon, 3rd class, June, 1849; 2nd class, 1855; medical assistant, 1858, and assistant colonial surgeon, 1859, ditto, 1st class, 1867.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1849 | Medical sub-assistant, 3rd class | Ceylon | [1883] |
| 1 | 1855 | Medical sub-assistant, 2nd class | — | [1883] |
| 2 | 1858 | medical assistant | — | [1883] |
| 3 | 1859 | assistant colonial surgeon | — | [1883] |
| 4 | 1867 | assistant colonial surgeon, 1st class | — | [1883] |

## Candidate stint `Covington, M___Ceylon___1877`

- Staff-list name: **Covington, M** | colony: **Ceylon** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | M. Covington | Assistant Colonial Surgeons | Medical Department | — | — |
| 1878 | M. Covington | Assistant Colonial Surgeons | Medical Department | — | — |
| 1879 | M. Covington | Assistant Colonial Surgeons | Medical Department | — | — |
| 1880 | M. Covington | Assistant Colonial Surgeons | Medical Department | — | — |
| 1883 | M. Covington | Assistant Colonial Surgeon | Medical Department | — | — |

### Deterministic checks: `covington_m_e1849` vs `Covington, M___Ceylon___1877`

- [PASS] surname_gate: bio 'COVINGTON' vs stint 'Covington, M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
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

