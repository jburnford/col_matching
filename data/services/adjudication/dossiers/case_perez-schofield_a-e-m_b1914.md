<!-- {"case_id": "case_perez-schofield_a-e-m_b1914", "bio_ids": ["perez-schofield_a-e-m_b1914"], "stint_ids": ["Perez-Schofield, A. E___British Honduras___1965"]} -->
# Dossier case_perez-schofield_a-e-m_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `perez-schofield_a-e-m_b1914`

- Printed name: **PEREZ-SCHOFIELD, A. E. M**
- Birth year: 1914 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L20652.v` — printed in editions [1964, 1965, 1966]:**

> PEREZ-SCHOFIELD, A. E. M.—b. 1914; ed. Univ. of Madrid; temp. M.O., B. Hond., 1961; C.M.O.; 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1961 | temp. M.O. | British Honduras | [1964, 1965, 1966] |
| 1 | 1962 | temp. M.O. | British Honduras *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Perez-Schofield, A. E___British Honduras___1965`

- Staff-list name: **Perez-Schofield, A. E** | colony: **British Honduras** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | A. E. Perez-Schofield | Chief Medical Officer | Civil Establishment | — | — |
| 1966 | A. E. Perez-Schofield | Chief Medical Officer | Civil Establishment | — | — |

### Deterministic checks: `perez-schofield_a-e-m_b1914` vs `Perez-Schofield, A. E___British Honduras___1965`

- [PASS] surname_gate: bio 'PEREZ-SCHOFIELD' vs stint 'Perez-Schofield, A. E' (exact)
- [PASS] initials: bio ['A', 'E', 'M'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1965, birth 1914 (age 51)
- [PASS] colony: 2 placed event(s) resolve to 'British Honduras'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1965-1966
- [FAIL] position_sim: best 21 vs bar 60: 'temp. M.O.' ~ 'Chief Medical Officer'
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

