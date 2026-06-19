<!-- {"case_id": "case_hodnett_ethel_b1895", "bio_ids": ["hodnett_ethel_b1895"], "stint_ids": ["Hodnett, Miss E___Northern Rhodesia___1929"]} -->
# Dossier case_hodnett_ethel_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hodnett_ethel_b1895'] carry a single initial only — the namesake trap applies.

## Biography `hodnett_ethel_b1895`

- Printed name: **HODNETT, Ethel**
- Birth year: 1895 (attested in editions [1948])
- Honours: C.M.B, M.B.E, S.L.C, S.R.N
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L33386.v` — printed in editions [1948]:**

> HODNETT, Ethel, M.B.E., S.L.C., S.R.N., C.M.B.—b. 1895; ed. at Hereford and Malvern; Q.V.J.I. cert.; on mil. serv., 1918-19; apptd. health dep., N. Rhod., 1927; prin. of Copperbelt African Girls Sch., 1940.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | apptd. health dep. | Northern Rhodesia | [1948] |
| 1 | 1940 | prin. of Copperbelt African Girls Sch | Northern Rhodesia *(inherited from previous clause)* | [1948] |

## Candidate stint `Hodnett, Miss E___Northern Rhodesia___1929`

- Staff-list name: **Hodnett, Miss E** | colony: **Northern Rhodesia** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | Miss E. Hodnett | Nurses | Health | — | — |
| 1930 | Miss E. Hodnett | Nurses | Health | — | — |

### Deterministic checks: `hodnett_ethel_b1895` vs `Hodnett, Miss E___Northern Rhodesia___1929`

- [PASS] surname_gate: bio 'HODNETT' vs stint 'Hodnett, Miss E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['M', 'E']
- [PASS] age_gate: stint starts 1929, birth 1895 (age 34)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1930
- [FAIL] position_sim: best 9 vs bar 60: 'apptd. health dep.' ~ 'Nurses'
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

