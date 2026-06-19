<!-- {"case_id": "case_fiorini-lowell_edward_b1899", "bio_ids": ["fiorini-lowell_edward_b1899"], "stint_ids": ["Fiorini Lowell, E___Malta___1930"]} -->
# Dossier case_fiorini-lowell_edward_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['fiorini-lowell_edward_b1899'] carry a single initial only — the namesake trap applies.

## Biography `fiorini-lowell_edward_b1899`

- Printed name: **FIORINI LOWELL, Edward**
- Birth year: 1899 (attested in editions [1951, 1955, 1956, 1957, 1958])
- Appears in editions: [1951, 1955, 1956, 1957, 1958]

### Verbatim printed entry text (OCR)

**Version `col1951-L38045.v` — printed in editions [1951, 1955, 1956, 1957, 1958]:**

> FIORINI LOWELL, Edward.—b. 1899; ed. Lyceum, Malta; substitute clk., 1917; apptd. civ. serv. (admin.), Malta, 1921; ch. examinr., audit offr., 1943; audr., 1948; ex-officio mem., lottery comsn.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917 | substitute clk | — | [1951, 1955, 1956, 1957, 1958] |
| 1 | 1921 | apptd. civ. serv. (admin.) | Malta | [1951, 1955, 1956, 1957, 1958] |
| 2 | 1943 | ch. examinr., audit offr | Malta *(inherited from previous clause)* | [1951, 1955, 1956, 1957, 1958] |
| 3 | 1948 | audr | Malta *(inherited from previous clause)* | [1951, 1955, 1956, 1957, 1958] |

## Candidate stint `Fiorini Lowell, E___Malta___1930`

- Staff-list name: **Fiorini Lowell, E** | colony: **Malta** | listed 1930–1931 | editions [1930, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | E. Fiorini Lowell | Clerks, 2nd Class | Audit Office | — | — |
| 1931 | E. Fiorini Lowell | Clerks, 2nd Class | Audit Office | — | — |

### Deterministic checks: `fiorini-lowell_edward_b1899` vs `Fiorini Lowell, E___Malta___1930`

- [PASS] surname_gate: bio 'FIORINI LOWELL' vs stint 'Fiorini Lowell, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1930, birth 1899 (age 31)
- [PASS] colony: 3 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1930-1931
- [FAIL] position_sim: best 39 vs bar 60: 'apptd. civ. serv. (admin.)' ~ 'Clerks, 2nd Class'
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

