from .assertions import assert_expected_enum_values
from digimon_card_game.cards.information import DigimonAttribute


def test_01_digimon_attributes() -> None:
    assert_expected_enum_values(
        DigimonAttribute, {"Data", "Free", "Unknown", "Vaccine", "Variable", "Virus"}
    )
