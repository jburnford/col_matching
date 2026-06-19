<!-- {"case_id": "case_bashraheel_a-m_b1926", "bio_ids": ["bashraheel_a-m_b1926"], "stint_ids": ["Bashrahil, A. M___Aden___1964"]} -->
# Dossier case_bashraheel_a-m_b1926

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bashraheel_a-m_b1926`

- Printed name: **BASHRAHEEL, A. M**
- Birth year: 1926 (attested in editions [1966])
- Honours: M.B.E (1963)
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L13145.v` — printed in editions [1966]:**

> BASHRAHEEL, A. M., M.B.E. (1963).—b. 1926; ed. St. Joseph’s High Sch., Aden; clk., Aden, 1948; asst. political offr., 1951; asst. advr., 1957; admin. offr., cl. III, 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | clk. | Aden | [1966] |
| 1 | 1951 | asst. political offr | Aden *(inherited from previous clause)* | [1966] |
| 2 | 1957 | asst. advr | Aden *(inherited from previous clause)* | [1966] |
| 3 | 1963 | admin. offr., cl. III | Aden *(inherited from previous clause)* | [1966] |

## Candidate stint `Bashrahil, A. M___Aden___1964`

- Staff-list name: **Bashrahil, A. M** | colony: **Aden** | listed 1964–1965 | editions [1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | A. M. Bashrahil | Permanent Secretaries/Deputy Permanent Secretaries | Civil Establishment | M.B.E. | — |
| 1965 | A. M. Bashrahil | Permanent Secretaries/Deputy Permanent Secretaries | Civil Establishment | — | — |

### Deterministic checks: `bashraheel_a-m_b1926` vs `Bashrahil, A. M___Aden___1964`

- [PASS] surname_gate: bio 'BASHRAHEEL' vs stint 'Bashrahil, A. M' (fuzzy:2)
- [PASS] initials: bio ['A', 'M'] ~ stint ['A', 'M']
- [PASS] age_gate: stint starts 1964, birth 1926 (age 38)
- [PASS] colony: 4 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1964-1965
- [FAIL] position_sim: best 25 vs bar 60: 'asst. advr' ~ 'Permanent Secretaries/Deputy Permanent Secretaries'
- [PASS] honour: shared: M.B.E
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

