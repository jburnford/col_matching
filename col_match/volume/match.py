"""Within-volume bio ↔ roster linking.

Both endpoints come from the SAME edition, so the match is far simpler than the
old cross-edition career-chain matcher: the edition year pins tenure (no
co-occurrence voting needed — a roster record IS that year), and a person is
listed under their current post. A link needs:

  * surname agreement (exact, or OCR-tolerant edit distance for fuzzy),
  * initials-compatible given names,
  * colony agreement — some bio career clause's place resolves (via the
    gazetteer) to the record's colony, and
  * a corroborator — position similarity, an honour overlap, or a distinctive
    multi-token forename match.

0-FP discipline carried over from the old matcher: exact surname outranks fuzzy;
a single-initial-only name is weak; same-colony name-ties resolve to no-link
unless one candidate is uniquely strongest.
"""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, field

from rapidfuzz import distance, fuzz

from ..services import gazetteer
from ..services.compile import _pos_norm
from ..services.match import _initials, _names_compatible, _norm
from .bios import VolumeBio
from .roster import VolumeRecord

POSITION_SIM = 60
AMBIGUITY_MARGIN = 20


def _colony_target_set(raw: str | None, data_dir: str) -> set[str]:
    """Normalized graph-colony targets for a roster header or bio place,
    splitting compound headers ('AUSTRALIA--VICTORIA', 'THE GOLD COAST')."""
    if not raw:
        return set()
    out: set[str] = set()
    cleaned = re.sub(r"^the\s+", "", raw.strip(), flags=re.I)
    parts = re.split(r"--|—|–|\s*-\s*-\s*", cleaned)
    for part in [cleaned] + parts:
        part = part.strip(" .,")
        if part:
            out |= gazetteer.colony_targets(part, data_dir)
    return out


@dataclass
class VolumeLink:
    bio_id: str
    record_id: str
    edition_year: int
    surname_match: str           # exact | fuzzy:N
    strength: str                # strong | medium | weak
    colony: str
    position_sim: float
    shared_honours: list[str]
    bio_event_index: int
    bio_surname: str
    bio_given: str | None
    rec_surname: str
    rec_given: str | None
    rec_position: str | None
    bio_prov: dict
    rec_prov: dict
    notes: str = ""

    def to_json(self) -> dict:
        return self.__dict__


def _surname_index(records: list[VolumeRecord]) -> tuple[dict[str, list[int]], list[str]]:
    by_surname: dict[str, list[int]] = defaultdict(list)
    for i, r in enumerate(records):
        # surname may carry a particle ("de Livera"); key on the final token
        key = _norm(r.surname.split()[-1]) if r.surname else ""
        if key:
            by_surname[key].append(i)
    return by_surname, list(by_surname)


def _best_position_sim(bio: VolumeBio, rec: VolumeRecord, ev_idx: int) -> float:
    rp = _pos_norm(rec.position)
    if not rp:
        return 0.0
    bp = _pos_norm(bio.events[ev_idx].get("position"))
    return fuzz.token_set_ratio(bp, rp) if bp else 0.0


