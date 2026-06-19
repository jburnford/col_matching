<!-- {"case_id": "case_dent_e-j_e1913", "bio_ids": ["dent_e-j_e1913"], "stint_ids": ["Dent, Edward___North Borneo___1908", "Dent, Edward___St Vincent___1909"]} -->
# Dossier case_dent_e-j_e1913

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dent_e-j_e1913`

- Printed name: **DENT, E. J**
- Birth year: not printed
- Appears in editions: [1915, 1917, 1918]

### Verbatim printed entry text (OCR)

**Version `col1915-L46457.v` — printed in editions [1915, 1917, 1918]:**

> DENT, E. J.—Asst. jun. staff survr., E.A.P., June, 1914; asst. dist. consnr., Dec., 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | asst. dist. consnr | East Africa Protectorate *(inherited from previous clause)* | [1915, 1917, 1918] |
| 1 | 1914 | Asst. jun. staff survr. | East Africa Protectorate | [1915, 1917, 1918] |

## Candidate stint `Dent, Edward___North Borneo___1908`

- Staff-list name: **Dent, Edward** | colony: **North Borneo** | listed 1908–1921 | editions [1908, 1910, 1913, 1919, 1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | Edward Dent | — | Court of Directors | — | — |
| 1910 | Edward Dent | — | Court of Directors | — | — |
| 1913 | Edward Dent | Vice-Chairman | Court of Directors | — | — |
| 1919 | Edward Dent | Vice-Chairman | Court of Directors | — | — |
| 1920 | Edward Dent | Vice-President | Court of Directors | — | — |
| 1921 | Edward Dent | Vice-President | Court of Directors | — | — |

### Deterministic checks: `dent_e-j_e1913` vs `Dent, Edward___North Borneo___1908`

- [PASS] surname_gate: bio 'DENT' vs stint 'Dent, Edward' (exact)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'North Borneo'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1921
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Dent, Edward___St Vincent___1909`

- Staff-list name: **Dent, Edward** | colony: **St Vincent** | listed 1909–1911 | editions [1909, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | Edward Dent | — | Court of Directors | — | — |
| 1911 | Edward Dent | Vice-Chairman | Court of Directors | — | — |

### Deterministic checks: `dent_e-j_e1913` vs `Dent, Edward___St Vincent___1909`

- [PASS] surname_gate: bio 'DENT' vs stint 'Dent, Edward' (exact)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'St Vincent'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1911
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

