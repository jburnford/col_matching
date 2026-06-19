<!-- {"case_id": "case_romilly_hugh-hastings_e1879", "bio_ids": ["romilly_hugh-hastings_e1879"], "stint_ids": ["Romilly, Hugh___Cyprus___1888"]} -->
# Dossier case_romilly_hugh-hastings_e1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `romilly_hugh-hastings_e1879`

- Printed name: **ROMILLY, HUGH HASTINGS**
- Birth year: not printed
- Honours: C.M.G. (1886)
- Appears in editions: [1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1889-L35412.v` — printed in editions [1889, 1890]:**

> ROMILLY, HUGH HASTINGS, C.M.G. (1886).—Priv. sec. to Sir A. Gordon in Fiji, 1879, and N. Zealand, 1880-1; dep. commssnr. for Western Pacific, 1881; visited and lived in all principal groups; in charge of N. Guinea before Sir P. Scratchley's arrival and after his death in 1885 till 1886; dep. commssnr. and consul for N. Hebrides and Solomon Islands, 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879–1879 | Priv. sec. to Sir A. Gordon | Fiji | [1889, 1890] |
| 1 | 1880–1881 | Priv. sec. to Sir A. Gordon | New Zealand | [1889, 1890] |
| 2 | 1881–1881 | dep. commssnr. | Western Pacific | [1889, 1890] |
| 3 | 1885–1886 | in charge | New Guinea | [1889, 1890] |
| 4 | 1888–1888 | dep. commssnr. and consul | New Hebrides and Solomon Islands | [1889, 1890] |

## Candidate stint `Romilly, Hugh___Cyprus___1888`

- Staff-list name: **Romilly, Hugh** | colony: **Cyprus** | listed 1888–1889 | editions [1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | Hugh Romilly | Deputy Commissioner | New Guinea | C.M.G. | — |
| 1888 | H. H. Romilly | Deputy Commissioner for the Western Pacific | Establishment | C.M.G. | — |
| 1889 | H. H. Romilly | Deputy Commissioner New Hebrides and Solomon Islands | Establishment | C.M.G. | — |

### Deterministic checks: `romilly_hugh-hastings_e1879` vs `Romilly, Hugh___Cyprus___1888`

- [PASS] surname_gate: bio 'ROMILLY' vs stint 'Romilly, Hugh' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1889
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G.
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

