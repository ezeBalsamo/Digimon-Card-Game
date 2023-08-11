from digimon_card_game.cards.information import CardColor, CardRarity
from digimon_card_game.cards import OptionCard
from .assertions import assert_attr_raises_not_blank, assert_attr_raises_not_within_range


def test_01_name_must_not_be_blank():
    assert_attr_raises_not_blank('name',
                                 lambda invalid_name: OptionCard(name=invalid_name, color=CardColor.RED,
                                                                 identifier='ST1-13',
                                                                 rarity=CardRarity.COMMON, cost=1))


def test_02_identifier_must_not_be_blank():
    assert_attr_raises_not_blank('identifier',
                                 lambda invalid_identifier: OptionCard(name='Shadow Wing', color=CardColor.RED,
                                                                       identifier=invalid_identifier,
                                                                       rarity=CardRarity.COMMON,
                                                                       cost=1))


def test_03_cost_must_be_between_zero_and_twenty():
    assert_attr_raises_not_within_range('cost', 0, 20,
                                        lambda invalid_cost: OptionCard(name='Shadow Wing', color=CardColor.RED,
                                                                        identifier='ST1-13', rarity=CardRarity.COMMON,
                                                                        cost=invalid_cost))


def test_04_instance_creation_and_accessing():
    card = OptionCard(name='Shadow Wing', color=CardColor.RED, identifier='ST1-13', rarity=CardRarity.COMMON, cost=1)
    assert card.name == 'Shadow Wing'
    assert card.color == CardColor.RED
    assert card.identifier == 'ST1-13'
    assert card.rarity == CardRarity.COMMON
    assert card.cost == 1
