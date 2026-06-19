<!-- {"case_id": "case_carlyle_thomas-fairfax_b1879", "bio_ids": ["carlyle_thomas-fairfax_b1879"], "stint_ids": ["Carlyle, T. F___Nigeria___1915"]} -->
# Dossier case_carlyle_thomas-fairfax_b1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `carlyle_thomas-fairfax_b1879`

- Printed name: **CARLYLE, THOMAS FAIRFAX**
- Birth year: 1879 (attested in editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925])
- Honours: F.R.G.S
- Appears in editions: [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1913-L44454.v` — printed in editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]:**

> CARLYLE, THOMAS FAIRFAX, F.R.G.S.—B. 1879; ed. Hereford Cathedral Schol.; articled to a firm of solicitors; served in S. African war with 7th New Zealand contingent, 1901-1902; returned to England and qualified as solicitor; asst. res., Northern Nigeria, 21st June, 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901–1902 | served in S. African war with 7th New Zealand contingent | — | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 1 | 1906 | asst. res. | Northern Nigeria | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |

## Candidate stint `Carlyle, T. F___Nigeria___1915`

- Staff-list name: **Carlyle, T. F** | colony: **Nigeria** | listed 1915–1919 | editions [1915, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | T. F. Carlyle | Thirty-Two Second Class District Officers | NORTHERN PROVINCES | — | — |
| 1918 | T. F. Carlyle | Thirty‑Two Second Class District Officer | Northern Provinces | — | — |
| 1919 | T. F. Carlyle | Thirty-Two Second Class District Officers | NORTHERN PROVINCES | — | — |

### Deterministic checks: `carlyle_thomas-fairfax_b1879` vs `Carlyle, T. F___Nigeria___1915`

- [PASS] surname_gate: bio 'CARLYLE' vs stint 'Carlyle, T. F' (exact)
- [PASS] initials: bio ['T', 'F'] ~ stint ['T', 'F']
- [PASS] age_gate: stint starts 1915, birth 1879 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1915-1919
- [FAIL] position_sim: best 30 vs bar 60: 'asst. res.' ~ 'Thirty‑Two Second Class District Officer'
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

