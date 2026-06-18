"""Pydantic models for the services-section pipeline.

The pipeline stages hand these to each other as JSONL:
RawEntry (segment) -> EntryVersion (dedup) -> ParsedEntry (rules/LLM parse)
-> Biography (compile) -> StintMatch (match).
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class RawEntry(BaseModel):
    """One biographical entry as printed in one edition."""

    entry_id: str            # e.g. "col1930-L62112"
    volume: str              # directory name
    edition_year: int
    era: str                 # early | mid | late
    line_start: int          # 1-based line numbers in olmocr_results.md
    line_end: int
    raw_text: str            # whitespace-joined entry text
    # 1939 double-print: the other copy of this entry, kept for the
    # consistency check; None everywhere else.
    twin_entry_id: str | None = None
    twin_text: str | None = None


class EntryVersion(BaseModel):
    """One distinct text version of one person's entry, attested by >=1
    editions whose printed text is the same modulo OCR drift / appended
    clauses. The unit of parsing."""

    version_id: str          # e.g. "col1930-L62112.v" (lead entry id)
    surname_key: str         # normalized blocking key
    canonical_text: str      # longest attestation, consensus-corrected
    era: str                 # era of the lead attestation
    edition_year: int        # edition of the canonical attestation
    entry_ids: list[str]     # all attesting RawEntry ids
    attesting_editions: list[int]


class Honour(BaseModel):
    award: str               # "K.C.M.G."
    year: int | None = None  # award year when printed, e.g. (1922)


class CareerEvent(BaseModel):
    position: str | None = None   # as printed (abbreviations kept)
    place: str | None = None      # colony/territory as printed
    year_start: int | None = None
    year_end: int | None = None
    text_span: str                # verbatim clause this event came from
    # place carried over from the previous clause rather than printed in this
    # one — weaker evidence for matching
    place_inherited: bool = False


class Terminal(BaseModel):
    kind: str                # retired | resigned | died | pensioned | other
    year: int | None = None
    text_span: str


class ParsedEntry(BaseModel):
    """Structured parse of one EntryVersion. Both parser tiers emit this and
    both must pass the same validation gates (validate.py)."""

    version_id: str
    surname: str
    given_names: str | None = None
    title_rank: str | None = None    # "Brig.-Gen. Sir"
    birth_year: int | None = None
    honours: list[Honour] = Field(default_factory=list)
    education: str | None = None     # "ed. Tonbridge and St. John's Coll., Oxford"
    events: list[CareerEvent] = Field(default_factory=list)
    terminal: Terminal | None = None
    notes: list[str] = Field(default_factory=list)  # whitelisted undated clauses
    parser: str = "rules"            # rules | flash | pro
    flags: list[str] = Field(default_factory=list)  # validation warnings


class ProvenancedYear(BaseModel):
    value: int
    editions: list[int]


class BioEvent(BaseModel):
    position: str | None = None
    place: str | None = None
    year_start: int | None = None
    year_end: int | None = None
    editions: list[int] = Field(default_factory=list)
    place_inherited: bool = False
    # place recovered for an otherwise place-less clause by cross-fragment
    # inference (infer_colony.py) — the colony was named nowhere in this entry
    # but the same person's staff-list rows pin it. Treated as printed-quality
    # for matching (not penalized like place_inherited); provenance records the
    # record(s) it was inferred from for audit.
    place_recovered: bool = False
    recovered_provenance: str | None = None


class Biography(BaseModel):
    """One person, compiled from all their entry versions, with per-fact
    edition provenance."""

    bio_id: str
    surname: str
    given_names: str | None = None
    birth_year: ProvenancedYear | None = None
    version_ids: list[str] = Field(default_factory=list)
    editions: list[int] = Field(default_factory=list)
    honours: list[Honour] = Field(default_factory=list)
    events: list[BioEvent] = Field(default_factory=list)
    terminal: Terminal | None = None
    flags: list[str] = Field(default_factory=list)


class Agreement(BaseModel):
    """One independent point of alignment between a biography and a stint."""

    kind: str                # colony_year | colony_year_position
    bio_event_index: int
    record_year: int
    detail: str


class StintMatch(BaseModel):
    bio_id: str
    official_id: str         # COL_Official.id
    n_agreements: int
    agreements: list[Agreement]
    # surname matched only via OCR-tolerant edit distance; such matches are
    # categorically weaker and never displace an exact-surname match
    fuzzy_surname: bool = False


class DimensionCheck(BaseModel):
    """One evidence dimension evaluated for a candidate pair — recorded
    whether it passed or failed, with the why, so a dossier can show an
    adjudicator exactly what the deterministic pass saw."""

    name: str                # surname_gate | initials | age_gate | colony
    #                        | tenure_overlap | position_sim | honour
    #                        | edition_cooccurrence | place_inherited
    passed: bool
    detail: str = ""


class StintCandidate(BaseModel):
    """One (biography, stint) pair that survives the HARD gates only
    (surname block, initials compatibility, age sanity). Everything phase 1
    used as an evidence bar is an annotation here, not a filter — this is the
    unit the dossier adjudicator weighs."""

    bio_id: str
    official_id: str
    surname_gate: str        # "exact" | "fuzzy:1" | "fuzzy:2"
    single_initial: bool     # <=1 given-name initial: the "J. Lewis" trap
    checks: list[DimensionCheck] = Field(default_factory=list)
    cooc_years: list[int] = Field(default_factory=list)
    best_position_score: float = 0
    honour_overlap: list[str] = Field(default_factory=list)
    # (bio_event_index, tenure_start, tenure_end) for colony-agreeing events
    # overlapping the stint's years
    tenure_overlaps: list[tuple[int, int, int]] = Field(default_factory=list)
    phase1_strength: float | None = None
    phase1_passed_bar: bool = False
    # passed phase 1's evidence bar but was dropped by its ambiguity guard —
    # an already-identified contest
    phase1_dropped_ambiguous: bool = False
    competing_bio_ids: list[str] = Field(default_factory=list)
    same_surname_officials: int = 0   # surname-frequency prior (graph side)
    same_surname_bios: int = 0        # surname-frequency prior (bio side)


class CitedEvidence(BaseModel):
    stint_id: str
    year: int | None = None
    fact: str                # must appear verbatim-ish in the dossier


class VerdictPerson(BaseModel):
    """One person in the adjudicator's partition of a case."""

    bio_id: str
    stint_ids: list[str] = Field(default_factory=list)
    confidence: str          # certain | probable | uncertain
    # the strongest case that this assignment is WRONG — mandatory, written
    # before concluding; perfunctory text is a red flag
    arguments_against: str
    evidence_cited: list[CitedEvidence] = Field(default_factory=list)
    would_overturn: str = ""  # what new evidence would reverse this verdict


