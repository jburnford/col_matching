<!-- {"case_id": "case_shahabudden_m_b1931", "bio_ids": ["shahabudden_m_b1931"], "stint_ids": ["Shahabuddeen, M___British Guiana___1964"]} -->
# Dossier case_shahabudden_m_b1931

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['shahabudden_m_b1931'] carry a single initial only — the namesake trap applies.

## Biography `shahabudden_m_b1931`

- Printed name: **SHAHABUDDEN, M**
- Birth year: 1931 (attested in editions [1963])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L24750.v` — printed in editions [1963]:**

> SHAHABUDDEN, M.—b. 1931; ed. Middle Temple, Lond.; barrister-at-law; ag. mag., B.G., 1959; ag. cr. couns., 1959; cr. couns., 1960; sovr.-gen., 1962.

**Version `col1964-L21639.v` — printed in editions [1964, 1965, 1966]:**

> SHAHABUDDEEN, M.—b. 1931; ed. Middle Temple, Lond.; barrister-at-law; ag. mag., B.G., 1959; ag. cr. couns., 1959; cr. couns., 1960; solr.-gen., 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1959 | ag. mag. | British Guiana | [1963, 1964, 1965, 1966] |
| 1 | 1960 | cr. couns | British Guiana *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 2 | 1962 | sovr.-gen | British Guiana *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Shahabuddeen, M___British Guiana___1964`

- Staff-list name: **Shahabuddeen, M** | colony: **British Guiana** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | M. Shahabuddeen | Solicitor-General | Civil Establishment | — | — |
| 1965 | M. Shahabuddeen | Solicitor-General | Civil Establishment | — | — |
| 1966 | M. Shahabuddeen | Solicitor-General | Civil Establishment | — | — |

### Deterministic checks: `shahabudden_m_b1931` vs `Shahabuddeen, M___British Guiana___1964`

- [PASS] surname_gate: bio 'SHAHABUDDEN' vs stint 'Shahabuddeen, M' (fuzzy:1)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1964, birth 1931 (age 33)
- [PASS] colony: 3 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1964-1966
- [FAIL] position_sim: best 52 vs bar 60: 'sovr.-gen' ~ 'Solicitor-General'
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

