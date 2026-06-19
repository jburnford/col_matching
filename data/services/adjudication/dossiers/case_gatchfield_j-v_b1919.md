<!-- {"case_id": "case_gatchfield_j-v_b1919", "bio_ids": ["gatchfield_j-v_b1919"], "stint_ids": ["Gatchfield, J. V___Windward Islands___1952"]} -->
# Dossier case_gatchfield_j-v_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gatchfield_j-v_b1919`

- Printed name: **GATCHFIELD, J. V**
- Birth year: 1919 (attested in editions [1956, 1957, 1958, 1959])
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1956-L21321.v` — printed in editions [1956, 1957, 1958, 1959]:**

> GATCHFIELD, J. V.—b. 1919; ed. City of Oxford High Sch.; mil. serv., 1939-46; C.A.D., 1946; asst. audr., Nig., 1946; audr., 1949; prin. audr., Windward Is., 1951; senr. audr., Fed. of Mal., 1954-58.

**Version `col1953-L17397.v` — printed in editions [1953, 1954, 1955]:**

> GATCHFIELD, J. V.—b. 1919; ed. City of Oxford High Sch. and Oxford Sch. of Tech. Arts and Comm.; C.A.D., 1946; asst. audr., Nig., 1946; audr., 1949; prin. audr., Windward Is., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | C.A.D | — | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |
| 1 | 1946 | asst. audr. | Nigeria | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |
| 2 | 1949 | audr | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |
| 3 | 1951 | prin. audr., Windward Is | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |
| 4 | 1954–1958 | senr. audr., Fed. of Mal | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |

## Candidate stint `Gatchfield, J. V___Windward Islands___1952`

- Staff-list name: **Gatchfield, J. V** | colony: **Windward Islands** | listed 1952–1954 | editions [1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | J. V. Gatchfield | Principal Auditor | Civil Establishment | — | — |
| 1953 | J. Gatchfield | Principal Auditor | Civil Establishment | — | — |
| 1954 | J. Gatchfield | Principal Auditor | Civil Establishment | — | — |

### Deterministic checks: `gatchfield_j-v_b1919` vs `Gatchfield, J. V___Windward Islands___1952`

- [PASS] surname_gate: bio 'GATCHFIELD' vs stint 'Gatchfield, J. V' (exact)
- [PASS] initials: bio ['J', 'V'] ~ stint ['J', 'V']
- [PASS] age_gate: stint starts 1952, birth 1919 (age 33)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1952-1954
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

