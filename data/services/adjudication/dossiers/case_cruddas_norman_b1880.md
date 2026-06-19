<!-- {"case_id": "case_cruddas_norman_b1880", "bio_ids": ["cruddas_norman_b1880"], "stint_ids": ["Cruddas, N___South Africa___1912"]} -->
# Dossier case_cruddas_norman_b1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['cruddas_norman_b1880'] carry a single initial only — the namesake trap applies.

## Biography `cruddas_norman_b1880`

- Printed name: **CRUDDAS, NORMAN**
- Birth year: 1880 (attested in editions [1917, 1918])
- Appears in editions: [1917, 1918]

### Verbatim printed entry text (OCR)

**Version `col1917-L48854.v` — printed in editions [1917, 1918]:**

> CRUDDAS, NORMAN.—B. 1880; ed. Sutton Valence, Kent; served in S. African war, 1901-2; Zululand rebellions, 1906; German S.W. Africa campaign, 1914-15; entd. Swaziland civ. serv., 1st May, 1910; asst. acctnt., 1st Apr., 1914.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901–1902 | served in S. African war | — | [1917, 1918] |
| 1 | 1906 | Zululand rebellions | Zululand | [1917, 1918] |
| 2 | 1910 | entd. Swaziland civ. serv | Zululand *(inherited from previous clause)* | [1917, 1918] |
| 3 | 1914–1915 | German S.W. Africa campaign | Zululand *(inherited from previous clause)* | [1917, 1918] |

## Candidate stint `Cruddas, N___South Africa___1912`

- Staff-list name: **Cruddas, N** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | N. Cruddas | Clerk | Establishment | — | — |
| 1914 | N. Cruddas | Clerk | Swaziland Administration Establishment | — | — |
| 1918 | N. Cruddas | Assistant Accountant | Swaziland Administration Establishment | — | — |

### Deterministic checks: `cruddas_norman_b1880` vs `Cruddas, N___South Africa___1912`

- [PASS] surname_gate: bio 'CRUDDAS' vs stint 'Cruddas, N' (exact)
- [PASS] initials: bio ['N'] ~ stint ['N']
- [PASS] age_gate: stint starts 1912, birth 1880 (age 32)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

