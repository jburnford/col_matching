<!-- {"case_id": "case_smartt_fitzpatrick-forbes-pearce_e1921", "bio_ids": ["smartt_fitzpatrick-forbes-pearce_e1921"], "stint_ids": ["Smartt, F. F. P___Northern Rhodesia___1927"]} -->
# Dossier case_smartt_fitzpatrick-forbes-pearce_e1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Smartt, F. F. P___Northern Rhodesia___1927` is also gate-compatible with biography(ies) outside this case: ['smartt_fitzpatrick-forbes-percy_b1900'] (already linked elsewhere or filtered).

## Biography `smartt_fitzpatrick-forbes-pearce_e1921`

- Printed name: **SMARTT, FITZPATRICK FORBES PEARCE**
- Birth year: not printed
- Appears in editions: [1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L62262.v` — printed in editions [1935, 1936, 1937, 1939, 1940]:**

> SMARTT, FITZPATRICK FORBES PEARCE.—Ed. Denstone Coll.; probationer, col. audit dept., July, 1921; asst. audr., Br. Honduras, Oct., 1921; asst. audr., N. Rhodesia, May, 1925; disto., Tanganyika Territory, 1934; senr. asst. audr., Apr., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | probationer, col. audit dept | — | [1935, 1936, 1937, 1939, 1940] |
| 1 | 1921 | asst. audr., Br. Honduras | — | [1935, 1936, 1937, 1939, 1940] |
| 2 | 1925 | asst. audr., N. Rhodesia | — | [1935, 1936, 1937, 1939, 1940] |
| 3 | 1934 | disto., Tanganyika Territory | Tanganyika | [1935, 1936, 1937, 1939, 1940] |
| 4 | 1937 | senr. asst. audr | Tanganyika *(inherited from previous clause)* | [1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Smartt, F. F. P___Northern Rhodesia___1927`

- Staff-list name: **Smartt, F. F. P** | colony: **Northern Rhodesia** | listed 1927–1934 | editions [1927, 1928, 1929, 1930, 1931, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | F. F. P. Smartt | Assistant Auditors | Audit | — | — |
| 1928 | F. F. P. Smartt | Assistant Auditor | Audit | — | — |
| 1929 | F. F. P. Smartt | Assistant Auditor | Audit | — | — |
| 1930 | F. F. P. Smartt | Assistant Auditor | Audit | — | — |
| 1931 | F. F. P. Smartt | Assistant Auditors | Audit | — | — |
| 1933 | F. F. P. Smartt | Assistant Auditor | Audit | — | — |
| 1934 | F. F. P. Smartt | Assistant Auditor | Audit | — | — |

### Deterministic checks: `smartt_fitzpatrick-forbes-pearce_e1921` vs `Smartt, F. F. P___Northern Rhodesia___1927`

- [PASS] surname_gate: bio 'SMARTT' vs stint 'Smartt, F. F. P' (exact)
- [PASS] initials: bio ['F', 'F', 'P'] ~ stint ['F', 'F', 'P']
- [PASS] age_gate: stint starts 1927; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1934
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

