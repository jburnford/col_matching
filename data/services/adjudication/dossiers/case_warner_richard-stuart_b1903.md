<!-- {"case_id": "case_warner_richard-stuart_b1903", "bio_ids": ["warner_richard-stuart_b1903"], "stint_ids": ["Warner, R. S. A___Tobago___1920"]} -->
# Dossier case_warner_richard-stuart_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 41 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Warner, R. S. A___Tobago___1920` is also gate-compatible with biography(ies) outside this case: ['warner_robert-stewart-aucher_b1859'] (already linked elsewhere or filtered).

## Biography `warner_richard-stuart_b1903`

- Printed name: **WARNER, Richard Stuart**
- Birth year: 1903 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L36675.v` — printed in editions [1948]:**

> WARNER, Richard Stuart.—b. 1903; ed. Wellington Coll., New Coll., Oxford, B.A. (Oxon.) (hons. sch. of mod. hist.); cadet, Nig., 1929; seconded to special serv. (P.E.R.O.), 1942-45.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | cadet | Nigeria | [1948] |
| 1 | 1942–1945 | seconded to special serv. (P.E.R.O.) | Nigeria *(inherited from previous clause)* | [1948] |

## Candidate stint `Warner, R. S. A___Tobago___1920`

- Staff-list name: **Warner, R. S. A** | colony: **Tobago** | listed 1920–1921 | editions [1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | R. S. A. Warner | Attorney-General | Legal | — | — |
| 1921 | R. S. A. Warner | Attorney-General | Legal | — | — |

### Deterministic checks: `warner_richard-stuart_b1903` vs `Warner, R. S. A___Tobago___1920`

- [PASS] surname_gate: bio 'WARNER' vs stint 'Warner, R. S. A' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S', 'A']
- [PASS] age_gate: stint starts 1920, birth 1903 (age 17)
- [FAIL] colony: no placed event resolves to 'Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1921
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

