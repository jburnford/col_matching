<!-- {"case_id": "case_beattie_h-r-m_b1916", "bio_ids": ["beattie_h-r-m_b1916"], "stint_ids": ["Beattie, H. R. M___Sierra Leone___1948", "Beattie, H. R. M___Sierra Leone___1957"]} -->
# Dossier case_beattie_h-r-m_b1916

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `beattie_h-r-m_b1916`

- Printed name: **BEATTIE, H. R. M.**
- Birth year: 1916 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1956-L19687.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> BEATTIE, H. R. M.—b. 1916; ed. Geo. Heriot's Sch., Edin. and London Univs.; cadet, S.L., 1940; asst. dist. comsnr., 1943; dist. comsnr., 1949; perm. sec., 1956 provincial comsnr., 1957-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | cadet | Sierra Leone | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1943 | asst. dist. comsnr. | — | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1949 | dist. comsnr. | — | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 3 | 1956 | perm. sec. | — | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 4 | 1957–1961 | provincial comsnr. | — | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Beattie, H. R. M___Sierra Leone___1948`

- Staff-list name: **Beattie, H. R. M** | colony: **Sierra Leone** | listed 1948–1951 | editions [1948, 1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1948 | H. R. M. Beattie | Clerk of Executive Council | Executive Council | — | — |
| 1949 | H. R. M. Beattie | Assistant District Commissioners and Cadets | Provincial Administration | — | — |
| 1950 | H. R. M. Beattie | District Commissioners | Provincial Administration | — | — |
| 1951 | H. R. M. Beattie | District Commissioner | Provincial Administration | — | — |

### Deterministic checks: `beattie_h-r-m_b1916` vs `Beattie, H. R. M___Sierra Leone___1948`

- [PASS] surname_gate: bio 'BEATTIE' vs stint 'Beattie, H. R. M' (exact)
- [PASS] initials: bio ['H', 'R', 'M'] ~ stint ['H', 'R', 'M']
- [PASS] age_gate: stint starts 1948, birth 1916 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1948-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Beattie, H. R. M___Sierra Leone___1957`

- Staff-list name: **Beattie, H. R. M** | colony: **Sierra Leone** | listed 1957–1960 | editions [1957, 1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | H. R. M. Beattie | Permanent Secretary | Civil Establishment | — | — |
| 1958 | H. R. M. Beattie | Provincial Commissioner | Civil Establishment | — | — |
| 1959 | H. R. M. Beattie | Provincial Commissioner | Civil Establishment | — | — |
| 1960 | H. R. M. Beattie | Provincial Commissioner | Civil Establishment | — | — |

### Deterministic checks: `beattie_h-r-m_b1916` vs `Beattie, H. R. M___Sierra Leone___1957`

- [PASS] surname_gate: bio 'BEATTIE' vs stint 'Beattie, H. R. M' (exact)
- [PASS] initials: bio ['H', 'R', 'M'] ~ stint ['H', 'R', 'M']
- [PASS] age_gate: stint starts 1957, birth 1916 (age 41)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1960
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

