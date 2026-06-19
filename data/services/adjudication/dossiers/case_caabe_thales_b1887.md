<!-- {"case_id": "case_caabe_thales_b1887", "bio_ids": ["caabe_thales_b1887"], "stint_ids": ["Cababe, Th___Cyprus___1934"]} -->
# Dossier case_caabe_thales_b1887

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['caabe_thales_b1887'] carry a single initial only — the namesake trap applies.

## Biography `caabe_thales_b1887`

- Printed name: **CAABE, THALES**
- Birth year: 1887 (attested in editions [1936])
- Appears in editions: [1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L59455.v` — printed in editions [1936]:**

> CAABE, THALES.—B. 1887; clk., P.W.D., Cyprus, 1910; ch. clk., secretariat, 1931; asst. postmr.-gen., 1934; ag. P.M.G. in 1934 and 1935.

**Version `col1937-L59406.v` — printed in editions [1937, 1940]:**

> CABABE, Thales.—B. 1887; clk., P.W.D., Cyprus, 1910; ch. clk., secretariat, 1931; asst. postmtr.-gen., 1934; ag. P.M.G., various periods, 1934-39.

**Version `dol1935-L57367.v` — printed in editions [1935]:**

> CABABE, Thales.—B. 1887; clk., P.W.D., Cyprus, 1910; ch. clk., secretariat, 1931; asst. postmr.-gen., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | clk., P.W.D. | Cyprus | [1935, 1936, 1937, 1940] |
| 1 | 1931 | ch. clk., secretariat | Cyprus *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |
| 2 | 1934 | asst. postmr.-gen. | Cyprus *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |
| 3 | 1934–1935 | ag. P.M.G. | — | [1936] |

## Candidate stint `Cababe, Th___Cyprus___1934`

- Staff-list name: **Cababe, Th** | colony: **Cyprus** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | Th. Cababe | Chief Clerk | Colonial Secretary's Office | — | — |
| 1939 | T. Cababe | Assistant Postmaster-General | Postal Department | — | — |

### Deterministic checks: `caabe_thales_b1887` vs `Cababe, Th___Cyprus___1934`

- [PASS] surname_gate: bio 'CAABE' vs stint 'Cababe, Th' (fuzzy:1)
- [PASS] initials: bio ['T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1934, birth 1887 (age 47)
- [PASS] colony: 3 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1939
- [PASS] position_sim: best 68 vs bar 60: 'asst. postmr.-gen.' ~ 'Assistant Postmaster-General'
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

