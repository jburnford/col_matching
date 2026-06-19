<!-- {"case_id": "case_fetherstonhaugh_alfred-hardinge_b1901", "bio_ids": ["fetherstonhaugh_alfred-hardinge_b1901"], "stint_ids": ["Fetherstonhaugh, A. H___Federation of Malaya___1950"]} -->
# Dossier case_fetherstonhaugh_alfred-hardinge_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fetherstonhaugh_alfred-hardinge_b1901`

- Printed name: **FETHERSTONHAUGH, Alfred Hardinge**
- Birth year: 1901 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L31999.v` — printed in editions [1949, 1950, 1951]:**

> FETHERSTONHAUGH, Alfred Hardinge—b. 1901; ed. St. Bee's Sch., Cumberland and Trinity Coll., Dublin; on war serv. 1918–19 and 1941–46, lt.; dist. inspr., R.I.C., 1920; asst. game warden, F.M.S., 1928; control offr., game dept., Mal.; ch. game warden, 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | dist. inspr., R.I.C | — | [1949, 1950, 1951] |
| 1 | 1928 | asst. game warden | Federated Malay States | [1949, 1950, 1951] |
| 2 | 1949 | ch. game warden | Federated Malay States *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Fetherstonhaugh, A. H___Federation of Malaya___1950`

- Staff-list name: **Fetherstonhaugh, A. H** | colony: **Federation of Malaya** | listed 1950–1952 | editions [1950, 1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | A. H. Fetherstonhaugh | Chief Game Warden | Civil Establishment | — | — |
| 1951 | A. H. Fetherstonhaugh | Chief Game Warden | GAME | — | — |
| 1952 | A. H. Fetherstonhaugh | Chief Game Warden | Civil Establishment | — | — |

### Deterministic checks: `fetherstonhaugh_alfred-hardinge_b1901` vs `Fetherstonhaugh, A. H___Federation of Malaya___1950`

- [PASS] surname_gate: bio 'FETHERSTONHAUGH' vs stint 'Fetherstonhaugh, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1950, birth 1901 (age 49)
- [FAIL] colony: no placed event resolves to 'Federation of Malaya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1952
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

