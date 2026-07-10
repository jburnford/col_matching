# Applied class-C links (career -> bio person)

- 'same' verdicts scored: 13,123
- applied: 9,296 pairs / 9,296 careers (tier1 6,358, tier2 2,938); corroboration {'llm_only': 2938, 'hard': 846, 'place': 5416, 'possim': 96}
- held for review: 3,827 (ambiguous careers: 160)

## Verification basis

34 pairs read closely across strata (July 2026). Every false positive
failed the exact-initials test; every policy-passing pair was correct
(0 observed FPs in the applied strata). LLM confidence is uniform
(90-95) and was NOT used; corroboration is recomputed deterministically.

## Link-rate lift (roster careers with a bio identity)

- before: 20,482 / 171,180 careers (12.0%)
- after:  29,778 / 171,180 (17.4%)

Links are an OVERLAY (career_person_links.jsonl) joining careers.jsonl
on career_id; careers.jsonl itself is untouched (it stays the product
of the within-volume linker).
