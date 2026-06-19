<!-- {"case_id": "case_gregory-smith_henry-graham_b1899", "bio_ids": ["gregory-smith_henry-graham_b1899"], "stint_ids": ["Gregory-Smith, H. G___Western Pacific___1951"]} -->
# Dossier case_gregory-smith_henry-graham_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gregory-smith_henry-graham_b1899`

- Printed name: **GREGORY-SMITH, Henry Graham**
- Birth year: 1899 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32994.v` — printed in editions [1948, 1949, 1950, 1951]:**

> GREGORY-SMITH, Henry Graham.—b. 1899 ; ed. Rugby and Sandhurst ; on mil. serv. 1918, lieut. and 1940-42, maj. ; admin. offr., Ken., 1929 ; comsnr. of the interior, B. Guiana, 1946 ; mem., settlement comsnr., 1947 ; res. comsnr., B. Sol. Is. Prot., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | admin. offr. | Kenya | [1948, 1949, 1950, 1951] |
| 1 | 1946 | comsnr. of the interior, B. Guiana | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1947 | mem., settlement comsnr | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1950 | res. comsnr., B. Sol. Is. Prot | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Gregory-Smith, H. G___Western Pacific___1951`

- Staff-list name: **Gregory-Smith, H. G** | colony: **Western Pacific** | listed 1951–1952 | editions [1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | H. G. Gregory-Smith | Resident Commissioner | Civil Establishment | — | — |
| 1951 | H. G. Gregory-Smith | Resident Commissioner | Resident Commissioners | — | — |
| 1952 | H. G. Gregory-Smith | Resident Commissioner | Civil Establishment | — | — |

### Deterministic checks: `gregory-smith_henry-graham_b1899` vs `Gregory-Smith, H. G___Western Pacific___1951`

- [PASS] surname_gate: bio 'GREGORY-SMITH' vs stint 'Gregory-Smith, H. G' (exact)
- [PASS] initials: bio ['H', 'G'] ~ stint ['H', 'G']
- [PASS] age_gate: stint starts 1951, birth 1899 (age 52)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1951-1952
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

