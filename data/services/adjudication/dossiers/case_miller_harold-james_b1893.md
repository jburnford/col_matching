<!-- {"case_id": "case_miller_harold-james_b1893", "bio_ids": ["miller_harold-james_b1893"], "stint_ids": ["Miller, H. J___Cyprus___1920"]} -->
# Dossier case_miller_harold-james_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 106 official(s) with this surname in the graph's staff lists; 38 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `miller_harold-james_b1893`

- Printed name: **MILLER, Harold James**
- Birth year: 1893 (attested in editions [1948])
- Honours: M.M (1917)
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L34651.v` — printed in editions [1948]:**

> MILLER, Harold James, M.M. (1917).—b. 1893; ed. King Edward VI Sch., Southampton; on mil. serv., 1916-18, obsvr. lieut.; apptd., survey, Cyp., 1919; asst. inspr., survey, Pal., 1922; land settlement offr., 1937; regnl. offr., Haifa, 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | apptd., survey | Cyprus | [1948] |
| 1 | 1922 | asst. inspr., survey | Palestine | [1948] |
| 2 | 1937 | land settlement offr | Palestine *(inherited from previous clause)* | [1948] |
| 3 | 1946 | regnl. offr., Haifa | Palestine *(inherited from previous clause)* | [1948] |

## Candidate stint `Miller, H. J___Cyprus___1920`

- Staff-list name: **Miller, H. J** | colony: **Cyprus** | listed 1920–1923 | editions [1920, 1921, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | H. J. Miller | Ordnance Surveyor | Land Registration and Survey Department | — | — |
| 1921 | H. J. Miller | Surveyor, First Grade | Land Registration and Survey Department | — | — |
| 1922 | H. J. Miller | Surveyor, First Grade | Land Registration and Survey Department | — | — |
| 1923 | H. J. Miller | Surveyor, First Grade | Survey Staff | — | — |

### Deterministic checks: `miller_harold-james_b1893` vs `Miller, H. J___Cyprus___1920`

- [PASS] surname_gate: bio 'MILLER' vs stint 'Miller, H. J' (exact)
- [PASS] initials: bio ['H', 'J'] ~ stint ['H', 'J']
- [PASS] age_gate: stint starts 1920, birth 1893 (age 27)
- [PASS] colony: 1 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1920-1923
- [FAIL] position_sim: best 56 vs bar 60: 'apptd., survey' ~ 'Surveyor, First Grade'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

