from digimon_card_game.src.cards.information import CardColor
from digimon_card_game.tests.assertions.enum import assert_expected_enum_values


def test_01_colors():
    assert_expected_enum_values(CardColor, {'Red', 'Blue', 'Yellow', 'Green', 'Black', 'Purple', 'White'})
