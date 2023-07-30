from src.digimon_card_game import DigimonAttribute
from tests.assertions import assert_expected_enum_values


def test_01_digimon_attributes():
    assert_expected_enum_values(DigimonAttribute, {'Data', 'Free', 'Unknown', 'Vaccine', 'Variable', 'Virus'})
