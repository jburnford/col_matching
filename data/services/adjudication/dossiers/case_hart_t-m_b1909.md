<!-- {"case_id": "case_hart_t-m_b1909", "bio_ids": ["hart_t-m_b1909"], "stint_ids": ["Hart, T. M___Singapore___1954"]} -->
# Dossier case_hart_t-m_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 64 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hart_t-m_b1909`

- Printed name: **HART, T. M**
- Birth year: 1909 (attested in editions [1953, 1954, 1955, 1956])
- Honours: C.M.G (1957)
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1953-L17624.v` — printed in editions [1953, 1954, 1955, 1956]:**

> HART, T. M.—b. 1909; ed. Strathallen Sch., Glasgow and Oxford Univs.; col. admin. serv., C.O., 1933; cl. V, M.C.S., 1936; off. of dir., co-op., 1941; 2nd asst. estab. offr., 1948; cl. II, 1949; cl. IC, 1951; cl. IB, 1952; dep. dir., commerce & industry, S'pore, 1953; staff gr. A, dir., 1953; fin. sec. and contrlr., foreign exch., 1955.

**Version `col1957-L23889.v` — printed in editions [1957, 1958, 1959, 1960]:**

> HART, T. M., C.M.G. (1957).—b. 1909; ed. Strathallan Sch., Glasgow and Oxford Univs.; col. admin. serv., 1933; secon., temp. asst. prin., C.O., 1933; M.C.S., 1936; cl. IC, 1951; cl. IB, 1952; staff gr. A, 1953; fin. sec., and contr., foreign exchange, 1955-59.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | col. admin. serv. | Colonial Office | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 1 | 1936 | cl. V, M.C.S | Colonial Office *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 2 | 1941 | off. of dir., co-op | Colonial Office *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 3 | 1948 | 2nd asst. estab. offr | Colonial Office *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 4 | 1949 | cl. II | Colonial Office *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 5 | 1951 | cl. IC | Colonial Office *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 6 | 1952 | cl. IB | Colonial Office *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 7 | 1953 | dep. dir., commerce & industry, S'pore | Colonial Office *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 8 | 1955 | fin. sec. and contrlr., foreign exch | Colonial Office *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |

## Candidate stint `Hart, T. M___Singapore___1954`

- Staff-list name: **Hart, T. M** | colony: **Singapore** | listed 1954–1959 | editions [1954, 1955, 1956, 1957, 1958, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | T. M. Hart | Director of Commerce and Industry | Civil Establishment | — | — |
| 1955 | T. M. Hart | Financial Secretary | Civil Establishment | — | — |
| 1956 | T. M. Hart | Financial Secretary and Controller of Foreign Exchange | Civil Establishment | — | — |
| 1957 | T. M. Hart | Financial Secretary and Controller of Foreign Exchange | Civil Establishment | C.M.G. | — |
| 1958 | T. M. Hart | Financial Secretary and Controller of Foreign Exchange | Civil Establishment | C.M.G. | — |
| 1959 | T. M. Hart | Financial Secretary and Controller of Foreign Exchange | Civil Establishment | C.M.G. | — |

### Deterministic checks: `hart_t-m_b1909` vs `Hart, T. M___Singapore___1954`

- [PASS] surname_gate: bio 'HART' vs stint 'Hart, T. M' (exact)
- [PASS] initials: bio ['T', 'M'] ~ stint ['T', 'M']
- [PASS] age_gate: stint starts 1954, birth 1909 (age 45)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1959
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G
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

