<!-- {"case_id": "case_howden_james-h_b1860", "bio_ids": ["howden_james-h_b1860"], "stint_ids": ["Howden, James H___Canada___1908"]} -->
# Dossier case_howden_james-h_b1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `howden_james-h_b1860`

- Printed name: **HOWDEN, James H.**
- Birth year: 1860 (attested in editions [1911, 1912, 1913, 1914, 1915, 1917])
- Appears in editions: [1911, 1912, 1913, 1914, 1915, 1917]

### Verbatim printed entry text (OCR)

**Version `col1911-L45602.v` — printed in editions [1911, 1912, 1913, 1914, 1915, 1917]:**

> HOWDEN, Hon. James H.—B. 1860; ed. high schl., Rockwood and St. Catherines; barrister-at-law; elect. to the Manitoba legis. for Beautiful Plains, 1903, 1907 and 1910; min. of telephones for Manitoba, 1907; prov. sec. 1908; atty.-gen., 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903–1910 | elect. to the Manitoba legis. for Beautiful Plains | Manitoba | [1911, 1912, 1913, 1914, 1915, 1917] |
| 1 | 1907–1907 | min. of telephones | Manitoba | [1911, 1912, 1913, 1914, 1915, 1917] |
| 2 | 1908–1908 | prov. sec. | — | [1911, 1912, 1913, 1914, 1915, 1917] |
| 3 | 1911–1911 | atty.-gen. | — | [1911, 1912, 1913, 1914, 1915, 1917] |

## Candidate stint `Howden, James H___Canada___1908`

- Staff-list name: **Howden, James H** | colony: **Canada** | listed 1908–1915 | editions [1908, 1912, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | James H. Howden | Commissioner of Railways, Telegraphs and Telephones | Seat of Government—Winnipeg | — | — |
| 1912 | James H. Howden | Provincial Secretary | Seat of Government | — | — |
| 1913 | James H. Howden | Attorney-General | Government | — | — |
| 1914 | Hon. James H. Howden | Attorney-General | — | — | — |
| 1915 | J. H. Howden | Member for Beautiful Plains | — | — | — |
| 1915 | James Howden | Attorney-General | — | — | — |

### Deterministic checks: `howden_james-h_b1860` vs `Howden, James H___Canada___1908`

- [PASS] surname_gate: bio 'HOWDEN' vs stint 'Howden, James H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1908, birth 1860 (age 48)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1915
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

