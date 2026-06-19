<!-- {"case_id": "case_wravy_leonard-jun_e1872", "bio_ids": ["wravy_leonard-jun_e1872"], "stint_ids": ["Wray, L___Federated Malay States___1906"]} -->
# Dossier case_wravy_leonard-jun_e1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Wray, L___Federated Malay States___1906` is also gate-compatible with biography(ies) outside this case: ['wray_leonard-jun_b1852'] (already linked elsewhere or filtered).

## Biography `wravy_leonard-jun_e1872`

- Printed name: **WRAVY, LEONARD, JUN.**
- Birth year: not printed
- Appears in editions: [1899]

### Verbatim printed entry text (OCR)

**Version `col1899-L38039.v` — printed in editions [1899]:**

> WRAVY, LEONARD, JUN.—Elected mem., teleg. engrs., 1877; mem., Photographic Soc., London, 1872; mem., Straits Roy. Asiatic Soc., 1884; F.Z.S., 1888, entered pub. wks. dept., Perak govt service, June, 1881; supt., Govt. Hill Garden, Larut Jan., 1882; and curator, Perak state museum, Jan., 1883; also state geologist, Jan., 1890.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872 | mem., Photographic Soc. | London | [1899] |
| 1 | 1877 | mem., teleg. engrs. | — | [1899] |
| 2 | 1881 | pub. wks. dept. | Perak | [1899] |
| 3 | 1882 | supt., Govt. Hill Garden | — | [1899] |
| 4 | 1883 | curator, Perak state museum | Perak | [1899] |
| 5 | 1884 | mem., Straits Roy. Asiatic Soc. | Straits Settlements | [1899] |
| 6 | 1888 | F.Z.S. | — | [1899] |
| 7 | 1890 | state geologist | — | [1899] |

## Candidate stint `Wray, L___Federated Malay States___1906`

- Staff-list name: **Wray, L** | colony: **Federated Malay States** | listed 1906–1908 | editions [1906, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | L. Wray | Director of Museums | — | — | — |
| 1908 | L. Wray | Director of Museums | Civil Establishment | — | — |

### Deterministic checks: `wravy_leonard-jun_e1872` vs `Wray, L___Federated Malay States___1906`

- [PASS] surname_gate: bio 'WRAVY' vs stint 'Wray, L' (fuzzy:1)
- [PASS] initials: bio ['L', 'J'] ~ stint ['L']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Federated Malay States'
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

