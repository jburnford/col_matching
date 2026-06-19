<!-- {"case_id": "case_biasini_r_b1904", "bio_ids": ["biasini_r_b1904"], "stint_ids": ["Biasini, R___Malta___1934", "Biasini, R___Malta___1949"]} -->
# Dossier case_biasini_r_b1904

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['biasini_r_b1904'] carry a single initial only — the namesake trap applies.

## Biography `biasini_r_b1904`

- Printed name: **BIASINI, R**
- Birth year: 1904 (attested in editions [1955, 1956, 1957, 1958])
- Appears in editions: [1955, 1956, 1957, 1958]

### Verbatim printed entry text (OCR)

**Version `col1955-L19725.v` — printed in editions [1955, 1956, 1957, 1958]:**

> BIASINI, R.—b. 1904; ed. Lyceum and Stella Maris Coll., Malta; postal clk., Malta, 1923; civ. serv. (admin.), 1926; dir. of agric., 1941; secon. to reg. protection offr., 1942-44.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | postal clk. | Malta | [1955, 1956, 1957, 1958] |
| 1 | 1926 | civ. serv. (admin.) | Malta *(inherited from previous clause)* | [1955, 1956, 1957, 1958] |
| 2 | 1941 | dir. of agric | Malta *(inherited from previous clause)* | [1955, 1956, 1957, 1958] |
| 3 | 1942–1944 | secon. to reg. protection offr | Malta *(inherited from previous clause)* | [1955, 1956, 1957, 1958] |

## Candidate stint `Biasini, R___Malta___1934`

- Staff-list name: **Biasini, R** | colony: **Malta** | listed 1934–1940 | editions [1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | R. Biasini | Clerk, 2nd Class | Agriculture | — | — |
| 1937 | R. Biasini | Clerk, 2nd Class | Agriculture | — | — |
| 1939 | R. Biasini | Clerk, 2nd Class | Agriculture | — | — |
| 1940 | R. Biasini | Clerk, 2nd Class | Agriculture | — | — |

### Deterministic checks: `biasini_r_b1904` vs `Biasini, R___Malta___1934`

- [PASS] surname_gate: bio 'BIASINI' vs stint 'Biasini, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1934, birth 1904 (age 30)
- [PASS] colony: 4 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1940
- [FAIL] position_sim: best 41 vs bar 60: 'civ. serv. (admin.)' ~ 'Clerk, 2nd Class'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Biasini, R___Malta___1949`

- Staff-list name: **Biasini, R** | colony: **Malta** | listed 1949–1957 | editions [1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. Biasini | Director of Agriculture | AGRICULTURE | — | — |
| 1950 | R. Biasini | Director of Agriculture | AGRICULTURE | — | — |
| 1951 | R. Biasini | Director of Agriculture | Agriculture | — | — |
| 1952 | R. Biasini | Director of Agriculture | Maltese Government | — | — |
| 1953 | R. Biasini | Director of Agriculture | The Maltese Government | — | — |
| 1954 | R. Biasini | Director of Agriculture | The Maltese Government | — | — |
| 1955 | R. Biasini | Director of Agriculture | THE MALTESE GOVERNMENT | — | — |
| 1956 | R. Biasini | Director of Agriculture | The Maltese Government | — | — |
| 1957 | R. Biasini | Director of Agriculture | The Maltese Government | — | — |

### Deterministic checks: `biasini_r_b1904` vs `Biasini, R___Malta___1949`

- [PASS] surname_gate: bio 'BIASINI' vs stint 'Biasini, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1949, birth 1904 (age 45)
- [PASS] colony: 4 placed event(s) resolve to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1957
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

