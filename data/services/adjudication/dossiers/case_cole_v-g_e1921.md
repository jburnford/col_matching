<!-- {"case_id": "case_cole_v-g_e1921", "bio_ids": ["cole_v-g_e1921"], "stint_ids": ["Cole, G___Bahamas___1886"]} -->
# Dossier case_cole_v-g_e1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 96 official(s) with this surname in the graph's staff lists; 31 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cole_v-g_e1921`

- Printed name: **COLE, V. G**
- Birth year: not printed
- Appears in editions: [1924, 1925, 1927, 1928]

### Verbatim printed entry text (OCR)

**Version `col1924-L53161.v` — printed in editions [1924, 1925, 1927, 1928]:**

> COLE, V. G.—Asst. dist. comsnr., Kenya, June, 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | Asst. dist. comsnr. | Kenya | [1924, 1925, 1927, 1928] |

## Candidate stint `Cole, G___Bahamas___1886`

- Staff-list name: **Cole, G** | colony: **Bahamas** | listed 1886–1913 | editions [1886, 1888, 1889, 1890, 1894, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | G. Cole | Inspector of Public Schools | Civil Establishment | — | — |
| 1888 | G. Cole | Inspector of Public Schools | Civil Establishment | — | — |
| 1889 | G. Cole | Inspector of Public Schools | Civil Establishment | — | — |
| 1890 | G. Cole | Inspector of Public Schools | Civil Establishment | — | — |
| 1894 | G. Cole | Inspector of Public Schools | Civil Establishment | — | — |
| 1897 | G. Cole | Inspector of Public Schools | Civil Establishment | — | — |
| 1898 | G. Cole | Inspector of Public Schools | Civil Establishment | — | — |
| 1899 | G. Cole | Secretary to the Board and Inspector of Schools | Education Department | — | — |
| 1900 | G. Cole | Secretary to the Board and Inspector of Schools | Education Department | — | — |
| 1905 | G. Cole | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1906 | G. Cole | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1907 | G. Cole | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1908 | G. Cole | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1909 | G. Cole | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1910 | G. Cole | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1911 | G. Cole | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1912 | G. Cole | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1913 | G. Cole | Inspector and General Superintendent of Schools | Education Department | — | — |

### Deterministic checks: `cole_v-g_e1921` vs `Cole, G___Bahamas___1886`

- [PASS] surname_gate: bio 'COLE' vs stint 'Cole, G' (exact)
- [PASS] initials: bio ['V', 'G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Bahamas'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1913
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

