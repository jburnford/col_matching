<!-- {"case_id": "case_edye_h-m_e1882", "bio_ids": ["edye_h-m_e1882"], "stint_ids": ["Edye, H. M. B___Cape of Good Hope___1877", "Edye, H. M. B___Cape of Good Hope___1890", "Edye, H. M. B___Cape of Good Hope___1906"]} -->
# Dossier case_edye_h-m_e1882

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Edye, H. M. B___Cape of Good Hope___1877` is also gate-compatible with biography(ies) outside this case: ['edye_h-m_e1882-2'] (already linked elsewhere or filtered).
- NOTE: stint `Edye, H. M. B___Cape of Good Hope___1890` is also gate-compatible with biography(ies) outside this case: ['edye_h-m_e1882-2'] (already linked elsewhere or filtered).
- NOTE: stint `Edye, H. M. B___Cape of Good Hope___1906` is also gate-compatible with biography(ies) outside this case: ['edye_h-m_e1882-2'] (already linked elsewhere or filtered).

## Biography `edye_h-m_e1882`

- Printed name: **EDYE, H. M**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L33202.v` — printed in editions [1886, 1888, 1889, 1890]:**

> EDYE, H. M.—Resident magistrate, Riversdale Division, Cape Colony, 13th January, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Resident magistrate, Riversdale Division | Cape of Good Hope | [1886, 1888, 1889, 1890] |

## Candidate stint `Edye, H. M. B___Cape of Good Hope___1877`

- Staff-list name: **Edye, H. M. B** | colony: **Cape of Good Hope** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. M. Edye | Clerk | Police Branch | — | — |
| 1878 | H. M. Edye | 1st Clerk | DIVISION OF PORT ELIZABETH | — | — |

### Deterministic checks: `edye_h-m_e1882` vs `Edye, H. M. B___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'EDYE' vs stint 'Edye, H. M. B' (exact)
- [PASS] initials: bio ['H', 'M'] ~ stint ['H', 'M', 'B']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Edye, H. M. B___Cape of Good Hope___1890`

- Staff-list name: **Edye, H. M. B** | colony: **Cape of Good Hope** | listed 1890–1896 | editions [1890, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | H. M. Edye | C.C. and R.M. | DIVISION OF BEDFORD | — | — |
| 1896 | H. M. Edye | R.M. | DIVISION OF PIQUETBERG | — | — |

### Deterministic checks: `edye_h-m_e1882` vs `Edye, H. M. B___Cape of Good Hope___1890`

- [PASS] surname_gate: bio 'EDYE' vs stint 'Edye, H. M. B' (exact)
- [PASS] initials: bio ['H', 'M'] ~ stint ['H', 'M', 'B']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1890-1896
- [FAIL] position_sim: best 17 vs bar 60: 'Resident magistrate, Riversdale Division' ~ 'C.C. and R.M.'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Edye, H. M. B___Cape of Good Hope___1906`

- Staff-list name: **Edye, H. M. B** | colony: **Cape of Good Hope** | listed 1906–1908 | editions [1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | H. M. Edye | Third Class Clerk | Treasury | — | — |
| 1907 | H. M. B. Edye | Third Class Clerks | Treasury | — | — |
| 1908 | H. M. B. Edye | Third Class Clerk | Treasury | — | — |

### Deterministic checks: `edye_h-m_e1882` vs `Edye, H. M. B___Cape of Good Hope___1906`

- [PASS] surname_gate: bio 'EDYE' vs stint 'Edye, H. M. B' (exact)
- [PASS] initials: bio ['H', 'M'] ~ stint ['H', 'M', 'B']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1908
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

