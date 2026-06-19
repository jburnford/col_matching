<!-- {"case_id": "case_schmidt_louis-edward_e1861", "bio_ids": ["schmidt_louis-edward_e1861"], "stint_ids": ["Schmidt, E___Lagos___1896", "Schmidt, L. E___Mauritius___1877"]} -->
# Dossier case_schmidt_louis-edward_e1861

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `schmidt_louis-edward_e1861`

- Printed name: **SCHMIDT, LOUIS EDWARD**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1889, 1890, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1883-L29422.v` — printed in editions [1883, 1886, 1889, 1890, 1896, 1897]:**

> SCHMIDT, LOUIS EDWARD.—Appointed in Aug., 1861, clerk to stipendiary magistrate, Moka, Mauritius; Sept. 18, 1861, clerk in the colonial secretary's office; July, 1868, corresponding clerk; registrar, April, 1866; chief clerk and secretary to council, Nov., 1877; now storekeeper-general; rec.-genl., 1889.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861 | clerk to stipendiary magistrate | Mauritius | [1883, 1886, 1889, 1890, 1896, 1897] |
| 1 | 1861 | clerk in the colonial secretary's office | — | [1883, 1886, 1889, 1890, 1896, 1897] |
| 2 | 1866 | registrar | — | [1883, 1886, 1889, 1890, 1896, 1897] |
| 3 | 1868 | corresponding clerk | — | [1883, 1886, 1889, 1890, 1896, 1897] |
| 4 | 1877 | chief clerk and secretary to council | — | [1883, 1886, 1889, 1890, 1896, 1897] |
| 5 | 1889 | rec.-genl. | — | [1883, 1886, 1889, 1890, 1896, 1897] |
| 6 | ? | storekeeper-general | — | [1883, 1886, 1889, 1890, 1896, 1897] |

## Candidate stint `Schmidt, E___Lagos___1896`

- Staff-list name: **Schmidt, E** | colony: **Lagos** | listed 1896–1899 | editions [1896, 1897, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | Herr E. Schmidt | German Consul | Foreign Consuls | — | — |
| 1897 | Herr E. Schmidt | German Consul | Foreign Consuls | — | — |
| 1899 | E. Schmidt | German Consul | Foreign Consuls | — | — |

### Deterministic checks: `schmidt_louis-edward_e1861` vs `Schmidt, E___Lagos___1896`

- [PASS] surname_gate: bio 'SCHMIDT' vs stint 'Schmidt, E' (exact)
- [PASS] initials: bio ['L', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Lagos'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1899
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Schmidt, L. E___Mauritius___1877`

- Staff-list name: **Schmidt, L. E** | colony: **Mauritius** | listed 1877–1896 | editions [1877, 1878, 1879, 1880, 1883, 1888, 1889, 1890, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | L. E. Schmidt | Acting Chief Clerk | Colonial Secretary's Office | — | — |
| 1878 | L. E. Schmidt | Acting Chief Clerk | Acting Chief Clerk | — | — |
| 1879 | L. E. Schmidt | Acting Chief Clerk | Colonial Secretary's Office | — | — |
| 1880 | L. E. Schmidt | Chief Clerk | Colonial Secretary's Office. | — | — |
| 1883 | L. E. Schmidt | Storekeeper-General | Civil Commissariat Department. | — | — |
| 1888 | L. E. Schmidt | Storekeeper-General | Civil Commissariat Department | — | — |
| 1889 | L. E. Schmidt | Storekeeper-General | Civil Commissariat Department | — | — |
| 1890 | L. E. Schmidt | Receiver-General | Receiver-General's Department | — | — |
| 1894 | L. E. Schmidt | Receiver-General | Receiver-General's Department | — | — |
| 1896 | L. E. Schmidt | Receiver-General | Receiver-General's Department | — | — |

### Deterministic checks: `schmidt_louis-edward_e1861` vs `Schmidt, L. E___Mauritius___1877`

- [PASS] surname_gate: bio 'SCHMIDT' vs stint 'Schmidt, L. E' (exact)
- [PASS] initials: bio ['L', 'E'] ~ stint ['L', 'E']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1896
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

