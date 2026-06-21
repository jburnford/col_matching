"""Lock in per-person context resolution of ambiguous place abbreviations."""
from col_match.kg.resolve_context import is_ambiguous, resolve


def test_is_ambiguous():
    for p in ("W. Prov.", "N. Prov.", "S. Provs.", "E. region", "S.A.", "W.A."):
        assert is_ambiguous(p), p
    for p in ("Ceylon", "Nigeria", "Western Province, Ceylon", "Accra"):
        assert not is_ambiguous(p), p


def test_directional_province_attaches_parent_country():
    q, _ = resolve("W. Prov.", ["Ceylon", "Colombo", "Ceylon"])
    assert q == "Western Province, Ceylon"
    q, _ = resolve("N. regn.", ["Nigeria", "Lagos"])
    assert q == "Northern Region, Nigeria"
    q, _ = resolve("S. Provs.", ["Southern Nigeria", "Lagos"])
    assert q == "Southern Provinces, Nigeria"  # regional Nigeria collapses to country


def test_directional_no_parent_stays_flagged():
    q, _ = resolve("W. Prov.", ["London", "Oxford"])
    assert q is None


def test_sa_resolves_by_region_cluster():
    q, _ = resolve("S.A.", ["Cape Colony", "Natal"])
    assert q == "South Africa"
    q, _ = resolve("S.A.", ["Adelaide", "New South Wales"])
    assert q == "South Australia"
    # conflicting / no signal -> flagged
    assert resolve("S.A.", ["Tanganyika", "Kenya"])[0] is None


def test_wa_resolves_by_region_cluster():
    q, _ = resolve("W.A.", ["Nigeria", "Gold Coast"])
    assert q == "British West Africa"
    q, _ = resolve("W.A.", ["Perth", "Western Australia"])
    assert q == "Western Australia"
    assert resolve("W.A.", ["Federated Malay States"])[0] is None
