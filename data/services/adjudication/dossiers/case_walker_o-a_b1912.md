<!-- {"case_id": "case_walker_o-a_b1912", "bio_ids": ["walker_o-a_b1912"], "stint_ids": ["Walker, O. A___Dominica___1963"]} -->
# Dossier case_walker_o-a_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 124 official(s) with this surname in the graph's staff lists; 70 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `walker_o-a_b1912`

- Printed name: **WALKER, O. A**
- Birth year: 1912 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L28109.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> WALKER, O. A.—b. 1912; ed. Rawle Inst. and Inst. of Educ. London Univ.; headmr., primary sch., St. L., 1938; asst. inspir., schs., 1948; inspir., 1949; educ. offr., Dominica, 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | headmr., primary sch. | St. Lucia | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1948 | asst. inspir., schs | St. Lucia *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1949 | inspir | St. Lucia *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Walker, O. A___Dominica___1963`

- Staff-list name: **Walker, O. A** | colony: **Dominica** | listed 1963–1966 | editions [1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | O. A. Walker | Education Officer | Civil Establishment | — | — |
| 1964 | O. A. Walker | Education Officer | Civil Establishment | — | — |
| 1965 | O. A. Walker | Education Officer | Civil Establishment | — | — |
| 1966 | O. A. Walker | Education Officer | Civil Establishment | — | — |

### Deterministic checks: `walker_o-a_b1912` vs `Walker, O. A___Dominica___1963`

- [PASS] surname_gate: bio 'WALKER' vs stint 'Walker, O. A' (exact)
- [PASS] initials: bio ['O', 'A'] ~ stint ['O', 'A']
- [PASS] age_gate: stint starts 1963, birth 1912 (age 51)
- [FAIL] colony: no placed event resolves to 'Dominica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1966
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

