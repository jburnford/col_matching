<!-- {"case_id": "case_mahon_hugh_e1901", "bio_ids": ["mahon_hugh_e1901"], "stint_ids": ["Mahon, H___Commonwealth Of Australia___1905"]} -->
# Dossier case_mahon_hugh_e1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mahon_hugh_e1901'] carry a single initial only — the namesake trap applies.

## Biography `mahon_hugh_e1901`

- Printed name: **MAHON, HUGH**
- Birth year: not printed
- Terminal: resigned 1916 — “resig., 14th Nov., 1916.”
- Appears in editions: [1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1917-L51613.v` — printed in editions [1917, 1918, 1919]:**

> MAHON, HON. HUGH.—Mem., H. of R., C. of A., general elections, 1901, 1903, 1906, 1910; at by-election, 1913, and general election, 1914; postmr.-gen., Apr. to Aug., 1904; mem. select comte. on Ocean Shipping Services, 1905, and of royal comsrs. on same, 1906; min. for home affairs, Nov., 1908 to June, 1909; mem. royal comsrs. on Pearlring Industry, 1912-13; asst. min. for external affairs, Sept., to Dec., 1914; min. for external affairs, Dec., 1914; resig., 14th Nov., 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901–1910 | Mem., H. of R. | Commonwealth of Australia | [1917, 1918, 1919] |
| 1 | 1904–1904 | postmr.-gen. | — | [1917, 1918, 1919] |
| 2 | 1905–1906 | mem. select comte. on Ocean Shipping Services, and of royal comsrs. on same | — | [1917, 1918, 1919] |
| 3 | 1908–1909 | min. for home affairs | — | [1917, 1918, 1919] |
| 4 | 1912–1913 | mem. royal comsrs. on Pearlring Industry | — | [1917, 1918, 1919] |
| 5 | 1913–1914 | — | — | [1917, 1918, 1919] |
| 6 | 1914–1914 | asst. min. for external affairs | — | [1917, 1918, 1919] |

## Candidate stint `Mahon, H___Commonwealth Of Australia___1905`

- Staff-list name: **Mahon, H** | colony: **Commonwealth Of Australia** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | H. Mahon | — | — | — | — |
| 1907 | Hon. H. Mahon | — | — | — | — |

### Deterministic checks: `mahon_hugh_e1901` vs `Mahon, H___Commonwealth Of Australia___1905`

- [PASS] surname_gate: bio 'MAHON' vs stint 'Mahon, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Commonwealth Of Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1907
- [FAIL] position_sim: no overlapping placed event to compare
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

