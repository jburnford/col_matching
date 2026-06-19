<!-- {"case_id": "case_panet_charles-louis_b1870", "bio_ids": ["panet_charles-louis_b1870"], "stint_ids": ["Panet, Charles L___Canada___1919"]} -->
# Dossier case_panet_charles-louis_b1870

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `panet_charles-louis_b1870`

- Printed name: **PANET, CHARLES LOUIS**
- Birth year: 1870 (attested in editions [1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1921-L59010.v` — printed in editions [1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> PANET, LIEUT.-COL. CHARLES LOUIS.—B. 1870; ed. Ottawa Univ.; ent. civ. serv., Canada, 1889; sec., Canadian defence comttee., 1898; priv. sec. to late Sir F. W. Borden, min. of militia and defence, 1904-12; sec., dept. of militia and defence from 1907; pres., bd. of enquiry, re claims of applicants for the fenian raid volunteer bounty, 1912-15; pres. of pensions and claims bd.; ment. in disp. for serv. rendered in Can., 1914-1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889 | ent. civ. serv. | Canada | [1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1898 | sec., Canadian defence comttee | Canada *(inherited from previous clause)* | [1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1904–1912 | priv. sec. to late Sir F. W. Borden, min. of militia and defence | Canada *(inherited from previous clause)* | [1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1907 | sec., dept. of militia and defence from | Canada *(inherited from previous clause)* | [1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1912–1915 | pres., bd. of enquiry, re claims of applicants for the fenian raid volunteer bounty | Canada *(inherited from previous clause)* | [1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1914–1918 | ment. in disp. for serv. rendered in Can | Canada *(inherited from previous clause)* | [1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Panet, Charles L___Canada___1919`

- Staff-list name: **Panet, Charles L** | colony: **Canada** | listed 1919–1922 | editions [1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | Charles L. Panet | Departmental Secretary | Department of Militia and Defence | — | Lieut.-Col. |
| 1920 | Charles L. Panet | Departmental Secretary | Militia and Defence | — | Lieut.-Col. |
| 1922 | Charles L. Panet | Departmental Secretary | Militia and Defence | — | — |

### Deterministic checks: `panet_charles-louis_b1870` vs `Panet, Charles L___Canada___1919`

- [PASS] surname_gate: bio 'PANET' vs stint 'Panet, Charles L' (exact)
- [PASS] initials: bio ['C', 'L'] ~ stint ['C', 'L']
- [PASS] age_gate: stint starts 1919, birth 1870 (age 49)
- [PASS] colony: 6 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1919-1922
- [FAIL] position_sim: best 43 vs bar 60: 'ment. in disp. for serv. rendered in Can' ~ 'Departmental Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

