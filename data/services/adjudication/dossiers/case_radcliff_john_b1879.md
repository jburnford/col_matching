<!-- {"case_id": "case_radcliff_john_b1879", "bio_ids": ["radcliff_john_b1879"], "stint_ids": ["Radcliff, J___Northern Nigeria___1909"]} -->
# Dossier case_radcliff_john_b1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['radcliff_john_b1879'] carry a single initial only — the namesake trap applies.

## Biography `radcliff_john_b1879`

- Printed name: **RADCLIFF, JOHN**
- Birth year: 1879 (attested in editions [1914, 1918, 1919])
- Appears in editions: [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1914-L49359.v` — printed in editions [1914, 1918, 1919]:**

> RADCLIFF, JOHN.—B. 1879; ed. Denstone and Royal Schl., Armagh; lieut., I.Y., S. African war, 1900-1901 (Queen's medal with 5 clasps); lieut., 5th Batt. Leinster Regt., 1903; D.S.C., N. Nigeria, 1906; senr. transport offr., 1908; ag. chief transport offr., Aug., 1909, to Feb., 1910; ag. cantonment mag., Zungeru, Jan., 1911 to July, 1912.

**Version `col1913-L48861.v` — printed in editions [1913, 1915, 1917, 1920, 1921]:**

> RADCLIFFE, JOHN.—B. 1879; ed. Denstone and Royal Schl., Armagh; lieut., I.Y., S. African war, 1900-1901 (Queen's medal with 5 clasps); lieut. 5th, Batt., Leinster Regt., 1903; D.S.C., N. Nigeria, 1906; senr. transport offr., 1908; ag. chief transport offr., Aug., 1909, to Feb., 1910; ag. cantonment mag., Zungera, Jan., 1911 to July, 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900–1901 | lieut., I.Y. | South Africa | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 1 | 1903 | lieut., 5th Batt. Leinster Regt. | — | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 2 | 1906 | D.S.C. | Northern Nigeria | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 3 | 1908 | senr. transport offr. | — | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 4 | 1909–1910 | ag. chief transport offr. | — | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 5 | 1911–1912 | ag. cantonment mag. | Zungeru | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |

## Candidate stint `Radcliff, J___Northern Nigeria___1909`

- Staff-list name: **Radcliff, J** | colony: **Northern Nigeria** | listed 1909–1910 | editions [1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | Lieut. J. Radcliff | District Superintendent | Police | — | Lieutenant |
| 1910 | J. Radcliff | District Superintendent | Police | — | — |

### Deterministic checks: `radcliff_john_b1879` vs `Radcliff, J___Northern Nigeria___1909`

- [PASS] surname_gate: bio 'RADCLIFF' vs stint 'Radcliff, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1909, birth 1879 (age 30)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1909-1910
- [FAIL] position_sim: best 23 vs bar 60: 'D.S.C.' ~ 'District Superintendent'
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

