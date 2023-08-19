from __future__ import annotations
from attr import frozen, field, Attribute
from ..extensions.attrs.validators import not_blank
from . import Deck


def validate_optional_decks(_instance: Deckset, attribute: Attribute[dict[str, Deck]],
                            optional_decks: dict[str, Deck]) -> None:
    lowercase_identifiers = [identifier.lower() for identifier in optional_decks]
    equivalent_identifiers = set(
        identifier for identifier in lowercase_identifiers if lowercase_identifiers.count(identifier) > 1)

    if equivalent_identifiers:
        raise ValueError(
            f"{attribute.name} must not include equivalent identifiers (lowercase): {', '.join(equivalent_identifiers)}"
        )


@frozen(kw_only=True)
class Deckset:
    name: str = field(validator=not_blank)
    main_deck: Deck
    optional_decks: dict[str, Deck] = field(factory=dict, validator=validate_optional_decks)

    def optional_deck_known_as(self, identifier: str) -> Deck:
        try:
            return self.optional_decks[identifier]
        except KeyError:
            raise ValueError(f'There is no optional deck identified by {identifier}.')

    def all_decks(self) -> list[Deck]:
        return [self.main_deck] + list(self.optional_decks.values())
