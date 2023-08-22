from ..cards import DigiEggCard, OptionCard, DigimonCard
from ..cards.information import CardColor, CardRarity, DigimonType, DigimonForm, DigimonAttribute


def koromon() -> DigiEggCard:
    return DigiEggCard(name='Koromon', color=CardColor.RED, identifier='ST1-01', rarity=CardRarity.UNCOMMON,
                       type=DigimonType.LESSER, level=2)


def shadow_wing() -> OptionCard:
    return OptionCard(name='Shadow Wing', colors=frozenset([CardColor.RED]), identifier='ST1-13',
                      rarity=CardRarity.COMMON, cost=1)


def biyomon() -> DigimonCard:
    return DigimonCard(name='Biyomon', colors=frozenset([CardColor.RED]), identifier='ST1-02',
                       rarity=CardRarity.COMMON, form=DigimonForm.ROOKIE, attribute=DigimonAttribute.VACCINE,
                       type=DigimonType.BIRD, cost=2, power=3000, level=3)
