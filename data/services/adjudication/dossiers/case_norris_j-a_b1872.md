<!-- {"case_id": "case_norris_j-a_b1872", "bio_ids": ["norris_j-a_b1872"], "stint_ids": ["Norris, J. A___Australia___1918"]} -->
# Dossier case_norris_j-a_b1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `norris_j-a_b1872`

- Printed name: **NORRIS, J. A**
- Birth year: 1872 (attested in editions [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Honours: C.M.G (1936)
- Appears in editions: [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1924-L56909.v` — printed in editions [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> NORRIS, J. A., C.M.G.(1936)—B. 1872; ed. Ballygunny and Williamstown, Ireland; acct. & treasry., Victoria, Mar., 1914; audr.-gen., Mar., 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | acct. & treasry. | Victoria | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1919 | audr.-gen | Victoria *(inherited from previous clause)* | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Norris, J. A___Australia___1918`

- Staff-list name: **Norris, J. A** | colony: **Australia** | listed 1918–1927 | editions [1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | J. A. Norris | Accountant | Treasurer | — | — |
| 1927 | J. A. Norris | Auditor-General | Public Service | — | — |

### Deterministic checks: `norris_j-a_b1872` vs `Norris, J. A___Australia___1918`

- [PASS] surname_gate: bio 'NORRIS' vs stint 'Norris, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1918, birth 1872 (age 46)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1927
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

