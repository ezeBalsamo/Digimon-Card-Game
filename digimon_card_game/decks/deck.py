from attr import field
from attr import frozen
from attr.validators import min_len

from ..assertions import assert_is_positive
from ..cards import Card


@frozen(kw_only=True)
class Deck:
    cards: list[Card] = field(validator=min_len(1))

    def draw(self) -> Card:
        self.assert_is_not_empty()
        return self.cards.pop(0)

    def draw_many(self, number_of_cards: int) -> list[Card]:
        self.assert_can_draw_many(number_of_cards)
        drawn_cards = self.cards[:number_of_cards]
        del self.cards[:number_of_cards]
        return drawn_cards

    def assert_can_draw_many(self, number_of_cards: int) -> None:
        self.assert_is_not_empty()
        assert_is_positive(
            number_of_cards, "The number of cards to draw must be positive."
        )
        number_of_remaining_cards = len(self.cards)
        if number_of_remaining_cards < number_of_cards:
            raise ValueError(
                f"You cannot draw {number_of_cards} cards. Number of remaining cards: {number_of_remaining_cards}."
            )

    def assert_is_not_empty(self) -> None:
        if self.is_empty():
            raise ValueError("There are no more cards.")

    def is_empty(self) -> bool:
        return not self.cards
