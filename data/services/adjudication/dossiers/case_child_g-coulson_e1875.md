<!-- {"case_id": "case_child_g-coulson_e1875", "bio_ids": ["child_g-coulson_e1875"], "stint_ids": ["Child___Natal___1905"]} -->
# Dossier case_child_g-coulson_e1875

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Child___Natal___1905` is also gate-compatible with biography(ies) outside this case: ['child_a_e1876-2', 'child_herbert-a_e1883'] (already linked elsewhere or filtered).

## Biography `child_g-coulson_e1875`

- Printed name: **CHILD, G. COULSON**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1889]

### Verbatim printed entry text (OCR)

**Version `col1883-L26820.v` — printed in editions [1883, 1886, 1889]:**

> CHILD, CAPTAIN G. COULSON, F.R.G.S., late 7th Queen's Own Hussars and King's Own Light Infantry Militia.—Assistant-inspector, Houssa constabulary, Sept., 1875; district commissioner of Elmiau, Oct., 1875, acting collector and treasurer, Gold Coast Colony, from Nov., 1876, to July, 1877, and as such member of the executive and legislative councils; first class inspector, Houssa constabulary, Jan., 1877; was acting colonial secretary and acting assistant colonial secretary from 8th August, 1878, to the 15th April, 1879; and as such acted in both councils; acting inspector-general, Houssa constabulary, May to Nov., 1879; inspector of immigrants, Mauritius, 3rd Sept., 1880; acting inspector-general, Mauritius police force, 8th Sept., 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | Assistant-inspector | — | [1883, 1886, 1889] |
| 1 | 1875 | district commissioner | — | [1883, 1886, 1889] |
| 2 | 1876–1877 | acting collector and treasurer | Gold Coast Colony | [1883, 1886, 1889] |
| 3 | 1877 | first class inspector | — | [1883, 1886, 1889] |
| 4 | 1878–1879 | acting colonial secretary and acting assistant colonial secretary | — | [1883, 1886, 1889] |
| 5 | 1879–1879 | acting inspector-general | — | [1883, 1886, 1889] |
| 6 | 1880 | inspector of immigrants | Mauritius | [1883, 1886, 1889] |
| 7 | 1881 | acting inspector-general | Mauritius | [1883, 1886, 1889] |

## Candidate stint `Child___Natal___1905`

- Staff-list name: **Child** | colony: **Natal** | listed 1905–1906 | editions [1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | Child | House Surgeon | Grey's Hospital, Pietermaritzburg | — | — |
| 1906 | Child | House Surgeon | Medical Department | — | — |

### Deterministic checks: `child_g-coulson_e1875` vs `Child___Natal___1905`

- [PASS] surname_gate: bio 'CHILD' vs stint 'Child' (exact)
- [PASS] initials: bio ['G', 'C'] ~ stint ['?']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Natal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1906
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

