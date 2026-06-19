<!-- {"case_id": "case_mardsden_herbert_b1887", "bio_ids": ["mardsden_herbert_b1887"], "stint_ids": ["Madsen, V. H. B___Australia___1912"]} -->
# Dossier case_mardsden_herbert_b1887

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mardsden_herbert_b1887'] carry a single initial only — the namesake trap applies.

## Biography `mardsden_herbert_b1887`

- Printed name: **MARDSDEN, HERBERT**
- Birth year: 1887 (attested in editions [1934, 1935])
- Honours: A.I.C
- Appears in editions: [1932, 1933, 1934, 1935, 1940]

### Verbatim printed entry text (OCR)

**Version `col1934-L61514.v` — printed in editions [1934, 1935]:**

> MARDSDEN, HERBERT, B.SC. (Manch.), A.I.C.—B. 1887; ed. Hulls Hall, Manch. Univ.; asst. chem., inst. med. resch., F.M.S., Jan., 1914; chmn., do., Jan., 1921; chem., trade and cust. dept., F.M.S., Aug., 1928.

**Version `col1940-L66632.v` — printed in editions [1940]:**

> MARSDEN, HERBERT, B.Sc. (Manc.), A.I.C.—B. 1887; ed. Hulme Hall, Manch. Univ.; asst. chem., inst. med. resch., F.M.S., Jan., 1914; chem., do., Jan., 1921; chem., trade and cust. dept., F.M.S., Aug., 1928.

**Version `col1932-L62367.v` — printed in editions [1932, 1933]:**

> MARDEN, HERBERT, B.Sc. (Manq.), A.I.C.—B. 1887; astt. chem., inst. med. resech., F.M.S., Jan., 1914; chem., trade and cust. dept., F.M.S., Aug., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | asst. chem., inst. med. resch. | Federated Malay States | [1932, 1933, 1934, 1935, 1940] |
| 1 | 1921 | chmn. | Dominions Office | [1934, 1935, 1940] |
| 2 | 1928 | chem., trade and cust. dept. | Federated Malay States | [1932, 1933, 1934, 1935, 1940] |

## Candidate stint `Madsen, V. H. B___Australia___1912`

- Staff-list name: **Madsen, V. H. B** | colony: **Australia** | listed 1912–1918 | editions [1912, 1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | V. H. B. Madsen | Acting Secretary Public Service Board | Chief Secretary's Department | — | — |
| 1913 | V. H. B. Madsen | Acting Secretary Public Service Board | Chief Secretary's Department | — | — |
| 1918 | V. H. B. Madsen | Secretary Public Service Board | Chief Secretary's Department | — | — |

### Deterministic checks: `mardsden_herbert_b1887` vs `Madsen, V. H. B___Australia___1912`

- [PASS] surname_gate: bio 'MARDSDEN' vs stint 'Madsen, V. H. B' (fuzzy:2)
- [PASS] initials: bio ['H'] ~ stint ['V', 'H', 'B']
- [PASS] age_gate: stint starts 1912, birth 1887 (age 25)
- [FAIL] colony: no placed event resolves to 'Australia'
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

