from attr import frozen, field
from src.digimon_card_game import Card
from attr.validators import min_len


@frozen(kw_only=True)
class Deck:
    cards: list[Card] = field(validator=min_len(1))
