<!-- {"case_id": "case_childs_g-coulson_e1875", "bio_ids": ["childs_g-coulson_e1875"], "stint_ids": ["Childs, G. C___Mauritius___1888"]} -->
# Dossier case_childs_g-coulson_e1875

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `childs_g-coulson_e1875`

- Printed name: **CHILDS, G. Coulson**
- Birth year: not printed
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L32617.v` — printed in editions [1888]:**

> CHILDS, Captain G. Coulson, I.R.G.S., late 7th Queen's Own Hussars and King's Own Light Infantry Militia.—Assistant-inspector, Houssa constabulary, Sept., 1875; district commissioner of Elmina, Oct., 1875, acting collector and treasurer, Gold Coast Colony, Nov., 1876, to July, 1877, first class inspector, Houssa constabulary, Jan., 1877; acting colonial secretary and acting assistant colonial secretary August, 1878, to April, 1879; acting inspector-general, May to Nov., 1879; inspector of immigrants, Mauritius, Sept., 1880; inspector-general of police, Nov., 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | Assistant-inspector | — | [1888] |
| 1 | 1875 | district commissioner | Elmina | [1888] |
| 2 | 1876–1877 | acting collector and treasurer | Gold Coast | [1888] |
| 3 | 1877 | first class inspector | — | [1888] |
| 4 | 1878–1879 | acting colonial secretary and acting assistant colonial secretary | — | [1888] |
| 5 | 1879–1879 | acting inspector-general | — | [1888] |
| 6 | 1880 | inspector of immigrants | Mauritius | [1888] |
| 7 | 1885 | inspector-general of police | — | [1888] |

## Candidate stint `Childs, G. C___Mauritius___1888`

- Staff-list name: **Childs, G. C** | colony: **Mauritius** | listed 1888–1890 | editions [1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | G. C. Childs | Inspector-General | Police Department | — | — |
| 1889 | G. C. Childs | Inspector-General | Police Department | — | — |
| 1890 | G. C. Childs | Inspector-General | Police Department | — | — |

### Deterministic checks: `childs_g-coulson_e1875` vs `Childs, G. C___Mauritius___1888`

- [PASS] surname_gate: bio 'CHILDS' vs stint 'Childs, G. C' (exact)
- [PASS] initials: bio ['G', 'C'] ~ stint ['G', 'C']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1890
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

