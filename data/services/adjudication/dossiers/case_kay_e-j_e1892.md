<!-- {"case_id": "case_kay_e-j_e1892", "bio_ids": ["kay_e-j_e1892"], "stint_ids": ["Kay, E. J___South Africa___1912", "Kay, James___New South Wales___1878"]} -->
# Dossier case_kay_e-j_e1892

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kay_e-j_e1892`

- Printed name: **KAY, E. J**
- Birth year: not printed
- Appears in editions: [1918, 1920, 1921, 1922, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1918-L51832.v` — printed in editions [1918, 1920, 1921, 1922, 1923, 1924]:**

> KAY, E. J.—Impl. serv., 1892; cashier, mines dept., Transvaal, July, 1900; audit inspr., rev. dept., Feb., 1904; recvr. of rev., Johannesburg, 1911; inspr., in rev. dept., Apr., 1912; dep. comsnr., income tax off., Sept., 1914; asst. comsnr. for in. rev., Oct., 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1892 | Impl. serv | — | [1918, 1920, 1921, 1922, 1923, 1924] |
| 1 | 1900 | cashier, mines dept. | Transvaal | [1918, 1920, 1921, 1922, 1923, 1924] |
| 2 | 1904 | audit inspr., rev. dept | Transvaal *(inherited from previous clause)* | [1918, 1920, 1921, 1922, 1923, 1924] |
| 3 | 1911 | recvr. of rev., Johannesburg | Transvaal *(inherited from previous clause)* | [1918, 1920, 1921, 1922, 1923, 1924] |
| 4 | 1912 | inspr., in rev. dept | Transvaal *(inherited from previous clause)* | [1918, 1920, 1921, 1922, 1923, 1924] |
| 5 | 1914 | dep. comsnr., income tax off | Transvaal *(inherited from previous clause)* | [1918, 1920, 1921, 1922, 1923, 1924] |
| 6 | 1916 | asst. comsnr. for in. rev | Transvaal *(inherited from previous clause)* | [1918, 1920, 1921, 1922, 1923, 1924] |

## Candidate stint `Kay, E. J___South Africa___1912`

- Staff-list name: **Kay, E. J** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | E. J. Kay | Receiver of Revenue | Inland Revenue Department | — | — |
| 1914 | E. J. Kay | Inspector | Inland Revenue Department | — | — |
| 1918 | E. J. Kay | Deputy Commissioner of Taxes | Income Tax Office | — | — |
| 1918 | E. J. Kay | Assistant Commissioner | Inland Revenue Department | — | — |

### Deterministic checks: `kay_e-j_e1892` vs `Kay, E. J___South Africa___1912`

- [PASS] surname_gate: bio 'KAY' vs stint 'Kay, E. J' (exact)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E', 'J']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Kay, James___New South Wales___1878`

- Staff-list name: **Kay, James** | colony: **New South Wales** | listed 1878–1886 | editions [1878, 1879, 1880, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | James Kay | Foreman of Works | Colonial Architect's Department | — | — |
| 1879 | James Kay | Foreman of Works | Colonial Architect's Department | — | — |
| 1880 | James Kay | Foreman of Works | Colonial Architect's Department | — | — |
| 1886 | James Kay | Foreman of Works | Colonial Architect's Department | — | — |

### Deterministic checks: `kay_e-j_e1892` vs `Kay, James___New South Wales___1878`

- [PASS] surname_gate: bio 'KAY' vs stint 'Kay, James' (exact)
- [PASS] initials: bio ['E', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1886
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

