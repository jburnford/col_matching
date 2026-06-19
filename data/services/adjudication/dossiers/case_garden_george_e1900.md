<!-- {"case_id": "case_garden_george_e1900", "bio_ids": ["garden_george_e1900"], "stint_ids": ["Garden, G___Nyasaland___1911"]} -->
# Dossier case_garden_george_e1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['garden_george_e1900'] carry a single initial only — the namesake trap applies.

## Biography `garden_george_e1900`

- Printed name: **GARDEN, GEORGE**
- Birth year: not printed
- Appears in editions: [1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1912-L44328.v` — printed in editions [1912, 1913, 1914, 1915, 1917, 1918, 1919]:**

> GARDEN, GEORGE.—M.R.C.V.S., Edin., 1900; certif., Trop. Vet. Med., R.C.V.S., Lond., 1908; offr. in charge of vet. survey, S. Nigeria, May, 1907, to Mar., 1910; vet. bact., Nyasaaland Prot., May, 1910; hon. capt., Nyasaaland Field Force, and ag. rinderpest comsnr., German East Africa, 1917.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900–1900 | M.R.C.V.S. | Edinburgh | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 1 | 1907–1910 | offr. in charge of vet. survey | Southern Nigeria | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 2 | 1908–1908 | certif., Trop. Vet. Med., R.C.V.S. | London | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 3 | 1910–1910 | vet. bact. | Nyasaaland Protectorate | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 4 | 1917–1917 | hon. capt., Nyasaaland Field Force, and ag. rinderpest comsnr. | German East Africa | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |

## Candidate stint `Garden, G___Nyasaland___1911`

- Staff-list name: **Garden, G** | colony: **Nyasaland** | listed 1911–1919 | editions [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | G. Garden | Veterinary Bacteriologist | Agricultural and Forestry Department | — | — |
| 1912 | G. Garden | Veterinary Bacteriologist | Agricultural Department | — | — |
| 1913 | G. Garden | Veterinary Bacteriologist | Agricultural Department | — | — |
| 1914 | G. Garden | Veterinary Officers | Veterinary Division | — | — |
| 1915 | G. Garden | Veterinary Officer | Veterinary Division | — | — |
| 1917 | G. Garden | Senior Veterinary Officer | Veterinary Division | — | — |
| 1918 | G. Garden | Senior Veterinary Officer | Agricultural Department | — | — |
| 1919 | G. Garden | Senior Veterinary Officer | Veterinary Division | — | — |

### Deterministic checks: `garden_george_e1900` vs `Garden, G___Nyasaland___1911`

- [PASS] surname_gate: bio 'GARDEN' vs stint 'Garden, G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1919
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

