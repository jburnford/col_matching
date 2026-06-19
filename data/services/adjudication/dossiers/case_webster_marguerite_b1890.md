<!-- {"case_id": "case_webster_marguerite_b1890", "bio_ids": ["webster_marguerite_b1890"], "stint_ids": ["Webster, Miss A___Windward Islands___1922", "Webster, Miss M___Bahamas___1931"]} -->
# Dossier case_webster_marguerite_b1890

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 44 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['webster_marguerite_b1890'] carry a single initial only — the namesake trap applies.

## Biography `webster_marguerite_b1890`

- Printed name: **WEBSTER, Marguerite**
- Birth year: 1890 (attested in editions [1949, 1950])
- Appears in editions: [1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1949-L36585.v` — printed in editions [1949, 1950]:**

> WEBSTER, Marguerite.—b. 1890; ed. Sheffield High Sch.; nursing sister, H.K., 1934; senr., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | nursing sister | Hong Kong | [1949, 1950] |
| 1 | 1944 | senr | Hong Kong *(inherited from previous clause)* | [1949, 1950] |

## Candidate stint `Webster, Miss A___Windward Islands___1922`

- Staff-list name: **Webster, Miss A** | colony: **Windward Islands** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | Miss A. Webster | Assistant Librarian | Boys' Secondary School | — | — |
| 1923 | Miss A. Webster | Assistant Librarian | Education | — | — |

### Deterministic checks: `webster_marguerite_b1890` vs `Webster, Miss A___Windward Islands___1922`

- [PASS] surname_gate: bio 'WEBSTER' vs stint 'Webster, Miss A' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M', 'A']
- [PASS] age_gate: stint starts 1922, birth 1890 (age 32)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Webster, Miss M___Bahamas___1931`

- Staff-list name: **Webster, Miss M** | colony: **Bahamas** | listed 1931–1933 | editions [1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | M. Webster | Sisters, Ave. | Medical Department | — | — |
| 1932 | Miss M. Webster | Sister | Medical Department | — | — |
| 1933 | Miss M. Webster | Sister | Medical Department | — | — |

### Deterministic checks: `webster_marguerite_b1890` vs `Webster, Miss M___Bahamas___1931`

- [PASS] surname_gate: bio 'WEBSTER' vs stint 'Webster, Miss M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M', 'M']
- [PASS] age_gate: stint starts 1931, birth 1890 (age 41)
- [FAIL] colony: no placed event resolves to 'Bahamas'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

