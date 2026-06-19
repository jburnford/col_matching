<!-- {"case_id": "case_boumphrey_robert-staveley_b1916", "bio_ids": ["boumphrey_robert-staveley_b1916"], "stint_ids": ["Boumphrey, R. S___Falkland Islands___1949"]} -->
# Dossier case_boumphrey_robert-staveley_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `boumphrey_robert-staveley_b1916`

- Printed name: **BOUMPHREY, Robert Staveley**
- Birth year: 1916 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961])
- Honours: M.B.E (1951)
- Appears in editions: [1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1956-L19924.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961]:**

> BOUMPHREY, R. S., M.B.E. (1951).—b. 1916; ed. L'pool Coll. and Pembroke Coll., Oxford; asst. audr., Nig., 1939; C.A.D., 1943; audr., Falkland Is., 1947; senr. audr., F. of Mal., 1951; S'pore, 1955; prin. audr. (later dep. dir., audit), 1958-59.

**Version `col1950-L33812.v` — printed in editions [1950, 1951]:**

> BOUMPHREY, Robert Staveley, M.B.E. (1951).—b. 1916; ed. Liverpool Coll. and Pembroke Coll., Oxford; M.A.; asst. audt., Nig., 1939; cent. off., C.A.D., 1943; audt., Falk. Is., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | asst. audr. | Nigeria | [1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1943 | C.A.D | Nigeria *(inherited from previous clause)* | [1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961] |
| 2 | 1947 | audr., Falkland Is | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |
| 3 | 1947 | audt. | Falkland Islands | [1950, 1951] |
| 4 | 1951 | senr. audr., F. of Mal | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |
| 5 | 1955 | S'pore | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |
| 6 | 1958–1959 | prin. audr. (later dep. dir., audit) | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Boumphrey, R. S___Falkland Islands___1949`

- Staff-list name: **Boumphrey, R. S** | colony: **Falkland Islands** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. S. Boumphrey | Auditor-in-Charge | AUDIT | — | — |
| 1950 | R. S. Boumphrey | Auditor-in-Charge | Audit | — | — |

### Deterministic checks: `boumphrey_robert-staveley_b1916` vs `Boumphrey, R. S___Falkland Islands___1949`

- [PASS] surname_gate: bio 'BOUMPHREY' vs stint 'Boumphrey, R. S' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1949, birth 1916 (age 33)
- [PASS] colony: 1 placed event(s) resolve to 'Falkland Islands'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 42 vs bar 60: 'audt.' ~ 'Auditor-in-Charge'
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

