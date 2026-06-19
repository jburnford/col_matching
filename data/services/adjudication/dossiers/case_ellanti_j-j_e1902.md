<!-- {"case_id": "case_ellanti_j-j_e1902", "bio_ids": ["ellanti_j-j_e1902"], "stint_ids": ["Bellanti, John J___Malta___1918"]} -->
# Dossier case_ellanti_j-j_e1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Bellanti, John J___Malta___1918` is also gate-compatible with biography(ies) outside this case: ['bellanti_j-j_b1886'] (already linked elsewhere or filtered).

## Biography `ellanti_j-j_e1902`

- Printed name: **ELLANTI, J. J**
- Birth year: not printed
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L58774.v` — printed in editions [1937]:**

> ELLANTI, J. J., LL.D., Malta Univ., 1910.— 885; ed. St. Ignatius Coll., Malta; matric. place in hons. list), Malta Univ., 1902; clk., serv., Malta, 1907; mem. of coun. of govt., asst. crown advocate, Gozo, 1914; assessor axes, Malta treasy., Apr., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902 | matric. place in hons. list), Malta Univ | Malta | [1937] |
| 1 | 1907 | clk., serv. | Malta | [1937] |
| 2 | 1914 | mem. of coun. of govt., asst. crown advocate, Gozo | Malta *(inherited from previous clause)* | [1937] |
| 3 | 1923 | assessor axes, Malta treasy | Malta | [1937] |

## Candidate stint `Bellanti, John J___Malta___1918`

- Staff-list name: **Bellanti, John J** | colony: **Malta** | listed 1918–1923 | editions [1918, 1919, 1920, 1921, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | John J. Bellanti | Assistant Crown Advocate and Advocate for the Poor | Crown Lawyers | — | — |
| 1919 | John J. Bellanti | Assistant Crown Advocate and Advocate for the Poor | Crown Lawyers | — | — |
| 1920 | John J. Bellanti | Assistant Crown Advocate and Advocate for the Poor | Crown Lawyers | — | — |
| 1921 | John J. Bellanti | Assistant Crown Advocate and Advocate for the Poor | Crown Lawyers | — | — |
| 1922 | John J. Bellanti | Assistant Crown Advocate and Advocate for the Poor | Crown Lawyers | — | — |
| 1923 | John J. Bellanti | Assistant Treasury Counsel | Crown Lawyers | — | — |

### Deterministic checks: `ellanti_j-j_e1902` vs `Bellanti, John J___Malta___1918`

- [PASS] surname_gate: bio 'ELLANTI' vs stint 'Bellanti, John J' (fuzzy:1)
- [PASS] initials: bio ['J', 'J'] ~ stint ['J', 'J']
- [PASS] age_gate: stint starts 1918; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1918-1923
- [PASS] position_sim: best 66 vs bar 60: 'mem. of coun. of govt., asst. crown advocate, Gozo' ~ 'Assistant Crown Advocate and Advocate for the Poor'
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

