from src.digimon_card_game import Deck
from pytest import raises


def test_01_cannot_create_deck_without_cards():
    invalid_cards = []
    minimum_length = 1
    with raises(ValueError) as exception_info:
        Deck(cards=invalid_cards)
    assert str(exception_info.value) == f"Length of 'cards' must be => {minimum_length}: {len(invalid_cards)}"
