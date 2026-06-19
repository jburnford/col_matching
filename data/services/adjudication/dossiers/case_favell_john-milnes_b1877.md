<!-- {"case_id": "case_favell_john-milnes_b1877", "bio_ids": ["favell_john-milnes_b1877"], "stint_ids": ["Favell, J M___Straits Settlements___1913"]} -->
# Dossier case_favell_john-milnes_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `favell_john-milnes_b1877`

- Printed name: **FAVELL, JOHN MILNES**
- Birth year: 1877 (attested in editions [1932])
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L60114.v` — printed in editions [1932]:**

> FAVELL, JOHN MILNES, B.Sc. (Durham).—B. 1877; govt. survr., Sudan, May, 1906-Nov., 1908; survr., 1st grade, rev. survey dept., F.M.S., Apr., 1909; ch. survr., Kelantan, Apr., 1911; asst. survr., surveys, Jan., 1914; on mily., serv., Jan. 1915 to Apr., 1919; senr. asst. supt., surveys, Kinta, May, 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906–1908 | govt. survr., Sudan | — | [1932] |
| 1 | 1909 | survr., 1st grade, rev. survey dept. | Federated Malay States | [1932] |
| 2 | 1911 | ch. survr. | Kelantan | [1932] |
| 3 | 1914 | asst. survr., surveys | Kelantan *(inherited from previous clause)* | [1932] |
| 4 | 1915–1919 | on mily., serv | Kelantan *(inherited from previous clause)* | [1932] |
| 5 | 1928 | senr. asst. supt., surveys, Kinta | Kelantan *(inherited from previous clause)* | [1932] |

## Candidate stint `Favell, J M___Straits Settlements___1913`

- Staff-list name: **Favell, J M** | colony: **Straits Settlements** | listed 1913–1915 | editions [1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | J. M. Favell | Chief Surveyor | Civil Establishment | — | — |
| 1914 | J. M. Favell | Chief Surveyor | Civil Establishment | — | — |
| 1915 | J. M. Favell | Chief Surveyor | Civil Establishment | — | — |

### Deterministic checks: `favell_john-milnes_b1877` vs `Favell, J M___Straits Settlements___1913`

- [PASS] surname_gate: bio 'FAVELL' vs stint 'Favell, J M' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1913, birth 1877 (age 36)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1915
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

