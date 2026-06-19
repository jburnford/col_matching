<!-- {"case_id": "case_wynne-jones_edward-irvine_b1898", "bio_ids": ["wynne-jones_edward-irvine_b1898"], "stint_ids": ["Wynne-Jones, E. I___Hong Kong___1924"]} -->
# Dossier case_wynne-jones_edward-irvine_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Wynne-Jones, E. I___Hong Kong___1924` is also gate-compatible with biography(ies) outside this case: ['wynne-jones_edward-irvine_b1895'] (already linked elsewhere or filtered).

## Biography `wynne-jones_edward-irvine_b1898`

- Printed name: **WYNNE-JONES, EDWARD IRVINE**
- Birth year: 1898 (attested in editions [1937])
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L66031.v` — printed in editions [1937]:**

> WYNNE-JONES, EDWARD IRVINE.—B. 1898; ed. Oxford Univ. of Wales; cadet, Hong Kong, July, 1919; secretariat, Nov., 1922; passed final exam., Feb., 1923; insp., May, 1923; ditto, South, Dec., 1923; secretariat, July, 1928; pol. mag., extra asst. col. sec., Nov., 1928; sec. and clk. of comrs., in 1929; North, 1930; 2nd pol. mag., Nov., 1930; pol. mag., Keruwa, 1931-33.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | cadet | Hong Kong | [1937] |
| 1 | 1922 | secretariat | Hong Kong *(inherited from previous clause)* | [1937] |
| 2 | 1923 | passed final exam | Hong Kong *(inherited from previous clause)* | [1937] |
| 3 | 1928 | secretariat | Hong Kong *(inherited from previous clause)* | [1937] |
| 4 | 1929 | sec. and clk. of comrs., in | Hong Kong *(inherited from previous clause)* | [1937] |
| 5 | 1930 | North | Hong Kong *(inherited from previous clause)* | [1937] |
| 6 | 1931–1933 | pol. mag., Keruwa | Hong Kong *(inherited from previous clause)* | [1937] |

## Candidate stint `Wynne-Jones, E. I___Hong Kong___1924`

- Staff-list name: **Wynne-Jones, E. I** | colony: **Hong Kong** | listed 1924–1940 | editions [1924, 1925, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | E. I. Wynne-Jones | District Officer, North | District Offices | — | — |
| 1925 | E. I. Wynne-Jones | District Officer, North | District Offices | — | — |
| 1928 | E. I. Wynne-Jones | District Officer | Cadet Officers | — | — |
| 1929 | E. I. Wynne-Jones | — | Cadet Officers | — | — |
| 1930 | E. I. Wynne-Jones | — | Cadet Officers | — | — |
| 1931 | E. I. Wynne-Jones | District Officer | Cadet Officers | — | — |
| 1932 | E. I. Wynne-Jones | on leave | Cadet Officers | — | — |
| 1933 | E. I. Wynne-Jones | 2nd Police Magistrate | Civil Establishment | — | — |
| 1934 | E. I. Wynne-Jones | 2nd Police Magistrate | Cadet Officers | — | — |
| 1937 | E. I. Wynne-Jones | Cadet Officer | Civil Establishment | — | — |
| 1939 | E. I. Wynne-Jones | Postmaster-General | Cadet Officers | — | — |
| 1940 | E. I. Wynne-Jones | Postmaster-General | Cadet Officers | — | — |

### Deterministic checks: `wynne-jones_edward-irvine_b1898` vs `Wynne-Jones, E. I___Hong Kong___1924`

- [PASS] surname_gate: bio 'WYNNE-JONES' vs stint 'Wynne-Jones, E. I' (exact)
- [PASS] initials: bio ['E', 'I'] ~ stint ['E', 'I']
- [PASS] age_gate: stint starts 1924, birth 1898 (age 26)
- [PASS] colony: 7 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 6 event tenure(s) overlap stint years 1924-1940
- [PASS] position_sim: best 100 vs bar 60: 'North' ~ 'District Officer, North'
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

