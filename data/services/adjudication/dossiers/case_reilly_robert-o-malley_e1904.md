<!-- {"case_id": "case_reilly_robert-o-malley_e1904", "bio_ids": ["reilly_robert-o-malley_e1904"], "stint_ids": ["Reilly, R___Bechuanaland___1905", "Reilly, R___South Africa___1912"]} -->
# Dossier case_reilly_robert-o-malley_e1904

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Reilly, R___Bechuanaland___1905` is also gate-compatible with biography(ies) outside this case: ['reilly_bernard-rawdon_b1882', 'reilly_robert-o-malley_e1904-2'] (already linked elsewhere or filtered).
- NOTE: stint `Reilly, R___South Africa___1912` is also gate-compatible with biography(ies) outside this case: ['reilly_bernard-rawdon_b1882', 'reilly_robert-o-malley_e1904-2'] (already linked elsewhere or filtered).

## Biography `reilly_robert-o-malley_e1904`

- Printed name: **REILLY, ROBERT O'MALLEY**
- Birth year: not printed
- Appears in editions: [1909, 1910]

### Verbatim printed entry text (OCR)

**Version `col1909-L49215.v` — printed in editions [1909, 1910]:**

> REILLY, ROBERT O'MALLEY.—Sub.-inspr., Bechuana land Prot. police, 1904.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904 | Sub.-inspr., Bechuana land Prot. police | Bechuana land | [1909, 1910] |

## Candidate stint `Reilly, R___Bechuanaland___1905`

- Staff-list name: **Reilly, R** | colony: **Bechuanaland** | listed 1905–1925 | editions [1905, 1906, 1907, 1909, 1911, 1917, 1921, 1922, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | R. Reilly | Sub-Inspector | Establishment | — | — |
| 1906 | R. Reilly | Sub-Inspector | Civil Establishment | — | — |
| 1907 | R. Reilly | Sub-Inspector | Establishment | — | — |
| 1909 | R. Reilly | Sub-Inspector | Establishment | — | — |
| 1911 | R. Reilly | Sub-Inspector | Establishment | — | — |
| 1917 | R. Reilly | Inspector | Establishment | — | — |
| 1921 | R. Reilly | Inspector | Establishment | — | — |
| 1922 | R. Reilly | Inspector | Establishment | — | — |
| 1924 | R. Reilly | Resident Magistrate, Lobatsi | — | — | — |
| 1925 | R. Reilly | Resident Magistrate | Civil Establishment | — | Captain |

### Deterministic checks: `reilly_robert-o-malley_e1904` vs `Reilly, R___Bechuanaland___1905`

- [PASS] surname_gate: bio 'REILLY' vs stint 'Reilly, R' (exact)
- [PASS] initials: bio ['R', 'O'] ~ stint ['R']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Bechuanaland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1925
- [FAIL] position_sim: best 36 vs bar 60: 'Sub.-inspr., Bechuana land Prot. police' ~ 'Resident Magistrate, Lobatsi'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Reilly, R___South Africa___1912`

- Staff-list name: **Reilly, R** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | R. Reilly | Sub-Inspector | Establishment | — | — |
| 1914 | R. Reilly | Sub-Inspector | Civil Establishment | — | — |
| 1918 | R. Reilly | Inspector | Establishment | — | — |

### Deterministic checks: `reilly_robert-o-malley_e1904` vs `Reilly, R___South Africa___1912`

- [PASS] surname_gate: bio 'REILLY' vs stint 'Reilly, R' (exact)
- [PASS] initials: bio ['R', 'O'] ~ stint ['R']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

