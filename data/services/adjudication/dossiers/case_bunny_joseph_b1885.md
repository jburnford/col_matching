<!-- {"case_id": "case_bunny_joseph_b1885", "bio_ids": ["bunny_joseph_b1885"], "stint_ids": ["Bunny, J___Nigeria___1921"]} -->
# Dossier case_bunny_joseph_b1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bunny_joseph_b1885'] carry a single initial only — the namesake trap applies.

## Biography `bunny_joseph_b1885`

- Printed name: **BUNNY, JOSEPH**
- Birth year: 1885 (attested in editions [1931, 1932, 1934, 1935, 1936, 1937])
- Honours: F.L.S
- Appears in editions: [1931, 1932, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1931-L62904.v` — printed in editions [1931, 1932, 1934, 1935, 1936, 1937]:**

> BUNNY, JOSEPH, F.L.S.—B. 1885; ed. Reading Schl. and Emmanuel Coll., Cambridge; asst. conserv., forests, S. Nigeria, 1912; conserv., 1918; senr. conserv., 1922; attended Imp. forestry confere., in Australia and N.Z. as del. for Nigeria and Sierra Leone, 1928; ag. dir., forests, Nigeria in 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | asst. conserv., forests | Southern Nigeria | [1931, 1932, 1934, 1935, 1936, 1937] |
| 1 | 1918 | conserv | Southern Nigeria *(inherited from previous clause)* | [1931, 1932, 1934, 1935, 1936, 1937] |
| 2 | 1922 | senr. conserv | Southern Nigeria *(inherited from previous clause)* | [1931, 1932, 1934, 1935, 1936, 1937] |
| 3 | 1928 | attended Imp. forestry confere., in Australia and N.Z. as del. for Nigeria and Sierra Leone | Southern Nigeria *(inherited from previous clause)* | [1931, 1932, 1934, 1935, 1936, 1937] |
| 4 | 1929 | ag. dir., forests, Nigeria in | Nigeria | [1931, 1932, 1934, 1935, 1936, 1937] |

## Candidate stint `Bunny, J___Nigeria___1921`

- Staff-list name: **Bunny, J** | colony: **Nigeria** | listed 1921–1925 | editions [1921, 1922, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | J. Bunny | Conservator | Forestry | — | — |
| 1922 | J. Bunny | Senior Conservator | Forestry | — | — |
| 1925 | J. Bunny | Senior Conservator | Forestry | — | — |

### Deterministic checks: `bunny_joseph_b1885` vs `Bunny, J___Nigeria___1921`

- [PASS] surname_gate: bio 'BUNNY' vs stint 'Bunny, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1921, birth 1885 (age 36)
- [PASS] colony: 5 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1921-1925
- [PASS] position_sim: best 80 vs bar 60: 'senr. conserv' ~ 'Senior Conservator'
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

