<!-- {"case_id": "case_cleland_john-stockwin_e1909", "bio_ids": ["cleland_john-stockwin_e1909"], "stint_ids": ["Cleland, J. S___South Africa___1914"]} -->
# Dossier case_cleland_john-stockwin_e1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cleland_john-stockwin_e1909`

- Printed name: **CLELAND, John Stockwin**
- Birth year: not printed
- Honours: F.R.I.B.A, M.B.E, M.I.A
- Appears in editions: [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939]

### Verbatim printed entry text (OCR)

**Version `col1921-L55240.v` — printed in editions [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1936, 1939]:**

> CLELAND, John Stockwin, M.B.E., F.R.I.B.A., M.I.A.—Draughtsman, P.W.D., Transvaal, Mar., 1909; asst. archt., P.W.D., Union of S. Africa, Apr., 1912; archt., Sept., 1920; sec. for pub. wks., June, 1932.

**Version `col1933-L58674.v` — printed in editions [1933, 1934, 1935]:**

> CLELAND, JOHN STOCKWIN, M.B.E., F.R.I.B.A., M.I.A.—Draughtsman, P.W.D., Transvaal, Mar., 1909; asst. archt., P.W.D., Union of S. Africa, Apr., 1912; archt., Sept., 1920; sec. for pub. wks., June, 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | Draughtsman, P.W.D. | Transvaal | [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939] |
| 1 | 1912 | asst. archt., P.W.D., Union of S. Africa | Transvaal *(inherited from previous clause)* | [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939] |
| 2 | 1920 | archt | Transvaal *(inherited from previous clause)* | [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939] |
| 3 | 1932 | sec. for pub. wks | Transvaal *(inherited from previous clause)* | [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939] |

## Candidate stint `Cleland, J. S___South Africa___1914`

- Staff-list name: **Cleland, J. S** | colony: **South Africa** | listed 1914–1918 | editions [1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | J. S. Cleland | Assistant Architect | Public Works Department | — | — |
| 1918 | J. S. Cleland | Assistant Architect | Public Works Department | — | — |

### Deterministic checks: `cleland_john-stockwin_e1909` vs `Cleland, J. S___South Africa___1914`

- [PASS] surname_gate: bio 'CLELAND' vs stint 'Cleland, J. S' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1914; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
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

