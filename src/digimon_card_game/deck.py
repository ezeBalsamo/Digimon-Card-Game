from attr import define, field
from src.digimon_card_game import Card
from attr.validators import min_len


@define(kw_only=True)
class Deck:
    cards: list[Card] = field(validator=min_len(1))

    def draw(self):
        if not self.cards:
            raise ValueError('There are no more cards in the deck.')
        return self.cards.pop(0)

    def draw_many(self, number_of_cards):
        if not self.cards:
            raise ValueError('There are no more cards in the deck.')
        number_of_remaining_cards = len(self.cards)
        if number_of_remaining_cards < number_of_cards:
            raise ValueError(
                f'You cannot draw {number_of_cards} cards. Number of remaining cards: {number_of_remaining_cards}.')
        drawn_cards = self.cards[:number_of_cards]
        del self.cards[:number_of_cards]
        return drawn_cards
