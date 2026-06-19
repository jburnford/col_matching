<!-- {"case_id": "case_dunn_robert-ernest_e1880", "bio_ids": ["dunn_robert-ernest_e1880"], "stint_ids": ["Dunn, E___Northern Rhodesia___1949", "Dunn, R. E___Natal___1905"]} -->
# Dossier case_dunn_robert-ernest_e1880

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 33 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Dunn, E___Northern Rhodesia___1949` is also gate-compatible with biography(ies) outside this case: ['dunn_eric-geoffrey-rendell_b1902', 'dunn_robert-ernst_e1880'] (already linked elsewhere or filtered).
- NOTE: stint `Dunn, R. E___Natal___1905` is also gate-compatible with biography(ies) outside this case: ['dunn_robert-ernst_e1880'] (already linked elsewhere or filtered).

## Biography `dunn_robert-ernest_e1880`

- Printed name: **DUNN, ROBERT ERNEST**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L27277.v` — printed in editions [1883, 1886, 1888, 1890]:**

> DUNN, ROBERT ERNEST.—Clerk and interpreter to the resident Umgeni Division, Natal, June, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Clerk and interpreter to the resident Umgeni Division | Natal | [1883, 1886, 1888, 1890] |

## Candidate stint `Dunn, E___Northern Rhodesia___1949`

- Staff-list name: **Dunn, E** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. Dunn | Master | Education | — | — |
| 1951 | E. Dunn | Master | Education | — | — |

### Deterministic checks: `dunn_robert-ernest_e1880` vs `Dunn, E___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'DUNN' vs stint 'Dunn, E' (exact)
- [PASS] initials: bio ['R', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Dunn, R. E___Natal___1905`

- Staff-list name: **Dunn, R. E** | colony: **Natal** | listed 1905–1906 | editions [1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | R. E. Dunn | Magistrate | Native High Court | — | — |
| 1906 | R. E. Dunn | Magistrate | Magistrates | — | — |

### Deterministic checks: `dunn_robert-ernest_e1880` vs `Dunn, R. E___Natal___1905`

- [PASS] surname_gate: bio 'DUNN' vs stint 'Dunn, R. E' (exact)
- [PASS] initials: bio ['R', 'E'] ~ stint ['R', 'E']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Natal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1906
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

