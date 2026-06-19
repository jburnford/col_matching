<!-- {"case_id": "case_brookes_e-c_b1933", "bio_ids": ["brookes_e-c_b1933"], "stint_ids": ["Brookes, E. C___Western Pacific___1965"]} -->
# Dossier case_brookes_e-c_b1933

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `brookes_e-c_b1933`

- Printed name: **BROOKES, E. C**
- Birth year: 1933 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L13466.v` — printed in editions [1966]:**

> BROOKES, E. C.—b. 1933; ed. Prince of Wales Sch., Nairobi; mil. serv., 1951-52, capt.; admin. offr., Ken., 1953; G. and E.I.C., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | admin. offr. | Kenya | [1966] |
| 1 | 1964 | G. and E.I.C | Kenya *(inherited from previous clause)* | [1966] |

## Candidate stint `Brookes, E. C___Western Pacific___1965`

- Staff-list name: **Brookes, E. C** | colony: **Western Pacific** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | E. C. Brookes | Administrative Officer | Civil Establishment | — | — |
| 1966 | E. C. Brookes | Administrative Officer (Class B) | Civil Establishment | — | — |

### Deterministic checks: `brookes_e-c_b1933` vs `Brookes, E. C___Western Pacific___1965`

- [PASS] surname_gate: bio 'BROOKES' vs stint 'Brookes, E. C' (exact)
- [PASS] initials: bio ['E', 'C'] ~ stint ['E', 'C']
- [PASS] age_gate: stint starts 1965, birth 1933 (age 32)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1965-1966
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

