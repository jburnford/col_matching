<!-- {"case_id": "case_glass_david_b1829", "bio_ids": ["glass_david_b1829"], "stint_ids": ["Glass___Ascension___1890"]} -->
# Dossier case_glass_david_b1829

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['glass_david_b1829'] carry a single initial only — the namesake trap applies.

## Biography `glass_david_b1829`

- Printed name: **GLASS, DAVID**
- Birth year: 1829 (attested in editions [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906])
- Appears in editions: [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906]

### Verbatim printed entry text (OCR)

**Version `col1889-L33327.v` — printed in editions [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906]:**

> GLASS, DAVID, Q.C.—Born 20th July, 1829; Ed. Gram. Sch., Lond. (Ont); called to the bar; Q.C. for Ontario, 1875; elected alderman in 1855; and mayor in 1858-64-65; member of commons, Canada, for E. Middlesex, 1872; has been pol. mag., recorder, and also dep. judge of Middlesex, and bencher of law soc., Ont.; removed to Manitoba, 1882; solr. of Winnipeg, 1884; member leg. ass., Winnipeg, 1886; unanimously elected speaker, 1887 to 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1855–1855 | alderman | — | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 1 | 1858–1865 | mayor | — | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 2 | 1872–1872 | member of commons | Canada | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 3 | 1875–1875 | Q.C. | Ontario | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 4 | 1882–1882 | — | Manitoba | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 5 | 1884–1884 | solr. | Winnipeg | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 6 | 1886–1886 | member leg. ass. | Winnipeg | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 7 | 1887–1888 | speaker | — | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |

## Candidate stint `Glass___Ascension___1890`

- Staff-list name: **Glass** | colony: **Ascension** | listed 1890–1897 | editions [1890, 1894, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | Glass | Governor; Founder of the settlement | — | — | Corporal |
| 1894 | Glass | Governor | — | — | Corporal |
| 1897 | Glass | Governor | — | — | — |

### Deterministic checks: `glass_david_b1829` vs `Glass___Ascension___1890`

- [PASS] surname_gate: bio 'GLASS' vs stint 'Glass' (exact)
- [PASS] initials: bio ['D'] ~ stint ['?']
- [PASS] age_gate: stint starts 1890, birth 1829 (age 61)
- [FAIL] colony: no placed event resolves to 'Ascension'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1890-1897
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

