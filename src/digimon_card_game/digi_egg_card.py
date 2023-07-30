from typing import Optional
from attr import frozen, field
from attr.validators import in_, optional
from src.digimon_card_game import CardColor, CardRarity, DigimonForm, DigimonType
from src.validators import not_blank, within_range


@frozen(kw_only=True)
class DigiEggCard:
    name: str = field(validator=not_blank)
    color: CardColor = field(validator=in_(CardColor))
    identifier: str = field(validator=not_blank)
    rarity: CardRarity = field(validator=in_(CardRarity))
    type: DigimonType = field(validator=in_(DigimonType))
    level: Optional[int] = field(default=None, validator=optional(within_range(lower=2, upper=7)))

    @property
    def form(self) -> DigimonForm:
        return DigimonForm.IN_TRAINING
