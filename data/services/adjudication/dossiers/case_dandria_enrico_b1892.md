<!-- {"case_id": "case_dandria_enrico_b1892", "bio_ids": ["dandria_enrico_b1892"], "stint_ids": ["Dandria, E___Malta___1936"]} -->
# Dossier case_dandria_enrico_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['dandria_enrico_b1892'] carry a single initial only — the namesake trap applies.

## Biography `dandria_enrico_b1892`

- Printed name: **DANDRIA, ENRICO**
- Birth year: 1892 (attested in editions [1924, 1927, 1928, 1929, 1930, 1931, 1934])
- Honours: D.D
- Appears in editions: [1924, 1927, 1928, 1929, 1930, 1931, 1934]

### Verbatim printed entry text (OCR)

**Version `col1924-L53522.v` — printed in editions [1924, 1927, 1928, 1929, 1930, 1931, 1934]:**

> DANDRIA, HON. REV. ENRICO, B.L. Can., D.D., Ph.D.—B. 1892; ed. St. Paul's Inst., Valletta; matric. Malta Univ., 1906; B.L. Can., D.D., 1913; awarded govt. prize as first student of academical course; Ph.D., Gregorian Univ., Rome, 1915; teacher of philosophy and English lit. and prefect of studies in Archiepiscopal Seminary, Malta, 1916-19; elec. for 2nd divn. in Maltese parlmt., Oct., 1921; min. for pub. instrn., 10th July, 1923; resigned, June, 1927; re-ele. Aug., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906 | matric. Malta Univ | — | [1924, 1927, 1928, 1929, 1930, 1931, 1934] |
| 1 | 1913 | B.L. Can., D.D | — | [1924, 1927, 1928, 1929, 1930, 1931, 1934] |
| 2 | 1915 | Ph.D., Gregorian Univ., Rome | — | [1924, 1927, 1928, 1929, 1930, 1931, 1934] |
| 3 | 1916–1919 | teacher of philosophy and English lit. and prefect of studies in Archiepiscopal Seminary | Malta | [1924, 1927, 1928, 1929, 1930, 1931, 1934] |
| 4 | 1921 | elec. for 2nd divn. in Maltese parlmt | Malta *(inherited from previous clause)* | [1924, 1927, 1928, 1929, 1930, 1931, 1934] |
| 5 | 1923 | min. for pub. instrn | Malta *(inherited from previous clause)* | [1924, 1927, 1928, 1929, 1930, 1931, 1934] |
| 6 | 1927 | resigned | Malta *(inherited from previous clause)* | [1924, 1927, 1928, 1929, 1930, 1931, 1934] |

## Candidate stint `Dandria, E___Malta___1936`

- Staff-list name: **Dandria, E** | colony: **Malta** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | E. Dandria | Assistant | Hospitals, etc. | — | — |
| 1937 | E. Dandria | Assistant | Hospitals, etc. | — | — |
| 1939 | E. Dandria | Junior Resident Medical Officer | Poor House and Leprosy Hospital | — | — |
| 1940 | E. Dandria | Junior Resident Medical Officer | Poor House | — | — |

### Deterministic checks: `dandria_enrico_b1892` vs `Dandria, E___Malta___1936`

- [PASS] surname_gate: bio 'DANDRIA' vs stint 'Dandria, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1936, birth 1892 (age 44)
- [PASS] colony: 4 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 35 vs bar 60: 'resigned' ~ 'Assistant'
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

