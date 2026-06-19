<!-- {"case_id": "case_neave_charles-alexander_e1889", "bio_ids": ["neave_charles-alexander_e1889"], "stint_ids": ["Neave, C. A___Kenya___1909", "Neave, C. A___Kenya___1920"]} -->
# Dossier case_neave_charles-alexander_e1889

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `neave_charles-alexander_e1889`

- Printed name: **NEAVE, Charles Alexander**
- Birth year: not printed
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923]

### Verbatim printed entry text (OCR)

**Version `col1908-L46461.v` — printed in editions [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923]:**

> NEAVE, Captain Charles Alexander.—Educated at Wellington College and R.M.A., Woolwich; joined Royal Artillery, 1889; served in South Africa (reserve of officers), Feb., 1900, to close of war; Queen's medal, 3 clasps; King's medal, 2 clasps; joined 4th Somerset Light Infantry as captain, 1904; appointed to veterinary department, East Africa Protectorate, Aug., 1905; transport officer, northern frontier district, E.A.P., April, 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889–1889 | Royal Artillery | — | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923] |
| 1 | 1900 | reserve of officers | South Africa | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923] |
| 2 | 1904–1904 | captain | — | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923] |
| 3 | 1905–1905 | veterinary department | East Africa Protectorate | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923] |
| 4 | 1913–1913 | transport officer | East Africa Protectorate | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923] |

## Candidate stint `Neave, C. A___Kenya___1909`

- Staff-list name: **Neave, C. A** | colony: **Kenya** | listed 1909–1913 | editions [1909, 1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | C. A. Neave | Live Stock Inspector | Veterinary | — | Captain |
| 1910 | C. A. Neave | Live Stock Inspector | Veterinary | — | Captain |
| 1911 | C. A. Neave | Live Stock Inspector | Veterinary | — | Captain |
| 1912 | C. A. Neave | Live Stock Inspector | Veterinary | — | Captain |
| 1913 | C. A. Neave | Live Stock Inspector | Veterinary | — | Captain |

### Deterministic checks: `neave_charles-alexander_e1889` vs `Neave, C. A___Kenya___1909`

- [PASS] surname_gate: bio 'NEAVE' vs stint 'Neave, C. A' (exact)
- [PASS] initials: bio ['C', 'A'] ~ stint ['C', 'A']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1909-1913
- [FAIL] position_sim: best 38 vs bar 60: 'transport officer' ~ 'Live Stock Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Neave, C. A___Kenya___1920`

- Staff-list name: **Neave, C. A** | colony: **Kenya** | listed 1920–1923 | editions [1920, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | C. A. Neave | Transport Officer N. F. District | Provincial Administration | — | — |
| 1922 | C. A. Neave | Chief Quarantine Officer | Veterinary | — | — |
| 1923 | C. A. Neave | Chief Quarantine Officer | Veterinary | — | — |

### Deterministic checks: `neave_charles-alexander_e1889` vs `Neave, C. A___Kenya___1920`

- [PASS] surname_gate: bio 'NEAVE' vs stint 'Neave, C. A' (exact)
- [PASS] initials: bio ['C', 'A'] ~ stint ['C', 'A']
- [PASS] age_gate: stint starts 1920; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1923
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

