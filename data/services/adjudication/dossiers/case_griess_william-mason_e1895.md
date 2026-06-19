<!-- {"case_id": "case_griess_william-mason_e1895", "bio_ids": ["griess_william-mason_e1895"], "stint_ids": ["Griess, W. M___Kenya___1909"]} -->
# Dossier case_griess_william-mason_e1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `griess_william-mason_e1895`

- Printed name: **GRIESS, WILLIAM MASON**
- Birth year: not printed
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1908-L44872.v` — printed in editions [1908, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]:**

> GRIESS, WILLIAM MASON.—Ed. at Repton Schl. and Cooper's Hill; senr. asst. engrnr., Uganda Rly., 20th Dec., 1895; dist. engrnr., Apr., 1909.

**Version `col1909-L45737.v` — printed in editions [1909]:**

> GRIESS, William Mason.—Ed. at Repton Schl., and Cooper's Hill; senr. asst. engrnr., Uganda Rly., 20th Dec., 1895. GRiffin, Chas. James.—B. 1875; R.A. (Hons.) Royal Univ., Ireland; 1st schlr. in mod. liter.; triple exhib.; chancellor's gold medallist; called to the bar, Ireland, June, 1898; apptd. cmr. prostr., B. Cent. Africa Prot., Aug., 1901; ag. chief judicial offr., and H.B.M. vice-consul, Nov., 1901, to June, 1902; ag. judge of high ct., Feb. to Oct., 1904; apptd. regsr. gen.of births, deaths, marriages, and banking, under various local ordinances, also regsr. of deeds and admstr. of deceased estates under the high ct., judge of high ct., B.C. Africa, 17th Feb., 1906; atty.-gen., Nov., 1906; mem. of E. Africa Prot., ct. of appeal.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | senr. asst. engrnr., Uganda Rly | Uganda | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |
| 1 | 1909 | dist. engrnr | Uganda *(inherited from previous clause)* | [1908, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |

## Candidate stint `Griess, W. M___Kenya___1909`

- Staff-list name: **Griess, W. M** | colony: **Kenya** | listed 1909–1922 | editions [1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | W. M. Griess | Engineering | Railway | — | — |
| 1910 | W. M. Griess | Engineering | Engineering | — | — |
| 1912 | W. M. Griess | Engineering | Engineering | — | — |
| 1913 | W. M. Griess | Engineering | Railway | — | — |
| 1914 | W. M. Griess | Engineering | Accounts | — | — |
| 1915 | W. M. Griess | District Engineer | Engineering | — | — |
| 1917 | W. M. Griess | District Engineers | Engineering | — | — |
| 1918 | W. M. Griess | District Engineer | Engineering | — | — |
| 1919 | W. M. Griess | District Engineer | Engineering | — | — |
| 1920 | W. M. Griess | District Engineer | Engineering | — | — |
| 1922 | W. M. Griess | District Engineers | Engineering | — | — |

### Deterministic checks: `griess_william-mason_e1895` vs `Griess, W. M___Kenya___1909`

- [PASS] surname_gate: bio 'GRIESS' vs stint 'Griess, W. M' (exact)
- [PASS] initials: bio ['W', 'M'] ~ stint ['W', 'M']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1922
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

