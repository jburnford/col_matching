<!-- {"case_id": "case_crisp_harold_b1874", "bio_ids": ["crisp_harold_b1874"], "stint_ids": ["Crisp, Harold___Australia___1918"]} -->
# Dossier case_crisp_harold_b1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['crisp_harold_b1874'] carry a single initial only — the namesake trap applies.

## Biography `crisp_harold_b1874`

- Printed name: **CRISP, HAROLD**
- Birth year: 1874 (attested in editions [1939, 1940])
- Honours: K.B
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L65977.v` — printed in editions [1939, 1940]:**

> CRISP, HON. SIR HAROLD, K.B., (1938).—B. 1874; called to bar, 1896; puisne judge, Tasmania, Aug., 1914; admstr. of govt., 1930; ch. just., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896 | called to bar | — | [1939, 1940] |
| 1 | 1914 | puisne judge | Tasmania | [1939, 1940] |
| 2 | 1930 | admstr. of govt | Tasmania *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1937 | ch. just | Tasmania *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Crisp, Harold___Australia___1918`

- Staff-list name: **Crisp, Harold** | colony: **Australia** | listed 1918–1927 | editions [1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | Harold Crisp | Puisne Judges | Judicial and Legal Departments | — | — |
| 1927 | Hon. Harold Crisp | Puisne Judge | Judges | — | — |

### Deterministic checks: `crisp_harold_b1874` vs `Crisp, Harold___Australia___1918`

- [PASS] surname_gate: bio 'CRISP' vs stint 'Crisp, Harold' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1918, birth 1874 (age 44)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1927
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

