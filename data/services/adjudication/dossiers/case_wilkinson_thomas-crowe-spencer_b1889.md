<!-- {"case_id": "case_wilkinson_thomas-crowe-spencer_b1889", "bio_ids": ["wilkinson_thomas-crowe-spencer_b1889"], "stint_ids": ["Wilkinson, C___Gibraltar___1905", "Wilkinson, C___Tanganyika___1921"]} -->
# Dossier case_wilkinson_thomas-crowe-spencer_b1889

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 72 official(s) with this surname in the graph's staff lists; 34 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Wilkinson, C___Tanganyika___1921` is also gate-compatible with biography(ies) outside this case: ['wilkinson_henry-campbell_b1893', 'wilkinson_richard-clary_b1905'] (already linked elsewhere or filtered).

## Biography `wilkinson_thomas-crowe-spencer_b1889`

- Printed name: **WILKINSON, THOMAS CROWE SPENCER**
- Birth year: 1889 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L69588.v` — printed in editions [1940]:**

> WILKINSON, THOMAS CROWE SPENCER, B.A. (Oxon.), Barrister-at-Law, Lieut. R.N.—B. 1889; ed. R.N. Colls. Osborne and Dartmouth, and Balliol Coll., Oxford; on war serv., N. Sea and Baltic, 1915-19; B.A., 1922; called to bar, Gray's Inn, 1925; pres. dist. ct., Cyprus, Dec., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | B.A | — | [1940] |
| 1 | 1925 | called to bar, Gray's Inn | — | [1940] |
| 2 | 1938 | pres. dist. ct. | Cyprus | [1940] |

## Candidate stint `Wilkinson, C___Gibraltar___1905`

- Staff-list name: **Wilkinson, C** | colony: **Gibraltar** | listed 1905–1906 | editions [1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | C. Wilkinson | Official Member (Chairman) | Board of Sanitary Commissioners | — | Colonel |
| 1905 | C. Wilkinson | Commanding Royal Engineers | Chief Military and Naval Officers | — | Colonel |
| 1906 | C. Wilkinson | Chairman | Board of Sanitary Commissioners | — | Colonel |
| 1906 | C. Wilkinson | Commanding Royal Engineers | Chief Military and Naval Officers | — | Colonel |

### Deterministic checks: `wilkinson_thomas-crowe-spencer_b1889` vs `Wilkinson, C___Gibraltar___1905`

- [PASS] surname_gate: bio 'WILKINSON' vs stint 'Wilkinson, C' (exact)
- [PASS] initials: bio ['T', 'C', 'S'] ~ stint ['C']
- [PASS] age_gate: stint starts 1905, birth 1889 (age 16)
- [FAIL] colony: no placed event resolves to 'Gibraltar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1906
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Wilkinson, C___Tanganyika___1921`

- Staff-list name: **Wilkinson, C** | colony: **Tanganyika** | listed 1921–1924 | editions [1921, 1922, 1923, 1924]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | C. Wilkinson | Assistant Inspector | Police and Prisons Department | — | — |
| 1922 | C. Wilkinson | Assistant Inspector | Police and Prisons Department | — | — |
| 1923 | C. Wilkinson | Assistant Inspector | Police and Prisons Department | — | — |
| 1924 | C. Wilkinson | Assistant Inspector | Police and Prisons Department | — | — |

### Deterministic checks: `wilkinson_thomas-crowe-spencer_b1889` vs `Wilkinson, C___Tanganyika___1921`

- [PASS] surname_gate: bio 'WILKINSON' vs stint 'Wilkinson, C' (exact)
- [PASS] initials: bio ['T', 'C', 'S'] ~ stint ['C']
- [PASS] age_gate: stint starts 1921, birth 1889 (age 32)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1924
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

