from attr import frozen, field, Attribute

from src.digimon_card_game import Deck


def validate_optional_decks(_instance: Deck, attribute: Attribute, optional_decks: dict[str, Deck]):
    lowercase_identifiers = {}
    duplicate_identifiers = set()

    for identifier in optional_decks:
        lowercase_identifier = identifier.lower()
        if lowercase_identifier in lowercase_identifiers:
            duplicate_identifiers.add(lowercase_identifiers[lowercase_identifier])
        lowercase_identifiers[lowercase_identifier] = lowercase_identifier

    if duplicate_identifiers:
        raise ValueError(
            f"{attribute.name} must not include equivalent identifiers (lowercase): {', '.join(duplicate_identifiers)}")


@frozen(kw_only=True)
class Deckset:
    main_deck: Deck
    optional_decks: dict[str, Deck] = field(factory=dict, validator=validate_optional_decks)
