<!-- {"case_id": "case_abraham_e-a-v_e1869", "bio_ids": ["abraham_e-a-v_e1869"], "stint_ids": ["Abraham, E. A. V___British Guiana___1877"]} -->
# Dossier case_abraham_e-a-v_e1869

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `abraham_e-a-v_e1869`

- Printed name: **ABRAHAM, E. A. V**
- Birth year: not printed
- Appears in editions: [1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1889-L31435.v` — printed in editions [1889, 1890, 1894]:**

> ABRAHAM, E. A. V.—Copyist, registrar's office, Br. Guiana, 1869; 3rd asst. sworn clerk, 1874; 1st ditto, 1876; sworn clerk and notary public, 1882; atty.-at-law, 1887; ex officio registrar, supreme cts.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | Copyist, registrar's office | British Guiana | [1889, 1890, 1894] |
| 1 | 1874 | 3rd asst. sworn clerk | British Guiana *(inherited from previous clause)* | [1889, 1890, 1894] |
| 2 | 1876 | 1st ditto | British Guiana *(inherited from previous clause)* | [1889, 1890, 1894] |
| 3 | 1882 | sworn clerk and notary public | British Guiana *(inherited from previous clause)* | [1889, 1890, 1894] |
| 4 | 1887 | atty.-at-law | British Guiana *(inherited from previous clause)* | [1889, 1890, 1894] |

## Candidate stint `Abraham, E. A. V___British Guiana___1877`

- Staff-list name: **Abraham, E. A. V** | colony: **British Guiana** | listed 1877–1889 | editions [1877, 1878, 1880, 1883, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. Abraham | Third Assistant Sworn Clerk | Judicial Establishment | — | — |
| 1878 | E. Abraham | Third Assistant Sworn Clerk | Judicial Establishment | — | — |
| 1880 | E. Abraham | Third Assistant Sworn Clerk | Judicial Establishment | — | — |
| 1883 | E. A. V. Abraham | Third Sworn Clerk and Notary Public | Judicial Establishment | — | — |
| 1886 | E. A. V. Abraham | Third Sworn Clerk and Notary Public | Judicial Establishment | — | — |
| 1888 | E. A. V. Abraham | Third Sworn Clerk and Notary Public | Judicial Establishment | — | — |
| 1889 | E. A. V. Abraham | Third Sworn Clerk and Notary Public | Judicial Establishment | — | — |

### Deterministic checks: `abraham_e-a-v_e1869` vs `Abraham, E. A. V___British Guiana___1877`

- [PASS] surname_gate: bio 'ABRAHAM' vs stint 'Abraham, E. A. V' (exact)
- [PASS] initials: bio ['E', 'A', 'V'] ~ stint ['E', 'A', 'V']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1877-1889
- [PASS] position_sim: best 100 vs bar 60: 'sworn clerk and notary public' ~ 'Third Sworn Clerk and Notary Public'
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

