<!-- {"case_id": "case_arley_f-m_e1858", "bio_ids": ["arley_f-m_e1858"], "stint_ids": ["Darley, Frederick M___New South Wales___1888"]} -->
# Dossier case_arley_f-m_e1858

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `arley_f-m_e1858` ↔ `Darley, Frederick M___New South Wales___1888` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Darley, Frederick M___New South Wales___1888` is also gate-compatible with biography(ies) outside this case: ['darley_f-m_e1853'] (already linked elsewhere or filtered).

## Biography `arley_f-m_e1858`

- Printed name: **ARLEY, F. M**
- Birth year: not printed
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L31566.v` — printed in editions [1897]:**

> ARLEY, SIR F. M., KNIGHT BACH. (1887.)—Attorney, 1858; Queen's counsel, 1878; vice-president executive council, New South Wales, 1878-9; chief justice, New South Wales, 1886; lieutenant-governor, 1891.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1858 | Attorney | — | [1897] |
| 1 | 1878 | Queen's counsel | — | [1897] |
| 2 | 1878–1879 | vice-president executive council | New South Wales | [1897] |
| 3 | 1886 | chief justice | New South Wales | [1897] |
| 4 | 1891 | lieutenant-governor | New South Wales *(inherited from previous clause)* | [1897] |

## Candidate stint `Darley, Frederick M___New South Wales___1888`

- Staff-list name: **Darley, Frederick M** | colony: **New South Wales** | listed 1888–1894 | editions [1888, 1889, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | Frederick M. Darley | Chief Justice | Judicial and Legal Departments | — | — |
| 1889 | Frederick M. Darley | Chief Justice | Judicial and Legal Department | — | — |
| 1894 | Frederick M. Darley | Chief Justice | Supreme Court Bench | — | — |

### Deterministic checks: `arley_f-m_e1858` vs `Darley, Frederick M___New South Wales___1888`

- [PASS] surname_gate: bio 'ARLEY' vs stint 'Darley, Frederick M' (fuzzy:1)
- [PASS] initials: bio ['F', 'M'] ~ stint ['F', 'M']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'New South Wales'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1888-1894
- [PASS] position_sim: best 100 vs bar 60: 'chief justice' ~ 'Chief Justice'
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

