<!-- {"case_id": "case_finlayson_john-george_e1906", "bio_ids": ["finlayson_john-george_e1906"], "stint_ids": ["Finlayson, J___Straits Settlements___1890"]} -->
# Dossier case_finlayson_john-george_e1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `finlayson_john-george_e1906`

- Printed name: **FINLAYSON, JOHN GEORGE**
- Birth year: not printed
- Terminal: resigned 1911 — “resigned, 1911.”
- Appears in editions: [1923, 1928]

### Verbatim printed entry text (OCR)

**Version `col1923-L54352.v` — printed in editions [1923, 1928]:**

> FINLAYSON, HON. SIR JOHN GEORGE, K.C.M.G. (1910); LL.D., K.C.—Atty.-gen. and col. sec., New Zealand, Nov., 1906; attended Imp. Conf., 1911; resigned, 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906 | Atty.-gen. and col. sec. | New Zealand | [1923, 1928] |
| 1 | 1911 | attended Imp. Conf | New Zealand *(inherited from previous clause)* | [1923, 1928] |

## Candidate stint `Finlayson, J___Straits Settlements___1890`

- Staff-list name: **Finlayson, J** | colony: **Straits Settlements** | listed 1890–1894 | editions [1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | J. Finlayson | Vice-Consul | Consuls | — | — |
| 1894 | J. Finlayson | Vice-Consul | Consuls | — | — |

### Deterministic checks: `finlayson_john-george_e1906` vs `Finlayson, J___Straits Settlements___1890`

- [PASS] surname_gate: bio 'FINLAYSON' vs stint 'Finlayson, J' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1890-1894
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

