<!-- {"case_id": "case_hobgen_george_b1853", "bio_ids": ["hobgen_george_b1853"], "stint_ids": ["Hobden, G.B___Kenya___1939"]} -->
# Dossier case_hobgen_george_b1853

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hobgen_george_b1853'] carry a single initial only — the namesake trap applies.

## Biography `hobgen_george_b1853`

- Printed name: **HOBGEN, George**
- Birth year: 1853 (attested in editions [1919])
- Honours: C.M.G (1915)
- Terminal: retired 1915 — “retired, 1915.”
- Appears in editions: [1919]

### Verbatim printed entry text (OCR)

**Version `col1919-L53123.v` — printed in editions [1919]:**

> HOBGEN, George, C.M.G. (1915).—B. 1853; M.A., F.G.S.; gold medallist, R.G.S., educ. at Congregational School, Lewishain, Univ. School, Nottingham, and Cambridge Univ., mathematical scholar and prizeman, St. Catherine's Coll. Cambridge; 1st class hons. in maths.; served in accountant and controller gen.'s dept., Inland Revenue, London, 1872-3; second master, boys' high school, Christchurch, New Zealand, 1881-1889; inspr. of schls., North Canterbury, 1887-1889; headmstr., Timaru high schl., 1889-1899; inspr. gen. of schls. and head of educn. dept., New Zealand, 1899; represented N.Z. at Education Conference in London, 1907; retired, 1915.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872–1873 | served in accountant and controller gen.'s dept., Inland Revenue, London | — | [1919] |
| 1 | 1881–1889 | second master, boys' high school, Christchurch | New Zealand | [1919] |
| 2 | 1887–1889 | inspr. of schls., North Canterbury | New Zealand *(inherited from previous clause)* | [1919] |
| 3 | 1889–1899 | headmstr., Timaru high schl | New Zealand *(inherited from previous clause)* | [1919] |
| 4 | 1899 | inspr. gen. of schls. and head of educn. dept. | New Zealand | [1919] |
| 5 | 1907 | represented N.Z. at Education Conference in London | New Zealand *(inherited from previous clause)* | [1919] |

## Candidate stint `Hobden, G.B___Kenya___1939`

- Staff-list name: **Hobden, G.B** | colony: **Kenya** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | G.B. Hobden | Postmaster-General | Posts and Telegraphs Department | — | — |
| 1940 | G. B. Hobden | Postmaster-General | Posts and Telegraphs Department | — | — |

### Deterministic checks: `hobgen_george_b1853` vs `Hobden, G.B___Kenya___1939`

- [PASS] surname_gate: bio 'HOBGEN' vs stint 'Hobden, G.B' (fuzzy:1)
- [PASS] initials: bio ['G'] ~ stint ['G', 'B']
- [PASS] age_gate: stint starts 1939, birth 1853 (age 86)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

