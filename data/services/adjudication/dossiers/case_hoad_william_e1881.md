<!-- {"case_id": "case_hoad_william_e1881", "bio_ids": ["hoad_william_e1881"], "stint_ids": ["Hoad, W___Straits Settlements___1894"]} -->
# Dossier case_hoad_william_e1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hoad_william_e1881'] carry a single initial only — the namesake trap applies.

## Biography `hoad_william_e1881`

- Printed name: **HOAD, William**
- Birth year: not printed
- Honours: C.M, M.B
- Appears in editions: [1888, 1889, 1890, 1894, 1896]

### Verbatim printed entry text (OCR)

**Version `col1888-L34035.v` — printed in editions [1888, 1889, 1890, 1894, 1896]:**

> HOAD, William, M.B., C.M., Edin.—Assistant medical officer and J.P., Seychelles, Nov., 1881; acting government medical officer, Mahé, Aug., 1884; government medical officer, Seychelles, 1885; district medical officer, Larnaca, Cyprus, 1886; med. officer, Malacca, 1889; col. surg., Malacca, July, 1890; ditto, Penang, 1891; col. surg. resdr., Singapore, Apr., 1893.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Assistant medical officer and J.P. | Seychelles | [1888, 1889, 1890, 1894, 1896] |
| 1 | 1884 | acting government medical officer, Mahé | Seychelles *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896] |
| 2 | 1885 | government medical officer | Seychelles | [1888, 1889, 1890, 1894, 1896] |
| 3 | 1886 | district medical officer, Larnaca | Cyprus | [1888, 1889, 1890, 1894, 1896] |
| 4 | 1889 | med. officer, Malacca | Cyprus *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896] |
| 5 | 1890 | col. surg., Malacca | Cyprus *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896] |
| 6 | 1891 | ditto, Penang | Cyprus *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896] |
| 7 | 1893 | col. surg. resdr. | Singapore | [1888, 1889, 1890, 1894, 1896] |

## Candidate stint `Hoad, W___Straits Settlements___1894`

- Staff-list name: **Hoad, W** | colony: **Straits Settlements** | listed 1894–1896 | editions [1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | W. Hoad | Colonial Surgeon Resident | Medical | — | — |
| 1896 | W. Hoad | Colonial Surgeon, Resident | Medical | — | — |

### Deterministic checks: `hoad_william_e1881` vs `Hoad, W___Straits Settlements___1894`

- [PASS] surname_gate: bio 'HOAD' vs stint 'Hoad, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1896
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

