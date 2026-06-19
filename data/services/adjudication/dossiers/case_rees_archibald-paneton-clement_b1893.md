<!-- {"case_id": "case_rees_archibald-paneton-clement_b1893", "bio_ids": ["rees_archibald-paneton-clement_b1893"], "stint_ids": ["Rees, A. P. C___Togoland___1920"]} -->
# Dossier case_rees_archibald-paneton-clement_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rees_archibald-paneton-clement_b1893`

- Printed name: **REES, ARCHIBALD PANETON CLEMENT**
- Birth year: 1893 (attested in editions [1923, 1925])
- Appears in editions: [1923, 1925]

### Verbatim printed entry text (OCR)

**Version `col1923-L57583.v` — printed in editions [1923, 1925]:**

> REES, ARCHIBALD PANETON CLEMENT.—B. 1893; ed. Christ Coll., Brecon, and St. Edmund Hall, Oxford; capt., Royal Welch Fusiliers, 1915; serv. Gallipoli, Mesopotamia and France; asst. dist. commnr., Gold Coast, 17th Jan., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | capt., Royal Welch Fusiliers | — | [1923, 1925] |
| 1 | 1920 | asst. dist. commnr. | Gold Coast | [1923, 1925] |

## Candidate stint `Rees, A. P. C___Togoland___1920`

- Staff-list name: **Rees, A. P. C** | colony: **Togoland** | listed 1920–1925 | editions [1920, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | A. P. C. Rees | Assistant District Commissioner | Administrative and Political Department | — | Captain |
| 1925 | Capt. A. P. C. Rees | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | Captain |

### Deterministic checks: `rees_archibald-paneton-clement_b1893` vs `Rees, A. P. C___Togoland___1920`

- [PASS] surname_gate: bio 'REES' vs stint 'Rees, A. P. C' (exact)
- [PASS] initials: bio ['A', 'P', 'C'] ~ stint ['A', 'P', 'C']
- [PASS] age_gate: stint starts 1920, birth 1893 (age 27)
- [FAIL] colony: no placed event resolves to 'Togoland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1925
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

