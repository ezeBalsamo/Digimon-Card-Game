from attr import frozen
from enum import Enum


@frozen(kw_only=True)
class Rarity:
    name: str
    identifier: str

    def __str__(self):
        return self.name


class CardRarity(Enum):
    COMMON = Rarity(name='Common', identifier='C')
    UNCOMMON = Rarity(name='Uncommon', identifier='U')
    RARE = Rarity(name='Rare', identifier='R')
    SUPER_RARE = Rarity(name='Super Rare', identifier='SR')
    SECRET_RARE = Rarity(name='Secret Rare', identifier='SEC')
    PROMO = Rarity(name='Promo', identifier='P')
