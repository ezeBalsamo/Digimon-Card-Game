from src.digimon_card_game import CardColor
from tests.assertions import assert_expected_enum_values


def test_01_colors():
    assert_expected_enum_values(CardColor, {'Red', 'Blue', 'Yellow', 'Green', 'Black', 'Purple', 'White'})
