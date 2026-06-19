<!-- {"case_id": "case_hyndman-jones_w-h_e1870", "bio_ids": ["hyndman-jones_w-h_e1870"], "stint_ids": ["Hyndman-Jones, William H___Straits Settlements___1900"]} -->
# Dossier case_hyndman-jones_w-h_e1870

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hyndman-jones_w-h_e1870`

- Printed name: **HYNDMAN-JONES, W. H**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28104.v` — printed in editions [1883]:**

> HYNDMAN-JONES, W. H.—Educated at Marlborough and Trinity College, Cambridge; LL.B., 1870; called to the bar at Lincoln's Inn, 1878; appointed acting judge of assistant court of appeal, Barbados, April, 1880; acting senior police magistrate for the city of Bridgetown, August, 1880; appointed one of the commissioners to inquire into the condition of the police force in Barbados, October, 1880; stipendiary magistrate, first district, St. Lucia, March, 1881; acting chief justice, St. Lucia, October, 1881; member of legislative council, May, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1870 | LL.B | — | [1883] |
| 1 | 1878 | called to the bar at Lincoln's Inn | — | [1883] |
| 2 | 1880 | appointed acting judge of assistant court of appeal | Barbados | [1883] |
| 3 | 1881 | stipendiary magistrate, first district | St. Lucia | [1883] |

## Candidate stint `Hyndman-Jones, William H___Straits Settlements___1900`

- Staff-list name: **Hyndman-Jones, William H** | colony: **Straits Settlements** | listed 1900–1914 | editions [1900, 1907, 1908, 1910, 1911, 1912, 1913, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1900 | W. H. Hyndman-Jones | Police Judge | Penang | — | — |
| 1907 | Sir W. H. Hyndman-Jones | Chief Justice | Judicial Department | — | — |
| 1908 | Sir W. H. Hyndman-Jones | Chief Justice | Judicial Department | — | — |
| 1910 | Sir W. H. Hyndman-Jones | Chief Justice | Judicial Department | — | — |
| 1911 | Sir W. H. Hyndman-Jones | Chief Justice | Judicial Department | — | — |
| 1912 | Sir W. H. Hyndman-Jones | Chief Justice | Judicial Department | — | — |
| 1913 | Sir W. H. Hyndman-Jones | Chief Justice | Judicial Department | — | — |
| 1914 | Sir W. H. Hyndman-Jones | Chief Justice | Judicial Department | — | — |

### Deterministic checks: `hyndman-jones_w-h_e1870` vs `Hyndman-Jones, William H___Straits Settlements___1900`

- [PASS] surname_gate: bio 'HYNDMAN-JONES' vs stint 'Hyndman-Jones, William H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1900; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1900-1914
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

