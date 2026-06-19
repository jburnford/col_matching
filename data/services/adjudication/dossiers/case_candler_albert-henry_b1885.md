<!-- {"case_id": "case_candler_albert-henry_b1885", "bio_ids": ["candler_albert-henry_b1885"], "stint_ids": ["Candler, A. H___Gold Coast___1923"]} -->
# Dossier case_candler_albert-henry_b1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `candler_albert-henry_b1885`

- Printed name: **CANDLER, ALBERT HENRY**
- Birth year: 1885 (attested in editions [1932])
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L58968.v` — printed in editions [1932]:**

> CANDLER, REV. ALBERT HENRY, B.A. (Manchester).—B. 1885; ed. pvtly. and St. John's Coll., Oxford; awarded Casdier exhib. in law, 2nd cls. final hona. schl. of jurisprudence; mily. serv. France and Italy; capt., sp. list; ment. in desps.; called to bar, 1921; practised on Western Circuit and in chambers; lect. in law to Univ. Coll., Southampton, 1925-28 and Sussex Schl. of Law, 1926-28; dep. chmn., cta. of refnse. for Metropolitan dist. under unemployment acts, Miny. of Lab., 1928; stip. and circuit mag., Bahamas, and coroner for New Providence, Oct., 1928; ag. atty. gen., in 1929 and 1930; ag. ch. just., Sept. to Oct., 1929; ag. atty. gen. and temp. mem., exec. coun., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921–1921 | called to bar | — | [1932] |
| 1 | 1925–1928 | lect. in law to Univ. Coll., Southampton and Sussex Schl. of Law | — | [1932] |
| 2 | 1928–1928 | dep. chmn., cta. of refnse. for Metropolitan dist. under unemployment acts, Miny. of Lab. | — | [1932] |
| 3 | 1928–1928 | stip. and circuit mag., and coroner for New Providence | Bahamas | [1932] |
| 4 | 1929–1930 | ag. atty. gen. | — | [1932] |
| 5 | 1929–1929 | ag. ch. just. | — | [1932] |
| 6 | 1931–1931 | ag. atty. gen. and temp. mem., exec. coun. | — | [1932] |

## Candidate stint `Candler, A. H___Gold Coast___1923`

- Staff-list name: **Candler, A. H** | colony: **Gold Coast** | listed 1923–1930 | editions [1923, 1924, 1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | A. H. Candler | Assistant Masters | Education Department | — | — |
| 1924 | A. H. Candler | Assistant Masters | Education Department | — | — |
| 1927 | A. H. Candler | Superintendent of Education | Education Department | — | — |
| 1928 | Rev. A. H. Candler | Superintendent of Education | Northern Territories | — | — |
| 1929 | Rev. A. H. Candler | Superintendent of Education | Education Department | — | — |
| 1930 | A. H. Candler | Superintendent of Education | Northern Territories | — | — |

### Deterministic checks: `candler_albert-henry_b1885` vs `Candler, A. H___Gold Coast___1923`

- [PASS] surname_gate: bio 'CANDLER' vs stint 'Candler, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1923, birth 1885 (age 38)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1930
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

