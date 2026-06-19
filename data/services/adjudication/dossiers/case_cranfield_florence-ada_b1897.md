<!-- {"case_id": "case_cranfield_florence-ada_b1897", "bio_ids": ["cranfield_florence-ada_b1897"], "stint_ids": ["Stanfield, Frank___Canada___1912"]} -->
# Dossier case_cranfield_florence-ada_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cranfield_florence-ada_b1897`

- Printed name: **CRANFIELD, Florence Ada**
- Birth year: 1897 (attested in editions [1949])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L31371.v` — printed in editions [1949]:**

> CRANFIELD, Florence Ada.—b. 1897 ; ed. pte. schs. and business training coll. ; nursing sister, H.K., 1925 ; senr., 1935 ; matron, 1946.

**Version `col1950-L34680.v` — printed in editions [1950, 1951]:**

> CRANFIELD, Florence Ada.—b. 1897; ed. sec. sch. and Lond. Hosp.; nursing sister, H.K., 1925; matron, gr. II, 1938; gr. I, 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | nursing sister | Hong Kong | [1949, 1950, 1951] |
| 1 | 1935 | senr | Hong Kong *(inherited from previous clause)* | [1949] |
| 2 | 1938 | matron, gr. II | Hong Kong *(inherited from previous clause)* | [1950, 1951] |
| 3 | 1946 | matron | Hong Kong *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Stanfield, Frank___Canada___1912`

- Staff-list name: **Stanfield, Frank** | colony: **Canada** | listed 1912–1920 | editions [1912, 1913, 1914, 1915, 1918, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | Frank Stanfield | Member | Legislative Assembly | — | — |
| 1913 | Frank Stanfield | Member | Legislative Assembly | — | — |
| 1914 | Frank Stanfield | — | Legislative Assembly | — | — |
| 1915 | Frank Stanfield | Legislative Assembly Member | Legislative Assembly | — | — |
| 1918 | Frank Stanfield | Member | Legislative Assembly | — | — |
| 1919 | Frank Stanfield | Member | Legislative Assembly | — | — |
| 1920 | Frank Stanfield | Member | Legislative Assembly | — | — |

### Deterministic checks: `cranfield_florence-ada_b1897` vs `Stanfield, Frank___Canada___1912`

- [PASS] surname_gate: bio 'CRANFIELD' vs stint 'Stanfield, Frank' (fuzzy:2)
- [PASS] initials: bio ['F', 'A'] ~ stint ['F']
- [PASS] age_gate: stint starts 1912, birth 1897 (age 15)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1920
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

