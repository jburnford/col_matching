<!-- {"case_id": "case_tudhope_john_e1885", "bio_ids": ["tudhope_john_e1885", "tudhope_john_e1885-2"], "stint_ids": ["Tudhope, John___Cape of Good Hope___1888"]} -->
# Dossier case_tudhope_john_e1885

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['tudhope_john_e1885', 'tudhope_john_e1885-2'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Tudhope, John___Cape of Good Hope___1888'] have more than one claimant biography in this case.
- Phase 1 found `tudhope_john_e1885` ↔ `Tudhope, John___Cape of Good Hope___1888` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `tudhope_john_e1885-2` ↔ `Tudhope, John___Cape of Good Hope___1888` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `tudhope_john_e1885`

- Printed name: **TUDHOPE, JOHN**
- Birth year: not printed
- Appears in editions: [1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1888-L36452.v` — printed in editions [1888, 1889]:**

> TUDHOPE, JOHN.—Colonial secretary, Cape Colony, Mar., 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1885 | Colonial secretary | Cape of Good Hope | [1888, 1889] |

## Biography `tudhope_john_e1885-2`

- Printed name: **TUDHOPE, JOHN**
- Birth year: not printed
- Appears in editions: [1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1890-L37127.v` — printed in editions [1890, 1894]:**

> TUDHOPE, JOHN.—Colonial secretary, Cape Colony, Mar., 1885; resigned, 1889; member of executive council.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1885 | Colonial secretary | Cape of Good Hope | [1890, 1894] |
| 1 | 1889 | resigned | Cape of Good Hope *(inherited from previous clause)* | [1890, 1894] |

## Candidate stint `Tudhope, John___Cape of Good Hope___1888`

- Staff-list name: **Tudhope, John** | colony: **Cape of Good Hope** | listed 1888–1889 | editions [1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | John Tudhope | Member | Constituency Members | — | — |
| 1888 | John Tudhope | Colonial Secretary | Colonial Secretary's Office | — | — |
| 1889 | John Tudhope | — | Constituency | — | — |
| 1889 | John Tudhope | Colonial Secretary | Colonial Secretary's Office | — | — |

### Deterministic checks: `tudhope_john_e1885` vs `Tudhope, John___Cape of Good Hope___1888`

- [PASS] surname_gate: bio 'TUDHOPE' vs stint 'Tudhope, John' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1889
- [PASS] position_sim: best 100 vs bar 60: 'Colonial secretary' ~ 'Colonial Secretary'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1888, 1889] pos~100 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `tudhope_john_e1885-2` vs `Tudhope, John___Cape of Good Hope___1888`

- [PASS] surname_gate: bio 'TUDHOPE' vs stint 'Tudhope, John' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1888-1889
- [PASS] position_sim: best 100 vs bar 60: 'Colonial secretary' ~ 'Colonial Secretary'
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

