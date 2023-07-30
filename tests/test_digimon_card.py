from src.digimon_card_game import DigimonCard, CardColor, CardRarity, DigimonForm, DigimonAttribute, DigimonType
from tests.assertions import assert_raises_not_blank, assert_raises_not_within_range, \
    assert_raises_not_positive


def test_01_name_must_not_be_blank():
    assert_raises_not_blank('name',
                            lambda invalid_name: DigimonCard(name=invalid_name, color=CardColor.RED,
                                                             identifier='ST1-02',
                                                             rarity=CardRarity.COMMON, form=DigimonForm.ROOKIE,
                                                             attribute=DigimonAttribute.VACCINE,
                                                             type=DigimonType.BIRD, cost=2, power=3000, level=3))


def test_02_identifier_must_not_be_blank():
    assert_raises_not_blank('identifier',
                            lambda invalid_identifier: DigimonCard(name='Biyomon', color=CardColor.RED,
                                                                   identifier=invalid_identifier,
                                                                   rarity=CardRarity.COMMON, form=DigimonForm.ROOKIE,
                                                                   attribute=DigimonAttribute.VACCINE,
                                                                   type=DigimonType.BIRD, cost=2, power=3000, level=3))


def test_03_cost_must_be_between_zero_and_twenty():
    assert_raises_not_within_range('cost', 0, 20, lambda invalid_cost: DigimonCard(name='Biyomon', color=CardColor.RED,
                                                                                   identifier='ST1-02',
                                                                                   rarity=CardRarity.COMMON,
                                                                                   form=DigimonForm.ROOKIE,
                                                                                   attribute=DigimonAttribute.VACCINE,
                                                                                   type=DigimonType.BIRD,
                                                                                   cost=invalid_cost, power=3000,
                                                                                   level=3))


def test_04_power_must_be_positive():
    assert_raises_not_positive('power', lambda invalid_power: DigimonCard(name='Biyomon', color=CardColor.RED,
                                                                          identifier='ST1-02',
                                                                          rarity=CardRarity.COMMON,
                                                                          form=DigimonForm.ROOKIE,
                                                                          attribute=DigimonAttribute.VACCINE,
                                                                          type=DigimonType.BIRD, cost=2,
                                                                          power=invalid_power, level=3))


def test_05_level_must_be_between_two_and_seven():
    assert_raises_not_within_range('level', 2, 7, lambda invalid_level: DigimonCard(name='Biyomon', color=CardColor.RED,
                                                                                    identifier='ST1-02',
                                                                                    rarity=CardRarity.COMMON,
                                                                                    form=DigimonForm.ROOKIE,
                                                                                    attribute=DigimonAttribute.VACCINE,
                                                                                    type=DigimonType.BIRD, cost=2,
                                                                                    power=3000, level=invalid_level))


def test_06_instance_creation_and_accessing():
    card = DigimonCard(name='Biyomon', color=CardColor.RED, identifier='ST1-02',
                       rarity=CardRarity.COMMON, form=DigimonForm.ROOKIE, attribute=DigimonAttribute.VACCINE,
                       type=DigimonType.BIRD, cost=2, power=3000, level=3)
    assert card.name == 'Biyomon'
    assert card.color == CardColor.RED
    assert card.identifier == 'ST1-02'
    assert card.rarity == CardRarity.COMMON
    assert card.form == DigimonForm.ROOKIE
    assert card.attribute == DigimonAttribute.VACCINE
    assert card.type == DigimonType.BIRD
    assert card.cost == 2
    assert card.power == 3000
    assert card.level == 3


def test_07_instance_creation_without_level():
    card_without_level = DigimonCard(name='Biyomon', color=CardColor.RED, identifier='ST1-02',
                                     rarity=CardRarity.COMMON, form=DigimonForm.ROOKIE,
                                     attribute=DigimonAttribute.VACCINE,
                                     type=DigimonType.BIRD, cost=2, power=3000)
    assert card_without_level.level is None
