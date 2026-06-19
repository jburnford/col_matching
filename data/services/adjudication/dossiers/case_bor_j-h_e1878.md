<!-- {"case_id": "case_bor_j-h_e1878", "bio_ids": ["bor_j-h_e1878", "bor_libut-j-h_e1878"], "stint_ids": ["Bor, J. H___Cyprus___1888"]} -->
# Dossier case_bor_j-h_e1878

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Bor, J. H___Cyprus___1888'] have more than one claimant biography in this case.

## Biography `bor_j-h_e1878`

- Printed name: **BOR, J.H**
- Birth year: not printed
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L32261.v` — printed in editions [1886, 1888]:**

> BOR, LIEUT. J.H.—Local commandant of police, Cyprus, 18th Aug., 1878; adjutant, 1885; chief commandant, 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | Local commandant of police | Cyprus | [1886, 1888] |
| 1 | 1884 | chief commandant | Cyprus *(inherited from previous clause)* | [1886, 1888] |
| 2 | 1885 | adjutant | Cyprus *(inherited from previous clause)* | [1886, 1888] |

## Biography `bor_libut-j-h_e1878`

- Printed name: **BOR, LIBUT J. H**
- Birth year: not printed
- Appears in editions: [1890]

### Verbatim printed entry text (OCR)

**Version `col1890-L32726.v` — printed in editions [1890]:**

> BOR, LIBUT J. H.—Local commandant of police, Cyprus, 18th Aug., 1878; adjutant, 1888; chief commandant, 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | Local commandant of police | Cyprus | [1890] |
| 1 | 1884 | chief commandant | Cyprus *(inherited from previous clause)* | [1890] |
| 2 | 1888 | adjutant | Cyprus *(inherited from previous clause)* | [1890] |

## Candidate stint `Bor, J. H___Cyprus___1888`

- Staff-list name: **Bor, J. H** | colony: **Cyprus** | listed 1888–1890 | editions [1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | J. H. Bor | Chief Commandant and Inspector of Prisons | Police | — | Captain |
| 1889 | J. H. Bor | Chief Commandant and Inspector of Prisons | Police | — | Captain |
| 1890 | Capt. J. H. Bor | Chief Commandant and Inspector of Prisons | Police | — | Captain |

### Deterministic checks: `bor_j-h_e1878` vs `Bor, J. H___Cyprus___1888`

- [PASS] surname_gate: bio 'BOR' vs stint 'Bor, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1890
- [FAIL] position_sim: best 20 vs bar 60: 'adjutant' ~ 'Chief Commandant and Inspector of Prisons'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

### Deterministic checks: `bor_libut-j-h_e1878` vs `Bor, J. H___Cyprus___1888`

- [PASS] surname_gate: bio 'BOR' vs stint 'Bor, J. H' (exact)
- [PASS] initials: bio ['L', 'J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1888-1890
- [PASS] position_sim: best 100 vs bar 60: 'chief commandant' ~ 'Chief Commandant and Inspector of Prisons'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

