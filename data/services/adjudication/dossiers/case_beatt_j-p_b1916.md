<!-- {"case_id": "case_beatt_j-p_b1916", "bio_ids": ["beatt_j-p_b1916"], "stint_ids": ["Beatty, J___North Borneo___1933", "Bett, J___Mauritius___1949"]} -->
# Dossier case_beatt_j-p_b1916

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Beatty, J___North Borneo___1933` is also gate-compatible with biography(ies) outside this case: ['beatty_james_b1895', 'beatty_sr-kenneth-james_b1878'] (already linked elsewhere or filtered).

## Biography `beatt_j-p_b1916`

- Printed name: **BEATT, J. P**
- Birth year: 1916 (attested in editions [1963, 1964, 1965, 1966])
- Honours: M.B.E (1946)
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L17284.v` — printed in editions [1963, 1964, 1965, 1966]:**

> BEATT, J. P., M.B.E. (1946).—b. 1916; ed. Braintree Inter. Sch.; mil. serv., 1936-47; dist. offr., Br. Somali., 1948; supt. police, Jamaica, 1949; supt. pol., Fiji, 1959; senr. supt., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | dist. offr., Br. Somali | — | [1963, 1964, 1965, 1966] |
| 1 | 1949 | supt. police | Jamaica | [1963, 1964, 1965, 1966] |
| 2 | 1959 | supt. pol. | Fiji | [1963, 1964, 1965, 1966] |
| 3 | 1960 | senr. supt | Fiji *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Beatty, J___North Borneo___1933`

- Staff-list name: **Beatty, J** | colony: **North Borneo** | listed 1933–1949 | editions [1933, 1936, 1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | J. Beatty | Permanent Way Engineer | Other Officers | — | — |
| 1933 | J. Beatty | General Manager of Railways | Staff | — | — |
| 1936 | J. Beatty | General Manager of Railways | Civil Service | — | — |
| 1936 | J. Beatty | Permanent Way Engineer | Other Officers | — | — |
| 1940 | J. Beatty | Permanent Way Engineer | Other Officers | — | — |
| 1940 | J. Beatty | General Manager of Railways | Civil Service | — | — |
| 1949 | J. Beatty | General Manager | Railways | — | — |

### Deterministic checks: `beatt_j-p_b1916` vs `Beatty, J___North Borneo___1933`

- [PASS] surname_gate: bio 'BEATT' vs stint 'Beatty, J' (fuzzy:1)
- [PASS] initials: bio ['J', 'P'] ~ stint ['J']
- [PASS] age_gate: stint starts 1933, birth 1916 (age 17)
- [FAIL] colony: no placed event resolves to 'North Borneo'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1949
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bett, J___Mauritius___1949`

- Staff-list name: **Bett, J** | colony: **Mauritius** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. Bett | Land Settlement Officer | Land Settlement | — | — |
| 1950 | J. Bett | Land Settlement Officer | Land Settlement | — | — |

### Deterministic checks: `beatt_j-p_b1916` vs `Bett, J___Mauritius___1949`

- [PASS] surname_gate: bio 'BEATT' vs stint 'Bett, J' (fuzzy:1)
- [PASS] initials: bio ['J', 'P'] ~ stint ['J']
- [PASS] age_gate: stint starts 1949, birth 1916 (age 33)
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

