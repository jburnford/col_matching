<!-- {"case_id": "case_arnold_r-h_b1928", "bio_ids": ["arnold_r-h_b1928"], "stint_ids": ["Arnold, R. H___Gambia___1959"]} -->
# Dossier case_arnold_r-h_b1928

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `arnold_r-h_b1928`

- Printed name: **ARNOLD, R. H**
- Birth year: 1928 (attested in editions [1959, 1960, 1961, 1962])
- Appears in editions: [1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1959-L20263.v` — printed in editions [1959, 1960, 1961, 1962]:**

> ARNOLD, R. H.—b. 1928; ed. Queen Elizabeth's Gram. Sch., Atherstone; D.D.P.W., Gambia, 1958-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1958–1961 | D.D.P.W. | Gambia | [1959, 1960, 1961, 1962] |

## Candidate stint `Arnold, R. H___Gambia___1959`

- Staff-list name: **Arnold, R. H** | colony: **Gambia** | listed 1959–1961 | editions [1959, 1960, 1961]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | R. H. Arnold | Deputy Director of Public Works | Civil Establishment | — | — |
| 1960 | R. H. Arnold | Deputy Director of Public Works | Civil Establishment | — | — |
| 1961 | R. H. Arnold | Deputy Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `arnold_r-h_b1928` vs `Arnold, R. H___Gambia___1959`

- [PASS] surname_gate: bio 'ARNOLD' vs stint 'Arnold, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1959, birth 1928 (age 31)
- [PASS] colony: 1 placed event(s) resolve to 'Gambia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1959-1961
- [FAIL] position_sim: best 23 vs bar 60: 'D.D.P.W.' ~ 'Deputy Director of Public Works'
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

