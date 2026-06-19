<!-- {"case_id": "case_marley_kathleen_b1906", "bio_ids": ["marley_kathleen_b1906", "marley_vernon-douglas-kenneth_b1897"], "stint_ids": ["Marley, V. D. K___Nigeria___1929"]} -->
# Dossier case_marley_kathleen_b1906

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['marley_kathleen_b1906'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Marley, V. D. K___Nigeria___1929'] have more than one claimant biography in this case.

## Biography `marley_kathleen_b1906`

- Printed name: **MARLEY, Kathleen**
- Birth year: 1906 (attested in editions [1950])
- Appears in editions: [1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1950-L37839.v` — printed in editions [1950]:**

> MARLEY, Kathleen.—b. 1906; ed. Girls' High Sch., Wakefield, Ursuline Convent, Lond., Hornsey Sch. of Art, Lond., Eliz. Garrett Anderson Hosp., Lond., and Seamen's Hosp., Greenwich; interned H.K., 1941-45; nursing sister, H.K., 1937; senr., 1947.

**Version `col1949-L34167.v` — printed in editions [1949]:**

> MARLEY, Kathleen.—b. 1906; ed. Girls' High Sch., Wakefield, Ursuline Convent, Lond. and Hornsey Sch. of Art, Lond.; nursing sister, H.K., 1937; senr., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | nursing sister | Hong Kong | [1949, 1950] |
| 1 | 1941–1945 | interned H.K | — | [1950] |
| 2 | 1947 | senr | Hong Kong *(inherited from previous clause)* | [1949, 1950] |

## Biography `marley_vernon-douglas-kenneth_b1897`

- Printed name: **MARLEY, Vernon Douglas Kenneth**
- Birth year: 1897 (attested in editions [1948, 1949, 1950])
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L34517.v` — printed in editions [1948, 1949, 1950]:**

> MARLEY, Vernon Douglas Kenneth.—b. 1897; ed. Downside Sch., near Bath, Somerset; on mil. serv. 1914-26, lieut. (regular army); asst. comsnr., police, N.P., Nig., 1927; supt., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | asst. comsnr., police, N.P. | Nigeria | [1948, 1949, 1950] |
| 1 | 1944 | supt | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950] |

## Candidate stint `Marley, V. D. K___Nigeria___1929`

- Staff-list name: **Marley, V. D. K** | colony: **Nigeria** | listed 1929–1939 | editions [1929, 1930, 1933, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | V. D. K. Marley | Commissioners and Assistant Commissioners | Marine | — | — |
| 1930 | V. D. K. Marley | Commissioners and Assistant Commissioners | Police | — | — |
| 1933 | V. D. K. Marley | Commissioner/Assistant Commissioner | Police | — | — |
| 1936 | V. D. K. Marley | Commissioners and Assistant Commissioners | Police | — | — |
| 1939 | V. D. K. Marley | Senior Assistant Superintendent | Police | — | — |

### Deterministic checks: `marley_kathleen_b1906` vs `Marley, V. D. K___Nigeria___1929`

- [PASS] surname_gate: bio 'MARLEY' vs stint 'Marley, V. D. K' (exact)
- [PASS] initials: bio ['K'] ~ stint ['V', 'D', 'K']
- [PASS] age_gate: stint starts 1929, birth 1906 (age 23)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1939
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `marley_vernon-douglas-kenneth_b1897` vs `Marley, V. D. K___Nigeria___1929`

- [PASS] surname_gate: bio 'MARLEY' vs stint 'Marley, V. D. K' (exact)
- [PASS] initials: bio ['V', 'D', 'K'] ~ stint ['V', 'D', 'K']
- [PASS] age_gate: stint starts 1929, birth 1897 (age 32)
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1939
- [FAIL] position_sim: best 46 vs bar 60: 'asst. comsnr., police, N.P.' ~ 'Senior Assistant Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

