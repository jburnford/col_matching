<!-- {"case_id": "case_taylor_philip-patrick_b1900", "bio_ids": ["taylor_philip-patrick_b1900"], "stint_ids": ["Taylor, P. P___Palestine___1927"]} -->
# Dossier case_taylor_philip-patrick_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 245 official(s) with this surname in the graph's staff lists; 84 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `taylor_philip-patrick_b1900`

- Printed name: **TAYLOR, Philip Patrick**
- Birth year: 1900 (attested in editions [1948, 1949, 1950])
- Honours: A.M.I.C.E, M.I.W.E, O.B.E
- Appears in editions: [1939, 1940, 1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L36326.v` — printed in editions [1948, 1949, 1950]:**

> TAYLOR, Philip Patrick, O.B.E., A.M.Inst.C.E., M.I.M. & Cy.E., M.I.W.E.—b. 1900; ed. Mayfield Coll., Sussex; on mil. serv., 1940–42, lieut.; asst. engnr., P.W.D., Pal.; engnr.-in-chg. of dist., 1929; engnr.-in-chg. of Jerus. water supply (construct.), 1936–38; asst. D.P.W., Cyp., 1938; contrlr., transport, 1942 (seconded); D.P.W., 1946; dir., wks. and hydraulics, Trin., 1949; seconded as contrlr., supplies, transport and marketing, ch. exec. engnr., construct. of Jerusalem water supply.

**Version `col1939-L71091.v` — printed in editions [1939, 1940]:**

> TAYLOR, PHILIP PATRICK, A.M.I.C.E., M.I.M. & Cy.E., M.I.W.E.—B. 1900; ed. St. Catherine's Schl., Littlehampton, Xaverian Coll., Mayfield and Rutherford Coll., Newcastle; asst. engr., P.W.D., Palestine, Sept., 1926; suptg. engr., P.W.D., Cyprus, May, 1938; ag. D.P.W., June-Sept., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | asst. engr., P.W.D. | Palestine | [1939, 1940] |
| 1 | 1929 | engnr.-in-chg. of dist | — | [1948, 1949, 1950] |
| 2 | 1936–1938 | engnr.-in-chg. of Jerus. water supply (construct.) | — | [1948, 1949, 1950] |
| 3 | 1938 | asst. D.P.W. | Cyprus | [1939, 1940, 1948, 1949, 1950] |
| 4 | 1939 | ag. D.P.W., June- | Cyprus *(inherited from previous clause)* | [1939, 1940] |
| 5 | 1942 | contrlr., transport | Cyprus *(inherited from previous clause)* | [1948, 1949, 1950] |
| 6 | 1946 | D.P.W | Cyprus *(inherited from previous clause)* | [1948, 1949, 1950] |
| 7 | 1949 | dir., wks. and hydraulics | Trinidad | [1948, 1949, 1950] |

## Candidate stint `Taylor, P. P___Palestine___1927`

- Staff-list name: **Taylor, P. P** | colony: **Palestine** | listed 1927–1932 | editions [1927, 1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | P. P. Taylor | Assistant Engineer | Department of Public Works | — | — |
| 1928 | P. P. Taylor | Assistant Engineer | Public Works | — | — |
| 1929 | P. P. Taylor | Assistant Engineer | Department of Public Works | — | — |
| 1930 | P. P. Taylor | Assistant Engineer | Public Works | — | — |
| 1931 | P. P. Taylor | Assistant Engineer | Public Works | — | — |
| 1932 | P. P. Taylor | Assistant Engineer | Public Works | — | — |

### Deterministic checks: `taylor_philip-patrick_b1900` vs `Taylor, P. P___Palestine___1927`

- [PASS] surname_gate: bio 'TAYLOR' vs stint 'Taylor, P. P' (exact)
- [PASS] initials: bio ['P', 'P'] ~ stint ['P', 'P']
- [PASS] age_gate: stint starts 1927, birth 1900 (age 27)
- [PASS] colony: 1 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1932
- [FAIL] position_sim: best 58 vs bar 60: 'asst. engr., P.W.D.' ~ 'Assistant Engineer'
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

