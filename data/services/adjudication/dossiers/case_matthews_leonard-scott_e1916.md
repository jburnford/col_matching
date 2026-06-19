<!-- {"case_id": "case_matthews_leonard-scott_e1916", "bio_ids": ["matthews_leonard-scott_e1916"], "stint_ids": ["Matthews, S___Australia___1913"]} -->
# Dossier case_matthews_leonard-scott_e1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 46 official(s) with this surname in the graph's staff lists; 22 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `matthews_leonard-scott_e1916`

- Printed name: **MATTHEWS, LEONARD SCOTT**
- Birth year: not printed
- Appears in editions: [1927, 1928, 1929, 1930]

### Verbatim printed entry text (OCR)

**Version `col1927-L61262.v` — printed in editions [1927, 1928, 1929]:**

> MATTHEWS, LEONARD SCOTT.—1st K.A.R., 1916-18; ag. senr. paymr., K.A.R., Apr., 1920; clearance offr., Zomba, K.A.R. war acc'ts., Apr., 1921 to Mar., 1922; dep. treas., Nyassaland, Dec., 1924; ag. treas., Apr., 1925.

**Version `col1930-L66728.v` — printed in editions [1930]:**

> MATTHEWS, Leonard Scott.—1st 1916-18; ag. senr. paymr., K.A.R., Apr.; clearance offr., Zomba, K.A.R. war accts., 1921 to Mar., 1922; dep. treas., Nyasaland, 1924; ag. treas., Apr., 1925; dep. treas., Yika Territory, 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916–1918 | 1st K.A.R | — | [1927, 1928, 1929] |
| 1 | 1916–1918 | — | — | [1930] |
| 2 | 1920 | ag. senr. paymr., K.A.R | — | [1927, 1928, 1929] |
| 3 | 1921–1922 | clearance offr., Zomba, K.A.R. war acc'ts | — | [1927, 1928, 1929, 1930] |
| 4 | 1924 | dep. treas., Nyassaland | Nyasaland | [1927, 1928, 1929, 1930] |
| 5 | 1925 | ag. treas | Nyasaland *(inherited from previous clause)* | [1927, 1928, 1929, 1930] |
| 6 | 1929 | dep. treas., Yika Territory | Nyasaland *(inherited from previous clause)* | [1930] |

## Candidate stint `Matthews, S___Australia___1913`

- Staff-list name: **Matthews, S** | colony: **Australia** | listed 1913–1918 | editions [1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | S. Matthews | District Medical Officer and Quarantine Officer | Medical and Public Health Department | — | — |
| 1918 | S. Matthews | District Medical Officer | Medical and Public Health Department | — | — |

### Deterministic checks: `matthews_leonard-scott_e1916` vs `Matthews, S___Australia___1913`

- [PASS] surname_gate: bio 'MATTHEWS' vs stint 'Matthews, S' (exact)
- [PASS] initials: bio ['L', 'S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1913; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1918
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