class UnassignedStint(BaseModel):
    stint_id: str
    reason: str


class Verdict(BaseModel):
    """Adjudicator output for one case: a partition of the case's stints
    among its biographies (or to nobody). The model never gets the last
    word — deterministic guards in adjudicate.py run after this."""

    case_id: str
    persons: list[VerdictPerson] = Field(default_factory=list)
    unassigned_stints: list[UnassignedStint] = Field(default_factory=list)
    # bios the adjudicator believes are the SAME person (e.g. one entry
    # re-compiled under two ids after an OCR birth-year flip). Never acted on
    # automatically — routed to the merge-review queue.
    duplicate_bio_groups: list[list[str]] = Field(default_factory=list)
    notes: str = ""


class Case(BaseModel):
    """One adjudication unit: a connected component of the bipartite
    bio↔candidate-stint graph. Partition framing — every bio competing for
    any stint in the case is weighed jointly, never edge-by-edge."""

    case_id: str             # "case_<min bio_id>" (a bio is in one component)
    bio_ids: list[str]
    stint_ids: list[str]
    n_candidates: int
    # adjudicate | review_oversized (too contested to fit one dossier;
    # chunking would reintroduce independent-edge reasoning, so don't)
    route: str = "adjudicate"
    est_tokens: int = 0


class GapEvent(BaseModel):
    """A biography career posting (colony + position + tenure) for which the
    staff-list graph holds NO matching record — i.e. a record the upstream
    extraction missed (or never reached). The biography is the evidence the
    record should exist; recovery confirms it against the source OCR."""

    bio_id: str
    event_index: int
    surname: str
    given_names: str | None = None
    place: str | None = None            # printed place, as in the biography
    resolved_colony: str | None = None  # normalized graph-colony it maps to
    year_start: int
    year_end: int
    position: str | None = None
    # section_present  = graph has records for this colony-year, person absent
    #                    (a missed row);
    # section_absent   = graph has no records for this colony-year at all
    #                    (a whole missing section);
    # place_unresolved = the printed place did not resolve to any colony.
    gap_type: str
    source_file: str | None = None      # resolved staff-list OCR file, if any


class CareerObservation(BaseModel):
    """One dated position-holding observation in the assembled graph — a single
    person seen in a post, colony and year. The unit of the career timeline,
    for grounded biographies and record-only persons alike."""

    person_id: str
    year: int
    colony: str
    department: str | None = None
    position_raw: str | None = None
    position_norm: str | None = None
    salary_min: float | None = None
    salary_max: float | None = None
    military_rank: str | None = None
    honors: list[str] = Field(default_factory=list)
    # graph (a COL_PersonRecord) | recovered (a confirmed_in_ocr proposal)
    source: str = "graph"
    provenance: str | None = None       # stint id, or source_file:line
    grounding_score: float | None = None


class PersonNode(BaseModel):
    """A node on the person spine. kind=biography is biography-anchored (the
    cross-colony spine); kind=record_only is a provisional within-colony person
    from one ungrounded COL_Official stint (never stitched across colonies)."""

    person_id: str
    kind: str                            # biography | record_only
    surname: str | None = None
    given_names: str | None = None
    birth_year: int | None = None
    first_year: int | None = None
    last_year: int | None = None
    colonies: list[str] = Field(default_factory=list)
    n_observations: int = 0
    honours: list[str] = Field(default_factory=list)
    terminal_kind: str | None = None
    terminal_year: int | None = None
    editions: list[int] = Field(default_factory=list)
    grounded: bool = False               # biography linked to >=1 graph record
    same_person_group_id: str | None = None
    source: str = "graph"


class RecoveredRecord(BaseModel):
    """A staff-list row recovered from the source OCR because a biography
    predicted it and it is absent from the graph. Every field traces to a real
    OCR line — nothing is synthesized. A proposal for upstream ingestion, never
    a graph write."""

    colony: str
    year: int
    position_raw: str | None = None
    department_raw: str | None = None
    name_raw: str
    surname: str
    given_names: str | None = None
    honors: list[str] = Field(default_factory=list)
    # confirmed_in_ocr (surname + position both found) | surname_only
    # (surname found, position mismatch/garbled) | not_in_ocr (surname absent —
    # NO record emitted, logged for review only)
    confidence: str
    source_file: str
    source_line: int
    snippet: str
    predicted_by_bio_id: str
    bio_position: str | None = None
    gap_type: str
