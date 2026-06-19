<!-- {"case_id": "case_elliot_james-robert-mcdowell_b1896", "bio_ids": ["elliot_james-robert-mcdowell_b1896"], "stint_ids": ["Elliot, J. R. McD___Uganda___1923"]} -->
# Dossier case_elliot_james-robert-mcdowell_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `elliot_james-robert-mcdowell_b1896`

- Printed name: **ELLIOT, James Robert McDowell**
- Birth year: 1896 (attested in editions [1948, 1949])
- Honours: O.B.E.
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L32419.v` — printed in editions [1948, 1949]:**

> ELLIOT, James Robert McDowell, O.B.E.—b. 1896; ed. Lancing Coll.; on mil. serv. 1914-19, maj.; cadet, Uga., 1920; A.D.C., 1922; dist. offr., 1931; senr. dist. offr., 1944; prov. comsnr., W. Prov., 1945; compiled lab. enq. reports, 1936 and 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | maj. | — | [1948, 1949] |
| 1 | 1920 | cadet | Uganda | [1948, 1949] |
| 2 | 1922 | A.D.C. | — | [1948, 1949] |
| 3 | 1931 | dist. offr. | — | [1948, 1949] |
| 4 | 1936–1937 | — | — | [1948, 1949] |
| 5 | 1944 | senr. dist. offr. | — | [1948, 1949] |
| 6 | 1945 | prov. comsnr. | Western Province | [1948, 1949] |

## Candidate stint `Elliot, J. R. McD___Uganda___1923`

- Staff-list name: **Elliot, J. R. McD** | colony: **Uganda** | listed 1923–1937 | editions [1923, 1925, 1928, 1930, 1933, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | J. R. McD. Elliot | 2nd Grade Administrative Officer | Administration | — | — |
| 1925 | J. R. McD. Elliot | 2nd Grade Administrative Officer | Civil Establishment | — | — |
| 1928 | J. R. McD. Elliot | Administrative Officer | Provincial Administration | — | — |
| 1930 | J. R. McD. Elliot | District Officer | District Officers and Assistant District Officers | — | — |
| 1933 | J. R. McD. Elliot | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1936 | J. R. McD. Elliot | District Officer | Provincial Administration | — | — |
| 1937 | J. R. McD. Elliot | District Officers and Assistant District Officers | Provincial Administration | — | — |

### Deterministic checks: `elliot_james-robert-mcdowell_b1896` vs `Elliot, J. R. McD___Uganda___1923`

- [PASS] surname_gate: bio 'ELLIOT' vs stint 'Elliot, J. R. McD' (exact)
- [PASS] initials: bio ['J', 'R', 'M'] ~ stint ['J', 'R', 'M']
- [PASS] age_gate: stint starts 1923, birth 1896 (age 27)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1923-1937
- [FAIL] position_sim: best 22 vs bar 60: 'cadet' ~ 'Administrative Officer'
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

