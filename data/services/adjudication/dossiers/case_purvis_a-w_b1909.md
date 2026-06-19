<!-- {"case_id": "case_purvis_a-w_b1909", "bio_ids": ["purvis_a-w_b1909"], "stint_ids": ["Purvis, A. W___Kenya___1950"]} -->
# Dossier case_purvis_a-w_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `purvis_a-w_b1909`

- Printed name: **PURVIS, A. W**
- Birth year: 1909 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1956-L23638.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961]:**

> PURVIS, A. W.—b. 1909; ed. Colfe's Gram. Sch. and London Univ.; barrister-at-law, Gray's Inn; mil. serv., 1941–46, major; admin. sec., med. dept., Ken., 1949; clk., leg. co., 1953–60.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | admin. sec., med. dept. | Kenya | [1956, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1953–1960 | clk., leg. co | Kenya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Purvis, A. W___Kenya___1950`

- Staff-list name: **Purvis, A. W** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | A. W. Purvis | Administrative Secretary | Medical | — | — |
| 1951 | A. W. Purvis | Administrative Secretary | Medical | — | — |

### Deterministic checks: `purvis_a-w_b1909` vs `Purvis, A. W___Kenya___1950`

- [PASS] surname_gate: bio 'PURVIS' vs stint 'Purvis, A. W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1950, birth 1909 (age 41)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 52 vs bar 60: 'admin. sec., med. dept.' ~ 'Administrative Secretary'
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

