<!-- {"case_id": "case_mortimer_hugh_b1882", "bio_ids": ["mortimer_hugh_b1882"], "stint_ids": ["Mortimer, H. J___Nigeria___1929"]} -->
# Dossier case_mortimer_hugh_b1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mortimer_hugh_b1882'] carry a single initial only — the namesake trap applies.

## Biography `mortimer_hugh_b1882`

- Printed name: **MORTIMER, HUGH**
- Birth year: 1882 (attested in editions [1932])
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L62683.v` — printed in editions [1932]:**

> MORTIMER, HUGH, B.A. (Lond.).—B. 1882; European mast., Johore, Nov., 1913; headmast., Eng. Schl., Muar, Jan., 1914; 2nd lieut., I.A.R.O., Apr., 1918; on service, India and Mesopotamia, 1918-19; headmast., Bukit Zaharah Schl., Johore Bahru, 1919, 1921 and 1924; ag. Eng. educn. offr., Johore, 1920 and 1924; headmast., Hutchings Schl., Penang, Nov., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | European mast. | Johore | [1932] |
| 1 | 1914 | headmast., Eng. Schl. | Muar | [1932] |
| 2 | 1918 | 2nd lieut. | — | [1932] |
| 3 | 1918–1919 | on service | India and Mesopotamia | [1932] |
| 4 | 1919–1924 | headmast., Bukit Zaharah Schl. | Johore Bahru | [1932] |
| 5 | 1920–1924 | ag. Eng. educn. offr. | Johore | [1932] |
| 6 | 1928 | headmast., Hutchings Schl. | Penang | [1932] |

## Candidate stint `Mortimer, H. J___Nigeria___1929`

- Staff-list name: **Mortimer, H. J** | colony: **Nigeria** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | H. J. Mortimer | Mechanic | Veterinary Department | — | — |
| 1930 | H. J. Mortimer | Mechanic | Veterinary Department | — | — |

### Deterministic checks: `mortimer_hugh_b1882` vs `Mortimer, H. J___Nigeria___1929`

- [PASS] surname_gate: bio 'MORTIMER' vs stint 'Mortimer, H. J' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H', 'J']
- [PASS] age_gate: stint starts 1929, birth 1882 (age 47)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1930
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

