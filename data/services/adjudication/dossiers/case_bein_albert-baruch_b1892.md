<!-- {"case_id": "case_bein_albert-baruch_b1892", "bio_ids": ["bein_albert-baruch_b1892"], "stint_ids": ["Bein, A. B___Federated Malay States___1918"]} -->
# Dossier case_bein_albert-baruch_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bein_albert-baruch_b1892`

- Printed name: **BEIN, Albert Baruch**
- Birth year: 1892 (attested in editions [1922])
- Appears in editions: [1922]

### Verbatim printed entry text (OCR)

**Version `col1922-L50574.v` — printed in editions [1922]:**

> BEIN, Albert Baruch.—B. 1892; ed. King's Coll., Cambridge, B.A.; app'td. cadet, F.M.S., Nov., 1915; attached to censor's office, Singapore, Apr., 1916; proceeded to China, Dec., 1916; passed final exam. in Chinese, Aug., 1918; app'td. ast. prot. of Chinese, and ast. contrir. of lahr., Selangor, Mar., 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | app'td. cadet | Federated Malay States | [1922] |
| 1 | 1916 | attached to censor's office | Singapore | [1922] |
| 2 | 1918 | passed final exam. in Chinese | Singapore *(inherited from previous clause)* | [1922] |
| 3 | 1919 | app'td. ast. prot. of Chinese, and ast. contrir. of lahr., Selangor | Singapore *(inherited from previous clause)* | [1922] |

## Candidate stint `Bein, A. B___Federated Malay States___1918`

- Staff-list name: **Bein, A. B** | colony: **Federated Malay States** | listed 1918–1919 | editions [1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | A. B. Bein | Cadet | Cadet Service | — | — |
| 1919 | A. B. Bein | Cadet | Cadet Service | — | — |

### Deterministic checks: `bein_albert-baruch_b1892` vs `Bein, A. B___Federated Malay States___1918`

- [PASS] surname_gate: bio 'BEIN' vs stint 'Bein, A. B' (exact)
- [PASS] initials: bio ['A', 'B'] ~ stint ['A', 'B']
- [PASS] age_gate: stint starts 1918, birth 1892 (age 26)
- [PASS] colony: 1 placed event(s) resolve to 'Federated Malay States'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1919
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

