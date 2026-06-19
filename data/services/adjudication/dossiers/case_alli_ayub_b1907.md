<!-- {"case_id": "case_alli_ayub_b1907", "bio_ids": ["alli_ayub_b1907"], "stint_ids": ["Alli, J. A___British Guiana___1961", "Alli, Pengiran Abu Baker bin Pengiran Omar___Brunei___1949"]} -->
# Dossier case_alli_ayub_b1907

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['alli_ayub_b1907'] carry a single initial only — the namesake trap applies.

## Biography `alli_ayub_b1907`

- Printed name: **ALLI, Ayub**
- Birth year: 1907 (attested in editions [1963])
- Honours: M.B.E, O.B.E (1956)
- Appears in editions: [1963]

### Verbatim printed entry text (OCR)

**Version `col1963-L16797.v` — printed in editions [1963]:**

> ALLI, Ayub, O.B.E. (1956), M.B.E.—b. 1907; ed. Govt. Indian Sch., Nairobi; clk., sec't, Ken., 1920; asst. estab. offr., 1944; estab. offr., 1948; asst. sec. (estab.), 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | clk., sec't | Kenya | [1963] |
| 1 | 1944 | asst. estab. offr | Kenya *(inherited from previous clause)* | [1963] |
| 2 | 1948 | estab. offr | Kenya *(inherited from previous clause)* | [1963] |
| 3 | 1955 | asst. sec. (estab.) | Kenya *(inherited from previous clause)* | [1963] |

## Candidate stint `Alli, J. A___British Guiana___1961`

- Staff-list name: **Alli, J. A** | colony: **British Guiana** | listed 1961–1965 | editions [1961, 1963, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | J. A. Alli | Deputy Commissioner of Inland Revenue | Civil Establishment | — | — |
| 1963 | J. A. Alli | Deputy Commissioner of Inland Revenue | Civil Establishment | — | — |
| 1964 | J. A. Alli | Deputy Commissioner of Inland Revenue | Civil Establishment | — | — |
| 1965 | J. A. Alli | Deputy Commissioner of Inland Revenue | Civil Establishment | — | — |

### Deterministic checks: `alli_ayub_b1907` vs `Alli, J. A___British Guiana___1961`

- [PASS] surname_gate: bio 'ALLI' vs stint 'Alli, J. A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1961, birth 1907 (age 54)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1965
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Alli, Pengiran Abu Baker bin Pengiran Omar___Brunei___1949`

- Staff-list name: **Alli, Pengiran Abu Baker bin Pengiran Omar** | colony: **Brunei** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | Pengiran Abu Baker bin Pengiran Omar Alli | District Officer | Land and District Offices | — | — |
| 1950 | Pengiran Abu Baker bin Pengiran Omar Alli | District Officer | Land and District Offices | — | — |
| 1951 | Pengiran Abu Baker bin Pengiran Omar Alli | District Officer | LAND AND DISTRICT OFFICES | — | — |

### Deterministic checks: `alli_ayub_b1907` vs `Alli, Pengiran Abu Baker bin Pengiran Omar___Brunei___1949`

- [PASS] surname_gate: bio 'ALLI' vs stint 'Alli, Pengiran Abu Baker bin Pengiran Omar' (exact)
- [PASS] initials: bio ['A'] ~ stint ['P', 'A', 'B', 'B', 'P', 'O']
- [PASS] age_gate: stint starts 1949, birth 1907 (age 42)
- [FAIL] colony: no placed event resolves to 'Brunei'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

