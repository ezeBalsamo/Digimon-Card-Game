from __future__ import annotations

from datetime import date as Date

from attr import Attribute
from attr import field
from attr import frozen
from attrs.validators import min_len

from ..cards import Card
from ..decks import Deck
from ..decks import Deckset


def validate_non_negative_number_of_copies(
    _instance: Banlist,
    attribute: Attribute[dict[Card, int]],
    number_of_copies_by_card: dict[Card, int],
) -> None:
    if any(value < 0 for value in number_of_copies_by_card.values()):
        raise ValueError(f"{attribute.name} must not include negative values.")


@frozen(kw_only=True)
class Banlist:
    date: Date
    number_of_copies_by_card: dict[Card, int] = field(
        validator=[min_len(1), validate_non_negative_number_of_copies]
    )

    def is_card_restricted(self, card: Card) -> bool:
        return card in self.number_of_copies_by_card

    def allowed_number_of_copies_of(self, card: Card) -> int:
        return self.number_of_copies_by_card[card]

    def is_card_allowed(self, card: Card, number_of_copies: int) -> bool:
        return not self.is_card_restricted(
            card
        ) or number_of_copies <= self.allowed_number_of_copies_of(card)

    def is_deck_allowed(self, deck: Deck) -> bool:
        return all(
            self.is_card_allowed(card, deck.cards.count(card)) for card in deck.cards
        )

    def is_deckset_allowed(self, deckset: Deckset) -> bool:
        return all(self.is_deck_allowed(deck) for deck in deckset.all_decks())
