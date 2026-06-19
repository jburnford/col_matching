<!-- {"case_id": "case_brizzell_annie-isabel_b1877", "bio_ids": ["brizzell_annie-isabel_b1877"], "stint_ids": ["Brizzell, Annie Isabel___Basutoland___1924"]} -->
# Dossier case_brizzell_annie-isabel_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `brizzell_annie-isabel_b1877`

- Printed name: **BRIZZELL, ANNIE ISABEL**
- Birth year: 1877 (attested in editions [1927, 1928, 1930, 1931, 1932, 1933])
- Honours: M.B.E (1926)
- Appears in editions: [1927, 1928, 1930, 1931, 1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1927-L57455.v` — printed in editions [1927, 1928, 1930, 1931, 1932, 1933]:**

> BRIZZELL, ANNIE ISABEL, M.B.E. (1926).—B. 1877; staff nurse, Basutoland, 1906; matron, 1907; war serv., 1915-19; ment. in despatches, 1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906 | staff nurse | Basutoland | [1927, 1928, 1930, 1931, 1932, 1933] |
| 1 | 1907 | matron | Basutoland *(inherited from previous clause)* | [1927, 1928, 1930, 1931, 1932, 1933] |
| 2 | 1918 | ment. in despatches | Basutoland *(inherited from previous clause)* | [1927, 1928, 1930, 1931, 1932, 1933] |

## Candidate stint `Brizzell, Annie Isabel___Basutoland___1924`

- Staff-list name: **Brizzell, Annie Isabel** | colony: **Basutoland** | listed 1924–1925 | editions [1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | Annie Isabel Brizzell | Matron | Nursing Staff | — | — |
| 1925 | Annie Isabel Brizzell | Matrons | Medical | — | — |

### Deterministic checks: `brizzell_annie-isabel_b1877` vs `Brizzell, Annie Isabel___Basutoland___1924`

- [PASS] surname_gate: bio 'BRIZZELL' vs stint 'Brizzell, Annie Isabel' (exact)
- [PASS] initials: bio ['A', 'I'] ~ stint ['A', 'I']
- [PASS] age_gate: stint starts 1924, birth 1877 (age 47)
- [PASS] colony: 3 placed event(s) resolve to 'Basutoland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1924-1925
- [FAIL] position_sim: best 25 vs bar 60: 'ment. in despatches' ~ 'Matron'
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

