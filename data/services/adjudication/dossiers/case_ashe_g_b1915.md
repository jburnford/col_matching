<!-- {"case_id": "case_ashe_g_b1915", "bio_ids": ["ashe_g_b1915"], "stint_ids": ["Ashe, G___British Somaliland___1949"]} -->
# Dossier case_ashe_g_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['ashe_g_b1915'] carry a single initial only — the namesake trap applies.

## Biography `ashe_g_b1915`

- Printed name: **ASHE, G**
- Birth year: 1915 (attested in editions [1959, 1960, 1961, 1962])
- Appears in editions: [1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1959-L20291.v` — printed in editions [1959, 1960, 1961, 1962]:**

> ASHE, G.—b. 1915; ed. Manchester Univ.; mil. serv., 1943-46, capt., R.A.M.C.; M.O., Som., 1947; S.M.O., 1950; T.B. offr., Aden, 1954-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | M.O. | Somaliland | [1959, 1960, 1961, 1962] |
| 1 | 1950 | S.M.O | Somaliland *(inherited from previous clause)* | [1959, 1960, 1961, 1962] |
| 2 | 1954–1961 | T.B. offr. | Aden | [1959, 1960, 1961, 1962] |

## Candidate stint `Ashe, G___British Somaliland___1949`

- Staff-list name: **Ashe, G** | colony: **British Somaliland** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. Ashe | Medical Officer | Medical | — | — |
| 1950 | G. Ashe | Medical Officer | Medical | — | — |
| 1951 | G. Ashe | Senior Medical Officer | Medical | — | — |

### Deterministic checks: `ashe_g_b1915` vs `Ashe, G___British Somaliland___1949`

- [PASS] surname_gate: bio 'ASHE' vs stint 'Ashe, G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [PASS] colony: 2 placed event(s) resolve to 'British Somaliland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
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

