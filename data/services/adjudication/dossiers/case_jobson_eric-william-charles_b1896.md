<!-- {"case_id": "case_jobson_eric-william-charles_b1896", "bio_ids": ["jobson_eric-william-charles_b1896"], "stint_ids": ["Hobson, E___Australia___1913"]} -->
# Dossier case_jobson_eric-william-charles_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hobson, E___Australia___1913` is also gate-compatible with biography(ies) outside this case: ['hobson_arthur-bertrand-late-r-e_b1893'] (already linked elsewhere or filtered).

## Biography `jobson_eric-william-charles_b1896`

- Printed name: **JOBSON, ERIC WILLIAM CHARLES**
- Birth year: 1896 (attested in editions [1940])
- Honours: M.B
- Appears in editions: [1940, 1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1940-L65636.v` — printed in editions [1940]:**

> JOBSON, ERIC WILLIAM CHARLES, M.B., Ch.B., Certif. Lond. Schl., Hyg. and Trop. Med.—B. 1896; mily. serv., 1917-19; med. offr., Kenya, 1924; senr. med. offr., Tanganyika Territory, 1939.

**Version `col1948-L33659.v` — printed in editions [1948, 1949, 1950, 1951]:**

> JOBSON, Eric William Charles, M.B., Ch.B.—b. 1896; cert., L.S.H.T.M.; on mil. serv., 1917-19; med. offr., Ken., 1924; S.M.O., T.T., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917–1919 | mily. serv | — | [1940] |
| 1 | 1924 | med. offr. | Kenya | [1940, 1948, 1949, 1950, 1951] |
| 2 | 1939 | senr. med. offr., Tanganyika Territory | Tanganyika | [1940] |
| 3 | 1939 | S.M.O., T.T | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Hobson, E___Australia___1913`

- Staff-list name: **Hobson, E** | colony: **Australia** | listed 1913–1927 | editions [1913, 1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | E. Hobson | Clerk | Department of Trade and Customs | — | — |
| 1918 | E. Hobson | Clerk | Department of Trade and Customs | — | — |
| 1927 | E. Hobson | Clerk | Department of Trade and Customs | — | — |

### Deterministic checks: `jobson_eric-william-charles_b1896` vs `Hobson, E___Australia___1913`

- [PASS] surname_gate: bio 'JOBSON' vs stint 'Hobson, E' (fuzzy:1)
- [PASS] initials: bio ['E', 'W', 'C'] ~ stint ['E']
- [PASS] age_gate: stint starts 1913, birth 1896 (age 17)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1927
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

