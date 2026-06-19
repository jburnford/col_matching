<!-- {"case_id": "case_coller_frank-herbert_b1866", "bio_ids": ["coller_frank-herbert_b1866"], "stint_ids": ["Coller, F. H___Windward Islands___1914", "Coller, F. H___Windward Islands___1925"]} -->
# Dossier case_coller_frank-herbert_b1866

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coller_frank-herbert_b1866`

- Printed name: **COLLER, FRANK HERBERT**
- Birth year: 1866 (attested in editions [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924])
- Appears in editions: [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1915-L46064.v` — printed in editions [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924]:**

> COLLER, FRANK HERBERT.—B. 1866; ed. Westminster schl. and Christ Church, Oxford; 1st cls. class. mods.; 1st cls. lit. hum.; M.A.; pres. of Oxford Union Society, 1890; called to the bar, Lincoln's Inn, 1893; ch. just., St. Lucia, 1912; seconded for special war duty in the U.K., 1st Jan., 1917.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890 | pres. of Oxford Union Society | — | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |
| 1 | 1893 | called to the bar, Lincoln's Inn | — | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |
| 2 | 1912 | ch. just. | St. Lucia | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |
| 3 | 1917 | seconded for special war duty in the U.K | St. Lucia *(inherited from previous clause)* | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |

## Candidate stint `Coller, F. H___Windward Islands___1914`

- Staff-list name: **Coller, F. H** | colony: **Windward Islands** | listed 1914–1919 | editions [1914, 1915, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | F. H. Coller | Chief Justice | Court of Appeal | — | — |
| 1914 | F. H. Coller | Chief Justice | Judicial | — | — |
| 1915 | F. H. Coller | Chief Justice | Judicial | — | — |
| 1918 | F. H. Coller | Chief Justice | Judicial | — | — |
| 1919 | F. H. Coller | Chief Justice | Judicial | — | — |
| 1919 | Mr. F. H. Coller | Chief Justice | — | — | — |

### Deterministic checks: `coller_frank-herbert_b1866` vs `Coller, F. H___Windward Islands___1914`

- [PASS] surname_gate: bio 'COLLER' vs stint 'Coller, F. H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1914, birth 1866 (age 48)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1919
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Coller, F. H___Windward Islands___1925`

- Staff-list name: **Coller, F. H** | colony: **Windward Islands** | listed 1925–1939 | editions [1925, 1933, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | F. H. Coller | Chief Justice | Judiciary | — | — |
| 1933 | F. H. Coller | Chief Justice | — | — | — |
| 1936 | F. H. Coller | Chief Justice | Judicial | — | — |
| 1939 | F. H. Coller | Chief Justice, editor of Commercial Code | Legal | — | — |

### Deterministic checks: `coller_frank-herbert_b1866` vs `Coller, F. H___Windward Islands___1925`

- [PASS] surname_gate: bio 'COLLER' vs stint 'Coller, F. H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1925, birth 1866 (age 59)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1939
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

