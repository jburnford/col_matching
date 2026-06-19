<!-- {"case_id": "case_faille_edward-anthony_e1866", "bio_ids": ["faille_edward-anthony_e1866"], "stint_ids": ["Faille, Edward A___Leeward Islands___1883"]} -->
# Dossier case_faille_edward-anthony_e1866

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `faille_edward-anthony_e1866`

- Printed name: **FAILLE, EDWARD ANTHONY**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1883-L27384.v` — printed in editions [1883, 1886]:**

> FAILLE, EDWARD ANTHONY.—Clerk to the revenue department, St. Kitts, 1866; clerk to the treasury, St. Kitts, 1866; clerk to the water commissioners and civil engineer, St. Kitts, 1872; acting treasurer and comptroller of revenue and shipping master, Antigua, 1873; magistrate for District G., Dominica, June, 1874; member of the local legislative assembly, Dominica, 1877; member of the general legislative council of the Leeward Islands, 1877; magistrate for District F., Dominica, January, 1878.

**Version `col1888-L33324.v` — printed in editions [1888]:**

> FAILLE, EDWARD ANTHONY.—Clerk, treasury, St. Kitts, 1866; clerk to the water commissioners and civil engineer, 1872; acting treasurer, comptroller of revenue, and shipping master, and member of council, Antigua, 1873; magistrate for District G., Dominica, June, 1874; member legislative assembly, 1877; member general legislative council Leeward Islands, 1877; magistrate for District P., Dominica, Jan., 1878; magistrate, Nevis, and member general and legislative councils, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | Clerk to the revenue department | St. Kitts | [1883, 1886, 1888] |
| 1 | 1872 | clerk to the water commissioners and civil engineer | St. Kitts | [1883, 1886, 1888] |
| 2 | 1873 | acting treasurer and comptroller of revenue and shipping master | Antigua | [1883, 1886, 1888] |
| 3 | 1874 | magistrate for District G. | Dominica | [1883, 1886, 1888] |
| 4 | 1877 | member of the local legislative assembly | Dominica | [1883, 1886, 1888] |
| 5 | 1878 | magistrate for District F. | Dominica | [1883, 1886, 1888] |
| 6 | 1883 | magistrate, Nevis, and member general and legislative councils | Dominica *(inherited from previous clause)* | [1888] |

## Candidate stint `Faille, Edward A___Leeward Islands___1883`

- Staff-list name: **Faille, Edward A** | colony: **Leeward Islands** | listed 1883–1886 | editions [1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | E. A. Faille | Crown Nominee | Legislative Assembly | — | — |
| 1886 | Edward A. Faille | Magistrate and Coroner for Nevis | Judicial Establishment | — | — |
| 1886 | E. A. Faille | Director | Poor Asylum | — | — |

### Deterministic checks: `faille_edward-anthony_e1866` vs `Faille, Edward A___Leeward Islands___1883`

- [PASS] surname_gate: bio 'FAILLE' vs stint 'Faille, Edward A' (exact)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1886
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

