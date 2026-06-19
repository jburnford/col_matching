<!-- {"case_id": "case_dodd_john-hugh_b1877", "bio_ids": ["dodd_john-hugh_b1877"], "stint_ids": ["Dodd, H___Southern Nigeria___1907", "Dodd, J. H. L___Jamaica___1913"]} -->
# Dossier case_dodd_john-hugh_b1877

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Dodd, H___Southern Nigeria___1907` is also gate-compatible with biography(ies) outside this case: ['dodd_j-h_e1880'] (already linked elsewhere or filtered).
- NOTE: stint `Dodd, J. H. L___Jamaica___1913` is also gate-compatible with biography(ies) outside this case: ['dodd_j-h_e1880'] (already linked elsewhere or filtered).

## Biography `dodd_john-hugh_b1877`

- Printed name: **DODD, JOHN HUGH**
- Birth year: 1877 (attested in editions [1932, 1933])
- Honours: A.M.I.C.E
- Appears in editions: [1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1932-L59735.v` — printed in editions [1932, 1933]:**

> DODD, JOHN HUGH, A.M.I.C.E.—B. 1877; asst. engrnr., Jamaica rly., 1897; chief engrnr., 1908; chief engrnr., Gold Coast rly., Jan., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897 | asst. engrnr., Jamaica rly | Jamaica | [1932, 1933] |
| 1 | 1908 | chief engrnr | Jamaica *(inherited from previous clause)* | [1932, 1933] |
| 2 | 1923 | chief engrnr., Gold Coast rly | Gold Coast | [1932, 1933] |

## Candidate stint `Dodd, H___Southern Nigeria___1907`

- Staff-list name: **Dodd, H** | colony: **Southern Nigeria** | listed 1907–1910 | editions [1907, 1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | H. Dodd | Curators | Forestry and Botanical | — | — |
| 1909 | H. Dodd | Curator | Forestry and Botanical | — | — |
| 1910 | H. Dodd | Curator | Forestry and Agriculture | — | — |

### Deterministic checks: `dodd_john-hugh_b1877` vs `Dodd, H___Southern Nigeria___1907`

- [PASS] surname_gate: bio 'DODD' vs stint 'Dodd, H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1907, birth 1877 (age 30)
- [FAIL] colony: no placed event resolves to 'Southern Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1910
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Dodd, J. H. L___Jamaica___1913`

- Staff-list name: **Dodd, J. H. L** | colony: **Jamaica** | listed 1913–1922 | editions [1913, 1914, 1915, 1918, 1919, 1920, 1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | J. H. Dodd | Engineer of Way and Works | Railways | — | — |
| 1914 | J. H. Dodd | Engineer of Way and Works | Railways | — | — |
| 1915 | J. H. Dodd | Engineer of Way and Works | Railways | — | — |
| 1918 | J. H. Dodd | Engineer of Way and Works | Railways | — | — |
| 1919 | J. H. Dodd | Director | Railways | — | — |
| 1919 | J. H. L. Dodd | Assistant Engineer of Way and Works | Railways | — | — |
| 1920 | J. H. L. Dodd | Assistant Engineer of Way and Works | Railways | — | — |
| 1920 | J. H. Dodd | Director | Railways | — | — |
| 1921 | J. H. L. Dodd | Assistant Engineer of Way and Works | Railways | — | — |
| 1922 | J. H. Dodd | Chief Engineer | Railways | — | — |

### Deterministic checks: `dodd_john-hugh_b1877` vs `Dodd, J. H. L___Jamaica___1913`

- [PASS] surname_gate: bio 'DODD' vs stint 'Dodd, J. H. L' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H', 'L']
- [PASS] age_gate: stint starts 1913, birth 1877 (age 36)
- [PASS] colony: 2 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1913-1922
- [PASS] position_sim: best 85 vs bar 60: 'chief engrnr' ~ 'Chief Engineer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

