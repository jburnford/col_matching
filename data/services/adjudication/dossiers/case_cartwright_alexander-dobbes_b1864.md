<!-- {"case_id": "case_cartwright_alexander-dobbes_b1864", "bio_ids": ["cartwright_alexander-dobbes_b1864"], "stint_ids": ["Cartwright, A. D___Canada___1912"]} -->
# Dossier case_cartwright_alexander-dobbes_b1864

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cartwright_alexander-dobbes_b1864`

- Printed name: **CARTWRIGHT, ALEXANDER DOBBES**
- Birth year: 1864 (attested in editions [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932])
- Honours: B.A.
- Appears in editions: [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1921-L55090.v` — printed in editions [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]:**

> CARTWRIGHT, ALEXANDER DOBBES, B.A.—B. 1864; ed. Queen's Univ., Kingston; barrister, 1888; prac. profession in Toronto until 1904, when apptd. sec. to the bd. of rly. comsrs., for Canada, Feb., 1904.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1888 | barrister | — | [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 1 | 1904 | sec. to the bd. of rly. comsrs. | Canada | [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 2 | ?–1904 | prac. profession | Toronto | [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |

## Candidate stint `Cartwright, A. D___Canada___1912`

- Staff-list name: **Cartwright, A. D** | colony: **Canada** | listed 1912–1922 | editions [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | A. D. Cartwright | Secretary | Permanent Railway Commission | — | — |
| 1913 | A. D. Cartwright | Secretary | Permanent Railway Commission | — | — |
| 1914 | A. D. Cartwright | Secretary | Permanent Railway Commission | — | — |
| 1915 | A. D. Cartwright | Secretary | Permanent Railway Commission | — | — |
| 1917 | A. D. Cartwright | Secretary | Permanent Railway Commission | — | — |
| 1918 | A. D. Cartwright | Secretary | Permanent Railway Commission | — | — |
| 1919 | A. D. Cartwright | Secretary | Permanent Railway Commission | — | — |
| 1920 | A. D. Cartwright | Secretary | Permanent Railway Commission | — | — |
| 1922 | A. D. Cartwright | Secretary | Railway Commission | — | — |

### Deterministic checks: `cartwright_alexander-dobbes_b1864` vs `Cartwright, A. D___Canada___1912`

- [PASS] surname_gate: bio 'CARTWRIGHT' vs stint 'Cartwright, A. D' (exact)
- [PASS] initials: bio ['A', 'D'] ~ stint ['A', 'D']
- [PASS] age_gate: stint starts 1912, birth 1864 (age 48)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1912-1922
- [FAIL] position_sim: best 28 vs bar 60: 'sec. to the bd. of rly. comsrs.' ~ 'Secretary'
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

