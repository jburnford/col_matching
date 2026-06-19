<!-- {"case_id": "case_herbert_percy-frederick_b1887", "bio_ids": ["herbert_percy-frederick_b1887"], "stint_ids": ["Herbert, P. F___Barbados___1913"]} -->
# Dossier case_herbert_percy-frederick_b1887

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `herbert_percy-frederick_b1887`

- Printed name: **HERBERT, PERCY FREDERICK**
- Birth year: 1887 (attested in editions [1931, 1939, 1940])
- Appears in editions: [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1931-L65273.v` — printed in editions [1931, 1939, 1940]:**

> HERBERT, PERCY FREDERICK.—B. 1887; ed. Latymer, Liverpool Inst. High Schl. and Jesus Coll., Oxford, B.A.; supt., schls., S. Prova., Nigeria, 1915; inspr. and schl.mast., 1919; ag. asst. dir., S. Prova., 1927 and 1928; ag. dep. dir., S. Prova., 1929; ch. inspr., S. Prova., 1929; ag. asst. dir., educen., S. Prova., 1934 and 1936; asst. dir., educen., 1936.

**Version `col1932-L61069.v` — printed in editions [1932, 1933, 1934, 1935, 1936, 1937]:**

> HERBERT, PERCY FREDERICK.—B. 1887; ed. Latymer, Liverpool Inst. High Schol. and Jesus Coll., Oxford, B.A.; supt., schls., S. Prova., Nigeria, 1915; inspr. and schlmast., 1919; ag. asst. dir., S. Provs., 1927 and 1928; ag. dep. dir., S. Provs., 1929; ch. inspr., S. Provs., 1929; ag. asst. dir., educn., S. Provs., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | supt., schls. | Southern Provinces, Nigeria | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1919 | inspr. and schl.mast. | — | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1927–1928 | ag. asst. dir. | Southern Provinces | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1929 | ag. dep. dir. | Southern Provinces | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1929 | ch. inspr. | Nigeria | [1932, 1933, 1934, 1935, 1936, 1937] |
| 5 | 1934–1936 | ag. asst. dir., educen. | Southern Provinces | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 6 | 1936 | asst. dir., educen. | — | [1931, 1939, 1940] |

## Candidate stint `Herbert, P. F___Barbados___1913`

- Staff-list name: **Herbert, P. F** | colony: **Barbados** | listed 1913–1917 | editions [1913, 1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | P. F. Herbert | Assistant-Masters | Educational | — | — |
| 1915 | P. F. Herbert | Lieutenant | Barbados Volunteers | — | Lieutenant |
| 1917 | P. F. Herbert | Reserve Force, Lieutenant | Burbados Volunteers | — | Lieutenant |

### Deterministic checks: `herbert_percy-frederick_b1887` vs `Herbert, P. F___Barbados___1913`

- [PASS] surname_gate: bio 'HERBERT' vs stint 'Herbert, P. F' (exact)
- [PASS] initials: bio ['P', 'F'] ~ stint ['P', 'F']
- [PASS] age_gate: stint starts 1913, birth 1887 (age 26)
- [FAIL] colony: no placed event resolves to 'Barbados'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1917
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

