<!-- {"case_id": "case_huggins_p-t_e1869", "bio_ids": ["huggins_p-t_e1869"], "stint_ids": ["Huggins, P. T___Leeward Islands___1877", "Huggins, P. T___St Christopher and Nevis___1888"]} -->
# Dossier case_huggins_p-t_e1869

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `huggins_p-t_e1869`

- Printed name: **HUGGINS, P. T.**
- Birth year: not printed
- Appears in editions: [1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1896-L39561.v` — printed in editions [1896, 1897, 1898, 1899]:**

> HUGGINS, P. T. M.D., Univ. Pennsylvania, U.S.A.; dist. med. offr. No. 9, Nevis, Nov., 1869; chairman bd. of Quarantine and memb. bd. of health.

**Version `col1900-L35570.v` — printed in editions [1900]:**

> HUGGINS, P. T., M.D., UNIV. PENNSYLVANIA, U.S.A.; DIST. MED. OFFR. NO. 9, NEVIS, NOV., 1869; CHMN. BD. OF QUARANTINE AND MEM. BD. OF HEALTH.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | dist. med. offr. No. 9 | Nevis | [1896, 1897, 1898, 1899, 1900] |

## Candidate stint `Huggins, P. T___Leeward Islands___1877`

- Staff-list name: **Huggins, P. T** | colony: **Leeward Islands** | listed 1877–1889 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | P. T. Huggins | Justice of the Peace | Justices of the Peace | — | — |
| 1877 | P. T. Huggins | — | Legislative Assembly | — | — |
| 1877 | P. T. Huggins | Medical Officer, District 3 | Board of Health | — | — |
| 1877 | P. T. Huggins | Coroner | Judicial Establishment | — | — |
| 1878 | P. T. Huggins | Medical Officer No. 3 | Board of Health | — | — |
| 1878 | P. T. Huggins | Coroner | Judicial Establishment | — | — |
| 1879 | P. T. Huggins | Medical Officer No. 3 | Board of Health | — | — |
| 1879 | P. T. Huggins | Justice of the Peace | Justices of the Peace | — | — |
| 1879 | P. T. Huggins | Coroners (paid by fees) | Judicial Establishment | — | — |
| 1880 | P. T. Huggins | Coroners (paid by fees) | Judicial Establishment | — | — |
| 1880 | P. T. Huggins | Medical Officer, No. 3 District | Board of Health | — | — |
| 1880 | P. T. Huggins | Justice of the Peace | Justices of the Peace | — | — |
| 1883 | P. T. Huggins | Medical Officer, No. 3 | Medical Officers | — | — |
| 1886 | P. T. Huggins | Medical Officer No. 3 District | Board of Health (Nevis) | — | — |
| 1889 | P. T. Huggins | No. 3 District | Board of Health (Nevis) | — | — |

### Deterministic checks: `huggins_p-t_e1869` vs `Huggins, P. T___Leeward Islands___1877`

- [PASS] surname_gate: bio 'HUGGINS' vs stint 'Huggins, P. T' (exact)
- [PASS] initials: bio ['P', 'T'] ~ stint ['P', 'T']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1889
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Huggins, P. T___St Christopher and Nevis___1888`

- Staff-list name: **Huggins, P. T** | colony: **St Christopher and Nevis** | listed 1888–1896 | editions [1888, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | P. T. Huggins | 3 | Medical Officers (Nevis) | — | — |
| 1894 | P. T. Huggins | Medical Officer | Medical Officers (Nevis) | — | — |
| 1896 | P. T. Huggins | District Medical Officer, Nevis | District Medical Officers | — | — |

### Deterministic checks: `huggins_p-t_e1869` vs `Huggins, P. T___St Christopher and Nevis___1888`

- [PASS] surname_gate: bio 'HUGGINS' vs stint 'Huggins, P. T' (exact)
- [PASS] initials: bio ['P', 'T'] ~ stint ['P', 'T']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'St Christopher and Nevis'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1896
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

