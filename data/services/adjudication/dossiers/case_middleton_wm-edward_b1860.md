<!-- {"case_id": "case_middleton_wm-edward_b1860", "bio_ids": ["middleton_wm-edward_b1860"], "stint_ids": ["Middleton, William Edward___Canada___1913"]} -->
# Dossier case_middleton_wm-edward_b1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `middleton_wm-edward_b1860`

- Printed name: **MIDDLETON, WM. EDWARD**
- Birth year: 1860 (attested in editions [1914])
- Appears in editions: [1914]

### Verbatim printed entry text (OCR)

**Version `col1914-L48583.v` — printed in editions [1914]:**

> MIDDLETON, HON. WM. EDWARD.—B. 1860; ED. TORONTO COLL., INST. AND TORONTO UNIV.; ADMITTED SOLR., 1884; CALLED TO THE BAR, 1886; K.C., 1908; JUDGE OF HIGH CT., ONTARIO, 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1884 | ADMITTED SOLR | — | [1914] |
| 1 | 1886 | CALLED TO THE BAR | — | [1914] |
| 2 | 1908 | K.C | — | [1914] |
| 3 | 1910 | JUDGE OF HIGH CT. | ONTARIO | [1914] |

## Candidate stint `Middleton, William Edward___Canada___1913`

- Staff-list name: **Middleton, William Edward** | colony: **Canada** | listed 1913–1922 | editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | William Edward Middleton | Puisne Judge | Supreme Court of Ontario | — | — |
| 1914 | William Edward Middleton | Puisne Judges | SUPREME COURT OF ONTARIO - HIGH COURT DIVISION | — | — |
| 1915 | William Edward Middleton | Puisne Judges | Supreme Court of Ontario - High Court Division | — | — |
| 1917 | William Edward Middleton | Puisne Judge | Supreme Court of Ontario - High Court Division | — | — |
| 1918 | William Edward Middleton | Puise Judges | Supreme Court of Ontario - High Court Division | — | — |
| 1919 | William Edward Middleton | Puisne Judge | Supreme Court of Ontario | — | — |
| 1920 | William Edward Middleton | Puisne Judges | SUPREME COURT OF ONTARIO - HIGH COURT DIVISION | — | — |
| 1922 | William Edward Middleton | Puisne Judges | HIGH COURT DIVISION | — | — |

### Deterministic checks: `middleton_wm-edward_b1860` vs `Middleton, William Edward___Canada___1913`

- [PASS] surname_gate: bio 'MIDDLETON' vs stint 'Middleton, William Edward' (exact)
- [PASS] initials: bio ['W', 'E'] ~ stint ['W', 'E']
- [PASS] age_gate: stint starts 1913, birth 1860 (age 53)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1913-1922
- [FAIL] position_sim: best 59 vs bar 60: 'JUDGE OF HIGH CT.' ~ 'Puisne Judge'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

