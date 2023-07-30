from attr import frozen, field
from attr.validators import in_

from src.digimon_card_game import CardColor, CardRarity
from src.extensions.attrs.validators import not_blank, within_range


@frozen(kw_only=True)
class TamerCard:
    name: str = field(validator=not_blank)
    color: CardColor = field(validator=in_(CardColor))
    identifier: str = field(validator=not_blank)
    rarity: CardRarity = field(validator=in_(CardRarity))
    cost: int = field(validator=within_range(0, 20))
