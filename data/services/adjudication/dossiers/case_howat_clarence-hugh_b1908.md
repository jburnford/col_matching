<!-- {"case_id": "case_howat_clarence-hugh_b1908", "bio_ids": ["howat_clarence-hugh_b1908"], "stint_ids": ["Howat, C. H___Nyasaland___1934"]} -->
# Dossier case_howat_clarence-hugh_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `howat_clarence-hugh_b1908`

- Printed name: **HOWAT, Clarence Hugh**
- Birth year: 1908 (attested in editions [1948, 1949, 1950])
- Honours: F.R.C.S.E, M.B
- Appears in editions: [1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33468.v` — printed in editions [1948, 1949, 1950]:**

> HOWAT, Clarence Hugh, M.B., Ch.B., F.R.C.S.E., D.T.M. & H.—b. 1908; ed. Edin. Acad. and Edin. Univ. (medallist and prizeman); D.M.O., Cyn., 1932; M.O., Nyasa., 1933; civ. surg., Aden, 1939; S.M.O. spec. surg., Cyp., 1944; med. offr. spec. (surg.), 1948; author of Medical Aid at Sea.

**Version `col1951-L39284.v` — printed in editions [1951]:**

> HOWAT, Clarence Hugh, M.B., Ch.B. (Edin.), F.R.C.S. (Edin.), D.T.M. & H. (Eng.).—b. 1908; ed. Edin. Acad. and Univ.; D.M.O., Cyp., 1932; M.O., Nyasa, 1933; S.M.O. (civ. surg.), Aden; 1939; surg. spec., Cyp., 1944; surg. spec., Tang., 1950.

**Version `col1933-L60826.v` — printed in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> HOWAT, CLARENCE HUGH, M.B., Ch.M. (Edin.), D.T.M. & H. (Lond.), F.R.C.S. (Edin.)—B. 1908; ed. Edin. Acad. and Univ. of Edin.; medallist in med. and clinical med.; dist. med. offr., Cyprus, 1932; med. offr., Nyasaland Prot., 1933; civ. surg., Aden, 1939; officiating sur. med. offr. and port health offr., July-Oct., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | D.M.O., Cyn | Cyprus | [1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951] |
| 1 | 1933 | M.O. | Nyasaland | [1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951] |
| 2 | 1939 | civ. surg. | Aden | [1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950] |
| 3 | 1939 | M.O. | Nyasaland *(inherited from previous clause)* | [1951] |
| 4 | 1944 | S.M.O. spec. surg. | Cyprus | [1948, 1949, 1950, 1951] |
| 5 | 1948 | med. offr. spec. (surg.) | Cyprus *(inherited from previous clause)* | [1948, 1949, 1950] |
| 6 | 1950 | surg. spec. | Tanganyika | [1951] |

## Candidate stint `Howat, C. H___Nyasaland___1934`

- Staff-list name: **Howat, C. H** | colony: **Nyasaland** | listed 1934–1939 | editions [1934, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | C. H. Howat | Medical Officer | Medical | — | — |
| 1936 | C. H. Howat | Medical Officers | Medical | — | — |
| 1937 | C. H. Howat | Medical Officer | Medical | — | — |
| 1939 | C. H. Howat | Medical Officers | Medical | — | — |

### Deterministic checks: `howat_clarence-hugh_b1908` vs `Howat, C. H___Nyasaland___1934`

- [PASS] surname_gate: bio 'HOWAT' vs stint 'Howat, C. H' (exact)
- [PASS] initials: bio ['C', 'H'] ~ stint ['C', 'H']
- [PASS] age_gate: stint starts 1934, birth 1908 (age 26)
- [PASS] colony: 2 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
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

