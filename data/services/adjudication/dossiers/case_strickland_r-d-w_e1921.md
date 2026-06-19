<!-- {"case_id": "case_strickland_r-d-w_e1921", "bio_ids": ["strickland_r-d-w_e1921"], "stint_ids": ["Strickland, R___Victoria___1879"]} -->
# Dossier case_strickland_r-d-w_e1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Strickland, R___Victoria___1879` is also gate-compatible with biography(ies) outside this case: ['strickland_r-b_e1894'] (already linked elsewhere or filtered).

## Biography `strickland_r-d-w_e1921`

- Printed name: **STRICKLAND, R. D. W**
- Birth year: not printed
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1957-L27583.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962]:**

> STRICKLAND, R. D. W.—1921; ed. Blundell's Sch.; mil. serv., 1940–46; capt.; cadet, Nig., 1946; cl. III, W. Nig., 1953; cl. II, 1957; cl. I, 1959–61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | — | — | [1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1946 | cadet | Nigeria | [1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1953 | cl. III | Western Nigeria | [1957, 1958, 1959, 1960, 1961, 1962] |
| 3 | 1957 | cl. II | Western Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962] |
| 4 | 1959–1961 | cl. I | Western Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Strickland, R___Victoria___1879`

- Staff-list name: **Strickland, R** | colony: **Victoria** | listed 1879–1883 | editions [1879, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | R. Strickland | Coroner | Coroners | — | — |
| 1883 | R. Strickland | Coroner | Coroners | — | — |

### Deterministic checks: `strickland_r-d-w_e1921` vs `Strickland, R___Victoria___1879`

- [PASS] surname_gate: bio 'STRICKLAND' vs stint 'Strickland, R' (exact)
- [PASS] initials: bio ['R', 'D', 'W'] ~ stint ['R']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1883
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

