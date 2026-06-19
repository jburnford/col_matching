<!-- {"case_id": "case_andrew-blamey_w-h-j_b1918", "bio_ids": ["andrew-blamey_w-h-j_b1918"], "stint_ids": ["Andrew-Blamey, W. H. J___St Helena___1949"]} -->
# Dossier case_andrew-blamey_w-h-j_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `andrew-blamey_w-h-j_b1918`

- Printed name: **ANDREW-BLAMEY, W. H. J**
- Birth year: 1918 (attested in editions [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1954-L19330.v` — printed in editions [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> ANDREW-BLAMEY, W. H. J.—b. 1918; ed. Probus Sch., Truro; mil. serv., 1939–46; col. audit serv., Nig., 1946; St. H., 1948; Ken., 1952; col. treas. and collr., cust., St. H., 1952; Uga., 1955–62. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | col. audit serv. | Nigeria | [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1948 | St. H | Nigeria *(inherited from previous clause)* | [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1952 | St. H | Kenya | [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1955–1962 | col. treas. and collr., cust., St. H | Uganda | [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Andrew-Blamey, W. H. J___St Helena___1949`

- Staff-list name: **Andrew-Blamey, W. H. J** | colony: **St Helena** | listed 1949–1955 | editions [1949, 1950, 1951, 1953, 1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. H. J. Andrew-Blamey | Aide de Camp (Honorary) | Governor and Personal Staff | — | — |
| 1949 | W. H. J. Andrew-Blamey | Auditor | Audit | — | — |
| 1950 | W. H. J. Andrew-Blamey | Aide de Camp (Honorary) | GOVERNOR AND PERSONAL STAFF | — | — |
| 1950 | W. H. J. Andrew-Blamey | Auditor | Audit | — | — |
| 1951 | W. H. J. Andrew-Blamey | Aide de Camp (Honorary) | GOVERNOR AND PERSONAL STAFF | — | — |
| 1951 | W. H. J. Andrew-Blamey | Auditor | AUDIT | — | — |
| 1953 | W. H. J. Andrew-Blamey | Colonial Treasurer and Collector of Customs | Civil Establishment | — | — |
| 1954 | W. H. J. Andrew-Blamey | Colonial Treasurer and Collector of Customs | Civil Establishment | — | — |
| 1955 | W. H. J. Andrew-Blamey | Colonial Treasurer and Collector of Customs | Civil Establishment | — | — |

### Deterministic checks: `andrew-blamey_w-h-j_b1918` vs `Andrew-Blamey, W. H. J___St Helena___1949`

- [PASS] surname_gate: bio 'ANDREW-BLAMEY' vs stint 'Andrew-Blamey, W. H. J' (exact)
- [PASS] initials: bio ['W', 'H', 'J'] ~ stint ['W', 'H', 'J']
- [PASS] age_gate: stint starts 1949, birth 1918 (age 31)
- [FAIL] colony: no placed event resolves to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1955
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

