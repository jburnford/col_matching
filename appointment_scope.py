"""Separate recorded visits from appointments in the atlas, preserving source facts.

Duration is not an exclusion: acting, temporary, visiting professional offices,
secondments and special-duty assignments remain eligible. These rules identify
explicit conference participation and travel, not every possible non-office event.
"""
import re
import json
from pathlib import Path

MEETING = re.compile(r'\b(?:conferences?|conf(?:ce|ec)?\.?|congress(?:es)?)\b', re.I)
PARTICIPANT = re.compile(r'\b(?:deleg(?:ate|ates|ation)?\.?|dels?\.?|rep(?:resent(?:ed|ative|atives|ation|ing))?\.?|attend\w*|member|presid\w*|presdt\.?|chair\w*|chmn\.?|deput(?:ation|ed|n))\b', re.I)
MOD = r'(?:(?:acting|temporary|assistant|joint|private|deputy|technical|tech|administrative|administration|departmental|british|br|indian|ind|ag|asst|jt|pte|chief|honorary|naval|law|special|social|loans|financial)\.?\s+)*'
OFFICE = r'(?:secretary|sec|adviser|advisor|advr|counsel|interpreter|translator|commissioner|umpire|organiser|organizer|director|surgeon|guardian|medical officer)\b'
WORK = re.compile(r'^(?:(?:appointed|served|employed)\s+(?:as\s+)?(?:an?\s+)?)?' + MOD + OFFICE +
                  r'|\bas\s+(?:an?\s+)?' + MOD + OFFICE +
                  r'|^(?:seconded|attached|on (?:special|spl\.?|specl\.?) duty with)\b', re.I)
VISIT = re.compile(r'^(?:(?:official|officially)\s+)?(?:visits?|visited|tours?|toured|lecture tours?)\b|^accompanied\b.*\b(?:visit|tour)\b', re.I)
STAFF = re.compile(r'\b(?:secretary|secretariat|adviser|advisor|advr\.?)\b|\bImperial War Cabinet\b', re.I)
# A travel verb can introduce a real assignment. Keep these mixed or incomplete
# descriptions until their source distinguishes the duty from the visit.
VISIT_ASSIGNMENT = re.compile(r'\b(?:missions?|service|duty|business|reports?|reported|rept|inquir\w*|survey|inspection|exploration|investig\w*|study|negotia\w*|advise|recommendations|purchase|assistant|director|treasurer|re-organ\w*|on behalf|as (?:\S+\s+){0,2}rep)\b', re.I)
ATTACHED_DELEGATION = re.compile(r'^(?:attd|att)\.?\s+(?:(?:Br|U\.K)\.?\s+)?del\b', re.I)


def classify_for_appointment_map(r):
    """Exclude explicit attendance/travel, retaining it in the person's event list."""
    pos = (r.get('position') or r.get('position_raw') or '').strip()
    # These fields are owned by this classifier and recomputed on every build.
    r.pop('appointment_map_excluded', None)
    r.pop('appointment_map_note', None)
    if WORK.search(pos) or STAFF.search(pos) or ATTACHED_DELEGATION.search(pos):
        return r
    reason = None
    if MEETING.search(pos) and PARTICIPANT.search(pos):
        reason = 'Conference participation; retained as a recorded event, not mapped as an appointment.'
    elif VISIT.search(pos) and not VISIT_ASSIGNMENT.search(pos):
        reason = 'Visit or tour; retained as a recorded event, not mapped as an appointment.'
    if reason:
        r['appointment_map_excluded'] = True
        r['appointment_map_note'] = reason
    return r


def write_audit():
    root = Path(__file__).resolve().parent
    out = root / 'research/appointment-map-2026-10-08'
    out.mkdir(exist_ok=True)
    rows, counts = [], {}
    for corpus in ('kg', 'iol'):
        excluded = acting = 0
        for line in (root / f'data/{corpus}/graph_stage3/career_events.jsonl').open():
            r = classify_for_appointment_map(json.loads(line))
            if r.get('appointment_map_excluded'):
                excluded += 1
                rows.append({k: r.get(k) for k in ('person_id', 'seq', 'year_start', 'position', 'place_raw', 'is_acting', 'appointment_map_note')} | {'corpus': corpus})
            elif r.get('is_acting'):
                acting += 1
        counts[corpus] = {'excluded_events': excluded, 'acting_events_retained': acting}
    (out / 'excluded-events.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
    (out / 'summary.json').write_text(json.dumps({'policy': 'Map substantive and temporary appointments. Preserve explicit conference participation and travel in written records without using them as map stops or route breaks. Retain temporary staff and special-duty assignments. Rules do not resolve every ambiguous event type.', 'counts': counts}, indent=2) + '\n')
