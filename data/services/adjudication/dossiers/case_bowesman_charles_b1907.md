<!-- {"case_id": "case_bowesman_charles_b1907", "bio_ids": ["bowesman_charles_b1907"], "stint_ids": ["Bowesman, C. W___Gambia___1936"]} -->
# Dossier case_bowesman_charles_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bowesman_charles_b1907'] carry a single initial only — the namesake trap applies.

## Biography `bowesman_charles_b1907`

- Printed name: **BOWESMAN, Charles**
- Birth year: 1907 (attested in editions [1948, 1949, 1950, 1951])
- Honours: B.A, M.D
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31311.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BOWESMAN, Charles, B.A., M.D., F.R.C.S. (Edin.), D.T.M. & H.—b. 1907; ed. Trinity Coll., Dublin and Edinburgh Univs.; med. offr., Gamb., 1935; G.C., 1941; surg. speclst., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | med. offr., Gamb | — | [1948, 1949, 1950, 1951] |
| 1 | 1941 | med. offr., Gamb | Gold Coast | [1948, 1949, 1950, 1951] |
| 2 | 1945 | surg. speclst | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Bowesman, C. W___Gambia___1936`

- Staff-list name: **Bowesman, C. W** | colony: **Gambia** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | C. W. Bowesman | Medical Officer | Medical | — | — |
| 1937 | C. W. Bowesman | Medical Officer | Medical | — | — |
| 1939 | C. W. Bowesman | Medical Officer | Medical | — | — |
| 1940 | C. W. Bowesman | Medical Officer | Medical | — | — |

### Deterministic checks: `bowesman_charles_b1907` vs `Bowesman, C. W___Gambia___1936`

- [PASS] surname_gate: bio 'BOWESMAN' vs stint 'Bowesman, C. W' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C', 'W']
- [PASS] age_gate: stint starts 1936, birth 1907 (age 29)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

