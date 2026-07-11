# Weak-key namesake stress test (career stringing)

A career whose within-volume bio links span >1 unified person was
strung across two real people. Testable = careers with >=2 distinct
linked bios (multi-year, well-linked — the stringing's best case, so
rates below are optimistic for well-linked careers but the weak/full
and rare/common CONTRASTS are the signal).

| key | surname band | careers | testable | over-merged | rate |
|---|---|---|---|---|---|
| full | rare (<10) | 42,226 | 3,280 | 102 | 3.1% |
| full | medium (10-99) | 48,394 | 4,594 | 223 | 4.9% |
| full | common (>=100) | 29,666 | 3,010 | 333 | 11.1% |
| weak | rare (<10) | 17,829 | 563 | 10 | 1.8% |
| weak | medium (10-99) | 23,209 | 590 | 19 | 3.2% |
| weak | common (>=100) | 17,823 | 256 | 12 | 4.7% |

Overall: 179,147 careers, 12,293 testable, 699 over-merged (5.69% of testable).

## The dynastic-succession mechanism

Over-merges concentrate in long spans — local families (Barbados
Berkeleys/Brownes/Smiths) passing posts father-to-son under shared
initials, which no name key can separate:

- spans <= 40 years: 681 / 12,226 testable (5.6%)
- spans  > 40 years: 18 / 67 testable (26.9%)

Methods takeaway: over-merge risk is driven by surname FREQUENCY and
dynastic span, not by single-initial keys — the weak_key flag is the
wrong sensitivity axis on its own; filter on (common surname) and/or
(span > 40) instead.

## Sample over-merged careers

- BAHAMAS | malcolm, H. G. | 1905–1918 | 2 persons
- BARBADOS | smith, F. B | 1867–1917 | 2 persons
- BARBADOS | smith, W. C | 1905–1925 | 2 persons
- BARBADOS | berkeley, A. P | 1905–1927 | 2 persons
- BARBADOS | berkeley, W. H | 1867–1883 | 3 persons
- BARBADOS | berkeley, D.—M. J | 1894–1898 | 2 persons
- BARBADOS | browne, I. K | 1867–1890 | 2 persons
- BARBADOS | browne, P. W | 1905–1934 | 2 persons
- BARBADOS | howell, J. B | 1890–1940 | 2 persons
- BARBADOS | knight, J. G | 1894–1913 | 2 persons
- BARBADOS | king, G. B | 1878–1924 | 3 persons
- BRITISH GUIANA | pollard, W. B | 1867–1890 | 2 persons
