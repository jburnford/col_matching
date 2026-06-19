<!-- {"case_id": "case_pendlebury_henry-maurice_b1893", "bio_ids": ["pendlebury_henry-maurice_b1893"], "stint_ids": ["Pendlebury, H. M___Straits Settlements___1931"]} -->
# Dossier case_pendlebury_henry-maurice_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pendlebury_henry-maurice_b1893`

- Printed name: **PENDLEBURY, HENRY MAURICE**
- Birth year: 1893 (attested in editions [1937, 1939, 1940])
- Honours: F.R.E.S, F.Z.S
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L63831.v` — printed in editions [1937, 1939, 1940]:**

> PENDLEBURY, CAPT. HENRY MAURICE, F.R.E.S., F.Z.S.—B. 1893; ed. Shrewsbury Schi. and R. Coll. of Sc., London; 2nd lieut., Kings Shropshire Ld. Infnty., Sept., 1914; lieut., Feb., 1915; capt., July, 1915; demob., Sept., 1919; syst. entomologist, F.M.S., Apr., 1921; curator, Selangor museum, Jan., 1932; hon. dy. game warden, Selangor, in addn., Sept., 1934; dir., museums, F.M.S., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | 2nd lieut., Kings Shropshire Ld. Infnty | — | [1937, 1939, 1940] |
| 1 | 1915 | lieut | — | [1937, 1939, 1940] |
| 2 | 1915 | capt | — | [1937, 1939, 1940] |
| 3 | 1919 | demob | — | [1937, 1939, 1940] |
| 4 | 1921 | syst. entomologist | Federated Malay States | [1937, 1939, 1940] |
| 5 | 1932 | curator, Selangor museum | Federated Malay States *(inherited from previous clause)* | [1937, 1939, 1940] |
| 6 | 1934 | hon. dy. game warden, Selangor, in addn | Federated Malay States *(inherited from previous clause)* | [1937, 1939, 1940] |
| 7 | 1937 | dir., museums | Federated Malay States | [1937, 1939, 1940] |

## Candidate stint `Pendlebury, H. M___Straits Settlements___1931`

- Staff-list name: **Pendlebury, H. M** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | H. M. Pendlebury | Systematic Entomologist | Museums | — | — |
| 1933 | H. M. Pendlebury | Systematic Entomologist | Museums | — | — |

### Deterministic checks: `pendlebury_henry-maurice_b1893` vs `Pendlebury, H. M___Straits Settlements___1931`

- [PASS] surname_gate: bio 'PENDLEBURY' vs stint 'Pendlebury, H. M' (exact)
- [PASS] initials: bio ['H', 'M'] ~ stint ['H', 'M']
- [PASS] age_gate: stint starts 1931, birth 1893 (age 38)
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

