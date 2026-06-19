<!-- {"case_id": "case_mantle_alfred-frank_b1882", "bio_ids": ["mantle_alfred-frank_b1882"], "stint_ids": ["Mantle, A. F___Canada___1912"]} -->
# Dossier case_mantle_alfred-frank_b1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mantle_alfred-frank_b1882`

- Printed name: **MANTLE, ALFRED FRANK**
- Birth year: 1882 (attested in editions [1911, 1913, 1914, 1915, 1917])
- Appears in editions: [1911, 1912, 1913, 1914, 1915, 1917]

### Verbatim printed entry text (OCR)

**Version `col1911-L46586.v` — printed in editions [1911, 1913, 1914, 1915, 1917]:**

> MANTLE, ALFRED FRANK.—B. 1882; ed. London and Watford, England; farmer in W. Canada, 1898 to 1908; agric. editor, "Manitoba Free Press," Dec., 1907, to Nov., 1909; chief of the statistics branch of the Saskatchewan dept. of agric., Nov., 1909; dep. min. of agric. for Sask., 1st Sept., 1910.

**Version `col1912-L46043.v` — printed in editions [1912]:**

> MANTLE, ALFRED FRANK.—B. London and Watford, England; fac. Canada, 1898 to 1908; agric. editor, "Free Press," Dec., 1907, to Nov., 1908; stats. branch of the Saskatchewan agric., Nov., 1909; dep. min. of agric., 1st Sept., 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898–1908 | farmer | Canada | [1911, 1912, 1913, 1914, 1915, 1917] |
| 1 | 1907–1909 | agric. editor | Manitoba | [1911, 1912, 1913, 1914, 1915, 1917] |
| 2 | 1909 | chief of the statistics branch of the Saskatchewan dept. of agric. | Saskatchewan | [1911, 1912, 1913, 1914, 1915, 1917] |
| 3 | 1910 | dep. min. of agric. | Saskatchewan | [1911, 1912, 1913, 1914, 1915, 1917] |

## Candidate stint `Mantle, A. F___Canada___1912`

- Staff-list name: **Mantle, A. F** | colony: **Canada** | listed 1912–1915 | editions [1912, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | A. F. Mantle | Deputy Minister of Agriculture | Chief Departmental Officials | — | — |
| 1913 | A. F. Mantle | Deputy Minister of Agriculture | Chief Departmental Officials | — | — |
| 1914 | A. F. Mantle | Deputy Minister of Agriculture | Chief Departmental Officials | — | — |
| 1915 | A. F. Mantle | Deputy Minister of Agriculture | Chief Departmental Officials | — | — |

### Deterministic checks: `mantle_alfred-frank_b1882` vs `Mantle, A. F___Canada___1912`

- [PASS] surname_gate: bio 'MANTLE' vs stint 'Mantle, A. F' (exact)
- [PASS] initials: bio ['A', 'F'] ~ stint ['A', 'F']
- [PASS] age_gate: stint starts 1912, birth 1882 (age 30)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1915
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

