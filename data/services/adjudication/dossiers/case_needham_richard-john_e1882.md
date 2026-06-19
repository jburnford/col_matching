<!-- {"case_id": "case_needham_richard-john_e1882", "bio_ids": ["needham_richard-john_e1882"], "stint_ids": ["Needham, J___Trinidad___1877", "Needham, R. J___South Australia___1888"]} -->
# Dossier case_needham_richard-john_e1882

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Needham, J___Trinidad___1877` is also gate-compatible with biography(ies) outside this case: ['needham_joseph_e1837'] (already linked elsewhere or filtered).
- NOTE: stint `Needham, R. J___South Australia___1888` is also gate-compatible with biography(ies) outside this case: ['needham_joseph_e1837'] (already linked elsewhere or filtered).

## Biography `needham_richard-john_e1882`

- Printed name: **NEEDHAM, RICHARD JOHN**
- Birth year: not printed
- Appears in editions: [1906, 1907, 1908, 1909, 1910, 1911]

### Verbatim printed entry text (OCR)

**Version `col1906-L47118.v` — printed in editions [1906, 1907, 1908, 1909, 1910, 1911]:**

> NEEDHAM, RICHARD JOHN.—Inspr. of stock, S. Australia, Oct., 1882, to June, 1883; ditto, Dec., 1886; dep. ch. inspr. of stock and dep. regist. of brands, Jan., 1891; ch. inspr. of ditto, July, 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882–1883 | Inspr. of stock | South Australia | [1906, 1907, 1908, 1909, 1910, 1911] |
| 1 | 1886 | Inspr. of stock | — | [1906, 1907, 1908, 1909, 1910, 1911] |
| 2 | 1891 | dep. ch. inspr. of stock and dep. regist. of brands | — | [1906, 1907, 1908, 1909, 1910, 1911] |
| 3 | 1905 | ch. inspr. of stock | — | [1906, 1907, 1908, 1909, 1910, 1911] |

## Candidate stint `Needham, J___Trinidad___1877`

- Staff-list name: **Needham, J** | colony: **Trinidad** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. Needham | Chief Justice | Judicial Department | — | — |
| 1878 | Sir J. Needham | Chief Justice | Judicial Department | — | — |
| 1879 | Sir J. Needham, Kt. | Chief Justice | Judicial Department | — | — |
| 1880 | Sir J. Needham | Chief Justice | Judicial Department | Kt. | — |
| 1883 | Sir J. Needham | Chief Justice | Judicial Department | — | — |

### Deterministic checks: `needham_richard-john_e1882` vs `Needham, J___Trinidad___1877`

- [PASS] surname_gate: bio 'NEEDHAM' vs stint 'Needham, J' (exact)
- [PASS] initials: bio ['R', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Needham, R. J___South Australia___1888`

- Staff-list name: **Needham, R. J** | colony: **South Australia** | listed 1888–1909 | editions [1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | R. J. Needham | Inspector | Sheep Inspector's Department | — | — |
| 1889 | R. J. Needham | — | Sheep Inspector's Department | — | — |
| 1890 | R. J. Needham | Inspectors | Sheep Inspector's Department | — | — |
| 1894 | R. J. Needham | Inspector | Sheep Inspector's Department | — | — |
| 1896 | R. J. Needham | Inspector | Sheep Inspector's Department | — | — |
| 1898 | R. J. Needham | Inspectors | Sheep Inspector's Department | — | — |
| 1899 | R. J. Needham | Inspectors | Stock and Brands Department | — | — |
| 1900 | R. J. Needham | Inspector | Stock and Brands Department | — | — |
| 1905 | R. J. Needham | Inspector | Stock and Brands Department | — | — |
| 1906 | R. J. Needham | Chief Inspector | Stock and Brands Department | — | — |
| 1907 | R. J. Needham | Chief Inspector | Stock and Brands Department | — | — |
| 1908 | R. J. Needham | Chief Inspector | Stock and Brands Department | — | — |
| 1909 | R. J. Needham | Chief Inspector | Stock and Brands Department | — | — |

### Deterministic checks: `needham_richard-john_e1882` vs `Needham, R. J___South Australia___1888`

- [PASS] surname_gate: bio 'NEEDHAM' vs stint 'Needham, R. J' (exact)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1909
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

