<!-- {"case_id": "case_sullivan_richard_b1906", "bio_ids": ["sullivan_richard_b1906"], "stint_ids": ["Sullivan, R. C___Jamaica___1933"]} -->
# Dossier case_sullivan_richard_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['sullivan_richard_b1906'] carry a single initial only — the namesake trap applies.

## Biography `sullivan_richard_b1906`

- Printed name: **SULLIVAN, Richard**
- Birth year: 1906 (attested in editions [1957])
- Honours: Bt
- Appears in editions: [1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L27612.v` — printed in editions [1957]:**

> SULLIVAN, Sir Richard, Bt.—b. 1906; ed. St. Andrew's Coll., Grahamstown, S.A. and Transvaal Univ. Coll.; cadet, Bech. Prot., 1928; secon., admin. offr. cl. III, Nig., 1950; admin. offr., cl. II, Nig., 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | cadet | Bechuanaland | [1957] |
| 1 | 1950 | secon., admin. offr. cl. III | Nigeria | [1957] |
| 2 | 1953 | admin. offr., cl. II | Nigeria | [1957] |

## Candidate stint `Sullivan, R. C___Jamaica___1933`

- Staff-list name: **Sullivan, R. C** | colony: **Jamaica** | listed 1933–1940 | editions [1933, 1934, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | R. C. Sullivan | Assistant Draughtsmen | Department of Public Works | — | — |
| 1934 | R. C. Sullivan | Assistant Draughtmen | Department of Public Works | — | — |
| 1937 | R. C. Sullivan | Assistant Draughtmen | Public Works | — | — |
| 1940 | R. C. Sullivan | Assistant Draughtsmen | Department of Public Works | — | — |

### Deterministic checks: `sullivan_richard_b1906` vs `Sullivan, R. C___Jamaica___1933`

- [PASS] surname_gate: bio 'SULLIVAN' vs stint 'Sullivan, R. C' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R', 'C']
- [PASS] age_gate: stint starts 1933, birth 1906 (age 27)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1940
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

