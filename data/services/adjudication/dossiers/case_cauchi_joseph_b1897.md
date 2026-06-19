<!-- {"case_id": "case_cauchi_joseph_b1897", "bio_ids": ["cauchi_joseph_b1897"], "stint_ids": ["Cauchi, J___Nigeria___1933"]} -->
# Dossier case_cauchi_joseph_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['cauchi_joseph_b1897'] carry a single initial only — the namesake trap applies.

## Biography `cauchi_joseph_b1897`

- Printed name: **CAUCHI, JOSEPH**
- Birth year: 1897 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L63056.v` — printed in editions [1940]:**

> CAUCHI, DR. JOSEPH.—B. 1897; ed. St. Mary's Schl., Malta and King's Coll., London, M.D. (Malta), D.P.H. (London), certif. of London S.T.M.; M.O., Nigeria, 1923; M.O.H., 1925; senr. health offr., 1928; asst. dir., health serv., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | M.O. | Nigeria | [1940] |
| 1 | 1925 | M.O.H | Nigeria *(inherited from previous clause)* | [1940] |
| 2 | 1928 | senr. health offr | Nigeria *(inherited from previous clause)* | [1940] |
| 3 | 1938 | asst. dir., health serv | Nigeria *(inherited from previous clause)* | [1940] |

## Candidate stint `Cauchi, J___Nigeria___1933`

- Staff-list name: **Cauchi, J** | colony: **Nigeria** | listed 1933–1934 | editions [1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | J. Cauchi | Senior Health Officer | Medical Health Service | — | — |
| 1934 | J. Cauchi | Senior Health Officer | Medical Health Service | — | — |

### Deterministic checks: `cauchi_joseph_b1897` vs `Cauchi, J___Nigeria___1933`

- [PASS] surname_gate: bio 'CAUCHI' vs stint 'Cauchi, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1933, birth 1897 (age 36)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1933-1934
- [PASS] position_sim: best 86 vs bar 60: 'senr. health offr' ~ 'Senior Health Officer'
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

