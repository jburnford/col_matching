<!-- {"case_id": "case_mcconnell_richard-bradford_b1903", "bio_ids": ["mcconnell_richard-bradford_b1903"], "stint_ids": ["McConnell, R. B___British Guiana___1957"]} -->
# Dossier case_mcconnell_richard-bradford_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcconnell_richard-bradford_b1903`

- Printed name: **McCONNELL, Richard Bradford**
- Birth year: 1903 (attested in editions [1955, 1956, 1957, 1958, 1960])
- Honours: A.I.M.M, C.B.E (1960), F.G.S, F.R.G.S
- Appears in editions: [1949, 1955, 1956, 1957, 1958, 1960, 1963]

### Verbatim printed entry text (OCR)

**Version `col1955-L21720.v` — printed in editions [1955, 1956, 1957, 1958, 1960]:**

> McCONNELL, R. B.—b. 1903; ed. McGill, Oxford and Lausanne Univs.; mil. serv., 1940-42, lieut.; asst. geol., Tang., 1939; geol., 1942; senr., Nig., 1948; asst. dir., geol. survey, Uga., 1950; secon., dir., Bech. Prot., 1954; dir., geol. surv., B. Guiana, 1957; author of pp. on geomorphology and pubns. on Tang., with partic. ref. to coal, lead, gold and Rift Valley structure.

**Version `col1963-L22288.v` — printed in editions [1963]:**

> McCONNELL, R. B., C.B.E. (1960).—b. 1903; ed. McGill, Oxford and Lausanne Univ.; mil. serv., 1940-42, lieut.; asst. geol., Tang., 1939; geol., 1942; senr., Nig., 1948; asst. dir., geol. survey, Uga., 1950; sec., dir., Bech. Prot., 1954; dir., geol. surv., B. Guiana, 1957-42.

**Version `col1949-L33868.v` — printed in editions [1949]:**

> McCONNELL, Richard Bradford, D.Phil. (Oxon.), D.Sci. (Lausanne), F.G.S., F.R.G.S., A.I.M.M.—b. 1903; ed. McGill, Oxford and Lausanne Univs.; on mil. serv., 1940-42; lieut.; asst. geol., T.T., 1939; geol., 1942; senr., Nig., 1948; author of papers on geomorphology and pubns. on Tang. with particular ref. to coal, lead, gold and Rift Valley structure.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | asst. geol. | Tanganyika | [1949, 1955, 1956, 1957, 1958, 1960, 1963] |
| 1 | 1942 | geol | Tanganyika *(inherited from previous clause)* | [1949, 1955, 1956, 1957, 1958, 1960, 1963] |
| 2 | 1948 | senr. | Nigeria | [1949, 1955, 1956, 1957, 1958, 1960, 1963] |
| 3 | 1950 | asst. dir., geol. survey | Uganda | [1955, 1956, 1957, 1958, 1960, 1963] |
| 4 | 1954 | secon., dir. | Bechuanaland | [1955, 1956, 1957, 1958, 1960, 1963] |
| 5 | 1957 | dir., geol. surv., B. Guiana | Bechuanaland *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1960, 1963] |

## Candidate stint `McConnell, R. B___British Guiana___1957`

- Staff-list name: **McConnell, R. B** | colony: **British Guiana** | listed 1957–1962 | editions [1957, 1958, 1959, 1960, 1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | R. B. McConnell | Director, Geological Surveys | Civil Establishment | — | — |
| 1958 | R. B. McConnell | Director, Geological Surveys | Civil Establishment | — | — |
| 1959 | R. B. McConnell | Director, Geological Surveys | British Guiana | — | — |
| 1960 | R. B. McConnell | Director, Geological Surveys | Civil Establishment | — | — |
| 1961 | R. B. McConnell | Director, Geological Surveys | Civil Establishment | — | — |
| 1962 | R. B. McConnell | Director of Geological Survey | Civil Establishment | — | — |

### Deterministic checks: `mcconnell_richard-bradford_b1903` vs `McConnell, R. B___British Guiana___1957`

- [PASS] surname_gate: bio 'McCONNELL' vs stint 'McConnell, R. B' (exact)
- [PASS] initials: bio ['R', 'B'] ~ stint ['R', 'B']
- [PASS] age_gate: stint starts 1957, birth 1903 (age 54)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1962
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

