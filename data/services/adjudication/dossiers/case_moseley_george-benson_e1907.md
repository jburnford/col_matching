<!-- {"case_id": "case_moseley_george-benson_e1907", "bio_ids": ["moseley_george-benson_e1907"], "stint_ids": ["Moseley, G. B___Bechuanaland___1909", "Moseley, G. B___South Africa___1912"]} -->
# Dossier case_moseley_george-benson_e1907

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Moseley, G. B___Bechuanaland___1909` is also gate-compatible with biography(ies) outside this case: ['moseley_george-benson_e1907-2'] (already linked elsewhere or filtered).
- NOTE: stint `Moseley, G. B___South Africa___1912` is also gate-compatible with biography(ies) outside this case: ['moseley_george-benson_e1907-2'] (already linked elsewhere or filtered).

## Biography `moseley_george-benson_e1907`

- Printed name: **MOSELEY, GEORGE BENSON**
- Birth year: not printed
- Appears in editions: [1909, 1910, 1911]

### Verbatim printed entry text (OCR)

**Version `col1909-L48625.v` — printed in editions [1909, 1910, 1911]:**

> MOSELEY, GEORGE BENSON.—Sub-inspr., Bechuana land Prot. pol., 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | Sub-inspr., Bechuana land Prot. pol | Bechuana land | [1909, 1910, 1911] |

## Candidate stint `Moseley, G. B___Bechuanaland___1909`

- Staff-list name: **Moseley, G. B** | colony: **Bechuanaland** | listed 1909–1925 | editions [1909, 1911, 1917, 1921, 1922, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | G. B. Moseley | Sub-Inspector | Establishment | — | — |
| 1911 | G. B. Moseley | Sub-Inspector | Establishment | — | — |
| 1917 | G. B. Moseley | Sub-Inspector | Establishment | — | — |
| 1921 | G. B. Moseley | Sub-Inspector | Establishment | — | — |
| 1922 | G. B. Moseley | Resident Magistrate | Establishment | — | — |
| 1925 | G. B. Moseley | Resident Magistrate | Civil Establishment | — | Captain |

### Deterministic checks: `moseley_george-benson_e1907` vs `Moseley, G. B___Bechuanaland___1909`

- [PASS] surname_gate: bio 'MOSELEY' vs stint 'Moseley, G. B' (exact)
- [PASS] initials: bio ['G', 'B'] ~ stint ['G', 'B']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Bechuanaland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1909-1925
- [FAIL] position_sim: best 37 vs bar 60: 'Sub-inspr., Bechuana land Prot. pol' ~ 'Sub-Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Moseley, G. B___South Africa___1912`

- Staff-list name: **Moseley, G. B** | colony: **South Africa** | listed 1912–1914 | editions [1912, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | G. B. Moseley | Sub-Inspector | Establishment | — | — |
| 1914 | G. B. Moseley | Sub-Inspector | Civil Establishment | — | — |

### Deterministic checks: `moseley_george-benson_e1907` vs `Moseley, G. B___South Africa___1912`

- [PASS] surname_gate: bio 'MOSELEY' vs stint 'Moseley, G. B' (exact)
- [PASS] initials: bio ['G', 'B'] ~ stint ['G', 'B']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1914
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

