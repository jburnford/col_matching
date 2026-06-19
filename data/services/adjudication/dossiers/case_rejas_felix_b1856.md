<!-- {"case_id": "case_rejas_felix_b1856", "bio_ids": ["rejas_felix_b1856"], "stint_ids": ["Rojas, F___Grenada___1963", "Rojas, F___Trinidad and Tobago___1912"]} -->
# Dossier case_rejas_felix_b1856

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['rejas_felix_b1856'] carry a single initial only — the namesake trap applies.

## Biography `rejas_felix_b1856`

- Printed name: **REJAS, FELIX**
- Birth year: 1856 (attested in editions [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936])
- Appears in editions: [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1917-L52678.v` — printed in editions [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936]:**

> REJAS, FELIX.—B. 1856; entd. civ. ser., Trinidad, 15th Feb., 1887; warden, 1st July, 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1887 | entd. civ. ser. | Trinidad | [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |
| 1 | 1912 | warden | Trinidad *(inherited from previous clause)* | [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |

## Candidate stint `Rojas, F___Grenada___1963`

- Staff-list name: **Rojas, F** | colony: **Grenada** | listed 1963–1965 | editions [1963, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | F. Rojas | Public Relations Officer | Civil Establishment | — | — |
| 1964 | F. Rojas | Public Relations Officer | Civil Establishment | — | — |
| 1965 | F. Rojas | Public Relations Officer | Civil Establishment | — | — |

### Deterministic checks: `rejas_felix_b1856` vs `Rojas, F___Grenada___1963`

- [PASS] surname_gate: bio 'REJAS' vs stint 'Rojas, F' (fuzzy:1)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1963, birth 1856 (age 107)
- [FAIL] colony: no placed event resolves to 'Grenada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1965
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Rojas, F___Trinidad and Tobago___1912`

- Staff-list name: **Rojas, F** | colony: **Trinidad and Tobago** | listed 1912–1915 | editions [1912, 1913, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | F. Rojas | Clerk of the Peace | Clerks of the Peace | — | — |
| 1912 | F. Rojas | Sub-Registrar | Judicial Department | — | — |
| 1913 | F. Rojas | Clerk of the Peace | Clerks of the Peace | — | — |
| 1913 | F. Rojas | Sub-Registrar | Judicial Department | — | — |
| 1915 | F. Rojas | Sub-Registrar | Judicial Department | — | — |
| 1915 | F. Rojas | Inspector | Inspectors and Supervisors | — | — |

### Deterministic checks: `rejas_felix_b1856` vs `Rojas, F___Trinidad and Tobago___1912`

- [PASS] surname_gate: bio 'REJAS' vs stint 'Rojas, F' (fuzzy:1)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1912, birth 1856 (age 56)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1915
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

