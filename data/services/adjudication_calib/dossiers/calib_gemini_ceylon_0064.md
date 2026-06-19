<!-- {"case_id": "calib_gemini_ceylon_0064", "bio_ids": ["willis_john-christopher_b1868"], "stint_ids": ["Willis, J. C___Ceylon___1898"]} -->
# Dossier calib_gemini_ceylon_0064

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 46 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `willis_john-christopher_b1868`

- Printed name: **WILLIS, JOHN CHRISTOPHER**
- Birth year: 1868 (attested in editions [1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912])
- Appears in editions: [1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912]

### Verbatim printed entry text (OCR)

**Version `col1897-L35112.v` — printed in editions [1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912]:**

> WILLIS, JOHN CHRISTOPHER, Sc.D.—B. 1868; Gonville and Caius Coll., Camb.; held for 3 years from 1890 the Frank Smart studentship for botan. research; was sen. asst. to regius prof. of botany, Glasgow Univ., and lecturer in botany, Queen Margaret's Coll., Glasgow; dir. of Royal Bot. Gardens, Ceylon, Aug., 1896; on special duty to Fed. Malay States, Mar., 1904; organising vice-pres. of Ceylon agric. soc'y.; author of "A Manual and Dictionary of the Flowering Plants and Ferns," and numerous scientific and economic papers; editor of "Annals of the Royal Botanic Gardens, Peradeniya," "Circulars and Agricultural Journal of Royal Botanic Gardens, Ceylon," and of the "Tropical Agriculturalist."

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890–1893 | Frank Smart studentship for botan. research | — | [1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 1 | 1896 | dir. of Royal Bot. Gardens | Ceylon | [1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 2 | 1904 | on special duty | Federated Malay States | [1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |

## Candidate stint `Willis, J. C___Ceylon___1898`

- Staff-list name: **Willis, J. C** | colony: **Ceylon** | listed 1898–1911 | editions [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | J. C. Willis | Director of the Royal Botanic Garden | Telegraphs | — | — |
| 1899 | J. C. Willis | Director of the Royal Botanic Garden | Telegraphs | — | — |
| 1900 | J. C. Willis | Director of the Royal Botanic Garden | Telegraphs | — | — |
| 1905 | J. C. Willis | Director of the Royal Botanic Garden | Department of Public Instruction | — | — |
| 1906 | J. C. Willis | Director of the Royal Botanic Garden | Department of Public Instruction | — | — |
| 1907 | J. C. Willis | Director of the Royal Botanic Garden | Department of Public Instruction | — | — |
| 1908 | J. C. Willis | Director of the Royal Botanic Garden | Botanic Gardens | — | — |
| 1909 | J. C. Willis | Director of the Royal Botanic Garden | Botanic Gardens | — | — |
| 1910 | J. C. Willis | Director of the Royal Botanic Garden | Botanic Gardens | — | — |
| 1911 | J. C. Willis | Director of the Royal Botanic Garden | Botanic Gardens | — | — |

### Deterministic checks: `willis_john-christopher_b1868` vs `Willis, J. C___Ceylon___1898`

- [PASS] surname_gate: bio 'WILLIS' vs stint 'Willis, J. C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1898, birth 1868 (age 30)
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1898-1911
- [PASS] position_sim: best 86 vs bar 60: 'dir. of Royal Bot. Gardens' ~ 'Director of the Royal Botanic Garden'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 3 agreeing edition-year(s) [1898, 1899, 1900] pos~86 (bar: >=2)
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

