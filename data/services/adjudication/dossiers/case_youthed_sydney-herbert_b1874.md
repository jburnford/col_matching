<!-- {"case_id": "case_youthed_sydney-herbert_b1874", "bio_ids": ["youthed_sydney-herbert_b1874"], "stint_ids": ["Youthed, S. H___Gold Coast___1909", "Youthed, S. H___Togoland___1920"]} -->
# Dossier case_youthed_sydney-herbert_b1874

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `youthed_sydney-herbert_b1874`

- Printed name: **YOUTHED, SYDNEY HERBERT**
- Birth year: 1874 (attested in editions [1921, 1922])
- Appears in editions: [1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1921-L61126.v` — printed in editions [1921, 1922]:**

> YOUTHED, SYDNEY HERBERT. — B. 1874; Sierra Leone rly. constrn., 1896; G. Coast rly. constrn., 1901; assist. loco. supt., G. Coast rlys. (open lines), Dec., 1904; loco. supt., Sept., 1908.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896 | Sierra Leone rly. constrn | Sierra Leone | [1921, 1922] |
| 1 | 1901 | G. Coast rly. constrn | Sierra Leone *(inherited from previous clause)* | [1921, 1922] |
| 2 | 1904 | assist. loco. supt., G. Coast rlys. (open lines) | Sierra Leone *(inherited from previous clause)* | [1921, 1922] |
| 3 | 1908 | loco. supt | Sierra Leone *(inherited from previous clause)* | [1921, 1922] |

## Candidate stint `Youthed, S. H___Gold Coast___1909`

- Staff-list name: **Youthed, S. H** | colony: **Gold Coast** | listed 1909–1918 | editions [1909, 1910, 1912, 1913, 1914, 1915, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | S. H. Youthed | Locomotive Superintendent | Railway Department | — | — |
| 1910 | S. H. Youthed | Locomotive Superintendent | Railway Department | — | — |
| 1912 | S. H. Youthed | Locomotive Superintendent | Railway Department | — | — |
| 1913 | S. H. Youthed | Locomotive Superintendent | Railway Department | — | — |
| 1914 | S. H. Youthed | Locomotive Superintendent | Railway Department | — | — |
| 1915 | S. H. Youthed | Locomotive Superintendent | Railway Department | — | — |
| 1918 | S. H. Youthed | Locomotive Superintendent | Railway Department | — | — |

### Deterministic checks: `youthed_sydney-herbert_b1874` vs `Youthed, S. H___Gold Coast___1909`

- [PASS] surname_gate: bio 'YOUTHED' vs stint 'Youthed, S. H' (exact)
- [PASS] initials: bio ['S', 'H'] ~ stint ['S', 'H']
- [PASS] age_gate: stint starts 1909, birth 1874 (age 35)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Youthed, S. H___Togoland___1920`

- Staff-list name: **Youthed, S. H** | colony: **Togoland** | listed 1920–1921 | editions [1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | S. H. Youthed | Locomotive Superintendent | Railway Department | — | — |
| 1921 | S. H. Youthed | Chief Mechanical Engineer | Railway Department | — | — |

### Deterministic checks: `youthed_sydney-herbert_b1874` vs `Youthed, S. H___Togoland___1920`

- [PASS] surname_gate: bio 'YOUTHED' vs stint 'Youthed, S. H' (exact)
- [PASS] initials: bio ['S', 'H'] ~ stint ['S', 'H']
- [PASS] age_gate: stint starts 1920, birth 1874 (age 46)
- [FAIL] colony: no placed event resolves to 'Togoland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1921
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

