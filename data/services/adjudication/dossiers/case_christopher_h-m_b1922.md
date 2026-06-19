<!-- {"case_id": "case_christopher_h-m_b1922", "bio_ids": ["christopher_h-m_b1922"], "stint_ids": ["Christopher, H. M___Windward Islands___1954"]} -->
# Dossier case_christopher_h-m_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `christopher_h-m_b1922`

- Printed name: **CHRISTOPHER, H. M**
- Birth year: 1922 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1957-L21921.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> CHRISTOPHER, H. M.—b. 1922; ed. Grenada Boys' Sec. Sch.; mil. serv., 1943-47; senr. clk., admin's. off., Grenada, 1948; asst. sec. (admin.), Wind. Is., 1952; admin. asst., W. Indies, 1958; asst. sec., 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | senr. clk., admin's. off. | Grenada | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1952 | asst. sec. (admin.), Wind. Is | Grenada *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1958 | admin. asst., W. Indies | Grenada *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Christopher, H. M___Windward Islands___1954`

- Staff-list name: **Christopher, H. M** | colony: **Windward Islands** | listed 1954–1957 | editions [1954, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | H. M. Christopher | Assistant Secretary (Administrative) (Windward Islands) | Civil Establishment | — | — |
| 1955 | H. M. Christopher | Assistant Secretary (Administrative) (Windward Islands) | Civil Establishment | — | — |
| 1956 | H. M. Christopher | Assistant Secretary (Administrative) (Windward Islands) | Civil Establishment | — | — |
| 1957 | H. M. Christopher | Assistant Secretary (Administrative) (Windward Islands) | Civil Establishment | — | — |

### Deterministic checks: `christopher_h-m_b1922` vs `Christopher, H. M___Windward Islands___1954`

- [PASS] surname_gate: bio 'CHRISTOPHER' vs stint 'Christopher, H. M' (exact)
- [PASS] initials: bio ['H', 'M'] ~ stint ['H', 'M']
- [PASS] age_gate: stint starts 1954, birth 1922 (age 32)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1957
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

