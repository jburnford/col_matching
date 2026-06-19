<!-- {"case_id": "case_ingles_f-h_b1878", "bio_ids": ["ingles_f-h_b1878"], "stint_ids": ["Ingles, F. H___Nigeria___1915"]} -->
# Dossier case_ingles_f-h_b1878

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ingles_f-h_b1878`

- Printed name: **INGLES, F. H**
- Birth year: 1878 (attested in editions [1912, 1913, 1914, 1917, 1918, 1919, 1920, 1922, 1923, 1924, 1925, 1928, 1929, 1930, 1931, 1932])
- Appears in editions: [1912, 1913, 1914, 1917, 1918, 1919, 1920, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1912-L45133.v` — printed in editions [1912, 1913, 1914, 1917, 1918, 1919, 1920, 1922, 1923, 1924, 1925, 1928, 1929, 1930, 1931, 1932]:**

> INGLES, F. H.—B. 1878; ed. at U.S. Coll., Westward Ho!, Newton Coll., Devon, and Jesus Coll., Cambridge; B.A. Cantab., 1902; asst. dist. comnr., S. Nigeria, 6th Oct., 1906; dist. comnr., 2nd grade, 17th Feb., 1913; dist. offr., 1st grade, 20th Oct., 1919; res., 5th Feb., 1922; cls. I., grade I., admstd. serv., 1922; ag. senr. comnr., 31st Oct., 1924.

**Version `col1927-L59971.v` — printed in editions [1927]:**

> INGLES, F. H.—B. 1878; ed. at U.S. Coll., Westward Ho., Newton Coll., Devon, and Jesus Coll., Cambridge; B.A. Cantab., 1902; asst. dist. commr., S. Nigeria, 6th Oct., 1908; dist. commr., 2nd grade, 17th Feb., 1913; dist. offr., 1st grade, 20th Oct., 1919; res., 5th Feb., 1922; ag. sen. res., 31st Oct., 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902 | B.A. Cantab | — | [1912, 1913, 1914, 1917, 1918, 1919, 1920, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 1 | 1906 | asst. dist. comnr. | Southern Nigeria | [1912, 1913, 1914, 1917, 1918, 1919, 1920, 1922, 1923, 1924, 1925, 1928, 1929, 1930, 1931, 1932] |
| 2 | 1908 | asst. dist. commr. | Southern Nigeria | [1927] |
| 3 | 1913 | dist. comnr., 2nd grade | Southern Nigeria *(inherited from previous clause)* | [1912, 1913, 1914, 1917, 1918, 1919, 1920, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 4 | 1919 | dist. offr., 1st grade | Southern Nigeria *(inherited from previous clause)* | [1912, 1913, 1914, 1917, 1918, 1919, 1920, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 5 | 1922 | res | Southern Nigeria *(inherited from previous clause)* | [1912, 1913, 1914, 1917, 1918, 1919, 1920, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 6 | 1924 | ag. senr. comnr | Southern Nigeria *(inherited from previous clause)* | [1912, 1913, 1914, 1917, 1918, 1919, 1920, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |

## Candidate stint `Ingles, F. H___Nigeria___1915`

- Staff-list name: **Ingles, F. H** | colony: **Nigeria** | listed 1915–1919 | editions [1915, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | F. H. Ingles | Thirty Second Class District Officers | NORTHERN PROVINCES | — | — |
| 1918 | F. H. Ingles | Second Class District Officer | Southern Provinces | — | — |
| 1919 | F. H. Ingles | Thirty Second Class District Officers | SOUTHERN PROVINCES | — | — |

### Deterministic checks: `ingles_f-h_b1878` vs `Ingles, F. H___Nigeria___1915`

- [PASS] surname_gate: bio 'INGLES' vs stint 'Ingles, F. H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1915, birth 1878 (age 37)
- [PASS] colony: 6 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1915-1919
- [FAIL] position_sim: best 50 vs bar 60: 'dist. offr., 1st grade' ~ 'Second Class District Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

