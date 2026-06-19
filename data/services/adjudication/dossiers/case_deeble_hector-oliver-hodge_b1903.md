<!-- {"case_id": "case_deeble_hector-oliver-hodge_b1903", "bio_ids": ["deeble_hector-oliver-hodge_b1903"], "stint_ids": ["Deeble, H. O. H___Trinidad and Tobago___1922", "Deeble, H. O. H___Trinidad and Tobago___1952"]} -->
# Dossier case_deeble_hector-oliver-hodge_b1903

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `deeble_hector-oliver-hodge_b1903`

- Printed name: **DEEBLE, Hector Oliver Hodge**
- Birth year: 1903 (attested in editions [1951, 1953, 1954, 1955, 1956, 1957, 1958])
- Appears in editions: [1951, 1953, 1954, 1955, 1956, 1957, 1958]

### Verbatim printed entry text (OCR)

**Version `col1951-L37509.v` — printed in editions [1951, 1953, 1954, 1955, 1956, 1957, 1958]:**

> DEEBLE, Hector Oliver Hodge.—b. 1903; ed. Queen’s Royal Coll., Trin.; barrister-at-law, Middle Temple; registr.-gen’s dept., Trin., 1920; dep. registr. gen., 1946; registr. gen., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | registr.-gen’s dept. | Trinidad | [1951, 1953, 1954, 1955, 1956, 1957, 1958] |
| 1 | 1946 | dep. registr. gen | Trinidad *(inherited from previous clause)* | [1951, 1953, 1954, 1955, 1956, 1957, 1958] |
| 2 | 1950 | registr. gen | Trinidad *(inherited from previous clause)* | [1951, 1953, 1954, 1955, 1956, 1957, 1958] |

## Candidate stint `Deeble, H. O. H___Trinidad and Tobago___1922`

- Staff-list name: **Deeble, H. O. H** | colony: **Trinidad and Tobago** | listed 1922–1927 | editions [1922, 1923, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | H. Deeble | 7th Clerk | Registrar-General's Department | — | — |
| 1923 | H. Deeble | 6th | Registrar-General's Department | — | — |
| 1927 | H. Deeble | 5th Clerk | Registrar-General's Department | — | — |

### Deterministic checks: `deeble_hector-oliver-hodge_b1903` vs `Deeble, H. O. H___Trinidad and Tobago___1922`

- [PASS] surname_gate: bio 'DEEBLE' vs stint 'Deeble, H. O. H' (exact)
- [PASS] initials: bio ['H', 'O', 'H'] ~ stint ['H', 'O', 'H']
- [PASS] age_gate: stint starts 1922, birth 1903 (age 19)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Deeble, H. O. H___Trinidad and Tobago___1952`

- Staff-list name: **Deeble, H. O. H** | colony: **Trinidad and Tobago** | listed 1952–1954 | editions [1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | H. Deeble | Registrar General | Civil Establishment | — | — |
| 1953 | H. O. H. Deeble | Registrar-General | Civil Establishment | — | — |
| 1954 | H. O. H. Deeble | Registrar-General | Civil Establishment | — | — |

### Deterministic checks: `deeble_hector-oliver-hodge_b1903` vs `Deeble, H. O. H___Trinidad and Tobago___1952`

- [PASS] surname_gate: bio 'DEEBLE' vs stint 'Deeble, H. O. H' (exact)
- [PASS] initials: bio ['H', 'O', 'H'] ~ stint ['H', 'O', 'H']
- [PASS] age_gate: stint starts 1952, birth 1903 (age 49)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1952-1954
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

