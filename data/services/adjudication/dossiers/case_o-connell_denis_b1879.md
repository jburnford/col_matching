<!-- {"case_id": "case_o-connell_denis_b1879", "bio_ids": ["o-connell_denis_b1879"], "stint_ids": ["O'Connell, D___Nyasaland___1908"]} -->
# Dossier case_o-connell_denis_b1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['o-connell_denis_b1879'] carry a single initial only — the namesake trap applies.

## Biography `o-connell_denis_b1879`

- Printed name: **O'CONNELL, DENIS**
- Birth year: 1879 (attested in editions [1908, 1909, 1910, 1911, 1912, 1913])
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1908-L46547.v` — printed in editions [1908, 1909, 1910, 1911, 1912, 1913]:**

> O'CONNELL, DENIS.—B. 1879; served in London postal serv., Nov., 1898 to Dec., 1901; Imp. cust. serv., Jan., 1902, to June, 1906; seconded to cust. serv., B. C. Africa Prot., June, 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898–1901 | London postal serv. | London | [1908, 1909, 1910, 1911, 1912, 1913] |
| 1 | 1902–1906 | Imp. cust. serv. | — | [1908, 1909, 1910, 1911, 1912, 1913] |
| 2 | 1906 | seconded to cust. serv. | British Central Africa Protectorate | [1908, 1909, 1910, 1911, 1912, 1913] |

## Candidate stint `O'Connell, D___Nyasaland___1908`

- Staff-list name: **O'Connell, D** | colony: **Nyasaland** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | D. O'Connell | Assistant | Customs Department | — | — |
| 1909 | D. O'Connell | Assistant | Customs Department | — | — |

### Deterministic checks: `o-connell_denis_b1879` vs `O'Connell, D___Nyasaland___1908`

- [PASS] surname_gate: bio 'O'CONNELL' vs stint 'O'Connell, D' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1908, birth 1879 (age 29)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1909
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

