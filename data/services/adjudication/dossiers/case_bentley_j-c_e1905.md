<!-- {"case_id": "case_bentley_j-c_e1905", "bio_ids": ["bentley_j-c_e1905"], "stint_ids": ["Bentley, J. C___Kenya___1909"]} -->
# Dossier case_bentley_j-c_e1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Bentley, J. C___Kenya___1909` is also gate-compatible with biography(ies) outside this case: ['bentley_j-c_e1905-2'] (already linked elsewhere or filtered).

## Biography `bentley_j-c_e1905`

- Printed name: **BENTLEY, J. C**
- Birth year: not printed
- Appears in editions: [1910, 1911]

### Verbatim printed entry text (OCR)

**Version `col1910-L44259.v` — printed in editions [1910, 1911]:**

> BENTLEY, J. C.—Inspr. of pol., E.A.P., Feb., 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1905 | Inspr. of pol. | East Africa Protectorate | [1910, 1911] |

## Candidate stint `Bentley, J. C___Kenya___1909`

- Staff-list name: **Bentley, J. C** | colony: **Kenya** | listed 1909–1925 | editions [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1920, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | J. C. Bentley | Assistant District Superintendent | Police | — | — |
| 1910 | J. C. Bentley | Assistant District Superintendent | Police | — | — |
| 1911 | J. C. Bentley | Assistant District Superintendent | Police | — | — |
| 1912 | J. C. Bentley | Superintendents | Police | — | — |
| 1913 | J. C. Bentley | Superintendent | Police | — | — |
| 1914 | J. C. Bentley | Superintendent | Police | — | — |
| 1915 | J. C. Bentley | Superintendent | Police | — | — |
| 1917 | J. C. Bentley | Superintendents | Police | — | — |
| 1918 | J. C. Bentley | Superintendents | Police | — | — |
| 1920 | J. C. Bentley | Superintendent | Police | — | — |
| 1922 | J. C. Bentley | Superintendent | Police | — | — |
| 1923 | J. C. Bentley | Superintendent | Police | — | — |
| 1924 | J. C. Bentley | Assistant Commissioner | Police | — | — |
| 1925 | J. C. Bentley | Assistant Commissioner | Police Department | — | — |

### Deterministic checks: `bentley_j-c_e1905` vs `Bentley, J. C___Kenya___1909`

- [PASS] surname_gate: bio 'BENTLEY' vs stint 'Bentley, J. C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1909-1925
- [FAIL] position_sim: best 29 vs bar 60: 'Inspr. of pol.' ~ 'Assistant Commissioner'
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

