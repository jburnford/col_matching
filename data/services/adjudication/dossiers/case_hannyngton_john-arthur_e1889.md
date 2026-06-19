<!-- {"case_id": "case_hannyngton_john-arthur_e1889", "bio_ids": ["hannyngton_john-arthur_e1889"], "stint_ids": ["Hannington, J. A___British Somaliland___1906"]} -->
# Dossier case_hannyngton_john-arthur_e1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `hannyngton_john-arthur_e1889` ↔ `Hannington, J. A___British Somaliland___1906` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Hannington, J. A___British Somaliland___1906` is also gate-compatible with biography(ies) outside this case: ['hannington_john-arthur_e1889'] (already linked elsewhere or filtered).

## Biography `hannyngton_john-arthur_e1889`

- Printed name: **HANNYNGTON, JOHN ARTHUR**
- Birth year: not printed
- Honours: C.M.G (1911)
- Appears in editions: [1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1906-L45924.v` — printed in editions [1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]:**

> HANNYNGTON, JOHN ARTHUR, C.M.G. (1911).—Capt., Indian army; temp. maj., King's African Rifles; ed. at Unit. Serv. Coll., Westward Ho!; passed in Hindustani, higher standard, Pushtu, higher standard, Kiswahili, gov't. test. exam. for promotion to field offr. and staff employ; gazetted 8th June, 1889; apptd. comdt., Jubaland Camel Corps, 15th Dec., 1901; comdt., 6th King's African Rifles, Somaliland Prot., 28th Feb., 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889 | gazetted | — | [1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |
| 1 | 1901 | apptd. comdt., Jubaland Camel Corps | — | [1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |
| 2 | 1905 | comdt., 6th King's African Rifles | Somaliland | [1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |

## Candidate stint `Hannington, J. A___British Somaliland___1906`

- Staff-list name: **Hannington, J. A** | colony: **British Somaliland** | listed 1906–1909 | editions [1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | J. A. Hannington | Commandant 6th Battalion King's African Rifles | Military Department | — | Major |
| 1907 | J. A. Hannington | Commandant 6th Battalion King's African Rifles | Military Department | — | Major |
| 1908 | J. A. Hannington | Commandant 6th Battalion King's African Rifles | Military Department | — | Major |
| 1909 | J. A. Hannington | Commandant 6th Battalion King's African Rifles | Military Department | — | Major |

### Deterministic checks: `hannyngton_john-arthur_e1889` vs `Hannington, J. A___British Somaliland___1906`

- [PASS] surname_gate: bio 'HANNYNGTON' vs stint 'Hannington, J. A' (fuzzy:1)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'British Somaliland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1906-1909
- [PASS] position_sim: best 89 vs bar 60: 'comdt., 6th King's African Rifles' ~ 'Commandant 6th Battalion King's African Rifles'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 4 agreeing edition-year(s) [1906, 1907, 1908, 1909] pos~89 (bar: >=2)
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

