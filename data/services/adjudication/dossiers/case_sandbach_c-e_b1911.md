<!-- {"case_id": "case_sandbach_c-e_b1911", "bio_ids": ["sandbach_c-e_b1911"], "stint_ids": ["Sandbach, C. E___Sarawak___1949"]} -->
# Dossier case_sandbach_c-e_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sandbach_c-e_b1911`

- Printed name: **SANDBACH, C. E**
- Birth year: 1911 (attested in editions [1959, 1960])
- Appears in editions: [1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1959-L27567.v` — printed in editions [1959, 1960]:**

> SANDBACH, C. E.—b. 1911; ed. Calday Grange Gram. Sch.; asst. treas., Sarawak, 1946; supt., customs, 1958-59.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | asst. treas. | Sarawak | [1959, 1960] |
| 1 | 1958–1959 | supt., customs | Sarawak *(inherited from previous clause)* | [1959, 1960] |

## Candidate stint `Sandbach, C. E___Sarawak___1949`

- Staff-list name: **Sandbach, C. E** | colony: **Sarawak** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. E. Sandbach | Superintendents of Customs | Trade and Customs | — | — |
| 1950 | C. E. Sandbach | Superintendent of Customs | TRADE AND CUSTOMS | — | — |
| 1951 | C. E. Sandbach | Superintendent of Customs | Trade and Customs | — | — |

### Deterministic checks: `sandbach_c-e_b1911` vs `Sandbach, C. E___Sarawak___1949`

- [PASS] surname_gate: bio 'SANDBACH' vs stint 'Sandbach, C. E' (exact)
- [PASS] initials: bio ['C', 'E'] ~ stint ['C', 'E']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 2 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 33 vs bar 60: 'asst. treas.' ~ 'Superintendents of Customs'
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

