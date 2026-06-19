<!-- {"case_id": "case_crawford_henry-john-pringle_b1914", "bio_ids": ["crawford_henry-john-pringle_b1914"], "stint_ids": ["Crawford, J. P___Northern Rhodesia___1949"]} -->
# Dossier case_crawford_henry-john-pringle_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 47 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `crawford_henry-john-pringle_b1914`

- Printed name: **CRAWFORD, Henry John Pringle**
- Birth year: 1914 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956])
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1948-L32008.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956]:**

> CRAWFORD, Henry John Pringle.—b. 1914; ed. Shrewsbury Sch. and Jesus Coll., Camb., B.A.; admin. cadet, G.C., 1937; asst. dist. comsnr., 1938; dist. comsnr., 1943; admin. offr., cl. II, 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | admin. cadet | Gold Coast | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 1 | 1938 | asst. dist. comsnr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 2 | 1943 | dist. comsnr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 3 | 1949 | admin. offr., cl. II | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |

## Candidate stint `Crawford, J. P___Northern Rhodesia___1949`

- Staff-list name: **Crawford, J. P** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. Crawford | Master | Education | — | — |
| 1951 | J. P. Crawford | Master | Education | — | — |

### Deterministic checks: `crawford_henry-john-pringle_b1914` vs `Crawford, J. P___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'CRAWFORD' vs stint 'Crawford, J. P' (exact)
- [PASS] initials: bio ['H', 'J', 'P'] ~ stint ['J', 'P']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

