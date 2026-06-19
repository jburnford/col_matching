<!-- {"case_id": "case_besson_h-a_b1926", "bio_ids": ["besson_h-a_b1926"], "stint_ids": ["Besson, H. A___Leeward Islands___1957", "Besson, H. A___Montserrat___1963", "Besson, H. A___Virgin Islands___1961"]} -->
# Dossier case_besson_h-a_b1926

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `besson_h-a_b1926`

- Printed name: **BESSON, H. A**
- Birth year: 1926 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L13262.v` — printed in editions [1966]:**

> BESSON, H. A.—b. 1926; ed. Queen's Royal Coll., Trinidad; barrister-at-law, Lincoln's Inn; legal asst., Br. Virgin Is., 1956; cr. atty., 1960; Montserrat, 1962; atty.-gen., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1956 | legal asst., Br. Virgin Is | — | [1966] |
| 1 | 1960 | cr. atty | — | [1966] |
| 2 | 1962 | cr. atty | Montserrat | [1966] |
| 3 | 1963 | atty.-gen | Montserrat *(inherited from previous clause)* | [1966] |

## Candidate stint `Besson, H. A___Leeward Islands___1957`

- Staff-list name: **Besson, H. A** | colony: **Leeward Islands** | listed 1957–1958 | editions [1957, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | H. A. Besson | Legal Assistant | Civil Establishment | — | — |
| 1957 | H. A. Besson | Legal Assistant | Executive Council | — | — |
| 1958 | H. A. Besson | Legal Assistant | Civil Establishment | — | — |

### Deterministic checks: `besson_h-a_b1926` vs `Besson, H. A___Leeward Islands___1957`

- [PASS] surname_gate: bio 'BESSON' vs stint 'Besson, H. A' (exact)
- [PASS] initials: bio ['H', 'A'] ~ stint ['H', 'A']
- [PASS] age_gate: stint starts 1957, birth 1926 (age 31)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1958
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Besson, H. A___Montserrat___1963`

- Staff-list name: **Besson, H. A** | colony: **Montserrat** | listed 1963–1966 | editions [1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | H. A. Besson | Law Officer: Crown Attorney-Magistrate (Registrar, Provost-Marshal) | Civil Establishment | — | — |
| 1964 | H. A. Besson | Law Officer: Crown Attorney | Civil Establishment | — | — |
| 1965 | H. A. Besson | Law Officer: Crown Attorney | Civil Establishment | — | — |
| 1966 | H. A. Besson | Law Officer: Attorney-General | Civil Establishment | — | — |

### Deterministic checks: `besson_h-a_b1926` vs `Besson, H. A___Montserrat___1963`

- [PASS] surname_gate: bio 'BESSON' vs stint 'Besson, H. A' (exact)
- [PASS] initials: bio ['H', 'A'] ~ stint ['H', 'A']
- [PASS] age_gate: stint starts 1963, birth 1926 (age 37)
- [PASS] colony: 2 placed event(s) resolve to 'Montserrat'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1963-1966
- [FAIL] position_sim: best 42 vs bar 60: 'cr. atty' ~ 'Law Officer: Crown Attorney'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Besson, H. A___Virgin Islands___1961`

- Staff-list name: **Besson, H. A** | colony: **Virgin Islands** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | H. A. Besson | Crown Attorney | Civil Establishment | — | — |
| 1962 | H. A. Besson | Crown Attorney | Civil Establishment | — | — |

### Deterministic checks: `besson_h-a_b1926` vs `Besson, H. A___Virgin Islands___1961`

- [PASS] surname_gate: bio 'BESSON' vs stint 'Besson, H. A' (exact)
- [PASS] initials: bio ['H', 'A'] ~ stint ['H', 'A']
- [PASS] age_gate: stint starts 1961, birth 1926 (age 35)
- [FAIL] colony: no placed event resolves to 'Virgin Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1962
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

