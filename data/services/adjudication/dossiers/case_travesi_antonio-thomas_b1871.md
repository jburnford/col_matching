<!-- {"case_id": "case_travesi_antonio-thomas_b1871", "bio_ids": ["travesi_antonio-thomas_b1871"], "stint_ids": ["Traversi, A. T___New Zealand___1914"]} -->
# Dossier case_travesi_antonio-thomas_b1871

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `travesi_antonio-thomas_b1871`

- Printed name: **TRAVESI, Antonio Thomas**
- Birth year: 1871 (attested in editions [1924])
- Appears in editions: [1924, 1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1924-L58441.v` — printed in editions [1924]:**

> TRAVESI, Antonio Thomas, F.I.A. (London), F.C.A.S. (New York).—B. 1871; govt. insurance dept., N.Z. 1891-1907; actuary, friendly societies dept., 1907-17; actuary and sec., national provident fund, 1910-17; ast. actuary, govt. insurance dept., 1917-22; actuary, 1922; commr., 1923.

**Version `col1925-L59943.v` — printed in editions [1925, 1927]:**

> TRAVERSI, ANTONIO THOMAS, F.I.A. (London), F.C.A.S. (New York).—B. 1871; govt. insurance dept., N.Z. 1891-1907; actuary, friendly societies dept., 1907-17; actuary and sec., national provident fund, 1910-17; astt. actuary, govt. insurance dept., 1917-22; actuary, 1922; comsnr., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891–1907 | govt. insurance dept. | New Zealand | [1924, 1925, 1927] |
| 1 | 1907–1917 | actuary, friendly societies dept | New Zealand *(inherited from previous clause)* | [1924, 1925, 1927] |
| 2 | 1910–1917 | actuary and sec., national provident fund | New Zealand *(inherited from previous clause)* | [1924, 1925, 1927] |
| 3 | 1917–1922 | ast. actuary, govt. insurance dept | New Zealand *(inherited from previous clause)* | [1924, 1925, 1927] |
| 4 | 1922 | actuary | New Zealand *(inherited from previous clause)* | [1924, 1925, 1927] |
| 5 | 1923 | commr | New Zealand *(inherited from previous clause)* | [1924, 1925, 1927] |

## Candidate stint `Traversi, A. T___New Zealand___1914`

- Staff-list name: **Traversi, A. T** | colony: **New Zealand** | listed 1914–1922 | editions [1914, 1915, 1917, 1918, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | A. T. Traversi | Actuary and Deputy Registrar | Friendly Societies' Office | — | — |
| 1915 | A. T. Traversi | Actuary and Deputy Registrar | Friendly Societies' Office | — | — |
| 1917 | A. T. Traversi | Actuary and Deputy Registrar | Friendly Societies' Office | — | — |
| 1918 | A. T. Traversi | Actuary and Deputy Registrar | Friendly Societies' Office | — | — |
| 1920 | A. T. Traversi | Assistant Actuary | Government Insurance Department | — | — |
| 1922 | A. T. Traversi | Assistant Actuary | Government Insurance Department | — | — |

### Deterministic checks: `travesi_antonio-thomas_b1871` vs `Traversi, A. T___New Zealand___1914`

- [PASS] surname_gate: bio 'TRAVESI' vs stint 'Traversi, A. T' (fuzzy:1)
- [PASS] initials: bio ['A', 'T'] ~ stint ['A', 'T']
- [PASS] age_gate: stint starts 1914, birth 1871 (age 43)
- [PASS] colony: 6 placed event(s) resolve to 'New Zealand'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1914-1922
- [PASS] position_sim: best 100 vs bar 60: 'actuary' ~ 'Assistant Actuary'
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

