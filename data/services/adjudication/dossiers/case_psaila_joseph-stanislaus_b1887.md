<!-- {"case_id": "case_psaila_joseph-stanislaus_b1887", "bio_ids": ["psaila_joseph-stanislaus_b1887"], "stint_ids": ["Psaila, J___British Guiana___1919", "Psaila, Stephen___British Guiana___1946"]} -->
# Dossier case_psaila_joseph-stanislaus_b1887

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `psaila_joseph-stanislaus_b1887`

- Printed name: **PSAILA, JOSEPH STANISLAUS**
- Birth year: 1887 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L67735.v` — printed in editions [1940]:**

> PSAILA, JOSEPH STANISLAUS.—B. 1887; ed. Stanislaus Gram. Schl., Br. Guiana and St. Francis Xavier's Coll., Bruges, Belgium; astt. commr., 1917; 3rd grade do., 1926; 3rd cls. offr., dist. commr.'s office, 1932; cls. II offr., do., 1934; inspr., distilleries, 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917 | astt. commr | — | [1940] |
| 1 | 1926 | 3rd grade do | — | [1940] |
| 2 | 1932 | 3rd cls. offr., dist. commr.'s office | — | [1940] |
| 3 | 1934 | cls. II offr. | Dominions Office | [1940] |
| 4 | 1936 | inspr., distilleries | Dominions Office *(inherited from previous clause)* | [1940] |

## Candidate stint `Psaila, J___British Guiana___1919`

- Staff-list name: **Psaila, J** | colony: **British Guiana** | listed 1919–1921 | editions [1919, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | J. Psaila | Assistant Commissary | Commissaries Department | — | — |
| 1921 | J. Psaila | Assistant Commissary | Commissaries Department | — | — |

### Deterministic checks: `psaila_joseph-stanislaus_b1887` vs `Psaila, J___British Guiana___1919`

- [PASS] surname_gate: bio 'PSAILA' vs stint 'Psaila, J' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J']
- [PASS] age_gate: stint starts 1919, birth 1887 (age 32)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1919-1921
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Psaila, Stephen___British Guiana___1946`

- Staff-list name: **Psaila, Stephen** | colony: **British Guiana** | listed 1946–1948 | editions [1946, 1948]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1946 | Stephen Psaila | Consular Agent, French Provisional Government | Foreign Consuls | — | — |
| 1948 | Stephen Psaila | Consular Agent | Foreign Consular Officers | — | — |

### Deterministic checks: `psaila_joseph-stanislaus_b1887` vs `Psaila, Stephen___British Guiana___1946`

- [PASS] surname_gate: bio 'PSAILA' vs stint 'Psaila, Stephen' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1946, birth 1887 (age 59)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1946-1948
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

