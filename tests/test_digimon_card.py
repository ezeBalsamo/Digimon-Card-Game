from typing import Any

from pytest import raises

from .assertions import assert_attr_raises_not_blank
from .assertions import assert_attr_raises_not_positive
from .assertions import assert_attr_raises_not_within_range
from .assertions import assert_frozenset_raises_not_minimum_length
from digimon_card_game.cards import DigimonCard
from digimon_card_game.cards.information import CardColor
from digimon_card_game.cards.information import CardRarity
from digimon_card_game.cards.information import DigimonAttribute
from digimon_card_game.cards.information import DigimonForm
from digimon_card_game.cards.information import DigimonType

colors = frozenset([CardColor.RED])
types = frozenset([DigimonType.BIRD])


def test_01_name_must_not_be_blank() -> None:
    assert_attr_raises_not_blank('name',
                                 lambda invalid_name: DigimonCard(name=invalid_name, colors=colors,
                                                                  identifier='ST1-02',
                                                                  rarity=CardRarity.COMMON, form=DigimonForm.ROOKIE,
                                                                  attribute=DigimonAttribute.VACCINE,
                                                                  types=types, cost=2, power=3000, level=3))


def test_02_identifier_must_not_be_blank() -> None:
    assert_attr_raises_not_blank('identifier',
                                 lambda invalid_identifier: DigimonCard(name='Biyomon', colors=colors,
                                                                        identifier=invalid_identifier,
                                                                        rarity=CardRarity.COMMON,
                                                                        form=DigimonForm.ROOKIE,
                                                                        attribute=DigimonAttribute.VACCINE,
                                                                        types=types, cost=2, power=3000,
                                                                        level=3))


def test_03_cost_must_be_between_zero_and_twenty() -> None:
    assert_attr_raises_not_within_range('cost', 0, 20,
                                        lambda invalid_cost: DigimonCard(name='Biyomon', colors=colors,
                                                                         identifier='ST1-02',
                                                                         rarity=CardRarity.COMMON,
                                                                         form=DigimonForm.ROOKIE,
                                                                         attribute=DigimonAttribute.VACCINE,
                                                                         types=types,
                                                                         cost=invalid_cost, power=3000,
                                                                         level=3))


def test_04_power_must_be_positive() -> None:
    assert_attr_raises_not_positive('power', lambda invalid_power: DigimonCard(name='Biyomon', colors=colors,
                                                                               identifier='ST1-02',
                                                                               rarity=CardRarity.COMMON,
                                                                               form=DigimonForm.ROOKIE,
                                                                               attribute=DigimonAttribute.VACCINE,
                                                                               types=types, cost=2,
                                                                               power=invalid_power, level=3))


def test_05_level_must_be_between_two_and_seven() -> None:
    assert_attr_raises_not_within_range('level', 2, 7,
                                        lambda invalid_level: DigimonCard(name='Biyomon', colors=colors,
                                                                          identifier='ST1-02',
                                                                          rarity=CardRarity.COMMON,
                                                                          form=DigimonForm.ROOKIE,
                                                                          attribute=DigimonAttribute.VACCINE,
                                                                          types=types, cost=2,
                                                                          power=3000, level=invalid_level))


def test_06_colors_must_be_elements_of_card_color_enum() -> None:
    invalid_colors: frozenset[Any] = frozenset([CardRarity.COMMON])
    with raises(ValueError) as exception_info:
        DigimonCard(name='Biyomon',
                    colors=invalid_colors,
                    identifier='ST1-02',
                    rarity=CardRarity.COMMON,
                    form=DigimonForm.ROOKIE,
                    attribute=
                    DigimonAttribute.VACCINE,
                    types=types,
                    cost=2,
                    power=3000, level=3)
    assert str(exception_info.value) == 'colors: all elements must be a member of CardColor enum.'


def test_07_cannot_create_card_without_color() -> None:
    assert_frozenset_raises_not_minimum_length('colors', 1,
                                               lambda invalid_colors: DigimonCard(name='Biyomon',
                                                                                  colors=invalid_colors,
                                                                                  identifier='ST1-02',
                                                                                  rarity=CardRarity.COMMON,
                                                                                  form=DigimonForm.ROOKIE,
                                                                                  attribute=
                                                                                  DigimonAttribute.VACCINE,
                                                                                  types=types,
                                                                                  cost=2,
                                                                                  power=3000, level=3))


def test_08_types_must_be_elements_of_digimon_type_enum() -> None:
    invalid_types: frozenset[Any] = frozenset([CardRarity.COMMON])
    with raises(ValueError) as exception_info:
        DigimonCard(name='Biyomon',
                    colors=colors,
                    identifier='ST1-02',
                    rarity=CardRarity.COMMON,
                    form=DigimonForm.ROOKIE,
                    attribute=
                    DigimonAttribute.VACCINE,
                    types=invalid_types,
                    cost=2,
                    power=3000, level=3)
    assert str(exception_info.value) == 'types: all elements must be a member of DigimonType enum.'


def test_09_cannot_create_card_without_types() -> None:
    assert_frozenset_raises_not_minimum_length('types', 1,
                                               lambda invalid_types: DigimonCard(name='Biyomon',
                                                                                 colors=colors,
                                                                                 identifier='ST1-02',
                                                                                 rarity=CardRarity.COMMON,
                                                                                 form=DigimonForm.ROOKIE,
                                                                                 attribute=
                                                                                 DigimonAttribute.VACCINE,
                                                                                 types=invalid_types,
                                                                                 cost=2,
                                                                                 power=3000, level=3))


def test_10_instance_creation_and_accessing() -> None:
    card = DigimonCard(name='Biyomon', colors=colors, identifier='ST1-02',
                       rarity=CardRarity.COMMON, form=DigimonForm.ROOKIE, attribute=DigimonAttribute.VACCINE,
                       types=types, cost=2, power=3000, level=3)
    assert card.name == 'Biyomon'
    assert card.colors == colors
    assert card.identifier == 'ST1-02'
    assert card.rarity == CardRarity.COMMON
    assert card.form == DigimonForm.ROOKIE
    assert card.attribute == DigimonAttribute.VACCINE
    assert card.types == types
    assert card.cost == 2
    assert card.power == 3000
    assert card.level == 3


def test_11_instance_creation_without_level() -> None:
    card_without_level = DigimonCard(name='Biyomon', colors=colors, identifier='ST1-02',
                                     rarity=CardRarity.COMMON, form=DigimonForm.ROOKIE,
                                     attribute=DigimonAttribute.VACCINE,
                                     types=types, cost=2, power=3000)
    assert card_without_level.level is None
