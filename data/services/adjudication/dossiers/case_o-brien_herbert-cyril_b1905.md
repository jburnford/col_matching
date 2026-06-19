<!-- {"case_id": "case_o-brien_herbert-cyril_b1905", "bio_ids": ["o-brien_herbert-cyril_b1905"], "stint_ids": ["O'Brien, H. C___Kenya___1928"]} -->
# Dossier case_o-brien_herbert-cyril_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 66 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `o-brien_herbert-cyril_b1905`

- Printed name: **O'BRIEN, Herbert Cyril**
- Birth year: 1905 (attested in editions [1956, 1957])
- Appears in editions: [1948, 1949, 1950, 1951, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L23307.v` — printed in editions [1956, 1957]:**

> O'BRIEN, H. C.—b. 1905 ; ed. Marist Bros. Coll., Jo'burg ; examr., accts., audit dept., Ken., 1926 ; accts., 1944 ; senr. acctnt., 1950 ; asst. acctnt.-gen., 1952 ; asst. fin. sec., 1955.

**Version `col1948-L34985.v` — printed in editions [1948, 1949, 1950, 1951]:**

> O'BRIEN, Herbert Cyril.—b. 1905; ed. Marist Bros. Coll., Johannesburg, S.A.; examr. of accts., audit dept., Ken., 1926; acctnt., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | examr., accts., audit dept. | Kenya | [1948, 1949, 1950, 1951, 1956, 1957] |
| 1 | 1944 | accts | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1956, 1957] |
| 2 | 1950 | senr. acctnt | Kenya *(inherited from previous clause)* | [1956, 1957] |
| 3 | 1952 | asst. acctnt.-gen | Kenya *(inherited from previous clause)* | [1956, 1957] |
| 4 | 1955 | asst. fin. sec | Kenya *(inherited from previous clause)* | [1956, 1957] |

## Candidate stint `O'Brien, H. C___Kenya___1928`

- Staff-list name: **O'Brien, H. C** | colony: **Kenya** | listed 1928–1930 | editions [1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | H. C. O'Brien | Examiner of Accounts | Audit Department | — | — |
| 1929 | H. C. O'Brien | Examiner of Accounts | Audit Department | — | — |
| 1930 | H. C. O'Brien | Examiner of Account | Audit Department | — | — |

### Deterministic checks: `o-brien_herbert-cyril_b1905` vs `O'Brien, H. C___Kenya___1928`

- [PASS] surname_gate: bio 'O'BRIEN' vs stint 'O'Brien, H. C' (exact)
- [PASS] initials: bio ['H', 'C'] ~ stint ['H', 'C']
- [PASS] age_gate: stint starts 1928, birth 1905 (age 23)
- [PASS] colony: 5 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1928-1930
- [FAIL] position_sim: best 54 vs bar 60: 'examr., accts., audit dept.' ~ 'Examiner of Account'
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

