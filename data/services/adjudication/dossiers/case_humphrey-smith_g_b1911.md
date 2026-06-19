<!-- {"case_id": "case_humphrey-smith_g_b1911", "bio_ids": ["humphrey-smith_g_b1911"], "stint_ids": ["Humphrey-Smith, G___Gambia___1953"]} -->
# Dossier case_humphrey-smith_g_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['humphrey-smith_g_b1911'] carry a single initial only — the namesake trap applies.

## Biography `humphrey-smith_g_b1911`

- Printed name: **HUMPHREY-SMITH, G**
- Birth year: 1911 (attested in editions [1954, 1955, 1956, 1957])
- Honours: O.B.E (1953)
- Appears in editions: [1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1954-L20930.v` — printed in editions [1954, 1955, 1956, 1957]:**

> HUMPHREY-SMITH, G., O.B.E. (1953).—b. 1911 ; ed. Uppingham and Jesus Coll., Camb.; cadet, Uga., 1934 ; asst. dist. offr., 1936 ; polit. offr., Aden, 1939 ; Hadhramaut famine relief commr., 1944 ; secon., C.O., 1946 ; admin. offr., Gam., 1948 ; senr. comsnr., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | cadet | Uganda | [1954, 1955, 1956, 1957] |
| 1 | 1936 | asst. dist. offr | Uganda *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |
| 2 | 1939 | polit. offr. | Aden | [1954, 1955, 1956, 1957] |
| 3 | 1944 | Hadhramaut famine relief commr | Aden *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |
| 4 | 1946 | secon. | Colonial Office | [1954, 1955, 1956, 1957] |
| 5 | 1948 | admin. offr., Gam | Colonial Office *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |
| 6 | 1950 | senr. comsnr | Colonial Office *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |

## Candidate stint `Humphrey-Smith, G___Gambia___1953`

- Staff-list name: **Humphrey-Smith, G** | colony: **Gambia** | listed 1953–1956 | editions [1953, 1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | G. Humphrey-Smith | Senior Commissioner | Civil Establishment | — | — |
| 1954 | G. Humphrey-Smith | Senior Commissioner | Civil Establishment | — | — |
| 1955 | G. Humphrey-Smith | Senior Commissioner | Civil Establishment | — | — |
| 1956 | G. Humphrey-Smith | Senior Commissioner | Civil Establishment | — | — |

### Deterministic checks: `humphrey-smith_g_b1911` vs `Humphrey-Smith, G___Gambia___1953`

- [PASS] surname_gate: bio 'HUMPHREY-SMITH' vs stint 'Humphrey-Smith, G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1953, birth 1911 (age 42)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1956
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

