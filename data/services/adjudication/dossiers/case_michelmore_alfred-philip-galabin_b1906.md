<!-- {"case_id": "case_michelmore_alfred-philip-galabin_b1906", "bio_ids": ["michelmore_alfred-philip-galabin_b1906"], "stint_ids": ["Michelmore, P. G___Uganda___1949"]} -->
# Dossier case_michelmore_alfred-philip-galabin_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `michelmore_alfred-philip-galabin_b1906`

- Printed name: **MICHELMORE, Alfred Philip Galabin'**
- Birth year: 1906 (attested in editions [1951])
- Honours: F.R.E.S
- Appears in editions: [1951, 1957]

### Verbatim printed entry text (OCR)

**Version `col1951-L40836.v` — printed in editions [1951]:**

> MICHELMORE, Alfred Philip Galabin', M.A. (Cantab.), F.R.E.S.—b. 1906; ed. Marlborough and Trinity Coll., Camb.; asst. entom., Sudan, 1929; locust investn., Imp. Inst. of Entom., 1932; entom., Ken., 1939; o/c. internat. red locust cont., based on Abercorn, N. Rhod., 1941; entom., Uga., 1946; senr., 1946; author of articles in technical journals, etc.

**Version `col1957-L25665.v` — printed in editions [1957]:**

> MICHELMORE, A. P. G.—b. 1906; ed. Marlborough Coll. and Trinity Coll., Camb.; asst. entom., Sudan, 1929; N. Rhod., 1932; internat. red locust control, 1941-46; senr. entom., Uga., 1946; various scientific pp. on entomology and botany.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | asst. entom., Sudan | — | [1951, 1957] |
| 1 | 1932 | locust investn., Imp. Inst. of Entom | — | [1951] |
| 2 | 1932 | asst. entom., Sudan | Northern Rhodesia | [1957] |
| 3 | 1939 | entom. | Kenya | [1951] |
| 4 | 1941 | o/c. internat. red locust cont., based on Abercorn | Northern Rhodesia | [1951, 1957] |
| 5 | 1946 | entom. | Uganda | [1951, 1957] |

## Candidate stint `Michelmore, P. G___Uganda___1949`

- Staff-list name: **Michelmore, P. G** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. G. Michelmore | Entomologist | Agricultural | — | — |
| 1951 | P. G. Michelmore | Entomologists | Agricultural | — | — |

### Deterministic checks: `michelmore_alfred-philip-galabin_b1906` vs `Michelmore, P. G___Uganda___1949`

- [PASS] surname_gate: bio 'MICHELMORE' vs stint 'Michelmore, P. G' (exact)
- [PASS] initials: bio ['A', 'P', 'G'] ~ stint ['P', 'G']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 59 vs bar 60: 'entom.' ~ 'Entomologist'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1951] pos~56 (bar: >=2)
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

