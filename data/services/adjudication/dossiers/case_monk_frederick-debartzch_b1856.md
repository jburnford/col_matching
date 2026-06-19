<!-- {"case_id": "case_monk_frederick-debartzch_b1856", "bio_ids": ["monk_frederick-debartzch_b1856"], "stint_ids": ["Monk, Frederick Debartzch___Canada___1897"]} -->
# Dossier case_monk_frederick-debartzch_b1856

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `monk_frederick-debartzch_b1856`

- Printed name: **MONK, FREDERICK DEBARTZCH**
- Birth year: 1856 (attested in editions [1912, 1913, 1914])
- Honours: D.C.L., K.C.
- Appears in editions: [1912, 1913, 1914]

### Verbatim printed entry text (OCR)

**Version `col1912-L46287.v` — printed in editions [1912, 1913, 1914]:**

> MONK, HON. FREDERICK DEBARTZCH, K.C., D.C.L.—B. 1856; ed. Montreal Coll. and McGill Univ. (Law); D.C.L. of Laval Univ.; prof. of constitutional law, Laval; schl. commsnr. of Montreal for 12 years; an advocate practising in Montreal; elec. to H. of C., Canada, at g.e., 1896; re-elec. 1900, 1904, 1908 and 1911; opposition leader for Quebec, 1901-1903; mem. of the privy council for Canada and min. of pub. wks. in Mr. Borden's cabinet, Oct., 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896–1896 | elec. to H. of C. | Canada | [1912, 1913, 1914] |
| 1 | 1900–1911 | re-elec. | — | [1912, 1913, 1914] |
| 2 | 1901–1903 | opposition leader | Quebec | [1912, 1913, 1914] |
| 3 | 1911 | mem. of the privy council and min. of pub. wks. | Canada | [1912, 1913, 1914] |
| 4 | ? | prof. of constitutional law | — | [1912, 1913, 1914] |
| 5 | ? | schl. commsnr. | — | [1912, 1913, 1914] |
| 6 | ? | advocate | — | [1912, 1913, 1914] |

## Candidate stint `Monk, Frederick Debartzch___Canada___1897`

- Staff-list name: **Monk, Frederick Debartzch** | colony: **Canada** | listed 1897–1914 | editions [1897, 1898, 1899, 1905, 1906, 1907, 1908, 1912, 1913, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | Frederick D. Monk | — | — | — | — |
| 1898 | Frederick D. Monk | — | — | — | — |
| 1899 | Frederick D. Monk | — | — | — | — |
| 1905 | Frederick D. Monk | — | — | — | — |
| 1906 | Frederick D. Monk | — | — | — | — |
| 1907 | Frederick D. Monk | — | — | — | — |
| 1908 | Frederick D. Monk | — | Province of Quebec | — | — |
| 1912 | Frederick D. Monk | Minister of Public Works | Public Works | — | — |
| 1912 | F. D. Monk | — | Treasury Board | — | — |
| 1912 | Frederick Debartzch Monk | Minister of Public Works | THE MINISTRY | — | — |
| 1913 | Frederick Debartych Monk | — | Office of the Privy Council | — | — |
| 1914 | Frederick Debartzch Monk | Privy Councillor | Privy Council | — | — |
| 1914 | Frederick Debartzch Monk | — | — | — | — |

### Deterministic checks: `monk_frederick-debartzch_b1856` vs `Monk, Frederick Debartzch___Canada___1897`

- [PASS] surname_gate: bio 'MONK' vs stint 'Monk, Frederick Debartzch' (exact)
- [PASS] initials: bio ['F', 'D'] ~ stint ['F', 'D']
- [PASS] age_gate: stint starts 1897, birth 1856 (age 41)
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1897-1914
- [FAIL] position_sim: best 50 vs bar 60: 'mem. of the privy council and min. of pub. wks.' ~ 'Privy Councillor'
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

