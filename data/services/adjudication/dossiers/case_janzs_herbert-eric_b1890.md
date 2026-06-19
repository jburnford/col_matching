<!-- {"case_id": "case_janzs_herbert-eric_b1890", "bio_ids": ["janzs_herbert-eric_b1890"], "stint_ids": ["Janz, H. E___Ceylon___1928"]} -->
# Dossier case_janzs_herbert-eric_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `janzs_herbert-eric_b1890`

- Printed name: **JANZS, HERBERT ERIC**
- Birth year: 1890 (attested in editions [1939])
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L67915.v` — printed in editions [1939]:**

> JANZS, HERBERT ERIC.—B. 1890; cadet, Ceylon civ. ser., Sept., 1914; ag. office astt., Batticaloa kach., Sept., 1915; office astt., Kegalla kach., Jan., 1917; do., Jaffna kach., Jan., 1918; pol. mag., Kalutara, Mar., 1920; dist. judge, Ratnapura, Jan., 1925; astt. sttlm. offr., Sept., 1928; ag. pol. mag., Colombo, Apr. to June, 1930; ag. sttlm. offr., May., 1931; offr., cls. I, grade II, Jan., 1937; sttlm. offr., Mar., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | cadet, Ceylon civ. ser | Ceylon | [1939] |
| 1 | 1915 | ag. office astt., Batticaloa kach | Ceylon *(inherited from previous clause)* | [1939] |
| 2 | 1917 | office astt., Kegalla kach | Ceylon *(inherited from previous clause)* | [1939] |
| 3 | 1918 | do., Jaffna kach | Ceylon *(inherited from previous clause)* | [1939] |
| 4 | 1920 | pol. mag., Kalutara | Ceylon *(inherited from previous clause)* | [1939] |
| 5 | 1925 | dist. judge, Ratnapura | Ceylon *(inherited from previous clause)* | [1939] |
| 6 | 1928 | astt. sttlm. offr | Ceylon *(inherited from previous clause)* | [1939] |
| 7 | 1930 | ag. pol. mag., Colombo | Ceylon *(inherited from previous clause)* | [1939] |
| 8 | 1931 | ag. sttlm. offr | Ceylon *(inherited from previous clause)* | [1939] |
| 9 | 1937 | offr., cls. I, grade II | Ceylon *(inherited from previous clause)* | [1939] |
| 10 | 1938 | sttlm. offr | Ceylon *(inherited from previous clause)* | [1939] |

## Candidate stint `Janz, H. E___Ceylon___1928`

- Staff-list name: **Janz, H. E** | colony: **Ceylon** | listed 1928–1931 | editions [1928, 1929, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | H. E. Janz | District Judge, Commissioner of Requests, Police Magistrate | District of Colombo and Midland Circuit | — | — |
| 1929 | H. E. Janz | Assistant Settlement Officer | Land Settlement Department | — | — |
| 1931 | H. E. Janz | Assistant Settlement Officer | Land Settlement Department | — | — |

### Deterministic checks: `janzs_herbert-eric_b1890` vs `Janz, H. E___Ceylon___1928`

- [PASS] surname_gate: bio 'JANZS' vs stint 'Janz, H. E' (fuzzy:1)
- [PASS] initials: bio ['H', 'E'] ~ stint ['H', 'E']
- [PASS] age_gate: stint starts 1928, birth 1890 (age 38)
- [PASS] colony: 11 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1928-1931
- [PASS] position_sim: best 70 vs bar 60: 'astt. sttlm. offr' ~ 'Assistant Settlement Officer'
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

