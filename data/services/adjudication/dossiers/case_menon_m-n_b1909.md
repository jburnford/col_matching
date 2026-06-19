<!-- {"case_id": "case_menon_m-n_b1909", "bio_ids": ["menon_m-n_b1909"], "stint_ids": ["Menon, M. N___Singapore___1959"]} -->
# Dossier case_menon_m-n_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `menon_m-n_b1909`

- Printed name: **MENON, M. N**
- Birth year: 1909 (attested in editions [1958, 1959, 1960])
- Appears in editions: [1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1958-L25246.v` — printed in editions [1958, 1959, 1960]:**

> MENON, M. N.—b. 1909; ed. Tech. Sch., Kuala Lumpur, and Melbourne Tech. Coll., Aust.; apprentice, survey dept., F.M.S. and S.S., 1927; tech. subordinate, 1931; tech. asst., spec. gr., 1949; surveyor, 1952; micro-film unit, 1954; dep. chief surveyor, 1957; chief surveyor, 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | apprentice, survey dept., F.M.S. and S.S | Federated Malay States | [1958, 1959, 1960] |
| 1 | 1931 | tech. subordinate | Federated Malay States *(inherited from previous clause)* | [1958, 1959, 1960] |
| 2 | 1949 | tech. asst., spec. gr | Federated Malay States *(inherited from previous clause)* | [1958, 1959, 1960] |
| 3 | 1952 | surveyor | Federated Malay States *(inherited from previous clause)* | [1958, 1959, 1960] |
| 4 | 1954 | micro-film unit | Federated Malay States *(inherited from previous clause)* | [1958, 1959, 1960] |
| 5 | 1957 | dep. chief surveyor | Federated Malay States *(inherited from previous clause)* | [1958, 1959, 1960] |
| 6 | 1959 | chief surveyor | Federated Malay States *(inherited from previous clause)* | [1958, 1959, 1960] |

## Candidate stint `Menon, M. N___Singapore___1959`

- Staff-list name: **Menon, M. N** | colony: **Singapore** | listed 1959–1962 | editions [1959, 1960, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | M. N. Menon | Deputy Chief Surveyor | Civil Establishment | — | — |
| 1960 | M. N. Menon | Chief Surveyor | Ministry of National Development | — | — |
| 1962 | M. N. Menon | Chief Surveyor | Prime Minister's Office | — | — |

### Deterministic checks: `menon_m-n_b1909` vs `Menon, M. N___Singapore___1959`

- [PASS] surname_gate: bio 'MENON' vs stint 'Menon, M. N' (exact)
- [PASS] initials: bio ['M', 'N'] ~ stint ['M', 'N']
- [PASS] age_gate: stint starts 1959, birth 1909 (age 50)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1962
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

