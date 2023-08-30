from digimon_card_game.cards.information import DigimonAttribute
from .assertions import assert_expected_enum_values


def test_01_digimon_attributes():
    assert_expected_enum_values(DigimonAttribute, {'Data', 'Free', 'Unknown', 'Vaccine', 'Variable', 'Virus'})
