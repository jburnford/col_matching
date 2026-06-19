<!-- {"case_id": "case_gunn_k-cameron_e1901", "bio_ids": ["gunn_k-cameron_e1901"], "stint_ids": ["Gunn, K. C___South Africa___1912"]} -->
# Dossier case_gunn_k-cameron_e1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gunn_k-cameron_e1901`

- Printed name: **GUNN, K. CAMERON**
- Birth year: not printed
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L60774.v` — printed in editions [1932]:**

> GUNN, K. CAMERON.—Clk., audit dept., May, 1901; ch. clk., civ. commr., Pretoria, 1902 and 1910; ch. clk., recr., rev., Joh'burg, 1905 and 1911; recr., rev., Krugerdorp, 1906; rec. rev., Joh'burg, 1920; ditto, Pretoria, 1923; ditto, Durban, 1928; ditto, Joh'burg, 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | Clk., audit dept. | — | [1932] |
| 1 | 1902–1910 | ch. clk., civ. commr. | Pretoria | [1932] |
| 2 | 1905–1911 | ch. clk., recr., rev. | Johannesburg | [1932] |
| 3 | 1906 | recr., rev. | Krugersdorp | [1932] |
| 4 | 1920 | rec. rev. | Johannesburg | [1932] |
| 5 | 1923 | ditto | Pretoria | [1932] |
| 6 | 1928 | ditto | Durban | [1932] |
| 7 | 1930 | ditto | Johannesburg | [1932] |

## Candidate stint `Gunn, K. C___South Africa___1912`

- Staff-list name: **Gunn, K. C** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | K. C. Gunn | Chief Clerk, Office of Receiver of Revenue | Inland Revenue Department | — | — |
| 1914 | K. C. Gunn | Receiver of Revenue | Inland Revenue Department | — | — |
| 1918 | K. C. Gunn | Receiver of Revenue | District Offices | — | — |

### Deterministic checks: `gunn_k-cameron_e1901` vs `Gunn, K. C___South Africa___1912`

- [PASS] surname_gate: bio 'GUNN' vs stint 'Gunn, K. C' (exact)
- [PASS] initials: bio ['K', 'C'] ~ stint ['K', 'C']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

