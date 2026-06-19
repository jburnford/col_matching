<!-- {"case_id": "case_hobbes_charles-christie-arthur_b1891", "bio_ids": ["hobbes_charles-christie-arthur_b1891"], "stint_ids": ["Hobbs, C. C. A___Hong Kong___1937"]} -->
# Dossier case_hobbes_charles-christie-arthur_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hobbes_charles-christie-arthur_b1891`

- Printed name: **HOBBES, CHARLES CHRISTIE ARTHUR**
- Birth year: 1891 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L65195.v` — printed in editions [1940]:**

> HOBBES, CAPT. CHARLES CHRISTIE ARTHUR, R.E. (R.A.R. of O.); F.R.I.B.A., A.M.I.Struct.Eng., Chtd. Architect.—B. 1891; archt., P.W.D., Hong Kong, 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | archt., P.W.D. | Hong Kong | [1940] |

## Candidate stint `Hobbs, C. C. A___Hong Kong___1937`

- Staff-list name: **Hobbs, C. C. A** | colony: **Hong Kong** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | C. C. A. Hobbs | Architect | Public Works Department | — | — |
| 1939 | C. C. A. Hobbs | Architect | Public Works Department | — | — |
| 1940 | C. C. A. Hobbs | Architects | Public Works Department | — | — |

### Deterministic checks: `hobbes_charles-christie-arthur_b1891` vs `Hobbs, C. C. A___Hong Kong___1937`

- [PASS] surname_gate: bio 'HOBBES' vs stint 'Hobbs, C. C. A' (fuzzy:1)
- [PASS] initials: bio ['C', 'C', 'A'] ~ stint ['C', 'C', 'A']
- [PASS] age_gate: stint starts 1937, birth 1891 (age 46)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 56 vs bar 60: 'archt., P.W.D.' ~ 'Architect'
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

