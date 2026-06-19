<!-- {"case_id": "case_oakeshott_brian-francis_b1900", "bio_ids": ["oakeshott_brian-francis_b1900"], "stint_ids": ["Oakeshott, B. F___Straits Settlements___1922"]} -->
# Dossier case_oakeshott_brian-francis_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `oakeshott_brian-francis_b1900`

- Printed name: **OAKESHOTT, BRIAN FRANCIS**
- Birth year: 1900 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L69490.v` — printed in editions [1939, 1940]:**

> OAKESHOTT, BRIAN FRANCIS.—B. 1900; ed. Berkhampsted Sch., St. George's Sch., Harpenden; pol. prob., S.S., Aug., 1919; ast. supt., July, 1923; i/c gambling suppression br., S'pore, July, 1927; C. of P., Trengganu, Sept., 1934; ag. ch. pol. offr., Negri Sembilan, Sept., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | pol. prob. | Straits Settlements | [1939, 1940] |
| 1 | 1923 | ast. supt | Straits Settlements *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1927 | i/c gambling suppression br., S'pore | Straits Settlements *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1934 | C. of P. | Trengganu | [1939, 1940] |
| 4 | 1938 | ag. ch. pol. offr., Negri Sembilan | Trengganu *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Oakeshott, B. F___Straits Settlements___1922`

- Staff-list name: **Oakeshott, B. F** | colony: **Straits Settlements** | listed 1922–1936 | editions [1922, 1923, 1925, 1931, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | B. F. Oakeshott | Probationers | Police | — | — |
| 1923 | B. F. Oakeshott | Probationer | Police | — | — |
| 1925 | B. F. Oakeshott | Assistant Superintendents | Police | — | — |
| 1931 | B. F. Oakeshott | Assistant Superintendent | Police | — | — |
| 1933 | B. F. Oakeshott | Assistant Superintendent | Police | — | — |
| 1934 | B. F. Oakeshott | Assistant Superintendents | Police | — | — |
| 1936 | B. F. Oakeshott | Assistant Superintendent | Police | — | — |

### Deterministic checks: `oakeshott_brian-francis_b1900` vs `Oakeshott, B. F___Straits Settlements___1922`

- [PASS] surname_gate: bio 'OAKESHOTT' vs stint 'Oakeshott, B. F' (exact)
- [PASS] initials: bio ['B', 'F'] ~ stint ['B', 'F']
- [PASS] age_gate: stint starts 1922, birth 1900 (age 22)
- [PASS] colony: 3 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1922-1936
- [FAIL] position_sim: best 50 vs bar 60: 'ast. supt' ~ 'Assistant Superintendent'
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

