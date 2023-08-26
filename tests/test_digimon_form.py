from digimon_card_game.cards.information import DigimonForm

from .assertions import assert_expected_enum_values


def test_01_digimon_forms() -> None:
    assert_expected_enum_values(
        DigimonForm, {"In-Training", "Rookie", "Champion", "Mega", "Ultimate", "Hybrid"}
    )
