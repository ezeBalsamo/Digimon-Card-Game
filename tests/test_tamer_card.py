from typing import Any

from pytest import raises

from .assertions import assert_attr_raises_not_blank
from .assertions import assert_attr_raises_not_within_range
from .assertions import assert_frozenset_raises_not_minimum_length
from digimon_card_game.cards import TamerCard
from digimon_card_game.cards.information import CardColor
from digimon_card_game.cards.information import CardRarity

colors = frozenset([CardColor.RED])


def test_01_name_must_not_be_blank() -> None:
    assert_attr_raises_not_blank('name',
                                 lambda invalid_name: TamerCard(name=invalid_name, colors=colors,
                                                                identifier='ST1-12',
                                                                rarity=CardRarity.RARE, cost=2))


def test_02_identifier_must_not_be_blank() -> None:
    assert_attr_raises_not_blank('identifier',
                                 lambda invalid_identifier: TamerCard(name='Tai Kamiya', colors=colors,
                                                                      identifier=invalid_identifier,
                                                                      rarity=CardRarity.RARE,
                                                                      cost=2))


def test_03_cost_must_be_between_zero_and_twenty() -> None:
    assert_attr_raises_not_within_range('cost', 0, 20,
                                        lambda invalid_cost: TamerCard(name='Tai Kamiya', colors=colors,
                                                                       identifier='ST1-12',
                                                                       rarity=CardRarity.RARE,
                                                                       cost=invalid_cost))


def test_04_colors_must_be_elements_of_card_color_enum() -> None:
    invalid_colors: frozenset[Any] = frozenset([CardRarity.COMMON])
    with raises(ValueError) as exception_info:
        TamerCard(name='Tai Kamiya', colors=invalid_colors,
                  identifier='ST1-12',
                  rarity=CardRarity.RARE,
                  cost=1)
    assert str(exception_info.value) == 'colors: all elements must be a member of CardColor enum.'


def test_05_cannot_create_card_without_color() -> None:
    assert_frozenset_raises_not_minimum_length('colors', 1,
                                               lambda invalid_colors: TamerCard(name='Tai Kamiya',
                                                                                colors=invalid_colors,
                                                                                identifier='ST1-12',
                                                                                rarity=CardRarity.RARE,
                                                                                cost=1))


def test_06_instance_creation_and_accessing() -> None:
    card = TamerCard(name='Tai Kamiya', colors=colors, identifier='ST1-12', rarity=CardRarity.RARE, cost=2)

    assert card.name == 'Tai Kamiya'
    assert card.colors == colors
    assert card.identifier == 'ST1-12'
    assert card.rarity == CardRarity.RARE
    assert card.cost == 2
