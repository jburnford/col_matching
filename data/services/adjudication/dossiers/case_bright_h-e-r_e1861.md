<!-- {"case_id": "case_bright_h-e-r_e1861", "bio_ids": ["bright_h-e-r_e1861"], "stint_ids": ["Bright, H. E. R___Cape of Good Hope___1877", "Bright, Henry E___South Australia___1878"]} -->
# Dossier case_bright_h-e-r_e1861

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bright_h-e-r_e1861`

- Printed name: **BRIGHT, H. E. R.**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L26576.v` — printed in editions [1883, 1886]:**

> BRIGHT, H. E. R.—Under secretary for native affairs, Cape of Good Hope; gazetted a sworn government land surveyor, 1868; in which capacity proceeded eastwards in November, 1861, and surveyed a large portion of the then Crown Colony of British Kaffraria; on the annexation of British Basutoland, was appointed chief clerk to the governor's agent, and chief magistrate in that territory (Nov., 1871); promoted to be chief clerk to the secretary for native affairs (1874); and to be under secretary (permanent head of the department), July 1st, 1878; civil commissioner and resident magistrate, Stellenbosch, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861–1861 | — | British Kaffraria | [1883, 1886] |
| 1 | 1868–1868 | sworn government land surveyor | — | [1883, 1886] |
| 2 | 1871–1871 | chief clerk to the governor's agent, and chief magistrate | British Basutoland | [1883, 1886] |
| 3 | 1874–1874 | chief clerk to the secretary for native affairs | — | [1883, 1886] |
| 4 | 1878–1878 | under secretary (permanent head of the department) | — | [1883, 1886] |
| 5 | 1881–1881 | civil commissioner and resident magistrate | Stellenbosch | [1883, 1886] |
| 6 | ? | Under secretary for native affairs | Cape of Good Hope | [1883, 1886] |

## Candidate stint `Bright, H. E. R___Cape of Good Hope___1877`

- Staff-list name: **Bright, H. E. R** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. E. R. Bright | Chief Clerk | Department of Native Affairs | — | — |
| 1879 | H. E. R. Bright | Under Secretary | Department of Native Affairs | — | — |
| 1880 | H. E. R. Bright | Under Secretary | Department of Native Affairs | — | — |

### Deterministic checks: `bright_h-e-r_e1861` vs `Bright, H. E. R___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'BRIGHT' vs stint 'Bright, H. E. R' (exact)
- [PASS] initials: bio ['H', 'E', 'R'] ~ stint ['H', 'E', 'R']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bright, Henry E___South Australia___1878`

- Staff-list name: **Bright, Henry E** | colony: **South Australia** | listed 1878–1879 | editions [1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | H. E. Bright | Member | House of Assembly | — | — |
| 1879 | H. E. Bright | Member | House of Assembly | — | — |

### Deterministic checks: `bright_h-e-r_e1861` vs `Bright, Henry E___South Australia___1878`

- [PASS] surname_gate: bio 'BRIGHT' vs stint 'Bright, Henry E' (exact)
- [PASS] initials: bio ['H', 'E', 'R'] ~ stint ['H', 'E']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1879
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

