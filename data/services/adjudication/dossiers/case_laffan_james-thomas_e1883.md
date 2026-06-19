<!-- {"case_id": "case_laffan_james-thomas_e1883", "bio_ids": ["laffan_james-thomas_e1883"], "stint_ids": ["Laffan, J. T___Western Australia___1889"]} -->
# Dossier case_laffan_james-thomas_e1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `laffan_james-thomas_e1883`

- Printed name: **LAFFAN, James Thomas**
- Birth year: not printed
- Honours: L.K, L.R.C.S.I
- Appears in editions: [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905]

### Verbatim printed entry text (OCR)

**Version `col1890-L35152.v` — printed in editions [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905]:**

> LAFFAN, James Thomas, L.R.C.S.I., L.K., and Q.C.P.I., &c.—Asst.-col. surgeon, Larneac, Cyprus, 1883; resident medical officer, Wyndham, New South Australia, 1886; acting R.M., Wyndham, 1887; resident medical officer, Bunbury, 1889; police magistrate, Blackwood, 1889.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Asst.-col. surgeon, Larneac | Cyprus | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905] |
| 1 | 1886 | resident medical officer, Wyndham, New South Australia | Cyprus *(inherited from previous clause)* | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905] |
| 2 | 1887 | acting R.M., Wyndham | Cyprus *(inherited from previous clause)* | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905] |
| 3 | 1889 | resident medical officer, Bunbury | Cyprus *(inherited from previous clause)* | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905] |

## Candidate stint `Laffan, J. T___Western Australia___1889`

- Staff-list name: **Laffan, J. T** | colony: **Western Australia** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | J. T. Laffan | District Medical Officer | Medical Department | — | — |
| 1890 | J. T. Laffan | Police Magistrate | Judicial Department | — | — |
| 1890 | J. T. Laffan | District Medical Officer | Medical Department | — | — |

### Deterministic checks: `laffan_james-thomas_e1883` vs `Laffan, J. T___Western Australia___1889`

- [PASS] surname_gate: bio 'LAFFAN' vs stint 'Laffan, J. T' (exact)
- [PASS] initials: bio ['J', 'T'] ~ stint ['J', 'T']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Western Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1890
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

