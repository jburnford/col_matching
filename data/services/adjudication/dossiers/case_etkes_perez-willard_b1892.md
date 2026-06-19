<!-- {"case_id": "case_etkes_perez-willard_b1892", "bio_ids": ["etkes_perez-willard_b1892"], "stint_ids": ["Etkes, P. W___Palestine___1931"]} -->
# Dossier case_etkes_perez-willard_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `etkes_perez-willard_b1892`

- Printed name: **ETKES, Perez Willard**
- Birth year: 1892 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L32462.v` — printed in editions [1948, 1949]:**

> ETKES, Perez Willard, B.Sc. (Civ. Eng.), M.Am.SOC.C.E., M.Am.SOC.M.I.E.—b. 1892; ed. Pub. Sch. No. 63, New York, Struyvesant High Sch., New York, Cooper Inst. (Tech.), New York City Coll., A. & M. Coll., Tex., U.S.A., medallist; clk. of wks., Pal., 1920; asst. engr., 1921; engr.-in-ch., 1930; senr. exec. engr., 1942.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | clk. of wks. | Palestine | [1948, 1949] |
| 1 | 1921 | asst. engr | Palestine *(inherited from previous clause)* | [1948, 1949] |
| 2 | 1930 | engr.-in-ch | Palestine *(inherited from previous clause)* | [1948, 1949] |
| 3 | 1942 | senr. exec. engr | Palestine *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Etkes, P. W___Palestine___1931`

- Staff-list name: **Etkes, P. W** | colony: **Palestine** | listed 1931–1940 | editions [1931, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | P. Etkes | Assistant Engineer | Public Works | — | — |
| 1940 | P. W. Etkes | Assistant Engineer | Department of Public Works | — | — |

### Deterministic checks: `etkes_perez-willard_b1892` vs `Etkes, P. W___Palestine___1931`

- [PASS] surname_gate: bio 'ETKES' vs stint 'Etkes, P. W' (exact)
- [PASS] initials: bio ['P', 'W'] ~ stint ['P', 'W']
- [PASS] age_gate: stint starts 1931, birth 1892 (age 39)
- [PASS] colony: 4 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1931-1940
- [PASS] position_sim: best 67 vs bar 60: 'asst. engr' ~ 'Assistant Engineer'
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

