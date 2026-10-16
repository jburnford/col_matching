#!/usr/bin/env python3
"""Prepare frequency-aware place review and an auditable image-review handoff.

No low-frequency record is deleted or approved. Short excerpts are INTERNAL
review evidence and may quote personal names; public WHG exports stay separate.
"""
import argparse
import collections
import csv
import difflib
import hashlib
import json
from pathlib import Path
import re

from build_whg_gazetteer import ROOT, contains, digest, norm, rows, write_json


def frequency_band(count):
    if count == 0:
        return "0"
    if count == 1:
        return "1"
    for upper in (5, 20, 100):
        if count <= upper:
            return "2-5" if upper == 5 else "6-20" if upper == 20 else "21-100"
    return ">100"


def source_path(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("Source locator escapes repository")
    return path


def clause_context(raw, start, end):
    if not 0 <= start < end <= len(raw):
        raise ValueError("Invalid source character offsets")
    left, right = raw.rfind(";", 0, start) + 1, raw.find(";", end)
    if right < 0:
        right = len(raw)
    # Bounded excerpts: do not copy an entire biography if punctuation is absent.
    left, right = max(left, start - 180), min(right, end + 180)
    return raw[left:right].strip()


def risk_signals(place, aliases_to_qids):
    variants = place["candidate_variants"]
    labels = place["grounded_labels"]
    signals = []
    if any(len(aliases_to_qids[norm(v)]) > 1 for v in variants):
        signals.append("name_maps_to_multiple_identities")
    if any(0 < len(norm(v).replace(" ", "")) <= 4 for v in variants):
        signals.append("short_name")
    if variants and labels:
        # Similarity flags retrieval work, not invalidity: historical names often differ.
        similarity = max(difflib.SequenceMatcher(None, norm(v), norm(label)).ratio()
                         for v in variants for label in labels)
        if similarity < 0.7:
            signals.append("historical_name_or_ocr_difference")
    if place.get("proposed_fclass") == "P" and any(
            re.search(r"\b(district|province|division|parish|county)\b", v, re.I) for v in variants):
        signals.append("settlement_vs_administrative_area")
    if not place["direct_evidence_count"]:
        signals.append("no_explicit_source_place_year_pair")
    if place.get("temporal_screen_event_count"):
        signals.append("temporal_screen_candidate")
    if "iol" in place["corpora"]:
        signals.append("check_india_office_source_coverage")
    return signals


def tail_view(place):
    """Adapt a v2 places.jsonl record to the screening fields used here."""
    return {"candidate_variants": sorted(set(place.get("printed_toponyms", {})) | ({place["title"]} if place.get("title") else set())),
            "grounded_labels": [place["wikidata_label"]] if place.get("wikidata_label") else [],
            "proposed_fclass": (place.get("fclasses") or [""])[0],
            "direct_evidence_count": place.get("evidence_tiers", {}).get("same_clause", 0),
            "temporal_screen_event_count": 0, "corpora": place.get("corpora", [])}


def authority_bounds(entity):
    result = {}
    for prop, key in (("P571", "inception_years"), ("P576", "dissolution_years")):
        years = set()
        for statement in entity.get("claims", {}).get(prop, []):
            if statement.get("rank") == "deprecated":
                continue
            value = statement.get("mainsnak", {}).get("datavalue", {}).get("value", {})
            if isinstance(value, dict) and value.get("precision", 0) >= 9:
                match = re.match(r"\+(\d+)-", value.get("time", ""))
                if match:
                    years.add(int(match[1]))
        result[key] = sorted(years)
    return result


def temporal_questions(years, bounds):
    before = [y for y in years if bounds["inception_years"] and y < min(bounds["inception_years"])]
    after = [y for y in years if bounds["dissolution_years"] and y > max(bounds["dissolution_years"])]
    return {"before_candidate_entity_inception": sorted(before),
            "after_candidate_entity_dissolution": sorted(after)}


def ocr_location(root, provenance):
    stems = {"col": "ColonialOfficeList", "dol": "DominionsOfficeList", "cro": "CommRelOffList"}
    family, year = provenance.get("doc"), provenance.get("edition_year")
    if family not in stems or type(year) is not int:
        return None
    matches = sorted((root / "raw_ocr/json").glob(f"*{stems[family]}{year}.pdf/result.json"))
    return matches[0] if len(matches) == 1 else None


def image_availability(root, volume, page, image_sources):
    spec = image_sources.get("volumes", {}).get(volume, {})
    image = spec.get("page_images", {}).get(str(page))
    pdf = spec.get("pdf_path")
    for kind, supplied in (("page_image", image), ("pdf", pdf)):
        if supplied:
            path = Path(supplied)
            path = path if path.is_absolute() else root / path
            return {"status": "available" if path.is_file() else "configured_file_missing",
                    "kind": kind, "path": str(path), "pdf_page_index": page,
                    "bbox_coordinate_space": spec.get("bbox_coordinate_space")}
    return {"status": "source_image_missing", "volume": volume, "pdf_page_index": page}


def run(root, gazetteer, out, max_references=5, samples=3, image_config=None):
    if max_references < 1 or samples < 1:
        raise ValueError("Positive tail threshold and sample count required")
    root, gazetteer, out = root.resolve(), gazetteer.resolve(), out.resolve()
    manifest = json.loads((gazetteer / "manifest.json").read_text())
    # Refuse stale evidence instead of mixing file generations silently.
    for name in ("places.jsonl", "evidence.jsonl"):
        if digest(gazetteer / name) != manifest["outputs"][name]:
            raise ValueError(f"Gazetteer output hash mismatch: {name}")
    counts, years, aliases = collections.Counter(), collections.defaultdict(set), collections.defaultdict(set)
    inputs = [Path(__file__), root / "build_whg_gazetteer.py", gazetteer / "manifest.json"]
    for corpus in ("kg", "iol"):
        path = root / f"data/{corpus}/graph_stage3/career_events.jsonl"
        inputs.append(path)
        expected = manifest["inputs"].get(str(path.relative_to(root)))
        if digest(path) != expected:
            raise ValueError("Graph changed; rebuild the gazetteer first")
    raw_places = {p["id"]: p for _, p in rows(gazetteer / "places.jsonl")}
    places, bounds_by_id = {}, {}
    for pid, record in raw_places.items():
        places[pid] = {**tail_view(record), "title": record["title"]}
        counts[pid] = record["mentions"]
        years[pid] = {y for ys in record["years_by_tier"].values() for y in ys}
        bounds_by_id[pid] = {"inception_years": [record["authority_inception"]] if record.get("authority_inception") else [],
                             "dissolution_years": [record["authority_dissolved"]] if record.get("authority_dissolved") else []}
        for name in places[pid]["candidate_variants"]:
            aliases[norm(name)].add(pid)
    tail = {q: p for q, p in places.items() if 1 <= counts[q] <= max_references}
    requested = collections.defaultdict(lambda: collections.defaultdict(list))
    for _, evidence in rows(gazetteer / "evidence.jsonl"):
        loc = evidence.get("source")
        if evidence["place_id"] in tail and loc and "char_start" in loc:
            evidence["qid"] = evidence["place_id"]
            requested[loc["path"]][loc["line"]].append(evidence)
    image_sources = json.loads(image_config.read_text()) if image_config else {"volumes": {}}
    if image_config:
        inputs.append(image_config)
    stats = {q: {"passages": set(), "publication_years": set(), "context_signals": set(),
                 "cooccurring_years": set(), "examples": []} for q in tail}
    for relative, needed in sorted(requested.items()):
        path = source_path(root, relative)
        if digest(path) != manifest["inputs"].get(relative):
            raise ValueError(f"Source changed; rebuild gazetteer: {relative}")
        inputs.append(path)
        for line, bio in rows(path):
            for evidence in needed.get(line, []):
                qid, raw = evidence["qid"], bio.get("raw_text") or ""
                loc = evidence["source"]
                start, end = loc["char_start"], loc["char_end"]
                if norm(raw[start:end]) != norm(evidence["printed_name"]):
                    raise ValueError("Source offsets no longer match evidence")
                excerpt = clause_context(raw, start, end)
                signature = hashlib.sha256(norm(excerpt).encode()).hexdigest()
                record = stats[qid]
                duplicate = signature in record["passages"]
                record["passages"].add(signature)
                record["publication_years"].update(evidence.get("printed_in_editions") or [evidence["publication_year"]])
                clause_years = {int(y) for y in re.findall(r"\b(?:1[5-9]\d\d)\b", excerpt)}
                record["cooccurring_years"].update(clause_years)
                if re.search(r"\b(educated|education|school|college|university|schl|educ|ed)\b", excerpt, re.I):
                    record["context_signals"].add("education_or_institution_context")
                if re.search(r"\b(king|queen|sultan|emperor)\s+of\b", excerpt, re.I):
                    record["context_signals"].add("ruler_or_polity_context")
                if not duplicate and len(record["examples"]) < samples:
                    record["examples"].append({
                        "source": loc, "printed_name": evidence["printed_name"],
                        "publication_year": evidence["publication_year"],
                        "ocr_excerpt": excerpt, "excerpt_sha256": hashlib.sha256(excerpt.encode()).hexdigest(),
                        "source_sha256": manifest["inputs"][relative],
                        "cooccurring_years_unverified": sorted(clause_years),
                        "provenance": bio.get("provenance", []),
                    })
    out.mkdir(parents=True, exist_ok=True)
    packets, reviews, ocr_requests = [], [], collections.defaultdict(list)
    for qid, place in sorted(tail.items()):
        stat = stats[qid]
        bounds = bounds_by_id[qid]
        questions = temporal_questions(years[qid], bounds)
        signals = risk_signals(place, aliases) + sorted(stat["context_signals"])
        if any(questions.values()):
            signals.append("candidate_year_outside_authority_entity_dates")
        unsupported_years = sorted(years[qid] - stat["cooccurring_years"]) if stat["examples"] else []
        if unsupported_years:
            signals.append("candidate_year_without_retrieved_clause_support")
        if not stat["examples"]:
            signals.append("no_retrieved_source_example")
        # Rarity never supplies an exclusion or an adverse historical judgement.
        diagnostic = [s for s in signals if s not in {
            "no_explicit_source_place_year_pair", "check_india_office_source_coverage", "no_retrieved_source_example"}]
        priority = 10 * len(diagnostic) + (5 if counts[qid] == 1 else 1)
        record = {"qid": qid, "title": place["title"], "event_references": counts[qid],
                  "candidate_year_endpoints": sorted(years[qid]),
                  "source_name_occurrences": counts[qid],
                  "distinct_excerpt_signatures": len(stat["passages"]),
                  "source_publication_years": sorted(stat["publication_years"]),
                  "source_clause_cooccurring_years_unverified": sorted(stat["cooccurring_years"]),
                  "candidate_years_without_retrieved_clause_support": unsupported_years,
                  "authority_date_candidates": bounds, "temporal_questions": questions,
                  "signals": signals, "priority": priority, "decision": "retain_pending_verification",
                  "source_examples": stat["examples"]}
        reviews.append(record)
        for example in stat["examples"]:
            packet_id = hashlib.sha256((qid + json.dumps(example["source"], sort_keys=True)
                                        + example["source_sha256"]).encode()).hexdigest()[:24]
            packet = {"packet_id": packet_id, "qid": qid, "candidate_title": place["title"],
                      "candidate_variants": place["candidate_variants"], "signals": signals,
                      "source_evidence": example, "image_targets": [],
                      "review_state": "awaiting_image",
                      "instructions": [
                          "Transcribe the image independently before comparing with the OCR excerpt.",
                          "Report the printed name and dates without expanding unclear abbreviations.",
                          "Keep transcription confidence separate from geographic identity confidence.",
                          "A name/date co-occurrence is not proof of their relationship.",
                          "Record reviewer model/version and image SHA-256; abstain if unreadable.",
                          "Do not approve a geographic identity solely because the proposed QID is supplied."
                      ]}
            for provenance in example["provenance"]:
                path = ocr_location(root, provenance)
                target = {"source_provenance": provenance,
                          "ocr_path": str(path.relative_to(root)) if path else None,
                          "localization": "biography_block_candidate_not_verified_quote_location"}
                if path:
                    volume = path.parent.name
                    target["image"] = image_availability(root, volume, provenance.get("page"), image_sources)
                    ocr_requests[path].append((packet, target, example["printed_name"]))
                else:
                    target["image"] = {"status": "ocr_locator_unresolved"}
                packet["image_targets"].append(target)
            packets.append(packet)
    # Read one OCR volume at a time, preserving its original page/block order.
    for path, requests in sorted(ocr_requests.items()):
        inputs.append(path)
        artifact_sha = digest(path)
        pages = json.loads(path.read_text())
        for packet, target, printed in requests:
            prov = target["source_provenance"]
            target["ocr_sha256"] = artifact_sha
            try:
                block = pages[prov["page"]][prov["block"]]
                if list(block.get("bbox", [])) != list(prov.get("bbox", [])):
                    target["localization"] = "bbox_mismatch_needs_alignment"
                elif contains(block.get("text", ""), packet["source_evidence"]["ocr_excerpt"]):
                    target["localization"] = "excerpt_supported_in_original_ocr_block"
                elif contains(block.get("text", ""), printed):
                    target["localization"] = "name_supported_in_original_ocr_block"
                else:
                    target["localization"] = "name_not_found_in_original_ocr_block"
            except (IndexError, KeyError, TypeError):
                target["localization"] = "invalid_block_locator"
        del pages
    for packet in packets:
        targets = packet["image_targets"]
        exact = [t for t in targets if t["localization"] == "excerpt_supported_in_original_ocr_block"]
        named = [t for t in targets if t["localization"] == "name_supported_in_original_ocr_block"]
        matched = exact or named
        packet["block_alignment_counts"] = dict(collections.Counter(t["localization"] for t in targets))
        packet["source_provenance_entries"] = len(targets)
        # A biography can carry a broad block-provenance list. Preserve its hash
        # and source locator without asking a reviewer to inspect unrelated pages.
        full_provenance = packet["source_evidence"]["provenance"]
        packet["source_evidence"]["provenance_sha256"] = hashlib.sha256(
            json.dumps(full_provenance, sort_keys=True).encode()).hexdigest()
        packet["image_targets"] = matched if matched else targets[:3]
        packet["source_evidence"]["provenance"] = [t["source_provenance"] for t in packet["image_targets"]]
        packet["quote_location_verified"] = False
        if any(t["image"]["status"] == "available" for t in packet["image_targets"]):
            packet["review_state"] = "image_available_not_reviewed"
    reviews.sort(key=lambda r: (-r["priority"], r["qid"]))
    with (out / "tail-review.tsv").open("w", newline="", encoding="utf-8") as handle:
        fields = ["qid", "title", "event_references", "source_name_occurrences", "distinct_excerpt_signatures", "priority", "signals", "decision"]
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for record in reviews:
            writer.writerow({k: ";".join(record[k]) if k == "signals" else record[k] for k in fields})
    for name, records in (("tail-details.jsonl", reviews), ("image-review-packets.jsonl", packets)):
        with (out / name).open("w", encoding="utf-8") as handle:
            for record in records:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    summary = {
        "candidate_places": len(places), "tail_max_event_references": max_references,
        "tail_places": len(tail), "tail_event_references": sum(counts[q] for q in tail),
        "frequency_distribution": dict(collections.Counter(frequency_band(counts[q]) for q in places)),
        "places_with_source_examples": sum(bool(r["source_examples"]) for r in reviews),
        "image_packets": len(packets), "image_states": dict(collections.Counter(p["review_state"] for p in packets)),
        "packets_with_name_aligned_ocr_block": sum(
            bool(p["block_alignment_counts"].get("name_supported_in_original_ocr_block")
                 or p["block_alignment_counts"].get("excerpt_supported_in_original_ocr_block")) for p in packets),
        "packets_with_excerpt_aligned_ocr_block": sum(
            bool(p["block_alignment_counts"].get("excerpt_supported_in_original_ocr_block")) for p in packets),
        "signals": dict(collections.Counter(s for r in reviews for s in r["signals"])),
        "retained_tail_places": len(tail), "automatically_excluded": 0, "automatically_approved": 0,
        "limits": ["No page image was transcribed by this preparation step.",
                   "Excerpt signatures measure textual repetition, not independent historical witnesses.",
                   "OCR text and page/block alignment are not visual verification.",
                   "Authority inception/dissolution mismatches are questions, not proven errors.",
                   "Review packets are internal evidence; excerpts may contain personal names."]}
    write_json(out / "summary.json", summary)
    write_json(out / "manifest.json", {"inputs": {str(p): digest(p) for p in sorted(set(inputs))},
                                        "max_references": max_references, "samples": samples,
                                        "outputs": {p.name: digest(p) for p in sorted(out.iterdir())
                                                    if p.is_file() and p.name != "manifest.json"}})
    print(json.dumps(summary, indent=2))
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--gazetteer", type=Path, default=ROOT / "out/whg")
    parser.add_argument("--out", type=Path, default=ROOT / "out/whg-tail")
    parser.add_argument("--max-event-references", type=int, default=5)
    parser.add_argument("--samples-per-place", type=int, default=3)
    parser.add_argument("--image-sources", type=Path)
    args = parser.parse_args()
    run(args.root, args.gazetteer, args.out, args.max_event_references, args.samples_per_place, args.image_sources)


if __name__ == "__main__":
    main()
