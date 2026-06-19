<!-- {"case_id": "case_gilkes_humphrey-arthur_b1895", "bio_ids": ["gilkes_humphrey-arthur_b1895"], "stint_ids": ["Gilkes, H. A___Northern Rhodesia___1927"]} -->
# Dossier case_gilkes_humphrey-arthur_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gilkes_humphrey-arthur_b1895`

- Printed name: **GILKES, HUMPHREY ARTHUR**
- Birth year: 1895 (attested in editions [1937, 1940])
- Honours: D.P.H, M.A, M.C, M.D
- Appears in editions: [1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L61185.v` — printed in editions [1937, 1940]:**

> GILKES, HUMPHREY ARTHUR, M.C., M.A., M.D., B.Ch. (Oxon), D.P.H., D.T.M. and H. (Lon.).—B. 1895; med. offr., N. Rhodesia, July, 1925; ag. dir., med. and sanv. services, Oct., Dec., 1930; dep. dir., med. services, Trinidad, June, 1936; ag. D.M.S., June-Nov., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | med. offr., N. Rhodesia | — | [1937, 1940] |
| 1 | 1930 | ag. dir., med. and sanv. services, Oct | — | [1937, 1940] |
| 2 | 1936 | dep. dir., med. services | Trinidad | [1937, 1940] |
| 3 | 1937 | ag. D.M.S., June- | Trinidad *(inherited from previous clause)* | [1937, 1940] |

## Candidate stint `Gilkes, H. A___Northern Rhodesia___1927`

- Staff-list name: **Gilkes, H. A** | colony: **Northern Rhodesia** | listed 1927–1936 | editions [1927, 1928, 1929, 1930, 1931, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | H. A. Gilkes | Medical Officer | Medical | — | — |
| 1928 | H. A. Gilkes | Medical Officer | Medical | — | — |
| 1929 | H. A. Gilkes | Medical Officers | Health | — | — |
| 1930 | H. A. Gilkes | Medical Officers | Health | — | — |
| 1931 | H. A. Gilkes | Medical Officer | Health | — | — |
| 1933 | H. A. Gilkes | Medical Officers | Health | — | — |
| 1934 | H. A. Gilkes | Medical Officers | Health | — | — |
| 1936 | H. A. Gilkes | Medical and Health Officer | Medical | — | — |

### Deterministic checks: `gilkes_humphrey-arthur_b1895` vs `Gilkes, H. A___Northern Rhodesia___1927`

- [PASS] surname_gate: bio 'GILKES' vs stint 'Gilkes, H. A' (exact)
- [PASS] initials: bio ['H', 'A'] ~ stint ['H', 'A']
- [PASS] age_gate: stint starts 1927, birth 1895 (age 32)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1936
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

