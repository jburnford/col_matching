<!-- {"case_id": "case_teelock_b_b1922", "bio_ids": ["teelock_b_b1922"], "stint_ids": ["Teelock, B___Mauritius___1963"]} -->
# Dossier case_teelock_b_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['teelock_b_b1922'] carry a single initial only — the namesake trap applies.

## Biography `teelock_b_b1922`

- Printed name: **TEELOCK, B**
- Birth year: 1922 (attested in editions [1964, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L22342.v` — printed in editions [1964, 1966]:**

> TEELOCK, B.—b. 1922; ed. Royal Coll., Maur. and Edinburgh Univ.; sch. med. offr., Maur., 1952; S.M.O., 1958; P.M.O., 1963.

**Version `col1965-L19625.v` — printed in editions [1965]:**

> TEEOCK, B.—b. 1922; ed. Royal Coll., Maur. and Edinburgh Univ.; sch. med. offr., Maur., 1952; S.M.O., 1958; P.M.O., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1952 | sch. med. offr. | Mauritius | [1964, 1965, 1966] |
| 1 | 1958 | S.M.O | Mauritius *(inherited from previous clause)* | [1964, 1965, 1966] |
| 2 | 1963 | P.M.O | Mauritius *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Teelock, B___Mauritius___1963`

- Staff-list name: **Teelock, B** | colony: **Mauritius** | listed 1963–1966 | editions [1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | B. Teelock | Principal Medical Officer | Civil Establishment | — | — |
| 1964 | B. Teelock | Principal Medical Officer | Civil Establishment | — | — |
| 1965 | B. Teelock | Principal Medical Officer | Civil Establishment | — | — |
| 1966 | B. Teelock | Principal Medical Officer | Civil Establishment | — | — |

### Deterministic checks: `teelock_b_b1922` vs `Teelock, B___Mauritius___1963`

- [PASS] surname_gate: bio 'TEELOCK' vs stint 'Teelock, B' (exact)
- [PASS] initials: bio ['B'] ~ stint ['B']
- [PASS] age_gate: stint starts 1963, birth 1922 (age 41)
- [PASS] colony: 3 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1963-1966
- [FAIL] position_sim: best 14 vs bar 60: 'S.M.O' ~ 'Principal Medical Officer'
- [FAIL] honour: no shared honour
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

