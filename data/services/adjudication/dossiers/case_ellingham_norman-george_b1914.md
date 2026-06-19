<!-- {"case_id": "case_ellingham_norman-george_b1914", "bio_ids": ["ellingham_norman-george_b1914"], "stint_ids": ["Ellingham, N. G___Swaziland___1965"]} -->
# Dossier case_ellingham_norman-george_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ellingham_norman-george_b1914`

- Printed name: **ELLINGHAM, Norman George**
- Birth year: 1914 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Honours: O.B.E (1963)
- Appears in editions: [1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1957-L22790.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> ELLINGHAM, N. G., O.B.E. (1963).—b. 1914; mil. serv., 1939-46, lt.-col.; Br. P.O., 1930-49; asst. contr., E.A. posts and tels. dept., 1949; postal contr., 1953; contr., postal servs., 1960-62.

**Version `col1950-L35238.v` — printed in editions [1950, 1951]:**

> ELLINGHAM, Norman George.—b. 1914; ed. St. Mary's C. of E. Sch. Bletchley, Penny Stratford Coun. Sch., Bletchley, and Adans Sec. Sch., Leighton Buzzard; on mil. serv., 1939-46, lieut.-col.; Br. P.O., 1930; asst. contrlr., posts and tels. dept., Ken., Uga. and T.T., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930–1949 | Br. P.O | — | [1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1949 | asst. contr., E.A. posts and tels. dept | Uganda | [1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1953 | postal contr | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1960–1962 | contr., postal servs | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Ellingham, N. G___Swaziland___1965`

- Staff-list name: **Ellingham, N. G** | colony: **Swaziland** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | N. G. Ellingham | Controller of Posts and Telegraphs | Law Officers | — | — |
| 1966 | N. G. Ellingham | Controller of Posts and Telegraphs | Civil Establishment | — | — |

### Deterministic checks: `ellingham_norman-george_b1914` vs `Ellingham, N. G___Swaziland___1965`

- [PASS] surname_gate: bio 'ELLINGHAM' vs stint 'Ellingham, N. G' (exact)
- [PASS] initials: bio ['N', 'G'] ~ stint ['N', 'G']
- [PASS] age_gate: stint starts 1965, birth 1914 (age 51)
- [FAIL] colony: no placed event resolves to 'Swaziland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1965-1966
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

