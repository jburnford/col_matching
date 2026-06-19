<!-- {"case_id": "case_verret_hector-bacon_b1874", "bio_ids": ["verret_hector-bacon_b1874"], "stint_ids": ["Verret, H. B___Canada___1912"]} -->
# Dossier case_verret_hector-bacon_b1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `verret_hector-bacon_b1874`

- Printed name: **VERRET, HECTOR BACON**
- Birth year: 1874 (attested in editions [1921, 1922])
- Honours: D.S.O. (1916)
- Appears in editions: [1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1921-L60642.v` — printed in editions [1921, 1922]:**

> VERRET, Lieut.-Colonel HECTOR BACON, D.S.O. (1916).—B. 1874; ed., Levis Coll., Laval Univ., Queb.; priv. sec. to Sir Chas. Fitzpatrick, 1898-1902; Hon. G. H. Carroll, 1902-04; Hon. Rodolphe Lemieux, 1904-06, successive solrs.-gen. of Can.; Hon. Rodolphe Lemieux, P.M.G., Can., 1906-11; asst. dep. P.M.G., Canada, since 1911; lieut., gov. gen's. foot guards, Ottawa, 1906-08; capt., 1908; major, 1915; went overseas with 2nd batt., 1st Canadian cont. as capt., 1914; promoted major in the field, 1915; mentioned in despatches.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898–1902 | priv. sec. to Sir Chas. Fitzpatrick | — | [1921, 1922] |
| 1 | 1902–1904 | priv. sec. to Hon. G. H. Carroll | — | [1921, 1922] |
| 2 | 1904–1906 | priv. sec. to Hon. Rodolphe Lemieux | Canada | [1921, 1922] |
| 3 | 1906–1911 | priv. sec. to Hon. Rodolphe Lemieux, P.M.G. | Canada | [1921, 1922] |
| 4 | 1906–1908 | lieut., gov. gen's. foot guards | Ottawa | [1921, 1922] |
| 5 | 1908–1908 | capt. | — | [1921, 1922] |
| 6 | 1911 | asst. dep. P.M.G. | Canada | [1921, 1922] |
| 7 | 1914–1914 | capt. | Canada | [1921, 1922] |
| 8 | 1915–1915 | major | — | [1921, 1922] |

## Candidate stint `Verret, H. B___Canada___1912`

- Staff-list name: **Verret, H. B** | colony: **Canada** | listed 1912–1918 | editions [1912, 1913, 1914, 1915, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | H. B. Verret | Assistant Deputy Postmaster-General | Post Office Department | — | — |
| 1913 | H. B. Verret | Assistant Deputy Postmaster-General | Post Office Department | — | — |
| 1914 | H. B. Verret | Assistant Deputy Postmaster-General | POST OFFICE DEPARTMENT | — | — |
| 1915 | H. B. Verret | Assistant Deputy Postmaster-General | Post Office Department | — | — |
| 1918 | H. B. Verret | Assistant Deputy Postmaster-General | Post Office Department | — | — |

### Deterministic checks: `verret_hector-bacon_b1874` vs `Verret, H. B___Canada___1912`

- [PASS] surname_gate: bio 'VERRET' vs stint 'Verret, H. B' (exact)
- [PASS] initials: bio ['H', 'B'] ~ stint ['H', 'B']
- [PASS] age_gate: stint starts 1912, birth 1874 (age 38)
- [PASS] colony: 4 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1912-1918
- [FAIL] position_sim: best 52 vs bar 60: 'asst. dep. P.M.G.' ~ 'Assistant Deputy Postmaster-General'
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

