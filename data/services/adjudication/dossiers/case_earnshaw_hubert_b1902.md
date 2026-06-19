<!-- {"case_id": "case_earnshaw_hubert_b1902", "bio_ids": ["earnshaw_hubert_b1902"], "stint_ids": ["Earnshaw, H___Sarawak___1949", "Earnshaw, H___Sierra Leone___1939"]} -->
# Dossier case_earnshaw_hubert_b1902

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['earnshaw_hubert_b1902'] carry a single initial only — the namesake trap applies.

## Biography `earnshaw_hubert_b1902`

- Printed name: **EARNSHAW, Hubert**
- Birth year: 1902 (attested in editions [1953, 1956])
- Honours: O.B.E
- Appears in editions: [1949, 1953, 1956]

### Verbatim printed entry text (OCR)

**Version `col1953-L17210.v` — printed in editions [1953, 1956]:**

> EARNSHAW, H., O.B.E.—b. 1902; ed. Archbishop Holgates Sch., York, and Leeds Univ.; agric. schmstr., Nig., 1928; educ. offr., Ken., 1934; S.L., 1938; senr. educ. offr., Ken., 1945; educ. advsr., Sarawak, 1947; dir., educ., 1948.

**Version `col1949-L31774.v` — printed in editions [1949]:**

> EARNSHAW, Hubert, M.Sc. (Leeds).—b. 1902; ed. Archbishop Holgates Sch., York and Leeds Univ., dip. of educ. (Leeds), bd. of educ. teacher's cert.; agric. schmstr., Nig., 1928; educ. offr., Ken., 1934; S.L., 1938; senr. educ. offr., Ken., 1945; educ. advsr., Sarawak, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | agric. schmstr. | Nigeria | [1949, 1953, 1956] |
| 1 | 1938 | agric. schmstr. | Sierra Leone | [1949, 1953, 1956] |
| 2 | 1945 | senr. educ. offr. | Kenya | [1949, 1953, 1956] |
| 3 | 1948 | dir., educ | Kenya *(inherited from previous clause)* | [1953, 1956] |

## Candidate stint `Earnshaw, H___Sarawak___1949`

- Staff-list name: **Earnshaw, H** | colony: **Sarawak** | listed 1949–1955 | editions [1949, 1950, 1951, 1952, 1953, 1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | H. Earnshaw | Director of Education | Education | — | — |
| 1950 | H. Earnshaw | Director of Education | Education | — | — |
| 1951 | H. Earnshaw | Director of Education | Education | — | — |
| 1952 | H. Earnshaw | Director of Education | Civil Establishment | — | — |
| 1953 | H. Earnshaw | Director of Education | Civil Establishment | — | — |
| 1954 | H. Earnshaw | Director of Education | Civil Establishment | O.B.E. | — |
| 1955 | H. Earnshaw | Director of Education | Civil Establishment | — | — |

### Deterministic checks: `earnshaw_hubert_b1902` vs `Earnshaw, H___Sarawak___1949`

- [PASS] surname_gate: bio 'EARNSHAW' vs stint 'Earnshaw, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1949, birth 1902 (age 47)
- [FAIL] colony: no placed event resolves to 'Sarawak'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1955
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: O.B.E
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Earnshaw, H___Sierra Leone___1939`

- Staff-list name: **Earnshaw, H** | colony: **Sierra Leone** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | H. Earnshaw | Education Officer | Education | — | — |
| 1940 | H. Earnshaw | Education Officers | Education | — | — |

### Deterministic checks: `earnshaw_hubert_b1902` vs `Earnshaw, H___Sierra Leone___1939`

- [PASS] surname_gate: bio 'EARNSHAW' vs stint 'Earnshaw, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1939, birth 1902 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 33 vs bar 60: 'agric. schmstr.' ~ 'Education Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

