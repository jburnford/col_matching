<!-- {"case_id": "case_grantham_sidney-howard_b1883", "bio_ids": ["grantham_sidney-howard_b1883"], "stint_ids": ["Grantham, S. H___Nigeria___1927"]} -->
# Dossier case_grantham_sidney-howard_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `grantham_sidney-howard_b1883`

- Printed name: **GRANTHAM, SIDNEY HOWARD**
- Birth year: 1883 (attested in editions [1935, 1936])
- Appears in editions: [1935, 1936]

### Verbatim printed entry text (OCR)

**Version `dol1935-L58993.v` — printed in editions [1935, 1936]:**

> GRANTHAM, SIDNEY HOWARD.—B. 1883; clk., W.O., Apr., 1901; asst. acct., army accnts. dept., Apr., 1904; served S. Africa, 1904-07 and 1912-14; asst. commr., pol., Nigeria, May, 1915; sent. ditto, Apr., 1930; asst. inspr.-gen., pol., Jan., 1931; ag. inspr.-gen., pol., in 1932, 1933 and 1934; dep. inspr.-gen., pol., July, 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | clk. | — | [1935, 1936] |
| 1 | 1904 | asst. acct. | — | [1935, 1936] |
| 2 | 1904–1914 | — | South Africa | [1935, 1936] |
| 3 | 1915 | asst. commr., pol. | Nigeria | [1935, 1936] |
| 4 | 1930 | sent. ditto | — | [1935, 1936] |
| 5 | 1931 | asst. inspr.-gen., pol. | — | [1935, 1936] |
| 6 | 1932–1934 | ag. inspr.-gen., pol. | — | [1935, 1936] |
| 7 | 1934 | dep. inspr.-gen., pol. | — | [1935, 1936] |

## Candidate stint `Grantham, S. H___Nigeria___1927`

- Staff-list name: **Grantham, S. H** | colony: **Nigeria** | listed 1927–1936 | editions [1927, 1929, 1930, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | S. H. Grantham | Commissioner | Police, Northern Provinces | — | — |
| 1929 | S. H. Grantham | Commissioners and Assistant Commissioners | Marine | M.C., D.S.O., M.C., D.S.O., M.C., D.C.M., M.C. | — |
| 1930 | S. H. Grantham | Commissioners and Assistant Commissioners | Police | — | — |
| 1933 | S. H. Grantham | Assistant Inspector-General of Police | Police | — | — |
| 1934 | S. H. Grantham | Assistant Inspector-General of Police | Police | — | — |
| 1936 | S. H. Grantham | Assistant Inspector-General of Police | Police | — | — |

### Deterministic checks: `grantham_sidney-howard_b1883` vs `Grantham, S. H___Nigeria___1927`

- [PASS] surname_gate: bio 'GRANTHAM' vs stint 'Grantham, S. H' (exact)
- [PASS] initials: bio ['S', 'H'] ~ stint ['S', 'H']
- [PASS] age_gate: stint starts 1927, birth 1883 (age 44)
- [PASS] colony: 1 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1936
- [FAIL] position_sim: best 49 vs bar 60: 'asst. commr., pol.' ~ 'Commissioners and Assistant Commissioners'
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

