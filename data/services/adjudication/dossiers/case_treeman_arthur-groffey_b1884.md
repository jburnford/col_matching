<!-- {"case_id": "case_treeman_arthur-groffey_b1884", "bio_ids": ["treeman_arthur-groffey_b1884"], "stint_ids": ["Freeman, A___Australia___1912", "Freeman, A___Newfoundland___1908"]} -->
# Dossier case_treeman_arthur-groffey_b1884

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 36 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `treeman_arthur-groffey_b1884`

- Printed name: **TREEMAN, ARTHUR GROFFEY**
- Birth year: 1884 (attested in editions [1933])
- Honours: A.I.E.E
- Appears in editions: [1933]

### Verbatim printed entry text (OCR)

**Version `col1933-L63974.v` — printed in editions [1933]:**

> TREEMAN, ARTHUR GROFFEY, A.I.E.E.—B. 1884; Br. P.O., inspr., London engng. dist., July, 1903; City and Guilds, London Inst., 1st hons. telegraphy, 1909; ditto, 1st final telephony, 1912; war serv., 1915-18; asst. teleg. engrnr., P. & T., F.M.S., May, 1920; teleg. engrnr., Johore, Sept., 1923; ch. teleg. engrnr., Nov., 1926; engrnr., P. & T., Seremban, Sept., 1930; sr. engrnr., P. & T., S.S. & F.M.S., Mar., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | Br. P.O., inspr., London engng. dist | — | [1933] |
| 1 | 1909 | City and Guilds, London Inst., 1st hons. telegraphy | — | [1933] |
| 2 | 1912 | ditto, 1st final telephony | — | [1933] |
| 3 | 1920 | asst. teleg. engrnr., P. & T. | Federated Malay States | [1933] |
| 4 | 1923 | teleg. engrnr. | Johore | [1933] |
| 5 | 1926 | ch. teleg. engrnr | Johore *(inherited from previous clause)* | [1933] |
| 6 | 1930 | engrnr., P. & T., Seremban | Johore *(inherited from previous clause)* | [1933] |
| 7 | 1931 | sr. engrnr., P. & T., S.S. & F.M.S | Straits Settlements | [1933] |

## Candidate stint `Freeman, A___Australia___1912`

- Staff-list name: **Freeman, A** | colony: **Australia** | listed 1912–1913 | editions [1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | A. Freeman | Consul | Foreign Consuls | — | Colonel |
| 1913 | A. Freeman | Consul | Foreign Consuls | — | Colonel |

### Deterministic checks: `treeman_arthur-groffey_b1884` vs `Freeman, A___Australia___1912`

- [PASS] surname_gate: bio 'TREEMAN' vs stint 'Freeman, A' (fuzzy:1)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A']
- [PASS] age_gate: stint starts 1912, birth 1884 (age 28)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1913
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Freeman, A___Newfoundland___1908`

- Staff-list name: **Freeman, A** | colony: **Newfoundland** | listed 1908–1915 | editions [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | A. Freeman | Sub-Collector | Department of Customs | — | — |
| 1909 | A. Freeman | Sub-Collector | Department of Customs | — | — |
| 1910 | A. Freeman | Sub-Collector | Department of Customs | — | — |
| 1911 | A. Freeman | Sub-Collector | Department of Customs | — | — |
| 1912 | A. Freeman | Sub-Collectors | Department of Customs | — | — |
| 1913 | A. Freeman | Sub-Collector | Department of Customs | — | — |
| 1914 | A. Freeman | Sub-Collector | Department of Customs | — | — |
| 1915 | A. Freeman | Sub-Collector | Department of Customs | — | — |

### Deterministic checks: `treeman_arthur-groffey_b1884` vs `Freeman, A___Newfoundland___1908`

- [PASS] surname_gate: bio 'TREEMAN' vs stint 'Freeman, A' (fuzzy:1)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A']
- [PASS] age_gate: stint starts 1908, birth 1884 (age 24)
- [FAIL] colony: no placed event resolves to 'Newfoundland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1915
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

