<!-- {"case_id": "case_carpenter_percy-tranter_e1892", "bio_ids": ["carpenter_percy-tranter_e1892"], "stint_ids": ["Carpenter, P. T___British Honduras___1894", "Carpenter___Bermuda___1878"]} -->
# Dossier case_carpenter_percy-tranter_e1892

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Carpenter___Bermuda___1878` is also gate-compatible with biography(ies) outside this case: ['carpenter_g-d-h_e1910'] (already linked elsewhere or filtered).

## Biography `carpenter_percy-tranter_e1892`

- Printed name: **CARPENTER, PERCY TRANTER**
- Birth year: not printed
- Appears in editions: [1896, 1897, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1896-L37929.v` — printed in editions [1896, 1897, 1899, 1900]:**

> CARPENTER, PERCY TRANTER, M.R.C.S. Eng., L.R.C.P. Lond. (St. Mary's Hosp., Lond.); dist. surg., Br. Honduras, 1892; ag. dist. comsurr., 1893 and 1895; asst. col. surg., 1894; dist. comsurr., 1897.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1892–1892 | dist. surg. | British Honduras | [1896, 1897, 1899, 1900] |
| 1 | 1893–1895 | ag. dist. comsurr. | — | [1896, 1897, 1899, 1900] |
| 2 | 1894–1894 | asst. col. surg. | — | [1896, 1897, 1899, 1900] |
| 3 | 1897–1897 | dist. comsurr. | — | [1896, 1897, 1899, 1900] |

## Candidate stint `Carpenter, P. T___British Honduras___1894`

- Staff-list name: **Carpenter, P. T** | colony: **British Honduras** | listed 1894–1900 | editions [1894, 1896, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | P. T. Carpenter | District Surgeon | Medical | — | — |
| 1896 | P. T. Carpenter | Assistant Colonial Surgeon | Medical | — | — |
| 1897 | P. T. Carpenter | Assistant Colonial Surgeon | Medical | — | — |
| 1898 | P. T. Carpenter | District Commissioner | District Commissioners | — | — |
| 1899 | P. T. Carpenter | District Commissioner | District Commissioners | — | — |
| 1900 | P. T. Carpenter | District Commissioner | District Commissioners | — | — |

### Deterministic checks: `carpenter_percy-tranter_e1892` vs `Carpenter, P. T___British Honduras___1894`

- [PASS] surname_gate: bio 'CARPENTER' vs stint 'Carpenter, P. T' (exact)
- [PASS] initials: bio ['P', 'T'] ~ stint ['P', 'T']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1900
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Carpenter___Bermuda___1878`

- Staff-list name: **Carpenter** | colony: **Bermuda** | listed 1878–1880 | editions [1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | Lieutenant Carpenter | Aide-de-Camp and Private Secretary | Civil Establishment | — | Lieutenant |
| 1879 | Lieutenant Carpenter | Aide-de-Camp and Private Secretary | Civil Establishment | — | — |
| 1880 | Lieutenant Carpenter | Aide-de-Camp and Private Secretary | Civil Establishment | — | Lieutenant |

### Deterministic checks: `carpenter_percy-tranter_e1892` vs `Carpenter___Bermuda___1878`

- [PASS] surname_gate: bio 'CARPENTER' vs stint 'Carpenter' (exact)
- [PASS] initials: bio ['P', 'T'] ~ stint ['?']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1880
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

