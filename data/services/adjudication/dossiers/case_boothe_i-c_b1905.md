<!-- {"case_id": "case_boothe_i-c_b1905", "bio_ids": ["boothe_i-c_b1905"], "stint_ids": ["Booth, I. C___Singapore___1954"]} -->
# Dossier case_boothe_i-c_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `boothe_i-c_b1905`

- Printed name: **BOOTHE, I. C**
- Birth year: 1905 (attested in editions [1955, 1956])
- Appears in editions: [1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1955-L19818.v` — printed in editions [1955, 1956]:**

> BOOTHE, I. C.—b. 1905; ed. Fort St. High Sch., Sydney; mil. serv., 1941–45; survr., F.M.S., revenue surv. bch., 1928; topog. bch., 1930; asst. supt., trig. and topog. bch., Brunei, 1934; senr. survr., S'pore, 1941; dep. ch. survr., 1947; ch. survr. II., 1948; ch. survr. I., S'pore, 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | survr., F.M.S., revenue surv. bch | — | [1955, 1956] |
| 1 | 1930 | topog. bch | — | [1955, 1956] |
| 2 | 1934 | asst. supt., trig. and topog. bch. | Brunei | [1955, 1956] |
| 3 | 1941 | senr. survr., S'pore | Brunei *(inherited from previous clause)* | [1955, 1956] |
| 4 | 1947 | dep. ch. survr | Brunei *(inherited from previous clause)* | [1955, 1956] |
| 5 | 1948 | ch. survr. II | Brunei *(inherited from previous clause)* | [1955, 1956] |
| 6 | 1952 | ch. survr. I., S'pore | Brunei *(inherited from previous clause)* | [1955, 1956] |

## Candidate stint `Booth, I. C___Singapore___1954`

- Staff-list name: **Booth, I. C** | colony: **Singapore** | listed 1954–1956 | editions [1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | I. C. Booth | Chief Surveyor | Civil Establishment | — | — |
| 1955 | I. C. Booth | Chief Surveyor | Civil Establishment | — | — |
| 1956 | I. C. Booth | Chief Surveyor | Civil Establishment | — | — |

### Deterministic checks: `boothe_i-c_b1905` vs `Booth, I. C___Singapore___1954`

- [PASS] surname_gate: bio 'BOOTHE' vs stint 'Booth, I. C' (fuzzy:1)
- [PASS] initials: bio ['I', 'C'] ~ stint ['I', 'C']
- [PASS] age_gate: stint starts 1954, birth 1905 (age 49)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1956
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

