<!-- {"case_id": "case_mercier_charles-edward_e1857", "bio_ids": ["mercier_charles-edward_e1857"], "stint_ids": ["Mercier, C. E___Leeward Islands___1889", "Mercier, C. E___Trinidad___1883"]} -->
# Dossier case_mercier_charles-edward_e1857

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mercier_charles-edward_e1857`

- Printed name: **MERCIER, CHARLES EDWARD**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1888-L34882.v` — printed in editions [1888, 1889, 1890, 1894]:**

> MERCIER, CHARLES EDWARD.—Entered customs service, London, after competitive examination, Oct., 1857; sub-receiver, sub-collector of customs, and harbour master, San Fernando, Trinidad, in Mar., 1880; acting port magistrate, Aug. to Sept., 1881; and acting collector of customs, May, 1881, to Jan., 1882; acting auditor-general, April to Dec., 1885; auditor-general, Leeward Islands, Dec., 1885; member the general leg. coun. and of ex. and leg. councils, Antigua; acting president, Antigua, Mar. to Aug., 1886, and at various times in 1887-8-9; member Federal Exec. Coun., 1887; is a J.P. and visiting Justice of Antigua gaol; ag. col. secy., Leeward Islands, July to Nov., 1889; ag. col. secy., Feb. to Sept., 1892.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1857 | Entered customs service | London | [1888, 1889, 1890, 1894] |
| 1 | 1880 | sub-receiver, sub-collector of customs, and harbour master | Trinidad | [1888, 1889, 1890, 1894] |
| 2 | 1881–1881 | acting port magistrate | — | [1888, 1889, 1890, 1894] |
| 3 | 1881–1882 | acting collector of customs | — | [1888, 1889, 1890, 1894] |
| 4 | 1885–1885 | acting auditor-general | Leeward Islands | [1888, 1889, 1890, 1894] |
| 5 | 1886–1889 | acting president | Antigua | [1888, 1889, 1890, 1894] |
| 6 | 1887–1887 | member Federal Exec. Coun. | — | [1888, 1889, 1890, 1894] |
| 7 | 1889–1889 | ag. col. secy. | Leeward Islands | [1888, 1889, 1890, 1894] |
| 8 | 1892–1892 | ag. col. secy. | — | [1888, 1889, 1890, 1894] |

## Candidate stint `Mercier, C. E___Leeward Islands___1889`

- Staff-list name: **Mercier, C. E** | colony: **Leeward Islands** | listed 1889–1894 | editions [1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | C. E. Mercier | Auditor-General | Civil Establishment | — | — |
| 1890 | C. E. Mercier | Auditor-General | Civil Establishment | — | — |
| 1894 | C. E. Mercier | Auditor-General | Civil Establishment | — | — |

### Deterministic checks: `mercier_charles-edward_e1857` vs `Mercier, C. E___Leeward Islands___1889`

- [PASS] surname_gate: bio 'MERCIER' vs stint 'Mercier, C. E' (exact)
- [PASS] initials: bio ['C', 'E'] ~ stint ['C', 'E']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Leeward Islands'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1889-1894
- [FAIL] position_sim: best 24 vs bar 60: 'ag. col. secy.' ~ 'Auditor-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Mercier, C. E___Trinidad___1883`

- Staff-list name: **Mercier, C. E** | colony: **Trinidad** | listed 1883–1886 | editions [1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | C. E. Mercier | Harbour Master, San Fernando | Harbour Master's Department | — | — |
| 1883 | C. E. Mercier | Sub-Receiver (San Fernando) | Receiver-General's Department | — | — |
| 1886 | C. E. Mercier | Sub-Receiver (San Fernando) | Receiver-General's Department | — | — |
| 1886 | C. E. Mercier | Harbour Master | Harbour Master's Department | — | — |

### Deterministic checks: `mercier_charles-edward_e1857` vs `Mercier, C. E___Trinidad___1883`

- [PASS] surname_gate: bio 'MERCIER' vs stint 'Mercier, C. E' (exact)
- [PASS] initials: bio ['C', 'E'] ~ stint ['C', 'E']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1886
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

