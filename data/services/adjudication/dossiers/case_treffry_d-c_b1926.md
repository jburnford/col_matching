<!-- {"case_id": "case_treffry_d-c_b1926", "bio_ids": ["treffry_d-c_b1926"], "stint_ids": ["Treffry, D. C___Aden___1960", "Treffry, D. C___Aden___1965"]} -->
# Dossier case_treffry_d-c_b1926

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `treffry_d-c_b1926`

- Printed name: **TREFFRY, D. C**
- Birth year: 1926 (attested in editions [1964, 1965, 1966])
- Honours: O.B.E (1966)
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L22544.v` — printed in editions [1964, 1965, 1966]:**

> TREFFRY, D. C., O.B.E. (1966).—b. 1926; ed. Marlborough and Magdalen Coll., Oxford; mil. serv., 1944–47, capt.; Indian polit. serv., 1947; polit. offr., Aden, 1952; regisr., co-ops., and chief marktg. offr., 1959; asst. ch. sec., 1961; advr. on co-ops. and marktg., 1962; admin. offr., cl. I, 1963.

**Version `col1961-L28162.v` — printed in editions [1961, 1962, 1963]:**

> TREFRY, D. C.—b. 1926; ed. Marlborough, and Magdalen Coll., Oxford; mil. serv., 1944-47, capt.; Indian polit. serv., 1947; polit. offr., Aden, 1952; registr., co-ops., and chief marktg. offr., 1959; asst. ch. sec., 1961; advr. on co-ops. and marktg., 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | Indian polit. serv | — | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1952 | polit. offr. | Aden | [1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1959 | regisr., co-ops., and chief marktg. offr | Aden *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1961 | asst. ch. sec | Aden *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1962 | advr. on co-ops. and marktg | Aden *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1963 | admin. offr., cl. I | Aden *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Treffry, D. C___Aden___1960`

- Staff-list name: **Treffry, D. C** | colony: **Aden** | listed 1960–1962 | editions [1960, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1960 | D. C. Treffry | Registrar of Co-operative Societies and Chief Marketing Officer | Civil Establishment | — | — |
| 1962 | D. C. Treffry | Registrar of Co-operative Societies and Chief Marketing Officer | Aden Protectorate | — | — |

### Deterministic checks: `treffry_d-c_b1926` vs `Treffry, D. C___Aden___1960`

- [PASS] surname_gate: bio 'TREFFRY' vs stint 'Treffry, D. C' (exact)
- [PASS] initials: bio ['D', 'C'] ~ stint ['D', 'C']
- [PASS] age_gate: stint starts 1960, birth 1926 (age 34)
- [PASS] colony: 5 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1960-1962
- [PASS] position_sim: best 69 vs bar 60: 'regisr., co-ops., and chief marktg. offr' ~ 'Registrar of Co-operative Societies and Chief Marketing Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Treffry, D. C___Aden___1965`

- Staff-list name: **Treffry, D. C** | colony: **Aden** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | D. C. Treffry | Permanent Secretaries/Deputy Permanent Secretaries | Civil Establishment | — | — |
| 1966 | D. C. Treffry | Permanent Secretary, Ministry of Finance | Civil Establishment | — | — |

### Deterministic checks: `treffry_d-c_b1926` vs `Treffry, D. C___Aden___1965`

- [PASS] surname_gate: bio 'TREFFRY' vs stint 'Treffry, D. C' (exact)
- [PASS] initials: bio ['D', 'C'] ~ stint ['D', 'C']
- [PASS] age_gate: stint starts 1965, birth 1926 (age 39)
- [PASS] colony: 5 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1965-1966
- [FAIL] position_sim: best 33 vs bar 60: 'admin. offr., cl. I' ~ 'Permanent Secretary, Ministry of Finance'
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

