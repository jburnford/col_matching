<!-- {"case_id": "case_rocheford_c-a_b1929", "bio_ids": ["rocheford_c-a_b1929"], "stint_ids": ["Rocheford, C. A___Barbados___1963"]} -->
# Dossier case_rocheford_c-a_b1929

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rocheford_c-a_b1929`

- Printed name: **ROCHEFORD, C. A**
- Birth year: 1929 (attested in editions [1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1962-L25925.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> ROCHEFORD, C. A.—b. 1929; ed. Harrison Coll.; solr., Barb., 1955; mag., 1959; dep. regtr., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1955 | solr. | Barbados | [1962, 1963, 1964, 1965, 1966] |
| 1 | 1959 | mag | Barbados *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Rocheford, C. A___Barbados___1963`

- Staff-list name: **Rocheford, C. A** | colony: **Barbados** | listed 1963–1966 | editions [1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | C. A. Rocheford | Deputy Registrar | Judiciary | — | — |
| 1964 | C. A. Rocheford | Deputy Registrar | Judiciary | — | — |
| 1965 | C. A. Rocheford | Deputy Registrar | Judiciary | — | — |
| 1966 | C. A. Rocheford | Deputy Registrar | Judiciary | — | — |

### Deterministic checks: `rocheford_c-a_b1929` vs `Rocheford, C. A___Barbados___1963`

- [PASS] surname_gate: bio 'ROCHEFORD' vs stint 'Rocheford, C. A' (exact)
- [PASS] initials: bio ['C', 'A'] ~ stint ['C', 'A']
- [PASS] age_gate: stint starts 1963, birth 1929 (age 34)
- [PASS] colony: 2 placed event(s) resolve to 'Barbados'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1963-1966
- [FAIL] position_sim: best 11 vs bar 60: 'mag' ~ 'Deputy Registrar'
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

