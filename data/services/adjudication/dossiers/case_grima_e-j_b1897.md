<!-- {"case_id": "case_grima_e-j_b1897", "bio_ids": ["grima_e-j_b1897"], "stint_ids": ["Grima, E___Malta___1953", "Grima, J___Malta___1936"]} -->
# Dossier case_grima_e-j_b1897

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `grima_e-j_b1897`

- Printed name: **GRIMA, E. J**
- Birth year: 1897 (attested in editions [1956, 1957])
- Appears in editions: [1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L21567.v` — printed in editions [1956, 1957]:**

> GRIMA, E. J.—b. 1897; ed. Lyceum and Royal Univ. of Malta; dep. dir., communal feeding, Malta, 1942; mag., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1942 | dep. dir., communal feeding | Malta | [1956, 1957] |
| 1 | 1946 | mag | Malta *(inherited from previous clause)* | [1956, 1957] |

## Candidate stint `Grima, E___Malta___1953`

- Staff-list name: **Grima, E** | colony: **Malta** | listed 1953–1955 | editions [1953, 1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | E. Grima | Magistrate | The Maltese Government | — | — |
| 1954 | E. Grima | Magistrate | The Maltese Government | — | — |
| 1955 | E. Grima | Magistrates | THE MALTESE GOVERNMENT | — | — |

### Deterministic checks: `grima_e-j_b1897` vs `Grima, E___Malta___1953`

- [PASS] surname_gate: bio 'GRIMA' vs stint 'Grima, E' (exact)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E']
- [PASS] age_gate: stint starts 1953, birth 1897 (age 56)
- [PASS] colony: 2 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1953-1955
- [FAIL] position_sim: best 46 vs bar 60: 'mag' ~ 'Magistrate'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Grima, J___Malta___1936`

- Staff-list name: **Grima, J** | colony: **Malta** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | J. Grima | Masters | Education Department | — | — |
| 1937 | J. Grima | Masters | Lyceum | — | — |
| 1939 | J. Grima | Masters | Lyceum | — | — |
| 1940 | J. Grima | Masters | Lyceum. | — | — |

### Deterministic checks: `grima_e-j_b1897` vs `Grima, J___Malta___1936`

- [PASS] surname_gate: bio 'GRIMA' vs stint 'Grima, J' (exact)
- [PASS] initials: bio ['E', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1936, birth 1897 (age 39)
- [PASS] colony: 2 placed event(s) resolve to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

