<!-- {"case_id": "case_abine_neville-warde_b1910", "bio_ids": ["abine_neville-warde_b1910"], "stint_ids": ["Sabine, N. W___North Borneo___1949"]} -->
# Dossier case_abine_neville-warde_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Sabine, N. W___North Borneo___1949` is also gate-compatible with biography(ies) outside this case: ['sabine_neville-warde_b1910'] (already linked elsewhere or filtered).

## Biography `abine_neville-warde_b1910`

- Printed name: **ABINE, NEVILLE WARDE**
- Birth year: 1910 (attested in editions [1937])
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L64435.v` — printed in editions [1937]:**

> ABINE, NEVILLE WARDE, B.A.—B. 1910; Chortlon-cum-Hardy Manchester Gram-r Schol. and Brasenose Coll., Oxford; col. dit dept., Feb., 1934; ast. audr., Gold Coast, 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | col. dit dept | — | [1937] |
| 1 | 1934 | ast. audr. | Gold Coast | [1937] |

## Candidate stint `Sabine, N. W___North Borneo___1949`

- Staff-list name: **Sabine, N. W** | colony: **North Borneo** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | N. Sabine | Principal Auditor | AUDIT | — | — |
| 1950 | N. W. Sabine | Principal Auditor | Audit | — | — |
| 1951 | N. W. Sabine | Principal Auditor | AUDIT | — | — |

### Deterministic checks: `abine_neville-warde_b1910` vs `Sabine, N. W___North Borneo___1949`

- [PASS] surname_gate: bio 'ABINE' vs stint 'Sabine, N. W' (fuzzy:1)
- [PASS] initials: bio ['N', 'W'] ~ stint ['N', 'W']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [FAIL] colony: no placed event resolves to 'North Borneo'
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

