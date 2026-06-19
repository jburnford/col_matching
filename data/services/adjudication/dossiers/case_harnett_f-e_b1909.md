<!-- {"case_id": "case_harnett_f-e_b1909", "bio_ids": ["harnett_f-e_b1909"], "stint_ids": ["Harnett, E___Sierra Leone___1934"]} -->
# Dossier case_harnett_f-e_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `harnett_f-e_b1909`

- Printed name: **HARNETT, F. E**
- Birth year: 1909 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L23846.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> HARNETT, F. E.—b. 1909; ed. Warehousemen, Clerks and Drapers Schs., Purley and Croydon, and Reading Univ.; mil. serv., 1940-45, maj.; sleeping sickness contl. offr., Nig., 1938; senr., 1948; prin. contl. offr., 1954; N. Nig. (Nig. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | sleeping sickness contl. offr. | Nigeria | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1948 | senr | Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1954 | prin. contl. offr | Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Harnett, E___Sierra Leone___1934`

- Staff-list name: **Harnett, E** | colony: **Sierra Leone** | listed 1934–1940 | editions [1934, 1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | E. Harnett | District Commissioner | Civil Establishment | — | — |
| 1936 | E. Harnett | District Commissioner | Civil Establishment | — | — |
| 1939 | E. Harnett | District Commissioner | Provincial Administration | — | — |
| 1940 | E. Harnett | District Commissioner | Provincial Administration | — | — |

### Deterministic checks: `harnett_f-e_b1909` vs `Harnett, E___Sierra Leone___1934`

- [PASS] surname_gate: bio 'HARNETT' vs stint 'Harnett, E' (exact)
- [PASS] initials: bio ['F', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1934, birth 1909 (age 25)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1940
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

