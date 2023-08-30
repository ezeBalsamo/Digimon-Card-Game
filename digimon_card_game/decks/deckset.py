from typing import Any
from attr import frozen, field, Attribute
from ..extensions.attrs.validators import not_blank
from . import Deck


def validate_optional_decks(_instance: Any, attribute: Attribute, optional_decks: dict[str, Deck]):
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
    name: str = field(validator=not_blank)
    main_deck: Deck
    optional_decks: dict[str, Deck] = field(factory=dict, validator=validate_optional_decks)

    def optional_deck_known_as(self, identifier: str):
        try:
            return self.optional_decks[identifier]
        except KeyError:
            raise ValueError(f'There is no optional deck identified by {identifier}.')

    def all_decks(self) -> list[Deck]:
        return [self.main_deck] + list(self.optional_decks.values())
