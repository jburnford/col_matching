<!-- {"case_id": "case_root_d_b1921", "bio_ids": ["root_d_b1921"], "stint_ids": ["Root, D___Uganda___1949"]} -->
# Dossier case_root_d_b1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['root_d_b1921'] carry a single initial only — the namesake trap applies.

## Biography `root_d_b1921`

- Printed name: **ROOT, D**
- Birth year: 1921 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1957-L26841.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> ROOT, D.—b. 1921; ed. elementary and secondary schs.; mil. serv., 1939-44; asst. supt., prisons, Uga., 1944; senr. asst. supt., 1953; supt., prisons, 1954; senr. supt., 1958-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | asst. supt., prisons | Uganda | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1953 | senr. asst. supt | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1954 | supt., prisons | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1958–1962 | senr. supt | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Root, D___Uganda___1949`

- Staff-list name: **Root, D** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. Root | Assistant Superintendents | Prisons | — | — |
| 1951 | D. Root | Assistant Superintendents | Prisons | — | — |

### Deterministic checks: `root_d_b1921` vs `Root, D___Uganda___1949`

- [PASS] surname_gate: bio 'ROOT' vs stint 'Root, D' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1949, birth 1921 (age 28)
- [PASS] colony: 4 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 52 vs bar 60: 'asst. supt., prisons' ~ 'Assistant Superintendents'
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

