<!-- {"case_id": "case_huitt_alan-norman_b1890", "bio_ids": ["huitt_alan-norman_b1890"], "stint_ids": ["Hutt, A. N___Ceylon___1914", "Hutt, A. N___Ceylon___1920"]} -->
# Dossier case_huitt_alan-norman_b1890

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `huitt_alan-norman_b1890` ↔ `Hutt, A. N___Ceylon___1914` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Hutt, A. N___Ceylon___1914` is also gate-compatible with biography(ies) outside this case: ['hutt_alan-norman_b1890'] (already linked elsewhere or filtered).
- NOTE: stint `Hutt, A. N___Ceylon___1920` is also gate-compatible with biography(ies) outside this case: ['hutt_alan-norman_b1890'] (already linked elsewhere or filtered).

## Biography `huitt_alan-norman_b1890`

- Printed name: **HUITT, ALAN NORMAN**
- Birth year: 1890 (attested in editions [1917])
- Appears in editions: [1917]

### Verbatim printed entry text (OCR)

**Version `col1917-L50615.v` — printed in editions [1917]:**

> HUITT, ALAN NORMAN.—B. 1890; B.A. Oxon.; cadet, Ceylon civ. ser., Dec., 1913; attached to Colombo Kachcheri, Dec., 1913; addtl. pol. mag., Colombo, in addition to his own duties, Apr., 1914; ag. office astt. to govt. agt., W. Prov., Dec., 1914; ditto, N.W. Prov., May, 1915.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | cadet, Ceylon civ. ser | Ceylon | [1917] |
| 1 | 1914 | addtl. pol. mag., Colombo, in addition to his own duties | Ceylon *(inherited from previous clause)* | [1917] |
| 2 | 1915 | ditto, N.W. Prov | Ceylon *(inherited from previous clause)* | [1917] |

## Candidate stint `Hutt, A. N___Ceylon___1914`

- Staff-list name: **Hutt, A. N** | colony: **Ceylon** | listed 1914–1915 | editions [1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | A. N. Hutt | Cadet | Civil Establishment | — | — |
| 1915 | A. N. Hutt | Cadet | Civil Establishment | — | — |

### Deterministic checks: `huitt_alan-norman_b1890` vs `Hutt, A. N___Ceylon___1914`

- [PASS] surname_gate: bio 'HUITT' vs stint 'Hutt, A. N' (fuzzy:1)
- [PASS] initials: bio ['A', 'N'] ~ stint ['A', 'N']
- [PASS] age_gate: stint starts 1914, birth 1890 (age 24)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1914-1915
- [PASS] position_sim: best 100 vs bar 60: 'cadet, Ceylon civ. ser' ~ 'Cadet'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Hutt, A. N___Ceylon___1920`

- Staff-list name: **Hutt, A. N** | colony: **Ceylon** | listed 1920–1925 | editions [1920, 1921, 1922, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | A. N. Hutt | Police Magistrate | Judicial Establishment | — | — |
| 1921 | A. N. Hutt | Assistant Controller | Civil Establishment | — | — |
| 1922 | A. N. Hutt | Assistant Controller | Civil Establishment | — | — |
| 1925 | A. N. Hutt | Assistant Government Agent | Central Province | — | — |

### Deterministic checks: `huitt_alan-norman_b1890` vs `Hutt, A. N___Ceylon___1920`

- [PASS] surname_gate: bio 'HUITT' vs stint 'Hutt, A. N' (fuzzy:1)
- [PASS] initials: bio ['A', 'N'] ~ stint ['A', 'N']
- [PASS] age_gate: stint starts 1920, birth 1890 (age 30)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1920-1925
- [FAIL] position_sim: best 42 vs bar 60: 'ditto, N.W. Prov' ~ 'Assistant Controller'
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

