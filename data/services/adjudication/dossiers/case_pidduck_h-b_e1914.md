<!-- {"case_id": "case_pidduck_h-b_e1914", "bio_ids": ["pidduck_h-b_e1914"], "stint_ids": ["Pidduck, H. B___Leeward Islands___1923", "Pidduck, H. B___Leeward Islands___1933"]} -->
# Dossier case_pidduck_h-b_e1914

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pidduck_h-b_e1914`

- Printed name: **PIDDUCK, H. B**
- Birth year: not printed
- Appears in editions: [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939]

### Verbatim printed entry text (OCR)

**Version `col1931-L67381.v` — printed in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939]:**

> PIDDUCK, H. B.—Ed. Harper Adams agril. coll., Univ. of Wales; Shropshire Yeomanry, 1914-19; science mast., Dominica Grammar Schl., 1922; headmast., 1921; agr. offr., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | Shropshire Yeomanry | — | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 1 | 1921 | headmast | Dominica *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 2 | 1922 | science mast., Dominica Grammar Schl | Dominica | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 3 | 1929 | agr. offr | Dominica *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939] |

## Candidate stint `Pidduck, H. B___Leeward Islands___1923`

- Staff-list name: **Pidduck, H. B** | colony: **Leeward Islands** | listed 1923–1928 | editions [1923, 1924, 1925, 1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | H. B. Pidduck | Assistant Master | Educational Establishment | — | — |
| 1924 | H. B. Pidduck | Head Master, Dominica Grammar School | Educational Establishment | — | — |
| 1925 | H. B. Pidduck | Head Master, Dominica Grammar School | Educational Establishment | — | — |
| 1927 | H. B. Pidduck | Head Master | Educational Establishment | — | — |
| 1928 | H. B. Pidduck | Head Master, Dominica Grammar School | Educational Establishment | — | — |

### Deterministic checks: `pidduck_h-b_e1914` vs `Pidduck, H. B___Leeward Islands___1923`

- [PASS] surname_gate: bio 'PIDDUCK' vs stint 'Pidduck, H. B' (exact)
- [PASS] initials: bio ['H', 'B'] ~ stint ['H', 'B']
- [PASS] age_gate: stint starts 1923; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1928
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Pidduck, H. B___Leeward Islands___1933`

- Staff-list name: **Pidduck, H. B** | colony: **Leeward Islands** | listed 1933–1936 | editions [1933, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | H. B. Pidduck | Assistant Agricultural Officer | Agriculture | — | — |
| 1936 | H. B. Pidduck | Assistant Agricultural Officers | Agriculture | — | — |

### Deterministic checks: `pidduck_h-b_e1914` vs `Pidduck, H. B___Leeward Islands___1933`

- [PASS] surname_gate: bio 'PIDDUCK' vs stint 'Pidduck, H. B' (exact)
- [PASS] initials: bio ['H', 'B'] ~ stint ['H', 'B']
- [PASS] age_gate: stint starts 1933; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1936
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

