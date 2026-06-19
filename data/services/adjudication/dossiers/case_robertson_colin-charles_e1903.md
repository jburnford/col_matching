<!-- {"case_id": "case_robertson_colin-charles_e1903", "bio_ids": ["robertson_colin-charles_e1903"], "stint_ids": ["Robertson, C. C___New Zealand___1900"]} -->
# Dossier case_robertson_colin-charles_e1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 131 official(s) with this surname in the graph's staff lists; 54 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `robertson_colin-charles_e1903`

- Printed name: **ROBERTSON, COLIN CHARLES**
- Birth year: not printed
- Honours: M.F.
- Appears in editions: [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1923-L57707.v` — printed in editions [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]:**

> ROBERTSON, COLIN CHARLES, M.F.—Probationary forest offr., O.F.S., Feb., 1903; studied forestry in Europe and at Yale Univ., 1905-07; astt. conservator of forests, O.F.S., 1907; dist. forest offr., and research offr., Pretoria, 1912; professional astt., 1917; on active service with S.A.H.A., Apr., 1917 to July, 1919; ag. conservator, forests, Eastern conservancy, 1919, Natal and Midland conservancies, 1920; resumed duties of prof. astt., Pretoria, Oct., 1920; conservator, forests, Oct., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | Probationary forest offr. | Orange Free State | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 1 | 1905–1907 | — | — | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 2 | 1907 | astt. conservator of forests | Orange Free State | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 3 | 1912 | dist. forest offr., and research offr. | Pretoria | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 4 | 1917 | professional astt. | — | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 5 | 1917–1919 | on active service with S.A.H.A. | — | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 6 | 1919–1920 | ag. conservator, forests | Natal | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 7 | 1920 | resumed duties of prof. astt. | Pretoria | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 8 | 1920 | conservator, forests | — | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |

## Candidate stint `Robertson, C. C___New Zealand___1900`

- Staff-list name: **Robertson, C. C** | colony: **New Zealand** | listed 1900–1912 | editions [1900, 1905, 1906, 1907, 1908, 1909, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1900 | C. C. Robertson | Officer in Charge of Telegraph Office | POST OFFICE AND TELEGRAPH DEPARTMENT | — | — |
| 1905 | C. C. Robertson | Inspector of Telegraphs | Post Office and Telegraph Department | — | — |
| 1906 | C. C. Robertson | Inspector of Telegraph | Post Office and Telegraph Department | — | — |
| 1907 | C. C. Robertson | Inspector of Telegraph | Post Office and Telegraph Department | — | — |
| 1908 | C. C. Robertson | Inspector of Telegraphs | Post Office and Telegraph Department | — | — |
| 1909 | C. C. Robertson | Inspector of Telegraphs | Post Office and Telegraph Department | — | — |
| 1912 | C. C. Robertson | Telegraph Engineer | Post Office and Telegraph Department | — | — |

### Deterministic checks: `robertson_colin-charles_e1903` vs `Robertson, C. C___New Zealand___1900`

- [PASS] surname_gate: bio 'ROBERTSON' vs stint 'Robertson, C. C' (exact)
- [PASS] initials: bio ['C', 'C'] ~ stint ['C', 'C']
- [PASS] age_gate: stint starts 1900; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New Zealand'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1900-1912
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

