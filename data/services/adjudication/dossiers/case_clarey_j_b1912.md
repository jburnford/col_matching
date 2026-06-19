<!-- {"case_id": "case_clarey_j_b1912", "bio_ids": ["clarey_j_b1912"], "stint_ids": ["Carey, A. de J___Western Pacific___1933", "Carey, J___Nyasaland___1928"]} -->
# Dossier case_clarey_j_b1912

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['clarey_j_b1912'] carry a single initial only — the namesake trap applies.

## Biography `clarey_j_b1912`

- Printed name: **CLAREY, J**
- Birth year: 1912 (attested in editions [1965, 1966])
- Appears in editions: [1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1965-L14260.v` — printed in editions [1965, 1966]:**

> CLAREY, J.—b. 1912; ed. Upperthorpe Sch., Sheffield and Univ. of Sheffield; mil. serv., 1942-46, capt., R.E.; tech. instr., H.K., 1951; educ. offr. (tech.), 1953; orgnsr. (tech.), 1960; senr. educ. offr., 1963-65.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | tech. instr. | Hong Kong | [1965, 1966] |
| 1 | 1960 | orgnsr. (tech.) | Hong Kong *(inherited from previous clause)* | [1965, 1966] |
| 2 | 1963–1965 | senr. educ. offr | Hong Kong *(inherited from previous clause)* | [1965, 1966] |

## Candidate stint `Carey, A. de J___Western Pacific___1933`

- Staff-list name: **Carey, A. de J** | colony: **Western Pacific** | listed 1933–1936 | editions [1933, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | A. de J. Carey | Judicial Commissioner | British Staff | — | — |
| 1936 | A. de J. Carey | Judicial Commissioner | British Staff | — | — |

### Deterministic checks: `clarey_j_b1912` vs `Carey, A. de J___Western Pacific___1933`

- [PASS] surname_gate: bio 'CLAREY' vs stint 'Carey, A. de J' (fuzzy:1)
- [PASS] initials: bio ['J'] ~ stint ['A', 'D', 'J']
- [PASS] age_gate: stint starts 1933, birth 1912 (age 21)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1936
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Carey, J___Nyasaland___1928`

- Staff-list name: **Carey, J** | colony: **Nyasaland** | listed 1928–1930 | editions [1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | J. Carey | Inspectors of Works | Public Works | — | — |
| 1929 | J. Carey | Inspector of Works | Public Works | — | — |
| 1930 | J. Carey | Inspector of Works | Public Works | — | — |

### Deterministic checks: `clarey_j_b1912` vs `Carey, J___Nyasaland___1928`

- [PASS] surname_gate: bio 'CLAREY' vs stint 'Carey, J' (fuzzy:1)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1928, birth 1912 (age 16)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1930
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

