<!-- {"case_id": "case_muller_jan-frederik_b1891", "bio_ids": ["muller_jan-frederik_b1891"], "stint_ids": ["Muller, J___Gold Coast___1910", "Muller, John Frederick___South Africa___1912"]} -->
# Dossier case_muller_jan-frederik_b1891

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `muller_jan-frederik_b1891`

- Printed name: **MULLER, JAN FREDERIK**
- Birth year: 1891 (attested in editions [1936, 1937, 1939, 1940])
- Appears in editions: [1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L63234.v` — printed in editions [1936, 1937, 1939, 1940]:**

> MULLER, JAN FREDERIK.—B. 1891; 3rd grade olk., dept. of agr., Union of S. Africa, 1909; 2nd grade olk., 1919; 1st grade clk., 1921; senr. clk., 1926; prin. clk., dept. of mines, 1928; 2nd grade ch. olk., do., 1932; 1st grade ch. olk., do., 1934; under sec., do., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | 3rd grade olk., dept. of agr., Union of S. Africa | — | [1936, 1937, 1939, 1940] |
| 1 | 1919 | 2nd grade olk | — | [1936, 1937, 1939, 1940] |
| 2 | 1921 | 1st grade clk | — | [1936, 1937, 1939, 1940] |
| 3 | 1926 | senr. clk | — | [1936, 1937, 1939, 1940] |
| 4 | 1928 | prin. clk., dept. of mines | — | [1936, 1937, 1939, 1940] |
| 5 | 1932 | 2nd grade ch. olk. | Dominions Office | [1936, 1937, 1939, 1940] |
| 6 | 1934 | 1st grade ch. olk. | Dominions Office | [1936, 1937, 1939, 1940] |

## Candidate stint `Muller, J___Gold Coast___1910`

- Staff-list name: **Muller, J** | colony: **Gold Coast** | listed 1910–1913 | editions [1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | J. Muller | Principal Teacher | Education Department | — | — |
| 1911 | J. Muller | Principal Teacher | Education Department | — | — |
| 1912 | J. Muller | Principal Teacher | Education Department | — | — |
| 1913 | J. Muller | Principal Teacher | Education Department | — | — |

### Deterministic checks: `muller_jan-frederik_b1891` vs `Muller, J___Gold Coast___1910`

- [PASS] surname_gate: bio 'MULLER' vs stint 'Muller, J' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J']
- [PASS] age_gate: stint starts 1910, birth 1891 (age 19)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1910-1913
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Muller, John Frederick___South Africa___1912`

- Staff-list name: **Muller, John Frederick** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | John Frederick Muller | Elected Member | Natal Provincial Council | — | — |
| 1914 | John Frederick Muller | Elected Member | Natal Provincial Council | — | — |
| 1918 | John Frederick Muller | Elected Member | Natal Provincial Council | — | — |
| 1918 | J. Muller | Government Analyst | Analyses | — | — |

### Deterministic checks: `muller_jan-frederik_b1891` vs `Muller, John Frederick___South Africa___1912`

- [PASS] surname_gate: bio 'MULLER' vs stint 'Muller, John Frederick' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1912, birth 1891 (age 21)
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

