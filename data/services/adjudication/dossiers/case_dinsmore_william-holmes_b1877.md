<!-- {"case_id": "case_dinsmore_william-holmes_b1877", "bio_ids": ["dinsmore_william-holmes_b1877"], "stint_ids": ["Dinsmore, W. H___Straits Settlements___1914"]} -->
# Dossier case_dinsmore_william-holmes_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dinsmore_william-holmes_b1877`

- Printed name: **DINSMORE, WILLIAM HOLMES**
- Birth year: 1877 (attested in editions [1933])
- Honours: B.A
- Appears in editions: [1933]

### Verbatim printed entry text (OCR)

**Version `col1933-L59222.v` — printed in editions [1933]:**

> DINSMORE, WILLIAM HOLMES, B.A., LL.B., Trinity Coll., Dublin, Barrister-at-Law, Inner Temple.—B., 1877; cadet, F.M.S., Dec., 1901; asst. cadet, Nov., 1903; cls. IV. July, 1912; cls. III, 1918; cls. II, 1919; dep. pub. proc., Penang, 1922; do., F.M.S., 1924; cls. IB, 1925; dep. legal advr., F.M.S., 1921; judge, high ct., Kedah, 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | cadet | Federated Malay States | [1933] |
| 1 | 1903 | asst. cadet | Federated Malay States *(inherited from previous clause)* | [1933] |
| 2 | 1912 | cls. IV | Federated Malay States *(inherited from previous clause)* | [1933] |
| 3 | 1918 | cls. III | Federated Malay States *(inherited from previous clause)* | [1933] |
| 4 | 1919 | cls. II | Federated Malay States *(inherited from previous clause)* | [1933] |
| 5 | 1921 | dep. legal advr. | Federated Malay States | [1933] |
| 6 | 1922 | dep. pub. proc., Penang | Federated Malay States *(inherited from previous clause)* | [1933] |
| 7 | 1924 | dep. pub. proc., Penang | Federated Malay States | [1933] |
| 8 | 1925 | cls. IB | Federated Malay States *(inherited from previous clause)* | [1933] |
| 9 | 1926 | judge, high ct. | Kedah | [1933] |

## Candidate stint `Dinsmore, W. H___Straits Settlements___1914`

- Staff-list name: **Dinsmore, W. H** | colony: **Straits Settlements** | listed 1914–1920 | editions [1914, 1915, 1917, 1918, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | W. H. Dinsmore | Class IV Cadet | Cadet Service | — | — |
| 1915 | W. H. Dinsmore | Class IV Cadet | Cadet Service | — | — |
| 1917 | W. H. Dinsmore (acting) | Assistant to Attorney-General | Judicial Department | — | — |
| 1918 | W. H. Dinsmore | Assistant to Attorney-General | Judicial Department | — | — |
| 1919 | W. H. Dinsmore | Assistant to Attorney-General | Judicial Department | — | — |
| 1920 | W. H. Dinsmore | Cadet Service Officer, Class III | Cadet Service | — | — |

### Deterministic checks: `dinsmore_william-holmes_b1877` vs `Dinsmore, W. H___Straits Settlements___1914`

- [PASS] surname_gate: bio 'DINSMORE' vs stint 'Dinsmore, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1914, birth 1877 (age 37)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1920
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

