<!-- {"case_id": "case_bruford_frederick-horatio_b1846", "bio_ids": ["bruford_frederick-horatio_b1846"], "stint_ids": ["Bruford, F. H___Australia___1912", "Bruford, F. H___Victoria___1898"]} -->
# Dossier case_bruford_frederick-horatio_b1846

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bruford_frederick-horatio_b1846`

- Printed name: **BRUFORD, FREDERICK HORATIO**
- Birth year: 1846 (attested in editions [1909, 1910, 1911, 1912, 1913, 1915, 1917, 1918])
- Appears in editions: [1909, 1910, 1911, 1912, 1913, 1915, 1917, 1918]

### Verbatim printed entry text (OCR)

**Version `col1909-L44188.v` — printed in editions [1909, 1910, 1911, 1912, 1913, 1915, 1917, 1918]:**

> BRUFORD, FREDERICK HORATIO.—B. 1846; aud.-gen., Victoria, 1903.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | aud.-gen. | Victoria | [1909, 1910, 1911, 1912, 1913, 1915, 1917, 1918] |

## Candidate stint `Bruford, F. H___Australia___1912`

- Staff-list name: **Bruford, F. H** | colony: **Australia** | listed 1912–1918 | editions [1912, 1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | F. H. Bruford | Auditor-General | Public Service | — | — |
| 1913 | F. H. Bruford | Auditor-General | Parliamentary Staff | — | — |
| 1918 | F. H. Bruford | Auditor-General | Public Service | — | — |

### Deterministic checks: `bruford_frederick-horatio_b1846` vs `Bruford, F. H___Australia___1912`

- [PASS] surname_gate: bio 'BRUFORD' vs stint 'Bruford, F. H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1912, birth 1846 (age 66)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bruford, F. H___Victoria___1898`

- Staff-list name: **Bruford, F. H** | colony: **Victoria** | listed 1898–1900 | editions [1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | F. H. Bruford | Deputy-Commissioner | Income Tax Office | — | — |
| 1899 | F. H. Bruford | Deputy-Commissioner | Income Tax Office | — | — |
| 1900 | F. H. Bruford | Deputy-Commissioner | Income Tax Office | — | — |

### Deterministic checks: `bruford_frederick-horatio_b1846` vs `Bruford, F. H___Victoria___1898`

- [PASS] surname_gate: bio 'BRUFORD' vs stint 'Bruford, F. H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1898, birth 1846 (age 52)
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1900
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

