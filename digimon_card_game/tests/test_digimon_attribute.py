from digimon_card_game.src.cards.information import DigimonAttribute
from digimon_card_game.tests.assertions.enum import assert_expected_enum_values


def test_01_digimon_attributes():
    assert_expected_enum_values(DigimonAttribute, {'Data', 'Free', 'Unknown', 'Vaccine', 'Variable', 'Virus'})
