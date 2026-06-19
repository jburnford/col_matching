<!-- {"case_id": "case_hewetson_william_e1868", "bio_ids": ["hewetson_william_e1868"], "stint_ids": ["Hewetson, William___St Helena___1896"]} -->
# Dossier case_hewetson_william_e1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hewetson_william_e1868'] carry a single initial only — the namesake trap applies.

## Biography `hewetson_william_e1868`

- Printed name: **HEWETSON, WILLIAM**
- Birth year: not printed
- Appears in editions: [1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1898-L33908.v` — printed in editions [1898, 1899, 1900]:**

> HEWETSON, WILLIAM.—Comdr., R.N.; entered H.M.'s navy, 1868; lieut., 1880; comdr., 1894; received Egyptian medal and clasp, Kiedive's bronze star for service in the Soudanese war, 1884-5; naval agt., col. treas., harbrmr., and stip. mag., St. Helena, 1893.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1868 | entered H.M.'s navy | — | [1898, 1899, 1900] |
| 1 | 1880 | lieut | — | [1898, 1899, 1900] |
| 2 | 1884–1885 | received Egyptian medal and clasp, Kiedive's bronze star for service in the Soudanese war | — | [1898, 1899, 1900] |
| 3 | 1893 | naval agt., col. treas., harbrmr., and stip. mag. | St. Helena | [1898, 1899, 1900] |
| 4 | 1894 | comdr | — | [1898, 1899, 1900] |

## Candidate stint `Hewetson, William___St Helena___1896`

- Staff-list name: **Hewetson, William** | colony: **St Helena** | listed 1896–1899 | editions [1896, 1897, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | William Hewetson | Receiver-General | Civil Establishment | — | — |
| 1897 | William Hewetson | Receiver-General | Civil Establishment | — | — |
| 1898 | William Hewetson | Receiver-General | Civil Establishment | — | — |
| 1899 | William Hewetson | Receiver-General | Civil Establishment | — | — |

### Deterministic checks: `hewetson_william_e1868` vs `Hewetson, William___St Helena___1896`

- [PASS] surname_gate: bio 'HEWETSON' vs stint 'Hewetson, William' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1899
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

