<!-- {"case_id": "case_becker_f_e1852", "bio_ids": ["becker_f_e1852"], "stint_ids": ["Becker, F. E___Australia___1913", "Becker, F. E___South Australia___1889", "Becker, F. R___Natal___1879"]} -->
# Dossier case_becker_f_e1852

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['becker_f_e1852'] carry a single initial only — the namesake trap applies.

## Biography `becker_f_e1852`

- Printed name: **BECKER, F.**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26377.v` — printed in editions [1883]:**

> BECKER, F.—Clerk to the resident magistrate, Klip River division, Natal, April, 1852; landing waiter in the customs' department, Dec., 1857, first clerk in the office of colonial secretary of that colony, 1860; postmaster-general of Natal, 1865.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1852 | Clerk to the resident magistrate | Natal | [1883] |
| 1 | 1857 | landing waiter | — | [1883] |
| 2 | 1860 | first clerk in the office of colonial secretary | Natal | [1883] |
| 3 | 1865 | postmaster-general | Natal | [1883] |

## Candidate stint `Becker, F. E___Australia___1913`

- Staff-list name: **Becker, F. E** | colony: **Australia** | listed 1913–1927 | editions [1913, 1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | F. E. Becker | Clerk and Storekeeper | Yatala Labour Prison | — | — |
| 1918 | F. E. Becker | Keeper of Adelaide Gaol | Sheriff's Department | — | — |
| 1927 | F. E. Becker | Superintendent | Yatala Labor Prison | — | — |

### Deterministic checks: `becker_f_e1852` vs `Becker, F. E___Australia___1913`

- [PASS] surname_gate: bio 'BECKER' vs stint 'Becker, F. E' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F', 'E']
- [PASS] age_gate: stint starts 1913; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Becker, F. E___South Australia___1889`

- Staff-list name: **Becker, F. E** | colony: **South Australia** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | F. E. Becker | Keeper H.M. Goal | Northern Territory | — | — |
| 1890 | F. E. Becker | Keeper H.M. Gaol | NORTHERN TERRITORY | — | — |

### Deterministic checks: `becker_f_e1852` vs `Becker, F. E___South Australia___1889`

- [PASS] surname_gate: bio 'BECKER' vs stint 'Becker, F. E' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F', 'E']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Becker, F. R___Natal___1879`

- Staff-list name: **Becker, F. R** | colony: **Natal** | listed 1879–1890 | editions [1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | F. R. Becker | 2nd Clerk | Post and Telegraph Department | — | — |
| 1880 | F. R. Becker | 2nd Clerk | Postal Department | — | — |
| 1883 | F. R. Becker | 2nd Clerk | Postal | — | — |
| 1886 | F. R. Becker | Clerk | Postal | — | — |
| 1888 | F. R. Becker | Clerk | Postal | — | — |
| 1889 | F. R. Becker | Clerk | Postal | — | — |
| 1890 | F. R. Becker | Clerk | Postal | — | — |

### Deterministic checks: `becker_f_e1852` vs `Becker, F. R___Natal___1879`

- [PASS] surname_gate: bio 'BECKER' vs stint 'Becker, F. R' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F', 'R']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Natal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1890
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

