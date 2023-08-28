from digimon_card_game.cards.information import CardColor

from .assertions import assert_expected_enum_values


def test_01_colors() -> None:
    assert_expected_enum_values(
        CardColor, {"Red", "Blue", "Yellow", "Green", "Black", "Purple", "White"}
    )
