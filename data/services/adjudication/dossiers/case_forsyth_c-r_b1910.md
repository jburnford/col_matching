<!-- {"case_id": "case_forsyth_c-r_b1910", "bio_ids": ["forsyth_c-r_b1910"], "stint_ids": ["Forsyth, C. R___Singapore___1951"]} -->
# Dossier case_forsyth_c-r_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `forsyth_c-r_b1910`

- Printed name: **FORSYTH, C. R**
- Birth year: 1910 (attested in editions [1953, 1954, 1955, 1956, 1957])
- Appears in editions: [1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1953-L17344.v` — printed in editions [1953, 1954, 1955, 1956, 1957]:**

> FORSYTH, C. R.—b. 1910; ed. Ballarat High Sch., Melbourne, and Oxford Univ.; mil. serv., 1942-45, lieut. (p.o.w.); cadet, C.A.S., Mal., 1936; asst. imm. comsnr. for Mal., Negapatam, S. India, 1937; cl. V, 1939; cl. IV, 1943; cl. III, 1947; p.a.s. S'pore, 1950; Imp. Def. Coll., 1951; cl. IC, 1951; cl. IB, 1952; ag. sec. for def. and internal security, S'pore, 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | cadet, C.A.S. | Malaya | [1953, 1954, 1955, 1956, 1957] |
| 1 | 1937 | asst. imm. comsnr. for Mal., Negapatam, S. India | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 2 | 1939 | cl. V | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 3 | 1943 | cl. IV | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 4 | 1947 | cl. III | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 5 | 1950 | p.a.s. S'pore | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 6 | 1951 | Imp. Def. Coll | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 7 | 1952 | cl. IB | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |

## Candidate stint `Forsyth, C. R___Singapore___1951`

- Staff-list name: **Forsyth, C. R** | colony: **Singapore** | listed 1951–1954 | editions [1951, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | C. R. Forsyth | Principal Assistant Secretary | Administration | — | — |
| 1953 | C. R. Forsyth | Secretary for Defence and Internal Security | Civil Establishment | — | — |
| 1954 | C. R. Forsyth | Secretary for Defence and Internal Security | Civil Establishment | — | — |

### Deterministic checks: `forsyth_c-r_b1910` vs `Forsyth, C. R___Singapore___1951`

- [PASS] surname_gate: bio 'FORSYTH' vs stint 'Forsyth, C. R' (exact)
- [PASS] initials: bio ['C', 'R'] ~ stint ['C', 'R']
- [PASS] age_gate: stint starts 1951, birth 1910 (age 41)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1951-1954
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

