<!-- {"case_id": "case_moss_matthew-lewis_b1863", "bio_ids": ["moss_matthew-lewis_b1863"], "stint_ids": ["Moss, Matthew Lewis___Australia___1912"]} -->
# Dossier case_moss_matthew-lewis_b1863

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `moss_matthew-lewis_b1863`

- Printed name: **MOSS, MATTHEW LEWIS**
- Birth year: 1863 (attested in editions [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914])
- Appears in editions: [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914]

### Verbatim printed entry text (OCR)

**Version `col1907-L45959.v` — printed in editions [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914]:**

> MOSS, HON. MATTHEW LEWIS.—B. 1863; admitted to New Zealand bar, 1886; M.L.A. for N. Fremantle, W. Australia, 1896; M.L.C. for W. Prov., 1900; mem. of ministry in 1901, also, without portfolio, 1902-4; hon. min. and atty.-gen., W. Australia, Aug., 1905; K.C., 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1886–1886 | — | New Zealand | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 1 | 1896–1896 | M.L.A. for N. Fremantle | Western Australia | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 2 | 1900–1900 | M.L.C. for W. Prov. | — | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 3 | 1901–1901 | mem. of ministry | — | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 4 | 1902–1904 | without portfolio | — | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 5 | 1905–1905 | hon. min. and atty.-gen. | Western Australia | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914] |
| 6 | 1906–1906 | K.C. | — | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914] |

## Candidate stint `Moss, Matthew Lewis___Australia___1912`

- Staff-list name: **Moss, Matthew Lewis** | colony: **Australia** | listed 1912–1913 | editions [1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | Matthew Lewis Moss | Member of Legislative Council | Legislative Council | — | — |
| 1913 | Matthew Lewis Moss | Member | Legislative Council | — | — |

### Deterministic checks: `moss_matthew-lewis_b1863` vs `Moss, Matthew Lewis___Australia___1912`

- [PASS] surname_gate: bio 'MOSS' vs stint 'Moss, Matthew Lewis' (exact)
- [PASS] initials: bio ['M', 'L'] ~ stint ['M', 'L']
- [PASS] age_gate: stint starts 1912, birth 1863 (age 49)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1913
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

