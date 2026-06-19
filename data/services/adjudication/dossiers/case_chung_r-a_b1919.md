<!-- {"case_id": "case_chung_r-a_b1919", "bio_ids": ["chung_r-a_b1919"], "stint_ids": ["Chung, A___British Guiana___1962"]} -->
# Dossier case_chung_r-a_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `chung_r-a_b1919`

- Printed name: **CHUNG, R. A**
- Birth year: 1919 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L13826.v` — printed in editions [1966]:**

> CHUNG, R. A.—b. 1919; ed. Central High Sch.; probationer, G.R.O., Br. Guiana, 1942; cl. II clk., 1944; cl. I clk., 1948; asst. inspr. of labr., 1953; inspr. of labr., 1957; dep. comsnr. of labr., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1942 | probationer, G.R.O. | British Guiana | [1966] |
| 1 | 1944 | cl. II clk | British Guiana *(inherited from previous clause)* | [1966] |
| 2 | 1948 | cl. I clk | British Guiana *(inherited from previous clause)* | [1966] |
| 3 | 1953 | asst. inspr. of labr | British Guiana *(inherited from previous clause)* | [1966] |
| 4 | 1957 | inspr. of labr | British Guiana *(inherited from previous clause)* | [1966] |
| 5 | 1964 | dep. comsnr. of labr | British Guiana *(inherited from previous clause)* | [1966] |

## Candidate stint `Chung, A___British Guiana___1962`

- Staff-list name: **Chung, A** | colony: **British Guiana** | listed 1962–1966 | editions [1962, 1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | A. Chung | Registrar of Deeds and of Supreme Court | Civil Establishment | — | — |
| 1963 | A. Chung | Registrar of Deeds and of Supreme Court | Civil Establishment | — | — |
| 1964 | A. Chung | Puisne Judge | Judiciary | — | — |
| 1965 | A. Chung | Puisne Judge | Judiciary | — | — |
| 1966 | A. Chung | Puisne Judge | Judiciary | — | — |

### Deterministic checks: `chung_r-a_b1919` vs `Chung, A___British Guiana___1962`

- [PASS] surname_gate: bio 'CHUNG' vs stint 'Chung, A' (exact)
- [PASS] initials: bio ['R', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1962, birth 1919 (age 43)
- [PASS] colony: 6 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1962-1966
- [FAIL] position_sim: best 44 vs bar 60: 'dep. comsnr. of labr' ~ 'Registrar of Deeds and of Supreme Court'
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

