# Applied class-C links (career -> bio person)

- 'same' verdicts scored: 13,737
- applied: 9,840 pairs / 9,840 careers (tier1 6,725, tier2 3,115); corroboration {'hard': 886, 'llm_only': 3115, 'place': 5743, 'possim': 96}
- held for review: 3,897 (ambiguous careers: 144)

## Verification basis

34 pairs read closely across strata (July 2026). Every false positive
failed the exact-initials test; every policy-passing pair was correct
(0 observed FPs in the applied strata). LLM confidence is uniform
(90-95) and was NOT used; corroboration is recomputed deterministically.

## Link-rate lift (roster careers with a bio identity)

- before: 23,152 / 179,148 careers (12.9%)
- after:  32,992 / 179,148 (18.4%)

Links are an OVERLAY (career_person_links.jsonl) joining careers.jsonl
on career_id; careers.jsonl itself is untouched (it stays the product
of the within-volume linker).
