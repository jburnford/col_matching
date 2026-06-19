<!-- {"case_id": "case_brace_ivor-llwellyn_b1898", "bio_ids": ["brace_ivor-llwellyn_b1898"], "stint_ids": ["Brace, I. L___Nigeria___1934", "Brace, Ivor___North Borneo___1949"]} -->
# Dossier case_brace_ivor-llwellyn_b1898

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Brace, I. L___Nigeria___1934` is also gate-compatible with biography(ies) outside this case: ['brace_ivor-llanelyn_b1898', 'brace_ivor-llewellyn_b1898'] (already linked elsewhere or filtered).
- NOTE: stint `Brace, Ivor___North Borneo___1949` is also gate-compatible with biography(ies) outside this case: ['brace_ivor-llanelyn_b1898', 'brace_ivor-llewellyn_b1898'] (already linked elsewhere or filtered).

## Biography `brace_ivor-llwellyn_b1898`

- Printed name: **BRACE, IVOR LLWELLYN**
- Birth year: 1898 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L65169.v` — printed in editions [1939, 1940]:**

> BRACE, IVOR LLWELLYN, B.L.—B. 1898; called to bar, Gray's Inn, 1921; pol. mag., Gold Coast, 1930; ditto, Nigeria, 1931; crown coun., 1932; ag. solr.-gen., July-Oct., 1937; asst. judge, prot. et al., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | called to bar, Gray's Inn | — | [1939, 1940] |
| 1 | 1930 | pol. mag. | Gold Coast | [1939, 1940] |
| 2 | 1931 | pol. mag. | Nigeria | [1939, 1940] |
| 3 | 1932 | crown coun | Nigeria *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1937 | ag. solr.-gen., July- | Nigeria *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Brace, I. L___Nigeria___1934`

- Staff-list name: **Brace, I. L** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | I. L. Brace | Crown Counsel | Legal | — | — |
| 1936 | I. L. Brace | Crown Counsel | Legal | — | — |
| 1939 | I. L. Brace | Assistant Judge | Protectorate Courts | — | — |

### Deterministic checks: `brace_ivor-llwellyn_b1898` vs `Brace, I. L___Nigeria___1934`

- [PASS] surname_gate: bio 'BRACE' vs stint 'Brace, I. L' (exact)
- [PASS] initials: bio ['I', 'L'] ~ stint ['I', 'L']
- [PASS] age_gate: stint starts 1934, birth 1898 (age 36)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1939
- [PASS] position_sim: best 87 vs bar 60: 'crown coun' ~ 'Crown Counsel'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Brace, Ivor___North Borneo___1949`

- Staff-list name: **Brace, Ivor** | colony: **North Borneo** | listed 1949–1952 | editions [1949, 1950, 1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | I. L. Brace | Chief Justice | Judicial | — | — |
| 1950 | I. L. Brace | Chief Justice | Judicial | — | — |
| 1951 | I. L. Brace | Chief Justice | Judicial | — | — |
| 1952 | Sir Ivor Brace | Chief Justice, Supreme Court of Sarawak, North Borneo and Brunei | Civil Establishment | — | — |

### Deterministic checks: `brace_ivor-llwellyn_b1898` vs `Brace, Ivor___North Borneo___1949`

- [PASS] surname_gate: bio 'BRACE' vs stint 'Brace, Ivor' (exact)
- [PASS] initials: bio ['I', 'L'] ~ stint ['I']
- [PASS] age_gate: stint starts 1949, birth 1898 (age 51)
- [FAIL] colony: no placed event resolves to 'North Borneo'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1952
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

