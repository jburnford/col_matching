<!-- {"case_id": "case_innes_e_e1881", "bio_ids": ["innes_e_e1881"], "stint_ids": ["Innes, E___Tasmania___1888", "Innes, Ed___Western Australia___1896"]} -->
# Dossier case_innes_e_e1881

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['innes_e_e1881'] carry a single initial only — the namesake trap applies.

## Biography `innes_e_e1881`

- Printed name: **INNES, E**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34174.v` — printed in editions [1886]:**

> INNES, E.—Resident engineer, Natal harbour board, 22 Sept., 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Resident engineer, Natal harbour board | Natal | [1886] |

## Candidate stint `Innes, E___Tasmania___1888`

- Staff-list name: **Innes, E** | colony: **Tasmania** | listed 1888–1889 | editions [1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | E. Innes | Resident S. M. and Coroner, Kingston | District of Kingborough. | — | — |
| 1889 | E. Innes | Resident S. M. and Coroner | Magistracy | — | — |

### Deterministic checks: `innes_e_e1881` vs `Innes, E___Tasmania___1888`

- [PASS] surname_gate: bio 'INNES' vs stint 'Innes, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Tasmania'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1889
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Innes, Ed___Western Australia___1896`

- Staff-list name: **Innes, Ed** | colony: **Western Australia** | listed 1896–1898 | editions [1896, 1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | Ed. Innes | Mining Registrar | Mining Department | — | — |
| 1897 | E. Innes | Mining Registrar | Mining Department | — | — |
| 1898 | E. Innes | Mining Registrar | Mining Department | — | — |

### Deterministic checks: `innes_e_e1881` vs `Innes, Ed___Western Australia___1896`

- [PASS] surname_gate: bio 'INNES' vs stint 'Innes, Ed' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Western Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1898
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

