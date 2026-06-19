<!-- {"case_id": "case_bewley_harold-de-beauvioir_b1886", "bio_ids": ["bewley_harold-de-beauvioir_b1886"], "stint_ids": ["Bewley, H. de B___Nigeria___1917"]} -->
# Dossier case_bewley_harold-de-beauvioir_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bewley_harold-de-beauvioir_b1886`

- Printed name: **BEWLEY, HAROLD DE BEAUVIOIR**
- Birth year: 1886 (attested in editions [1931, 1932, 1933])
- Appears in editions: [1931, 1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1931-L62381.v` — printed in editions [1931, 1932, 1933]:**

> BEWLEY, HAROLD DE BEAUVIOIR, B.A. (Dublin).—B. 1886; ed. Oswestry Schol. and Trinity Coll., Dublin; (junr. mod., silver med.); asst. dist. comsnr., S. Nigeria, 1910; junr. asst. sec., S. Provs., 1914; A.D.C. to gov.-gen., 1915; pte. sec. to gov.-gen., 1916 and in 1918-19; attd., Nigeria Regt., 1917-18; 2nd asst. sec., S. Provs., 1918; local comsnr., Br. Empire Exhibn., 1925; cls. I, grade I, admstive serv., 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910–1910 | asst. dist. comsnr. | Southern Nigeria | [1931, 1932, 1933] |
| 1 | 1914–1914 | junr. asst. sec. | Southern Provinces | [1931, 1932, 1933] |
| 2 | 1915–1915 | A.D.C. to gov.-gen. | — | [1931, 1932, 1933] |
| 3 | 1916–1919 | pte. sec. to gov.-gen. | — | [1931, 1932, 1933] |
| 4 | 1917–1918 | attd. | Nigeria | [1931, 1932, 1933] |
| 5 | 1918–1918 | 2nd asst. sec. | Southern Provinces | [1931, 1932, 1933] |
| 6 | 1925–1925 | local comsnr. | — | [1931, 1932, 1933] |
| 7 | 1926–1926 | cls. I, grade I, admstive serv. | — | [1931, 1932, 1933] |

## Candidate stint `Bewley, H. de B___Nigeria___1917`

- Staff-list name: **Bewley, H. de B** | colony: **Nigeria** | listed 1917–1922 | editions [1917, 1918, 1919, 1920, 1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | H. de B. Bewley | Junior Assistant Secretary | Secretariat, Southern Provinces and Colony | — | — |
| 1918 | H. de B. Bewley | Junior Assistant Secretary | Secretariat, Southern Provinces and Colony | — | — |
| 1919 | H. de B. Bewley | Junior Assistant Secretary | Secretariat, Southern Provinces and Colony | — | — |
| 1920 | H. de B. Bewley | Second Assistant Secretary | Secretariat, Southern Provinces and Colony | — | — |
| 1921 | H. de B. Bewley | Assistant Secretary | Secretariat, Southern Provinces and Colony | — | — |
| 1922 | H. de B. Bewley | Assistant Secretary | Secretariat, Southern Provinces and Colony | — | — |

### Deterministic checks: `bewley_harold-de-beauvioir_b1886` vs `Bewley, H. de B___Nigeria___1917`

- [PASS] surname_gate: bio 'BEWLEY' vs stint 'Bewley, H. de B' (exact)
- [PASS] initials: bio ['H', 'D', 'B'] ~ stint ['H', 'D', 'B']
- [PASS] age_gate: stint starts 1917, birth 1886 (age 31)
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1917-1922
- [FAIL] position_sim: best 27 vs bar 60: 'attd.' ~ 'Second Assistant Secretary'
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

