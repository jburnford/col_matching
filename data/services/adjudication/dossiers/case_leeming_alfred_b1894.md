<!-- {"case_id": "case_leeming_alfred_b1894", "bio_ids": ["leeming_alfred_b1894"], "stint_ids": ["Leeming, R. A___British Guiana___1953"]} -->
# Dossier case_leeming_alfred_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['leeming_alfred_b1894'] carry a single initial only — the namesake trap applies.

## Biography `leeming_alfred_b1894`

- Printed name: **LEEMING, Alfred**
- Birth year: 1894 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L33990.v` — printed in editions [1948, 1949]:**

> LEEMING, Alfred.—b. 1894; ed. Jesus Coll., Oxford; on mil. serv., 1914-23, capt.; cadet, Nig., 1924; senr. dist. offr., 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | cadet | Nigeria | [1948, 1949] |
| 1 | 1943 | senr. dist. offr | Nigeria *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Leeming, R. A___British Guiana___1953`

- Staff-list name: **Leeming, R. A** | colony: **British Guiana** | listed 1953–1957 | editions [1953, 1954, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | R. A. Leeming | Deputy Director (Drainage, Irrigation and Sea Defences) | Civil Establishment | — | — |
| 1954 | R. A. Leeming | Deputy Director (Drainage, Irrigation and Sea Defences) | Civil Establishment | — | — |
| 1955 | R. A. Leeming | Director of Drainage and Irrigation | Civil Establishment | — | — |
| 1956 | R. A. Leeming | Director of Drainage and Irrigation | Civil Establishment | — | — |
| 1957 | R. A. Leeming | Director of Drainage and Irrigation | Civil Establishment | — | — |

### Deterministic checks: `leeming_alfred_b1894` vs `Leeming, R. A___British Guiana___1953`

- [PASS] surname_gate: bio 'LEEMING' vs stint 'Leeming, R. A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['R', 'A']
- [PASS] age_gate: stint starts 1953, birth 1894 (age 59)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1957
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

