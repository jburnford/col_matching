<!-- {"case_id": "case_cornish_h-e_b1904", "bio_ids": ["cornish_h-e_b1904"], "stint_ids": ["Cornish, H. E___Sarawak___1952"]} -->
# Dossier case_cornish_h-e_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cornish_h-e_b1904`

- Printed name: **CORNISH, H. E**
- Birth year: 1904 (attested in editions [1953, 1954, 1955, 1956])
- Appears in editions: [1953, 1954, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1953-L16975.v` — printed in editions [1953, 1954, 1955, 1956]:**

> CORNISH, H. E.—b. 1904; engnr., P. & T., S.S. & F.M.S., 1928; asst. contrlr. telecoms. (engnr.), 1948; contrlr., telecoms., Sarawak, 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | engnr., P. & T., S.S. & F.M.S | Straits Settlements | [1953, 1954, 1955, 1956] |
| 1 | 1948 | asst. contrlr. telecoms. (engnr.) | Straits Settlements *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 2 | 1952 | contrlr., telecoms. | Sarawak | [1953, 1954, 1955, 1956] |

## Candidate stint `Cornish, H. E___Sarawak___1952`

- Staff-list name: **Cornish, H. E** | colony: **Sarawak** | listed 1952–1955 | editions [1952, 1953, 1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | H. E. Cornish | Postmaster-General | Civil Establishment | — | — |
| 1953 | H. E. Cornish | Postmaster-General | Civil Establishment | — | — |
| 1954 | H. E. Cornish | Postmaster-General | Civil Establishment | — | — |
| 1955 | H. E. Cornish | Postmaster-General | Civil Establishment | — | — |

### Deterministic checks: `cornish_h-e_b1904` vs `Cornish, H. E___Sarawak___1952`

- [PASS] surname_gate: bio 'CORNISH' vs stint 'Cornish, H. E' (exact)
- [PASS] initials: bio ['H', 'E'] ~ stint ['H', 'E']
- [PASS] age_gate: stint starts 1952, birth 1904 (age 48)
- [PASS] colony: 1 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1952-1955
- [FAIL] position_sim: best 30 vs bar 60: 'contrlr., telecoms.' ~ 'Postmaster-General'
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

