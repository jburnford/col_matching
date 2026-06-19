<!-- {"case_id": "case_rosborough_j_e1893", "bio_ids": ["rosborough_j_e1893"], "stint_ids": ["Rosborough, J___Nyasaland___1909"]} -->
# Dossier case_rosborough_j_e1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['rosborough_j_e1893'] carry a single initial only — the namesake trap applies.

## Biography `rosborough_j_e1893`

- Printed name: **ROSBOROUGH, J**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1908-L47085.v` — printed in editions [1908, 1909, 1910, 1911, 1912, 1913]:**

> ROSBOROUGH, J.—Ed. at Trin. Coll., Dublin; B.A., Univ. of Dublin, 1893; capt. 6th R.I. Rifles, 1896; served with Gambia expedit., 1901 (medal with clasps); Sonalland, 19-2-1904 (clasps); Nandi expedit., B. E. Africa, 1905-1906 (ment. in desps., clasps); capt., K.A.R., Nyasaland Prof.

**Version `col1905-L45606.v` — printed in editions [1905, 1907]:**

> ROSBOROUGH, J.—Ed. at Trin. Coll., Dublin; B.A., Univ. of Dublin, 1893; capt. 6th R.I. Rifles, 1896; served with Gambia expdn., 1901; Somaliland, 1902-1904 (medal with two clasps); capt. 1st Batt., King's African Rifles, British Central African Prot.

**Version `col1906-L47732.v` — printed in editions [1906]:**

> ROSBOROUGH, J.—ED. AT TRIN. COLL., DUBLIN; B.A., UNIV. OF DUBLIN, 1893; CAPT. 6TH R.I. RIFLES, 1896; SERVED WITH GAMBIAN EXPEDN., 1901; SOMALILAND, 1902-1904 (MEDAL WITH TWO CLASPS); CAPT. 1ST BATT., KING'S AFRICAN RIFLES, BRITISH CENTRAL AFRICAN PROT.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893 | B.A., Univ. of Dublin | — | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |
| 1 | 1896 | capt. 6th R.I. Rifles | — | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |
| 2 | 1901 | served with Gambia expedit | — | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |
| 3 | 1902–1904 | served with Gambia expdn | Somaliland | [1905, 1906, 1907] |
| 4 | 1904 | Sonalland, 19-2- | — | [1908, 1909, 1910, 1911, 1912, 1913] |
| 5 | 1905–1906 | Nandi expedit., B. E. Africa | — | [1908, 1909, 1910, 1911, 1912, 1913] |

## Candidate stint `Rosborough, J___Nyasaland___1909`

- Staff-list name: **Rosborough, J** | colony: **Nyasaland** | listed 1909–1910 | editions [1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | J. Rosborough | Company Commander | King's African Rifles | — | — |
| 1910 | J. Rosborough | Company Commander | King's African Rifles | — | — |

### Deterministic checks: `rosborough_j_e1893` vs `Rosborough, J___Nyasaland___1909`

- [PASS] surname_gate: bio 'ROSBOROUGH' vs stint 'Rosborough, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1910
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

