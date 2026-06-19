<!-- {"case_id": "case_vaughan_j-h-h_b1920", "bio_ids": ["vaughan_j-h-h_b1920"], "stint_ids": ["Vaughan, J. H___Fiji___1946"]} -->
# Dossier case_vaughan_j-h-h_b1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 45 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Vaughan, J. H___Fiji___1946` is also gate-compatible with biography(ies) outside this case: ['vaughan_john-henry_b1892'] (already linked elsewhere or filtered).

## Biography `vaughan_j-h-h_b1920`

- Printed name: **VAUGHAN, J. H. H**
- Birth year: 1920 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L22667.v` — printed in editions [1964, 1965, 1966]:**

> VAUGHAN, J. H. H.—b. 1920; ed. Highbury County Sch.; mil. serv., 1940-46, R.A.F.; cler. offr., C.O., 1937; higher cler./exec. offr., 1947; higher exec. offr., 1951; secon. D.W.W.I., 1952-58; senr. exec. offr., 1960; ch. exec. offr., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | cler. offr. | Colonial Office | [1964, 1965, 1966] |
| 1 | 1947 | higher cler./exec. offr | Colonial Office *(inherited from previous clause)* | [1964, 1965, 1966] |
| 2 | 1951 | higher exec. offr | Colonial Office *(inherited from previous clause)* | [1964, 1965, 1966] |
| 3 | 1952–1958 | secon. D.W.W.I | Colonial Office *(inherited from previous clause)* | [1964, 1965, 1966] |
| 4 | 1960 | senr. exec. offr | Colonial Office *(inherited from previous clause)* | [1964, 1965, 1966] |
| 5 | 1963 | ch. exec. offr | Colonial Office *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Vaughan, J. H___Fiji___1946`

- Staff-list name: **Vaughan, J. H** | colony: **Fiji** | listed 1946–1952 | editions [1946, 1950, 1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1946 | J. H. Vaughan | Attorney-General | Legislative Council | — | — |
| 1950 | J. H. Vaughan | Chief Justice | JUDICIAL | — | — |
| 1951 | J. H. Vaughan | Chief Justice | JUDICIAL | — | — |
| 1952 | J. H. Vaughan | Chief Justice | Civil Establishment | — | — |

### Deterministic checks: `vaughan_j-h-h_b1920` vs `Vaughan, J. H___Fiji___1946`

- [PASS] surname_gate: bio 'VAUGHAN' vs stint 'Vaughan, J. H' (exact)
- [PASS] initials: bio ['J', 'H', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1946, birth 1920 (age 26)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1946-1952
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

