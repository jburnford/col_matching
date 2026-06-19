<!-- {"case_id": "case_stordy_robert-john_e1898", "bio_ids": ["stordy_robert-john_e1898"], "stint_ids": ["Stordy, R. J___Kenya___1906", "Stordy, R. J___Kenya___1915"]} -->
# Dossier case_stordy_robert-john_e1898

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stordy_robert-john_e1898`

- Printed name: **STORDY, ROBERT JOHN**
- Birth year: not printed
- Honours: D.S.O (1915)
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1908-L47553.v` — printed in editions [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]:**

> STORDY, ROBERT JOHN, D.S.O. (1915).—Uganda transport service, 1st Jan., 1898; chief veterinary offr., E. Africa and Uganda Prots., 1st Apr., 1901.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898 | Uganda transport service | Uganda | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |
| 1 | 1901 | chief veterinary offr., E. Africa and Uganda Prots | Uganda *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |

## Candidate stint `Stordy, R. J___Kenya___1906`

- Staff-list name: **Stordy, R. J** | colony: **Kenya** | listed 1906–1908 | editions [1906, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | R. J. Stordy | Chief Veterinary Officer | — | — | — |
| 1908 | R. J. Stordy | Chief Veterinary Officer | Civil Establishment | — | — |

### Deterministic checks: `stordy_robert-john_e1898` vs `Stordy, R. J___Kenya___1906`

- [PASS] surname_gate: bio 'STORDY' vs stint 'Stordy, R. J' (exact)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1908
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Stordy, R. J___Kenya___1915`

- Staff-list name: **Stordy, R. J** | colony: **Kenya** | listed 1915–1917 | editions [1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | R. J. Stordy | Chief Veterinary Officer | Veterinary | — | — |
| 1917 | R. J. Stordy | Chief Veterinary Officer | Veterinary | — | — |

### Deterministic checks: `stordy_robert-john_e1898` vs `Stordy, R. J___Kenya___1915`

- [PASS] surname_gate: bio 'STORDY' vs stint 'Stordy, R. J' (exact)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1917
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

