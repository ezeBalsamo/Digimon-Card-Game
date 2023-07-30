from src.digimon_card_game import Rarity, CardRarity
from tests.assertions.enum import assert_expected_enum_values


def test_01_rarity_instance_creation_and_accessing():
    common = Rarity(name='Common', identifier='C')
    assert common.name == 'Common'
    assert common.identifier == 'C'
    assert str(common) == common.name


def test_02_card_rarities():
    common = Rarity(name='Common', identifier='C')
    uncommon = Rarity(name='Uncommon', identifier='U')
    rare = Rarity(name='Rare', identifier='R')
    super_rare = Rarity(name='Super Rare', identifier='SR')
    secret_rare = Rarity(name='Secret Rare', identifier='SEC')
    promo = Rarity(name='Promo', identifier='P')

    assert_expected_enum_values(CardRarity, {common, uncommon, rare, super_rare, secret_rare, promo})
