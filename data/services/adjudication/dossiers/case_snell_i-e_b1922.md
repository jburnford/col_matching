<!-- {"case_id": "case_snell_i-e_b1922", "bio_ids": ["snell_i-e_b1922"], "stint_ids": ["Snell, I.E___Aden___1949", "Snell, I.E___Aden___1960", "Snell, I.E___Aden___1964"]} -->
# Dossier case_snell_i-e_b1922

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `snell_i-e_b1922`

- Printed name: **SNELL, I. E**
- Birth year: 1922 (attested in editions [1966])
- Honours: O.B.E (1957)
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L18068.v` — printed in editions [1966]:**

> SNELL, I. E., O.B.E. (1957).—b. 1922; ed. Churcher's Coll, Petersfield; mil. serv., 1939–51; political offr., Aden, 1951; commdt., Hadrami Beduin Legion, 1957; asst. sec., 1960; admin. offr. cl. II, 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | political offr. | Aden | [1966] |
| 1 | 1957 | commdt., Hadrami Beduin Legion | Aden *(inherited from previous clause)* | [1966] |
| 2 | 1960 | asst. sec | Aden *(inherited from previous clause)* | [1966] |
| 3 | 1964 | admin. offr. cl. II | Aden *(inherited from previous clause)* | [1966] |

## Candidate stint `Snell, I.E___Aden___1949`

- Staff-list name: **Snell, I.E** | colony: **Aden** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | Major I. E. Snell | Military Assistant to the Resident Adviser, Mukalla | ADEN PROTECTORATE | — | Major |
| 1950 | I. E. Snell | Military Assistant to the Resident Adviser, Mukalla | ADEN PROTECTORATE | — | Major |

### Deterministic checks: `snell_i-e_b1922` vs `Snell, I.E___Aden___1949`

- [PASS] surname_gate: bio 'SNELL' vs stint 'Snell, I.E' (exact)
- [PASS] initials: bio ['I', 'E'] ~ stint ['I', 'E']
- [PASS] age_gate: stint starts 1949, birth 1922 (age 27)
- [PASS] colony: 4 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 22 vs bar 60: 'political offr.' ~ 'Military Assistant to the Resident Adviser, Mukalla'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Snell, I.E___Aden___1960`

- Staff-list name: **Snell, I.E** | colony: **Aden** | listed 1960–1961 | editions [1960, 1961]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1960 | I. E. Snell | Commandant, Hadhrami Beduin Legion | Aden Protectorate | — | — |
| 1961 | I. E. Snell | Commandant, Hadhrami Beduin Legion | Aden Protectorate | — | — |

### Deterministic checks: `snell_i-e_b1922` vs `Snell, I.E___Aden___1960`

- [PASS] surname_gate: bio 'SNELL' vs stint 'Snell, I.E' (exact)
- [PASS] initials: bio ['I', 'E'] ~ stint ['I', 'E']
- [PASS] age_gate: stint starts 1960, birth 1922 (age 38)
- [PASS] colony: 4 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1960-1961
- [PASS] position_sim: best 92 vs bar 60: 'commdt., Hadrami Beduin Legion' ~ 'Commandant, Hadhrami Beduin Legion'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Snell, I.E___Aden___1964`

- Staff-list name: **Snell, I.E** | colony: **Aden** | listed 1964–1965 | editions [1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | I.E. Snell | Administrative Officers (Superscale) | CIVIL ESTABLISHMENT | — | — |
| 1965 | I. E. Snell | Administrative Officers (Superscale) | Civil Establishment | — | — |

### Deterministic checks: `snell_i-e_b1922` vs `Snell, I.E___Aden___1964`

- [PASS] surname_gate: bio 'SNELL' vs stint 'Snell, I.E' (exact)
- [PASS] initials: bio ['I', 'E'] ~ stint ['I', 'E']
- [PASS] age_gate: stint starts 1964, birth 1922 (age 42)
- [PASS] colony: 4 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1964-1965
- [FAIL] position_sim: best 48 vs bar 60: 'admin. offr. cl. II' ~ 'Administrative Officers (Superscale)'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

