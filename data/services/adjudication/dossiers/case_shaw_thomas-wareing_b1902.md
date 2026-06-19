<!-- {"case_id": "case_shaw_thomas-wareing_b1902", "bio_ids": ["shaw_thomas-wareing_b1902"], "stint_ids": ["Shaw, T. W___Sierra Leone___1951", "Shaw, T___Jamaica___1933"]} -->
# Dossier case_shaw_thomas-wareing_b1902

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 83 official(s) with this surname in the graph's staff lists; 29 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Shaw, T___Jamaica___1933` is also gate-compatible with biography(ies) outside this case: ['shaw_george-anthony-theodore_b1917'] (already linked elsewhere or filtered).

## Biography `shaw_thomas-wareing_b1902`

- Printed name: **SHAW, Thomas Wareing**
- Birth year: 1902 (attested in editions [1953, 1954, 1955])
- Honours: A.M.I.C.E
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1953-L18965.v` — printed in editions [1953, 1954, 1955]:**

> SHAW, T. W.—b. 1902; ed. Wigan Gram. Sch., and Wigan Mining Coll.; exec. engnr., P.W.D., Nig., 1928; senr., 1949; D.D.P.W., S.L., 1950; D.P.W., 1951.

**Version `col1951-L42428.v` — printed in editions [1951]:**

> SHAW, Thomas Wareing, B.Sc. (min.) (Lond.), A.M.I.C.E., J.P. (Nig.).—b. 1902; ed. Wigan Gram. Sch. and Wigan Mining Coll. (dip.); exec. engr., P.W.D., Nig., 1928; senr., 1949; D.D.P.W., S.L., 1950.

**Version `col1948-L35833.v` — printed in editions [1948, 1949, 1950]:**

> SHAW, Thomas Wareing, B.Sc. (min.) (Lond.), A.M.I.C.E., J.P. (Nig.).—b. 1902; ed. Wigan Gram. Sch. and Wigan Mining Coll. (dip.); apptd. col. serv., Nig., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | exec. engnr., P.W.D. | Nigeria | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 1 | 1949 | senr | Nigeria *(inherited from previous clause)* | [1951, 1953, 1954, 1955] |
| 2 | 1950 | D.D.P.W. | Sierra Leone | [1951, 1953, 1954, 1955] |
| 3 | 1951 | D.P.W | Sierra Leone *(inherited from previous clause)* | [1953, 1954, 1955] |

## Candidate stint `Shaw, T. W___Sierra Leone___1951`

- Staff-list name: **Shaw, T. W** | colony: **Sierra Leone** | listed 1951–1954 | editions [1951, 1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | T. W. Shaw | Deputy Director of Public Works | Public Works | — | — |
| 1952 | T. W. Shaw | Director of Public Works | Civil Establishment | — | — |
| 1953 | T. W. Shaw | Director of Public Works | Civil Establishment | — | — |
| 1954 | T. W. Shaw | Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `shaw_thomas-wareing_b1902` vs `Shaw, T. W___Sierra Leone___1951`

- [PASS] surname_gate: bio 'SHAW' vs stint 'Shaw, T. W' (exact)
- [PASS] initials: bio ['T', 'W'] ~ stint ['T', 'W']
- [PASS] age_gate: stint starts 1951, birth 1902 (age 49)
- [PASS] colony: 2 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1951-1954
- [FAIL] position_sim: best 23 vs bar 60: 'D.D.P.W.' ~ 'Deputy Director of Public Works'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Shaw, T___Jamaica___1933`

- Staff-list name: **Shaw, T** | colony: **Jamaica** | listed 1933–1934 | editions [1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | T. Shaw | Commander Royal Artillery | Officers (Military, etc.) | — | Major |
| 1934 | T. Shaw | Commander Royal Artillery | Officers (Military, &c.) | — | Major |

### Deterministic checks: `shaw_thomas-wareing_b1902` vs `Shaw, T___Jamaica___1933`

- [PASS] surname_gate: bio 'SHAW' vs stint 'Shaw, T' (exact)
- [PASS] initials: bio ['T', 'W'] ~ stint ['T']
- [PASS] age_gate: stint starts 1933, birth 1902 (age 31)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1934
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

