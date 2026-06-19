<!-- {"case_id": "case_noad_george-edward_b1902", "bio_ids": ["noad_george-edward_b1902"], "stint_ids": ["Noad, G. E___Zanzibar___1937"]} -->
# Dossier case_noad_george-edward_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `noad_george-edward_b1902`

- Printed name: **NOAD, George Edward**
- Birth year: 1902 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L34948.v` — printed in editions [1948, 1949, 1950, 1951]:**

> NOAD, George Edward.—b. 1902 ; ed. Sedbergh and Camb. ; prov. admin., Ken., 1926 ; N. Rhod., 1926 ; dist. comsnr., Zanz., 1936 ; Ken., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | prov. admin. | Kenya | [1948, 1949, 1950, 1951] |
| 1 | 1936 | dist. comsnr. | Zanzibar | [1948, 1949, 1950, 1951] |
| 2 | 1947 | dist. comsnr. | Kenya | [1948, 1949, 1950, 1951] |

## Candidate stint `Noad, G. E___Zanzibar___1937`

- Staff-list name: **Noad, G. E** | colony: **Zanzibar** | listed 1937–1940 | editions [1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | G. E. Noad | Administrative Officer (2nd Grade) | Secretariat and Administration | — | — |
| 1940 | G. E. Noad | Administrative Officer | Administration | — | — |

### Deterministic checks: `noad_george-edward_b1902` vs `Noad, G. E___Zanzibar___1937`

- [PASS] surname_gate: bio 'NOAD' vs stint 'Noad, G. E' (exact)
- [PASS] initials: bio ['G', 'E'] ~ stint ['G', 'E']
- [PASS] age_gate: stint starts 1937, birth 1902 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Zanzibar'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 30 vs bar 60: 'dist. comsnr.' ~ 'Administrative Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

