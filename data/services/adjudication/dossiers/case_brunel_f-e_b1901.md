<!-- {"case_id": "case_brunel_f-e_b1901", "bio_ids": ["brunel_f-e_b1901"], "stint_ids": ["Brunel, E___Mauritius___1936"]} -->
# Dossier case_brunel_f-e_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `brunel_f-e_b1901`

- Printed name: **BRUNEL, F. E**
- Birth year: 1901 (attested in editions [1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1958-L20950.v` — printed in editions [1958, 1959, 1960, 1961, 1962]:**

> BRUNEL, F. E.—b. 1901; ed. Royal Coll., Maur. and Montpellier Univ., France; M.O., Maur., 1932; med. supt., mental hosp., 1954-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | M.O. | Mauritius | [1958, 1959, 1960, 1961, 1962] |
| 1 | 1954–1961 | med. supt., mental hosp | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Brunel, E___Mauritius___1936`

- Staff-list name: **Brunel, E** | colony: **Mauritius** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | E. Brunel | Medical Officer | Medical and Health Department | — | — |
| 1937 | E. Brunel | Medical Officer | Medical and Health Department | — | — |
| 1939 | E. Brunel | Medical Officer | Medical and Health Department | — | — |

### Deterministic checks: `brunel_f-e_b1901` vs `Brunel, E___Mauritius___1936`

- [PASS] surname_gate: bio 'BRUNEL' vs stint 'Brunel, E' (exact)
- [PASS] initials: bio ['F', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1936, birth 1901 (age 35)
- [PASS] colony: 2 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1939
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

