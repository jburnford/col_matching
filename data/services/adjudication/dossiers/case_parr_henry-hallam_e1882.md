<!-- {"case_id": "case_parr_henry-hallam_e1882", "bio_ids": ["parr_henry-hallam_e1882"], "stint_ids": ["Parr, H. Hallam___Cape of Good Hope___1878"]} -->
# Dossier case_parr_henry-hallam_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `parr_henry-hallam_e1882`

- Printed name: **PARR, Henry Hallam**
- Birth year: not printed
- Honours: C.M.G. (1889)
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1888-L35416.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897]:**

> PARR, Lt.-Col. Henry Hallam, C.M.G. (1889).—Military secretary to Sir B. Eyre at the Cape; served in the Egyptian expedition, 1882; deputy assistant adjt. and quartermaster-general, 1882, A.D.C. to Her Majesty.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882–1882 | — | Egypt | [1888, 1889, 1890, 1894, 1896, 1897] |
| 1 | 1882–1882 | deputy assistant adjt. and quartermaster-general | — | [1888, 1889, 1890, 1894, 1896, 1897] |
| 2 | ? | Military secretary to Sir B. Eyre | Cape Colony | [1888, 1889, 1890, 1894, 1896, 1897] |
| 3 | ? | A.D.C. to Her Majesty | — | [1888, 1889, 1890, 1894, 1896, 1897] |

## Candidate stint `Parr, H. Hallam___Cape of Good Hope___1878`

- Staff-list name: **Parr, H. Hallam** | colony: **Cape of Good Hope** | listed 1878–1880 | editions [1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | Lieut. H. Hallam Parr | Colonial Aide-de-Camp and Acting Military Secretary to His Excellency the Governor | Civil Establishment | — | — |
| 1879 | Capt. H. Hallam Parr | Colonial Aide-de-Camp and Acting Military Secretary to His Excellency the Governor | Civil Establishment | — | Captain |
| 1880 | Major H. Hallam Parr | Colonial Aide-de-Camp and Military Secretary to the Governor | Governor's Establishment | — | Major |

### Deterministic checks: `parr_henry-hallam_e1882` vs `Parr, H. Hallam___Cape of Good Hope___1878`

- [PASS] surname_gate: bio 'PARR' vs stint 'Parr, H. Hallam' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H', 'H']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
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

