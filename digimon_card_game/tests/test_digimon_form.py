from digimon_card_game.src.cards.information import DigimonForm
from digimon_card_game.tests.assertions.enum import assert_expected_enum_values


def test_01_digimon_forms():
    assert_expected_enum_values(DigimonForm, {'In-Training', 'Rookie', 'Champion', 'Mega', 'Ultimate'})
