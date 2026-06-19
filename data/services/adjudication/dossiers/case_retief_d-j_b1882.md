<!-- {"case_id": "case_retief_d-j_b1882", "bio_ids": ["retief_d-j_b1882"], "stint_ids": ["Retief, D___South Africa___1912"]} -->
# Dossier case_retief_d-j_b1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `retief_d-j_b1882`

- Printed name: **RETIEF, D. J**
- Birth year: 1882 (attested in editions [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940])
- Appears in editions: [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1928-L69416.v` — printed in editions [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940]:**

> RETIEF, D. J., B.A.—B. 1882; ed. Victoria Coll., Stellenbosch; prin., Boshof, 1913; prin., Winburg, 1921; inspr. of schls., O.F.S., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | prin., Boshof | — | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 1 | 1921 | prin., Winburg | — | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 2 | 1927 | inspr. of schls. | Orange Free State | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |

## Candidate stint `Retief, D___South Africa___1912`

- Staff-list name: **Retief, D** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | D. Retief | Member | Provincial Council | — | — |
| 1914 | D. Retief | Member of Provincial Council | Provincial Council | — | — |
| 1918 | D. Retief | Member | Provincial Council | — | — |

### Deterministic checks: `retief_d-j_b1882` vs `Retief, D___South Africa___1912`

- [PASS] surname_gate: bio 'RETIEF' vs stint 'Retief, D' (exact)
- [PASS] initials: bio ['D', 'J'] ~ stint ['D']
- [PASS] age_gate: stint starts 1912, birth 1882 (age 30)
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

