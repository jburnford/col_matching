<!-- {"case_id": "case_molteno_john-charles_e1854", "bio_ids": ["molteno_john-charles_e1854"], "stint_ids": ["Molteno, J. Charles___Cape of Good Hope___1877", "Molteno, J. Charles___Cape of Good Hope___1896"]} -->
# Dossier case_molteno_john-charles_e1854

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `molteno_john-charles_e1854`

- Printed name: **MOLTENO, JOHN CHARLES**
- Birth year: not printed
- Honours: K.C.M.G. (1882)
- Terminal: retired 1883 — “retired 1883.”
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L28733.v` — printed in editions [1883, 1886]:**

> MOLTENO, SIR JOHN CHARLES, K.C.M.G. (1882).—Colonial secretary to the government of the Cape of Good Hope in 1872, under Act No. 1, 1872, of the Cape legislature, commonly called "The Responsible Government Act;" ceased to hold that office 6th Feb., 1878; elected member of the Cape legislative assembly for Beaufort West, in 1854, and returned for the same electoral division in each succeeding election; repaired to England in 1876, to confer with secretary of state on public business. Again took office as colonial secretary 1881 to 1882; retired 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1854–1854 | member of the Cape legislative assembly | Cape of Good Hope | [1883, 1886] |
| 1 | 1872–1872 | Colonial secretary to the government | Cape of Good Hope | [1883, 1886] |
| 2 | 1876–1876 | — | England | [1883, 1886] |
| 3 | 1878–1878 | — | — | [1883, 1886] |
| 4 | 1881–1882 | colonial secretary | — | [1883, 1886] |

## Candidate stint `Molteno, J. Charles___Cape of Good Hope___1877`

- Staff-list name: **Molteno, J. Charles** | colony: **Cape of Good Hope** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. C. Molteno | Colonial Secretary | Colonial Secretary's Department | — | — |
| 1878 | J. C. Molteno | Colonial Secretary | Colonial Secretary's Department | — | — |
| 1878 | J. Charles Molteno | Clerk, Third Class | Colonial Secretary's Department | — | — |

### Deterministic checks: `molteno_john-charles_e1854` vs `Molteno, J. Charles___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'MOLTENO' vs stint 'Molteno, J. Charles' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Molteno, J. Charles___Cape of Good Hope___1896`

- Staff-list name: **Molteno, J. Charles** | colony: **Cape of Good Hope** | listed 1896–1897 | editions [1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | J. C. Molteno | — | House of Assembly | — | — |
| 1897 | J. C. Molteno | — | Members | — | — |

### Deterministic checks: `molteno_john-charles_e1854` vs `Molteno, J. Charles___Cape of Good Hope___1896`

- [PASS] surname_gate: bio 'MOLTENO' vs stint 'Molteno, J. Charles' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1897
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

