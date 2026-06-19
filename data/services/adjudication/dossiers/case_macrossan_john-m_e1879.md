<!-- {"case_id": "case_macrossan_john-m_e1879", "bio_ids": ["macrossan_john-m_e1879", "macrossan_john-m_e1879-2"], "stint_ids": ["McCrossan, J. M___Queensland___1878"]} -->
# Dossier case_macrossan_john-m_e1879

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['McCrossan, J. M___Queensland___1878'] have more than one claimant biography in this case.

## Biography `macrossan_john-m_e1879`

- Printed name: **MACROSSAN, John M.**
- Birth year: not printed
- Appears in editions: [1883, 1888]

### Verbatim printed entry text (OCR)

**Version `col1883-L28548.v` — printed in editions [1883, 1888]:**

> MACROSSAN, John M.—Secretary for public works and mines, Queensland, 21 Jan., 1879, to 13th November, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879–1883 | Secretary for public works and mines | Queensland | [1883, 1888] |

## Biography `macrossan_john-m_e1879-2`

- Printed name: **MACROSSAN, JOHN M.**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34678.v` — printed in editions [1886]:**

> MACROSSAN, JOHN M.—Secretary for public works and mines, Queensland, 21 Jan., 1879, to 13th November, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879–1883 | Secretary for public works and mines | Queensland | [1886] |

## Candidate stint `McCrossan, J. M___Queensland___1878`

- Staff-list name: **McCrossan, J. M** | colony: **Queensland** | listed 1878–1879 | editions [1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | J. M. McCrossan | Member | Legislative Assembly | — | — |
| 1879 | J. M. McCrossan | Member of Legislative Assembly | Legislative Assembly | — | — |

### Deterministic checks: `macrossan_john-m_e1879` vs `McCrossan, J. M___Queensland___1878`

- [PASS] surname_gate: bio 'MACROSSAN' vs stint 'McCrossan, J. M' (fuzzy:1)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Queensland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1879
- [FAIL] position_sim: best 36 vs bar 60: 'Secretary for public works and mines' ~ 'Member of Legislative Assembly'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `macrossan_john-m_e1879-2` vs `McCrossan, J. M___Queensland___1878`

- [PASS] surname_gate: bio 'MACROSSAN' vs stint 'McCrossan, J. M' (fuzzy:1)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Queensland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1879
- [FAIL] position_sim: best 36 vs bar 60: 'Secretary for public works and mines' ~ 'Member of Legislative Assembly'
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

