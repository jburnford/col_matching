<!-- {"case_id": "case_bisset_william-david_b1889", "bio_ids": ["bisset_william-david_b1889"], "stint_ids": ["Bisset, W. D___Nigeria___1933"]} -->
# Dossier case_bisset_william-david_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bisset_william-david_b1889`

- Printed name: **BISSET, WILLIAM DAVID**
- Birth year: 1889 (attested in editions [1935, 1937, 1940])
- Appears in editions: [1935, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L56934.v` — printed in editions [1935, 1937, 1940]:**

> BISSET, WILLIAM DAVID, O.B.E. (mil.), M.I.Mech.E.—B. 1889; ed. Gordon Schl., Huntly, Aberdeenshire, and Allen Glen's Schl., Glasgow; engnr. lieut., R.N., Jan., 1914; engnr. lieut. comdr., R.N., Apr., 1919; engnr.-in-ch., Misida dockyard, Malta, 1916-19; H.M.S. "Egmont," 1920; asst. engnr., marine dept., Nigeria, 1920; prin. engnr., 1933; ag. supt. engnr., for various periods, 1934-37.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | engnr. lieut., R.N | — | [1935, 1937, 1940] |
| 1 | 1916–1919 | engnr.-in-ch., Misida dockyard | Malta | [1935, 1937, 1940] |
| 2 | 1919 | engnr. lieut. comdr., R.N | — | [1935, 1937, 1940] |
| 3 | 1920 | H.M.S. "Egmont," | Malta *(inherited from previous clause)* | [1935, 1937, 1940] |
| 4 | 1920 | asst. engnr., marine dept. | Nigeria | [1935, 1937, 1940] |
| 5 | 1933 | prin. engnr | Nigeria *(inherited from previous clause)* | [1935, 1937, 1940] |
| 6 | 1934–1937 | ag. supt. engnr., for various periods | Nigeria *(inherited from previous clause)* | [1935, 1937, 1940] |

## Candidate stint `Bisset, W. D___Nigeria___1933`

- Staff-list name: **Bisset, W. D** | colony: **Nigeria** | listed 1933–1934 | editions [1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | W. D. Bisset | Engineer Grade I | Marine | — | — |
| 1934 | W. D. Bisset | Engineers, Grade I | Marine | — | — |

### Deterministic checks: `bisset_william-david_b1889` vs `Bisset, W. D___Nigeria___1933`

- [PASS] surname_gate: bio 'BISSET' vs stint 'Bisset, W. D' (exact)
- [PASS] initials: bio ['W', 'D'] ~ stint ['W', 'D']
- [PASS] age_gate: stint starts 1933, birth 1889 (age 44)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1933-1934
- [PASS] position_sim: best 62 vs bar 60: 'prin. engnr' ~ 'Engineer Grade I'
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

