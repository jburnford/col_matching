<!-- {"case_id": "case_curie_donald_e1876", "bio_ids": ["curie_donald_e1876", "currie_donald_e1876"], "stint_ids": ["Currie, D___Canada___1877"]} -->
# Dossier case_curie_donald_e1876

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['curie_donald_e1876', 'currie_donald_e1876'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Currie, D___Canada___1877'] have more than one claimant biography in this case.

## Biography `curie_donald_e1876`

- Printed name: **CURIE, DONALD**
- Birth year: not printed
- Honours: C.M.G. (1877), K.C.M.G. (1881)
- Appears in editions: [1889]

### Verbatim printed entry text (OCR)

**Version `col1889-L32598.v` — printed in editions [1889]:**

> CURIE, SIR DONALD, K.C.M.G. (1881), C.M.G. (1877).—Chairman of the Castle Mail Packets Co. In July, 1876, at the time of the negotiations between the Earl of Carnarvon and President Brand, he assisted by his good offices in bringing about the success of these negotiations and thus ending the long dispute between the British Government and the Orange Free State in reference to the Diamond Fields; has been M.P. for Perthshire since 1890.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876–1876 | — | Orange Free State | [1889] |
| 1 | 1890 | M.P. | — | [1889] |

## Biography `currie_donald_e1876`

- Printed name: **CURRIE, DONALD**
- Birth year: not printed
- Honours: C.M.G. (1877), K.C.M.G. (1881)
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27047.v` — printed in editions [1883]:**

> CURRIE, SIR DONALD, K.C.M.G. (1881), C.M.G. (1877).—An eminent shipowner, member of a firm owning a line of mail steamers running between Dartmouth and the principal ports of South Africa. Sir Donald Currie is well known for the interest he takes in South African politics. In July, 1876, at the time of the negotiations between the Earl of Carnarvon and President Brand, he assisted by his good offices in bringing about the success of these negotiations, and thus ending the long dispute between the British Government and the Orange Free State in reference to the Diamond Fields.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876–1876 | — | Orange Free State | [1883] |

## Candidate stint `Currie, D___Canada___1877`

- Staff-list name: **Currie, D** | colony: **Canada** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | D. Currie | Collector of Customs | — | — | — |
| 1878 | D. Currie | Collector of Customs | — | — | — |
| 1879 | D. Currie | Collector of Customs | — | — | — |
| 1880 | D. Currie | Collector of Customs | — | — | — |

### Deterministic checks: `curie_donald_e1876` vs `Currie, D___Canada___1877`

- [PASS] surname_gate: bio 'CURIE' vs stint 'Currie, D' (fuzzy:1)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `currie_donald_e1876` vs `Currie, D___Canada___1877`

- [PASS] surname_gate: bio 'CURRIE' vs stint 'Currie, D' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

