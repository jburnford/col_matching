<!-- {"case_id": "case_codrington_r-e_e1890", "bio_ids": ["codrington_r-e_e1890"], "stint_ids": ["Codrington, R. E___Northern Rhodesia___1946", "Codrington, Robert___Rhodesia___1900"]} -->
# Dossier case_codrington_r-e_e1890

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `codrington_r-e_e1890`

- Printed name: **CODRINGTON, R. E**
- Birth year: not printed
- Appears in editions: [1910, 1911, 1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1910-L44968.v` — printed in editions [1910, 1911, 1912, 1913]:**

> CODRINGTON, R. E.—Ed. at Marlborough; joined Boch. Border pol., 1890; served through Matabele war (medal); collr. of revenues, B.C. Africa, 1895 (Cent. Africa medal); dep. admstr., N.E. Rhodesia, 1898; admstr., June, 1900; admstr., N.W. Rhodesia, 16th May, 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890 | joined Boch. Border pol | — | [1910, 1911, 1912, 1913] |
| 1 | 1895 | collr. of revenues, B.C. Africa | British Columbia | [1910, 1911, 1912, 1913] |
| 2 | 1898 | dep. admstr., N.E. Rhodesia | British Columbia *(inherited from previous clause)* | [1910, 1911, 1912, 1913] |
| 3 | 1900 | admstr | British Columbia *(inherited from previous clause)* | [1910, 1911, 1912, 1913] |
| 4 | 1907 | admstr., N.W. Rhodesia | British Columbia *(inherited from previous clause)* | [1910, 1911, 1912, 1913] |

## Candidate stint `Codrington, R. E___Northern Rhodesia___1946`

- Staff-list name: **Codrington, R. E** | colony: **Northern Rhodesia** | listed 1946–1948 | editions [1946, 1948]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1946 | R. E. Codrington | Administrator, North Eastern Rhodesia | Administrators | — | — |
| 1948 | R. E. Codrington | Administrator | ADMINISTRATORS | — | — |

### Deterministic checks: `codrington_r-e_e1890` vs `Codrington, R. E___Northern Rhodesia___1946`

- [PASS] surname_gate: bio 'CODRINGTON' vs stint 'Codrington, R. E' (exact)
- [PASS] initials: bio ['R', 'E'] ~ stint ['R', 'E']
- [PASS] age_gate: stint starts 1946; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1946-1948
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Codrington, Robert___Rhodesia___1900`

- Staff-list name: **Codrington, Robert** | colony: **Rhodesia** | listed 1900–1906 | editions [1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1900 | Deputy Administrator of North-Eastern Rhodesia, R. Codrington. | Deputy Administrator of North-Eastern Rhodesia | Board of Directors | — | — |
| 1905 | Robert Codrington | Administrator | North-Eastern Rhodesia | — | — |
| 1906 | Robert Codrington | Administrator | North-Eastern Rhodesia | — | — |

### Deterministic checks: `codrington_r-e_e1890` vs `Codrington, Robert___Rhodesia___1900`

- [PASS] surname_gate: bio 'CODRINGTON' vs stint 'Codrington, Robert' (exact)
- [PASS] initials: bio ['R', 'E'] ~ stint ['R']
- [PASS] age_gate: stint starts 1900; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1900-1906
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

