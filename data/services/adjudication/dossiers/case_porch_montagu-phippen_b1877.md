<!-- {"case_id": "case_porch_montagu-phippen_b1877", "bio_ids": ["porch_montagu-phippen_b1877"], "stint_ids": ["Porch, M. P___Nigeria___1915"]} -->
# Dossier case_porch_montagu-phippen_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `porch_montagu-phippen_b1877`

- Printed name: **PORCH, MONTAGU PHIPPEN**
- Birth year: 1877 (attested in editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921])
- Appears in editions: [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1913-L48752.v` — printed in editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]:**

> PORCH, MONTAGU PHIPPEN.—B. 1877; ed. at Bath Coll. and Magdalen Coll., Oxford; B.A., 1902; M.A., 1904; served with Middlesex Yeomanry in S. African war, 1900 (Queen's medal and three clasps); Egyptian exploration fund with Prof. Flinders Petrie, 1904 and 1905; asst. res., Northern Nigeria, 14th July, 1906; 3rd cls. res., 1st Apr., 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900–1900 | — | South Africa | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 1 | 1902–1902 | B.A. | — | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 2 | 1904–1904 | M.A. | — | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 3 | 1904–1905 | — | Egypt | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 4 | 1906 | asst. res. | Northern Nigeria | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 5 | 1912 | 3rd cls. res. | — | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |

## Candidate stint `Porch, M. P___Nigeria___1915`

- Staff-list name: **Porch, M. P** | colony: **Nigeria** | listed 1915–1919 | editions [1915, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | M. P. Porch | Thirty-Two Second Class District Officers | NORTHERN PROVINCES | — | — |
| 1918 | M. P. Porch | Thirty‑Two Second Class District Officer | Northern Provinces | — | — |
| 1919 | M. P. Porch | Thirty-Two Second Class District Officers | NORTHERN PROVINCES | — | — |

### Deterministic checks: `porch_montagu-phippen_b1877` vs `Porch, M. P___Nigeria___1915`

- [PASS] surname_gate: bio 'PORCH' vs stint 'Porch, M. P' (exact)
- [PASS] initials: bio ['M', 'P'] ~ stint ['M', 'P']
- [PASS] age_gate: stint starts 1915, birth 1877 (age 38)
- [PASS] colony: 1 placed event(s) resolve to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1919
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

