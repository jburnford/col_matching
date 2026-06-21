"""Lock in the colonial place canonicalisation used before Wikidata grounding."""
from col_match.kg.place_canon import canonicalize, is_institution, canon_key


def test_canon_key_strips_dots_apostrophes_case():
    assert canon_key("F.M.S.") == "fms"
    assert canon_key("N. Rhod.") == "n rhod"
    assert canon_key("S'pore") == "spore"
    assert canon_key("H.K.") == "hk"


def test_high_frequency_abbreviations_expand():
    cases = {
        "Nig.": "Nigeria", "Ken.": "Kenya", "F.M.S.": "Federated Malay States",
        "Tang.": "Tanganyika", "H.K.": "Hong Kong", "N. Rhod.": "Northern Rhodesia",
        "Uga.": "Uganda", "G.C.": "Gold Coast", "S'pore": "Singapore",
        "T.T.": "Tanganyika", "E.A.P.": "East Africa Protectorate",
        "N.S.W.": "New South Wales", "S. Leone": "Sierra Leone",
        "Maur.": "Mauritius", "Cyp.": "Cyprus", "O.R.C.": "Orange River Colony",
    }
    for printed, want in cases.items():
        assert canonicalize(printed) == want, f"{printed!r} -> {canonicalize(printed)!r}"


def test_surface_variants_collapse_to_one_canonical():
    for v in ("B. Guiana", "Br. Guiana", "British Guiana", "B.G.", "Guiana"):
        assert canonicalize(v) == "British Guiana"
    for v in ("G.C.", "G. Coast", "Gold Coast"):
        assert canonicalize(v) == "Gold Coast"


def test_compound_place_keeps_both_parts():
    assert canonicalize("Penang, S. Sttlmts.") == "Penang Straits Settlements"
    assert canonicalize("the Gambia") == "Gambia"


def test_unknown_place_passes_through():
    assert canonicalize("Ixopo, Natal") == "Ixopo Natal"
    assert canonicalize("Kumasi") == "Kumasi"


def test_institutions_are_flagged():
    for s in ("colonial office", "War Office", "public works department",
              "Ghana civil service", "Queen's college", "F.M.S. railways",
              "sup. court"):
        flag, _ = is_institution(s)
        assert flag, s


def test_real_places_not_flagged_as_institution():
    for s in ("Accra", "Lagos", "Galle kach.", "Singapore", "Nigeria"):
        flag, _ = is_institution(s)
        assert not flag, s


def test_ambiguous_initialisms_left_untouched():
    # S.A. / W.A. are genuinely ambiguous -> not guessed
    assert canonicalize("S.A.") == "S.A."
    assert canonicalize("W.A.") == "W.A."
