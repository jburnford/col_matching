<!-- {"case_id": "case_goude_g-f_b1908", "bio_ids": ["goude_g-f_b1908"], "stint_ids": ["Goude, F___Uganda___1927"]} -->
# Dossier case_goude_g-f_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `goude_g-f_b1908`

- Printed name: **GOUDE, G. F**
- Birth year: 1908 (attested in editions [1957])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L23485.v` — printed in editions [1957]:**

> GOUDE, G. F.—b. 1908; ed. Lyceum and Royal Univ. of Malta, Rome Univ. and Instituto di Medicina Legate, Rome; mag., Malta, 1948.

**Version `col1958-L23001.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> GOUDER, G. F.—b. 1908; ed. Lyceum and Royal Univ. of Malta, Rome Univ. and Instituto di Medicina Legate, Rome; mag., Malta, 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | mag. | Malta | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Goude, F___Uganda___1927`

- Staff-list name: **Goude, F** | colony: **Uganda** | listed 1927–1928 | editions [1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | F. Goude | Mechanic | Transport | — | — |
| 1928 | F. Goude | Mechanic | Transport | — | — |

### Deterministic checks: `goude_g-f_b1908` vs `Goude, F___Uganda___1927`

- [PASS] surname_gate: bio 'GOUDE' vs stint 'Goude, F' (exact)
- [PASS] initials: bio ['G', 'F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1927, birth 1908 (age 19)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1928
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

