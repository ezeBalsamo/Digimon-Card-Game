from src.digimon_card_game import TamerCard, CardColor, CardRarity
from tests.assertions import assert_attr_raises_not_blank, assert_attr_raises_not_within_range


def test_01_name_must_not_be_blank():
    assert_attr_raises_not_blank('name',
                                 lambda invalid_name: TamerCard(name=invalid_name, color=CardColor.RED,
                                                                identifier='ST1-12',
                                                                rarity=CardRarity.RARE, cost=2))


def test_02_identifier_must_not_be_blank():
    assert_attr_raises_not_blank('identifier',
                                 lambda invalid_identifier: TamerCard(name='Tai Kamiya', color=CardColor.RED,
                                                                      identifier=invalid_identifier,
                                                                      rarity=CardRarity.RARE,
                                                                      cost=2))


def test_03_cost_must_be_between_zero_and_twenty():
    assert_attr_raises_not_within_range('cost', 0, 20,
                                        lambda invalid_cost: TamerCard(name='Tai Kamiya', color=CardColor.RED,
                                                                       identifier='ST1-12',
                                                                       rarity=CardRarity.RARE,
                                                                       cost=invalid_cost))


def test_04_instance_creation_and_accessing():
    card = TamerCard(name='Tai Kamiya', color=CardColor.RED, identifier='ST1-12', rarity=CardRarity.RARE, cost=2)
    assert card.name == 'Tai Kamiya'
    assert card.color == CardColor.RED
    assert card.identifier == 'ST1-12'
    assert card.rarity == CardRarity.RARE
    assert card.cost == 2
