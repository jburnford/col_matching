<!-- {"case_id": "case_dubisset_alexander_e1873", "bio_ids": ["dubisset_alexander_e1873"], "stint_ids": ["Bisset, A___Uganda___1911", "Bisset, Alex___Cape of Good Hope___1877"]} -->
# Dossier case_dubisset_alexander_e1873

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['dubisset_alexander_e1873'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Bisset, A___Uganda___1911` is also gate-compatible with biography(ies) outside this case: ['bisset_alexander_e1840'] (already linked elsewhere or filtered).
- NOTE: stint `Bisset, Alex___Cape of Good Hope___1877` is also gate-compatible with biography(ies) outside this case: ['bisset_alexander_e1840'] (already linked elsewhere or filtered).

## Biography `dubisset_alexander_e1873`

- Printed name: **DUBISSET, ALEXANDER**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27259.v` — printed in editions [1883]:**

> DUBISSET, ALEXANDER.—Clerk to magistrate, and district registrar of births and deaths, St. David, Grenada, 1873.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1873 | Clerk to magistrate, and district registrar of births and deaths, St. David | Grenada | [1883] |

## Candidate stint `Bisset, A___Uganda___1911`

- Staff-list name: **Bisset, A** | colony: **Uganda** | listed 1911–1929 | editions [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1925, 1927, 1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | A. Bisset | Foreman of Works | Public Works | — | — |
| 1912 | A. Bisset | Foreman of Works | Public Works | — | — |
| 1913 | A. Bisset | Overseer | Public Works | — | — |
| 1914 | A. Bisset | Overseer | Public Works | — | — |
| 1915 | A. Bisset | Assistant Engineer | Public Works | — | — |
| 1917 | A. Bisset | Assistant Engineer | Public Works | — | — |
| 1918 | A. Bisset | Assistant Engineer | Public Works | — | — |
| 1919 | A. Bisset | Assistant Engineer | Public Works | — | — |
| 1920 | A. Bisset | District Engineer | Public Works | — | — |
| 1921 | A. Bisset | Engineer | Public Works | — | — |
| 1922 | A. Bisset | Assistant Engineer | Public Works | — | — |
| 1923 | A. Bisset | Assistant Engineer | Public Works | — | — |
| 1925 | A. Bisset | Assistant Engineer | Public Works | — | — |
| 1927 | A. Bisset | Assistant Engineer | Public Works | — | — |
| 1928 | A. Bisset | Assistant Engineer | Public Works | — | — |
| 1929 | A. Bisset | Senior Assistant Engineer | Public Works | — | — |

### Deterministic checks: `dubisset_alexander_e1873` vs `Bisset, A___Uganda___1911`

- [PASS] surname_gate: bio 'DUBISSET' vs stint 'Bisset, A' (fuzzy:2)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1929
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bisset, Alex___Cape of Good Hope___1877`

- Staff-list name: **Bisset, Alex** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1878, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Alex. Bisset | Civil Commissioner and Resident Magistrate | Police Branch | — | — |
| 1878 | Alex. Bisset | Civil Commissioner and Resident Magistrate | Division of Pietermaritzburg | — | — |
| 1880 | Alex. Bisset | Civil Commissioner and Resident Magistrate | DIVISION OF PIQUETBERG | — | — |

### Deterministic checks: `dubisset_alexander_e1873` vs `Bisset, Alex___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'DUBISSET' vs stint 'Bisset, Alex' (fuzzy:2)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

