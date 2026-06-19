<!-- {"case_id": "case_cramer_j-h_e1888", "bio_ids": ["cramer_j-h_e1888"], "stint_ids": ["Cramer, J. H___Gold Coast___1894"]} -->
# Dossier case_cramer_j-h_e1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cramer_j-h_e1888`

- Printed name: **CRAMER, J. H.**
- Birth year: not printed
- Appears in editions: [1896, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1896-L38225.v` — printed in editions [1896, 1898, 1899, 1900]:**

> CRAMER, CAPT. J. H.—Capt. 3rd Batt. Higldh. L.I.; served in Roy. Canadian Milit. Inftry., 1888; apptd. to G. Coast constab., 1891; served in Atabuba expedit., 1893-4 in command of guns, and received thanks of sec. of state; gunnery instructor and intelligence offr., 1895.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1888–1888 | served in Roy. Canadian Milit. Inftry. | — | [1896, 1898, 1899, 1900] |
| 1 | 1891–1891 | constab. | Gold Coast | [1896, 1898, 1899, 1900] |
| 2 | 1893–1894 | command of guns | — | [1896, 1898, 1899, 1900] |
| 3 | 1895–1895 | gunnery instructor and intelligence offr. | — | [1896, 1898, 1899, 1900] |

## Candidate stint `Cramer, J. H___Gold Coast___1894`

- Staff-list name: **Cramer, J. H** | colony: **Gold Coast** | listed 1894–1900 | editions [1894, 1896, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | J. H. Cramer | Assistant Inspector | Constabulary | — | — |
| 1896 | J. H. Cramer | Assistant Inspector | Constabulary—Hausa | — | — |
| 1897 | J. H. Cramer | Inspector | Constabulary | — | — |
| 1898 | J. H. Cramer | Inspector | Constabulary | — | — |
| 1899 | J. H. Cramer | Inspector | Constabulary—Hausa | — | — |
| 1900 | J. H. Cramer | Inspector | Constabulary—Hausa | — | — |

### Deterministic checks: `cramer_j-h_e1888` vs `Cramer, J. H___Gold Coast___1894`

- [PASS] surname_gate: bio 'CRAMER' vs stint 'Cramer, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1900
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

