<!-- {"case_id": "case_troy_michael-francis_b1877", "bio_ids": ["troy_michael-francis_b1877"], "stint_ids": ["Troy, M. F___Australia___1912"]} -->
# Dossier case_troy_michael-francis_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `troy_michael-francis_b1877`

- Printed name: **TROY, MICHAEL FRANCIS**
- Birth year: 1877 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L69089.v` — printed in editions [1940]:**

> TROY, HON. MICHAEL FRANCIS.—B. 1877; ed. Pub. Schl., Wardell, N.S.W.; rep., Mt. Magnet, leg. assem., W. Australia, 1904-39; speaker, 1911-17; min. for mines and agr., 1924-27; lands and immigrn., 1927-30 and 1933-39; agt.-gen., W.A., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904–1939 | rep., Mt. Magnet, leg. assem. | Western Australia | [1940] |
| 1 | 1911–1917 | speaker | — | [1940] |
| 2 | 1924–1927 | min. for mines and agr. | — | [1940] |
| 3 | 1927–1939 | lands and immigrn. | — | [1940] |
| 4 | 1939 | agt.-gen. | Western Australia | [1940] |

## Candidate stint `Troy, M. F___Australia___1912`

- Staff-list name: **Troy, M. F** | colony: **Australia** | listed 1912–1927 | editions [1912, 1913, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | M. F. Troy | Speaker | Legislative Assembly | — | — |
| 1913 | M. F. Troy | Speaker | Legislative Assembly | — | — |
| 1927 | Hon. M. F. Troy, M.L.A. | Minister for Agriculture | Department of Minister for Agriculture | — | — |
| 1927 | M. F. Troy | Minister for Mines, also Minister for Agriculture | Minister for Mines | — | — |

### Deterministic checks: `troy_michael-francis_b1877` vs `Troy, M. F___Australia___1912`

- [PASS] surname_gate: bio 'TROY' vs stint 'Troy, M. F' (exact)
- [PASS] initials: bio ['M', 'F'] ~ stint ['M', 'F']
- [PASS] age_gate: stint starts 1912, birth 1877 (age 35)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

