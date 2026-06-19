<!-- {"case_id": "case_hamp_arthur-edward_b1886", "bio_ids": ["hamp_arthur-edward_b1886"], "stint_ids": ["Hamp, A. E___Kenya___1917", "Hamp, A. E___Uganda___1920"]} -->
# Dossier case_hamp_arthur-edward_b1886

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hamp_arthur-edward_b1886`

- Printed name: **HAMP, ARTHUR EDWARD**
- Birth year: 1886 (attested in editions [1940])
- Honours: C.B.E. (1937)
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L64899.v` — printed in editions [1940]:**

> HAMP, ARTHUR EDWARD, C.B.E. (1937), A.M.I.C.E., M.Inst.C.E., M.Inst. E., B. 1886; asst. engnr., P.W.D., E.A.P., 1912; asst. engnr., Uganda rly., 1914; dist. engnr., K.U.R. & H., 1925; asst. C.E., 1928; C.E., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | asst. engnr. | East Africa Protectorate | [1940] |
| 1 | 1914 | asst. engnr. | Uganda | [1940] |
| 2 | 1925 | dist. engnr. | Kenya and Uganda | [1940] |
| 3 | 1928 | asst. C.E. | — | [1940] |

## Candidate stint `Hamp, A. E___Kenya___1917`

- Staff-list name: **Hamp, A. E** | colony: **Kenya** | listed 1917–1927 | editions [1917, 1918, 1919, 1920, 1922, 1923, 1924, 1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | A. E. Hamp | Assistant Engineer | Engineering | — | — |
| 1918 | A. E. Hamp | Assistant Engineer | Engineering | — | — |
| 1919 | A. E. Hamp | Assistant Engineer | Engineering | — | — |
| 1920 | A. E. Hamp | Assistant Engineer | Engineering | — | — |
| 1922 | A. E. Hamp | Assistant Engineers | Engineering | — | — |
| 1923 | A. E. Hamp | Assistant Engineers | Engineering | — | — |
| 1924 | A. E. Hamp | Assistant Engineer | Engineering | — | — |
| 1925 | A. E. Hamp | Assistant Engineers | Engineering | — | — |
| 1927 | A. E. Hamp | District Engineers | Engineering | — | — |

### Deterministic checks: `hamp_arthur-edward_b1886` vs `Hamp, A. E___Kenya___1917`

- [PASS] surname_gate: bio 'HAMP' vs stint 'Hamp, A. E' (exact)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1917, birth 1886 (age 31)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hamp, A. E___Uganda___1920`

- Staff-list name: **Hamp, A. E** | colony: **Uganda** | listed 1920–1923 | editions [1920, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | A. E. Hamp | Superintendent | Busoga Railway | — | — |
| 1922 | A. E. Hamp | Superintendent | Busoga Railway | — | — |
| 1923 | A. E. Hamp | Superintendent | Busoga Railway | — | — |

### Deterministic checks: `hamp_arthur-edward_b1886` vs `Hamp, A. E___Uganda___1920`

- [PASS] surname_gate: bio 'HAMP' vs stint 'Hamp, A. E' (exact)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1920, birth 1886 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1920-1923
- [FAIL] position_sim: best 42 vs bar 60: 'asst. engnr.' ~ 'Superintendent'
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

