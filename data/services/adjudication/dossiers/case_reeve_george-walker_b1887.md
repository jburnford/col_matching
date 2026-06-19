<!-- {"case_id": "case_reeve_george-walker_b1887", "bio_ids": ["reeve_george-walker_b1887"], "stint_ids": ["Reeve, G. W___Hong Kong___1923", "Reeve, G. W___Hong Kong___1936"]} -->
# Dossier case_reeve_george-walker_b1887

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `reeve_george-walker_b1887`

- Printed name: **REEVE, GEORGE WALKER**
- Birth year: 1887 (attested in editions [1934, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1934-L62508.v` — printed in editions [1934, 1935, 1936, 1937, 1939, 1940]:**

> REEVE, GEORGE WALKER, B.A. hons. (Alta., Canada).—B. 1887; on mil. serv., 1914-19; admstr. branch, A.I.P., Air Mny., 1918-22; asst. mast., educn. dept., Hong Kong, Mar., 1922; lectr., Hong Kong Univ., 1925-33; 2nd mast., Queen's Coll., 1931 and 1933; headmnr., Wansai schl., 1934; do., Kadodio schl., 1936; do., Yaumati schl., 1938; senr. mast., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | on mil. serv. | — | [1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1918–1922 | admstr. branch, A.I.P., Air Mny. | — | [1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1922–1922 | asst. mast., educn. dept. | Hong Kong | [1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1925–1933 | lectr. | Hong Kong | [1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1931–1933 | 2nd mast. | — | [1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1934–1934 | headmnr. | — | [1934, 1935, 1936, 1937, 1939, 1940] |
| 6 | 1936–1936 | headmnr. | — | [1934, 1935, 1936, 1937, 1939, 1940] |
| 7 | 1938–1938 | headmnr. | — | [1934, 1935, 1936, 1937, 1939, 1940] |
| 8 | 1939–1939 | senr. mast. | — | [1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Reeve, G. W___Hong Kong___1923`

- Staff-list name: **Reeve, G. W** | colony: **Hong Kong** | listed 1923–1925 | editions [1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | G. W. Reeve | Assistants | Queen's College | — | — |
| 1924 | G. W. Reeve | Assistant | Queen's College | — | — |
| 1925 | G. W. Reeve | Assistant Master, Kowloon British School | Director of Education | — | — |

### Deterministic checks: `reeve_george-walker_b1887` vs `Reeve, G. W___Hong Kong___1923`

- [PASS] surname_gate: bio 'REEVE' vs stint 'Reeve, G. W' (exact)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G', 'W']
- [PASS] age_gate: stint starts 1923, birth 1887 (age 36)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1923-1925
- [FAIL] position_sim: best 44 vs bar 60: 'asst. mast., educn. dept.' ~ 'Assistant Master, Kowloon British School'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Reeve, G. W___Hong Kong___1936`

- Staff-list name: **Reeve, G. W** | colony: **Hong Kong** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | G. W. Reeve | Head Master, Wanchai School | Evening Institute Director | — | — |
| 1937 | G. W. Reeve | Head Master, Ellis Kadoorie School | Director of Education | — | — |
| 1939 | G. W. Reeve | Head Master, Wanchai School | Department of Director of Education | — | — |
| 1940 | G. W. Reeve | Head Master, Yaumati School | Department of Director of Education | — | — |

### Deterministic checks: `reeve_george-walker_b1887` vs `Reeve, G. W___Hong Kong___1936`

- [PASS] surname_gate: bio 'REEVE' vs stint 'Reeve, G. W' (exact)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G', 'W']
- [PASS] age_gate: stint starts 1936, birth 1887 (age 49)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

