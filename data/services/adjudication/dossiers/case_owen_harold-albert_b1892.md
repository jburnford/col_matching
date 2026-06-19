<!-- {"case_id": "case_owen_harold-albert_b1892", "bio_ids": ["owen_harold-albert_b1892"], "stint_ids": ["Owen, H. A___Leeward Islands___1917"]} -->
# Dossier case_owen_harold-albert_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 58 official(s) with this surname in the graph's staff lists; 26 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `owen_harold-albert_b1892`

- Printed name: **OWEN, HAROLD ALBERT**
- Birth year: 1892 (attested in editions [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937])
- Appears in editions: [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1918-L53234.v` — printed in editions [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]:**

> OWEN, HAROLD ALBERT.—B. 1892; entd. crown agt.'s office, Dec., 1911; seconded as 3rd clk., col. sec.'s office, Antigua, July, 1916; sec. to comanr. of enquiry into condition of St. John's fire brigade, Nov., 1916; returned to crown agt.'s office, Sept., 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | entd. crown agt.'s office | — | [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 1 | 1916 | seconded as 3rd clk., col. sec.'s office | Antigua | [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 2 | 1919 | returned to crown agt.'s office | Antigua *(inherited from previous clause)* | [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Owen, H. A___Leeward Islands___1917`

- Staff-list name: **Owen, H. A** | colony: **Leeward Islands** | listed 1917–1919 | editions [1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | H. A. Owen | 3rd Clerk | Secretariat | — | — |
| 1917 | H. A. Owen | Clerk | Civil Establishment | — | — |
| 1918 | H. A. Owen | Clerk | Civil Establishment | — | — |
| 1918 | H. A. Owen | 3rd Clerk | Secretariat | — | — |
| 1919 | H. A. Owen | Clerk | Civil Establishment | — | — |
| 1919 | H. A. Owen | 3rd Clerk | Secretariat | — | — |

### Deterministic checks: `owen_harold-albert_b1892` vs `Owen, H. A___Leeward Islands___1917`

- [PASS] surname_gate: bio 'OWEN' vs stint 'Owen, H. A' (exact)
- [PASS] initials: bio ['H', 'A'] ~ stint ['H', 'A']
- [PASS] age_gate: stint starts 1917, birth 1892 (age 25)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1919
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

