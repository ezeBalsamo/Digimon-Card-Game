from . import DigiEggCard, OptionCard, DigimonCard
from .information import CardColor, CardRarity, DigimonType, DigimonForm, DigimonAttribute


def koromon():
    return DigiEggCard(name='Koromon', color=CardColor.RED, identifier='ST1-01', rarity=CardRarity.UNCOMMON,
                       type=DigimonType.LESSER, level=2)


def shadow_wing():
    return OptionCard(name='Shadow Wing', color=CardColor.RED, identifier='ST1-13', rarity=CardRarity.COMMON, cost=1)


def biyomon():
    return DigimonCard(name='Biyomon', color=CardColor.RED, identifier='ST1-02',
                       rarity=CardRarity.COMMON, form=DigimonForm.ROOKIE, attribute=DigimonAttribute.VACCINE,
                       type=DigimonType.BIRD, cost=2, power=3000, level=3)
