<!-- {"case_id": "case_machan_john-william_b1890", "bio_ids": ["machan_john-william_b1890"], "stint_ids": ["Machan, J. W___Straits Settlements___1925"]} -->
# Dossier case_machan_john-william_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `machan_john-william_b1890`

- Printed name: **MACHAN, JOHN WILLIAM**
- Birth year: 1890 (attested in editions [1934, 1935, 1936, 1937, 1939])
- Appears in editions: [1934, 1935, 1936, 1937, 1939]

### Verbatim printed entry text (OCR)

**Version `col1934-L61354.v` — printed in editions [1934, 1935, 1936, 1937, 1939]:**

> MACHAN, JOHN WILLIAM.—B. 1890; ed. Marconi Wireless Schl., Lond.; Marconi Internat. Marine Communication Co., Lond., Sept., 1914; Aug., 1914; operator, S'pore, Aug., 1915; astt. engrnr.-opertr., S'pore, May, 1920 and Aug., 1921; supt., P. and T., S.S. and F.M.S., Mar., 1923; engrnr.-opertr., Penang, Oct., 1929 and Mar., 1932; engrnr., wireless, P. Lebar, S'pore, July, 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | Marconi Internat. Marine Communication Co., Lond | — | [1934, 1935, 1936, 1937, 1939] |
| 1 | 1915 | operator, S'pore | — | [1934, 1935, 1936, 1937, 1939] |
| 2 | 1920 | astt. engrnr.-opertr., S'pore | — | [1934, 1935, 1936, 1937, 1939] |
| 3 | 1921 | astt. engrnr.-opertr., S'pore | — | [1934, 1935, 1936, 1937, 1939] |
| 4 | 1923 | supt., P. and T., S.S. and F.M.S | Straits Settlements | [1934, 1935, 1936, 1937, 1939] |
| 5 | 1929 | engrnr.-opertr., Penang | Straits Settlements *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939] |
| 6 | 1932 | engrnr.-opertr., Penang | Straits Settlements *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939] |

## Candidate stint `Machan, J. W___Straits Settlements___1925`

- Staff-list name: **Machan, J. W** | colony: **Straits Settlements** | listed 1925–1933 | editions [1925, 1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | J. W. Machan | Assistant Engineer Operator | Post Office | — | — |
| 1931 | J. W. Machan | Engineer Operators, Wireless Stations | Post Office | — | — |
| 1933 | J. W. Machan | Engineer, Wireless | Post Office | — | — |

### Deterministic checks: `machan_john-william_b1890` vs `Machan, J. W___Straits Settlements___1925`

- [PASS] surname_gate: bio 'MACHAN' vs stint 'Machan, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1925, birth 1890 (age 35)
- [PASS] colony: 3 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1925-1933
- [FAIL] position_sim: best 51 vs bar 60: 'engrnr.-opertr., Penang' ~ 'Engineer Operators, Wireless Stations'
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

