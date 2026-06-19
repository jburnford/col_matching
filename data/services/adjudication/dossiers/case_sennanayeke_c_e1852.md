<!-- {"case_id": "case_sennanayeke_c_e1852", "bio_ids": ["sennanayeke_c_e1852"], "stint_ids": ["Senanayake, C___Ceylon___1883", "Sennanayake, C___Ceylon___1877"]} -->
# Dossier case_sennanayeke_c_e1852

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['sennanayeke_c_e1852'] carry a single initial only — the namesake trap applies.

## Biography `sennanayeke_c_e1852`

- Printed name: **SENNANAYEKE, C**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29457.v` — printed in editions [1883]:**

> SENNANAYEKE, REV. C.—Colonial chaplain of Morottoo, Corolawella, Ceylon, Sept., 1852; colonial chaplain, Galkisse and Millagraya, 1861; colonial chaplain, Galkisse, 1861.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1852 | Colonial chaplain of Morottoo, Corolawella | Ceylon | [1883] |
| 1 | 1861 | colonial chaplain, Galkisse and Millagraya | Ceylon *(inherited from previous clause)* | [1883] |

## Candidate stint `Senanayake, C___Ceylon___1883`

- Staff-list name: **Senanayake, C** | colony: **Ceylon** | listed 1883–1886 | editions [1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | C. Senanayake | Colonial Chaplain | Ecclesiastical Department | — | — |
| 1886 | C. Senanayake | Colonial Chaplain | List of Colonial Chaplains | — | — |

### Deterministic checks: `sennanayeke_c_e1852` vs `Senanayake, C___Ceylon___1883`

- [PASS] surname_gate: bio 'SENNANAYEKE' vs stint 'Senanayake, C' (fuzzy:2)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1886
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Sennanayake, C___Ceylon___1877`

- Staff-list name: **Sennanayake, C** | colony: **Ceylon** | listed 1877–1879 | editions [1877, 1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. Sennanayake | Colonial Chaplain | Colonial Chaplains | — | — |
| 1878 | C. Sennanayake | — | Ecclesiastical Department | — | — |
| 1879 | C. Sennanayake | Colonial Chaplain | Ecclesiastical Department | — | — |

### Deterministic checks: `sennanayeke_c_e1852` vs `Sennanayake, C___Ceylon___1877`

- [PASS] surname_gate: bio 'SENNANAYEKE' vs stint 'Sennanayake, C' (fuzzy:1)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1879
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

