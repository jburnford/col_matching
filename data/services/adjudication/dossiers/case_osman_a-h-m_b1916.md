<!-- {"case_id": "case_osman_a-h-m_b1916", "bio_ids": ["osman_a-h-m_b1916"], "stint_ids": ["Osman, A. M___Mauritius___1946"]} -->
# Dossier case_osman_a-h-m_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Osman, A. M___Mauritius___1946` is also gate-compatible with biography(ies) outside this case: ['osman_a-r-m_b1902'] (already linked elsewhere or filtered).

## Biography `osman_a-h-m_b1916`

- Printed name: **OSMAN, A. H. M**
- Birth year: 1916 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L25759.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> OSMAN, A. H. M.—b. 1916; ed. Royal Coll., Maur., and Edin. Univ.; dentist, Maur., 1945; senr. dentist, 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | dentist | Mauritius | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1962 | senr. dentist | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Osman, A. M___Mauritius___1946`

- Staff-list name: **Osman, A. M** | colony: **Mauritius** | listed 1946–1948 | editions [1946, 1948]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1946 | A. M. Osman | Executive Council Member | Executive Council | — | — |
| 1946 | A. M. Osman | Nominated Member | Nominated Members | — | — |
| 1948 | A. M. Osman | Nominated Member | Medical and Health Department | — | — |
| 1948 | A. M. Osman | Member | Executive Council | — | — |

### Deterministic checks: `osman_a-h-m_b1916` vs `Osman, A. M___Mauritius___1946`

- [PASS] surname_gate: bio 'OSMAN' vs stint 'Osman, A. M' (exact)
- [PASS] initials: bio ['A', 'H', 'M'] ~ stint ['A', 'M']
- [PASS] age_gate: stint starts 1946, birth 1916 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1946-1948
- [FAIL] position_sim: best 35 vs bar 60: 'dentist' ~ 'Nominated Member'
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

