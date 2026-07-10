# Applied class-C links (career -> bio person)

- 'same' verdicts scored: 11,992
- applied: 8,418 pairs / 8,418 careers (tier1 5,647, tier2 2,771); corroboration {'hard': 766, 'llm_only': 2771, 'place': 4790, 'possim': 91}
- held for review: 3,574 (ambiguous careers: 124)

## Verification basis

34 pairs read closely across strata (July 2026). Every false positive
failed the exact-initials test; every policy-passing pair was correct
(0 observed FPs in the applied strata). LLM confidence is uniform
(90-95) and was NOT used; corroboration is recomputed deterministically.

## Link-rate lift (roster careers with a bio identity)

- before: 23,152 / 179,148 careers (12.9%)
- after:  31,570 / 179,148 (17.6%)

Links are an OVERLAY (career_person_links.jsonl) joining careers.jsonl
on career_id; careers.jsonl itself is untouched (it stays the product
of the within-volume linker).
