<!-- {"case_id": "case_schermbrucker_frederic_e1857", "bio_ids": ["schermbrucker_frederic_e1857"], "stint_ids": ["Schermbrucker, F___Cape of Good Hope___1878"]} -->
# Dossier case_schermbrucker_frederic_e1857

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['schermbrucker_frederic_e1857'] carry a single initial only — the namesake trap applies.

## Biography `schermbrucker_frederic_e1857`

- Printed name: **SCHERMBRUCKER, Frederic**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1897, 1899]

### Verbatim printed entry text (OCR)

**Version `col1888-L35937.v` — printed in editions [1888, 1889, 1890, 1897, 1899]:**

> SCHERMBRUCKER, The Hon. Frederic.—Lieutenant, British-German legion, during the Crimean war; came to the colony with the corps of German military settlers in 1857; represented the division of King William's Town in house of assembly in 1868; commandant during the Gaika rebellion and Gcaleka war, 1877-78, and subsequently commanded the corps of Kaffrarian riflemen during the Zulu war, 1879; organised the corps of Basutoland police at the outbreak of hostilities in Basutoland in 1880, and was appointed commandant thereto; retired from the service, 1881, and entered the legislative council as one of the representatives of the eastern circle in 1882; at the general election in 1884 again returned at the head of the poll for the eastern circle; commissioner of crown lands and public works, 1884 to 1890.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1857 | — | — | [1888, 1889, 1890, 1897, 1899] |
| 1 | 1868 | representative | King William's Town | [1888, 1889, 1890, 1897, 1899] |
| 2 | 1877 | commandant | — | [1888, 1889, 1890, 1897, 1899] |
| 3 | 1879 | commander | — | [1888, 1889, 1890, 1897, 1899] |
| 4 | 1880 | commandant | Basutoland | [1888, 1889, 1890, 1897, 1899] |
| 5 | 1881 | — | — | [1888, 1889, 1890, 1897, 1899] |
| 6 | 1882 | representative | — | [1888, 1889, 1890, 1897, 1899] |
| 7 | 1884 | — | — | [1888, 1889, 1890, 1897, 1899] |
| 8 | 1884 | commissioner of crown lands and public works | — | [1888, 1889, 1890, 1897, 1899] |
| 9 | ? | Lieutenant | — | [1888, 1889, 1890, 1897, 1899] |

## Candidate stint `Schermbrucker, F___Cape of Good Hope___1878`

- Staff-list name: **Schermbrucker, F** | colony: **Cape of Good Hope** | listed 1878–1889 | editions [1878, 1880, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | F. Schermbrucker | Clerk | DIVISION OF KING WILLIAM'S TOWN | — | — |
| 1880 | F. Schermbrucker | Clerk | Division of Cathcart | — | — |
| 1888 | Hon. F. Schermbrucker | Commissioner | Commissioner's Office | — | — |
| 1889 | F. Schermbrucker | Commissioner | Commissioner's Office | — | — |

### Deterministic checks: `schermbrucker_frederic_e1857` vs `Schermbrucker, F___Cape of Good Hope___1878`

- [PASS] surname_gate: bio 'SCHERMBRUCKER' vs stint 'Schermbrucker, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1889
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

