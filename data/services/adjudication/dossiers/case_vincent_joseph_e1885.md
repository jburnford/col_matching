<!-- {"case_id": "case_vincent_joseph_e1885", "bio_ids": ["vincent_joseph_e1885"], "stint_ids": ["Vincent, J___Rhodesia___1908", "Vincent, J___Swaziland___1908", "Vincent, Jos. U___Canada___1915"]} -->
# Dossier case_vincent_joseph_e1885

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['vincent_joseph_e1885'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Vincent, J___Rhodesia___1908` is also gate-compatible with biography(ies) outside this case: ['vincent_joseph-ulric_b1872'] (already linked elsewhere or filtered).
- NOTE: stint `Vincent, J___Swaziland___1908` is also gate-compatible with biography(ies) outside this case: ['vincent_joseph-ulric_b1872'] (already linked elsewhere or filtered).
- NOTE: stint `Vincent, Jos. U___Canada___1915` is also gate-compatible with biography(ies) outside this case: ['vincent_joseph-ulric_b1872'] (already linked elsewhere or filtered).

## Biography `vincent_joseph_e1885`

- Printed name: **VINCENT, JOSEPH**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L36520.v` — printed in editions [1888, 1889, 1890]:**

> VINCENT, JOSEPH.—Clerk to R.M., Taungs, Bechuanaland, Oct., 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1885 | Clerk to R.M., Taungs | Bechuanaland | [1888, 1889, 1890] |

## Candidate stint `Vincent, J___Rhodesia___1908`

- Staff-list name: **Vincent, J** | colony: **Rhodesia** | listed 1908–1910 | editions [1908, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | J. Vincent | Senior Judge | High Court | — | — |
| 1910 | J. Vincent | Senior Judge | High Court | — | — |

### Deterministic checks: `vincent_joseph_e1885` vs `Vincent, J___Rhodesia___1908`

- [PASS] surname_gate: bio 'VINCENT' vs stint 'Vincent, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1910
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Vincent, J___Swaziland___1908`

- Staff-list name: **Vincent, J** | colony: **Swaziland** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | J. Vincent | Senior Judge | High Court | — | — |
| 1909 | J. Vincent | Senior Judge | High Court | — | — |

### Deterministic checks: `vincent_joseph_e1885` vs `Vincent, J___Swaziland___1908`

- [PASS] surname_gate: bio 'VINCENT' vs stint 'Vincent, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Swaziland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Vincent, Jos. U___Canada___1915`

- Staff-list name: **Vincent, Jos. U** | colony: **Canada** | listed 1915–1918 | editions [1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | Jos. U. Vincent | Deputy Minister of Inland Revenue | Department of Inland Revenue | — | — |
| 1917 | Jos. U. Vincent | Deputy Minister of Inland Revenue | Inland Revenue | — | — |
| 1918 | Jos. U. Vincent | Deputy Minister of Inland Revenue | Department of Inland Revenue | — | — |

### Deterministic checks: `vincent_joseph_e1885` vs `Vincent, Jos. U___Canada___1915`

- [PASS] surname_gate: bio 'VINCENT' vs stint 'Vincent, Jos. U' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'U']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1918
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

