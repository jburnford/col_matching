<!-- {"case_id": "case_mccrae_john_e1903", "bio_ids": ["mccrae_john_e1903"], "stint_ids": ["McCrae, J___South Africa___1912"]} -->
# Dossier case_mccrae_john_e1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mccrae_john_e1903'] carry a single initial only — the namesake trap applies.

## Biography `mccrae_john_e1903`

- Printed name: **MCCRAE, JOHN**
- Birth year: not printed
- Honours: F.I.C, M.S.P.A
- Appears in editions: [1923, 1931]

### Verbatim printed entry text (OCR)

**Version `col1931-L66319.v` — printed in editions [1931]:**

> MCCRAE, JOHN, Ph.D., F.I.C., M.S.P.A., F. Chem. Soc., Pestly Schol., Ehrhardt prizeman—Asst. chem., dept. of agr., Pretoria, 1903; ag. govt. chemist, col. sec.'s office, 1906; app't confirmed, 1907; dept. of int., 1912; govt. analyst, 1917; examr., physiochem. and chem., Transvaal Pharmacy Bd., 1916; examr., chemery., Univ. of S. Africa, 1920; transf'd. to dept. of agr., 1st Apr., 1923.

**Version `col1923-L56277.v` — printed in editions [1923]:**

> McCRAE, JOHN, Ph.D., F.I.C., M.S.P.A.—Asst. chem., dept. of agr., Pretoria, 1903; govt. analyst, Johannesburg, 1906; examr., physics and chem., Transvaal Pharmacy Bd., 1916; examr., chem., Univ. of S. Africa, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | Asst. chem., dept. of agr., Pretoria | — | [1923, 1931] |
| 1 | 1906 | ag. govt. chemist, col. sec.'s office | — | [1931] |
| 2 | 1906 | govt. analyst, Johannesburg | — | [1923] |
| 3 | 1907 | app't confirmed | — | [1931] |
| 4 | 1912 | dept. of int | — | [1931] |
| 5 | 1916 | examr., physiochem. and chem., Transvaal Pharmacy Bd | Transvaal | [1923, 1931] |
| 6 | 1917 | govt. analyst | — | [1931] |
| 7 | 1920 | examr., chemery., Univ. of S. Africa | Transvaal *(inherited from previous clause)* | [1923, 1931] |
| 8 | 1923 | transf'd. to dept. of agr | Transvaal *(inherited from previous clause)* | [1931] |

## Candidate stint `McCrae, J___South Africa___1912`

- Staff-list name: **McCrae, J** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | Dr. J. McCrae | Government Analyst | Analyses | — | — |
| 1914 | J. McCrae | Government Analyst, Transvaal | Analyses | — | — |
| 1918 | Dr. J. McCrae | Government Analyst | Analyses | — | — |

### Deterministic checks: `mccrae_john_e1903` vs `McCrae, J___South Africa___1912`

- [PASS] surname_gate: bio 'MCCRAE' vs stint 'McCrae, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

