<!-- {"case_id": "case_douglass_edward-wingfield_b1873", "bio_ids": ["douglass_edward-wingfield_b1873"], "stint_ids": ["Douglass, E. W___Transvaal___1907"]} -->
# Dossier case_douglass_edward-wingfield_b1873

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `douglass_edward-wingfield_b1873`

- Printed name: **DOUGLASS, EDWARD WINGFIELD**
- Birth year: 1873 (attested in editions [1920, 1921, 1922, 1923, 1924, 1925])
- Honours: K.C (1913)
- Appears in editions: [1920, 1921, 1922, 1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1920-L53092.v` — printed in editions [1920, 1921, 1922, 1923, 1924, 1925]:**

> DOUGLASS, EDWARD WINGFIELD, K.C. (1913)—B. 1873; ed. St. Andrew's Coll., Grahamstown, Cape Province; B.A. in law, Oxford, 1895; final bar exam., Middle Temple, 1895; called to the bar, Middle Temple, 1896; called to the bar, Cape, 1898; called to the bar, E.D. Court, 1898; capt., Neabitt's Horse, S. African War, 1900-1902; crown prosecutor, mil. tribunal, Johannesburg, 1900-1901; crown prosecu- tor, Witwatersrand dist., 1902-1913; atty.-gen., Natal, 1913-1915; atty.-gen., Cape Province, Dec., 1915; ag. judge, Griqualand West Local Divn. of supreme ct. of S. Africa, May-June and Aug.-Sep., 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | B.A. in law, Oxford | — | [1920, 1921, 1922, 1923, 1924, 1925] |
| 1 | 1895 | final bar exam., Middle Temple | — | [1920, 1921, 1922, 1923, 1924, 1925] |
| 2 | 1896 | called to the bar, Middle Temple | — | [1920, 1921, 1922, 1923, 1924, 1925] |
| 3 | 1898 | called to the bar | Cape of Good Hope | [1920, 1921, 1922, 1923, 1924, 1925] |
| 4 | 1900–1902 | capt., Neabitt's Horse, S. African War | Cape of Good Hope *(inherited from previous clause)* | [1920, 1921, 1922, 1923, 1924, 1925] |
| 5 | 1902–1913 | crown prosecu- tor, Witwatersrand dist | Cape of Good Hope *(inherited from previous clause)* | [1920, 1921, 1922, 1923, 1924, 1925] |
| 6 | 1913–1915 | atty.-gen. | Natal | [1920, 1921, 1922, 1923, 1924, 1925] |
| 7 | 1915 | atty.-gen., Cape Province | Cape of Good Hope | [1920, 1921, 1922, 1923, 1924, 1925] |
| 8 | 1919 | ag. judge, Griqualand West Local Divn. of supreme ct. of S. Africa, May-June and Aug.- | Cape of Good Hope *(inherited from previous clause)* | [1920, 1921, 1922, 1923, 1924, 1925] |

## Candidate stint `Douglass, E. W___Transvaal___1907`

- Staff-list name: **Douglass, E. W** | colony: **Transvaal** | listed 1907–1908 | editions [1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | E. W. Douglass | Crown Prosecutor | High Court of Witwatersrand | — | — |
| 1908 | E. W. Douglass | Crown Prosecutor | High Court of Witwatersrand | — | — |

### Deterministic checks: `douglass_edward-wingfield_b1873` vs `Douglass, E. W___Transvaal___1907`

- [PASS] surname_gate: bio 'DOUGLASS' vs stint 'Douglass, E. W' (exact)
- [PASS] initials: bio ['E', 'W'] ~ stint ['E', 'W']
- [PASS] age_gate: stint starts 1907, birth 1873 (age 34)
- [FAIL] colony: no placed event resolves to 'Transvaal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1908
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

