<!-- {"case_id": "case_spielsburg_thomas-h_e1869", "bio_ids": ["spielsburg_thomas-h_e1869", "spilsbury_thomas-h_e1869-2"], "stint_ids": ["Spilsbury, Thomas H___Gambia___1879"]} -->
# Dossier case_spielsburg_thomas-h_e1869

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Spilsbury, Thomas H___Gambia___1879'] have more than one claimant biography in this case.
- NOTE: stint `Spilsbury, Thomas H___Gambia___1879` is also gate-compatible with biography(ies) outside this case: ['spilsbury_thomas-h_e1869'] (already linked elsewhere or filtered).
- NOTE: stint `Spilsbury, Thomas H___Gambia___1879` is also gate-compatible with biography(ies) outside this case: ['spilsbury_thomas-h_e1869'] (already linked elsewhere or filtered).

## Biography `spielsburg_thomas-h_e1869`

- Printed name: **SPIELSBURG, THOMAS H.**
- Birth year: not printed
- Appears in editions: [1890]

### Verbatim printed entry text (OCR)

**Version `col1890-L36811.v` — printed in editions [1890]:**

> SPIELSBURG, THOMAS H.—Colonial surgeon, Gambia, 2nd Nov., 1869; acting chief magistrate in 1872, 1876, 1882, and 1886-7; acting collector and treasurer, July, 1877, to April, 1878, Nov., 1878, to Apr., 1879, Dec., 1885, to Feb., 1886, and from Aug., 1888; is a J.P. and commissioner, court of requests.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | Colonial surgeon | Gambia | [1890] |
| 1 | 1872–1887 | acting chief magistrate | — | [1890] |
| 2 | 1877 | acting collector and treasurer | — | [1890] |

## Biography `spilsbury_thomas-h_e1869-2`

- Printed name: **SPILSBURY, Thomas H.**
- Birth year: not printed
- Appears in editions: [1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1888-L36154.v` — printed in editions [1888, 1889]:**

> SPILSBURY, Thomas H.—Colonial surgeon, Gambia, 2nd Nov., 1869; acting chief magistrate in 1872, 1876, 1882, and 1886-7; acting collector and treasurer, July, 1877, to April, 1878, Nov., 1878, to Apr., 1879, Dec., 1885, to Feb., 1886, and from Aug., 1888; is a J.P. and commissioner, court of requests.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | Colonial surgeon | Gambia | [1888, 1889] |
| 1 | 1872–1887 | acting chief magistrate | — | [1888, 1889] |
| 2 | 1877 | acting collector and treasurer | — | [1888, 1889] |

## Candidate stint `Spilsbury, Thomas H___Gambia___1879`

- Staff-list name: **Spilsbury, Thomas H** | colony: **Gambia** | listed 1879–1890 | editions [1879, 1880, 1883, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | Thomas H. Spilsbury | Colonial Surgeon | Medical Establishment | — | — |
| 1880 | Thomas H. Spilsbury | Colonial Surgeon | Medical Establishment | — | — |
| 1883 | Thomas H. Spilsbury | Colonial Surgeon | Medical Establishment | — | — |
| 1889 | Thomas H. Spilsbury | Colonial Surgeon | Medical Establishment | — | — |
| 1890 | Thomas H. Spilsbury | Colonial Surgeon | Civil Establishment | — | — |

### Deterministic checks: `spielsburg_thomas-h_e1869` vs `Spilsbury, Thomas H___Gambia___1879`

- [PASS] surname_gate: bio 'SPIELSBURG' vs stint 'Spilsbury, Thomas H' (fuzzy:2)
- [PASS] initials: bio ['T', 'H'] ~ stint ['T', 'H']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `spilsbury_thomas-h_e1869-2` vs `Spilsbury, Thomas H___Gambia___1879`

- [PASS] surname_gate: bio 'SPILSBURY' vs stint 'Spilsbury, Thomas H' (exact)
- [PASS] initials: bio ['T', 'H'] ~ stint ['T', 'H']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1890
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

