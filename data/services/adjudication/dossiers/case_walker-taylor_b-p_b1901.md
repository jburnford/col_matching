<!-- {"case_id": "case_walker-taylor_b-p_b1901", "bio_ids": ["walker-taylor_b-p_b1901"], "stint_ids": ["Walker-Taylor, B. P___Singapore___1957"]} -->
# Dossier case_walker-taylor_b-p_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `walker-taylor_b-p_b1901`

- Printed name: **WALKER-TAYLOR, B. P**
- Birth year: 1901 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1957-L28117.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> WALKER-TAYLOR, B. P.—b. 1901; ed. Sydney Gram. Sch.; mil. serv., 1942–45; survr.-on-agreement, Johore, 1926; asst. supt., surv., S'pore, 1932; dist. survr., Mal., 1934; food contrlr. in addn., 1941–42; emergency duties, C.I.D., 1949; secon., Mal. rlyws., 1949–50; chief survr., II, 1951; chief survr. I, 1954; S'pore, 1956–60.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | survr.-on-agreement | Johore | [1957, 1958, 1959, 1960, 1961] |
| 1 | 1932 | asst. supt., surv., S'pore | Johore *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 2 | 1934 | dist. survr. | Malaya | [1957, 1958, 1959, 1960, 1961] |
| 3 | 1941–1942 | food contrlr. in addn | Malaya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 4 | 1949 | emergency duties, C.I.D | Malaya | [1957, 1958, 1959, 1960, 1961] |
| 5 | 1951 | chief survr., II | Malaya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 6 | 1954 | chief survr. I | Malaya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 7 | 1956–1960 | S'pore | Malaya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Walker-Taylor, B. P___Singapore___1957`

- Staff-list name: **Walker-Taylor, B. P** | colony: **Singapore** | listed 1957–1959 | editions [1957, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | B. P. Walker-Taylor | Chief Surveyor | Civil Establishment | — | — |
| 1959 | B. P. Walker-Taylor | Chief Surveyor | Civil Establishment | — | — |

### Deterministic checks: `walker-taylor_b-p_b1901` vs `Walker-Taylor, B. P___Singapore___1957`

- [PASS] surname_gate: bio 'WALKER-TAYLOR' vs stint 'Walker-Taylor, B. P' (exact)
- [PASS] initials: bio ['B', 'P'] ~ stint ['B', 'P']
- [PASS] age_gate: stint starts 1957, birth 1901 (age 56)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1959
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

