<!-- {"case_id": "case_thunder_maurice_e1905", "bio_ids": ["thunder_maurice_e1905"], "stint_ids": ["Thunder, M___Straits Settlements___1907"]} -->
# Dossier case_thunder_maurice_e1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['thunder_maurice_e1905'] carry a single initial only — the namesake trap applies.

## Biography `thunder_maurice_e1905`

- Printed name: **THUNDER, MAURICE**
- Birth year: not printed
- Appears in editions: [1909, 1910, 1911]

### Verbatim printed entry text (OCR)

**Version `col1909-L50033.v` — printed in editions [1909, 1910, 1911]:**

> THUNDER, MAURICE.—Cadet, S. Sttlmts., Dec., 1905; ag. dist. offr., Penang, Sept., 1906; ag. dist. offr., Prov. Wellesley, Nov., 1907; passed final exam.in Malay, Jan., 1908; ag. 4th mag., Singapore, Apr., 1908; ag. astt. to atty.-gen., Dec., 1908.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1905 | Cadet, S. Sttlmts | — | [1909, 1910, 1911] |
| 1 | 1906 | ag. dist. offr., Penang | — | [1909, 1910, 1911] |
| 2 | 1907 | ag. dist. offr., Prov. Wellesley | — | [1909, 1910, 1911] |
| 3 | 1908 | passed final exam.in Malay | — | [1909, 1910, 1911] |
| 4 | 1908 | ag. 4th mag. | Singapore | [1909, 1910, 1911] |

## Candidate stint `Thunder, M___Straits Settlements___1907`

- Staff-list name: **Thunder, M** | colony: **Straits Settlements** | listed 1907–1911 | editions [1907, 1908, 1910, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | M. Thunder | Cadet | Colonial Secretary's Office | — | — |
| 1908 | M. Thunder | Cadet | Colonial Secretary's Office | — | — |
| 1910 | M. Thunder | Passed Cadets | Colonial Secretary's Office | — | — |
| 1911 | M. Thunder | Passed Cadets | Colonial Secretary's Office | — | — |

### Deterministic checks: `thunder_maurice_e1905` vs `Thunder, M___Straits Settlements___1907`

- [PASS] surname_gate: bio 'THUNDER' vs stint 'Thunder, M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1907; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1911
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

