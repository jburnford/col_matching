<!-- {"case_id": "case_perkins_robt-clerk_e1902", "bio_ids": ["perkins_robt-clerk_e1902", "perkins_robt-clerk_e1902-2"], "stint_ids": ["Perkins, R. Clark___South Africa___1912"]} -->
# Dossier case_perkins_robt-clerk_e1902

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 32 official(s) with this surname in the graph's staff lists; 19 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Perkins, R. Clark___South Africa___1912'] have more than one claimant biography in this case.

## Biography `perkins_robt-clerk_e1902`

- Printed name: **PERKINS, ROBT. CLERK**
- Birth year: not printed
- Honours: D.S.O, L.R.C.P, M.R.C.S
- Appears in editions: [1909, 1910, 1911, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1909-L48971.v` — printed in editions [1909, 1910, 1911, 1913, 1914, 1915]:**

> PERKINS, ROBT. CLERK, D.S.O., M.R.C.S., L.R.C.P.—Med. offr., S.A.C., and ag. dist. surg., Swaziland, 1902 to 1907; is now med. offr. to Swaziland adminstr.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902–1907 | Med. offr., S.A.C., and ag. dist. surg. | Swaziland | [1909, 1910, 1911, 1913, 1914, 1915] |

## Biography `perkins_robt-clerk_e1902-2`

- Printed name: **PERKINS, ROBT. CLERK**
- Birth year: not printed
- Honours: D.S.O., L.R.C.P., M.R.C.S.
- Appears in editions: [1912]

### Verbatim printed entry text (OCR)

**Version `col1912-L46866.v` — printed in editions [1912]:**

> PERKINS, ROBT. CLERK, D.S.O., M.R.C.S., L.R.C.P.—MED. OFFR., S.A.C., AND AG. DIST. SURVR., SWAZILAND, 1902 TO 1907; IS NOW MED. OFFR. TO SWAZILAND ADMSTR.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902–1907 | MED. OFFR., S.A.C., AND AG. DIST. SURVR. | Swaziland | [1912] |
| 1 | ? | MED. OFFR. | Swaziland | [1912] |

## Candidate stint `Perkins, R. Clark___South Africa___1912`

- Staff-list name: **Perkins, R. Clark** | colony: **South Africa** | listed 1912–1914 | editions [1912, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | R. Clark Perkins | Medical Officer | Medical Department | D.S.O. | Captain |
| 1914 | R. Clark Perkins | Government Medical Officer and Resident Justice of the Peace | Medical Department | D.S.O. | Captain |

### Deterministic checks: `perkins_robt-clerk_e1902` vs `Perkins, R. Clark___South Africa___1912`

- [PASS] surname_gate: bio 'PERKINS' vs stint 'Perkins, R. Clark' (exact)
- [PASS] initials: bio ['R', 'C'] ~ stint ['R', 'C']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1914
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: D.S.O
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `perkins_robt-clerk_e1902-2` vs `Perkins, R. Clark___South Africa___1912`

- [PASS] surname_gate: bio 'PERKINS' vs stint 'Perkins, R. Clark' (exact)
- [PASS] initials: bio ['R', 'C'] ~ stint ['R', 'C']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1914
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: D.S.O.
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

