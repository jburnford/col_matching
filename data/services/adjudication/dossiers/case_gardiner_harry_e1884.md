<!-- {"case_id": "case_gardiner_harry_e1884", "bio_ids": ["gardiner_harry_e1884"], "stint_ids": ["Gardiner, H. H___Ceylon___1919"]} -->
# Dossier case_gardiner_harry_e1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gardiner_harry_e1884'] carry a single initial only — the namesake trap applies.

## Biography `gardiner_harry_e1884`

- Printed name: **GARDINER, HARRY**
- Birth year: not printed
- Appears in editions: [1900]

### Verbatim printed entry text (OCR)

**Version `col1900-L35046.v` — printed in editions [1900]:**

> GARDINER, HARRY.—Major (ret.) Roy. Scots; served in Bechuanaland expdn., 1884, and Zululand, 1888; ag. col. sec. and rec.-gen., St. Helena, 1886-7; ag. treas., Zululand, 1890; confirmed, 1891; acting, offr. for prov. of Zululand, 1897.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1884 | served in Bechuanaland expdn | — | [1900] |
| 1 | 1886–1887 | ag. col. sec. and rec.-gen. | St. Helena | [1900] |
| 2 | 1888 | served in Bechuanaland expdn | Zululand | [1900] |
| 3 | 1890 | ag. treas. | Zululand | [1900] |
| 4 | 1891 | confirmed | Zululand *(inherited from previous clause)* | [1900] |
| 5 | 1897 | acting, offr. for prov. of Zululand | Zululand *(inherited from previous clause)* | [1900] |

## Candidate stint `Gardiner, H. H___Ceylon___1919`

- Staff-list name: **Gardiner, H. H** | colony: **Ceylon** | listed 1919–1920 | editions [1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | H. H. Gardiner | Cadets | Civil Establishment | — | — |
| 1920 | H. H. Gardiner | Cadet | Civil Establishment | — | — |

### Deterministic checks: `gardiner_harry_e1884` vs `Gardiner, H. H___Ceylon___1919`

- [PASS] surname_gate: bio 'GARDINER' vs stint 'Gardiner, H. H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H', 'H']
- [PASS] age_gate: stint starts 1919; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1919-1920
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

