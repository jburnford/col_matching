<!-- {"case_id": "case_durie_mansergh-pace_e1875", "bio_ids": ["durie_mansergh-pace_e1875"], "stint_ids": ["Durieu, P___Canada___1877"]} -->
# Dossier case_durie_mansergh-pace_e1875

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `durie_mansergh-pace_e1875`

- Printed name: **DURIE, Mansergh Pace**
- Birth year: not printed
- Honours: L.M (1875), M.R.C.P
- Appears in editions: [1905]

### Verbatim printed entry text (OCR)

**Version `col1905-L42983.v` — printed in editions [1905]:**

> DURIE, Mansergh Pace, M.R.C.P., and L.R.C.S.I., L.M. (1875).—Ed. Academic inst., and Meath hosp., Dub.; med. offr., dist. 2, Dominica, 1875 to 1880; asst. surg., Gold Coast, 1880-1; med. offr., dist. 2, Montserrat, May, 1886; offr. mem. legis. coun., Jan., 1888; med. offr., dist. 1, and med. offr. of health, Oct., 1889; mem. exec. coun., Sept., 1895; mem. pub. lib. comtee., Oct., 1896; *x officio* mem. bd. of health,

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875–1880 | med. offr., dist. 2 | Dominica | [1905] |
| 1 | 1880–1881 | asst. surg. | Gold Coast | [1905] |
| 2 | 1886 | med. offr., dist. 2 | Montserrat | [1905] |
| 3 | 1888 | offr. mem. legis. coun | Montserrat *(inherited from previous clause)* | [1905] |
| 4 | 1889 | med. offr., dist. 1, and med. offr. of health | Montserrat *(inherited from previous clause)* | [1905] |
| 5 | 1895 | mem. exec. coun | Montserrat *(inherited from previous clause)* | [1905] |
| 6 | 1896 | mem. pub. lib. comtee | Montserrat *(inherited from previous clause)* | [1905] |

## Candidate stint `Durieu, P___Canada___1877`

- Staff-list name: **Durieu, P** | colony: **Canada** | listed 1877–1899 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | P. Durieu | Coadjutor | — | — | — |
| 1878 | P. Durieu | Coadjutor | — | — | — |
| 1879 | P. Durieu | Coadjutor | — | — | — |
| 1880 | P. Durieu | Coadjutor | — | — | — |
| 1883 | P. Durieu | Coadjutor | — | — | — |
| 1886 | P. Durieu | Rt. Rev., Coadjutor | — | — | — |
| 1888 | P. Durieu | Coadjutor | — | — | — |
| 1889 | P. Durieu | Vic. Apost. of British Columbia | Roman Catholic Church | — | — |
| 1890 | P. Durieu | Vic. Apost. of British Columbia | ROMAN CATHOLIC CHURCH. | — | — |
| 1894 | P. Durieu | Vic. Apost. of British Columbia | Roman Catholic Church | — | — |
| 1896 | P. Durieu | Coadjutor | Roman Catholic Church | — | — |
| 1897 | P. Durieu | Vic. Apost. of British Columbia | Roman Catholic Church | — | — |
| 1898 | P. Durieu | Coadjutor | Roman Catholic Church | — | — |
| 1899 | P. Durieu | Coadjutor | Roman Catholic Church | — | — |

### Deterministic checks: `durie_mansergh-pace_e1875` vs `Durieu, P___Canada___1877`

- [PASS] surname_gate: bio 'DURIE' vs stint 'Durieu, P' (fuzzy:1)
- [PASS] initials: bio ['M', 'P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1899
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

