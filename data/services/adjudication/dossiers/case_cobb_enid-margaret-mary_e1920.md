<!-- {"case_id": "case_cobb_enid-margaret-mary_e1920", "bio_ids": ["cobb_enid-margaret-mary_e1920"], "stint_ids": ["Cobb, E. M___Straits Settlements___1931"]} -->
# Dossier case_cobb_enid-margaret-mary_e1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cobb_enid-margaret-mary_e1920`

- Printed name: **COBB, Enid Margaret Mary**
- Birth year: not printed
- Appears in editions: [1932, 1934]

### Verbatim printed entry text (OCR)

**Version `col1932-L59197.v` — printed in editions [1932, 1934]:**

> COBB, Enid Margaret Mary, M.R.C.S. (Eng.), L.R.C.P. (Lond.), D.T.M. (Liverpool).—Med. offr., F.M.S., Apr., 1920; infant welfare centre, Taiping, Mar., 1928; gen. hosp., Kuala Lumpur, Aug., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | Med. offr. | Federated Malay States | [1932, 1934] |
| 1 | 1928 | infant welfare centre, Taiping | Federated Malay States *(inherited from previous clause)* | [1932, 1934] |
| 2 | 1929 | gen. hosp., Kuala Lumpur | Federated Malay States *(inherited from previous clause)* | [1932, 1934] |

## Candidate stint `Cobb, E. M___Straits Settlements___1931`

- Staff-list name: **Cobb, E. M** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | E. M. Cobb | Lady Medical Officer | Medical | — | — |
| 1932 | E. M. Cobb | Lady Medical Officer | Medical | — | — |
| 1933 | E. M. Cobb | Lady Medical Officer | Medical | — | — |

### Deterministic checks: `cobb_enid-margaret-mary_e1920` vs `Cobb, E. M___Straits Settlements___1931`

- [PASS] surname_gate: bio 'COBB' vs stint 'Cobb, E. M' (exact)
- [PASS] initials: bio ['E', 'M', 'M'] ~ stint ['E', 'M']
- [PASS] age_gate: stint starts 1931; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

