<!-- {"case_id": "case_cillie_f-p_e1903", "bio_ids": ["cillie_f-p_e1903"], "stint_ids": ["Collie, F___Trinidad___1890"]} -->
# Dossier case_cillie_f-p_e1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cillie_f-p_e1903`

- Printed name: **CILLIE, F. P**
- Birth year: not printed
- Appears in editions: [1914, 1915, 1917, 1918, 1919, 1920, 1922, 1924, 1925, 1927, 1928, 1929, 1930]

### Verbatim printed entry text (OCR)

**Version `col1914-L45319.v` — printed in editions [1914, 1915, 1917, 1918, 1919, 1920, 1922, 1924, 1925, 1927, 1928, 1929, 1930]:**

> CILLIE, F. P., B.A.—Ed. Stellenbosch; teacher of Dutch, Gymnasium, Stellenbosch, 1903; inspr. of schls., O.F.S., 9th Jan., 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | teacher of Dutch, Gymnasium, Stellenbosch | — | [1914, 1915, 1917, 1918, 1919, 1920, 1922, 1924, 1925, 1927, 1928, 1929, 1930] |
| 1 | 1911 | inspr. of schls. | Orange Free State | [1914, 1915, 1917, 1918, 1919, 1920, 1922, 1924, 1925, 1927, 1928, 1929, 1930] |

## Candidate stint `Collie, F___Trinidad___1890`

- Staff-list name: **Collie, F** | colony: **Trinidad** | listed 1890–1898 | editions [1890, 1894, 1896, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | F. Collie | Assistant | Clerks of the Peace | — | — |
| 1894 | F. Collie | 3rd Clerk | Medical Establishment | — | — |
| 1896 | F. Collie | Assistant Clerk | Clerks of the Peace | — | — |
| 1898 | F. Collie | Assistant Clerks | Clerks of the Peace | — | — |

### Deterministic checks: `cillie_f-p_e1903` vs `Collie, F___Trinidad___1890`

- [PASS] surname_gate: bio 'CILLIE' vs stint 'Collie, F' (fuzzy:1)
- [PASS] initials: bio ['F', 'P'] ~ stint ['F']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1890-1898
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

