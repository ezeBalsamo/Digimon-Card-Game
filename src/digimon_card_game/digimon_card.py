from typing import Optional
from attr import frozen, field
from attr.validators import in_, optional, gt
from src.digimon_card_game import CardColor, CardRarity, DigimonForm, DigimonAttribute, DigimonType
from src.validators import not_blank, within_range


@frozen(kw_only=True)
class DigimonCard:
    name: str = field(validator=not_blank)
    color: CardColor = field(validator=in_(CardColor))
    identifier: str = field(validator=not_blank)
    rarity: CardRarity = field(validator=in_(CardRarity))
    form: DigimonForm = field(validator=in_(DigimonForm))
    attribute: DigimonAttribute = field(validator=in_(DigimonAttribute))
    type: DigimonType = field(validator=in_(DigimonType))
    cost: int = field(validator=within_range(0, 20))
    power: int = field(validator=gt(0))
    level: Optional[int] = field(default=None, validator=optional(within_range(lower=2, upper=7)))
