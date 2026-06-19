<!-- {"case_id": "case_preston_phillip-geoffrey_b1898", "bio_ids": ["preston_phillip-geoffrey_b1898"], "stint_ids": ["Preston, P. G___Kenya___1949"]} -->
# Dossier case_preston_phillip-geoffrey_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `preston_phillip-geoffrey_b1898`

- Printed name: **PRESTON, Phillip Geoffrey**
- Birth year: 1898 (attested in editions [1948, 1949])
- Honours: M.B, M.R.C.O.G
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L35330.v` — printed in editions [1948, 1949]:**

> PRESTON, Phillip Geoffrey, M.B., Ch.B., M.R.C.O.G.—b. 1898; ed. King Edward VII Sch., Sheffield Univ.; on mil. serv. 1915–19; med. offr., Ken., 1929; author of numerous articles in the E.A. Med. Journal and other medical publications.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | med. offr. | Kenya | [1948, 1949] |

## Candidate stint `Preston, P. G___Kenya___1949`

- Staff-list name: **Preston, P. G** | colony: **Kenya** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. G. Preston | Medical Officer | Medical | — | — |
| 1950 | P. G. Preston | Medical Officer | Medical | — | — |

### Deterministic checks: `preston_phillip-geoffrey_b1898` vs `Preston, P. G___Kenya___1949`

- [PASS] surname_gate: bio 'PRESTON' vs stint 'Preston, P. G' (exact)
- [PASS] initials: bio ['P', 'G'] ~ stint ['P', 'G']
- [PASS] age_gate: stint starts 1949, birth 1898 (age 51)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

