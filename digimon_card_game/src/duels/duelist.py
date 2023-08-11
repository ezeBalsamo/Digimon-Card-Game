from attr import frozen, field
from digimon_card_game.src.decks import Deckset
from digimon_card_game.src.extensions.attrs.validators import not_blank


@frozen(kw_only=True)
class Duelist:
    name: str = field(validator=not_blank)
    deckset: Deckset
