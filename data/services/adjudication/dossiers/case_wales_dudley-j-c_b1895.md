<!-- {"case_id": "case_wales_dudley-j-c_b1895", "bio_ids": ["wales_dudley-j-c_b1895", "wales_john_e1906"], "stint_ids": ["Wales, J___Fiji___1918"]} -->
# Dossier case_wales_dudley-j-c_b1895

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['wales_john_e1906'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Wales, J___Fiji___1918'] have more than one claimant biography in this case.

## Biography `wales_dudley-j-c_b1895`

- Printed name: **WALES, Dudley J. C**
- Birth year: 1895 (attested in editions [1931])
- Appears in editions: [1931]

### Verbatim printed entry text (OCR)

**Version `col1931-L69094.v` — printed in editions [1931]:**

> WALES, Dudley J. C.—B. 1895; ed. Merchant Taylors Schl.; served with H.A.C. in France, 1914-15; 2nd lieut., Middlesex Regt., 1915; W. African Regt., Sierra Leone, Nigeria, 1916-17; transf., 2nd K.A.R. and served in E. Africa 1918-21; Somaliland campaign, 1920; dist. pol. offr. Somaliland, Feb., 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1915 | served with H.A.C. in France | — | [1931] |
| 1 | 1915 | 2nd lieut., Middlesex Regt | — | [1931] |
| 2 | 1916–1917 | W. African Regt., Sierra Leone | Nigeria | [1931] |
| 3 | 1918–1921 | transf., 2nd K.A.R. and served in E. Africa | Nigeria *(inherited from previous clause)* | [1931] |
| 4 | 1920 | Somaliland campaign | Somaliland | [1931] |
| 5 | 1922 | dist. pol. offr. Somaliland | Somaliland *(inherited from previous clause)* | [1931] |

## Biography `wales_john_e1906`

- Printed name: **WALES, JOHN**
- Birth year: not printed
- Appears in editions: [1924]

### Verbatim printed entry text (OCR)

**Version `col1924-L58651.v` — printed in editions [1924]:**

> WALES, JOHN.—Ed. Rockwell Coll. and Univ. of London (Scholar, Inter. B.A.); served in dept. of special comans. of income tax and secretariat, inland revenue; apptd., after ops compet. exam., examiner, exchequer and audit dept., Feb., 1906; asst. local auditor G. Coast, Nov., 1908; auditor, Gambia, Apl., 1910; 2nd lieut., G. Coast, volrs., 1909; lieut., Gambia volr. artillery, 1910; qualified in Mandingo language, 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906 | apptd., after ops compet. exam., examiner, exchequer and audit dept | — | [1924] |
| 1 | 1908 | asst. local auditor G. Coast | — | [1924] |
| 2 | 1909 | 2nd lieut., G. Coast, volrs | Gambia *(inherited from previous clause)* | [1924] |
| 3 | 1910 | auditor | Gambia | [1924] |
| 4 | 1912 | qualified in Mandingo language | Gambia *(inherited from previous clause)* | [1924] |

## Candidate stint `Wales, J___Fiji___1918`

- Staff-list name: **Wales, J** | colony: **Fiji** | listed 1918–1921 | editions [1918, 1919, 1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | J. Wales | Assistant Master | Education Department | — | — |
| 1919 | J. Wales | Assistant Masters | Education Department | — | — |
| 1920 | J. Wales | Assistant Masters | Education Department | — | — |
| 1921 | J. Wales | Assistant Masters | Education Department | — | — |

### Deterministic checks: `wales_dudley-j-c_b1895` vs `Wales, J___Fiji___1918`

- [PASS] surname_gate: bio 'WALES' vs stint 'Wales, J' (exact)
- [PASS] initials: bio ['D', 'J', 'C'] ~ stint ['J']
- [PASS] age_gate: stint starts 1918, birth 1895 (age 23)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1921
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `wales_john_e1906` vs `Wales, J___Fiji___1918`

- [PASS] surname_gate: bio 'WALES' vs stint 'Wales, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1918; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1921
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

