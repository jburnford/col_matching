<!-- {"case_id": "case_kindersley_j-m_e1863", "bio_ids": ["kindersley_j-m_e1863", "kindersley_j-m_e1893"], "stint_ids": ["Kindersley, J. M___Straits Settlements___1894"]} -->
# Dossier case_kindersley_j-m_e1863

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Kindersley, J. M___Straits Settlements___1894'] have more than one claimant biography in this case.

## Biography `kindersley_j-m_e1863`

- Printed name: **KINDERSLEY, J. M**
- Birth year: not printed
- Appears in editions: [1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1896-L39783.v` — printed in editions [1896, 1898, 1899, 1900]:**

> KINDERSLEY, J. M.—Ed. Repton and Hertford Coll., Oxon; cadet, S.S., Mar., 1863; passed final exam. in Malay, June, 1894; dist. off., Penang, Apr., 1897; supt. of educn., Penang, June, 1898.

**Version `col1897-L32837.v` — printed in editions [1897]:**

> KINDERSLEY, J. M.—Ed. Repton and Harrow Coll. Oxon.; cadet, S.S., Mar., 1893; passed final exam in Malay, June, 1894; ag. dist. offr., Penang, Mar., 1896.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1863 | cadet | Straits Settlements | [1896, 1898, 1899, 1900] |
| 1 | 1893 | cadet | Straits Settlements | [1897] |
| 2 | 1894 | passed final exam. in Malay | Straits Settlements *(inherited from previous clause)* | [1896, 1897, 1898, 1899, 1900] |
| 3 | 1896 | ag. dist. offr., Penang | Straits Settlements *(inherited from previous clause)* | [1897] |
| 4 | 1897 | dist. off., Penang | Straits Settlements *(inherited from previous clause)* | [1896, 1898, 1899, 1900] |
| 5 | 1898 | supt. of educn., Penang | Straits Settlements *(inherited from previous clause)* | [1896, 1898, 1899, 1900] |

## Biography `kindersley_j-m_e1893`

- Printed name: **KINDERSLEY, J. M**
- Birth year: not printed
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L32433.v` — printed in editions [1894]:**

> KINDERSLEY, J. M.—Cadet, S.S., 1893.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893 | Cadet | Straits Settlements | [1894] |

## Candidate stint `Kindersley, J. M___Straits Settlements___1894`

- Staff-list name: **Kindersley, J. M** | colony: **Straits Settlements** | listed 1894–1897 | editions [1894, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | J. M. Kindersley | Student Cadets | Colonial Secretary's Office | — | — |
| 1896 | J. M. Kindersley | Passed Cadets | Colonial Secretary's Office | — | — |
| 1897 | J. M. Kindersley | — | Colonial Secretary's Office | — | — |

### Deterministic checks: `kindersley_j-m_e1863` vs `Kindersley, J. M___Straits Settlements___1894`

- [PASS] surname_gate: bio 'KINDERSLEY' vs stint 'Kindersley, J. M' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 6 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 6 event tenure(s) overlap stint years 1894-1897
- [PASS] position_sim: best 63 vs bar 60: 'passed final exam. in Malay' ~ 'Passed Cadets'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `kindersley_j-m_e1893` vs `Kindersley, J. M___Straits Settlements___1894`

- [PASS] surname_gate: bio 'KINDERSLEY' vs stint 'Kindersley, J. M' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1894-1897
- [FAIL] position_sim: best 56 vs bar 60: 'Cadet' ~ 'Passed Cadets'
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

