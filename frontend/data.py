"""Static lookups used by the UI (Latin binomial names, etc.).

Falls back gracefully — any class missing from the table simply renders
without its Latin name rather than erroring.
"""

LATIN_NAMES: dict[str, str] = {
    "ATLAS_MOTH": "Attacus atlas",
    "BLACK_HAIRSTREAK": "Satyrium pruni",
    "BLUE_MORPHO": "Morpho peleides",
    "GREY_HAIRSTREAK": "Strymon melinus",
    "LUNA_MOTH": "Actias luna",
    "MADAGASCAN_SUNSET_MOTH": "Chrysiridia rhipheus",
    "MONARCH": "Danaus plexippus",
    "PAINTED_LADY": "Vanessa cardui",
    "PEACOCK": "Aglais io",
    "PIPEVINE_SWALLOW": "Battus philenor",
    "RED_SPOTTED_PURPLE": "Limenitis arthemis",
    "VICEROY": "Limenitis archippus",
    "ZEBRA_LONG_WING": "Heliconius charithonia",
}


def latin_for(name: str) -> str | None:
    """Return the Latin binomial for a class label, if known."""
    key = name.upper().replace(" ", "_").replace("-", "_")
    return LATIN_NAMES.get(key)
