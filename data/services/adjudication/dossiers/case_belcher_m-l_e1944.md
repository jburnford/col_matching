<!-- {"case_id": "case_belcher_m-l_e1944", "bio_ids": ["belcher_m-l_e1944"], "stint_ids": ["Belcher, Mary___South Australia___1888"]} -->
# Dossier case_belcher_m-l_e1944

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `belcher_m-l_e1944`

- Printed name: **BELCHER, M. L**
- Birth year: not printed
- Honours: M.B.E
- Appears in editions: [1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1957-L21025.v` — printed in editions [1957, 1958, 1959]:**

> BELCHER, Miss M. L., M.B.E.—ed. Badminton Sch. and London Univ.; social welfare offr., Pal., 1944; Nig., 1948; E. Nig.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | social welfare offr. | Palestine | [1957, 1958, 1959] |
| 1 | 1948 | social welfare offr. | Nigeria | [1957, 1958, 1959] |

## Candidate stint `Belcher, Mary___South Australia___1888`

- Staff-list name: **Belcher, Mary** | colony: **South Australia** | listed 1888–1894 | editions [1888, 1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | Mary Belcher | Head Mistress | Flinders Street Public School | — | — |
| 1889 | Mary Belcher | Head Mistress | Flinders Street Public School | — | — |
| 1890 | Mary Belcher | Head Mistress | Flinders Street Public School | — | — |
| 1894 | Mary Belcher | Head Mistress | Flinders Street Public School | — | — |

### Deterministic checks: `belcher_m-l_e1944` vs `Belcher, Mary___South Australia___1888`

- [PASS] surname_gate: bio 'BELCHER' vs stint 'Belcher, Mary' (exact)
- [PASS] initials: bio ['M', 'L'] ~ stint ['M']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1894
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

