<!-- {"case_id": "case_clarence_l-b_e1861", "bio_ids": ["clarence_l-b_e1861"], "stint_ids": ["Clarence, L. B___Ceylon___1877"]} -->
# Dossier case_clarence_l-b_e1861

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `clarence_l-b_e1861`

- Printed name: **CLARENCE, L.B.**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1889-L32330.v` — printed in editions [1889, 1890]:**

> CLARENCE, L.B.—Educated at Milton Abbas school and Trin. Coll., Camb.; B.A. (Sen. Opt.), 1861; called to the bar at the Inner Temple in 1864; deputy Queen's advocate, for the island, Ceylon, 1873; puisne judge of the supreme court, 1876; acted as chief justice in 1877, 1883, and 1888.

**Version `col1883-L26847.v` — printed in editions [1883, 1886, 1888]:**

> CLARENCE, L. B.—Educated at Milton Abbas school and Trinity College, Cambridge; graduated B.A., 1861; called to the bar at the Inner Temple in 1864; deputy Queen's advocate for the island, Ceylon, 1873; puisne judge of the supreme court, 1876.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861–1861 | B.A. (Sen. Opt.) | — | [1889, 1890] |
| 1 | 1861 | graduated B.A | — | [1883, 1886, 1888] |
| 2 | 1864–1864 | called to the bar | — | [1883, 1886, 1888, 1889, 1890] |
| 3 | 1873–1873 | deputy Queen's advocate | Ceylon | [1883, 1886, 1888, 1889, 1890] |
| 4 | 1876–1876 | puisne judge of the supreme court | Ceylon *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890] |
| 5 | 1877–1888 | acted as chief justice | — | [1889, 1890] |

## Candidate stint `Clarence, L. B___Ceylon___1877`

- Staff-list name: **Clarence, L. B** | colony: **Ceylon** | listed 1877–1889 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | L. B. Clarence | Junior Puisne Judge | Judicial Establishment | — | — |
| 1878 | L. B. Clarence | Junior Puisne Judge | Judicial Establishment | — | — |
| 1879 | L. B. Clarence | Junior Puisne Judge | Judicial Establishment | — | — |
| 1880 | Hon. L. B. Clarence | Senior Puisme Judge | Judicial Establishment | — | — |
| 1883 | Hon. L. B. Clarence | Senior Puise Judge | Judicial Establishment | — | — |
| 1886 | Hon. L. B. Clarence | Senior Puisne Judge | Judicial Establishment | — | — |
| 1889 | L. B. Clarence | Senior Private Judge | Judicial Establishment | — | — |

### Deterministic checks: `clarence_l-b_e1861` vs `Clarence, L. B___Ceylon___1877`

- [PASS] surname_gate: bio 'CLARENCE' vs stint 'Clarence, L. B' (exact)
- [PASS] initials: bio ['L', 'B'] ~ stint ['L', 'B']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1889
- [PASS] position_sim: best 77 vs bar 60: 'puisne judge of the supreme court' ~ 'Junior Puisne Judge'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

