<!-- {"case_id": "case_loos_w-t_b1886", "bio_ids": ["loos_w-t_b1886"], "stint_ids": ["Loos, W. T___Ceylon___1934"]} -->
# Dossier case_loos_w-t_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `loos_w-t_b1886`

- Printed name: **LOOS, W.T**
- Birth year: 1886 (attested in editions [1935, 1936, 1937])
- Appears in editions: [1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `dol1935-L60344.v` — printed in editions [1935, 1936, 1937]:**

> LOOS, W.T.—B. 1886; apptd. cls. III., Ceylon civ. serv., Mar., 1934; office ast., Trincomalee kach., Mar., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | apptd. cls. III., Ceylon civ. serv | Ceylon | [1935, 1936, 1937] |

## Candidate stint `Loos, W. T___Ceylon___1934`

- Staff-list name: **Loos, W. T** | colony: **Ceylon** | listed 1934–1940 | editions [1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | W. T. Loos | Chief Clerk | Civil Establishment | — | — |
| 1936 | W. T. Loos | Office Assistant | Eastern Province | — | — |
| 1937 | W. T. Loos | Office Assistant | EASTERN PROVINCE | — | — |
| 1940 | W. T. Loos | Office Assistant | Secretariat | — | — |

### Deterministic checks: `loos_w-t_b1886` vs `Loos, W. T___Ceylon___1934`

- [PASS] surname_gate: bio 'LOOS' vs stint 'Loos, W. T' (exact)
- [PASS] initials: bio ['W', 'T'] ~ stint ['W', 'T']
- [PASS] age_gate: stint starts 1934, birth 1886 (age 48)
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1940
- [FAIL] position_sim: best 35 vs bar 60: 'apptd. cls. III., Ceylon civ. serv' ~ 'Chief Clerk'
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

