<!-- {"case_id": "case_kerr_j-errington_e1889", "bio_ids": ["kerr_j-errington_e1889"], "stint_ids": ["Kerr, Joseph___Canada___1877"]} -->
# Dossier case_kerr_j-errington_e1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 68 official(s) with this surname in the graph's staff lists; 23 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Kerr, Joseph___Canada___1877` is also gate-compatible with biography(ies) outside this case: ['kerr_james-kirkpatrick_b1841'] (already linked elsewhere or filtered).

## Biography `kerr_j-errington_e1889`

- Printed name: **KERR, J. ERRINGTON**
- Birth year: not printed
- Appears in editions: [1907]

### Verbatim printed entry text (OCR)

**Version `col1907-L45243.v` — printed in editions [1907]:**

> KERR, J. ERRINGTON.—M.R.C.S.(Eng.), L.R.C.P. (Lond.); house surg., gen. hosp., Birmingham; house surg., Hertford Br. hosp., Paris; house surg., homoeopathic hosp., Birmingham; asst. surg., col. hosp., Gibraltar, 1889; port surg., 1892; pol. surg., 1889; dist. surg., 1889; P.O. surg., 1902; public vaccinator, 1889; suptdg. med. offr., Jamaica, Oct., 1904; is also chmn. of quarantine bd. and central bd. of health; mem. of bd. of supervision; nom. M.L.C., 1904.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889 | asst. surg., col. hosp. | Gibraltar | [1907] |
| 1 | 1892 | port surg | Gibraltar *(inherited from previous clause)* | [1907] |
| 2 | 1902 | P.O. surg | Gibraltar *(inherited from previous clause)* | [1907] |
| 3 | 1904 | suptdg. med. offr. | Jamaica | [1907] |

## Candidate stint `Kerr, Joseph___Canada___1877`

- Staff-list name: **Kerr, Joseph** | colony: **Canada** | listed 1877–1886 | editions [1877, 1878, 1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. J. Kerr | Inspector | Customs Department | — | — |
| 1878 | J. J. Kerr | Inspector | Customs Department | — | — |
| 1879 | J. J. Kerr | Inspector | Customs Department | — | — |
| 1880 | J. J. Kerr | Inspector | Customs Department | — | — |
| 1880 | Joseph Kerr | — | — | — | — |
| 1883 | J. J. Kerr | Inspector | Customs Department | — | — |
| 1883 | Joseph Kerr | — | — | — | — |
| 1886 | Joseph Kerr | — | — | — | — |

### Deterministic checks: `kerr_j-errington_e1889` vs `Kerr, Joseph___Canada___1877`

- [PASS] surname_gate: bio 'KERR' vs stint 'Kerr, Joseph' (exact)
- [PASS] initials: bio ['J', 'E'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1886
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

