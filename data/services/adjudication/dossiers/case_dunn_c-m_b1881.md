<!-- {"case_id": "case_dunn_c-m_b1881", "bio_ids": ["dunn_c-m_b1881"], "stint_ids": ["Dunn, C. M___Nigeria___1915"]} -->
# Dossier case_dunn_c-m_b1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 33 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dunn_c-m_b1881`

- Printed name: **DUNN, C. M.**
- Birth year: 1881 (attested in editions [1914, 1915, 1917, 1918])
- Appears in editions: [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1914-L46016.v` — printed in editions [1914, 1915, 1917, 1918]:**

> DUNN, C. M.—B. 1881; ed. Clifton Coll. and King's Coll., Cambridge; honos., 3rd cls., modern and medieval languages tripes, 1904; asst. res., N. Nigeria, 1909. DUNRAVEN AND MOUNT-EARL (4th Earl of), WINDHAM THOMAS WINDHAM-QUIN, K.P.—B. 1841; parly. under-sec. of state for the cols., June, 1886, to Feb., 1886, and again Aug., 1886, to Feb., 1887.

**Version `col1919-L51932.v` — printed in editions [1919, 1920, 1921, 1922, 1923, 1924]:**

> DUNN, C. M.—B. 1881; ed. Clifton Coll. and King's Coll., Cambridge; honrs., 3rd cls., modern and medieval languages tripus, 1904; asst. res., N. Nigeria, 1909.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904–1904 | — | — | [1914, 1915, 1917, 1918] |
| 1 | 1904 | honrs., 3rd cls., modern and medieval languages tripus | — | [1919, 1920, 1921, 1922, 1923, 1924] |
| 2 | 1909–1909 | asst. res. | Northern Nigeria | [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |

## Candidate stint `Dunn, C. M___Nigeria___1915`

- Staff-list name: **Dunn, C. M** | colony: **Nigeria** | listed 1915–1919 | editions [1915, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | C. M. Dunn | Sixty-four Assistant District Officers | NORTHERN PROVINCES | — | — |
| 1918 | C. M. Dunn | Sixty‑four Assistant District Officer | Northern Provinces | — | — |
| 1919 | C. M. Dunn | Thirty Second Class District Officers | SOUTHERN PROVINCES | — | — |

### Deterministic checks: `dunn_c-m_b1881` vs `Dunn, C. M___Nigeria___1915`

- [PASS] surname_gate: bio 'DUNN' vs stint 'Dunn, C. M' (exact)
- [PASS] initials: bio ['C', 'M'] ~ stint ['C', 'M']
- [PASS] age_gate: stint starts 1915, birth 1881 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1919
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

