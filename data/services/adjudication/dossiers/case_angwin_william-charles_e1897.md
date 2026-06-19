<!-- {"case_id": "case_angwin_william-charles_e1897", "bio_ids": ["angwin_william-charles_e1897"], "stint_ids": ["Angwin, William Charles___Australia___1912"]} -->
# Dossier case_angwin_william-charles_e1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `angwin_william-charles_e1897`

- Printed name: **ANGWIN, WILLIAM CHARLES**
- Birth year: not printed
- Appears in editions: [1930, 1931, 1933]

### Verbatim printed entry text (OCR)

**Version `col1930-L62217.v` — printed in editions [1930, 1931, 1933]:**

> ANGWIN, HON. WILLIAM CHARLES.—M.L.A., Western Australia (North-East Fremantle), 1904-27; min. for lands, immigrn. and industries, 1924-27; mem., East Fremantle munici. coun., 1897-1926; agt. gen. in England for W. Australia, Mar., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897–1926 | mem., East Fremantle munici. coun | Western Australia *(inherited from previous clause)* | [1930, 1931, 1933] |
| 1 | 1904–1927 | M.L.A., Western Australia (North-East Fremantle) | Western Australia | [1930, 1931, 1933] |
| 2 | 1924–1927 | min. for lands, immigrn. and industries | Western Australia *(inherited from previous clause)* | [1930, 1931, 1933] |
| 3 | 1927 | agt. gen. in England for W. Australia | Western Australia *(inherited from previous clause)* | [1930, 1931, 1933] |

## Candidate stint `Angwin, William Charles___Australia___1912`

- Staff-list name: **Angwin, William Charles** | colony: **Australia** | listed 1912–1927 | editions [1912, 1913, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | The Hon. William Charles Angwin | Minister without Portfolio | Executive Council | — | — |
| 1912 | William Charles Angwin | Member of Legislative Assembly | Legislative Assembly | — | — |
| 1913 | William Charles Angwin | Minister without Portfolio | Executive Council | — | — |
| 1913 | William Charles Angwin | Member | Legislative Assembly | — | — |
| 1927 | W. C. Angwin | Minister for Lands and Immigration, Hon. | Department of Minister for Lands | — | — |

### Deterministic checks: `angwin_william-charles_e1897` vs `Angwin, William Charles___Australia___1912`

- [PASS] surname_gate: bio 'ANGWIN' vs stint 'Angwin, William Charles' (exact)
- [PASS] initials: bio ['W', 'C'] ~ stint ['W', 'C']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1927
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

