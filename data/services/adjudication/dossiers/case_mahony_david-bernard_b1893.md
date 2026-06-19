<!-- {"case_id": "case_mahony_david-bernard_b1893", "bio_ids": ["mahony_david-bernard_b1893"], "stint_ids": ["Mahony, D. B___Tanganyika___1922"]} -->
# Dossier case_mahony_david-bernard_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mahony_david-bernard_b1893`

- Printed name: **MAHONY, DAVID BERNARD**
- Birth year: 1893 (attested in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933])
- Honours: M.R.C.V.S
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1927-L61133.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933]:**

> MAHONY, DAVID BERNARD, M.R.C.V.S.—B. 1893; ed., Blackrock Coll. and R. Vety. Coll., Dublin; vety. offr., Tanganyika Territory, Feb., 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | vety. offr., Tanganyika Territory | Tanganyika | [1927, 1928, 1929, 1930, 1931, 1932, 1933] |

## Candidate stint `Mahony, D. B___Tanganyika___1922`

- Staff-list name: **Mahony, D. B** | colony: **Tanganyika** | listed 1922–1933 | editions [1922, 1923, 1924, 1925, 1930, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | D. B. Mahony | Veterinary Officer | Veterinary Department | — | — |
| 1923 | D. B. Mahony | Veterinary Officer | Veterinary Department | — | — |
| 1924 | D. B. Mahony | Veterinary Officers | Veterinary Department | — | — |
| 1925 | D. B. Mahony | Veterinary Officer | Veterinary Department | — | — |
| 1930 | D. B. Mahony | Veterinary Officer | Veterinary | — | — |
| 1933 | D. B. Mahony | Senior Veterinary Officers | Veterinary | — | — |

### Deterministic checks: `mahony_david-bernard_b1893` vs `Mahony, D. B___Tanganyika___1922`

- [PASS] surname_gate: bio 'MAHONY' vs stint 'Mahony, D. B' (exact)
- [PASS] initials: bio ['D', 'B'] ~ stint ['D', 'B']
- [PASS] age_gate: stint starts 1922, birth 1893 (age 29)
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1933
- [FAIL] position_sim: best 50 vs bar 60: 'vety. offr., Tanganyika Territory' ~ 'Senior Veterinary Officers'
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

