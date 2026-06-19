<!-- {"case_id": "case_hellrich_kenneth-sergeant_b1912", "bio_ids": ["hellrich_kenneth-sergeant_b1912"], "stint_ids": ["Hellrich, K. S___Singapore___1949"]} -->
# Dossier case_hellrich_kenneth-sergeant_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hellrich_kenneth-sergeant_b1912`

- Printed name: **HELLRICH, Kenneth Sergeant**
- Birth year: 1912 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951, 1957]

### Verbatim printed entry text (OCR)

**Version `col1950-L36282.v` — printed in editions [1950, 1951]:**

> HELLRICH, Kenneth Sergeant.—b. 1912; ed. Berkhamsted and Peterhouse, Camb., B.A. hons., hist. and anthropol.; interned, S’pore., 1942-45; probr., gov. monopolies, S’pore., 1934; asst. supt., excise, 1937; customs offr., preventive, Parit Buntar, 1939; senr. customs offr. (warehouse), Telok Anson, 1940; liquors divn., S’pore., 1946; tobacco divn., 1949.

**Version `col1957-L23997.v` — printed in editions [1957]:**

> HELLRICH, K. S.—b. 1912; ed. Berks. hamsted Sch. and Peterhouse Camb.; prob., trade and customs dept., S.S., 1934; customs offr., 1938; senr., S'pore, 1946; asst. compt., customs, Fed. of Mal., 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | probr., gov. monopolies, S’pore | — | [1950, 1951] |
| 1 | 1934 | prob., trade and customs dept. | Straits Settlements | [1957] |
| 2 | 1937 | asst. supt., excise | — | [1950, 1951] |
| 3 | 1938 | customs offr | Straits Settlements *(inherited from previous clause)* | [1957] |
| 4 | 1939 | customs offr., preventive, Parit Buntar | — | [1950, 1951] |
| 5 | 1940 | senr. customs offr. (warehouse), Telok Anson | — | [1950, 1951] |
| 6 | 1942–1945 | interned, S’pore | — | [1950, 1951] |
| 7 | 1946 | liquors divn., S’pore | — | [1950, 1951] |
| 8 | 1946 | senr., S'pore | Straits Settlements *(inherited from previous clause)* | [1957] |
| 9 | 1949 | tobacco divn | — | [1950, 1951] |
| 10 | 1952 | asst. compt., customs, Fed. of Mal | Straits Settlements *(inherited from previous clause)* | [1957] |

## Candidate stint `Hellrich, K. S___Singapore___1949`

- Staff-list name: **Hellrich, K. S** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | K. S. Hellrich | Senior Customs Officers and Customs Officers | CUSTOMS AND EXCISE | — | — |
| 1951 | K. S. Hellrich | Senior Customs Officers and Customs Officers | CUSTOMS | — | — |

### Deterministic checks: `hellrich_kenneth-sergeant_b1912` vs `Hellrich, K. S___Singapore___1949`

- [PASS] surname_gate: bio 'HELLRICH' vs stint 'Hellrich, K. S' (exact)
- [PASS] initials: bio ['K', 'S'] ~ stint ['K', 'S']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [FAIL] colony: no placed event resolves to 'Singapore'
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

