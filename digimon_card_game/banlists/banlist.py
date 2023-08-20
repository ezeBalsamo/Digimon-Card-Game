from typing import Any
from attr import frozen, field, Attribute
from ..cards import Card
from attrs.validators import min_len
from datetime import date
from ..decks import Deckset, Deck


def validate_non_negative_number_of_copies(_instance: Any, attribute: Attribute,
                                           number_of_copies_by_card: dict[Card, int]):
    if any(value < 0 for value in number_of_copies_by_card.values()):
        raise ValueError(f"{attribute.name} must not include negative values.")


@frozen(kw_only=True)
class Banlist:
    date: date
    number_of_copies_by_card: dict[Card, int] = field(validator=[min_len(1), validate_non_negative_number_of_copies])

    def is_card_restricted(self, card: Card) -> bool:
        return card in self.number_of_copies_by_card

    def allowed_number_of_copies_of(self, card: Card) -> int:
        return self.number_of_copies_by_card[card]

    def is_card_allowed(self, card: Card, number_of_copies: int) -> bool:
        return not self.is_card_restricted(card) or number_of_copies <= self.allowed_number_of_copies_of(card)
