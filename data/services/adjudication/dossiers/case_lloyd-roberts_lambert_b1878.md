<!-- {"case_id": "case_lloyd-roberts_lambert_b1878", "bio_ids": ["lloyd-roberts_lambert_b1878"], "stint_ids": ["Lloyd-Roberts, L___Gold Coast___1917"]} -->
# Dossier case_lloyd-roberts_lambert_b1878

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['lloyd-roberts_lambert_b1878'] carry a single initial only — the namesake trap applies.

## Biography `lloyd-roberts_lambert_b1878`

- Printed name: **LLOYD-ROBERTS, LAMBERT**
- Birth year: 1878 (attested in editions [1918, 1919, 1921, 1922])
- Appears in editions: [1918, 1919, 1920, 1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1918-L52246.v` — printed in editions [1918, 1919, 1921, 1922]:**

> LLOYD-ROBERTS, LAMBERT.—B. 1878; ed. Harrow and Wadham Coll., Oxford, B.A.; called to the bar, Middle Temple, 1905; dist. comsnr., Gold Coast, 1909; ag. solr.-gen., Oct. to Dec., 1912; ag. pol. mag., Accra, Mar. to June, 1916.

**Version `col1920-L55201.v` — printed in editions [1920]:**

> LOYD-ROBERTS, LAMBERT.—B. 1878; ed. Harrow and Wadham Coll., Oxford; B.A.; called to the bar, Middle Temple, 1905; dist. comsnr., Gold Coast, 1909; ag. solr.-gen., Oct. to Dec., 1912; ag. pol. mag., Accra, Mar. to June, 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1905 | called to the bar, Middle Temple | — | [1918, 1919, 1920, 1921, 1922] |
| 1 | 1909 | dist. comsnr. | Gold Coast | [1918, 1919, 1920, 1921, 1922] |
| 2 | 1912 | ag. solr.-gen | Gold Coast *(inherited from previous clause)* | [1918, 1919, 1920, 1921, 1922] |
| 3 | 1916 | ag. pol. mag., Accra | Gold Coast *(inherited from previous clause)* | [1918, 1919, 1920, 1921, 1922] |

## Candidate stint `Lloyd-Roberts, L___Gold Coast___1917`

- Staff-list name: **Lloyd-Roberts, L** | colony: **Gold Coast** | listed 1917–1918 | editions [1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | L. Lloyd-Roberts | District Commissioner | Administrative and Political Department | — | — |
| 1918 | L. Lloyd-Roberts | District Commissioner | Administrative and Political Department | — | — |

### Deterministic checks: `lloyd-roberts_lambert_b1878` vs `Lloyd-Roberts, L___Gold Coast___1917`

- [PASS] surname_gate: bio 'LLOYD-ROBERTS' vs stint 'Lloyd-Roberts, L' (exact)
- [PASS] initials: bio ['L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1917, birth 1878 (age 39)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1917-1918
- [FAIL] position_sim: best 19 vs bar 60: 'ag. solr.-gen' ~ 'District Commissioner'
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

