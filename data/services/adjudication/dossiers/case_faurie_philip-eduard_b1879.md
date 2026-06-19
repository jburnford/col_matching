<!-- {"case_id": "case_faurie_philip-eduard_b1879", "bio_ids": ["faurie_philip-eduard_b1879"], "stint_ids": ["Faure, P. E___Cape of Good Hope___1899"]} -->
# Dossier case_faurie_philip-eduard_b1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `faurie_philip-eduard_b1879`

- Printed name: **FAURIE, PHILIP EDUARD**
- Birth year: 1879 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L64172.v` — printed in editions [1940]:**

> FAURIE, PHILIP EDUARD.—B. 1879; educated Graaff Reinet Coll., Normal Coll. Schl. and S. African Coll., Cape Town; C.S. higher law; clk., atty. gen.'s office, Cape Town, 1898; mag's office, Cape Town, 1900; astt. mag., Simonstown, 1909; pub. pros., Cape Town, 1916; ch. clk. and astt. mag., Cape Town, 1918; mag., Murrayburg, 1919; Bedford, 1923; Nylstroom (Waterberg), 1929; Harrismith, 1932; Paarl, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898 | clk., atty. gen.'s office, Cape Town | Cape of Good Hope | [1940] |
| 1 | 1900 | mag's office, Cape Town | Cape of Good Hope | [1940] |
| 2 | 1909 | astt. mag., Simonstown | Cape of Good Hope *(inherited from previous clause)* | [1940] |
| 3 | 1916 | pub. pros., Cape Town | Cape of Good Hope | [1940] |
| 4 | 1918 | ch. clk. and astt. mag., Cape Town | Cape of Good Hope | [1940] |
| 5 | 1919 | mag., Murrayburg | Cape of Good Hope *(inherited from previous clause)* | [1940] |
| 6 | 1923 | Bedford | Cape of Good Hope *(inherited from previous clause)* | [1940] |
| 7 | 1929 | Nylstroom (Waterberg) | Cape of Good Hope *(inherited from previous clause)* | [1940] |
| 8 | 1932 | Harrismith | Cape of Good Hope *(inherited from previous clause)* | [1940] |
| 9 | 1937 | Paarl | Cape of Good Hope *(inherited from previous clause)* | [1940] |

## Candidate stint `Faure, P. E___Cape of Good Hope___1899`

- Staff-list name: **Faure, P. E** | colony: **Cape of Good Hope** | listed 1899–1900 | editions [1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | P. E. Faure | Clerks | Divisional Courts and Police Branch | — | — |
| 1900 | P. E. Faure | Clerks | Divisional Courts and Police Branch | — | — |

### Deterministic checks: `faurie_philip-eduard_b1879` vs `Faure, P. E___Cape of Good Hope___1899`

- [PASS] surname_gate: bio 'FAURIE' vs stint 'Faure, P. E' (fuzzy:1)
- [PASS] initials: bio ['P', 'E'] ~ stint ['P', 'E']
- [PASS] age_gate: stint starts 1899, birth 1879 (age 20)
- [PASS] colony: 10 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1899-1900
- [FAIL] position_sim: best 22 vs bar 60: 'clk., atty. gen.'s office, Cape Town' ~ 'Clerks'
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

