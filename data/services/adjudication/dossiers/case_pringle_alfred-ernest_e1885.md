<!-- {"case_id": "case_pringle_alfred-ernest_e1885", "bio_ids": ["pringle_alfred-ernest_e1885"], "stint_ids": ["Pringle, A. E___Straits Settlements___1911"]} -->
# Dossier case_pringle_alfred-ernest_e1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pringle_alfred-ernest_e1885`

- Printed name: **PRINGLE, ALFRED ERNEST**
- Birth year: not printed
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913, 1914]

### Verbatim printed entry text (OCR)

**Version `col1908-L46840.v` — printed in editions [1908, 1909, 1910, 1911, 1912, 1913, 1914]:**

> PRINGLE, ALFRED ERNEST.—Mast., high schl., Malacca, Oct., 1885; headmast., Malay coll., Singapore, Aug., 1894; headmast., govt. Outram schl., Singapore, Aug., 1895; sub-inspr. of schls., Malacca, Jan., 1896; ag. supt. of educn., Penang, Dec., 1906; confirmed, Jan., 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1885 | Mast., high schl., Malacca | — | [1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 1 | 1894 | headmast., Malay coll. | Singapore | [1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 2 | 1895 | headmast., govt. Outram schl. | Singapore | [1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 3 | 1896 | sub-inspr. of schls., Malacca | Singapore *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 4 | 1906 | ag. supt. of educn., Penang | Singapore *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 5 | 1907 | confirmed | Singapore *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914] |

## Candidate stint `Pringle, A. E___Straits Settlements___1911`

- Staff-list name: **Pringle, A. E** | colony: **Straits Settlements** | listed 1911–1913 | editions [1911, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | A. E. Pringle | Superintendent of Education | Penang | — | — |
| 1913 | A. E. Pringle | Inspector of Schools | Penang | — | — |

### Deterministic checks: `pringle_alfred-ernest_e1885` vs `Pringle, A. E___Straits Settlements___1911`

- [PASS] surname_gate: bio 'PRINGLE' vs stint 'Pringle, A. E' (exact)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1913
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

