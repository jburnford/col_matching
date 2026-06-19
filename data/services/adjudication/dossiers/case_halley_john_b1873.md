<!-- {"case_id": "case_halley_john_b1873", "bio_ids": ["halley_john_b1873"], "stint_ids": ["Halley, J___Fiji___1905"]} -->
# Dossier case_halley_john_b1873

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['halley_john_b1873'] carry a single initial only — the namesake trap applies.

## Biography `halley_john_b1873`

- Printed name: **HALLEY, JOHN**
- Birth year: 1873 (attested in editions [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915])
- Appears in editions: [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1907-L44708.v` — printed in editions [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]:**

> HALLEY, JOHN.—B. 1873; ed. Gordon’s Coll., Marischal Coll., and Univ. of Aberdeen, M.B., C.M., D.Ph.; civ. surg. attached to R.A.M.C., Sierra Leone, 1900-2; ditto, S. Africa, 1902; dist. med. offr., Fiji, 1903; health offr. and local authority, Suva, 1903; supt. of Muana leper asylum, Beqa, 1904; dist. med. offr., Navua, 1905; stip. mag. of the colony, 1906; gov’t. med. offr., Levuka, 1906; ag. res. commnr., Rotumah, 1908.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900–1902 | civ. surg. attached to R.A.M.C. | Sierra Leone | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 1 | 1902 | ditto, S. Africa | Sierra Leone *(inherited from previous clause)* | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 2 | 1903 | dist. med. offr. | Fiji | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 3 | 1904 | supt. of Muana leper asylum, Beqa | Fiji *(inherited from previous clause)* | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 4 | 1905 | dist. med. offr., Navua | Fiji *(inherited from previous clause)* | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 5 | 1906 | stip. mag. of the colony | Fiji *(inherited from previous clause)* | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 6 | 1908 | ag. res. commnr., Rotumah | Fiji *(inherited from previous clause)* | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |

## Candidate stint `Halley, J___Fiji___1905`

- Staff-list name: **Halley, J** | colony: **Fiji** | listed 1905–1915 | editions [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | J. Halley | Government Medical Officer | Medical Department | — | — |
| 1905 | J. Halley | Medical Superintendent | Leper Asylum | — | — |
| 1906 | J. Halley | Government Medical Officer | Medical Department | — | — |
| 1907 | J. Halley | Government Medical Officer | Medical Department | — | — |
| 1908 | J. Halley | Government Medical Officer | Medical Department | — | — |
| 1909 | J. Halley | Government Medical Officer | Medical Department | — | — |
| 1910 | J. Halley | Government Medical Officer | Medical Department | — | — |
| 1911 | J. Halley | Government Medical Officer | Medical Department | — | — |
| 1912 | J. Halley | Government Medical Officer | Medical Department | — | — |
| 1913 | J. Halley | Government Medical Officer | Medical Department | — | — |
| 1914 | J. Halley | Government Medical Officer | Medical Department | — | — |
| 1915 | J. Halley | Government Medical Officers | MEDICAL DEPARTMENT | — | — |

### Deterministic checks: `halley_john_b1873` vs `Halley, J___Fiji___1905`

- [PASS] surname_gate: bio 'HALLEY' vs stint 'Halley, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1905, birth 1873 (age 32)
- [PASS] colony: 5 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1905-1915
- [FAIL] position_sim: best 51 vs bar 60: 'dist. med. offr.' ~ 'Government Medical Officer'
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

