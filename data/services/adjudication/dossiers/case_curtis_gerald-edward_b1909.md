<!-- {"case_id": "case_curtis_gerald-edward_b1909", "bio_ids": ["curtis_gerald-edward_b1909"], "stint_ids": ["Curtis, G. E___Northern Rhodesia___1936"]} -->
# Dossier case_curtis_gerald-edward_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 27 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `curtis_gerald-edward_b1909`

- Printed name: **CURTIS, Gerald Edward**
- Birth year: 1909 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32072.v` — printed in editions [1948, 1949, 1950, 1951]:**

> CURTIS, Gerald Edward,—b. 1909; ed. Winchester Coll. and Trinity Coll., Oxford, M.A. (Oxon); on mil. serv. 1940-45, maj.; cadet, N. Rhod., 1932; dist. offr., 1934; seconded as asst. dir., game and tsetse control, 1947; seconded C.O., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | cadet | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 1 | 1934 | dist. offr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1947 | seconded as asst. dir., game and tsetse control | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1949 | seconded C.O | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Curtis, G. E___Northern Rhodesia___1936`

- Staff-list name: **Curtis, G. E** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | G. E. Curtis | District Officers | District Administration | — | — |
| 1939 | G. E. Curtis | District Officer | District Administration | — | — |
| 1940 | G. E. Curtis | District Officer | District Administration | — | — |

### Deterministic checks: `curtis_gerald-edward_b1909` vs `Curtis, G. E___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'CURTIS' vs stint 'Curtis, G. E' (exact)
- [PASS] initials: bio ['G', 'E'] ~ stint ['G', 'E']
- [PASS] age_gate: stint starts 1936, birth 1909 (age 27)
- [PASS] colony: 4 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [PASS] position_sim: best 72 vs bar 60: 'dist. offr' ~ 'District Officer'
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

