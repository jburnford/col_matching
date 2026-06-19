<!-- {"case_id": "case_pickridge_geoffrey-martin_b1896", "bio_ids": ["pickridge_geoffrey-martin_b1896"], "stint_ids": ["Puckridge, G. M___Gold Coast___1927"]} -->
# Dossier case_pickridge_geoffrey-martin_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Puckridge, G. M___Gold Coast___1927` is also gate-compatible with biography(ies) outside this case: ['puckridge_geoffrey-martin_b1895'] (already linked elsewhere or filtered).

## Biography `pickridge_geoffrey-martin_b1896`

- Printed name: **PICKRIDGE, GEOFFREY MARTIN**
- Birth year: 1896 (attested in editions [1931])
- Appears in editions: [1931]

### Verbatim printed entry text (OCR)

**Version `col1931-L67531.v` — printed in editions [1931]:**

> PICKRIDGE, GEOFFREY MARTIN.—B. 1896; ed. Exeter Schl.; 2nd lieut., Devon Regt., T.F., Dec., 1913; capt., Dec., 1914; served in France with 6th West Yorks regt.; seconded to Royal Flying Corps, July, 1917; seconded to Inter Allied Aeronautical Comn. of Control, Germany, 1920; re-signed comm., Sept., 1921; asst. dist. commr., Gold Coast, 1921; dist. commr., 1925; asst. col. sec., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | 2nd lieut., Devon Regt., T.F | — | [1931] |
| 1 | 1914 | capt | — | [1931] |
| 2 | 1917 | seconded to Royal Flying Corps | — | [1931] |
| 3 | 1920 | seconded to Inter Allied Aeronautical Comn. of Control, Germany | — | [1931] |
| 4 | 1921 | re-signed comm | — | [1931] |
| 5 | 1921 | asst. dist. commr. | Gold Coast | [1931] |
| 6 | 1925 | dist. commr | Gold Coast *(inherited from previous clause)* | [1931] |
| 7 | 1928 | asst. col. sec | Gold Coast *(inherited from previous clause)* | [1931] |

## Candidate stint `Puckridge, G. M___Gold Coast___1927`

- Staff-list name: **Puckridge, G. M** | colony: **Gold Coast** | listed 1927–1936 | editions [1927, 1929, 1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | G. M. Puckridge | District Commissioner | Administrative and Political Service | — | — |
| 1929 | G. M. Puckridge | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | Captain |
| 1932 | G. M. Puckridge | Assistant Colonial Secretary | Colonial Secretary's Office | — | Captain |
| 1934 | G. M. Puckridge | Assistant Colonial Secretary | Colonial Secretary's Office | — | Captain |
| 1936 | G. M. Puckridge | Assistant Colonial Secretary | Colonial Secretary's Office | — | Captain |

### Deterministic checks: `pickridge_geoffrey-martin_b1896` vs `Puckridge, G. M___Gold Coast___1927`

- [PASS] surname_gate: bio 'PICKRIDGE' vs stint 'Puckridge, G. M' (fuzzy:1)
- [PASS] initials: bio ['G', 'M'] ~ stint ['G', 'M']
- [PASS] age_gate: stint starts 1927, birth 1896 (age 31)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1927-1936
- [PASS] position_sim: best 65 vs bar 60: 'dist. commr' ~ 'District Commissioner'
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

