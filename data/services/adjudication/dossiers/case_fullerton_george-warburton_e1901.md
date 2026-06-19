<!-- {"case_id": "case_fullerton_george-warburton_e1901", "bio_ids": ["fullerton_george-warburton_e1901"], "stint_ids": ["Fullarton, George___New South Wales___1877"]} -->
# Dossier case_fullerton_george-warburton_e1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fullerton_george-warburton_e1901`

- Printed name: **FULLERTON, GEORGE WARBURTON**
- Birth year: not printed
- Honours: K.C.M.G. (1919)
- Appears in editions: [1935]

### Verbatim printed entry text (OCR)

**Version `dol1935-L58728.v` — printed in editions [1935]:**

> FULLERTON, HON. SIR GEORGE WARBURTON, K.C.M.G. (1919).—Elected to first H. of R., C. of A., 1901; re-elected, 1903 and 1906; min. of home affairs, C. of A., June, 1909 to Apr., 1910; col. sec., N. S. Wales, Nov., 1916-20; premier, 1922-25; agt.-gen., N.S.W., 1926-31.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901–1901 | Elected to first H. of R. | Commonwealth of Australia | [1935] |
| 1 | 1903–1906 | re-elected | — | [1935] |
| 2 | 1909–1910 | min. of home affairs | Commonwealth of Australia | [1935] |
| 3 | 1916–1920 | col. sec. | New South Wales | [1935] |
| 4 | 1922–1925 | premier | — | [1935] |
| 5 | 1926–1931 | agt.-gen. | New South Wales | [1935] |

## Candidate stint `Fullarton, George___New South Wales___1877`

- Staff-list name: **Fullarton, George** | colony: **New South Wales** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | George Fullarton | Commissioner of Crown Lands | Crown Lands Occupation Department | — | — |
| 1878 | George Fullarton | Commissioner of Crown Lands | Crown Lands Occupation Department | — | — |
| 1879 | George Fullarton | Commissioner of Crown Lands | Pastoral Districts | — | — |
| 1880 | George Fullarton | Commissioner of Crown Lands | Pastoral Districts | — | — |

### Deterministic checks: `fullerton_george-warburton_e1901` vs `Fullarton, George___New South Wales___1877`

- [PASS] surname_gate: bio 'FULLERTON' vs stint 'Fullarton, George' (fuzzy:1)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

