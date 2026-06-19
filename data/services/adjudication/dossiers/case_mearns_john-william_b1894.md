<!-- {"case_id": "case_mearns_john-william_b1894", "bio_ids": ["mearns_john-william_b1894"], "stint_ids": ["Mearns, J. W___British Guiana___1923"]} -->
# Dossier case_mearns_john-william_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mearns_john-william_b1894`

- Printed name: **MEARNS, JOHN WILLIAM**
- Birth year: 1894 (attested in editions [1934, 1935, 1936, 1937])
- Honours: A.M.I.C.E
- Appears in editions: [1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1934-L61609.v` — printed in editions [1934, 1935, 1936, 1937]:**

> MEARNS, JOHN WILLIAM, B.Sc. (Engnr.), Glasgow, A.M.I.Struct.E., A.M.I.C.E.—B.1894; asst. engnr., sea defences, Br. Guiana, 1920; do., pub. wks. dept., 1922; dist. engnr., 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | asst. engnr., sea defences | British Guiana | [1934, 1935, 1936, 1937] |
| 1 | 1922 | do., pub. wks. dept | British Guiana *(inherited from previous clause)* | [1934, 1935, 1936, 1937] |
| 2 | 1925 | dist. engnr | British Guiana *(inherited from previous clause)* | [1934, 1935, 1936, 1937] |

## Candidate stint `Mearns, J. W___British Guiana___1923`

- Staff-list name: **Mearns, J. W** | colony: **British Guiana** | listed 1923–1930 | editions [1923, 1924, 1925, 1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | J. W. Mearns | Assistant Engineer | Public Works | — | — |
| 1924 | J. W. Mearns | Assistant Engineer | Public Works | — | — |
| 1925 | J. W. Mearns | Assistant Engineer | Public Works | — | — |
| 1927 | J. W. Mearns | District Engineer (West Coast) | Public Works | — | — |
| 1928 | J. W. Mearns | District Engineer (West Coast) | Public Works | — | — |
| 1929 | J. W. Mearns | District Engineer (West Coast) | Public Works | — | — |
| 1930 | J. W. Mearns | District Engineer (West Coast) | Public Works | — | — |

### Deterministic checks: `mearns_john-william_b1894` vs `Mearns, J. W___British Guiana___1923`

- [PASS] surname_gate: bio 'MEARNS' vs stint 'Mearns, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1923, birth 1894 (age 29)
- [PASS] colony: 3 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1923-1930
- [PASS] position_sim: best 64 vs bar 60: 'dist. engnr' ~ 'Assistant Engineer'
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

