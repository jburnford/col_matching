<!-- {"case_id": "calib_gemini_fiji_0105", "bio_ids": ["forth_j-ogilvie_e1883"], "stint_ids": ["Forth, J. O___Fiji___1886"]} -->
# Dossier calib_gemini_fiji_0105

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `forth_j-ogilvie_e1883`

- Printed name: **FORTH, J. OGILVIE**
- Birth year: not printed
- Appears in editions: [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1896-L38914.v` — printed in editions [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]:**

> FORTH, J. OGILVIE.—Audit clk., Fiji, Aug., 1883; accntnt. native taxes and clk. nat. native accts., June, 1889; ch. clk. audit office, Oct., 1890; col. auditor, Nov., 1891; Oct., 1890, proceeded to Tonga to audit accts. of Tongan govt., for which he received thanks of King George Tubon's cabinet.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Audit clk. | Fiji | [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |
| 1 | 1889 | accntnt. native taxes and clk. nat. native accts. | — | [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |
| 2 | 1890 | ch. clk. audit office | — | [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |
| 3 | 1890 | — | Tonga | [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |
| 4 | 1891 | col. auditor | — | [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |

## Candidate stint `Forth, J. O___Fiji___1886`

- Staff-list name: **Forth, J. O** | colony: **Fiji** | listed 1886–1909 | editions [1886, 1888, 1894, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | J. O. Forth | Clerk, Second | Colonial Secretary's Department | — | — |
| 1888 | J. O. Forth | Second | Colonial Secretary | — | — |
| 1894 | J. O. Forth | Auditor | Colonial Secretary's Department | — | — |
| 1897 | J. O. Forth | Auditor | Colonial Secretary's Department | — | — |
| 1898 | J. O. Forth | Auditor | Colonial Secretary's Department | — | — |
| 1899 | J. O. Forth | Auditor | Colonial Secretary's Department | — | — |
| 1900 | J. O. Forth | Auditor | Colonial Secretary's Department | — | — |
| 1905 | J. O. Forth | Auditor | Colonial Secretary | — | — |
| 1906 | J. O. Forth | Colonial Auditor | Audit Department | — | — |
| 1907 | J. O. Forth | Colonial Auditor | Audit Department | — | — |
| 1908 | J. O. Forth | Colonial Auditor | Audit Department | — | — |
| 1909 | J. O. Forth | Colonial Auditor | Audit Department | — | — |

### Deterministic checks: `forth_j-ogilvie_e1883` vs `Forth, J. O___Fiji___1886`

- [PASS] surname_gate: bio 'FORTH' vs stint 'Forth, J. O' (exact)
- [PASS] initials: bio ['J', 'O'] ~ stint ['J', 'O']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1886-1909
- [PASS] position_sim: best 67 vs bar 60: 'Audit clk.' ~ 'Auditor'
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

