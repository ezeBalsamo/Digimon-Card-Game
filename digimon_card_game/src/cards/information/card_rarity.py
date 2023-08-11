from attr import frozen, field
from enum import Enum
from digimon_card_game.src.extensions.attrs.validators import not_blank


@frozen(kw_only=True)
class Rarity:
    name: str = field(validator=not_blank)
    identifier: str = field(validator=not_blank)

    def __str__(self):
        return self.name


class CardRarity(Enum):
    COMMON = Rarity(name='Common', identifier='C')
    UNCOMMON = Rarity(name='Uncommon', identifier='U')
    RARE = Rarity(name='Rare', identifier='R')
    SUPER_RARE = Rarity(name='Super Rare', identifier='SR')
    SECRET_RARE = Rarity(name='Secret Rare', identifier='SEC')
    PROMO = Rarity(name='Promo', identifier='P')