def _evaluate(bio: VolumeBio, rec: VolumeRecord, data_dir: str,
              fuzzy_dist: int) -> VolumeLink | None:
    """Return a VolumeLink if (bio, rec) clear the gates, else None."""
    if not _names_compatible(bio.given_names, rec.given_names):
        return None
    rec_targets = _colony_target_set(rec.colony, data_dir)
    if not rec_targets:
        return None
    # find a bio career event whose place resolves to the record's colony
    best_ev = -1
    best_sim = -1.0
    for i, ev in enumerate(bio.events):
        if not ev.get("place"):
            continue
        if _colony_target_set(ev["place"], data_dir) & rec_targets:
            sim = _best_position_sim(bio, rec, i)
            if sim > best_sim:
                best_sim, best_ev = sim, i
    if best_ev < 0:
        return None

    shared = sorted({h.rstrip(".") for h in rec.honours}
                    & {h["award"].rstrip(".") for h in bio.honours})
    bio_inits = _initials(bio.given_names)
    rec_inits = _initials(rec.given_names)
    full_forename_match = bool(
        bio.given_names and rec.given_names
        and len(bio.given_names.split()) >= 1
        and bio.given_names.split()[0].lower() == (rec.given_names.split()[0].lower())
        and len(bio.given_names.split()[0]) > 1
    )
    single_initial = max(len(bio_inits), len(rec_inits)) <= 1

    # strength: corroboration beyond surname+colony
    if best_sim >= POSITION_SIM or shared or (full_forename_match and len(bio_inits) >= 2):
        strength = "strong"
    elif len(bio_inits) >= 2 and len(rec_inits) >= 2:
        strength = "medium"
    else:
        strength = "weak"

    if fuzzy_dist > 0 and strength != "strong":
        return None  # fuzzy surname demands strong corroboration
    if single_initial and strength != "strong":
        return None

    return VolumeLink(
        bio_id=bio.bio_id, record_id=rec.record_id, edition_year=bio.edition_year,
        surname_match="exact" if fuzzy_dist == 0 else f"fuzzy:{fuzzy_dist}",
        strength=strength, colony=rec.colony, position_sim=round(best_sim, 1),
        shared_honours=shared, bio_event_index=best_ev,
        bio_surname=bio.surname, bio_given=bio.given_names,
        rec_surname=rec.surname, rec_given=rec.given_names, rec_position=rec.position,
        bio_prov=bio.provenance[0] if bio.provenance else {}, rec_prov=rec.provenance,
    )


_STRENGTH_RANK = {"strong": 3, "medium": 2, "weak": 1}


def link_volume(
    bios: list[VolumeBio], records: list[VolumeRecord], data_dir: str
) -> tuple[list[VolumeLink], dict]:
    by_surname, surname_keys = _surname_index(records)
    links: list[VolumeLink] = []
    stats = {"bios_in": len(bios), "records_in": len(records),
             "bios_linked": 0, "links": 0, "ambiguous_dropped": 0,
             "by_strength": defaultdict(int), "by_surname_match": defaultdict(int)}

    for bio in bios:
        if not bio.events or not bio.surname:
            continue
        key = _norm(bio.surname.split()[-1])
        if not key:
            continue
        cand_idx: list[tuple[int, int]] = [(i, 0) for i in by_surname.get(key, [])]
        if not cand_idx and len(key) >= 5:  # OCR-tolerant fuzzy surname
            for k in surname_keys:
                if abs(len(k) - len(key)) <= 2:
                    d = distance.Levenshtein.distance(key, k, score_cutoff=2)
                    if d <= 2:
                        cand_idx += [(i, d) for i in by_surname[k]]

        bio_links: list[VolumeLink] = []
        for ri, fdist in cand_idx:
            link = _evaluate(bio, records[ri], data_dir, fdist)
            if link is not None:
                bio_links.append(link)
        if not bio_links:
            continue

        # ambiguity guard: per colony, keep the uniquely strongest candidate.
        kept: list[VolumeLink] = []
        per_colony: dict[frozenset, list[VolumeLink]] = defaultdict(list)
        for ln in bio_links:
            per_colony[frozenset(_colony_target_set(ln.colony, data_dir))].append(ln)
        for group in per_colony.values():
            group.sort(key=lambda l: (_STRENGTH_RANK[l.strength], l.position_sim), reverse=True)
            top = group[0]
            rivals = [g for g in group[1:]
                      if (g.rec_given or "") != (top.rec_given or "")
                      and _STRENGTH_RANK[g.strength] == _STRENGTH_RANK[top.strength]]
            if rivals:
                stats["ambiguous_dropped"] += 1
                continue
            kept.append(top)

        if kept:
            stats["bios_linked"] += 1
            for ln in kept:
                links.append(ln)
                stats["by_strength"][ln.strength] += 1
                stats["by_surname_match"][ln.surname_match.split(":")[0]] += 1

    stats["links"] = len(links)
    stats["by_strength"] = dict(stats["by_strength"])
    stats["by_surname_match"] = dict(stats["by_surname_match"])
    return links, stats
