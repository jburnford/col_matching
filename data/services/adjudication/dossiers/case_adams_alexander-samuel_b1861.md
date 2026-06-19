<!-- {"case_id": "case_adams_alexander-samuel_b1861", "bio_ids": ["adams_alexander-samuel_b1861"], "stint_ids": ["Adams, S___Canada___1877"]} -->
# Dossier case_adams_alexander-samuel_b1861

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 96 official(s) with this surname in the graph's staff lists; 42 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `adams_alexander-samuel_b1861`

- Printed name: **ADAMS, ALEXANDER SAMUEL**
- Birth year: 1861 (attested in editions [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933])
- Appears in editions: [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1922-L50205.v` — printed in editions [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933]:**

> ADAMS, HON. ALEXANDER SAMUEL.—B. 1861; ed., pub. schls. and Otago Univ., N.Z.; barrister and solr., 1883; crown solr., 1920; judge, N.Z. sup. obl., 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | barrister and solr | — | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933] |
| 1 | 1920 | crown solr | — | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933] |
| 2 | 1921 | judge, N.Z. sup. obl | New Zealand | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933] |

## Candidate stint `Adams, S___Canada___1877`

- Staff-list name: **Adams, S** | colony: **Canada** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | S. Adams | Private Secretary | Civil Establishment | — | — |
| 1878 | S. Adams | Private Secretary | Civil Establishment | — | — |

### Deterministic checks: `adams_alexander-samuel_b1861` vs `Adams, S___Canada___1877`

- [PASS] surname_gate: bio 'ADAMS' vs stint 'Adams, S' (exact)
- [PASS] initials: bio ['A', 'S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1877, birth 1861 (age 16)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
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

